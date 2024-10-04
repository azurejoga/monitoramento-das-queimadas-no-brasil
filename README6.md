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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5ea67e4c-785c-3c12-a713-3e018c062dab | -14.8134 | -48.0243 | 2024-10-04 00:36:29 | GOES-16 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 83.3 |
| a03ac760-05bd-3115-b4f9-82e39d53dcc2 | -16.1094 | -50.4489 | 2024-10-04 00:36:36 | GOES-16 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 58.1 |
| 8210d6d7-3b14-33f1-b164-c32cfd4ccecb | -16.4148 | -57.4028 | 2024-10-04 00:36:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 59.7 |
| 118a2f10-8f4e-3179-82c1-49eefc672a5d | -16.4151 | -57.3823 | 2024-10-04 00:36:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 66.7 |
| 1dbcd8cc-41df-3d9e-8b1d-95ccc3449151 | -16.4554 | -57.2962 | 2024-10-04 00:36:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 62.1 |
| 68774447-85e8-3a74-bbbb-0713df13a07c | -16.475 | -57.294 | 2024-10-04 00:36:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 58.2 |
| a5ab323d-6873-3ad3-aff6-7c9b5fa44577 | -16.5537 | -57.2442 | 2024-10-04 00:36:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 72.1 |
| 736ab8d7-3a11-39dd-8dc4-c3fae5c7cf0c | -16.573 | -57.2624 | 2024-10-04 00:36:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 113.6 |
| 8c5b47e3-dc56-355a-9e3c-c453c510317f | -16.5733 | -57.2419 | 2024-10-04 00:36:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 143.8 |
| ce29fdc8-b351-329d-805d-b867feaa7790 | -16.5736 | -57.2215 | 2024-10-04 00:36:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 109.8 |
| 859d365d-2172-39b8-b15d-04dd8417da03 | -16.5783 | -58.198 | 2024-10-04 00:36:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 43.4 |
| 165d1925-92b6-3cff-9590-25e803ec5633 | -16.5925 | -57.2602 | 2024-10-04 00:36:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 141.2 |
| e8ae37ba-0235-336f-9e08-810aa27cc226 | -16.5928 | -57.2397 | 2024-10-04 00:36:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 130.0 |
| 92da57f0-5530-3197-adc6-9ccfb9ee513b | -16.5938 | -57.1783 | 2024-10-04 00:36:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 78.3 |
| 797794cb-8948-371d-abb7-5443cf60b086 | -16.9302 | -47.1224 | 2024-10-04 00:36:40 | GOES-16 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 95.3 |
| 28008da5-8d3d-31a9-8c3b-94bf8c65f721 | -16.613 | -57.1965 | 2024-10-04 00:36:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 81.5 |
| c5349b3f-9946-3d99-b138-13ee63815a59 | -16.6133 | -57.176 | 2024-10-04 00:36:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 107.0 |
| bd1b8e33-f001-3f95-8059-b8e553b52a8a | -16.7606 | -57.7512 | 2024-10-04 00:36:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 46.7 |
| 91ac58f1-8d46-334d-9495-b1b7a0c3c690 | -16.779 | -57.8306 | 2024-10-04 00:36:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 48.1 |
| b709e00a-08c8-3b98-8331-2f38e20be4b2 | -16.7985 | -57.8284 | 2024-10-04 00:36:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 42.9 |
| 6cb6206a-db24-3682-852c-b6c7678e1f42 | -16.843 | -57.4767 | 2024-10-04 00:36:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 55.7 |
| 0e5d67b1-3ae7-3196-99bf-f64020545107 | -16.9087 | -55.843 | 2024-10-04 00:36:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 76.4 |
| 420ac910-b867-394d-b7f4-02a11e5dd6fb | -16.9283 | -55.8405 | 2024-10-04 00:36:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 105.2 |
| a0dadb05-289b-3b87-90e4-b29d061a775c | -16.9287 | -55.8197 | 2024-10-04 00:36:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 72.6 |
| 8dca260a-3ca8-36ab-bf9c-652f9976fdc8 | -17.0616 | -56.0723 | 2024-10-04 00:36:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 59.5 |
| b12a9807-aa09-3d98-83bb-09c65c7c6623 | -18.8413 | -42.8985 | 2024-10-04 00:36:50 | GOES-16 | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 81.5 |
| 8cbd0acd-31de-329c-b07e-bf75ffdca766 | -18.8609 | -42.9182 | 2024-10-04 00:36:50 | GOES-16 | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 91.8 |
| 7252387b-886e-3d3a-9b75-8fe839520c9f | -18.8617 | -42.8932 | 2024-10-04 00:36:50 | GOES-16 | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 108.7 |
| c09809df-98bb-3c8b-ab8d-470a223acdf0 | -18.8613 | -43.5837 | 2024-10-04 00:36:50 | GOES-16 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 123.4 |
| 8e5638d6-aa3c-3645-85c2-6d2a7860755f | -19.4899 | -42.8746 | 2024-10-04 00:36:53 | GOES-16 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 116.8 |
| d339e201-b095-354d-902d-c4d8e0558aa3 | -19.5104 | -42.8691 | 2024-10-04 00:36:53 | GOES-16 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 70.7 |
| c46ac47c-128a-37ae-ac55-d9d647f00767 | -19.9907 | -48.6913 | 2024-10-04 00:36:57 | GOES-16 | PLANURA | MINAS GERAIS | Brasil | 3151602 | 31 | 33 | nan | nan | nan | Cerrado | 127.6 |
| 89e64f6d-348e-312e-8f0e-8f7b655cb373 | -20.0111 | -48.6869 | 2024-10-04 00:36:57 | GOES-16 | PLANURA | MINAS GERAIS | Brasil | 3151602 | 31 | 33 | nan | nan | nan | Cerrado | 139.7 |
| 37c46250-5d77-3ad5-9383-81f565ba98bf | -20.4591 | -43.1795 | 2024-10-04 00:36:58 | GOES-16 | DIOGO DE VASCONCELOS | MINAS GERAIS | Brasil | 3121704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 151.2 |
| 39723eff-3a1e-353f-968a-de2df50ba79e | -21.3334 | -48.8044 | 2024-10-04 00:37:04 | GOES-16 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 129.5 |
| 6b214e9a-6e92-3553-b191-a699ead0769e | -21.3541 | -48.7996 | 2024-10-04 00:37:04 | GOES-16 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 120.5 |
| a4081d35-30b7-3bcb-8358-b1d7b53ee437 | -21.7988 | -48.3691 | 2024-10-04 00:37:06 | GOES-16 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 98.7 |
| 4a666f83-5e42-3ac9-9b8f-79e9e4c1493a | -21.8175 | -48.4346 | 2024-10-04 00:37:06 | GOES-16 | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 83.7 |
| b6579930-aadf-3864-afd8-06239a608988 | -21.8189 | -48.3876 | 2024-10-04 00:37:06 | GOES-16 | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 91.7 |
| c437bca5-2faa-3d34-a29b-09d49e43d096 | -21.8196 | -48.3641 | 2024-10-04 00:37:06 | GOES-16 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 108.0 |
| 97fec902-90c6-300e-953c-08ee232e2660 | -21.8376 | -48.4531 | 2024-10-04 00:37:06 | GOES-16 | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 99.7 |
| 2871b0fd-6a15-369b-b1db-245722f345c4 | -21.8383 | -48.4296 | 2024-10-04 00:37:06 | GOES-16 | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 132.0 |
| afb73325-e01b-30fd-a2cb-277e20f59743 | -21.8591 | -48.4245 | 2024-10-04 00:37:06 | GOES-16 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 85.7 |
| 458f0afd-f52f-353c-991d-b4c913d60442 | -22.830099 | -47.0434 | 2024-10-04 00:40:03 | METOP-C | CAMPINAS | SÃO PAULO | Brasil | 3509502 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| e8c12e2b-ce07-3bdd-8f71-efe7246397e5 | -22.8319 | -47.052299 | 2024-10-04 00:40:03 | METOP-C | CAMPINAS | SÃO PAULO | Brasil | 3509502 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 5f851b72-2b84-36a7-8113-6c10af00043e | -22.3848 | -47.893299 | 2024-10-04 00:40:13 | METOP-C | ITIRAPINA | SÃO PAULO | Brasil | 3523602 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 94afa4d4-5a68-3fad-b49b-e70ef37137d5 | -22.3867 | -47.903 | 2024-10-04 00:40:13 | METOP-C | ITIRAPINA | SÃO PAULO | Brasil | 3523602 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 96883c47-3bdb-3116-a93d-25deef5891d1 | -22.183701 | -47.594101 | 2024-10-04 00:40:15 | METOP-C | CORUMBATAÍ | SÃO PAULO | Brasil | 3512704 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 4d5f40d9-e125-3d1c-85d5-bb1e529227f0 | -22.185499 | -47.603298 | 2024-10-04 00:40:15 | METOP-C | CORUMBATAÍ | SÃO PAULO | Brasil | 3512704 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 753461c6-1641-367f-a6a7-f75d9349e8cc | -21.7575 | -45.548401 | 2024-10-04 00:40:16 | METOP-C | MONSENHOR PAULO | MINAS GERAIS | Brasil | 3142601 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 0f2a423a-c3f4-326f-bbd2-cb1bc3d7df0d | -22.3783 | -49.251202 | 2024-10-04 00:40:17 | METOP-C | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| db749650-67ef-31f5-98f7-a5feefad7986 | -21.0744 | -42.8568 | 2024-10-04 00:40:17 | METOP-C | VISCONDE DO RIO BRANCO | MINAS GERAIS | Brasil | 3172004 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 4fe9fa27-2dac-3d88-925e-db8d52c834a1 | -21.076099 | -42.864399 | 2024-10-04 00:40:17 | METOP-C | VISCONDE DO RIO BRANCO | MINAS GERAIS | Brasil | 3172004 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 862e4a42-d082-3b2a-bfe3-b4d8e219a3b6 | -21.325899 | -44.022301 | 2024-10-04 00:40:17 | METOP-C | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| a2f19b0d-ece0-3dd9-acab-8721b35c50af | -21.327499 | -44.029701 | 2024-10-04 00:40:17 | METOP-C | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 75de5905-a639-349a-986f-d4a0ac9e0030 | -22.071699 | -48.487099 | 2024-10-04 00:40:20 | METOP-C | BOCAINA | SÃO PAULO | Brasil | 3506805 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| e887d1a0-4dcb-3306-91c3-ec5b7e00aea2 | -22.0737 | -48.497398 | 2024-10-04 00:40:20 | METOP-C | BOCAINA | SÃO PAULO | Brasil | 3506805 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 628372de-3bc2-376b-ad81-b0545c40bc1b | -21.308901 | -44.8405 | 2024-10-04 00:40:20 | METOP-C | ITUMIRIM | MINAS GERAIS | Brasil | 3134301 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 5613e4b7-f4cc-3004-974e-7c6bc832175a | -21.884199 | -48.411499 | 2024-10-04 00:40:23 | METOP-C | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 2383c43a-e481-309a-96dd-5fd8d55e2252 | -21.8862 | -48.4216 | 2024-10-04 00:40:23 | METOP-C | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| a29e5e05-7fd5-30f2-bbfd-e352d456c4f3 | -21.855101 | -48.365601 | 2024-10-04 00:40:23 | METOP-C | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 032e9ddd-ed4d-31c3-a77e-5288211015f3 | -21.8433 | -48.3578 | 2024-10-04 00:40:23 | METOP-C | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 34212765-a3eb-3eef-8b0d-cfa7a6177bf2 | -21.845301 | -48.367699 | 2024-10-04 00:40:23 | METOP-C | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| d55fce0f-1b1a-37c7-85b4-9377546e3c66 | -21.8472 | -48.377701 | 2024-10-04 00:40:23 | METOP-C | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| e4b62608-6e76-3e1d-92d1-025b6ba41280 | -21.8375 | -48.379799 | 2024-10-04 00:40:24 | METOP-C | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 1876ca32-36d5-30fd-8fc9-4bacdb8d0d8d | -21.8452 | -48.419899 | 2024-10-04 00:40:24 | METOP-C | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 76006d07-910f-3036-969c-45df9f74d1ab | -21.8472 | -48.43 | 2024-10-04 00:40:24 | METOP-C | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 6d0b9455-063c-3c1d-b6ae-9bc04feeae74 | -21.823799 | -48.362 | 2024-10-04 00:40:24 | METOP-C | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| b967016c-4313-3dd9-bfd3-7c10a1937729 | -21.8258 | -48.371899 | 2024-10-04 00:40:24 | METOP-C | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 31211f6e-e7d4-3324-8243-27237b13932d | -21.8277 | -48.381901 | 2024-10-04 00:40:24 | METOP-C | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| fdf62cae-36d7-37ac-ba44-50c1631f535a | -21.829599 | -48.391899 | 2024-10-04 00:40:24 | METOP-C | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 1c2127fc-f3cd-3ded-999a-1ccd03c6f2c7 | -21.8354 | -48.422001 | 2024-10-04 00:40:24 | METOP-C | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 81460337-5d22-3638-a0f2-4d98d1c9ce67 | -21.8374 | -48.432098 | 2024-10-04 00:40:24 | METOP-C | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 22dbd54e-97cf-3574-ae77-680914ff615d | -21.8393 | -48.442101 | 2024-10-04 00:40:24 | METOP-C | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 5e29b813-5b66-34cc-bbae-d659d01abbba | -21.8412 | -48.452202 | 2024-10-04 00:40:24 | METOP-C | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 07bc46e8-3a41-313e-bb7f-19ad4e032cfd | -21.816 | -48.374001 | 2024-10-04 00:40:24 | METOP-C | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| d0d7891d-a943-3b5c-a6c7-c55862fe0901 | -21.8256 | -48.424099 | 2024-10-04 00:40:24 | METOP-C | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 7feb4108-d25d-3cd1-80aa-fbc98750347d | -21.8276 | -48.4342 | 2024-10-04 00:40:24 | METOP-C | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| fb18837c-78f4-3768-bade-5b5477d4a081 | -21.8295 | -48.444199 | 2024-10-04 00:40:24 | METOP-C | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 9ce71522-bd0c-313d-a3e5-16ab761b37b2 | -21.8314 | -48.4543 | 2024-10-04 00:40:24 | METOP-C | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| a4db585d-00a6-33ec-a5be-7932d16884ca | -21.802401 | -48.356201 | 2024-10-04 00:40:24 | METOP-C | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| a5253b15-57cc-391d-8232-04c9e8de5f4a | -21.8043 | -48.366199 | 2024-10-04 00:40:24 | METOP-C | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 1fab4ace-588c-3e42-8dad-4a9a094dc821 | -21.806299 | -48.376202 | 2024-10-04 00:40:24 | METOP-C | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 3a8ad6a0-700e-3f42-bdcc-4abad1342958 | -21.808201 | -48.386101 | 2024-10-04 00:40:24 | METOP-C | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| e6733e16-bcf3-3082-bfe6-7db07b8e3056 | -21.815901 | -48.426201 | 2024-10-04 00:40:24 | METOP-C | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 04c93391-d433-35c0-b0d4-2b273d881cbb | -21.8179 | -48.436298 | 2024-10-04 00:40:24 | METOP-C | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| c0c5a48c-7fd5-370e-a264-8aa105138ed8 | -21.819799 | -48.446301 | 2024-10-04 00:40:24 | METOP-C | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 2ae299d4-26ca-3f36-ab8c-c402a8484d2e | -21.7945 | -48.368401 | 2024-10-04 00:40:24 | METOP-C | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 563cda44-f6c6-37e0-ba39-1ab48f5be27f | -21.796499 | -48.3783 | 2024-10-04 00:40:24 | METOP-C | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 4cbe8e1c-252c-34f7-bed3-b07815266770 | -21.798401 | -48.388302 | 2024-10-04 00:40:24 | METOP-C | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| cd0944f7-7a34-3f70-9677-a971fa858baa | -21.800301 | -48.3983 | 2024-10-04 00:40:24 | METOP-C | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| c4bd8e99-25ea-3a5f-bf73-a17ee44a40d9 | -21.8081 | -48.438499 | 2024-10-04 00:40:24 | METOP-C | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| d6e20de1-8f54-37b4-8efa-83502ad04042 | -21.809999 | -48.448502 | 2024-10-04 00:40:24 | METOP-C | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 6789142b-ba8b-3615-99e4-8c817fb19e58 | -21.786699 | -48.380501 | 2024-10-04 00:40:24 | METOP-C | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 04fc7e63-7947-3d9e-89e3-0aa91f8a9b66 | -21.788601 | -48.3904 | 2024-10-04 00:40:24 | METOP-C | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 32a418e7-a443-35ee-9eeb-75219cf2eea1 | -21.7983 | -48.440601 | 2024-10-04 00:40:24 | METOP-C | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| e8a54110-48ab-3fd7-acff-200b612588e9 | -21.8002 | -48.4506 | 2024-10-04 00:40:24 | METOP-C | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 9834f65e-8a01-3251-acc2-cd3d78aeb234 | -20.4387 | -41.986698 | 2024-10-04 00:40:24 | METOP-C | ALTO JEQUITIBÁ | MINAS GERAIS | Brasil | 3153509 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 0cb28a53-1b47-37e3-9c62-3d46a80d0ccd | -20.440599 | -41.994701 | 2024-10-04 00:40:24 | METOP-C | ALTO JEQUITIBÁ | MINAS GERAIS | Brasil | 3153509 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| a95fbba5-3884-32da-83c6-7a2951d1c15e | -21.7885 | -48.442699 | 2024-10-04 00:40:25 | METOP-C | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README7.md)
