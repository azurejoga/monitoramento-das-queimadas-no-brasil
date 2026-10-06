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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2b5eff78-b31d-3a66-adea-a967e051081c | -9.1531 | -68.237099 | 2026-10-06 01:29:00 | METOP-C | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 88880e9a-2e3a-3288-8658-558a3a0da0b9 | -8.773 | -62.876801 | 2026-10-06 01:29:00 | METOP-C | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 7864027c-c8c0-3d2a-945c-00ebc607a377 | -3.8716 | -55.818501 | 2026-10-06 01:29:00 | METOP-C | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 44c834d5-242a-3ec9-b2a7-3e03ed980a1e | -3.1304 | -53.714802 | 2026-10-06 01:29:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 44426af8-b6d7-3502-b58f-9eef556a0985 | -3.3717 | -58.1875 | 2026-10-06 01:29:00 | METOP-C | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d04ce56f-7b86-32d0-9d2b-3e072576b021 | -3.0571 | -54.176899 | 2026-10-06 01:29:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| aa5faf42-4109-3354-961e-dbd788ea1ce3 | -9.0266 | -65.717499 | 2026-10-06 01:29:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f3cce4da-773b-38fa-ba03-8a8adda69ac7 | -14.9219 | -59.3909 | 2026-10-06 01:29:00 | METOP-C | CONQUISTA D'OESTE | MATO GROSSO | Brasil | 5103361 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ad0fa707-1b4e-3d61-bbb6-607399f28eb7 | -3.7136 | -58.9426 | 2026-10-06 01:29:00 | METOP-C | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 9b5e4bd2-4dc9-3f46-b001-6614a00d74f9 | -3.2868 | -54.193802 | 2026-10-06 01:29:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dda5cdb3-d356-30e0-99e9-edaca84d87e9 | -2.9963 | -54.137402 | 2026-10-06 01:29:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a9b4213d-e411-3ad5-bec1-d6c3e296c819 | -3.3338 | -59.4804 | 2026-10-06 01:29:00 | METOP-C | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 1bf35271-195c-31e6-ada6-96867f25dd69 | -8.9186 | -66.835503 | 2026-10-06 01:29:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 863f19ea-07c9-3ba5-8d76-f5c83cecdfa8 | 3.1215 | -60.575298 | 2026-10-06 01:29:00 | METOP-C | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| fa6bdceb-70c8-3e60-ac6d-843ede53ecd8 | -9.3409 | -64.708397 | 2026-10-06 01:29:00 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| c2574134-924f-3e1e-a209-dc1ce5b69ff2 | -9.1307 | -65.868103 | 2026-10-06 01:29:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| cbfb1e9d-986d-34d8-8e5f-0492ca9d1008 | -8.9212 | -66.847504 | 2026-10-06 01:29:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 4889bb1a-8c78-3015-bcc7-e4fd0f04119c | -3.0916 | -53.723999 | 2026-10-06 01:29:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c89991b2-9c6b-316a-83ea-347459e54c12 | -3.0862 | -54.170101 | 2026-10-06 01:29:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dc3d1b67-9d16-33dd-a928-6ca67f519931 | -3.3356 | -59.4883 | 2026-10-06 01:29:00 | METOP-C | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 1ae6d326-c28f-340c-bc45-d84610bba495 | 2.0057 | -61.087799 | 2026-10-06 01:29:00 | METOP-C | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 20142731-c4e3-39da-91ee-f1ecb4897a55 | -3.5407 | -59.482899 | 2026-10-06 01:29:00 | METOP-C | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 5248c467-1dd2-3160-8740-9f9c46269e6f | -3.1047 | -53.778301 | 2026-10-06 01:29:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f54db387-4d06-3c93-a20d-a1ccac3065b8 | -3.376 | -58.205799 | 2026-10-06 01:29:00 | METOP-C | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2eb03a84-2465-3164-a7fd-97b881a6339a | -3.6901 | -59.637402 | 2026-10-06 01:29:00 | METOP-C | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ba9197d3-0a00-3de6-aa2e-643b2ceddf7a | 1.9793 | -60.617699 | 2026-10-06 01:29:00 | METOP-C | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| d0e10218-1802-3273-81e7-6df1263d8255 | -2.9922 | -54.1203 | 2026-10-06 01:29:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ed8ffba8-eb2b-3558-b5ce-55914154232f | -9.113 | -67.705498 | 2026-10-06 01:29:00 | METOP-C | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a20661a4-d5da-3ddc-937c-989dd76173ea | -14.9137 | -59.4002 | 2026-10-06 01:29:00 | METOP-C | CONQUISTA D'OESTE | MATO GROSSO | Brasil | 5103361 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| cdd1ca82-907e-3c02-a9c2-261ffdf7896b | -3.0539 | -54.248798 | 2026-10-06 01:29:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 29a64804-84a7-38f7-8074-4564c5393582 | -3.0872 | -53.705799 | 2026-10-06 01:29:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3db29998-bb8e-3df8-b90f-d262957bc69c | -2.9299 | -54.116901 | 2026-10-06 01:29:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ca70a040-4e75-3052-9aad-3eb6e4a18b50 | -8.5954 | -66.804398 | 2026-10-06 01:29:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 5aa5ae3f-24ff-3672-9857-cd45abbdb58a | -3.3879 | -58.212601 | 2026-10-06 01:29:00 | METOP-C | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a4cd2219-a825-3742-a208-24afe24138e7 | -9.6723 | -66.829102 | 2026-10-06 01:29:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 0300ae2e-f74c-3190-a854-9e120f849bb6 | -9.8229 | -65.041397 | 2026-10-06 01:29:00 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 0f5d5c15-df32-3692-9e6d-aba9f518fe2f | -2.8896 | -54.162601 | 2026-10-06 01:29:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9af8fcdf-d1e8-3411-84fc-2d91cfb1d018 | -3.6352 | -59.004101 | 2026-10-06 01:29:00 | METOP-C | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 08355b76-f037-3fa4-ba21-7ade808e71bc | -3.6851 | -55.942101 | 2026-10-06 01:29:00 | METOP-C | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 52656c16-8f22-3547-b4e8-762624e4ff68 | -3.104 | -54.2015 | 2026-10-06 01:29:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a7523d5c-25b6-308e-8d06-9798b368f27d | -14.9317 | -59.388599 | 2026-10-06 01:29:00 | METOP-C | CONQUISTA D'OESTE | MATO GROSSO | Brasil | 5103361 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 89487a97-e3af-3318-a75c-f3bb7a0e382f | -2.916 | -54.102001 | 2026-10-06 01:29:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a82ba258-0d43-346f-b632-8a5cdb335a14 | -3.3858 | -58.203499 | 2026-10-06 01:29:00 | METOP-C | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 122c75c3-bdc3-391e-a908-034a571978f6 | -3.096 | -53.742199 | 2026-10-06 01:29:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7838571b-8883-3174-9546-2d25b982fc1f | -2.9202 | -54.119202 | 2026-10-06 01:29:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a7d8e496-46cc-3078-89c4-c704ab144a61 | -3.0019 | -54.118 | 2026-10-06 01:29:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8d106637-d7a1-3c28-b941-ecbdb17b206b | -3.0652 | -54.210701 | 2026-10-06 01:29:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6253b8c6-e913-3749-a41f-cd8d6eeacef2 | -2.8814 | -54.128399 | 2026-10-06 01:29:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 406ee82e-be8f-3e59-bfad-ed89dc4dced1 | -9.7311 | -65.091103 | 2026-10-06 01:29:00 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| f0a4e8f7-e792-33d2-8b9d-3d95f80f1d00 | -14.8752 | -57.573898 | 2026-10-06 01:29:00 | METOP-C | NOVA OLÍMPIA | MATO GROSSO | Brasil | 5106232 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 18ab7af2-33f5-368d-99d5-47dfb278ec74 | -3.0196 | -53.892899 | 2026-10-06 01:29:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 32d24efe-bd98-3591-b05d-0a3b88c8feb2 | -9.0245 | -65.707298 | 2026-10-06 01:29:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f7b818e3-4436-3308-a00e-00987004011b | -9.4638 | -64.330704 | 2026-10-06 01:29:00 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| adaf006c-19ed-39e0-8795-246d04421ecf | -2.9866 | -54.139702 | 2026-10-06 01:29:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 52640c05-d319-3c58-a0d1-79da77f8986e | -9.1563 | -68.252098 | 2026-10-06 01:29:00 | METOP-C | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6aea65df-3e5b-3ea1-90e4-8cc70243794a | -3.1056 | -53.739899 | 2026-10-06 01:29:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bdbf3b4e-9c35-36f3-b352-ff63c82c0c94 | 2.0155 | -61.09 | 2026-10-06 01:29:00 | METOP-C | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| f666c7b8-5c7d-3575-b5ff-0bd0b74e6405 | -14.9333 | -59.395599 | 2026-10-06 01:29:00 | METOP-C | CONQUISTA D'OESTE | MATO GROSSO | Brasil | 5103361 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| debe1e4e-b4d0-3af7-84de-f9153bb97097 | -2.9519 | -54.165901 | 2026-10-06 01:29:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3c24d0fd-3bdc-31a5-be57-3fcec01a0e2e | -3.0668 | -54.174599 | 2026-10-06 01:29:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7337bceb-2e6e-3063-ad55-291ca6c936d7 | -8.3497 | -62.8242 | 2026-10-06 01:29:00 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 154cb664-aa4f-391d-b47f-d64d5b7c33e3 | -9.7291 | -65.081497 | 2026-10-06 01:29:00 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 46402bdf-bfd3-3e40-8346-476fac766dea | 3.5658 | -61.3386 | 2026-10-06 01:29:00 | METOP-C | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| a7ad00e9-60c0-3633-9e40-bfca9e86641c | -9.166 | -68.250099 | 2026-10-06 01:29:00 | METOP-C | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 873c3dac-9ef4-3039-9292-ad53c341c246 | -2.934 | -54.133999 | 2026-10-06 01:29:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 192102b1-5f87-3071-a825-83b8765cb4ce | -2.1389 | -56.710098 | 2026-10-06 01:29:00 | METOP-C | FARO | PARÁ | Brasil | 1503002 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 89c20c66-8039-35b4-b101-ef94537bfb73 | 3.5676 | -61.330898 | 2026-10-06 01:29:00 | METOP-C | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 3e5b1449-ae90-33cb-8c5d-d9e687ad37c9 | -14.3032 | -57.471001 | 2026-10-06 01:29:00 | METOP-C | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7eaa92d2-3caa-3f66-b837-9b2e62c2f406 | -9.4846 | -64.050003 | 2026-10-06 01:29:00 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 01250519-67a5-3eb7-a105-a004b8c55f2f | -12.1315 | -63.151299 | 2026-10-06 01:29:00 | METOP-C | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| d7ab475a-1bca-3272-8b7e-b58be774528e | -2.8716 | -54.1306 | 2026-10-06 01:29:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4e8be449-0ec5-316d-837a-0eff6a2be95b | -3.3277 | -59.498402 | 2026-10-06 01:29:00 | METOP-C | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 55e38c3d-e6c7-31dd-8bd6-cb3dcb1f701e | -2.8839 | -54.1819 | 2026-10-06 01:29:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 057cac78-2410-32a7-8292-bf66d0ee3b92 | -10.2759 | -60.543098 | 2026-10-06 01:29:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 71441ff4-8631-3a67-82c8-f6f70333ec4d | -3.0498 | -54.232101 | 2026-10-06 01:29:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7bea3fde-4993-3e71-a926-5fdbe97263ef | -2.9478 | -54.1488 | 2026-10-06 01:29:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f96de802-ce85-313d-8976-a9a83353f7cb | -9.1209 | -65.870201 | 2026-10-06 01:29:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 7f13ae47-3b1d-369f-8685-55bea60b0f14 | -2.7816 | -54.097099 | 2026-10-06 01:29:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 23f49891-fedf-3088-804c-2e976e1c035c | -3.1003 | -53.7603 | 2026-10-06 01:29:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 55a19b46-7243-3631-a043-b12dd086155f | -2.7719 | -54.0994 | 2026-10-06 01:29:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 41baa4f7-63da-3e83-bda6-4c6c3e015918 | -9.7193 | -65.083603 | 2026-10-06 01:29:00 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| c9dcc2f8-5560-32bb-93ce-db1608e42158 | -3.0555 | -54.213001 | 2026-10-06 01:29:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 933b8cc1-43c4-3989-9df3-71820817d5f5 | -3.3375 | -59.496201 | 2026-10-06 01:29:00 | METOP-C | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b77f0692-5ee3-3af6-9eb6-59495e7e949b | -2.9616 | -54.163601 | 2026-10-06 01:29:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 370ba58d-8ec5-3a52-a02c-df908a8fcb3e | -3.0636 | -54.246498 | 2026-10-06 01:29:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1d4d3d1f-7f21-303a-b978-4b3535486d62 | -9.7332 | -65.1007 | 2026-10-06 01:29:00 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| d3856501-b3a1-3613-867e-e2e21a5901f1 | -8.5979 | -66.8162 | 2026-10-06 01:29:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 1a8cbbd2-9130-3d79-9f5b-192cf31b6667 | -2.9381 | -54.1511 | 2026-10-06 01:29:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9d71bde9-db0a-3a66-9b6d-2d03e25c9410 | -2.7858 | -57.667099 | 2026-10-06 01:29:00 | METOP-C | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| add746b2-6c47-3a71-ba71-738489e0e5c0 | -2.7879 | -57.6843 | 2026-10-06 01:30:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 82.4 |
| 2ea730de-33f9-330a-af4e-4cca7b0452e4 | -3.3906 | -58.1953 | 2026-10-06 01:30:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 93.9 |
| 7811f421-a66c-39f5-bea3-12c605b3b2c6 | -2.7796 | -54.0937 | 2026-10-06 01:30:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 80.1 |
| 44f0862e-345f-3af2-80af-3c744b0cfa61 | 3.5647 | -61.3246 | 2026-10-06 01:30:00 | GOES-19 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 65.6 |
| eac6cfcc-7e65-307e-a5f7-7ff095e1f579 | -3.1115 | -53.7637 | 2026-10-06 01:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 87.2 |
| 0e233ee9-4a7b-3e16-814b-28786a4a9468 | -11.2607 | -45.5078 | 2026-10-06 01:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 81.5 |
| cabbe85e-7444-3fc0-a534-67be996fceb3 | -3.1116 | -53.7234 | 2026-10-06 01:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 65.7 |
| 52cf8543-5217-3865-a154-0197091cfd43 | -11.2802 | -45.4823 | 2026-10-06 01:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 119.8 |
| 2dd7108c-876f-3140-ae35-bdb70002a908 | -3.0375 | -53.9066 | 2026-10-06 01:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 60.6 |
| 363d6782-2583-3616-8104-e2b596bbc1e2 | -3.6731 | -55.9622 | 2026-10-06 01:30:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 79.1 |
| 20d4e17c-72d0-353d-9451-8aa1bba03be7 | -2.7879 | -57.6649 | 2026-10-06 01:30:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 68.3 |


[Clique aqui para ver as próximas entradas](README14.md)
