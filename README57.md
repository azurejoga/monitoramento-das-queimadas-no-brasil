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

## Dados Diários - Página 57

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7e17a038-3f8e-3a5c-be3d-90185e706dd3 | -21.39401 | -45.07851 | 2025-10-06 04:29:00 | NOAA-21 | LAVRAS | MINAS GERAIS | Brasil | 3138203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| 8433d03e-7965-3fc9-bd00-cfe02831ba6c | -17.2874 | -49.27338 | 2025-10-06 04:29:00 | NOAA-21 | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 628355c7-f078-33f1-a5d2-fbc935bceb5d | -19.71078 | -49.29165 | 2025-10-06 04:29:00 | NOAA-21 | ITAPAGIPE | MINAS GERAIS | Brasil | 3133402 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 709b6b8c-cd18-3052-9321-139ea9155078 | -16.96095 | -52.69141 | 2025-10-06 04:29:00 | NOAA-21 | DOVERLÂNDIA | GOIÁS | Brasil | 5207253 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 59e323fd-2ac0-3cfb-abd4-b8151819990e | -22.15121 | -51.4614 | 2025-10-06 04:29:00 | NOAA-21 | PRESIDENTE PRUDENTE | SÃO PAULO | Brasil | 3541406 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 208e243c-7e95-3b85-baa4-e1d6650ebc16 | -19.94437 | -44.64165 | 2025-10-06 04:29:00 | NOAA-21 | IGARATINGA | MINAS GERAIS | Brasil | 3130200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 4b2dee35-1628-371e-a303-dd98ffc90621 | -17.99314 | -57.59878 | 2025-10-06 04:29:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.1 |
| c85a7680-70cc-3f71-a1ba-52f91077bfec | -17.26195 | -46.91986 | 2025-10-06 04:29:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ff3faa75-a92c-3069-81dc-e96fcb7ac5e6 | -22.00653 | -49.74999 | 2025-10-06 04:29:00 | NOAA-21 | GUARANTÃ | SÃO PAULO | Brasil | 3518107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 83358e91-4fe6-35b3-aaca-ad73ff0e640f | -17.97834 | -57.59544 | 2025-10-06 04:29:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 0c4436c6-ad06-3775-abe9-f5f912032d59 | -17.99466 | -57.53959 | 2025-10-06 04:29:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 13.2 |
| f7cc848b-4c47-347f-9c56-9ce98fd6d99a | -17.9797 | -51.13498 | 2025-10-06 04:29:00 | NOAA-21 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b275e374-a7f9-3c62-bf3a-30ea71aa866f | -17.71527 | -56.77097 | 2025-10-06 04:29:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.3 |
| b7c0c1f1-1bff-318e-a1ca-6333bc2d1f80 | -19.48407 | -47.16838 | 2025-10-06 04:29:00 | NOAA-21 | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1966d683-d96a-382a-a557-e245fed2d039 | -21.188 | -45.61464 | 2025-10-06 04:29:00 | NOAA-21 | CAMPOS GERAIS | MINAS GERAIS | Brasil | 3111606 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 06be6323-e264-353b-aeb4-b2925bec5b68 | -21.11016 | -49.95619 | 2025-10-06 04:29:00 | NOAA-21 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 2548cc9b-c380-37f1-bcac-156042aa42da | -23.174 | -46.26303 | 2025-10-06 04:29:00 | NOAA-21 | NAZARÉ PAULISTA | SÃO PAULO | Brasil | 3532405 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 81e679ef-8c31-3775-87f7-d6db66a65b4c | -22.97861 | -48.34291 | 2025-10-06 04:29:00 | NOAA-21 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 4a9cb3ba-b46d-3710-98cd-3d28c89f26d1 | -22.36377 | -44.21283 | 2025-10-06 04:29:00 | NOAA-21 | QUATIS | RIO DE JANEIRO | Brasil | 3304128 | 33 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| 7ac58dbb-0390-3e55-b68e-a7b42f132c8d | -17.99372 | -57.54428 | 2025-10-06 04:29:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 13.2 |
| 8a356b74-5350-3e0a-bfad-7f0c0e21d739 | -18.11802 | -53.41643 | 2025-10-06 04:29:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 39e64c1f-8f84-3f0d-a80e-5dc559c7320f | -17.24886 | -46.91398 | 2025-10-06 04:29:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e18a2dee-22cc-302f-9139-d11c107c9228 | -20.11858 | -44.40202 | 2025-10-06 04:29:00 | NOAA-21 | MATEUS LEME | MINAS GERAIS | Brasil | 3140704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| d251945b-a549-3919-ae9c-c9a917702784 | -22.3892 | -50.02284 | 2025-10-06 04:29:00 | NOAA-21 | MARÍLIA | SÃO PAULO | Brasil | 3529005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| ecb2ee84-8899-3eda-8247-fdd5c0fd7c92 | -21.40112 | -45.05947 | 2025-10-06 04:29:00 | NOAA-21 | INGAÍ | MINAS GERAIS | Brasil | 3130804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| e0e7eba5-c15b-3c97-989e-2f1037375120 | -22.36549 | -50.02238 | 2025-10-06 04:29:00 | NOAA-21 | MARÍLIA | SÃO PAULO | Brasil | 3529005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 555f3388-dba8-36e8-819a-10160d3ac486 | -18.12727 | -53.38649 | 2025-10-06 04:29:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 8fad5c98-b022-3e8c-bf51-4caf6330d402 | -20.78882 | -43.3153 | 2025-10-06 04:29:00 | NOAA-21 | SENHORA DE OLIVEIRA | MINAS GERAIS | Brasil | 3166006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 151f9910-81f3-37c5-9da0-00dd23c28cb0 | -18.25442 | -53.32883 | 2025-10-06 04:29:00 | NOAA-21 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 870864cb-a43c-30ab-b30b-d854b51bd87b | -18.2637 | -53.32042 | 2025-10-06 04:29:00 | NOAA-21 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ab99f328-6aec-3c6a-b771-98bfb0d1849c | -23.39124 | -45.39072 | 2025-10-06 04:29:00 | NOAA-21 | NATIVIDADE DA SERRA | SÃO PAULO | Brasil | 3532306 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.5 |
| ba9710e4-6c34-3019-9baf-f66ee0fb2e1c | -19.03264 | -50.6376 | 2025-10-06 04:29:00 | NOAA-21 | SÃO SIMÃO | GOIÁS | Brasil | 5220405 | 52 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 763f869f-2445-3aa2-b54c-4d4132c12f01 | -18.26922 | -53.33324 | 2025-10-06 04:29:00 | NOAA-21 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 15b6ed17-f773-32fd-b91c-45aa22f774d4 | -19.01674 | -45.02499 | 2025-10-06 04:29:00 | NOAA-21 | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 5e8dbc86-ee0a-3a6d-aee5-c2e5075989eb | -19.6283 | -45.92456 | 2025-10-06 04:29:00 | NOAA-21 | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f2d90f55-ee61-3f8c-a570-6db895e00b0a | -18.2734 | -53.33178 | 2025-10-06 04:29:00 | NOAA-21 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ef0359fc-5aa3-3bba-9dff-6d9f73303be0 | -18.17879 | -53.37984 | 2025-10-06 04:29:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 9b7d084e-acba-3498-8418-700987f43b0b | -15.9903 | -59.54065 | 2025-10-06 04:29:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9149402a-bc86-37df-9f16-ab39906ec27b | -18.61333 | -48.62447 | 2025-10-06 04:29:00 | NOAA-21 | TUPACIGUARA | MINAS GERAIS | Brasil | 3169604 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1aab4c96-f72d-3b1d-94b2-21cd45866f60 | -21.39098 | -45.041 | 2025-10-06 04:29:00 | NOAA-21 | INGAÍ | MINAS GERAIS | Brasil | 3130804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 3119734c-d5af-3f3d-87a9-1c72e20a17c5 | -18.15557 | -53.31389 | 2025-10-06 04:29:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 1d769cad-3f05-3f20-9a2b-4e2300cc2f27 | -21.69685 | -50.05604 | 2025-10-06 04:29:00 | NOAA-21 | GETULINA | SÃO PAULO | Brasil | 3517000 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 31d0fcdd-cafa-3cc0-9e69-c98765972178 | -17.67974 | -52.2437 | 2025-10-06 04:29:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 7.8 |
| b39a7b3b-8f9f-313b-b81d-8033b74e2a99 | -17.67541 | -52.24727 | 2025-10-06 04:29:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 1fcdc15f-b3f6-3c3e-b5e5-cc4137059d9e | -18.19691 | -49.52631 | 2025-10-06 04:29:00 | NOAA-21 | PANAMÁ | GOIÁS | Brasil | 5216007 | 52 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| f36f6ba4-6527-367b-8e0e-952a6799aea3 | -18.25694 | -53.35873 | 2025-10-06 04:29:00 | NOAA-21 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 6.1 |
| cfa9ebce-0880-34c3-b62f-6824bf9ccdb1 | -21.94706 | -46.45792 | 2025-10-06 04:29:00 | NOAA-21 | CALDAS | MINAS GERAIS | Brasil | 3110301 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 71b95a3e-5086-3f06-87d7-a1f9592ce078 | -21.56222 | -48.3307 | 2025-10-06 04:29:00 | NOAA-21 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5dfc642c-9ad0-3f02-bde8-832fc2618cc2 | -16.35815 | -51.48381 | 2025-10-06 04:29:00 | NOAA-21 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6a0ca254-b2da-3da3-be9b-a7c04a093412 | -17.83917 | -57.61628 | 2025-10-06 04:29:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 542060ff-6920-3632-af0d-40f7f7a29311 | -22.28767 | -46.7292 | 2025-10-06 04:29:00 | NOAA-21 | ESPÍRITO SANTO DO PINHAL | SÃO PAULO | Brasil | 3515186 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 8f0416ef-7bfd-31f1-83f7-b7ad6354551e | -22.37748 | -49.96729 | 2025-10-06 04:29:00 | NOAA-21 | OCAUÇU | SÃO PAULO | Brasil | 3533700 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 18d2c34a-8411-3842-adde-576358f28647 | -18.25526 | -53.32404 | 2025-10-06 04:29:00 | NOAA-21 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ac55e384-6b47-3367-838f-52c4bc9e0e91 | -17.7048 | -56.77425 | 2025-10-06 04:29:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.5 |
| c8ffe0cc-47e5-32f3-b49a-068c90184505 | -22.82825 | -45.54611 | 2025-10-06 04:29:00 | NOAA-21 | PINDAMONHANGABA | SÃO PAULO | Brasil | 3538006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 3d22d059-5f1a-3080-b581-ebd62e491192 | -18.11889 | -53.41157 | 2025-10-06 04:29:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 8.6 |
| e9f90824-83c9-384e-845b-25376f30bae8 | -17.53874 | -44.33046 | 2025-10-06 04:29:00 | NOAA-21 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f719bb40-b71f-3f00-9c8b-57cc8911a444 | -22.00925 | -49.75428 | 2025-10-06 04:29:00 | NOAA-21 | JÚLIO MESQUITA | SÃO PAULO | Brasil | 3525805 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| cc09de1b-884b-36e3-8b80-8ed4aea38234 | -22.45121 | -46.86192 | 2025-10-06 04:29:00 | NOAA-21 | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7c26d496-35c4-3689-b896-80044401bde5 | -22.60522 | -44.68829 | 2025-10-06 04:29:00 | NOAA-21 | AREIAS | SÃO PAULO | Brasil | 3503505 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| add65a3f-a7af-3496-a12f-3d6abfda4e66 | -21.69006 | -50.07761 | 2025-10-06 04:29:00 | NOAA-21 | GETULINA | SÃO PAULO | Brasil | 3517000 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| e1efe1b6-476c-3e75-887a-c240b69ed648 | -17.8551 | -57.64007 | 2025-10-06 04:29:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 57efdc94-d7ad-3b86-8909-c80a680f4cde | -17.97341 | -57.59431 | 2025-10-06 04:29:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 9f581397-a83b-334e-9055-e3ef21453d85 | -21.93874 | -51.8298 | 2025-10-06 04:29:00 | NOAA-21 | PRESIDENTE VENCESLAU | SÃO PAULO | Brasil | 3541505 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 7d9ceb9d-afa9-38d5-866c-063281595700 | -19.05425 | -50.65319 | 2025-10-06 04:29:00 | NOAA-21 | SÃO SIMÃO | GOIÁS | Brasil | 5220405 | 52 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 8dbd48da-7ed4-3fd1-801e-d63e1bb3513c | -22.96912 | -47.60128 | 2025-10-06 04:29:00 | NOAA-21 | MOMBUCA | SÃO PAULO | Brasil | 3530904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 93261501-dfd8-3460-a25c-8987844157a0 | -18.00049 | -57.54207 | 2025-10-06 04:29:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 10.3 |
| 1770f0a0-0dde-3751-9112-bad6876ff2e0 | -18.26629 | -53.3279 | 2025-10-06 04:29:00 | NOAA-21 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 52556d05-e025-319f-b93a-92b7de5af518 | -17.65679 | -44.43184 | 2025-10-06 04:29:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 99c2e891-2d4f-3f58-af82-7e8576cc34f7 | -22.36011 | -44.20805 | 2025-10-06 04:29:00 | NOAA-21 | QUATIS | RIO DE JANEIRO | Brasil | 3304128 | 33 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 7d1ba8b7-aa11-3701-8eb0-726660c18e7c | -19.03599 | -50.6382 | 2025-10-06 04:29:00 | NOAA-21 | SÃO SIMÃO | GOIÁS | Brasil | 5220405 | 52 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| d5e63df2-81e5-357c-bb08-f7d59b8b9cb4 | -22.97802 | -48.34694 | 2025-10-06 04:29:00 | NOAA-21 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 1a998847-4728-3429-89cc-e1f99fbe0847 | -17.96482 | -57.53462 | 2025-10-06 04:29:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.9 |
| 0b8bde8e-7d0c-3ae6-ae1d-424dcd65000a | -18.14532 | -53.39529 | 2025-10-06 04:29:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 24efae30-477d-3138-8c0e-8bf5b3b9ea73 | -19.90236 | -43.53884 | 2025-10-06 04:29:00 | NOAA-21 | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 5b23b355-5f60-3fe9-adfe-57372a943983 | -21.29815 | -43.83857 | 2025-10-06 04:29:00 | NOAA-21 | ANTÔNIO CARLOS | MINAS GERAIS | Brasil | 3102902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 1d5d69d7-07c9-31e9-9350-b3ad6486ddcf | -21.30601 | -43.84406 | 2025-10-06 04:29:00 | NOAA-21 | ANTÔNIO CARLOS | MINAS GERAIS | Brasil | 3102902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| a3ede7c3-5c3f-35fb-a9bb-ad942c845760 | -17.96968 | -57.58721 | 2025-10-06 04:29:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| e0a32f0b-3a8b-3a75-834a-6bd1906685a9 | -21.40502 | -45.05997 | 2025-10-06 04:29:00 | NOAA-21 | INGAÍ | MINAS GERAIS | Brasil | 3130804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| f652cf57-eb8c-336e-b25d-ab6b04e00b64 | -17.87602 | -57.58735 | 2025-10-06 04:29:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| d53f8e91-0071-3731-99b4-384cdbb0ad21 | -22.29819 | -49.90798 | 2025-10-06 04:29:00 | NOAA-21 | MARÍLIA | SÃO PAULO | Brasil | 3529005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 1a763768-d39d-3a1b-9e73-d8f1a14918e8 | -18.26715 | -53.32317 | 2025-10-06 04:29:00 | NOAA-21 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 4c777f4d-4ae9-3bd6-8e88-942402392126 | -18.11009 | -53.39478 | 2025-10-06 04:29:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 5.0 |
| b813beff-5452-35a7-9a96-010a86bac0f9 | -18.28136 | -53.33086 | 2025-10-06 04:29:00 | NOAA-21 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| dcd6f18b-ebc5-3003-a07f-fa91a6bbc267 | -17.3921 | -46.64899 | 2025-10-06 04:29:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0d5303b8-9ffc-3d1c-b4f6-d110a45efa4f | -18.2767 | -45.41455 | 2025-10-06 04:29:00 | NOAA-21 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3fbe925f-d569-3e97-a123-5c85cf555971 | -18.11777 | -53.3958 | 2025-10-06 04:29:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 255b15af-aeba-3986-a82a-6b53a140ff39 | -16.72287 | -49.07788 | 2025-10-06 04:29:00 | NOAA-21 | SENADOR CANEDO | GOIÁS | Brasil | 5220454 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 29ea602b-edf7-3c77-a605-15b9050d764c | -21.39462 | -45.07984 | 2025-10-06 04:29:00 | NOAA-21 | LAVRAS | MINAS GERAIS | Brasil | 3138203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 8e1f7f4a-6b34-3fd5-abf8-c5baa7bffa07 | -19.63193 | -45.92513 | 2025-10-06 04:29:00 | NOAA-21 | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 48bd5046-a39c-3986-8079-2009e2927fba | -22.44983 | -46.85958 | 2025-10-06 04:29:00 | NOAA-21 | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 0d33ec4d-0d88-3868-a35d-2c126d1af57c | -18.26332 | -53.32272 | 2025-10-06 04:29:00 | NOAA-21 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 3.8 |
| f7c975ef-8aee-3fb2-b3ff-6260b77e1a23 | -17.85651 | -57.63307 | 2025-10-06 04:29:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 419b86c3-f51f-3de9-875f-e72ca81274db | -18.87917 | -43.74588 | 2025-10-06 04:29:00 | NOAA-21 | CONGONHAS DO NORTE | MINAS GERAIS | Brasil | 3118106 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 548c36b9-0e3b-3259-84f8-d59dfb95ad89 | -21.8687 | -48.29659 | 2025-10-06 04:29:00 | NOAA-21 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| af04970a-915f-3537-98e8-c937b5a2a39d | -22.67982 | -44.92224 | 2025-10-06 04:29:00 | NOAA-21 | CACHOEIRA PAULISTA | SÃO PAULO | Brasil | 3508603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 2cedb30f-079d-375f-949b-9f42d8ce8704 | -17.98879 | -57.54323 | 2025-10-06 04:29:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 13.2 |
| cc0c38ac-1b3f-3790-b002-4cef20438855 | -19.02894 | -50.66022 | 2025-10-06 04:29:00 | NOAA-21 | SÃO SIMÃO | GOIÁS | Brasil | 5220405 | 52 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| bdb367eb-26a6-33d5-ada1-59560c31f488 | -17.98054 | -51.15118 | 2025-10-06 04:29:00 | NOAA-21 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a11f43c9-c27d-3dce-8b07-77b89844d8bf | -17.96267 | -57.59639 | 2025-10-06 04:29:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |


[Clique aqui para ver as próximas entradas](README58.md)
