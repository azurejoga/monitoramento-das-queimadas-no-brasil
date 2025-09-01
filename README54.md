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

## Dados Diários - Página 54

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bdc9a758-7a5e-3475-a52c-e5b0cbc36918 | -8.85687 | -47.22018 | 2025-09-01 04:32:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ea23e284-3f76-3811-8e35-fc1bc7f256fb | -7.84446 | -46.95732 | 2025-09-01 04:32:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ea21fc17-cd7d-3610-b12e-6da0a0ed8d11 | -6.19615 | -43.33564 | 2025-09-01 04:32:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9c0208e2-0d65-3853-98b4-76fcdb3551ff | -10.04075 | -48.11643 | 2025-09-01 04:32:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5c66504d-10fe-3704-a263-890b1d30d415 | -5.7331 | -45.54529 | 2025-09-01 04:32:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 823477db-7454-3488-b6fc-74c6e2d3e1ba | -6.74528 | -43.78858 | 2025-09-01 04:32:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 15c81c4c-b39d-32cc-902e-50b06bb3e0b8 | -9.64493 | -47.82297 | 2025-09-01 04:32:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3716c3af-f1bb-3a55-856c-1795f0704e6f | -5.35911 | -41.15273 | 2025-09-01 04:32:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 66368de4-2507-3bfa-88f1-829925cee08e | -7.94047 | -46.4439 | 2025-09-01 04:32:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 90c5a80e-7de2-3eb3-9644-8a8bc40f3dc9 | -9.67321 | -47.81658 | 2025-09-01 04:32:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9145e91c-45db-3319-a600-2f1148a743df | -7.08828 | -44.33774 | 2025-09-01 04:32:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 29.9 |
| f1cecc2a-e1ce-3943-b9e4-a7d6880c6dc4 | -8.05825 | -52.35791 | 2025-09-01 04:32:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c6c65d50-4958-357b-b7b4-b0acb284e125 | -6.30426 | -43.63316 | 2025-09-01 04:32:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e694c63f-5f74-340b-b6bf-71f281dae644 | -9.15576 | -47.93721 | 2025-09-01 04:32:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d2e04138-fd0a-33af-96f7-7ae8f1539a30 | -9.63423 | -46.60508 | 2025-09-01 04:32:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 40fb33f0-6de8-30ce-a2b1-5bb169563237 | -7.06526 | -44.33907 | 2025-09-01 04:32:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 105f4f22-71d2-3dc4-8889-b8ae3f851134 | -8.82922 | -47.80987 | 2025-09-01 04:32:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c90118f1-b3c5-362e-9b78-75384c818fd6 | -6.28802 | -43.30885 | 2025-09-01 04:32:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 39b8a2d3-6fe9-3da4-80df-6c012a729ce1 | -6.20019 | -45.37825 | 2025-09-01 04:32:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 7fa34579-320c-3c46-90cd-3347a4964cea | -7.91569 | -44.94805 | 2025-09-01 04:32:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ccf90a02-e5a8-352c-9532-5ca90b80cf17 | -6.82363 | -52.83056 | 2025-09-01 04:32:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4c8048a8-3706-35e7-8f63-fee5af2be3aa | -9.63945 | -47.81856 | 2025-09-01 04:32:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 75cd1bec-5469-32e9-b575-440f1941c4fa | -6.63773 | -44.25074 | 2025-09-01 04:32:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 16d47589-958b-3e6e-a2ac-eb8f0db7f5db | -4.73292 | -44.44871 | 2025-09-01 04:32:00 | NOAA-20 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1dbd0854-65eb-3bd6-859e-20f03c8c410c | -9.6608 | -48.35395 | 2025-09-01 04:32:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 595eca83-fb6b-3f99-9e5e-a98453eb5427 | -7.11096 | -44.31356 | 2025-09-01 04:32:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| d7f9428d-a17e-3ed1-9305-ab57a7e4faf4 | -6.33582 | -53.43352 | 2025-09-01 04:32:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e3853890-ac29-36dc-ac97-bb44372df138 | -5.99975 | -43.36354 | 2025-09-01 04:32:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 2e2e7180-599b-36ae-90d8-0312b6fd72d8 | -6.95643 | -44.3422 | 2025-09-01 04:32:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cb8bb23a-a7e6-3dd4-abc0-7d234e6f026e | -9.14416 | -47.94614 | 2025-09-01 04:32:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| adb66e42-8cff-3112-827a-6c21169ac68f | -8.06222 | -48.41285 | 2025-09-01 04:32:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 517128cc-9561-3055-95a2-3e4be8a85aa0 | -7.67908 | -61.08678 | 2025-09-01 04:32:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| d62c7f2c-0bff-309d-ba6f-65f8bf759d81 | -9.14361 | -47.94965 | 2025-09-01 04:32:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 30382c31-e2c4-3f54-b757-2527b0811ae6 | -6.15623 | -43.33374 | 2025-09-01 04:32:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5180b366-b791-3f09-80f7-87cd56faabb9 | -8.85093 | -49.56054 | 2025-09-01 04:32:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1b3ac1dd-a83f-302c-b0a8-3882b31b4027 | -8.8254 | -47.83439 | 2025-09-01 04:32:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 603257d7-9fa1-3b00-92a3-cc989b23aefc | -6.14876 | -44.12812 | 2025-09-01 04:32:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cb0b44c9-d5e3-3441-98f7-196d496e0fe5 | -9.5028 | -48.86113 | 2025-09-01 04:32:00 | NOAA-20 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 46e09156-19f8-33e5-9b3d-ffd55258d2b8 | -5.658 | -43.66489 | 2025-09-01 04:32:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 419de804-4780-3be9-9081-fd0e44a47685 | -6.93221 | -42.02058 | 2025-09-01 04:32:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 67f78079-d6a2-3432-822f-f4518815bf37 | -6.08974 | -43.18869 | 2025-09-01 04:32:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 11326753-6ce9-3791-a4ac-5be1507be449 | -5.75133 | -43.68595 | 2025-09-01 04:32:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8cf5b433-26e4-3709-b7f0-c3efae5e3d42 | -3.22021 | -46.83043 | 2025-09-01 04:32:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6ce40390-beb6-35ec-bf13-8aaf1515b273 | -5.56358 | -47.41421 | 2025-09-01 04:32:00 | NOAA-20 | DAVINÓPOLIS | MARANHÃO | Brasil | 2103752 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4cc93de2-f1db-3fc7-a3fa-33bea0ba137d | -5.85323 | -43.21581 | 2025-09-01 04:32:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2806e812-f4f3-3981-be31-eeab7ed0f9ac | -9.66783 | -47.05476 | 2025-09-01 04:32:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e2307716-6e76-3ff3-9603-188f466e6adc | -10.04516 | -48.10993 | 2025-09-01 04:32:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 240c259c-a546-3ae4-8811-6dec73692a22 | -6.19224 | -43.33506 | 2025-09-01 04:32:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| bf2b1c28-346d-3055-aed9-d3038edea687 | -6.29348 | -43.6264 | 2025-09-01 04:32:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 73991091-1d26-3b79-8cc3-82e5d20d85a2 | -6.74457 | -43.79327 | 2025-09-01 04:32:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 3e20e4ac-c10a-3c7d-b173-27451358320f | -5.8513 | -42.53485 | 2025-09-01 04:32:00 | NOAA-20 | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 3b5b8144-bfda-316a-bc69-38b723d0cf4e | -10.04184 | -48.10941 | 2025-09-01 04:32:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7ccaf74c-b150-3bc6-ace5-056bc9a7b0b0 | -9.64215 | -47.81889 | 2025-09-01 04:32:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c8c522fd-d4f8-32d4-8440-1b6dcbce48de | -6.44667 | -43.94953 | 2025-09-01 04:32:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 5340d1f2-ec44-3c88-be19-2bbf06765f19 | -6.35044 | -55.56271 | 2025-09-01 04:32:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 84be3b73-71b6-3fa1-b6de-a1fb79e1d602 | -6.80762 | -45.6844 | 2025-09-01 04:32:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 61843054-5cc9-3551-9b32-928d63deaf3f | -8.86369 | -47.95898 | 2025-09-01 04:32:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4ade35a3-824a-3ee8-aa91-5986a66b5038 | -6.46031 | -43.96166 | 2025-09-01 04:32:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| e64e6105-a6c6-3b86-a192-1212c3a2413d | -6.77625 | -44.62438 | 2025-09-01 04:32:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| cc3a9774-13e4-38e5-ad75-8c2b4e5b4e95 | -5.97883 | -42.57158 | 2025-09-01 04:32:00 | NOAA-20 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| f30d3ea7-a424-3736-a5d5-a1da8d7f2e73 | -5.80363 | -42.54659 | 2025-09-01 04:32:00 | NOAA-20 | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 1a54b1b9-3abd-3eec-98e2-57a3a2f1322c | -6.19546 | -43.99682 | 2025-09-01 04:32:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1d4b1427-1aec-331e-b16c-3d6cee46ef69 | -6.29647 | -43.79017 | 2025-09-01 04:32:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 645dea0c-90a1-3519-a049-baa42d3d9545 | -7.57046 | -45.21028 | 2025-09-01 04:32:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9f1d74b8-3b32-3c2b-ac00-16e32a78a656 | -6.55096 | -44.07963 | 2025-09-01 04:32:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a229f1e5-fc6c-3a41-9591-caf8675453cc | -6.8214 | -52.81949 | 2025-09-01 04:32:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 7be9ce2f-1124-33b9-a360-534429709002 | -5.3528 | -49.04194 | 2025-09-01 04:32:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 35f3d186-f17a-3605-b5c1-21b493fb3671 | -6.81658 | -52.82388 | 2025-09-01 04:32:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 54e7b8fe-1336-3f53-bbf7-3f7f6a2c69ae | -4.9806 | -45.15295 | 2025-09-01 04:32:00 | NOAA-20 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cfa63eb8-5188-3532-b09f-7d3280302417 | -6.53718 | -44.59756 | 2025-09-01 04:32:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 267a03a9-83f3-3d4b-883d-c688c346ef87 | -7.08257 | -44.35051 | 2025-09-01 04:32:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 3d050a5d-e94e-3252-a84b-c4d843fc7b0a | -7.70438 | -50.27201 | 2025-09-01 04:32:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f2ff6c40-b683-3f4d-966d-c4d616690396 | -9.63823 | -46.60183 | 2025-09-01 04:32:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8e53d691-7b49-349a-9af3-7bd3b1838e74 | -3.22388 | -49.48191 | 2025-09-01 04:32:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a12d1453-3c7d-38c1-b322-400afb50a70b | -7.50085 | -45.83922 | 2025-09-01 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f37e0716-26d4-360a-b2e1-475043c33f70 | -6.79759 | -52.81546 | 2025-09-01 04:32:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| a24ae985-22be-36bb-a4a8-d60311de13a0 | -7.09201 | -44.33824 | 2025-09-01 04:32:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 29.9 |
| fa0fda04-be94-3e64-8c16-615342968cac | -9.14029 | -47.94912 | 2025-09-01 04:32:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cf87f5d2-77e7-33c7-b7cd-fada37948cb2 | -8.8193 | -47.82984 | 2025-09-01 04:32:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 45c5e69c-9b66-3fee-b47e-2ee38a72be75 | -6.84691 | -52.81325 | 2025-09-01 04:32:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| f06d4157-ebfe-30f1-a4db-a886cf62f385 | -8.00057 | -44.05238 | 2025-09-01 04:32:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1ef46239-878b-3e5e-baf0-df72756887d9 | -6.19061 | -43.34383 | 2025-09-01 04:32:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 243004a1-c931-3aa5-9714-028bb253325a | -9.6671 | -47.81199 | 2025-09-01 04:32:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cb8473d2-9c27-3ff7-8fb9-5ba11240e0b3 | -9.15631 | -47.93369 | 2025-09-01 04:32:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 291c3bc0-3b47-3df2-b169-addcd142b574 | -9.27421 | -47.08463 | 2025-09-01 04:32:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b1f758f1-3bc3-321e-953f-dd22787905f8 | -9.1381 | -47.96314 | 2025-09-01 04:32:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6fcbe607-bc21-357d-969c-14a907b0cfdf | -8.83462 | -47.51132 | 2025-09-01 04:32:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3d1d6e80-af11-3272-a372-68d40eee8910 | -9.5791 | -46.00503 | 2025-09-01 04:32:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| def0a891-9a70-338c-afdc-86bd5fa97e21 | -10.27519 | -49.04643 | 2025-09-01 04:32:00 | NOAA-20 | CHAPADA DE AREIA | TOCANTINS | Brasil | 1704600 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0c8ec0c1-de0a-316e-9acd-3311b1fc4bd8 | -7.08695 | -44.34663 | 2025-09-01 04:32:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 37.9 |
| 6dc8e6ff-32ae-3e79-9b7a-e7d5b7a7a231 | -9.66389 | -47.0579 | 2025-09-01 04:32:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1fc98144-84e9-36d7-8cdf-0f2c0316937e | -6.18341 | -43.31232 | 2025-09-01 04:32:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 765149c4-5c61-3259-bc4f-3dd6887ff357 | -8.19805 | -46.7758 | 2025-09-01 04:32:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 20.1 |
| 1ca65b76-60ac-3d52-aecd-5d74e24b07b3 | -10.88828 | -45.80168 | 2025-09-01 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6d76ead5-c5bd-3b29-b747-dc5b047d52d8 | -6.3304 | -53.44046 | 2025-09-01 04:32:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 224a230f-c877-3820-8406-fe535471189f | -8.82455 | -47.48801 | 2025-09-01 04:32:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d13260e7-646e-3fad-96d9-2138e3e2cd84 | -7.94902 | -46.45646 | 2025-09-01 04:32:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 27aa5969-8655-3053-bdbb-0dbacabf29a6 | -6.75745 | -43.78566 | 2025-09-01 04:32:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 26.3 |
| 706e003d-358e-3b24-85c5-171fc79ce3f3 | -9.15357 | -47.95123 | 2025-09-01 04:32:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4335a12c-345a-3f67-bff3-b5368736dc7d | -11.02893 | -45.14074 | 2025-09-01 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |


[Clique aqui para ver as próximas entradas](README55.md)
