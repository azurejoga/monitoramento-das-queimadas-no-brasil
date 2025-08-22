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

## Dados Diários - Página 30

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e4b0d5ec-a3e2-3619-8c4a-3be9977f92bd | -11.44692 | -47.31129 | 2025-08-22 04:19:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 53b83058-ecc5-34f2-97a4-bde2b8ecbd01 | -6.50364 | -43.42912 | 2025-08-22 04:19:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 0a63c642-c277-31d6-9154-911ff971562f | -6.04176 | -44.36283 | 2025-08-22 04:19:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 65488c95-11d6-3c41-b6af-2e4734477603 | -10.85602 | -50.81655 | 2025-08-22 04:19:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 310033ab-ba9b-33bb-a2e5-277c9dcb088e | -9.19086 | -59.64202 | 2025-08-22 04:19:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4e570ac5-7146-3552-9a03-3bfca741baba | -9.58957 | -43.32697 | 2025-08-22 04:19:00 | NOAA-20 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 6fa7a06c-edd8-3fba-b1af-1a39a918a2af | -6.25337 | -43.72867 | 2025-08-22 04:19:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5d36e578-5527-3157-a8d5-8a45ad8d6be1 | -10.85353 | -47.25492 | 2025-08-22 04:19:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 07a9c901-eef0-3859-b6a2-f21245518ba6 | -6.1763 | -44.73837 | 2025-08-22 04:19:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b4c066b3-2118-3619-aa5e-2ef5560b45bb | -9.39208 | -48.26702 | 2025-08-22 04:19:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cf4cb5e5-d32a-3347-b2a1-db4339cbcd03 | -6.06876 | -44.10436 | 2025-08-22 04:19:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e003328b-951f-38bb-a9d6-8169b9c6a61e | -4.8834 | -55.98583 | 2025-08-22 04:19:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 821e5a5b-be96-3fed-a3b2-5da08e29846d | -6.94618 | -44.55163 | 2025-08-22 04:19:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| efc87142-5646-3c5e-aec2-f4aab6a88f8c | -7.02913 | -44.62861 | 2025-08-22 04:19:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5372df55-8272-32c1-8f47-59797711e857 | -6.94274 | -44.29148 | 2025-08-22 04:19:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 1c728f2e-c9a1-39d4-8659-f013a73f8215 | -6.57983 | -44.46198 | 2025-08-22 04:19:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7bb3cf20-96ad-37c6-b90b-5c044594ae8e | -5.88116 | -53.61593 | 2025-08-22 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0b859074-a7f2-319a-89bd-b6b5be8f64c0 | -8.77289 | -46.6934 | 2025-08-22 04:19:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0e3a133c-b783-3697-b44c-525f1b2e9de6 | -6.43983 | -53.38593 | 2025-08-22 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9d0d1e37-e1b1-31c2-9aaf-996eb7b69468 | -9.64001 | -44.60572 | 2025-08-22 04:19:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0ee6deae-d8dc-36e2-98e0-6e17baff65f4 | -6.43475 | -44.52043 | 2025-08-22 04:19:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d0f1d9b8-3832-3b38-a8fb-85cfc9e4dc99 | -6.1616 | -53.76828 | 2025-08-22 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| eeb20b50-cf37-3867-8731-10844b787559 | -6.9219 | -44.38093 | 2025-08-22 04:19:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7bc64710-dcf1-3d30-9d79-6b0b15e8d692 | -10.49559 | -46.46383 | 2025-08-22 04:19:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d4a55af7-b65f-3aa8-8309-66cb2e83878f | -6.42683 | -44.67852 | 2025-08-22 04:19:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b04d8524-60ef-3562-8960-41e29af75e79 | -6.49796 | -42.97057 | 2025-08-22 04:19:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| aac16d27-baa6-3f90-bac3-01d3556157af | -6.53502 | -45.45567 | 2025-08-22 04:19:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f9ea37be-475b-3fa6-9e9d-f5b9121bb62c | -6.16872 | -42.71987 | 2025-08-22 04:19:00 | NOAA-20 | ANGICAL DO PIAUÍ | PIAUÍ | Brasil | 2200608 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| c3e0f4f1-5e14-31b6-8464-d0e7c928ec77 | -6.26415 | -53.67704 | 2025-08-22 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e9792533-c30f-3097-bbd6-f098e94cc96d | -6.26443 | -53.67587 | 2025-08-22 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b0be4b04-5c80-3b3a-b915-42d15b04a51e | -7.71497 | -47.33174 | 2025-08-22 04:19:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cc259dc1-f95c-3a76-8c64-d1f332d8f017 | -10.72921 | -48.22706 | 2025-08-22 04:19:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 3598ddc5-5073-3f4e-b006-df1ccf724608 | -8.67809 | -47.98079 | 2025-08-22 04:19:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 48cb491f-d84e-349b-98a5-609355fe0665 | -11.28057 | -44.95073 | 2025-08-22 04:19:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6831dc15-167d-3b34-9768-e5ba4ec06f59 | -10.20372 | -47.55925 | 2025-08-22 04:19:00 | NOAA-20 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7062bf00-a5e1-3ac2-91e1-f970de4957c2 | -7.25176 | -44.70311 | 2025-08-22 04:19:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f47290e6-8552-37a7-8dd3-b99f1bf7bdae | -6.43805 | -44.52095 | 2025-08-22 04:19:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 88a97818-7d56-3942-8943-d3dd23c0088d | -6.53779 | -45.45967 | 2025-08-22 04:19:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 807062d5-e094-3efa-a7c1-e02218566eb5 | -10.71524 | -48.22475 | 2025-08-22 04:19:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 07e9541d-167c-3732-a035-1310b20a46f5 | -7.65455 | -46.25256 | 2025-08-22 04:19:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ff1fd321-2093-3c67-8808-98e39f3fec18 | -6.21951 | -44.13898 | 2025-08-22 04:19:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ec529759-9ffe-33c5-bb04-2a59e97a4cab | -6.44082 | -44.52494 | 2025-08-22 04:19:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a3641357-595d-3fd4-89f3-8a6a6dcb5251 | -10.96998 | -49.57335 | 2025-08-22 04:19:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 31c59959-6f26-3642-8c90-c50c4c81f9fb | -7.86836 | -46.99228 | 2025-08-22 04:19:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d13c70f2-1c5f-3d2b-881b-497250cc64b6 | -6.03242 | -44.37909 | 2025-08-22 04:19:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ea8605f9-2db5-3c43-a000-18eea027388b | -10.17703 | -47.90954 | 2025-08-22 04:19:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9a3a6a11-a2e7-3462-9e67-cba1e50e68ee | -10.73425 | -48.24001 | 2025-08-22 04:19:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 126621d1-b765-3866-85da-bce93a3f678a | -7.81437 | -46.86954 | 2025-08-22 04:19:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 576d7eb2-2ccf-3569-bd0d-a54da6b21c26 | -5.87422 | -53.62465 | 2025-08-22 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f66084bc-2189-3213-aff7-7875f5923740 | -7.94657 | -42.65806 | 2025-08-22 04:19:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 9117a03c-5b14-3e18-b57e-ea3f2049d79f | -9.59254 | -55.35715 | 2025-08-22 04:19:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a7e46b7d-24c5-3f90-ae9c-9c45d74d7fe6 | -12.5867 | -47.09198 | 2025-08-22 04:19:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c7e615a0-18f3-3115-97ea-ba736e8b7852 | -5.45872 | -46.47083 | 2025-08-22 04:19:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d5d500df-eb96-362a-88f6-7b933417259e | -6.3737 | -43.25422 | 2025-08-22 04:19:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1716065a-a98e-3f4f-88bd-c7483cb32f5a | -5.83192 | -45.98447 | 2025-08-22 04:19:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 49b720ce-ca1f-32e6-bee7-b19ba95383e7 | -6.50624 | -45.52988 | 2025-08-22 04:19:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7fb925b4-466f-3d1c-bee0-a6a3781f0fc8 | -11.30369 | -44.95057 | 2025-08-22 04:19:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0dd4a72d-25a3-3f67-845b-dd5623eba9f2 | -11.14804 | -44.70603 | 2025-08-22 04:19:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 92033242-9222-3375-a925-1f66d8a52c76 | -6.29632 | -43.88643 | 2025-08-22 04:19:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 3d8c6e8e-ada6-3293-acbd-47b9ac65b730 | -6.92908 | -44.37848 | 2025-08-22 04:19:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f1affb56-e641-3328-beb6-a362e6d71b3d | -6.49523 | -43.43888 | 2025-08-22 04:19:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 23fc8e04-aed7-352b-ad0d-fbd307bafaa9 | -10.7384 | -48.23661 | 2025-08-22 04:19:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| aa0438f1-156b-3290-b8e8-9b7bdd47e073 | -6.25315 | -44.33607 | 2025-08-22 04:19:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| be838f9f-4c66-36c7-87cb-0ebac2532fc9 | -6.81059 | -47.81439 | 2025-08-22 04:19:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5f241817-60a4-3b9f-b1e3-32c9438705bb | -6.03237 | -44.35781 | 2025-08-22 04:19:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| dc3d4709-234f-3bd8-89e6-a4c3c69ea209 | -6.44387 | -53.39292 | 2025-08-22 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 857ccafe-acf6-3a00-8e6f-55f0364e0926 | -8.5114 | -48.82349 | 2025-08-22 04:19:00 | NOAA-20 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 47db2365-1da7-3184-87fa-07e67dc3a4d0 | -9.18355 | -59.64119 | 2025-08-22 04:19:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3600a407-923e-3f96-84c3-00984de76a05 | -11.77557 | -47.56055 | 2025-08-22 04:19:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c12ecbc2-e402-30aa-bef7-8175c8fbc55a | -6.93997 | -44.28749 | 2025-08-22 04:19:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 4f6ed937-46c3-3b92-a32e-42888b66b405 | -10.73229 | -48.25192 | 2025-08-22 04:19:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| d2b09451-05df-37a0-a62b-72c7524f4116 | -7.09787 | -43.68806 | 2025-08-22 04:19:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 33c5ca89-1faa-3d4c-b235-1c1c2c7160e8 | -11.31589 | -44.93788 | 2025-08-22 04:19:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2f7b49be-38f9-39a1-871e-2ffd6c380209 | -6.43876 | -53.39198 | 2025-08-22 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ff23b317-5194-3146-b193-7b23bc223cdb | -10.26714 | -46.76228 | 2025-08-22 04:19:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b08ae939-956a-3e6e-ad9b-d448a458381a | -11.43623 | -47.31322 | 2025-08-22 04:19:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 42602882-f029-3fcb-bbd3-6edd347a38f9 | -10.28491 | -46.77981 | 2025-08-22 04:19:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7c5e12a1-3667-31ec-84e8-9de4e82c65f9 | -11.44019 | -47.31015 | 2025-08-22 04:19:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 43b2a560-fcf1-3e3b-8089-fd82818f39d3 | -12.44049 | -44.70266 | 2025-08-22 04:19:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 984bffe8-a6b2-3d9c-b540-69940271cbec | -7.24899 | -44.69912 | 2025-08-22 04:19:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4eb39082-966d-3f1e-af41-4a48c30f2433 | -6.10819 | -44.39487 | 2025-08-22 04:19:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d0ab6a7a-bc0e-3456-b9a0-951170d6abb8 | -8.51434 | -48.82849 | 2025-08-22 04:19:00 | NOAA-20 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2ea19da6-fc0e-3a01-aa2a-3705c33fa655 | -6.49588 | -43.0983 | 2025-08-22 04:19:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 65e660f6-df7e-319c-880e-69f0a5023a52 | -6.29029 | -43.70554 | 2025-08-22 04:19:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 66f65a35-a633-36a5-a5f6-7d77be0ea648 | -5.86813 | -45.6733 | 2025-08-22 04:19:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3554f8d5-9cb0-301e-b46b-c7812ca9d9af | -6.51062 | -44.5788 | 2025-08-22 04:19:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 779d306c-e3db-3fc6-9309-58b86ce8b0e7 | -9.20939 | -59.47475 | 2025-08-22 04:19:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e2821c17-ce47-3065-b209-6b790925cbf3 | -10.7358 | -48.2524 | 2025-08-22 04:19:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| aa43353f-12d0-3bb1-ab2a-3a13e85fe159 | -7.86653 | -47.00352 | 2025-08-22 04:19:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 85ef9d65-4903-3e8d-b427-06a434fad6bc | -6.2567 | -43.7292 | 2025-08-22 04:19:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e495a551-2b18-3312-b0b6-f5eb121d34d6 | -6.5741 | -42.99738 | 2025-08-22 04:19:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5ecc263f-e8d5-3b18-bb73-206a0b44404a | -6.3675 | -43.24953 | 2025-08-22 04:19:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| edbb5858-54ed-39fc-992f-1a75426509c4 | -7.09676 | -43.69519 | 2025-08-22 04:19:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| e904f522-41da-303b-8c03-45b4f789325c | -6.97219 | -44.14565 | 2025-08-22 04:19:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 64567bf1-742d-367c-94f7-c8e729f5a0de | -6.42185 | -44.66711 | 2025-08-22 04:19:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b31b1f78-8feb-3e2e-bb19-312c35839d8c | -6.07436 | -44.13363 | 2025-08-22 04:19:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0a653988-3d3c-3372-84a2-887f4f73c851 | -10.9784 | -45.6032 | 2025-08-22 04:19:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d59f149a-3937-3b06-ace5-6acd12b7c81e | -11.1302 | -44.71056 | 2025-08-22 04:19:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e13613aa-a7c6-35b9-bbe9-7eb21ba047b2 | -6.449 | -53.39384 | 2025-08-22 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 21b6a43c-f096-3388-b17d-74728fba95cf | -7.76055 | -46.54963 | 2025-08-22 04:19:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |


[Clique aqui para ver as próximas entradas](README31.md)
