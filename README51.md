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

## Dados Diários - Página 51

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ddf90efb-f691-323c-b714-bb2517e61544 | -6.2869 | -44.05001 | 2025-10-04 04:12:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b30c3d62-c56a-3f30-b827-68be8db1584e | -4.44923 | -43.23411 | 2025-10-04 04:12:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 58309654-34ef-37ba-aa43-1d83a5f66b3a | -5.83249 | -42.88623 | 2025-10-04 04:12:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 191ee9c4-52bd-3482-bed6-12b178030a4c | -6.16819 | -43.91965 | 2025-10-04 04:12:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b544805a-10de-3fdd-87a4-a2212d7b0159 | -4.61588 | -43.14686 | 2025-10-04 04:12:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 23bfcdbd-1b41-3802-a4de-3e9b95d58a0d | -7.05354 | -43.22128 | 2025-10-04 04:12:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| f1defa74-257a-3809-9f08-1a658374eace | -7.73999 | -42.52533 | 2025-10-04 04:12:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| b1a888f4-07a9-370d-8565-7818a82391e5 | -6.37323 | -43.89036 | 2025-10-04 04:12:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| af6f8b35-3b41-38fa-aea4-c4b175e91871 | -5.41834 | -44.00002 | 2025-10-04 04:12:00 | NOAA-20 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4fbee68b-24b0-3f82-aa9f-8d59c47c4cbb | -6.67036 | -42.37582 | 2025-10-04 04:12:00 | NOAA-20 | ARRAIAL | PIAUÍ | Brasil | 2201002 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| ec6d34bf-7985-3551-afb6-d9394a3425ee | -4.61478 | -43.1538 | 2025-10-04 04:12:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 28.3 |
| 3c003365-f2aa-357d-870c-a4177a874513 | -5.09057 | -37.60647 | 2025-10-04 04:12:00 | NOAA-20 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 407217e0-1dea-3ab7-8a55-a54392c4c1b1 | -5.47041 | -43.15778 | 2025-10-04 04:12:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 675649f3-a3ae-3525-b24f-2cab26dba065 | -7.73765 | -42.95371 | 2025-10-04 04:12:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| e0737a47-5e95-3ab4-bd8d-e6bd1ab81584 | -6.35533 | -43.44728 | 2025-10-04 04:12:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9e477f79-c990-3220-8980-88a0186808e9 | -5.69287 | -42.84651 | 2025-10-04 04:12:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| cd739d0f-56c1-3ffa-abff-6a37746839fa | -4.95532 | -45.06989 | 2025-10-04 04:12:00 | NOAA-20 | SÃO ROBERTO | MARANHÃO | Brasil | 2111672 | 21 | 33 | nan | nan | nan | Cerrado | 22.6 |
| cc895548-bc9c-30ec-b4a2-c98e2f54b228 | -5.54618 | -42.65692 | 2025-10-04 04:12:00 | NOAA-20 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 52305dac-3e33-3bd2-8ea2-92dc230371e3 | -6.37046 | -43.8863 | 2025-10-04 04:12:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e52f2fc2-5b31-31b9-91e2-12fb9330ccbe | -6.36487 | -43.89989 | 2025-10-04 04:12:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| f56420fd-8787-374a-9e0f-2eb899b05f4d | -6.09792 | -43.48492 | 2025-10-04 04:12:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 160e6b15-8024-346f-9ad8-f0e31969e1fb | -5.66338 | -42.71106 | 2025-10-04 04:12:00 | NOAA-20 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 2f2cbe48-d9e2-3e5c-a10c-4cd32b2db0ed | -6.37656 | -43.89093 | 2025-10-04 04:12:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2aa36ba6-60a7-3aeb-bfa1-8e193102b299 | -7.04388 | -42.78696 | 2025-10-04 04:12:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 454ba960-9beb-344f-9ffa-1a3dddb20fef | -7.04443 | -42.78349 | 2025-10-04 04:12:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 14ebb061-dfa2-346c-8397-20d71dbad699 | -7.78112 | -42.58922 | 2025-10-04 04:12:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 6d074da5-692d-383d-a726-1beaedc60714 | -6.96876 | -44.39619 | 2025-10-04 04:12:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3f53c279-edba-320c-9dc6-e024a4d6ac59 | -5.3319 | -43.3455 | 2025-10-04 04:12:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ae11c227-bdf5-3525-8b39-54b58b590201 | -6.35202 | -43.44675 | 2025-10-04 04:12:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c2b6a5cf-124d-3ab5-a3c2-513e51632de7 | -4.25795 | -48.55801 | 2025-10-04 04:12:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 7861019b-a51e-3a31-84e9-324bcd062539 | -2.90154 | -50.72867 | 2025-10-04 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2dc1f151-4ba5-3040-826e-2b6974314c24 | -5.87348 | -44.27366 | 2025-10-04 04:12:00 | NOAA-20 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ba9e01d3-0916-3329-838a-f2efc2045554 | -7.72775 | -42.58444 | 2025-10-04 04:12:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| dcacce67-457b-3458-a8f4-95456599d348 | -6.35035 | -43.43583 | 2025-10-04 04:12:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8823ab35-a3b0-3aa7-83cd-01185e61d564 | -4.43484 | -43.23897 | 2025-10-04 04:12:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d9fd1649-bc9b-3eae-a8bb-7618b60ef973 | -2.69231 | -48.38908 | 2025-10-04 04:12:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8885827f-6311-3c04-87e2-537cc4e5ff9b | -1.13513 | -47.80524 | 2025-10-04 04:12:00 | NOAA-20 | SÃO FRANCISCO DO PARÁ | PARÁ | Brasil | 1507409 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d4cab3a3-2283-3bdb-b204-b0c1e8352e9c | -4.25094 | -48.56185 | 2025-10-04 04:12:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c11127ff-af5d-3fe5-9848-a0b254010cec | -5.45934 | -43.1631 | 2025-10-04 04:12:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 04cfabfd-6b37-36e8-8d3a-c06c08672f74 | -6.74104 | -48.09726 | 2025-10-04 04:12:00 | NOAA-20 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 705d407e-842d-3b07-983d-a5539a494b31 | -6.24243 | -44.22139 | 2025-10-04 04:12:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6733fcfb-0777-3073-9c3e-21e5091aa0ba | -7.55647 | -42.39573 | 2025-10-04 04:12:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 1e331002-f9ba-3f1a-bd99-808c37ef5434 | -7.0006 | -44.197 | 2025-10-04 04:12:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8f66b666-79bf-36c1-a023-a7baa917842a | -7.78813 | -42.50055 | 2025-10-04 04:12:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| c714854f-fa9d-3127-8fd0-c1211183751d | -4.6441 | -43.1833 | 2025-10-04 04:12:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 1308859b-5be9-3a23-b8b9-fd400e61ea9d | -5.20819 | -44.35403 | 2025-10-04 04:12:00 | NOAA-20 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 78f7e7e0-7683-360e-84ca-a2b048ffaaa8 | -5.47354 | -42.77271 | 2025-10-04 04:12:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 3b24c147-2bb1-346a-83d4-72febe07db78 | -5.31493 | -43.77308 | 2025-10-04 04:12:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 26fcdd69-2006-3b6a-9d08-a02475e03cf5 | -6.80658 | -44.62111 | 2025-10-04 04:12:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5a615564-c895-3e4e-b7e6-99d402c04bda | -6.17765 | -43.92475 | 2025-10-04 04:12:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 45c6899e-9848-310a-847f-0760c124475e | -6.18899 | -42.71609 | 2025-10-04 04:12:00 | NOAA-20 | ANGICAL DO PIAUÍ | PIAUÍ | Brasil | 2200608 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| b81008c4-fd69-3030-89c1-5ba5b48b17fe | -5.98586 | -43.48508 | 2025-10-04 04:12:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 2721942f-0d4f-3c24-a72b-e9339b291129 | -7.10321 | -45.08791 | 2025-10-04 04:12:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| bfd1bfbb-611f-3d10-badd-a4a59197e046 | -7.71169 | -42.57834 | 2025-10-04 04:12:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 2cedc58e-3116-368c-b68a-9e0b101414d1 | -5.68403 | -42.83805 | 2025-10-04 04:12:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 2cf3b3a6-79ee-34fa-a285-a8a4d4912584 | -4.43042 | -43.2454 | 2025-10-04 04:12:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d2f25e0a-e566-3b00-9ac7-49958bfae8bc | -6.23639 | -45.34739 | 2025-10-04 04:12:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cfa46b94-5f49-3314-866a-085281317393 | -2.55603 | -47.65823 | 2025-10-04 04:12:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ae8c1193-2ff4-3dbb-b6e6-a1a5148631ac | -5.84827 | -42.78616 | 2025-10-04 04:12:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| e4d88712-b9b2-3676-8fe7-d8b9b93178f8 | -4.94696 | -42.66464 | 2025-10-04 04:12:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9a40d034-b8e4-3811-96e5-42f2d1d57895 | -6.99551 | -42.33744 | 2025-10-04 04:12:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 313131a7-87a1-32f2-b683-dcc6cda77a44 | -4.58568 | -47.03995 | 2025-10-04 04:12:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 15.6 |
| 9edde554-5d0d-3ca2-950b-bc18757fcb70 | -5.94377 | -43.3002 | 2025-10-04 04:12:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 35c5b121-3df7-34a8-8c80-84e9e0e90a9c | -6.22991 | -44.65335 | 2025-10-04 04:12:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 90fe4168-e581-3541-9098-32c86d2cc316 | -6.10344 | -43.42887 | 2025-10-04 04:12:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d0d376c7-704e-3873-900a-557b91b73421 | -5.79492 | -42.58682 | 2025-10-04 04:12:00 | NOAA-20 | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 1ee886f1-2bc5-382b-867f-87c30f1a18c4 | -5.23947 | -45.55043 | 2025-10-04 04:12:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e0b8235f-56b7-335d-8f60-e347aa691bfd | -6.60202 | -44.30495 | 2025-10-04 04:12:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 81c232f3-6da2-39f2-bd06-ede7aee90d93 | -4.43928 | -43.25393 | 2025-10-04 04:12:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ca5d3cfe-e01c-34ee-9426-3dc0486fd6dd | -7.80207 | -42.54228 | 2025-10-04 04:12:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| f7c38241-a93a-3eb3-a170-5d9f945a7ad8 | -6.12279 | -45.92923 | 2025-10-04 04:12:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ac614094-4d0b-31b5-9270-f9f42edebe2d | -7.76016 | -42.61453 | 2025-10-04 04:12:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| dbe515a0-a9fe-30a0-9943-7442846ebcc0 | -5.40142 | -41.34872 | 2025-10-04 04:12:00 | NOAA-20 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 61ed6945-fb0d-3785-92ae-d687cbaec478 | -7.01349 | -42.30761 | 2025-10-04 04:12:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| c0b3abd6-9224-3df9-8e2f-55d9e627c46d | -7.04606 | -42.77309 | 2025-10-04 04:12:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| f965642c-4b1b-3ec5-af85-7e75fa5a6698 | -7.80262 | -42.53877 | 2025-10-04 04:12:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 5844f69b-e99b-3fb1-a599-fa2fd21c2a77 | -6.67008 | -44.20227 | 2025-10-04 04:12:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1243b4dd-cd26-3098-94d2-bd0c26b03905 | -5.47023 | -42.77219 | 2025-10-04 04:12:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 7.7 |
| 6bd6b88b-be23-3ece-9ba0-abc3918c5715 | -7.11006 | -45.08902 | 2025-10-04 04:12:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 31a9aa30-6396-32c3-83c5-280f093fe7cd | -6.98819 | -42.79597 | 2025-10-04 04:12:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 62d74cbe-32c2-3900-9a64-80cac9434a8f | -5.95202 | -43.26955 | 2025-10-04 04:12:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 9745899e-376c-3097-9901-980d1a06a624 | -5.48892 | -44.11018 | 2025-10-04 04:12:00 | NOAA-20 | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| cfa1aa8b-a238-34a8-aaaa-c2d58d4a11c9 | -5.6546 | -43.8814 | 2025-10-04 04:12:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ca8220b5-45e5-30e3-8204-be7f2edb7dc6 | -6.15912 | -44.61196 | 2025-10-04 04:12:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ccf5b582-d62e-3268-a84c-c134793d870d | -5.0814 | -44.09019 | 2025-10-04 04:12:00 | NOAA-20 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 894883b9-cd68-3082-b492-13e85636aadd | -5.77362 | -42.93708 | 2025-10-04 04:12:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 2d33cf4c-391d-3552-b0a0-6320d76e2e46 | -5.48003 | -45.54189 | 2025-10-04 04:12:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b7906f11-1558-3c0f-9f53-8751a3388236 | -4.25593 | -48.55848 | 2025-10-04 04:12:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2563c38a-e093-389c-832e-58bf6e212c24 | -6.30646 | -43.99163 | 2025-10-04 04:12:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a81525fc-6e24-397a-9893-d7e3abd1d403 | -5.9366 | -43.30261 | 2025-10-04 04:12:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5a8af9e0-ae91-3878-9d18-cb48852293f7 | -4.30829 | -39.28128 | 2025-10-04 04:12:00 | NOAA-20 | CANINDÉ | CEARÁ | Brasil | 2302800 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| f759ce42-7af7-3101-b517-e1faf9626d84 | -6.36266 | -43.89233 | 2025-10-04 04:12:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| bbfd9cda-af16-3e19-8312-5f9e425d1fa6 | -6.67621 | -44.20689 | 2025-10-04 04:12:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 99b46006-f4c4-3c04-a59e-8922f73e99e5 | -6.366 | -43.89283 | 2025-10-04 04:12:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 7a063f6f-3030-3eaf-9544-afe4cb731664 | -7.74332 | -42.52585 | 2025-10-04 04:12:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 206d8ae6-ee25-304f-b87f-6d9c49944814 | -6.74584 | -44.58189 | 2025-10-04 04:12:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 33b039a0-a35a-30c7-82d3-c32e8b5118e8 | -7.04552 | -42.77656 | 2025-10-04 04:12:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 1300d255-6185-3779-88fe-4c1f4f85caf9 | -6.98488 | -42.79545 | 2025-10-04 04:12:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 664d45b4-5297-3ee0-8802-eecbcfa7f1ad | -5.31364 | -44.13723 | 2025-10-04 04:12:00 | NOAA-20 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d40e015e-358d-3f97-bddd-fd04f97d2518 | -6.07743 | -42.51745 | 2025-10-04 04:12:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 18.4 |


[Clique aqui para ver as próximas entradas](README52.md)
