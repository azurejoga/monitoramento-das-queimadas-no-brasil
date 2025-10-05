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

## Dados Diários - Página 144

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7f4d71cb-c181-3668-8464-ec5e932b9f0f | -10.82886 | -57.19861 | 2025-10-05 05:36:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 91ac2add-79d7-347a-830e-64c389bc131b | -9.65793 | -63.79377 | 2025-10-05 05:36:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a3f5fb9f-8cca-36a4-bc35-623b31dc643f | -9.57257 | -62.26132 | 2025-10-05 05:36:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fd823d7a-9ef3-33f7-a79b-212bafff640f | -11.76158 | -64.92837 | 2025-10-05 05:36:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 38aa08f7-15d9-324e-8e8a-c1fc688789a8 | -9.84029 | -59.46982 | 2025-10-05 05:36:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6ae8c46a-17d9-3b94-a7a3-4241bcfa0221 | -12.30006 | -55.14342 | 2025-10-05 05:36:00 | NOAA-20 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4a6efec5-5304-3a60-aa01-a8c2735077c5 | -14.74144 | -54.62056 | 2025-10-05 05:36:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 03966e7a-78f0-31f3-94a6-44bf262513f7 | -9.52812 | -62.80772 | 2025-10-05 05:36:00 | NOAA-20 | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 85d02c7f-c152-37f0-95a3-38bd102d403a | -12.98031 | -51.05005 | 2025-10-05 05:36:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 1f0d9606-113f-395a-ace8-7857da66993d | -12.97314 | -51.04926 | 2025-10-05 05:36:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 139f4745-25aa-3878-ab5a-25337067b564 | -9.10175 | -61.5318 | 2025-10-05 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 107ee469-1bb9-361e-ae02-3e708e614ef6 | -10.82817 | -57.20372 | 2025-10-05 05:36:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5cdc1068-e9ff-34df-b7a2-c891420e6559 | -10.839 | -57.19474 | 2025-10-05 05:36:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f814b7cf-c95f-3838-8e7d-fcbf680657da | -12.31753 | -55.13834 | 2025-10-05 05:36:00 | NOAA-20 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0400c176-d7c8-37f4-86b4-032dc9c081e9 | -8.42294 | -70.12231 | 2025-10-05 05:36:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e5556082-676c-330d-9ccb-69d4daa38ab2 | -11.204 | -54.85323 | 2025-10-05 05:36:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 33008ba9-6232-3440-9023-92e46ef006ab | -9.33325 | -54.52786 | 2025-10-05 05:36:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cb07c164-e728-32a2-8877-459027af6057 | -9.84429 | -59.47038 | 2025-10-05 05:36:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 15152b29-edac-3bec-9ccb-f2283274a94b | -11.87284 | -56.88803 | 2025-10-05 05:36:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 10.4 |
| cdd8600e-be0e-36c8-b130-5396aef69c28 | -10.65249 | -58.75568 | 2025-10-05 05:36:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cb5bb641-9ec5-3fb8-939c-1f8bdf5ba914 | -9.02081 | -58.9863 | 2025-10-05 05:36:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 20647341-1910-3e76-b1d3-46019018a30e | -12.41401 | -51.11195 | 2025-10-05 05:36:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d964a0dd-e127-3293-af20-b636b5db467c | -9.56133 | -63.23213 | 2025-10-05 05:36:00 | NOAA-20 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 23bf97b5-e361-344f-9d23-039b831d652a | -10.46056 | -57.5012 | 2025-10-05 05:36:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 21036b21-1644-306c-ae58-b4752df26c76 | -11.20999 | -54.98491 | 2025-10-05 05:36:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0c7a6875-6d59-36c2-9122-934f42a89a05 | -9.63712 | -54.31453 | 2025-10-05 05:36:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f2eb5227-741d-3a5e-8dd3-0a280a844fa1 | -10.1825 | -58.18116 | 2025-10-05 05:36:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| adb3ec8e-74b8-383e-b3d0-49096fefa47b | -10.65196 | -58.75959 | 2025-10-05 05:36:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f70157e0-016f-3b5b-ae2b-55830d1e723c | -10.17913 | -58.17952 | 2025-10-05 05:36:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a2bac6af-59c8-3488-98ac-5b7676e61c78 | -9.10527 | -61.53234 | 2025-10-05 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fc29cc25-30c0-36e9-b58b-523cf4899e79 | -12.41477 | -51.10498 | 2025-10-05 05:36:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 30f975b4-2bcb-388b-bac0-c3518a761b53 | -11.76213 | -64.92486 | 2025-10-05 05:36:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8a2c8fbe-c526-39d5-857a-747142252d11 | -12.32047 | -55.16067 | 2025-10-05 05:36:00 | NOAA-20 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1ff2e0d9-cf83-3ddc-a2b6-e52b67776f6d | -9.93501 | -62.26796 | 2025-10-05 05:36:00 | NOAA-20 | VALE DO ANARI | RONDÔNIA | Brasil | 1101757 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| acd8b476-5dbf-3e2d-9273-c27974c3502c | -10.45923 | -57.51089 | 2025-10-05 05:36:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cceece13-140e-3049-9753-3de3c2066204 | -12.31243 | -55.13401 | 2025-10-05 05:36:00 | NOAA-20 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 348115cc-5a0e-3b9c-8f44-50572d6f8e97 | -11.86933 | -56.87642 | 2025-10-05 05:36:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 6e53f87f-5a98-3116-9c38-90e19f5f0857 | -10.46515 | -57.5019 | 2025-10-05 05:36:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 22f5d98f-b314-330a-973a-1b53d879bc4b | -9.33422 | -54.52039 | 2025-10-05 05:36:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f43be785-2b56-31ec-9208-7f5c8ebcc79a | -11.45958 | -51.51685 | 2025-10-05 05:36:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ee08692c-2def-33bd-a921-2f11baf24ed5 | -11.87043 | -56.88574 | 2025-10-05 05:36:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 6a97bb35-496c-3912-ac79-766056a939f5 | -9.32917 | -54.5159 | 2025-10-05 05:36:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9d17f47f-dc42-3091-b61b-bc79c92092aa | -9.90781 | -63.58487 | 2025-10-05 05:36:00 | NOAA-20 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 42213021-8f8c-3d1d-903b-f21a76aed270 | -11.93568 | -64.03157 | 2025-10-05 05:36:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b1d5583f-8fd8-379f-a5e1-f2e3631925d3 | -14.82445 | -54.77215 | 2025-10-05 05:36:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 65d1e1fc-bf8d-3894-99d6-d36f29ad203d | -8.67181 | -64.10516 | 2025-10-05 05:36:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b309e3d6-0b4f-3f0a-89ec-5760bc58d003 | -10.83771 | -57.1688 | 2025-10-05 05:36:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b73a1b4f-c797-3861-a3e9-dc42fd74c127 | -14.74344 | -54.65633 | 2025-10-05 05:36:00 | NOAA-20 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4ea10913-2f98-39c6-8147-b829a3093884 | -8.43394 | -70.12183 | 2025-10-05 05:36:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.4 |
| cba00fdf-9ad0-35c5-892e-072c88d1ef8b | -11.4574 | -51.52742 | 2025-10-05 05:36:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ee8c11e7-2fbb-3982-be92-618924c5c44c | -9.3103 | -60.54827 | 2025-10-05 05:36:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5312d10a-43ad-31e7-98bb-4858635cdd95 | -10.64465 | -69.03681 | 2025-10-05 05:36:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fd6dd321-88b3-304a-a1fc-37c997c8e564 | -9.12036 | -61.76423 | 2025-10-05 05:36:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f7c32f0d-6860-3668-8b89-739e7935ab4d | -10.4638 | -57.51167 | 2025-10-05 05:36:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 58199ffb-28ea-37ad-bb54-8c42139d8c87 | -9.84418 | -60.27336 | 2025-10-05 05:36:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2f05e265-1f03-3efd-b469-32ea5c205dd3 | -10.46581 | -57.49709 | 2025-10-05 05:36:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0eb8427a-ead0-3808-bf68-5887471045ea | -11.76489 | -64.9289 | 2025-10-05 05:36:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4db50359-3e99-33d3-9fa5-327b73135e5b | -11.87116 | -56.88027 | 2025-10-05 05:36:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 5a675113-0762-35a7-bc8d-06d23830472a | -10.62564 | -68.89284 | 2025-10-05 05:36:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 798a8b20-eb31-3faf-bd02-7009a43c8b08 | -9.93857 | -65.15439 | 2025-10-05 05:36:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e5af656e-5979-3529-aa20-522d90b013eb | -11.45199 | -51.52257 | 2025-10-05 05:36:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2f069666-d5c3-3ba1-a29e-0d5db65b2999 | -9.63485 | -54.31411 | 2025-10-05 05:36:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 81dabe04-09ff-3584-b8ba-c428525d4194 | -11.39905 | -55.17562 | 2025-10-05 05:36:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cc863ee9-3294-3f66-a8aa-759fdee2259b | -9.92106 | -67.3426 | 2025-10-05 05:36:00 | NOAA-20 | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e3572f02-eedb-3f3b-8c10-39dde638a04a | -9.33878 | -54.5286 | 2025-10-05 05:36:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0afcfc0f-37d6-31cd-8914-605e4d080c6a | -11.77101 | -64.86867 | 2025-10-05 05:36:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 311e0834-00d1-3f76-af5c-7b08adace4db | -12.30516 | -55.14782 | 2025-10-05 05:36:00 | NOAA-20 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 465a0200-b68c-388d-8652-90eb034be109 | -14.74879 | -54.66195 | 2025-10-05 05:36:00 | NOAA-20 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a1746d0e-3c65-3dd7-86da-3a1d158f720f | -12.32221 | -55.14621 | 2025-10-05 05:36:00 | NOAA-20 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0463ff2e-2571-3cfc-b7fa-f56c6a09844b | -14.58414 | -52.46138 | 2025-10-05 05:36:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3dc09cb3-6724-3866-9f27-dd0b32b6c0b1 | -8.43467 | -70.11772 | 2025-10-05 05:36:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 94fd3973-42de-3bf7-816e-2cb5d8c3e6c5 | -8.82359 | -64.23985 | 2025-10-05 05:36:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f0247a9a-1a28-3984-b09a-f32f4e9a14f6 | -9.31256 | -60.54604 | 2025-10-05 05:36:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0b28ea5e-fba2-3674-acb1-04add0b73ee8 | -10.17813 | -58.18057 | 2025-10-05 05:36:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| dcbbfca8-f460-33b0-b22c-c4540a5ddfe4 | -8.17951 | -63.88768 | 2025-10-05 05:36:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3f081494-9d16-3e7b-8c70-16e3813139dd | -9.37175 | -62.29296 | 2025-10-05 05:36:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0b5117ef-d0cc-34d1-aadf-f49445e2a375 | -14.74096 | -54.62489 | 2025-10-05 05:36:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bf516e36-0da8-3164-af5c-78679828639d | -9.91222 | -58.56439 | 2025-10-05 05:36:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5be4570f-d1e3-3215-9c27-2643dd3c6d6f | -14.29782 | -52.92758 | 2025-10-05 05:36:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 1a7407e7-3ca2-3719-adf0-c86c91b11bf3 | -10.84423 | -69.30471 | 2025-10-05 05:36:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1c25132c-f100-3726-beb4-ceb7fcd20a6e | -12.96422 | -50.9973 | 2025-10-05 05:36:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 419676d0-ca63-3a8a-a050-a7ded6790e66 | -9.14176 | -60.29638 | 2025-10-05 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e9f03c2a-f30e-3834-8ba5-2f0bd2a8c28c | -9.14996 | -59.54018 | 2025-10-05 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e75dcaef-ae94-39ed-80ef-ea97b0bcabf1 | -8.83293 | -62.36042 | 2025-10-05 05:36:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9cda6878-3fdf-381b-b9e1-817685d10f17 | -10.35758 | -58.4529 | 2025-10-05 05:36:00 | NOAA-20 | JURUENA | MATO GROSSO | Brasil | 5105176 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4f296fc9-f292-3904-ba5f-7c4b560d7159 | -8.42225 | -70.12643 | 2025-10-05 05:36:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 56e122a1-6c40-354d-90a1-1340dbb0d98e | -9.19165 | -62.53174 | 2025-10-05 05:36:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f7fa519a-3d45-3ad5-99f6-c1a260dc0078 | -9.32166 | -54.53029 | 2025-10-05 05:36:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a4be4cd7-9f65-3c7a-8f89-74765e805f44 | -11.8287 | -60.48201 | 2025-10-05 05:36:00 | NOAA-20 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7437137b-56df-34f9-b29b-fcf6b0767787 | -14.82492 | -54.76786 | 2025-10-05 05:36:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e9a25825-4efe-3cc0-953f-1c23a28d130e | -13.732 | -51.31063 | 2025-10-05 05:36:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b650d3f9-6e61-3688-b07e-3c539480be1f | -12.3209 | -55.15707 | 2025-10-05 05:36:00 | NOAA-20 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c06e3ce4-5a3f-3220-bdcf-ddf96a8e510b | -8.42964 | -70.12108 | 2025-10-05 05:36:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.7 |
| dead18de-d541-31d9-af9e-5befc09dd4de | -9.13392 | -61.87261 | 2025-10-05 05:36:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 59a0cf3d-a91a-3259-9dd9-aa560bb4fa0a | -9.32819 | -54.5234 | 2025-10-05 05:36:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d4de9f3e-70b5-31bc-bc3e-d9143bfeab0a | -12.97391 | -51.04211 | 2025-10-05 05:36:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 10.3 |
| af55902c-3ef4-311b-b1f1-ba17a9cac48f | -9.79516 | -62.29394 | 2025-10-05 05:36:00 | NOAA-20 | VALE DO ANARI | RONDÔNIA | Brasil | 1101757 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8d63526e-5e69-329b-88b4-26927d6e736e | -12.3171 | -55.14197 | 2025-10-05 05:36:00 | NOAA-20 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9210bfc6-e6cc-31ae-ac71-43d812b83434 | -8.42724 | -70.12309 | 2025-10-05 05:36:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.5 |
| dd239a17-f998-36b8-9d0c-93d4ee97c067 | -10.83564 | -57.18407 | 2025-10-05 05:36:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |


[Clique aqui para ver as próximas entradas](README145.md)
