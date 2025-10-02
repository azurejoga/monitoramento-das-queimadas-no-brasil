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

## Dados Diários - Página 38

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 126e4504-c826-3d1b-a6a0-65b0bff3bb2e | -13.8636 | -47.95401 | 2025-10-02 04:04:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 4b37a044-226f-3802-94a8-23b2f46d59d8 | -12.70157 | -48.58751 | 2025-10-02 04:04:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 42ac64ae-8cc0-3ca3-a7e0-2c903a95c122 | -13.17018 | -47.81875 | 2025-10-02 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 282199c8-3fde-324c-b469-f5b304fad712 | -13.12978 | -47.40726 | 2025-10-02 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 993db9ba-99a3-3f5b-9223-fe1c774e27b9 | -13.66596 | -48.0899 | 2025-10-02 04:04:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ab0202b6-a85a-320f-ae7e-33d2ad426893 | -13.32078 | -47.22009 | 2025-10-02 04:04:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1e0239ec-5f85-3b4e-b3b1-d5e1e78925a4 | -13.3024 | -46.99685 | 2025-10-02 04:04:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| ced2acec-2aaf-379f-af74-1fe7188f2381 | -14.09246 | -46.65476 | 2025-10-02 04:04:00 | NOAA-21 | IACIARA | GOIÁS | Brasil | 5209903 | 52 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 016b78f9-b8c1-32ff-806e-16a1f167b011 | -13.76036 | -48.69507 | 2025-10-02 04:04:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| f38b2b8b-31df-3ae8-8bbe-72d60090fd50 | -13.22285 | -47.35025 | 2025-10-02 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c7f5b5a3-8500-3174-9cfc-b03e5e46212d | -16.36756 | -47.06023 | 2025-10-02 04:04:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 89e42249-5ce1-3eb0-9dcc-8aab4f4ec1f3 | -13.39761 | -47.77898 | 2025-10-02 04:04:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 2f9a2620-0467-3491-8665-09127715f4c3 | -15.1423 | -46.44756 | 2025-10-02 04:04:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8304282b-eb17-33a0-8d32-1e9ca49752b3 | -12.58638 | -49.89488 | 2025-10-02 04:04:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2b75e892-2a0d-3432-be2a-7b7349af0192 | -13.55699 | -47.28505 | 2025-10-02 04:04:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 4351f108-3b15-31c9-81fe-b6ed3baa3ce5 | -14.21117 | -46.09071 | 2025-10-02 04:04:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c44e8bf4-ef22-32c3-a15f-01eaf66f9a72 | -14.81757 | -51.40585 | 2025-10-02 04:04:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 08948a9e-1858-375b-ac2d-3a374bacc8f3 | -13.64898 | -47.30861 | 2025-10-02 04:04:00 | NOAA-21 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4bcb3414-a9d6-30da-9307-1b86610d1d33 | -14.35088 | -43.84643 | 2025-10-02 04:04:00 | NOAA-21 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ca0995b4-0064-38b2-b652-d591de9152f8 | -14.58945 | -46.72161 | 2025-10-02 04:04:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| a433066a-0576-3ad7-bfb0-8d5fba3efe39 | -19.30425 | -46.24924 | 2025-10-02 04:04:00 | NOAA-21 | RIO PARANAÍBA | MINAS GERAIS | Brasil | 3155504 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 9b5a36d7-6dc1-3c0a-b821-a36251718631 | -14.42618 | -46.13083 | 2025-10-02 04:04:00 | NOAA-21 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 340e04bd-24b0-3a13-91a4-4d96fc9ecc5c | -13.97095 | -44.92299 | 2025-10-02 04:04:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 10dfb331-1c51-32aa-b219-fe6f41ac37a2 | -13.05977 | -47.01774 | 2025-10-02 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 929bdce5-cc8d-3218-b6d7-eaf7a75398ce | -13.52537 | -47.27077 | 2025-10-02 04:04:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 07aaa6b0-1f42-3b7f-b2ce-a9f6308b6c9c | -16.03898 | -50.87091 | 2025-10-02 04:04:00 | NOAA-21 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3180a793-6920-3edb-a7bd-6530e2cb3a76 | -15.2301 | -50.11471 | 2025-10-02 04:04:00 | NOAA-21 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 8.1 |
| cd65b465-f9ee-38f0-8904-51730c93be91 | -13.04833 | -47.0584 | 2025-10-02 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 28798947-2a5f-3833-9afe-d42701e18cc1 | -15.235 | -50.11531 | 2025-10-02 04:04:00 | NOAA-21 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 8.1 |
| a68a0882-ded6-3f93-b4dc-bcabf954fdaf | -13.30713 | -46.99387 | 2025-10-02 04:04:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b50a57a9-f008-3e26-b22d-8ac5bd777452 | -13.46944 | -47.23724 | 2025-10-02 04:04:00 | NOAA-21 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3ab719b2-b1dc-37c3-b336-3c1e3b520d8a | -16.02398 | -50.92047 | 2025-10-02 04:04:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 76f1e11b-5901-311a-8dd5-cf1a2fe0c734 | -19.25648 | -46.22667 | 2025-10-02 04:04:00 | NOAA-21 | RIO PARANAÍBA | MINAS GERAIS | Brasil | 3155504 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 849c8cfa-47fa-34b2-9a4c-aed013f59510 | -14.47226 | -48.42289 | 2025-10-02 04:04:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| affe0788-23f9-31c1-a0e8-20d073e24b7f | -14.21909 | -44.93298 | 2025-10-02 04:04:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5c9d3287-9b97-3fa0-a689-59ddeb18f484 | -13.15938 | -47.83962 | 2025-10-02 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| c52fd41c-09fc-301e-a702-c9453aa1807c | -18.89164 | -48.29313 | 2025-10-02 04:04:00 | NOAA-21 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 260872bf-e491-335f-904e-00a28a79c820 | -14.31663 | -45.99923 | 2025-10-02 04:04:00 | NOAA-21 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 8766df0d-05bc-374b-b577-e77b77136f8b | -15.92927 | -43.33828 | 2025-10-02 04:04:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1de1675d-4fca-3a11-8f14-955db87159fa | -16.3696 | -47.07257 | 2025-10-02 04:04:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c39bfa6a-64af-31f3-a2ef-e92214b26ed3 | -14.36634 | -45.9592 | 2025-10-02 04:04:00 | NOAA-21 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 0431b5b0-7567-3a86-b5aa-3fec0cb5d072 | -14.91164 | -47.23364 | 2025-10-02 04:04:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b0c4a54d-1348-3202-b005-90b0be1bd86c | -14.21068 | -46.11622 | 2025-10-02 04:04:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| a41207f3-daa8-3f27-9332-d4832ac1c138 | -17.95116 | -46.80653 | 2025-10-02 04:04:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 707412d4-895c-386d-969a-567d92ca20ee | -14.33054 | -45.87473 | 2025-10-02 04:04:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 58766366-95fd-39f5-9c99-91f74330619e | -14.97898 | -46.86961 | 2025-10-02 04:04:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 20d28356-3fb6-3272-ae68-7cd50d2c0d50 | -17.11334 | -47.12149 | 2025-10-02 04:04:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8c0fcc5b-e5bf-32a7-8db5-3cc242634d54 | -14.41054 | -46.10806 | 2025-10-02 04:04:00 | NOAA-21 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c58c3387-dd2b-391d-aa26-0a2c573cd6e9 | -13.40322 | -47.79658 | 2025-10-02 04:04:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 51c612ce-fd5a-348d-b43d-5881ed4c8314 | -14.34367 | -47.12862 | 2025-10-02 04:04:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 235aea41-fbc5-3666-8007-07158f5a1132 | -14.35237 | -47.12664 | 2025-10-02 04:04:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a21d00a9-e47a-3562-8814-ccf6fa5b5811 | -14.42026 | -46.11972 | 2025-10-02 04:04:00 | NOAA-21 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3aa2969a-2ff2-3a3a-80b4-77bd0db16f18 | -14.90384 | -48.32199 | 2025-10-02 04:04:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| ac844841-d28a-3538-8090-bb4f89ee3523 | -15.75994 | -43.66535 | 2025-10-02 04:04:00 | NOAA-21 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bbe72ef2-8091-398c-ace4-d8493aac18b2 | -16.36958 | -42.30523 | 2025-10-02 04:04:00 | NOAA-21 | RUBELITA | MINAS GERAIS | Brasil | 3156502 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| e9dc7e91-1044-3eb8-ba2a-29f5c018194f | -19.35701 | -44.54564 | 2025-10-02 04:04:00 | NOAA-21 | PARAOPEBA | MINAS GERAIS | Brasil | 3147402 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f455eba1-22cf-3a10-bf2f-5a0d6421a963 | -17.55499 | -44.48462 | 2025-10-02 04:04:00 | NOAA-21 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 974d5157-3d2e-3509-ba57-431dbfd703cc | -15.31477 | -46.39362 | 2025-10-02 04:04:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c9b2eeda-1168-389a-bb48-f93d4f6af57f | -14.59872 | -48.33132 | 2025-10-02 04:04:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c0e253bb-ca79-3cd7-b3a6-60b04495b69d | -12.68912 | -48.57763 | 2025-10-02 04:04:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 20e7d917-02a3-3afa-b01f-66dcba3b4087 | -14.42652 | -46.10624 | 2025-10-02 04:04:00 | NOAA-21 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| e03f44b7-ec79-34d2-b4a2-18e5dec3387e | -16.37288 | -42.30578 | 2025-10-02 04:04:00 | NOAA-21 | RUBELITA | MINAS GERAIS | Brasil | 3156502 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| e6986638-8805-36f2-bd98-004439c7253b | -15.78658 | -43.73501 | 2025-10-02 04:04:00 | NOAA-21 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d208cc0c-0e55-3aef-aaa5-f9b740e143da | -15.30552 | -45.06807 | 2025-10-02 04:04:00 | NOAA-21 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e0c961ef-1e14-3231-a10a-a56e3954a605 | -15.83008 | -42.6207 | 2025-10-02 04:04:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 00b97448-7b1a-34ca-907a-22a4cab4f6cd | -17.18144 | -47.03168 | 2025-10-02 04:04:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 100.6 |
| 35666576-7487-3309-98de-22ee103a7100 | -14.68418 | -48.11306 | 2025-10-02 04:04:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4f0afeb4-6637-360a-abe8-93cea96833e3 | -17.95767 | -44.41294 | 2025-10-02 04:04:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 60d6c6ec-314d-331b-b790-b0f6af9ba425 | -15.74953 | -43.68648 | 2025-10-02 04:04:00 | NOAA-21 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0dc0aa67-643f-3282-b4e3-68427e82b43c | -13.30648 | -46.99759 | 2025-10-02 04:04:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f9bab268-81ac-3dd1-96d4-a185553cc686 | -13.77369 | -48.04656 | 2025-10-02 04:04:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 0142beff-933c-3bd0-af80-5b7e9e50c4c4 | -13.148 | -47.8431 | 2025-10-02 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| c2ae4fe9-402f-3f1d-8033-86cf2422000a | -19.62046 | -43.91281 | 2025-10-02 04:04:00 | NOAA-21 | LAGOA SANTA | MINAS GERAIS | Brasil | 3137601 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 69dafe28-a372-3bbf-b482-b43a0d432d4f | -14.71152 | -48.20616 | 2025-10-02 04:04:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ad24e8b1-9ef2-3bac-aa2e-8f58eb02f822 | -16.06786 | -51.00932 | 2025-10-02 04:04:00 | NOAA-21 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| eb902a90-5185-30be-bb76-2510070ac144 | -18.12015 | -42.72913 | 2025-10-02 04:04:00 | NOAA-21 | FREI LAGONEGRO | MINAS GERAIS | Brasil | 3126950 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 18788ff2-12bb-3d2c-a0f6-2ee72b04389b | -20.1115 | -44.38962 | 2025-10-02 04:04:00 | NOAA-21 | MATEUS LEME | MINAS GERAIS | Brasil | 3140704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| c06261b5-c511-3c52-96ea-ff04a63ced66 | -13.78225 | -47.9989 | 2025-10-02 04:04:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c3a116cb-221a-38a1-8d0f-4392efb30ad0 | -14.58473 | -48.32891 | 2025-10-02 04:04:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 538c3b86-b546-367d-adc7-bae5e83c5832 | -13.30087 | -47.21209 | 2025-10-02 04:04:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ea279fda-285c-3857-bc42-ce2b0c4afec2 | -13.76161 | -47.98964 | 2025-10-02 04:04:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 99104795-e4fb-3fec-b300-0a748d94f33f | -13.21693 | -48.43699 | 2025-10-02 04:04:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 3d2c7a8d-140a-3fb7-aa1e-7c147cc18b49 | -16.15353 | -45.10772 | 2025-10-02 04:04:00 | NOAA-21 | PINTÓPOLIS | MINAS GERAIS | Brasil | 3150570 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 693732de-6b6a-35e1-9c15-6be51776088c | -14.90394 | -47.18307 | 2025-10-02 04:04:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c4edc677-1649-35f8-8fb9-a9ada9fec704 | -20.12652 | -46.33225 | 2025-10-02 04:04:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d3172fce-396b-3e6c-8f29-11291b477e78 | -15.36084 | -47.06543 | 2025-10-02 04:04:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 91f3db0f-ea63-37f4-a1a1-f8a41ea58041 | -19.46164 | -43.65071 | 2025-10-02 04:04:00 | NOAA-21 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5834fae3-84f7-3fc3-b23c-e56047d4b4ef | -15.99706 | -50.89833 | 2025-10-02 04:04:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 4ea543b2-d551-3322-a45c-4ac48f744aa5 | -13.40601 | -44.39124 | 2025-10-02 04:04:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 47312be7-e02a-3442-b7a5-dbebdf772f04 | -14.90825 | -47.22924 | 2025-10-02 04:04:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f5e25b0e-935a-3db8-bff1-34ee5cac9816 | -14.89711 | -48.33434 | 2025-10-02 04:04:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 14e9e511-b054-35a1-a0aa-2050204bac73 | -12.42048 | -54.34832 | 2025-10-02 04:04:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 24b24eb6-160a-3b63-a2b7-da49ab62a028 | -14.46824 | -48.39511 | 2025-10-02 04:04:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| ce1a653c-4750-3b48-945e-97e403a4497e | -14.88724 | -48.12289 | 2025-10-02 04:04:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| aa25c32b-8503-3f48-8f15-652f8a66352a | -16.36781 | -47.08245 | 2025-10-02 04:04:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 23a851b8-bb8e-385b-b883-eb7f0a86906f | -14.20362 | -46.08897 | 2025-10-02 04:04:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3f43cad0-a962-3857-992d-64b2ca1b5cd9 | -20.1306 | -46.35088 | 2025-10-02 04:04:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 91523370-72b8-3c6e-89eb-ba12ff9d0a43 | -13.95149 | -48.09456 | 2025-10-02 04:04:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 626c748e-ba88-3284-9109-f7781b8a3961 | -14.79146 | -46.99382 | 2025-10-02 04:04:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4b71158c-a2f6-387a-91a4-a977a5e1bd99 | -13.76235 | -47.98557 | 2025-10-02 04:04:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |


[Clique aqui para ver as próximas entradas](README39.md)
