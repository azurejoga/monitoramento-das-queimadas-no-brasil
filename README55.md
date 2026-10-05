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

## Dados Diários - Página 55

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 30012df1-6248-3a2f-9efc-1dfa9dc7b676 | -2.98585 | -54.10088 | 2026-10-05 05:42:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 52b4fe20-c9a1-3582-9dcc-29c15dfc1a3c | -3.31019 | -53.84591 | 2026-10-05 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b33729a9-5720-32c2-98a2-bed64be54bde | -3.09967 | -53.74186 | 2026-10-05 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| f651420f-af9d-30b0-ad56-ae61a9ca8b7f | -2.89956 | -54.12377 | 2026-10-05 05:42:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 69e31657-abcc-383e-bc18-6135be2d8dc1 | -2.80778 | -54.10334 | 2026-10-05 05:42:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d1c55ffa-31bd-3bcb-9a7d-2c63aacae759 | -3.86406 | -55.83596 | 2026-10-05 05:42:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| be65ea8c-fead-332e-84bb-28466aa201d1 | -2.89369 | -54.12284 | 2026-10-05 05:42:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c5405d12-e227-3b37-b131-80ea63f72f18 | -3.31086 | -53.84143 | 2026-10-05 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d18a9c44-c751-352c-adde-0e9b195694d9 | -2.82014 | -54.10099 | 2026-10-05 05:42:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fd6dfe4a-72b4-3d29-91d7-f74d0d75822d | -2.90605 | -54.12049 | 2026-10-05 05:42:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a0516cb9-fe66-327c-9406-4a30a1dd95fb | -6.20836 | -52.83444 | 2026-10-05 05:42:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| c4d4e360-4b86-36ce-a037-11f2e6027ccc | -3.09632 | -53.72285 | 2026-10-05 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 5be5e564-377d-3c51-a537-4ceec72c5b35 | -3.37874 | -54.10176 | 2026-10-05 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ecca931b-4419-305f-a578-7983b4e8999a | -8.88128 | -66.64672 | 2026-10-05 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| edb4c854-1f20-3673-9541-a1c55e91eafb | -7.4166 | -64.66836 | 2026-10-05 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| de8fbe24-6ba9-3864-bf9a-d21a5fae055d | -8.69948 | -69.28245 | 2026-10-05 05:44:00 | NOAA-21 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 34c1242c-d88c-3da6-94b3-669668728939 | -8.52807 | -54.59306 | 2026-10-05 05:44:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b28a3d3c-408c-3a60-9050-6a268621d27b | -9.43837 | -67.42412 | 2026-10-05 05:44:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e099b1e4-afea-3cf1-bb78-af4ef0510e01 | -9.48059 | -66.79353 | 2026-10-05 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d1e3fc99-3f95-325a-b62d-e83765088908 | -10.63986 | -69.30005 | 2026-10-05 05:44:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| dfd7fb8b-8108-310a-9e40-2fe5d1ad9980 | -9.11423 | -67.70882 | 2026-10-05 05:44:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 605d7ba7-b7ee-3a6a-bbae-459131be27c0 | -8.35443 | -62.83888 | 2026-10-05 05:44:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 456b45a1-2805-38d3-9c00-09861899db80 | -12.87926 | -61.71751 | 2026-10-05 05:44:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 733c4325-4699-313a-9de2-b4a6b986eecf | -9.16802 | -68.27013 | 2026-10-05 05:44:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5cbc67fe-222f-317e-aace-5e9c88faaaaa | -9.25728 | -67.6466 | 2026-10-05 05:44:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f470a188-a0d0-3c1e-8154-467e090ab979 | -10.63836 | -69.28732 | 2026-10-05 05:44:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 22a0afb7-9c55-32ed-8527-5e6ba2b49b3f | -10.27575 | -68.33248 | 2026-10-05 05:44:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 97a19e79-850d-309f-a0c1-08753877f947 | -8.62212 | -69.49918 | 2026-10-05 05:44:00 | NOAA-21 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4868a9aa-d40f-3c80-80b0-01c8302bb8e5 | -8.59233 | -66.81543 | 2026-10-05 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| aa183208-cf91-3d9d-8642-a277f6252574 | -9.32325 | -65.81988 | 2026-10-05 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 37d73ea6-19cd-3645-9fa1-95ea9d73fd46 | -8.65703 | -54.55802 | 2026-10-05 05:44:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5f7d71e0-d291-3139-b605-7a37e92d250c | -12.87422 | -61.72425 | 2026-10-05 05:44:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c9f43fa6-adbd-3f47-9207-a83ed48b4f3e | -8.7789 | -62.87994 | 2026-10-05 05:44:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5d8164ed-308c-383e-8896-db12c657f729 | -10.3581 | -68.06045 | 2026-10-05 05:44:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b3c2758c-7d5f-3706-9fb5-efa3db805533 | -9.12921 | -65.91053 | 2026-10-05 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 14ec1e38-b0f2-35db-8c13-7192e42e9239 | -9.11308 | -65.46509 | 2026-10-05 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 921da60d-0803-32e7-aff5-4c07bae48e63 | -9.12416 | -68.21687 | 2026-10-05 05:44:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 84913abe-af0d-3de6-8aef-905f88e0d576 | -10.057 | -67.55738 | 2026-10-05 05:44:00 | NOAA-21 | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 74047f76-8e87-35ef-852c-91051ee361fd | -7.45221 | -63.56574 | 2026-10-05 05:44:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0c428f5d-778f-3d65-ab56-58a5048d11a4 | -9.12255 | -67.83824 | 2026-10-05 05:44:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 207b3cd0-5c11-3930-8931-7580a21f6d16 | -8.74603 | -72.82545 | 2026-10-05 05:44:00 | NOAA-21 | MARECHAL THAUMATURGO | ACRE | Brasil | 1200351 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b51eddd4-443d-3bb5-9be9-c85d24b73363 | -8.45016 | -62.72771 | 2026-10-05 05:44:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ea615f20-79a7-326c-8152-fb52ed5d352f | -9.16707 | -68.25441 | 2026-10-05 05:44:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a41e07ec-bfd6-3415-9575-04999b15eb0f | -8.62507 | -69.5041 | 2026-10-05 05:44:00 | NOAA-21 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bac943bc-0de0-32f9-8af2-f97190a78e50 | -8.67012 | -70.04038 | 2026-10-05 05:44:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| caa1d74b-78c8-3760-9258-38dca26660e2 | -7.45336 | -63.55816 | 2026-10-05 05:44:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0170e257-dd4e-3c32-a03d-1531a57e8bf9 | -8.35146 | -62.83419 | 2026-10-05 05:44:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 64733b7c-569f-3928-93d4-42e5ced2754a | -7.44187 | -63.56416 | 2026-10-05 05:44:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c2b8cbd7-579c-3335-90b3-9ee17aedb1bd | -8.34973 | -62.8212 | 2026-10-05 05:44:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0e95b022-6335-310a-bd75-6cceb341ec31 | -9.09611 | -64.37935 | 2026-10-05 05:44:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 3ca3413f-2954-3dd0-ad78-8ca4ed3f924e | -10.83125 | -61.40997 | 2026-10-05 05:44:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 87659917-f295-3a76-9a65-1ee7a843c0e6 | -10.41705 | -68.95355 | 2026-10-05 05:44:00 | NOAA-21 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 812c3a47-d2e4-3f19-9010-91973c04eaa9 | -9.13301 | -68.24937 | 2026-10-05 05:44:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e7aeebc5-bdc7-32db-b5fb-01ddb85ce6c1 | -7.44302 | -63.55658 | 2026-10-05 05:44:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| e5d09a7d-387e-3b7f-8c95-1aa722b9e1c3 | -8.34192 | -62.82428 | 2026-10-05 05:44:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 72ec42f9-c971-3087-a009-2a98238c650d | -9.14979 | -68.23266 | 2026-10-05 05:44:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1afe3e82-a499-3dfd-98ed-6a471c89fcc1 | -9.15524 | -68.26463 | 2026-10-05 05:44:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ee0489b6-e8e8-3c6b-babe-28792f07f465 | -9.05414 | -65.42728 | 2026-10-05 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4c014092-0517-3e4e-b45d-43241aca0d83 | -10.90128 | -57.08595 | 2026-10-05 05:44:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 19.5 |
| 4a7b47dc-e9ef-3113-8cbf-551c38f00040 | -9.03348 | -67.55436 | 2026-10-05 05:44:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8b62f9b2-acfd-3aa8-a19b-556d11159f0b | -10.95396 | -60.91131 | 2026-10-05 05:44:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 27037589-68d7-3df6-b2b3-4f08eec3c1d1 | -7.44819 | -63.56901 | 2026-10-05 05:44:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8eb9cd72-52ca-3c19-852a-16f8c729cc33 | -10.64302 | -68.60172 | 2026-10-05 05:44:00 | NOAA-21 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 60c8cfff-0b56-348f-928d-4551e972cc36 | -8.67741 | -54.54595 | 2026-10-05 05:44:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e68e5fad-d563-3048-96de-066f0aa6187f | -10.4808 | -68.60632 | 2026-10-05 05:44:00 | NOAA-21 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 207ac1b8-41a9-3d1b-a418-5896767326d5 | -9.11646 | -64.35983 | 2026-10-05 05:44:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 88c32347-afcd-3431-b0ec-13d1bbbf165e | -13.50493 | -61.12225 | 2026-10-05 05:44:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1fc0055f-c77e-3e53-ad79-72a70d0f561e | -12.87975 | -61.71383 | 2026-10-05 05:44:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 88cc0d75-aa1c-38fe-8879-2fb591383f36 | -8.58902 | -66.8149 | 2026-10-05 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6fb7b979-b140-3383-9e22-de5bb4f33e57 | -10.24189 | -68.30387 | 2026-10-05 05:44:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6516aae1-afdc-33ed-9488-280f96cd395a | -10.86046 | -68.69103 | 2026-10-05 05:44:00 | NOAA-21 | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e6d5623f-7ee3-3864-bd59-5404f87d7057 | -9.15585 | -68.26083 | 2026-10-05 05:44:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 130320e5-bca5-3210-9954-7bca91d1065f | -9.16301 | -68.25764 | 2026-10-05 05:44:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 51c5b74f-87e3-337b-b3e9-db08eeed414e | -8.64805 | -62.52745 | 2026-10-05 05:44:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 154061e9-e535-34b0-9a21-bece02797d97 | -9.09951 | -64.37986 | 2026-10-05 05:44:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 5174de74-857d-3111-b3eb-d25a4b9225b3 | -8.60008 | -66.80947 | 2026-10-05 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 54fea38b-6211-369b-8107-3cc148830c7b | -12.87829 | -61.72486 | 2026-10-05 05:44:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d7699e9b-a62e-3946-a72e-d26de93e26dc | -9.03011 | -67.55383 | 2026-10-05 05:44:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| df68160d-f429-3b58-8989-fd3cc031b214 | -9.12194 | -68.20876 | 2026-10-05 05:44:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ca5dacb6-90af-3ae9-9476-b714f8d8634d | -8.74237 | -69.45419 | 2026-10-05 05:44:00 | NOAA-21 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 06703f8b-fc09-38be-bde9-16805cc03ea9 | -9.88381 | -65.13718 | 2026-10-05 05:44:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a1a00f99-f151-34bf-87b9-6ede39a901af | -9.22974 | -67.8704 | 2026-10-05 05:44:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 214ea3c9-75c6-317b-b12f-d3e923c02245 | -10.8963 | -57.08176 | 2026-10-05 05:44:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c14094ea-8f8e-3536-9f32-23ee6d4c3e91 | -10.34362 | -67.95662 | 2026-10-05 05:44:00 | NOAA-21 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 600a0d64-0555-398f-b5e9-f27e7ee5b1e1 | -8.34229 | -62.87091 | 2026-10-05 05:44:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| afc04ee5-f7c4-3684-86bb-1992f8e6f40f | -8.65832 | -54.55331 | 2026-10-05 05:44:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b21edd71-d73b-3b53-9539-787bbb26f870 | -9.16458 | -68.26957 | 2026-10-05 05:44:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5645d2b7-3021-3c30-81f7-63baf3e07efe | -9.34005 | -64.71522 | 2026-10-05 05:44:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ae173262-6490-3e2a-bfba-0a4569ebe2f3 | -10.61872 | -67.92304 | 2026-10-05 05:44:00 | NOAA-21 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 592258f4-a373-35ab-87f4-ae60dac3ba27 | -8.59289 | -66.81192 | 2026-10-05 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 62f6905c-2d57-32c2-8f9e-c00939545568 | -8.58846 | -66.81841 | 2026-10-05 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ac6486b6-2aae-30dc-a6b6-af200cb05ea8 | -8.56271 | -67.06739 | 2026-10-05 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 908a822c-1108-3f58-ab93-8441da3976f3 | -9.46496 | -64.33215 | 2026-10-05 05:44:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bb6094ed-3d28-3a95-ae1f-ccd427ff714e | -8.33871 | -62.87037 | 2026-10-05 05:44:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 081bca8c-2a74-383e-b534-a5a213e68e77 | -8.87093 | -67.45823 | 2026-10-05 05:44:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3e9c6ff5-962e-3e26-ae14-5002242b6ee2 | -9.50409 | -68.49601 | 2026-10-05 05:44:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e0eb7245-0538-32d9-a776-f30c8a0e5604 | -10.87817 | -61.4053 | 2026-10-05 05:44:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 17f1d74e-98dc-3e89-879c-285872bf6e3a | -9.8926 | -67.33 | 2026-10-05 05:44:00 | NOAA-21 | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 437f0fe1-d8d4-348f-b209-3569456cb667 | -9.67202 | -66.83175 | 2026-10-05 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cdbb5b41-b63c-3b76-86dc-3de866f4e03b | -8.65769 | -54.55812 | 2026-10-05 05:44:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README56.md)
