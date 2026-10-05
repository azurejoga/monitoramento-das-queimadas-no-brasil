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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a4d9058e-ab19-3313-a1bd-a0372a65dd97 | -3.06177 | -54.16144 | 2026-10-05 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| af05207d-a2ad-3b63-8985-c4cc316e82b5 | -3.13065 | -53.72563 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1c7a2f2e-0a98-3b61-b8dd-4c7de974fb28 | -4.30343 | -50.78575 | 2026-10-05 04:38:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 88eaeb4d-5c4a-36c8-b3e0-d841f825f2c8 | -6.90005 | -43.67928 | 2026-10-05 04:38:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 6baf76b9-da56-355a-b40d-074c9efb530b | -3.30521 | -53.85551 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 72df125d-912b-36dd-a16f-bad87c671fa3 | -2.21921 | -53.71132 | 2026-10-05 04:38:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c44c5938-10ed-32d4-8d71-5eb25d2cd910 | -3.07164 | -54.16644 | 2026-10-05 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 20.8 |
| 1fab6daa-f57f-321a-b523-d9a42c723425 | -6.00486 | -53.51542 | 2026-10-05 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 6a3e7d02-684d-3da9-8767-c63ecac34592 | -2.8214 | -54.12517 | 2026-10-05 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 757057dc-ae3f-3d89-ad7d-1d740d9335be | -2.86045 | -49.63134 | 2026-10-05 04:38:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 02769276-3bc6-3218-a76d-d09a87a583e0 | -3.50107 | -54.6168 | 2026-10-05 04:38:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5039f785-bbf5-3b10-8ab9-d25c3e9100d5 | -3.43877 | -50.66348 | 2026-10-05 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 626f31f4-9318-380f-af32-d1d31ca7d87b | -5.5874 | -49.74578 | 2026-10-05 04:38:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 3568792a-65ee-3d0b-864b-e9ce28c0c26f | -6.21453 | -52.68357 | 2026-10-05 04:38:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9c7cea7c-84e3-3a3a-b461-a5e49323ece3 | -3.10976 | -53.70664 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| cbc463f2-03a2-30d9-b467-acd701e38d93 | -3.11755 | -53.74145 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 098d38e6-27e1-34db-ab9b-937f0411ae21 | -7.487 | -44.42892 | 2026-10-05 04:38:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a152e596-c5b6-3049-ae17-291dedaf02cf | -3.05671 | -54.16056 | 2026-10-05 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c8e78f93-6c22-3bed-a00c-f05067b69931 | -3.84198 | -50.31067 | 2026-10-05 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| def4ace2-45c0-346d-8d4f-61c16645ae54 | -2.98642 | -54.10054 | 2026-10-05 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| cd827fc1-b9f9-3d6b-90e7-95a24d7aeede | -3.4706 | -50.08747 | 2026-10-05 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b119759e-edc8-3a07-933e-72f7d1be0eae | -2.80575 | -54.12247 | 2026-10-05 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fc4153a2-34c6-3016-b02a-8ac5e3b8d0a1 | -7.72149 | -45.4624 | 2026-10-05 04:38:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c4b10b11-a076-3416-9406-a06697dae2be | -4.11519 | -49.071 | 2026-10-05 04:38:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 504e22a8-6b6d-3240-b795-a4ffc3cd1a4a | -3.65421 | -55.31878 | 2026-10-05 04:38:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 25d35e32-3155-30b3-82eb-1c390ca2f8b1 | -2.82765 | -54.11975 | 2026-10-05 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2bb80d12-e8ff-3e66-a1f7-f187d57fb5ff | -3.10999 | -53.75523 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 81d12b7a-9022-3482-b14b-3833559a78f4 | -6.90483 | -43.67186 | 2026-10-05 04:38:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 5906eab8-b0a0-3702-a1a9-959a712bc40d | -3.11098 | -53.73086 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1ac33b85-a01c-3953-9a9a-04c5bf131e81 | -2.89734 | -54.11845 | 2026-10-05 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 599efe81-3943-3595-845d-a04cc1d53028 | -5.80902 | -47.79972 | 2026-10-05 04:38:00 | NPP-375D | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f13d5490-1845-3e50-a7f5-3836c4ed716a | -3.11962 | -53.75984 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 8764d159-44ea-3d0f-82c8-4f0dee7ee035 | -5.58667 | -49.75024 | 2026-10-05 04:38:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 1451614e-9ea3-37a7-9126-367884dcad47 | -3.15205 | -50.43903 | 2026-10-05 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9b228a58-2de7-32fd-9e46-ba4c33feb42f | -4.46827 | -54.97596 | 2026-10-05 04:38:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f51771fb-cf1e-3975-b6e7-086c43710e47 | -6.91254 | -43.66891 | 2026-10-05 04:38:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 76b7cb32-3e22-3ebd-a856-a85be8a2c2b0 | -3.46117 | -54.59301 | 2026-10-05 04:38:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 29.7 |
| b07d5280-dd61-369f-8d94-12896a33f552 | -7.72821 | -45.46342 | 2026-10-05 04:38:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3c23a484-f94b-3f96-bb03-32f546cd31b2 | -1.10427 | -54.14824 | 2026-10-05 04:38:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| aca2f407-ce8a-3047-b9bf-418980729a75 | -3.26342 | -52.25113 | 2026-10-05 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cfa26072-3a8f-3cc1-842c-ffcf1ef6418d | -2.81877 | -54.10854 | 2026-10-05 04:38:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e343cca8-31cb-3b4f-b8d3-4451c9950b9a | -4.90798 | -46.00425 | 2026-10-05 04:38:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 816d8aab-0a08-3b23-bfe2-bb329b56e7dd | -3.27573 | -50.03154 | 2026-10-05 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6b3a815f-1021-362b-9fb7-602d821f6785 | -3.18159 | -50.53817 | 2026-10-05 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ea03c6b8-3b94-328b-ba2d-b571f12844b1 | -2.89786 | -54.11533 | 2026-10-05 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1ee29a6c-b049-3325-b06d-207b3f576941 | -1.0882 | -54.11108 | 2026-10-05 04:38:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| eb6bd83b-12fc-3679-991b-6cdb29b5398c | -3.11222 | -53.75513 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| e2822c43-03b2-3d17-a2b5-1167f36a71fe | -3.07946 | -54.18361 | 2026-10-05 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 26.8 |
| cbbf373e-8e89-3e0c-b29d-d56b35453a39 | -2.24174 | -51.91679 | 2026-10-05 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 38e50324-f76b-35ea-adfc-337740541da7 | -3.12055 | -53.72392 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 11ce08b9-38c6-3795-922a-841d28b2ac03 | -3.11003 | -53.7367 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| aac8d698-e610-3f5f-b956-bf9bdeb08ddd | -3.12211 | -53.74524 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 54bc4687-f739-3c3b-b948-5d1c4125f002 | -3.702 | -50.65541 | 2026-10-05 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 04779735-7445-3cc6-a942-7206707f585d | -6.8759 | -43.67142 | 2026-10-05 04:38:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 537c8cdf-652a-3d8e-a46b-7f0e66e8c1ff | -6.08487 | -53.47991 | 2026-10-05 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f2582a3f-b785-34c6-826d-64c870294fa8 | -7.33057 | -44.36309 | 2026-10-05 04:38:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 462e500e-cf5a-394b-83a4-ac01a5028e3f | -3.11605 | -53.75023 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 329a3d94-6c62-329a-bacb-874f4fd1b045 | -4.45922 | -54.96422 | 2026-10-05 04:38:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4ed3acac-918f-3f1c-ad3d-d1e4916f5d7e | -2.89837 | -54.08018 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fad6c358-38b8-31a3-a24f-bb0ea7d4a01a | -6.89482 | -43.66628 | 2026-10-05 04:38:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 330e629b-9453-3956-8417-6eff643d23db | -6.20495 | -52.79174 | 2026-10-05 04:38:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0aeeb210-b945-3b80-ae30-30e8c3e0e6f3 | -3.13015 | -53.72855 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 87a6bb45-38b4-34d3-8ce7-954725c2701d | -3.71023 | -40.34574 | 2026-10-05 04:38:00 | NPP-375D | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| fefaae28-139b-39d7-b760-c686e8286621 | -2.79375 | -54.09787 | 2026-10-05 04:38:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ab954757-c11d-37c5-88f5-46a8c986c7df | -3.13164 | -53.71979 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| fe93a35d-0bef-3aff-aa06-d83ca67a5f08 | -6.0031 | -53.52562 | 2026-10-05 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0e5134d1-d70c-3627-93e0-961b299a98f3 | -3.20437 | -50.74895 | 2026-10-05 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1ec8bc99-f295-3f75-8937-be01075f4a8d | -6.06032 | -53.48093 | 2026-10-05 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8ab652e7-6fa6-3cf2-a122-a957a7d672e8 | -3.11049 | -53.7523 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9edbb815-8ee8-3eba-a9a6-3f202493c81d | -5.31475 | -46.67863 | 2026-10-05 04:38:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ea6acb4e-0742-3ed2-b54b-383be7dcac2c | -2.92702 | -54.13325 | 2026-10-05 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 39fa2d23-4f84-3b16-bc98-0fe2ded2807c | -3.10375 | -53.71162 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| bee4c22f-7805-37a1-9c18-0473076ceaa8 | -2.81929 | -54.10538 | 2026-10-05 04:38:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e117ff2a-8900-3f46-9ae1-4e78a0840e5a | -3.11433 | -53.71037 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| b96ea56e-4baf-3858-be08-599ef8e986aa | -3.70085 | -50.66248 | 2026-10-05 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| c9fa393b-c21a-3a89-9c8e-3dfc478d485b | -3.5117 | -54.60511 | 2026-10-05 04:38:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 46ad39fc-80c7-3fc2-b577-b3d37d0e279b | -3.51869 | -54.60971 | 2026-10-05 04:38:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4a90467b-f311-3665-a112-1a19e6167ffe | -3.07999 | -54.18048 | 2026-10-05 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 26.8 |
| 6794a8c5-08ea-3a40-ab67-c77920195d0b | -4.10892 | -49.07189 | 2026-10-05 04:38:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7f87478a-51c4-3510-b5a3-c9b351926386 | -3.18508 | -50.54237 | 2026-10-05 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| af85afb0-a74d-3fb7-83b4-961ec2f4a3af | -3.6513 | -55.50603 | 2026-10-05 04:38:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9641f533-26e3-3ed8-b0f6-565c1663017f | -1.55558 | -54.79899 | 2026-10-05 04:38:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3e3b63c8-9478-3c7d-bf88-4409a34e8ac2 | -2.79636 | -54.11443 | 2026-10-05 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b7dd5546-bb6f-3eeb-a67d-e33bf1580af3 | -2.81149 | -54.12022 | 2026-10-05 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b629d82e-0c0d-3423-bd00-0d113406575c | -3.12261 | -53.74231 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0f6cff04-fbe9-3ea2-9050-d7ba71d0225f | -3.46704 | -54.59071 | 2026-10-05 04:38:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 94797192-64c3-3caf-94f4-ddae0ff780f5 | -3.10928 | -53.70954 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 4b9d8e64-cb80-3796-ab9e-c9b6e422f889 | -2.58486 | -51.85219 | 2026-10-05 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5689156d-5f84-3302-86d2-bea7e40d241a | -6.90359 | -43.67983 | 2026-10-05 04:38:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 7ba888a8-d9b8-30d6-8d50-ffff3751110e | -3.12535 | -50.34492 | 2026-10-05 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1637965b-490e-3415-b557-92d45d72388b | -3.12015 | -53.7384 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f6697fec-3f4d-3250-90fd-52f70c6ebabe | -3.11338 | -53.71622 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 655369c9-ee4d-3d03-b4b6-8d4a6c5cd08c | -2.78174 | -54.10564 | 2026-10-05 04:38:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4fad959f-966f-32b8-82d1-f581d402aad7 | -3.50353 | -54.62065 | 2026-10-05 04:38:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f0c0d185-b0c9-3d0e-bb8c-ba372367cab2 | -1.61582 | -55.13807 | 2026-10-05 04:38:00 | NPP-375D | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 044ef14d-41ee-3d06-829d-4f99b8547cb3 | -6.00785 | -53.52642 | 2026-10-05 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0bc6f28f-d262-3670-837d-26050ed47790 | -6.88236 | -43.6765 | 2026-10-05 04:38:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 33e1184a-c6fb-3fde-b39f-f9a23cdb498a | -2.7927 | -54.10419 | 2026-10-05 04:38:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3044f7c1-0971-3dc0-a2fd-9dfb06cec075 | -3.12709 | -53.71604 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| a95b0256-631c-3209-b790-c5819662bf7d | -3.12034 | -53.70538 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |


[Clique aqui para ver as próximas entradas](README21.md)
