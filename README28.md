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

## Dados Diários - Página 28

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9befd983-cdea-3108-83ea-8e5ba56e00d8 | -11.16593 | -54.01283 | 2026-08-21 04:02:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 13.4 |
| b9d3e444-8e1c-3c23-a0a3-f99776111900 | -14.46061 | -45.62742 | 2026-08-21 04:02:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 683cf911-5d3a-3d3e-923d-8acb58e135f2 | -12.71609 | -44.49158 | 2026-08-21 04:02:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 46ec18e2-f88e-376b-b01e-7c8b08fb0d19 | -12.79961 | -48.42154 | 2026-08-21 04:02:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b788f199-8bd8-36ae-ae25-6587d3584174 | -13.39799 | -54.37846 | 2026-08-21 04:02:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 5653295f-2a9a-397b-a219-d64fbd91956d | -13.44797 | -51.77752 | 2026-08-21 04:02:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9c6ffcc3-94ba-353c-a115-0d2a21cad6b7 | -13.74803 | -51.86317 | 2026-08-21 04:02:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2e2cc248-5136-322a-8cd9-c57bb204123c | -11.1746 | -54.00732 | 2026-08-21 04:02:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 55acdde7-c0d1-33cc-b8d1-f16615e7cf5f | -10.28821 | -48.2198 | 2026-08-21 04:02:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 16f02806-9513-3010-8446-af04ce6f141f | -10.82604 | -51.00102 | 2026-08-21 04:02:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 5148c228-867a-389f-8b8e-fdd7acd62e09 | -10.89723 | -50.27777 | 2026-08-21 04:02:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 06e3139e-b7b3-3405-ab26-7f714d44a74b | -11.66044 | -48.35482 | 2026-08-21 04:02:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 84fc87ec-af69-3ed5-abf5-911a7e6ffd46 | -12.26689 | -43.16022 | 2026-08-21 04:02:00 | NOAA-20 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 7.6 |
| 7e8ff502-1bb9-39f1-a820-8cb6858efd76 | -10.75847 | -50.31262 | 2026-08-21 04:02:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| dbb67477-cee4-3e34-83e1-ff33ddc2ed53 | -13.73549 | -51.86206 | 2026-08-21 04:02:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3e6169ae-e873-3f7b-9232-4616ea52b6d3 | -13.39623 | -54.36996 | 2026-08-21 04:02:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 12d56c1e-1fb6-3fe4-8704-559c834e1c7b | -8.15802 | -46.73451 | 2026-08-21 04:02:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 77d3a96e-d124-3de4-b1ac-745d4a14582b | -12.78858 | -48.39762 | 2026-08-21 04:02:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 611c2865-2d03-3626-8023-b02b365973ad | -12.74402 | -48.46865 | 2026-08-21 04:02:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 77834043-8775-3ae3-8882-b91c8aeda43c | -12.83496 | -48.45267 | 2026-08-21 04:02:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e86042c5-6065-33ad-8506-bd518deccdea | -12.80971 | -48.42257 | 2026-08-21 04:02:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 635b1271-7774-3381-8ece-a4655fe89ffa | -11.99757 | -53.43111 | 2026-08-21 04:02:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 4d50b19a-276b-372d-8771-9b4f6049dca7 | -10.29733 | -48.22802 | 2026-08-21 04:02:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8b680f97-d598-3181-a1fc-afb772f557e7 | -7.72451 | -46.15662 | 2026-08-21 04:02:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4e2c51a6-7e67-3cbf-b8f9-ec8aef69e8bd | -9.26666 | -45.64395 | 2026-08-21 04:02:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9e1c4802-5d3d-3f77-8066-1bb538b92f62 | -12.73771 | -48.4475 | 2026-08-21 04:02:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d92d71a5-2932-3e8f-ae34-39e616ffae2c | -12.26176 | -43.16838 | 2026-08-21 04:02:00 | NOAA-20 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 7275c832-6d67-33e0-95f2-2336710b8daf | -11.48926 | -45.11436 | 2026-08-21 04:02:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0ffe5acc-8f5c-314d-9d73-b0968b26253b | -12.79601 | -48.41353 | 2026-08-21 04:02:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a9baaf5d-6728-3db9-bee0-e1fc41f46814 | -11.35542 | -46.00613 | 2026-08-21 04:02:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7dc1b09e-05b2-3ce9-9c5f-620a62e25a99 | -14.4552 | -45.61133 | 2026-08-21 04:02:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| eff1d3ee-a176-3ee2-95f2-5017d5debe26 | -12.86059 | -48.427 | 2026-08-21 04:02:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a98afef7-d53c-3374-8420-82898a235248 | -8.71657 | -49.62094 | 2026-08-21 04:02:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a883b13a-08c9-3066-902d-ad2ef173ea61 | -12.79631 | -48.41137 | 2026-08-21 04:02:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a2fbce03-fcfa-31f9-b9ad-ebc7b0e0b878 | -12.83123 | -48.44523 | 2026-08-21 04:02:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| fe5abd84-db92-3887-a60b-7425fd512092 | -12.14498 | -44.98162 | 2026-08-21 04:02:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4824456f-0841-3d2c-be65-062cbe09cf1a | -10.76595 | -50.30536 | 2026-08-21 04:02:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e553ed9f-178d-3eac-bb72-24afd4b8a95a | -10.76512 | -50.30959 | 2026-08-21 04:02:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 14777b17-fb35-38aa-9ee2-5662a34121ec | -13.64088 | -51.7659 | 2026-08-21 04:02:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| e6bb5a82-f6ae-30a3-9e60-fb035337bcd9 | -10.35882 | -48.24116 | 2026-08-21 04:02:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 57ace599-0523-3874-a818-5ae8fab17b96 | -12.7591 | -48.47131 | 2026-08-21 04:02:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8eacf987-0fff-39f2-b9e9-4c0ce175cd82 | -12.80463 | -48.42235 | 2026-08-21 04:02:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| e6229295-fc66-3179-92dd-cbd6aa5c3cb9 | -13.45416 | -51.77829 | 2026-08-21 04:02:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9672b945-84b1-339c-bf3f-f300f71d4a2d | -13.25657 | -51.62591 | 2026-08-21 04:02:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| b6d69580-1c99-35e2-8e52-fc7184e73148 | -11.4851 | -45.0904 | 2026-08-21 04:02:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 20253d55-ce35-378d-8537-c3a4f26d8cf8 | -11.19757 | -54.00502 | 2026-08-21 04:02:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ee7d78d3-21fe-3e9b-8f80-5ea0190993b0 | -10.33419 | -40.62077 | 2026-08-21 04:02:00 | NOAA-20 | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 85ebf754-fcbb-3d59-ad89-7e9b63927505 | -9.85952 | -37.35183 | 2026-08-21 04:02:00 | NOAA-20 | PORTO DA FOLHA | SERGIPE | Brasil | 2805604 | 28 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 3a7c85ea-83c8-3ecf-a58c-d8e64ed21f53 | -10.36026 | -48.24203 | 2026-08-21 04:02:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b62199ab-4d88-37ef-a5cc-03ba9e04f7ca | -13.09921 | -51.59031 | 2026-08-21 04:02:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 28cecd7c-f423-33c7-9e6e-dbbceab4f142 | -13.43805 | -51.79509 | 2026-08-21 04:02:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7330cbf0-de33-32cf-8edf-97b890bd88fa | -12.74278 | -48.44806 | 2026-08-21 04:02:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a36ab7c5-b3eb-3b10-9cc2-125138854eb8 | -11.48584 | -45.1099 | 2026-08-21 04:02:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 682bc6a6-4473-3376-8086-df02fd73a750 | -12.43658 | -43.39582 | 2026-08-21 04:02:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 223a1827-855e-3a8b-95bd-a7f58bacf454 | -7.45146 | -47.16704 | 2026-08-21 04:02:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1f39a567-0e46-3ecf-8e88-d02bd966662b | -12.8558 | -48.42502 | 2026-08-21 04:02:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| dfb454bc-508c-3cfb-a79b-aa47e4782b90 | -10.7485 | -50.33261 | 2026-08-21 04:02:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| dda0d47e-32b6-3a51-ba88-1638d7fa21df | -10.74978 | -44.35349 | 2026-08-21 04:02:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cb8e392b-3432-3877-8865-4de7288c1b6e | -13.43744 | -51.79817 | 2026-08-21 04:02:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e11c31e9-0643-3dd5-9c96-cb4376bb84d3 | -12.72124 | -48.47915 | 2026-08-21 04:02:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 77ed713a-2c29-36bc-8c8b-7e7efc13e392 | -11.20468 | -54.00682 | 2026-08-21 04:02:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 62e16cac-4a13-3398-9a92-2279ff1ea659 | -10.66003 | -49.02634 | 2026-08-21 04:02:00 | NOAA-20 | NOVA ROSALÂNDIA | TOCANTINS | Brasil | 1715002 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0d7c215a-aaa6-3b32-9d4e-0459e7a1b476 | -10.52693 | -50.78317 | 2026-08-21 04:02:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| dc4bd908-ba8f-337c-bbc4-21cde9708d10 | -13.66605 | -51.7997 | 2026-08-21 04:02:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 39be049e-c776-3d03-92a7-db7ef0aecb63 | -12.50195 | -47.8455 | 2026-08-21 04:02:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| c09a025f-c988-3639-a76e-c6403c9742fc | -10.52191 | -50.77693 | 2026-08-21 04:02:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 978fcbc0-45ea-39cd-aa26-5a08053ad369 | -13.66507 | -51.80434 | 2026-08-21 04:02:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 037d7404-c375-377d-9953-227450a89822 | -12.84766 | -48.44046 | 2026-08-21 04:02:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6f500b38-ac6a-3060-b727-f919f50a3c51 | -14.90379 | -44.80266 | 2026-08-21 04:02:00 | NOAA-20 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d8a1bec7-9553-312d-8d23-4c635dbc2e27 | -9.44149 | -51.64164 | 2026-08-21 04:02:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4af076b5-f558-330d-a913-f4dbbc764f56 | -12.84879 | -48.43461 | 2026-08-21 04:02:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 93247051-90bf-34f4-843d-2cffcc2e5726 | -10.74183 | -50.33566 | 2026-08-21 04:02:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4aadec0f-9f23-3433-91d7-312ff2958c60 | -12.00352 | -53.43708 | 2026-08-21 04:02:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| fc94d029-02ae-3c6c-b9b1-33ef8df367ba | -10.30173 | -48.23303 | 2026-08-21 04:02:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2d87d22a-f301-3956-8cd5-e0110ee4986e | -12.80192 | -48.40977 | 2026-08-21 04:02:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| f1ee5d42-1895-33d4-8c14-fdd83dfb636d | -10.73214 | -44.78585 | 2026-08-21 04:02:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 7d8c6117-f2f2-3ea3-b881-4fd9086d49c6 | -13.39843 | -54.39317 | 2026-08-21 04:02:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 908bfd0d-5c7f-3780-aef4-7fb7784fdc06 | -11.6655 | -48.35582 | 2026-08-21 04:02:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 48ea149a-0aaa-36c8-8c03-32a4025ed5a4 | -11.00857 | -45.21752 | 2026-08-21 04:02:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 90c4dfe3-7c28-39c2-ae86-6c9a4c4c1fa1 | -14.45659 | -45.62663 | 2026-08-21 04:02:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 66ef438b-ca8c-3c8f-834e-56c66bfb9d73 | -12.80104 | -48.41375 | 2026-08-21 04:02:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| f143bb81-bda2-3cd3-8fc7-30fb46e2663d | -11.32311 | -45.01538 | 2026-08-21 04:02:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 41514a06-4e2d-3421-a2e7-8a0025c83a32 | -12.85387 | -48.43506 | 2026-08-21 04:02:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 37c3fe9f-c060-3eac-8865-ea42fc80ab28 | -11.62895 | -46.55096 | 2026-08-21 04:02:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 86606c2f-4e74-3311-afd3-5b5f78df621e | -14.71967 | -47.14538 | 2026-08-21 04:02:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2cfa6e0f-afa5-387b-bde6-217fa61d7d80 | -13.25569 | -51.63028 | 2026-08-21 04:02:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 7cf4ca9e-354f-3d60-a3aa-fef678a6647a | -11.48651 | -45.10613 | 2026-08-21 04:02:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0ad381b5-f015-384d-be75-ee400024e2a1 | -11.3238 | -45.01146 | 2026-08-21 04:02:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2646c1d6-c05e-3486-8935-6873bfa3c708 | -9.27027 | -45.64931 | 2026-08-21 04:02:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4ff1095d-7ecb-359d-9823-2daab8beeb67 | -11.1726 | -54.00779 | 2026-08-21 04:02:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 959cce6d-d4ba-3a58-be2e-d29c0480fa47 | -11.66608 | -48.35281 | 2026-08-21 04:02:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7d6dcb28-666e-30d1-9230-f0423e54add7 | -8.10578 | -50.03551 | 2026-08-21 04:02:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 5c9d3fdd-14aa-35f6-882d-1c508372d612 | -11.87513 | -40.96654 | 2026-08-21 04:02:00 | NOAA-20 | TAPIRAMUTÁ | BAHIA | Brasil | 2931301 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 4d274818-197d-3a1f-9125-6cf639370c24 | -10.81903 | -51.00446 | 2026-08-21 04:02:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 6.9 |
| ffb3aa9f-61eb-3e55-a292-8c29644ab480 | -13.67361 | -48.7672 | 2026-08-21 04:02:00 | NOAA-20 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7cfa2b9e-4f0c-3181-8196-2db8fb47fb8d | -12.00442 | -53.43262 | 2026-08-21 04:02:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| ccecda09-dc9e-3602-a999-1b9df87a1b5f | -15.44125 | -41.38425 | 2026-08-21 04:02:00 | NOAA-20 | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| 7f4c0598-569d-3a8c-84e5-ed790c3c3535 | -8.69064 | -47.49308 | 2026-08-21 04:02:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fabf1492-99ed-3d8c-81dd-0c91b7975e98 | -10.77259 | -50.30233 | 2026-08-21 04:02:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a53b26ef-589e-356f-9b27-49862287c1c6 | -14.72052 | -47.14088 | 2026-08-21 04:02:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |


[Clique aqui para ver as próximas entradas](README29.md)
