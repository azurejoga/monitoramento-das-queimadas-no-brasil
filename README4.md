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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c7b57982-626e-3b89-8f85-807de7fae44c | -8.07445 | -43.13578 | 2025-05-08 03:45:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 10.1 |
| 8a69fb96-a258-3307-8bb6-898d8d672c6d | -10.66669 | -44.38364 | 2025-05-08 03:45:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7c1e3b2a-317f-3bfc-ad92-12f0a4e2ca10 | -5.16861 | -45.10553 | 2025-05-08 03:45:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 70a56bb0-5cee-3138-b17c-122271ca1f02 | -6.69606 | -42.13836 | 2025-05-08 03:45:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 13.4 |
| 7d0318e9-e85a-311d-a74e-9946534a39e3 | -9.61101 | -37.04296 | 2025-05-08 03:45:00 | NPP-375D | MAJOR ISIDORO | ALAGOAS | Brasil | 2704401 | 27 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 1513a925-5ca1-3f52-9c41-8512cee44a15 | -6.70142 | -42.13453 | 2025-05-08 03:45:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 8.5 |
| 6c7aeddb-d3a3-3c18-8429-42d748619ae6 | -7.07057 | -44.39062 | 2025-05-08 03:45:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 53e7d193-ea9b-3c15-b2f5-9b8ddc995fc7 | -6.95924 | -47.92868 | 2025-05-08 03:45:00 | NPP-375D | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 69df4265-641a-38cc-b75f-4f3fcd40f94e | -8.65867 | -44.26374 | 2025-05-08 03:45:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c703247b-d6ab-39f4-b4a9-fa34c4a89e08 | -9.80442 | -37.48705 | 2025-05-08 03:45:00 | NPP-375D | PORTO DA FOLHA | SERGIPE | Brasil | 2805604 | 28 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 4ed7fbe7-018f-310b-84d8-fd4ff6ebb23a | -6.83821 | -42.78954 | 2025-05-08 03:45:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 648b399d-8d5a-347a-a951-8fe63288e681 | -8.07352 | -34.97582 | 2025-05-08 03:45:00 | NPP-375D | RECIFE | PERNAMBUCO | Brasil | 2611606 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 6d75ad5d-5019-39f6-a0a1-1a3bf7deb731 | -6.97898 | -42.79638 | 2025-05-08 03:45:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| fb5d6e17-b80f-3fe2-b65d-9ed78ca4c927 | -21.79327 | -52.74842 | 2025-05-08 03:47:00 | NPP-375D | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 012d3581-b568-3eb2-be7f-af1dc3091f1d | -14.63947 | -45.13249 | 2025-05-08 03:47:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 3b69a82f-5c18-3cdb-8f63-a704a3907230 | -16.18128 | -46.4715 | 2025-05-08 03:47:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ef9981c5-ee00-3854-9f94-17670fad7a66 | -14.64391 | -45.14584 | 2025-05-08 03:47:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 3887860c-35c3-3bdb-a861-f2c399d75591 | -22.67684 | -49.83194 | 2025-05-08 03:47:00 | NPP-375D | SÃO PEDRO DO TURVO | SÃO PAULO | Brasil | 3550506 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ebccaacd-0bed-377b-8518-2e77d8099491 | -23.6012 | -49.00484 | 2025-05-08 03:47:00 | NPP-375D | ITAÍ | SÃO PAULO | Brasil | 3521804 | 35 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c1a94e7c-8977-30a4-b432-e8699792a555 | -23.60596 | -49.00346 | 2025-05-08 03:47:00 | NPP-375D | ITAÍ | SÃO PAULO | Brasil | 3521804 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8dcd5b12-1bcd-38ff-8a65-6f6e92355449 | -15.83031 | -46.57523 | 2025-05-08 03:47:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0c58ef73-e3d9-3279-8331-602b1826561a | -18.50463 | -45.60674 | 2025-05-08 03:47:00 | NPP-375D | MORADA NOVA DE MINAS | MINAS GERAIS | Brasil | 3143500 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 92b584a6-f4a1-36ae-946f-52433a2af97e | -23.59599 | -49.00359 | 2025-05-08 03:47:00 | NPP-375D | ITAÍ | SÃO PAULO | Brasil | 3521804 | 35 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 655e4bb3-60c8-3c79-986d-7de71f4b1a75 | -23.6064 | -49.00613 | 2025-05-08 03:47:00 | NPP-375D | ITAÍ | SÃO PAULO | Brasil | 3521804 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2b42f139-e85b-35fb-9e41-45dc8d2dd5ff | -17.5948 | -43.19714 | 2025-05-08 03:47:00 | NPP-375D | CARBONITA | MINAS GERAIS | Brasil | 3113503 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 57d76e78-0578-3adf-a885-44cf0dc41bee | -14.64499 | -45.14032 | 2025-05-08 03:47:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 11.6 |
| cd5b9301-acba-362f-b518-ae0133ae2735 | -11.77743 | -48.70752 | 2025-05-08 03:47:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| aee45d22-895a-3ca7-869a-ab7baf0c38f3 | -18.81236 | -41.98321 | 2025-05-08 03:47:00 | NPP-375D | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 2fe8763d-0cac-3b00-a6d2-e90bae756337 | -13.50462 | -43.65618 | 2025-05-08 03:47:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e9d77a1b-a123-34d1-9bd8-21688066f0eb | -14.09643 | -44.23619 | 2025-05-08 03:47:00 | NPP-375D | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 0d10e9d6-19cb-3c5a-91a9-cb601526f1da | -17.77738 | -42.81031 | 2025-05-08 03:47:00 | NPP-375D | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 626458f1-370f-3c00-bc6b-6241ffa49ca2 | -12.75158 | -47.96994 | 2025-05-08 03:47:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2bfbcccd-da82-3c3e-afc6-2c4519de869a | -16.683 | -43.88383 | 2025-05-08 03:47:00 | NPP-375D | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d24cae6d-bcab-3a90-bd20-b0c16539921c | -16.18192 | -46.4683 | 2025-05-08 03:47:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 64169f98-7d75-3472-be6b-79c88b71e342 | -14.6337 | -45.12083 | 2025-05-08 03:47:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4be53cf1-0d25-3cad-ac2c-e9d2e2790308 | -19.53435 | -43.92429 | 2025-05-08 03:47:00 | NPP-375D | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 63ad2691-ec77-3323-87e1-169845e072a8 | -23.60718 | -49.00258 | 2025-05-08 03:47:00 | NPP-375D | ITAÍ | SÃO PAULO | Brasil | 3521804 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5abe596d-e9ef-3f62-be97-2355a41471c8 | -17.78134 | -42.8111 | 2025-05-08 03:47:00 | NPP-375D | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1da952ff-aca1-3f2a-a124-15f427b08b5f | -14.63746 | -45.1273 | 2025-05-08 03:47:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 31.0 |
| 68b7a317-e0a7-34c5-8138-c4eb49547d04 | -14.63461 | -45.13148 | 2025-05-08 03:47:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 881257ff-8140-36a6-aafc-39a9b2840ef2 | -23.59395 | -49.008 | 2025-05-08 03:47:00 | NPP-375D | ITAÍ | SÃO PAULO | Brasil | 3521804 | 35 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2cd096b0-49f1-3bc5-a02c-638338aee01c | -18.81306 | -41.98193 | 2025-05-08 03:47:00 | NPP-375D | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| aa99b996-41e6-34ee-9aa5-ad74a474529d | -23.60075 | -49.00223 | 2025-05-08 03:47:00 | NPP-375D | ITAÍ | SÃO PAULO | Brasil | 3521804 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b47bad75-1b3e-382b-ae7c-10d92d46cc60 | -15.82511 | -46.57405 | 2025-05-08 03:47:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d0432526-bf2e-3826-b87a-a23d2220c348 | -15.82576 | -46.57079 | 2025-05-08 03:47:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2ebcad17-99d0-3c82-9ccb-6491eaf2af58 | -14.10103 | -44.23726 | 2025-05-08 03:47:00 | NPP-375D | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| f6d2ee02-dea6-372f-9ede-70595c858b31 | -23.60197 | -49.00133 | 2025-05-08 03:47:00 | NPP-375D | ITAÍ | SÃO PAULO | Brasil | 3521804 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 584916f4-00fc-3905-97b1-dedb2c988166 | -19.5323 | -43.92292 | 2025-05-08 03:47:00 | NPP-375D | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c07c944a-208d-3048-bb3e-dbba80796250 | -15.82379 | -46.5806 | 2025-05-08 03:47:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 3dccc066-16b8-3ac3-8ad2-b34e5a987d47 | -14.64051 | -45.12696 | 2025-05-08 03:47:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 23.8 |
| 76f4f0e6-e477-3488-bb50-cc87574640cb | -14.63842 | -45.13802 | 2025-05-08 03:47:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 581a970e-865c-3df3-837e-5ef387ef169c | -14.64328 | -45.13902 | 2025-05-08 03:47:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 9ace6c59-41a6-30b3-b9a8-3dd907b1bb6f | -22.67125 | -49.83069 | 2025-05-08 03:47:00 | NPP-375D | SÃO PEDRO DO TURVO | SÃO PAULO | Brasil | 3550506 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 863115f7-b0ed-3732-a401-c16d0a70192f | -19.53155 | -43.92683 | 2025-05-08 03:47:00 | NPP-375D | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2e9d3ac3-863e-3d3f-9f73-a49cae3c2baf | -23.59522 | -49.0071 | 2025-05-08 03:47:00 | NPP-375D | ITAÍ | SÃO PAULO | Brasil | 3521804 | 35 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0eeca88b-84c2-3fef-9ace-961faa20ca26 | -16.56742 | -45.31718 | 2025-05-08 03:47:00 | NPP-375D | SANTA FÉ DE MINAS | MINAS GERAIS | Brasil | 3157609 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e7cb4659-b5e1-3dac-808e-7507f47dd52b | -23.60515 | -49.00702 | 2025-05-08 03:47:00 | NPP-375D | ITAÍ | SÃO PAULO | Brasil | 3521804 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 677f79bd-5c2e-3c3c-9fce-71122d3565b0 | -17.36509 | -42.51416 | 2025-05-08 03:47:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a3311ee7-55fe-3e20-8be1-5f8360ba52a2 | -23.98575 | -48.91626 | 2025-05-08 03:47:00 | NPP-375D | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4c315f82-9916-3244-a074-4b2872f54977 | -13.50367 | -43.65372 | 2025-05-08 03:47:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| acc1461b-4b82-33e1-9627-ebd6afb76257 | -14.64223 | -45.14455 | 2025-05-08 03:47:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 6b0435cb-7aee-3788-bcd4-2917116000a2 | -17.88692 | -43.99189 | 2025-05-08 03:47:00 | NPP-375D | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 42c79890-856a-3b74-a5e3-0315260b4959 | -14.63855 | -45.12182 | 2025-05-08 03:47:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 34.4 |
| c7049bad-7965-35c9-821f-5004c56ad2bf | -23.40843 | -46.42154 | 2025-05-08 03:47:00 | NPP-375D | GUARULHOS | SÃO PAULO | Brasil | 3518800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| cc272013-3426-3af3-bd98-0e6c1934d0f9 | -14.64014 | -45.13933 | 2025-05-08 03:47:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 10.7 |
| f0473e8f-c233-372a-83e3-57c89df0625b | -14.64156 | -45.12146 | 2025-05-08 03:47:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 23.8 |
| 1bfb6af4-0a65-3cae-a0f4-ac7f7f15b99f | -11.77853 | -48.70221 | 2025-05-08 03:47:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3ef0cdd2-5943-300b-b3a6-daa6cb67741d | -14.64123 | -45.13382 | 2025-05-08 03:47:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 31.0 |
| 4c218e8b-c3ec-3cea-8908-3f22f9b0c59c | -23.59474 | -49.00449 | 2025-05-08 03:47:00 | NPP-375D | ITAÍ | SÃO PAULO | Brasil | 3521804 | 35 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f5a669a9-b7a5-33dc-a2a2-2bf06aecd1d7 | -19.15822 | -47.81802 | 2025-05-08 03:47:00 | NPP-375D | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | 4.9 |
| a49ecf42-3c88-36a5-87c4-464ef8ede301 | -19.15743 | -47.82177 | 2025-05-08 03:47:00 | NPP-375D | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | 4.9 |
| dd49e2b3-9af7-345c-b616-ea2cba0f1b6e | -14.64813 | -45.14002 | 2025-05-08 03:47:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5a18b2f2-feeb-34be-91d7-e14672a7573b | -14.64231 | -45.12831 | 2025-05-08 03:47:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 31.0 |
| 910916cd-5f71-3f10-8d38-da9be9fb1155 | -15.83096 | -46.57197 | 2025-05-08 03:47:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fb6a2ff8-4dce-3c8d-825e-78853f17e475 | -15.82445 | -46.57732 | 2025-05-08 03:47:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 5.6 |
| fa133db3-b1f0-34a1-8fce-124057c37560 | -23.59995 | -49.00573 | 2025-05-08 03:47:00 | NPP-375D | ITAÍ | SÃO PAULO | Brasil | 3521804 | 35 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2ab2b194-acfd-322d-b50a-e83b417115c3 | -22.67777 | -49.82792 | 2025-05-08 03:47:00 | NPP-375D | SÃO PEDRO DO TURVO | SÃO PAULO | Brasil | 3550506 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 407a1f33-2b01-3914-88c9-ec395e44f91f | -19.43886 | -44.34067 | 2025-05-08 03:47:00 | NPP-375D | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c8c5efc8-ec6e-3c8f-b063-99c7e8ac7369 | -17.78009 | -42.80677 | 2025-05-08 03:47:00 | NPP-375D | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 50ff359b-ab0c-32ef-9d4a-4049371eed11 | -14.64708 | -45.14555 | 2025-05-08 03:47:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 61a5d67e-140f-34f6-9ceb-06b36272e59d | -23.40384 | -46.5569 | 2025-05-08 03:47:00 | NPP-375D | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| fce27d75-4a12-3e7b-9e02-a8eac93821b0 | -14.64432 | -45.1335 | 2025-05-08 03:47:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 12.5 |
| cff43cee-d640-3b63-93b9-db792b97c396 | -14.63637 | -45.13282 | 2025-05-08 03:47:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 31.0 |
| be53eefa-524e-3ac2-8147-487218793607 | -23.60153 | -48.99879 | 2025-05-08 03:47:00 | NPP-375D | ITAÍ | SÃO PAULO | Brasil | 3521804 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ad564f97-f355-3e0d-ab62-6ee7aed3f119 | -23.61116 | -49.00475 | 2025-05-08 03:47:00 | NPP-375D | ITAÍ | SÃO PAULO | Brasil | 3521804 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 67e830a9-414d-37c0-9c47-c394bd5b1e8e | -21.79161 | -52.75513 | 2025-05-08 03:47:00 | NPP-375D | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 685a5eda-1a09-3e97-8b40-f6d5cc20bcff | -14.63671 | -45.12046 | 2025-05-08 03:47:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 37.4 |
| 68101610-7a8e-3188-9804-7fede73f24d5 | -14.63566 | -45.12597 | 2025-05-08 03:47:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 37.4 |
| 0f2b18be-8be2-33bb-b51f-ee6e31fafd6b | -19.97073 | -44.21759 | 2025-05-08 03:47:00 | NPP-375D | BETIM | MINAS GERAIS | Brasil | 3106705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 1d9ab4e4-c509-3cb4-b7c5-59f907f9dfcc | -21.21049 | -42.83669 | 2025-05-08 03:49:00 | NPP-375D | RODEIRO | MINAS GERAIS | Brasil | 3156304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 4465a894-a521-33ad-a0d0-ca81120160d0 | -22.74873 | -43.2742 | 2025-05-08 03:49:00 | NPP-375D | DUQUE DE CAXIAS | RIO DE JANEIRO | Brasil | 3301702 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| d78e8198-cc86-3c67-a91a-738394aad166 | -20.05997 | -49.36258 | 2025-05-08 03:49:00 | NPP-375D | PAULO DE FARIA | SÃO PAULO | Brasil | 3536604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| a4f2236b-9858-3b20-8329-cd7022963205 | -22.85744 | -42.97985 | 2025-05-08 03:49:00 | NPP-375D | SÃO GONÇALO | RIO DE JANEIRO | Brasil | 3304904 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 1a81818e-7c5f-3a33-a597-4b66d85388f4 | -20.06038 | -49.36052 | 2025-05-08 03:49:00 | NPP-375D | PAULO DE FARIA | SÃO PAULO | Brasil | 3536604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| ed91a31f-b9dc-3d25-b734-61e202317f8a | -22.78748 | -43.75628 | 2025-05-08 03:49:00 | NPP-375D | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 3cfb1aa9-e196-39b8-a6ef-c6e6af6e39b5 | -20.91211 | -48.82576 | 2025-05-08 03:49:00 | NPP-375D | CAJOBI | SÃO PAULO | Brasil | 3509304 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 9e0943f1-b56c-3327-8a7a-f9f227afcfd5 | -20.91243 | -48.82556 | 2025-05-08 03:49:00 | NPP-375D | CAJOBI | SÃO PAULO | Brasil | 3509304 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 36d7352f-e15a-3832-b50d-09c4f8bee726 | -22.67863 | -42.85387 | 2025-05-08 03:49:00 | NPP-375D | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 6f311cfc-4436-3ecd-bf23-c731a110201d | -20.05948 | -49.36465 | 2025-05-08 03:49:00 | NPP-375D | PAULO DE FARIA | SÃO PAULO | Brasil | 3536604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 15bc5a67-66d9-350c-a6de-0194251f8ace | -21.11103 | -42.89507 | 2025-05-08 03:49:00 | NPP-375D | UBÁ | MINAS GERAIS | Brasil | 3169901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |


[Clique aqui para ver as próximas entradas](README5.md)
