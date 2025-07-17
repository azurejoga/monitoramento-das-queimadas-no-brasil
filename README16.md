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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9c9266aa-a102-37b1-9057-34ca22e699d2 | -14.31884 | -48.65314 | 2025-07-17 03:55:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fe481811-1444-301f-af42-02727c1f6c41 | -11.47468 | -47.31868 | 2025-07-17 03:55:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b56ca0db-2230-35d7-9179-6ee97cb74c02 | -10.96866 | -46.46989 | 2025-07-17 03:55:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 80f81e56-83b5-36ec-9cff-180510c9e1aa | -12.41663 | -50.03981 | 2025-07-17 03:55:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9e0b7a5f-4bf7-35b6-8a0c-7c922713eb95 | -12.57056 | -44.75745 | 2025-07-17 03:55:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0ef98092-0756-3eb7-ac4f-94eda53de9f3 | -9.23892 | -48.56191 | 2025-07-17 03:55:00 | NOAA-20 | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 11ae004d-a00c-36db-b973-71adf8a0f894 | -12.42778 | -50.04216 | 2025-07-17 03:55:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 5c1cf310-fbae-3b6e-8249-2acfb438448f | -11.35824 | -48.72766 | 2025-07-17 03:55:00 | NOAA-20 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 324fe1c6-22f0-3d22-bea1-cee79b982908 | -13.00272 | -44.86758 | 2025-07-17 03:55:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 17b31a27-f7f5-3c02-a3d6-d093ede62fbc | -10.07585 | -43.08982 | 2025-07-17 03:55:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 5b2c5fd1-5c05-3bd7-825e-728c4434f64e | -12.99789 | -44.87187 | 2025-07-17 03:55:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| dff9571e-9cce-3cd1-badc-7f1d9cf189d6 | -12.70078 | -46.80768 | 2025-07-17 03:55:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 84bec565-13ff-30ed-aad6-2eb1ffaa9b20 | -11.10901 | -46.99849 | 2025-07-17 03:55:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6f245c66-a61d-30b9-aa89-312656540268 | -11.84693 | -46.7538 | 2025-07-17 03:55:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 4a47adb2-c047-3f0a-a99e-2a155b84374f | -12.4839 | -46.93862 | 2025-07-17 03:55:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5f9bef14-00fd-3301-adaa-2bf42f2e486e | -11.50452 | -48.95784 | 2025-07-17 03:55:00 | NOAA-20 | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 71de1f2e-69f0-319e-b1b1-2451d8ba4a2c | -12.42299 | -50.03706 | 2025-07-17 03:55:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 5f48d5ed-e668-39b6-aea0-fa028cd20542 | -12.69628 | -46.80682 | 2025-07-17 03:55:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a121aeae-dbdb-343b-9e73-a9539a88b2a5 | -12.42701 | -50.04605 | 2025-07-17 03:55:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 22acd2b7-1d52-33ee-a411-873067e3803f | -12.70979 | -46.80938 | 2025-07-17 03:55:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| c24e96c6-e321-377d-a7a2-38dbbc5825d8 | -9.24047 | -48.5655 | 2025-07-17 03:55:00 | NOAA-20 | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 11.4 |
| beafc1b4-a8f7-34ce-b55a-cf48fbcfec59 | -12.40414 | -50.48898 | 2025-07-17 03:55:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 6eb35503-a250-31f8-b0b5-90de721127b1 | -11.85146 | -46.75475 | 2025-07-17 03:55:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| bd934657-ab12-36fb-93b2-eb335d2674c0 | -9.23575 | -48.56101 | 2025-07-17 03:55:00 | NOAA-20 | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 11.4 |
| cf10d225-e597-34b5-b009-6efd5f08b398 | -12.40576 | -50.48074 | 2025-07-17 03:55:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| a4cc5ec1-ee2b-3a68-8842-d560f8cffafb | -13.12279 | -47.2645 | 2025-07-17 03:55:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ebac23e1-c83f-33c1-9ec9-725b6e446144 | -11.56672 | -47.09238 | 2025-07-17 03:55:00 | NOAA-20 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 65916807-b456-3361-83ac-138a4e467aa5 | -12.42426 | -50.04252 | 2025-07-17 03:55:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a0bde39a-a28c-34f7-9f3d-42def17bc230 | -12.48832 | -46.91491 | 2025-07-17 03:55:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0ba825f6-5a69-3d48-adcf-84ac4ffce504 | -11.39725 | -42.29287 | 2025-07-17 03:55:00 | NOAA-20 | IBIPEBA | BAHIA | Brasil | 2912400 | 29 | 33 | nan | nan | nan | Caatinga | 2.8 |
| cedae8ad-c3b6-38c5-baae-01a85c8d0f6a | -12.41429 | -50.05146 | 2025-07-17 03:55:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 965b9925-cd8b-38ff-b4ce-d5881d4f4858 | -11.94682 | -48.41832 | 2025-07-17 03:55:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| dc794408-7ded-3955-a224-3da6de4de4a9 | -11.24117 | -49.50272 | 2025-07-17 03:55:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 533d5aab-50bb-392c-b0dd-a647d20b9377 | -12.47466 | -44.50181 | 2025-07-17 03:55:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 68e4c26d-45e2-3d83-a45c-fbb5ddb200c0 | -12.69178 | -46.80596 | 2025-07-17 03:55:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 68ccc133-7828-30c3-9df1-d0fa1f2a456b | -11.755 | -47.84651 | 2025-07-17 03:55:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 523cde6e-2155-3f61-b21c-7717a7b07b92 | -12.69305 | -46.80793 | 2025-07-17 03:55:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1a8a2371-bfe8-3388-aec1-84dd2fc8ff7e | -11.3576 | -48.73095 | 2025-07-17 03:55:00 | NOAA-20 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 29eae08e-d97d-36ce-b551-289bd74c863f | -14.2509 | -42.84255 | 2025-07-17 03:55:00 | NOAA-20 | GUANAMBI | BAHIA | Brasil | 2911709 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 8c4ea114-2851-3d5a-b788-61ab71885cf2 | -12.41507 | -50.04758 | 2025-07-17 03:55:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| bf6ab483-fc2b-358a-8b20-91302aa910d7 | -12.58879 | -44.79304 | 2025-07-17 03:55:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fb63c043-9945-35d5-b902-d13a40c79cee | -9.30592 | -44.84697 | 2025-07-17 03:55:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1bbeae88-2c2d-36b5-82be-34f76fabb86d | -13.05631 | -47.80842 | 2025-07-17 03:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6c8b929c-0340-3805-8104-445145e7018e | -14.02061 | -51.22926 | 2025-07-17 03:55:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 033f012b-384e-3c96-8624-13b5a5ed5c5f | -12.09187 | -48.19439 | 2025-07-17 03:55:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d6705993-8920-38ec-af65-c923b13f289c | -14.74836 | -46.3001 | 2025-07-17 03:55:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f1d6be64-fd45-3354-bc64-28915c38e558 | -12.02513 | -47.77976 | 2025-07-17 03:55:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| a3228733-4888-3bcb-a7b7-e9ce1d3b95ee | -13.00091 | -44.87785 | 2025-07-17 03:55:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ad5eed06-0f43-3ce6-85d5-6de1d8e1e2af | -11.58046 | -47.30723 | 2025-07-17 03:55:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8b377ba7-80a3-3cc2-a0b3-ccc9f232e5f1 | -9.49983 | -43.16913 | 2025-07-17 03:55:00 | NOAA-20 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 21cd6565-0490-35bc-9a97-ed9da61f5770 | -12.70528 | -46.80854 | 2025-07-17 03:55:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 2383bb5a-dc3f-3acd-b7fc-f0d9a088912c | -8.87711 | -47.27409 | 2025-07-17 03:55:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9b2da4e6-92d4-3d53-b572-0c7a204638dc | -9.30659 | -44.84308 | 2025-07-17 03:55:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7acf66df-0884-3f30-8ea5-74738ff5bfc5 | -9.41562 | -48.41435 | 2025-07-17 03:55:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b90f482f-de48-371e-9763-5fa4b4fcbedc | -9.24648 | -48.56315 | 2025-07-17 03:55:00 | NOAA-20 | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| d8053989-9c02-3e66-90aa-f641b94e91d0 | -12.47289 | -46.92181 | 2025-07-17 03:55:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e8e90033-688f-3e2f-8515-da3a57368bce | -8.91442 | -47.35363 | 2025-07-17 03:55:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b7e7c1eb-c47c-38dc-abf1-0093d4546953 | -12.49566 | -46.92613 | 2025-07-17 03:55:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 23651de7-7bff-3faa-a768-3ac9759ee925 | -11.1053 | -48.86734 | 2025-07-17 03:55:00 | NOAA-20 | CRIXÁS DO TOCANTINS | TOCANTINS | Brasil | 1706258 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 15b3993b-fe08-3ba5-a35b-505437692fe4 | -12.09171 | -44.73707 | 2025-07-17 03:55:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c61e5cbb-8008-357f-a464-769658575d50 | -12.10244 | -48.19313 | 2025-07-17 03:55:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 920726ba-8a17-3be6-b492-a193b283fa33 | -11.11063 | -48.86825 | 2025-07-17 03:55:00 | NOAA-20 | CRIXÁS DO TOCANTINS | TOCANTINS | Brasil | 1706258 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 11957f09-c01e-3610-8206-b438b6bf5554 | -12.40738 | -50.47251 | 2025-07-17 03:55:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| a2146ddf-febb-3e3e-b569-6de1ebc6fafc | -15.93243 | -43.52342 | 2025-07-17 03:55:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 7c7fd4cb-4d83-3028-ac92-94ecf8c1d090 | -12.41245 | -45.37086 | 2025-07-17 03:55:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 59faab2e-e7b5-3b17-a729-8b0234489e72 | -17.04407 | -43.77491 | 2025-07-17 03:55:00 | NOAA-20 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7212251e-3c2d-3c5a-9fed-2d429872b80d | -12.99879 | -44.86676 | 2025-07-17 03:55:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a554aa3e-3703-3f2b-ad30-5752a4677c12 | -12.41868 | -50.04133 | 2025-07-17 03:55:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| edbec1ed-d65d-37d6-ba85-8dd2cd9333ae | -12.49287 | -46.91579 | 2025-07-17 03:55:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f87127af-ef24-30c4-aa3e-0db9c5a90f1a | -8.87427 | -50.1506 | 2025-07-17 03:55:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9a7900d4-912a-3e91-a1d3-c28ab57c0f92 | -12.70742 | -46.80585 | 2025-07-17 03:55:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a947f00e-454d-3fff-8f23-cac97e7141b5 | -12.56662 | -44.75673 | 2025-07-17 03:55:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0ea822c2-10e1-3fa2-93e3-b86c04fa3c5b | -14.02824 | -51.22192 | 2025-07-17 03:55:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| b5c17325-5016-3ebc-8197-0567bc4bce45 | -9.80335 | -47.74007 | 2025-07-17 03:55:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| f8422ea7-8c4c-3606-8394-67c7b64aef9c | -12.09631 | -48.19829 | 2025-07-17 03:55:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 79366f32-364b-34b8-934d-79bcfab88f03 | -9.23512 | -48.56433 | 2025-07-17 03:55:00 | NOAA-20 | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 79467561-3806-3d39-bad1-97de75712f2a | -12.99485 | -44.86597 | 2025-07-17 03:55:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 74c43a73-9a0e-3105-8fa3-17a0f159b74a | -10.96781 | -46.47461 | 2025-07-17 03:55:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| cf96155d-d3dc-33fd-a3a4-9244f1f0c1ec | -13.06115 | -47.80901 | 2025-07-17 03:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4f98f75c-9d63-32c6-9018-aa548f9453a0 | -14.52033 | -47.67155 | 2025-07-17 03:55:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6c5a5e69-52b2-3606-bea0-09ec403ccddb | -12.70205 | -46.80964 | 2025-07-17 03:55:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 10f7533f-5480-32b6-bdf2-18f599f969dd | -9.24429 | -48.56297 | 2025-07-17 03:55:00 | NOAA-20 | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 4ea86601-b032-3003-9f57-bcd1980aa3a9 | -12.42065 | -50.04874 | 2025-07-17 03:55:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 0bb02e85-bfd4-30cf-aa84-2f4ba6fdc2f2 | -9.4144 | -48.42092 | 2025-07-17 03:55:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b26006f3-a9a7-3222-ac5a-3f91da7ea579 | -11.66662 | -43.76747 | 2025-07-17 03:55:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3f5613e4-3211-398a-9a81-b12987d478c2 | -12.41793 | -50.04523 | 2025-07-17 03:55:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 79043b0b-78c8-379e-a803-6492b5472ca6 | -9.31429 | -44.84846 | 2025-07-17 03:55:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| dacdbaab-89c8-3215-b8f0-219739379b9e | -11.46023 | -45.1006 | 2025-07-17 03:55:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f07e8e1d-f0f3-3079-a812-5bd380be2adf | -11.07813 | -44.53629 | 2025-07-17 03:55:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 17a14b96-b41f-354a-8fb2-9c4722db20e1 | -12.4131 | -50.04018 | 2025-07-17 03:55:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a42c7656-d831-3bd3-8dea-9a58e65a6898 | -9.24583 | -48.5666 | 2025-07-17 03:55:00 | NOAA-20 | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 4b2fd412-1f11-302f-aa5d-730afa4f9376 | -12.48289 | -46.91879 | 2025-07-17 03:55:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7d300820-7f15-301c-bb90-ae435971a729 | -14.24741 | -42.84193 | 2025-07-17 03:55:00 | NOAA-20 | GUANAMBI | BAHIA | Brasil | 2911709 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 8ffed75a-6470-303e-97cc-c4af7a469e3a | -12.19489 | -43.46809 | 2025-07-17 03:55:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2560dfb3-936b-3dbc-95fb-fd58e577d0cb | -14.02319 | -51.22381 | 2025-07-17 03:55:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 1e4b5af6-e3cb-3f95-8f47-8f16bd34870a | -8.70802 | -50.05486 | 2025-07-17 03:55:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 6f213d50-2804-338f-8147-eedf1d9b5043 | -13.06063 | -47.80909 | 2025-07-17 03:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b0115644-4099-3b6b-a101-0f5a73049235 | -8.87342 | -50.15508 | 2025-07-17 03:55:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 5b648a4f-693a-319f-8d64-173ec071f613 | -14.32058 | -48.64926 | 2025-07-17 03:55:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4b030f72-e39f-3388-a59b-9e45a499744b | -12.41719 | -50.04911 | 2025-07-17 03:55:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |


[Clique aqui para ver as próximas entradas](README17.md)
