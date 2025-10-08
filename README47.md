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

## Dados Diários - Página 47

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b96dad4a-36af-3698-9871-6030f6fe000b | -14.71636 | -46.00224 | 2025-10-08 04:19:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 2ccd18ac-d577-31f0-a8a8-31491199e50e | -15.30879 | -46.16567 | 2025-10-08 04:19:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9573b99c-b28e-3eb8-9aff-c7eb10d86613 | -17.93962 | -57.53288 | 2025-10-08 04:19:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| c686153b-92c0-3072-b987-9ffd929ac6fd | -7.80662 | -44.22898 | 2025-10-08 04:19:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0baa77d6-31cc-357d-bac2-37038efe1d95 | -18.49402 | -42.90109 | 2025-10-08 04:19:00 | NPP-375D | PAULISTAS | MINAS GERAIS | Brasil | 3148400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| d5d98974-3eff-302e-b6b5-aa39a1b39da2 | -8.86409 | -46.77378 | 2025-10-08 04:19:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| ddb3a513-ccb5-3c94-8f74-671bb088a97f | -17.85886 | -57.58243 | 2025-10-08 04:19:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 57fa2e0b-2fd9-3249-89ae-1a2cc71932f2 | -19.82758 | -46.16718 | 2025-10-08 04:19:00 | NPP-375D | TAPIRAÍ | MINAS GERAIS | Brasil | 3168200 | 31 | 33 | nan | nan | nan | Cerrado | 7.0 |
| c90975e3-6619-3894-ba56-433970bfc1c7 | -13.97334 | -48.06395 | 2025-10-08 04:19:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 28ef2caf-0fc2-37dc-b249-671921b4c278 | -7.8078 | -44.17867 | 2025-10-08 04:19:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3dfe760a-a12b-3c99-8e91-192d2dbc6110 | -7.6191 | -44.13427 | 2025-10-08 04:19:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 9013b7ad-207e-3e3c-b1a8-b95336bed8ec | -7.65315 | -43.94202 | 2025-10-08 04:19:00 | NPP-375D | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 92258e96-f633-3801-a851-f3ec146fcd33 | -8.93448 | -46.59525 | 2025-10-08 04:19:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 06a47fd6-635a-3606-b48b-8384942f1197 | -16.10807 | -43.87073 | 2025-10-08 04:19:00 | NPP-375D | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 7a62fd0f-ac72-30c7-ac67-3f9865006fdd | -18.35718 | -42.39668 | 2025-10-08 04:19:00 | NPP-375D | PEÇANHA | MINAS GERAIS | Brasil | 3148608 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 2e20a133-d5f0-3a72-a45d-ce9201261895 | -14.83593 | -48.41801 | 2025-10-08 04:19:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bb4e91af-e67e-3082-bb67-c6922aa4515f | -15.24524 | -46.36518 | 2025-10-08 04:19:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9ba299bb-3c88-3023-b204-dd4398e8d2de | -19.83148 | -46.16409 | 2025-10-08 04:19:00 | NPP-375D | TAPIRAÍ | MINAS GERAIS | Brasil | 3168200 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 606dd257-343d-3a35-a31e-3544e38e92d2 | -15.30998 | -46.15833 | 2025-10-08 04:19:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a03f71d8-7433-3794-8aa8-f643872a27b9 | -8.58526 | -44.33578 | 2025-10-08 04:19:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 0298e1d6-f0bd-31c3-a03a-2c672f1e9426 | -15.8025 | -46.24554 | 2025-10-08 04:19:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ddd1a07a-39b6-3b54-a6cc-643d404513e4 | -15.38024 | -47.31717 | 2025-10-08 04:19:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 859a563b-45c2-390c-816f-c2b0e208b038 | -18.40676 | -45.20424 | 2025-10-08 04:19:00 | NPP-375D | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 80a26a5c-c7fc-3084-8923-fde5d4815480 | -14.91259 | -46.81435 | 2025-10-08 04:19:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a7dd9661-c163-343d-a65f-adae7e5310e9 | -8.16198 | -43.33249 | 2025-10-08 04:19:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 1ad7d399-3094-3fa8-a0fc-2900c6702df5 | -15.37955 | -47.3212 | 2025-10-08 04:19:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 40f2ba9f-c8c3-3b91-ae7c-afedf6a1a736 | -20.72923 | -42.91529 | 2025-10-08 04:19:00 | NPP-375D | VIÇOSA | MINAS GERAIS | Brasil | 3171303 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| e9af2f5f-91ce-3c83-bd9b-c49a0a655622 | -15.26349 | -46.33817 | 2025-10-08 04:19:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| aee34982-c6e0-327f-8e18-93b39d8d2c92 | -17.82538 | -57.64633 | 2025-10-08 04:19:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 16.8 |
| 82a159fb-5d99-38e4-b0b8-f74a455ee097 | -13.29917 | -48.02912 | 2025-10-08 04:19:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 6b1f04ba-295d-320b-8f89-3ecb1349ec3f | -13.73554 | -45.71889 | 2025-10-08 04:19:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ee43673a-66a7-38fa-817d-d535439ef18f | -15.99218 | -50.84537 | 2025-10-08 04:19:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| db22d7e9-dc43-3962-89de-733c34f17a66 | -17.82729 | -57.63752 | 2025-10-08 04:19:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 29.1 |
| 6d8c13b5-d302-3ed9-b671-408ab684ba57 | -14.25655 | -45.86895 | 2025-10-08 04:19:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d97f39cf-6c12-329d-ad68-f955d019506c | -13.80675 | -45.80116 | 2025-10-08 04:19:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f6b7b270-e908-399d-99fd-ebdaa416b73c | -8.4654 | -47.20805 | 2025-10-08 04:19:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| fa33e2f8-9cf1-38b5-81dd-b1ddfaf8855d | -7.6537 | -43.93853 | 2025-10-08 04:19:00 | NPP-375D | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 456da0df-78dd-3264-ab7d-189b47a2cb8d | -20.1285 | -44.41813 | 2025-10-08 04:19:00 | NPP-375D | MATEUS LEME | MINAS GERAIS | Brasil | 3140704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| ac8df7d7-23f0-3653-800b-f7d5ec033600 | -17.27346 | -42.65319 | 2025-10-08 04:19:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 6.9 |
| f4a5185f-7f1e-3e8f-9c0e-0ca7d22871ff | -14.94788 | -46.81152 | 2025-10-08 04:19:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 46a98fd2-8f45-316b-bcd4-d5611ef203f8 | -14.77196 | -46.00753 | 2025-10-08 04:19:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 04c70ef2-c1ce-31e9-9ff7-51d3d6b6ad91 | -9.09153 | -47.95889 | 2025-10-08 04:19:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| af10b543-8af9-36d6-9be9-a9ec993f3608 | -9.68858 | -45.68341 | 2025-10-08 04:19:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0bdeea26-e1bb-3eeb-83fa-ffac35b3b14d | -17.28547 | -42.64637 | 2025-10-08 04:19:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 6.0 |
| c7be5003-2bf8-33c0-af99-da516c83f32d | -14.79013 | -42.33352 | 2025-10-08 04:19:00 | NPP-375D | JACARACI | BAHIA | Brasil | 2917409 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| a0fbdce9-ddf5-3968-91cf-ce0127d13fae | -18.06309 | -44.44387 | 2025-10-08 04:19:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 51fe716a-adf0-339c-b040-6c884d6f837e | -16.29128 | -45.24222 | 2025-10-08 04:19:00 | NPP-375D | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ac58d3b9-46fc-3793-8f29-7729331a16f6 | -16.02857 | -43.70404 | 2025-10-08 04:19:00 | NPP-375D | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8dbae058-3d1c-3ca4-9edb-065d820c1fc4 | -7.78769 | -44.21872 | 2025-10-08 04:19:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e15bdc99-07b8-3d78-b6f6-197574fd2a76 | -8.41327 | -46.8108 | 2025-10-08 04:19:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5e0e4b56-396f-321a-9eee-53c151e2f57a | -17.94546 | -57.50786 | 2025-10-08 04:19:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 95d14157-d1da-349e-aae0-5618abbbf723 | -15.94803 | -42.59874 | 2025-10-08 04:19:00 | NPP-375D | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 20424549-e409-3007-8113-4a45e7d96e81 | -15.25101 | -46.35105 | 2025-10-08 04:19:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 8ba80cf7-4c5a-3317-94a4-1b934639bb32 | -7.80328 | -44.22844 | 2025-10-08 04:19:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 471e3eeb-ee0f-3c5e-becf-bac8693a4bd8 | -15.98806 | -50.84465 | 2025-10-08 04:19:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| af91433c-76d7-3ef2-acc1-3fc2c1cb0265 | -19.47176 | -43.89346 | 2025-10-08 04:19:00 | NPP-375D | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bfc7f5c6-28ef-3fb8-919d-2da14e3423ae | -7.8173 | -44.14066 | 2025-10-08 04:19:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ab058ed7-c7ae-38e0-9882-cf668ad37a4e | -13.85201 | -51.86407 | 2025-10-08 04:19:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a86503cd-3562-3c7e-9841-a88caef8278b | -8.47886 | -46.31718 | 2025-10-08 04:19:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 68072e7d-2f32-3301-a218-83e820ec05d9 | -18.41289 | -45.20903 | 2025-10-08 04:19:00 | NPP-375D | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e20808cd-257c-3306-9dc2-b57e6844a23f | -7.80395 | -44.13851 | 2025-10-08 04:19:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 86091086-5305-3237-8ad6-73e2fbb7aa92 | -18.29468 | -45.44106 | 2025-10-08 04:19:00 | NPP-375D | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 93ca247d-8396-3411-9d9b-e663366133c3 | -15.47921 | -55.99002 | 2025-10-08 04:19:00 | NPP-375D | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 75c615aa-0081-315a-8d88-94ad52ae8008 | -20.12793 | -44.42198 | 2025-10-08 04:19:00 | NPP-375D | MATEUS LEME | MINAS GERAIS | Brasil | 3140704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 0c73a398-9d6d-37ba-acfb-fa8d609931d4 | -15.94448 | -42.59816 | 2025-10-08 04:19:00 | NPP-375D | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| 5d189519-ac49-32fe-be37-482de2f84578 | -20.20429 | -48.70535 | 2025-10-08 04:19:00 | NPP-375D | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 2f2e4b39-b2eb-39ab-b6e9-f497f40407c9 | -18.87566 | -44.15882 | 2025-10-08 04:19:00 | NPP-375D | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9faad2fc-0ea6-379b-a444-dd18580c8920 | -7.76979 | -49.23927 | 2025-10-08 04:19:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4fca07ec-7e17-3a27-8fb0-bd162b69018a | -19.58002 | -44.73518 | 2025-10-08 04:19:00 | NPP-375D | MARAVILHAS | MINAS GERAIS | Brasil | 3139706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| dd85b69e-ad6a-32bf-b32d-dad3c6d1557e | -13.84204 | -51.86692 | 2025-10-08 04:19:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 2440a9db-505b-35bc-acdf-2bfabf6ba87b | -17.90251 | -44.40275 | 2025-10-08 04:19:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| aaa95861-0d17-3a24-a01e-539b3fb6aa9b | -8.67914 | -47.07724 | 2025-10-08 04:19:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5d9bbf60-dd72-3774-ad0b-1a54f533b79c | -15.39458 | -46.28152 | 2025-10-08 04:19:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 959c52ea-f128-389b-b06a-521ffc2bb6a5 | -17.36103 | -45.05445 | 2025-10-08 04:19:00 | NPP-375D | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 616907b6-e2d9-34ac-9859-4f8a44cf0825 | -16.62203 | -45.41943 | 2025-10-08 04:19:00 | NPP-375D | SANTA FÉ DE MINAS | MINAS GERAIS | Brasil | 3157609 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| eaa9f2e1-c726-38dd-ada6-ed174772931e | -19.51804 | -44.07227 | 2025-10-08 04:19:00 | NPP-375D | MATOZINHOS | MINAS GERAIS | Brasil | 3141108 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 65e5afb8-3d3a-3d34-907b-a12500623165 | -18.40342 | -45.20367 | 2025-10-08 04:19:00 | NPP-375D | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6a47fa6a-cdb3-3394-a2d3-705953c7b4d2 | -17.90533 | -44.40708 | 2025-10-08 04:19:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 07ebe865-6401-356a-ba58-28da0462e94f | -19.51688 | -44.08018 | 2025-10-08 04:19:00 | NPP-375D | MATOZINHOS | MINAS GERAIS | Brasil | 3141108 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6a07a219-00fd-34a8-a75e-3d7e790ca7c1 | -15.49561 | -47.9329 | 2025-10-08 04:19:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 73602b2b-13b7-3fc1-b8df-7849dd7484d6 | -13.69481 | -55.01445 | 2025-10-08 04:19:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c19a0ed8-b2fd-378a-9a83-0505618edc43 | -8.52056 | -46.2371 | 2025-10-08 04:19:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| a996529d-9c7a-3440-bf4f-bbea7194ecac | -15.99666 | -50.96033 | 2025-10-08 04:19:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 73c975ab-87ad-3ac2-8ed1-778732a65a39 | -16.32533 | -47.063 | 2025-10-08 04:19:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 27b79563-c2f6-3a3a-b91a-c9ea7b0b6396 | -18.04964 | -57.55116 | 2025-10-08 04:19:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 74bc21e6-4aaf-3cff-accc-77ef6ad0b45a | -15.37014 | -47.30437 | 2025-10-08 04:19:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c84be82a-f291-34d3-8caa-278eaef2270b | -13.79963 | -45.78137 | 2025-10-08 04:19:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 00190c02-e566-36ac-a891-a5230e514757 | -9.1642 | -43.01944 | 2025-10-08 04:19:00 | NPP-375D | ANÍSIO DE ABREU | PIAUÍ | Brasil | 2200707 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| fed96e54-075d-3c73-a05b-948c64bfd776 | -20.29192 | -48.51499 | 2025-10-08 04:19:00 | NPP-375D | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e1b1046c-f4cb-3b66-b46f-dd92f820df9e | -18.0241 | -44.30976 | 2025-10-08 04:19:00 | NPP-375D | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5bb06595-766f-3c3d-bb00-c32bacfb0202 | -15.61384 | -52.5831 | 2025-10-08 04:19:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7a6c8209-7539-3959-8187-48286fc0cf86 | -15.25834 | -46.34856 | 2025-10-08 04:19:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0844707a-9c62-3f7b-96e4-efbf67497bc4 | -14.95811 | -46.81325 | 2025-10-08 04:19:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f63eb477-a66f-3ece-ba89-263adba7b2b7 | -17.92913 | -57.52299 | 2025-10-08 04:19:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.8 |
| 3fe3d741-20a9-38a0-8f73-3172b4bc6d0b | -18.05577 | -44.46938 | 2025-10-08 04:19:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2c929526-e502-3551-9830-9b269ed32772 | -8.56807 | -44.62682 | 2025-10-08 04:19:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 94e5f539-2621-3909-8133-5df2235ad6d0 | -8.92377 | -46.59345 | 2025-10-08 04:19:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 3dcb5ac0-09c7-3107-b5ba-0a2cf5fc74b5 | -9.67928 | -45.67871 | 2025-10-08 04:19:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2018d640-efab-38ad-862b-584689ac9ebc | -18.0505 | -57.52312 | 2025-10-08 04:19:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| c340a02b-ec52-3a4c-a165-ab4eb0daff31 | -7.80724 | -44.18218 | 2025-10-08 04:19:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README48.md)
