# Monitoramento de Queimadas na Amazônia

Este projeto tem como objetivo monitorar as queimadas na Amazônia e apresentar informações diárias atualizadas sobre os focos de incêndio detectados. Abaixo, você pode visualizar as queimadas mais recentes, com detalhes sobre localização, satélite que realizou a detecção, e outros fatores relevantes.

## Estrutura dos Dados

Cada entrada na tabela representa um foco de incêndio com as seguintes informações:

- **ID:** Identificador único do foco de incêndio.
- **Latitude/Longitude:** Coordenadas geográficas do foco detectado. Para visualizar o local exato, insira estas coordenadas no Google Maps ou outro aplicativo de mapas.
- **Data/Hora GMT:** Data e hora da detecção em formato GMT (Greenwich Mean Time).
- **Satélite:** Satélite responsável pela detecção do foco de incêndio.
- **Município, Estado e País:** Localização administrativa do foco detectado.
- **Dias sem Chuva:** Número de dias consecutivos sem precipitação na região, o que pode indicar um aumento no risco de incêndio.
- **Precipitação:** Quantidade de chuva (em milímetros) registrada no local.
- **Risco de Fogo:** Índice que indica a probabilidade de ocorrência de incêndio, baseado em fatores como condições climáticas e quantidade de combustível disponível.
- **Bioma:** Bioma onde o foco foi identificado, como Amazônia, Cerrado, ou Mata Atlântica.
- **FRP (Fire Radiative Power):** Potência radiativa do fogo, que mede a intensidade do incêndio. Focos com FRP mais alto indicam incêndios mais intensos.

## Visualização Gráfica

Se você deseja visualizar de forma gráfica onde as queimadas estão ocorrendo, copie as coordenadas de latitude e longitude mais recentes e cole no Google Maps. Isso permite uma compreensão espacial mais clara da distribuição dos focos de incêndio. Alternativamente, você também pode usar a descrição de localização (Município, Estado e País) para identificar a região afetada.

## Informação Adicional

As queimadas na Amazônia não apenas afetam a biodiversidade local, mas também têm implicações globais, contribuindo para o aquecimento global e a emissão de gases de efeito estufa. O monitoramento contínuo é essencial para entender e mitigar os impactos desses incêndios, além de auxiliar na gestão de políticas ambientais e ações de preservação.

## Dados Diários - Página 135

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 059225bd-4851-3860-8b20-88e304de7d60 | -17.96114 | -57.58575 | 2025-10-05 05:16:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| bc58d3c5-7df7-3a8b-b3a4-c40be8eefb0d | -13.1342 | -50.87849 | 2025-10-05 05:16:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 1b17c8a8-03dd-3f67-9eab-fa4da79cafd7 | -15.97788 | -50.86266 | 2025-10-05 05:16:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d78d46f5-94b7-3907-93dc-11b2708692f0 | -12.59011 | -48.13571 | 2025-10-05 05:16:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c45a82f0-9d5e-3842-b3bb-af7c73a91759 | -13.46613 | -47.28733 | 2025-10-05 05:16:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6370344e-f4a2-3a20-8a59-9282529800a0 | -10.64958 | -58.75818 | 2025-10-05 05:16:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2e8f0ad0-4e6f-3f5a-8c63-546a8fa20d1c | -12.59925 | -48.13805 | 2025-10-05 05:16:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a74da75d-4771-3a69-b6f2-e8e8062155c7 | -13.37237 | -47.55293 | 2025-10-05 05:16:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| be26194d-4229-3326-8b7b-c748fe44742e | -17.95117 | -57.60492 | 2025-10-05 05:16:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.0 |
| 8bfe1018-3ce6-312f-bb22-810e82631484 | -13.27086 | -47.18433 | 2025-10-05 05:16:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 82ec9abb-1ec5-384e-92de-79722c68b2d7 | -18.25132 | -53.33825 | 2025-10-05 05:16:00 | NPP-375D | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 47fa538c-f4c4-349f-a3c6-db315e2152cf | -16.3655 | -51.47486 | 2025-10-05 05:16:00 | NPP-375D | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4beb1b25-ddbe-3fb4-96cd-50d30b5202d9 | -13.2299 | -47.82659 | 2025-10-05 05:16:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b7b1f671-cfc0-3d86-b669-953b470fe65f | -14.98108 | -49.99894 | 2025-10-05 05:16:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7bf797fd-1f8a-31a4-9fd8-e4e7092119d7 | -13.34099 | -48.06188 | 2025-10-05 05:16:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 385e29ae-5a59-3c29-82d0-a71d3daa96e1 | -13.33656 | -47.59327 | 2025-10-05 05:16:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 85c22a4b-3f19-38a0-b053-9f2a60e97c8d | -15.97712 | -50.91269 | 2025-10-05 05:16:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 8bcaad0a-40ea-3fde-8541-742de556309b | -11.82771 | -60.48334 | 2025-10-05 05:16:00 | NPP-375D | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c963b791-2918-3352-a4b1-7deabeb23d88 | -18.18504 | -53.35657 | 2025-10-05 05:16:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 6ef174f0-515c-3f30-a7bd-a43e800ee9bd | -13.35621 | -47.24436 | 2025-10-05 05:16:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 213dbcbe-9032-3c1f-be95-28ea5b94b260 | -15.23734 | -49.30733 | 2025-10-05 05:16:00 | NPP-375D | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d6332daf-ef90-3c29-90c5-4f946acdfdbc | -15.58889 | -52.51054 | 2025-10-05 05:16:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| ff55e71b-63fc-346a-9a00-b133ce03c377 | -13.30205 | -47.78882 | 2025-10-05 05:16:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| a5cfeb8e-e3d8-3d3a-9b2d-1676d4654649 | -15.39054 | -47.94758 | 2025-10-05 05:16:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9ff29551-368e-3bcc-ac07-a2d9ad369e21 | -14.91886 | -46.8535 | 2025-10-05 05:16:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| e867c737-6597-331c-9bb7-c7b58ee48402 | -15.23034 | -49.29979 | 2025-10-05 05:16:00 | NPP-375D | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7afb748d-285b-39fb-93ad-7ada1c839f2e | -14.92725 | -46.83689 | 2025-10-05 05:16:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| e68323e2-4617-31b0-be65-ecc68abdffc2 | -15.55574 | -46.96167 | 2025-10-05 05:16:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7a64ecce-37d8-3e22-88f9-0361d444d7a2 | -10.1871 | -63.62966 | 2025-10-05 05:16:00 | NPP-375D | BURITIS | RONDÔNIA | Brasil | 1100452 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b858896b-dbe6-3ffa-a2c6-585157835abb | -17.84642 | -57.63206 | 2025-10-05 05:16:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 283049d5-b624-3308-bfd7-4cf425318821 | -12.70175 | -45.85419 | 2025-10-05 05:16:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6662608a-1185-3a99-a72c-f011b3d81bd6 | -13.10439 | -47.94309 | 2025-10-05 05:16:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 437caf43-ec9b-36db-ba14-29f9d21ee3e4 | -16.1612 | -57.573 | 2025-10-05 05:16:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 34ee6c11-b25a-358d-9e20-30f91e87526e | -15.7441 | -46.27756 | 2025-10-05 05:16:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c097f3d1-3588-3ae2-9bef-fbe1a5e16234 | -17.84583 | -57.63618 | 2025-10-05 05:16:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 9b7d68ef-907e-3386-88a6-18ced35ac1a8 | -14.33855 | -52.9698 | 2025-10-05 05:16:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bb9b96dc-2af3-3949-91b5-ec82f69bb4bb | -10.83958 | -57.19115 | 2025-10-05 05:16:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 83085729-0d56-37e9-aef9-63fda3fa7e37 | -14.32764 | -47.70752 | 2025-10-05 05:16:00 | NPP-375D | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 002b064b-dabe-3d0e-8e93-8a80b1f3c800 | -10.10071 | -65.04161 | 2025-10-05 05:16:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 549dd166-7fa4-3cc0-8c36-6640e271a9a6 | -14.74015 | -54.62015 | 2025-10-05 05:16:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 68114880-e63c-33bf-80f0-02a5d7c53a04 | -15.60265 | -52.51244 | 2025-10-05 05:16:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 4cfc35c3-49f9-316a-8d05-56e2d29b3f2f | -18.15668 | -53.32622 | 2025-10-05 05:16:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 87ae235e-36f7-3023-99d9-9f53f33285e0 | -14.67525 | -48.3622 | 2025-10-05 05:16:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| d14f4d54-a527-3ee2-8de9-6e806748bf8d | -14.65868 | -48.3482 | 2025-10-05 05:16:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 33f6db02-bb87-30d3-84c9-dc4b84feef03 | -13.13812 | -47.96722 | 2025-10-05 05:16:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6b01e629-989f-3410-8936-964cc4911a05 | -14.82263 | -54.76912 | 2025-10-05 05:16:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 934c3f34-37bc-3f85-91ce-59f68ba6e34c | -13.25558 | -47.81725 | 2025-10-05 05:16:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| d242e8c0-e4ae-3c15-a718-6b1b15f2f1a3 | -12.90838 | -47.31615 | 2025-10-05 05:16:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| b436333a-3087-30a8-bee2-3bfe80df4e6f | -15.30976 | -56.93658 | 2025-10-05 05:16:00 | NPP-375D | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c5cf2cd4-d69d-32c9-8dfb-4cce763ecaf6 | -10.64625 | -58.75763 | 2025-10-05 05:16:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6db18522-abbe-3121-bfa2-3371e32774bf | -11.86921 | -56.88056 | 2025-10-05 05:16:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 9.8 |
| bcee71bb-53d7-39d5-9301-6c39954f36fb | -17.89618 | -57.63796 | 2025-10-05 05:16:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 6d31fdac-cb18-3d1d-a66a-bc1c930d4e69 | -10.83608 | -57.18356 | 2025-10-05 05:16:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 12dd6404-03c9-3399-8a1e-ce8ddb982484 | -17.895 | -57.64321 | 2025-10-05 05:16:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 7347090d-152a-3d5f-9865-2c1b0d1f3768 | -12.98409 | -51.01414 | 2025-10-05 05:16:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ee49b097-c0b4-38a3-a281-6ff16ebcfac7 | -13.2538 | -48.47639 | 2025-10-05 05:16:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| d3f1b7ab-a84c-3693-b4ed-6d5fdd8a1626 | -17.88096 | -57.64107 | 2025-10-05 05:16:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.1 |
| c5150945-13f8-305f-a205-6f667b5294e2 | -16.94655 | -52.67957 | 2025-10-05 05:16:00 | NPP-375D | DOVERLÂNDIA | GOIÁS | Brasil | 5207253 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1599ced1-e972-340c-bed6-7f102036cdf8 | -18.16031 | -53.32451 | 2025-10-05 05:16:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8f473646-c070-3456-bdb9-2ad96097cf92 | -12.45948 | -45.51649 | 2025-10-05 05:16:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| adfaf7df-85d9-30e4-9118-a8915985ba99 | -10.83382 | -57.17579 | 2025-10-05 05:16:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9d3c76b9-918a-398a-875a-892e523315d4 | -15.23327 | -49.29216 | 2025-10-05 05:16:00 | NPP-375D | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1a9dbb31-efca-3df0-8477-939dfe4a94ea | -17.93005 | -57.60198 | 2025-10-05 05:16:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.9 |
| e9c183cb-a8cf-308d-8a15-c169959daa54 | -12.60663 | -48.12584 | 2025-10-05 05:16:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| b71ebb1f-f78c-3247-90c1-d8904a14315f | -15.75144 | -46.27315 | 2025-10-05 05:16:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4b819f4e-cac2-39d2-b031-cb146059a1ab | -14.94635 | -46.84477 | 2025-10-05 05:16:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9e4a90d9-6206-3333-80ba-937cb4ed1136 | -14.66347 | -48.35946 | 2025-10-05 05:16:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 05593631-b6da-383a-a602-ee6437309421 | -14.93972 | -46.84467 | 2025-10-05 05:16:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e45c60cb-5d29-3185-a0fd-e7a7857b39e8 | -15.23173 | -49.30618 | 2025-10-05 05:16:00 | NPP-375D | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 250e98cb-165f-3cf3-b444-c780a8723078 | -17.70279 | -56.76616 | 2025-10-05 05:16:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 81f70c79-c4f1-32ce-9d10-1a576513c539 | -15.74405 | -46.27803 | 2025-10-05 05:16:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3e2ef0c9-9f7d-30c5-9973-72c60cd34ef7 | -14.93375 | -46.83825 | 2025-10-05 05:16:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 1d4e9068-a79c-3c41-92e4-0cfd02a8ca63 | -13.13109 | -47.97527 | 2025-10-05 05:16:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| fd0ef9a4-95e1-3638-82cd-ff28061511f4 | -17.89616 | -57.63528 | 2025-10-05 05:16:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.4 |
| febe9c40-33ab-3fd3-b14d-cb6deccd1c5a | -15.38496 | -47.94154 | 2025-10-05 05:16:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 49e59f2a-0fcf-3da4-ac64-8bc2c8f2230a | -13.30483 | -48.08839 | 2025-10-05 05:16:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 77c2a677-3574-3743-acaa-7acdf4e682c9 | -10.05438 | -62.46254 | 2025-10-05 05:16:00 | NPP-375D | THEOBROMA | RONDÔNIA | Brasil | 1101609 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b8123750-5e46-3451-be1d-de4317e754fe | -14.74336 | -54.62601 | 2025-10-05 05:16:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 94465616-eae6-3c01-a950-2f1efd54aeae | -13.30329 | -47.7784 | 2025-10-05 05:16:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6152b6cf-fc35-36ee-a467-0748ce280abf | -13.13633 | -47.98246 | 2025-10-05 05:16:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 3355bcb5-7b2c-37a6-ad3a-ea56039888d8 | -12.46096 | -45.51165 | 2025-10-05 05:16:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 51bb3819-8930-3b5f-a060-196b8629a5dc | -12.93123 | -54.72404 | 2025-10-05 05:16:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f27661b9-b3b4-30fa-9741-51a91555eab5 | -17.84703 | -57.62787 | 2025-10-05 05:16:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 4befa90a-ccf6-33af-a327-aa412f72c526 | -17.84418 | -57.62285 | 2025-10-05 05:16:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 474ac3a6-e0e8-304a-8d80-5d8de732ff99 | -14.92616 | -46.84724 | 2025-10-05 05:16:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 61ee0f19-1700-3ea4-97e8-b8f7dc40535a | -13.10191 | -47.85816 | 2025-10-05 05:16:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 0048c990-6441-318d-ab68-210fb862781f | -15.29434 | -46.32357 | 2025-10-05 05:16:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e1e42f64-e2d1-3419-8268-4b13995e075e | -15.60893 | -52.49943 | 2025-10-05 05:16:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6f52dd26-8eee-3429-b78c-3ec75a1ed1b8 | -12.60295 | -48.12859 | 2025-10-05 05:16:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 79f1b05d-c98b-3585-a4d4-663dd142fa84 | -14.82655 | -54.76964 | 2025-10-05 05:16:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4fa7ccc4-8a35-3ca4-a855-1e1028f49018 | -15.22789 | -49.74305 | 2025-10-05 05:16:00 | NPP-375D | IPIRANGA DE GOIÁS | GOIÁS | Brasil | 5210158 | 52 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 0f6ed7f5-b5fb-3727-90fe-1fa59b192291 | -12.55696 | -48.16289 | 2025-10-05 05:16:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9c55604a-dc73-3e76-a4db-0edd6fe6bb30 | -18.14542 | -53.34416 | 2025-10-05 05:16:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 3.8 |
| d4d97ea8-b823-3531-b712-7f04b318e23d | -14.92478 | -46.86042 | 2025-10-05 05:16:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 9d44f1f8-8a53-33df-b62f-7d92b7eaacb9 | -12.27058 | -49.194 | 2025-10-05 05:16:00 | NPP-375D | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 6711b71e-6738-3a0e-9831-cb87e3c3ab68 | -15.2377 | -49.30408 | 2025-10-05 05:16:00 | NPP-375D | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9d2e568b-0bc0-379a-86b8-14bcb80f07b3 | -12.8885 | -47.29147 | 2025-10-05 05:16:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 85e3d66f-2f98-3eb9-83a9-fc2ca0d6682a | -13.5765 | -48.16587 | 2025-10-05 05:16:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7e7e1ba7-4c36-3abf-9806-024148d49edf | -13.14095 | -47.96432 | 2025-10-05 05:16:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e5773f44-7355-3cd2-84e8-1ccf98941d48 | -12.94002 | -51.00821 | 2025-10-05 05:16:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |


[Clique aqui para ver as próximas entradas](README136.md)
