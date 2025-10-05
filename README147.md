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

## Dados Diários - Página 147

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f2623daf-269a-3f1e-b2a2-8d550ca3e930 | -15.22544 | -56.80134 | 2025-10-05 05:38:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f9e851c6-c831-31e3-89fc-b56cb55937d1 | -17.96132 | -57.55841 | 2025-10-05 05:38:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 31a9a2f7-b655-3305-981a-8a7732990683 | -15.58296 | -52.48805 | 2025-10-05 05:38:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6a71c12c-82b4-3c77-a448-ed6c85bb4012 | -17.94659 | -57.59705 | 2025-10-05 05:38:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 7f33c572-35d5-3062-a8ab-a5ea2a4dfba9 | -17.95497 | -57.56885 | 2025-10-05 05:38:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 744e0f87-13a7-38e2-8e42-26c976f8a4f3 | -6.15605 | -44.6645 | 2025-10-05 06:12:00 | AQUA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 275.6 |
| 6113de33-52e5-3cc0-b0ae-cd8ae4186c3c | -8.56789 | -46.26175 | 2025-10-05 06:12:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 8895f248-e1a7-31bf-aa17-110b4069bf34 | -9.6206 | -46.63183 | 2025-10-05 06:12:00 | AQUA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 10.7 |
| b934de13-d606-3a30-a393-13909ef24826 | -6.14881 | -44.62952 | 2025-10-05 06:12:00 | AQUA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 88.3 |
| db8fec7c-6a56-3c69-bfd9-643b4fd9a903 | -7.02391 | -42.77494 | 2025-10-05 06:12:00 | AQUA_M-M | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 19.6 |
| b1e43596-15b6-3143-97a1-35273fe3a666 | -7.71251 | -46.27428 | 2025-10-05 06:12:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 15.5 |
| dbb9e0a3-537b-3798-b649-e00b97fde9a7 | -4.25096 | -48.56866 | 2025-10-05 06:12:00 | AQUA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| f4bdf598-abe8-33ad-93fd-bcaf84591dc2 | -4.44325 | -43.22115 | 2025-10-05 06:12:00 | AQUA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 34.5 |
| ba19b85b-5fca-3abe-87b2-313587b8ac56 | -6.84743 | -45.48262 | 2025-10-05 06:12:00 | AQUA_M-M | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 71ec13c4-adad-3aa1-b05d-c77aa3eae930 | -6.15832 | -44.64799 | 2025-10-05 06:12:00 | AQUA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 96.4 |
| 8b71636f-ce23-3880-8a56-956a68985ac3 | -8.53911 | -46.27918 | 2025-10-05 06:12:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 17.6 |
| 0bb641bf-489e-3523-a1d3-2f4ed0889861 | -4.13718 | -47.64968 | 2025-10-05 06:12:00 | AQUA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| ca7fa5cd-3632-356b-bfc4-bf4dd93cfac5 | -8.58217 | -46.31867 | 2025-10-05 06:12:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 21.2 |
| 05c7fb12-faf3-3753-a69a-6df0f235e0b1 | -8.93692 | -48.65845 | 2025-10-05 06:12:00 | AQUA_M-M | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 5eb788d9-f060-3779-a8c3-316ed57f60f0 | -8.87487 | -50.88956 | 2025-10-05 06:12:00 | AQUA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 29b9c9e4-73d6-3399-a2db-042b6e7d11b4 | -8.58404 | -46.30495 | 2025-10-05 06:12:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 23.0 |
| ddd3e519-190f-34ef-81f6-a1e1dc9c9bde | -5.64414 | -43.90585 | 2025-10-05 06:12:00 | AQUA_M-M | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 16.9 |
| a2428797-5bb6-3ebd-9dd1-1b6e639c1873 | -7.79891 | -44.54076 | 2025-10-05 06:12:00 | AQUA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 13.0 |
| eb2c0349-6d12-3f66-8eff-530bc8ad9dba | -8.59666 | -46.293 | 2025-10-05 06:12:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 56.7 |
| addbbb3a-0689-3365-ab9e-7d2a5fa1ea7a | -2.29561 | -47.99046 | 2025-10-05 06:12:00 | AQUA_M-M | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| fed8bfd4-83f3-3a58-8a67-ed4993f0d5c8 | -8.55182 | -46.26704 | 2025-10-05 06:12:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 54.0 |
| 70ce7878-677b-30cd-a5d0-8fa97fa2e0f7 | -3.61073 | -51.0359 | 2025-10-05 06:12:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 7a986084-7544-3439-8a05-60f16bd3470c | -8.60032 | -46.26633 | 2025-10-05 06:12:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 22.8 |
| 65bfaa1f-e8a8-329d-be91-4a500cf0cf37 | -4.63276 | -43.1768 | 2025-10-05 06:12:00 | AQUA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 46.4 |
| 53ab5529-c3de-3a53-a682-e332f0add7cf | -5.91277 | -42.8886 | 2025-10-05 06:12:00 | AQUA_M-M | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 17.6 |
| 05959ae2-5c94-3647-9a59-c5a045097bfe | -8.59293 | -46.32017 | 2025-10-05 06:12:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 17.4 |
| be36b824-61dd-3160-8b7c-339b34a6e45f | -8.6197 | -54.95929 | 2025-10-05 06:12:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 0836de26-c83f-3556-b680-220a9f769c56 | -6.84687 | -45.47713 | 2025-10-05 06:12:00 | AQUA_M-M | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 85b3361b-31f6-3b76-b33f-b9a55c4766a7 | -2.68761 | -48.39281 | 2025-10-05 06:12:00 | AQUA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| ff7b96af-dd50-3fe3-98b6-e21a508d2b68 | -8.22817 | -46.80762 | 2025-10-05 06:12:00 | AQUA_M-M | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| c138a34e-4724-36f7-9a4a-2cd6817919fd | -2.89022 | -50.72826 | 2025-10-05 06:12:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| f74bda33-a907-3323-af25-19835c994b68 | -7.75506 | -46.31384 | 2025-10-05 06:12:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 69f8a5cb-76dd-368a-9a2e-c2bbbcea4bd1 | -8.56445 | -46.25555 | 2025-10-05 06:12:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 26.5 |
| c8d7defb-c42d-3110-98c2-98d6b39ff2e8 | -9.25569 | -46.7723 | 2025-10-05 06:12:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 44e51b39-b408-393f-9a5b-8b7a16541c65 | -7.71433 | -46.26135 | 2025-10-05 06:12:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 18.9 |
| 73ee7a91-8707-378a-a7d7-d9d4dbdcb21d | -5.89616 | -42.90958 | 2025-10-05 06:12:00 | AQUA_M-M | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 75.4 |
| 024c5904-a137-38cc-a137-f14ca412dc75 | -4.31339 | -48.08862 | 2025-10-05 06:12:00 | AQUA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 16.5 |
| e5914f70-ff68-37c1-846d-f62b0227b81b | -6.14069 | -44.63816 | 2025-10-05 06:12:00 | AQUA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 47.7 |
| c223ebad-b657-3473-b3b1-c41f48ae5215 | -8.56257 | -46.26889 | 2025-10-05 06:12:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 11.0 |
| e01e115a-8488-3ebb-a5ae-d51414035335 | -9.04889 | -47.0155 | 2025-10-05 06:12:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 05fe6fe0-b568-3b56-94a0-9a56c5ea1dc3 | -9.28868 | -46.01282 | 2025-10-05 06:12:00 | AQUA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 6255fa34-b6de-33d1-9e0d-67e0f44cd019 | -8.8762 | -50.88073 | 2025-10-05 06:12:00 | AQUA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 17.7 |
| cf511667-f40d-317a-9ecc-4fb076b7045b | -8.53147 | -46.33374 | 2025-10-05 06:12:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 8b3621f4-9628-38ca-a31c-ccb1f7e9a1d7 | -5.93281 | -43.3212 | 2025-10-05 06:12:00 | AQUA_M-M | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 16.7 |
| a467605d-03ad-33f2-84d0-6c33a09e323c | -6.14652 | -44.64624 | 2025-10-05 06:12:00 | AQUA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 131.5 |
| 8757a359-6055-35f5-bb5d-a988afb39e9a | -9.29982 | -46.01451 | 2025-10-05 06:12:00 | AQUA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 0acd82c5-3d4a-3c54-a001-f1ddbdd621f8 | -5.888 | -42.90318 | 2025-10-05 06:12:00 | AQUA_M-M | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 83.8 |
| 09248fa5-b301-3bcc-ae4c-cbde75a8a643 | -4.44042 | -43.24137 | 2025-10-05 06:12:00 | AQUA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 27.9 |
| 58014d27-6f2f-37ca-b4c6-2a902466c79a | -6.39576 | -44.77809 | 2025-10-05 06:12:00 | AQUA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 4218acbf-9f2d-3c9a-bc3c-3304ce46ecef | -8.58589 | -46.29135 | 2025-10-05 06:12:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| afc40a16-b3e1-3fb7-a747-574c7f5142f1 | -6.1442 | -44.6632 | 2025-10-05 06:12:00 | AQUA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 52.2 |
| bd00f44a-ab8f-3035-b434-8042865a33b9 | -5.99089 | -44.35229 | 2025-10-05 06:12:00 | AQUA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 15.0 |
| a9707b29-a0d7-3ee2-bfaf-161dfa38022d | -7.79379 | -44.55077 | 2025-10-05 06:12:00 | AQUA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 12.2 |
| f8a8eec5-d394-3ec5-8fde-a3597235d7a0 | -6.84478 | -45.49168 | 2025-10-05 06:12:00 | AQUA_M-M | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 9b5047aa-6618-3297-a8d1-04c9400d7ce7 | -6.45699 | -44.57061 | 2025-10-05 06:12:00 | AQUA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 20.3 |
| 87b3d970-26a3-340f-95de-7933eaae7d87 | -3.80897 | -51.07383 | 2025-10-05 06:12:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 1cdefe73-6edf-3c81-99de-201941e65819 | -8.59481 | -46.30653 | 2025-10-05 06:12:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 60.3 |
| 4f216123-689f-33df-9d7b-edde7fde03ff | -8.55374 | -46.25338 | 2025-10-05 06:12:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 28.2 |
| cc00ef9c-d206-3080-bfd0-0401efdfac1e | -2.89783 | -50.73877 | 2025-10-05 06:12:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 70c425ab-8442-39ba-9dac-887fac5bec06 | -2.89922 | -50.72958 | 2025-10-05 06:12:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 74e7ef61-ea9e-3ed5-b1c6-76fceec5a99c | -7.03202 | -50.73299 | 2025-10-05 06:12:00 | AQUA_M-M | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 38c42144-934d-3865-81ee-2640266ad9aa | -8.53337 | -46.32017 | 2025-10-05 06:12:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 11.7 |
| eb4d9b38-8b09-39e5-9d26-551bbf9d7295 | -4.13576 | -47.6595 | 2025-10-05 06:12:00 | AQUA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| f982a515-cfbd-32aa-8018-734078172eae | -6.40244 | -43.05492 | 2025-10-05 06:12:00 | AQUA_M-M | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 71.6 |
| dbe3a286-6d45-3a86-8e39-3422991812ec | -7.72811 | -46.31703 | 2025-10-05 06:12:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 62cf47df-a211-343f-8f69-6a1e73cf4419 | -7.73 | -46.30382 | 2025-10-05 06:12:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 2c7d841d-cbce-3aa3-8ea9-9d592ec716fe | -2.68895 | -48.38385 | 2025-10-05 06:12:00 | AQUA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 4659b86a-61e7-328d-951a-f2f82f088959 | -8.59849 | -46.27967 | 2025-10-05 06:12:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 27.7 |
| 54d9ad2f-bb1c-311f-9f71-07c55eae399a | -3.84875 | -41.57827 | 2025-10-05 06:12:00 | AQUA_M-M | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 29.7 |
| f7a605c4-97f9-3278-8298-b116377ba32e | -4.25232 | -48.55961 | 2025-10-05 06:12:00 | AQUA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| d59a4def-f393-3298-b73c-552935abd7c1 | -8.23849 | -46.80904 | 2025-10-05 06:12:00 | AQUA_M-M | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 17.7 |
| e0218b02-7fac-35e2-bf13-aeb5baf6643c | -6.40558 | -43.03194 | 2025-10-05 06:12:00 | AQUA_M-M | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 41.6 |
| 84bb3544-25c7-38c5-bf94-a40c3584f43c | -4.64576 | -43.17855 | 2025-10-05 06:12:00 | AQUA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 68.5 |
| d9484684-1219-3154-96f7-fce7f82ecdce | -3.3952 | -50.27116 | 2025-10-05 06:12:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 10aa62dc-8ff5-371a-a04d-42d431894adb | -9.3019 | -45.99929 | 2025-10-05 06:12:00 | AQUA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 42.7 |
| e5420657-3225-369e-8ece-bcf79d0856a9 | -8.58033 | -46.33215 | 2025-10-05 06:12:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 3cce7a88-d4f1-381a-beef-bcb62cb0fe55 | -17.95644 | -57.60291 | 2025-10-05 06:14:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 18.7 |
| 85158926-fdca-363a-bc46-6d6b47fbf0b4 | -14.69029 | -48.35145 | 2025-10-05 06:14:00 | AQUA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 40.0 |
| d4496ca1-ba10-36a4-99b1-d822899faa06 | -14.67846 | -48.36229 | 2025-10-05 06:14:00 | AQUA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 30.6 |
| 2b6d7932-83de-3de9-8734-967746d7c662 | -13.27983 | -47.58988 | 2025-10-05 06:14:00 | AQUA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 19.1 |
| 89790ab0-a529-336c-ba58-bab1863c4b39 | -17.95911 | -57.5878 | 2025-10-05 06:14:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 19.1 |
| a16812b4-65f9-3886-a717-4f6dbb60adcf | -15.58044 | -52.49105 | 2025-10-05 06:14:00 | AQUA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 891001f3-77d5-360c-81ac-40e219c6eb79 | -10.9423 | -47.08841 | 2025-10-05 06:14:00 | AQUA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 31.0 |
| 98569a12-a718-3c27-b353-69d86418d844 | -14.99846 | -49.97755 | 2025-10-05 06:14:00 | AQUA_M-M | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 48bcc7a1-1cbb-3755-96a0-d558365c7c6f | -13.35185 | -47.58114 | 2025-10-05 06:14:00 | AQUA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 5e03fc9b-b7f8-3cc9-add6-63c90cc59441 | -13.08937 | -47.95517 | 2025-10-05 06:14:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 6ea1fcce-72ff-3232-aba9-016198bcaf6b | -15.60735 | -52.51035 | 2025-10-05 06:14:00 | AQUA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 65b0e821-b76f-3fac-ac1a-99e6cb031965 | -11.35221 | -47.6572 | 2025-10-05 06:14:00 | AQUA_M-M | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 8af1c737-6d63-33dd-b2a2-9d60f2de1fe0 | -13.57213 | -48.15639 | 2025-10-05 06:14:00 | AQUA_M-M | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 36.3 |
| b8333634-c86b-39fd-b317-c1e7f6b57d0f | -10.59651 | -54.34715 | 2025-10-05 06:14:00 | AQUA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 14.2 |
| abf4994a-4bcd-3444-a228-2870479cb7ed | -13.08587 | -47.82662 | 2025-10-05 06:14:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 3cfd1433-7478-3693-9ff1-f9d635662c69 | -13.12502 | -50.88367 | 2025-10-05 06:14:00 | AQUA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 18.8 |
| 891b73f4-6a5a-3549-8138-594e54d0c5c5 | -13.29598 | -48.08639 | 2025-10-05 06:14:00 | AQUA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 007318f6-2c3b-345d-b960-ab070409b86b | -11.10762 | -47.87662 | 2025-10-05 06:14:00 | AQUA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 553e17a4-24f2-3237-810f-8d9b8248f7d6 | -11.09559 | -47.73777 | 2025-10-05 06:14:00 | AQUA_M-M | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |


[Clique aqui para ver as próximas entradas](README148.md)
