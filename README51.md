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

## Dados Diários - Página 51

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 50a6b151-ae2d-3be1-887e-9af5dad97699 | -3.49178 | -50.37962 | 2026-09-15 05:16:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e63477c8-5710-3edd-bf48-5c23eb383b56 | -2.89209 | -50.41946 | 2026-09-15 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| db9491d3-64ca-3c72-99fb-712c22e76f2d | -2.96416 | -50.40811 | 2026-09-15 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 71f804c4-e334-3f26-80b7-67645b98bf8b | 2.31702 | -60.91982 | 2026-09-15 05:16:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 01bbb149-9acb-3bf3-ab34-66b936fb0d31 | -3.72698 | -61.7446 | 2026-09-15 05:16:00 | NOAA-21 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 8d2a06b6-9d64-384b-bdc3-d822ec9e148d | -2.68491 | -57.58543 | 2026-09-15 05:16:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| aabd7af3-ec49-3cda-aa7e-791438dd49ca | -3.46363 | -58.41642 | 2026-09-15 05:16:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9a1edc6c-d09e-3da1-bcd0-0611487244fa | -2.81919 | -51.33764 | 2026-09-15 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d82795e8-7b3a-33b2-aa97-831418f6045e | -2.90364 | -54.16493 | 2026-09-15 05:16:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 98faba80-5c4a-3c54-be94-83131f6ec033 | -3.54004 | -53.98832 | 2026-09-15 05:16:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 734d9f19-a1a8-3edc-822a-84d5244a0c09 | -3.09425 | -51.38073 | 2026-09-15 05:16:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1003ea8b-696d-3232-b3cf-506b70675895 | -3.351 | -59.83064 | 2026-09-15 05:16:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 972bea54-4b7c-3a2f-8eed-7cff3fd1a35c | -3.07784 | -51.20039 | 2026-09-15 05:16:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 887b93ce-c959-33f8-9582-8403e24bd458 | -2.89332 | -50.43026 | 2026-09-15 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 7cfaff32-bfd4-3506-9024-0e40eaee0e5b | -3.04034 | -59.16554 | 2026-09-15 05:16:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8f6118e9-abf6-36b8-8f86-484fcf4aa5f7 | -4.5556 | -50.46154 | 2026-09-15 05:16:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2e6b7acd-609b-31b4-8af0-a58b85e3f9f6 | -4.53328 | -54.91998 | 2026-09-15 05:16:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| e7e29d79-8da0-3bcf-8df1-905f15e7c1e7 | -2.96498 | -50.40261 | 2026-09-15 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f80be208-85e4-3e60-b88f-c6ecceff27ec | -4.56893 | -54.91141 | 2026-09-15 05:16:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d257ade8-d1f8-38fb-8b34-c668502280f9 | -3.42659 | -58.21656 | 2026-09-15 05:16:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4dad3765-9f6b-3ed7-8391-9c8016893b04 | -3.83326 | -55.86201 | 2026-09-15 05:16:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 83427ccd-8ceb-3696-8e4b-8dc22f21e444 | -2.66437 | -57.56452 | 2026-09-15 05:16:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 7.0 |
| e295a1e8-0c9d-3bd8-af01-55b67fe4faaf | -3.11098 | -61.09969 | 2026-09-15 05:16:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b9c29f96-234f-3ec5-bd0e-617f5e8206af | -3.37331 | -45.09458 | 2026-09-15 05:16:00 | NOAA-21 | CAJARI | MARANHÃO | Brasil | 2102507 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 9849f63c-1b90-378c-b548-05f3ea701851 | -2.91438 | -54.17141 | 2026-09-15 05:16:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| adbae7c6-38ab-378c-a205-54d3fd3791f2 | -2.89049 | -50.43048 | 2026-09-15 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| f2c8aedd-c87c-38f2-b82d-a1d4f95b4052 | -2.90602 | -50.42726 | 2026-09-15 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 6d9242d5-a532-3607-878d-5c4f248139a5 | -3.26147 | -54.51606 | 2026-09-15 05:16:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| a5a1a407-a6dd-325d-9667-eaed4343513a | -2.92156 | -50.42402 | 2026-09-15 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1b5cd0ef-f274-3ae7-91ba-c3cd9ba5b5e9 | -3.8775 | -52.05101 | 2026-09-15 05:16:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3a9da396-806d-3ba9-b5e2-c042aff3de8e | -5.29403 | -49.08848 | 2026-09-15 05:16:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f9e59a25-66f2-3b8e-9f0d-369749d216f6 | -3.55228 | -58.67635 | 2026-09-15 05:16:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| aea5296f-3408-3c54-97a7-ca025480a968 | -3.38227 | -50.39138 | 2026-09-15 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 54321019-e77f-309c-b2a5-9289f5bed19c | -3.35712 | -58.18473 | 2026-09-15 05:16:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 43140c09-19d0-3f6f-bf92-57036d2fe7db | -3.7421 | -61.74272 | 2026-09-15 05:16:00 | NOAA-21 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 495156d0-3e91-3815-b058-96409db9333b | -2.91086 | -50.39417 | 2026-09-15 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7db39dc0-79d0-3428-b1aa-e6684439f741 | -3.74348 | -61.74181 | 2026-09-15 05:16:00 | NOAA-21 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0e2d5b96-2817-3c05-8bf9-4e1ae7f4565d | -3.18508 | -61.11114 | 2026-09-15 05:16:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 93616f39-19db-385e-9feb-012ea2a31802 | -4.2999 | -49.10555 | 2026-09-15 05:16:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| ad686e40-1d3e-36aa-8ff4-3dd5020bddc3 | -2.82307 | -51.3431 | 2026-09-15 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7be69a40-f434-3bc6-90e8-7abd1f25e2ae | -2.69764 | -57.59094 | 2026-09-15 05:16:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 3b3ade0b-65aa-3e5f-9547-e5b35b74667f | -4.44852 | -55.0136 | 2026-09-15 05:16:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f07ec9ed-352b-3232-a78f-78088257a139 | 1.10309 | -60.51052 | 2026-09-15 05:16:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1fa2f7aa-da02-3632-bfcc-6ca134f6435e | -2.88841 | -50.42952 | 2026-09-15 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| e9ba98df-3893-3a26-9893-53091f36a40b | -4.53873 | -54.93447 | 2026-09-15 05:16:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| a565241b-ca8d-356b-bb5f-80d71e482515 | -3.54149 | -53.98506 | 2026-09-15 05:16:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 0977baa9-d0f2-3c2d-b35c-95cacc288ab7 | -5.00807 | -56.09059 | 2026-09-15 05:16:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 46d29a7f-0def-3ad3-81b5-ea2ac4859f70 | -3.33479 | -58.12849 | 2026-09-15 05:16:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d5470d67-c9ff-388b-a504-c9bc6d77750b | -3.42498 | -58.22687 | 2026-09-15 05:16:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b5df17c7-d583-3af6-bfdb-22bdcf29d312 | -3.31791 | -57.05387 | 2026-09-15 05:16:00 | NOAA-21 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 350fd8e1-8b22-398d-a633-3a5621301b36 | -4.51412 | -54.97151 | 2026-09-15 05:16:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| b06cf08b-0904-36c8-951e-d525b91bef72 | -3.07431 | -51.20395 | 2026-09-15 05:16:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 855f4c59-ea00-37f2-9bbc-88dd4e683856 | -3.64995 | -58.61765 | 2026-09-15 05:16:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ac855c91-999a-3219-a28c-39aeaad502c8 | -3.36957 | -57.70954 | 2026-09-15 05:16:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4021b014-6d8d-3004-93b2-bc4456504ecc | -2.91988 | -50.40127 | 2026-09-15 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| b184225c-6eab-3db5-baac-84c9dcbe8914 | -3.54844 | -58.67928 | 2026-09-15 05:16:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 527934ad-1ce6-3e15-af2f-77f866c4294b | -2.65305 | -57.50593 | 2026-09-15 05:16:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 482942b0-1f8d-3e55-8d1b-20d86c2b8669 | -3.86049 | -51.98022 | 2026-09-15 05:16:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| acc1d8f3-4868-3da8-baf9-c926b4f0a5d8 | -2.86543 | -49.6323 | 2026-09-15 05:16:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ea1e062e-da14-3f7f-a286-ef8e96e8f4dc | -2.8962 | -50.42573 | 2026-09-15 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| ad2048a2-6d99-32c2-a9af-bfa8c43c3944 | -3.16912 | -58.64805 | 2026-09-15 05:16:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f4bd9ea3-444d-3e52-9161-1d163d241e7d | -3.71965 | -58.86847 | 2026-09-15 05:16:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 487662c4-a5db-3977-b2f0-0c97dc6f3f40 | -2.897 | -50.42025 | 2026-09-15 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 0b8a917d-9dce-3d34-b276-bd05bdc9c5cd | -2.92318 | -50.41301 | 2026-09-15 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| ad1cc154-3556-3055-baa8-d1518a5ad400 | -2.96089 | -50.39631 | 2026-09-15 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b6bdf551-da14-3326-8151-a8dee76e9911 | -4.39233 | -55.20951 | 2026-09-15 05:16:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f0efe60f-14c7-30a6-bf4c-293b258fbf3a | -3.19003 | -61.12727 | 2026-09-15 05:16:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 231c8363-26ce-3581-8457-3dc938de5072 | -4.39296 | -55.20536 | 2026-09-15 05:16:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6a0c7ecd-6c8b-3ecf-98ce-a01b48b9e9a6 | -3.02206 | -53.86055 | 2026-09-15 05:16:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f1e93c06-b7c9-356d-9979-190d32e9c887 | -3.75858 | -57.4837 | 2026-09-15 05:16:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| f8dfccad-fbff-3627-855d-0d7c69c336ad | -1.22681 | -54.12526 | 2026-09-15 05:16:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d3f5c1ab-f55e-3b22-b13b-a1d2e8a328ea | -2.89459 | -50.43678 | 2026-09-15 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 845a53c1-6275-396f-8396-d68a14469267 | -2.69512 | -57.5195 | 2026-09-15 05:16:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 7.7 |
| f896167e-4bf3-368d-b590-cde41690d362 | 0.17522 | -51.47477 | 2026-09-15 05:16:00 | NOAA-21 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0a7aa321-dd34-312f-846b-49af31e1f2f7 | -3.88753 | -51.92067 | 2026-09-15 05:16:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b7ab55c2-7609-3e18-a0e6-15897397f2f1 | -2.95432 | -50.40659 | 2026-09-15 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9d7967e0-bf33-38fd-8815-d17eb2506299 | 2.3191 | -60.92053 | 2026-09-15 05:16:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d33a2fdb-4210-3350-a168-e237727aa9da | -5.4144 | -48.53149 | 2026-09-15 05:16:00 | NOAA-21 | ESPERANTINA | TOCANTINS | Brasil | 1707405 | 17 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0a084ced-b384-3de1-a63c-0e473a2ce371 | -3.5408 | -53.98342 | 2026-09-15 05:16:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 41f96663-9b69-3d06-aaa1-a33e055763cc | 0.95626 | -59.89475 | 2026-09-15 05:16:00 | NOAA-21 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c684b3bf-d617-3b98-bad0-ec7eae84327c | -2.91745 | -50.41777 | 2026-09-15 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 92e1d38d-f423-3ca0-a3a6-577461c51ea4 | -3.34932 | -59.8194 | 2026-09-15 05:16:00 | NOAA-21 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f1cc6797-60a1-3ecd-bc01-4e3e9faf204a | -3.27703 | -57.89024 | 2026-09-15 05:16:00 | NOAA-21 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 232aad6e-91ea-3ecc-94de-16f39705a326 | -3.2251 | -50.59106 | 2026-09-15 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 9372d923-cae5-3dc0-84d0-37f2f40e375b | -3.54392 | -53.99559 | 2026-09-15 05:16:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 21.1 |
| 646873c3-bee1-3f6f-8ea2-77065fe3d454 | -4.3736 | -55.0332 | 2026-09-15 05:16:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4f2c5477-f8a9-39fb-9ba2-1195dfe192fc | -3.54782 | -53.99615 | 2026-09-15 05:16:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 21.1 |
| 3c78354e-0954-366c-8d23-e4cd5ffed9d1 | -2.78422 | -58.1476 | 2026-09-15 05:16:00 | NOAA-21 | ITAPIRANGA | AMAZONAS | Brasil | 1302009 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 63ccc882-8d82-3222-812b-1758ebf4c453 | -2.65049 | -59.37314 | 2026-09-15 05:16:00 | NOAA-21 | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7d12c55c-77c2-3960-af70-a2e07d21b8bb | -2.78206 | -51.36575 | 2026-09-15 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2728d3dc-499d-3a80-86f1-5a2eefef97b6 | -3.0751 | -50.57298 | 2026-09-15 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4cff2204-869d-3c6b-a898-81edd242ba5b | -1.22535 | -54.13458 | 2026-09-15 05:16:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e0a55a8c-0e6a-31ef-8d1f-83b0cb570454 | -3.58586 | -58.54787 | 2026-09-15 05:16:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 366c9e1f-ca1f-3da1-9a86-fd6f5a033ee3 | -2.94858 | -50.41132 | 2026-09-15 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e05324e2-536b-3b86-ac7c-1d27b0c7b165 | -3.01622 | -51.20979 | 2026-09-15 05:16:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6c26f7ea-a38a-3641-b127-2f73b2cb5141 | -4.52516 | -54.92322 | 2026-09-15 05:16:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 74d83b10-fa6c-321c-946c-cd00e3ef6a0c | -3.57674 | -55.59711 | 2026-09-15 05:16:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 324619a3-e491-3a84-a892-8967eb4ee55e | -3.35989 | -58.18868 | 2026-09-15 05:16:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a7b88817-0f69-3527-a0f4-72d7a94f90e4 | -3.69766 | -58.87918 | 2026-09-15 05:16:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 823c2268-00f4-3840-b169-e6b2bffdd88a | -2.90031 | -50.43198 | 2026-09-15 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |


[Clique aqui para ver as próximas entradas](README52.md)
