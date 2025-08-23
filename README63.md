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

## Dados Diários - Página 63

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c2936558-c34f-3402-9b0f-c2152f7cb22a | -9.17018 | -59.58622 | 2025-08-23 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d60a6110-98e6-3ade-8822-ad37aa8ac373 | -14.6197 | -54.80674 | 2025-08-23 05:21:00 | NPP-375D | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 5277d18f-0abf-308f-88c8-fe40b5d3334c | -9.22696 | -60.92781 | 2025-08-23 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9296a7ca-2707-3054-9bb9-e8e97293ab84 | -9.22228 | -59.75225 | 2025-08-23 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c97278f9-1baf-3077-9503-b48220fd227e | -10.60941 | -55.40562 | 2025-08-23 05:21:00 | NPP-375D | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c6fa6aab-e070-3d7b-b89b-53de3ced7db8 | -7.44173 | -60.62659 | 2025-08-23 05:21:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1f7053e9-e4b5-33db-9126-f0d033b7a61f | -14.7007 | -54.9101 | 2025-08-23 05:21:00 | NPP-375D | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9062abe0-0f12-3eba-b082-890a42cefbb1 | -9.96108 | -60.18824 | 2025-08-23 05:21:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 9816d6fa-2bc0-380e-9043-477ee2f73d7d | -9.17906 | -59.65926 | 2025-08-23 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a758e9c6-b055-36bc-9963-0ad1305c0dfd | -14.67579 | -56.61434 | 2025-08-23 05:21:00 | NPP-375D | ALTO PARAGUAI | MATO GROSSO | Brasil | 5100508 | 51 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 081ffbe6-2d0d-3821-abf7-05e0a0ed192f | -12.8579 | -60.16271 | 2025-08-23 05:21:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 95b77154-3639-3a71-b220-a61cded00e54 | -9.5193 | -60.52018 | 2025-08-23 05:21:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e7fa802a-4a87-3f11-950b-a8ed85a45bb8 | -15.03135 | -54.90192 | 2025-08-23 05:21:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| f3edba9a-2531-3f41-bb96-a91e8960271d | -13.3779 | -46.21119 | 2025-08-23 05:21:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 909c35c4-c46d-31db-aec4-29fc21ee7568 | -7.80946 | -63.56016 | 2025-08-23 05:21:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7ec4c774-01a9-3a34-bb37-5a37ca6ba004 | -9.20486 | -60.9354 | 2025-08-23 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 56dc7c7a-83dc-3599-8bf5-73c48b5e1ef3 | -7.2961 | -59.6304 | 2025-08-23 05:21:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 81d79c7d-c783-3477-a77f-e882ab780b2e | -14.27966 | -58.55298 | 2025-08-23 05:21:00 | NPP-375D | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e2d0ce06-f45b-3e3b-b5ca-9d92dc5253e0 | -9.21665 | -59.46472 | 2025-08-23 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 56bd5dda-4872-33d3-b1ea-9f7a147eb821 | -14.28484 | -58.52956 | 2025-08-23 05:21:00 | NPP-375D | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7e09289f-18cb-3bc9-aa19-f40f9160854c | -9.16577 | -59.67863 | 2025-08-23 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3738db27-90bb-31ff-a039-57f3676bf809 | -15.07887 | -48.50672 | 2025-08-23 05:21:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 5dbf5103-b873-37ab-97db-cb04cd427ec0 | -13.12655 | -46.90813 | 2025-08-23 05:21:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8c9d36a8-83d3-3325-b5e2-f1225587c756 | -7.05693 | -59.82998 | 2025-08-23 05:21:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| dccb2798-8a6c-3bd5-ab91-cc2dbcf5fb9f | -9.20287 | -59.61654 | 2025-08-23 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 93e34bbc-ea93-389c-ad03-a8cf5164d87e | -14.46533 | -55.93598 | 2025-08-23 05:21:00 | NPP-375D | NOBRES | MATO GROSSO | Brasil | 5105903 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5ca76fab-7cca-35f2-9c08-d43f2b44ce5d | -13.3907 | -46.34776 | 2025-08-23 05:21:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| fd201348-e271-3913-9eaa-ce459a554d8f | -9.16244 | -59.67809 | 2025-08-23 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d0204908-5dab-3a19-aef6-0dc20a0dac58 | -9.20177 | -59.62353 | 2025-08-23 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cc588422-8a2c-329f-9395-1573bedd4e0e | -7.95324 | -63.04366 | 2025-08-23 05:21:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1ae60109-6661-3859-a37c-8252fcf6c79c | -12.77342 | -48.71095 | 2025-08-23 05:21:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 14.7 |
| edc019b8-9073-3e3a-a8e6-18ab47aa774a | -6.87632 | -59.81898 | 2025-08-23 05:21:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 8b1fb9dc-a1bd-3b9e-8884-d7f99b6423ad | -14.3344 | -58.57688 | 2025-08-23 05:21:00 | NPP-375D | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f2f61c41-5413-3524-9d8f-8e79b1ceb9cf | -8.66532 | -51.27423 | 2025-08-23 05:21:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 33d81419-0f2a-34cc-a9d0-63d9662edfbf | -9.17851 | -59.70576 | 2025-08-23 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6725134d-9e28-3163-b498-66f07e15c99b | -12.94478 | -46.30521 | 2025-08-23 05:21:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 27d1301b-d3db-3e68-890f-45bdf5e8a03c | -6.8812 | -59.89587 | 2025-08-23 05:21:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4bda9f77-7915-3a19-a22a-9a84896b6c68 | -14.82131 | -47.95879 | 2025-08-23 05:21:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 6c0fb377-a6e8-314f-b887-5a4fd359af3f | -7.56009 | -61.37417 | 2025-08-23 05:21:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ac4b2241-0648-363a-8003-84a88d92596f | -6.93944 | -59.63801 | 2025-08-23 05:21:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 525fcdf4-38ae-3cbf-ab16-8697ae6e2830 | -9.45357 | -63.50466 | 2025-08-23 05:21:00 | NPP-375D | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cbacdead-21c3-39fd-8a55-fa1c8695908f | -7.43435 | -60.62915 | 2025-08-23 05:21:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 82c052d1-0fa4-3ceb-b120-86050ef3f4f8 | -11.29529 | -53.95723 | 2025-08-23 05:21:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b7e47f4d-00c0-3ed5-9675-11ee32ccefe3 | -9.50646 | -60.51442 | 2025-08-23 05:21:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9356649a-bb12-382f-8c72-d4cbb6664cc7 | -6.9013 | -59.89907 | 2025-08-23 05:21:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b5856459-e251-3e22-91f9-b2cf122f6e29 | -13.38219 | -47.51469 | 2025-08-23 05:21:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c0f25f38-0531-3e9b-a4ec-28537fe8ad22 | -14.28045 | -60.38685 | 2025-08-23 05:21:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4e7c509e-47a8-38fa-9573-0c88c224eb13 | -7.8064 | -63.55462 | 2025-08-23 05:21:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 423b51b1-04af-3f49-9473-eb7e908b68ec | -9.47793 | -57.82833 | 2025-08-23 05:21:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 83281c04-210f-3a28-a32a-089407587692 | -9.20723 | -59.45963 | 2025-08-23 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3728ae36-0790-3e9a-9e9f-2d5bf6e7f4cf | -9.50253 | -60.51743 | 2025-08-23 05:21:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c864a674-b80c-38e5-b9af-2d1afb380812 | -14.3505 | -58.58733 | 2025-08-23 05:21:00 | NPP-375D | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 566c6994-802d-341e-a78c-806666d4f77d | -14.61765 | -54.85549 | 2025-08-23 05:21:00 | NPP-375D | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ca4bc95d-ba8c-32bc-8182-d04edbb3b3cc | -14.81522 | -47.95243 | 2025-08-23 05:21:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| e15afea3-b811-30c7-b20a-47b115c63c8d | -7.44114 | -60.63026 | 2025-08-23 05:21:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| bf113ab8-81dd-3a01-99d3-4c40bc1135de | -9.82105 | -64.27245 | 2025-08-23 05:21:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 840db0e0-bb27-35ff-9cea-991c8b33f7e4 | -9.17131 | -59.66518 | 2025-08-23 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 31c199b9-c5c0-3695-8c9d-cf1da6fffa85 | -8.9042 | -62.43261 | 2025-08-23 05:21:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 87558b49-eafe-3653-8742-1d3af2df01c2 | -14.88197 | -47.95949 | 2025-08-23 05:21:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| daf65b9c-7bf6-370c-8c7d-37f55d97f897 | -10.63292 | -50.14139 | 2025-08-23 05:21:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a0406ea0-aa4b-3065-857d-8e1fee48fd92 | -9.19289 | -59.59344 | 2025-08-23 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2f74e535-ad13-31b3-9470-ddf3fad0e203 | -6.94558 | -59.55635 | 2025-08-23 05:21:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| cc4e4bef-6aca-3a82-8203-95bf56149f0b | -9.17629 | -59.65524 | 2025-08-23 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e0fb6d4f-89ca-37a4-9ae3-727a4b2a4c89 | -9.6071 | -55.36243 | 2025-08-23 05:21:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3a3be101-2e82-3e71-adf7-64566f0286ac | -7.56294 | -61.37857 | 2025-08-23 05:21:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 50f687da-2588-30f3-b766-82325148950f | -8.66044 | -51.27286 | 2025-08-23 05:21:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7623f45f-6c12-3d11-ad3e-300b2052b736 | -14.61818 | -54.85144 | 2025-08-23 05:21:00 | NPP-375D | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2f494b6d-3550-3449-8d1f-f8e5abbbfc44 | -9.21063 | -59.63211 | 2025-08-23 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cf21147d-2c14-394c-a95b-bd32378437a8 | -8.86804 | -62.42305 | 2025-08-23 05:21:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d502ca99-82e0-3349-be14-4e8098634bc0 | -9.51301 | -60.55944 | 2025-08-23 05:21:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e5b8db2a-1b56-3b4f-8370-ebeda026997c | -9.19679 | -59.65493 | 2025-08-23 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 8ae283be-a72a-3712-9d2d-1e0a6c01f4db | -13.43304 | -57.1678 | 2025-08-23 05:21:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 312f5e04-f474-3e35-8e84-1146947ff2ac | -9.18348 | -59.63134 | 2025-08-23 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ca33c745-bf9b-39d0-bc7c-876dc1b4d899 | -9.21062 | -59.61062 | 2025-08-23 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0a392ef7-c667-3a4c-92dc-0e9796788443 | -14.28317 | -58.52975 | 2025-08-23 05:21:00 | NPP-375D | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c03b4af6-7609-3e97-a762-adffdebf52a1 | -13.46818 | -47.03461 | 2025-08-23 05:21:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d4ee10b8-72e8-310b-87ee-098263f0e021 | -14.37572 | -52.04935 | 2025-08-23 05:21:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 8.2 |
| e2730a0e-3b8e-3c79-8b91-94a81bf8703a | -8.92507 | -60.72235 | 2025-08-23 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ce2c461c-9242-3187-8bb8-24b1e19006fa | -14.66559 | -56.61063 | 2025-08-23 05:21:00 | NPP-375D | ALTO PARAGUAI | MATO GROSSO | Brasil | 5100508 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 791311a5-f067-387c-a3dd-1b6a57e6ef9a | -12.94245 | -46.29969 | 2025-08-23 05:21:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 01e18ad0-c42d-3904-8c97-6f19f02131ab | -15.01609 | -54.86655 | 2025-08-23 05:21:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e5cf564e-356a-314f-bffd-4df346064ef4 | -6.8791 | -59.82304 | 2025-08-23 05:21:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 71243f81-0b3e-33d8-b447-de36c99ea85a | -9.21704 | -60.79569 | 2025-08-23 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 23f58235-e343-3ab6-b699-57f44ac0fc39 | -9.21308 | -60.79874 | 2025-08-23 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| eec90ec4-9312-32c3-92d0-303d3ecb0eaa | -9.52543 | -60.52483 | 2025-08-23 05:21:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5df64759-13ce-3eb8-ae1d-9aba31a67a33 | -14.3436 | -58.58624 | 2025-08-23 05:21:00 | NPP-375D | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 0a1af3fc-e9fa-35cb-8a2b-b1a13b854240 | -13.42879 | -57.17153 | 2025-08-23 05:21:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 87245e91-cdd9-35b2-a01f-00ece83ebadf | -9.20279 | -59.4446 | 2025-08-23 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d3d04336-e04e-341d-9376-c236525fa0d3 | -13.04039 | -46.79763 | 2025-08-23 05:21:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 9045dcdc-499c-3c80-a9c8-6693e96d9169 | -13.44032 | -57.16893 | 2025-08-23 05:21:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 84d1c90a-1dc2-31c5-8913-ec210cebfef5 | -9.7176 | -65.71192 | 2025-08-23 05:21:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2208e6b5-f433-38a5-829b-109c71d95a8b | -8.59324 | -62.61745 | 2025-08-23 05:21:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1571d22b-0372-3313-aa46-93c03b5862de | -8.86855 | -62.39759 | 2025-08-23 05:21:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 19bd10cb-f583-315c-bbca-a46929436f9b | -10.10471 | -57.76208 | 2025-08-23 05:21:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6955b70c-f818-3821-9642-26d66df0e8a8 | -8.59688 | -62.61806 | 2025-08-23 05:21:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a0bb4425-8c56-38c3-a02c-131bb02b8e09 | -10.75448 | -48.25257 | 2025-08-23 05:21:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 4353f109-a689-3b76-86b4-0f1817983b1d | -12.30433 | -49.99134 | 2025-08-23 05:21:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| aded097f-d718-39c7-8aaf-142bf053e111 | -7.51072 | -63.83371 | 2025-08-23 05:21:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 83ae630e-f875-31e3-9cf1-e001ba77145b | -9.50703 | -60.51085 | 2025-08-23 05:21:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4a490aa4-cbd5-308f-a4d1-b4f25a40e333 | -13.37507 | -47.5175 | 2025-08-23 05:21:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |


[Clique aqui para ver as próximas entradas](README64.md)
