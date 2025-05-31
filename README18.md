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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d2650b19-8b48-30b5-b359-275ebc015b4a | -11.83574 | -51.27501 | 2025-05-31 05:16:00 | NOAA-20 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 8630c6c5-1acb-3fa7-a821-7aeb44add9df | -11.91176 | -54.82617 | 2025-05-31 05:16:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 61d4057d-d36d-366e-822b-990048bc217f | -11.83658 | -51.26855 | 2025-05-31 05:16:00 | NOAA-20 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 57d1aeca-e004-39af-af64-1d538c5b792e | -10.64655 | -49.42896 | 2025-05-31 05:16:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 66a3b6af-7b1c-3ae8-89e6-9daca48b62fc | -11.64183 | -55.37272 | 2025-05-31 05:16:00 | NOAA-20 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 85a918be-c62f-330e-bc08-a2b1b9620534 | -13.10129 | -52.28368 | 2025-05-31 05:16:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a455b18b-27c7-33ac-9981-535278f84ed9 | -12.50554 | -55.18517 | 2025-05-31 05:16:00 | NOAA-20 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 19aed6c9-882f-3223-9a32-70b34d1de8eb | -11.91382 | -54.42385 | 2025-05-31 05:16:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8660f4f1-422c-3e10-badd-5cb741c8a146 | -11.8418 | -51.26921 | 2025-05-31 05:16:00 | NOAA-20 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| cf5e5ca8-9676-3242-984a-78f0e63baf84 | -12.03774 | -54.9671 | 2025-05-31 05:16:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7f702dcc-158f-3301-ba74-e69839225d6d | -11.91437 | -54.41986 | 2025-05-31 05:16:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d03eee63-0370-30c7-9df9-020c3d88ba9f | -10.32902 | -57.4921 | 2025-05-31 05:16:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 59992cd0-ded0-3c8f-a054-82967540c9ae | -11.14515 | -53.94089 | 2025-05-31 05:16:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 27d356d8-7c15-3be4-af7b-2969471a51d4 | -9.39396 | -48.42062 | 2025-05-31 05:16:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 21dfa40f-c2da-3f8f-8940-6fd7224db21c | -11.83692 | -51.26899 | 2025-05-31 05:16:00 | NOAA-20 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 78dea003-ee63-35ab-b5e4-5307b755b799 | -8.47188 | -49.60173 | 2025-05-31 05:16:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b7253e1d-1aa2-3cef-833c-73be62cf8a55 | -11.83178 | -51.26455 | 2025-05-31 05:16:00 | NOAA-20 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 2ae7ada4-0c61-3ac9-8fce-e3e8a20439dc | -10.21696 | -59.33686 | 2025-05-31 05:16:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b264946e-6f83-3eaf-b843-bbfc9c6e2ef3 | -13.0896 | -52.04748 | 2025-05-31 05:16:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f433247a-a7b8-3245-8e45-11e25e644349 | -11.84784 | -57.85133 | 2025-05-31 05:16:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fa9cddb2-297a-33ac-aefc-5411e52c983b | -13.6378 | -52.18351 | 2025-05-31 05:16:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 03143de8-12e2-3913-940e-4dc130440f4d | -12.034 | -49.52111 | 2025-05-31 05:16:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 73642198-9c2b-3c33-b570-7569236f0c9b | -12.45478 | -54.91608 | 2025-05-31 05:16:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f995eb2d-cf20-3687-b8af-09a1b61312b4 | -11.837 | -51.2653 | 2025-05-31 05:16:00 | NOAA-20 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 12.1 |
| e7a54df6-fabd-3770-87c6-f1fde7e5633b | -12.12572 | -54.66584 | 2025-05-31 05:16:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| deb070fb-abc4-331c-b9d3-b3b0bfcf6060 | -11.4553 | -49.09756 | 2025-05-31 05:16:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0debe2e9-4fcf-3b25-903d-e2e63354053f | -7.30933 | -55.30874 | 2025-05-31 05:16:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 17810624-b99b-341a-9c81-5cf75b47fa76 | -11.83012 | -51.27742 | 2025-05-31 05:16:00 | NOAA-20 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 7.5 |
| b62d5670-d4d0-30cc-bc5e-3681bc030d81 | -9.91996 | -59.90858 | 2025-05-31 05:16:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c966a02e-24f0-36a6-b942-9f1d27c2b326 | -11.14028 | -53.94436 | 2025-05-31 05:16:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e199759f-bdb0-3581-bde1-b072a222db1f | -10.8264 | -56.95043 | 2025-05-31 05:16:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 9b25fb6a-585e-3e36-a4f6-dbe253a6e3ed | -12.37527 | -54.16457 | 2025-05-31 05:16:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cc355b9d-bab4-3342-87c4-72a661c86453 | -11.91804 | -54.4244 | 2025-05-31 05:16:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 1de0e149-f780-34a4-8061-f2a627150374 | -8.81044 | -49.84387 | 2025-05-31 05:16:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a50350ea-3cae-3b94-96e6-ac8e5f84a404 | -10.3325 | -57.49263 | 2025-05-31 05:16:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c6ca4e48-26ec-32be-be66-b19f839add89 | -11.13219 | -54.21895 | 2025-05-31 05:16:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 41aa795c-cda1-3ca1-a51d-66122e1957d5 | -10.63971 | -49.43641 | 2025-05-31 05:16:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| de0f60ad-279f-32f7-b249-722f9a7084e1 | -11.83772 | -51.26246 | 2025-05-31 05:16:00 | NOAA-20 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 0beea0c7-849b-3603-927b-0eef683a7f97 | -10.46397 | -47.94982 | 2025-05-31 05:16:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 11.2 |
| bbd9aa0a-b9c5-3ddc-a1ab-b4c47add4631 | -11.63507 | -58.01296 | 2025-05-31 05:16:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fa721a68-b09c-3f15-90cf-6c94f2563458 | -11.83616 | -51.27179 | 2025-05-31 05:16:00 | NOAA-20 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 14.3 |
| be469f30-d40c-3f97-9ae3-7ad62c56c09e | -11.901 | -54.79068 | 2025-05-31 05:16:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 437454b5-5de3-37ba-b4b7-9df2a087f6ec | -10.83735 | -54.01873 | 2025-05-31 05:16:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9668de3a-d27f-3c3a-9208-8a1460585127 | -10.65234 | -49.42978 | 2025-05-31 05:16:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 3a27aaca-c5ba-303c-b782-6cc90bfa737b | -12.12518 | -54.66969 | 2025-05-31 05:16:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 475f032a-9524-307a-8e2e-69e71e63ba0d | -11.82491 | -51.27663 | 2025-05-31 05:16:00 | NOAA-20 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d41e9ae6-9f1c-3506-acbe-d2710928eaeb | -9.52509 | -54.76947 | 2025-05-31 05:16:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d2416168-d573-3bde-aaf5-4813739c825b | -10.11684 | -58.22067 | 2025-05-31 05:16:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 20089fd9-ce61-3fd1-9635-1b58d36ed6fa | -10.64601 | -49.43318 | 2025-05-31 05:16:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 1581a3a8-34f5-3d47-84b8-d5a6615a85fc | -10.33076 | -57.49157 | 2025-05-31 05:16:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 83ff9c66-93af-39d5-9786-e04400f246a0 | -11.90511 | -54.79126 | 2025-05-31 05:16:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 906437ef-6111-3294-95c0-a5e2b14c5ae7 | -10.55903 | -59.21049 | 2025-05-31 05:16:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a682b39e-3ca6-319a-95d7-eff254328842 | -10.2999 | -57.13744 | 2025-05-31 05:16:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ff53b052-6d67-30be-9b9c-25f6d23620d7 | -7.55751 | -63.27023 | 2025-05-31 05:16:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b6df1655-175b-3733-a253-dc1e16cd7b5c | -11.82574 | -51.27022 | 2025-05-31 05:16:00 | NOAA-20 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 24be068f-b42d-3f2c-ac75-14d3fd2a79f6 | -12.50073 | -55.18535 | 2025-05-31 05:16:00 | NOAA-20 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9367e186-801d-3e0e-a8a0-5812592c87b4 | -9.52586 | -54.76418 | 2025-05-31 05:16:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0c9546fb-ba4f-32a6-b216-2a53f365b09c | -12.18353 | -54.24947 | 2025-05-31 05:16:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 7bb1e793-983d-3275-8813-ae3ba523d591 | -11.14085 | -53.94025 | 2025-05-31 05:16:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 30b57197-3430-30e5-a0c6-e40456ad7e2d | -14.07281 | -47.65899 | 2025-05-31 05:16:00 | NOAA-20 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ef2ac38f-5082-3df6-9278-7f744cf3933e | -11.3602 | -55.12806 | 2025-05-31 05:16:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e4f8817a-0483-353a-a8a4-50dbc4a70c83 | -14.01638 | -55.1264 | 2025-05-31 05:18:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c1ff15e0-06a3-3ab2-963d-fe841fc05e8a | -14.0278 | -55.13599 | 2025-05-31 05:18:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 08cfaa09-a5bf-371c-a71d-1619a4dd1353 | -14.01934 | -55.12021 | 2025-05-31 05:18:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| db16126a-c78e-3942-8d8f-fa0e8cfe6495 | -14.02081 | -55.1402 | 2025-05-31 05:18:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 525753b8-5ff7-38da-9f46-36c86f43fea7 | -13.95376 | -54.49097 | 2025-05-31 05:18:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c12e04b3-1f00-35a5-8246-37671a14965e | -14.55518 | -59.69512 | 2025-05-31 05:18:00 | NOAA-20 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c6006c6f-942c-3e8e-9a66-2c2e67cfff0b | -13.94943 | -54.49043 | 2025-05-31 05:18:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c421245c-ecf3-3f7e-bffe-ec28fcad0ed8 | -18.83853 | -53.60484 | 2025-05-31 05:18:00 | NOAA-20 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c8a4ee7f-84c3-329d-bd3b-715b65915a0e | -19.1949 | -52.09382 | 2025-05-31 05:18:00 | NOAA-20 | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5dc2dff1-e205-30a3-90b5-dadd371d4922 | -13.94998 | -54.48628 | 2025-05-31 05:18:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 32175cbe-0215-345b-9516-1bdded57f3b8 | -19.19379 | -52.09243 | 2025-05-31 05:18:00 | NOAA-20 | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a1e170a6-4f4e-303c-b9af-48754026ec47 | -13.9451 | -54.4899 | 2025-05-31 05:18:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 580f9324-fc16-3ef1-a8f0-6d1e55126a71 | -14.02831 | -55.13211 | 2025-05-31 05:18:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 86df68a4-357a-30fb-af53-5a62f329b746 | -19.19563 | -52.08653 | 2025-05-31 05:18:00 | NOAA-20 | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0fbf223c-2365-37b3-8788-fc74e4c0ea37 | -14.01881 | -55.1241 | 2025-05-31 05:18:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d3ec205a-7c1c-3b5c-b698-9eb14916358f | -16.12292 | -46.82594 | 2025-05-31 05:18:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| dc183edc-8181-3394-8ea8-d817a1f0a823 | -14.02053 | -55.12699 | 2025-05-31 05:18:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c4f30175-197a-3543-a029-993b4628abe0 | -14.38594 | -60.22532 | 2025-05-31 05:18:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 551e934f-f1b9-3436-9db1-cf3f0b0eec87 | -16.11575 | -46.8246 | 2025-05-31 05:18:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e76f42af-397f-3b16-917f-354b113aa93c | -18.83914 | -53.59927 | 2025-05-31 05:18:00 | NOAA-20 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 57e29e47-b39e-3149-8dc4-7d8ac0e5ea09 | -14.01901 | -55.13863 | 2025-05-31 05:18:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dd793087-a891-3d9b-a749-2707cdcbc68d | -14.02264 | -55.14312 | 2025-05-31 05:18:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 67b07e78-1746-3c78-80e5-fa1689e59b10 | -14.02417 | -55.13149 | 2025-05-31 05:18:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 59efd3f1-5233-3836-8c9f-aeba2809cd63 | -14.0185 | -55.14251 | 2025-05-31 05:18:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ae3757f9-4780-3393-b0f9-f308394fd468 | -19.19418 | -52.0888 | 2025-05-31 05:18:00 | NOAA-20 | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| aec3b876-7dfd-3176-bdd9-ccdaab5c92a5 | -13.78483 | -54.31087 | 2025-05-31 05:18:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 44c048db-8185-38b2-bf37-b40c3690d360 | -19.19526 | -52.09018 | 2025-05-31 05:18:00 | NOAA-20 | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| df65a062-1194-3b7f-951e-662691d5497d | -13.95432 | -54.4868 | 2025-05-31 05:18:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 384646c2-6ddf-3ce6-b33c-7ff1f70e58a1 | -14.03144 | -55.14044 | 2025-05-31 05:18:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| dcebdb3c-6c2e-38b1-9ce2-27011f0f02fb | -19.19924 | -52.09305 | 2025-05-31 05:18:00 | NOAA-20 | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7871d907-6355-3a70-9e80-6a14bb4520fe | -15.07845 | -48.9448 | 2025-05-31 05:18:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b5b2098e-3450-334d-9c93-779dca06a240 | -14.02882 | -55.12823 | 2025-05-31 05:18:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e84ce013-90b8-3d88-874f-a3a62723794e | -19.19341 | -52.09604 | 2025-05-31 05:18:00 | NOAA-20 | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a59f6179-4f04-38d7-ba0c-50b9d9ce578b | -14.01689 | -55.12249 | 2025-05-31 05:18:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1167ad29-0994-3171-9495-61b8c9a8d12b | -14.01827 | -55.128 | 2025-05-31 05:18:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b1fafa68-9e5c-35ff-a361-2c796e18e2be | -14.03195 | -55.13658 | 2025-05-31 05:18:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1e62a9ff-306f-35de-9269-6a8581cf1cc0 | -19.19599 | -52.08288 | 2025-05-31 05:18:00 | NOAA-20 | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1b4e26bf-c73e-398e-865a-629ad43ddb79 | -19.19496 | -52.08154 | 2025-05-31 05:18:00 | NOAA-20 | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4f235534-e69e-35cf-b8d1-4fe013071c1b | -14.61333 | -47.96732 | 2025-05-31 05:18:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |


[Clique aqui para ver as próximas entradas](README19.md)
