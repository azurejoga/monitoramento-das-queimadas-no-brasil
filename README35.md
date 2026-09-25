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
| d31f9021-de57-354d-ac81-9c4f36efe551 | -12.20552 | -50.73239 | 2026-09-25 05:31:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 12b60e94-ff85-38b3-bdac-3a259bfe27e3 | -9.39182 | -60.34638 | 2026-09-25 05:31:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 01524f79-52c6-3747-a7c3-d271c6358f28 | -12.20897 | -50.70219 | 2026-09-25 05:31:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| bdb0e58f-1605-312d-9ba1-09e188d29d6b | -10.07934 | -63.08241 | 2026-09-25 05:31:00 | NOAA-21 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6aada302-3adf-34f3-b534-47a9c08f2914 | -11.28866 | -51.29076 | 2026-09-25 05:31:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 39.1 |
| 0e248427-5785-3170-a062-704d06613523 | -12.20271 | -50.7271 | 2026-09-25 05:31:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 9af3f243-237d-3a70-895f-e4a611fe7630 | -9.16165 | -59.47349 | 2026-09-25 05:31:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 3f78f8a5-ff2f-35ee-8c90-220a7d233ba7 | -12.14724 | -61.17236 | 2026-09-25 05:31:00 | NOAA-21 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f26d73f4-6b1d-314e-9b0b-264fa9f6079d | -12.2376 | -50.7193 | 2026-09-25 05:31:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 68cbe5b9-6b9e-3b7c-8c80-6a60c07b3f7a | -12.18827 | -50.7984 | 2026-09-25 05:31:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 6726dc2c-c3f1-354d-bc68-031079defbda | -12.23035 | -50.78558 | 2026-09-25 05:31:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 41.6 |
| 33e62664-2a0e-3282-8b29-3817336fe05a | -9.58624 | -60.52304 | 2026-09-25 05:31:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| cd8bedca-6af7-30a0-8a2b-d7c055af35bd | -12.19797 | -50.79842 | 2026-09-25 05:31:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 9c57b3ef-f785-36e7-af50-a80047003f2d | -8.90774 | -71.34247 | 2026-09-25 05:31:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 01def6c2-5dc3-32b0-91f4-7bc9453420f8 | -10.62473 | -53.99266 | 2026-09-25 05:31:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 699b8532-1ce9-35b0-8146-895273589211 | -12.22154 | -50.74179 | 2026-09-25 05:31:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 23.3 |
| d68b2522-90c8-34de-863e-1152b014f089 | -9.02742 | -60.55793 | 2026-09-25 05:31:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5f95eff2-0bee-305b-9051-5385e9f18f1c | -12.2343 | -50.74952 | 2026-09-25 05:31:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 79.6 |
| 289aea22-0039-3b83-82a3-00c5d585bede | -11.18268 | -51.36319 | 2026-09-25 05:31:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 07643c52-78c8-3a35-a8b3-e1ad882fd190 | -9.67181 | -66.83253 | 2026-09-25 05:31:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| faeff029-d851-3ea8-a13a-5b9d2409e514 | -12.23022 | -50.72449 | 2026-09-25 05:31:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 36.0 |
| 8c005089-ad9c-34cf-8af4-129b20ebeac3 | -9.3878 | -66.50809 | 2026-09-25 05:31:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d3380b7d-f268-3c6e-8810-d51c65911ba6 | -12.19729 | -50.80438 | 2026-09-25 05:31:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| adf1e8e7-5236-38e4-aabe-1a7d01cb0870 | -8.9027 | -71.34158 | 2026-09-25 05:31:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f57b515d-2e87-3645-a498-ccf111079d47 | -10.44776 | -69.30154 | 2026-09-25 05:31:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 37a02ca0-f51d-34a2-bb45-79d029ab2ac2 | -10.62347 | -54.00299 | 2026-09-25 05:31:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ac6e5428-36e1-31fe-ab2e-42707052b10f | -9.9383 | -60.71728 | 2026-09-25 05:31:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 535e77f6-e67a-3c76-9d94-d80b3c016cd1 | -9.20979 | -60.45617 | 2026-09-25 05:31:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fa2ca943-8c44-3d15-b0c2-7b19a54ea1c0 | -12.22431 | -50.77874 | 2026-09-25 05:31:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 0169ae6e-06f4-330a-aef7-a7f72e9ac469 | -9.86467 | -65.18967 | 2026-09-25 05:31:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| da7431d7-2fd1-3d5e-bc3d-154bf34307b6 | -12.16795 | -50.70324 | 2026-09-25 05:31:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 8.9 |
| ed647ac6-4935-3157-bc19-024334f19ff1 | -12.22562 | -50.76674 | 2026-09-25 05:31:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 87147ef0-992a-360a-b474-da5a7fd1e4bd | -9.15612 | -59.48587 | 2026-09-25 05:31:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d8774d92-e9aa-339a-b436-88b5021d3402 | -12.19664 | -50.72021 | 2026-09-25 05:31:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 48959b7e-f7d8-3d1b-b65b-4dd59819eebe | -9.16227 | -59.46915 | 2026-09-25 05:31:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d093bc74-9952-36e6-9a69-2d4509b8008c | -12.21548 | -50.73487 | 2026-09-25 05:31:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 2d34d937-9ff3-3c6c-b683-81b516f68c54 | -12.19129 | -50.79758 | 2026-09-25 05:31:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 291471c2-e5b7-3872-91df-a59018425ad6 | -9.02277 | -60.51768 | 2026-09-25 05:31:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e839e09f-25e4-3e89-b535-fca47e666075 | -9.02567 | -60.52208 | 2026-09-25 05:31:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| d8f4c577-ed72-3379-a02a-dd104dc57cd2 | -12.21501 | -50.80184 | 2026-09-25 05:31:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 0064992f-4aba-3e03-aeed-90803c08a01c | -8.90218 | -71.34451 | 2026-09-25 05:31:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d77bfcbf-13fb-35b1-8744-f2aa2e01b7b2 | -7.86693 | -72.86436 | 2026-09-25 05:31:00 | NOAA-21 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 5834dbd8-0a79-3484-a3da-b4f7892059d3 | -12.21007 | -50.72191 | 2026-09-25 05:31:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 3ad43779-5c19-33d9-a7f5-340d5f1d0759 | -9.07152 | -65.69705 | 2026-09-25 05:31:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5bd3f925-2c8b-3b1a-a1c4-c8b9a573dc9b | -9.028 | -60.55405 | 2026-09-25 05:31:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0b5afc71-1bc8-3bd6-b397-ed935f0161a6 | -9.0875 | -61.44085 | 2026-09-25 05:31:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b64bf59c-1a06-3af9-9e48-f7558812e6a9 | -14.46653 | -53.64442 | 2026-09-25 05:31:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 35cf73d8-98ff-3185-ad23-48dd47532502 | -10.3945 | -64.00045 | 2026-09-25 05:31:00 | NOAA-21 | CAMPO NOVO DE RONDÔNIA | RONDÔNIA | Brasil | 1100700 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e5d8771d-3058-3f46-b9f9-ac2a19567fe9 | -9.15183 | -59.48963 | 2026-09-25 05:31:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 68fe08a9-19b1-3424-a795-09d0eb3c0df0 | -7.52282 | -70.39397 | 2026-09-25 05:31:00 | NOAA-21 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| d1fad55c-59f0-33e6-88fc-8b5dc602315a | -10.90471 | -53.94204 | 2026-09-25 05:31:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 23889a7f-ad50-33da-b7dc-4f5164f1c3ea | -12.25309 | -50.7641 | 2026-09-25 05:31:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 20.1 |
| 667edd20-248d-3a0c-b941-5db8d0d25e11 | -12.20293 | -50.78817 | 2026-09-25 05:31:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 28.7 |
| cf2471b1-823c-33d9-b0f2-c24048a77242 | -9.25478 | -60.93388 | 2026-09-25 05:31:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cd309bd3-922d-3f96-835d-8c6c6ddf52ba | -10.62234 | -53.98625 | 2026-09-25 05:31:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 27faf653-8bbd-32e2-bcc6-0dd3107e043d | -11.29444 | -51.29692 | 2026-09-25 05:31:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 1c34345c-139a-3e9f-9b9f-7b7da9f8e114 | -12.241 | -50.75037 | 2026-09-25 05:31:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 79.6 |
| e2f2ac0f-217a-3d9d-a822-fcdd324a1db6 | -10.9551 | -58.9634 | 2026-09-25 05:31:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 00f5396e-b92c-3116-81e7-71a352c32ec7 | -12.20759 | -50.7143 | 2026-09-25 05:31:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 81dad773-0bbf-3345-842f-874ac06a72b3 | -9.21213 | -60.46454 | 2026-09-25 05:31:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7a9b6e03-0bf8-3e89-a989-0db1e8d63725 | -9.41822 | -60.46629 | 2026-09-25 05:31:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e54aa370-16fd-3ffc-bf8e-604d7636c81d | -9.93424 | -60.72065 | 2026-09-25 05:31:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6da1fabf-35c7-3dec-970f-e40b378dd645 | -12.21483 | -50.74093 | 2026-09-25 05:31:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 20.9 |
| 2faa1bc8-2dd8-3340-a198-2751d12580dd | -11.28378 | -51.28957 | 2026-09-25 05:31:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| facc7595-a47a-3df4-8b0b-9ec9d59a3244 | -12.22285 | -50.72966 | 2026-09-25 05:31:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 60.7 |
| 252ff6a5-7799-35a7-a95d-7ce7628d13e2 | -8.55952 | -63.07753 | 2026-09-25 05:31:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0e14f79e-698d-39d5-a25c-03f9362edeca | -11.2816 | -51.29528 | 2026-09-25 05:31:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 8524dc0d-f2ed-3fd9-b113-ad569feceab4 | -10.62013 | -54.00334 | 2026-09-25 05:31:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c5b057f9-d9b3-3d60-8a12-f0b158bd5c7e | -12.23154 | -50.71235 | 2026-09-25 05:31:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 666f549a-4975-31a7-9b8a-85791d987adc | -13.78325 | -54.04187 | 2026-09-25 05:31:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 50867cd2-aa77-3a69-ac1c-69fa290df1f3 | -12.22366 | -50.78473 | 2026-09-25 05:31:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 6.3 |
| b2d30507-c6c1-34c2-8d97-90f2a7d3483a | -15.18827 | -56.05172 | 2026-09-25 05:31:00 | NOAA-21 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 7e986ea6-7cfc-3e13-9162-dc69dca77b36 | -12.24034 | -50.75639 | 2026-09-25 05:31:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 12.1 |
| c84c8c03-444d-36f6-9872-74e2039e72e7 | -9.50271 | -64.7523 | 2026-09-25 05:31:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6d44e365-7efc-3de3-a4ba-f5d76f4a7f0f | -9.36427 | -60.3626 | 2026-09-25 05:31:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 68d51361-a2c3-3a92-819f-2191117562bc | -9.16249 | -59.41581 | 2026-09-25 05:31:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0d9956c3-200b-30d0-9fca-d26f067fcbe8 | -11.28097 | -51.30056 | 2026-09-25 05:31:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 11c9e42f-5417-3f83-ae0b-6f32d2337b39 | -6.95181 | -71.78905 | 2026-09-25 05:31:00 | NOAA-21 | IPIXUNA | AMAZONAS | Brasil | 1301803 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 37a0b52f-3810-3d93-b5f2-fe67c5936926 | -10.61522 | -53.99916 | 2026-09-25 05:31:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4aa7f440-b53e-358f-a2c1-503267e209cc | -12.19346 | -50.71868 | 2026-09-25 05:31:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 83848ff9-fcb8-36ba-872f-1e06f7febcd5 | -12.19865 | -50.79245 | 2026-09-25 05:31:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 7617ae78-4db4-39e0-b22f-329c8ba07cf4 | -15.18932 | -56.05312 | 2026-09-25 05:31:00 | NOAA-21 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c0eb8eaa-4587-3e06-ab8d-6638421e1b87 | -9.03685 | -61.66175 | 2026-09-25 05:31:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 4.4 |
| b7a20972-1d14-3826-867e-65930d08b944 | -10.90427 | -53.94554 | 2026-09-25 05:31:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f789a4b5-7b13-3ae7-9361-1653a46b3e9d | -9.02394 | -60.55742 | 2026-09-25 05:31:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9e6131e6-12b3-36c3-9c51-4b079a134760 | -12.23694 | -50.72536 | 2026-09-25 05:31:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 852d0d4f-5eb1-3ecf-87e3-bbe5bd684fb3 | -8.90722 | -71.3454 | 2026-09-25 05:31:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a330c2a8-ece8-36b8-937e-ab86457f7baa | -19.10652 | -57.81861 | 2026-09-25 05:33:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 771e391d-b6d2-3cd4-8ab9-6eec3547c1d6 | 0.49904 | -60.59825 | 2026-09-25 06:03:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 12d17c3e-87bc-30fc-b4eb-954dcf42f7fd | 1.57968 | -56.01361 | 2026-09-25 06:03:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 47e99de9-46ee-3dff-8f4d-278286ed407e | 3.56263 | -61.16713 | 2026-09-25 06:03:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 81dcd971-e81f-3d8e-911c-84dca347b01f | -1.14326 | -54.09184 | 2026-09-25 06:03:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4348e1a1-1dcd-3871-9789-930e22b53b5c | -1.1423 | -54.09824 | 2026-09-25 06:03:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| a113cc85-3856-3387-80d6-d37f3d71bbc0 | 1.59531 | -55.85146 | 2026-09-25 06:03:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9850fc00-7225-33a1-a6cd-13fdc1aea82c | 0.49833 | -60.59388 | 2026-09-25 06:03:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 246aca23-ef7c-3b14-8da2-86489c8293ce | -1.14288 | -54.1031 | 2026-09-25 06:03:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| a9d99c67-54cd-3db5-b0e9-cc4ae6924b94 | -1.1449 | -54.09027 | 2026-09-25 06:03:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| ae1bc92a-4c30-3689-b026-5e02472013a9 | 1.62755 | -55.93548 | 2026-09-25 06:03:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| a316ef81-2a27-3405-9224-d56b1d7aa5ef | 3.0786 | -59.96964 | 2026-09-25 06:03:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5bac4c7d-ab9e-3bb1-b98c-6c4ecc847981 | 0.4955 | -60.59661 | 2026-09-25 06:03:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README36.md)
