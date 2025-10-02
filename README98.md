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

## Dados Diários - Página 98

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3425dd86-5653-3e80-9762-7a4dd8fabfc5 | -14.22268 | -44.93057 | 2025-10-02 04:32:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6285b3a5-c1f4-38c4-a744-ca8667008b25 | -13.31071 | -47.85677 | 2025-10-02 04:32:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| adbc8c2b-58c2-3e7b-916a-b45d49cb4914 | -12.58368 | -49.88944 | 2025-10-02 04:32:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e0787c54-3827-3b3b-a07d-0d4dd5a8296e | -15.52118 | -47.85744 | 2025-10-02 04:32:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 583c6d4f-b75b-3d65-a7cb-0cdc224161f9 | -12.69782 | -48.57741 | 2025-10-02 04:32:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a4bfd359-b839-3700-a3e4-3e5b59c88faa | -14.31073 | -46.00428 | 2025-10-02 04:32:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 66fe7176-fa79-3244-bfb2-ee3e1f05e994 | -12.80856 | -47.01986 | 2025-10-02 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 5e6f10f1-0e4e-31af-99a4-ef5709a2ef58 | -12.77416 | -44.91999 | 2025-10-02 04:32:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9bce45dd-0f4f-33f8-a6fc-0ad6dacd3df4 | -17.17064 | -47.02314 | 2025-10-02 04:32:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d424aac5-ff2e-30ca-ac70-ca3f1fc89f01 | -14.86051 | -48.30102 | 2025-10-02 04:32:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7880bfd3-092e-3259-8e29-b20630f30398 | -12.20074 | -47.79491 | 2025-10-02 04:32:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fe2de4fc-3691-37f6-be2d-1415a6398c6e | -12.07226 | -47.98838 | 2025-10-02 04:32:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 75b37678-9a09-3be1-9274-45ac9fefee84 | -13.85525 | -51.24606 | 2025-10-02 04:32:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| dcd481e8-fbed-3fd4-b6dc-1434ccba2df1 | -16.04014 | -50.88117 | 2025-10-02 04:32:00 | NPP-375D | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 89e7599b-c447-39ab-b6df-c0e7bd0ee742 | -14.41093 | -46.07841 | 2025-10-02 04:32:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c2b0bcbf-874e-3a17-9e55-d783e3df023a | -17.96738 | -44.3952 | 2025-10-02 04:32:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 65d89bf9-0671-38ee-b8fb-1fc395829fa7 | -12.8119 | -47.02042 | 2025-10-02 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| f3766077-7e87-3ecf-8996-a2a5c4da3523 | -15.48767 | -45.92336 | 2025-10-02 04:32:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 968dcc95-3386-3da3-9ecc-608a46d5fcae | -13.91238 | -48.07157 | 2025-10-02 04:32:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 44abc282-a295-3f4c-bc77-a709f4d159ff | -14.36855 | -45.94984 | 2025-10-02 04:32:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1d5f8be1-329a-3a08-b985-b584b9a1a8f1 | -14.42648 | -46.11632 | 2025-10-02 04:32:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 59ac2cc2-dcb0-378c-a1d2-d5d9392dee26 | -15.1873 | -46.40349 | 2025-10-02 04:32:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3da5b198-d29e-3593-841c-4770accc78d3 | -16.5821 | -45.12524 | 2025-10-02 04:32:00 | NPP-375D | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 425b6220-3a66-33ae-b284-68fe8e420b6b | -13.46565 | -47.23154 | 2025-10-02 04:32:00 | NPP-375D | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7009debf-4d54-3775-9443-a324e7c892ea | -13.8558 | -51.24454 | 2025-10-02 04:32:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b8c0abfc-a984-3a61-9a32-b5e0beeae4db | -15.23663 | -50.10602 | 2025-10-02 04:32:00 | NPP-375D | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 13f2a56a-3bd1-36bf-9a4b-484836ae7d35 | -13.95922 | -48.11556 | 2025-10-02 04:32:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4d3c6530-198c-39a3-bd72-0c393be627d9 | -14.72962 | -48.16206 | 2025-10-02 04:32:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 638036da-c611-306f-b633-077b0df8a0c4 | -12.20406 | -47.79546 | 2025-10-02 04:32:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 32fa4d79-2b00-382f-ad48-52f42f30746f | -14.698 | -49.61798 | 2025-10-02 04:32:00 | NPP-375D | PILAR DE GOIÁS | GOIÁS | Brasil | 5216908 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e098962c-278d-3a55-bc45-c391babedd32 | -14.42806 | -46.35878 | 2025-10-02 04:32:00 | NPP-375D | BURITINÓPOLIS | GOIÁS | Brasil | 5203962 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f487b8d3-85b1-3271-bc36-ecc363440c9f | -13.81594 | -47.54087 | 2025-10-02 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 16ae1555-5d7f-3198-803e-74c06bd499c1 | -15.24016 | -46.98232 | 2025-10-02 04:32:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b96454b6-6964-3be7-9cf8-fb820503056a | -13.75835 | -48.69392 | 2025-10-02 04:32:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0560caf7-bd58-3109-a9d2-cd831648b2b7 | -13.24027 | -47.33444 | 2025-10-02 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7fb43119-e59d-3307-b6fa-5843022ba09b | -12.64085 | -46.94963 | 2025-10-02 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bb119f31-8064-3452-8769-556e439aa0e6 | -13.30257 | -46.99909 | 2025-10-02 04:32:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 3319af6e-0bd5-3595-8845-082adb18989f | -17.16722 | -47.02259 | 2025-10-02 04:32:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d66b02ca-cfae-3653-a4e3-8da998eafca9 | -13.07929 | -47.08922 | 2025-10-02 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 81651423-3bf3-3cc8-a08a-16912532e7f2 | -13.95433 | -44.90751 | 2025-10-02 04:32:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f6d2f638-0149-34e1-a6ff-ab8a9f652226 | -12.67014 | -48.56893 | 2025-10-02 04:32:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c49e283f-7093-3aba-bdc7-a7f79722b857 | -13.17727 | -47.80177 | 2025-10-02 04:32:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 47f2a31b-2a8d-3a5b-864a-3e9ab37c4155 | -15.60123 | -46.92075 | 2025-10-02 04:32:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6cff1e91-5543-3908-9a19-bc98fe27ec43 | -15.93333 | -46.21658 | 2025-10-02 04:32:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9a099a6d-f5b4-333e-be37-087f8fc97643 | -19.90032 | -44.49679 | 2025-10-02 04:32:00 | NPP-375D | FLORESTAL | MINAS GERAIS | Brasil | 3126000 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 75bb78db-3741-36c9-96cf-c79ce5bcc5e8 | -14.41898 | -46.11917 | 2025-10-02 04:32:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 58375898-a5db-3e24-a7ce-86e8be2b6854 | -14.44007 | -46.37228 | 2025-10-02 04:32:00 | NPP-375D | BURITINÓPOLIS | GOIÁS | Brasil | 5203962 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1709d665-fbd4-3a02-910d-e8744ec44d96 | -13.17889 | -47.8348 | 2025-10-02 04:32:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9a76f002-1d5d-3762-92b8-2272554eb640 | -14.86244 | -48.39669 | 2025-10-02 04:32:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 8e7e0077-f2a7-3fbe-9de8-99222e3364ec | -13.7793 | -48.05723 | 2025-10-02 04:32:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a4221296-8af9-30ef-84b9-f25fb7ee1af7 | -14.40289 | -46.08491 | 2025-10-02 04:32:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| cee035e5-00a5-3309-ae66-19cbd82a12d7 | -14.0907 | -46.65545 | 2025-10-02 04:32:00 | NPP-375D | IACIARA | GOIÁS | Brasil | 5209903 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| ff778df4-622e-3a99-8573-d88015f7b35c | -15.60578 | -46.9137 | 2025-10-02 04:32:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b654f82e-66dc-3010-9c8e-6446d02d5ada | -15.22448 | -50.11585 | 2025-10-02 04:32:00 | NPP-375D | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 99d8479d-f177-3e2f-bb71-d2659a292712 | -14.47464 | -48.4053 | 2025-10-02 04:32:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 5def1758-ad58-3e58-8751-0995f5b980f3 | -11.59038 | -50.16788 | 2025-10-02 04:32:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 50d6826b-e8d5-3825-aa83-f6aac530ab75 | -18.63865 | -50.68864 | 2025-10-02 04:32:00 | NPP-375D | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 27c8eecd-4089-3808-aa54-5a6483dfa5a4 | -15.14036 | -46.44381 | 2025-10-02 04:32:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1c9b6b22-8a11-3dfc-a69f-9709f220ffb3 | -13.33658 | -47.34296 | 2025-10-02 04:32:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 867caffb-1166-3f65-bffc-9f745eabb686 | -12.89154 | -46.92696 | 2025-10-02 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7f59a9b6-3415-3f66-8838-0f960f0743a6 | -13.80904 | -47.86871 | 2025-10-02 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4b7b4706-382a-34ab-b92b-e5d2ea723fa8 | -16.01363 | -50.8682 | 2025-10-02 04:32:00 | NPP-375D | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a3ac5a1c-3de9-3c5a-935b-212d27117fcb | -13.75664 | -48.00602 | 2025-10-02 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1128ef45-a98b-3b7f-9d9c-f9981fa93f19 | -14.10914 | -45.64169 | 2025-10-02 04:32:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ff6da4c4-f709-3cae-8512-bb37f1e89163 | -14.37447 | -45.96541 | 2025-10-02 04:32:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d15c6d41-0dee-3752-be55-b04ad2a870cd | -13.12957 | -47.41539 | 2025-10-02 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c0e6bd68-7390-38b7-92fe-e900cb813980 | -12.80363 | -46.86132 | 2025-10-02 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 375a41f8-16ff-325e-a88e-497b1605059f | -13.37267 | -47.80488 | 2025-10-02 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3f9fee74-592d-3e1d-8817-c58d5ea87020 | -14.29507 | -45.9664 | 2025-10-02 04:32:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e40e24cb-0687-3064-9225-7c2b22d4f416 | -13.52354 | -47.25591 | 2025-10-02 04:32:00 | NPP-375D | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d073bbe7-3c61-350e-b45f-fe7bde618ab2 | -14.89268 | -48.30595 | 2025-10-02 04:32:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e26a4290-8862-3d15-b768-a3446239401d | -14.30667 | -45.98386 | 2025-10-02 04:32:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3e2dfe51-0e05-3fae-ab6e-1e999842e6f7 | -18.50534 | -44.03261 | 2025-10-02 04:32:00 | NPP-375D | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c1df90ea-1a10-3adf-91db-183220b85413 | -13.15057 | -47.84107 | 2025-10-02 04:32:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 1da356e3-7e5c-31da-a964-0bee7f6f647d | -13.2129 | -48.49368 | 2025-10-02 04:32:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 74bc7ff3-6719-3b27-a73d-cd48f4f16a62 | -12.76127 | -50.55502 | 2025-10-02 04:32:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c9b9ba81-443f-38c5-ba09-2634cb35cca9 | -15.27682 | -49.30835 | 2025-10-02 04:32:00 | NPP-375D | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 484488fb-3f02-3e4f-a27f-ab80df50fa28 | -12.5865 | -49.89392 | 2025-10-02 04:32:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5f2d5598-9c1a-33cb-8e18-9a3aa43370b8 | -14.89149 | -48.33508 | 2025-10-02 04:32:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 761a7d90-4885-387d-9f8a-5d42e95a127a | -13.74777 | -47.99726 | 2025-10-02 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6abda457-ec72-3e83-96d6-febbd69a9d95 | -14.43721 | -46.36796 | 2025-10-02 04:32:00 | NPP-375D | BURITINÓPOLIS | GOIÁS | Brasil | 5203962 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cae18662-b5e8-372f-9af4-8691608de69c | -15.83137 | -46.25014 | 2025-10-02 04:32:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f1361266-804f-3384-90eb-0d40660bf4e5 | -15.32118 | -46.39602 | 2025-10-02 04:32:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 305e9176-9f2d-3881-aa4e-1213bab65831 | -13.01283 | -45.22256 | 2025-10-02 04:32:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 70e880e4-c334-31df-9c6b-d750d8155cf0 | -13.1689 | -47.83316 | 2025-10-02 04:32:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 75738012-4a35-35c3-bfda-0caef7085ff7 | -12.51215 | -46.83712 | 2025-10-02 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 85a39d01-c9ad-3136-a73f-131a5deeda90 | -14.69441 | -48.25516 | 2025-10-02 04:32:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 783c9fe2-e232-3b0e-b8d4-90ac6cd0c75e | -15.34358 | -46.29265 | 2025-10-02 04:32:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| baa73810-06e4-39b4-9d43-9b1214e01ac5 | -13.40319 | -47.7844 | 2025-10-02 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6ae0ed5b-ec63-3c21-a0f5-d9abd07b0708 | -13.31208 | -47.00428 | 2025-10-02 04:32:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d5a90be8-c017-305b-8e19-736f151eff3f | -13.52575 | -47.26366 | 2025-10-02 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0d8b519b-8024-330b-8513-a106bc847294 | -19.42003 | -46.80867 | 2025-10-02 04:32:00 | NPP-375D | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 622d7832-3948-38d9-950c-6b07499dd217 | -13.31624 | -47.82133 | 2025-10-02 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 08b2fc04-e45e-3ee0-a161-b6fd575d8889 | -14.64763 | -48.12682 | 2025-10-02 04:32:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f7c9dae6-811d-33c6-9631-4e2caebdf7ec | -13.36994 | -47.28253 | 2025-10-02 04:32:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 02da73e4-89f7-3b5f-b228-9659694a02e3 | -15.255 | -49.30484 | 2025-10-02 04:32:00 | NPP-375D | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a613181e-e6ca-3abd-b7b1-4439c83cc819 | -13.07873 | -47.0928 | 2025-10-02 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d9d19603-ed1f-3726-98a7-4201793fe91d | -12.5748 | -49.8999 | 2025-10-02 04:32:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3307bb59-ebc2-3815-beb9-93c0b2193747 | -15.3205 | -46.2812 | 2025-10-02 04:32:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 07c0529f-fb1f-3c81-ae7a-eaeffdc7499f | -13.81264 | -48.04084 | 2025-10-02 04:32:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |


[Clique aqui para ver as próximas entradas](README99.md)
