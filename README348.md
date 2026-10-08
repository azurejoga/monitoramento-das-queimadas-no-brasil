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

## Dados Diários - Página 348

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| acf1d338-6187-3db6-9b72-31393054cba4 | -2.55778 | -57.43785 | 2026-10-08 16:39:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 15.7 |
| f15f9c07-16f3-3cee-b6b3-04a74fc70ebe | -3.20855 | -44.37878 | 2026-10-08 16:39:00 | NOAA-20 | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 6.8 |
| f1e78349-2a71-3124-a55e-875d0b340f4b | -5.4846 | -43.96405 | 2026-10-08 16:39:00 | NOAA-20 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 649bf807-c549-31d4-8bdc-927318a20ba2 | -1.50544 | -47.94005 | 2026-10-08 16:39:00 | NOAA-20 | INHANGAPI | PARÁ | Brasil | 1503408 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f97c32be-59fe-35e6-8bea-4384bab6d72f | -6.07985 | -53.72352 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 45.4 |
| fe3ab872-9eaa-39f3-baff-b7d27e05eca8 | -6.82052 | -59.11494 | 2026-10-08 16:39:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 6ccbc750-e197-3479-9b67-9a61196e1a08 | -1.83112 | -55.00019 | 2026-10-08 16:39:00 | NOAA-20 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 49.8 |
| afdf5c1b-88f7-319a-91a8-0fc4933fa4b2 | -4.18956 | -40.40107 | 2026-10-08 16:39:00 | NOAA-20 | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 3.9 |
| dc0f3ff3-bab1-310d-bb8d-273f4dcea7fc | -5.35058 | -45.71399 | 2026-10-08 16:39:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 23.7 |
| c35dc1ac-a04d-390d-a181-8ac4f3510d0d | -3.4332 | -58.59916 | 2026-10-08 16:39:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 17.1 |
| 71a7d74b-80ac-3c9f-a254-e3e9e1245e87 | -6.2472 | -52.67291 | 2026-10-08 16:39:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 6767d369-d39f-3bbc-817f-c6583d612c28 | -3.6796 | -39.10891 | 2026-10-08 16:39:00 | NOAA-20 | SÃO GONÇALO DO AMARANTE | CEARÁ | Brasil | 2312403 | 23 | 33 | nan | nan | nan | Caatinga | 8.7 |
| 1d24190e-d513-36e2-86a0-857a5ee28a2e | -3.07586 | -57.99996 | 2026-10-08 16:39:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 1e816d73-1899-3d5f-8952-b9c72762f4e2 | -3.08898 | -53.93466 | 2026-10-08 16:39:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 35.5 |
| 394390b2-1176-32e7-a13a-9888eac51eb5 | -1.70694 | -55.02539 | 2026-10-08 16:39:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 15.9 |
| 1878128d-984b-3244-a75c-5da4ec616fc6 | -3.00678 | -54.10283 | 2026-10-08 16:39:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 28.5 |
| f7734947-00ea-3168-afb7-d19009f075c8 | -3.5206 | -50.35066 | 2026-10-08 16:39:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 140.7 |
| 368b0175-5ddd-3b3f-9706-4ceae20f6c9d | -6.51533 | -55.38045 | 2026-10-08 16:39:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 5b8824db-49d0-3e65-895a-919c1c58f06f | -6.10261 | -53.46418 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 98c7e468-e6f8-3119-be7c-5fbba442cf87 | -6.86604 | -59.34857 | 2026-10-08 16:39:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 20.5 |
| 63bb277e-de33-3250-89dc-4c3978017058 | -2.99908 | -53.84384 | 2026-10-08 16:39:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 18.7 |
| b8b5895a-fb7c-3545-9dc4-ec6b098e180a | -1.8012 | -57.1089 | 2026-10-08 16:39:00 | NOAA-20 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 2164d78e-56aa-3bf8-8328-552380ddbfef | -3.23345 | -57.87668 | 2026-10-08 16:39:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 29c1f5cb-66c5-341b-a4db-c5d97ee6a6db | -4.42061 | -43.72871 | 2026-10-08 16:39:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| aa8123a2-87d6-34cb-ace9-7b7b577aa909 | -2.21799 | -56.91898 | 2026-10-08 16:39:00 | NOAA-20 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 21.6 |
| 9e6ad083-d073-3452-95ab-45e599a942d0 | -3.56929 | -54.67258 | 2026-10-08 16:39:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 26.5 |
| b1cd892a-aa1e-334d-96a3-6f3de998132c | -3.94976 | -56.02372 | 2026-10-08 16:39:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 67a0e46d-9eaa-39e5-a023-79063e49ad23 | -3.43819 | -56.93756 | 2026-10-08 16:39:00 | NOAA-20 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 5107041e-9829-3344-b4e6-d88b2a2d1f17 | -5.74125 | -45.34175 | 2026-10-08 16:39:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 15.9 |
| e2e8b474-fca2-3df8-8455-6373519ffa12 | -3.17426 | -54.73655 | 2026-10-08 16:39:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 13.9 |
| 5ff6c45e-6bf8-392d-8fca-ddc081317920 | -5.37305 | -44.19345 | 2026-10-08 16:39:00 | NOAA-20 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 18.8 |
| be451381-b1f4-3e6c-8433-d8f224a3020a | -5.37422 | -44.2009 | 2026-10-08 16:39:00 | NOAA-20 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 33.8 |
| bff43c95-dca1-3cee-8224-2dac041f2b0e | -2.57077 | -56.18084 | 2026-10-08 16:39:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 15.9 |
| 9a4c2e7b-a893-3646-8341-32b989fcf4d0 | -2.99538 | -54.02739 | 2026-10-08 16:39:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 2a0afce8-2241-35c8-a439-6d2d7ea098a7 | -6.23927 | -52.87636 | 2026-10-08 16:39:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 16.0 |
| 5467ef9e-3750-31c0-afad-f6bf04841bcb | -2.18256 | -56.30368 | 2026-10-08 16:39:00 | NOAA-20 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 8ef4a8d2-fdc9-3936-b09b-d191325f177d | -3.30095 | -53.69774 | 2026-10-08 16:39:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 36.1 |
| ffb37dd0-7eb7-30e9-8b0e-eac7374c27a3 | -6.73113 | -55.05758 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 1b2cc1b6-6c21-3abc-930a-168842c38ad4 | -3.58088 | -54.68237 | 2026-10-08 16:39:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 902235bf-fdc8-3a70-af81-0dc1bdc12656 | -2.08309 | -46.56448 | 2026-10-08 16:39:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| c1330dd0-cc07-3e5d-a6f0-607e34352efb | -5.88967 | -51.19247 | 2026-10-08 16:39:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 992ff52d-e867-31fc-bba6-b48653c22e25 | -4.06928 | -51.03711 | 2026-10-08 16:39:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| aa00be17-ab86-36f0-985e-070b2a130fa5 | -1.53881 | -54.82217 | 2026-10-08 16:39:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 42.6 |
| 9c6fbb48-5715-3875-be38-fc1ed8a8db5e | -2.99845 | -54.76134 | 2026-10-08 16:39:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 0b71ab09-d778-3360-90c4-b840993b88c1 | 0.38345 | -51.15119 | 2026-10-08 16:39:00 | NOAA-20 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 2f8be489-acce-3518-bd86-dfe1fd2a1269 | -3.59149 | -54.68528 | 2026-10-08 16:39:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 2f83f05a-d518-3161-b37a-96ba11f8d046 | -3.06411 | -58.00328 | 2026-10-08 16:39:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 6.7 |
| cd8d6042-eb19-38a5-8d14-dc86685f4fb8 | -5.31122 | -45.7239 | 2026-10-08 16:39:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 117.4 |
| 59aff2ec-d165-37e3-990a-9669e0f8a6bf | -7.23991 | -55.12904 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 28.3 |
| 32b088be-4ed6-399a-abb5-cb916089f3cb | -2.56963 | -56.14874 | 2026-10-08 16:39:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 39094fc3-b457-3355-a2ac-2fa0ca543671 | -2.75142 | -54.09443 | 2026-10-08 16:39:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 835c85c6-7b52-3052-83a3-b099609ec422 | -1.32947 | -55.44125 | 2026-10-08 16:39:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 9bc270eb-b2f5-3eb6-9017-9c9bec1bf505 | -7.23681 | -55.13451 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 30.5 |
| 5b171f1a-41b5-3011-8ee8-e1892336e0c6 | -3.1442 | -54.36644 | 2026-10-08 16:39:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 35f4c4f7-8ad4-3fc3-a90f-4dd11fd8532a | -3.24973 | -57.86164 | 2026-10-08 16:39:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 12.0 |
| d7f1fec3-e592-3ec5-82f1-83620d883ad7 | -1.85873 | -57.05019 | 2026-10-08 16:39:00 | NOAA-20 | FARO | PARÁ | Brasil | 1503002 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| faa22815-38a1-3fb2-bd61-b95d3e110cb6 | -3.10709 | -57.66078 | 2026-10-08 16:39:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 92bdfa66-9afc-3b3f-8a13-a6889cd7f2b2 | -2.99948 | -41.42904 | 2026-10-08 16:39:00 | NOAA-20 | CAJUEIRO DA PRAIA | PIAUÍ | Brasil | 2202083 | 22 | 33 | nan | nan | nan | Caatinga | 7.4 |
| a4fcec7a-9579-30d0-a867-934412ed66a4 | -6.12712 | -53.04462 | 2026-10-08 16:39:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 18.0 |
| acc4eb8a-1d56-3f31-92eb-59c151650ccb | -6.73408 | -55.11987 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| e2696c36-2d68-3670-9c69-4268fea82e20 | -6.06875 | -44.65214 | 2026-10-08 16:39:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 20.0 |
| ed5c88c9-2eae-3ba8-a18e-187d074a5582 | -3.43242 | -58.59388 | 2026-10-08 16:39:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 17.1 |
| 7199d4c1-8d71-3402-a180-99fd318ad113 | -3.0051 | -54.08498 | 2026-10-08 16:39:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 38.2 |
| 37fc3394-8925-37d6-a080-203dad60c15a | -4.60976 | -55.71737 | 2026-10-08 16:39:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| a580f245-196d-3280-a719-c05907975bfa | -3.48091 | -44.39157 | 2026-10-08 16:39:00 | NOAA-20 | MIRANDA DO NORTE | MARANHÃO | Brasil | 2106755 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 5abbdf44-1797-3c13-b142-d48e5fcff76b | -3.03133 | -54.06559 | 2026-10-08 16:39:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 20.9 |
| f06530a1-b7c2-327b-80fb-0e539290beae | -3.89648 | -41.59431 | 2026-10-08 16:39:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| aea03d93-5de1-306d-9760-43bb63fca858 | -3.26982 | -54.02621 | 2026-10-08 16:39:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 486113e0-72f0-3f44-a14f-e62b83265d57 | -2.44274 | -56.54051 | 2026-10-08 16:39:00 | NOAA-20 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 28.8 |
| 49afaf12-8645-35e6-8bca-9f344412302b | -3.55747 | -44.57209 | 2026-10-08 16:39:00 | NOAA-20 | MIRANDA DO NORTE | MARANHÃO | Brasil | 2106755 | 21 | 33 | nan | nan | nan | Amazônia | 23.3 |
| d35ca0a2-7ec7-3fe9-9e00-51718d0a9317 | -3.59645 | -58.99243 | 2026-10-08 16:39:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 15.1 |
| b9c0e47b-b813-3b9c-81e0-9b3655fbb2b5 | -2.78297 | -57.63469 | 2026-10-08 16:39:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 801c166c-619f-3137-b184-c97d40057cef | -2.07354 | -46.59058 | 2026-10-08 16:39:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 8577f7a2-0167-382a-be5a-ab17d94febde | -2.61969 | -56.48101 | 2026-10-08 16:39:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 4c40fe10-6793-3a1d-937f-ac36feda8a92 | -6.45897 | -52.64764 | 2026-10-08 16:39:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| fa8e7f94-1a55-3911-82bf-80f53c953e33 | -3.09511 | -59.18836 | 2026-10-08 16:39:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 15.8 |
| 85aad5f1-7eb9-3b89-bad1-ce999997d4d3 | -3.77072 | -44.36578 | 2026-10-08 16:39:00 | NOAA-20 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 4788d20d-99fc-371c-b8fd-9c97e3406039 | -3.00524 | -54.09266 | 2026-10-08 16:39:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 27.3 |
| 7669a364-3168-3241-9d8e-75e222c7dadc | -3.10684 | -53.95748 | 2026-10-08 16:39:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 15.2 |
| 4fd4ff14-012f-3ed7-afb3-9edd6f4d4302 | -6.24271 | -52.67371 | 2026-10-08 16:39:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| a8cfc74c-6100-3e2f-941f-18bacda86c4b | -3.17344 | -54.73098 | 2026-10-08 16:39:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 13.9 |
| 1dd06aa3-f1af-3719-a0a3-91c2eddec436 | -4.96662 | -42.82553 | 2026-10-08 16:39:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 26.2 |
| 70c55f84-06ea-3ec0-a0e4-98d00b117d5f | -5.01093 | -42.39473 | 2026-10-08 16:39:00 | NOAA-20 | ALTOS | PIAUÍ | Brasil | 2200400 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 1657fbcb-7035-38b2-8d3b-4d7045e5a65f | -3.90055 | -44.13538 | 2026-10-08 16:39:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 37.2 |
| 083a8a13-3f51-316d-b203-0f0d1648fcc6 | -3.16666 | -56.82551 | 2026-10-08 16:39:00 | NOAA-20 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 8b342e75-ed4f-39ff-bbf2-db6d39947049 | -3.45434 | -58.06116 | 2026-10-08 16:39:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 12.2 |
| c63cbabd-3b13-3edb-ae45-a829ec3570ee | -1.05778 | -53.59001 | 2026-10-08 16:39:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| b86f01eb-c0a3-355e-8405-2e18122a1244 | -3.04647 | -57.41753 | 2026-10-08 16:39:00 | NOAA-20 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 2bfb4437-e6fd-3ac1-8be2-5a0ed9cd8619 | -3.17641 | -50.45222 | 2026-10-08 16:39:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 453f6f5a-2083-3aa0-8027-a7d0532defb7 | -6.14941 | -47.92484 | 2026-10-08 16:39:00 | NOAA-20 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 34.6 |
| f2f02a4a-07b3-3df2-9cf7-471b22c44f72 | -5.3758 | -45.92239 | 2026-10-08 16:39:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| ebbf074d-08cc-3d89-8bf5-11b5aa70149a | -2.59905 | -57.56573 | 2026-10-08 16:39:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 0583361e-c8dc-3561-977d-effacd09d5d8 | -5.9296 | -44.27995 | 2026-10-08 16:39:00 | NOAA-20 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 20bd7dad-187b-3bd0-9426-2aa26fdcd03e | -6.38577 | -53.28886 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 826789bb-0eb9-38ad-b41e-768faae9b039 | -4.92063 | -40.36747 | 2026-10-08 16:39:00 | NOAA-20 | TAMBORIL | CEARÁ | Brasil | 2313203 | 23 | 33 | nan | nan | nan | Caatinga | 14.1 |
| c36be574-a3e8-31cc-93f5-1a103d900653 | -2.05353 | -54.30774 | 2026-10-08 16:39:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 34.5 |
| 000571b9-8b2f-3f90-ad0f-a4dd61721c76 | -3.00936 | -54.05597 | 2026-10-08 16:39:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 29.0 |
| 78dacc98-73eb-303d-9caa-2b7c1474f769 | -2.61351 | -57.58135 | 2026-10-08 16:39:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 19.8 |
| 18b2a8bb-2d89-3f40-ae5d-a716b4ea0bd6 | -5.70908 | -53.48263 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 31.9 |
| 3a4808b1-a019-39e2-b8c9-0a86b33d944a | -3.26184 | -41.84692 | 2026-10-08 16:39:00 | NOAA-20 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Caatinga | 7.7 |


[Clique aqui para ver as próximas entradas](README349.md)
