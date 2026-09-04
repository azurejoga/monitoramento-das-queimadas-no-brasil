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

## Dados Diários - Página 28

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ab4c691c-7774-3809-b522-4760d4920406 | -8.56691 | -63.19339 | 2026-09-04 05:23:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e8a58803-a00e-3472-ac7b-89060a35371a | -6.77967 | -58.95607 | 2026-09-04 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8df6a2b3-1add-30ea-8c9b-239be776aafc | -6.35562 | -65.48683 | 2026-09-04 05:23:00 | NOAA-21 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c6781d93-cbb1-3d80-ae45-407cc2c3aa44 | -3.14109 | -61.21531 | 2026-09-04 05:23:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 3210209f-b1ed-3e95-8b5b-a01446977ccd | -2.89775 | -57.18604 | 2026-09-04 05:23:00 | NOAA-21 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0e1c807c-4fd4-3b88-a5cf-22c2983413de | -6.12689 | -59.89218 | 2026-09-04 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5e71a2ea-3213-3a1f-bbf3-bbbb521ed72d | -6.55124 | -58.54405 | 2026-09-04 05:23:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9c087f4d-1ff3-3884-acae-645c06c3204a | -3.12375 | -61.22298 | 2026-09-04 05:23:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 31a82253-cd9d-3336-a9e8-4ba86a136409 | -6.88892 | -59.40527 | 2026-09-04 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0792c534-d5bb-369f-9bfe-76a47e894d1d | -6.68526 | -59.97502 | 2026-09-04 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 27.7 |
| 497a5e46-af65-32f2-bbaf-0d455bb3178f | -8.69126 | -62.87809 | 2026-09-04 05:23:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3c1a3692-dd04-30b3-b4ab-0fc030559ca8 | -10.2908 | -68.85593 | 2026-09-04 05:25:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 27fb3e61-143a-36be-8a68-a9be0df68a4c | -4.19669 | -59.94871 | 2026-09-04 05:25:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 308e3216-3463-3af6-bfe7-9a469dd26d9e | -9.03855 | -65.74268 | 2026-09-04 05:25:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 466321f8-bb5e-3565-b298-b1ec66a1e1a6 | -5.96191 | -57.69962 | 2026-09-04 05:25:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8309f773-fc80-325a-957a-1b7be77de2dc | -14.1248 | -58.88372 | 2026-09-04 05:25:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7bbc6453-bfe0-3f34-bccb-88ee20a9148c | -6.31809 | -56.05068 | 2026-09-04 05:25:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8746cf17-d578-3cb1-a399-8898983643fe | -11.94539 | -55.91619 | 2026-09-04 05:25:00 | NOAA-21 | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 41fdcc99-b300-3660-84e5-c99ff0259277 | -4.09907 | -60.66353 | 2026-09-04 05:25:00 | NOAA-21 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 55a2ce5d-88be-3019-86ef-058c4e4e087f | -8.8765 | -66.66996 | 2026-09-04 05:25:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 18cce945-c7f3-3c71-8619-fd01b369e5e5 | -6.14523 | -57.75993 | 2026-09-04 05:25:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ef23ea43-87de-3c6d-89ce-c935c1e25ba2 | -5.33347 | -60.14066 | 2026-09-04 05:25:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d2e3a273-7da2-3b15-b01a-c7d0106c491b | -10.45196 | -61.20477 | 2026-09-04 05:25:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 46001c9b-fb77-3839-9996-83d37f4aa760 | -9.04091 | -65.73635 | 2026-09-04 05:25:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d8a8d718-c1bf-37da-b50d-36990bf18e37 | -10.64071 | -61.76104 | 2026-09-04 05:25:00 | NOAA-21 | JI-PARANÁ | RONDÔNIA | Brasil | 1100122 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 55f640d4-5c70-3c8d-a04e-4e4ffc563df3 | -9.10945 | -65.49616 | 2026-09-04 05:25:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c2c7fc82-d7a1-3429-be67-04d3cc6eeecf | -5.17095 | -56.18131 | 2026-09-04 05:25:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| f8485e18-0e68-335b-8d26-39e2ac73f8a3 | -4.0017 | -59.73803 | 2026-09-04 05:25:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6fe54d64-5e9c-330d-baa6-40ef876c9aea | -6.0207 | -57.69619 | 2026-09-04 05:25:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 61c049c2-d6a1-3006-ab01-02330a31856d | -6.39077 | -55.22715 | 2026-09-04 05:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4ebdf03f-cdb8-3cb9-9901-b1642cc84399 | -4.46911 | -55.42343 | 2026-09-04 05:25:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a40218b0-f8ef-30f2-8056-6b554b6ec7ca | -17.10051 | -56.84619 | 2026-09-04 05:25:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 98085fb7-e2af-31f7-9424-985e18616ed6 | -3.77401 | -61.75869 | 2026-09-04 05:25:00 | NOAA-21 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f4267dbe-1e4c-380e-8365-ed4363897dfa | -9.03936 | -65.73778 | 2026-09-04 05:25:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d9afea00-660f-3f79-bd84-80aa0074843e | -6.13787 | -57.68824 | 2026-09-04 05:25:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 92a2a2f7-c4a3-342d-8786-3eabba82c16f | -18.14049 | -51.80384 | 2026-09-04 05:25:00 | NOAA-21 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 34c3c1ab-6f53-385b-89d6-8ecfc5ca7821 | -5.83161 | -55.72803 | 2026-09-04 05:25:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d345d041-8d60-3205-9471-eaf812d334e7 | -3.75424 | -61.7519 | 2026-09-04 05:25:00 | NOAA-21 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 68502c97-ebb8-30af-ad2f-923adf6f54a5 | -9.95046 | -60.26363 | 2026-09-04 05:25:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| d32f1470-a789-389c-89b9-e209b76eecca | -5.17545 | -60.28216 | 2026-09-04 05:25:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| d9854e68-8dcf-309c-9355-86e5e92f9cae | -9.04403 | -65.73352 | 2026-09-04 05:25:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ccac481a-dab0-395c-8299-5647e9261cba | -9.034 | -65.73025 | 2026-09-04 05:25:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 58c59b0b-9aab-3f3e-9d06-796aa8f3ad2b | -9.04007 | -65.74125 | 2026-09-04 05:25:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c819d83a-c60d-3cdc-8254-bdbd314e4bd6 | -11.38347 | -58.33422 | 2026-09-04 05:25:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 37b15fe3-aa8c-3447-adf1-06722c3a5a9a | -6.31884 | -56.0457 | 2026-09-04 05:25:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0d693b9b-0a37-38af-adf8-d7ddad9d9aa1 | -9.03787 | -65.73087 | 2026-09-04 05:25:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b1fbd42b-9392-3f59-8d9d-751d3777df52 | -11.51884 | -58.50989 | 2026-09-04 05:25:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| af44af79-4fc4-3c29-9c7a-82a54eb65b5b | -8.59966 | -67.175 | 2026-09-04 05:25:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 12.7 |
| f03f87e9-0f50-3ca3-adf1-ed56cb28e639 | -9.11246 | -65.50153 | 2026-09-04 05:25:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4dbbfb44-75e2-3622-9e2a-25715dd8ed55 | -10.45419 | -61.2123 | 2026-09-04 05:25:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dddec7b2-12ba-38a0-875d-d98a71fc293e | -8.86914 | -68.49283 | 2026-09-04 05:25:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 24099722-0e43-3fe1-a5e6-51c29feebb61 | -17.09538 | -56.86522 | 2026-09-04 05:25:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 43ad5f73-781b-35ff-80ee-e6b85f10654f | -3.21649 | -61.17255 | 2026-09-04 05:25:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 60ddafe1-02ec-3d7d-93cf-3f3508391121 | -8.6061 | -67.18858 | 2026-09-04 05:25:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 13.5 |
| cb153af5-e959-39ca-96d7-ea6c7e20f598 | -9.04394 | -65.74187 | 2026-09-04 05:25:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a7adb5fa-8b8b-308a-9b5c-ff76b8048814 | -3.21647 | -61.15082 | 2026-09-04 05:25:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5bfdd5b9-ee01-372f-a377-9f5996d7f181 | -8.87175 | -66.67307 | 2026-09-04 05:25:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 712bc482-cb1f-3acc-82b4-45a852786268 | -7.87521 | -71.76408 | 2026-09-04 05:25:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6b8059f6-99e0-3e23-b3b6-83716c7a83fc | -4.14828 | -60.69594 | 2026-09-04 05:25:00 | NOAA-21 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| aa567a05-cf0f-3b6f-b1b1-7946e493af8c | -4.10293 | -60.66059 | 2026-09-04 05:25:00 | NOAA-21 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 9b9c6d4f-3812-3b96-96d7-aa025874a7a1 | -5.9756 | -57.68099 | 2026-09-04 05:25:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| afcb32a2-f675-354e-9e24-61b835351596 | -8.87379 | -68.49364 | 2026-09-04 05:25:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 490d6d51-2f05-366d-b143-ade37971b236 | -17.10319 | -56.85964 | 2026-09-04 05:25:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| a9de5f61-7f22-3e7d-8670-b03453533039 | -17.1056 | -56.85354 | 2026-09-04 05:25:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 57929170-de64-3383-b350-8948385bbd5c | -9.5329 | -63.56076 | 2026-09-04 05:25:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 42ae3da3-c72b-3941-a5ae-9b420b316acb | -17.10508 | -56.85784 | 2026-09-04 05:25:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 3057b9b2-9e5b-35bd-a2d8-5a31851faeeb | -10.28504 | -68.83466 | 2026-09-04 05:25:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 82a5ee47-654e-3b72-948a-f7b190194cee | -10.28993 | -68.8608 | 2026-09-04 05:25:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 58110060-644c-33a8-9305-561caa2a8b1e | -3.43432 | -60.41054 | 2026-09-04 05:25:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b72270e9-bcd4-3e9d-9f73-9f6aea91fd23 | -7.88563 | -71.73972 | 2026-09-04 05:25:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ed536b34-53ca-3c37-afc4-c6b6dee50ec8 | -17.09618 | -56.84558 | 2026-09-04 05:25:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 79f5f1d4-c617-3fd3-8d8e-924161213ae3 | -17.09777 | -56.86761 | 2026-09-04 05:25:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.2 |
| 9791f288-1396-3f38-abb2-a15c16aec4cd | -8.6359 | -67.01653 | 2026-09-04 05:25:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e6c83e79-270d-356b-a9a5-a77885dbc5d9 | -10.20029 | -69.08826 | 2026-09-04 05:25:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 32847080-7566-3a6b-af9f-0c728931127d | -15.47577 | -60.06097 | 2026-09-04 05:25:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 44457141-a5ca-3aea-a782-fcfb0b4f7e78 | -17.10126 | -56.85294 | 2026-09-04 05:25:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 8ca40fd8-91ae-3974-8715-5fd2fabb9775 | -5.59106 | -61.47357 | 2026-09-04 05:25:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4d0edaab-dbf7-3507-8154-fbd232be905e | -4.46861 | -55.42685 | 2026-09-04 05:25:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 33819cd6-5aaf-3a8c-b31d-22627359c6a9 | -4.48134 | -55.08172 | 2026-09-04 05:25:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 758440d6-fae4-34a1-8b0e-0fbcee68e240 | -17.09971 | -56.86581 | 2026-09-04 05:25:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| d0759fcc-7652-36ab-ab01-56a614258f01 | -5.08106 | -56.28779 | 2026-09-04 05:25:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| ddb9985a-f3d0-3b33-b9ab-355f2259f1b0 | -17.09453 | -56.85845 | 2026-09-04 05:25:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| c208061e-5bab-3c20-b70d-ed56767a4196 | -17.09693 | -56.85233 | 2026-09-04 05:25:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| b0f46f8b-7b72-33dc-a9f7-80e299860f19 | -3.21536 | -61.15789 | 2026-09-04 05:25:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4a35eeb1-139f-33a9-b11b-25c2583ed980 | -9.10865 | -65.50091 | 2026-09-04 05:25:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| af33fddf-e8c1-379d-ab10-30abdc627bc5 | -10.39241 | -61.23783 | 2026-09-04 05:25:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 97149874-dd6e-3b93-ba16-740315867ef6 | -14.65458 | -54.8841 | 2026-09-04 05:25:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a8fd37fd-2106-324b-b402-d790512e0f56 | -12.16056 | -60.76317 | 2026-09-04 05:25:00 | NOAA-21 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9054f381-1121-335f-a40b-b23eee6e47b5 | -8.64285 | -67.0015 | 2026-09-04 05:25:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a6d58b8a-b032-3c24-b033-c4069dc76d6c | -4.47905 | -55.41117 | 2026-09-04 05:25:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8ce89410-2888-3670-a0af-b3caf98e93c0 | -9.02122 | -65.44405 | 2026-09-04 05:25:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 59d9e2fb-63d0-3b5f-9d2b-82221a0f7ef1 | -3.2037 | -61.23226 | 2026-09-04 05:25:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 5928fecf-facc-3729-af68-c0f31642585d | -3.21312 | -61.1503 | 2026-09-04 05:25:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 275309f4-3345-3c01-af54-280e3befc8cc | -6.31468 | -56.0474 | 2026-09-04 05:25:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c41ee1c5-6076-3a4f-b73f-6c5c778283ae | -9.17797 | -68.26471 | 2026-09-04 05:25:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 54b6c3b2-c8e5-3237-9f60-558124fd40c8 | -9.04865 | -65.73764 | 2026-09-04 05:25:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7d90c159-4c87-3806-987b-2e08d3ff8bf8 | -5.56243 | -60.17675 | 2026-09-04 05:25:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a34e7664-dd4c-3d4c-8505-724e45949d27 | -17.10612 | -56.84925 | 2026-09-04 05:25:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 85c508f9-314a-3309-89bf-f82da4e4ab75 | -8.8062 | -69.02533 | 2026-09-04 05:25:00 | NOAA-21 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b8c2c946-9ef8-364e-a458-f163c0382c34 | -10.45805 | -61.20931 | 2026-09-04 05:25:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README29.md)
