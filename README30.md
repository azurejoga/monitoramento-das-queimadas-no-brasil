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
| 2db38824-259c-3440-b666-33f05220cf6d | -17.86645 | -44.40407 | 2026-09-22 03:45:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| da49687e-e66d-3514-967e-3f72ebc69958 | -12.59998 | -45.0899 | 2026-09-22 03:45:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ea920d3a-2e33-3d98-8322-c8e148f16377 | -12.14934 | -47.39475 | 2026-09-22 03:45:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6b879936-df0a-35a5-86a1-04ccfcfde3db | -12.56309 | -45.96635 | 2026-09-22 03:45:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 021a8a87-1905-384e-ad69-33716167feed | -11.84958 | -46.81268 | 2026-09-22 03:45:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 7c8a602c-41c7-3311-80de-9e69541d1f47 | -11.93971 | -46.51959 | 2026-09-22 03:45:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| de7205ae-30e4-3c0b-9fdf-8ecbf5b2ca4a | -12.13939 | -47.38844 | 2026-09-22 03:45:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 679b0d3d-096b-3b40-91ac-c6f466f98a63 | -15.44908 | -43.81611 | 2026-09-22 03:45:00 | NPP-375D | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a578c0f4-bc8e-3798-b996-903a3e9adea8 | -12.84776 | -44.33515 | 2026-09-22 03:45:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 751db134-cb74-3cce-8438-bf0b33877636 | -11.3897 | -46.76046 | 2026-09-22 03:45:00 | NPP-375D | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| dfb66ed4-9bf8-3fb9-8a35-e8fa7c0dcc03 | -12.02426 | -47.81424 | 2026-09-22 03:45:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 186761f4-f37e-3dad-842d-1c7a6d1c3124 | -14.76999 | -48.44583 | 2026-09-22 03:45:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a6874f73-26ba-3878-b6cf-293e9400be2f | -15.99239 | -43.27996 | 2026-09-22 03:45:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 5ba4bb78-795c-3146-ace1-ac3b0b240394 | -12.01975 | -47.80021 | 2026-09-22 03:45:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d4d994bf-7ab4-3b7d-9bbb-f56108e9022e | -14.66244 | -45.66779 | 2026-09-22 03:45:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ca8840f3-8f9e-344b-a73a-0a0b6dc0bbe1 | -17.35769 | -41.19281 | 2026-09-22 03:45:00 | NPP-375D | NOVO ORIENTE DE MINAS | MINAS GERAIS | Brasil | 3145356 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 54052b2f-55cb-3101-8490-ed2a978bda83 | -12.03137 | -47.81301 | 2026-09-22 03:45:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 7d607359-22f7-3433-9ee6-50bd6490dc9c | -15.36235 | -48.11854 | 2026-09-22 03:45:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6f102292-dc69-3fe1-81f6-f843fcf58af6 | -11.15068 | -42.84124 | 2026-09-22 03:45:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| ecc9ad1c-230d-3385-b60a-257e54390175 | -15.62449 | -48.31843 | 2026-09-22 03:45:00 | NPP-375D | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a47ee1e8-1c90-3d83-a01f-6ff2325d3593 | -11.14659 | -42.83291 | 2026-09-22 03:45:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 5be730cb-2118-34b8-b710-4c9d95dcd9a3 | -11.66357 | -43.46358 | 2026-09-22 03:45:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8cfc6053-c5f3-394c-ab5b-29970670347c | -14.67363 | -45.67553 | 2026-09-22 03:45:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 6b6fb5d2-9928-3461-80fb-6b8c22dbc08e | -15.98722 | -43.27888 | 2026-09-22 03:45:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| fad94d41-29ea-3663-a962-ceb48d0c0ef0 | -14.76768 | -48.45586 | 2026-09-22 03:45:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 9794f63d-d3e0-33b5-aa23-8bfb04615f2d | -12.84106 | -44.33819 | 2026-09-22 03:45:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 1c0da8a5-c09e-3707-9390-992d6034ca6c | -12.56958 | -45.96769 | 2026-09-22 03:45:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8ca727bf-f69d-3580-8b19-c5707b2205cb | -11.40512 | -46.79753 | 2026-09-22 03:45:00 | NPP-375D | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3ae9222d-3a38-3cb8-892b-bf200df8cb64 | -15.99303 | -43.27673 | 2026-09-22 03:45:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 93ee576e-44d4-3d02-89c0-9097a50a846a | -12.56842 | -45.97324 | 2026-09-22 03:45:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 290afee3-3921-3351-883f-9ae449549b65 | -11.67642 | -43.4581 | 2026-09-22 03:45:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b1ca8373-8d78-3ba0-a03e-aadf73342d44 | -12.03289 | -47.80947 | 2026-09-22 03:45:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 87feb11d-49d5-3a89-9402-a4d922bf41fa | -15.74919 | -43.30681 | 2026-09-22 03:45:00 | NPP-375D | NOVA PORTEIRINHA | MINAS GERAIS | Brasil | 3145059 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9a83c45a-92c5-3971-89f9-6f375d922f78 | -15.44144 | -48.44161 | 2026-09-22 03:45:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b571a478-7433-3e54-b864-bba3530d7284 | -12.10445 | -45.6602 | 2026-09-22 03:45:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ed49a4ee-26f2-3f57-9dba-31384eb8554d | -12.09919 | -45.65327 | 2026-09-22 03:45:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 60a03a83-1d64-3b56-bd17-55e7708019f5 | -11.67488 | -43.46592 | 2026-09-22 03:45:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 055733f6-5140-33fb-bc9e-e22e6cc69381 | -10.01969 | -45.21152 | 2026-09-22 03:45:00 | NPP-375D | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 80207029-0dc7-3696-80be-14e1d246785c | -12.14077 | -47.40043 | 2026-09-22 03:45:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f357271b-48e4-3e17-a3b3-869b1730c33f | -11.44093 | -47.33253 | 2026-09-22 03:45:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| a6b03a15-4780-3bdd-9d43-02aa8a44587b | -12.84192 | -44.33391 | 2026-09-22 03:45:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 1f5c79d2-6cee-37a0-b121-9c59f11fd4ed | -11.41214 | -46.79853 | 2026-09-22 03:45:00 | NPP-375D | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9f07629b-ece6-326c-99ca-9e3875380bc9 | -15.35517 | -48.1082 | 2026-09-22 03:45:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 78c68bb8-ee42-3b80-82e8-9a49c715ffdc | -12.60612 | -45.09125 | 2026-09-22 03:45:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6e55f29f-84d1-3791-9712-5f2d4295d8d3 | -15.98778 | -43.27942 | 2026-09-22 03:45:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 5.1 |
| fdd57d1d-1155-3e20-bbc8-0bfcc7ee286e | -12.14228 | -47.3932 | 2026-09-22 03:45:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 94f9a2c2-7c27-3819-b056-754896a6af53 | -15.7246 | -41.57447 | 2026-09-22 03:45:00 | NPP-375D | ÁGUAS VERMELHAS | MINAS GERAIS | Brasil | 3101003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 31439e71-f30d-3b84-a679-37c9b7c94646 | -12.09808 | -45.65862 | 2026-09-22 03:45:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 563dd676-d8b2-355f-8a04-6be072f73713 | -15.3519 | -48.09998 | 2026-09-22 03:45:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 11a177de-2225-3b15-9bb9-a910c843156f | -11.40341 | -46.79805 | 2026-09-22 03:45:00 | NPP-375D | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 760583e9-d24c-3af6-a537-0eca29d6b404 | -15.96117 | -42.95742 | 2026-09-22 03:45:00 | NPP-375D | RIACHO DOS MACHADOS | MINAS GERAIS | Brasil | 3154507 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 51dbe998-bf3e-3889-9b5b-5186ece12211 | -14.66751 | -45.67411 | 2026-09-22 03:45:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| b0bf2c25-fc5d-321f-8431-4e2463024248 | -11.14519 | -42.84012 | 2026-09-22 03:45:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| c90d797b-2599-38af-bc6a-2ac1ebaa0668 | -11.42896 | -47.35385 | 2026-09-22 03:45:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 7a1961a5-bc0f-3c09-8417-ea59c67a8cb9 | -11.39534 | -46.76791 | 2026-09-22 03:45:00 | NPP-375D | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0f90fb74-db66-3da4-a290-d60cdf649268 | -10.02086 | -45.20572 | 2026-09-22 03:45:00 | NPP-375D | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9d1fdfab-0235-3d10-ae07-7d1efebed2a1 | -12.02413 | -47.81142 | 2026-09-22 03:45:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 1e9d5996-eea8-3fd9-86f8-841821d99e56 | -10.25111 | -45.49752 | 2026-09-22 03:45:00 | NPP-375D | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 523fe72b-4c1f-3922-bcb9-c8330f2c7b96 | -15.98482 | -42.99725 | 2026-09-22 03:45:00 | NPP-375D | RIACHO DOS MACHADOS | MINAS GERAIS | Brasil | 3154507 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b2b6522e-4651-3529-8afc-1315fd08250d | -15.44386 | -48.47563 | 2026-09-22 03:45:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b26282fc-381f-329f-9ea3-566d8310f7d3 | -15.05195 | -38.99913 | 2026-09-22 03:45:00 | NPP-375D | ILHÉUS | BAHIA | Brasil | 2913606 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 0dda0ede-6df1-32ce-882d-a246127590e3 | -12.02541 | -47.8054 | 2026-09-22 03:45:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| c8a035b6-078a-3255-a564-fb95ecaa00ee | -15.96055 | -42.96048 | 2026-09-22 03:45:00 | NPP-375D | RIACHO DOS MACHADOS | MINAS GERAIS | Brasil | 3154507 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1624e8f9-efb9-3668-82da-9529031446a8 | -13.62673 | -42.47968 | 2026-09-22 03:45:00 | NPP-375D | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| b60c45b8-7ea1-3edb-8628-32c63e5c1d54 | -10.25206 | -45.49273 | 2026-09-22 03:45:00 | NPP-375D | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d7b517f4-b8f2-3e16-9ad8-6a9a355eef93 | -12.84691 | -44.33944 | 2026-09-22 03:45:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 611d1365-f7b5-3c46-9df8-6a0382d2a1c8 | -12.1535 | -47.39156 | 2026-09-22 03:45:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 320273fe-76cd-3a15-80f5-5faf0534e3cb | -15.05595 | -38.99986 | 2026-09-22 03:45:00 | NPP-375D | ILHÉUS | BAHIA | Brasil | 2913606 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| ab844507-61e4-3cd9-b6ac-c2a404d26597 | -11.68208 | -43.45924 | 2026-09-22 03:45:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1d2f48fd-d6c7-3c57-8648-52d3b6fbe917 | -12.5578 | -45.95935 | 2026-09-22 03:45:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 3690ef03-a62c-39b5-8ddc-72c510793c3e | -12.84412 | -44.34084 | 2026-09-22 03:45:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 46bedbec-6636-33c0-9fa5-d8086b6275ab | -14.76295 | -48.4437 | 2026-09-22 03:45:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a9a9578a-953e-33a4-8f47-423dc2b810e8 | -11.14337 | -42.79094 | 2026-09-22 03:45:00 | NPP-375D | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 1c29457c-c468-32f5-b625-678572e836a9 | -11.41042 | -46.79908 | 2026-09-22 03:45:00 | NPP-375D | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4a6f7759-8e7f-39af-a255-66f797786b95 | -15.43986 | -48.44867 | 2026-09-22 03:45:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| bc6f886b-907a-3036-894e-932cbc7254d4 | -13.94155 | -42.96812 | 2026-09-22 03:45:00 | NPP-375D | MATINA | BAHIA | Brasil | 2921054 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 83c3a6aa-fcb0-35a6-b030-8e99a041744a | -11.15137 | -42.83763 | 2026-09-22 03:45:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 805e5e26-8fc1-31dc-95c0-17276a290bb7 | -14.63042 | -45.67326 | 2026-09-22 03:45:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7c22a517-a2db-3e06-ba24-287389724a33 | -15.98786 | -43.27566 | 2026-09-22 03:45:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 99186b41-9a3e-330e-ad5d-da854698a374 | -15.99295 | -43.28048 | 2026-09-22 03:45:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ee295924-6433-38a8-a5f0-1b7ab6e90c5a | -18.74751 | -45.59542 | 2026-09-22 03:47:00 | NPP-375D | BIQUINHAS | MINAS GERAIS | Brasil | 3107000 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3e0f19c2-8da8-31b6-9615-ae4257d19745 | -20.84821 | -43.40779 | 2026-09-22 03:47:00 | NPP-375D | RIO ESPERA | MINAS GERAIS | Brasil | 3155207 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 484f9184-0c30-3287-8027-7aaea11f8fbe | -20.84738 | -43.40836 | 2026-09-22 03:47:00 | NPP-375D | RIO ESPERA | MINAS GERAIS | Brasil | 3155207 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| d726e944-59c5-3785-b847-7d626cbaf0ca | -21.593 | -41.25398 | 2026-09-22 03:47:00 | NPP-375D | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 7b0c8432-25bd-3ff0-84dd-b61578c69807 | -18.76943 | -45.11598 | 2026-09-22 03:47:00 | NPP-375D | FELIXLÂNDIA | MINAS GERAIS | Brasil | 3125705 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 04a6e02f-5dce-37fe-90d3-fe3130cd1bf0 | -18.73665 | -46.94868 | 2026-09-22 03:47:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 380bbe63-3898-3378-8788-524712f8e8dd | -21.60041 | -41.215 | 2026-09-22 03:47:00 | NPP-375D | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| d3fd2b99-e007-32f0-ad58-e489d83475a2 | -20.39207 | -42.52474 | 2026-09-22 03:47:00 | NPP-375D | JEQUERI | MINAS GERAIS | Brasil | 3135506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 4d10cd6a-be1b-3d0e-b56f-8b6a026ce3bc | -18.76858 | -45.11989 | 2026-09-22 03:47:00 | NPP-375D | FELIXLÂNDIA | MINAS GERAIS | Brasil | 3125705 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 51f1c09c-c00b-3749-b824-2a8c82cf33fb | -18.74196 | -45.59359 | 2026-09-22 03:47:00 | NPP-375D | BIQUINHAS | MINAS GERAIS | Brasil | 3107000 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 285ecbee-0a76-37f2-9ab6-3aa3cd23e5af | -17.84168 | -45.78382 | 2026-09-22 03:47:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 17b99e76-348b-39f6-8c1c-d0ce4e56fc31 | -17.84075 | -45.78815 | 2026-09-22 03:47:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 05db2ce2-5016-3b4b-8806-836cc24d0d5a | -18.0228 | -46.72776 | 2026-09-22 03:47:00 | NPP-375D | LAGAMAR | MINAS GERAIS | Brasil | 3137106 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f00e7639-ed2d-3bf5-812e-1ceaf8d35d80 | -18.74329 | -45.59504 | 2026-09-22 03:47:00 | NPP-375D | BIQUINHAS | MINAS GERAIS | Brasil | 3107000 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e8363b72-f800-332d-929c-f9307c93f8a1 | -18.73781 | -46.94358 | 2026-09-22 03:47:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 25.3 |
| bbd02d5e-cd86-33bd-b4ac-485e90cf3efd | -21.58891 | -41.25306 | 2026-09-22 03:47:00 | NPP-375D | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| b871bc8a-c3e9-3b40-b6f4-e26afd9274c2 | -21.60115 | -41.21111 | 2026-09-22 03:47:00 | NPP-375D | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 3ebd1bd7-8b35-3400-ba75-5d7a90dc1aec | -18.73282 | -46.93711 | 2026-09-22 03:47:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 790ee6b4-eba9-3397-9b08-8d1cca5004cb | -18.02388 | -46.72295 | 2026-09-22 03:47:00 | NPP-375D | LAGAMAR | MINAS GERAIS | Brasil | 3137106 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3d9c8d1d-07cf-3fd2-8e8e-49d5688dd5fc | -18.73893 | -46.93863 | 2026-09-22 03:47:00 | NPP-375D | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 25.3 |


[Clique aqui para ver as próximas entradas](README31.md)
