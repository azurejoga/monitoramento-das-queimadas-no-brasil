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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1c7859fd-3e4d-33ba-a0b7-fd08b983e4f2 | -10.2742 | -36.4408 | 2025-05-03 00:00:00 | GOES-19 | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | 49.4 |
| c55627a1-7db3-32d8-916e-7b8fd4316c66 | -6.7053 | -42.1234 | 2025-05-03 00:00:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 91.7 |
| 19b02bc2-0601-34cf-8385-753984becf09 | -21.1477 | -48.62856 | 2025-05-03 00:09:00 | TERRA_M-M | VISTA ALEGRE DO ALTO | SÃO PAULO | Brasil | 3556909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 37.7 |
| 316240b5-5fa5-3ac2-ad89-3395f2de912d | -21.14523 | -48.63604 | 2025-05-03 00:09:00 | TERRA_M-M | VISTA ALEGRE DO ALTO | SÃO PAULO | Brasil | 3556909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 44.4 |
| 69d1828b-fd07-32e5-a9dd-d9f4fd7e10c5 | -6.7053 | -42.1234 | 2025-05-03 00:10:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 86.7 |
| 445901a1-e2c7-338c-a9af-7f02c00f922a | -13.68972 | -45.21633 | 2025-05-03 00:11:00 | TERRA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 11.9 |
| a1c03e7f-e30e-3458-912a-cbe0d6164814 | -10.27832 | -36.44048 | 2025-05-03 00:11:00 | TERRA_M-M | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | 14.8 |
| 8d345587-9a94-3982-9b15-0a8d28a4a1b5 | -13.6996 | -45.19825 | 2025-05-03 00:11:00 | TERRA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 99aa356c-b513-3a44-9088-0667e614e9e9 | -13.69584 | -45.20943 | 2025-05-03 00:11:00 | TERRA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 22.5 |
| 903cc0a6-035e-3864-9123-a208f0717fd8 | -10.27639 | -36.42765 | 2025-05-03 00:11:00 | TERRA_M-M | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | 101.9 |
| caa19169-abc4-37d3-9c14-b1dcd0c61bd1 | -5.79429 | -43.61811 | 2025-05-03 00:13:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 1cef5086-e2de-3d5c-9cfd-2db8284895e5 | -8.08005 | -43.11472 | 2025-05-03 00:13:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 7.5 |
| 6c8d132c-3428-3b4d-80de-13c04e3276bc | -7.68563 | -42.98855 | 2025-05-03 00:13:00 | TERRA_M-M | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 84.7 |
| fa326951-7ad2-3f6a-a30b-91390e7de642 | -6.96149 | -42.79986 | 2025-05-03 00:13:00 | TERRA_M-M | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 36.8 |
| b129c7d5-9cd7-3dc3-9487-b0868f7a8d1e | -6.96935 | -42.78903 | 2025-05-03 00:13:00 | TERRA_M-M | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 13.6 |
| 70947406-b935-3a5b-8430-90f8290cce0d | -6.96018 | -42.79031 | 2025-05-03 00:13:00 | TERRA_M-M | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 11.1 |
| 3780385d-f64b-32bc-b657-224040c1e8b3 | -5.16837 | -45.10613 | 2025-05-03 00:13:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 1ba68425-07d7-3f43-a0b0-97fc4d0c10d8 | -6.9628 | -42.80943 | 2025-05-03 00:13:00 | TERRA_M-M | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 8.8 |
| e07ed59c-9dfd-3f2d-8490-c3dedb66c70a | -8.07869 | -43.10458 | 2025-05-03 00:13:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 63488aad-f6dd-3576-88d9-b1171cee03a5 | -6.69411 | -42.12784 | 2025-05-03 00:13:00 | TERRA_M-M | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 66.2 |
| 2d47edfa-3e6e-3833-a924-ee530d43ecd1 | -6.97066 | -42.79857 | 2025-05-03 00:13:00 | TERRA_M-M | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 11.5 |
| f6072001-43b1-35f9-a516-4cbbb3f3d51b | -6.69537 | -42.13692 | 2025-05-03 00:13:00 | TERRA_M-M | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 23.4 |
| 06ae3a9d-fcb2-39e1-b291-ec05d0242e3e | -7.67631 | -42.98988 | 2025-05-03 00:13:00 | TERRA_M-M | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 30.3 |
| e896f334-b725-3db9-86fb-5582ebe421da | -7.68429 | -42.9786 | 2025-05-03 00:13:00 | TERRA_M-M | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 10.7 |
| e0e0b84d-b492-3040-adba-06732afbb4ae | -6.70447 | -42.12946 | 2025-05-03 00:13:00 | TERRA_M-M | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 51.4 |
| 05442161-e236-31dd-9a2c-3e73309b40d1 | -13.0474 | -53.6903 | 2025-05-03 00:17:00 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 96cb399f-3d85-3f5f-a16f-ab7f9a5a3c3d | -2.6554 | -48.785099 | 2025-05-03 00:17:00 | METOP-B | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 44778ead-5b9a-34ab-b3f3-e77f648f6b18 | -7.6816 | -42.982201 | 2025-05-03 00:17:00 | METOP-B | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 65015fcb-2f61-38a5-ad88-3696b08d3fbd | -21.151501 | -48.606899 | 2025-05-03 00:17:00 | METOP-B | VISTA ALEGRE DO ALTO | SÃO PAULO | Brasil | 3556909 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| c9d49ae9-c77a-34af-a5b5-1255ada92702 | -6.6957 | -42.133701 | 2025-05-03 00:17:00 | METOP-B | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 3ce7ef45-abd0-3201-a4cc-de7ad877be32 | -6.6924 | -42.1199 | 2025-05-03 00:17:00 | METOP-B | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 31437b3d-a89f-3b7a-8b1e-31d94b6c397b | -7.6788 | -42.970501 | 2025-05-03 00:17:00 | METOP-B | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 4530ab43-1154-30b2-9886-f06e9387f98c | -13.6932 | -45.195202 | 2025-05-03 00:17:00 | METOP-B | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 97cb0f13-c72d-3db9-9fa0-ded2e9c6659c | -6.7021 | -42.1175 | 2025-05-03 00:17:00 | METOP-B | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 94db5afe-33ff-375c-b9d5-6a248620b246 | -10.2822 | -36.424 | 2025-05-03 00:17:00 | METOP-B | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| f92e73f0-54c7-3dbc-a62d-b687f04d8bf5 | -13.0499 | -53.7029 | 2025-05-03 00:17:00 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 893227c7-0206-3e47-8515-6d7fdbad9be1 | -2.657 | -48.792099 | 2025-05-03 00:17:00 | METOP-B | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ce5a17b5-2c07-323b-8e78-574c21cf243e | -13.0524 | -53.7155 | 2025-05-03 00:17:00 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 856a79e6-50ec-3f60-a10f-879f53d3f9e5 | -7.694 | -42.991501 | 2025-05-03 00:17:00 | METOP-B | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 0768c7ef-f3e4-3deb-a0f0-6c08b6890e69 | -7.6843 | -42.9939 | 2025-05-03 00:17:00 | METOP-B | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 44644d8d-272a-3274-b2c3-8ed5b4889f63 | -6.9651 | -42.785702 | 2025-05-03 00:17:00 | METOP-B | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 5cf086fe-22da-3df3-9bcd-edca32414f25 | -13.695 | -45.202801 | 2025-05-03 00:17:00 | METOP-B | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 8e127448-d67f-34be-80f5-6b77953bb937 | -21.149799 | -48.5984 | 2025-05-03 00:17:00 | METOP-B | VISTA ALEGRE DO ALTO | SÃO PAULO | Brasil | 3556909 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 6653ba81-b4f7-39ed-b844-da056ea8aeae | -7.6913 | -42.979801 | 2025-05-03 00:17:00 | METOP-B | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 11167376-49de-3a6e-a0e0-6303c346df55 | -10.2727 | -36.426601 | 2025-05-03 00:17:00 | METOP-B | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| bd824d66-32c4-30d1-a834-fad6afc43f8c | -6.968 | -42.798 | 2025-05-03 00:17:00 | METOP-B | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 4c2ea9bf-70b6-3eca-9449-c5908dce99cd | -6.9582 | -42.800301 | 2025-05-03 00:17:00 | METOP-B | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 70567a17-87c7-3109-ac99-7b7148324160 | -21.1434 | -48.617599 | 2025-05-03 00:17:00 | METOP-B | VISTA ALEGRE DO ALTO | SÃO PAULO | Brasil | 3556909 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 096a95b0-24f9-3c49-9f1a-b925719f2e6e | -5.1721 | -45.1022 | 2025-05-03 00:17:00 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 30ee7f67-bf98-3ae2-957e-3c42f1c3bdb7 | -2.6586 | -48.799 | 2025-05-03 00:17:00 | METOP-B | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7ec1e9c5-d839-3832-a702-b50aea815ef5 | -21.141701 | -48.6091 | 2025-05-03 00:17:00 | METOP-B | PIRANGI | SÃO PAULO | Brasil | 3539004 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 85fec8ba-7553-3e03-8cfa-601f01791e25 | -17.872801 | -44.5616 | 2025-05-03 00:17:00 | METOP-B | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| a3fe6295-1fe6-334c-a8ee-73871c2cb198 | -6.7054 | -42.131302 | 2025-05-03 00:17:00 | METOP-B | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| db8fe657-f75a-3350-b070-73e467e80bd5 | -10.2805 | -36.455898 | 2025-05-03 00:17:00 | METOP-B | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 0ca4d944-d5ab-361c-9188-44d337635619 | -6.7053 | -42.1234 | 2025-05-03 00:20:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 87.5 |
| 81df92a0-d9a1-37b7-a0b9-bbe964277a78 | -10.2747 | -36.4138 | 2025-05-03 00:30:00 | GOES-19 | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | 64.0 |
| 1a070b1e-d74c-3aa8-ad0d-bd0eead31b02 | -6.7053 | -42.1234 | 2025-05-03 00:30:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 75.6 |
| 3a3cb576-7efa-3511-86f2-2a8b5c45fa32 | -10.2742 | -36.4408 | 2025-05-03 00:30:00 | GOES-19 | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | 74.4 |
| 218d040a-1e82-3c56-a0f2-1cd44f7032a8 | -6.6865 | -42.1252 | 2025-05-03 00:40:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 59.7 |
| 82df549e-a6f6-3434-a9b1-2cf6591f4568 | -6.7053 | -42.1234 | 2025-05-03 00:40:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 77.3 |
| 3be08092-fda4-3d49-bdb9-3ed4edea646f | -6.7053 | -42.1234 | 2025-05-03 00:50:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 83.2 |
| b5f460d9-6a84-36fd-8146-42f983be9617 | -6.7053 | -42.1234 | 2025-05-03 01:00:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 71.8 |
| 30399a71-6340-3f40-8fff-4c5293c9172e | -6.6865 | -42.1252 | 2025-05-03 01:00:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 62.0 |
| a0b73ece-968e-3757-8232-be4ff1b05d77 | -6.7053 | -42.1234 | 2025-05-03 01:10:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 75.3 |
| acda29c5-4885-37cb-b15b-6229c916b36d | -13.0505 | -53.727001 | 2025-05-03 01:11:00 | METOP-C | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e8718535-1adf-3bab-9d4b-44ea2178a872 | -13.0587 | -53.717602 | 2025-05-03 01:11:00 | METOP-C | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 08b4dc84-2a4a-34c0-ab5d-9eba4292239d | -20.8232 | -55.532902 | 2025-05-03 01:11:00 | METOP-C | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 7560ffa3-fb1d-37cb-83dc-bbd56b1da23d | -13.057 | -53.7104 | 2025-05-03 01:11:00 | METOP-C | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a47f9327-25f5-336c-b435-be1b36ee2cbb | -17.633699 | -50.9198 | 2025-05-03 01:11:00 | METOP-C | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 77d17102-653d-3146-a322-0cf712a64d1c | -20.821501 | -55.5247 | 2025-05-03 01:11:00 | METOP-C | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 5af5b36c-d6f0-3ea1-8b65-2005c036fb44 | -19.98 | -49.819401 | 2025-05-03 01:11:00 | METOP-C | RIOLÂNDIA | SÃO PAULO | Brasil | 3544202 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| a41b6753-c994-346f-8400-b4d31c1c5f45 | -19.9821 | -49.828098 | 2025-05-03 01:11:00 | METOP-C | RIOLÂNDIA | SÃO PAULO | Brasil | 3544202 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 2d19c0f7-89eb-3163-8e35-38c0e606f7cc | -21.1567 | -48.605202 | 2025-05-03 01:11:00 | METOP-C | VISTA ALEGRE DO ALTO | SÃO PAULO | Brasil | 3556909 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 4f38e7cb-1172-39e7-9b43-ed030a5cfcda | -12.6651 | -58.106098 | 2025-05-03 01:11:00 | METOP-C | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 8e5b29c3-3797-3574-b346-9baf19478fcb | -21.1591 | -48.615002 | 2025-05-03 01:11:00 | METOP-C | VISTA ALEGRE DO ALTO | SÃO PAULO | Brasil | 3556909 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 6818a888-7b6e-35eb-8440-56e99a15ac1f | -18.260599 | -52.997601 | 2025-05-03 01:11:00 | METOP-C | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| b19d9b89-4e53-3629-81be-2242b7d02ea9 | -17.631701 | -50.911598 | 2025-05-03 01:11:00 | METOP-C | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| aeb25198-a0f2-3774-abbb-bf3d17e3583b | -21.149401 | -48.617699 | 2025-05-03 01:11:00 | METOP-C | VISTA ALEGRE DO ALTO | SÃO PAULO | Brasil | 3556909 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 57c0253f-f47c-3081-b2f0-0acb73360b6f | -18.2638 | -53.0121 | 2025-05-03 01:11:00 | METOP-C | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 840a8a75-a488-300f-a36c-b97d74319b9d | -18.262199 | -53.004902 | 2025-05-03 01:11:00 | METOP-C | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 09f6352d-0f59-3d80-a0bc-9ea986399df2 | -6.7053 | -42.1234 | 2025-05-03 01:20:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 94.8 |
| a933a120-a52e-3fcc-92ae-3984128dfe46 | -6.7053 | -42.1234 | 2025-05-03 01:30:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 72.9 |
| e721b069-7058-3af1-8fa5-9f534e2bedf5 | -6.7053 | -42.1234 | 2025-05-03 01:40:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 77.8 |
| afa81e55-21c4-3587-9453-d646b03c5ffb | -20.81787 | -55.536 | 2025-05-03 01:47:00 | TERRA_M-M | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 18.1 |
| 0150e232-2e93-3053-8b56-ac9a273a831e | -13.04449 | -53.72187 | 2025-05-03 01:49:00 | TERRA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 39.6 |
| 15a00bd8-7e2d-38c1-950d-736402e1aa71 | -13.04456 | -53.71465 | 2025-05-03 01:49:00 | TERRA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 37.7 |
| 7541c4e0-bae6-3306-b725-04e7ccaa0873 | -6.6865 | -42.1252 | 2025-05-03 01:50:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 62.1 |
| f93e1ac0-ed20-37e0-b7ab-f92a6ad3c825 | -6.7053 | -42.1234 | 2025-05-03 01:50:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 77.3 |
| 8b5bd065-5daf-34b9-84aa-adc56e89e04a | -6.6865 | -42.1252 | 2025-05-03 02:00:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 64.0 |
| 977ee34a-e76a-3eab-b5b1-f66c3cbe5595 | -6.7053 | -42.1234 | 2025-05-03 02:00:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 66.6 |
| 862596c9-0954-384b-8054-dcdb020c7022 | -6.7053 | -42.1234 | 2025-05-03 02:10:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 78.7 |
| 6211611e-546d-3d16-8ac8-e59465548a67 | -6.7053 | -42.1234 | 2025-05-03 02:20:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 75.0 |
| 2f4f3375-728f-3cba-92ba-26bf71a4e210 | -6.6865 | -42.1252 | 2025-05-03 02:20:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 70.0 |
| 30267ee8-b2db-375c-8d03-6e0ce0c2b4e1 | -6.7053 | -42.1234 | 2025-05-03 02:30:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 90.4 |
| a84a426c-8fac-3427-928d-ec300d8100fd | -6.7053 | -42.1234 | 2025-05-03 02:40:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 94.0 |
| 0032335a-19fb-3ebc-9281-d9de98aeec3a | -6.7053 | -42.1234 | 2025-05-03 02:50:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 90.1 |
| 0fe57a1b-7d37-3cc4-bc43-57daf79ecf4b | -6.7053 | -42.1234 | 2025-05-03 03:00:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 84.9 |
| b0f71213-3aa6-347a-a507-e626fcf41492 | -6.7053 | -42.1234 | 2025-05-03 03:10:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 63.3 |
| 87bc75a4-3dda-3cc7-a7cb-ad7e6b01e7a1 | -9.09502 | -40.48083 | 2025-05-03 03:10:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 51856b13-ae7d-3b06-bdde-f76fdcfa204b | -8.42369 | -35.6478 | 2025-05-03 03:10:00 | NOAA-21 | BARRA DE GUABIRABA | PERNAMBUCO | Brasil | 2601300 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |


[Clique aqui para ver as próximas entradas](README2.md)
