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

## Dados Diários - Página 32

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 50b48469-fc96-3f02-80a4-2784aceb39e8 | -9.1535 | -59.4834 | 2025-08-24 04:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 88.8 |
| 6e8fea9a-1eca-3ac0-9773-24e425f4ed62 | -9.1536 | -59.464 | 2025-08-24 04:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 113.6 |
| 54ca3e1b-4961-3d80-8ddc-ab7e899b9309 | -9.1998 | -60.793 | 2025-08-24 04:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 56.0 |
| 52c2e8b3-b60a-3ab6-a778-0d427c5f5595 | -9.1722 | -59.4629 | 2025-08-24 04:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 87.5 |
| 823237af-d760-3278-aeec-fd92325b3300 | -9.1721 | -59.4823 | 2025-08-24 04:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 62.2 |
| fc09a715-ee96-30cb-9812-18489ad0bb33 | -11.5247 | -51.8474 | 2025-08-24 04:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 125.3 |
| 27393d93-3a6d-31ee-a8b3-48b7c14fd80d | -15.308 | -56.1581 | 2025-08-24 04:30:00 | GOES-19 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 64.8 |
| 47518bd2-ac81-36b2-82cb-1bdaad71deec | -9.0232 | -65.6982 | 2025-08-24 04:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 85.2 |
| fb3c3d2d-4d15-32fc-a8ee-876ae647d1de | -9.0046 | -65.6988 | 2025-08-24 04:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 67.1 |
| 512e354d-19cb-3d5c-a9b8-a2d16f273caa | -11.5245 | -51.8685 | 2025-08-24 04:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 62.8 |
| 5a1c4fcc-9ffa-3f28-847f-717c47e27c44 | -11.5437 | -51.8454 | 2025-08-24 04:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 74.6 |
| 28645958-81b2-34b1-9a64-b477a8d16abc | -4.95813 | -55.8112 | 2025-08-24 04:32:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 3b4478b1-557f-327a-b91f-38c6b60c4ce2 | -2.91754 | -48.30484 | 2025-08-24 04:32:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2ce5ca72-5318-3f92-a978-aa6a19c52aa8 | -5.657 | -45.14954 | 2025-08-24 04:32:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| ed7c245d-58cd-394d-bb28-641e35346f78 | -2.92327 | -53.69746 | 2025-08-24 04:32:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| d1141674-8546-3899-8c60-b8a67680a273 | -6.13931 | -43.1534 | 2025-08-24 04:32:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 6a22aac0-c9f2-30e1-9587-08e1b92ead69 | -5.4098 | -44.98819 | 2025-08-24 04:32:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 17.6 |
| 9d839209-47ff-3d95-b3ce-a212578be93d | -5.46102 | -42.6082 | 2025-08-24 04:32:00 | NOAA-21 | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 47a39230-411c-3247-ac6d-b5c6549743b3 | -5.66053 | -45.1501 | 2025-08-24 04:32:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 7711d6a4-e2f9-3e67-98f5-b91302508833 | -6.1896 | -45.43238 | 2025-08-24 04:32:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 8d3f3dce-dfa8-3ee1-91c5-e3ed0d826759 | -6.19877 | -44.12638 | 2025-08-24 04:32:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8af8e07d-8721-3a2f-b46f-56dbfdad64c4 | -5.65278 | -51.84013 | 2025-08-24 04:32:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 992959d3-4214-3573-8c90-f9264c72b29d | -3.45125 | -44.13619 | 2025-08-24 04:32:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| acb31038-7603-3dca-8b82-dea210c303d7 | -2.88414 | -40.24445 | 2025-08-24 04:32:00 | NOAA-21 | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| dee3d369-9d33-3966-ab79-67f1ed7559a6 | -6.2202 | -48.45938 | 2025-08-24 04:32:00 | NOAA-21 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 21b06d5f-5591-3fcd-b540-a1ce4bcdd992 | -6.50496 | -42.95472 | 2025-08-24 04:32:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ebbb3866-857d-3974-85cd-a1cd6da82282 | -2.62717 | -58.11262 | 2025-08-24 04:32:00 | NOAA-21 | ITAPIRANGA | AMAZONAS | Brasil | 1302009 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a46642b5-0811-32d4-b460-fe1df2bc0674 | -6.09145 | -43.80331 | 2025-08-24 04:32:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| af4a31a3-a6e0-3843-8e4a-7219f1acdf33 | -4.95857 | -55.8147 | 2025-08-24 04:32:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| fcd29ad9-9c20-32a5-9b39-18d3764f8a5a | -4.48873 | -47.6794 | 2025-08-24 04:32:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 87b095e2-886d-3b8e-9f4c-a92c05eefb02 | -5.58847 | -43.24758 | 2025-08-24 04:32:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5fe703f5-64f9-3ecf-bdf2-5538a94ef25b | -6.05975 | -44.26825 | 2025-08-24 04:32:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2c3e0a35-dc92-3b20-bdbc-d90e88fb3c15 | -6.43423 | -41.84705 | 2025-08-24 04:32:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 0dd826ac-182a-35f1-a3a6-fa76658cc84b | -3.79178 | -47.56619 | 2025-08-24 04:32:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 331d77a4-c184-3e72-8b0b-656002ad0ba8 | -6.31777 | -43.76572 | 2025-08-24 04:32:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9634ff2b-6682-39f9-ad03-86aca284fccb | 0.79045 | -51.96846 | 2025-08-24 04:32:00 | NOAA-21 | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7aa86002-3944-3181-800f-8bfe4a7fc8d8 | -3.51434 | -47.20923 | 2025-08-24 04:32:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| cd1b0689-815a-33e7-8ed6-f43c3077a83f | -2.29471 | -47.98137 | 2025-08-24 04:32:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6bbae2c6-6c90-3442-bac9-f0d71ca762be | -6.0421 | -44.00479 | 2025-08-24 04:32:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4c9f5788-4541-3dd8-bc74-631d580023a7 | -4.49011 | -55.57067 | 2025-08-24 04:32:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 28384691-bf50-39d8-a9c2-fdd04aa9a9f5 | -4.96256 | -55.82112 | 2025-08-24 04:32:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 18.9 |
| 4c8f2113-9d3b-3697-877e-7ba11b721034 | -6.03115 | -42.80593 | 2025-08-24 04:32:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 9c45a4a5-0a43-3818-9bea-5db9beed65ca | -2.92771 | -53.69817 | 2025-08-24 04:32:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| f3416883-b012-3912-9974-54104cc27dea | -6.10009 | -44.69139 | 2025-08-24 04:32:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dbfe5d8e-4d7f-3ca6-859a-ec4067cd7115 | -6.03833 | -44.00425 | 2025-08-24 04:32:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a267854f-bf62-3268-94e0-550829aa5d6c | -1.55473 | -54.54372 | 2025-08-24 04:32:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 00d73467-9afd-34a9-89e9-a890b2e249f1 | -5.66586 | -45.13874 | 2025-08-24 04:32:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 861cf2fe-aaa9-3a41-bca4-7673cb454d02 | -5.26502 | -42.58285 | 2025-08-24 04:32:00 | NOAA-21 | PAU D'ARCO DO PIAUÍ | PIAUÍ | Brasil | 2207793 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4baaa8c8-9bd5-34b8-915f-f933281ddddf | -3.43779 | -49.04088 | 2025-08-24 04:32:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 75d3708b-74c9-33ad-ae6b-df4fbd25a56b | -5.89012 | -43.46012 | 2025-08-24 04:32:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3ca6eed8-19bd-393d-814a-616ec301966a | -6.03064 | -42.80934 | 2025-08-24 04:32:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| bce631c1-5197-3676-81d9-57fc82a0ae5f | -4.96614 | -55.82434 | 2025-08-24 04:32:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 29.8 |
| 16a3b447-a3ec-300c-9dd6-6bb61f658464 | -6.0922 | -44.69447 | 2025-08-24 04:32:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e9987021-aa97-3037-b398-b8f781b1fe4d | -5.44872 | -49.97609 | 2025-08-24 04:32:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f0c5d9e8-92a0-394a-a870-eb1633b62ca1 | -6.21491 | -42.99929 | 2025-08-24 04:32:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| dac2ebba-abf1-3f95-a2a7-ce5c3784258f | -6.03903 | -43.9995 | 2025-08-24 04:32:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 614012c6-8efb-3bd6-a8fb-8662dd70ff70 | -6.14328 | -43.15408 | 2025-08-24 04:32:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 2db02bc4-5a92-310d-9d4e-f58fa525c70b | -4.95659 | -55.82606 | 2025-08-24 04:32:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 18.9 |
| dc483045-30ad-3288-a3ba-1be741149d6b | -2.81039 | -49.01094 | 2025-08-24 04:32:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4a07be92-47fc-3251-8219-77ed2e1ffa24 | -4.95758 | -55.82041 | 2025-08-24 04:32:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 18.9 |
| ba093c5c-491c-3dc4-b2a1-479e0bc5d173 | -2.58377 | -51.91392 | 2025-08-24 04:32:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8e4ebd68-706e-3380-b392-a7ce4aa04c32 | -2.79618 | -41.88472 | 2025-08-24 04:32:00 | NOAA-21 | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 97c42c47-2950-3f6f-9e92-a7600b7ab0ed | -2.5874 | -51.92275 | 2025-08-24 04:32:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 464eb129-e8f1-38fe-b64e-c98301e9b614 | -6.09944 | -44.6956 | 2025-08-24 04:32:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e8bccc91-529e-3c65-a1c0-8c11a4bd3adc | -5.74163 | -45.35545 | 2025-08-24 04:32:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 62103252-9564-3767-b50e-df66dd13aa03 | -4.48044 | -47.66754 | 2025-08-24 04:32:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bf678b37-f15e-3b40-810b-ee27365031df | -6.7022 | -42.97226 | 2025-08-24 04:32:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 4fa12b59-e9bf-3330-96ad-105d85a196ef | -4.94137 | -55.81999 | 2025-08-24 04:32:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 2d9ed3bb-8e7d-387b-826d-03f94267fbc9 | -5.68119 | -45.13299 | 2025-08-24 04:32:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1d4d2849-cfa2-3f7e-a028-fea166fe6f01 | -6.12669 | -43.15652 | 2025-08-24 04:32:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 4054726c-cd1f-3815-bb75-3e49339956d3 | -5.65992 | -45.15407 | 2025-08-24 04:32:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3a409f1d-d36a-37a6-8c55-f2b0eb0be599 | -3.60027 | -47.52864 | 2025-08-24 04:32:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 70999749-fed1-35c8-8e9f-97258dcbe2cd | -4.87443 | -47.40874 | 2025-08-24 04:32:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9e1169d7-be2c-3f36-95fe-86f19466c5bc | -3.78848 | -47.56568 | 2025-08-24 04:32:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 6dc6b12a-1944-337c-93d0-dbc6d5487670 | -3.38375 | -47.61125 | 2025-08-24 04:32:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f3944c86-a3db-330a-81f2-6acabce7e429 | -3.60473 | -47.52585 | 2025-08-24 04:32:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 208575a4-c898-31f4-8195-948f53787877 | -6.77851 | -44.98553 | 2025-08-24 04:32:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d112d5ac-0efb-36e9-b364-4c3e351264b7 | -6.21065 | -44.12367 | 2025-08-24 04:32:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 69a58c55-601a-33a3-9eb7-a009c4ebaf68 | -4.55257 | -43.22158 | 2025-08-24 04:32:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3c397fb6-ec60-3efe-9011-eb5172ebb849 | -4.94043 | -55.82557 | 2025-08-24 04:32:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| b285e5d9-2fd6-327e-ba81-13503800ccc0 | -3.51765 | -47.20974 | 2025-08-24 04:32:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c3931da3-d0ac-3194-ac6d-e5201d8b1342 | -3.79124 | -47.56963 | 2025-08-24 04:32:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 93134657-5dc3-3249-a9a4-efa97bfbb216 | -6.22297 | -48.46336 | 2025-08-24 04:32:00 | NOAA-21 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 71ac716f-73f3-33a2-99f8-4bca5185b7df | -4.09069 | -43.17305 | 2025-08-24 04:32:00 | NOAA-21 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0f4b8258-dfd6-395a-90b1-6beaedaf76bc | -2.58503 | -51.91195 | 2025-08-24 04:32:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 04e356e4-acc3-341a-9249-8e675d2d489c | -6.86887 | -44.40694 | 2025-08-24 04:32:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5688e4c4-3aa7-367b-af19-26d0471d25dc | -2.92701 | -53.70252 | 2025-08-24 04:32:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 9aa85533-80dc-36c5-94af-26a155d1936e | -3.5942 | -47.52418 | 2025-08-24 04:32:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 7dac4450-44bb-36b9-9fea-0c73b0dd748a | -6.77845 | -44.3121 | 2025-08-24 04:32:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b36a722b-68c9-3d28-8c35-b3eb55cc1ccf | -6.20118 | -47.84359 | 2025-08-24 04:32:00 | NOAA-21 | LUZINÓPOLIS | TOCANTINS | Brasil | 1712454 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b024e066-c869-37e4-82a4-0314636edbe6 | -3.13877 | -58.04024 | 2025-08-24 04:32:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e465601e-071a-3e1a-9348-9d70cfbf8077 | -2.62939 | -58.11395 | 2025-08-24 04:32:00 | NOAA-21 | ITAPIRANGA | AMAZONAS | Brasil | 1302009 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6b91ccee-85a8-3afc-809b-01bf87970e39 | -6.5085 | -42.95883 | 2025-08-24 04:32:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1addbe66-b58b-3d08-8e4c-c2118722e995 | -4.69672 | -43.25763 | 2025-08-24 04:32:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 92b517c9-cad6-3225-a5e6-aaa4892daf80 | -4.92839 | -47.54401 | 2025-08-24 04:32:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| fff911ae-aa8e-3021-a7bd-33279d398b0b | -3.16025 | -43.25666 | 2025-08-24 04:32:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7609f1d9-40e5-3deb-9d7c-4321dc62d93f | -6.59121 | -44.56173 | 2025-08-24 04:32:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f31e24f7-2bff-3be1-8327-b2a519603836 | -3.84192 | -55.96793 | 2025-08-24 04:32:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 66668f02-7b81-3ad8-b67d-92c6fdc6abc4 | -4.74863 | -48.64332 | 2025-08-24 04:32:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 63194ba3-3681-3b55-b2c1-358307072e8b | -5.58456 | -43.24691 | 2025-08-24 04:32:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |


[Clique aqui para ver as próximas entradas](README33.md)
