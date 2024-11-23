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

## Dados Diários - Página 47

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 46521c6e-e43e-354d-b744-83e75491a8e3 | -2.18304 | -55.14737 | 2024-11-23 05:10:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 4b8715fc-5096-3d71-8582-f1c368937619 | -1.61005 | -52.58833 | 2024-11-23 05:10:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 60b0f14e-60be-30ae-a9c4-114cd70dbb1e | -2.76842 | -54.06253 | 2024-11-23 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a4acbce8-6e43-33e5-811c-e53688982c10 | -1.20447 | -54.03391 | 2024-11-23 05:10:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f66f9c79-9627-34b6-9d60-37d513cf671c | -0.97494 | -51.71222 | 2024-11-23 05:10:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 742bf197-0e38-322e-a4a0-c98ff893127c | -1.56181 | -53.52448 | 2024-11-23 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c6427ec0-6ba4-38ce-b8f9-48dba1b6afb9 | -1.06472 | -51.75428 | 2024-11-23 05:10:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 87f3838b-101a-38d8-8e3c-d2d3f0060aa0 | -2.1836 | -55.14377 | 2024-11-23 05:10:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| f0135c4b-2d8c-3a45-b56f-7c5421ba508b | -1.62681 | -52.43088 | 2024-11-23 05:10:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 63630493-0945-3026-b340-8c5df6857f34 | -1.24608 | -51.74952 | 2024-11-23 05:10:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8251ce39-8111-36d4-9d25-57dc5b088fe6 | -0.98281 | -51.71346 | 2024-11-23 05:10:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 2b81ce98-599c-3ffd-9339-aba8a400b144 | -1.62105 | -52.59667 | 2024-11-23 05:10:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 6a517950-d173-3fdb-b8f1-fa614612650e | -2.45332 | -53.70483 | 2024-11-23 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| fa6a63ba-45d8-3b3c-873a-dd5ef66d9e75 | -1.40908 | -53.4772 | 2024-11-23 05:10:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ae2e6892-9a25-3120-b2db-81b68c9205fa | -2.44166 | -49.08989 | 2024-11-23 05:10:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| eb345bdd-6e7c-3308-a3bd-5fdb32355bdb | -2.72371 | -52.5598 | 2024-11-23 05:10:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a80b5060-23ed-3a49-a903-5dcebaed2b3b | -0.9125 | -51.64957 | 2024-11-23 05:10:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 58b3e76d-642e-3596-acb4-7c99c926076d | -0.95764 | -51.71976 | 2024-11-23 05:10:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 7b4ead9d-ad75-33dd-ad1f-0bbc95e84b96 | -1.5993 | -52.25338 | 2024-11-23 05:10:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a37c3df3-8968-39ae-bc1a-d5f7c224b527 | -2.73679 | -47.54368 | 2024-11-23 05:10:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 93d8a039-02b1-32bf-a74a-861609407928 | -2.18423 | -45.67792 | 2024-11-23 05:10:00 | NOAA-21 | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 584b4466-6e46-3842-ad25-3ec2005c1928 | -1.22835 | -53.68719 | 2024-11-23 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 06bb2302-0c94-3385-8c1b-53426d203563 | -1.66226 | -52.70489 | 2024-11-23 05:10:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| ee37de41-f5c9-37ad-a129-eee9dd3df69e | -1.43426 | -53.38472 | 2024-11-23 05:10:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 73aa6cda-9240-3ae5-a666-4330e0b49bc0 | 1.23634 | -50.72527 | 2024-11-23 05:10:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7a4cfa4d-236d-3527-8103-91d4ee827baf | -1.60163 | -52.41747 | 2024-11-23 05:10:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c210b566-f056-3eba-8dfc-d8912de15295 | -1.06415 | -55.25616 | 2024-11-23 05:10:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 69963d37-6c69-3dd0-911f-7f3d1978336b | -1.29259 | -51.73608 | 2024-11-23 05:10:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 542bf497-57a3-3561-8c2f-cd9e61d89e06 | -1.23895 | -51.74327 | 2024-11-23 05:10:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 799ff424-33fd-3ca3-a671-f65266d669df | -0.96629 | -51.71598 | 2024-11-23 05:10:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2c73cb41-20c0-3dbb-b4e4-e73b82e0f454 | -2.26453 | -50.46669 | 2024-11-23 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 314839d8-017d-3136-835f-0b8ee9379e19 | -1.75457 | -54.51778 | 2024-11-23 05:10:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8e053250-f79c-38dc-940a-22ff8dfbddc7 | -1.45899 | -55.45029 | 2024-11-23 05:10:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c312181a-f868-3cde-94fc-d3a2a78766fa | -2.01003 | -48.10351 | 2024-11-23 05:10:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 49d0c992-500c-3a1c-b7e8-d256fd74d6f0 | -1.96831 | -48.38465 | 2024-11-23 05:10:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 88fed72a-e08e-37cc-a551-5546d76a9020 | -2.22387 | -51.8425 | 2024-11-23 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 30a67be6-f231-3fc4-9ac0-7ad6258027c1 | -1.5612 | -53.52841 | 2024-11-23 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e3c58621-e9ec-320a-833d-dc76f23bb66c | -2.70236 | -46.2667 | 2024-11-23 05:10:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4934a11c-e42c-3845-a22b-7b355d595e07 | -3.46729 | -48.24497 | 2024-11-23 05:10:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| c48aef87-a5b8-36ef-b86b-79c038d80279 | -1.77936 | -53.61762 | 2024-11-23 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 683b1496-ab22-3a56-9673-57bbc1f01719 | -1.24049 | -54.03134 | 2024-11-23 05:10:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c9fcd314-d6c4-3aad-854c-d87c3cf5408b | -2.09275 | -53.34062 | 2024-11-23 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 140a26d0-d781-303b-8dc8-d45b5c4f8855 | -0.98125 | -51.72344 | 2024-11-23 05:10:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5137fc71-9e60-31a5-81d2-452f4d6f0d5d | -1.73354 | -52.72268 | 2024-11-23 05:10:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 15.3 |
| daa6a90f-3bf1-3c9e-acdc-706062962861 | -2.76659 | -54.07441 | 2024-11-23 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 76156f81-7511-3cb7-8699-3374d497f27a | -1.44301 | -54.51333 | 2024-11-23 05:10:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 173e4523-59b6-37c8-a23a-4b6d398c6220 | -0.95371 | -51.71915 | 2024-11-23 05:10:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c8e2677a-6126-3ce3-903c-d92ca49cfd32 | -2.74759 | -51.88075 | 2024-11-23 05:10:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5db2b3c3-c077-3b6a-a0fc-71c513171ba5 | -3.15726 | -50.58327 | 2024-11-23 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5a9520ea-7ac7-3630-924c-7cd62e32ee15 | -1.7846 | -53.63086 | 2024-11-23 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b4ac27e8-0cfb-3a13-85d7-0f60531dca79 | -3.06708 | -49.19947 | 2024-11-23 05:10:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 3a6d403d-3ce8-399b-ab84-cc23a3921daf | -1.64939 | -53.86858 | 2024-11-23 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 14.4 |
| 3b7eb11b-1881-3cc7-8b43-f5f158575f1b | -2.18416 | -55.14018 | 2024-11-23 05:10:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| b32d30a7-6a85-33b5-a869-593e3c4d43a6 | -2.33026 | -47.08231 | 2024-11-23 05:10:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c070328b-c96b-301a-9d1d-24c81b77b6ed | -2.55981 | -54.05225 | 2024-11-23 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 6d84bf60-bc6c-32e3-af24-aebb9dc3e2ff | -2.50448 | -49.00206 | 2024-11-23 05:10:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7bb05e1c-8759-306f-b718-ba722340bebb | -1.42338 | -52.67211 | 2024-11-23 05:10:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3e8dd5d9-1e36-3ec4-bad3-c1260bc4511f | -2.75348 | -54.11277 | 2024-11-23 05:10:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a777ef9e-9cca-3ef7-a6a1-a87465186d61 | -1.78063 | -53.6095 | 2024-11-23 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 398de3a4-e46a-3598-a96c-a06947322d04 | -2.15644 | -50.49405 | 2024-11-23 05:10:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a18b9e77-c920-3617-b7b5-09d9b4d889ee | -1.76992 | -53.60786 | 2024-11-23 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 66503247-ac9f-3a53-bbe0-5e6730af7fc6 | -0.04767 | -50.81371 | 2024-11-23 05:10:00 | NOAA-21 | AFUÁ | PARÁ | Brasil | 1500305 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 034399f9-6f0a-3a56-93ac-d263e028b713 | -0.97888 | -51.71284 | 2024-11-23 05:10:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 95cb2e31-b75b-33e8-85c3-f4c04ce681af | -0.94977 | -51.71856 | 2024-11-23 05:10:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5da8ab47-310c-3db0-b8dd-deef097d764e | -3.24841 | -50.12253 | 2024-11-23 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 891cd701-2fff-3c67-9c48-4ab4e1342eeb | 1.32581 | -60.71598 | 2024-11-23 05:10:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 64071e84-9a1d-3612-a6a9-ab8d5bcec16b | 1.22295 | -50.72039 | 2024-11-23 05:10:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 49e9a899-d806-337e-8d09-ced1f183b1e3 | -1.72605 | -52.72152 | 2024-11-23 05:10:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 5aa2bfef-d820-3749-820e-9454d63b0144 | -2.57951 | -51.88307 | 2024-11-23 05:10:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c6f341ec-e1a3-33ff-887f-bc36b868dff4 | -3.46614 | -48.24357 | 2024-11-23 05:10:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c6697efd-98a2-3132-91c9-5484136299b1 | -3.4647 | -48.25321 | 2024-11-23 05:10:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| aef99f5b-e486-3c11-9816-bc2f4be5bab5 | -3.12931 | -49.4067 | 2024-11-23 05:10:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a3af1e37-d316-329a-a03f-1082298cb259 | -2.06745 | -53.23694 | 2024-11-23 05:10:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0ee8fa47-8838-34bd-92ef-a9189c624729 | -1.22393 | -51.73576 | 2024-11-23 05:10:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9a8e7985-77eb-3f09-a629-f8f49243441a | -0.81762 | -51.60892 | 2024-11-23 05:10:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b33533fb-3bbc-3e82-bb2b-8954796165b4 | -1.36482 | -52.54565 | 2024-11-23 05:10:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 6f214cf3-b260-3706-a4b7-9f9e2683e19a | -2.00322 | -48.52606 | 2024-11-23 05:10:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 21e10cc7-a43a-3a47-99c8-28ffca4547ba | -1.21144 | -51.74255 | 2024-11-23 05:10:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 76159262-86ab-33bd-ba7b-ecf371d56775 | -2.51189 | -54.15326 | 2024-11-23 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0455d56b-8691-32a8-b545-78ab805b0e48 | -1.94418 | -49.52514 | 2024-11-23 05:10:00 | NOAA-21 | LIMOEIRO DO AJURU | PARÁ | Brasil | 1504000 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 87f136a6-08d4-33d1-b229-a1a304b64b6a | -2.3905 | -53.71705 | 2024-11-23 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 234a5fde-1f08-304f-b4e3-f105f50b61e8 | -2.76551 | -48.60655 | 2024-11-23 05:10:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e9720eef-d14a-3b0c-b893-01b9bc7fb805 | -2.40613 | -50.30502 | 2024-11-23 05:10:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| df12ef02-54e9-3ace-8435-ea302f7fa21f | -2.69653 | -46.26574 | 2024-11-23 05:10:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8d07ccf4-8bbf-33e9-bb51-8e7100d82dc8 | -1.46684 | -51.12091 | 2024-11-23 05:10:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c4ff5a15-a5ae-33ff-8d5a-c1e8b33873ea | -1.46741 | -51.11721 | 2024-11-23 05:10:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| def90300-2b10-32d7-885d-36a25620a4d0 | -2.20478 | -53.67825 | 2024-11-23 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c69a500d-734a-3d90-b951-c63b6e30dac0 | -1.7753 | -54.904 | 2024-11-23 05:10:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 9e9f6788-4aac-3736-92f8-b49630a0edf8 | -2.39112 | -53.71301 | 2024-11-23 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 99002a7f-2ac1-3056-9b86-02e00efba8f0 | -1.63208 | -53.31836 | 2024-11-23 05:10:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e9e440ef-c4c8-3f17-862d-3e6c21f90b03 | -1.62653 | -52.61149 | 2024-11-23 05:10:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| fcfc34d6-1187-3511-a986-f006fcc72750 | -1.6231 | -52.583 | 2024-11-23 05:10:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fbe23fd3-3c5e-3f31-98e1-b615509b02c5 | -1.60771 | -52.57864 | 2024-11-23 05:10:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 26dfe4e2-88a8-3662-8600-a0530a3abb15 | -1.94345 | -49.52992 | 2024-11-23 05:10:00 | NOAA-21 | LIMOEIRO DO AJURU | PARÁ | Brasil | 1504000 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bfc8d4c7-922c-3577-85db-ad7c4d15a5c9 | -3.00907 | -51.55286 | 2024-11-23 05:10:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9668c49f-07fc-3eba-8e1a-1560a9bbe7ff | -2.44647 | -49.09065 | 2024-11-23 05:10:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 38e255e5-2be2-327c-af95-1fec4c96880e | -2.2423 | -53.61565 | 2024-11-23 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d62dc4fe-e9ce-34d6-b8f7-440a4830169e | -1.7346 | -54.19027 | 2024-11-23 05:10:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a1b36bc1-5987-3c0a-bac0-e8eae921c042 | -1.06749 | -55.25666 | 2024-11-23 05:10:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 26719d15-b656-3612-9aef-60b645e741de | -1.60793 | -52.60196 | 2024-11-23 05:10:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |


[Clique aqui para ver as próximas entradas](README48.md)
