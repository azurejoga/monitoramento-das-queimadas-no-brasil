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

## Dados Diários - Página 33

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 229b8814-584b-3a9c-bc9e-0a59738f3229 | -7.94781 | -71.46284 | 2026-08-12 05:55:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9308e75f-33b8-33c9-914e-524de9e5cc3c | -8.95353 | -60.56875 | 2026-08-12 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a0ad64ad-044e-3533-8c7a-3914e88bebf1 | 0.18481 | -60.48877 | 2026-08-12 05:55:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e0044441-e4aa-37f3-a1d7-c3d774a62828 | -8.9547 | -60.55976 | 2026-08-12 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 49a8cded-b1e8-31a0-9249-bfe7fd955962 | -8.95244 | -60.49678 | 2026-08-12 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4b90b5a4-6466-3185-8273-35ba6bdecf06 | -8.96192 | -60.50442 | 2026-08-12 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9a37c0a9-e320-3cae-be51-bb38b6f76eea | -8.9607 | -60.51374 | 2026-08-12 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 9039378b-f520-3ffe-8a9f-a80e1e85a477 | -8.95751 | -60.53822 | 2026-08-12 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| ab49f912-3109-37bf-ab68-4be874319d8d | -8.98392 | -60.53595 | 2026-08-12 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 93053f44-7c58-37d5-9e1f-d9eb72f6a8f4 | -7.90023 | -71.60126 | 2026-08-12 05:55:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ecbef8ac-3af3-3dbe-8f92-f1e583f7b2c2 | -8.95278 | -60.53442 | 2026-08-12 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| b59b23e7-8c84-3c55-baed-56cac7585b43 | -8.95597 | -60.50993 | 2026-08-12 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 83ecba06-92a8-399a-a9bf-773860193924 | -8.89916 | -60.56394 | 2026-08-12 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| df1f10bd-96df-3ffd-a166-eec5d92ba433 | -9.7616 | -60.76062 | 2026-08-12 05:55:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cdc6c323-016b-34ab-ac7c-f202f4281b53 | -6.59155 | -59.0099 | 2026-08-12 05:55:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 174f1cea-85f3-3889-b9a5-0e3a58f8f6e9 | -8.94687 | -60.53977 | 2026-08-12 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 26636d98-8f0c-3d1f-a3e5-d118bd6d1ebe | -6.59704 | -59.01077 | 2026-08-12 05:55:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 7c75f9bc-9f8d-3171-9fb8-838c3f9e73e4 | -8.96151 | -60.50753 | 2026-08-12 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e4323952-3838-3e42-b2af-d00742ba5a75 | -8.95318 | -60.53138 | 2026-08-12 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 6e8e45ef-da9f-3eef-95e7-3f897c891631 | -8.94651 | -60.5022 | 2026-08-12 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 58cfad74-73c4-3376-b302-d389fd207063 | -8.95557 | -60.51302 | 2026-08-12 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 8891ab49-1a2f-339a-97fd-b538ddb4ffab | -8.94766 | -60.5337 | 2026-08-12 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f141f75e-63d7-3bea-83fa-fa5381bdaa17 | -8.94845 | -60.52758 | 2026-08-12 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3f05681a-c19a-3955-a53f-74a4a71405cb | -6.61544 | -58.99904 | 2026-08-12 05:55:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 100b27b5-6492-366a-9264-1c8ccd9a7e46 | -8.89793 | -60.5731 | 2026-08-12 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 62b84172-4f40-3b24-a363-5bbb513268c0 | -8.95204 | -60.49988 | 2026-08-12 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 24535c83-bf3e-3c63-8a4e-c30fcf17c842 | -8.9457 | -60.50841 | 2026-08-12 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6d83322a-0062-3193-8f79-23d1e060bfa3 | -6.59752 | -59.00721 | 2026-08-12 05:55:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| bd392b1e-1313-3add-9996-1eca010b21bc | -7.40704 | -59.99316 | 2026-08-12 05:55:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e061768d-e7b0-380a-ac25-06610b31d2b0 | -9.76038 | -60.7697 | 2026-08-12 05:55:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cbb8ce4c-2689-3f32-a8d9-74c0f55fada8 | -8.8971 | -60.57924 | 2026-08-12 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e3fe6481-182c-3f10-b7f7-7db647879fb5 | -9.47502 | -60.51399 | 2026-08-12 05:55:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4934faa6-7fe4-3ae1-9344-dc6487fd3d05 | -11.11002 | -62.88865 | 2026-08-12 05:55:00 | NOAA-21 | MIRANTE DA SERRA | RONDÔNIA | Brasil | 1101302 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7df78aa3-3b62-3323-b3cc-b32d04941164 | -7.40185 | -59.99235 | 2026-08-12 05:55:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ac160b87-534f-3e67-98d2-9875d24b19a4 | -8.9018 | -60.58298 | 2026-08-12 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3200d71a-3a6e-3b1b-9e9b-18ab2b08be04 | -6.8491 | -59.10051 | 2026-08-12 05:55:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0c331247-5353-366c-8720-133afe3f42e7 | -7.41615 | -60.0044 | 2026-08-12 05:55:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 91acfe5d-6523-3c57-adea-4cdb76458d70 | -9.75928 | -60.76165 | 2026-08-12 05:55:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 142d10b0-d1ea-35ea-bf23-3810f9637f3b | -9.76079 | -60.76668 | 2026-08-12 05:55:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b7335504-ea1f-312f-b2f6-a1e5a78f5fd0 | -8.89669 | -60.58228 | 2026-08-12 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b8bfd389-cd84-3491-ba71-00a5c4376ae0 | -9.76362 | -60.76843 | 2026-08-12 05:55:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ccaa5222-2ffa-3e38-a1a8-5c33b1089a07 | -8.95358 | -60.52833 | 2026-08-12 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| fd0f612f-c054-345c-b09a-a267fbb37bad | -8.89446 | -60.56015 | 2026-08-12 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 5bb4eca9-d109-3b5f-9aa4-97194d5da7e1 | -8.90221 | -60.57993 | 2026-08-12 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ce7e32f0-46c6-36fb-a709-6153588592f0 | -10.81697 | -65.08958 | 2026-08-12 05:55:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 67091a6b-5fb9-3222-af3a-49d2d9ff5e33 | -8.95632 | -60.54731 | 2026-08-12 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 6ad63a12-6733-390e-b370-e01e6c333a93 | -7.41181 | -59.99717 | 2026-08-12 05:55:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| af53ddac-cb13-3775-bc9c-74e5c9479e25 | -9.76324 | -60.77144 | 2026-08-12 05:55:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 891effdb-071a-38d9-95bd-8ce07103a595 | -8.98606 | -60.59841 | 2026-08-12 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 431ed006-91a3-387c-b6ac-4f2bc5ef9baa | -9.76439 | -60.76238 | 2026-08-12 05:55:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ac67fd31-b80b-3479-a824-23421f818180 | -8.96263 | -60.53899 | 2026-08-12 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e9677337-3b97-3875-bcda-11d151e63ed3 | -8.94531 | -60.5115 | 2026-08-12 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 101d6c0f-7266-3aef-b3ab-6aa45c8a2cfe | -6.8496 | -59.09687 | 2026-08-12 05:55:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c4f0e1c0-cdbc-352b-b7ec-8f99ae3c0dea | -9.07143 | -60.40494 | 2026-08-12 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6981ded0-f50b-361c-96d8-3a33afd8cb00 | -8.94731 | -60.49599 | 2026-08-12 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 156ff880-5a00-3acf-8af0-b28aa9d071ef | -8.89547 | -60.59138 | 2026-08-12 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 46c5c81b-af46-3830-8dd1-d163075bec44 | -8.95391 | -60.56581 | 2026-08-12 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5eb5ff0c-6787-3ee2-8235-5b8782fad4bd | -8.96303 | -60.53596 | 2026-08-12 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| aa8000d0-b46c-30be-b4a2-08a6263961fb | -7.40619 | -59.99961 | 2026-08-12 05:55:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 262846f5-7362-308b-bd1b-d233a8ab4f15 | -7.41138 | -60.00043 | 2026-08-12 05:55:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 13288a02-c6b9-327b-be10-672904d48fc8 | -5.15725 | -62.529 | 2026-08-12 05:55:00 | NOAA-21 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ad3126dd-4148-3990-b0c4-f43acde24415 | -8.96111 | -60.51063 | 2026-08-12 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 320661da-1f98-3172-8b9e-2c45604bbc07 | -7.40094 | -59.98985 | 2026-08-12 05:55:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bad9aabc-bdc3-3834-bd6a-95413ff46650 | -8.95718 | -60.50062 | 2026-08-12 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0b13fc6f-1c74-35b9-afbf-64958b7c2eab | -6.59107 | -59.01345 | 2026-08-12 05:55:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d3516eb9-2cd0-3b18-a555-7352462e8510 | -9.7612 | -60.76366 | 2026-08-12 05:55:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 00653ced-ffb0-3416-8ccd-a5ea830ed28e | -8.94372 | -60.52375 | 2026-08-12 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ac56c6b6-7f3e-3380-aac9-5d86862f23d6 | -8.95044 | -60.51226 | 2026-08-12 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 71290d98-2afd-3510-8d21-285f71cee8c9 | -8.89997 | -60.55789 | 2026-08-12 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 9118df23-66c8-35ff-9e80-e09fe0592f0f | -8.94805 | -60.53065 | 2026-08-12 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1e85f5fe-2220-33e7-b18a-b826f7332bec | -7.41095 | -60.00367 | 2026-08-12 05:55:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7a24b381-aec0-3e48-89fb-32af461b8c2d | -7.41053 | -60.00681 | 2026-08-12 05:55:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 63652840-b91e-38ff-9369-67ce57278e04 | -9.76873 | -60.76912 | 2026-08-12 05:55:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6874169d-f70d-3d82-bf52-3df17f0af9fc | -9.07102 | -60.40814 | 2026-08-12 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8827fac7-2f7c-39e7-940b-22629dae0939 | -8.9543 | -60.56284 | 2026-08-12 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c4009f0c-f78d-3e8e-9c85-c6d4e4f8e12a | -8.89834 | -60.57004 | 2026-08-12 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 40625cce-5e58-3d1f-ba66-2ca1eb141185 | -8.89405 | -60.56318 | 2026-08-12 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c1f50c46-bd23-3283-b33f-c8329b69517f | -9.72355 | -60.20396 | 2026-08-12 05:55:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3e71ef11-ae3f-36b6-b907-e7775f3449f9 | -8.95199 | -60.54048 | 2026-08-12 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 918c11a5-bb25-3934-8008-30009804c01c | -8.95239 | -60.53746 | 2026-08-12 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 55b2a2a2-a4a2-3741-851a-eecf24301193 | -8.94726 | -60.53675 | 2026-08-12 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 604664be-d658-3eda-af28-1940c2d57a0e | 0.18549 | -60.49316 | 2026-08-12 05:55:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7e411f29-98e2-3d85-ab82-e4e5ebb7b01e | -8.94611 | -60.5053 | 2026-08-12 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6ae8af6c-1eef-3262-af1e-7b425f1bc76c | -8.95511 | -60.55664 | 2026-08-12 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 836175a8-cf77-3740-a451-1228928e5e2b | -8.9583 | -60.53215 | 2026-08-12 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| e9bd5bf5-3b84-3be5-bdd5-da74cb9049df | -8.89588 | -60.58833 | 2026-08-12 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8d90b714-ef67-30da-a46a-3c9ea773c749 | -8.95677 | -60.50373 | 2026-08-12 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| fb32c057-3715-3d0b-a2dd-a424e75265d5 | -8.95637 | -60.50684 | 2026-08-12 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 89baba47-f971-32f6-bcd4-c944bc8d1eaf | -7.41658 | -60.00117 | 2026-08-12 05:55:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6f596f02-b455-30bb-87d4-ddc87c770dbf | -9.76478 | -60.75933 | 2026-08-12 05:55:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4357f74e-b567-3007-aee8-7de7cf21926f | -8.89957 | -60.56091 | 2026-08-12 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 693e799a-be50-3b35-81d1-c50c4b05f3d7 | -9.47462 | -60.51714 | 2026-08-12 05:55:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c1fa234e-ba87-34c2-a6d2-539bcf09b1eb | -8.95592 | -60.55042 | 2026-08-12 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 5ba5caf6-49e3-3780-87ff-f11b41892483 | -8.95672 | -60.54425 | 2026-08-12 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bb511715-0809-3ff9-9957-7f5ebbe79872 | -8.9788 | -60.53518 | 2026-08-12 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2df9b163-dca2-3472-80c4-54a6af66dce3 | -8.95123 | -60.50609 | 2026-08-12 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 81624449-997c-339d-afe8-4f768cf4e713 | -11.9527 | -46.3899 | 2026-08-12 06:00:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 55.8 |
| c5e08c77-a090-37a6-8c41-f02986d3bb2c | -8.96 | -60.5358 | 2026-08-12 06:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 63.9 |
| d2927ae8-8192-3cc1-8d92-684bdea0f068 | -6.88932 | -41.94221 | 2026-08-12 06:14:00 | AQUA_M-M | SÃO JOÃO DA VARJOTA | PIAUÍ | Brasil | 2209955 | 22 | 33 | nan | nan | nan | Caatinga | 9.7 |
| 6e24c79d-1e51-31f1-b4a8-536634c03436 | -6.99684 | -42.62772 | 2026-08-12 06:14:00 | AQUA_M-M | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |


[Clique aqui para ver as próximas entradas](README34.md)
