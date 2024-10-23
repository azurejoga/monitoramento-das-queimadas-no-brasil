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
| b6070dfb-7f09-3a09-ae86-545608df78a5 | -5.83647 | -43.6592 | 2024-10-23 00:48:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 2fef42c0-bc3e-39d1-aadd-391791b7a9e4 | -5.83497 | -43.6489 | 2024-10-23 00:48:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 6d4c7d39-d8db-377f-a3a4-619375deac83 | -5.7527 | -39.78081 | 2024-10-23 00:48:00 | TERRA_M-M | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 23.0 |
| 9242cdb2-6b27-35af-8879-b5f8a2270212 | -5.70647 | -43.26469 | 2024-10-23 00:48:00 | TERRA_M-M | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 96fa6c33-ce32-3a60-b459-e3480ff1d945 | -5.69771 | -42.5005 | 2024-10-23 00:48:00 | TERRA_M-M | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 16.3 |
| 9609098e-6263-38d2-8d20-120724aa8309 | -5.6498 | -43.23446 | 2024-10-23 00:48:00 | TERRA_M-M | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 8588d3a9-a1cb-310f-bfcb-5688cf052603 | -5.57509 | -43.20082 | 2024-10-23 00:48:00 | TERRA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 5dc4dd85-8317-3bb2-aa86-ca19b6efaf7f | -5.57503 | -43.26799 | 2024-10-23 00:48:00 | TERRA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 34.0 |
| 491658b9-382b-3031-ba9b-27f02ccf2ee9 | -5.57341 | -43.25705 | 2024-10-23 00:48:00 | TERRA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 209.1 |
| 48ace0de-a802-3749-9447-b095838d229b | -5.57179 | -43.24608 | 2024-10-23 00:48:00 | TERRA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 98b14bd7-ee69-31ca-82e5-9a3dd472a8a6 | -5.57177 | -43.26365 | 2024-10-23 00:48:00 | TERRA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 78.4 |
| 05a95a6c-1897-347b-9a72-11a091dd79ed | -5.57022 | -43.2527 | 2024-10-23 00:48:00 | TERRA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 100.1 |
| 071e2655-09ef-398b-9e3d-b508a4af7f90 | -5.51381 | -43.71009 | 2024-10-23 00:48:00 | TERRA_M-M | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 21386ae9-1ba2-3b97-9217-378228064ed8 | -5.51234 | -43.69979 | 2024-10-23 00:48:00 | TERRA_M-M | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 29.2 |
| 153d36a6-b6b8-31b8-a8b7-87e755a5ae37 | -5.51087 | -43.68951 | 2024-10-23 00:48:00 | TERRA_M-M | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 70f38e4e-f329-3c27-9e9b-b4acf36e5e3f | -5.50316 | -43.49843 | 2024-10-23 00:48:00 | TERRA_M-M | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 575cc88c-ec76-31e7-888b-a92f448762ef | -5.50284 | -43.70121 | 2024-10-23 00:48:00 | TERRA_M-M | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 80097612-c1d7-3b46-911a-b1c9a166a274 | -5.48738 | -43.66129 | 2024-10-23 00:48:00 | TERRA_M-M | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 22.0 |
| 1cc2daa7-91de-3d75-82d4-3b420c2c2761 | -5.26539 | -41.20267 | 2024-10-23 00:48:00 | TERRA_M-M | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 23.0 |
| 18096a56-8c72-3a5b-80f2-b1c51804b32f | -5.26329 | -41.19651 | 2024-10-23 00:48:00 | TERRA_M-M | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 44.8 |
| f984fdf3-7f27-39ab-bc41-365b0c62c877 | -5.2632 | -41.18759 | 2024-10-23 00:48:00 | TERRA_M-M | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 32.6 |
| e8fdae1e-b80d-3ab4-8f1a-7889a7398b55 | -5.26098 | -41.18143 | 2024-10-23 00:48:00 | TERRA_M-M | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 15.0 |
| ffd1587c-cd09-3700-a605-abeecd4a1814 | -5.22983 | -43.58953 | 2024-10-23 00:48:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| f4554531-1ee2-3d51-a76f-922f4e9fcf86 | -5.22606 | -43.19792 | 2024-10-23 00:48:00 | TERRA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 28.9 |
| d804bfa3-32d9-38d3-96cf-df86848841a0 | -5.22445 | -43.18688 | 2024-10-23 00:48:00 | TERRA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 143.0 |
| 6fb593ba-b97c-3a2b-aef0-03524407159b | -5.16205 | -43.96267 | 2024-10-23 00:48:00 | TERRA_M-M | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 87853bfc-3847-3e40-b981-8f2470d33e95 | -5.15408 | -43.97401 | 2024-10-23 00:48:00 | TERRA_M-M | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 32f5b398-24bd-3cfd-af93-9902e48efb9f | -5.15263 | -43.96397 | 2024-10-23 00:48:00 | TERRA_M-M | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 23.2 |
| efcbe4d9-cc7b-3021-9df5-f8038f63807e | -4.92174 | -41.98027 | 2024-10-23 00:48:00 | TERRA_M-M | JATOBÁ DO PIAUÍ | PIAUÍ | Brasil | 2205276 | 22 | 33 | nan | nan | nan | Caatinga | 11.8 |
| 7799d8ef-e75f-3541-8bb0-9b3e7c3a892e | -4.9197 | -41.96674 | 2024-10-23 00:48:00 | TERRA_M-M | JATOBÁ DO PIAUÍ | PIAUÍ | Brasil | 2205276 | 22 | 33 | nan | nan | nan | Caatinga | 7.0 |
| 9d926970-04b1-3003-95b0-58074e4c881d | -4.9169 | -41.9728 | 2024-10-23 00:48:00 | TERRA_M-M | JATOBÁ DO PIAUÍ | PIAUÍ | Brasil | 2205276 | 22 | 33 | nan | nan | nan | Caatinga | 14.6 |
| b6f0ae34-793e-3680-a087-edf9301005c8 | -4.71862 | -42.66327 | 2024-10-23 00:48:00 | TERRA_M-M | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 19.8 |
| 08626140-2cbf-3c75-9c21-4835505d3753 | -4.40872 | -43.64525 | 2024-10-23 00:48:00 | TERRA_M-M | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 7c5b3a15-ecdb-38b8-a7db-f8a34e8d03c2 | -4.05971 | -43.98828 | 2024-10-23 00:48:00 | TERRA_M-M | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 43f9a4d8-2b17-3f1a-bfcd-9574d72a91f2 | -3.84786 | -43.99959 | 2024-10-23 00:48:00 | TERRA_M-M | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| feca884e-bce4-35ee-866d-33123aaf3d94 | -3.8037 | -42.55363 | 2024-10-23 00:48:00 | TERRA_M-M | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Cerrado | 7.0 |
| f3504128-e77d-3a68-806c-aeb7dac7e8ab | -3.71528 | -41.68993 | 2024-10-23 00:48:00 | TERRA_M-M | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 145.1 |
| 5b63822b-ee84-39c0-b55f-aed2f5f68de6 | -3.71309 | -41.67511 | 2024-10-23 00:48:00 | TERRA_M-M | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 34.9 |
| 3bf40b32-6108-3b6d-acf8-5269538ac409 | -3.30667 | -43.51627 | 2024-10-23 00:48:00 | TERRA_M-M | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 11.2 |
| ded037b1-3ab8-3d7b-bec0-b3462c416c29 | -7.98741 | -50.68724 | 2024-10-23 00:48:00 | TERRA_M-M | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 692e6fba-3fcc-3a74-8397-fc40148e66f3 | -7.98545 | -50.67168 | 2024-10-23 00:48:00 | TERRA_M-M | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 24.8 |
| 76b6c285-ae8c-352d-9493-f0f1d54a3f0f | -7.97661 | -50.67851 | 2024-10-23 00:48:00 | TERRA_M-M | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 13.2 |
| ad15a677-25fa-3de6-a106-253141c5a213 | -7.97426 | -49.69403 | 2024-10-23 00:48:00 | TERRA_M-M | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| c46566c4-0458-3d1d-a548-3d009c6826c5 | -7.67578 | -47.30844 | 2024-10-23 00:48:00 | TERRA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 13.5 |
| c6977fdb-7cb9-33f2-8d94-537888cf2528 | -7.45052 | -49.65497 | 2024-10-23 00:48:00 | TERRA_M-M | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| bf34bd62-062c-39a8-b2d9-a9ccb69b5d44 | -7.44881 | -49.6422 | 2024-10-23 00:48:00 | TERRA_M-M | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 23.6 |
| 73ceb5aa-60af-35ee-a9af-3880951f0b8f | -7.42434 | -46.61877 | 2024-10-23 00:48:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 28.2 |
| e4452400-9ffe-3da3-986f-59b2017cbdeb | -7.42309 | -46.60973 | 2024-10-23 00:48:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c28d08bf-d523-3449-b502-7a4282b1593f | -7.41541 | -46.62001 | 2024-10-23 00:48:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| caa093e0-bf58-31d6-841c-255fd7e9911c | -7.32178 | -45.2845 | 2024-10-23 00:48:00 | TERRA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 97798b34-cf9d-332f-90f5-be0f41865abe | -7.31293 | -45.28578 | 2024-10-23 00:48:00 | TERRA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 12.9 |
| cc8cac80-07a3-3631-9093-f748b308ec76 | -7.17434 | -45.14803 | 2024-10-23 00:48:00 | TERRA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 18.2 |
| d92ab3a4-0cce-39e8-8e7c-6b3e7ccbb0fd | -7.17308 | -45.13908 | 2024-10-23 00:48:00 | TERRA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 89.2 |
| 860e716f-ad96-3be6-9edf-266217ea0956 | -7.17181 | -45.13008 | 2024-10-23 00:48:00 | TERRA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 07b70ac2-a88d-3b30-92aa-20cd231f7543 | -7.16546 | -45.14926 | 2024-10-23 00:48:00 | TERRA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 69b36d94-9ed7-3805-9228-b932c8e9f9f2 | -7.1642 | -45.14035 | 2024-10-23 00:48:00 | TERRA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 51.0 |
| e53836a1-e141-3b8d-8aaa-c976600859a4 | -7.16294 | -45.13142 | 2024-10-23 00:48:00 | TERRA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 0e7aa550-8dd2-3b1c-92ea-6ca463791bc9 | -7.13445 | -49.51051 | 2024-10-23 00:48:00 | TERRA_M-M | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 4872c82c-97a8-3f22-ba24-d8cc8fb6cdee | -7.05103 | -46.44242 | 2024-10-23 00:48:00 | TERRA_M-M | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 6bb86965-5d67-3ce5-a23d-d8d88ddb4187 | -7.01042 | -49.34642 | 2024-10-23 00:48:00 | TERRA_M-M | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 14.1 |
| ad293e4b-3a25-346d-91d1-1a11f19d2ff9 | -7.00883 | -49.33442 | 2024-10-23 00:48:00 | TERRA_M-M | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 1ce536e4-caa1-3574-844e-cc8762818794 | -7.00497 | -46.71162 | 2024-10-23 00:48:00 | TERRA_M-M | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| eeb9b940-6815-39d2-a961-5c0211be2d24 | -6.94256 | -45.20926 | 2024-10-23 00:48:00 | TERRA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 11.8 |
| e780e352-2fa4-38fb-97c6-b63f7bf2774b | -6.67325 | -46.37501 | 2024-10-23 00:48:00 | TERRA_M-M | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 06ba5ab6-482a-3cab-b351-9e969b78fb16 | -6.51553 | -47.03949 | 2024-10-23 00:48:00 | TERRA_M-M | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 27.0 |
| 9ac8ea9d-e001-303e-b0cd-eef295f0a0ae | -6.35299 | -47.13072 | 2024-10-23 00:48:00 | TERRA_M-M | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 78318ead-ee0c-3afc-9ebf-28be5249ef16 | -6.35173 | -47.12156 | 2024-10-23 00:48:00 | TERRA_M-M | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 57a2200c-2b5f-3998-bb4f-b343740044ce | -6.2631 | -44.96415 | 2024-10-23 00:48:00 | TERRA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| dbe83de0-e820-3976-a638-dc5b83770b26 | -6.25785 | -44.15253 | 2024-10-23 00:48:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 21.0 |
| 2f6d1967-bb26-3633-a0ce-55653b259a83 | -6.25644 | -44.14281 | 2024-10-23 00:48:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 45.8 |
| 79b7692d-c5bf-3f4e-9d20-2cc79dc5e51a | -6.24985 | -44.1501 | 2024-10-23 00:48:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 22.5 |
| ed74d496-33b9-39bc-b0d0-e7abe58b279f | -6.24848 | -44.14039 | 2024-10-23 00:48:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 9c61ec80-5ed6-3d6d-a20e-ea6fd1adbf48 | -6.09581 | -46.13233 | 2024-10-23 00:48:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| b0eea3da-6b0e-3efb-902f-2a1c3be650a4 | -6.07793 | -44.63158 | 2024-10-23 00:48:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 680385a2-b1d7-38ac-8161-a5f4fbcc2a59 | -6.06888 | -44.63289 | 2024-10-23 00:48:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 24.7 |
| 79a015c9-584a-3904-a4eb-1c30bccff1ab | -6.06756 | -44.62363 | 2024-10-23 00:48:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 276b16e5-42cd-316a-bb5f-b314026298a7 | -5.85951 | -44.52315 | 2024-10-23 00:48:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 17.3 |
| e0555bb9-7b81-3eb2-aca0-d4f5e725d5fd | -5.84342 | -46.24033 | 2024-10-23 00:48:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 3d42bfa7-162e-335f-befe-c5bfebc4bc6e | -5.76734 | -45.5663 | 2024-10-23 00:48:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| ff9a14ba-056f-3cb6-a07a-93966112fd66 | -0.12267 | -51.65573 | 2024-10-23 00:50:00 | TERRA_M-M | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 18.0 |
| 808c04db-2445-3a48-80b1-b80cae9b8926 | -0.12078 | -51.64198 | 2024-10-23 00:50:00 | TERRA_M-M | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 16.8 |
| 3dc798b9-a3d9-39d6-973f-9129adca01d5 | -0.12063 | -51.6624 | 2024-10-23 00:50:00 | TERRA_M-M | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 7.7 |
| cb2d4890-6639-3a5c-b929-9792a63d78ed | -0.11864 | -51.64865 | 2024-10-23 00:50:00 | TERRA_M-M | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 32.4 |
| f9e18f57-1725-344a-8bd6-10b90d71fd92 | -0.11176 | -51.65728 | 2024-10-23 00:50:00 | TERRA_M-M | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 0fc9996b-5c09-3d3f-bacd-b33cdfa2fd38 | 1.84778 | -50.49771 | 2024-10-23 00:50:00 | TERRA_M-M | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 5243b243-4711-3570-bf47-3d469bd54595 | 1.80068 | -50.48001 | 2024-10-23 00:50:00 | TERRA_M-M | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 60c21fbf-7a15-3edb-951a-5d35164f9747 | -1.388 | -51.9867 | 2024-10-23 00:55:14 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 67.3 |
| f68de660-7e94-30b1-9d17-cd22625fe5b9 | -2.5224 | -54.1193 | 2024-10-23 00:55:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 57.6 |
| b6f1b71c-8430-3972-bdee-f81a86396464 | -2.5225 | -54.0992 | 2024-10-23 00:55:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 69.5 |
| 2ef7675a-3d93-31fc-8059-bb9691dd0bcc | -2.7589 | -49.3072 | 2024-10-23 00:55:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 49.9 |
| 91b09b40-a719-31b2-a297-28fcf83ab18c | -3.109 | -45.3194 | 2024-10-23 00:55:24 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 68.0 |
| 68188363-5661-39fb-92be-e1d964fce731 | -3.1091 | -45.2968 | 2024-10-23 00:55:24 | GOES-16 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 97.8 |
| ebe21128-83f7-30d6-a052-1c9307749c32 | -3.0917 | -54.1666 | 2024-10-23 00:55:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 92.3 |
| b4d21398-3a40-3e1e-b27d-357f8076cd61 | -3.0918 | -54.1465 | 2024-10-23 00:55:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 75.5 |
| 3ccce973-8dfb-3368-a593-96e9cd2c287a | -3.1276 | -45.3186 | 2024-10-23 00:55:24 | GOES-16 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 60.9 |
| 4ab7b835-304d-3aa2-a81b-ba8749338770 | -3.1277 | -45.2961 | 2024-10-23 00:55:24 | GOES-16 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 84.8 |
| 90b2e381-4b38-3dc6-ab64-0bf94d009a62 | -3.1101 | -54.1661 | 2024-10-23 00:55:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 89.8 |
| dbab24bf-64ae-3fbb-9be7-cc6f6eb8351c | -3.1102 | -54.146 | 2024-10-23 00:55:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 68.8 |
| d3a31211-d6bb-3286-8ae6-30523d9bea90 | -3.5307 | -54.7556 | 2024-10-23 00:55:26 | GOES-16 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 55.8 |
| c581eeb7-b729-3962-b01c-cb336ad96822 | -3.5307 | -54.7356 | 2024-10-23 00:55:26 | GOES-16 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 82.5 |


[Clique aqui para ver as próximas entradas](README9.md)
