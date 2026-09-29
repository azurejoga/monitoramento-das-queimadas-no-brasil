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

## Dados Diários - Página 83

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 71ff00f6-5383-37ef-9d65-3d237629b3e3 | -10.9156 | -50.6845 | 2026-09-29 14:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 80.9 |
| 7aee4ae8-611d-3833-8013-33a395c5dfe1 | -10.7913 | -48.7596 | 2026-09-29 14:50:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 82.8 |
| ce29c06a-089d-3caa-a120-6a390f5bcfc0 | -11.885 | -50.5768 | 2026-09-29 14:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 48.4 |
| efc5b269-dce4-352e-8991-78b361a4f4aa | -11.9932 | -50.97 | 2026-09-29 14:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 98.2 |
| d05f6157-f030-3683-b4ec-203ce16a08dd | 3.9351 | -59.721 | 2026-09-29 14:50:00 | GOES-19 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 88.9 |
| 05a58a60-68b0-3d51-9ad8-deca1084e0de | -8.3208 | -44.1679 | 2026-09-29 14:50:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 227.9 |
| 452b9b62-d20b-3e70-8a31-2bee5d049d3e | -12.0806 | -50.232 | 2026-09-29 14:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 87.3 |
| 31c0b76f-7e95-3990-ac07-af274ebd76d3 | -11.9364 | -50.9552 | 2026-09-29 14:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 61.3 |
| c4a03a12-9ddb-36f1-9724-344ebba7fd24 | -11.8859 | -50.5125 | 2026-09-29 14:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 91.7 |
| 26783aba-f9e4-361f-a42b-8f328f3d27ae | -1.3008 | -49.0613 | 2026-09-29 14:50:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 92.6 |
| 46704943-09cb-32cc-a860-dde7a2a7f720 | -12.1366 | -50.3112 | 2026-09-29 14:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 45.3 |
| a72dc7a4-8d1c-334b-80ce-efc6e12b22a5 | -6.6874 | -45.6231 | 2026-09-29 14:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 50.9 |
| a0851403-1ee1-3971-bb17-bdf0afcb2d15 | -11.3743 | -43.3734 | 2026-09-29 14:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 127.3 |
| 36493ab7-35bb-3a6c-8346-891812ddca4f | -7.4869 | -44.5751 | 2026-09-29 14:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 71.4 |
| 97cb8474-df57-3c89-ad1b-264f89c07a72 | -10.8109 | -48.7137 | 2026-09-29 14:50:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 58.3 |
| 9aab2a4e-eb09-379d-857b-b0f7da2cb38d | -18.1158 | -44.3503 | 2026-09-29 14:50:00 | GOES-19 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 128.7 |
| d7e69c7a-ff40-3997-ab77-7e8b7d7d5189 | -8.3617 | -45.4013 | 2026-09-29 14:50:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 86.6 |
| 2d5a4d6b-eac7-3c5c-a79d-d5b5f8808f65 | -10.8964 | -50.7079 | 2026-09-29 14:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 80.2 |
| da4751d9-a0c0-35a4-9c88-b3ce7ff08b01 | 1.8403 | -55.6244 | 2026-09-29 14:50:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 73.1 |
| fbf1d1aa-058b-3b6f-b4ce-8de1b5342c11 | -1.3193 | -49.061 | 2026-09-29 14:50:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 72.9 |
| a95b68aa-4ace-3fd2-90c6-4922b6793781 | -7.4871 | -44.5521 | 2026-09-29 14:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 139.8 |
| 506a246f-57e7-3d0a-8d5a-2bb8e4a63085 | -11.9842 | -50.3079 | 2026-09-29 14:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 61.2 |
| 8f9aa3b7-d9e0-3cda-9904-558856f74d89 | -11.9745 | -50.9508 | 2026-09-29 14:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 49.3 |
| ceb79bfb-e860-379d-85c8-f5e228ed0968 | -11.9037 | -50.5961 | 2026-09-29 14:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 70.7 |
| 582cc154-ef52-39d2-a412-51c3065d1f41 | -11.1907 | -45.1274 | 2026-09-29 14:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 76.1 |
| 953e9158-7078-36da-907a-5c50465e66cd | -15.3998 | -47.9261 | 2026-09-29 14:50:00 | GOES-19 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 111.8 |
| f4a021aa-df64-31d3-8c0e-de79586d094e | -4.2981 | -48.6094 | 2026-09-29 14:50:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 70.8 |
| 0008f6d2-b1c6-3a77-a3b6-3545eac67e05 | -6.1599 | -52.8929 | 2026-09-29 14:50:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 79.8 |
| e2fe3422-e6a6-3721-b3b9-5d73f9092714 | -12.0033 | -50.3057 | 2026-09-29 14:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 68.0 |
| ea7a73f9-9346-3088-a439-360fbf1796ef | -6.2401 | -41.6153 | 2026-09-29 14:50:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 61.6 |
| 3127a4ac-d5d8-3523-b301-91f2da404f49 | -9.4702 | -45.8023 | 2026-09-29 14:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 77.0 |
| e6241b96-517a-3d79-9469-74d995f1a509 | -20.817 | -57.6919 | 2026-09-29 14:50:00 | GOES-19 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 131.1 |
| b07369b0-6f70-3a62-bb26-ce59bbc23c75 | -10.9671 | -49.7152 | 2026-09-29 14:50:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 65.0 |
| 855a2515-5d4e-3a20-8b40-acf7dfc4b5ee | -10.423 | -49.3649 | 2026-09-29 14:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 59.0 |
| 25f967b0-52fb-3839-b2bc-65c92079682d | -10.3894 | -61.2502 | 2026-09-29 14:50:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 138.9 |
| 875ebe29-e4ba-312c-956d-9117623b715f | -9.2914 | -46.4305 | 2026-09-29 14:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 91.0 |
| 2c95d781-27e6-3e6f-ad75-db316e39da3b | -11.7887 | -50.6521 | 2026-09-29 14:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 72.7 |
| 38518dfc-d8dd-349c-bd73-45350a7f6f40 | -6.7251 | -45.5975 | 2026-09-29 14:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 63.9 |
| 33b3050d-1e21-315f-83dd-73f5880870cb | 3.5659 | -60.8516 | 2026-09-29 14:50:00 | GOES-19 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 86.4 |
| b6463727-fd64-39b2-bc7c-bd0341dc1f16 | -9.0249 | -49.6334 | 2026-09-29 14:50:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 76.0 |
| b70a572d-9d95-3d02-a564-f4c10cab59f1 | -8.0169 | -42.8444 | 2026-09-29 14:50:00 | GOES-19 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 145.9 |
| c84614d2-7bde-3a83-ae87-f4a6ec09c4ce | -12.7801 | -50.6619 | 2026-09-29 14:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 161.0 |
| a1acac68-c489-36a4-b90c-54104fa2fcf9 | -10.3895 | -61.231 | 2026-09-29 14:50:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 91.5 |
| 12e44307-ed2a-3108-9747-66d4729dd936 | -15.735 | -46.0384 | 2026-09-29 14:50:00 | GOES-19 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 141.7 |
| 6cfe7851-8f33-3a60-b3c3-aa3b80d1f8ae | -8.2102 | -45.4621 | 2026-09-29 14:50:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 89.2 |
| 63547f37-8cb8-3763-b4ef-fed5e40208b8 | -11.904 | -50.5746 | 2026-09-29 14:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 47.7 |
| 46e328af-e822-3949-b56f-d5dac8db1153 | -11.9596 | -50.6751 | 2026-09-29 14:50:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 62.1 |
| 288594b2-7bd8-3737-90f2-c76a4acd6b6a | -6.7254 | -45.5749 | 2026-09-29 14:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 44.7 |
| 894810f5-f268-357c-b44d-5f101c1425a0 | -11.8078 | -50.6499 | 2026-09-29 14:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 72.9 |
| 0f349e87-556e-3277-bab0-aaa62e1ef419 | -1.3008 | -49.0826 | 2026-09-29 14:50:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 74.0 |
| ff7c15d0-7df2-3838-875e-beeb4748b387 | -12.2699 | -50.3166 | 2026-09-29 14:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 53.6 |
| 55ec46d8-2f0e-31b3-8df9-e358461d7cf2 | -11.6404 | -43.4981 | 2026-09-29 14:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 207.5 |
| bf3afdaf-dd5b-330f-b096-fff7e5b347ba | -12.8847 | -44.8015 | 2026-09-29 14:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 94.1 |
| f622c265-35cd-3a53-a1ac-5ea5ccf6a392 | -6.7055 | -45.6892 | 2026-09-29 14:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 94.0 |
| f07a41a1-e3d1-32e4-a40e-deac935db49c | -9.9266 | -60.7171 | 2026-09-29 14:50:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 82.4 |
| a98783d8-5a98-3fa2-a2c8-59a1df15757d | -17.6585 | -46.5355 | 2026-09-29 14:50:00 | GOES-19 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 161.0 |
| f0750f71-9b3d-321e-8d29-71a635ca5e9c | -12.1185 | -50.2489 | 2026-09-29 14:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 75.4 |
| 6ca480d7-4c7a-3db4-a65f-a09966e66eed | -11.9936 | -50.9486 | 2026-09-29 14:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 90.5 |
| 060deec0-9a8c-3b84-8d2f-ab6638453858 | -11.998 | -44.9177 | 2026-09-29 14:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 105.4 |
| 55f92d81-11f0-37c3-9bc2-d8aa43349acc | -12.1668 | -50.8218 | 2026-09-29 14:50:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 67.9 |
| dbdaa39a-ccb7-3694-bc55-e80f697701a1 | -20.6905 | -57.9607 | 2026-09-29 14:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 126.4 |
| 2a61fe57-6973-32b8-972c-f5df4c0b4725 | 1.4453 | -50.7863 | 2026-09-29 14:50:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 64.9 |
| 6cf9f7d1-ee6c-3448-8313-77a1effeca75 | -8.3397 | -44.1658 | 2026-09-29 14:50:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 173.0 |
| f20d1206-e62b-3467-8699-fd4b1ff65d9c | -12.6267 | -47.2851 | 2026-09-29 14:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 80.2 |
| bb22c754-2458-3336-b56d-05f25bd63ef3 | -10.8967 | -50.6866 | 2026-09-29 14:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 91.5 |
| bb791519-ed6c-32ca-bb9f-74f38c83d5d9 | -15.3802 | -47.9294 | 2026-09-29 14:50:00 | GOES-19 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 93.4 |
| 3e45e763-c266-3d1e-a68d-ede693562932 | -12.7798 | -50.6834 | 2026-09-29 14:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 125.4 |
| e2c47be0-6803-362b-8637-d067fbd56426 | -7.2718 | -45.3246 | 2026-09-29 14:50:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 117.1 |
| ed327b45-0796-350a-8969-a06e705f3fa4 | -20.9155 | -57.8456 | 2026-09-29 14:50:00 | GOES-19 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 136.2 |
| 791d192c-136e-372f-aa89-c505182975e9 | -12.0362 | -50.6448 | 2026-09-29 15:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 64.3 |
| 81cb3ef6-8d0e-37e9-a1cf-019935578f08 | -8.7264 | -44.9066 | 2026-09-29 15:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 106.2 |
| f56d6cc4-8883-3968-83b6-a4eea907d7dc | -12.0178 | -50.6041 | 2026-09-29 15:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 58.9 |
| 9378e0cc-d66c-3cf4-ba06-3de799e590b7 | -12.0314 | -50.9656 | 2026-09-29 15:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 105.2 |
| 620e5709-d8c9-3e0f-9034-558d84acc6e1 | -10.9912 | -50.6978 | 2026-09-29 15:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 84.1 |
| 740ee605-5416-3a61-8e48-d909ad56bb05 | -9.9266 | -60.7171 | 2026-09-29 15:00:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 81.5 |
| 2e48450e-566a-334b-b808-b965755b6301 | -12.2508 | -50.3189 | 2026-09-29 15:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 72.1 |
| 92091e73-ba5d-3802-89db-0a9a1c2d9acf | -12.0311 | -50.9869 | 2026-09-29 15:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 82.5 |
| 70ef8703-95f2-326b-beb9-ad52ded902ec | -1.3008 | -49.0613 | 2026-09-29 15:00:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 92.9 |
| 977f4604-f36a-33ec-9cbe-b999625c675d | -10.9864 | -49.6915 | 2026-09-29 15:00:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 74.0 |
| 891f7f25-445b-3824-8b14-1b7d4e6685e6 | -10.2565 | -50.5185 | 2026-09-29 15:00:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 98.4 |
| fc60cd34-97a6-3e78-8dae-da8c891ab345 | -4.2981 | -48.6094 | 2026-09-29 15:00:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 64.9 |
| 1a0a705b-1d8d-373c-95cd-0112e8ff9b23 | -10.8967 | -50.6866 | 2026-09-29 15:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 97.1 |
| e1e6f258-9484-35ab-a4af-ff802796ca05 | -10.8109 | -48.7137 | 2026-09-29 15:00:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 50.4 |
| 3702ece3-4901-32df-b255-a497669260be | -10.2376 | -50.5204 | 2026-09-29 15:00:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 72.7 |
| ee1024a1-2f4c-33d1-8ea7-4b359c145270 | -9.0249 | -49.6334 | 2026-09-29 15:00:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 86.5 |
| 30748ecb-3658-37dd-b217-b9620ef8a4be | -11.1707 | -50.0581 | 2026-09-29 15:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 74.5 |
| 6a3ac656-d04a-3a3d-9bad-d4b9c4bd047a | -20.817 | -57.6919 | 2026-09-29 15:00:00 | GOES-19 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 122.8 |
| 7d9548e8-9809-3404-b3e7-2934e47236a9 | -12.0175 | -50.6256 | 2026-09-29 15:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 82.4 |
| 17167002-2f90-358d-810c-61cf2685ee69 | -11.8802 | -50.8977 | 2026-09-29 15:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 89.7 |
| feb58f15-a46d-3d56-8048-2bc0f5c0eb79 | -12.2897 | -50.2712 | 2026-09-29 15:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 49.9 |
| 7154fee6-1dc2-3007-8f63-b1251cf1696b | -0.5073 | -49.1326 | 2026-09-29 15:00:00 | GOES-19 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 111.7 |
| 41dc86bc-76a8-32f9-a268-b611323bb21d | -1.3193 | -49.061 | 2026-09-29 15:00:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 69.1 |
| 0f589f42-dc4b-3bde-9c1e-669c804c095a | -6.1599 | -52.8929 | 2026-09-29 15:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 89.5 |
| 60e4c2dd-8982-38f7-b841-35c9f6235822 | -10.9861 | -49.7131 | 2026-09-29 15:00:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 87.3 |
| 8791a2e9-501c-3332-abdd-f3ac84cac62b | -10.9915 | -50.6765 | 2026-09-29 15:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 55.3 |
| 020f497c-9683-39aa-8c7b-09b68a16a182 | -12.0559 | -50.5996 | 2026-09-29 15:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 52.2 |
| d801be46-6cf2-3f5f-91c5-a96be2d063ca | -11.8608 | -50.9212 | 2026-09-29 15:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 94.1 |
| 145b93a3-b241-368e-9ab6-cf9f17ee3c97 | -11.4791 | -49.743 | 2026-09-29 15:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 88.0 |
| ca639aab-36a6-369c-b2a0-db72678bb478 | 1.8403 | -55.6244 | 2026-09-29 15:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 112.8 |
| dfa32896-4877-347e-9805-d551d0d450b3 | -11.9402 | -50.6987 | 2026-09-29 15:00:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 79.4 |


[Clique aqui para ver as próximas entradas](README84.md)
