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

## Dados Diários - Página 90

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 26777799-f611-374d-8ec6-5569a5a65378 | -9.14167 | -65.81331 | 2025-08-30 07:33:00 | AQUA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 1689da5e-df43-31e3-88ec-bbe5b7eb8b72 | -9.07395 | -65.43145 | 2025-08-30 07:33:00 | AQUA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 37.8 |
| a1a09e41-1a73-3572-9492-cb957fbbc552 | -9.07123 | -65.45226 | 2025-08-30 07:33:00 | AQUA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 12.5 |
| f2c7ad17-0a23-3cc3-8d6a-4d7e0042ea1f | -9.43904 | -62.354 | 2025-08-30 07:33:00 | AQUA_M-M | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 62.2 |
| 4e289241-016c-3e92-b9ed-3b4f220508c1 | -9.1088 | -65.76931 | 2025-08-30 07:33:00 | AQUA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 33.1 |
| ad4e6bbb-083f-387a-9465-a7575bf6c14f | -13.383 | -46.947 | 2025-08-30 07:40:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 76.5 |
| f532315b-e532-3fc1-aced-38f9febb335e | -9.0614 | -65.4355 | 2025-08-30 07:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 66.5 |
| a35578b9-b21e-3017-a53c-e953a7383393 | -13.3632 | -46.9727 | 2025-08-30 07:40:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 111.5 |
| fbe1f27e-8a9b-34d7-aadf-6e0a3fb14e92 | -13.3825 | -46.9697 | 2025-08-30 07:40:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 131.9 |
| f20b219a-b44d-3302-a35d-dc99a14458ae | -13.3258 | -46.9107 | 2025-08-30 07:40:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 67.0 |
| 369e9962-59df-374b-b02c-c5f697e2e832 | -13.3628 | -46.9953 | 2025-08-30 07:40:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 160.0 |
| 5f62b967-9e61-32ea-b71a-437f7efa9277 | -9.4433 | -60.5499 | 2025-08-30 07:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 77.4 |
| 61e27bdf-9ef5-3d7c-be89-c5fafc0b980d | -13.3649 | -46.882 | 2025-08-30 07:40:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 202.1 |
| 9754938c-bd86-3f57-9495-4a0361ccef9b | -13.3456 | -46.885 | 2025-08-30 07:40:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 173.9 |
| 3e4a3ac2-2164-3056-8f87-ca61b0f2fb94 | -14.6186 | -48.056 | 2025-08-30 07:40:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 58.5 |
| 92ed2a1e-295b-3e96-a329-1d9530372274 | -6.4068 | -45.6004 | 2025-08-30 07:40:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 111.2 |
| ab92e32d-017f-3099-8543-e1a11747ab97 | -6.4255 | -45.5989 | 2025-08-30 07:40:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 245.7 |
| cfb32bdc-3c44-3655-9fe2-9e7d416cf764 | -11.8956 | -46.3753 | 2025-08-30 07:40:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 67.4 |
| 5fa6d405-c021-3fac-a5aa-69c2ab5f1352 | -13.3452 | -46.9077 | 2025-08-30 07:40:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 178.0 |
| bf3e7347-30a7-3bc8-8b23-cf8e018d0d49 | -11.8764 | -46.378 | 2025-08-30 07:40:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 63.6 |
| 636c476f-557d-3c60-8603-51aa4a4edb1a | -9.4683 | -62.3476 | 2025-08-30 07:40:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 63.4 |
| 02a3eb3e-c7c0-30fb-8b51-6c56853d2851 | -13.3645 | -46.9047 | 2025-08-30 07:40:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 140.5 |
| 3aae1f43-8ded-354f-beac-2fdbb273d986 | -6.4066 | -45.6229 | 2025-08-30 07:40:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 82.2 |
| 446df235-0b40-33c8-8656-6e889bf58526 | -9.4684 | -62.3286 | 2025-08-30 07:40:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 163.6 |
| c6b91c00-61ab-3206-b9c8-7874e9fb6e94 | -9.4497 | -62.3485 | 2025-08-30 07:40:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 98.9 |
| 0a536a0a-4fd7-327c-8fd1-3873d19edc14 | -6.4253 | -45.6214 | 2025-08-30 07:40:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 183.4 |
| 99cd611c-e3c0-3bb9-b5ab-01fa3776b028 | -11.8952 | -46.398 | 2025-08-30 07:40:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 117.2 |
| 4865293a-6be1-3b9a-b768-8208c10bd661 | -9.4498 | -62.3294 | 2025-08-30 07:40:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 211.2 |
| da986669-4d03-359f-8697-23b5c76f0082 | -7.0951 | -44.3128 | 2025-08-30 07:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 61.8 |
| d2dbbe98-23fd-3bd0-8393-e13a60b38c89 | -9.1155 | -65.7699 | 2025-08-30 07:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 38.7 |
| 94e13333-4a19-37c1-b7aa-d44cf69ab0c6 | -13.3623 | -47.018 | 2025-08-30 07:40:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 66.6 |
| 468dfb9c-006d-3390-9a59-c1fb359656df | -10.678 | -48.7289 | 2025-08-30 07:50:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 92.1 |
| c5e6b527-33fb-38c0-81df-ec043de3df93 | -13.3825 | -46.9697 | 2025-08-30 07:50:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 104.3 |
| 5d225110-eb94-3af6-aeb1-4f14187b5887 | -6.4255 | -45.5989 | 2025-08-30 07:50:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 130.0 |
| e4cff866-4f98-3040-9826-185bc103433f | -13.3632 | -46.9727 | 2025-08-30 07:50:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 105.5 |
| 9fe069ac-a802-3efb-b3b6-5ca68de2e6ee | -13.3456 | -46.885 | 2025-08-30 07:50:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 155.0 |
| f6a8ff18-8396-3a4d-bd4e-7cc70f3487f7 | -13.3452 | -46.9077 | 2025-08-30 07:50:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 168.2 |
| 2b86728b-1bd6-3faa-82db-a28cda5028d2 | -11.8956 | -46.3753 | 2025-08-30 07:50:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 74.4 |
| 6ba3009b-12f8-3452-a111-dcacbe37bb26 | -9.4498 | -62.3294 | 2025-08-30 07:50:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 168.3 |
| 49b18219-cb72-342a-85b8-a612bde9c6ce | -9.0614 | -65.4355 | 2025-08-30 07:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 58.3 |
| 6b3acb1b-1fd6-3075-8bb3-65d3eb8f3194 | -11.8764 | -46.378 | 2025-08-30 07:50:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 71.7 |
| 3c9c5107-b90f-351b-9def-53d80f4ac67c | -9.4497 | -62.3485 | 2025-08-30 07:50:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 105.8 |
| 812db1a3-687a-33c4-954e-cf6e59360700 | -13.3628 | -46.9953 | 2025-08-30 07:50:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 116.4 |
| 9c40b29c-5373-335d-b3ea-b95e97524461 | -6.4068 | -45.6004 | 2025-08-30 07:50:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 48.3 |
| 9d5d4854-4bab-355f-ba2b-2af0da25ff4a | -9.4683 | -62.3476 | 2025-08-30 07:50:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 71.0 |
| 6b9323c0-8170-3b3c-bd33-0064c2410a1a | -7.0951 | -44.3128 | 2025-08-30 07:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 61.5 |
| 1cc365de-8b7a-3566-8d80-fa0d7887c8cd | -11.8952 | -46.398 | 2025-08-30 07:50:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 129.5 |
| 1c575c34-abc9-321c-94d1-2c3069807c82 | -11.876 | -46.4007 | 2025-08-30 07:50:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 59.1 |
| 36fcdcae-d42b-396e-b1a6-8e3e3c1218ff | -13.3645 | -46.9047 | 2025-08-30 07:50:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 155.6 |
| 30655624-6cb3-3229-bc6e-e0362856935e | -13.3649 | -46.882 | 2025-08-30 07:50:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 186.7 |
| 072247c6-ddc8-3526-97c4-9664e7ed8f58 | -9.4684 | -62.3286 | 2025-08-30 07:50:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 137.8 |
| c9fa4e5f-e0a1-3b04-9060-b0eb25e6a2be | -9.1155 | -65.7699 | 2025-08-30 07:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 47.3 |
| c56a40d6-d5f4-3ac5-a343-1bd17def00a8 | -10.659 | -48.7311 | 2025-08-30 07:50:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 55.7 |
| f48b6d29-4e22-3a15-b540-4685244db68e | -9.4433 | -60.5499 | 2025-08-30 07:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 77.5 |
| 4dbf8da8-2e7c-3692-ae58-3da74ba85c06 | -6.4253 | -45.6214 | 2025-08-30 07:50:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 84.1 |
| 6f52a2e4-6424-3e82-bd15-208b690b2a6c | -10.659 | -48.7311 | 2025-08-30 08:00:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 62.7 |
| eacdb300-50c9-33e3-86e0-268f0de19905 | -9.4497 | -62.3485 | 2025-08-30 08:00:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 88.3 |
| ebff0b28-e697-351e-b36f-7daf04c45b1b | -9.0799 | -65.4349 | 2025-08-30 08:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 40.6 |
| d6ac12b0-0493-316c-94e0-a22afbd1e53c | -11.8952 | -46.398 | 2025-08-30 08:00:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 144.1 |
| 814f2d54-33bd-3d9a-b8e1-93b1db81b629 | -11.8956 | -46.3753 | 2025-08-30 08:00:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 75.9 |
| 3c8d30fb-3406-3026-b3d8-3df34b0f1221 | -6.4253 | -45.6214 | 2025-08-30 08:00:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 57.1 |
| 987ce8d6-dc93-3b77-8ef0-bcc1a3003345 | -11.876 | -46.4007 | 2025-08-30 08:00:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 61.8 |
| 2e75283c-a96f-371e-9569-017acaa3a4ef | -11.8764 | -46.378 | 2025-08-30 08:00:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 80.1 |
| 38ac7a49-c6a7-3775-9cbb-ba7fa4b5eec8 | -9.4498 | -62.3294 | 2025-08-30 08:00:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 151.0 |
| 5e440f03-9943-3bf5-93e3-bfbf78089819 | -13.3632 | -46.9727 | 2025-08-30 08:00:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 116.0 |
| 6bc3d5c2-3aad-3db0-b974-cd52d3c33972 | -9.4684 | -62.3286 | 2025-08-30 08:00:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 118.3 |
| d5ab75f0-0327-33ea-a396-5ff6a9a74193 | -9.4433 | -60.5499 | 2025-08-30 08:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 81.7 |
| 2627ee0c-c9b4-3505-a542-daabee90369a | -9.0614 | -65.4355 | 2025-08-30 08:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 53.1 |
| f8fbe197-a5c7-3d3f-8716-6bcd0c5c8a30 | -13.3628 | -46.9953 | 2025-08-30 08:00:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 91.6 |
| 3848d33e-a5be-3731-940d-e1966087df18 | -6.4255 | -45.5989 | 2025-08-30 08:00:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 54.7 |
| ab944bef-70d2-309c-a798-1edff66d374a | -9.4683 | -62.3476 | 2025-08-30 08:00:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 53.3 |
| 19925d89-57f8-3a64-9275-8d2d6f807aed | -10.678 | -48.7289 | 2025-08-30 08:00:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 63.7 |
| a68e1115-3f61-31f6-92eb-5d32637002e9 | -13.3825 | -46.9697 | 2025-08-30 08:00:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 129.8 |
| 14c1e9e6-b880-3d39-8286-79823cf5f5de | -11.8764 | -46.378 | 2025-08-30 08:10:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 78.6 |
| 95b945c2-466d-3cc5-bc32-8c8aeaf894b3 | -13.3632 | -46.9727 | 2025-08-30 08:10:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 98.2 |
| 53053923-fdff-3ace-9a82-e1a6adc07570 | -13.3825 | -46.9697 | 2025-08-30 08:10:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 102.4 |
| 31399b6a-8ef0-3f40-a366-d6f3a743c9a7 | -9.0799 | -65.4349 | 2025-08-30 08:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 31.8 |
| 81184721-b614-3128-b740-5c37133ef966 | -11.8956 | -46.3753 | 2025-08-30 08:10:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 63.6 |
| acd7660c-f398-312b-ace6-e9ca4a337e46 | -11.876 | -46.4007 | 2025-08-30 08:10:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 58.2 |
| d27b6d53-ac7e-35f0-a0a3-0ed0358bd20e | -13.3628 | -46.9953 | 2025-08-30 08:10:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 69.5 |
| 2ccb77ae-6ce9-39fb-8fe3-da4e50db1981 | -9.4433 | -60.5499 | 2025-08-30 08:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 81.0 |
| 71280c02-54ad-32b8-acaf-753891a958cf | -9.4432 | -60.5692 | 2025-08-30 08:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 58.8 |
| 0cedd507-65b2-3aac-bb5e-ca09440b0c26 | -9.4497 | -62.3485 | 2025-08-30 08:10:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 83.7 |
| 209d147a-15fc-368f-8dcf-58ff21a04e25 | -9.4498 | -62.3294 | 2025-08-30 08:10:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 136.4 |
| 50b5f528-cc20-3365-9852-12207f5665e2 | -9.1155 | -65.7699 | 2025-08-30 08:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 37.1 |
| 99f31b92-84ef-36b6-bab9-9e41447556bc | -9.4684 | -62.3286 | 2025-08-30 08:10:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 100.7 |
| 8e133553-697f-32e3-8cb5-b666057c99b0 | -11.8952 | -46.398 | 2025-08-30 08:10:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 96.0 |
| 17203d59-31eb-3221-8884-e847120b5e49 | -13.3632 | -46.9727 | 2025-08-30 08:20:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 97.6 |
| d8a1baf6-e1a2-364b-9f4b-105a604d712d | -11.8952 | -46.398 | 2025-08-30 08:20:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 124.0 |
| ab471419-4a08-3979-8547-6ca26decd9ab | -9.4684 | -62.3286 | 2025-08-30 08:20:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 92.2 |
| 9f99c85c-cacf-3ca1-a697-b3ac3de11a3f | -13.3628 | -46.9953 | 2025-08-30 08:20:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 78.4 |
| a7409606-b36d-32fc-8a78-5c10736e5b04 | -13.3263 | -46.888 | 2025-08-30 08:20:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 73.4 |
| ca88979d-278e-3729-a49a-7144e075b57f | -11.8764 | -46.378 | 2025-08-30 08:20:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 62.3 |
| aebda5e5-8ce7-3df1-a235-e8420a159b53 | -13.3825 | -46.9697 | 2025-08-30 08:20:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 109.5 |
| de2677a0-279a-3a8b-839c-0bf4c3d68671 | -11.8956 | -46.3753 | 2025-08-30 08:20:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 59.7 |
| d0da785a-81c6-308c-94a9-ec1f5ece9bbb | -13.3452 | -46.9077 | 2025-08-30 08:20:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 241.0 |
| 4300f205-b451-3296-9b4f-98928588fcb3 | -9.4683 | -62.3476 | 2025-08-30 08:20:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 46.3 |
| a715c82d-35a5-30bc-97ac-6a38a8025e51 | -9.4498 | -62.3294 | 2025-08-30 08:20:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 132.2 |
| e37abf78-c51f-3fdb-a94c-b31e81370c95 | -13.3645 | -46.9047 | 2025-08-30 08:20:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 166.5 |
| 2fe33c21-0041-3f61-bee2-ecf2a3dcc77d | -9.4497 | -62.3485 | 2025-08-30 08:20:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 81.4 |


[Clique aqui para ver as próximas entradas](README91.md)
