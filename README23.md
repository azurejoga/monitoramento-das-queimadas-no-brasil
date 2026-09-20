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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 946352de-9e63-34ac-aa23-3783537669f8 | -3.591 | -47.35707 | 2026-09-20 04:17:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 7466c430-32b0-3674-a2f7-4ac793854c4b | -2.25221 | -48.75299 | 2026-09-20 04:17:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 83e2a4fa-c27a-3264-8d20-1afc24654d5e | -4.84532 | -40.52164 | 2026-09-20 04:17:00 | NPP-375D | NOVA RUSSAS | CEARÁ | Brasil | 2309300 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 089d8e4e-9d54-3fe9-8b1b-099bdd704cb9 | -3.35776 | -42.36329 | 2026-09-20 04:17:00 | NPP-375D | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 1a5c887e-c201-39a2-92e9-ddfc0fe49e30 | -4.68144 | -40.14382 | 2026-09-20 04:17:00 | NPP-375D | CATUNDA | CEARÁ | Brasil | 2303659 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 1f258469-9210-3058-b382-a2a296354601 | -3.56711 | -43.48038 | 2026-09-20 04:17:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 097523fd-7a6e-3591-8942-d2ce18d30fae | -3.35416 | -50.44827 | 2026-09-20 04:17:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b5ef5018-fcf6-32eb-aa86-78b903e67e14 | -3.56648 | -43.48433 | 2026-09-20 04:17:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 67324c54-f71c-3821-a9a8-f9b5475b8277 | -3.38022 | -39.20269 | 2026-09-20 04:17:00 | NPP-375D | PARAIPABA | CEARÁ | Brasil | 2310258 | 23 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 6e26dd75-d55e-379f-b76c-3f03bf1c3578 | -3.40169 | -50.40168 | 2026-09-20 04:17:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a15d88af-9e82-30c7-be84-a4927deb9341 | -5.10496 | -37.68954 | 2026-09-20 04:17:00 | NPP-375D | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 9d25b94f-4520-3bf5-8074-fd4cae85986f | -3.34839 | -42.7721 | 2026-09-20 04:17:00 | NPP-375D | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 815582a6-db7c-3a53-a26a-2791e4cbe4da | -1.31483 | -49.27755 | 2026-09-20 04:17:00 | NPP-375D | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2979c60f-6f68-3c13-a350-cf5bbfdac59e | -3.09316 | -48.67864 | 2026-09-20 04:17:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f6fad084-195c-38d6-a1d0-8e31affc9755 | -3.37566 | -50.45572 | 2026-09-20 04:17:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| dac7b42e-4f54-332f-9546-857af585a1b3 | -3.50788 | -43.35425 | 2026-09-20 04:17:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 880cebfd-4a46-3650-9858-1439473cfcbc | -3.56294 | -43.48376 | 2026-09-20 04:17:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 30293373-4e47-3f56-9e40-41a018578b46 | -2.3047 | -48.40014 | 2026-09-20 04:17:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 22d9b31f-8c1f-3d13-896b-0c54dc3497ef | -2.84009 | -49.5182 | 2026-09-20 04:17:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d1af2e2b-4d79-3293-9993-12a51c89ce84 | -2.4509 | -49.21579 | 2026-09-20 04:17:00 | NPP-375D | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 21e0acb2-74dc-38bb-9bbf-6c52223444dd | -3.57127 | -43.47699 | 2026-09-20 04:17:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0b1a959f-9bc2-34c9-a866-9b2f5b2ce14a | -3.40717 | -39.16538 | 2026-09-20 04:17:00 | NPP-375D | PARAIPABA | CEARÁ | Brasil | 2310258 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 8f09f379-0349-3e2d-b32c-e3ca70910e06 | -3.37505 | -50.45937 | 2026-09-20 04:17:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 260caec8-97f9-3bfd-8e1d-f8586c885014 | -5.57641 | -36.25769 | 2026-09-20 04:17:00 | NPP-375D | PEDRO AVELINO | RIO GRANDE DO NORTE | Brasil | 2409704 | 24 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 838337d6-16b4-35c1-a9a2-dbcd22a5f63f | -2.63804 | -54.69398 | 2026-09-20 04:17:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| cbcf3d5d-64b4-3706-9bac-62e43d0c6e5c | -3.58847 | -47.35733 | 2026-09-20 04:17:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 5d7857fd-6512-32cf-a8ec-88e8070ff625 | -4.62207 | -42.84194 | 2026-09-20 04:17:00 | NPP-375D | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b10cdcf1-8fb0-347b-886c-2767785fe62f | -4.56241 | -42.97235 | 2026-09-20 04:17:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| eceb60c9-b0bd-3ade-a8e6-56ac11b6f418 | -3.37014 | -50.45474 | 2026-09-20 04:17:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d95253a9-effa-307c-be12-d089232da205 | -3.56774 | -43.47643 | 2026-09-20 04:17:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b7b4453e-2ded-3883-9597-548fca0a1755 | -3.35968 | -50.44926 | 2026-09-20 04:17:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6e56beb0-42ca-3d7a-8ab2-8967a5cd30a7 | -2.17028 | -48.32111 | 2026-09-20 04:17:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 128612a7-74c8-3d0b-b3cc-68b16882ca6c | -3.8756 | -40.73221 | 2026-09-20 04:17:00 | NPP-375D | MUCAMBO | CEARÁ | Brasil | 2309003 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| ccf35d6f-f4e0-3923-817e-37247d604ac4 | -3.68449 | -38.81653 | 2026-09-20 04:17:00 | NPP-375D | CAUCAIA | CEARÁ | Brasil | 2303709 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| a9a3885d-eee9-3484-b954-fd0965e93951 | -3.04334 | -46.92714 | 2026-09-20 04:17:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 84cd56b8-0a57-33ac-9c22-1747a7568ea2 | -2.45608 | -49.21662 | 2026-09-20 04:17:00 | NPP-375D | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| dce59ea5-867a-3591-88a8-d9ebac86931b | -2.45141 | -49.21275 | 2026-09-20 04:17:00 | NPP-375D | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 42a4f3cc-9867-3914-aa44-99c2d0940b46 | -3.84848 | -45.42454 | 2026-09-20 04:17:00 | NPP-375D | SANTA INÊS | MARANHÃO | Brasil | 2109908 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 2155ae8c-52f8-3689-9506-3802fca9beaa | -4.8481 | -40.52565 | 2026-09-20 04:17:00 | NPP-375D | NOVA RUSSAS | CEARÁ | Brasil | 2309300 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| cc97e157-12d8-3a85-b373-794183e7e151 | -3.37806 | -50.44139 | 2026-09-20 04:17:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8f986228-04cb-3ce4-b52f-83f7f860a76f | -5.10563 | -37.68518 | 2026-09-20 04:17:00 | NPP-375D | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 1.0 |
| dc7dc753-46d2-37f9-a793-d6e442b6ad22 | -4.84422 | -40.52861 | 2026-09-20 04:17:00 | NPP-375D | NOVA RUSSAS | CEARÁ | Brasil | 2309300 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 11999ac1-0fc4-36f1-b4bd-69b761b7a804 | -2.82227 | -46.70921 | 2026-09-20 04:17:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ad704d39-ff6b-3397-a833-ff390eda0a43 | -4.56927 | -42.97346 | 2026-09-20 04:17:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| c84b6086-e1df-39d4-852a-4b83d84ffa68 | -2.14319 | -50.9064 | 2026-09-20 04:17:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5e9ea0f2-3d13-35dc-90bd-a283d0f18f45 | -4.84477 | -40.52513 | 2026-09-20 04:17:00 | NPP-375D | NOVA RUSSAS | CEARÁ | Brasil | 2309300 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| ef299c4d-eb47-3047-b9b7-6366badcce69 | -5.10933 | -37.68574 | 2026-09-20 04:17:00 | NPP-375D | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 1.0 |
| fc20c1b2-1d2e-309e-8e65-b2dbf073c269 | -3.38356 | -50.44246 | 2026-09-20 04:17:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 2cdb91a9-b41d-382f-be43-0be72f0fa039 | -3.82178 | -40.68477 | 2026-09-20 04:17:00 | NPP-375D | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 64b2320e-3b58-3742-a731-3a986d8e5c43 | -3.34495 | -42.77156 | 2026-09-20 04:17:00 | NPP-375D | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 5465ac86-885b-3373-bcb8-f2cc75034cc5 | -2.14385 | -50.90231 | 2026-09-20 04:17:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c2ee805c-a9b0-3aa3-badf-6d8838582abe | -2.86511 | -49.62768 | 2026-09-20 04:17:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 44610288-064c-3072-bc87-d5d3010c8051 | -3.40781 | -50.39895 | 2026-09-20 04:17:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6986490b-3dfc-35bc-907d-87b049c907f9 | -1.49773 | -48.93923 | 2026-09-20 04:17:00 | NPP-375D | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bb4bcccd-d9c0-3e20-b7bb-bb36f148c237 | -3.13097 | -44.47514 | 2026-09-20 04:17:00 | NPP-375D | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 0.2 |
| 9edeae35-b9a9-3d2f-a0a6-b982fc3e7a70 | -4.58938 | -40.57748 | 2026-09-20 04:17:00 | NPP-375D | NOVA RUSSAS | CEARÁ | Brasil | 2309300 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 59380fb3-7cdb-364b-aa1c-2c2d849f1c51 | -3.5719 | -43.47305 | 2026-09-20 04:17:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7a103208-20f9-380a-b7b4-80668f5dbf1f | -5.24632 | -38.17329 | 2026-09-20 04:17:00 | NPP-375D | TABULEIRO DO NORTE | CEARÁ | Brasil | 2313104 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 93cc50d9-d1cf-3235-ac82-38f55860e04e | -2.1907 | -48.38008 | 2026-09-20 04:17:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d67e4bd4-bed2-314a-85c3-116222fabbbd | -3.44306 | -44.30569 | 2026-09-20 04:17:00 | NPP-375D | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| abd197a1-eb4b-3d22-b962-a654909f9268 | -4.33308 | -40.18713 | 2026-09-20 04:17:00 | NPP-375D | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 062e0358-9cca-355e-80c1-36e4192af6ff | -3.12651 | -44.47898 | 2026-09-20 04:17:00 | NPP-375D | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 52f9c97c-e5ba-3a51-aced-1b02c17cc09e | -4.56584 | -42.97291 | 2026-09-20 04:17:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dbd38157-b095-350a-a2e0-bd4c4e839941 | -3.1697 | -48.61265 | 2026-09-20 04:17:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 2e600ed5-62ac-3900-bb0c-e607860008a1 | -4.77253 | -37.74628 | 2026-09-20 04:17:00 | NPP-375D | JAGUARUANA | CEARÁ | Brasil | 2307007 | 23 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 1f467da0-07ac-34dd-8218-20839a5d316f | -3.17137 | -48.61464 | 2026-09-20 04:17:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| e849e40a-9b55-33a4-ac91-c088fa6b8748 | -3.34614 | -42.76413 | 2026-09-20 04:17:00 | NPP-375D | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f5c2e7d1-ef1f-31f0-a13f-317b7bf98d01 | -2.8266 | -46.70993 | 2026-09-20 04:17:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 741723b0-c44d-3b60-a85f-acb768a14360 | -3.16646 | -48.61386 | 2026-09-20 04:17:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| bd005541-77ef-3e0d-b3bf-b98e35ef14fb | -3.59543 | -47.35795 | 2026-09-20 04:17:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 42f0d006-85c4-31bb-b20d-bea592b116fd | -3.7103 | -39.43506 | 2026-09-20 04:17:00 | NPP-375D | UMIRIM | CEARÁ | Brasil | 2313757 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| bdf716b6-de7c-34fd-8a92-3f99751a2219 | -3.99016 | -41.26733 | 2026-09-20 04:17:00 | NPP-375D | SÃO JOÃO DA FRONTEIRA | PIAUÍ | Brasil | 2209872 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 8e18c191-4e3b-3562-971b-1d1167787765 | -3.34958 | -42.76466 | 2026-09-20 04:17:00 | NPP-375D | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 17621876-c4aa-3833-8890-bb757bb444d7 | -3.35848 | -50.45639 | 2026-09-20 04:17:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cd48af63-d84d-3a71-9bcd-7d4435aa906a | -3.36027 | -50.44574 | 2026-09-20 04:17:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5e7c8f69-a8d2-3660-9bd5-430483c4af29 | -2.82189 | -50.46478 | 2026-09-20 04:17:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 95d303cb-6167-329b-9760-ce3c0d3b966e | -3.35184 | -42.77265 | 2026-09-20 04:17:00 | NPP-375D | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| be78cf76-9d7f-3f0e-ba9e-2975fc8bf2dc | -4.56404 | -42.98403 | 2026-09-20 04:17:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ee993e7f-94eb-3aec-bf7f-7cbc06a6d4d1 | -2.86405 | -49.63415 | 2026-09-20 04:17:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f3693a85-04dc-3812-973e-c9ad605942e8 | -2.84063 | -49.51503 | 2026-09-20 04:17:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 97e212d4-1e05-3092-b62b-913dad6f84c2 | -2.30959 | -48.401 | 2026-09-20 04:17:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c3ba3fbf-2f45-38ae-a46d-b35ea2e9852f | -3.87228 | -40.73169 | 2026-09-20 04:17:00 | NPP-375D | MUCAMBO | CEARÁ | Brasil | 2309003 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| ee9ec222-71f3-3d8b-8975-49c14f6ad7b1 | -3.16156 | -48.61307 | 2026-09-20 04:17:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8ebe05ac-3d9c-331e-af7d-66acdd8f28d1 | -4.56987 | -42.96976 | 2026-09-20 04:17:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 15304a15-db45-338f-acf9-d63ecc559ef4 | -2.46124 | -49.21749 | 2026-09-20 04:17:00 | NPP-375D | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6b4f5246-0db3-303b-9d19-147dba3cebb7 | -4.56061 | -42.98347 | 2026-09-20 04:17:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c3bd81a9-0367-398b-bb4c-b6d5fe24fc4b | -1.32011 | -49.27847 | 2026-09-20 04:17:00 | NPP-375D | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e991e660-d3c1-38b8-a9ca-1001f600ccea | -2.82128 | -50.46848 | 2026-09-20 04:17:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a5cd6b32-0a0b-3c96-9729-bb8e31410437 | -2.64531 | -54.69506 | 2026-09-20 04:17:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| f4115d70-0f4e-34cb-b86d-87388cf1f86d | -3.38363 | -39.20322 | 2026-09-20 04:17:00 | NPP-375D | PARAIPABA | CEARÁ | Brasil | 2310258 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 0775f2fb-d02c-3c5a-be3b-faab1525583f | -3.16739 | -48.60839 | 2026-09-20 04:17:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 5a440f58-b7c5-37ae-b119-35d026bc7d54 | -3.50437 | -43.35368 | 2026-09-20 04:17:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| eca3cf85-3c9f-3ed9-ae66-0fb58db913fe | -2.8704 | -49.62851 | 2026-09-20 04:17:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6106692c-0f47-36b3-acad-a610059f401f | -5.57637 | -36.25723 | 2026-09-20 04:17:00 | NPP-375D | PEDRO AVELINO | RIO GRANDE DO NORTE | Brasil | 2409704 | 24 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 75bb49ba-9070-3b39-8063-b81c4eca2592 | -3.3658 | -50.44666 | 2026-09-20 04:17:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3561ca02-bacb-3b12-93c5-e1451335d93e | -3.364 | -50.45742 | 2026-09-20 04:17:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 63938b08-c775-3a47-8d65-59f304ecb1e5 | -2.82748 | -50.4657 | 2026-09-20 04:17:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8ab42fcd-9de8-3c34-8fbf-0f60c92ec58d | -2.45659 | -49.21357 | 2026-09-20 04:17:00 | NPP-375D | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 55b06ef6-f226-33d6-a7b3-b9d718f77c30 | -3.4072 | -50.40262 | 2026-09-20 04:17:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 38c4f3fd-3005-35dd-aa4d-81e2bcc600c9 | -11.01355 | -48.32667 | 2026-09-20 04:19:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |


[Clique aqui para ver as próximas entradas](README24.md)
