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

## Dados Diários - Página 26

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a0e41dea-d11c-351d-b541-27d4fef83428 | -13.23237 | -61.77459 | 2026-09-07 05:06:00 | NPP-375D | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e76794b1-4245-3178-b767-4bdad348a638 | -13.23708 | -61.77554 | 2026-09-07 05:06:00 | NPP-375D | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 10c90bd7-5379-3039-8626-60dd5329451c | -13.22197 | -61.77782 | 2026-09-07 05:06:00 | NPP-375D | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9fd62716-4284-3f8c-a5ef-b906a1a14c0c | -12.75287 | -52.84084 | 2026-09-07 05:06:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6f8360b5-1b7f-3e06-9df6-5a20d85ca9d5 | -13.21444 | -61.73765 | 2026-09-07 05:06:00 | NPP-375D | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 66ff41fe-fecf-3447-95ff-dfe93ef92e34 | -13.27485 | -61.75658 | 2026-09-07 05:06:00 | NPP-375D | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c0063dc3-80db-3a79-bbad-cf9beb0f9633 | -13.21066 | -61.78465 | 2026-09-07 05:06:00 | NPP-375D | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c6651f00-1930-333c-be01-d323a41aeabf | -12.75625 | -52.84138 | 2026-09-07 05:06:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ea9ac5fa-239d-3630-8842-7d03c9b1e707 | -13.2194 | -61.74022 | 2026-09-07 05:06:00 | NPP-375D | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 950618cc-bb3e-3169-bec8-4a4a47dd924d | -12.76525 | -52.85028 | 2026-09-07 05:06:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e1e377ed-8f5f-39aa-98ff-84542042655b | -12.76018 | -52.86071 | 2026-09-07 05:06:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 521d92ba-69dd-3fa3-b9ca-52f4c0ed7586 | -13.2182 | -61.7437 | 2026-09-07 05:06:00 | NPP-375D | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 656959c4-8438-3bb3-8fab-3289b680fbe9 | -12.76582 | -52.84663 | 2026-09-07 05:06:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7ec62a07-d560-3914-b5e8-4b578cadf4cf | -13.22099 | -61.78294 | 2026-09-07 05:06:00 | NPP-375D | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a40836a5-2758-3241-a7a7-1836fe259cd7 | -13.2135 | -61.74274 | 2026-09-07 05:06:00 | NPP-375D | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 484f1310-a26d-3c78-a67d-885559ca1b58 | -12.763 | -52.84245 | 2026-09-07 05:06:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f167e071-b4a0-3258-a7fe-2dccc4fbcbf6 | -12.76638 | -52.84298 | 2026-09-07 05:06:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 593942a9-d3f9-31e3-a245-bcd9be1189f5 | -13.25411 | -61.76302 | 2026-09-07 05:06:00 | NPP-375D | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 18edcfec-690e-3751-8d27-3af74bf6d0e5 | -14.52544 | -59.80722 | 2026-09-07 05:06:00 | NPP-375D | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 73218dc2-03f2-377e-9870-c0b24b6afcde | -12.76469 | -52.85394 | 2026-09-07 05:06:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f6e42646-0537-3216-868b-38ac18f6da59 | -3.1461 | -60.6696 | 2026-09-07 05:10:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 56.4 |
| a7a1c811-07b2-3c86-93b9-f8160a5757cc | -28.67479 | -49.05116 | 2026-09-07 05:10:00 | NPP-375D | JAGUARUNA | SANTA CATARINA | Brasil | 4208807 | 42 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| dbeb2938-991a-367e-8687-537bbf9d87b6 | -28.18099 | -49.86234 | 2026-09-07 05:10:00 | NPP-375D | SÃO JOAQUIM | SANTA CATARINA | Brasil | 4216503 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 045aff41-1fb5-336a-b033-f6c7e77d3991 | -28.18124 | -49.86404 | 2026-09-07 05:10:00 | NPP-375D | SÃO JOAQUIM | SANTA CATARINA | Brasil | 4216503 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 33d644da-c87a-3f5e-86ac-9b5153ff2024 | -28.67376 | -49.052 | 2026-09-07 05:10:00 | NPP-375D | JAGUARUNA | SANTA CATARINA | Brasil | 4208807 | 42 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| a3147c38-6267-3257-b2b8-9eab96664bdd | -13.3 | -45.24 | 2026-09-07 05:15:00 | MSG-03 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 983ecdfc-9ef6-3e8d-8433-703bfd357132 | -13.2669 | -61.7135 | 2026-09-07 05:20:00 | GOES-19 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 76.6 |
| 5bf35619-3ce6-3da0-9d66-b76df80fc421 | -13.2289 | -61.7161 | 2026-09-07 05:20:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 156.1 |
| 2dd283de-f806-3aab-8179-cb1aea4d8595 | -13.2479 | -61.7148 | 2026-09-07 05:20:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 136.6 |
| 15853b8e-fb06-3fed-ba60-07b067d1360a | -13.2097 | -61.7367 | 2026-09-07 05:20:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 64.1 |
| 03afadd5-e365-3afe-83a2-17b9840162fc | -3.1462 | -60.6506 | 2026-09-07 05:20:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 63.2 |
| 75aa4bad-74a2-300e-b4fa-640a1e7fc4a3 | -13.2287 | -61.7355 | 2026-09-07 05:20:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 139.9 |
| bc8bbee6-cc0f-3fc8-bb4b-90a1afe9781d | -13.2477 | -61.7342 | 2026-09-07 05:20:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 83.8 |
| 0a4d3933-5170-3ec6-8cec-3c9883be0953 | 1.66837 | -56.06906 | 2026-09-07 05:21:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 13cceeb3-7d24-36d1-bcc9-40c51a922221 | 0.21394 | -51.28897 | 2026-09-07 05:21:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a3e0dfc1-37c9-3bc6-92f8-eba7924ade03 | 0.22141 | -51.27904 | 2026-09-07 05:21:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 3a64fb0c-161d-3725-8422-204b3d901b17 | 0.21256 | -51.28038 | 2026-09-07 05:21:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 6926e728-3641-3fe8-baab-5498526918a7 | 2.36251 | -50.77879 | 2026-09-07 05:21:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 42da69e6-7a6f-3868-b812-24066cde53ad | 0.21325 | -51.28468 | 2026-09-07 05:21:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 76a286f5-e644-3fbf-8847-06b4d5558eed | 0.58485 | -54.21318 | 2026-09-07 05:21:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cf6d7e65-6fcb-3e2a-8010-b2e3718cb4c5 | 2.36283 | -50.77759 | 2026-09-07 05:21:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f7b04a08-9d1a-32ea-8a31-908ae60e873a | 0.21698 | -51.27972 | 2026-09-07 05:21:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 36e083a4-20cc-339c-9078-d57c078f4958 | 2.4951 | -50.81648 | 2026-09-07 05:21:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 3.3 |
| a8ecc535-bb0e-3196-ba23-945e9a8f8d86 | 1.72895 | -50.98459 | 2026-09-07 05:21:00 | NOAA-20 | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 44b97598-9155-32ea-b671-51e1db62084e | -5.36555 | -56.01507 | 2026-09-07 05:23:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| dced05d8-a40e-31d8-b775-091f6b68d001 | -5.16405 | -55.96208 | 2026-09-07 05:23:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3e86688a-e0a7-3099-8e5a-e5c707a15d58 | -5.34847 | -56.03856 | 2026-09-07 05:23:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5f6353a8-d5ce-340a-b019-104f9f99ff63 | -3.15003 | -60.63734 | 2026-09-07 05:23:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 62b06a59-12e0-382b-85a0-340d3ab81a1c | -8.72971 | -62.4437 | 2026-09-07 05:23:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 42880d56-7cc8-3797-b8e0-336453eb979d | -6.00129 | -57.69737 | 2026-09-07 05:23:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0a19b7d1-198f-304a-bd7b-69d9d722593b | -6.10967 | -57.74372 | 2026-09-07 05:23:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 82e14290-a740-379b-b97a-07a9c99a210c | -5.35875 | -56.01941 | 2026-09-07 05:23:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cfa0104c-d8f9-3314-9f3a-bec719e15447 | -5.1557 | -55.96907 | 2026-09-07 05:23:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 438f1da3-4e3e-317c-bc23-2abb3b29e6b4 | -4.66886 | -55.62849 | 2026-09-07 05:23:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| da7604ca-08e2-3f61-8037-be386348f7ab | -3.83172 | -60.76241 | 2026-09-07 05:23:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9239ec4e-ba8e-3f54-bf88-a1650e603a0c | -5.26957 | -60.15512 | 2026-09-07 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0adf9c62-50a8-3337-a05a-766918f35c2e | -5.4636 | -59.70913 | 2026-09-07 05:23:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c1139e08-ba67-38b0-909d-06661a9519ad | -3.83111 | -60.76619 | 2026-09-07 05:23:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 860ac78d-8085-31b6-a949-5eb5fd8da25e | -8.71624 | -62.43732 | 2026-09-07 05:23:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6402df7e-be2d-38d4-aeab-247a67c94fd2 | -3.03305 | -59.16276 | 2026-09-07 05:23:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 143eed71-998f-380c-84c6-73aad592b7dd | -4.11581 | -49.08765 | 2026-09-07 05:23:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 114560b4-ccc3-3683-9b46-a0ad611793ef | -4.66824 | -55.6326 | 2026-09-07 05:23:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4eed78c5-3a82-3aad-b406-447e4915ca13 | -3.76022 | -59.31351 | 2026-09-07 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bfacfab1-4d97-3824-883f-61e0de4c6e77 | -3.63798 | -59.54508 | 2026-09-07 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e3e6bffd-d509-33df-9dc3-d41caa78246b | -6.13544 | -57.68885 | 2026-09-07 05:23:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1fbea23a-c0fd-3943-a719-7e3f167b716e | -2.55661 | -59.44329 | 2026-09-07 05:23:00 | NOAA-20 | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d008d123-8a88-3eec-a362-8d2ad4e2a13f | -3.67399 | -48.91381 | 2026-09-07 05:23:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 349f33d6-831f-3f1b-8c9e-9e6c3fa5d985 | -5.36336 | -56.03666 | 2026-09-07 05:23:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d32001a1-38e3-305a-9d2e-537813c89668 | -5.28144 | -60.12416 | 2026-09-07 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1c1d637f-0005-36d7-94d0-91a41ffe5aa2 | -6.10625 | -57.69907 | 2026-09-07 05:23:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 50cf3dc8-4e09-3973-8371-36eef1573e74 | -1.19466 | -55.71642 | 2026-09-07 05:23:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e8ff7e8f-ed4d-31ed-a38c-c9a063aa9b55 | -12.7548 | -52.84517 | 2026-09-07 05:23:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5ac3aa63-bd6b-3fa5-8bf1-8d960553147e | -8.7527 | -62.41455 | 2026-09-07 05:23:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6c04c526-a816-3883-989a-33d3c02bccdc | -4.34643 | -48.97649 | 2026-09-07 05:23:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e208f121-c07d-3ee3-a713-f19766202560 | -3.33597 | -53.40483 | 2026-09-07 05:23:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 30909677-183f-38c5-b933-97354167c251 | -5.99566 | -57.68912 | 2026-09-07 05:23:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5aeff65c-fe8c-3689-813c-9dbb94a36201 | -3.1482 | -60.64873 | 2026-09-07 05:23:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 520cc3db-902a-33e4-9f66-e771cca08716 | -3.41575 | -54.77389 | 2026-09-07 05:23:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b039523d-9da1-3bc0-b5fa-75197ae9c5b5 | -3.16019 | -61.06665 | 2026-09-07 05:23:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8cfda12e-b0da-3fea-a597-72e8c0fedf1c | -5.14939 | -55.97002 | 2026-09-07 05:23:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c41ec708-4271-324c-a8ed-355d2b4ff58c | -5.35916 | -56.04015 | 2026-09-07 05:23:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b01a87f7-5f92-3db2-8c8c-28ec8fe1b272 | -5.27858 | -56.11433 | 2026-09-07 05:23:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f9d3b914-50e9-3ac5-91e9-eb8e991c1a8b | -3.64075 | -59.54912 | 2026-09-07 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d7efc3e7-7539-3dfd-9063-0a0929cbc3cf | -3.83721 | -59.59483 | 2026-09-07 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 27462f2c-7cf4-30f2-8e5e-53de93147b78 | -8.75622 | -62.41518 | 2026-09-07 05:23:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 26353ac2-2cb5-3af5-b5a7-aa83431cbc34 | -8.7668 | -62.41702 | 2026-09-07 05:23:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cc4316bb-a4a1-340e-ac57-e470030624cc | -3.51526 | -59.05813 | 2026-09-07 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d5709414-4d4f-3033-8be9-00d5591b524f | -5.15926 | -55.96964 | 2026-09-07 05:23:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9fccd75e-8181-316a-8dc4-157d6312bc4f | -5.15065 | -55.96193 | 2026-09-07 05:23:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5f888893-9414-3074-bf1b-6325297d5d7a | -11.65123 | -52.86539 | 2026-09-07 05:23:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ac710160-29d8-3f6f-ac3c-0d646bffb1f7 | -4.0374 | -50.87709 | 2026-09-07 05:23:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| a217696f-d13c-3ec9-9256-692eceb47d97 | -3.38891 | -61.31228 | 2026-09-07 05:23:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| aaa9eb8a-6c58-3082-9ec5-5db8af8fa484 | -1.20449 | -55.72169 | 2026-09-07 05:23:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 14edf615-494a-395d-a836-739b80510dbf | -5.99848 | -57.69324 | 2026-09-07 05:23:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 71753951-80a2-3ebb-9f56-684fff04f4d5 | -3.14514 | -60.66767 | 2026-09-07 05:23:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 16.0 |
| eef60a78-5fa1-3290-a26e-17ba3e434a90 | -3.64465 | -59.54613 | 2026-09-07 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e818ca30-b496-3aae-a171-cc38c600030e | -6.17644 | -57.73566 | 2026-09-07 05:23:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f1a9138e-226d-3825-81fd-6d88057c9b62 | -4.59677 | -50.98652 | 2026-09-07 05:23:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 90bbc92f-d1fe-3ae5-8fef-40ef087468e1 | -3.1586 | -58.65112 | 2026-09-07 05:23:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c03bfcdc-c116-3d9d-bc72-69a89c547fde | -3.24229 | -58.89391 | 2026-09-07 05:23:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README27.md)
