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

## Dados Diários - Página 59

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4a5f5618-1f2f-34cf-8fc6-65dba079a595 | -14.70669 | -55.9506 | 2025-08-26 04:46:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f161ff8f-7f32-3b0e-a6cb-9a4a324e29f4 | -11.55089 | -50.4639 | 2025-08-26 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ab16d490-4926-314c-9f01-f4a48e8fe64a | -8.8596 | -62.44303 | 2025-08-26 04:46:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 2b15be5b-d01c-3a23-bbdc-ec7b179aa90e | -6.75998 | -62.87096 | 2025-08-26 04:46:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 91e080df-5227-307f-9342-f7365ce6431b | -14.71751 | -45.38618 | 2025-08-26 04:46:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6c4f2790-bfa5-3fec-91d6-33613eabcbcd | -13.05959 | -46.3206 | 2025-08-26 04:46:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 70357f26-befd-3e8e-88a3-e7a560d2f9d2 | -8.56419 | -63.93045 | 2025-08-26 04:46:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4d85ae55-bcde-32ce-a1e0-abc058c68662 | -9.18432 | -59.53043 | 2025-08-26 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 0058621d-414a-383b-9f4d-2799983f2213 | -14.24612 | -48.04476 | 2025-08-26 04:46:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 192a245c-1865-369a-b02c-d9eb869d9200 | -11.55696 | -52.10531 | 2025-08-26 04:46:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dc51f196-415b-3447-9fcf-c58108963e7f | -10.61304 | -54.89134 | 2025-08-26 04:46:00 | NOAA-20 | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2de77599-56b8-3ab8-8f34-84c6ee803a84 | -7.62269 | -61.03609 | 2025-08-26 04:46:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 8d949ffc-c06b-36b4-84e3-e9f9f4aa14f3 | -11.56635 | -52.11042 | 2025-08-26 04:46:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 9f4ad6d5-e415-3cab-b16f-c8776d79777a | -9.02942 | -65.73064 | 2025-08-26 04:46:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 47bb602c-cc8a-3cae-b69c-8e133ea8c4e8 | -8.59038 | -62.63777 | 2025-08-26 04:46:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d413ae78-c24d-353a-8d5a-c27b59de711e | -8.87285 | -62.4591 | 2025-08-26 04:46:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 83caf98b-5669-3290-80b6-f9211a1deae5 | -7.35148 | -59.66237 | 2025-08-26 04:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 037fc48e-3e0b-369c-a823-9dcc1ec20dda | -13.65599 | -46.8797 | 2025-08-26 04:46:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 212fbc0d-27a6-3c9a-a696-b028d023acfb | -9.17181 | -59.51705 | 2025-08-26 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 70e1f1d3-6e48-36e0-b99a-6d66638f1e7f | -9.62122 | -55.3592 | 2025-08-26 04:46:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 07e4dde9-598b-36cd-8db0-182127ce548f | -11.44605 | -47.29502 | 2025-08-26 04:46:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f32a5902-5892-3db1-80cd-30da13ad8516 | -15.16307 | -48.19806 | 2025-08-26 04:46:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0588d567-fbef-3da7-b0c3-3c6b0695965a | -16.31883 | -43.62053 | 2025-08-26 04:46:00 | NOAA-20 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a45f9c2c-c37b-3541-a482-81db79739693 | -9.18551 | -59.44677 | 2025-08-26 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 2bcd2245-2aa9-3ef3-8385-ae7704e72965 | -9.70247 | -57.87883 | 2025-08-26 04:46:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b6571e3f-0afc-3d64-9fb5-e7136613580b | -11.81252 | -54.50187 | 2025-08-26 04:46:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c3b51206-8533-3072-a0ae-4f0deb82418d | -9.19868 | -60.92545 | 2025-08-26 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b9dafbf5-93f7-3f15-a90a-2f81d21218b5 | -8.63398 | -62.64852 | 2025-08-26 04:46:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| af5136b3-7039-35f4-9af8-88c294b45dbf | -11.30436 | -55.11444 | 2025-08-26 04:46:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 14.3 |
| 9dadc6b1-7dfb-3fc4-a367-0f3cd1015a08 | -9.07847 | -62.67226 | 2025-08-26 04:46:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0731fbd3-b459-3740-a711-0d85adad22ba | -13.83882 | -46.69809 | 2025-08-26 04:46:00 | NOAA-20 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9f54ab16-1620-3dd7-880c-99837f33adca | -9.04629 | -49.55998 | 2025-08-26 04:46:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7e07f25e-873f-37b4-a383-8116c290e861 | -8.9153 | -62.42743 | 2025-08-26 04:46:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fc7e1f2f-b7f1-38f6-a3c3-149e7d283441 | -11.54041 | -52.12423 | 2025-08-26 04:46:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 126.5 |
| 5709befd-7e65-3f83-9ad9-d1a30e9d92c1 | -13.58124 | -48.19724 | 2025-08-26 04:46:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 12.0 |
| c2a69140-caf6-3085-a6e6-8c0a02fd0c5a | -14.40568 | -53.39802 | 2025-08-26 04:46:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 71e1cf73-2483-37ad-8def-206b4f12e3e5 | -13.65784 | -46.8978 | 2025-08-26 04:46:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fd77fe86-9fd0-3da5-aad4-b353b18f8d0e | -7.35044 | -59.66831 | 2025-08-26 04:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| af7f7a18-945f-3865-bfcc-268b95db02c6 | -12.94116 | -46.33675 | 2025-08-26 04:46:00 | NOAA-20 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e5f520b9-3779-3b98-ae02-0e2614ec7bab | -8.85802 | -62.45162 | 2025-08-26 04:46:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 9fa2d0bd-3c35-3eed-9aec-468e5fd9a481 | -11.54537 | -52.11424 | 2025-08-26 04:46:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7fb48e68-39de-3837-937f-bc94c4bdf3e7 | -7.53589 | -61.38341 | 2025-08-26 04:46:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 23af8f3b-ff28-3163-b4ea-87af74a25d10 | -13.6554 | -46.88404 | 2025-08-26 04:46:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 7e04e896-d560-3a81-8126-1f0ace6a9ac4 | -7.3964 | -64.35368 | 2025-08-26 04:46:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 45eca169-a859-35b9-8184-99803f8718c6 | -6.76494 | -59.66874 | 2025-08-26 04:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 55470bb1-81a6-33f6-aad4-df233e5facaf | -11.56304 | -52.10989 | 2025-08-26 04:46:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f937544f-bc4b-3c03-b63c-78c592276841 | -11.5542 | -52.10126 | 2025-08-26 04:46:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c86f665a-f49c-36be-ad2c-26442391b222 | -9.17854 | -59.53482 | 2025-08-26 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 9256684a-951a-3bb1-b85e-908b32fdfd91 | -9.2598 | -59.7945 | 2025-08-26 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a1596b32-4944-3454-96cb-fd3e33e56ee9 | -13.49626 | -46.88317 | 2025-08-26 04:46:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f3397ce8-a883-31a8-a694-3a8a146feb71 | -9.19399 | -59.50464 | 2025-08-26 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 098ed629-7947-3b18-8507-fb9ab688bb10 | -9.0024 | -65.4001 | 2025-08-26 04:46:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| c2b0687c-648c-3b14-9790-e9b9a02eca4b | -9.16692 | -59.54377 | 2025-08-26 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| e18afb07-101e-32a9-ab2f-972432133c94 | -12.41197 | -46.49789 | 2025-08-26 04:46:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b4de5a4d-34d5-3001-bed2-85cc002eb81c | -11.25249 | -44.983 | 2025-08-26 04:46:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cfcd6e54-bac3-3f89-9ad2-c081526892ba | -13.41749 | -46.92354 | 2025-08-26 04:46:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 773525bf-15a0-3333-8ece-d89ae1e07d01 | -9.19108 | -59.52068 | 2025-08-26 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8ca7d735-571c-3107-803b-aabdf5e8b093 | -9.18422 | -60.79631 | 2025-08-26 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6746f5c1-a7bb-36a0-91f7-722fca1016e8 | -10.53698 | -46.80194 | 2025-08-26 04:46:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 24.1 |
| f50194cb-c612-3adc-addb-a12640fc846f | -12.02741 | -49.70845 | 2025-08-26 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 335edb8b-ceb8-3ceb-a869-426d396064b2 | -9.16502 | -59.52689 | 2025-08-26 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| b63b34b2-f3e6-302d-a81c-298b079617e2 | -6.91557 | -59.36296 | 2025-08-26 04:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e5bd7586-d851-3c6d-a7fc-735021f797d5 | -9.6931 | -48.34042 | 2025-08-26 04:46:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ec1c341f-c6f3-3e1c-8973-ab73b9b94f40 | -6.91518 | -59.36085 | 2025-08-26 04:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 58af691c-8774-300c-adda-422aefe16581 | -11.54648 | -52.10722 | 2025-08-26 04:46:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ef2c2d1f-31a1-3c0f-a581-44d930e1921b | -6.76392 | -59.67468 | 2025-08-26 04:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 782ccf24-3068-3bb1-b9a1-f420f40ea751 | -7.52901 | -63.38306 | 2025-08-26 04:46:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4440e17b-38a1-3c0b-80a4-44f346a96052 | -7.4807 | -61.3502 | 2025-08-26 04:46:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1c8614bf-76aa-3a39-97a5-8c78a4b4f76a | -9.17371 | -59.53393 | 2025-08-26 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| a0a195fc-11c1-32f3-bb36-1f575e613347 | -8.5486 | -62.62962 | 2025-08-26 04:46:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 248a789f-da49-30e7-8e99-e17e8c5d21cd | -13.59676 | -48.19981 | 2025-08-26 04:46:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| dd072bd5-f6fe-3d2f-b9fa-111fe14dfc69 | -10.743 | -47.08007 | 2025-08-26 04:46:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8933a2bc-8782-3572-bb11-cc3a077ff6c3 | -8.56653 | -62.63298 | 2025-08-26 04:46:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4b3f11a0-5267-3412-9bef-29ec93ecbb2b | -9.17885 | -59.45647 | 2025-08-26 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 19.5 |
| 343a46ce-ddb9-3387-ab11-a152cd1242a5 | -9.18301 | -60.80282 | 2025-08-26 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b2abc7f1-e033-39a4-9271-a8c1b5da017c | -15.06808 | -48.5465 | 2025-08-26 04:46:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7df53115-ac0a-3f49-ab93-29cf63b234ea | -6.81474 | -58.96732 | 2025-08-26 04:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 18969c48-e17d-3374-893a-60676742c9ae | -7.28928 | -59.66671 | 2025-08-26 04:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 987e0ee4-532a-3b88-84c6-f934193e0a80 | -9.23197 | -60.91594 | 2025-08-26 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 21c2ba3f-a10e-3a2f-9666-3e2b6d77e3ea | -9.16231 | -59.4604 | 2025-08-26 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 9193a7da-da25-380b-9891-28656f931594 | -10.53906 | -46.78739 | 2025-08-26 04:46:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 6b4ea021-5c06-3af2-9d5b-579fd8f227f3 | -16.3184 | -43.62423 | 2025-08-26 04:46:00 | NOAA-20 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a28a31dc-10e1-3000-bba4-b4c99365310d | -11.52937 | -52.12965 | 2025-08-26 04:46:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 15.2 |
| c0adc0c5-091c-3c12-b695-200900439009 | -7.38733 | -64.35464 | 2025-08-26 04:46:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 2ddcbd28-d98f-3619-87b7-295041adc82b | -15.32332 | -53.8424 | 2025-08-26 04:46:00 | NOAA-20 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 159bf827-6429-3eba-8576-8b31becf6026 | -10.39847 | -57.70228 | 2025-08-26 04:46:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 60d019e8-7802-3101-a4a6-d99b8e3dbeb8 | -8.54527 | -62.64745 | 2025-08-26 04:46:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f33db5a9-cf1c-36cf-bf65-cfa929d6c997 | -13.44292 | -46.99502 | 2025-08-26 04:46:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 36574a5a-bb23-37bb-be2e-16337c2aa5ac | -14.24751 | -53.04682 | 2025-08-26 04:46:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1cd7f318-796e-361b-9fa8-293af878c33d | -12.07889 | -46.63311 | 2025-08-26 04:46:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 74f03380-58e2-3880-afab-38d02a39f04c | -15.05444 | -48.70626 | 2025-08-26 04:46:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d276bc54-fe26-38c4-86d6-aedb9413dbcc | -8.35225 | -62.93433 | 2025-08-26 04:46:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 237b372b-e346-3025-b016-4f6fd28f4e5f | -9.26974 | -56.91426 | 2025-08-26 04:46:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 0b6893f8-bdc0-3967-9a04-4404b3711f16 | -9.02092 | -65.73627 | 2025-08-26 04:46:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8d516401-8e01-3350-8897-ccaab18fc3cb | -14.3626 | -51.91262 | 2025-08-26 04:46:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| daf25837-a4b1-38ec-b5b1-6feb0ac97042 | -13.16611 | -45.29354 | 2025-08-26 04:46:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 6.9 |
| c5425f95-5437-3d32-8600-c888fa915096 | -6.81585 | -59.43003 | 2025-08-26 04:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c71d75db-19f5-3803-b672-08b34de9d3b9 | -11.52716 | -52.12209 | 2025-08-26 04:46:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a54c31ec-15d0-3e51-b6cb-b39b91161492 | -9.23811 | -60.91934 | 2025-08-26 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d0c88f10-de07-3168-bd63-97903aade13f | -8.97748 | -65.41611 | 2025-08-26 04:46:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |


[Clique aqui para ver as próximas entradas](README60.md)
