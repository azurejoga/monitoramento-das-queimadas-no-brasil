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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9f441303-eb65-3e2d-9d61-e7614e17fb14 | -21.07506 | -46.90891 | 2025-10-07 00:09:00 | TERRA_M-M | MONTE SANTO DE MINAS | MINAS GERAIS | Brasil | 3143203 | 31 | 33 | nan | nan | nan | Cerrado | 13.8 |
| c3aaf9dd-b19e-3dcc-a7c4-60ec5a024bbb | -21.49115 | -46.02269 | 2025-10-07 00:09:00 | TERRA_M-M | ALFENAS | MINAS GERAIS | Brasil | 3101607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 59.1 |
| acfd54be-36c9-3611-a226-c2e3353c247c | -18.59895 | -46.79642 | 2025-10-07 00:09:00 | TERRA_M-M | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 20.1 |
| 623108b2-b781-38e8-a99a-5a6e97e03554 | -19.84194 | -41.82936 | 2025-10-07 00:09:00 | TERRA_M-M | SIMONÉSIA | MINAS GERAIS | Brasil | 3167608 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.0 |
| 486d4656-b120-366a-a615-f88c1fd28d04 | -20.49732 | -42.7335 | 2025-10-07 00:09:00 | TERRA_M-M | JEQUERI | MINAS GERAIS | Brasil | 3135506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 38.1 |
| 6fc6098f-0c97-3130-9ace-c36abc3621a2 | -23.11981 | -46.09496 | 2025-10-07 00:09:00 | TERRA_M-M | IGARATÁ | SÃO PAULO | Brasil | 3520202 | 35 | 33 | nan | nan | nan | Mata Atlântica | 23.8 |
| 2fcf97d0-15d7-38f3-85a0-1bc2e9b74306 | -23.20705 | -47.81745 | 2025-10-07 00:09:00 | TERRA_M-M | CERQUILHO | SÃO PAULO | Brasil | 3511508 | 35 | 33 | nan | nan | nan | Mata Atlântica | 28.4 |
| 5a345223-845b-35c7-82b9-c2bbe2d158b4 | -19.59323 | -47.20961 | 2025-10-07 00:09:00 | TERRA_M-M | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 24.2 |
| 5cb82cc6-51da-3654-ad60-e2ee04529bd4 | -18.52707 | -43.41887 | 2025-10-07 00:09:00 | TERRA_M-M | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.8 |
| 5fde0846-0d82-30d3-b106-b7b3c1ee10c9 | -18.55547 | -41.57874 | 2025-10-07 00:09:00 | TERRA_M-M | NOVA MÓDICA | MINAS GERAIS | Brasil | 3144904 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| afa6d318-622e-36a3-8d6a-6d750122b6f9 | -20.10406 | -44.20158 | 2025-10-07 00:09:00 | TERRA_M-M | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 67.3 |
| 8d409213-ffda-3e82-af08-74e80945370e | -18.04976 | -43.14362 | 2025-10-07 00:09:00 | TERRA_M-M | SENADOR MODESTINO GONÇALVES | MINAS GERAIS | Brasil | 3165909 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| 41abb5a2-591b-3a83-9337-dbde08de9b7b | -21.10941 | -43.85622 | 2025-10-07 00:09:00 | TERRA_M-M | RESSAQUINHA | MINAS GERAIS | Brasil | 3154408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 23.5 |
| becfdfb0-1acc-3a66-9b2a-f6d3a3ded5ae | -21.10802 | -43.84507 | 2025-10-07 00:09:00 | TERRA_M-M | RESSAQUINHA | MINAS GERAIS | Brasil | 3154408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 14.2 |
| 86086b5b-2dae-376a-a077-f81d03bbe5ba | -21.07365 | -45.0725 | 2025-10-07 00:09:00 | TERRA_M-M | PERDÕES | MINAS GERAIS | Brasil | 3149903 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.4 |
| 9ebdd235-4a3f-343b-8103-569741f44fb7 | -23.10744 | -46.19565 | 2025-10-07 00:09:00 | TERRA_M-M | IGARATÁ | SÃO PAULO | Brasil | 3520202 | 35 | 33 | nan | nan | nan | Mata Atlântica | 11.3 |
| 0339ca43-654c-3186-a91e-15398c9c36cc | -22.38381 | -49.99336 | 2025-10-07 00:09:00 | TERRA_M-M | MARÍLIA | SÃO PAULO | Brasil | 3529005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 33.7 |
| eb7d0d9a-5988-37ac-82a7-651b746adbca | -18.57143 | -44.19004 | 2025-10-07 00:09:00 | TERRA_M-M | PRESIDENTE JUSCELINO | MINAS GERAIS | Brasil | 3153202 | 31 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 2dd14379-eca4-3278-a781-884cdfad8294 | -23.20519 | -47.81084 | 2025-10-07 00:09:00 | TERRA_M-M | CERQUILHO | SÃO PAULO | Brasil | 3511508 | 35 | 33 | nan | nan | nan | Mata Atlântica | 24.6 |
| cbc010ee-7a29-39ed-b971-d6cbb46dd022 | -21.90457 | -44.88638 | 2025-10-07 00:09:00 | TERRA_M-M | BAEPENDI | MINAS GERAIS | Brasil | 3104908 | 31 | 33 | nan | nan | nan | Mata Atlântica | 43.3 |
| 303374dd-0087-37c4-a934-7f23e8e24bf4 | -19.64577 | -42.00576 | 2025-10-07 00:09:00 | TERRA_M-M | UBAPORANGA | MINAS GERAIS | Brasil | 3170057 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.5 |
| 32a81165-4fe6-3b87-b0fa-8af1f78aed0f | -20.98765 | -45.58048 | 2025-10-07 00:09:00 | TERRA_M-M | BOA ESPERANÇA | MINAS GERAIS | Brasil | 3107109 | 31 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 78d31033-6070-3384-8e6c-f9f3380e8ca0 | -20.90849 | -48.85519 | 2025-10-07 00:09:00 | TERRA_M-M | CAJOBI | SÃO PAULO | Brasil | 3509304 | 35 | 33 | nan | nan | nan | Mata Atlântica | 17.7 |
| 1cf7cd7c-96ad-3e43-b017-3ca1f222dc10 | -19.9333 | -44.65007 | 2025-10-07 00:09:00 | TERRA_M-M | IGARATINGA | MINAS GERAIS | Brasil | 3130200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| cb2951ab-0cd5-359e-8863-ed066d26030f | -19.93181 | -44.63805 | 2025-10-07 00:09:00 | TERRA_M-M | PARÁ DE MINAS | MINAS GERAIS | Brasil | 3147105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.8 |
| 66ffd06d-fc79-305f-9013-42a71805d5a3 | -21.30028 | -45.95231 | 2025-10-07 00:09:00 | TERRA_M-M | ALFENAS | MINAS GERAIS | Brasil | 3101607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 19.1 |
| df340db7-79c9-3b92-8437-60ef2ddc9b64 | -23.12159 | -46.11127 | 2025-10-07 00:09:00 | TERRA_M-M | IGARATÁ | SÃO PAULO | Brasil | 3520202 | 35 | 33 | nan | nan | nan | Mata Atlântica | 23.9 |
| a946ad7b-f797-3024-b328-d6cffb5f19b7 | -18.92573 | -49.47956 | 2025-10-07 00:09:00 | TERRA_M-M | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Mata Atlântica | 21.9 |
| deb3b19f-283e-38c3-a73f-3945f1aa69b7 | -20.11898 | -44.4054 | 2025-10-07 00:09:00 | TERRA_M-M | MATEUS LEME | MINAS GERAIS | Brasil | 3140704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 48.0 |
| 9da20f76-8a2d-3e65-9f4c-058a6811d4e5 | -21.49361 | -46.03201 | 2025-10-07 00:09:00 | TERRA_M-M | ALFENAS | MINAS GERAIS | Brasil | 3101607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 45.3 |
| 5c6f9dd1-9abc-3eb4-8268-9b24868872d7 | -21.90757 | -44.8917 | 2025-10-07 00:09:00 | TERRA_M-M | BAEPENDI | MINAS GERAIS | Brasil | 3104908 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.2 |
| cca515f4-9fe3-3f11-987f-d3db809dc2d7 | -22.57631 | -44.44378 | 2025-10-07 00:09:00 | TERRA_M-M | RESENDE | RIO DE JANEIRO | Brasil | 3304201 | 33 | 33 | nan | nan | nan | Mata Atlântica | 9.1 |
| 8825c3de-655e-3e89-9fd1-5c2e05252ccd | -20.90615 | -48.83091 | 2025-10-07 00:09:00 | TERRA_M-M | CAJOBI | SÃO PAULO | Brasil | 3509304 | 35 | 33 | nan | nan | nan | Mata Atlântica | 85.8 |
| c24390bf-fa3e-30ea-a601-e519dc1755ea | -22.57787 | -44.45678 | 2025-10-07 00:09:00 | TERRA_M-M | RESENDE | RIO DE JANEIRO | Brasil | 3304201 | 33 | 33 | nan | nan | nan | Mata Atlântica | 10.1 |
| fee7b051-899a-3175-8396-8b223185f281 | -22.5477 | -44.46116 | 2025-10-07 00:09:00 | TERRA_M-M | RESENDE | RIO DE JANEIRO | Brasil | 3304201 | 33 | 33 | nan | nan | nan | Mata Atlântica | 8.7 |
| 096184df-8bba-322a-bcc6-a8c9b2713b1a | -18.84089 | -48.29846 | 2025-10-07 00:09:00 | TERRA_M-M | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 57797ed9-830c-3ead-8708-6e3315c8e004 | -20.10543 | -44.21277 | 2025-10-07 00:09:00 | TERRA_M-M | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.1 |
| 6981df4d-f45d-381e-87e9-b83377aa7973 | -22.38642 | -50.02378 | 2025-10-07 00:09:00 | TERRA_M-M | MARÍLIA | SÃO PAULO | Brasil | 3529005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 16.2 |
| 53feb147-b3fa-3c93-a85d-130401589e77 | -18.78019 | -44.62633 | 2025-10-07 00:09:00 | TERRA_M-M | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 6b4e2f8b-0d44-3afb-a1e7-799e06373d95 | -20.12038 | -44.41699 | 2025-10-07 00:09:00 | TERRA_M-M | MATEUS LEME | MINAS GERAIS | Brasil | 3140704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 33.5 |
| 1b16f85c-0421-36d7-84c4-1419504b8d96 | -21.03868 | -40.95243 | 2025-10-07 00:09:00 | TERRA_M-M | ITAPEMIRIM | ESPÍRITO SANTO | Brasil | 3202801 | 32 | 33 | nan | nan | nan | Mata Atlântica | 17.2 |
| 7404f7e5-9b3b-3ec4-a202-c57a1981161d | -18.67284 | -44.04008 | 2025-10-07 00:09:00 | TERRA_M-M | PRESIDENTE JUSCELINO | MINAS GERAIS | Brasil | 3153202 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| f8b6e618-b1cc-3105-96d5-371b5df42760 | -20.20949 | -43.92196 | 2025-10-07 00:09:00 | TERRA_M-M | NOVA LIMA | MINAS GERAIS | Brasil | 3144805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.8 |
| 04a763d3-d27e-3a77-9240-7b4afdf5e100 | -22.01616 | -49.74818 | 2025-10-07 00:09:00 | TERRA_M-M | JÚLIO MESQUITA | SÃO PAULO | Brasil | 3525805 | 35 | 33 | nan | nan | nan | Mata Atlântica | 30.3 |
| a4759549-2262-37df-8507-ba8e1c48864f | -21.49198 | -46.01685 | 2025-10-07 00:09:00 | TERRA_M-M | ALFENAS | MINAS GERAIS | Brasil | 3101607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 49.3 |
| 6d0a0098-c69b-3132-a981-c0ff18b89a93 | -20.8925 | -48.83218 | 2025-10-07 00:09:00 | TERRA_M-M | CAJOBI | SÃO PAULO | Brasil | 3509304 | 35 | 33 | nan | nan | nan | Mata Atlântica | 61.7 |
| b7d2176d-298a-3071-b57b-71585e1d2704 | -20.10265 | -44.19002 | 2025-10-07 00:09:00 | TERRA_M-M | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.2 |
| 63d91605-2435-314d-ba9c-d238c36c2535 | -21.0999 | -43.85767 | 2025-10-07 00:09:00 | TERRA_M-M | CARANDAÍ | MINAS GERAIS | Brasil | 3113206 | 31 | 33 | nan | nan | nan | Mata Atlântica | 17.1 |
| e9022557-df40-35fa-907a-615a20ebd564 | -21.3655 | -45.04077 | 2025-10-07 00:09:00 | TERRA_M-M | LAVRAS | MINAS GERAIS | Brasil | 3138203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.3 |
| a1b10896-e692-3b03-baed-e0d84f235a70 | -20.1139 | -44.4085 | 2025-10-07 00:10:00 | GOES-19 | MATEUS LEME | MINAS GERAIS | Brasil | 3140704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 76.9 |
| b8568fd0-d34a-3aa9-aec7-43db762cf3d2 | -12.4267 | -45.6136 | 2025-10-07 00:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 135.0 |
| 9e2dddf6-0db5-3554-8339-ee075a469b7a | -18.1574 | -53.3485 | 2025-10-07 00:10:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 71.5 |
| 1e28471c-711c-3d98-a1ce-416cc36dd105 | -6.4543 | -44.5749 | 2025-10-07 00:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 113.2 |
| 01008748-55ed-38da-9b5e-2946d67ee0d7 | -7.2964 | -44.799 | 2025-10-07 00:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 122.1 |
| 6a6bf8bb-9795-3fac-b42d-2fd8d1c84138 | -8.6133 | -44.896 | 2025-10-07 00:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 57.9 |
| 605bf2c4-dbf8-3ef0-b284-42c2afdf9890 | -14.7199 | -45.9942 | 2025-10-07 00:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 64.6 |
| afb0079b-8b64-35b3-9003-c52e73c74390 | -15.6003 | -52.5742 | 2025-10-07 00:10:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 107.7 |
| ea6f2dfa-0b61-3ca9-9910-ffe0efde37c8 | -15.6198 | -52.5715 | 2025-10-07 00:10:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 128.6 |
| 63160836-23c5-3ffd-bb1f-c0374456277a | -8.6519 | -46.2964 | 2025-10-07 00:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 86.8 |
| 9073f241-fc28-344b-897c-a6cadae9b780 | -10.8731 | -51.0289 | 2025-10-07 00:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 186.3 |
| de36620c-abbd-3592-ad49-3a8527465943 | -14.8832 | -51.4561 | 2025-10-07 00:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 117.2 |
| e9ddd640-592f-325d-b982-d08d8833f427 | -18.0977 | -53.3579 | 2025-10-07 00:10:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 68.4 |
| b71a3163-b734-3490-b07d-596d99571ecc | -8.6521 | -46.274 | 2025-10-07 00:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 81.6 |
| ebda353f-739a-371e-bccf-5cfa78370ef5 | -6.2421 | -43.2743 | 2025-10-07 00:10:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 55.1 |
| e5ab4095-9216-3a27-a9a4-40efd275aca2 | -11.7401 | -43.2928 | 2025-10-07 00:10:00 | GOES-19 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 123.7 |
| 5df94e0a-a76d-3fbc-bf10-e9dffc5e9ee3 | -18.1565 | -53.3915 | 2025-10-07 00:10:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 62.9 |
| bc937df5-87b5-36b0-8380-f77ac049c533 | -8.6127 | -44.9418 | 2025-10-07 00:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 146.9 |
| ab265821-eac8-3110-8c04-1841903b2ab7 | -8.174 | -50.3035 | 2025-10-07 00:10:00 | GOES-19 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 96.4 |
| 931fa1e0-6b28-30c2-a2ff-ccda0f4d0826 | -5.4937 | -43.0761 | 2025-10-07 00:10:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 46.9 |
| 9b33528f-4e41-38b2-91c0-21a20e267198 | -8.1927 | -50.3019 | 2025-10-07 00:10:00 | GOES-19 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 80.7 |
| bf7d1b72-171f-3098-a3c1-64198e4a0f17 | -22.3337 | -49.8867 | 2025-10-07 00:10:00 | GOES-19 | VERA CRUZ | SÃO PAULO | Brasil | 3556602 | 35 | 33 | nan | nan | nan | Mata Atlântica | 94.4 |
| 2fd04457-7a9b-3a27-8534-f767e0e5da6e | -3.0864 | -50.5835 | 2025-10-07 00:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 51.8 |
| 7762fefd-a2d1-395f-94a8-a73d28815cfe | -13.541 | -42.9835 | 2025-10-07 00:10:00 | GOES-19 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 66.5 |
| 0734ba1a-a9ab-3a0f-8f83-d1cac1643718 | -18.1172 | -53.3763 | 2025-10-07 00:10:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 69.6 |
| f36599bc-9da5-396e-967f-af6eaa55eccb | -14.8641 | -51.4373 | 2025-10-07 00:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 98.7 |
| 7e37ca4c-3265-396a-bf88-362e40168ce9 | -14.9362 | -46.8049 | 2025-10-07 00:10:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 60.9 |
| 464cb8ec-4938-31c2-beff-2963dd4d765d | -8.633 | -46.2984 | 2025-10-07 00:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 70.3 |
| c55d7661-62f7-364d-aef9-3e91a239d2c3 | -4.1367 | -47.6653 | 2025-10-07 00:10:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 51.6 |
| f39fa676-3939-37ea-9663-ede53588430e | -7.4623 | -63.6146 | 2025-10-07 00:10:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 67.9 |
| 77901e1b-cad6-3864-82ca-0d8a57f41860 | -4.6875 | -45.828 | 2025-10-07 00:10:00 | GOES-19 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 85.1 |
| 4ae54a98-c0d1-32ef-9f12-4c9b0421e66c | -8.613 | -44.9189 | 2025-10-07 00:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 280.9 |
| 5800cc5a-787f-334c-85c2-a5a603016b88 | -18.1769 | -53.3669 | 2025-10-07 00:10:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 69.4 |
| 560690e6-c122-3057-be66-ba96523a27ea | -15.6202 | -52.5501 | 2025-10-07 00:10:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 112.0 |
| 5c690fda-b016-3dfc-b8ec-e741a1cec5c1 | -22.3128 | -49.8915 | 2025-10-07 00:10:00 | GOES-19 | MARÍLIA | SÃO PAULO | Brasil | 3529005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 82.4 |
| 5a0b7561-8266-3065-98e8-18f16e10297a | -7.2966 | -44.7761 | 2025-10-07 00:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 71.1 |
| 7955c460-37c4-3efc-bb93-c7d25534f0be | -14.7003 | -45.9976 | 2025-10-07 00:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 81.3 |
| 0a2f6a28-1d4c-3626-825d-0df076d035e2 | -22.3343 | -49.8635 | 2025-10-07 00:10:00 | GOES-19 | VERA CRUZ | SÃO PAULO | Brasil | 3556602 | 35 | 33 | nan | nan | nan | Mata Atlântica | 87.6 |
| 3e25de26-5a84-328f-86e8-025f32b7b16a | -14.8835 | -51.4346 | 2025-10-07 00:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 206.8 |
| 58c3a2f2-5087-3af9-b57b-fef7104e0f1c | -12.9103 | -54.7352 | 2025-10-07 00:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 69.8 |
| c8fdf7ae-931f-3f41-8206-9c6e2d8baa61 | -4.6873 | -45.8504 | 2025-10-07 00:10:00 | GOES-19 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 85.4 |
| 4ca42e78-fd45-3ddb-b927-1ee719425eee | -8.6333 | -46.2759 | 2025-10-07 00:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 66.2 |
| 4750727b-7b8d-3f1c-b530-9dcca6173773 | -8.501 | -46.3117 | 2025-10-07 00:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 70.7 |
| dfbe9bd1-563c-33b8-b342-c6f343f6c903 | -18.157 | -53.37 | 2025-10-07 00:10:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 103.9 |
| 3bb4bcf5-58de-30e2-858f-ce01b22fe3b3 | -10.3913 | -50.313 | 2025-10-07 00:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 87.1 |
| d7946cc9-9081-3fb0-a8f1-655d4eb92ac7 | -14.9166 | -46.8083 | 2025-10-07 00:10:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 101.7 |
| 6b844ea0-08b7-3631-9fe5-41d6af292ce8 | -12.4271 | -45.5906 | 2025-10-07 00:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 49.0 |
| b5339fd4-2dd2-36c5-9104-8549819833df | -6.2609 | -43.2727 | 2025-10-07 00:10:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 48.6 |
| 5177fe8a-7560-3043-8414-bab77e1784e2 | -15.6007 | -52.5529 | 2025-10-07 00:10:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 109.5 |
| 1536dfa4-d7dd-369a-aabb-d049bba1c49a | -22.0071 | -49.7321 | 2025-10-07 00:10:00 | GOES-19 | GUARANTÃ | SÃO PAULO | Brasil | 3518107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 105.2 |
| a6b25c8d-e431-331b-b7f2-2e0e91e56b29 | -23.0614 | -49.8998 | 2025-10-07 00:10:00 | GOES-19 | JACAREZINHO | PARANÁ | Brasil | 4111803 | 41 | 33 | nan | nan | nan | Mata Atlântica | 68.7 |


[Clique aqui para ver as próximas entradas](README3.md)
