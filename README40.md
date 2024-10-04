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

## Dados Diários - Página 40

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| edf55a60-77c0-3d08-bf53-22b8f6003fe6 | -9.0898 | -67.4997 | 2024-10-04 01:55:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 130.6 |
| b70434e4-d355-35b5-88db-2cd70206ee74 | -9.0899 | -67.4812 | 2024-10-04 01:55:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 51.7 |
| da8b72c9-ab6f-3ace-bf13-a2330eb3cfc0 | -9.1084 | -67.4993 | 2024-10-04 01:55:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 62.1 |
| 2ce93c27-015a-3771-951f-54b00bac2758 | -9.3115 | -50.8203 | 2024-10-04 01:55:59 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 120.3 |
| 8a25ef0a-77c9-36b3-a7d2-b8ad9cc37ca8 | -9.3118 | -50.7991 | 2024-10-04 01:55:59 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 160.1 |
| 43000a63-be8d-3545-82b0-52feb371e2c9 | -9.3303 | -50.8186 | 2024-10-04 01:55:59 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 123.8 |
| b7b7e8eb-b204-34b8-9e93-152fea807dea | -9.3306 | -50.7974 | 2024-10-04 01:55:59 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 138.8 |
| 24b73b98-b43e-3e98-a71c-0b2b5f5f57ad | -9.8349 | -46.7726 | 2024-10-04 01:56:01 | GOES-16 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 64.3 |
| 63136e8f-019e-30bf-ad73-2e3dc361b06f | -9.8353 | -46.7502 | 2024-10-04 01:56:01 | GOES-16 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 92.8 |
| 978b1383-9b3d-33ff-8820-405f49b30519 | -9.8542 | -46.7481 | 2024-10-04 01:56:02 | GOES-16 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 64.5 |
| b17d3204-3a45-3f84-973f-fd9f3d624ba2 | -11.0921 | -46.4843 | 2024-10-04 01:56:08 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 48.5 |
| 2f8c5319-1eb1-380e-80ef-f119140f7a76 | -11.6369 | -64.981 | 2024-10-04 01:56:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 43.9 |
| 325a7169-159e-34d5-ae24-f160428536ff | -11.8052 | -56.6024 | 2024-10-04 01:56:13 | GOES-16 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 58.4 |
| f7074636-dcb3-3ed0-aeb6-d267b0a2a892 | -11.8242 | -56.6009 | 2024-10-04 01:56:13 | GOES-16 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 116.0 |
| 45d5295f-bc5c-3086-ac05-f88af6a06f79 | -11.8244 | -56.5808 | 2024-10-04 01:56:13 | GOES-16 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 74.7 |
| 476a0446-9a9f-3a18-8cb7-c268e1e2b061 | -12.4037 | -63.0201 | 2024-10-04 01:56:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 71.1 |
| ac69cffe-2362-376b-9390-8d18c2fc5687 | -12.4038 | -63.0009 | 2024-10-04 01:56:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 53.1 |
| 551ebabb-9d94-32be-b44e-1f80603e0ddb | -12.4225 | -63.019 | 2024-10-04 01:56:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 167.2 |
| 889c4e74-8ea1-36ef-9185-603be6cc2e54 | -12.4227 | -62.9999 | 2024-10-04 01:56:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 96.5 |
| 4801666d-7186-352f-bef9-d728bad5887c | -12.4414 | -63.018 | 2024-10-04 01:56:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 51.6 |
| 06cf0e22-d2ce-3169-8fd2-01f6971c56fb | -12.4416 | -62.9988 | 2024-10-04 01:56:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 52.8 |
| ea186cd2-e162-311d-beb1-e5c2fec9541e | -12.5898 | -53.1359 | 2024-10-04 01:56:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 107.3 |
| ba8130f1-aa78-351d-a254-78a8a8bc6688 | -12.5901 | -53.115 | 2024-10-04 01:56:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 176.0 |
| 10dc8344-4db1-3f07-b634-83397a4ee3a3 | -12.6089 | -53.1338 | 2024-10-04 01:56:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 73.5 |
| 395d717d-dab1-3807-9e8f-da967f5051b2 | -12.6092 | -53.1129 | 2024-10-04 01:56:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 118.8 |
| 5bf9e228-99a3-38ec-abcc-fc1fc52043b3 | -12.6295 | -63.1225 | 2024-10-04 01:56:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 108.2 |
| de9867c1-f429-3458-859b-2b86230589ed | -12.6296 | -63.1033 | 2024-10-04 01:56:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 90.8 |
| 1319c793-ae34-3bf4-8ac7-ed51cb433ab1 | -12.6484 | -63.1214 | 2024-10-04 01:56:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 67.5 |
| f25733ae-2a5a-348a-b708-737bae140baf | -12.6486 | -63.1022 | 2024-10-04 01:56:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 87.2 |
| 8220f32f-2454-36ae-9594-5ef4219cab2b | -12.7255 | -62.9442 | 2024-10-04 01:56:19 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 64.7 |
| 314f750c-43f8-3706-a8f7-6295b6adba35 | -12.7256 | -62.925 | 2024-10-04 01:56:19 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 58.7 |
| 934cbdca-5f45-3953-aeb6-1b30223bb05f | -12.9639 | -51.1314 | 2024-10-04 01:56:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 87.1 |
| 3e0c8c52-7b02-3014-bf88-3536348eb200 | -12.9831 | -51.129 | 2024-10-04 01:56:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 296.9 |
| e9b4a12f-3287-3dca-af68-343b10b7b536 | -12.9834 | -51.1076 | 2024-10-04 01:56:19 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 116.8 |
| 6656db49-6dce-3213-ade1-622f04014dd1 | -13.0022 | -51.1266 | 2024-10-04 01:56:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 194.4 |
| 2d7b0ce5-49ad-3704-a69e-9c8b048e1df1 | -13.0026 | -51.1052 | 2024-10-04 01:56:19 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 74.7 |
| 6f478f02-b96b-3769-bcf6-2cab3cf61e12 | -13.5754 | -51.2464 | 2024-10-04 01:56:22 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 101.6 |
| 2ef83c61-f42d-3218-8417-de9ebbb45eaa | -14.004 | -44.0201 | 2024-10-04 01:56:24 | GOES-16 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 69.8 |
| 30b86719-65f9-3710-895c-223ef45d4e55 | -14.7744 | -48.0307 | 2024-10-04 01:56:29 | GOES-16 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 80.6 |
| 33545fcc-7b62-305e-ab0b-0715fc7939be | -14.7939 | -48.0275 | 2024-10-04 01:56:29 | GOES-16 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 101.1 |
| 32734d6c-708d-3fdf-bf19-656884aae445 | -16.0897 | -50.452 | 2024-10-04 01:56:36 | GOES-16 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 73.5 |
| 09dfa322-dcc9-3efc-bcca-8123e5fda6d1 | -16.1094 | -50.4489 | 2024-10-04 01:56:36 | GOES-16 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 80.4 |
| 8adbe3ea-19db-3735-9be7-b54775b0bd6d | -16.4148 | -57.4028 | 2024-10-04 01:56:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 56.0 |
| 86207c61-5dcd-33f1-8f5c-118db173bd2a | -16.4151 | -57.3823 | 2024-10-04 01:56:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 56.9 |
| 78de67b4-fc76-3eb4-bd4f-d69809d78e0b | -16.4554 | -57.2962 | 2024-10-04 01:56:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 57.6 |
| 1a267c61-5eaf-31b4-a412-48db4299c32b | -16.573 | -57.2624 | 2024-10-04 01:56:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 64.7 |
| c5b377e3-119e-3745-a043-bcc0aa1f9134 | -16.5733 | -57.2419 | 2024-10-04 01:56:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 90.5 |
| 7b28d6d5-34e1-30de-a25f-f380e7e192ce | -16.5736 | -57.2215 | 2024-10-04 01:56:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 67.9 |
| 7823b44b-0297-3542-aaa0-c1c194f869ba | -16.5783 | -58.198 | 2024-10-04 01:56:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 49.0 |
| 997c104a-b788-3e20-85ab-40e25afcd2c6 | -16.5925 | -57.2602 | 2024-10-04 01:56:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 56.5 |
| df30dc63-902b-3775-9d74-eb57d95b506a | -16.5928 | -57.2397 | 2024-10-04 01:56:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 57.6 |
| e3eeefe8-242f-3b22-a0bb-193a2c38d357 | -16.5935 | -57.1988 | 2024-10-04 01:56:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 70.5 |
| 80377ff4-c923-3688-8424-80ce70b14f5a | -16.5938 | -57.1783 | 2024-10-04 01:56:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 91.0 |
| 6d6758fc-205f-303a-98d5-95b609ba4ae7 | -16.9302 | -47.1224 | 2024-10-04 01:56:40 | GOES-16 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 58.6 |
| 4a70ccf7-22c9-360a-8a06-48c2befb5261 | -16.95 | -47.1185 | 2024-10-04 01:56:40 | GOES-16 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 51.6 |
| e4d9bbb8-211a-3756-9d94-922854fd87e0 | -16.613 | -57.1965 | 2024-10-04 01:56:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 99.3 |
| 5f67a2ed-d345-3719-9b0a-08298c19bb2b | -16.6133 | -57.176 | 2024-10-04 01:56:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 120.3 |
| 89cd8009-cdba-3eb0-b0e9-34858ea28e3a | -16.7606 | -57.7512 | 2024-10-04 01:56:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 46.5 |
| 00989c77-21f1-3920-8bde-29e9b4988ecf | -16.7859 | -57.3811 | 2024-10-04 01:56:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 63.1 |
| 67052638-f87c-3cb7-84fe-dfbcf83d67a2 | -16.8055 | -57.3788 | 2024-10-04 01:56:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 57.4 |
| 4c8e048b-77c0-350b-9695-f6e213a46b7a | -16.843 | -57.4767 | 2024-10-04 01:56:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 53.9 |
| 28aef9fe-febe-3b6a-b984-285c465d069e | -16.9087 | -55.843 | 2024-10-04 01:56:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 63.8 |
| cbbe0f6a-8bb8-3e7c-b037-9f80b1a83ff3 | -16.9091 | -55.8222 | 2024-10-04 01:56:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 59.8 |
| f5832829-00e6-3d6a-a611-81bb82e2ce9e | -16.9283 | -55.8405 | 2024-10-04 01:56:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 89.9 |
| a3c0d25c-d03c-3396-8a99-9e48d98a209d | -16.9287 | -55.8197 | 2024-10-04 01:56:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 61.7 |
| 31b0a902-d965-3b1e-9f83-9bf2ca3a2045 | -17.3643 | -42.6284 | 2024-10-04 01:56:42 | GOES-16 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 73.0 |
| eea8de7b-f28f-3c9a-9bf4-a0bb1c20dbba | -17.3844 | -42.6235 | 2024-10-04 01:56:42 | GOES-16 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 93.2 |
| 9dba2fd5-e6b8-36c5-be5d-6a394bb95499 | -17.5344 | -46.7239 | 2024-10-04 01:56:43 | GOES-16 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 69.0 |
| 924d3874-1000-3556-8636-df31d7a45e7a | -18.8413 | -42.8985 | 2024-10-04 01:56:50 | GOES-16 | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 80.4 |
| 7e6b53f1-fbc7-3cb1-b99d-1a16758f2216 | -18.8609 | -42.9182 | 2024-10-04 01:56:50 | GOES-16 | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 81.3 |
| e7c1cd1b-3cb1-3d65-9639-e58ed28220ba | -18.8617 | -42.8932 | 2024-10-04 01:56:50 | GOES-16 | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 92.9 |
| 25d0ccd0-b03b-365d-9650-80184cef3e82 | -18.8613 | -43.5837 | 2024-10-04 01:56:50 | GOES-16 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 83.1 |
| 10161a3e-4bc8-369d-85a4-9dafec82f379 | -19.2962 | -42.5779 | 2024-10-04 01:56:52 | GOES-16 | MESQUITA | MINAS GERAIS | Brasil | 3141702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 87.7 |
| e87d2768-17b2-37b5-9091-78fc773cfa50 | -19.3159 | -42.5976 | 2024-10-04 01:56:52 | GOES-16 | MESQUITA | MINAS GERAIS | Brasil | 3141702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 156.0 |
| 7e54dd4a-e29b-37c1-8da0-d24dbbb493e8 | -19.3167 | -42.5724 | 2024-10-04 01:56:52 | GOES-16 | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 156.4 |
| 1078756c-303b-3cd8-a1e7-233dff58c0e5 | -19.3363 | -42.592 | 2024-10-04 01:56:52 | GOES-16 | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 117.5 |
| 41f092e7-d09c-33ed-855e-8f53d4ef6bfc | -19.3371 | -42.5668 | 2024-10-04 01:56:52 | GOES-16 | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 105.9 |
| 97f5fb20-3d3e-3535-87d3-f00c0a9d3fce | -19.4899 | -42.8746 | 2024-10-04 01:56:53 | GOES-16 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 84.6 |
| ac02ac33-c368-355f-8e35-746ebcf8a251 | -19.6477 | -42.3808 | 2024-10-04 01:56:54 | GOES-16 | BOM JESUS DO GALHO | MINAS GERAIS | Brasil | 3107802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 90.7 |
| cdddd2cd-7e12-38ba-9f6f-302c934db0da | -19.8516 | -42.3738 | 2024-10-04 01:56:55 | GOES-16 | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 215.0 |
| 98a64137-cb34-3cbc-bfc4-95c4c225cc58 | -19.8524 | -42.3484 | 2024-10-04 01:56:55 | GOES-16 | BOM JESUS DO GALHO | MINAS GERAIS | Brasil | 3107802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 129.9 |
| 031c7586-5b29-3fc6-adee-3d37b02ec578 | -19.8721 | -42.368 | 2024-10-04 01:56:55 | GOES-16 | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 112.2 |
| f9d0d8c8-f74c-30be-bfb8-51ad99a14f89 | -20.121 | -43.5219 | 2024-10-04 01:56:56 | GOES-16 | SANTA BÁRBARA | MINAS GERAIS | Brasil | 3157203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 85.1 |
| 30c5e185-b905-3943-be65-5ed332cb9ab6 | -20.1218 | -43.4969 | 2024-10-04 01:56:56 | GOES-16 | CATAS ALTAS | MINAS GERAIS | Brasil | 3115359 | 31 | 33 | nan | nan | nan | Mata Atlântica | 74.6 |
| e4d7fe4c-a3a2-3a06-9720-b72cb8ac661e | -21.7981 | -48.3926 | 2024-10-04 01:57:06 | GOES-16 | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 129.2 |
| d97bb824-3e1a-3cca-a5f3-a6b0df0f09b6 | -21.7988 | -48.3691 | 2024-10-04 01:57:06 | GOES-16 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 197.3 |
| c9e01b5b-0622-32c7-9d8b-d101d58a169e | -21.8175 | -48.4346 | 2024-10-04 01:57:06 | GOES-16 | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 82.3 |
| 90c9893f-cf17-31db-8917-6ab14394d9c1 | -21.8189 | -48.3876 | 2024-10-04 01:57:06 | GOES-16 | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 92.1 |
| 83eb91ff-8f15-3131-9d05-b265cdcb6e80 | -21.8196 | -48.3641 | 2024-10-04 01:57:06 | GOES-16 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 147.7 |
| dc4b4548-141b-3a55-9621-3bff45fdfb3e | -21.8383 | -48.4296 | 2024-10-04 01:57:06 | GOES-16 | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 84.7 |
| 4bbcf205-ce1b-3742-99ae-3df8debe9d21 | -22.2684 | -51.4941 | 2024-10-04 01:57:09 | GOES-16 | PIRAPOZINHO | SÃO PAULO | Brasil | 3539202 | 35 | 33 | nan | nan | nan | Mata Atlântica | 110.3 |
| 9af3c9d4-9971-31b7-822e-f8660371bc04 | -22.269 | -51.4714 | 2024-10-04 01:57:09 | GOES-16 | PIRAPOZINHO | SÃO PAULO | Brasil | 3539202 | 35 | 33 | nan | nan | nan | Mata Atlântica | 93.0 |
| 373e634f-f0ac-3bfa-88b6-f6fe74b7d763 | -21.29 | -48.87 | 2024-10-04 02:03:23 | MSG-03 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 887bc0e6-7730-376a-9619-2c43afbc149c | -4.67 | -45.91 | 2024-10-04 02:05:01 | MSG-03 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| c0686e9e-ca7d-3c32-a6c4-be0c4844cbdd | -4.67 | -45.86 | 2024-10-04 02:05:01 | MSG-03 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| e96c63dd-ff78-3074-8c07-6827cdba1636 | -4.7 | -45.91 | 2024-10-04 02:05:01 | MSG-03 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| aefb12aa-6c49-3a1a-8dff-cb0d61238f0b | -4.7 | -45.86 | 2024-10-04 02:05:01 | MSG-03 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 5287ebac-1fb8-30e6-acbb-07199768f9fe | -3.2349 | -50.3695 | 2024-10-04 02:05:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 69.9 |
| b366df06-3861-3c7e-9408-d33a56030469 | -3.2534 | -50.3689 | 2024-10-04 02:05:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 76.3 |
| a20d99af-da93-3760-a129-9d36a996ffdb | -3.2899 | -50.4725 | 2024-10-04 02:05:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 127.2 |


[Clique aqui para ver as próximas entradas](README41.md)
