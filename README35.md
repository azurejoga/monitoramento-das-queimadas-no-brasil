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

## Dados Diários - Página 35

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fe129326-d733-3ef4-ae1f-b2f91ab18a7a | -9.48958 | -68.4959 | 2026-09-11 05:50:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9bb65196-c00f-3b16-bba3-818cb0162e6c | -13.24846 | -61.60192 | 2026-09-11 05:50:00 | NOAA-20 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 7668bea2-09a1-3348-95de-afcd94fbd242 | -13.21627 | -61.8367 | 2026-09-11 05:50:00 | NOAA-20 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a16ab53c-6025-3285-8c59-319f6f3ada66 | -9.04052 | -65.40908 | 2026-09-11 05:50:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| a8f18fec-1175-393b-bcba-dfc221fa5822 | -9.0228 | -65.41349 | 2026-09-11 05:50:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3b0b4e7d-626e-36dc-8b0b-7ffefda7f19f | -9.22892 | -65.57156 | 2026-09-11 05:50:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| eb1a3814-86b0-3123-96e6-2a5e30df6ebf | -8.53135 | -66.99001 | 2026-09-11 05:50:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 28aa0e20-c772-366c-b536-029ab0f096f0 | -8.93543 | -66.84586 | 2026-09-11 05:50:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c0d9fa84-4fac-3e97-a2f6-013c87498c42 | -9.23224 | -65.57208 | 2026-09-11 05:50:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9d91be96-c669-3d24-80f5-9fd17c54a18e | -11.41359 | -62.12593 | 2026-09-11 05:50:00 | NOAA-20 | NOVA BRASILÂNDIA D'OESTE | RONDÔNIA | Brasil | 1100148 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 60198492-364c-36d8-98de-e1ff096d68fd | -8.6362 | -66.50573 | 2026-09-11 05:50:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ec348f55-f432-3cc9-990e-295a0e0ae533 | -9.30092 | -65.89138 | 2026-09-11 05:50:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1646f051-e040-3133-94c8-246848520b6e | -9.02002 | -65.40945 | 2026-09-11 05:50:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0fb35cc9-0120-3349-aa27-dbf9068c43fb | -9.18452 | -68.21555 | 2026-09-11 05:50:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 11.7 |
| b5aee151-bf2c-33ea-81f0-e7a34afc54e1 | -12.15642 | -64.13274 | 2026-09-11 05:50:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5ef790ab-4397-3cbd-8890-9a267fb7f86c | -13.35064 | -61.67408 | 2026-09-11 05:50:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| a05aedea-45ad-3495-abe2-30830f895c7c | -9.01282 | -65.41191 | 2026-09-11 05:50:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1e586b1e-f2ce-3b8d-800a-37ac0cd7237c | -9.43197 | -67.11828 | 2026-09-11 05:50:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 478756d2-1af7-33a0-be05-422c3394cd56 | -20.49771 | -57.4711 | 2026-09-11 05:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.6 |
| e9ed8ff8-db20-3bc0-8d86-a24bcf27fc11 | -20.49484 | -57.46815 | 2026-09-11 05:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 2e94dccf-9388-38ac-8ed0-140a2c08950e | -22.26775 | -55.8362 | 2026-09-11 05:53:00 | NOAA-20 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 66fd7282-f778-3f60-9ed6-f44136c00810 | -20.50081 | -57.46878 | 2026-09-11 05:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 60dceb25-b044-3257-8d82-ae00d65fc92e | -22.26014 | -55.84788 | 2026-09-11 05:53:00 | NOAA-20 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 87f23efc-f1fe-3ffc-9f25-adb03e25041c | -20.48579 | -57.46985 | 2026-09-11 05:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 282e38d0-778b-3d02-b72b-7447313726cf | -20.48623 | -57.46528 | 2026-09-11 05:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 4e8fe346-f658-3255-a9d1-36f5bfa303e7 | -22.26061 | -55.84167 | 2026-09-11 05:53:00 | NOAA-20 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| be23f0da-5786-331f-8267-49e69514b106 | -22.26727 | -55.84249 | 2026-09-11 05:53:00 | NOAA-20 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 91983536-61b9-334e-8713-3cdf53dccc76 | -20.49219 | -57.46591 | 2026-09-11 05:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 51e9c9c0-a48d-3bfe-92cd-c71b620a3283 | -20.49816 | -57.46652 | 2026-09-11 05:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.9 |
| 481588ad-ab41-3fca-946b-4cd3b8d4b324 | -13.249 | -61.5983 | 2026-09-11 06:00:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 60.6 |
| fee90d8e-b246-3696-821c-c8680c68a7de | -13.249 | -61.5983 | 2026-09-11 06:10:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 63.6 |
| 48db8b54-854c-3c7e-8407-38970bfe3e57 | -7.14261 | -73.11356 | 2026-09-11 06:33:00 | NOAA-21 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e6669e83-adad-3220-ad42-cc9d75f6c3ec | -9.23329 | -65.57134 | 2026-09-11 06:33:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| bfd44887-b96c-3120-8c4f-34e33d384772 | -9.14578 | -67.81329 | 2026-09-11 06:33:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 00f00108-9bf6-317e-b79a-d1680b44a312 | -8.35144 | -71.02547 | 2026-09-11 06:33:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 39d13e2f-928e-3465-bb48-f124ba569895 | -7.86594 | -73.40439 | 2026-09-11 06:33:00 | NOAA-21 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 63092127-2cf5-342a-b994-0bb3f42daf7b | -7.79355 | -72.50002 | 2026-09-11 06:33:00 | NOAA-21 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ddcb14b8-4c84-3d2a-ac52-c748af6844af | -9.49057 | -68.49603 | 2026-09-11 06:33:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1de86fb2-0339-37bd-9a2a-166e58d34ace | -9.41113 | -65.8605 | 2026-09-11 06:33:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 379756aa-c8a7-3cc3-9c9b-3742d81dd99d | -9.03417 | -65.41956 | 2026-09-11 06:33:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| e7de7afc-12cf-39ae-951b-6fc660beffe1 | -9.04241 | -65.40807 | 2026-09-11 06:33:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 0124fae8-84af-3e39-9052-8cd75e003a5d | -8.63444 | -66.50963 | 2026-09-11 06:33:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 2834b1e0-f0b1-361d-9fd7-e1d0c07db656 | -9.17729 | -68.21544 | 2026-09-11 06:33:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b02cb45f-827a-319a-85de-fb29ec2a5f0d | -9.42219 | -65.86358 | 2026-09-11 06:33:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 487b63da-d257-3d90-a220-253f933b9b27 | -8.63511 | -66.5042 | 2026-09-11 06:33:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| e544580b-b202-3bf7-9277-5e2f717e01b5 | -9.4179 | -65.86148 | 2026-09-11 06:33:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 05cc9ae3-92cc-374d-9971-ab296d955466 | -8.88447 | -70.8455 | 2026-09-11 06:33:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bf8a9b74-ca07-3fe7-a452-9504908dc4ad | -9.13979 | -67.81244 | 2026-09-11 06:33:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c401dcad-e1f2-3b1a-9d23-b969bd6df4b8 | -9.14036 | -67.80797 | 2026-09-11 06:33:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4119f989-210e-3655-a4ef-0c7e03ff2051 | -9.10631 | -67.68861 | 2026-09-11 06:33:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 377ec61b-d618-3261-a657-e55c78423e6c | -9.04189 | -65.41398 | 2026-09-11 06:33:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 33abc97f-bc0f-33cd-a893-e15588aef83b | -9.01419 | -65.41031 | 2026-09-11 06:33:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a8ec1d08-6a8c-3db5-b882-860a7734c1e5 | -8.6409 | -66.51053 | 2026-09-11 06:33:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 1f1a0fe4-66f5-32c9-b721-93e4bddb6aa4 | -9.43674 | -68.26523 | 2026-09-11 06:33:00 | NOAA-21 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a5f1d88a-eebd-39af-9352-86e2daacdae1 | -9.41541 | -65.86273 | 2026-09-11 06:33:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| f60e99ba-7a3d-3fe5-92ff-f90d63ad7743 | -8.88033 | -70.83938 | 2026-09-11 06:33:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 64d98713-f881-3162-90d7-2d73d0047904 | -9.14692 | -67.80434 | 2026-09-11 06:33:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 43674510-e189-3482-a9a4-217959438bce | -9.17137 | -71.84763 | 2026-09-11 06:33:00 | NOAA-21 | JORDÃO | ACRE | Brasil | 1200328 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d56b29d6-e4fa-3bb5-b7d2-4fe53072ab0e | -9.46396 | -68.83715 | 2026-09-11 06:33:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d612345c-8d97-3d18-9a2e-fc2cbde6a0d6 | -9.39691 | -65.86443 | 2026-09-11 06:33:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6965797e-b75c-3d07-bf95-388245651510 | -9.23252 | -65.57763 | 2026-09-11 06:33:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 3f4492c6-2d12-3a98-a11e-03b1d7f340b0 | -8.63957 | -66.52123 | 2026-09-11 06:33:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 62174b9f-6465-3e10-9fc0-1dad73ae6055 | -9.19002 | -68.20879 | 2026-09-11 06:33:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 22f85433-8a50-3685-a628-c6f94edc09b1 | -9.18418 | -68.20795 | 2026-09-11 06:33:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| c4cbce56-5201-3ddb-8cdf-f419d94a9538 | -9.04269 | -65.40744 | 2026-09-11 06:33:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 7c2e3e50-9649-3c53-8bc4-0768e8f31173 | -9.49005 | -68.50007 | 2026-09-11 06:33:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4ea61209-328d-3e42-94ec-d0ade315bb41 | -7.75479 | -66.9138 | 2026-09-11 06:33:00 | NOAA-21 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 71ea1dba-9409-326d-88c7-9a0f7c4156a2 | -9.04165 | -65.41462 | 2026-09-11 06:33:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| f6ed0c45-64a9-315d-b1a1-7cf69cbe8027 | -8.65299 | -69.79343 | 2026-09-11 06:33:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 896fc61f-eeb5-3fbf-b247-2b7d8c8052e9 | -8.99188 | -65.42034 | 2026-09-11 06:33:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 480a996f-209a-3d4f-96c8-4f1373e50e0c | -9.23349 | -65.57529 | 2026-09-11 06:33:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 73cee2a0-0f9a-3f7d-bf17-f822f18dd371 | -9.18312 | -68.2164 | 2026-09-11 06:33:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 555cfd7b-e1f0-3bfa-91b9-7b69a590de2c | -8.65863 | -69.79099 | 2026-09-11 06:33:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a743b813-b50a-379b-a608-ac18510e8c54 | -9.42468 | -65.86234 | 2026-09-11 06:33:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2a7337d0-98bb-3a18-a728-66ed6d1d4e43 | -9.03472 | -65.4137 | 2026-09-11 06:33:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 4b416f26-5fcd-3234-8008-038cd3fdf520 | -9.75852 | -64.94781 | 2026-09-11 06:33:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fa754001-94bd-30f0-b578-c9fea1f0f777 | -9.21896 | -65.58018 | 2026-09-11 06:33:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1c39aed5-da47-3025-92dc-d061bb8f84c5 | -9.02112 | -65.41124 | 2026-09-11 06:33:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 019a4573-21bc-3965-acb0-32431d5be565 | -9.18948 | -68.21307 | 2026-09-11 06:33:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 78b1eafc-da32-3924-a135-384b8a617a48 | -8.86882 | -72.70374 | 2026-09-11 06:33:00 | NOAA-21 | MARECHAL THAUMATURGO | ACRE | Brasil | 1200351 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f509ec91-8923-3735-a05b-ea3d4be0b251 | -9.22515 | -65.58706 | 2026-09-11 06:33:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 5249bb2f-3d12-3cb0-b215-cf0cdc623b7d | -9.10575 | -67.69315 | 2026-09-11 06:33:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 18e5e313-b34f-31d2-8cae-13ab81961673 | -9.03576 | -65.40656 | 2026-09-11 06:33:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 97f83612-9fa6-3b53-80b2-85c53bdcce98 | -8.63378 | -66.515 | 2026-09-11 06:33:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| f55beae1-2268-339f-a0ec-23986a34dfe0 | -9.39763 | -65.85825 | 2026-09-11 06:33:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a85969aa-ffbc-3325-a5bd-8dff62f562bd | -9.18472 | -68.20371 | 2026-09-11 06:33:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 71d9e90e-4493-3a4a-9599-1ac440ac1185 | -7.14208 | -73.11718 | 2026-09-11 06:33:00 | NOAA-21 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 091977ae-4d2f-323d-b55e-58c8204603cd | -8.76931 | -70.82845 | 2026-09-11 06:33:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e06e359c-4602-311d-8208-fd3a0c5a9888 | -9.04089 | -65.42115 | 2026-09-11 06:33:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| b8025203-39d3-335c-8ded-def86ae5b7cd | -9.17782 | -68.21126 | 2026-09-11 06:33:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b70670ea-a402-3d34-858d-126283817311 | -9.03397 | -65.42019 | 2026-09-11 06:33:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 9d0418d3-4a7d-3291-ba18-47858838b91d | -9.48479 | -68.49535 | 2026-09-11 06:33:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c984252c-bcb7-3c7b-a317-07bf470c4b8c | -9.43725 | -68.26103 | 2026-09-11 06:33:00 | NOAA-21 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b921d91a-5a37-3534-89a9-02d8893cdd0d | -8.99266 | -65.41386 | 2026-09-11 06:33:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5328e411-5dba-3017-aad3-eb827036b6c7 | -9.21873 | -65.5761 | 2026-09-11 06:33:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3c500f53-86c4-345c-aff8-9427f1d9b4eb | -7.13801 | -73.11658 | 2026-09-11 06:33:00 | NOAA-21 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e40f5b95-23f1-3d72-ad5c-c929f9e664ca | -9.17834 | -68.20714 | 2026-09-11 06:33:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 820e1afc-621c-33d7-b78b-7d64d45e64c7 | -8.72109 | -71.54617 | 2026-09-11 06:33:00 | NOAA-21 | JORDÃO | ACRE | Brasil | 1200328 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ee0bbfde-6bc7-3d32-8a76-15fca55ccd36 | -9.19057 | -68.20453 | 2026-09-11 06:33:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 583f8f1d-a41e-30b9-a4e6-7a38d645edf5 | -9.03548 | -65.40717 | 2026-09-11 06:33:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |


[Clique aqui para ver as próximas entradas](README36.md)
