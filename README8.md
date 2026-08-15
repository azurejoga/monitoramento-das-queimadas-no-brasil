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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| aeb6978e-fab0-3282-a164-14896552a356 | -5.1166 | -41.10016 | 2026-08-15 03:53:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 04dd5e44-f399-33d9-a86e-747c20944d45 | -9.56907 | -45.37648 | 2026-08-15 03:53:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b2e31fe3-e141-30fc-a1ca-9d1187d70862 | -6.12265 | -44.02936 | 2026-08-15 03:53:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| df620515-5e7a-30c4-b0bd-657974024bf2 | -9.12334 | -46.40517 | 2026-08-15 03:53:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 6e01bebf-05a2-3a38-b72c-3ad96896e873 | -7.26264 | -44.70046 | 2026-08-15 03:53:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3ca8fd05-4b2a-3595-ab72-956f9a4fbda2 | -6.2502 | -47.71405 | 2026-08-15 03:53:00 | NPP-375D | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c3d4b977-4100-3c29-8672-75af32be18e1 | -6.84222 | -45.36661 | 2026-08-15 03:53:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f8350c4f-bb93-3910-aca3-42fa3a4f4b65 | -6.60382 | -39.64036 | 2026-08-15 03:53:00 | NPP-375D | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 3.0 |
| af4fcbce-dd84-3e70-8a94-a3f109f4b9f7 | -9.1191 | -46.39612 | 2026-08-15 03:53:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 16f65633-ecf1-38a6-ba6b-d229e76916c8 | -7.28393 | -44.70469 | 2026-08-15 03:53:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 80c725c1-f4c4-3edd-bee2-e223f2bb88a0 | -9.11339 | -46.39698 | 2026-08-15 03:53:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 88fa6b77-2d8f-3b03-a863-f0c1320133e6 | -6.91215 | -43.63406 | 2026-08-15 03:53:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 6.9 |
| bed64d28-2e5f-3609-8ee5-099fa089ca1b | -8.49142 | -44.74259 | 2026-08-15 03:53:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| c9d9d474-88f1-31cc-ba0b-feb06d8c6bec | -7.82097 | -44.11187 | 2026-08-15 03:53:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b9687737-8b92-3c99-aefd-821f4d5f8018 | -7.26797 | -44.70151 | 2026-08-15 03:53:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 975c6738-2333-30e7-b1e5-1710b11df5de | -5.9365 | -43.64714 | 2026-08-15 03:53:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a94e7495-9022-30e3-a5fd-708c4aae5571 | -6.92113 | -43.64169 | 2026-08-15 03:53:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 22.8 |
| 3b24cd50-23d8-3ddf-b48c-319a20c804b8 | -6.83957 | -45.36323 | 2026-08-15 03:53:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f8a64a9b-7f21-35b2-a709-9477a722f0ee | -6.93217 | -43.6375 | 2026-08-15 03:53:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 8aeeb8a9-16c2-324d-b51f-35f2e22599c8 | -6.41299 | -39.25334 | 2026-08-15 03:53:00 | NPP-375D | IGUATU | CEARÁ | Brasil | 2305506 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| e2abc6fd-b285-312a-9390-fd70f9070ff1 | -6.24359 | -47.71309 | 2026-08-15 03:53:00 | NPP-375D | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cf052813-95dc-38ac-9e4f-8cedae2d66dc | -7.14915 | -39.31376 | 2026-08-15 03:53:00 | NPP-375D | JUAZEIRO DO NORTE | CEARÁ | Brasil | 2307304 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 819cf6e2-752f-3754-99f6-265483e76fed | -6.93317 | -43.63172 | 2026-08-15 03:53:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a3a080ad-d58b-38ff-851d-1b3f0025eb57 | -6.97829 | -41.29175 | 2026-08-15 03:53:00 | NPP-375D | SANTO ANTÔNIO DE LISBOA | PIAUÍ | Brasil | 2209401 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 60415df1-886a-308b-b281-ada5bf553f09 | -5.67061 | -43.57731 | 2026-08-15 03:53:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 737b3a05-6618-351d-af16-b271f2699ba7 | -6.34167 | -44.06858 | 2026-08-15 03:53:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ee7c01a2-a6cf-381c-9c36-3bf52b77ebf6 | -5.66763 | -43.57751 | 2026-08-15 03:53:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 23b7230e-6721-393b-a2d9-a24447ad043a | -5.11587 | -41.10437 | 2026-08-15 03:53:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| a7287585-3acb-3c58-b258-0f92d0784461 | -6.99695 | -44.82942 | 2026-08-15 03:53:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 74d7d610-5286-331d-af9e-79b6d723cc4b | -8.71472 | -49.60695 | 2026-08-15 03:53:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6554550b-922e-3b49-b600-0bbe8a33ea98 | -6.11651 | -44.03422 | 2026-08-15 03:53:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 20.9 |
| 354d5799-2e7b-328f-8d5c-c624033aa9fe | -9.13726 | -46.3972 | 2026-08-15 03:53:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8080ff45-32b8-3eab-9cd9-2f5f3364bc31 | -7.80883 | -44.1069 | 2026-08-15 03:53:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ae981cb5-2750-337a-a62c-8012a40bb7af | -5.93755 | -43.6411 | 2026-08-15 03:53:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7920b63d-5401-3b62-8a7b-1ea5fce1417c | -6.33592 | -44.07073 | 2026-08-15 03:53:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5ed48d01-700d-3436-859e-0bd0877216f7 | -9.11916 | -46.3981 | 2026-08-15 03:53:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 3e3c0f48-44c9-34b4-8c75-6d8fdb1e73c8 | -6.33639 | -44.06775 | 2026-08-15 03:53:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8dfefa94-64c6-3a3e-a714-339bf8bb3ed0 | -6.85958 | -41.64464 | 2026-08-15 03:53:00 | NPP-375D | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 4d979381-b9c3-3c8d-8597-dcc8c6501e04 | -9.11497 | -49.26567 | 2026-08-15 03:53:00 | NPP-375D | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b2d79a72-adef-3477-bde5-1621e787f12f | -6.92318 | -43.6299 | 2026-08-15 03:53:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 8.3 |
| de4b58f0-5d02-3f78-b76e-aeb9bce5765e | -7.27802 | -44.70698 | 2026-08-15 03:53:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8dbfe409-5049-3626-92e4-0a408dec7a72 | -7.72312 | -46.24409 | 2026-08-15 03:53:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5098f71a-54b1-3fe3-82bb-5067561fca75 | -5.12004 | -41.10151 | 2026-08-15 03:53:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 787d9a2b-71af-371e-9458-e66870559764 | -6.91715 | -43.63491 | 2026-08-15 03:53:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 6.9 |
| fba67944-a021-383a-8342-c435d645dc39 | -5.66604 | -43.57351 | 2026-08-15 03:53:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 36a15d33-c909-3e97-a8e5-d25343463be4 | -6.1216 | -44.03522 | 2026-08-15 03:53:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 0ef7e447-7d09-3bbe-a27a-0b97835d05fe | -6.94054 | -44.54245 | 2026-08-15 03:53:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d985cac2-9267-30f7-8389-da3763e9539e | -8.07213 | -35.61271 | 2026-08-15 03:53:00 | NPP-375D | PASSIRA | PERNAMBUCO | Brasil | 2610509 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 3b8c6823-bc03-349c-8974-2849097d9898 | -9.2888 | -36.85275 | 2026-08-15 03:53:00 | NPP-375D | MINADOR DO NEGRÃO | ALAGOAS | Brasil | 2705309 | 27 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 46f55c3c-b259-36a6-a4e0-4c09c53b7100 | -7.2808 | -44.70542 | 2026-08-15 03:53:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6777d89d-c34e-3b67-8429-73e009fa34c0 | -5.93246 | -43.64018 | 2026-08-15 03:53:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 82a28b43-9841-3ea3-ac91-2d44ecb73b55 | -6.34112 | -44.07162 | 2026-08-15 03:53:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 42ab6e22-f033-312e-96f4-4c55db3fa83c | -6.86485 | -43.87467 | 2026-08-15 03:53:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 36633bfb-a38d-3592-bf31-be06f7ec0397 | -9.1119 | -46.40501 | 2026-08-15 03:53:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 0e2bec68-b994-36b8-a5bf-540ff9cc2141 | -6.11749 | -44.02819 | 2026-08-15 03:53:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 18.3 |
| 756ae952-32bb-3464-9e6d-c1647261d33d | -6.92216 | -43.63576 | 2026-08-15 03:53:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 22.8 |
| 04f28ce5-0af2-35f3-ae9a-4eb8c201032c | -7.72901 | -46.24501 | 2026-08-15 03:53:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a8223af7-c57a-3f35-9b4d-1b6688aaa9b1 | -6.92614 | -43.64254 | 2026-08-15 03:53:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 22.8 |
| 80a0a5f6-04a4-3cf2-9e98-c8b6703d5b37 | -7.28278 | -44.68003 | 2026-08-15 03:53:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 652dd6b1-0e59-3e3c-a1f8-07976c34e58a | -6.91817 | -43.62905 | 2026-08-15 03:53:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0fae1de4-cbf4-3f3d-b497-f4d25c8b0ba5 | -7.8083 | -44.10991 | 2026-08-15 03:53:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fbfa1c2d-5515-3809-b3a7-4915b6939bc7 | -9.11671 | -46.40849 | 2026-08-15 03:53:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 12.2 |
| dc4f2ea2-3cbc-3d77-a441-d27be8236b64 | -8.6236 | -45.85842 | 2026-08-15 03:53:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4cfe3fc0-1a0a-3b67-ab60-87285a2150a2 | -7.62436 | -44.15206 | 2026-08-15 03:53:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d3e98b04-1a33-3d65-b7d0-d67fac1be927 | -6.92818 | -43.63079 | 2026-08-15 03:53:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 5f89fb36-80af-33bd-bcc7-59b80700d70c | -7.01683 | -41.43851 | 2026-08-15 03:53:00 | NPP-375D | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 4b2bc057-e646-3ba5-b25b-9ce0ed0fd556 | -6.93463 | -44.54485 | 2026-08-15 03:53:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 48d7e0aa-dd26-3bbb-9e73-991e0126acc3 | -8.52145 | -46.53162 | 2026-08-15 03:53:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| d513d436-9ee9-3875-8e36-3391a90882e2 | -7.81742 | -44.11772 | 2026-08-15 03:53:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a871cc8e-54e6-3ada-a0cd-69c1cc2df8b8 | -5.93702 | -43.64415 | 2026-08-15 03:53:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ef7774c8-4770-31b6-98df-fa67d258f85b | -7.81979 | -44.11832 | 2026-08-15 03:53:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e2f84c24-b710-3ad8-9927-cddac339fb25 | -8.49546 | -44.75005 | 2026-08-15 03:53:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| bbd297c9-d2da-3a87-99b4-18f75d690bbb | -6.84521 | -45.38186 | 2026-08-15 03:53:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c8bcc3f6-1baa-3477-a817-323bbe61b47b | -8.51559 | -46.53042 | 2026-08-15 03:53:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| ecd33c5f-f718-33ae-9827-56fa41651107 | -9.11371 | -49.27191 | 2026-08-15 03:53:00 | NPP-375D | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e62c6c31-bdf5-3615-82bb-4c3ea08b60cf | -10.76367 | -42.09138 | 2026-08-15 03:53:00 | NPP-375D | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| b55e7b56-526a-35f0-ac1a-d42ec3fedfa1 | -6.12219 | -44.03241 | 2026-08-15 03:53:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 0438d6c7-2a6f-354d-bc4d-3fb1d61e353a | -7.81341 | -44.11071 | 2026-08-15 03:53:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5548e090-fb74-30ce-b606-f39d583033e0 | -11.41584 | -46.3348 | 2026-08-15 03:55:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f9065964-9099-3f77-ae1d-2c29feabf8ec | -12.13022 | -47.16967 | 2026-08-15 03:55:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 87d4c817-9fc3-3697-89e6-3cf82c1242b8 | -13.38054 | -41.34481 | 2026-08-15 03:55:00 | NPP-375D | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| ea52dc87-0af3-314c-85b7-bcd77dba09ed | -14.42948 | -51.85558 | 2026-08-15 03:55:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f0edbb0f-0e8d-3aab-800e-e96a7fae1131 | -16.10417 | -49.86091 | 2026-08-15 03:55:00 | NPP-375D | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 161b6242-2db0-34ed-b189-c35d69d94e4e | -12.08129 | -43.17752 | 2026-08-15 03:55:00 | NPP-375D | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 701841af-9258-30ba-b34c-e7c8f6825739 | -12.1253 | -47.16438 | 2026-08-15 03:55:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 35be61e3-6987-32c2-9dad-50037c99de66 | -11.4143 | -46.34266 | 2026-08-15 03:55:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a5c21160-d054-3eb9-b854-e93d85867a0c | -13.76695 | -41.83791 | 2026-08-15 03:55:00 | NPP-375D | DOM BASÍLIO | BAHIA | Brasil | 2910107 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 40646450-2ca6-36b6-b0ec-4c8b83141798 | -16.71206 | -46.3993 | 2026-08-15 03:55:00 | NPP-375D | DOM BOSCO | MINAS GERAIS | Brasil | 3122470 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5fdc554e-743a-3867-9c77-e2bc6baec8b5 | -14.93512 | -46.61506 | 2026-08-15 03:55:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7d6d1234-f7e3-37d5-99cf-71c19f1792b3 | -14.94798 | -46.63306 | 2026-08-15 03:55:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1d061819-15ab-39de-a0d1-46dc1024c648 | -18.17459 | -43.98723 | 2026-08-15 03:55:00 | NPP-375D | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 14a561fd-b62d-344e-aaf5-1cadeb352d8b | -12.72314 | -48.42537 | 2026-08-15 03:55:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8e62d5b3-ed4e-399a-916a-271042f6382d | -14.43896 | -51.9138 | 2026-08-15 03:55:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 21.2 |
| 8a5283f2-62ba-309e-8605-e4a49cc19826 | -13.68638 | -46.26217 | 2026-08-15 03:55:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7d0e3cd4-681a-3a3f-8096-0086dce22b0c | -13.42931 | -48.34861 | 2026-08-15 03:55:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 42982c7c-8fac-3dca-8fcc-e9ab204bef9e | -12.09576 | -43.16347 | 2026-08-15 03:55:00 | NPP-375D | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 3.1 |
| bf857b4e-f1df-3388-bfb0-a5d0b238e294 | -10.53002 | -44.85302 | 2026-08-15 03:55:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6b190eb4-b44f-36e8-b667-f597a1a41f60 | -11.43062 | -43.91917 | 2026-08-15 03:55:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c9800c3c-4c70-30f8-8bf1-814a5fc731c0 | -11.40783 | -46.34643 | 2026-08-15 03:55:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 73348ed4-5472-361f-81c9-6de9602f0af0 | -14.92194 | -46.62581 | 2026-08-15 03:55:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |


[Clique aqui para ver as próximas entradas](README9.md)
