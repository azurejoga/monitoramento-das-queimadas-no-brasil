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

## Dados Diários - Página 24

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5a1153a5-4ed1-3e68-8594-43a8c78691ed | -6.1792 | -48.0494 | 2025-07-09 05:20:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 64.8 |
| 92d8db0e-8e13-3afe-839e-008dbf28e3be | -8.5214 | -43.2828 | 2025-07-09 05:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 125.8 |
| a17a8bae-4e5c-34dd-9526-4bcb695a9c44 | -10.5776 | -49.1316 | 2025-07-09 05:20:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 64.2 |
| c5fd4f67-a88e-3d72-b623-cba08e7f2c94 | -11.4393 | -45.1154 | 2025-07-09 05:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 39.0 |
| e7e47316-1155-3fa5-b7f9-76d84a2bb958 | -8.5028 | -43.2614 | 2025-07-09 05:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 119.6 |
| 1da5a5d5-0970-366d-976f-bcd13dec2481 | -8.5217 | -43.2593 | 2025-07-09 05:20:00 | GOES-19 | TAMBORIL DO PIAUÍ | PIAUÍ | Brasil | 2210953 | 22 | 33 | nan | nan | nan | Caatinga | 75.6 |
| ad41826b-0e16-36b5-9032-6faa2bc217ad | -8.5217 | -43.2593 | 2025-07-09 05:30:00 | GOES-19 | TAMBORIL DO PIAUÍ | PIAUÍ | Brasil | 2210953 | 22 | 33 | nan | nan | nan | Caatinga | 76.8 |
| 2723e691-90ec-3a74-81a2-b0dd69c53aaa | -8.5028 | -43.2614 | 2025-07-09 05:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 94.8 |
| 1bb9da90-b307-3880-a805-0a70f9fa8699 | -11.4397 | -45.0923 | 2025-07-09 05:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 51.5 |
| 845862b5-1d1e-38f9-af55-33877eb2c7c0 | -8.5214 | -43.2828 | 2025-07-09 05:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 140.2 |
| 28ef2d8a-ad4b-3ebe-b047-7f458c6588ea | -8.5025 | -43.285 | 2025-07-09 05:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 172.1 |
| 15654bb5-7c75-358a-9e53-a9ecebd35f1c | -11.4393 | -45.1154 | 2025-07-09 05:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 57.9 |
| e0de9e07-e180-3735-8dd3-e6dc8a49b04f | -10.5776 | -49.1316 | 2025-07-09 05:30:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 60.5 |
| b5336860-7570-3f35-8db0-5220863c9849 | 2.72556 | -61.45884 | 2025-07-09 05:33:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| cdbb7a67-c3fd-3b27-ae71-0c94da4f3998 | -4.27121 | -49.72608 | 2025-07-09 05:36:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| cd34b077-ba93-3ecc-9d72-057cf7d50eea | -7.63378 | -56.71392 | 2025-07-09 05:36:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4dba1878-3042-32ec-bfb4-9fefa004b781 | -5.58899 | -52.07889 | 2025-07-09 05:36:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7796889c-fc56-3b8a-98b4-ba0f90a9607d | -7.93197 | -61.55914 | 2025-07-09 05:36:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2f975b1d-2033-336c-b6aa-7af708b6e8a4 | -4.26509 | -49.71804 | 2025-07-09 05:36:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 36e5301d-c50e-399e-af23-a3bb3f8988d9 | -7.91727 | -61.5574 | 2025-07-09 05:36:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 85482126-1b22-3e51-beac-80425b569a62 | -7.63488 | -56.71603 | 2025-07-09 05:36:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3767349f-debe-380a-b3d8-9dc99a6c099b | -5.12495 | -56.11584 | 2025-07-09 05:36:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 87206fb7-96cb-3895-972f-005097bb4055 | -8.3062 | -55.10946 | 2025-07-09 05:36:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5a82d379-f814-3cff-bd72-8c2659e7e9cf | -5.5929 | -52.07993 | 2025-07-09 05:36:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 11d9f9fe-53a4-3ef0-928f-387a2f7a074f | -5.59225 | -52.08486 | 2025-07-09 05:36:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| a13b5af8-6afe-3744-a55e-e0e684f01858 | -5.58831 | -52.08381 | 2025-07-09 05:36:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 75edbb91-0f47-3905-89de-35629767f09d | -9.33368 | -58.84713 | 2025-07-09 05:38:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 64f7b36f-e16f-3eb9-850a-aba0e883eef1 | -12.58082 | -56.97299 | 2025-07-09 05:38:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7b60df40-8d73-3413-82d5-320a292d52b4 | -9.02319 | -61.22865 | 2025-07-09 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d0bb8825-c0f6-3d69-8882-92c166098f34 | -9.02256 | -61.23285 | 2025-07-09 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3da2f153-12e2-3334-8d8f-5a8504f6c1c8 | -9.41213 | -58.90501 | 2025-07-09 05:38:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 75095840-3fa9-384c-b730-e8574e7afec6 | -9.01576 | -59.54391 | 2025-07-09 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| fea8d1ae-0397-3ef0-abba-65ed7c734f99 | -15.88769 | -58.55988 | 2025-07-09 05:38:00 | NOAA-21 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 414203d9-c675-33bd-b80d-fbfade8a9cb5 | -9.33841 | -58.84388 | 2025-07-09 05:38:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 45b4379e-4add-3e95-960f-5f87f4b84ba6 | -10.30028 | -57.12564 | 2025-07-09 05:38:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 54d2349c-d3d3-3c2b-bcea-a67e3122deb2 | -9.50563 | -65.58676 | 2025-07-09 05:38:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6c62b695-6126-31b7-baaa-c376829d5b7f | -9.41161 | -58.90876 | 2025-07-09 05:38:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 07cdc720-f813-3e0d-9e29-88d75b3f4a03 | -10.34642 | -56.48884 | 2025-07-09 05:38:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fa575f98-6694-3938-9ed5-cbdfa98f95a8 | -9.92634 | -59.90164 | 2025-07-09 05:38:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a97ada78-0ba4-36c6-a2a9-deca38f79844 | -11.33279 | -55.21813 | 2025-07-09 05:38:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c7ae04b0-4a9e-3b72-9e16-f15f1d94cc57 | -9.01833 | -61.2365 | 2025-07-09 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 621f3988-85b3-3cab-ba4a-99db1cdf3df7 | -10.34603 | -56.49174 | 2025-07-09 05:38:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 745eeec3-712f-39d8-b0a0-9fb0ff2fcaff | -9.4163 | -58.90568 | 2025-07-09 05:38:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c92c7f7a-6fb5-33c1-9fe0-16ed42ba3229 | -15.88953 | -58.56126 | 2025-07-09 05:38:00 | NOAA-21 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| b657fb49-8f5c-3f48-ba22-74d22acb2a89 | -12.02679 | -57.08149 | 2025-07-09 05:38:00 | NOAA-21 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6ee808eb-d309-3d20-8867-a61db40b71d9 | -9.41579 | -58.90944 | 2025-07-09 05:38:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0c02c432-c026-3b3e-8922-51057ff27fcf | -7.9153 | -70.92515 | 2025-07-09 05:38:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1ac4d88c-5676-352e-ab85-b316e24f7478 | -8.92783 | -63.8729 | 2025-07-09 05:38:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7d60056a-fa41-3049-ae56-eb5fbaf0725c | -9.60887 | -63.46587 | 2025-07-09 05:38:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a4fc8bd3-5476-37dc-9249-e7a92085d501 | -9.46295 | -62.19471 | 2025-07-09 05:38:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7bc38409-62ee-3aa8-8a6e-ff7200ca8bbc | -10.29563 | -60.54697 | 2025-07-09 05:38:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 13760701-29b1-3911-9830-cde584b42d4e | -9.94576 | -66.86142 | 2025-07-09 05:38:00 | NOAA-21 | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bad0d8c2-6200-31d9-b6ee-08d5febc2d89 | -12.58046 | -56.97595 | 2025-07-09 05:38:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d8ab0d06-2303-311e-90b5-a712e6ebab25 | -11.33232 | -55.22189 | 2025-07-09 05:38:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a38bcbd9-dfea-31c5-943e-7e7843cc7c0b | -12.79778 | -62.01109 | 2025-07-09 05:38:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5519dd52-cf73-3e22-b57c-8b101278a943 | -11.88033 | -58.7154 | 2025-07-09 05:38:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 0c5af4cb-f8cf-3853-a674-32074ee796c6 | -9.92995 | -59.93339 | 2025-07-09 05:38:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| e82c6746-7612-3639-bb92-35646e83478f | -9.63054 | -67.25019 | 2025-07-09 05:38:00 | NOAA-21 | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6d01f497-ef64-327c-b0d1-6454af6a8a99 | -10.5776 | -49.1316 | 2025-07-09 05:40:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 64.8 |
| 69f818c0-f6c1-346a-bcbf-57e92884b5b4 | -8.5214 | -43.2828 | 2025-07-09 05:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 97.4 |
| 539be189-8f35-3737-b49b-940f4a2b3e4b | -6.1792 | -48.0494 | 2025-07-09 05:40:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 58.4 |
| 352c00ad-6595-3d69-a814-cce060d5c38b | -11.4393 | -45.1154 | 2025-07-09 05:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 66.2 |
| 57628a75-45b3-3c26-bd0c-67b625ee13c0 | -11.4397 | -45.0923 | 2025-07-09 05:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 62.9 |
| 213d064c-35ba-3010-aa43-3538e4bb2831 | -8.5028 | -43.2614 | 2025-07-09 05:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 102.9 |
| ea0b8765-506a-322c-b648-835779f4daf5 | -10.5779 | -49.1098 | 2025-07-09 05:40:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 64.8 |
| c820bba6-0e42-35b4-a4d6-bf640cd25b3e | -8.5025 | -43.285 | 2025-07-09 05:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 214.3 |
| c484be57-f42a-3456-b12c-ce3894408ada | -18.64102 | -55.72999 | 2025-07-09 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| de0cb823-5b94-3b3d-93b5-c8ddb208d147 | -21.44196 | -54.5761 | 2025-07-09 05:40:00 | NOAA-21 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0dc84361-a599-3f80-b987-0430eb84faaf | -19.09268 | -56.04942 | 2025-07-09 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 0672c146-ea68-3c1f-963b-c2abc24e20ad | -19.75207 | -53.99961 | 2025-07-09 05:40:00 | NOAA-21 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1de91a4a-4dfd-3f94-aa7b-90ed07890fca | -18.65356 | -55.73106 | 2025-07-09 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 07947c79-c4e8-3574-bd84-fc8f2d50c3da | -20.86321 | -55.29683 | 2025-07-09 05:40:00 | NOAA-21 | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d1c78d3c-0d46-3a27-953a-af70488f0a5c | -18.65401 | -55.72669 | 2025-07-09 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.9 |
| 86d0075d-3f1e-3ec9-988b-34f4261660d0 | -18.64647 | -55.73505 | 2025-07-09 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.7 |
| fc9986f7-f395-399e-b5bd-da8cd6754c4a | -18.65274 | -55.73136 | 2025-07-09 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.6 |
| 7bcb111d-b83f-382b-a39a-619352e4f577 | -19.08691 | -56.04875 | 2025-07-09 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| cd31b026-ff99-3590-89c9-ba90d5e0b169 | -18.64726 | -55.73477 | 2025-07-09 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 5cbe3692-e7f5-381f-98b4-d0b08e099321 | -18.64688 | -55.73068 | 2025-07-09 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.6 |
| 813975fb-f305-3fd2-bb7a-dd486591be28 | -18.64184 | -55.72973 | 2025-07-09 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.5 |
| fe65e9b6-b5a7-3728-852a-1fb41d3d1a69 | -18.64814 | -55.72604 | 2025-07-09 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.9 |
| d84c4d7e-3e10-34af-8cdb-66e3869858b9 | -20.7287 | -56.65773 | 2025-07-09 05:40:00 | NOAA-21 | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 38ad34e5-73a3-35ad-81c0-88899ad79ee2 | -18.64143 | -55.72561 | 2025-07-09 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 7f0c9072-90ab-3955-a31b-3f96ec88a852 | -18.64228 | -55.72535 | 2025-07-09 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 735ae857-5bb0-3ce6-955f-78e14a7bd476 | -20.72915 | -56.65294 | 2025-07-09 05:40:00 | NOAA-21 | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 69931464-5251-3ed9-87ea-c01d6ad5d956 | -18.64729 | -55.7263 | 2025-07-09 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.6 |
| 0a1979a7-e906-3696-84e0-c9b4619871b5 | -18.64183 | -55.72122 | 2025-07-09 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 2e8051bc-e03c-3225-8666-52a1e95cbea5 | -18.64272 | -55.72098 | 2025-07-09 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 94d96cfc-72a2-357d-bd82-f7b7281c5bdd | -18.65315 | -55.72698 | 2025-07-09 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.6 |
| db0845f8-aa6a-3857-80b7-57ff917ede68 | -18.6477 | -55.72192 | 2025-07-09 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.5 |
| d4451def-5bc4-38d1-b2a2-3b221f68b341 | -18.6477 | -55.7304 | 2025-07-09 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 35a8e2ca-3ed5-3ccd-bd04-abeeaac292c1 | -6.1792 | -48.0494 | 2025-07-09 05:50:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 58.7 |
| ca8d7091-2bcd-3941-a119-ee7444ae920f | -8.5028 | -43.2614 | 2025-07-09 05:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 93.2 |
| 1fac5550-d061-3731-b205-dfa16b5affa7 | -8.5025 | -43.285 | 2025-07-09 05:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 196.7 |
| 7dcdeca0-9413-39b8-8775-804240513e38 | -11.4397 | -45.0923 | 2025-07-09 05:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 53.6 |
| 9abbbf90-373d-3f3c-873c-e5bc6cd30c7d | -10.5776 | -49.1316 | 2025-07-09 05:50:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 65.5 |
| 3d5b3d67-df1e-3f5e-a876-b232e8a9efd0 | -10.5779 | -49.1098 | 2025-07-09 05:50:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 62.9 |
| a3b561a5-4162-3e55-9eb8-5c34b68db481 | -11.4393 | -45.1154 | 2025-07-09 05:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 70.9 |
| ac0b3355-5f7c-32f5-9fc1-caa7533eb65c | -8.5214 | -43.2828 | 2025-07-09 05:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 100.5 |
| 00e37eb7-a356-35fb-a0bc-2fbeb49acb56 | -11.4397 | -45.0923 | 2025-07-09 06:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 68.6 |
| a4bb79c3-7722-3626-a5fc-548bbbdd6aca | -8.5214 | -43.2828 | 2025-07-09 06:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 96.1 |


[Clique aqui para ver as próximas entradas](README25.md)
