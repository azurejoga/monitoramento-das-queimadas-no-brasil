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

## Dados Diários - Página 26

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3cc5ab57-0ce0-3330-9172-b94f8d99b392 | -17.712 | -46.7798 | 2026-07-02 12:10:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 167.5 |
| 5d28017e-bc55-30bf-99d0-16616667fc12 | -10.7843 | -53.5434 | 2026-07-02 12:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 91.4 |
| 44a8334a-2630-3d09-8598-165d00b3e2c6 | -9.0494 | -44.7787 | 2026-07-02 12:10:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 82.6 |
| 4ee71783-1c3b-3516-9f32-d4deb3eec178 | -17.712 | -46.7798 | 2026-07-02 12:20:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 216.1 |
| cfda30f4-7dbf-3ab3-b6e7-611121d73805 | -9.0684 | -44.7765 | 2026-07-02 12:20:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 86.9 |
| 65cab1d2-8972-30f6-8515-57bda28aa01b | -17.732 | -46.7756 | 2026-07-02 12:20:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 120.7 |
| 709d64c9-6aa4-30b9-80bc-126bd2add364 | -10.7843 | -53.5434 | 2026-07-02 12:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 107.2 |
| 33185734-0c0f-3ca7-b4f3-7a5f611e374c | -3.50936 | -48.04013 | 2026-07-02 12:25:00 | TERRA_M-T | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 27.1 |
| b2fce2b7-c9ad-349d-8448-3bccdc4457d4 | -6.43119 | -45.61094 | 2026-07-02 12:25:00 | TERRA_M-T | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 162.0 |
| 2a61647f-a1d3-3d97-b02a-daccde93962a | -6.41418 | -45.6092 | 2026-07-02 12:25:00 | TERRA_M-T | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 65.9 |
| 6501a382-8325-319a-af2c-dbb5e3196ea1 | -6.42642 | -45.64933 | 2026-07-02 12:25:00 | TERRA_M-T | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 33.6 |
| 205609ff-d353-3be5-aa2f-9374172b421e | -3.51393 | -48.03533 | 2026-07-02 12:25:00 | TERRA_M-T | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 47.4 |
| ca1e18ad-3acb-3c90-bc74-a62ea2a92fae | -11.38715 | -47.8157 | 2026-07-02 12:27:00 | TERRA_M-T | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 35.4 |
| d67ea60f-83bf-3ea0-973c-94be64805d42 | -10.78805 | -53.53651 | 2026-07-02 12:27:00 | TERRA_M-T | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 126.0 |
| fc94ac70-c7b6-34a0-87b5-d1ff94283e1b | -10.44382 | -56.31083 | 2026-07-02 12:27:00 | TERRA_M-T | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 539f226f-cf48-3127-ac58-49810dc6c93d | -11.41929 | -56.06533 | 2026-07-02 12:27:00 | TERRA_M-T | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 15.2 |
| e1ca427e-37e1-3b20-abec-8b0f568e33b6 | -10.78631 | -54.0992 | 2026-07-02 12:27:00 | TERRA_M-T | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 6d0880bb-bbf3-382d-8815-fce2dd284445 | -11.49846 | -54.49484 | 2026-07-02 12:27:00 | TERRA_M-T | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 7.6 |
| f82214f1-05fe-374a-9ffd-dabee6c305ce | -6.92506 | -51.93662 | 2026-07-02 12:27:00 | TERRA_M-T | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| b715a7c5-1894-3aff-910c-8daeeec0bcb1 | -12.51585 | -48.26355 | 2026-07-02 12:27:00 | TERRA_M-T | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 45.1 |
| dcabcd01-9edb-3381-b54b-718ad1d5a61e | -8.39746 | -48.21185 | 2026-07-02 12:27:00 | TERRA_M-T | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 99.2 |
| 7a31fc1a-9664-3897-b37a-fe64b49af782 | -11.0486 | -56.92848 | 2026-07-02 12:27:00 | TERRA_M-T | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 15.4 |
| 9d42d667-f541-3972-b681-a4ef7e8f7f01 | -8.40072 | -48.21756 | 2026-07-02 12:27:00 | TERRA_M-T | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 101.6 |
| a9a36d8a-3d16-3773-9d70-d9c02894b516 | -10.44255 | -56.31971 | 2026-07-02 12:27:00 | TERRA_M-T | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 13.4 |
| ab710d67-2518-3e98-b4dd-c0b2a3d2fb46 | -10.13216 | -52.0954 | 2026-07-02 12:27:00 | TERRA_M-T | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 13.2 |
| f7538f35-af4f-3117-9017-14c2ce639031 | -11.42056 | -56.05634 | 2026-07-02 12:27:00 | TERRA_M-T | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 13.1 |
| d8f50382-536a-32de-b8b8-1470d074db87 | -8.63233 | -51.29572 | 2026-07-02 12:27:00 | TERRA_M-T | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 89d68f6f-db6f-3958-a6f6-5c6bc04e09aa | -12.51243 | -48.29334 | 2026-07-02 12:27:00 | TERRA_M-T | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 39.4 |
| b2c0b87d-f94f-3105-8b62-fdbc7bc81ab4 | -11.85124 | -48.24279 | 2026-07-02 12:27:00 | TERRA_M-T | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 21.5 |
| a088e845-2f71-3417-98e2-5e8c1debe810 | -10.78658 | -53.54767 | 2026-07-02 12:27:00 | TERRA_M-T | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 46.8 |
| 16d5f1d5-195a-33e0-bd34-1d9d43547738 | -11.85245 | -48.23768 | 2026-07-02 12:27:00 | TERRA_M-T | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 20.8 |
| 1811bee8-ac72-36a7-8150-cd7d1d9b4db6 | -11.38354 | -47.82108 | 2026-07-02 12:27:00 | TERRA_M-T | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 29.5 |
| 7e8fcdc3-7d5b-32f5-808d-212c070b91c2 | -10.12515 | -52.10029 | 2026-07-02 12:27:00 | TERRA_M-T | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 9.6 |
| f4494ddf-f045-38a8-a502-c87965140123 | -10.77681 | -53.54632 | 2026-07-02 12:27:00 | TERRA_M-T | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 7ff9fc3b-0aff-3d9b-8f47-ed6d86e6b4c5 | -12.51373 | -48.27028 | 2026-07-02 12:27:00 | TERRA_M-T | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 59.0 |
| 7aa27f34-fb03-3bf5-9338-ae858cb8d7ff | -12.31339 | -54.12337 | 2026-07-02 12:27:00 | TERRA_M-T | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 754941ad-df0f-31c3-8812-338bc4d5d15c | -10.9099 | -56.85947 | 2026-07-02 12:27:00 | TERRA_M-T | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| bb04eab6-3606-3bce-b8bf-2572e3504b24 | -12.93518 | -56.64105 | 2026-07-02 12:27:00 | TERRA_M-T | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 2066d30d-632a-3383-9625-a30f0db8a7fe | -17.92566 | -52.71105 | 2026-07-02 12:29:00 | TERRA_M-T | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 128.3 |
| 8069a7e6-e4fc-3a5d-9c40-f0e714b42b44 | -14.80943 | -49.00434 | 2026-07-02 12:29:00 | TERRA_M-T | SANTA RITA DO NOVO DESTINO | GOIÁS | Brasil | 5219456 | 52 | 33 | nan | nan | nan | Cerrado | 35.6 |
| e39b6ad8-d2ff-3acf-884b-339dabb81fc1 | -16.92665 | -53.43633 | 2026-07-02 12:29:00 | TERRA_M-T | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 6.8 |
| f42fdd6a-6e1b-341d-ab89-5e822d71810f | -17.92271 | -52.71628 | 2026-07-02 12:29:00 | TERRA_M-T | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 98.7 |
| 00adb723-9ccd-3da3-8808-edfcc7ba021d | -16.92146 | -53.44408 | 2026-07-02 12:29:00 | TERRA_M-T | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 22.9 |
| 193de3fd-d782-300a-97b2-f6190aa6f026 | -17.92451 | -52.69998 | 2026-07-02 12:29:00 | TERRA_M-T | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 27.5 |
| 2c232ba6-4319-3447-8b8e-23eedf32a60d | -22.95782 | -52.58429 | 2026-07-02 12:29:00 | TERRA_M-T | PARANAVAÍ | PARANÁ | Brasil | 4118402 | 41 | 33 | nan | nan | nan | Mata Atlântica | 14.2 |
| ffcb8519-1ada-349c-a947-2e80d5429c7b | -14.80919 | -48.99738 | 2026-07-02 12:29:00 | TERRA_M-T | SANTA RITA DO NOVO DESTINO | GOIÁS | Brasil | 5219456 | 52 | 33 | nan | nan | nan | Cerrado | 31.4 |
| dcfbb797-27cc-3836-bf3f-398b492092fa | -17.58206 | -54.02978 | 2026-07-02 12:29:00 | TERRA_M-T | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 17.2 |
| c5cc9484-2f57-351b-8ec0-82bff8da05da | -17.92374 | -52.72732 | 2026-07-02 12:29:00 | TERRA_M-T | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 19.7 |
| f0096bdd-241b-3cf7-b7eb-6af99d4d3975 | -22.69247 | -53.96418 | 2026-07-02 12:29:00 | TERRA_M-T | JATEÍ | MATO GROSSO DO SUL | Brasil | 5005103 | 50 | 33 | nan | nan | nan | Mata Atlântica | 9.6 |
| 27c0549e-ef6b-3ff3-bdd0-b03499f8a268 | -22.95682 | -52.57778 | 2026-07-02 12:29:00 | TERRA_M-T | PARANAVAÍ | PARANÁ | Brasil | 4118402 | 41 | 33 | nan | nan | nan | Mata Atlântica | 13.1 |
| db094ecf-1901-3263-9034-4618879a1aa9 | -16.92501 | -53.4504 | 2026-07-02 12:29:00 | TERRA_M-T | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 20.0 |
| b61d5e6a-634b-3c91-b597-f23a8a945570 | -17.712 | -46.7798 | 2026-07-02 12:30:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 201.9 |
| 7805f4b9-1656-369e-90c4-d375fcd4ff02 | -8.3583 | -45.6735 | 2026-07-02 12:30:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 116.0 |
| 40e969f9-d946-3bdf-aa8b-d32c490ad333 | -9.0684 | -44.7765 | 2026-07-02 12:30:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 93.5 |
| 5f44556e-9c5f-3c2c-a864-107e4ce3faae | -17.732 | -46.7756 | 2026-07-02 12:30:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 164.5 |
| d19cfa1f-bd1d-3126-a5ea-9b18e8c1ec2e | -12.8552 | -44.3389 | 2026-07-02 12:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 102.0 |
| 1702261c-b949-3d23-a612-ffa69dd66b0e | -10.7843 | -53.5434 | 2026-07-02 12:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 93.6 |
| cb8107e9-d3f8-3f59-927e-7e3f3199f294 | -9.0684 | -44.7765 | 2026-07-02 12:40:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 87.8 |
| 06fbb346-50e1-3335-996a-2f2e39132b41 | -17.7114 | -46.8031 | 2026-07-02 12:40:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 88.4 |
| 47343814-88e5-3763-8a78-41d9d4086780 | -17.732 | -46.7756 | 2026-07-02 12:40:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 94.8 |
| 7be00258-4af4-3105-a6ad-88d86aaa5f67 | -10.7843 | -53.5434 | 2026-07-02 12:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 144.3 |
| 9a5c8624-d754-3484-8942-35629ff4dce8 | -17.712 | -46.7798 | 2026-07-02 12:40:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 238.7 |
| c531ead7-c15f-32e2-b2d7-00d9a7c03ff9 | -12.5135 | -48.2802 | 2026-07-02 12:50:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 88.2 |
| a9abe837-1f35-379c-bd1e-20e072a67c13 | -10.7843 | -53.5434 | 2026-07-02 12:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 134.6 |
| e0e2ce45-c31f-378e-95e6-02d966f9e059 | -17.712 | -46.7798 | 2026-07-02 12:50:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 191.6 |
| e1ac746b-720d-3163-9f24-393c140da42e | -17.732 | -46.7756 | 2026-07-02 12:50:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 170.7 |
| 3e15123a-9099-3151-9782-9a7f8afb216a | -10.7843 | -53.5434 | 2026-07-02 13:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 128.5 |
| 4da4ab49-c26c-369a-be16-a298d5b81b14 | -12.5135 | -48.2802 | 2026-07-02 13:00:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 105.8 |
| 1945fd8c-4b16-3687-a18e-c0b79b2aaa55 | -6.9135 | -43.7281 | 2026-07-02 13:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 86.0 |
| 731548de-2ed8-3f0e-b128-fa76bbf8e34a | -17.732 | -46.7756 | 2026-07-02 13:00:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 186.6 |
| f97488a9-543d-3131-b1a7-12135b564242 | -12.5138 | -48.2581 | 2026-07-02 13:00:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 96.5 |
| c16a1b67-565e-3a92-a2b6-e86300cf99d1 | -9.0684 | -44.7765 | 2026-07-02 13:00:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 75.4 |
| d9c7c5c1-8383-3fac-a352-8219b5a0e98d | -17.712 | -46.7798 | 2026-07-02 13:00:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 192.8 |
| 82639634-5764-3e7c-9941-230748a46408 | -6.9135 | -43.7281 | 2026-07-02 13:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 90.3 |
| 0407dc6f-ea2e-3e1c-b125-936fc1042bd0 | -17.712 | -46.7798 | 2026-07-02 13:10:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 169.1 |
| 7f70035f-e6c3-3e6e-82ef-1e5e7e397bc0 | -12.5135 | -48.2802 | 2026-07-02 13:10:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 118.2 |
| 7f8ca365-33e1-3604-9132-56a33a7cba19 | -12.8552 | -44.3389 | 2026-07-02 13:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 106.8 |
| f3a6d216-2abe-3534-971f-8df39b59a88a | -6.9323 | -43.7264 | 2026-07-02 13:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 85.7 |
| 33482bbb-f4eb-3040-b8b9-ec7ce61a242a | -5.3787 | -43.388 | 2026-07-02 13:10:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 74.2 |
| 61512279-e287-397a-b128-56c117356586 | -12.5138 | -48.2581 | 2026-07-02 13:10:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 117.7 |
| 648b1811-c58c-3f5b-8be1-539c4a3038b0 | -6.9138 | -43.7049 | 2026-07-02 13:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 78.9 |
| 42887895-2890-3bdd-865a-4bff6830bc93 | -10.7843 | -53.5434 | 2026-07-02 13:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 107.9 |
| c95097f9-7bf1-3c98-af7f-f183d6975f04 | -17.732 | -46.7756 | 2026-07-02 13:10:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 185.6 |
| ab0e6f02-4d85-3ed1-a99a-601bd41fe1b4 | -5.3787 | -43.388 | 2026-07-02 13:20:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 84.2 |
| 1ef087f6-73ea-36ed-b0a3-dcdf7774d865 | -12.5135 | -48.2802 | 2026-07-02 13:20:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 111.8 |
| 3e058a65-e3cf-3a56-ae37-23aa960e5658 | -17.7114 | -46.8031 | 2026-07-02 13:20:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 85.0 |
| c50c6ef2-470a-337f-abd8-e802aa67bdac | -12.5138 | -48.2581 | 2026-07-02 13:20:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 109.7 |
| 4d9496e3-845e-307e-8a70-4acf558c864c | -6.9326 | -43.7032 | 2026-07-02 13:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 68.9 |
| 16067aee-1a08-3c57-bae9-f8b76ce7d52a | -6.9042 | -42.8634 | 2026-07-02 13:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 75.7 |
| 8d3f7512-61aa-3ae5-a84d-feafb9954160 | -17.732 | -46.7756 | 2026-07-02 13:20:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 123.4 |
| aa49cef6-c611-35c5-b87f-0fbc73b71370 | -6.9045 | -42.8398 | 2026-07-02 13:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 83.1 |
| ee8cc5e1-5e24-3ae0-8b9b-7977561a48c4 | -6.9323 | -43.7264 | 2026-07-02 13:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 82.3 |
| 6547c875-f2e4-315e-a4f1-325f20772d5f | -10.7843 | -53.5434 | 2026-07-02 13:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 116.2 |
| 9bf48849-af2e-34d3-9525-fc1955161eed | -17.712 | -46.7798 | 2026-07-02 13:20:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 195.1 |
| 4f57c180-3396-3000-b71e-796105612656 | -6.9135 | -43.7281 | 2026-07-02 13:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 71.3 |
| 8b97dc3b-ee26-31e6-a918-3afe7b272a55 | -6.9326 | -43.7032 | 2026-07-02 13:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 77.7 |
| dd8f2c32-5433-3abf-98b5-d8bb346e4a5a | -6.9138 | -43.7049 | 2026-07-02 13:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 77.8 |
| c0e86f95-e536-3ed9-ad72-5103305e97e6 | -6.9135 | -43.7281 | 2026-07-02 13:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 84.4 |
| be4b844b-deb0-3bcf-bb84-37c726b39e21 | -10.7843 | -53.5434 | 2026-07-02 13:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 88.4 |
| 4d97af4b-dd7a-3582-9ab3-1ec3dd0c3d9b | -17.732 | -46.7756 | 2026-07-02 13:30:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 147.3 |


[Clique aqui para ver as próximas entradas](README27.md)
