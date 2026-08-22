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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f6c29224-a194-3a50-ab78-00bdd8b541ed | -6.89135 | -56.72663 | 2026-08-22 00:28:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| ce883ff2-f9cb-3ab5-bfc6-61be84c8953a | -8.52361 | -55.33162 | 2026-08-22 00:28:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| d6599144-6610-312d-91bd-b217e7ddf937 | -6.48868 | -51.59802 | 2026-08-22 00:28:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| f191aa98-a458-38d1-9fd9-a46ff5d16c91 | -5.9964 | -57.80973 | 2026-08-22 00:28:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 27.7 |
| f3e73765-b709-3033-9b51-076828e7dd38 | -7.08504 | -55.44781 | 2026-08-22 00:28:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| b4964038-a039-368e-b404-769107b20d94 | -6.82103 | -59.67825 | 2026-08-22 00:28:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 59.9 |
| 519dacef-45e4-3fee-a177-894d9d235fce | -6.78801 | -58.6546 | 2026-08-22 00:28:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 34.9 |
| 6abc6bf2-6bc8-33f9-88e1-166386be25d2 | -6.77747 | -55.69579 | 2026-08-22 00:28:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 0505fa36-3802-3f46-942e-e15e619b2a73 | -6.15222 | -57.73735 | 2026-08-22 00:28:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| a2965023-de76-34f1-a03e-48fbab628066 | -5.9977 | -57.81933 | 2026-08-22 00:28:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| ef51217a-feb3-3e5d-bac7-94d552d7b79b | -6.09644 | -57.86864 | 2026-08-22 00:28:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 4d392099-ee15-30d6-9bbc-5f710d8f384b | -7.346 | -55.67728 | 2026-08-22 00:28:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 25.0 |
| 93084685-3c16-3a07-a0fd-91350f82798f | -6.6445 | -53.37634 | 2026-08-22 00:28:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 72be9cfb-6f8e-3f43-a0e7-0366703177b9 | -9.17458 | -56.99798 | 2026-08-22 00:28:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 8f1dc727-989f-370c-a9f6-dd3014591a96 | -8.59096 | -54.74723 | 2026-08-22 00:28:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 25.0 |
| 2fd6a374-2904-3dca-9b19-e23c96746488 | -6.80896 | -59.66712 | 2026-08-22 00:28:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 53.6 |
| d96b36a1-9c14-3d9e-b9d3-ed0778c6192d | -6.11841 | -57.69347 | 2026-08-22 00:28:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| cd2487fa-f2c0-36df-ad7c-23a04aad585d | -7.33843 | -55.68734 | 2026-08-22 00:28:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 8db7071f-33f2-38ec-8cd3-8f58c6ca1925 | -9.16876 | -59.44678 | 2026-08-22 00:28:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 85.8 |
| ceb9a8f0-ea9e-3067-bbd2-863527509c81 | -6.82735 | -59.67168 | 2026-08-22 00:28:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 101.4 |
| 3badd4dd-cf1a-3134-94bb-dfca1577a17b | -6.23188 | -55.62104 | 2026-08-22 00:28:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 14.4 |
| 2b88b049-89f0-3684-98c1-0ca6c542406f | -9.44006 | -51.61272 | 2026-08-22 00:28:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 24.6 |
| 5e4f3384-18bd-3f5d-ae00-45b45026623b | -6.76466 | -58.65302 | 2026-08-22 00:28:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 72.7 |
| 255ee96c-c85b-3749-8146-5705cfe17a2c | -7.21294 | -59.40711 | 2026-08-22 00:28:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 12.9 |
| fd4879af-5dde-379d-a3b9-a68cc26b2b0c | -6.1435 | -59.90114 | 2026-08-22 00:28:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 52218767-5ec0-3150-bc9c-d9555f7f115a | -10.26182 | -50.33839 | 2026-08-22 00:28:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 9.9 |
| af5a6fb9-b5fe-3577-bc28-2ae75c0df665 | -8.51482 | -55.33288 | 2026-08-22 00:28:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| ece0fb09-ea60-3b55-b49c-9c2f343ac021 | -11.16284 | -54.01818 | 2026-08-22 00:28:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 15.2 |
| 2c7475ea-e4f1-3fb4-9783-8e71fa96d30a | -8.22608 | -55.0338 | 2026-08-22 00:28:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 68447c1f-18f9-3df2-b4bd-372283dd64c2 | -6.25923 | -55.41299 | 2026-08-22 00:28:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 19.2 |
| 352eb2b2-25de-3ee9-a834-77afe048d53d | -6.25164 | -55.42311 | 2026-08-22 00:28:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 66efc514-f42c-37d9-b8f7-33f733ca71af | -6.81694 | -59.673 | 2026-08-22 00:28:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 41.8 |
| e9b0577f-27d3-3005-a911-00e001c8da49 | -8.11106 | -50.05021 | 2026-08-22 00:28:00 | TERRA_M-M | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 16.7 |
| 03dd6e21-ee2d-38fd-8fe2-54f756d808d8 | -11.10307 | -49.8924 | 2026-08-22 00:28:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 449dc5f8-7c54-3a7f-92f4-d4d2c93260a4 | -6.76901 | -58.68533 | 2026-08-22 00:28:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 86.6 |
| 8368d296-574f-3cd4-9259-6904a2a070fc | -6.7957 | -59.42495 | 2026-08-22 00:28:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2104.3 |
| 0d783ad0-7dc4-39be-a2b4-03489729f9a1 | -8.40354 | -62.69744 | 2026-08-22 00:28:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 25.0 |
| 21277951-1cd1-3ca7-b4e3-e454a2daa988 | -6.78018 | -58.69484 | 2026-08-22 00:28:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 87c76b49-f516-3647-b9a2-1d10e865a43f | -6.07975 | -59.95459 | 2026-08-22 00:28:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 887c5fe3-e51d-3d33-ac0c-134d479bd2ee | -5.74337 | -53.5906 | 2026-08-22 00:28:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 9c82ff52-69f5-3088-ba2f-2a697c161ef6 | -6.86831 | -59.03926 | 2026-08-22 00:28:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 49.6 |
| 2a5cacb4-b0d8-34de-a402-58c89848563b | -7.33964 | -55.69615 | 2026-08-22 00:28:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 6a8a9354-a717-3830-9ba6-968cbe66396f | -8.15796 | -46.73948 | 2026-08-22 00:28:00 | TERRA_M-M | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 30.6 |
| 53b9b06c-d567-3772-99a6-f9919564ad80 | -6.89948 | -55.71741 | 2026-08-22 00:28:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 17.4 |
| dc10c96e-21d8-3288-a726-18dbaa37fd46 | -6.80591 | -59.42364 | 2026-08-22 00:28:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 634.6 |
| 1e8358c9-dc0e-3dde-816f-9effc8143cbf | -7.34086 | -55.70496 | 2026-08-22 00:28:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 8265b30d-bc3e-34c3-8494-5caf01e117a2 | -6.37832 | -54.94579 | 2026-08-22 00:28:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 54.2 |
| e51c9d26-a61c-30ef-94ff-a983c28177a6 | -8.62898 | -54.69585 | 2026-08-22 00:28:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 344fdc13-51ca-3481-b18f-a08e8231cf1a | -9.16158 | -59.47448 | 2026-08-22 00:28:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 41.2 |
| 1ddcb73f-4101-3852-887b-787630622948 | -6.65407 | -56.33586 | 2026-08-22 00:28:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 428e0a85-133c-36c7-a75c-25830d7ec668 | -6.80903 | -59.44776 | 2026-08-22 00:28:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.9 |
| d3f7b475-eb1d-3d52-9c9a-0d1fcf708548 | -7.36051 | -55.52244 | 2026-08-22 00:28:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| f86542d2-569e-33f5-9eff-dfab6458495d | -6.78551 | -59.42641 | 2026-08-22 00:28:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 14.4 |
| 8686d208-2b40-3e15-813d-ea0931d75fbe | -10.25069 | -50.34019 | 2026-08-22 00:28:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 17.6 |
| f8fe913d-4baf-3819-b509-562c7da8d3e0 | -6.84943 | -58.97232 | 2026-08-22 00:28:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 5e97b520-dadf-3c73-8c2e-1c58c2b0adbf | -7.66742 | -49.8789 | 2026-08-22 00:28:00 | TERRA_M-M | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 14.2 |
| dc2c0fcf-9e0c-3d31-b81e-9777d6210f0d | -7.55536 | -61.18335 | 2026-08-22 00:28:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 41.3 |
| 39bef4dd-0f1e-3478-9a53-25764219bad6 | -6.77926 | -59.44536 | 2026-08-22 00:28:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 045b2435-0c4d-33cc-a361-2705f7bb7259 | -7.17987 | -60.64417 | 2026-08-22 00:28:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 11d86542-11f4-37b5-b3fc-09d2dd4b69a3 | -9.11913 | -61.59874 | 2026-08-22 00:28:00 | TERRA_M-M | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 53.5 |
| f91ad899-bf45-34e0-aec5-b1d7d9500cc7 | -8.1644 | -54.99409 | 2026-08-22 00:28:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 24.9 |
| edca3d72-30ee-38ae-be87-5e2b989309ba | -6.89069 | -55.71865 | 2026-08-22 00:28:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 19a08697-52d2-3fe4-8bd9-4f5f5d96f5fd | -8.99758 | -50.73172 | 2026-08-22 00:28:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 46.4 |
| 1bd25b79-3ce7-3622-ba8d-47522efcf24a | -6.90502 | -59.01119 | 2026-08-22 00:28:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 2caa1e1d-32b9-3c6b-a47a-6e7eadbf125a | -6.79626 | -58.64236 | 2026-08-22 00:28:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 27.9 |
| 419047fb-3e7d-3680-a75e-2571789e8eeb | -6.7449 | -58.57927 | 2026-08-22 00:28:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 65d173bc-5298-30d8-a988-2141c66ce40f | -6.22186 | -55.61348 | 2026-08-22 00:28:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 23a4c030-785e-350a-b949-94e1775ee609 | -8.02836 | -54.026 | 2026-08-22 00:28:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 16.3 |
| b2ef8c5f-d0cb-3487-82ff-3dd70d482be4 | -8.96154 | -50.72946 | 2026-08-22 00:28:00 | TERRA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| d0902f70-3276-3ce0-a970-425f62e18393 | -7.86316 | -63.76999 | 2026-08-22 00:28:00 | TERRA_M-M | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 22.1 |
| ad4108c1-e4be-37a6-ad3d-8a9762ad9fd7 | -6.70376 | -58.95806 | 2026-08-22 00:28:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.2 |
| ed774294-bb13-3640-99de-0d4adceefb30 | -6.22114 | -55.47856 | 2026-08-22 00:28:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| cb888609-d185-3201-9818-a0e33078059f | -6.78785 | -59.43192 | 2026-08-22 00:28:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 54.1 |
| 56b3deda-e28a-3424-af10-0b00870d0a03 | -7.66324 | -49.88528 | 2026-08-22 00:28:00 | TERRA_M-M | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 25.7 |
| f1d0d753-4236-3501-9de2-9c1f5d8d3a86 | -9.18736 | -59.46543 | 2026-08-22 00:28:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 31.3 |
| 52e8626a-833a-3767-b534-4bc22751e073 | -10.81062 | -50.98605 | 2026-08-22 00:28:00 | TERRA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 23.3 |
| ba996eca-ec0a-3aa0-8d51-6eb2451fe74f | -6.86176 | -59.45303 | 2026-08-22 00:28:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 42.6 |
| e2d14906-6767-3a46-a029-8dbf77ae321a | -7.59697 | -60.94423 | 2026-08-22 00:28:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 18.4 |
| e40c6bd8-db8d-309c-8982-08eb0d7f1f20 | -6.82474 | -59.40886 | 2026-08-22 00:28:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 140.1 |
| 4b4b7d6b-d1d1-3e94-a3f2-308b9fbb10e7 | -8.02703 | -54.01665 | 2026-08-22 00:28:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 68d1c285-aeae-38a7-a838-2168f4d86a8c | -6.85686 | -59.02911 | 2026-08-22 00:28:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 11.8 |
| a05fa20d-b925-3564-978b-2b0217ffd820 | -6.94554 | -59.31324 | 2026-08-22 00:28:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 14.4 |
| 13e75c91-4df7-377a-b986-b36868c426e1 | -8.03514 | -51.80062 | 2026-08-22 00:28:00 | TERRA_M-M | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 3509360b-ba55-3fc5-b5fc-26ccab37a776 | -6.433 | -54.94714 | 2026-08-22 00:28:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 13.9 |
| 42e9d70c-a910-3721-802a-85bf0004b98c | -6.5532 | -56.55199 | 2026-08-22 00:28:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 702d0bca-f810-33f0-8497-9b4b0933e78c | -6.79897 | -59.59246 | 2026-08-22 00:28:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 38.5 |
| 2d6ead03-8747-3e1b-b951-d10b8e3340e3 | -9.18108 | -59.45852 | 2026-08-22 00:28:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 64.2 |
| 54b26e83-382b-3e7a-879e-8fd41900db0e | -11.16541 | -54.03638 | 2026-08-22 00:28:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 19.8 |
| 5efd7323-0304-3d32-bff3-61c1876552ea | -8.5922 | -54.75617 | 2026-08-22 00:28:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 273e1546-41ec-31c4-985d-f1aea41346c4 | -8.63023 | -54.70485 | 2026-08-22 00:28:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| b08195e1-3a15-364f-a167-78cb0b792339 | -6.41793 | -52.72667 | 2026-08-22 00:28:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 4dbdb919-af0d-34ba-8f1e-fb3c06fb101e | -6.60805 | -58.38954 | 2026-08-22 00:28:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 22.9 |
| e03fdafe-1c79-3a34-ab9f-e2cfadbd149d | -8.52787 | -54.82618 | 2026-08-22 00:28:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 411.3 |
| 14c66b1c-7942-396c-b2e7-9f518c64b875 | -9.21109 | -60.76169 | 2026-08-22 00:28:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 16.7 |
| fb8922a0-3d2d-34a5-921d-6fed35bbe4b0 | -6.66409 | -56.34347 | 2026-08-22 00:28:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 9b440da1-3c74-37b1-a719-cc9961921fe6 | -6.80435 | -59.41159 | 2026-08-22 00:28:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 280.1 |
| ed342429-1810-30b3-b9db-9547bda170d6 | -7.01582 | -59.54515 | 2026-08-22 00:28:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.4 |
| ed984b39-ed94-35e6-9969-2a648e4a06d6 | -6.06519 | -57.70697 | 2026-08-22 00:28:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| cfb125f9-90bb-3d1d-9e33-76e959300c15 | -8.61626 | -54.73434 | 2026-08-22 00:28:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 5a8f222b-239e-3378-a592-7a790a67c49b | -6.90348 | -58.99977 | 2026-08-22 00:28:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 80.7 |


[Clique aqui para ver as próximas entradas](README6.md)
