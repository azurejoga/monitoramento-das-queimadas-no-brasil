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

## Dados Diários - Página 117

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 95a87949-e3f9-3d7c-bced-2a2c73b8651f | -3.05789 | -54.15296 | 2026-10-07 05:59:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e4e6f2b1-b922-3bac-aa63-d82761ac984c | -3.09607 | -54.28592 | 2026-10-07 05:59:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 5229ad65-c230-3fca-9fb7-7b782af39574 | -3.1697 | -58.63404 | 2026-10-07 05:59:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0bb78e50-3963-3ee4-bbea-5a951a221c1b | -3.66456 | -60.62017 | 2026-10-07 05:59:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| f8fc2303-57d2-34d9-9355-ea4c8dd12534 | -3.08591 | -54.30527 | 2026-10-07 05:59:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 747e81d1-e499-3ed9-b06a-c384ab8b9ac6 | -3.43862 | -56.93774 | 2026-10-07 05:59:00 | NOAA-20 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 06dbea4f-3df9-3751-930f-b5a3d6dba019 | -3.58856 | -54.56081 | 2026-10-07 05:59:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 836e84f1-459e-3e5c-b9cf-aa7210a4dabd | -2.77417 | -54.10216 | 2026-10-07 05:59:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 7d05ffd8-f9cf-3063-b9c2-0de9e367ef1f | -3.05365 | -54.23065 | 2026-10-07 05:59:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 46b7a80a-d9c2-35f5-8a62-231daad14753 | -2.77715 | -54.08149 | 2026-10-07 05:59:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 5e3adf98-7769-33cb-99d2-544d5b73328e | 0.44724 | -60.5345 | 2026-10-07 05:59:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a0a08aa5-c45a-33d2-bbbf-3662ba0469d0 | -2.48944 | -58.06324 | 2026-10-07 05:59:00 | NOAA-20 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d2c66d06-7a6e-32dd-a7dd-ed98d6c7fa20 | -1.80348 | -57.10615 | 2026-10-07 05:59:00 | NOAA-20 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 7c610e74-f77e-30d7-9a4e-0ba9da8b7541 | -2.8759 | -54.15224 | 2026-10-07 05:59:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d824098a-ecd9-3c5f-85c9-fa8633506e0d | -2.94659 | -54.07097 | 2026-10-07 05:59:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 15.1 |
| ced66cd6-a334-3ec3-be97-cdecd13b33a2 | -2.7034 | -59.80478 | 2026-10-07 05:59:00 | NOAA-20 | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0d41211a-b780-385d-aed2-476a3eba2ad9 | -1.79637 | -57.11824 | 2026-10-07 05:59:00 | NOAA-20 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 117fcd18-e37a-3016-871f-9b22db777599 | -3.50452 | -54.66003 | 2026-10-07 05:59:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3e18aa36-370f-398a-bbc3-0b39ab0c665d | -3.54599 | -59.48244 | 2026-10-07 05:59:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 843ec623-840c-32b6-a59d-067bef1751b4 | -2.86747 | -54.20829 | 2026-10-07 05:59:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 46cd000b-78c4-32c1-9c28-23ca9a98026b | -3.47799 | -59.46534 | 2026-10-07 05:59:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8c96f536-2559-3af7-99cf-f5246dc4b24e | -3.5282 | -54.64407 | 2026-10-07 05:59:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 77c84d2f-ba65-3fe9-b04e-243b626e62c3 | -4.13561 | -54.92399 | 2026-10-07 05:59:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 90bb3574-d97f-3910-8c37-f51b6d17ee54 | -3.08258 | -54.26058 | 2026-10-07 05:59:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| fed14df2-530b-3c99-bdad-579cbfc91f0c | -3.76696 | -59.40479 | 2026-10-07 05:59:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2f19a9b3-b09c-3b4b-ac92-95002f4055bf | -3.05075 | -54.15196 | 2026-10-07 05:59:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 02866319-2ca2-3a50-b065-d3cd2d19cf06 | -3.08192 | -54.28379 | 2026-10-07 05:59:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 73ed6367-9c3f-304f-a824-1d34ca8db424 | -3.0755 | -54.25945 | 2026-10-07 05:59:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 072500b8-07dc-3cf6-8a06-27a594beaad3 | -2.97727 | -54.13352 | 2026-10-07 05:59:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 767299df-761c-3bd4-bf83-cdbf8aad316e | -3.094 | -54.29956 | 2026-10-07 05:59:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 3fe67015-c03f-3f6b-b3a8-3713aa11fe5a | -3.55625 | -59.48396 | 2026-10-07 05:59:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2f740114-12e4-33e6-88a9-4e0133891eb5 | -2.76257 | -54.10805 | 2026-10-07 05:59:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 30056782-1001-3bac-bf31-6915ac68d65b | -3.24507 | -56.80739 | 2026-10-07 05:59:00 | NOAA-20 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e99ea020-fa60-3a3f-b421-275d2992727a | -3.01616 | -54.13944 | 2026-10-07 05:59:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 619c875b-a3e9-3972-90d6-0d609bad6f1a | -1.28885 | -54.56423 | 2026-10-07 05:59:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 4dbae90d-8fc8-3488-a46c-33eb34d8da32 | -3.60061 | -54.57656 | 2026-10-07 05:59:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| eccba4b0-f439-388a-a48d-684a41f4aea2 | -3.58383 | -54.3145 | 2026-10-07 05:59:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| b870753d-9820-37eb-b05f-7357b6b402c6 | -3.50545 | -54.65363 | 2026-10-07 05:59:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 227c7b68-9486-34e8-a6ad-cb82520825b3 | -2.87157 | -54.21031 | 2026-10-07 05:59:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 2dc9923c-8b85-3186-80ca-0be4b48a60f7 | -2.94978 | -54.07293 | 2026-10-07 05:59:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| c50424d6-2558-35cc-8e42-329f8bef9682 | -3.96952 | -56.06048 | 2026-10-07 05:59:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1ae9093b-827b-379f-b1fc-46fdfb3dfbb3 | -2.30595 | -57.08544 | 2026-10-07 05:59:00 | NOAA-20 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4b727956-230c-3d98-8c2f-cc3c616a8070 | -2.75853 | -54.08636 | 2026-10-07 05:59:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 77888b7e-7655-3879-88fc-db38cbbe424c | -3.17458 | -58.63827 | 2026-10-07 05:59:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0d9945a8-27e7-3599-be91-b1a311724374 | -2.5996 | -59.3823 | 2026-10-07 05:59:00 | NOAA-20 | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 79c9a008-bd3d-3355-bffe-5b7941e4f3f9 | -3.09276 | -54.29034 | 2026-10-07 05:59:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| c7b0d00e-156d-396c-abb1-29a034ec5a47 | -3.09503 | -54.29276 | 2026-10-07 05:59:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 76d1ff79-26f3-39ad-8143-e2574f47c34c | -3.84728 | -55.98874 | 2026-10-07 05:59:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 86d49e6f-8d47-3a88-a566-bfb81afb15e5 | -3.17406 | -58.64169 | 2026-10-07 05:59:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1f84e156-8973-372a-8672-3e8aa144c589 | -3.54041 | -54.64851 | 2026-10-07 05:59:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 0d6da633-910a-3a2e-88e7-6d4bf657ce91 | -4.38379 | -59.90392 | 2026-10-07 05:59:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 80f69e37-ba6e-33aa-bb8a-3147a49668ca | -3.67504 | -55.94489 | 2026-10-07 05:59:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d515a646-0d4d-3dfc-92ae-32c047ac89e2 | -3.54041 | -59.48471 | 2026-10-07 05:59:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 255fb93a-f325-3f46-a7e0-19d60e7da842 | -3.06846 | -54.25808 | 2026-10-07 05:59:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b0389af4-400a-3f5a-8936-156c37ef812f | -3.73388 | -59.45028 | 2026-10-07 05:59:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b668cae2-e162-3084-a2d2-3a07f27bd185 | -3.68817 | -58.89449 | 2026-10-07 05:59:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 447e48d3-3e0b-3aa0-95a8-d9503c5ea756 | 1.98296 | -60.61462 | 2026-10-07 05:59:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 488ff024-d38c-32ea-8a48-7be94e16a25a | -3.68 | -55.95645 | 2026-10-07 05:59:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 77341b0d-3a24-3da3-956c-754d2ee7000d | -3.58787 | -54.31134 | 2026-10-07 05:59:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f7ca7eff-659c-3d68-8ff2-5ecb6175a22f | -3.05717 | -59.90879 | 2026-10-07 05:59:00 | NOAA-20 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| cd84267d-7881-3ec8-ac7e-6563e4be10d3 | -3.86017 | -55.99091 | 2026-10-07 05:59:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 2b5a2eeb-d658-3dad-996a-a8a5dd1a8f6b | -3.48913 | -59.5846 | 2026-10-07 05:59:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b29f06fd-db5e-3144-bb79-8c8f35265d08 | -3.48969 | -54.62209 | 2026-10-07 05:59:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7ed96887-e562-3dd5-bf1b-8306a835c7da | -3.61895 | -55.27991 | 2026-10-07 05:59:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 963ef22f-935f-3c9a-9b36-dc514341ede5 | -2.76361 | -54.10112 | 2026-10-07 05:59:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 14.1 |
| f15f9cc9-eda0-343d-80f1-00aa5459aa37 | -4.15818 | -55.1595 | 2026-10-07 05:59:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 1df93284-d23a-3a97-ba8e-ac1489a187ba | -2.76152 | -54.11499 | 2026-10-07 05:59:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| a252e7a8-3aa9-3dca-85d0-f2f50868322b | -3.09177 | -54.29716 | 2026-10-07 05:59:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 7f15eb01-7318-303e-badb-94d9fb82ce60 | -3.98742 | -56.26206 | 2026-10-07 05:59:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 735cdb56-0c30-30d5-b23c-7423e5b7ca7f | -3.34217 | -59.479 | 2026-10-07 05:59:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0813e32b-1b02-3d37-939b-c6d7923a3310 | -2.95083 | -54.06585 | 2026-10-07 05:59:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| e3f67e04-bce7-3fc6-8525-f071d2bd9a0e | -3.5888 | -54.30478 | 2026-10-07 05:59:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 78570369-84bf-33cd-b7fa-1d49d9a03c56 | -3.37757 | -58.19471 | 2026-10-07 05:59:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 54c31526-7fcb-360d-8e1d-a1a23db1f09c | -2.85003 | -59.11278 | 2026-10-07 05:59:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4ef682cb-a2b0-3a7e-93cb-a02c62d74524 | -3.53996 | -59.48774 | 2026-10-07 05:59:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e683a771-6c90-36b7-b369-6e657bc0a2ab | -3.99597 | -56.24782 | 2026-10-07 05:59:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 227a3379-9c1a-3b4c-9f4a-1fac4f461d94 | -3.84805 | -55.98349 | 2026-10-07 05:59:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 12.7 |
| f2f770a9-263f-3f3a-b5ac-837bed0013a0 | -2.76464 | -54.09425 | 2026-10-07 05:59:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 14.1 |
| acbad772-059b-3c7e-ad54-77e8a9b998fe | -3.47708 | -59.47137 | 2026-10-07 05:59:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9ef14e7d-323e-347e-888a-644e292e34cd | -3.39136 | -59.52021 | 2026-10-07 05:59:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e62d8702-bfdc-3156-89ec-63d497aa3dd5 | -3.10978 | -54.17254 | 2026-10-07 05:59:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3e534537-86f8-394e-89d4-89c932fd607c | -3.73993 | -59.4449 | 2026-10-07 05:59:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5e7abc76-9435-39bd-a4dd-29dd6008eb6a | -3.08693 | -54.29852 | 2026-10-07 05:59:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 55b4cc37-ce8d-3cfc-a4e1-452f0fc3ce76 | -2.13561 | -54.79926 | 2026-10-07 05:59:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 866a0805-3e9a-3e58-a486-394edc4b161f | -3.10083 | -54.28452 | 2026-10-07 05:59:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 916d1ac3-22fe-392a-8ec0-6cfe91fbc281 | -3.98545 | -56.21828 | 2026-10-07 05:59:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 02105880-cf04-370e-9a99-6d7b05d57916 | -4.15042 | -55.15709 | 2026-10-07 05:59:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7446447d-3975-3a8a-9a44-725d64a8a34f | -3.06944 | -54.25119 | 2026-10-07 05:59:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d0bed061-e208-3f92-a3ba-660f98963eda | -2.48888 | -58.06688 | 2026-10-07 05:59:00 | NOAA-20 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f02b1b85-7c6d-344f-bf70-f95e8f7b8294 | -3.59605 | -54.57195 | 2026-10-07 05:59:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d0f1205e-eed4-34da-bac0-9b952ddb2e58 | -3.56598 | -54.48476 | 2026-10-07 05:59:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6c7decd3-2eb7-3532-ba8c-1bd051ffcd3c | -3.49663 | -54.66532 | 2026-10-07 05:59:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f1665b4a-cdd6-3b4f-a55b-6f9e42d49cad | -3.6861 | -55.95493 | 2026-10-07 05:59:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0e83c5b7-1f64-314c-9862-e87f07cceffc | -4.15215 | -55.14545 | 2026-10-07 05:59:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 69604433-cded-3ea5-b5ba-046237cde226 | -3.08453 | -54.247 | 2026-10-07 05:59:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e608838e-0cb1-3649-9607-adff9e7b1b73 | -2.94258 | -54.12179 | 2026-10-07 05:59:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 32229560-1165-328b-969b-08329866f8e6 | -3.44009 | -56.93552 | 2026-10-07 05:59:00 | NOAA-20 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d00aff78-e6e5-356d-8b16-3565144959b0 | -3.07648 | -54.25264 | 2026-10-07 05:59:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 97e1ca0e-60f6-33e3-82d8-1306b6311cbf | -3.08401 | -54.26989 | 2026-10-07 05:59:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 66bac6bc-eae8-3a4d-b86c-797074881efe | -3.09965 | -54.16599 | 2026-10-07 05:59:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |


[Clique aqui para ver as próximas entradas](README118.md)
