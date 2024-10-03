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

## Dados Diários - Página 138

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 438f6e4a-fcca-32ac-970a-eba8592b182b | -10.88935 | -63.90541 | 2024-10-03 04:51:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 4ada3cc6-a7b0-3a38-88af-1e65b2a5ef9e | -10.88872 | -63.90231 | 2024-10-03 04:51:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 95876e31-f938-3023-abf2-cca70bdaa882 | -10.88795 | -63.90642 | 2024-10-03 04:51:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 831f43c0-a2fa-3889-ad1f-ddb11c09d1e4 | -10.88501 | -63.89734 | 2024-10-03 04:51:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 32d738b7-6426-35e5-a6b2-2410a1009fe3 | -10.88355 | -63.89838 | 2024-10-03 04:51:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ea72b2a1-715e-3640-8c6b-41a04be140ba | -10.8741 | -63.89263 | 2024-10-03 04:51:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 04d0f3e6-de03-3f7e-b78a-04c0bfd8d042 | -10.87338 | -63.88965 | 2024-10-03 04:51:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 12b094ae-82cc-38f1-96dd-266323e84e3c | -10.87265 | -63.89352 | 2024-10-03 04:51:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 78ce55c9-ac9d-38a9-a660-8015d84b107e | -10.86838 | -63.88486 | 2024-10-03 04:51:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 763a72b9-6946-3a99-bb7a-a1e7962cfaaa | -10.86829 | -63.89206 | 2024-10-03 04:51:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 97e626b6-173d-3594-a937-807d9a9c5859 | -10.83922 | -64.19154 | 2024-10-03 04:51:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 621e75fd-03f2-3ea8-8aad-59222e5e86b1 | -10.83477 | -64.18813 | 2024-10-03 04:51:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 9.1 |
| c16177fb-95c5-330c-8253-59c17be2bad0 | -10.83421 | -64.18634 | 2024-10-03 04:51:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 6.3 |
| fb1344f6-6897-39aa-aca0-00fe2936f888 | -10.83401 | -64.19209 | 2024-10-03 04:51:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 9.1 |
| f6aebbe9-ac99-37d2-afb1-34278ce4e1cd | -10.83341 | -64.1904 | 2024-10-03 04:51:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 661202fc-2828-3895-b965-ca9115862691 | -10.83179 | -64.2038 | 2024-10-03 04:51:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ddcdb359-f096-38ac-b811-2166ed38b1b1 | -10.83108 | -64.20222 | 2024-10-03 04:51:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d070c307-fb6f-3c8b-96eb-04dd96dd38cc | -10.83101 | -64.20792 | 2024-10-03 04:51:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 27c28507-ba21-386b-8076-a4489723d993 | -10.8303 | -64.20619 | 2024-10-03 04:51:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9cfa4e28-b322-31c9-aa58-ad42a11e3a08 | -11.45449 | -63.33455 | 2024-10-03 04:51:00 | NPP-375D | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e8f9e9e6-3715-3651-a366-7dfa8a9379a9 | -11.45378 | -63.3382 | 2024-10-03 04:51:00 | NPP-375D | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b3a3beb9-9143-3bea-ac03-3353cad75e90 | -11.00047 | -63.57336 | 2024-10-03 04:51:00 | NPP-375D | GOVERNADOR JORGE TEIXEIRA | RONDÔNIA | Brasil | 1101005 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4989f776-e158-3b95-8f72-e9b0a90ceb50 | -10.99498 | -63.57183 | 2024-10-03 04:51:00 | NPP-375D | GOVERNADOR JORGE TEIXEIRA | RONDÔNIA | Brasil | 1101005 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2f2451fa-2f2d-3a42-937b-51811fd955a1 | -10.99447 | -63.57449 | 2024-10-03 04:51:00 | NPP-375D | GOVERNADOR JORGE TEIXEIRA | RONDÔNIA | Brasil | 1101005 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 31952b7d-f0ba-334b-a9a4-ae62bdbec978 | -10.9893 | -63.57128 | 2024-10-03 04:51:00 | NPP-375D | GOVERNADOR JORGE TEIXEIRA | RONDÔNIA | Brasil | 1101005 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 55dcc803-b05b-313a-b5a2-43d69f749bc9 | -10.98879 | -63.57393 | 2024-10-03 04:51:00 | NPP-375D | GOVERNADOR JORGE TEIXEIRA | RONDÔNIA | Brasil | 1101005 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f934522f-2635-3de9-8a46-e927aa54fd3e | -7.46777 | -64.68014 | 2024-10-03 04:51:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a441e017-52d0-35d9-b40d-123bedd5d049 | -7.45999 | -64.44378 | 2024-10-03 04:51:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 38f2f85e-cdaf-38f3-b9bb-881af211bfcf | -7.45906 | -64.44868 | 2024-10-03 04:51:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e9ff5bd2-c7e4-37c7-95d6-7e1d2073ef09 | -7.4572 | -64.44275 | 2024-10-03 04:51:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| adfa598c-7070-3051-81c9-5472124b107d | -7.4563 | -64.44766 | 2024-10-03 04:51:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 88f3c426-19e5-3fcd-bd76-b42c70bb8e1f | -7.45375 | -64.44254 | 2024-10-03 04:51:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ce34e4c8-6b3d-341a-aa07-35dc5a23040b | -7.45096 | -64.44148 | 2024-10-03 04:51:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6f2924d8-d7c2-3763-af7c-d4f2cf230a0c | -7.38762 | -64.68034 | 2024-10-03 04:51:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b5af77ce-4bd4-3dd0-b248-399de71147d4 | -7.38128 | -64.67908 | 2024-10-03 04:51:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5a9c67e7-26cf-3f11-8523-f9ebd909e190 | -7.29698 | -64.66388 | 2024-10-03 04:51:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 240dcb3f-2c79-3500-8813-961b7d4b4f32 | -7.29245 | -64.66206 | 2024-10-03 04:51:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 3fcf65e7-911b-3a29-9a3b-d90f77d8f065 | -7.29158 | -64.65749 | 2024-10-03 04:51:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| de789e9d-a819-33ee-8649-ada8c593f33c | -7.29063 | -64.66267 | 2024-10-03 04:51:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4613a974-e5b8-3275-b00b-df940450dec8 | -9.24197 | -65.60056 | 2024-10-03 04:51:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c798d80f-9f40-3dde-a514-5a537057ae06 | -9.24091 | -65.60601 | 2024-10-03 04:51:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| df1a770d-e1a3-3ba5-8bc9-901dcaaf4c1f | -9.17825 | -65.55314 | 2024-10-03 04:51:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2e7561e5-382b-32cb-92e5-ba57811db727 | -9.1772 | -65.55863 | 2024-10-03 04:51:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| fe558898-a6d1-3337-8196-552fe917044e | -9.17703 | -65.55288 | 2024-10-03 04:51:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e14f95b1-80c3-3ce4-a6c2-e40a81e0c23e | -9.17595 | -65.55836 | 2024-10-03 04:51:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a92742c4-a0a6-3980-b02c-5bff5efccff8 | -9.04697 | -64.4447 | 2024-10-03 04:51:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 15009ff1-892f-32d7-884c-7197dedfae38 | -9.04662 | -64.44673 | 2024-10-03 04:51:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.4 |
| a8d383ad-50cd-3199-9d86-0038254a0dab | -9.0461 | -64.44934 | 2024-10-03 04:51:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2fe6d3db-41b1-35fe-b39c-14c7f243f4fb | -9.02344 | -64.46906 | 2024-10-03 04:51:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.8 |
| cf44de8b-b156-3676-ada2-4c25b2444b5f | -9.02256 | -64.47372 | 2024-10-03 04:51:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c8707b6a-18ee-3501-9d54-aed7c8d164de | -9.44432 | -64.54202 | 2024-10-03 04:51:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 14ee24f8-f220-3861-9102-1fefd4721562 | -9.44343 | -64.54668 | 2024-10-03 04:51:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 21291843-4089-3cd4-a94a-b4652ab355b2 | -9.4374 | -64.54523 | 2024-10-03 04:51:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f4a7249b-a982-3b78-af69-0213b6880527 | -9.43653 | -64.54978 | 2024-10-03 04:51:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d4834c57-b3ac-30ad-8c08-0fee2bd6634d | -9.43128 | -64.5442 | 2024-10-03 04:51:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a6f10ef5-1497-3fca-bf8f-84230e4bcf37 | -9.43039 | -64.54887 | 2024-10-03 04:51:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 42c3586e-d92d-32e3-b264-7dde794961c7 | -9.31161 | -65.3769 | 2024-10-03 04:51:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e928ba35-2000-374c-a8d9-212e6fbb00d1 | -9.30875 | -65.36158 | 2024-10-03 04:51:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 022173d8-9953-38af-9c1f-217a351f01ec | -9.30823 | -65.35971 | 2024-10-03 04:51:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 746b46a5-6c6a-3547-865b-b8831f54ec11 | -9.30769 | -65.36693 | 2024-10-03 04:51:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| c7157bda-ff2e-3f64-8d44-2fcd6b2d419a | -9.30719 | -65.36517 | 2024-10-03 04:51:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| fe8b4021-56a5-3ea7-8f73-3fa4011c573d | -9.30663 | -65.37227 | 2024-10-03 04:51:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 5b3dd360-307b-34d8-9611-0f2208c333b6 | -9.30618 | -65.37049 | 2024-10-03 04:51:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| b10eebe1-9f18-391a-8570-b135667f8647 | -9.30555 | -65.37772 | 2024-10-03 04:51:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 540771a3-6ad9-3300-b2b7-8f74dd4c1d70 | -9.30514 | -65.37593 | 2024-10-03 04:51:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 0fb13d5f-4087-3792-ad66-792e4160a015 | -9.30228 | -65.36061 | 2024-10-03 04:51:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| cbde3d0f-0121-385f-a688-5cfbc98dfe4a | -9.30178 | -65.35872 | 2024-10-03 04:51:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| a00a46c8-da6e-3906-a81f-0daaab860273 | -9.30124 | -65.36589 | 2024-10-03 04:51:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 1301dcc9-9d38-35d8-b355-9a0d59d4a963 | -9.30075 | -65.36407 | 2024-10-03 04:51:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 35ecd501-4849-3842-a785-b332d1d19bb7 | -9.2985 | -65.34112 | 2024-10-03 04:51:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f0e5685f-48f8-3bbb-8174-482d7eb482f6 | -9.29742 | -65.34675 | 2024-10-03 04:51:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cca663f3-5486-33e2-b1ac-40734928c294 | -8.74238 | -64.19118 | 2024-10-03 04:51:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4998ea37-310b-3f2a-855f-8cf4ba0affac | -8.73637 | -64.18996 | 2024-10-03 04:51:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f2b3ed06-a8d4-3e51-8a8f-3669da54c5bb | -9.99355 | -64.76714 | 2024-10-03 04:51:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| bab7e3a7-1116-3f55-8f95-6824cbf4a90e | -9.98744 | -64.76595 | 2024-10-03 04:51:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8d5618c5-1207-3c29-b321-c2cf5154f0cd | -9.98651 | -64.77072 | 2024-10-03 04:51:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8546e6ba-ae7e-3ebe-b397-0926a61f823a | -9.97541 | -64.76791 | 2024-10-03 04:51:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ba1fb0a7-04be-322f-a922-cfabfa2f69ee | -9.97451 | -64.77266 | 2024-10-03 04:51:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9e1b3d88-591a-3955-a1db-7929669cd37b | -9.97427 | -64.76838 | 2024-10-03 04:51:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 555eab8b-8c7b-38cf-9d53-1f82c958fe46 | -9.97334 | -64.77309 | 2024-10-03 04:51:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4111a49b-503d-3d2b-b934-cbcd9ecd2f6c | -9.9684 | -64.77143 | 2024-10-03 04:51:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 711eed7a-00a2-305b-94d0-43974a9cc051 | -9.96752 | -64.77604 | 2024-10-03 04:51:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a11ef102-9b51-3668-9463-896101acedd8 | -9.96723 | -64.77185 | 2024-10-03 04:51:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ca20b55a-d46d-3e5c-9145-f69fa55f255b | -9.96664 | -64.78068 | 2024-10-03 04:51:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 115fa737-454d-3a17-9327-7a43787fe049 | -9.96632 | -64.77647 | 2024-10-03 04:51:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0dd266a8-14f0-3c71-9652-041ecfcd79be | -9.96541 | -64.7811 | 2024-10-03 04:51:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.2 |
| eb344278-d303-3111-aae4-da783fa9eb4b | -9.96142 | -64.77475 | 2024-10-03 04:51:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e7cf04d5-5d41-313a-9c3d-d90435d239aa | -9.96054 | -64.77939 | 2024-10-03 04:51:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b3411bc9-74f1-35b1-9281-c87a64bb96d9 | -9.96022 | -64.7752 | 2024-10-03 04:51:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4e24e182-9831-31d8-b31e-9fc55aa375e6 | -9.95931 | -64.77984 | 2024-10-03 04:51:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 84787685-5eb1-3f29-ad5d-888e8a7f8f91 | -9.94912 | -64.9067 | 2024-10-03 04:51:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4c9eb907-232e-34b4-bcba-49c9c3c4c077 | -9.9482 | -64.91156 | 2024-10-03 04:51:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 083c5036-824b-3e39-9aff-5b73fa353d78 | -9.94799 | -64.90198 | 2024-10-03 04:51:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9ec8d6c4-5507-3aac-9e7b-714024ae6b85 | -9.94726 | -64.91651 | 2024-10-03 04:51:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4daa8c0e-7bcc-36d1-b9c7-5296ed0ac175 | -9.94703 | -64.90681 | 2024-10-03 04:51:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 446530d4-398a-3c97-95ea-f7ae6030524a | -9.94608 | -64.91163 | 2024-10-03 04:51:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 18fad6a8-aa6e-30cb-929d-1283c69dffba | -9.94511 | -64.91657 | 2024-10-03 04:51:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2fa1ecd8-89b5-3e15-a0d3-188af55c6a8f | -9.94296 | -64.90543 | 2024-10-03 04:51:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a6bb5d8e-3a80-3aba-a716-4eca53848430 | -9.94204 | -64.91026 | 2024-10-03 04:51:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e6a67e9c-dce7-3d49-af3a-8834644b810f | -9.94111 | -64.91515 | 2024-10-03 04:51:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |


[Clique aqui para ver as próximas entradas](README139.md)
