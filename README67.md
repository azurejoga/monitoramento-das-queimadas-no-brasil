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

## Dados Diários - Página 67

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bfc775a3-c180-3a60-b83c-ef5a833055d8 | -3.07765 | -54.24647 | 2026-10-07 05:04:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3d34ffc4-abe4-3e03-850f-c89363237089 | -3.04824 | -53.91018 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| df035bde-1547-3107-a068-e8966cc1f232 | -3.77544 | -58.5246 | 2026-10-07 05:04:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 16b9d31d-6334-3ed1-a4bc-7f829d2f7913 | -8.69366 | -45.22227 | 2026-10-07 05:04:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c3a64c0c-499f-3f33-bce0-9a97ca622430 | -3.49964 | -54.63998 | 2026-10-07 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c6aadf40-f5ed-3d27-8473-53792fc4f0ac | -1.42211 | -53.23309 | 2026-10-07 05:04:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 56277084-55a5-3c73-b276-5f0dae285b39 | -3.21818 | -53.88546 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ff4ac9ec-2ad5-35ea-994f-f3fa1a76dc5e | -3.50187 | -54.64743 | 2026-10-07 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d172caff-905c-375a-8287-d59889a30116 | -3.52171 | -58.75415 | 2026-10-07 05:04:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9a31eb7b-533b-341c-9bc2-cfc74bd49d7f | -3.64814 | -55.27939 | 2026-10-07 05:04:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dd9a4f44-ec76-39f0-8655-d7f640fbe1ce | -3.24106 | -53.87074 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 033a322f-4084-3587-87c3-6479176b113a | -4.37319 | -54.75425 | 2026-10-07 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 498c4216-758f-3d7c-907b-b14d62429ae6 | -3.59633 | -54.56598 | 2026-10-07 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 24447a5c-d2d8-39e4-96d2-81069426a378 | -3.97176 | -55.8231 | 2026-10-07 05:04:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 59510f6f-a9ac-3359-804e-0dab1f472eba | -3.0495 | -54.20988 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1e2ae9c1-fa6b-3898-8ea0-5e5e31cbec2f | -1.46529 | -54.52661 | 2026-10-07 05:04:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8d236b4b-a87d-3ce2-ab3d-eb65bcff0940 | -1.10376 | -54.13925 | 2026-10-07 05:04:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1d0b18ae-af09-323e-b382-c5b3b9a09666 | -1.34052 | -55.45926 | 2026-10-07 05:04:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 300049dc-4954-3dcc-b994-af877ad161c3 | -3.66451 | -60.62374 | 2026-10-07 05:04:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2943d934-ab27-3c43-a04d-84cc7cd32825 | -3.18065 | -49.44963 | 2026-10-07 05:04:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cde988e7-8274-30e8-9505-786217d2ee14 | -3.0939 | -54.29548 | 2026-10-07 05:04:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| b66fb2f2-48ad-310e-9dd0-c625974c7994 | -4.9706 | -50.89946 | 2026-10-07 05:04:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 62fe341b-0e03-3106-b821-38d9df26d642 | -4.36597 | -43.91229 | 2026-10-07 05:04:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 19031487-3d91-3784-81ce-abbb719aeae3 | -6.32021 | -54.78977 | 2026-10-07 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e50e256a-eaf4-3c8a-bf08-0b1010c64b31 | -2.92573 | -54.13002 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c15d5c1c-3bbe-3153-b8fc-5b816f2e596e | -3.48163 | -55.43267 | 2026-10-07 05:04:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b468fa6f-0df1-3f2f-bc09-49530b9762c2 | -3.27496 | -54.02874 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 25006de2-f77e-3429-9f94-527079c999c3 | -3.96646 | -56.05536 | 2026-10-07 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6d6155cc-2456-3ca1-8612-568ef7216d72 | -3.07873 | -54.23948 | 2026-10-07 05:04:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0aa5ca0e-56bf-3aec-b646-8768f64b6d6f | -3.29558 | -54.02827 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| d3cb2766-ed12-3a62-815b-58dee6062873 | -3.05265 | -57.51779 | 2026-10-07 05:04:00 | NOAA-21 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ee417466-dd8c-3bc2-9fd0-fcd7e56e4798 | -1.12643 | -54.19219 | 2026-10-07 05:04:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8a81f130-77cd-3819-963b-b48de20160e9 | -1.42887 | -53.23412 | 2026-10-07 05:04:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a0376b24-37fe-3c24-b31f-6a1dfd404fa0 | -3.06794 | -54.17685 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 188d6879-e300-3a9f-b0f8-cea555ff5e53 | -5.23762 | -50.90929 | 2026-10-07 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9de5e3a1-8548-383c-b0e2-2cf0a6a99642 | -1.41195 | -55.41385 | 2026-10-07 05:04:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cb645ab1-1b36-38b6-8f53-a3c2b8ec9985 | -2.99595 | -54.11547 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 453fb58e-ee01-3dbf-a209-c02eb38788c2 | -3.30039 | -54.03608 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 88f75c82-bd4a-3ba4-955e-92b24b0ebde9 | -3.89419 | -59.327 | 2026-10-07 05:04:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 52e4ea78-1b03-33d3-94bb-1c50b81d1be8 | -3.8536 | -55.99111 | 2026-10-07 05:04:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d547d8cf-ebc2-38e8-a515-2922e028d7e6 | -3.29341 | -54.06415 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| c4467cb4-78d0-31a1-9abe-b96c2b6ea69f | -3.03855 | -54.25826 | 2026-10-07 05:04:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 924b5330-4abc-3454-ac1d-b4be3a37e165 | -3.18864 | -50.54699 | 2026-10-07 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 28a7015e-baf9-3d71-9fb7-b099ec4324b5 | -3.80523 | -51.03807 | 2026-10-07 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 159237f6-e78c-33e5-87a0-914dae73c188 | -3.10786 | -53.76968 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| cb269402-8471-3daf-a598-861f53af25f8 | -2.49056 | -56.82674 | 2026-10-07 05:04:00 | NOAA-21 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dfceb1a9-c4a2-3ef3-9023-baaabc00be1f | -1.68275 | -55.00966 | 2026-10-07 05:04:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d23ceb3a-ee78-36f8-8d6f-a21b238e42e3 | -0.05068 | -53.25378 | 2026-10-07 05:04:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| eed58cd9-27e4-39e3-a5be-d348139e1aa9 | -3.48148 | -50.08199 | 2026-10-07 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 15.0 |
| e5fbd22c-9fa3-375f-b9a7-45b738ccda2c | -2.87638 | -54.14038 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b0699484-52d7-30dc-a2ea-873238f2a583 | -3.99331 | -56.25125 | 2026-10-07 05:04:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6b557d36-2388-338e-a78d-c36072a76763 | -3.88882 | -55.83067 | 2026-10-07 05:04:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b81590ce-846c-3318-a2d2-737fd78ce2bd | -1.10268 | -54.14614 | 2026-10-07 05:04:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8af3409d-b6e7-3ec1-9fc7-90737e409fe3 | -3.29396 | -54.06062 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 03217ee8-2f78-3114-9d61-71f3ccb2d450 | -3.47332 | -50.08068 | 2026-10-07 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 2327625a-948c-33bb-9754-a12873898da0 | -3.06182 | -54.17232 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 75926351-7cce-3782-bdbf-e7df3b4be27f | -4.41783 | -55.75594 | 2026-10-07 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 555f3bb3-262e-3f1f-9f19-5990d47da364 | -3.18392 | -50.55143 | 2026-10-07 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 908d8b3c-c132-3cce-a7c4-02229440a2b4 | -4.57111 | -55.9954 | 2026-10-07 05:04:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5ece38d6-d054-30b4-b83b-262e4fe1f60a | -2.79895 | -54.09208 | 2026-10-07 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a716ea61-3f35-3675-84a9-eaf297822824 | -3.05481 | -54.21788 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d67ea11c-88ce-3005-b8dc-fc2cc0879a46 | -3.50788 | -54.63063 | 2026-10-07 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 81b660b5-5a81-3abd-8cc9-a2fa13d8ac6a | -4.1529 | -55.14446 | 2026-10-07 05:04:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cb69340a-0ed5-3657-b298-a4b553b60688 | -1.80507 | -57.09961 | 2026-10-07 05:04:00 | NOAA-21 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| f8ef1c85-23f1-3047-8de7-dfca94db0160 | -8.70945 | -45.19579 | 2026-10-07 05:04:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 9bea2371-ce70-3e2d-9195-55f6a42bd8e7 | -3.17846 | -50.5573 | 2026-10-07 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 924d95d5-259f-3a4a-9773-bbab0924ac94 | -2.10062 | -52.0592 | 2026-10-07 05:04:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 148c1668-f763-3a29-aa84-37bb6e1a8d54 | -5.98633 | -55.36434 | 2026-10-07 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 069c33d3-9d3a-38f0-9714-105b55b76922 | -2.93076 | -54.14157 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f37fe31d-8bf2-3c6e-a6ce-e842e9371794 | -3.22046 | -48.81839 | 2026-10-07 05:04:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ca665ad8-e03b-369b-9527-77ac6e221146 | -3.8376 | -52.14012 | 2026-10-07 05:04:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f1eb6dd4-bb25-3d84-a16c-3269aabefa3c | -3.28842 | -54.07421 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 15.5 |
| 0aac45a8-ce83-3513-8595-a04eaa30c0b0 | -2.94076 | -54.1431 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 36919589-40e0-3cea-b687-6b076ac190b8 | -2.50119 | -56.13101 | 2026-10-07 05:04:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9f49f108-c398-3244-9317-819f63ca17e2 | -3.50688 | -54.65883 | 2026-10-07 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d12752e9-b8b5-3bc1-a804-16f1c8a7146e | -3.22514 | -54.30524 | 2026-10-07 05:04:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 71a2890f-4140-3be5-b0e9-20c95b527950 | -3.21764 | -53.889 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8aa36a95-0888-3bda-88a3-10a3beb2cd11 | -2.84332 | -54.07014 | 2026-10-07 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| dd1fc468-3e5a-35f0-852d-d801cb5ded02 | -3.10955 | -54.17247 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 82a8a8ae-a34f-356c-83b1-93df6877ecf6 | -3.08152 | -54.24349 | 2026-10-07 05:04:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e3288cb0-fd95-39a7-ad14-985d3c01d4e6 | -3.09119 | -54.15881 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d6768a9b-7334-3fd6-a96c-1462a57a91f7 | -3.0921 | -53.71588 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c45a262c-79d4-3d2e-b0eb-c05d5830eaf3 | -4.16119 | -55.1563 | 2026-10-07 05:04:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6c09112c-f4da-346d-9245-edd4da6f982c | -3.29169 | -54.0313 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| b393e3e6-3b41-3cd6-92ac-ecd945328073 | -0.42131 | -52.06462 | 2026-10-07 05:04:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 16b33075-5ccf-3505-8d08-bd977ca434c5 | -2.94946 | -54.06534 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 25.5 |
| 1fbb1ebe-623d-3851-81c6-d9ad6482da58 | -3.04379 | -53.91677 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 92002b97-c0bb-396a-846e-dfbbbf265181 | -2.95289 | -54.10904 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 989ba00c-abc1-3e6e-9ce4-3702d32eb986 | -3.49625 | -54.61819 | 2026-10-07 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 40847928-c5f4-3061-8361-715f21ff4c51 | -5.01234 | -49.93943 | 2026-10-07 05:04:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9a727472-4089-3287-96f8-1689bd5d1ad8 | -3.26607 | -54.04185 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 38.8 |
| 7b9fff85-ed50-33da-87e6-583ee47c56f1 | -3.51065 | -54.63461 | 2026-10-07 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 05fcd873-b4b1-3cca-afbd-d3514c68fb62 | -3.06848 | -54.17334 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d44ff193-3e2c-3ff1-92a0-f69d3d67cb24 | -3.48386 | -55.44003 | 2026-10-07 05:04:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 24365e5d-103e-31a1-bda5-d947ada3ffd9 | -2.7048 | -59.80175 | 2026-10-07 05:04:00 | NOAA-21 | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c660cd67-7594-3fcd-9630-b782941b07cb | -2.14541 | -54.44244 | 2026-10-07 05:04:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 969e7b78-8fbd-30a9-b760-fb05a7b58b7e | -1.40416 | -54.6155 | 2026-10-07 05:04:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5e9dd3fd-d50b-3bc6-8990-211b95b25b06 | -3.11907 | -53.76409 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0ed5f7ae-f8d6-3bc9-b611-4faf4ea9977b | -3.71551 | -54.2119 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| da061717-7336-352c-a916-94cf973f8cf6 | -3.97252 | -56.05985 | 2026-10-07 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |


[Clique aqui para ver as próximas entradas](README68.md)
