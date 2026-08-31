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

## Dados Diários - Página 180

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6f43f563-f94b-3c7c-b19d-e0ad9d25dac1 | -9.9708 | -53.9419 | 2026-08-31 17:50:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 80.0 |
| 523299ff-e661-34ad-a57a-fd19ed79b66c | -8.9002 | -68.8899 | 2026-08-31 17:50:00 | GOES-19 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 52.8 |
| 5bd44dd5-93e2-3f80-bc90-58cbc1e5619c | -9.196 | -64.4568 | 2026-08-31 17:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 35.7 |
| b8932e1e-5d19-3f36-afd7-3cf7f290f897 | -3.1998 | -61.161 | 2026-08-31 17:50:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 58.7 |
| 373c9177-ee51-3eb6-b7d6-caf603b9819f | -8.5555 | -66.9574 | 2026-08-31 17:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 56.8 |
| 8d9f2023-8712-36fa-8a2c-deeb7221c2b2 | -9.7126 | -65.0951 | 2026-08-31 17:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 46.5 |
| 9e7b777e-5213-3941-bb63-b6fa581fd7c9 | -8.7991 | -62.4715 | 2026-08-31 17:50:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 39.2 |
| 8cd1eb3f-4712-3221-9395-63bafe275c1d | -6.2864 | -53.3351 | 2026-08-31 17:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 38.0 |
| 7d6b023e-0038-3161-8580-321a31b7d8c9 | -9.0534 | -60.4542 | 2026-08-31 17:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 46.1 |
| b5fe10b6-8c59-3dcc-afa7-3b6599d99bdb | -9.6676 | -47.9429 | 2026-08-31 17:50:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 242.4 |
| 7834afcf-9a38-3196-a002-1968ae90c6ed | -3.9708 | -60.0067 | 2026-08-31 17:50:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 48.9 |
| 50e9be12-59dd-3b16-9b3e-d226022d9116 | -8.8521 | -66.7641 | 2026-08-31 17:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 47.0 |
| a0ab6310-2e53-359f-bb7b-a36c46f683ff | -7.5661 | -61.3239 | 2026-08-31 17:50:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 70.7 |
| 852eb16b-32f7-350e-9a7f-299d8ba15cf3 | -8.803 | -70.84 | 2026-08-31 17:50:00 | GOES-19 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 44.5 |
| 7d717881-3e90-3beb-8776-e23ea6ffbe0c | -11.2482 | -45.1194 | 2026-08-31 17:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 110.8 |
| 3653b03a-e886-37d9-962d-50cab41e3a8b | -6.6542 | -59.426 | 2026-08-31 17:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 46.8 |
| 4beb692d-87a3-3ba9-bce2-01e3df6a40a5 | -13.8563 | -54.0967 | 2026-08-31 17:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 65.3 |
| 10dd3ba5-b72d-39d7-86f6-313b07fdbf9c | -14.4004 | -52.5438 | 2026-08-31 17:50:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 37.6 |
| b304a931-5882-3c97-9afb-81f0505cfa00 | -11.3236 | -45.1778 | 2026-08-31 17:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 194.0 |
| aefcfc14-a107-3b61-a165-72ab28c5439b | -14.4838 | -52.1725 | 2026-08-31 17:50:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 73.6 |
| 5431701c-a454-3691-a605-81c228a5f1f8 | -8.8031 | -70.785 | 2026-08-31 17:50:00 | GOES-19 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 79.9 |
| 7c00035f-01e3-3434-932f-39dfcb9ee21b | -9.1544 | -59.3669 | 2026-08-31 17:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 35.1 |
| 7bcbe64e-3161-32ed-b50f-a9a415a71e8a | -3.1267 | -61.1811 | 2026-08-31 17:50:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 205.8 |
| e8a76392-2151-3560-bb36-2602947392e8 | -8.574 | -66.9569 | 2026-08-31 17:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 74.7 |
| 0a74d83c-0dbe-36c5-bb10-a5eaec5fba12 | -3.4185 | -61.3273 | 2026-08-31 17:50:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 95.6 |
| 0fec6817-2c39-35f1-b4c5-a8a9e96c84e5 | -8.8705 | -66.7822 | 2026-08-31 17:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 75.5 |
| 90eaf3d1-c175-3caf-9fd9-3c64b474a685 | -11.1995 | -55.1008 | 2026-08-31 17:50:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 69.1 |
| eb249ad6-452c-3d8e-8f6a-8c192ef4372e | -8.8026 | -71.0783 | 2026-08-31 17:50:00 | GOES-19 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 61.2 |
| 7bfc3576-0216-3ccf-9b79-ed281b135825 | -9.9896 | -53.9404 | 2026-08-31 17:50:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 109.6 |
| 682bdbb1-6e90-3a89-8d0f-6653d61be453 | -9.4153 | -45.6726 | 2026-08-31 17:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 136.1 |
| 0b4c5c43-2e4e-30d4-933e-a94ca1e20169 | -11.5475 | -45.4906 | 2026-08-31 17:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 120.7 |
| e5311344-065d-3798-acda-b418588b1b56 | -8.4528 | -70.5881 | 2026-08-31 17:50:00 | GOES-19 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 133.3 |
| f420f8dd-4722-3cf5-abb9-0723d4724d23 | -7.5659 | -61.362 | 2026-08-31 17:50:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 196.2 |
| 5705d1ec-4308-374b-bcec-fdbebb9b149a | -11.5479 | -45.4676 | 2026-08-31 17:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 197.6 |
| ec57cb34-e8db-3bb6-8304-fdea4e045f0a | -13.1837 | -55.6682 | 2026-08-31 17:50:00 | GOES-19 | SORRISO | MATO GROSSO | Brasil | 5107925 | 51 | 33 | nan | nan | nan | Cerrado | 78.9 |
| d76a3d10-b968-30d2-b668-b1ea39f5cbf4 | -14.5028 | -52.1913 | 2026-08-31 17:50:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 131.6 |
| fadc76ff-92f5-3381-bf1c-52b258cc39c7 | -10.3202 | -49.9782 | 2026-08-31 17:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 65.9 |
| 1c39abdb-45b1-3165-af29-2fc4721f500c | -10.7271 | -50.6405 | 2026-08-31 17:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 147.6 |
| 5e00aa5d-3281-3087-9170-77f6fa5156ec | -3.4185 | -61.3461 | 2026-08-31 17:50:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 122.0 |
| db84474f-8819-3d82-aca4-9a1c99f83022 | -7.5844 | -61.3613 | 2026-08-31 17:50:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 175.8 |
| 2a8b6b74-4647-34be-ad3d-f3d3126b87db | -6.7832 | -59.4401 | 2026-08-31 17:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 82.3 |
| 9e89cebf-3ef2-3ab0-95c3-f0d716cd7e25 | -10.8614 | -50.4985 | 2026-08-31 17:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 49.3 |
| 767cbf8e-d131-3488-a18c-0d44678f8ba5 | -10.9355 | -50.6186 | 2026-08-31 17:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 51.3 |
| e3987888-ee3a-37d1-b8ff-eaae623de1c8 | -10.8046 | -50.5046 | 2026-08-31 17:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 106.6 |
| cc75c571-57ab-33f3-90c8-67f22755aeb8 | -8.7842 | -71.0236 | 2026-08-31 17:50:00 | GOES-19 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 48.1 |
| d9e7a2f8-a785-3491-a938-b058f4610ece | -11.2103 | -45.1017 | 2026-08-31 17:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 109.2 |
| 957a7710-c871-372c-afde-651bd7eb4f12 | -10.8218 | -50.6306 | 2026-08-31 17:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 62.4 |
| d62b6bd2-1e41-3764-a418-7c46174527a6 | -10.844 | -45.3356 | 2026-08-31 17:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 84.0 |
| 54bce46c-0f7e-3aef-b9da-fc9d6c8f8373 | -5.9636 | -57.6704 | 2026-08-31 17:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 69.5 |
| 6b4ac792-39ca-3119-8379-01baa765e40c | -9.4156 | -45.6499 | 2026-08-31 17:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 99.5 |
| b1bd0cdb-6bd1-3652-aacd-3b168a17ee11 | -6.1295 | -57.6637 | 2026-08-31 17:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 50.6 |
| 2fd986f0-9e03-367d-9863-afa68ef202f1 | -9.6939 | -65.1145 | 2026-08-31 17:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 189.4 |
| 1ace9eb9-71ab-3f80-9e4c-2f2cede0e97b | -14.4201 | -52.5201 | 2026-08-31 18:00:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 130.9 |
| cc12df66-055f-33f8-b6b2-302cf075fd22 | -14.4835 | -52.1938 | 2026-08-31 18:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 109.8 |
| b42615fd-3245-30f5-92e6-7aaad38dca89 | -8.9002 | -68.8899 | 2026-08-31 18:00:00 | GOES-19 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 69.0 |
| e1f0a1e6-e8dc-3243-94cb-91d5d54e3f8e | -9.1711 | -59.618 | 2026-08-31 18:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 59.0 |
| 6a50e522-803b-3c34-bf4c-b889b83ec285 | -11.2482 | -45.1194 | 2026-08-31 18:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 118.5 |
| 67575e35-c356-33d7-90f0-18ae099ab211 | -8.5177 | -55.3039 | 2026-08-31 18:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 63.9 |
| 3e2e3562-4050-3419-88a3-b5871872841a | 1.5465 | -56.0618 | 2026-08-31 18:00:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 61.9 |
| 30ba7a51-cf46-3a2e-a003-a84498ea14dc | -9.694 | -65.0958 | 2026-08-31 18:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 266.6 |
| f077292a-a747-3985-837d-a47a4e1c79e7 | -3.4185 | -61.3461 | 2026-08-31 18:00:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 75.5 |
| c8d454c4-ff6b-395c-b8b5-d84952e0492f | -8.87 | -66.9121 | 2026-08-31 18:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 49.6 |
| 56bc219f-ed76-3857-a990-aee0932eb0df | -8.574 | -66.9569 | 2026-08-31 18:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 93.1 |
| 56e90034-bc6c-3070-a792-a5533c5b338c | -9.208 | -65.8044 | 2026-08-31 18:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 61.8 |
| 4c9fd19f-f589-3cf0-a771-a53db500f863 | -13.1839 | -55.6479 | 2026-08-31 18:00:00 | GOES-19 | SORRISO | MATO GROSSO | Brasil | 5107925 | 51 | 33 | nan | nan | nan | Cerrado | 68.0 |
| e6d33179-6b5a-3790-9127-66baf04a0ac0 | -8.821 | -71.0781 | 2026-08-31 18:00:00 | GOES-19 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 57.4 |
| 00793014-9d49-3df0-99d2-e0b18a04b681 | -8.4896 | -70.6243 | 2026-08-31 18:00:00 | GOES-19 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 102.5 |
| ebc269c5-440a-3b0c-b054-cba78e937ea7 | -12.0925 | -44.996 | 2026-08-31 18:00:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 112.5 |
| 9997fcd4-69b6-3bc6-86e0-253565367dfa | -13.1837 | -55.6682 | 2026-08-31 18:00:00 | GOES-19 | SORRISO | MATO GROSSO | Brasil | 5107925 | 51 | 33 | nan | nan | nan | Cerrado | 66.6 |
| 0c97bb87-4b8a-3758-b341-1ddb011d0022 | -6.8193 | -59.5734 | 2026-08-31 18:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 62.7 |
| 09c0f6b7-994b-35ac-a165-d18fca990461 | -7.2191 | -60.6699 | 2026-08-31 18:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 43.3 |
| 9a22b825-e061-33b4-acb7-332d8cf65c21 | -7.4802 | -63.7454 | 2026-08-31 18:00:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 44.3 |
| 441dec8b-8f8b-3229-b554-1376bc31d1d5 | -12.9054 | -59.8857 | 2026-08-31 18:00:00 | GOES-19 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 53.8 |
| b074a016-c792-356f-b33a-fc96581aefbe | -13.4707 | -57.0574 | 2026-08-31 18:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 93.8 |
| 16687f67-c283-3aea-bb96-170c6d6ab64d | -9.445 | -66.7289 | 2026-08-31 18:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 55.9 |
| a20b5e34-6e30-3312-b43c-2f293e93c398 | -8.6674 | -62.8179 | 2026-08-31 18:00:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 58.0 |
| 2f82f447-76ed-371d-9ab2-b926c0da62d5 | -9.196 | -64.4568 | 2026-08-31 18:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 38.8 |
| 2e3aa4ca-7ac5-35fe-8e99-f487fb9095ae | -15.0244 | -48.1689 | 2026-08-31 18:00:00 | GOES-19 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 80.8 |
| e73e4a2c-fd1c-3d1b-9d4a-d5f1871bdab0 | -9.0057 | -65.456 | 2026-08-31 18:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 68.9 |
| 38d26620-7281-3412-a14c-ff62ea1183b6 | -9.2081 | -65.7857 | 2026-08-31 18:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 58.5 |
| 8bd6f747-ffac-387e-ad95-64475f302a98 | -10.7593 | -54.0589 | 2026-08-31 18:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 64.9 |
| 7968072c-716f-311c-96ba-03f19c4e1e54 | -13.967 | -54.395 | 2026-08-31 18:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 116.7 |
| 5efa9e4a-a1a8-35d1-b2bd-038d3725e4cf | -3.9708 | -60.0067 | 2026-08-31 18:00:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 66.4 |
| a644c404-aa8b-3ac9-8d0e-7dbd0922c071 | -9.173 | -59.3659 | 2026-08-31 18:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 65.8 |
| 5c90ed24-ad44-3374-86df-d3ce3d7f7272 | -14.2373 | -51.9284 | 2026-08-31 18:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 76.8 |
| d93535bf-d890-3c2c-8758-25dc94368f2f | -6.6541 | -59.4452 | 2026-08-31 18:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 50.5 |
| 1dc31322-170f-32d4-a8c1-ca1ebc58aa2d | -7.6067 | -55.2798 | 2026-08-31 18:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 56.5 |
| 1f222c5e-c092-3f60-9700-2bab55b64640 | -7.5103 | -73.4627 | 2026-08-31 18:00:00 | GOES-19 | MÂNCIO LIMA | ACRE | Brasil | 1200336 | 12 | 33 | nan | nan | nan | Amazônia | 76.1 |
| cc155b2a-9cf0-3afc-ab37-2e107ebb9629 | -7.9158 | -72.2759 | 2026-08-31 18:00:00 | GOES-19 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 58.2 |
| b3614149-1a52-34e1-ab09-011667568ee5 | -8.6852 | -62.9496 | 2026-08-31 18:00:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 72.2 |
| 800f3ac8-3900-3d80-ac25-660c4a518baa | -14.5032 | -52.17 | 2026-08-31 18:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 89.7 |
| e2524249-3914-37bc-a039-c8f8144aa9a1 | -6.8416 | -41.7272 | 2026-08-31 18:00:00 | GOES-19 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 103.0 |
| af1fd2f8-4c5f-3cc9-ae0d-fc59387143a1 | -11.2107 | -45.0786 | 2026-08-31 18:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 114.5 |
| f45323e3-af06-31c7-aa2d-04e0c31ac543 | -3.1267 | -61.1811 | 2026-08-31 18:00:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 273.0 |
| 09daf0e9-5fdb-3d36-b4b7-0abdc46f24ab | -12.2096 | -50.5171 | 2026-08-31 18:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 100.9 |
| a9a9a862-e22b-3d60-9082-28444425cc20 | -10.0105 | -46.4161 | 2026-08-31 18:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 81.0 |
| 056cc063-a9bb-37de-9cca-76de3cee7c42 | -8.6026 | -69.65 | 2026-08-31 18:00:00 | GOES-19 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 67.2 |
| cd447f46-db21-38c3-a65a-4deeb0b35788 | -8.9873 | -65.4379 | 2026-08-31 18:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 94.8 |
| f999c202-a34a-32a8-8040-82b62dfc866b | -8.8953 | -70.8938 | 2026-08-31 18:00:00 | GOES-19 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 69.8 |
| 6bedf551-b44c-3734-a02f-7b542e8c9072 | -10.4794 | -64.5012 | 2026-08-31 18:00:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 48.2 |


[Clique aqui para ver as próximas entradas](README181.md)
