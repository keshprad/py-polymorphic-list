import React from 'react';
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';
import { Redirect } from '@docusaurus/router';

export default function Home() {
  const { siteConfig } = useDocusaurusContext();
  return <Redirect to="docs/intro/" />;
}
