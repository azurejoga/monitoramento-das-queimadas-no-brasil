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

## Dados Diários - Página 91

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 78ce5941-394d-3381-97ab-1468eb517c1b | -13.3258 | -46.9107 | 2025-08-30 08:20:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 138.9 |
| e898a35e-17af-3d2e-a6e1-5f9c15c6e8b5 | -9.4433 | -60.5499 | 2025-08-30 08:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 74.8 |
| 01e6009c-c872-3ca4-9239-086445bf1ef7 | -7.0951 | -44.3128 | 2025-08-30 08:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 69.0 |
| 167f7d88-adec-3641-ac17-b24b2cf682db | -13.3456 | -46.885 | 2025-08-30 08:20:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 146.1 |
| b1215ee8-90ef-35bc-9883-3da9ab71d130 | -13.3649 | -46.882 | 2025-08-30 08:20:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 148.1 |
| a57b14b1-0909-35e2-b846-9cb9bccb8c7f | -9.4683 | -62.3476 | 2025-08-30 08:30:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 44.6 |
| 3104a637-a58d-32c1-a391-bbbf82e2733a | -13.3628 | -46.9953 | 2025-08-30 08:30:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 67.7 |
| 3d04724d-bcc8-3654-afb4-3e7c8f0e8d5a | -11.8956 | -46.3753 | 2025-08-30 08:30:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 58.7 |
| d1dddbd0-fa08-3090-8959-6d48645a9adf | -9.4498 | -62.3294 | 2025-08-30 08:30:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 118.6 |
| 13c624a2-f0e6-3cbd-91d7-3850b43b4423 | -11.8764 | -46.378 | 2025-08-30 08:30:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 61.7 |
| 2091393a-42e3-3a2c-af9b-23957822bf58 | -13.3632 | -46.9727 | 2025-08-30 08:30:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 85.7 |
| 371c6fd3-b1c3-3eb8-9b1e-07ffcedffeba | -13.3825 | -46.9697 | 2025-08-30 08:30:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 87.6 |
| 84f46113-6546-3360-895b-af1237c3c59e | -9.4684 | -62.3286 | 2025-08-30 08:30:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 95.5 |
| 0223efa5-5e22-3c71-baef-b5976c089948 | -11.8952 | -46.398 | 2025-08-30 08:30:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 116.8 |
| ac38b2e8-7776-3fac-8ba4-f295a9b15ce0 | -9.4433 | -60.5499 | 2025-08-30 08:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 76.9 |
| 0913924a-dd87-3df4-85e9-e8c0e8f7a6ae | -9.0614 | -65.4355 | 2025-08-30 08:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 54.6 |
| 775bbbf2-d752-3a08-830e-ce462a24b796 | -9.1155 | -65.7699 | 2025-08-30 08:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 47.7 |
| 8ec91254-504b-3951-97eb-d87faf848af9 | -9.4497 | -62.3485 | 2025-08-30 08:30:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 75.0 |
| 239b6d74-ec26-39db-8f3d-8a53f7bd183e | -9.4498 | -62.3294 | 2025-08-30 08:40:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 102.9 |
| 1b47e7d8-7023-3f09-89cd-07cfc204d9d5 | -9.4497 | -62.3485 | 2025-08-30 08:40:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 79.3 |
| ea8b5c89-0750-3437-a0f5-cfabbda5a8d5 | -9.0614 | -65.4355 | 2025-08-30 08:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 39.4 |
| 8fa619be-aa93-3e57-89f4-0372896ad8db | -9.4684 | -62.3286 | 2025-08-30 08:40:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 80.8 |
| ffb3505c-bf0c-37c1-a76f-84cbee7e5d35 | -9.4683 | -62.3476 | 2025-08-30 08:40:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 49.7 |
| 65c2de23-6f45-3090-bcc7-6830daabc054 | -9.1155 | -65.7699 | 2025-08-30 08:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 54.6 |
| 67b49851-90be-3fab-800f-7b1ee3228a47 | -9.4433 | -60.5499 | 2025-08-30 08:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 74.5 |
| 1d63ed70-606c-3bd2-aee2-c7f37196d6e2 | -23.7369 | -51.8964 | 2025-08-30 08:40:00 | GOES-19 | BOM SUCESSO | PARANÁ | Brasil | 4103206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 64.5 |
| 3838daa4-ee7f-3fc3-9558-e836051ad790 | -23.7369 | -51.8964 | 2025-08-30 08:50:00 | GOES-19 | BOM SUCESSO | PARANÁ | Brasil | 4103206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 69.9 |
| fdf2c1db-1f2c-3c5a-8e83-ca44501808fc | -9.4684 | -62.3286 | 2025-08-30 08:50:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 79.7 |
| b10cf865-8a79-37af-a835-09e74c62249a | -9.4497 | -62.3485 | 2025-08-30 08:50:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 72.6 |
| 078b1135-e365-378b-8b20-b573160ea4db | -9.4498 | -62.3294 | 2025-08-30 08:50:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 121.3 |
| 0fb45cdf-3df5-3130-89f3-5a43ef309d0a | -9.4433 | -60.5499 | 2025-08-30 08:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 75.9 |
| d6fb14a0-8d9f-3d6b-a924-9beb9b0210ca | -9.0799 | -65.4349 | 2025-08-30 08:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 39.0 |
| 279e2d2c-b2f7-31e8-ac2d-8aed49c024e0 | -9.1155 | -65.7699 | 2025-08-30 08:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 45.2 |
| 0342f0de-e9ba-35b2-91d9-fe73e1a5984d | -9.4432 | -60.5692 | 2025-08-30 08:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 56.9 |
| b9081e95-7f12-36ff-818c-41755e960c91 | -9.4497 | -62.3485 | 2025-08-30 09:00:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 77.4 |
| 7e0e5bea-9d54-37df-9465-0f1cbd300f55 | -9.4683 | -62.3476 | 2025-08-30 09:00:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 45.9 |
| edf9059e-7b7f-351e-8a42-ce44fc1447fd | -6.185 | -43.3491 | 2025-08-30 09:00:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 109.7 |
| f9943255-ea6f-3f91-a4ab-f00c1111bcc8 | -6.1665 | -43.3273 | 2025-08-30 09:00:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 133.5 |
| 19361b54-5171-3a70-9413-3b8a3a40b054 | -9.4433 | -60.5499 | 2025-08-30 09:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 72.9 |
| 700502dc-b444-382a-91f7-5968a5327d63 | -9.0614 | -65.4355 | 2025-08-30 09:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 43.9 |
| b4007d88-9ab3-34d4-b926-ff0e2bbb8ad2 | -9.1155 | -65.7699 | 2025-08-30 09:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 46.6 |
| 24a2211c-ad09-3316-89d2-dffaf95187a1 | -6.1663 | -43.3506 | 2025-08-30 09:00:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 116.9 |
| 3d796897-5345-388c-b5ba-37c370cb04ef | -9.4498 | -62.3294 | 2025-08-30 09:00:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 102.7 |
| 21af1f8c-8e05-3f27-8490-a8aaad95da64 | -9.4684 | -62.3286 | 2025-08-30 09:00:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 71.6 |
| 3c95c485-64b6-312d-889b-fc8b574ac018 | -6.1853 | -43.3257 | 2025-08-30 09:00:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 131.0 |
| 32f9865d-23b9-3462-b6b7-3df652f56a13 | -9.4498 | -62.3294 | 2025-08-30 09:10:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 120.2 |
| f27c6f83-49fa-3a6e-b596-b7ca3b63ec6f | -9.4497 | -62.3485 | 2025-08-30 09:10:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 70.3 |
| 16e34ecc-a207-3c75-9c60-a44535dc22f6 | -6.1853 | -43.3257 | 2025-08-30 09:10:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 120.2 |
| bc96cae1-496c-3a1b-9923-b554f5e3e994 | -9.0614 | -65.4355 | 2025-08-30 09:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 51.0 |
| c1f1174f-ef7d-37c7-bbbd-0c255a85c57a | -9.4684 | -62.3286 | 2025-08-30 09:10:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 85.4 |
| 235e55ef-78f8-30b9-aab9-bc5dd309e78f | -9.4433 | -60.5499 | 2025-08-30 09:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 68.7 |
| 0336d439-6ee4-3ab2-ad8e-0ecafe71226d | -9.1155 | -65.7699 | 2025-08-30 09:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 40.8 |
| d4ea30db-31a5-340b-9b20-3aaa5716c133 | -6.1665 | -43.3273 | 2025-08-30 09:10:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 142.7 |
| 660aab14-d84e-3e93-94e0-4098483264fb | -13.3649 | -46.882 | 2025-08-30 09:20:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 268.6 |
| 30fcb5cd-e5cd-34c9-8a94-217e8613f7ba | -6.1853 | -43.3257 | 2025-08-30 09:20:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 117.3 |
| c782a6cb-24aa-3f4b-b673-5cab7351b73e | -9.4498 | -62.3294 | 2025-08-30 09:20:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 138.1 |
| e064d181-4673-3081-b8bb-eb07ba07e707 | -9.4684 | -62.3286 | 2025-08-30 09:20:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 60.4 |
| 6d675c5f-9d48-35dc-bc07-a2e76626aa52 | -13.3645 | -46.9047 | 2025-08-30 09:20:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 117.6 |
| 65f80cce-20e4-3d3d-990e-da36b3c403df | -9.4433 | -60.5499 | 2025-08-30 09:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 58.1 |
| ef76db47-e2a1-3407-9ecf-76a0bd2f5dae | -13.3452 | -46.9077 | 2025-08-30 09:20:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 177.6 |
| 9ca858a2-d853-3f82-8d8c-7c5be142ed86 | -13.3456 | -46.885 | 2025-08-30 09:20:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 203.0 |
| 6f6885d0-77ed-3ea3-b4eb-8487ade0313a | -9.4497 | -62.3485 | 2025-08-30 09:20:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 74.2 |
| 5045430f-b499-30bf-aa88-d5bee10a4573 | -11.8556 | -46.4714 | 2025-08-30 09:20:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 103.3 |
| 541b68a6-b32a-3d39-9c87-548a8c7d7fb7 | -13.3452 | -46.9077 | 2025-08-30 09:30:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 138.9 |
| e2e82477-eeaf-3572-9f54-5d864256d723 | -9.4498 | -62.3294 | 2025-08-30 09:30:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 116.2 |
| feea485d-0504-3c90-ab98-70b722a27780 | -13.3649 | -46.882 | 2025-08-30 09:30:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 187.5 |
| 9b04b146-b2fb-3f00-a950-e789916773b1 | -13.3258 | -46.9107 | 2025-08-30 09:30:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 103.9 |
| 2026bf01-9d68-334b-a989-19d619a5fcd8 | -9.4684 | -62.3286 | 2025-08-30 09:30:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 66.5 |
| 7af5f880-9e4b-328d-9e44-82f6e336779c | -13.3456 | -46.885 | 2025-08-30 09:30:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 162.5 |
| 694e7372-613a-3ce4-9b8b-4d994b6d11e9 | -11.8556 | -46.4714 | 2025-08-30 09:30:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 132.7 |
| f563aa4a-0b8e-352d-bea6-1b562f6a3d18 | -9.4497 | -62.3485 | 2025-08-30 09:30:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 70.6 |
| d4923d59-7b47-355d-9e66-41fa0fe03733 | -9.1155 | -65.7699 | 2025-08-30 09:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 45.0 |
| 16c81681-903a-3c47-a0ba-9e2480139c7f | -11.8952 | -46.398 | 2025-08-30 09:40:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 103.6 |
| 93bdfee7-051e-324a-a3e5-0e50ccc8165f | -11.8556 | -46.4714 | 2025-08-30 09:40:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 125.1 |
| adca24b7-8cef-3d56-bd8f-d5eb99296b7a | -11.8956 | -46.3753 | 2025-08-30 09:40:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 145.7 |
| a40636d9-4e7f-3b43-89fc-53cdb0510cbc | -13.3456 | -46.885 | 2025-08-30 09:40:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 158.5 |
| 5f55a308-c82a-3be9-bc0a-01fe142209a1 | -13.3649 | -46.882 | 2025-08-30 09:40:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 193.7 |
| 9e3bed0f-7aff-3319-9c68-2d1cab155d50 | -6.1853 | -43.3257 | 2025-08-30 09:40:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 111.0 |
| 5082927e-42de-3071-a808-88a1398eed06 | -13.3452 | -46.9077 | 2025-08-30 09:40:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 131.6 |
| 8aa3d237-c1f8-36e1-9d6d-caa196a2c12e | -11.8556 | -46.4714 | 2025-08-30 09:50:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 111.0 |
| d22bc3fb-7e71-3887-bb4a-b4f5784bc5f2 | -13.3452 | -46.9077 | 2025-08-30 09:50:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 122.2 |
| 92981150-6da6-3d58-ac1b-d63dafff09cb | -9.1155 | -65.7699 | 2025-08-30 09:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 40.1 |
| 9abfc423-e939-31a7-8756-1cc0a39e10f2 | -13.3456 | -46.885 | 2025-08-30 09:50:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 225.2 |
| 785a8320-9075-3d18-82e5-2fe12db65ec5 | -11.8748 | -46.4687 | 2025-08-30 09:50:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 97.8 |
| 651cd860-d2bf-33ea-bf78-1767db6b663f | -13.3649 | -46.882 | 2025-08-30 09:50:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 256.6 |
| 6594537c-93bb-336a-9077-ccba990ea9ee | -11.8556 | -46.4714 | 2025-08-30 10:00:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 171.8 |
| d4148a70-7174-335c-9420-d7b548e58abc | -11.8952 | -46.398 | 2025-08-30 10:00:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 122.7 |
| 92280b8a-648b-39bd-af69-53067eaae0e3 | -13.3456 | -46.885 | 2025-08-30 10:00:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 134.3 |
| 54678df9-a0a6-318d-8049-5113d56b6bf9 | -11.8365 | -46.4741 | 2025-08-30 10:00:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 115.7 |
| 7216c0b3-53e9-30e2-8dbb-caae5a65c30a | -11.8748 | -46.4687 | 2025-08-30 10:00:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 120.8 |
| 1eb958a8-0691-3a8b-9388-ae5c9fbf5cd0 | -13.3258 | -46.9107 | 2025-08-30 10:00:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 104.1 |
| 7bc00d97-b80d-3dea-aa86-1ef35ef107e1 | -11.856 | -46.4487 | 2025-08-30 10:00:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 112.9 |
| 6bce47ba-c6a9-38cd-906c-d6888de2d221 | -13.3452 | -46.9077 | 2025-08-30 10:00:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 114.4 |
| dddd26dd-0d8f-3ec3-ba88-e29043e0feec | -13.3649 | -46.882 | 2025-08-30 10:00:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 115.7 |
| 7e0facbc-1da4-3d70-8be8-052f58ed4d4f | -11.8748 | -46.4687 | 2025-08-30 10:10:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 195.4 |
| e907b4eb-0343-3705-b1e6-8d2243e587ce | -11.8365 | -46.4741 | 2025-08-30 10:10:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 126.1 |
| 3a904877-3e95-31e6-a235-3b9510d333ac | -13.3258 | -46.9107 | 2025-08-30 10:10:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 120.5 |
| bdeea838-e793-36d9-aed1-cf0ae72ab94a | -11.8752 | -46.446 | 2025-08-30 10:10:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 132.1 |
| 0599d8a7-2681-32da-be92-f3e98dad5884 | -13.3649 | -46.882 | 2025-08-30 10:10:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 104.5 |
| 686f13e7-c789-3547-8723-9bec87d33e18 | -11.8556 | -46.4714 | 2025-08-30 10:10:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 292.0 |


[Clique aqui para ver as próximas entradas](README92.md)
