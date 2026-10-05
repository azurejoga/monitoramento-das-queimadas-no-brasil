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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ce959fd8-b1af-37e1-949a-282a5ba533eb | -3.17235 | -54.08199 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 300f0633-3bbe-3f9b-96de-ffb17b58910f | -6.82262 | -38.52935 | 2026-10-05 04:38:00 | NPP-375D | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 51a43379-31d8-3978-84f5-40a2e1eceb61 | -3.10949 | -53.75816 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 0b6933b4-dcfb-316a-b6e3-484ac4f698aa | -3.37302 | -54.10242 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3c153238-c811-3f1c-b8a4-9daad2ff88fe | -3.39203 | -52.23703 | 2026-10-05 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 996875e0-df4b-3e9b-8ee7-09fed4139a33 | -2.94418 | -54.12881 | 2026-10-05 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a6a1785a-4ecf-3b83-b9ca-d9eccf0c9763 | -2.8021 | -54.11215 | 2026-10-05 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a2f8fcb1-c195-35aa-b8ff-42144212ea2a | -3.10907 | -53.74255 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 61bac13e-05e7-3142-a5db-90c05b1dddf6 | -2.98071 | -54.10275 | 2026-10-05 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7623ae90-999b-3ffa-a4a7-3208c32c886b | -6.92776 | -43.68225 | 2026-10-05 04:38:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 2201e5d4-9433-3a64-b74a-56d6a908ffe4 | -2.90356 | -54.08107 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c8de00b0-4200-3ea5-b8d6-ba4d071ddc4d | -6.90711 | -43.67506 | 2026-10-05 04:38:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| af0e60a2-078b-3b48-968f-cac67b266b88 | -6.15766 | -43.63311 | 2026-10-05 04:38:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 299e5079-f66c-3b9a-913c-55b68d1e15a7 | -4.64613 | -46.31109 | 2026-10-05 04:38:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9610e2ec-19f5-318a-90bf-3cdefff8ecec | -4.46888 | -54.97243 | 2026-10-05 04:38:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8c06eeba-4a9e-31b5-a5c7-0653ba82b2c8 | -2.89993 | -54.13509 | 2026-10-05 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f4355532-0a10-34ad-ab3d-b4189bde5c2b | -2.89889 | -54.07707 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a3856ea6-3d5e-3a99-a0ad-b3f4f226dd06 | -3.1168 | -53.75892 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 34893a79-7f1f-390d-aba3-6f24a6e43ac7 | -2.90462 | -54.13911 | 2026-10-05 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 140e8e86-cb6c-32fe-adef-aa15d87e867b | -3.469 | -50.09734 | 2026-10-05 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 49a71c8d-c0ae-3985-8d26-c238228050fc | -2.80573 | -54.09021 | 2026-10-05 04:38:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 949019a3-21fb-3372-9499-469279625593 | -2.16101 | -53.6671 | 2026-10-05 04:38:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ea4c9e2d-2853-33e3-96d5-8502c6d99a86 | -6.61524 | -37.88419 | 2026-10-05 04:38:00 | NPP-375D | LAGOA | PARAÍBA | Brasil | 2508109 | 25 | 33 | nan | nan | nan | Caatinga | 0.5 |
| e9924f08-9c4b-35fe-a5f8-fc414c44d277 | -3.91408 | -49.70403 | 2026-10-05 04:38:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 35f33f3b-b9c1-36c9-9476-cc154f458204 | -6.91359 | -43.68013 | 2026-10-05 04:38:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 389806ac-968e-33ad-86d3-82491783077c | -2.81042 | -54.09422 | 2026-10-05 04:38:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 06c09cee-d3c3-314f-b186-2aa85f41c67f | -0.39546 | -52.04346 | 2026-10-05 04:38:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 557899c0-3c1f-309d-bb76-2172c7d3fb9b | -3.06697 | -54.1624 | 2026-10-05 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| f57dea42-063c-38c9-8587-ba7644e78a64 | -3.60692 | -50.97689 | 2026-10-05 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 02686e69-31c7-3431-8829-cecdde84a672 | -1.97892 | -54.4198 | 2026-10-05 04:38:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 50b51925-3323-3a1a-adab-628a47282a12 | -3.12948 | -53.71294 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| b7ae8cd7-a8ac-32c3-b297-6c643c7dd3bf | -3.09726 | -53.71951 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 00cc8366-2285-3e10-ab13-c960eee8717f | -3.15899 | -50.44727 | 2026-10-05 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 0d78642c-1d99-3fd3-9222-64e4ddee3658 | -3.07735 | -54.16435 | 2026-10-05 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 865002fc-21ae-3abb-85a7-be39ccb19203 | -3.84513 | -50.31623 | 2026-10-05 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 9fd06302-7079-3218-9898-c13c1edbf3bc | -1.61609 | -55.10877 | 2026-10-05 04:38:00 | NPP-375D | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6381562e-0887-3b96-9611-ab77ebb3051e | -3.71185 | -50.64614 | 2026-10-05 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 019f9ee0-8661-368a-b5c2-500ee42d2579 | -6.60869 | -37.89395 | 2026-10-05 04:38:00 | NPP-375D | LAGOA | PARAÍBA | Brasil | 2508109 | 25 | 33 | nan | nan | nan | Caatinga | 1.0 |
| a3636625-e98b-33e3-a8e6-f7d2b0866d66 | -2.59454 | -51.84937 | 2026-10-05 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 73affee5-05aa-3af6-9c62-8afd2ca4c086 | -2.94311 | -54.13505 | 2026-10-05 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f3c62906-65a4-3350-8e5b-6c6c8380f08a | -3.28187 | -50.40589 | 2026-10-05 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fb7d6cad-9fb0-3332-a898-52c65dc635cc | -3.6117 | -50.97381 | 2026-10-05 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5b94928b-c5b2-39fc-ba7a-b614c9194103 | -7.19176 | -44.31142 | 2026-10-05 04:38:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3d5390bb-57a7-3144-a988-12ba32514f6f | -3.12154 | -53.71809 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4e6dd2af-5fc1-3fba-95f4-b2d49ad059b2 | -4.11222 | -49.06611 | 2026-10-05 04:38:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c576d41f-4ca5-3c0f-a201-3df942817eb0 | -2.10033 | -48.22596 | 2026-10-05 04:38:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2093d677-4802-3311-8327-569c45ceb1f9 | -3.12091 | -53.76566 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 74eb566c-9c5e-3a7a-8065-c5c62b38fcbf | -4.28123 | -50.26738 | 2026-10-05 04:38:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c261d4c3-16b2-3a0b-8771-72ad1dd7327d | -2.81459 | -54.10136 | 2026-10-05 04:38:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 974d41fc-b469-37c7-997b-4a46b2d032b2 | -4.28516 | -50.26803 | 2026-10-05 04:38:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 04db2ab9-32b8-3d42-b48e-d5048caff801 | -3.26589 | -42.53902 | 2026-10-05 04:38:00 | NPP-375D | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 42dd1125-cc4e-3b4c-bd97-dc4dc2c2729c | -3.28126 | -50.02225 | 2026-10-05 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 67e6460b-7023-3ea1-99ac-1799e9ccacde | -6.2024 | -52.83311 | 2026-10-05 04:38:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 93281492-bbb3-3264-b48f-3cfd1f05f1e9 | -2.81983 | -54.13471 | 2026-10-05 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 488b040c-dc12-3a3e-b80a-821d5f4a715a | -3.37761 | -54.09824 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bf5b400b-d3cf-3498-a1ef-f832bf8c8224 | -2.9072 | -54.09135 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 8552b258-919c-384e-bd36-678b01452c4c | -6.91239 | -43.68808 | 2026-10-05 04:38:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fae84b37-7991-380d-8e74-411d621805b7 | -2.75736 | -45.54704 | 2026-10-05 04:38:00 | NPP-375D | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 86cbc306-bb2a-3e89-8a2b-c9226b7c49be | -3.9685 | -53.46492 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6b55a24e-46da-32ba-99a8-623e68b627a6 | -2.97656 | -54.09569 | 2026-10-05 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c9ac9955-bffc-3ad3-9343-e249d2954870 | -4.11448 | -49.07526 | 2026-10-05 04:38:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6032d4ac-14f3-3f1b-9d93-aea429ac4ff5 | -3.07633 | -54.17043 | 2026-10-05 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 20.8 |
| dac87b42-13bf-3b1f-bdf0-08e4b32e5b4e | -7.19233 | -44.30769 | 2026-10-05 04:38:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3f96a1e1-34e1-3b83-a199-f04ff1abe6e5 | -2.81045 | -54.12652 | 2026-10-05 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 24ff89b6-f12f-3c74-94c6-56e3b67c17a6 | -6.20764 | -45.40359 | 2026-10-05 04:38:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0936db45-5d69-3e29-a5cb-9c5e73b9f6be | -3.12663 | -53.73048 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0997f776-addc-3898-b213-bcca8530c788 | -3.11556 | -53.73463 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 558c177a-6a7f-368a-ae3d-7cd5bfa6d608 | -4.92924 | -48.40184 | 2026-10-05 04:38:00 | NPP-375D | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0cd0e1b2-c56f-328f-ad9d-85d52e46e288 | -2.93898 | -54.12789 | 2026-10-05 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 330172be-298b-31e4-aecc-d0d83e4bef53 | -2.93949 | -54.12254 | 2026-10-05 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 73c9495c-2fd7-34b8-958d-acb1db498782 | -2.76069 | -45.54757 | 2026-10-05 04:38:00 | NPP-375D | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c52182cb-11ca-3fd3-a1e6-8f60df4cfff6 | -6.05514 | -53.47822 | 2026-10-05 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4d74c9c5-7a07-3b76-a9a9-49e977380ae1 | -3.10763 | -53.75134 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0d05e681-e9e4-30cb-9c6b-056817db52e1 | -3.88591 | -55.80423 | 2026-10-05 04:38:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 033a0ff6-ba0e-3624-89e0-6346446a3f91 | -3.87384 | -55.80575 | 2026-10-05 04:38:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 70f842d6-bb90-3cb7-bc97-845a2f37c907 | -3.11405 | -53.76194 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 915d8f00-a94c-3116-8a11-19801a3e5f1a | -3.32094 | -53.85514 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 26dbfb13-60c1-3faa-aff8-9d7e49169eb6 | -2.8094 | -54.13286 | 2026-10-05 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 709c8883-909f-3ba7-a7ff-30263eb92e1a | -2.97551 | -54.10189 | 2026-10-05 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 29fe5f43-8803-3390-916e-792e648031bc | -2.91764 | -54.12516 | 2026-10-05 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4aef671e-e6d1-3bba-9c40-aba338be5fa5 | -2.99085 | -51.04769 | 2026-10-05 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 08bff124-119f-3ee1-8fb6-34f1e75de91b | -4.11081 | -49.07468 | 2026-10-05 04:38:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d940bb47-b3cb-3556-8624-95d6c92893b8 | -4.29936 | -50.78513 | 2026-10-05 04:38:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ca3b6292-218a-3936-b075-f0e2061f1e65 | -3.30812 | -53.83778 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a6162c5e-cc14-3793-a3e3-71e177a706a9 | -2.98649 | -54.03691 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 960b7549-3515-3975-83a1-f113e3a4c146 | -1.55702 | -54.79997 | 2026-10-05 04:38:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9dce30a8-4c70-3fdf-a796-86d18f62e963 | -7.89478 | -44.18823 | 2026-10-05 04:38:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| db3c4a99-3c09-3a21-8c55-6594d793f010 | -3.10667 | -53.75721 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| a57fad1e-7f10-3ceb-a2cb-fb68aded2f65 | -3.51059 | -54.61155 | 2026-10-05 04:38:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1045abf6-bff4-3a4c-9b72-4ac0de3da79b | -3.50586 | -54.62104 | 2026-10-05 04:38:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e1cef420-e64b-3eba-b95f-03599601fb12 | -2.79166 | -54.11045 | 2026-10-05 04:38:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f0b73562-73c8-397f-9516-624ef1d9fc3d | -2.79948 | -54.0956 | 2026-10-05 04:38:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 597cd25c-d68a-33c3-a645-c25dcf205488 | -3.04532 | -54.22648 | 2026-10-05 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 19430b7a-899c-3b6a-8176-5b6efc90291b | -6.05989 | -53.47897 | 2026-10-05 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 03200b12-82de-39b9-b076-aeb2fd43663f | -4.11744 | -49.08018 | 2026-10-05 04:38:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9c9e4415-5555-31e3-b68a-0210d0fc56fa | -6.91065 | -43.67559 | 2026-10-05 04:38:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 491a6cd3-269a-36d3-9208-ce3f018de886 | -3.8839 | -55.8159 | 2026-10-05 04:38:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 817ed6eb-1962-37e8-9df5-fe85c0d10cda | -3.37404 | -54.09655 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 73bbb490-b0da-37bf-b147-0f5c013fe3e5 | -3.84429 | -50.3214 | 2026-10-05 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 095bbb47-0143-344e-92d0-3fd32f5f9132 | -1.1938 | -53.39038 | 2026-10-05 04:38:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README24.md)
