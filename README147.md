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

## Dados Diários - Página 147

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f39d6534-61ff-3023-990b-b0d2a0889679 | -3.33069 | -58.16629 | 2026-10-08 05:23:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 73938421-5f19-310b-95a3-e0c690e1f7e8 | -6.0718 | -59.88162 | 2026-10-08 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 877a3edb-05ee-3cb1-8834-afaae83132e7 | -3.53187 | -54.67398 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 11cf207f-1e3a-38c2-b338-61a3c7122e0e | -7.19212 | -55.12746 | 2026-10-08 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 5fbfd361-c8a4-37e8-8be3-c3d317f446bf | -3.773 | -56.79971 | 2026-10-08 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 67640273-bcfb-3404-be39-a885d035de92 | -1.106 | -54.16806 | 2026-10-08 05:23:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 593337da-a3c4-3025-8d39-ff89f831d603 | -2.96669 | -54.14387 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f3fc00ba-c95e-3737-beb4-12afca34dc78 | -2.99092 | -54.13184 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 44527369-4ef1-3210-b38c-b84a2d05efbd | -3.23564 | -53.88028 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1441c89f-bdcc-327e-856d-50fe8a15cda0 | -4.26965 | -54.87996 | 2026-10-08 05:23:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 962d0805-9d64-319a-8c9d-367e67e106ae | -3.26513 | -54.01311 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 607a2bad-f458-3fc2-82a7-c905a0dd1e48 | -7.1985 | -55.1325 | 2026-10-08 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 745a053a-b514-3d57-87a7-0ff913b491c0 | -10.23291 | -58.21893 | 2026-10-08 05:23:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f6871b66-3422-388f-ad3d-1e68d95d31f7 | -4.96202 | -55.12062 | 2026-10-08 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 214b7740-b6bc-3dc3-bba4-9d02042f6335 | -3.15745 | -54.10109 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 274098ac-9211-3099-a000-8dfa4d66582e | -3.26438 | -54.04104 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bb995872-8f81-3c55-b424-3a4577fd3ed7 | -3.71168 | -60.54554 | 2026-10-08 05:23:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 308191d0-34ea-3b4e-9a39-f5c285168a6d | -3.73363 | -54.65436 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c5fcc058-1fb6-3824-b410-ae5051f6cc76 | -1.82227 | -55.08828 | 2026-10-08 05:23:00 | NPP-375D | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e7cc1ab8-96d1-3661-8981-2f732ea51a5d | -3.71756 | -54.23024 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 29fa14cf-d816-3ad6-8513-077110391f05 | -3.61267 | -54.04791 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 61795380-9416-3387-a8d9-1df79cf2c4bd | -3.17095 | -50.59913 | 2026-10-08 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 18.6 |
| c575c288-4be1-3e68-a566-68d29bb2b5a6 | -3.26602 | -54.25928 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 43432a09-a614-391f-a8e9-a6b58f739c23 | -4.14208 | -54.02738 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e3d01103-dd04-3376-b4ba-2ae709f025b9 | -1.45476 | -55.24831 | 2026-10-08 05:23:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fa0b09fc-5b06-3b8d-96f3-7263012f5e5e | -3.58904 | -54.24405 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e6f9936a-36ae-3f41-8cb4-7035857fbfc7 | -12.20142 | -57.12611 | 2026-10-08 05:23:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a116bfa3-e8aa-3ea6-aebf-e71c04905151 | -2.93121 | -54.1188 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 99ba4f92-3f93-3393-b2e7-4205676c47db | -2.79432 | -54.07488 | 2026-10-08 05:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 23272ac9-f7e4-322b-bc21-d32363d7ebe4 | -3.01108 | -53.90749 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 83161198-e1fb-335f-8a91-62ca7cb1bc0c | -8.73007 | -45.15994 | 2026-10-08 05:23:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| c3cbf61a-632f-3b69-8fdd-ba0a1885abb0 | -4.51995 | -54.97876 | 2026-10-08 05:23:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cf687c6f-4f18-3954-91a6-20a38ed58a78 | -3.28061 | -54.07552 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 158b79a0-915c-3317-8671-8fba6c06d896 | -4.3016 | -60.95102 | 2026-10-08 05:23:00 | NPP-375D | BERURI | AMAZONAS | Brasil | 1300631 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2073cae3-caaf-3a6d-9649-7bc4bfd88164 | -4.92835 | -55.87073 | 2026-10-08 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3c20912b-0bac-315a-97cc-30be90f33a62 | -3.08151 | -54.26669 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2730ba5c-ed93-3a03-92a0-5eecaa97af87 | -3.32936 | -50.1787 | 2026-10-08 05:23:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 105cae5d-449d-3ee7-9e7f-bc8bf91701d5 | -5.29408 | -60.09116 | 2026-10-08 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0f5c653f-273e-331a-b7fe-2c657fa57b37 | -3.86048 | -55.99645 | 2026-10-08 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5364287a-aba5-3adb-acba-fcd403f73c5c | -3.01813 | -54.04884 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 85e1ede8-2ad0-3ce0-9fdc-a0507c64ddf6 | -3.54248 | -54.66743 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 4bed8477-2166-3770-8712-d424f43b535c | -3.22048 | -54.29902 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5b200d31-e2f4-3260-88a8-e9d871fbdead | -1.52332 | -54.52787 | 2026-10-08 05:23:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a335275d-57ea-3de7-8c1d-1d1d1e1a704c | -3.59388 | -54.56403 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e3670d12-8bcf-36cd-86b4-840cdfebf755 | -3.0446 | -53.9248 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ea801a1f-f59a-3db3-8afa-7eac11534ade | -1.28611 | -55.41512 | 2026-10-08 05:23:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c055b910-7996-3e08-86d6-0d5e232f88c2 | -3.16492 | -58.63271 | 2026-10-08 05:23:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b88002e1-e878-3a4a-8c28-427256fc3e28 | -3.20665 | -53.87979 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 92598a3a-2f75-3094-ab4b-eed1f403f3a8 | -7.2176 | -55.17102 | 2026-10-08 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 23dff41e-3aac-3d67-819b-6ac5680cce26 | -2.96805 | -54.1126 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 283fce2e-d7d5-36c8-ad7f-4b6d73d102b7 | -8.61454 | -67.02979 | 2026-10-08 05:23:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 8.5 |
| f08e4e63-ab15-3889-93d5-7d9f3104f26a | -8.59609 | -67.3081 | 2026-10-08 05:23:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a7a43c48-5165-3ae4-83c1-b356986ffe6c | -3.72167 | -54.2269 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 158882e2-e326-357c-8509-47979edae87b | -3.08315 | -54.3021 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 59badf89-a5b7-3332-839f-9e59e2332d3b | -3.59737 | -58.26754 | 2026-10-08 05:23:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| fa51c205-aa5a-3c75-ad76-b3da491d20d0 | -3.29055 | -54.08106 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 99d66143-dadc-3027-89c5-304bb7e250dd | -1.26882 | -55.39454 | 2026-10-08 05:23:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 38e6b888-487f-3d81-ab61-4f8a9a717e28 | -3.314 | -53.86289 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 062e3de5-5613-3154-8664-d7674a9b4605 | -8.61374 | -67.01888 | 2026-10-08 05:23:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 7c89bf25-2efb-3352-b483-582e7e512ce4 | -3.35606 | -59.502 | 2026-10-08 05:23:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 76bb9249-aa2c-3ae1-a774-178c20956523 | -3.67774 | -55.94652 | 2026-10-08 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| df5d90b3-c9d5-3f3c-9baf-8d070cd2e3dc | -1.29381 | -55.71151 | 2026-10-08 05:23:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 322b3702-7da0-3235-b602-7b3b05a32198 | -3.02532 | -54.1411 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0a75ec9d-9faa-35fc-ad18-3caa5c098b90 | -3.05996 | -53.91914 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e49ccbae-0a52-39b6-ba76-a3b0af0775b2 | -3.18895 | -50.56857 | 2026-10-08 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f605a08e-ac1b-38e9-bbf3-4e72fce5bd8f | -8.73155 | -45.14837 | 2026-10-08 05:23:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 30408f53-4dc4-3d6e-aa98-0f84f6adcf2f | -3.04843 | -57.48462 | 2026-10-08 05:23:00 | NPP-375D | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3c68b2a2-10a0-33eb-ba29-e6047b5f687d | -3.58899 | -54.68606 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 9c878ca3-c1e9-3407-a986-94db6e0dfc44 | -3.53793 | -59.40998 | 2026-10-08 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 626475b3-3f4c-3fd5-b164-0cc04d1698af | -3.63335 | -59.56844 | 2026-10-08 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 550ffc69-e993-3ad8-bf7e-ca7cdd5f3083 | -4.54108 | -59.92695 | 2026-10-08 05:23:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b9cb1a6d-ba58-30cd-b09b-96e7e99e28df | -3.96183 | -59.99972 | 2026-10-08 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 69b3839d-5b29-33a7-8f08-903a2ad912c2 | -3.05699 | -54.21302 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8e9f65fc-99ab-35ce-a969-fafb8444b366 | -2.84718 | -54.12648 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 17.1 |
| 324d595e-da94-3943-98ee-322a0c56061a | -1.45671 | -54.77279 | 2026-10-08 05:23:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6bf57786-6839-39e7-88f9-18364fd31cf1 | -3.5003 | -59.28118 | 2026-10-08 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a12b8247-2c5b-340a-8edd-dfe3c451feb4 | -3.27556 | -51.06598 | 2026-10-08 05:23:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 2396af09-3802-3612-ae5e-265fde0e5ff1 | -3.68442 | -55.94757 | 2026-10-08 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ed677d38-e89e-3b17-beed-6a6255c9eba8 | -3.03871 | -54.26095 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8cbba915-8435-31f1-95c7-83a92fdf71bb | -10.32513 | -64.51569 | 2026-10-08 05:23:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 524e07e0-2cfe-3c14-bbfd-0dfda6d676a8 | -3.00228 | -54.05833 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| d9e4302e-eed3-39ef-b8e9-37d0a0cd947b | -3.53942 | -59.47968 | 2026-10-08 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e27f6941-eced-3e07-a9a0-61dfb1f0da72 | -3.04813 | -53.92535 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 84d18533-1840-3064-9c6f-1d9adf36743e | -4.78319 | -55.72491 | 2026-10-08 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e33a344c-9abf-3c1c-b602-10dcdf07ccbd | -3.01952 | -54.13234 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7490c30c-1742-3a70-b615-2936be6ba67a | -3.9809 | -56.21493 | 2026-10-08 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 4753cb5a-6013-3803-ba9d-2780ac0713a5 | -4.21286 | -56.05139 | 2026-10-08 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d2c22303-439e-3086-bd94-446330a7fd26 | -3.16763 | -50.44732 | 2026-10-08 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| d2964305-5491-3825-871e-5bb89e3bfe37 | -3.01901 | -57.73403 | 2026-10-08 05:23:00 | NPP-375D | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 170945ae-ef6a-3960-9494-09b03b9dd483 | -4.86732 | -55.854 | 2026-10-08 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| eaf20f01-04bf-3e75-8089-3b724a1f10ed | -7.22477 | -55.12461 | 2026-10-08 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ff984904-766e-31f3-aac5-9b88bb8e4068 | -2.04023 | -54.48293 | 2026-10-08 05:23:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f6d6cf21-b273-319e-8556-e168847ad790 | -1.37638 | -56.89099 | 2026-10-08 05:23:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 068893f4-1da4-3de5-95cf-0e8b565fab02 | -3.59316 | -54.24071 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9380322b-3854-3a2f-905e-d2cab5d3cea5 | -3.8336 | -50.9891 | 2026-10-08 05:23:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 37d828d4-8b35-31fd-a233-e7982114a36b | -2.93174 | -58.30304 | 2026-10-08 05:23:00 | NPP-375D | SILVES | AMAZONAS | Brasil | 1304005 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fa83c779-2da2-3d8f-86cd-a338ade07c54 | -6.87671 | -55.59046 | 2026-10-08 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 443c0ed1-5349-3600-b156-80e68720bc1e | -7.38764 | -55.21519 | 2026-10-08 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1c9b1198-9590-399a-b908-7b1e9b0cb42c | -1.10885 | -54.17228 | 2026-10-08 05:23:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6f098ee2-972a-3870-acfb-ba93b2c3ce6b | -3.6532 | -55.50237 | 2026-10-08 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README148.md)
