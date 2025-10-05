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

## Dados Diários - Página 161

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8cc2d51b-1da1-3c20-8086-5d51a5dfec2a | -17.9616 | -57.5286 | 2025-10-05 13:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 52.4 |
| 66257e60-1980-3f3d-98c8-9e69282d6a5a | -17.9408 | -57.5928 | 2025-10-05 13:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 74.1 |
| f7b3c75d-a6ca-3e2c-82d8-9ea7efd38802 | -7.2389 | -44.8955 | 2025-10-05 13:50:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 62.4 |
| 92165d63-856e-3307-b39b-cac149bda50e | -18.1968 | -53.3638 | 2025-10-05 13:50:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 72.3 |
| 69594951-be58-39b8-96c6-e69f02fab3c9 | -9.921 | -50.2109 | 2025-10-05 13:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 128.7 |
| 5e83ac2c-8548-306d-b094-eadaad8ab48a | -7.4672 | -43.0438 | 2025-10-05 13:50:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 101.3 |
| 3efb86fe-b1bf-3c16-bc78-48d52fa5535a | -8.5393 | -46.2631 | 2025-10-05 13:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 94.3 |
| a191ece3-9b4e-3df5-a803-5a6772f8d10f | -16.0759 | -45.7399 | 2025-10-05 13:50:00 | GOES-19 | URUCUIA | MINAS GERAIS | Brasil | 3170529 | 31 | 33 | nan | nan | nan | Cerrado | 118.3 |
| 177e24b5-e7fc-3c9d-9499-51ba29f53ba2 | -9.5791 | -46.1286 | 2025-10-05 13:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 100.1 |
| 2d297859-2d08-3c7d-9142-4db8fe6d5842 | -13.7476 | -51.2883 | 2025-10-05 13:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 157.8 |
| fa64dd07-7daa-3452-a2f7-592b2171d9fe | -11.0911 | -47.7573 | 2025-10-05 13:50:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 77.2 |
| 8242997b-c217-3604-9d6e-2fad239ab63a | -9.2627 | -51.8117 | 2025-10-05 13:50:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 71.8 |
| 6e6d64e3-0c26-3894-b31b-c6bab1985e6e | -11.5069 | -46.7671 | 2025-10-05 13:50:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 143.2 |
| 8d804b8e-7419-3c09-aab5-879d2b8001b5 | -6.7167 | -42.8101 | 2025-10-05 13:50:00 | GOES-19 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 75.9 |
| ad163c60-d58d-3df9-8673-bde46523f1c6 | -11.9327 | -46.438 | 2025-10-05 13:50:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 110.4 |
| b318f059-ff3d-3c60-b3db-04e205af7334 | -15.5824 | -52.4916 | 2025-10-05 13:50:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 145.6 |
| 4d21670c-af9e-3c0d-8667-26f4e39c6279 | -6.7164 | -42.8337 | 2025-10-05 13:50:00 | GOES-19 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 82.6 |
| 368b501f-a004-32c8-a282-2d2c421a3d1f | -7.7743 | -42.6103 | 2025-10-05 13:50:00 | GOES-19 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 188.7 |
| cc7ae57b-9979-36b2-9037-fa4c40e0ee57 | -9.931 | -50.911 | 2025-10-05 13:50:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 100.1 |
| 459b95ee-a084-3a02-a65b-4adb4f3ce64c | -16.0966 | -51.0829 | 2025-10-05 13:50:00 | GOES-19 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 196.7 |
| e75c8fe2-42d0-3f0e-9ee4-84a99657b937 | -11.526 | -46.7645 | 2025-10-05 13:50:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 287.5 |
| 51bd02f2-c09f-3977-a3eb-0af876363341 | -17.9602 | -57.611 | 2025-10-05 13:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 55.8 |
| 81aaa59e-ec6c-37e9-893b-969e26bd673b | -13.7284 | -51.2908 | 2025-10-05 13:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 160.0 |
| 102fda0f-5ceb-36cc-a3d1-82a4b8be5dda | -16.077 | -51.0859 | 2025-10-05 13:50:00 | GOES-19 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 170.5 |
| 597e0fc9-5f49-3904-9d5b-350ec0d9e7c0 | -10.0504 | -50.4113 | 2025-10-05 13:50:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 234.3 |
| 8926eadc-a864-392b-a6b8-4ea019fb3dea | -12.3154 | -55.1416 | 2025-10-05 13:50:00 | GOES-19 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 74.3 |
| 0d980a84-9702-397e-adfd-acf92aab2508 | -6.7866 | -41.5882 | 2025-10-05 13:50:00 | GOES-19 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 138.3 |
| 81246c5f-bdec-3994-95f5-6b334b3f7021 | -18.1769 | -53.3669 | 2025-10-05 13:50:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 50.6 |
| 8b88db10-faaf-3ff5-a473-e27b872c6e2c | -21.6888 | -50.0559 | 2025-10-05 13:50:00 | GOES-19 | PROMISSÃO | SÃO PAULO | Brasil | 3541604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 95.5 |
| 1381732a-e3fd-364e-b41b-adc7d5936f30 | -8.595 | -46.3246 | 2025-10-05 13:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 124.3 |
| ec6825d6-f977-34e3-b515-1f2c9917bb03 | -16.0805 | -50.9116 | 2025-10-05 13:50:00 | GOES-19 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 88.8 |
| ef778d60-61f8-3d16-8377-26dbb2d2a54c | -10.0506 | -50.39 | 2025-10-05 13:50:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 110.8 |
| db7b986d-dd9f-305b-a6f7-45f8bc036376 | -17.9661 | -51.1474 | 2025-10-05 13:50:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 159.3 |
| b32a4ed8-4548-3050-96b3-209d5a92befd | -6.3341 | -41.6309 | 2025-10-05 13:50:00 | GOES-19 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 100.8 |
| df3a01f3-c858-3866-869d-f2dfe6bb18c1 | -8.6138 | -54.976 | 2025-10-05 13:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 81.8 |
| d815ce8c-6cd2-3bf7-93c2-0fcb10b34d5e | -12.5297 | -54.7326 | 2025-10-05 13:50:00 | GOES-19 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 79.7 |
| 59844222-5efe-3f1c-ae0b-ad22db2a1e15 | -15.1882 | -52.8215 | 2025-10-05 14:00:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 98.3 |
| e56c0a45-c29b-3c4c-b970-0ef268c9cbb0 | -7.7885 | -44.5228 | 2025-10-05 14:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 101.3 |
| ad6d9be1-8f67-3d8a-a20a-46ce7f46a514 | -6.2408 | -45.3424 | 2025-10-05 14:00:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 59.4 |
| 6e756d39-08f5-3b91-8b29-65045d069554 | -17.9616 | -57.5286 | 2025-10-05 14:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 42.6 |
| 956c8daf-9350-3890-87d8-e54de4c5b181 | -10.6568 | -46.3372 | 2025-10-05 14:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 139.3 |
| ff23e80e-109b-3e54-a1ec-e883c4c3e67f | -12.3911 | -51.1153 | 2025-10-05 14:00:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 89.0 |
| 507dae15-22fa-33cc-b8e4-6172f07f32f1 | -6.7048 | -42.1712 | 2025-10-05 14:00:00 | GOES-19 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 66.8 |
| 6b403184-7318-3c39-86a4-e773958f2b01 | -8.539 | -46.2855 | 2025-10-05 14:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 179.8 |
| c2fbc952-dec8-39b3-9d4c-e2d91eee22b3 | -10.0504 | -50.4113 | 2025-10-05 14:00:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 129.5 |
| c73c2875-9355-36c3-91be-d1c211348aa5 | -7.4276 | -46.5239 | 2025-10-05 14:00:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 99.5 |
| 34513063-4276-3234-b496-1ff47407100a | -16.0016 | -50.9456 | 2025-10-05 14:00:00 | GOES-19 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 100.8 |
| 14fc3bdd-89d7-38c2-a40a-e76418394f43 | -17.9602 | -57.611 | 2025-10-05 14:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 53.4 |
| 1be5c5a7-8ce0-3277-a0fd-55cabb9023e6 | -8.1699 | -44.1608 | 2025-10-05 14:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 94.9 |
| 876da3fa-28c2-3bb0-8a77-77e7a03ec8fc | -8.5956 | -46.2798 | 2025-10-05 14:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 76.9 |
| 989432ad-a471-3dd3-a333-b3ccb83f1f28 | -16.0212 | -50.9425 | 2025-10-05 14:00:00 | GOES-19 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 107.1 |
| 66cf6c16-3207-36f0-a963-4d1ff01ce27b | -8.8803 | -47.6061 | 2025-10-05 14:00:00 | GOES-19 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 79.8 |
| bd2f94dd-9e48-3998-809b-5ebfd7e097f7 | -12.3157 | -55.1212 | 2025-10-05 14:00:00 | GOES-19 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 71.8 |
| ee5f5df2-8aec-36b1-ad1a-6c3856991bbb | -12.1652 | -50.9287 | 2025-10-05 14:00:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 87.6 |
| 9a9eac92-9495-3291-bce1-0c45b4c6b7e9 | -7.0367 | -42.8036 | 2025-10-05 14:00:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 120.2 |
| 95344e60-8a95-39b8-bcf8-3fe0220bd777 | -10.1763 | -45.4678 | 2025-10-05 14:00:00 | GOES-19 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 62.3 |
| aff65a9a-4eca-3d69-96b5-ca0ff6660495 | -14.9357 | -46.8278 | 2025-10-05 14:00:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 102.0 |
| 7ec566f1-9d19-36fe-ba1f-e9451f128e55 | -10.8093 | -48.8229 | 2025-10-05 14:00:00 | GOES-19 | FÁTIMA | TOCANTINS | Brasil | 1707553 | 17 | 33 | nan | nan | nan | Cerrado | 102.4 |
| 116adede-933b-3123-bdcd-e92bdbb0cb0b | -6.4134 | -43.0489 | 2025-10-05 14:00:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 89.0 |
| 91c669f4-f67d-3ac1-9e72-e110344b0620 | -7.0558 | -42.7782 | 2025-10-05 14:00:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 90.2 |
| 1f0d98ec-6d40-34e0-bdda-a70503ae658d | -12.4669 | -45.5155 | 2025-10-05 14:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 112.5 |
| 0e06afcd-279c-3803-a7d4-6ff1b861a35c | -7.0372 | -42.7563 | 2025-10-05 14:00:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 94.7 |
| be60b3cd-8141-3948-a1ce-30b481de79ea | -21.6888 | -50.0559 | 2025-10-05 14:00:00 | GOES-19 | PROMISSÃO | SÃO PAULO | Brasil | 3541604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 99.3 |
| 5c4a92e5-67a6-3120-8979-c460123c07d8 | -8.595 | -46.3246 | 2025-10-05 14:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 107.8 |
| aa04cce3-7fed-3a38-93d0-1bc1b0e5393f | -6.4076 | -43.6099 | 2025-10-05 14:00:00 | GOES-19 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 82.8 |
| daef5473-bb54-3d8b-9ecf-457088052ec2 | -6.3946 | -43.0505 | 2025-10-05 14:00:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 70.7 |
| 7c00b8a2-c48a-3a93-ae7e-b6a37d37cba8 | -7.6463 | -45.4262 | 2025-10-05 14:00:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 60.2 |
| cc36b2ba-fe5e-3431-8b73-9f4cceb3acad | -6.6546 | -41.601 | 2025-10-05 14:00:00 | GOES-19 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 102.5 |
| b6df0151-5955-3ffa-9b30-266979b8b47e | -11.823 | -45.0596 | 2025-10-05 14:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 190.1 |
| e072a412-7bd4-37fe-adc5-92f27a64780e | -8.6138 | -54.976 | 2025-10-05 14:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 87.2 |
| d5e226fd-a720-3736-b647-5a6b45c79bc0 | -6.6976 | -42.8354 | 2025-10-05 14:00:00 | GOES-19 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 84.6 |
| eeb0b4ca-0d9f-3390-9f67-e23881e72393 | -9.6287 | -46.6394 | 2025-10-05 14:00:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 108.9 |
| 891089ad-f583-3c9a-90e4-9955fc766e7c | -7.7935 | -42.5845 | 2025-10-05 14:00:00 | GOES-19 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 132.9 |
| e9db35ca-e0e8-3003-bf41-28fba289e6ba | -9.2439 | -51.8133 | 2025-10-05 14:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 88.3 |
| 42bcd8e7-2bd5-3d52-9f24-b6f9f79f5417 | -12.5733 | -48.1393 | 2025-10-05 14:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 75.9 |
| e6e26295-8af2-361d-9fc3-a3939074f763 | -11.7912 | -48.0448 | 2025-10-05 14:00:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 182.6 |
| 83e2dd0f-dd2a-31ba-869c-a37715f8d6ed | -11.8225 | -45.0827 | 2025-10-05 14:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 196.6 |
| 7190f99d-58b8-3f1e-9350-2ad1f60ed0e2 | -10.0692 | -50.4094 | 2025-10-05 14:00:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 117.8 |
| 7be140f1-3e55-3ffd-bcdf-3b87a764a2ae | -8.1615 | -43.3465 | 2025-10-05 14:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 62.9 |
| a16ed4ff-1c7f-38c8-a49f-ec21963016a2 | -6.7164 | -42.8337 | 2025-10-05 14:00:00 | GOES-19 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 81.9 |
| a6fd39ff-529d-3660-828e-68ed8e5b4831 | -10.069 | -50.4307 | 2025-10-05 14:00:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 149.3 |
| 8daa0c82-cf59-3893-88f2-76cdf75d5adb | -9.5791 | -46.1286 | 2025-10-05 14:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 105.9 |
| ac7f42d3-5677-3ff9-902a-e8f8606a6c37 | -6.7052 | -43.8859 | 2025-10-05 14:00:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 85.0 |
| 865b6a42-7cde-34af-814f-a6f450a4cf52 | -6.9871 | -47.4885 | 2025-10-05 14:00:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 85.8 |
| c3254ea3-0798-3f63-b25b-a989d15360f7 | -7.6993 | -42.5708 | 2025-10-05 14:00:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 94.7 |
| 7c740f34-70c9-3741-8b17-33e20e37fefe | -16.0774 | -51.0642 | 2025-10-05 14:00:00 | GOES-19 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 98.3 |
| c8d18fa0-f48b-391b-881d-43fc1123d2cc | -12.5294 | -54.7531 | 2025-10-05 14:00:00 | GOES-19 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 76.2 |
| a81769dd-6818-3cf3-8a10-e57ddc34bd84 | -15.1886 | -52.8003 | 2025-10-05 14:00:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 89.6 |
| 3295c052-7697-3247-8f63-9cde0072c8fa | -11.8635 | -44.938 | 2025-10-05 14:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 143.9 |
| 2fe6e079-d03b-33ab-bb6b-91d6d41d0be7 | -7.646 | -45.4489 | 2025-10-05 14:00:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 60.2 |
| cb13f4a9-c34c-3358-99ee-d9694096e300 | -6.4158 | -44.6695 | 2025-10-05 14:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 64.9 |
| 49795b68-36e9-3b36-b73d-3cf8ef0d22af | -10.456 | -48.3607 | 2025-10-05 14:00:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 86.2 |
| dc0763b2-6cf4-30e9-9a6e-1c18c055817a | -10.3864 | -45.3955 | 2025-10-05 14:00:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 118.3 |
| f5a1b482-915d-3c52-bace-229418b8f924 | -10.3721 | -50.3363 | 2025-10-05 14:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 141.4 |
| 08077f29-2058-3a25-a6e5-ff8484575d78 | -7.4464 | -46.5223 | 2025-10-05 14:00:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 78.4 |
| 7461d892-51ae-32ae-b754-bba503f9b351 | -7.2392 | -44.8727 | 2025-10-05 14:00:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 54.7 |
| 127589d2-8aea-37bd-a0a3-a31ddc0d43fa | -16.077 | -51.0859 | 2025-10-05 14:00:00 | GOES-19 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 243.0 |
| fc702da2-3e36-3415-9de7-7290479603cd | -7.7746 | -42.5865 | 2025-10-05 14:00:00 | GOES-19 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 110.7 |
| 61fce662-a72d-3a0d-882a-fcb723458b4e | -17.986 | -51.144 | 2025-10-05 14:00:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 116.2 |
| 858f3b6b-e587-38c4-a42c-c46a53fc6031 | -7.7932 | -42.6082 | 2025-10-05 14:00:00 | GOES-19 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 150.9 |


[Clique aqui para ver as próximas entradas](README162.md)
