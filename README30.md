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

## Dados Diários - Página 30

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 078a4beb-de1c-36c0-91ea-f180e73a13a3 | -15.5602 | -42.68462 | 2025-08-23 04:02:00 | NOAA-20 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.9 |
| 14322612-637a-3bf5-af32-63e49fe14ef8 | -11.28515 | -44.93647 | 2025-08-23 04:02:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 1eb41f3c-3b15-3354-9e02-41777a334ca8 | -13.64466 | -46.8812 | 2025-08-23 04:02:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 41c9a9e2-6c70-35ed-9446-8c54bd125763 | -15.20502 | -48.70383 | 2025-08-23 04:02:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| bb560e04-2bc6-395c-92ff-6463847586d5 | -14.79921 | -45.43446 | 2025-08-23 04:02:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 70ef1edc-a18e-3556-aa82-435e9290e6fe | -10.64614 | -50.13026 | 2025-08-23 04:02:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 18322261-923b-3847-8ede-b5287bb20087 | -9.4417 | -47.65084 | 2025-08-23 04:02:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| e281cbb4-42ad-3a9d-86be-58bd07f25f8e | -15.71032 | -41.92827 | 2025-08-23 04:02:00 | NOAA-20 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.0 |
| ae565533-fd37-3ad5-be59-6f03dab8d99d | -13.60156 | -46.88911 | 2025-08-23 04:02:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d49089c3-5e37-3a66-8e3b-e9f3c87267f0 | -11.61692 | -50.42976 | 2025-08-23 04:02:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 34000081-7a09-30bc-a4dd-6b8a7c8bb47a | -9.32946 | -37.98305 | 2025-08-23 04:02:00 | NOAA-20 | ÁGUA BRANCA | ALAGOAS | Brasil | 2700102 | 27 | 33 | nan | nan | nan | Caatinga | 3.7 |
| e0c6b5fb-46c7-3fc0-a3e2-73179ec67c91 | -10.39689 | -42.58181 | 2025-08-23 04:02:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f35c4ebe-73bb-345d-bf0b-ffd0e2d507bc | -11.19123 | -55.03747 | 2025-08-23 04:02:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f07fbc8c-7905-3d59-8d1c-7cb1c10ad26d | -14.80754 | -47.94368 | 2025-08-23 04:02:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cebfd43e-576d-3c9a-b668-9191ef8b7377 | -14.78476 | -45.49547 | 2025-08-23 04:02:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 89324ad1-5b7f-3763-8bd9-c94fce885e51 | -11.51116 | -50.47441 | 2025-08-23 04:02:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bed7e59a-c34e-3c4d-a94a-718ab77a7b40 | -17.2684 | -46.76165 | 2025-08-23 04:04:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f438eb6b-49f0-3aa6-ac4a-f7f0a74f8434 | -21.80858 | -46.50211 | 2025-08-23 04:04:00 | NOAA-20 | POÇOS DE CALDAS | MINAS GERAIS | Brasil | 3151800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| d86d6ecf-28e1-3188-beab-f0d31fcd412d | -17.27425 | -46.77293 | 2025-08-23 04:04:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 37787cbb-3f3c-3173-87bd-79e9801233e1 | -17.70238 | -48.51411 | 2025-08-23 04:04:00 | NOAA-20 | CALDAS NOVAS | GOIÁS | Brasil | 5204508 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d2b7f3f2-7b10-3d01-94b5-b3e47e3c611f | -15.71185 | -48.23111 | 2025-08-23 04:04:00 | NOAA-20 | ÁGUAS LINDAS DE GOIÁS | GOIÁS | Brasil | 5200258 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 59bccc37-5bd2-3872-abfa-4f2b02eed235 | -15.02883 | -54.9041 | 2025-08-23 04:04:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 52dd3e48-657a-3f81-8fd1-a4508620d7e8 | -14.67696 | -54.87619 | 2025-08-23 04:04:00 | NOAA-20 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 06b7d352-1361-3d52-aa12-7cd49a7a0d9d | -18.40366 | -42.78603 | 2025-08-23 04:04:00 | NOAA-20 | SÃO JOÃO EVANGELISTA | MINAS GERAIS | Brasil | 3162807 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| fa2475e2-3817-364e-9128-24f2fabc21cd | -15.23069 | -53.86088 | 2025-08-23 04:04:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 12.9 |
| fc838cc7-4c7d-39aa-ad53-3fb8c7df709e | -17.82826 | -44.40522 | 2025-08-23 04:04:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 16155b9c-ab48-3f13-8da1-14c48ceefd78 | -20.33758 | -46.54384 | 2025-08-23 04:04:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a53b34a3-6446-3bd4-98af-4450be293868 | -22.49221 | -43.81757 | 2025-08-23 04:04:00 | NOAA-20 | BARRA DO PIRAÍ | RIO DE JANEIRO | Brasil | 3300308 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| b4175a13-5f13-39d2-b250-750b528442a7 | -14.72674 | -55.42348 | 2025-08-23 04:04:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9878febf-93ac-3642-88c5-efd6e0d626da | -18.68122 | -41.19642 | 2025-08-23 04:04:00 | NOAA-20 | MANTENA | MINAS GERAIS | Brasil | 3139607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| f230f88d-87fa-367b-9fa1-9194aa788383 | -20.35808 | -46.54009 | 2025-08-23 04:04:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 024e4070-6f5c-3933-9b7f-d44f010b5234 | -22.1564 | -44.59799 | 2025-08-23 04:04:00 | NOAA-20 | AIURUOCA | MINAS GERAIS | Brasil | 3101201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 6452ea12-b254-3c7b-a439-99bb3f8c4a43 | -21.80783 | -46.50637 | 2025-08-23 04:04:00 | NOAA-20 | POÇOS DE CALDAS | MINAS GERAIS | Brasil | 3151800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 961aeb4d-71f4-3db2-809e-8fd3258d7d26 | -18.05083 | -42.95613 | 2025-08-23 04:04:00 | NOAA-20 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 2e0c65e2-4167-3d56-b3d2-3ad12721243e | -17.58318 | -46.56491 | 2025-08-23 04:04:00 | NOAA-20 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c096730d-104a-370b-8436-0d2ddb2855cd | -15.21749 | -53.86283 | 2025-08-23 04:04:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 053916f4-491d-3acc-bd33-a7d8b63ac8ca | -17.59436 | -46.5671 | 2025-08-23 04:04:00 | NOAA-20 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 137af7c1-181c-3ae7-8b7c-d5f169230638 | -17.52244 | -47.06017 | 2025-08-23 04:04:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0b384e27-8cb9-3f76-886e-60f1b179d2c9 | -18.27113 | -45.57967 | 2025-08-23 04:04:00 | NOAA-20 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5f16d6d9-4ef5-3888-974d-944ce03e66a6 | -20.08946 | -47.75728 | 2025-08-23 04:04:00 | NOAA-20 | IGARAPAVA | SÃO PAULO | Brasil | 3520103 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8c36fdd3-5daa-34cd-a0be-aa8d05a9910c | -17.50245 | -48.02721 | 2025-08-23 04:04:00 | NOAA-20 | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e1a3fe38-e7e0-3c20-a387-15521fe56675 | -17.58774 | -46.56096 | 2025-08-23 04:04:00 | NOAA-20 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 5.3 |
| e44312b8-eb58-397a-b971-9f99218fce74 | -15.04777 | -56.3983 | 2025-08-23 04:04:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 4d7ee646-d1ff-3722-96ad-60c5e7a90cc2 | -17.59063 | -46.56636 | 2025-08-23 04:04:00 | NOAA-20 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 4dce99c2-1ce6-37d4-af4b-72507584468d | -15.02372 | -54.90336 | 2025-08-23 04:04:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 4164966f-e39a-3b7d-956c-0fef6467e83c | -20.268 | -46.68462 | 2025-08-23 04:04:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8417144d-2b11-3486-bfe6-d59ea74b7cc4 | -17.59511 | -49.42375 | 2025-08-23 04:04:00 | NOAA-20 | PONTALINA | GOIÁS | Brasil | 5217708 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 7ae434b9-93d1-3bc2-96d7-cefdaeaa63e2 | -20.08659 | -47.75126 | 2025-08-23 04:04:00 | NOAA-20 | IGARAPAVA | SÃO PAULO | Brasil | 3520103 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b968c0b3-ddaf-37b0-9735-b331f873e8c6 | -22.93167 | -43.395 | 2025-08-23 04:04:00 | NOAA-20 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 83173c49-fd60-3dd4-96dd-3d37c286af35 | -17.60644 | -46.69618 | 2025-08-23 04:04:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c8da32ec-4fdc-38df-9cd0-db613f07e1df | -23.10503 | -46.7984 | 2025-08-23 04:04:00 | NOAA-20 | JUNDIAÍ | SÃO PAULO | Brasil | 3525904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| a73e5b36-ada4-3f23-8947-e268f0452cf6 | -22.92141 | -43.5052 | 2025-08-23 04:04:00 | NOAA-20 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| c5c901e1-6a3b-3a2c-b285-7504e5ed2454 | -15.546 | -51.70376 | 2025-08-23 04:04:00 | NOAA-20 | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a7cb3a08-ec01-3782-b862-9755454a8069 | -17.26206 | -46.77543 | 2025-08-23 04:04:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 0f3fdda4-e9e0-3b46-aeb8-16ce693dce64 | -19.93986 | -47.48974 | 2025-08-23 04:04:00 | NOAA-20 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1eb74c1f-a480-31eb-ba9b-405c33304739 | -17.60728 | -46.6914 | 2025-08-23 04:04:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6793a718-1155-3bfc-9da5-625530885d4d | -22.09314 | -45.02464 | 2025-08-23 04:04:00 | NOAA-20 | SÃO LOURENÇO | MINAS GERAIS | Brasil | 3163706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| a77e1177-8905-3af3-b5cc-a26fd4a416dc | -17.80737 | -52.0649 | 2025-08-23 04:04:00 | NOAA-20 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d026519e-3653-353f-be86-5a61cf3f2044 | -22.30851 | -43.16785 | 2025-08-23 04:04:00 | NOAA-20 | AREAL | RIO DE JANEIRO | Brasil | 3300225 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 71f5c420-3846-3144-964a-dfba27af5b6e | -19.97456 | -47.5095 | 2025-08-23 04:04:00 | NOAA-20 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 237ab384-998b-3183-891b-59dacbd13ff4 | -20.28068 | -46.6554 | 2025-08-23 04:04:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3aea74be-1b3c-330c-96b1-13ab29d3ca70 | -17.69147 | -48.50291 | 2025-08-23 04:04:00 | NOAA-20 | CALDAS NOVAS | GOIÁS | Brasil | 5204508 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| be20bcfa-79ca-3a46-aacf-867b9a8544e0 | -22.57298 | -47.02731 | 2025-08-23 04:04:00 | NOAA-20 | SANTO ANTÔNIO DE POSSE | SÃO PAULO | Brasil | 3548005 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 16ab972b-be8a-339b-9f4b-2f6ec907d631 | -22.09649 | -45.02526 | 2025-08-23 04:04:00 | NOAA-20 | SÃO LOURENÇO | MINAS GERAIS | Brasil | 3163706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| b0c8d194-ec27-3efd-9720-05e876a9b2f2 | -20.08372 | -47.76691 | 2025-08-23 04:04:00 | NOAA-20 | IGARAPAVA | SÃO PAULO | Brasil | 3520103 | 35 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 3561c7f0-7ccd-3153-8d54-b84819509531 | -19.96145 | -47.5166 | 2025-08-23 04:04:00 | NOAA-20 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dd195413-5b88-3394-883b-a34229a0c2cc | -20.2247 | -46.7152 | 2025-08-23 04:04:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| bf676a57-28ed-3ed9-9638-c3720b8ab8a5 | -14.66149 | -54.91501 | 2025-08-23 04:04:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 4e048979-4d9d-3b00-8fb5-a47d766ae5e7 | -20.44521 | -42.12849 | 2025-08-23 04:04:00 | NOAA-20 | SÃO JOÃO DO MANHUAÇU | MINAS GERAIS | Brasil | 3162559 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 9f586d3b-cb8d-37cb-baf8-7a2e3570dd4c | -17.92086 | -44.48105 | 2025-08-23 04:04:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9e161a36-e942-3263-bf58-4924b59b53a1 | -20.27397 | -42.83081 | 2025-08-23 04:04:00 | NOAA-20 | SANTA CRUZ DO ESCALVADO | MINAS GERAIS | Brasil | 3157401 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| c19809f1-4218-3fed-b31e-5a3b6ba53cbe | -20.87432 | -42.54502 | 2025-08-23 04:04:00 | NOAA-20 | ERVÁLIA | MINAS GERAIS | Brasil | 3124005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.5 |
| 2f7fd388-da13-3484-aec6-859c589c9175 | -15.64929 | -52.6826 | 2025-08-23 04:04:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2c2b3993-24b0-3411-acbe-98d86e431bc3 | -17.69486 | -48.50798 | 2025-08-23 04:04:00 | NOAA-20 | CALDAS NOVAS | GOIÁS | Brasil | 5204508 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f4905583-7cff-38bb-a8d5-174e4045dbb5 | -22.15702 | -44.59417 | 2025-08-23 04:04:00 | NOAA-20 | ALAGOA | MINAS GERAIS | Brasil | 3101300 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 1ea85ae2-2ddb-3dd8-878f-f10cdc3c1edf | -15.2235 | -53.86098 | 2025-08-23 04:04:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 9eb99ac8-f538-3fd1-96ad-0507a88079ab | -18.2676 | -45.57901 | 2025-08-23 04:04:00 | NOAA-20 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e494b837-dac4-38d2-b32e-6b2236bb2bab | -19.96525 | -47.51733 | 2025-08-23 04:04:00 | NOAA-20 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 546502e8-c85e-33aa-aa6a-f73c2e00cfb2 | -22.47225 | -44.28629 | 2025-08-23 04:04:00 | NOAA-20 | BARRA MANSA | RIO DE JANEIRO | Brasil | 3300407 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| c4be0e25-5ca4-3727-acd0-0dd52cb65145 | -20.11636 | -47.78429 | 2025-08-23 04:04:00 | NOAA-20 | ARAMINA | SÃO PAULO | Brasil | 3503000 | 35 | 33 | nan | nan | nan | Cerrado | 4.2 |
| ddd3a9c4-3722-3154-995c-0da786e0b5cf | -17.27594 | -46.76332 | 2025-08-23 04:04:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6f0a6594-24d3-3ab9-939d-0651040f2456 | -22.16607 | -43.27729 | 2025-08-23 04:04:00 | NOAA-20 | PARAÍBA DO SUL | RIO DE JANEIRO | Brasil | 3303708 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 673dc64f-fff3-3483-8c50-442eb5d62867 | -21.90447 | -47.24873 | 2025-08-23 04:04:00 | NOAA-20 | SANTA CRUZ DAS PALMEIRAS | SÃO PAULO | Brasil | 3546306 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 90cd5ba2-99a3-3a36-9114-6293815b014c | -17.27119 | -46.76356 | 2025-08-23 04:04:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 65c26bc8-ffea-301a-b799-69b0efdb3caf | -18.85803 | -49.46938 | 2025-08-23 04:04:00 | NOAA-20 | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 779d9df7-a8ca-38e6-8098-4b1d2a1fe906 | -18.06436 | -47.87172 | 2025-08-23 04:04:00 | NOAA-20 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b29f10f6-5837-30c4-85a5-e3014e8f49cd | -20.25101 | -46.65407 | 2025-08-23 04:04:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1d11ba64-b384-3117-a910-60edf6705569 | -17.04547 | -47.13442 | 2025-08-23 04:04:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0d180f8b-59ae-3d6a-8164-13df11e503bd | -17.6102 | -46.69688 | 2025-08-23 04:04:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5c116bf2-2e81-3015-b361-d25f3944dcdf | -16.61389 | -49.40452 | 2025-08-23 04:04:00 | NOAA-20 | TRINDADE | GOIÁS | Brasil | 5221403 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d541dcef-ed4c-3396-9b0a-0240f75e62c9 | -20.09431 | -47.77424 | 2025-08-23 04:04:00 | NOAA-20 | ARAMINA | SÃO PAULO | Brasil | 3503000 | 35 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 28f8e306-b47e-3c6d-a382-d31bbd99c671 | -19.93704 | -44.94017 | 2025-08-23 04:04:00 | NOAA-20 | NOVA SERRANA | MINAS GERAIS | Brasil | 3145208 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 005bfcc5-86b1-388d-b17a-73654a2dd787 | -14.69767 | -54.91624 | 2025-08-23 04:04:00 | NOAA-20 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| df24963d-3954-3a2e-96ff-2409e52d4725 | -20.0933 | -47.75806 | 2025-08-23 04:04:00 | NOAA-20 | IGARAPAVA | SÃO PAULO | Brasil | 3520103 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 83415263-69bb-357a-945f-4a7f2c562ccf | -20.28391 | -46.63716 | 2025-08-23 04:04:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b1f5c657-0c29-37d2-85c3-c46665832e4e | -17.27217 | -46.76249 | 2025-08-23 04:04:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 089dab2f-0ad3-3c1a-a9bd-ed26477d9d20 | -17.26655 | -46.76755 | 2025-08-23 04:04:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 5.5 |
| daeef4aa-fa99-37b0-9771-b7dca00753cc | -23.10152 | -46.79768 | 2025-08-23 04:04:00 | NOAA-20 | ITATIBA | SÃO PAULO | Brasil | 3523404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| adb31a42-61f2-374d-acf3-e1a752950b4e | -20.35268 | -45.45113 | 2025-08-23 04:04:00 | NOAA-20 | FORMIGA | MINAS GERAIS | Brasil | 3126109 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 257cb8a8-3939-3963-974b-9572223cfadd | -20.39596 | -45.4469 | 2025-08-23 04:04:00 | NOAA-20 | FORMIGA | MINAS GERAIS | Brasil | 3126109 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |


[Clique aqui para ver as próximas entradas](README31.md)
