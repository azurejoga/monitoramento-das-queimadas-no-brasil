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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 84fa9ab1-59f9-37bb-ae29-230a20f1a228 | -4.111 | -51.05409 | 2024-11-19 00:45:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 102.3 |
| 48af5a6a-6259-3f2f-b4d6-bcae01c2687d | -3.61194 | -54.22356 | 2024-11-19 00:45:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 25.8 |
| 862c7fce-47f5-3f0c-b00f-6405ad53a0d5 | -5.50797 | -46.43952 | 2024-11-19 00:45:00 | TERRA_M-M | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 946689b2-961d-328f-bef4-4898962212d9 | -1.99765 | -44.78918 | 2024-11-19 00:45:00 | TERRA_M-M | MIRINZAL | MARANHÃO | Brasil | 2106805 | 21 | 33 | nan | nan | nan | Amazônia | 6.2 |
| f0773780-913f-3bb5-a668-b8ffccfb0f67 | -2.94216 | -48.06574 | 2024-11-19 00:45:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 16.0 |
| d1940c5b-2f3e-3c1d-b272-54870eecccc5 | -2.64788 | -46.21362 | 2024-11-19 00:45:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 58eccfb5-4c54-3c7f-9052-953aba33ba67 | -1.99313 | -45.54903 | 2024-11-19 00:45:00 | TERRA_M-M | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 77eee10f-379a-3eb6-bad6-80c3fa2634ef | -2.92255 | -48.05551 | 2024-11-19 00:45:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| b75c1d6e-eea4-347f-bf3b-909d63911a6e | -2.96576 | -51.4073 | 2024-11-19 00:45:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 14.5 |
| a76e0aea-197b-3440-a94b-9c19ab6065dd | -2.68755 | -51.80448 | 2024-11-19 00:45:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 86041a0e-526b-3f5d-a195-7c75bb07d8bd | -4.9922 | -44.33773 | 2024-11-19 00:45:00 | TERRA_M-M | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 14.9 |
| ce98554f-a983-3a03-a005-a789673b0b9b | -2.85041 | -46.66832 | 2024-11-19 00:45:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 30804a6a-d3cf-35ee-a91f-8a0353aeed8b | -2.446 | -49.1528 | 2024-11-19 00:45:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 8b69dd80-b315-3840-8fc1-649a0ddc5133 | -2.51945 | -45.29454 | 2024-11-19 00:45:00 | TERRA_M-M | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 646e2431-c79a-364a-9baa-f16466cb5571 | -3.84683 | -50.69691 | 2024-11-19 00:45:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 2a4128f5-9f5f-39c6-a75e-e7cee53a0aa6 | -3.42199 | -50.26107 | 2024-11-19 00:45:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 0e198fa2-fe21-375f-b411-31eda5e33848 | -3.56646 | -51.43821 | 2024-11-19 00:45:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| d7792ffd-f3a3-3bec-bacb-ea8db31250fb | -3.32194 | -50.48908 | 2024-11-19 00:45:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 14.8 |
| 2ca43b54-ea5e-378a-a066-c665f6c2e77e | -4.99083 | -44.328 | 2024-11-19 00:45:00 | TERRA_M-M | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| ed8bc7e4-7614-31e0-ae3f-b9c29a5ddcd9 | -2.9329 | -48.06348 | 2024-11-19 00:45:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 8e31ae37-0cf7-3b76-b0e6-3af54f67ee7a | -3.8507 | -46.63969 | 2024-11-19 00:45:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 3eb92799-ed7e-3ecc-b3e6-c8111e3a46f5 | -2.44462 | -49.14261 | 2024-11-19 00:45:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 48391e0d-3403-3177-8f76-0d78fdb37d1b | -4.19662 | -46.81529 | 2024-11-19 00:45:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 568fd853-5722-3da1-911e-c4fba306d288 | -5.15099 | -48.18842 | 2024-11-19 00:45:00 | TERRA_M-M | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 97b2fcde-eaaa-3e80-bf71-b6d81b50d070 | -2.47968 | -49.11702 | 2024-11-19 00:45:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 15.5 |
| 9f87d0cd-299b-35d0-a5d9-64a3e8818847 | -3.04059 | -49.47022 | 2024-11-19 00:45:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 51.8 |
| b8511577-8792-3d86-9568-846f54825e6e | -3.55408 | -51.51658 | 2024-11-19 00:45:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 10512ebe-d571-3c2e-84f1-064b6cfc522f | -2.9677 | -51.42169 | 2024-11-19 00:45:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| e8f73b45-b46b-3320-bfc0-85b2f99eefde | -2.71228 | -46.08054 | 2024-11-19 00:45:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 7.4 |
| e69cda08-86dd-32b6-8a20-d5b2d15d5607 | -2.64995 | -48.48502 | 2024-11-19 00:45:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 761f74b7-4855-34f1-a07f-7928343c54ce | -3.43721 | -50.29641 | 2024-11-19 00:45:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 34fd04da-913a-32cf-bb38-8ad39433b10a | -3.89234 | -46.93999 | 2024-11-19 00:45:00 | TERRA_M-M | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 98b95ac4-aa04-3e75-a4e2-2675f388e8b3 | -3.55612 | -51.53159 | 2024-11-19 00:45:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 61.2 |
| 6a694b0d-61dd-3bdb-9428-07ea40eed01c | -3.7755 | -50.68569 | 2024-11-19 00:45:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 4f2d6d0e-8117-31a8-b1e1-0c26ee463792 | -4.5765 | -45.64147 | 2024-11-19 00:45:00 | TERRA_M-M | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 2eb6746f-9c33-3928-9582-4d0f20588ffb | -3.39074 | -52.81331 | 2024-11-19 00:45:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 9b00f27f-4f6d-355a-b490-2a28995b3d01 | -5.06911 | -44.23015 | 2024-11-19 00:45:00 | TERRA_M-M | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 9a2bb5be-b955-3250-b183-d2f746c51e0c | -3.89112 | -46.93112 | 2024-11-19 00:45:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 895891e1-9132-3c85-8657-bb3e3ce28a44 | -2.31956 | -45.64441 | 2024-11-19 00:45:00 | TERRA_M-M | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 10.6 |
| ccec812a-53ca-344f-8200-dbb2d94c97ba | -3.25631 | -50.39631 | 2024-11-19 00:45:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 14.9 |
| e94f985a-9f42-3370-91b4-cec10ab59dc1 | -2.93015 | -49.11765 | 2024-11-19 00:45:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 19.8 |
| 4ac387cd-be9b-3dd8-8457-f0f9ad439f93 | -3.29587 | -43.54509 | 2024-11-19 00:45:00 | TERRA_M-M | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 542239a9-ba11-3732-a070-4770832f8489 | -2.53691 | -47.33669 | 2024-11-19 00:45:00 | TERRA_M-M | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 76c70b9e-afb2-347a-a69e-d77ccc60683b | -2.86048 | -46.67587 | 2024-11-19 00:45:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| c0d2edbd-930c-321e-92e3-62587eaf5836 | -2.68432 | -46.0754 | 2024-11-19 00:45:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 9.1 |
| bf765c27-f4e5-315b-a1f0-6b96a182d979 | -2.93288 | -48.33026 | 2024-11-19 00:45:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| c1d6868d-d85f-30c5-80e4-64ffc53c176d | -4.55867 | -45.64396 | 2024-11-19 00:45:00 | TERRA_M-M | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 50b2c113-7084-3ba1-b85b-af55a9966905 | -4.30531 | -46.73997 | 2024-11-19 00:45:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 43ec0383-0381-340b-9b0a-1716d4edcb0c | -5.76591 | -46.17692 | 2024-11-19 00:45:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 8a1a0dd8-a382-33ee-a433-505173b7c953 | -2.49681 | -49.03239 | 2024-11-19 00:45:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 50.3 |
| 67280d7a-f8c9-3a7d-87bc-0628c209d2b0 | -2.79117 | -51.72186 | 2024-11-19 00:45:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 93dececf-75ab-3536-9813-9329da189dca | -2.54746 | -48.40857 | 2024-11-19 00:45:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| ae088168-2d66-3479-a5b8-4c2f12418b4d | -2.64808 | -46.15007 | 2024-11-19 00:45:00 | TERRA_M-M | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 43adc946-9aa9-30cb-933e-a0a67d79e36e | -3.36624 | -50.81289 | 2024-11-19 00:45:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 31d618a8-66bb-3b9d-86dc-0a1310b80594 | -2.57904 | -45.58892 | 2024-11-19 00:45:00 | TERRA_M-M | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 1d5abdb5-274b-3538-b077-087054b2ec84 | -4.82195 | -43.6871 | 2024-11-19 00:45:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| dc433af0-1f84-3c66-8482-735f40ba7521 | -4.36076 | -45.28719 | 2024-11-19 00:45:00 | TERRA_M-M | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | 11.8 |
| f45e4306-d5ab-3d9b-a254-efe25a9e7e4b | -2.72404 | -45.96939 | 2024-11-19 00:45:00 | TERRA_M-M | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 17.9 |
| f6945c23-447a-373e-8312-a18d3df393c9 | -2.91154 | -46.84818 | 2024-11-19 00:45:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| e6160142-f7ed-32a0-b405-65751d2087eb | -5.8492 | -46.439 | 2024-11-19 00:45:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 0fc391f4-cae9-3fbc-9122-12e52d067f9c | -3.29903 | -45.33766 | 2024-11-19 00:45:00 | TERRA_M-M | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 47.5 |
| 9da46494-75a7-3ea9-be79-b995571c8437 | -3.3324 | -50.48758 | 2024-11-19 00:45:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 32.3 |
| 19efc7eb-799f-395f-9e2c-aeca1a6093bc | -2.85511 | -49.0301 | 2024-11-19 00:45:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| a86f5b46-d837-34d9-bd92-19d985a0b2e9 | -5.60273 | -44.8822 | 2024-11-19 00:45:00 | TERRA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 2c25f6fb-6485-3632-84f3-19e876ebb7cc | -3.59273 | -43.62001 | 2024-11-19 00:45:00 | TERRA_M-M | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| a863b800-264a-3738-a793-53a6a1636764 | -2.64429 | -48.83744 | 2024-11-19 00:45:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| d9a29172-4210-3811-a62e-efe067e17d05 | -3.31454 | -51.53082 | 2024-11-19 00:45:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 91332f56-304d-3ae7-beed-8f1aa48030dc | -2.53809 | -46.21741 | 2024-11-19 00:45:00 | TERRA_M-M | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 28bb4c73-0d8f-30e5-b113-6990bc3a65a1 | -5.05515 | -48.36848 | 2024-11-19 00:45:00 | TERRA_M-M | SÃO PEDRO DA ÁGUA BRANCA | MARANHÃO | Brasil | 2111532 | 21 | 33 | nan | nan | nan | Amazônia | 7.6 |
| f532c29d-193a-37ad-858a-7abf538c57cd | -2.68671 | -51.88361 | 2024-11-19 00:45:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 15.2 |
| bcae6a1b-1251-3405-9707-d1c03b794fb5 | -5.54575 | -47.04929 | 2024-11-19 00:45:00 | TERRA_M-M | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c62f5cd1-5017-3523-8eb4-d4eebeaf0dd4 | -5.57758 | -46.34208 | 2024-11-19 00:45:00 | TERRA_M-M | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| b423f47f-b7eb-3a66-b647-d54b546fcf57 | -3.47518 | -48.2566 | 2024-11-19 00:45:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 14.8 |
| 4b28d946-0bed-3a01-b29c-404e5d55daab | -3.38225 | -50.33487 | 2024-11-19 00:45:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| a22c58d6-15ad-38b0-acb3-83f8310655c2 | -2.64287 | -46.56609 | 2024-11-19 00:45:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 1601ca44-6a33-39d1-9e27-bb82833cc51f | -3.66194 | -50.44402 | 2024-11-19 00:45:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 81f6fd23-0fb1-3a7e-8351-10712bcc013f | -4.10907 | -51.03962 | 2024-11-19 00:45:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| b4f753d6-d9a8-3bc7-ac45-ca104bc5becc | -2.98507 | -45.33128 | 2024-11-19 00:45:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 15.5 |
| 34684e0b-f132-388a-9704-159281ada859 | -2.39601 | -45.79484 | 2024-11-19 00:45:00 | TERRA_M-M | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| f1a04aac-6fae-36e7-a43e-7fe64859ab97 | -4.57776 | -45.65042 | 2024-11-19 00:45:00 | TERRA_M-M | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 5.2 |
| b5566974-0683-3789-b605-b642ceb4616b | -4.82349 | -43.69771 | 2024-11-19 00:45:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 0eca77b6-237e-3813-bef2-56d25c2ef430 | -3.6079 | -49.96758 | 2024-11-19 00:45:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| dfc6bf24-c63f-3e87-b3d5-310373b81acc | -5.63952 | -46.25527 | 2024-11-19 00:45:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7bb7b61c-d7f8-3ea3-b914-1fe62359ca83 | -3.95126 | -46.70004 | 2024-11-19 00:45:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 7.4 |
| f66a7a01-facc-3113-a183-aa8b1d8f2e25 | -3.51141 | -50.22398 | 2024-11-19 00:45:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 110.1 |
| 7a497c84-e0a1-3dd7-9884-761077697083 | -4.90953 | -44.02397 | 2024-11-19 00:45:00 | TERRA_M-M | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 12.5 |
| c4a29a05-46e7-32d1-8dd3-dc637899988a | -2.39728 | -45.80392 | 2024-11-19 00:45:00 | TERRA_M-M | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 7.0 |
| c66274a6-3fb9-319c-9bd5-845c365e1ab0 | -2.68557 | -46.08433 | 2024-11-19 00:45:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 36f05551-9ce7-3caa-949c-fdcc46e3e7fb | -3.54311 | -50.40178 | 2024-11-19 00:45:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 30829fdf-1876-33ac-9345-8f28a1059eb2 | -2.88856 | -48.27884 | 2024-11-19 00:45:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 7652115b-b0aa-3656-ad95-bf1a0319e440 | -4.38145 | -50.4935 | 2024-11-19 00:45:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 14.7 |
| ef122fe9-7385-3047-a1af-f699780fc81b | -2.6086 | -46.19198 | 2024-11-19 00:45:00 | TERRA_M-M | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 05d3913f-0b37-3cee-bb2e-0d024994dbc0 | -3.91962 | -46.4079 | 2024-11-19 00:45:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 2f41b3ae-4a2f-3875-b2bb-fc0d7bc42cff | -3.50975 | -50.23048 | 2024-11-19 00:45:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 111.5 |
| c74d5245-bb09-331f-9a48-3e7b073e9cbb | -3.0315 | -45.20404 | 2024-11-19 00:45:00 | TERRA_M-M | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 81447eb9-7845-3ba7-aeb4-591bb1a119a5 | -3.28345 | -50.52016 | 2024-11-19 00:45:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 4ab8e11b-2bf4-397a-ab82-e5468afe24ed | -3.18756 | -53.24609 | 2024-11-19 00:45:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 473ccf49-b6be-3d25-b377-3b4bca1d545f | -2.64864 | -48.47548 | 2024-11-19 00:45:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 3ee16e0c-6eb0-385a-9fc2-6188abc88128 | -3.10089 | -53.09425 | 2024-11-19 00:45:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| b885a58f-40ff-38d8-8609-9e125d89a4b0 | -2.48601 | -49.02369 | 2024-11-19 00:45:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 20.4 |


[Clique aqui para ver as próximas entradas](README9.md)
