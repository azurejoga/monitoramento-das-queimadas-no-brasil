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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d0cdcf4c-0194-3997-9599-a3aef216ba27 | -17.69276 | -46.74583 | 2025-07-09 04:23:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ff0bd414-ed5a-30a9-b047-89b91eeb563d | -12.57885 | -56.97133 | 2025-07-09 04:23:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f98b6438-0861-356e-8c02-f4edc4dfe160 | -13.63859 | -44.41704 | 2025-07-09 04:23:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| a433236f-62a1-3bb5-8d99-f9145be9b3c4 | -12.98406 | -44.87025 | 2025-07-09 04:23:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 17679e0b-02ef-38ff-9299-acd16bca41be | -13.3989 | -47.90073 | 2025-07-09 04:23:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9aa2f915-065c-36a9-9702-1f1939fb8673 | -17.69112 | -46.73434 | 2025-07-09 04:23:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 6d783bb3-d1af-3a16-8285-ecdd8b74bf4a | -13.00547 | -46.76384 | 2025-07-09 04:23:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c3ba1a45-61bf-3dd8-9f8b-31a65077bd75 | -13.36513 | -47.78459 | 2025-07-09 04:23:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 23c7f8b0-0073-3e96-8eeb-aec66e680776 | -13.64712 | -46.81502 | 2025-07-09 04:23:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 0.3 |
| f69d8669-836c-33a5-8887-5e3a8de4e184 | -12.9778 | -47.82442 | 2025-07-09 04:23:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0e84dceb-1276-34f8-b241-14d9e5f520d6 | -16.68044 | -43.88529 | 2025-07-09 04:23:00 | NPP-375D | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d2f3a4dc-2a66-3801-8da8-55fd0f335785 | -12.98236 | -44.88124 | 2025-07-09 04:23:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 70986b5e-1b99-3883-9ddd-2946fd152f23 | -13.39519 | -47.88094 | 2025-07-09 04:23:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 19696430-4f75-35bd-ba4d-f16d49aa6aa8 | -17.26849 | -49.00783 | 2025-07-09 04:23:00 | NPP-375D | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| bddcdaf1-b2d5-3457-baab-e05e5fb0edbf | -15.64176 | -46.43779 | 2025-07-09 04:23:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2845d972-e513-3d8f-b077-bd3367aabc85 | -17.75283 | -42.89482 | 2025-07-09 04:23:00 | NPP-375D | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cd86ca69-11d7-37b9-8090-c087a46cd312 | -13.01107 | -46.75011 | 2025-07-09 04:23:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ddd6d7da-b2d5-3072-ae23-6b120b6c3c1c | -12.98349 | -44.87391 | 2025-07-09 04:23:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d87b23b6-517e-3e68-bec4-3f80ef5c0347 | -15.78107 | -48.25377 | 2025-07-09 04:23:00 | NPP-375D | ÁGUAS LINDAS DE GOIÁS | GOIÁS | Brasil | 5200258 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b249d36f-5f8f-3004-a159-feb09b421d14 | -13.38998 | -47.89137 | 2025-07-09 04:23:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8f6cab24-9610-3ade-9e11-fb91a834aad6 | -14.85621 | -45.12634 | 2025-07-09 04:23:00 | NPP-375D | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| bee88b5b-c973-3736-b169-9b85a4ee9783 | -17.69497 | -46.75368 | 2025-07-09 04:23:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6d5edc55-6b43-3065-b7c0-8ebf1e258e35 | -13.00837 | -46.29513 | 2025-07-09 04:23:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| e82b1587-74db-3f81-a477-5d6d9cd32002 | -13.01659 | -46.75832 | 2025-07-09 04:23:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bf427ddf-bf5f-34cf-aafc-05af023c30ce | -12.05196 | -48.54389 | 2025-07-09 04:23:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| df7624d0-09fc-335f-b156-a50355f34d3d | -15.78781 | -48.25507 | 2025-07-09 04:23:00 | NPP-375D | ÁGUAS LINDAS DE GOIÁS | GOIÁS | Brasil | 5200258 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1bb2c9eb-d783-3a15-9d07-2d6596a6b210 | -15.61732 | -46.46319 | 2025-07-09 04:23:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 558ae032-c410-37a1-9e44-66a69bfb4446 | -12.98012 | -44.87336 | 2025-07-09 04:23:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 245c0242-ad0d-369f-bd61-0bbc8726fd29 | -15.30568 | -47.37837 | 2025-07-09 04:23:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| dbe13967-6ada-3466-81ed-3a0648bdcff8 | -17.77658 | -42.80675 | 2025-07-09 04:23:00 | NPP-375D | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f5d2a22b-2dd0-3afd-b24b-be50357261d8 | -13.3872 | -47.88707 | 2025-07-09 04:23:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a9960bed-9270-37cd-8b3a-74f48c148889 | -12.09783 | -44.73704 | 2025-07-09 04:23:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 95096cab-7981-3aa0-ab5e-b05f91cfcf79 | -13.92786 | -43.94667 | 2025-07-09 04:23:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8f481fbc-8417-3a26-8de9-a9c7a4d608d9 | -16.37955 | -54.5787 | 2025-07-09 04:23:00 | NPP-375D | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 35a06437-cdb6-3da8-87ea-ddb053c2194d | -11.52394 | -48.95683 | 2025-07-09 04:23:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3cede056-c797-3294-9130-0e45648247eb | -12.46998 | -46.9098 | 2025-07-09 04:23:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b32fe731-8161-3a07-bcc0-2b6d0e776438 | -13.32065 | -42.28356 | 2025-07-09 04:23:00 | NPP-375D | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 3.9 |
| e9341e69-f7b4-3919-8468-a9ef97a91493 | -11.90233 | -49.19543 | 2025-07-09 04:23:00 | NPP-375D | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 57b7c8fc-a0c9-3240-a382-fde6af5fc94b | -13.00893 | -46.2916 | 2025-07-09 04:23:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 26c941b2-b89b-3081-b023-698aa6e1295b | -17.78046 | -42.80734 | 2025-07-09 04:23:00 | NPP-375D | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 90431759-aa1c-302b-b0ba-f9ee8646a4e1 | -14.8596 | -45.12688 | 2025-07-09 04:23:00 | NPP-375D | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 2353873f-e9c4-3e6c-bc03-870e237ce461 | -11.4195 | -54.33623 | 2025-07-09 04:23:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 97e3d9ec-173a-3174-bacb-a6af4d702300 | -15.19515 | -44.05903 | 2025-07-09 04:23:00 | NPP-375D | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 18aaec51-6b31-35dc-bda5-7bfe368db514 | -10.3427 | -56.4895 | 2025-07-09 04:23:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 39fa0ff2-8c5a-369c-b69c-8d8b1e11a21b | -17.7128 | -46.72684 | 2025-07-09 04:23:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d918eae0-7041-3a10-98ca-8bfad27b66ad | -17.6961 | -46.7464 | 2025-07-09 04:23:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a1908542-39cd-31fa-88b8-5688e34e85bb | -11.8028 | -46.6609 | 2025-07-09 04:23:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 4b1ddc49-c91d-3ce7-aa33-7ec4ffb7430b | -17.68999 | -46.74162 | 2025-07-09 04:23:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 7.4 |
| bb7a92fc-fca8-3050-8e0c-76062ac445c6 | -17.68723 | -46.73742 | 2025-07-09 04:23:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3231f573-8305-3180-9243-86d293e775a9 | -13.70038 | -45.61307 | 2025-07-09 04:23:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f91f32c6-4a36-3094-8b49-7c7e2fa565e0 | -11.42455 | -54.3372 | 2025-07-09 04:23:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4b9541de-cdfd-3b24-992d-a709de23cd29 | -17.69056 | -46.73798 | 2025-07-09 04:23:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 7.4 |
| eca69547-6157-3860-bc50-5117d9459e7b | -17.70947 | -46.72626 | 2025-07-09 04:23:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 5203533a-6fd0-322b-90ae-6a78cf4ae2c0 | -13.39119 | -47.88401 | 2025-07-09 04:23:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bc052e3f-4821-3ba0-94ff-7973d0dfe55c | -12.98068 | -44.8697 | 2025-07-09 04:23:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a030f6bf-3a0b-32b6-8c81-2329be0c1b28 | -16.63138 | -42.21197 | 2025-07-09 04:23:00 | NPP-375D | CORONEL MURTA | MINAS GERAIS | Brasil | 3119500 | 31 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 90e8444c-df90-32e9-876f-b2c582ae576b | -16.66074 | -46.03137 | 2025-07-09 04:23:00 | NPP-375D | BONFINÓPOLIS DE MINAS | MINAS GERAIS | Brasil | 3108206 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a78d7619-8cc5-3a3e-8998-a6cff9b1d79f | -12.97718 | -47.82814 | 2025-07-09 04:23:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b3251025-0579-39f1-a9bf-5470992a95d8 | -12.97843 | -44.88435 | 2025-07-09 04:23:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b24441d9-8b65-38f8-bed1-d9be8e2bf463 | -15.12622 | -44.01662 | 2025-07-09 04:23:00 | NPP-375D | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 23e75628-db08-3d44-82c0-6939a2f890a8 | -14.85678 | -45.12262 | 2025-07-09 04:23:00 | NPP-375D | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 95597948-1072-3d20-bff2-aa11bb73c9d3 | -13.38936 | -47.89512 | 2025-07-09 04:23:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 39371ec2-fe23-3d42-a212-54363c3d258a | -12.9744 | -47.82384 | 2025-07-09 04:23:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a75b82b9-1bbb-3525-a666-ba630ccccd62 | -15.0784 | -48.94487 | 2025-07-09 04:23:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 53aa3930-600e-37ab-bdf5-159832d85e41 | -13.02001 | -46.28616 | 2025-07-09 04:23:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 150c7942-9906-35de-8382-e4ebcb5fb677 | -16.0018 | -46.37852 | 2025-07-09 04:23:00 | NPP-375D | URUANA DE MINAS | MINAS GERAIS | Brasil | 3170479 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 275e0a38-1096-323a-a988-f7129f82fcf6 | -12.97787 | -44.88801 | 2025-07-09 04:23:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 52c44d7d-032b-3dfc-ae99-29a76eebb05b | -15.37428 | -47.52662 | 2025-07-09 04:23:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 4c3b7a6d-e5b7-3a08-94fd-970a7156bf86 | -12.04778 | -48.54728 | 2025-07-09 04:23:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 516e53ac-fda5-35ec-b9fc-f2e4b8dd4127 | -13.0105 | -46.75365 | 2025-07-09 04:23:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bb07b05d-1994-3099-a8e7-a3823cc19ded | -12.50086 | -43.1524 | 2025-07-09 04:23:00 | NPP-375D | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2f2e2abc-e952-31c8-bd80-d01cf17f8d0d | -17.69333 | -46.7422 | 2025-07-09 04:23:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 02cf646f-b9f1-39bb-a24e-920f0b53fb33 | -17.21468 | -46.84568 | 2025-07-09 04:23:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7ff9b2b0-0433-367e-9402-6d358387b0a3 | -12.0343 | -48.76027 | 2025-07-09 04:23:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e9026c90-39e1-3ebc-9bc0-d110ccda02d9 | -13.70316 | -45.6172 | 2025-07-09 04:23:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f87fc403-0f29-33e4-9d79-c019e724a39b | -11.50953 | -48.95436 | 2025-07-09 04:23:00 | NPP-375D | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1cc502af-b081-3df6-a877-15290dc4f13c | -14.85565 | -45.13006 | 2025-07-09 04:23:00 | NPP-375D | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 884ac197-9c38-3f1f-9e07-69960903e373 | -13.01669 | -46.28561 | 2025-07-09 04:23:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0a82dfed-003d-388b-b84a-2b70fc682946 | -12.47332 | -46.91035 | 2025-07-09 04:23:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b277570e-e622-382e-a013-457edbc81a17 | -16.6274 | -42.21156 | 2025-07-09 04:23:00 | NPP-375D | CORONEL MURTA | MINAS GERAIS | Brasil | 3119500 | 31 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 7bb3ed62-f51c-333c-839d-39a135d76575 | -13.39952 | -47.89693 | 2025-07-09 04:23:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d877e138-fcaa-32cb-aab8-f71914657ee6 | -17.6922 | -46.74947 | 2025-07-09 04:23:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5485da7b-0f4d-3375-afaa-2ad198390211 | -17.89804 | -43.99594 | 2025-07-09 04:23:00 | NPP-375D | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 2a01290b-b7f9-3d14-93f4-f8c261f9ff77 | -13.01383 | -46.7542 | 2025-07-09 04:23:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 114b673d-5c7c-30f3-a840-7b0ea540747e | -12.98124 | -44.88856 | 2025-07-09 04:23:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 261f91ae-b88d-3b7d-8ccb-e9ba1f51bdcd | -17.90306 | -44.30057 | 2025-07-09 04:23:00 | NPP-375D | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| af5127d1-3b3f-3294-9c42-53a7a9755939 | -13.54425 | -44.13639 | 2025-07-09 04:23:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c355718a-0e64-3061-b745-b7b6a6a52a5f | -13.10488 | -46.8822 | 2025-07-09 04:23:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 32f2c955-f73d-3eae-8eef-05198eca4c96 | -13.00661 | -46.7567 | 2025-07-09 04:23:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 87aecf63-6b35-3296-8fa8-650dfcfc6a45 | -13.00823 | -46.76794 | 2025-07-09 04:23:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e3fbbbe8-69a9-3a72-891d-a85ed1935fad | -12.97956 | -44.87703 | 2025-07-09 04:23:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cf72ade9-078a-35e2-9547-b9967207db48 | -13.70372 | -45.61361 | 2025-07-09 04:23:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 569f3a2a-81d0-3589-a684-0f18a0ecf53d | -13.00604 | -46.76027 | 2025-07-09 04:23:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1031f98e-1e6b-3ca2-8224-ae83a6dcd62c | -12.4661 | -44.49693 | 2025-07-09 04:23:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 94cba33b-6a71-3bf3-adea-368f2d8c73c7 | -14.85904 | -45.13061 | 2025-07-09 04:23:00 | NPP-375D | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 51052379-f448-357f-a5a4-f6d506f0ec9b | -11.70991 | -48.79974 | 2025-07-09 04:23:00 | NPP-375D | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 8f7b4b6d-fa6a-3060-8019-7e335a525269 | -11.52754 | -48.95745 | 2025-07-09 04:23:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a5379830-d40a-37bf-839f-7cc56868d1b1 | -10.34863 | -56.49059 | 2025-07-09 04:23:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 978a9803-c007-3816-98cc-e6571c31fb4b | -15.76257 | -45.05755 | 2025-07-09 04:23:00 | NPP-375D | SÃO FRANCISCO | MINAS GERAIS | Brasil | 3161106 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c7a54221-933e-3fc9-9f27-5bc97f416c46 | -10.29896 | -57.12662 | 2025-07-09 04:23:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |


[Clique aqui para ver as próximas entradas](README18.md)
