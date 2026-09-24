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

## Dados Diários - Página 42

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d95306e2-5adf-38db-a272-2a98ef9d5315 | -3.17204 | -51.36153 | 2026-09-24 04:44:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 940f9b78-851a-31dc-b3ac-529803af40e4 | -3.17599 | -48.02688 | 2026-09-24 04:44:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 85f2aa8d-061b-34cc-a460-0d9dc204b320 | -6.78055 | -48.67839 | 2026-09-24 04:44:00 | NPP-375D | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 39c5e37d-583b-3e45-991c-7523cb6edfad | -5.25201 | -49.23113 | 2026-09-24 04:44:00 | NPP-375D | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6eb7e4a4-15c5-33d7-acf2-65fd5490d9bb | -4.28662 | -48.61221 | 2026-09-24 04:44:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fb6a71cb-9226-37b0-a24b-3a43e3c2baf1 | -6.4026 | -46.20225 | 2026-09-24 04:44:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2abd46f0-fce8-3f78-85f1-9ea8a29b0b39 | -2.64373 | -54.69527 | 2026-09-24 04:44:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 17.9 |
| ec807b64-b49c-34cb-a284-bd04da63ee7a | -3.45005 | -50.08183 | 2026-09-24 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 1f17795a-7ced-3b74-a8b4-f9862a4a874d | -2.79548 | -51.36731 | 2026-09-24 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8b61ce0a-78c5-3049-b90c-6f241f25f83c | -2.29463 | -48.57785 | 2026-09-24 04:44:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fcbb0b28-beaa-3738-bfc0-ec9296b03f52 | -5.83463 | -53.86042 | 2026-09-24 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cfed766a-cb04-3644-a77d-ff4afeb45221 | -3.0646 | -43.76033 | 2026-09-24 04:44:00 | NPP-375D | MORROS | MARANHÃO | Brasil | 2107100 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| dfc6e922-62df-35c2-8e1f-339c5d4cfae3 | -2.20505 | -48.15357 | 2026-09-24 04:44:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 19097978-444e-30ee-b58a-282820226a56 | -3.16818 | -51.3609 | 2026-09-24 04:44:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4b8a2920-a8cd-39fd-8dc9-add4215ecb3f | -5.23494 | -49.29667 | 2026-09-24 04:44:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 58fb9dcd-6ed5-300f-be40-487e3ac07e64 | -3.70992 | -54.20337 | 2026-09-24 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| dac1a2d6-3edf-3122-bfcc-e8e4dd160713 | -7.54627 | -47.32539 | 2026-09-24 04:44:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 920529a5-9a98-36e7-ae2e-6bf5c10ee469 | -3.44287 | -50.08071 | 2026-09-24 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cb827c85-1aff-38bd-ab2d-627cdaca458b | -3.80997 | -58.88805 | 2026-09-24 04:44:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 48045a89-65f5-302d-8a80-c8d66cf3d81a | -7.39935 | -44.76862 | 2026-09-24 04:44:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cc0f9d8e-de73-3813-9d04-f71a370d3d8a | -7.27087 | -46.79147 | 2026-09-24 04:44:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 85fb1350-04b5-3184-91df-030cc4b99b89 | -7.46677 | -44.57177 | 2026-09-24 04:44:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c2dbd70b-e605-3e47-8c32-94a3dc3aafc5 | -4.98698 | -45.54599 | 2026-09-24 04:44:00 | NPP-375D | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7cbe8532-4c35-3215-abb4-52f8957a7a74 | -1.83443 | -55.71894 | 2026-09-24 04:44:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 2ab2b05d-5613-3096-8e82-2d3db30d6ae5 | -7.2724 | -45.53407 | 2026-09-24 04:44:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f31541fe-b7e5-3367-9d91-6bb7bf3a543e | -2.82467 | -46.70975 | 2026-09-24 04:44:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| e3ccea58-1514-3939-9b2f-98944464cadf | -2.44908 | -49.22085 | 2026-09-24 04:44:00 | NPP-375D | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 21067ffc-8e4e-3e3a-a5b2-33c1bc518ae0 | -4.27642 | -48.63256 | 2026-09-24 04:44:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 34b5f435-6dda-3714-8ad3-b8f3f76b1619 | -7.19776 | -47.45755 | 2026-09-24 04:44:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 7fc7ef4e-9e0e-3c32-914f-cb67ee62740c | -4.95465 | -45.14914 | 2026-09-24 04:44:00 | NPP-375D | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8b66ffad-c4c4-3ab7-96fe-a9e35e8699ca | -7.41924 | -47.35971 | 2026-09-24 04:44:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0002103f-9139-3721-8f7a-a20b0dc8c0ba | -1.83389 | -55.72219 | 2026-09-24 04:44:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 969943f4-10aa-3bc3-a03c-4257ebda1fb9 | -4.19978 | -47.88755 | 2026-09-24 04:44:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 6a83f7d4-7d1e-3502-9677-c137b9d56dc5 | -4.99043 | -45.54655 | 2026-09-24 04:44:00 | NPP-375D | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 76340c4c-8cd7-39f2-a592-e8ac0a10dcae | -7.49996 | -39.27261 | 2026-09-24 04:44:00 | NPP-375D | JARDIM | CEARÁ | Brasil | 2307106 | 23 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 129e1109-779d-36a6-b8dd-b2e7584a24cd | -6.43242 | -48.46811 | 2026-09-24 04:44:00 | NPP-375D | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 4.5 |
| eeedcb24-d289-34e0-9e28-692b24991d6b | -3.37194 | -50.03338 | 2026-09-24 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 64c4a98c-f334-358d-a770-cea97416ecb2 | -6.5207 | -52.82486 | 2026-09-24 04:44:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 80298caf-fb6d-3f4a-9233-424ebb7e3523 | -6.53108 | -51.50293 | 2026-09-24 04:44:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d14e6fcb-ad78-3b85-abbf-cc3de83e983c | -2.94655 | -49.19608 | 2026-09-24 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fb92e90d-4d4f-3c23-b4db-64d0ea2ef2de | -4.29805 | -49.12658 | 2026-09-24 04:44:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0d225554-ba96-3695-b40e-297ad3adeb48 | -6.97264 | -45.05058 | 2026-09-24 04:44:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2e19ef62-685f-386e-a748-18d3a685b48c | -6.09496 | -46.36416 | 2026-09-24 04:44:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0059eee3-f7a4-333b-8b94-5bcc6a1984e7 | -6.77833 | -48.67083 | 2026-09-24 04:44:00 | NPP-375D | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7636c30b-1d68-31f5-a157-837c2e3c0eac | -3.45786 | -50.07895 | 2026-09-24 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 64.9 |
| 7540755f-cb81-3819-84d1-5619dd66d03e | -4.33712 | -55.21743 | 2026-09-24 04:44:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 95e09464-145b-3dd3-ad66-448b9c6ca020 | -4.99732 | -45.5476 | 2026-09-24 04:44:00 | NPP-375D | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| a3a021fa-1db3-325a-bb68-c04df90614d9 | -3.78971 | -49.02822 | 2026-09-24 04:44:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 35bb5f68-9690-392d-ae81-4718a3b52366 | -6.12639 | -44.59798 | 2026-09-24 04:44:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 095f4846-b875-360a-8a18-9406d1b587a4 | -1.62984 | -54.91879 | 2026-09-24 04:44:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| d93502d4-ef4e-3c49-bdbe-a4422135447f | -1.62975 | -54.92358 | 2026-09-24 04:44:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b8f85eef-c99c-39e4-91d5-34fad07faf4c | -7.54572 | -47.32891 | 2026-09-24 04:44:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ec64afe3-f04d-3349-8637-058fbe8b5465 | -2.39056 | -48.52209 | 2026-09-24 04:44:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| fa31e7bc-cdd1-3064-98ab-d4f76c34c37f | -5.32992 | -48.98673 | 2026-09-24 04:44:00 | NPP-375D | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1c816690-af9b-307d-80cb-56174e6339d5 | -5.95281 | -51.79436 | 2026-09-24 04:44:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9a8b203c-b16f-326c-9220-fc43f8d0b292 | -4.472 | -54.96647 | 2026-09-24 04:44:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 43224e99-d759-32dd-922e-72d1ab20656b | -3.41306 | -50.74887 | 2026-09-24 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 679e622f-6c9d-3300-9dfe-13ecef15f582 | -6.61131 | -43.73445 | 2026-09-24 04:44:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e04e2cc3-4679-30c5-aea7-e29f3c31a91c | -4.2896 | -55.25961 | 2026-09-24 04:44:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8ae51a86-25aa-30d8-bc07-fc00f9d781a5 | -3.58541 | -50.02768 | 2026-09-24 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 97e07a33-0c0a-3f80-a5e9-7ac22e68c6a9 | -6.20751 | -47.49449 | 2026-09-24 04:44:00 | NPP-375D | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d2e8bb7f-6262-3456-8ce2-d495652cd77f | -7.03062 | -44.6499 | 2026-09-24 04:44:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| a81a0a61-c11f-3135-a075-19951583bf4b | -1.27629 | -57.04147 | 2026-09-24 04:44:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 048a7124-2419-332a-825a-be022b027146 | -7.32657 | -46.74457 | 2026-09-24 04:44:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| f927e0c0-b6d2-349d-a856-74733ae5bb03 | -7.19163 | -47.45305 | 2026-09-24 04:44:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e2a0d321-4266-372b-815b-226fb5e81304 | -1.02228 | -53.73373 | 2026-09-24 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cdfbaa84-93e7-36a3-97d5-ff870db912f9 | -7.03128 | -44.6456 | 2026-09-24 04:44:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 46a4b1d1-d1da-31fc-ba9f-88f2f935739d | -6.12795 | -43.74337 | 2026-09-24 04:44:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8fb05b86-b230-3187-972a-bb15d564c1db | -5.72117 | -49.82764 | 2026-09-24 04:44:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 28f5db52-0d25-312a-ac3b-18000498fc46 | -3.79091 | -52.42237 | 2026-09-24 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 875ba41a-fc26-34c3-944e-78e16437a7cb | -6.57115 | -51.49154 | 2026-09-24 04:44:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f4cb2466-1cf1-3bba-b8c9-4df77aaf25d1 | -2.89426 | -54.09872 | 2026-09-24 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| cf5b5acd-70cf-3015-9adf-564c140678a2 | -6.42603 | -43.4817 | 2026-09-24 04:44:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| af5ac16e-fbc3-3431-9f86-caf4e200fe22 | -7.67329 | -45.47913 | 2026-09-24 04:44:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 27a518b2-fd9a-3206-b805-8bec3b025bbc | -6.64795 | -43.62287 | 2026-09-24 04:44:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ed2d6bf4-4138-3137-8f48-b85bec02f54b | -4.53071 | -44.03157 | 2026-09-24 04:44:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 64dd3cd8-a6d9-35d8-923e-fcf125d320aa | -1.8297 | -55.71476 | 2026-09-24 04:44:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| aea7dcc8-5b8b-38f0-8280-019ea95c8e8b | -3.16293 | -54.6058 | 2026-09-24 04:44:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6062e260-f109-3ac1-83a1-bde061be222c | -7.6762 | -45.48374 | 2026-09-24 04:44:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 74d03732-46cd-393d-af11-2215fab438b9 | -3.42059 | -53.9998 | 2026-09-24 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b286d89e-6c11-3618-b51f-36e1d1138651 | -3.15336 | -54.60415 | 2026-09-24 04:44:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| b3b126a8-bab1-3c4e-8027-b124a1f0b0af | -3.68227 | -60.5582 | 2026-09-24 04:44:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| dd2f5bfc-a17e-338b-9706-7099c7fb36d3 | -6.004 | -44.10768 | 2026-09-24 04:44:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a2be5502-7635-3001-a24e-f9493036c6c2 | -5.84247 | -49.87765 | 2026-09-24 04:44:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8f4a73ae-0414-3143-9e33-86d1dc0f0e63 | -7.61387 | -46.80357 | 2026-09-24 04:44:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 47c91f4b-06d3-34fe-a20e-28dd96873a3b | -5.60412 | -45.95357 | 2026-09-24 04:44:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fb8ced1e-f14b-38a9-ae1a-31ed57154d5b | -7.67557 | -45.48779 | 2026-09-24 04:44:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 088a13a0-4c77-32ae-b712-512550e94a66 | -3.71534 | -54.19932 | 2026-09-24 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 889b9ba7-b18d-381b-b4f2-8fd621e7d753 | -3.17934 | -48.0274 | 2026-09-24 04:44:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| b71e8ecd-e454-37dc-8c66-6b689bbb0ae2 | -5.29549 | -49.28692 | 2026-09-24 04:44:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 108ff3c2-2035-36bc-abf4-88ac909695f9 | -5.29726 | -49.27597 | 2026-09-24 04:44:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7665dce4-5766-3974-a945-652c4713a0b3 | -4.30087 | -49.13082 | 2026-09-24 04:44:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d7fda3c8-c4ce-309f-9da0-f2d46ecd3ff9 | -2.38715 | -48.52155 | 2026-09-24 04:44:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dba94346-aba9-3c73-929b-db813c9da70d | -1.15534 | -47.63404 | 2026-09-24 04:44:00 | NPP-375D | IGARAPÉ-AÇU | PARÁ | Brasil | 1503200 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 14c914f9-eebf-3513-8e46-9c247af23343 | -3.55498 | -43.46546 | 2026-09-24 04:44:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| fa0811a8-d620-328a-a2af-7b2e3c376775 | -3.67763 | -60.58428 | 2026-09-24 04:44:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| bab65996-eeaa-39a7-bfa8-979c4c237603 | -6.05216 | -53.28952 | 2026-09-24 04:44:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9528f53b-ddf0-3ae6-ba65-cb60cca4cf2f | -1.62565 | -54.91697 | 2026-09-24 04:44:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2a6bd789-2fb5-3a2c-8224-dccdd21bf70f | -3.18047 | -48.02037 | 2026-09-24 04:44:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 592f1ffb-f55c-3ed4-bddb-f6bbdf46a5cf | -1.60178 | -49.82013 | 2026-09-24 04:44:00 | NPP-375D | CURRALINHO | PARÁ | Brasil | 1502806 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README43.md)
