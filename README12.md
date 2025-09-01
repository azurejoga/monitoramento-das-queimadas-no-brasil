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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 55999491-c6d4-314e-895a-002441ced91c | -6.15809 | -43.32705 | 2025-09-01 03:42:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8bd3cb2c-b215-339f-9c1e-3030cbd862b6 | -6.4558 | -43.96233 | 2025-09-01 03:42:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| d5788fa6-4a58-3590-91b8-bc4a69cdbd0c | -4.64647 | -41.39281 | 2025-09-01 03:42:00 | NOAA-21 | MILTON BRANDÃO | PIAUÍ | Brasil | 2206357 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 8aeadec6-3fc1-33e4-810f-1d4fda5f4639 | -6.29883 | -43.55364 | 2025-09-01 03:42:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a9320417-d045-3c94-9803-7c6eb499a5d7 | -6.57052 | -43.71073 | 2025-09-01 03:42:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 483878d5-e012-366c-94dd-b1a5383672e1 | -4.92534 | -43.18203 | 2025-09-01 03:42:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| fb931420-8f8c-33dc-ac2d-b6cde30c97bf | -5.56949 | -47.4135 | 2025-09-01 03:42:00 | NOAA-21 | DAVINÓPOLIS | MARANHÃO | Brasil | 2103752 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 04a2aa66-df84-3bba-93e7-03de9df3dddd | -6.30325 | -43.61868 | 2025-09-01 03:42:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| edd3afd4-5ac2-33d8-a47e-95b83f8c0f28 | -7.28605 | -43.689 | 2025-09-01 03:42:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 59115c4b-2dcc-393a-8abe-e580867c40fb | -6.16597 | -43.34012 | 2025-09-01 03:42:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 92087355-9628-3ccd-b393-dcca255131c8 | -6.32683 | -43.5416 | 2025-09-01 03:42:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bcc95974-23dc-39d4-8ec4-e2e3343263c0 | -6.16888 | -43.32335 | 2025-09-01 03:42:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 232c5bc0-0a28-3626-b5c2-cd5db629201b | -6.74234 | -43.78837 | 2025-09-01 03:42:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 030d5ed6-ab23-3fbd-9342-1d19d9303819 | -6.30337 | -43.64544 | 2025-09-01 03:42:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 40e0f37b-00bd-33e6-8ea9-c55e8176d46d | -7.10922 | -44.55772 | 2025-09-01 03:42:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0e7010cb-06b4-376e-80c3-9f93fdf18d54 | -6.8012 | -45.68646 | 2025-09-01 03:42:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f6d6c7f4-1233-318a-82ef-d6524de6cd71 | -6.81119 | -45.6962 | 2025-09-01 03:42:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| edd764f8-9607-31ac-ac55-14e239764669 | -6.44382 | -43.97072 | 2025-09-01 03:42:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b767d7bc-8bf5-34c5-8d3b-b59ccbea5251 | -6.58152 | -43.70689 | 2025-09-01 03:42:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2614648c-2cd0-3085-a88f-4827fba9c25f | -6.16202 | -43.33361 | 2025-09-01 03:42:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 76c031af-2a3f-3c34-ab78-b7fd2fca1991 | -6.57249 | -43.69931 | 2025-09-01 03:42:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 93465ef9-9856-3815-bd7e-1e1acfba3580 | -6.4568 | -43.95647 | 2025-09-01 03:42:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 54a7fa28-7b7f-3e39-9714-9a4c4635ae53 | -6.53324 | -42.95535 | 2025-09-01 03:42:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6472aff2-22e7-330b-b8a0-441aaaa3bb8d | -6.53714 | -42.9612 | 2025-09-01 03:42:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2d735f54-9b71-3426-9985-eb7e41ea1c14 | -6.55086 | -44.08138 | 2025-09-01 03:42:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d4668fab-d233-39d7-a90d-0a783ba1e5a6 | -6.00329 | -40.22899 | 2025-09-01 03:42:00 | NOAA-21 | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 4974dbf5-5b40-31c5-830c-222b954f7518 | -4.41058 | -40.48719 | 2025-09-01 03:42:00 | NOAA-21 | HIDROLÂNDIA | CEARÁ | Brasil | 2305209 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 5f9d7331-16e4-355f-8b46-465856fa32b1 | -7.0724 | -44.34012 | 2025-09-01 03:42:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| abfb5cd4-bd8a-35c6-a43f-941ea0a5a8a0 | -2.34294 | -47.58467 | 2025-09-01 03:42:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 71ed71ca-fd5a-3035-8867-5af872114a9f | -6.26544 | -43.53862 | 2025-09-01 03:42:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fd1ae739-5073-35f3-92ab-74902e2bc220 | -6.758 | -43.78776 | 2025-09-01 03:42:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 42fc4e24-8673-3ebf-9070-9d36b9efdbc8 | -6.37318 | -43.54066 | 2025-09-01 03:42:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 097619be-90fa-3fc7-b9d2-0fb09d25cd93 | -6.44691 | -43.95267 | 2025-09-01 03:42:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 076cd33c-f0b0-3c8e-b790-b05929fafe2c | -6.71259 | -42.24897 | 2025-09-01 03:42:00 | NOAA-21 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| b0073a70-adb5-39c3-95d5-3cc8a8400936 | -6.32778 | -43.56541 | 2025-09-01 03:42:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 677db7f3-8326-38b7-9023-7d158c60d5dc | -6.94235 | -42.01213 | 2025-09-01 03:42:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 4cb0d0c2-a769-3e60-9c86-f8b7abc1cfb1 | -6.27099 | -43.53621 | 2025-09-01 03:42:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| b22650aa-9f4c-30bb-90cf-7d5af737f5eb | -6.17572 | -44.1188 | 2025-09-01 03:42:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4343a226-9445-3f27-b71d-41d1b69e8607 | -6.4499 | -43.95124 | 2025-09-01 03:42:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| cc6fa0bf-955e-3fa3-9883-9f0b274998fb | -6.51514 | -43.55325 | 2025-09-01 03:42:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 44cd42dc-259e-3d9a-ac14-87ad81d056f4 | -7.11085 | -44.76137 | 2025-09-01 03:42:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fee2b3e4-96d2-3c89-9e85-dc1990266078 | -6.42443 | -43.96078 | 2025-09-01 03:42:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 47620c47-86cd-3258-80f7-afffa38a6369 | -6.15613 | -43.33831 | 2025-09-01 03:42:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5b78736b-e890-3139-8374-febd301f2a51 | -6.57652 | -43.70588 | 2025-09-01 03:42:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9d0a55da-8704-3669-a99b-f0560b84c8ba | -5.95526 | -44.27017 | 2025-09-01 03:42:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ad236494-a109-3586-a099-02fc36d7ac4c | -6.77407 | -44.62534 | 2025-09-01 03:42:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 14ad522d-8915-3bb3-86ae-e019fd147742 | -6.30275 | -43.62162 | 2025-09-01 03:42:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 9ee20050-1702-373f-893a-ae9845282040 | -6.46723 | -41.74823 | 2025-09-01 03:42:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 446ec693-4e61-3083-9e88-40f994d92201 | -6.36029 | -43.55581 | 2025-09-01 03:42:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3f0208da-dbce-36ec-9456-f326ea2ce928 | -7.09312 | -44.34412 | 2025-09-01 03:42:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 145e4c13-b172-348f-8b58-c8eb95b6245a | -6.30543 | -43.63379 | 2025-09-01 03:42:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fb57a763-a5b9-34b5-9ef6-aab2062aefd6 | -6.27743 | -43.52863 | 2025-09-01 03:42:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 180840a2-4d19-3145-8cf0-5b3578c4c8ba | -6.26803 | -43.55338 | 2025-09-01 03:42:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f76ae7f9-a512-3c2f-86c8-5bdcc03e98db | -7.10901 | -44.31466 | 2025-09-01 03:42:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b900d597-51b7-3014-92f8-d6fce8ee3038 | -6.64152 | -43.95607 | 2025-09-01 03:42:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| eef4d937-aa75-38c4-a693-a06e3142b6bb | -6.30912 | -43.7902 | 2025-09-01 03:42:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e9ff6922-4ce1-3dea-b0c0-7c5595281765 | -5.9646 | -42.96568 | 2025-09-01 03:42:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| bc028a97-2203-3749-ae92-ac8149511fa7 | -6.57505 | -43.71444 | 2025-09-01 03:42:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| fd010c5a-8812-3278-b5d6-b75f7b9f0ff7 | -6.41817 | -43.9665 | 2025-09-01 03:42:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8c95e69b-444c-30d6-b216-270088e3d3c4 | -6.29814 | -43.61839 | 2025-09-01 03:42:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| cce01087-8a7f-313e-834e-aaca50886dde | -6.41565 | -43.62315 | 2025-09-01 03:42:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7de12697-baf2-38da-b34d-bc881630d80d | -6.64661 | -43.95705 | 2025-09-01 03:42:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4b067966-18ad-350b-9d70-6198a2b965b3 | -6.09386 | -43.19014 | 2025-09-01 03:42:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 483cdccd-f51d-3668-8b13-1e139a700b1f | -7.07812 | -44.33809 | 2025-09-01 03:42:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ccd228fd-5389-382a-9c85-4fa9990ec2e8 | -6.30388 | -43.64253 | 2025-09-01 03:42:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| db8499a3-6e79-3b21-abeb-5731395ee696 | -7.10442 | -44.31039 | 2025-09-01 03:42:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 895307a7-220c-390f-8cc5-144b371e4cb2 | -6.77791 | -44.62484 | 2025-09-01 03:42:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 221e3c3f-5bdb-338d-96bf-176245a1c391 | -7.24572 | -44.06297 | 2025-09-01 03:42:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f6814ba9-8530-3d48-aa1b-10e07e8cb01a | -6.75954 | -43.77896 | 2025-09-01 03:42:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| b52fa81d-e1d2-3176-b975-13a6dfbb74fd | -7.10492 | -44.30751 | 2025-09-01 03:42:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 076d3224-a9fd-346a-806e-e693c2ff7629 | -5.31565 | -45.45134 | 2025-09-01 03:42:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e05fc2f1-5610-36d2-939d-4486b12ef6b8 | -6.44613 | -43.97235 | 2025-09-01 03:42:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 76461e1b-62d1-3e46-9443-1ddb87894960 | -6.74337 | -43.78247 | 2025-09-01 03:42:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 79d44811-20a6-3b67-afe4-5c4c01dd80db | -3.42523 | -43.33342 | 2025-09-01 03:42:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3ab05ec3-f584-3aa9-baf9-466dbbf6a350 | -7.11437 | -44.77253 | 2025-09-01 03:42:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 444a41e9-32d8-3b23-8884-d4975d7d666f | -6.12669 | -42.9422 | 2025-09-01 03:42:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 86c465d6-7534-3c8d-b3e6-8c6efad3c0db | -4.91442 | -43.18601 | 2025-09-01 03:42:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7265998b-66f7-35ba-8d24-f247c3797ae8 | -6.45133 | -43.97275 | 2025-09-01 03:42:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c2eaa2bc-e00b-3f47-9f93-e7776a2b1817 | -6.44847 | -43.97439 | 2025-09-01 03:42:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a6ef1709-8bdb-3391-bfde-c268fa57b1d1 | -3.60593 | -42.85538 | 2025-09-01 03:42:00 | NOAA-21 | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ab7ed475-0b93-314d-b9fe-76aad5ba5499 | -6.2835 | -43.2873 | 2025-09-01 03:42:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6328fb50-21ac-3d00-abe9-6431efa903bb | -6.2393 | -43.38669 | 2025-09-01 03:42:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 0f89c509-d713-3429-a954-92854f4763d5 | -6.45459 | -43.95453 | 2025-09-01 03:42:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7429735d-d794-3ccb-b57a-e536279f7294 | -5.36026 | -41.15126 | 2025-09-01 03:42:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 05e86347-ccd2-3cc6-b933-b4a7a224f9e0 | -4.1551 | -46.78809 | 2025-09-01 03:42:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 31b0f039-9072-31f9-9e4e-854359f089be | -6.74687 | -43.79211 | 2025-09-01 03:42:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 1a4b3e16-28d8-3a78-a649-2dc55a94905c | -6.15415 | -43.32061 | 2025-09-01 03:42:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 4.1 |
| fe266028-47d0-32f2-8f27-cd121da0a222 | -5.65988 | -43.64165 | 2025-09-01 03:42:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2871c195-ed73-3c54-8677-86e39ad7c143 | -4.4112 | -40.48339 | 2025-09-01 03:42:00 | NOAA-21 | HIDROLÂNDIA | CEARÁ | Brasil | 2305209 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| f7c39f25-a392-3915-87b8-5d85969016f1 | -5.99048 | -43.3684 | 2025-09-01 03:42:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 2b78993c-3186-35ff-a235-d394e4af5b6d | -7.09197 | -44.35064 | 2025-09-01 03:42:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 64401400-8b77-3f29-809a-18bcd512c36e | -6.30439 | -43.63962 | 2025-09-01 03:42:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c1250277-ec4d-3794-8bf7-26bb73815ee2 | -6.14728 | -43.33088 | 2025-09-01 03:42:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 1fe6a160-78bd-34a4-b3cf-a2ca721cf0fe | -7.08332 | -44.33898 | 2025-09-01 03:42:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 18.8 |
| 259ec9e4-39f5-3510-b76a-734b7daa29a4 | -6.29866 | -43.6153 | 2025-09-01 03:42:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 36c50eb6-7bab-3ed8-9b85-a45ee3823f4b | -6.46887 | -42.43541 | 2025-09-01 03:42:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| ba90805a-0c62-3267-8fea-aa76df73bd1a | -6.94262 | -45.56751 | 2025-09-01 03:42:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b97863c3-a722-3d1d-b230-e980d8105101 | -6.27145 | -43.53356 | 2025-09-01 03:42:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fa0f8acd-0b56-3073-ade1-5bfcd57ff5b0 | -4.91538 | -43.18038 | 2025-09-01 03:42:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7311a494-4cea-389a-b3fa-f307cb915445 | -6.81061 | -45.68899 | 2025-09-01 03:42:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |


[Clique aqui para ver as próximas entradas](README13.md)
