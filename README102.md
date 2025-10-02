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

## Dados Diários - Página 102

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ef4b0958-f247-338e-a0c4-21fb04f08370 | -13.46509 | -47.25731 | 2025-10-02 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 47a95f40-2090-3c1b-9be2-f4e7b9fab9ff | -16.13871 | -46.68089 | 2025-10-02 04:32:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c0655696-5848-3f46-9cac-0aaae971892a | -13.80031 | -47.53794 | 2025-10-02 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 5c227cf1-c9d6-3631-9ce6-422b9a63af98 | -13.01048 | -45.21399 | 2025-10-02 04:32:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| d94ccdbe-0184-3ae4-9ca9-c5de9f1d50e3 | -11.9102 | -47.88243 | 2025-10-02 04:32:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| ec4805b2-0db1-3b8d-833f-f19e154c32f1 | -19.51631 | -43.60836 | 2025-10-02 04:32:00 | NPP-375D | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2f42e332-2d52-3c15-ad0f-4b53aff60035 | -17.56315 | -44.80159 | 2025-10-02 04:32:00 | NPP-375D | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 695aa1f3-15b0-3329-a444-14f4f8358158 | -15.23616 | -46.96291 | 2025-10-02 04:32:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 42776bbe-c8de-34ba-aaf2-d085bd86d81b | -12.85295 | -46.86545 | 2025-10-02 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7eb01e50-368f-39e2-80cb-77942414cef6 | -19.85721 | -42.58778 | 2025-10-02 04:32:00 | NPP-375D | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| df273985-6aa8-3254-81e2-1c0cfea56980 | -16.36831 | -47.05564 | 2025-10-02 04:32:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 37dba282-2ba5-3c6b-991e-dad66cb5ca99 | -13.56202 | -47.28367 | 2025-10-02 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 920296ee-d009-3286-8e7e-b675b8c724e0 | -17.09151 | -48.56082 | 2025-10-02 04:32:00 | NPP-375D | VIANÓPOLIS | GOIÁS | Brasil | 5222005 | 52 | 33 | nan | nan | nan | Cerrado | 16.2 |
| d852e530-4a10-31eb-9e13-5ded01f221a9 | -11.90908 | -47.8895 | 2025-10-02 04:32:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 241b6056-abfc-339e-aa5a-6a8988f4438a | -13.17167 | -47.83726 | 2025-10-02 04:32:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8413c675-0d8a-398a-b867-8c1222feecd8 | -12.81539 | -48.56382 | 2025-10-02 04:32:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5c443d6f-9a76-3aeb-bd56-fb5bb1b3f3bb | -13.21567 | -48.4978 | 2025-10-02 04:32:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 51a54c1b-e3d0-3a36-b31d-29f79be0456d | -13.7511 | -47.99781 | 2025-10-02 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9f3e382a-0541-3603-9747-b517f8cc54bc | -16.09554 | -48.59451 | 2025-10-02 04:32:00 | NPP-375D | ALEXÂNIA | GOIÁS | Brasil | 5200308 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 74eea07b-22ca-33a4-8fdf-0d1953f09a32 | -17.95023 | -45.03347 | 2025-10-02 04:32:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e7277337-fe09-36cf-a442-9ee7f8bca13b | -14.35406 | -43.84034 | 2025-10-02 04:32:00 | NPP-375D | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e3506708-2590-3560-a033-aa351ee3fad3 | -12.1985 | -47.80902 | 2025-10-02 04:32:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| da353f83-71b2-3e16-8445-04891699ce35 | -15.92937 | -43.33508 | 2025-10-02 04:32:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d2ce072f-d707-331a-8834-681bd10485d1 | -14.47066 | -48.43031 | 2025-10-02 04:32:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5d3c8534-b3b0-3d56-b78e-59b8c7f2697a | -17.55349 | -44.48491 | 2025-10-02 04:32:00 | NPP-375D | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 348a983c-c02c-39e9-9ed0-dec90b35f0f8 | -13.86016 | -51.24092 | 2025-10-02 04:32:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| abc34523-3467-36d9-89ee-f3e6cfbd7e04 | -18.18331 | -53.27896 | 2025-10-02 04:32:00 | NPP-375D | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a6b4ca2c-fffa-3969-9a97-8c16a5a5791a | -18.64758 | -48.04237 | 2025-10-02 04:32:00 | NPP-375D | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b09973d5-5071-3449-9041-b38878e21dba | -13.20948 | -48.51508 | 2025-10-02 04:32:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 1d5a4a3c-9463-3142-86bf-39e2105bbd99 | -14.39886 | -46.0882 | 2025-10-02 04:32:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 90abff25-ad0d-36dd-a18e-0c8c2450a7d7 | -14.42302 | -46.11582 | 2025-10-02 04:32:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d5b87f37-df0a-3504-825d-831ea3a79d9a | -12.49886 | -50.24311 | 2025-10-02 04:32:00 | NPP-375D | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 6e093d1e-d6a6-31ba-8eac-954af904adb4 | -15.40217 | -47.04198 | 2025-10-02 04:32:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fea924a3-513e-3926-b829-2811d3578a54 | -12.8429 | -46.86377 | 2025-10-02 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8f8b8c50-57d3-3221-bfba-b525aa309064 | -15.13831 | -48.01985 | 2025-10-02 04:32:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2d07d797-750c-310d-b893-7a0083d95618 | -14.91489 | -47.23631 | 2025-10-02 04:32:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| a0b9799b-d916-33d2-a941-46ff2dd31051 | -13.37383 | -47.30151 | 2025-10-02 04:32:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3f0abd04-430a-35ad-b387-945fcb4cfe98 | -12.24284 | -47.83083 | 2025-10-02 04:32:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fb5e9053-aad0-39ab-8f21-08aed19757e8 | -13.52688 | -47.25644 | 2025-10-02 04:32:00 | NPP-375D | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f8b585f4-ce55-3830-9715-4e5abb29b2e2 | -14.91938 | -47.22956 | 2025-10-02 04:32:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 795c1406-69e5-3999-b7f5-6a64f0021832 | -13.4017 | -47.55458 | 2025-10-02 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| dffc9610-4bb5-3738-9d1e-7614f34b860d | -14.88879 | -48.30896 | 2025-10-02 04:32:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 47384ad3-6076-35dc-b44e-10ed3b6e6c0a | -12.93599 | -48.42193 | 2025-10-02 04:32:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2c1b23f3-ba20-32c6-9bc9-761999104f23 | -12.50458 | -50.25232 | 2025-10-02 04:32:00 | NPP-375D | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| bb42c4ee-8b67-3772-9cca-8926f90bb552 | -14.59035 | -46.71724 | 2025-10-02 04:32:00 | NPP-375D | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 050f660b-506c-3882-ab50-8f97de67d661 | -12.70568 | -48.57128 | 2025-10-02 04:32:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1d99c960-677b-3fb4-86e1-95368f3b8ae5 | -13.93818 | -48.09747 | 2025-10-02 04:32:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| af94b0bf-6fda-363a-ae02-4d98f47efadc | -12.66564 | -48.57556 | 2025-10-02 04:32:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 61cbeef9-2333-3b39-9417-000cceb28c44 | -13.16946 | -47.82962 | 2025-10-02 04:32:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5d9728a7-b29b-369f-b014-72a8b38065a5 | -12.02016 | -46.63487 | 2025-10-02 04:32:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bad6a7f4-e5e6-341f-8aba-e517710fdb80 | -13.85868 | -51.24947 | 2025-10-02 04:32:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 009f6a29-bb84-3578-b04f-07710f1b2887 | -13.56595 | -48.10212 | 2025-10-02 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c0032734-ea7e-3591-8e8a-4db2ae7fefcc | -15.34011 | -46.29217 | 2025-10-02 04:32:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8fb5ab3c-33de-3dd1-a006-97c9a0a95c98 | -15.22789 | -50.11647 | 2025-10-02 04:32:00 | NPP-375D | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 75d63303-bf2b-3ffc-9501-8539b3bd6af6 | -13.24306 | -47.33853 | 2025-10-02 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d9341445-c3b1-3198-92fa-111ca60271e1 | -17.67748 | -43.83551 | 2025-10-02 04:32:00 | NPP-375D | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ee3b7aff-f156-35d2-a564-aa4e3fb58351 | -14.02271 | -47.99463 | 2025-10-02 04:32:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5b6e74a4-a91b-317c-9e0c-2d50f5653a9e | -14.30604 | -45.89211 | 2025-10-02 04:32:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bdf183e7-bdd9-3523-9905-6db05b6d6fd2 | -13.29032 | -47.25483 | 2025-10-02 04:32:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| c526493f-ac94-3988-9c21-7b5d9cdb34ed | -13.75167 | -47.99425 | 2025-10-02 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e4752f2f-3b3f-3505-811a-6a2b0392b526 | -14.90429 | -48.31888 | 2025-10-02 04:32:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| efb5a87c-3987-3dda-ae81-b984eea2b4d9 | -13.21119 | -48.50439 | 2025-10-02 04:32:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e61aeb5a-7a5a-3c88-91c0-4c09277c733e | -12.90729 | -47.16804 | 2025-10-02 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1aa0e1f4-69a2-38fe-95f3-b04d301a119e | -19.46368 | -43.6545 | 2025-10-02 04:32:00 | NPP-375D | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 04c445f2-f28c-395e-8ff1-1e3da6cc57c5 | -18.506 | -44.02737 | 2025-10-02 04:32:00 | NPP-375D | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9f3fcb72-c02a-3d0f-9fc5-ee5cdbeb955c | -12.8999 | -46.91734 | 2025-10-02 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6a25fd10-bfb9-38ec-8ff3-a8a3706033bb | -19.95949 | -43.65655 | 2025-10-02 04:32:00 | NPP-375D | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.5 |
| cfa1dab6-3263-3ad8-b487-edb464531ce0 | -12.83955 | -46.86319 | 2025-10-02 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d1069242-4228-3972-83e8-f18bfe11eeef | -12.47863 | -47.27429 | 2025-10-02 04:32:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 06044cd5-e3e5-318a-9ed2-8cce8fbfa2c9 | -14.86301 | -48.39311 | 2025-10-02 04:32:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b7adee17-7fab-3728-bb2b-f037d230c49d | -15.42818 | -42.76649 | 2025-10-02 04:32:00 | NPP-375D | MATO VERDE | MINAS GERAIS | Brasil | 3141009 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1d4e882f-da38-3a6b-be8d-bd775e208eec | -15.13971 | -48.02394 | 2025-10-02 04:32:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 41fa852c-9216-3ff6-8b62-7384be6aa8b7 | -14.9021 | -48.31118 | 2025-10-02 04:32:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 08cf7df8-b819-3a5b-a38c-4585b9fa3f15 | -11.82473 | -48.07548 | 2025-10-02 04:32:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8593ebad-ba2e-3119-8c84-5d0c58cc09c5 | -13.52019 | -47.25538 | 2025-10-02 04:32:00 | NPP-375D | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0b7557ac-736a-3ad5-9d90-fb3b26ee4be3 | -14.68447 | -49.61563 | 2025-10-02 04:32:00 | NPP-375D | PILAR DE GOIÁS | GOIÁS | Brasil | 5216908 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 4e236fc2-7a12-3a6c-bf05-4f9eeae9d042 | -17.16609 | -47.03022 | 2025-10-02 04:32:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 5c91f7db-2ea1-34a1-8fb5-64703ad0dd8a | -13.47287 | -47.25134 | 2025-10-02 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9084a8bd-1227-3834-b977-e03da63f4bc3 | -14.9666 | -46.89886 | 2025-10-02 04:32:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 794a90d6-ce22-3f61-aa0e-0514bbbe271b | -13.95481 | -48.10023 | 2025-10-02 04:32:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e5398c16-2041-3e1f-896a-bc67a95dbad9 | -14.40863 | -46.09381 | 2025-10-02 04:32:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 89011e18-7cf4-3a28-8ff1-78df5d1a23dd | -12.41348 | -54.36116 | 2025-10-02 04:32:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8be54432-161e-35a2-a93c-c67c428185b5 | -13.0146 | -45.21049 | 2025-10-02 04:32:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5cc550b6-e093-3b44-b0dd-3db2f2d7ffb2 | -13.50849 | -48.20572 | 2025-10-02 04:32:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 604f77dc-73c3-31a1-b55e-c66ab2668a4e | -19.71135 | -45.91101 | 2025-10-02 04:32:00 | NPP-375D | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 5f31909b-5074-3b79-b69c-5d85ec789fd3 | -14.32225 | -45.87873 | 2025-10-02 04:32:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 06b0a1eb-dbfd-3210-842c-7b0cdaac6f56 | -13.3003 | -47.21267 | 2025-10-02 04:32:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5c014c06-e872-35e9-96b9-a1cf33aa235b | -12.89767 | -46.90958 | 2025-10-02 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6312b6ce-ae9a-3f54-b41d-5b8372ff5ad9 | -13.96711 | -44.87067 | 2025-10-02 04:32:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| df14b0d3-b836-33e9-9a46-7f90a583d6e1 | -16.36533 | -47.07381 | 2025-10-02 04:32:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1ecc80b8-af84-3a45-a38b-1d658b29d778 | -15.29422 | -46.38752 | 2025-10-02 04:32:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 69ecc475-ee44-3403-9e82-ce43011668ce | -19.45504 | -44.27768 | 2025-10-02 04:32:00 | NPP-375D | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 431893e7-f3f7-3a26-b345-a11819ea6064 | -14.86665 | -48.2837 | 2025-10-02 04:32:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c0dcb147-d8f4-3630-bc63-f83a262b4f09 | -17.1143 | -47.11998 | 2025-10-02 04:32:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f93f0b29-c746-3531-8f02-c8830e8deb35 | -13.15396 | -47.79794 | 2025-10-02 04:32:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 78fa5e88-2d68-3fe2-924f-e740e681b49d | -15.83544 | -46.24669 | 2025-10-02 04:32:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ce685901-1f5d-3fae-9012-9a633d6a00a9 | -15.33557 | -47.94564 | 2025-10-02 04:32:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 84ee09ec-9963-3cba-af09-ca057a3bc806 | -12.01681 | -46.63432 | 2025-10-02 04:32:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6dd4c859-0b41-36bc-bf69-c1533aec2748 | -14.89468 | -48.3796 | 2025-10-02 04:32:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b96debc3-c57b-3aba-8913-c6577176f13e | -12.7655 | -50.55156 | 2025-10-02 04:32:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |


[Clique aqui para ver as próximas entradas](README103.md)
