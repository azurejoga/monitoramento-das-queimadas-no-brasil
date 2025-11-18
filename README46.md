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

## Dados Diários - Página 46

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 28b66412-87c0-38ee-a57f-832e8b547759 | -7.61986 | -42.58558 | 2025-11-18 04:50:00 | NPP-375D | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| ba88773c-6e64-36a3-afca-ff65be4f254a | -12.87827 | -54.74193 | 2025-11-18 04:50:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a49e8032-d713-38c2-9d90-cf0e25a52ccb | -7.69548 | -46.84694 | 2025-11-18 04:50:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5ecc2582-08e2-32d9-a715-e1a29addcca1 | -9.89067 | -44.18632 | 2025-11-18 04:50:00 | NPP-375D | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 7.1 |
| cf1eb6f0-1ba0-3316-849f-9dea08f4088b | -11.20942 | -49.41657 | 2025-11-18 04:50:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 63ad22ee-bd7f-3f33-aacf-cd085570844c | -8.79379 | -44.38822 | 2025-11-18 04:50:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7d1dd170-2789-3962-b7b3-fbb40ef3bce7 | -6.19421 | -49.53937 | 2025-11-18 04:50:00 | NPP-375D | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ceedf30d-020a-3216-8e6b-33922a0d257d | -12.4541 | -54.44993 | 2025-11-18 04:50:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 69c56a78-8f33-392f-b8e0-e344d3d7f466 | -10.51483 | -43.96037 | 2025-11-18 04:50:00 | NPP-375D | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ff5b19a2-5bb8-3026-a889-e002b3d26d27 | -7.45691 | -46.84195 | 2025-11-18 04:50:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b222dc5e-c300-3d5d-b468-c23b92ace461 | -10.37889 | -49.91317 | 2025-11-18 04:50:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 499e123e-6179-37ac-9486-8afca3b97e7e | -12.55311 | -52.24967 | 2025-11-18 04:50:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.2 |
| 8e0f90d1-b597-370e-a7b7-1a90650b9bdf | -9.53445 | -48.34449 | 2025-11-18 04:50:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3ffa25c8-0e09-3b2e-b86a-d8a37b072cea | -12.86536 | -41.47524 | 2025-11-18 04:50:00 | NPP-375D | MUCUGÊ | BAHIA | Brasil | 2921906 | 29 | 33 | nan | nan | nan | Caatinga | 4.0 |
| c06306d1-2e18-36a8-8ce8-c3897bdf5fb7 | -7.62017 | -42.58571 | 2025-11-18 04:50:00 | NPP-375D | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 20cdd74d-884e-33cd-85a7-53dfde9f3895 | -12.86887 | -46.41372 | 2025-11-18 04:50:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1c6394db-d707-3e2c-a4ee-21d5c5ef014c | -11.29008 | -48.50952 | 2025-11-18 04:50:00 | NPP-375D | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fa3e1a37-5c06-3638-9258-fe39b224a790 | -7.29315 | -48.31874 | 2025-11-18 04:50:00 | NPP-375D | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 375d4e69-0b99-34a4-a2c7-922ca79b0fc3 | -12.41779 | -54.35441 | 2025-11-18 04:50:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9affdc33-b0a8-30de-8175-03c0e8f75915 | -6.93834 | -49.67152 | 2025-11-18 04:50:00 | NPP-375D | SAPUCAIA | PARÁ | Brasil | 1507755 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6fe88500-88b5-32fc-afb0-e5bcea28049d | -10.85781 | -44.1017 | 2025-11-18 04:50:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 6c82b10d-079f-32c8-a188-992fce75d11d | -8.09144 | -46.05732 | 2025-11-18 04:50:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ba47b5eb-5d7a-3ad1-8241-b10144dd0c25 | -6.09306 | -51.26679 | 2025-11-18 04:50:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8bab6cbb-5869-313f-a225-0925e49c0702 | -12.69792 | -46.77662 | 2025-11-18 04:50:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| f7d1883e-6e13-3be3-8e07-cf869c3df20f | -9.06025 | -45.42587 | 2025-11-18 04:50:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 709c15f9-d75b-37da-8ca7-09841b9fe69b | -10.76394 | -44.81239 | 2025-11-18 04:50:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4ea512bf-b987-3fe1-bbe4-f730c92c9a43 | -10.52054 | -43.9554 | 2025-11-18 04:50:00 | NPP-375D | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e2abaf46-9a84-35c0-9ebb-4ab33179d198 | -12.69683 | -46.78442 | 2025-11-18 04:50:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| db8f94ae-e4a5-3245-a37f-76cb81cbdfc8 | -8.73078 | -48.31752 | 2025-11-18 04:50:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d8047b62-365d-3284-971b-c4dc3ff00652 | -10.58956 | -49.0088 | 2025-11-18 04:50:00 | NPP-375D | NOVA ROSALÂNDIA | TOCANTINS | Brasil | 1715002 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4942590b-037d-3ece-a704-8e7c49743669 | -9.53812 | -48.34505 | 2025-11-18 04:50:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1975a9e3-b0f1-30dc-adb2-556281840fce | -9.4069 | -48.44972 | 2025-11-18 04:50:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 53373826-b567-33dc-9e93-5602bec9dc48 | -7.54317 | -47.04422 | 2025-11-18 04:50:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e2d1a8f4-47b0-3844-9b29-16b6e2d4ed57 | -10.34637 | -48.91291 | 2025-11-18 04:50:00 | NPP-375D | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5c62c6e2-c7e2-3a0a-a639-3e72b195653b | -10.85287 | -44.10118 | 2025-11-18 04:50:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6775c154-3804-3807-b461-056625c7297b | -7.358 | -46.21043 | 2025-11-18 04:50:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ff842e35-d954-30c0-8bb4-bb977fb8dc87 | -13.89916 | -47.49544 | 2025-11-18 04:50:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f06b5f1e-26a7-377e-9185-6d1e7282d27e | -7.14583 | -44.92402 | 2025-11-18 04:50:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a5d0955d-ac9b-3f60-aa98-b7a18074dc05 | -11.72498 | -49.84386 | 2025-11-18 04:50:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a49ce62d-49a8-3004-b8bf-08350a9e98d3 | -10.51591 | -43.96278 | 2025-11-18 04:50:00 | NPP-375D | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3ac458ac-8d9f-3c0e-801c-1ffc4c4c8116 | -7.30806 | -45.75813 | 2025-11-18 04:50:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3cb3ab8f-6ad2-3e34-8153-debaa248b80f | -10.51169 | -43.95649 | 2025-11-18 04:50:00 | NPP-375D | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4b2fdd2e-421e-39f9-b9f7-23e09e67a48c | -12.85876 | -41.47939 | 2025-11-18 04:50:00 | NPP-375D | MUCUGÊ | BAHIA | Brasil | 2921906 | 29 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 0a21a966-4d20-3c71-9d5f-54f547ca7ded | -7.42041 | -42.75579 | 2025-11-18 04:50:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| e1627960-061c-344d-9e6c-f3b76c7c36dc | -10.66213 | -49.37147 | 2025-11-18 04:50:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 91b22915-9713-3c3e-a786-e292636f3139 | -10.34809 | -48.92591 | 2025-11-18 04:50:00 | NPP-375D | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| cd9e7a39-3a27-30b6-840d-cf7cd3552a68 | -10.64748 | -49.73052 | 2025-11-18 04:50:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 102899e1-e62b-3a67-8162-f6d5ceafa254 | -9.16138 | -50.14072 | 2025-11-18 04:50:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| aded5bb5-a1c7-3b5e-97e5-65279693d2b3 | -11.66708 | -44.74022 | 2025-11-18 04:50:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 7.6 |
| e2763e61-cc48-398b-b973-acf1e0b3b532 | -8.66696 | -45.45559 | 2025-11-18 04:50:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 13bba4e1-f67d-3f5d-89db-ec86fc5a5b87 | -7.53862 | -47.04846 | 2025-11-18 04:50:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6f1f27c5-f1db-368a-8409-bc102a48118f | -10.66154 | -49.37545 | 2025-11-18 04:50:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 23956f22-5a91-31aa-b0b0-eea472db5b1d | -7.63098 | -42.58423 | 2025-11-18 04:50:00 | NPP-375D | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 33911d28-2797-3316-bee0-7ab8f80c2305 | -9.21353 | -48.59521 | 2025-11-18 04:50:00 | NPP-375D | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 05e13b0d-b2d7-3afb-9bfe-60bde263292b | -9.88102 | -44.18509 | 2025-11-18 04:50:00 | NPP-375D | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 7.1 |
| a99d5be0-4f97-389e-b101-e93c10a32986 | -12.70415 | -46.79339 | 2025-11-18 04:50:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7e623915-a8c5-3f25-bea6-21f398bc362b | -10.72511 | -49.07078 | 2025-11-18 04:50:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 9739924f-4d1c-33b2-9185-cfbe8ee98330 | -11.71121 | -48.86509 | 2025-11-18 04:50:00 | NPP-375D | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 84814f40-9dd3-3044-8d86-82e32232c954 | -9.72225 | -48.91262 | 2025-11-18 04:50:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f20d6e24-8147-3c16-968c-f21cceb7248f | -6.86514 | -47.07705 | 2025-11-18 04:50:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f2614e5e-ad61-3f9f-afc3-acd28678fb9a | -10.75152 | -45.14814 | 2025-11-18 04:50:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f959bbcc-4924-3488-af3a-61c22eaed11f | -12.2337 | -49.38201 | 2025-11-18 04:50:00 | NPP-375D | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| bb8383df-2fc7-304c-838e-e5bbde362b41 | -10.30902 | -54.20446 | 2025-11-18 04:50:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e38edbb5-4b7e-3e99-8ec9-da84707e1b5d | -12.00593 | -49.26474 | 2025-11-18 04:50:00 | NPP-375D | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1fe355b9-1a9e-3b0b-b5ce-f8a3dd78d9e0 | -11.88518 | -44.20547 | 2025-11-18 04:50:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f8c237ec-fc69-3e33-a312-b708fcaa761a | -7.86012 | -46.86854 | 2025-11-18 04:50:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 88f14ef3-612d-32c9-be80-9d760c325d60 | -11.56162 | -48.46262 | 2025-11-18 04:50:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 3c2068c6-9c8d-3864-894f-2aa416a326a4 | -9.39599 | -48.44802 | 2025-11-18 04:50:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 19.2 |
| 7f760e76-5679-337f-beda-e2a38e626267 | -8.20348 | -49.79293 | 2025-11-18 04:50:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 85140609-3b4b-3bd0-a0c9-8e1a4aa4aee4 | -12.86487 | -41.47927 | 2025-11-18 04:50:00 | NPP-375D | MUCUGÊ | BAHIA | Brasil | 2921906 | 29 | 33 | nan | nan | nan | Caatinga | 4.0 |
| e822eb13-c74e-394a-beb7-2fedb79a1253 | -8.93215 | -49.83816 | 2025-11-18 04:50:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 61124107-4227-334c-b959-8f3ef4620dea | -9.38809 | -48.45113 | 2025-11-18 04:50:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1d2c88ed-4bbf-34ab-b7a3-589a6590a326 | -10.66272 | -49.36749 | 2025-11-18 04:50:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2ed2be0e-14ed-373e-9bc4-a8f525da5450 | -7.43693 | -45.20062 | 2025-11-18 04:50:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c518e8ff-0977-34ab-9385-fd01896911ed | -10.53695 | -47.99324 | 2025-11-18 04:50:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f26e1518-9084-3759-ab02-5317a76bf60a | -7.43871 | -45.1885 | 2025-11-18 04:50:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cb12251b-e2fb-384c-aea9-9fe13d8a48bd | -10.99728 | -50.9278 | 2025-11-18 04:50:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 08701441-fe95-3b6c-b753-72342dff24f4 | -8.29994 | -44.22556 | 2025-11-18 04:50:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4e69b8de-f407-3336-b138-7b9b8a4e3f5b | -11.28847 | -48.5107 | 2025-11-18 04:50:00 | NPP-375D | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| aa8dffea-5edf-3efd-a601-9c740412c136 | -12.69846 | -46.77272 | 2025-11-18 04:50:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 3623b44b-f1c0-3721-bb62-86cd0bb136d7 | -12.23878 | -49.38111 | 2025-11-18 04:50:00 | NPP-375D | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0a6f5a96-9b71-3a4f-8781-af5df99c50cf | -12.8593 | -41.48795 | 2025-11-18 04:50:00 | NPP-375D | MUCUGÊ | BAHIA | Brasil | 2921906 | 29 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 3e49865e-c355-300f-97f7-709f42e42e44 | -9.9728 | -44.77802 | 2025-11-18 04:50:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b9032c98-5f9d-39bb-96c0-039475239b57 | -10.16377 | -48.15498 | 2025-11-18 04:50:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e4166297-2c3a-3874-b003-1d31dbc85d57 | -10.99448 | -50.92367 | 2025-11-18 04:50:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d29d4f94-295d-350e-bfcc-82beefb89c00 | -8.12526 | -49.50404 | 2025-11-18 04:50:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2d8de614-d1a8-3bee-8404-836d77954dc6 | -9.96953 | -44.77602 | 2025-11-18 04:50:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 44bb9b75-42eb-32da-a643-a042b4bd42e5 | -11.51974 | -48.95321 | 2025-11-18 04:50:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f5bdf7d7-ea23-313c-99c6-b0bf02d3555f | -9.49452 | -63.50552 | 2025-11-18 04:50:00 | NPP-375D | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 38146eab-5255-34cf-9aa3-b4f582904a15 | -7.0925 | -52.86684 | 2025-11-18 04:50:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4d092440-c344-3e41-a4f2-77789f60021f | -9.41053 | -48.45029 | 2025-11-18 04:50:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d3473605-f781-31af-937a-5ee0af348b6b | -12.85829 | -41.48323 | 2025-11-18 04:50:00 | NPP-375D | MUCUGÊ | BAHIA | Brasil | 2921906 | 29 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 23f95588-5185-3eac-be3a-82a0f1c30d43 | -7.07964 | -52.61827 | 2025-11-18 04:50:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f334eedd-015f-3f4e-994d-fad6591b0468 | -6.09638 | -51.26731 | 2025-11-18 04:50:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 921d29e2-ab69-3eb4-a130-892740efa41c | -9.40263 | -48.45339 | 2025-11-18 04:50:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 96ffacae-7685-3234-9a0e-37f46acf127b | -12.71926 | -45.39062 | 2025-11-18 04:50:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| dfa21fac-e7eb-3c1e-9b75-a91adf8cdb44 | -5.95925 | -52.93521 | 2025-11-18 04:50:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ed34f264-426c-3a8d-aabb-d5dfb32461e4 | -11.20234 | -49.41546 | 2025-11-18 04:50:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b71c5bf5-4dc5-31d9-98c6-e5c81d92127b | -10.52013 | -43.96898 | 2025-11-18 04:50:00 | NPP-375D | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7e7fcdc6-e166-30d4-98a4-67032302456c | -11.8377 | -47.59809 | 2025-11-18 04:50:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |


[Clique aqui para ver as próximas entradas](README47.md)
