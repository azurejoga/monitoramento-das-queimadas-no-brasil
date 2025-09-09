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

## Dados Diários - Página 25

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2cd023ed-c516-3580-a3a4-0f7f6695ec59 | -5.91097 | -52.46885 | 2025-09-09 04:32:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e597d3af-e1e0-37ca-b822-09401d6b38f5 | -5.86242 | -45.30865 | 2025-09-09 04:32:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0a43afc7-131e-34a1-accb-2ba341433bec | -5.43914 | -42.79903 | 2025-09-09 04:32:00 | NOAA-21 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| f32e6818-74fd-3d82-b2f1-fbc963e52afe | -6.03907 | -44.42484 | 2025-09-09 04:32:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6c0e62f0-2603-34d3-855c-8286f2c226b6 | -5.22447 | -42.94019 | 2025-09-09 04:32:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 2.4 |
| d649d175-2482-3b35-983e-0df7fb4d5687 | -5.41479 | -42.85219 | 2025-09-09 04:32:00 | NOAA-21 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 0a57cd3a-83ac-3923-946e-59b4b80ca255 | -5.8148 | -43.98066 | 2025-09-09 04:32:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 5701663c-a90d-35f9-9e42-1bf16e604d3b | -6.20647 | -41.01647 | 2025-09-09 04:32:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| b6f113e0-f7e4-32d7-b625-3c79af9532f3 | -7.07966 | -45.20499 | 2025-09-09 04:32:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 24.1 |
| dd92740b-b316-3dfe-80b6-4a5a11894a1d | -6.56258 | -43.14705 | 2025-09-09 04:32:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| cf194431-ff36-33a6-a28e-fc7dc77a482f | -5.53564 | -42.6576 | 2025-09-09 04:32:00 | NOAA-21 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 794331d8-a87c-3072-94c5-b432b05675af | -6.43444 | -44.06142 | 2025-09-09 04:32:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 3bff5812-333b-3dab-9eb6-1cd364e19cb4 | -3.39668 | -47.50219 | 2025-09-09 04:32:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a1f5876c-33cc-3164-8530-a4e3479dc092 | -5.25072 | -42.72051 | 2025-09-09 04:32:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 3124a08f-0e07-3e7d-acab-391ca3b5c680 | -6.71261 | -44.30001 | 2025-09-09 04:32:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f0b1bccd-0793-36c5-bdfe-a341ac567762 | -5.45344 | -42.79724 | 2025-09-09 04:32:00 | NOAA-21 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 0fc60e5e-520b-3ff4-87eb-03a819afeea8 | -7.02749 | -44.94868 | 2025-09-09 04:32:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a202cd08-1582-3fb5-ab84-d8525737a086 | -6.34699 | -43.79029 | 2025-09-09 04:32:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 4f7431a6-b5fb-3420-96b1-5e6a57190a29 | -5.93429 | -45.94691 | 2025-09-09 04:32:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 50a5c199-a8b8-3518-a526-8785b01e7ed5 | -6.55683 | -42.93364 | 2025-09-09 04:32:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 072012cf-03c7-3522-9834-e2343ed1022b | -5.16709 | -42.9514 | 2025-09-09 04:32:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a3fee6c5-e909-3691-a6bd-264e55e5c196 | -5.77992 | -44.84863 | 2025-09-09 04:32:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 49a020b5-b0d2-3f00-84ce-88e425427839 | -2.79284 | -49.61764 | 2025-09-09 04:32:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 00ef76ba-7fa6-35a8-a933-fd20bc7df1eb | -5.73916 | -45.40638 | 2025-09-09 04:32:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 98341fa7-b9cc-3af3-9ac1-358cec4271b7 | -3.68903 | -49.57133 | 2025-09-09 04:32:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 061503b1-a5de-33b4-9134-97e274286bd3 | -6.20475 | -45.0281 | 2025-09-09 04:32:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 62948a9a-35cd-3c2b-9498-ca27d54e01bb | -5.82111 | -43.97062 | 2025-09-09 04:32:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| fcb12902-64a0-35c4-baec-6576fd664544 | -6.33607 | -44.64073 | 2025-09-09 04:32:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d8010ce6-b69c-3fda-be4e-49c3fcc5163f | -5.36002 | -44.77642 | 2025-09-09 04:32:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| bebc0a53-c6ad-3513-b28c-e2e542fd3de2 | -5.94122 | -45.78733 | 2025-09-09 04:32:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fb535f4b-adbb-3c81-aa4e-f5426f08d9f1 | -3.94402 | -41.82838 | 2025-09-09 04:32:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 8d3750ed-714c-3f78-bc02-29cdd5b33464 | -6.3178 | -44.38571 | 2025-09-09 04:32:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 661b5fad-2b21-329c-9488-50cb70b6bf74 | -5.54893 | -45.17892 | 2025-09-09 04:32:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 7cac2f3a-60cf-31ae-b771-d4bdbab8b218 | -5.4346 | -42.80192 | 2025-09-09 04:32:00 | NOAA-21 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 37f902d0-2f61-3ea4-84a4-bd0f7d728753 | -6.64421 | -44.08337 | 2025-09-09 04:32:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| aca0644d-50b8-3374-86ee-8baa3e748447 | -5.92289 | -45.76904 | 2025-09-09 04:32:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 72e4798b-9be4-370a-8abf-d00169ba2afb | -5.85202 | -44.19996 | 2025-09-09 04:32:00 | NOAA-21 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 219b4f1d-846f-3e83-850c-f3d42f554e3c | -2.78875 | -49.62093 | 2025-09-09 04:32:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 059f41fc-8a4e-390e-a161-78ca862609a7 | -6.43001 | -44.06531 | 2025-09-09 04:32:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 4fb75b93-dbd3-3d16-8bc4-ac3948dca808 | -6.40457 | -44.43534 | 2025-09-09 04:32:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 044760e1-7ade-3dc7-857c-9c53b5156697 | -5.99355 | -46.20039 | 2025-09-09 04:32:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a4edac03-76cb-35f1-8fe5-feebd2e6da3b | -6.1023 | -44.77524 | 2025-09-09 04:32:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 89359751-6ad6-35c6-9fab-963040c66eda | -4.40791 | -48.94374 | 2025-09-09 04:32:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0615428f-c29a-3c86-9e7c-244a7d06f790 | -6.39724 | -44.43406 | 2025-09-09 04:32:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| a02355fc-098a-3a16-843c-3257d0acd0d3 | -5.97147 | -47.42111 | 2025-09-09 04:32:00 | NOAA-21 | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 97e92a6c-e482-32a1-8439-5f6a098db431 | -7.2356 | -43.98839 | 2025-09-09 04:32:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 80aacf14-b808-3873-8302-c183892ea372 | -6.81981 | -44.9596 | 2025-09-09 04:32:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 323a60b9-bbde-33dd-baf1-9a69dc297686 | -5.82266 | -44.82438 | 2025-09-09 04:32:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 125880e4-3e6c-36c2-abd3-42d5abd917af | -4.99841 | -56.25774 | 2025-09-09 04:32:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b9a80b1c-6064-3ec6-8d6e-2aa8c20fd2b6 | -4.57893 | -48.12276 | 2025-09-09 04:32:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7f2e9e63-090f-37c3-b85c-1f40c11da3ec | -6.56088 | -42.93422 | 2025-09-09 04:32:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 45563079-25ef-3537-ae70-dcf617271ae3 | -5.67586 | -43.90182 | 2025-09-09 04:32:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 775efbe4-326f-3ad6-b70c-8d5acf162c40 | -6.3269 | -44.65231 | 2025-09-09 04:32:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2b5611fd-b1d2-3165-b671-54927482fd54 | -5.70727 | -45.45277 | 2025-09-09 04:32:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 898bc6ad-fe93-3561-9827-079b4cb5cf05 | -5.08722 | -42.42177 | 2025-09-09 04:32:00 | NOAA-21 | ALTOS | PIAUÍ | Brasil | 2200400 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| a2e471aa-b422-3bf6-9fa6-d9f65cb49352 | -5.92117 | -45.75719 | 2025-09-09 04:32:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4d2f8cbd-3085-37b9-ba65-3afe4a56d96c | -5.4153 | -42.84876 | 2025-09-09 04:32:00 | NOAA-21 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| c2aa9092-ab2e-3448-9d9b-97964fa85904 | -2.63025 | -46.83323 | 2025-09-09 04:32:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 2b9c430e-a82c-3994-b2d4-f1c1bc870967 | -6.23058 | -45.58472 | 2025-09-09 04:32:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9bb0e1e6-49d6-3aad-b021-cbe97b5450bf | -6.19172 | -45.82446 | 2025-09-09 04:32:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c88bf64e-2e1b-3a1a-a83f-d639d34608eb | -5.71171 | -45.41093 | 2025-09-09 04:32:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 8bea09fb-eb6f-393f-87f6-89d257be4c85 | -5.98387 | -43.70387 | 2025-09-09 04:32:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5b1a88a2-98be-3a3d-b2b0-64a3cc7f6d1b | -6.30024 | -43.81648 | 2025-09-09 04:32:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c4512dca-21e3-3fa3-a2e8-3b87852d917a | -5.11065 | -44.6744 | 2025-09-09 04:32:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0fd6de6a-4276-3681-9f6e-94e0b1ea1399 | -5.9776 | -43.69321 | 2025-09-09 04:32:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4f96c62d-ed85-35a4-9401-1604453491f3 | -5.44577 | -43.44925 | 2025-09-09 04:32:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9d8a1164-470b-3712-8063-f0d416ec708c | -4.89018 | -42.21233 | 2025-09-09 04:32:00 | NOAA-21 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 6f2eaa47-1125-37fb-86f5-b77a0492e598 | -5.93189 | -46.17221 | 2025-09-09 04:32:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2717e4c1-88c0-34d0-9d21-6236fd13b9ca | -6.23107 | -43.52072 | 2025-09-09 04:32:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2a8baa2c-4fc4-381e-ac3a-97de2bc45f6a | -6.5679 | -47.3471 | 2025-09-09 04:32:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 570bf5f5-9adb-32c7-bbb9-1f121ea894db | -5.91945 | -45.76852 | 2025-09-09 04:32:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ba7b9b9a-b74c-3c2b-824f-ef6d86adfb07 | -5.42465 | -51.53627 | 2025-09-09 04:32:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 26a3e723-5d96-3d25-914f-2079761fcc71 | -6.44276 | -45.30062 | 2025-09-09 04:32:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 241c66df-8b4b-31df-9c4a-5abd82c4d583 | -5.45695 | -42.80138 | 2025-09-09 04:32:00 | NOAA-21 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 2d80b4ee-1400-39ec-9235-466abaf4d47d | -4.24626 | -48.26889 | 2025-09-09 04:32:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f9b71db1-1802-3cb3-b32f-4f369556abc1 | -7.04437 | -43.24678 | 2025-09-09 04:32:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| daec6daf-a82f-355e-9c2f-2739b59d22b0 | -6.23493 | -43.52143 | 2025-09-09 04:32:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f280762c-aab5-3490-97b7-b24179f68ca1 | -6.67518 | -44.55026 | 2025-09-09 04:32:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f2c968e0-cbb1-30de-9830-2e7866411338 | -5.26858 | -44.44613 | 2025-09-09 04:32:00 | NOAA-21 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 1795b9d8-8ee6-3dec-8117-040c7e6ca572 | -6.13296 | -46.32561 | 2025-09-09 04:32:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 78b87e8f-758f-3d2e-8f2f-52c02f909fcd | -5.81425 | -45.65204 | 2025-09-09 04:32:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1f19eab8-2dde-311b-9a9c-f404a3ce0ceb | -5.70865 | -45.45388 | 2025-09-09 04:32:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| bfd8b28f-9b79-30ea-8317-5285d200f0a0 | -5.69385 | -45.98251 | 2025-09-09 04:32:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4bfa13a6-54db-393b-8253-2dfb1208d1d6 | -6.23466 | -45.60499 | 2025-09-09 04:32:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5c891cc8-2946-30dc-9bab-f99502b36849 | -2.55765 | -47.71166 | 2025-09-09 04:32:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9ed20ed0-8520-327d-8681-4ecb53e90495 | -4.69956 | -42.82662 | 2025-09-09 04:32:00 | NOAA-21 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 375df94e-6973-3df3-8cde-429e68128529 | -5.16784 | -42.94632 | 2025-09-09 04:32:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e3379e0a-893d-3182-bcef-f5b15e27c589 | -5.82046 | -43.97512 | 2025-09-09 04:32:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 306606e4-ccf4-3c93-95e2-3e521fb558e8 | -6.06797 | -43.12329 | 2025-09-09 04:32:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 247d83d5-64c5-3ab7-a336-dadb286a650b | -6.5674 | -42.94624 | 2025-09-09 04:32:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b5652f4e-9aa4-38cd-b242-d39d4a822776 | -6.4314 | -44.05603 | 2025-09-09 04:32:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 0b4da914-7928-394a-82fa-09f3875002e2 | -6.57056 | -43.14818 | 2025-09-09 04:32:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6ae19413-6d9b-3704-95d6-24150e9993ca | -6.19531 | -41.02913 | 2025-09-09 04:32:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| ff7ecaac-5c6e-3fdc-84fa-7b5d317eef88 | -5.11903 | -42.7938 | 2025-09-09 04:32:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 24dbd89c-40ac-3688-8e89-26dfaa1e6bf4 | -6.30291 | -42.20407 | 2025-09-09 04:32:00 | NOAA-21 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| f280ffb5-f691-3bc2-86b9-528051d06227 | -5.17253 | -45.17362 | 2025-09-09 04:32:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8d9a4c10-92e4-3f14-b369-10068bd503da | -6.3035 | -42.20008 | 2025-09-09 04:32:00 | NOAA-21 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 61057898-b9c7-3211-9099-bc7429dcc914 | -5.32941 | -42.6992 | 2025-09-09 04:32:00 | NOAA-21 | DEMERVAL LOBÃO | PIAUÍ | Brasil | 2203305 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 4a2f4b59-d962-3f97-81e5-62d43c091f5c | -2.62972 | -46.83666 | 2025-09-09 04:32:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 5bb3bda8-ed76-3e5b-b30d-4a69bd225a95 | -5.71519 | -45.41149 | 2025-09-09 04:32:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |


[Clique aqui para ver as próximas entradas](README26.md)
