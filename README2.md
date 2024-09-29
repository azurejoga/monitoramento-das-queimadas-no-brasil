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
| 73690b2a-2af7-3628-8048-658d0cd07df5 | -17.757799 | -43.312599 | 2024-09-29 00:45:14 | METOP-C | SENADOR MODESTINO GONÇALVES | MINAS GERAIS | Brasil | 3165909 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| ee632ce0-de52-3513-a795-1ab567ee99dc | -17.7598 | -43.320599 | 2024-09-29 00:45:14 | METOP-C | SENADOR MODESTINO GONÇALVES | MINAS GERAIS | Brasil | 3165909 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 6f2c2b27-eff1-3e63-b43c-cb2accdadc30 | -17.7635 | -43.3367 | 2024-09-29 00:45:14 | METOP-C | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 3234b2e7-e3bb-32ba-af77-225b0e2901c2 | -17.6276 | -43.243099 | 2024-09-29 00:45:16 | METOP-C | SENADOR MODESTINO GONÇALVES | MINAS GERAIS | Brasil | 3165909 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 4bdb4a82-267f-3cf8-8cdd-28536e77ed9e | -17.629499 | -43.251202 | 2024-09-29 00:45:16 | METOP-C | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 9e78b834-25f6-3978-a2b7-273c4f7763e0 | -17.817801 | -44.454498 | 2024-09-29 00:45:17 | METOP-C | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 15875f88-40c8-3ae6-9e69-822a49691181 | -17.799999 | -44.466801 | 2024-09-29 00:45:18 | METOP-C | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| c1af4dd4-cefc-3396-8090-9b4c5579a3e9 | -17.5047 | -44.485001 | 2024-09-29 00:45:22 | METOP-C | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| dd4eb573-0bad-32e2-8b97-21d92bf7840c | -17.856199 | -45.899601 | 2024-09-29 00:45:22 | METOP-C | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| e8945fca-44cb-3f5b-9aeb-74039afaac33 | -17.8578 | -45.906799 | 2024-09-29 00:45:22 | METOP-C | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| fb1c682c-049e-3087-8273-9642a0b815fd | -17.8594 | -45.914001 | 2024-09-29 00:45:22 | METOP-C | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| dbbca516-f980-3600-b399-0c8010910410 | -17.4949 | -44.4874 | 2024-09-29 00:45:23 | METOP-C | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 8543c037-ba94-3b8f-a0bf-7df6102c5f47 | -16.898001 | -45.305401 | 2024-09-29 00:45:35 | METOP-C | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| c48f2593-3c62-3284-a7ab-9fd7a00503fa | -16.899599 | -45.312599 | 2024-09-29 00:45:35 | METOP-C | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 20c0e695-f561-316a-990e-4c8e72ded9ba | -16.901199 | -45.319801 | 2024-09-29 00:45:35 | METOP-C | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| ce211bdd-6864-38a7-9a0c-f8990ec1a3f6 | -16.888201 | -45.307701 | 2024-09-29 00:45:35 | METOP-C | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 0ba60da5-b7ef-300e-bc0c-2a9cffd363ca | -16.889799 | -45.314899 | 2024-09-29 00:45:35 | METOP-C | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 81ebca63-b757-3094-9134-6c740b88b170 | -16.891399 | -45.322102 | 2024-09-29 00:45:35 | METOP-C | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| b54337f9-ca94-3160-9e23-88bc6e479766 | -16.878401 | -45.310101 | 2024-09-29 00:45:36 | METOP-C | SANTA FÉ DE MINAS | MINAS GERAIS | Brasil | 3157609 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 6e89bddb-37c9-3264-84ed-0a363c00e444 | -16.8801 | -45.317299 | 2024-09-29 00:45:36 | METOP-C | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 5cd9802b-7f14-3090-8743-6386b6faa7e2 | -15.7724 | -43.575298 | 2024-09-29 00:45:47 | METOP-C | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 447d77b3-b244-33e8-bc11-68ff202687ab | -17.724199 | -53.1549 | 2024-09-29 00:45:48 | METOP-C | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 902ad939-11a2-3f1b-8eea-787596dbb605 | -17.711599 | -53.141998 | 2024-09-29 00:45:48 | METOP-C | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 7747daeb-6113-317d-a217-1527f5480d20 | -17.714399 | -53.156898 | 2024-09-29 00:45:48 | METOP-C | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| ca27f4c8-e73b-3c58-bc29-1443f3182f9e | -17.717199 | -53.171902 | 2024-09-29 00:45:48 | METOP-C | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 47a9f0f6-ffcd-3afb-807b-6917a8ba2bd2 | -17.7019 | -53.143902 | 2024-09-29 00:45:49 | METOP-C | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 0c1a12be-d0db-38fb-a259-eaa88429b2f1 | -17.7047 | -53.158798 | 2024-09-29 00:45:49 | METOP-C | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 73e9ecd0-5b36-381a-8967-9da6a8458a33 | -15.8873 | -45.0373 | 2024-09-29 00:45:51 | METOP-C | SÃO FRANCISCO | MINAS GERAIS | Brasil | 3161106 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| db042f16-998f-35c0-a572-40ebe284ccdd | -15.889 | -45.044601 | 2024-09-29 00:45:51 | METOP-C | SÃO FRANCISCO | MINAS GERAIS | Brasil | 3161106 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 093d6a2f-1d54-36c9-867f-d298cd46e2d8 | -15.196 | -43.847301 | 2024-09-29 00:45:57 | METOP-C | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| cef735f5-69df-392f-9416-e7e3fb61be49 | -15.6374 | -47.220501 | 2024-09-29 00:46:03 | METOP-C | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 27b487c4-ebbd-33fa-963b-2309c5819803 | -15.639 | -47.227699 | 2024-09-29 00:46:03 | METOP-C | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 854b2a20-cee6-39d6-a746-1fe8948c2d72 | -15.4389 | -47.440399 | 2024-09-29 00:46:07 | METOP-C | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| e608fb90-d152-3e0a-8e04-c9ff05ce4f0e | -17.1085 | -56.147598 | 2024-09-29 00:46:07 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| ecdc1148-08bd-3ce2-8de0-d5648f65678e | -17.1126 | -56.170799 | 2024-09-29 00:46:07 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 38b1d683-8f63-36a1-92ba-02fc286fb832 | -17.1166 | -56.194099 | 2024-09-29 00:46:07 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 28ed2932-50f2-3c54-b906-c98814612d64 | -17.1029 | -56.1726 | 2024-09-29 00:46:08 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 528e92ff-965f-3eec-8c2c-be45ec7b3e29 | -17.106899 | -56.1959 | 2024-09-29 00:46:08 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 917d9ddc-bcb6-3635-a3b6-b76754abf185 | -15.3019 | -47.471901 | 2024-09-29 00:46:09 | METOP-C | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 273e1721-b9fe-3290-9a7b-872296b82c40 | -13.8968 | -41.6492 | 2024-09-29 00:46:10 | METOP-C | DOM BASÍLIO | BAHIA | Brasil | 2910107 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| c2894f61-4336-3f5d-a558-22ad6622a66d | -13.8995 | -41.659901 | 2024-09-29 00:46:10 | METOP-C | DOM BASÍLIO | BAHIA | Brasil | 2910107 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 087dff50-16d1-31fd-9964-14d6fa9991d6 | -17.0459 | -56.707298 | 2024-09-29 00:46:10 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 58c0e9ec-e595-36e8-819b-873d10b0d2a4 | -17.0362 | -56.709 | 2024-09-29 00:46:10 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| bad6942d-e2bb-34cc-8899-00e1c5699090 | -15.1543 | -47.362099 | 2024-09-29 00:46:11 | METOP-C | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| bb5812e1-02f9-3674-bd06-c3a14863a029 | -15.1558 | -47.369202 | 2024-09-29 00:46:11 | METOP-C | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 4ca286e1-1380-3a2d-823e-57671c9e89f6 | -16.426399 | -53.937901 | 2024-09-29 00:46:12 | METOP-C | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 08db986e-fee8-3439-bb3d-e28a330d5970 | -16.639 | -55.199699 | 2024-09-29 00:46:12 | METOP-C | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| bef2c640-94f8-34d0-986d-4c0ba0cb15fc | -16.629299 | -55.2015 | 2024-09-29 00:46:13 | METOP-C | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 8ba62d22-b4d8-341d-967b-328d7635d6a8 | -14.475 | -45.2244 | 2024-09-29 00:46:14 | METOP-C | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| c6cdb4cc-754c-399d-8856-e72353f49101 | -14.4767 | -45.231701 | 2024-09-29 00:46:14 | METOP-C | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 8a85a254-b4a0-3f41-9cb5-f8a508e25db2 | -14.4784 | -45.238998 | 2024-09-29 00:46:14 | METOP-C | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 99f2e3bb-ff86-313c-acb1-9b0a0bcec1d3 | -14.5802 | -45.725601 | 2024-09-29 00:46:14 | METOP-C | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 07c1e268-c9ae-3015-a84a-07c20fe7d146 | -14.5687 | -45.720901 | 2024-09-29 00:46:14 | METOP-C | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| c12312d2-fe4f-35d9-a939-a0cae05a7a8a | -14.5704 | -45.728001 | 2024-09-29 00:46:14 | METOP-C | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 7bca382d-2030-3a55-b73f-61d13ad551ae | -14.572 | -45.735199 | 2024-09-29 00:46:14 | METOP-C | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 33ce1886-b84e-342b-a1a0-fd06adf92dc9 | -14.5737 | -45.742298 | 2024-09-29 00:46:14 | METOP-C | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e416b590-250e-3ec8-b02a-5151b2bd11d5 | -14.5753 | -45.7495 | 2024-09-29 00:46:14 | METOP-C | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| f66b9345-7404-30dc-919c-fc10ff2289e9 | -14.183 | -44.240299 | 2024-09-29 00:46:15 | METOP-C | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 180ebfcc-9dc8-33d7-8d75-be2844c0c006 | -14.5606 | -45.730301 | 2024-09-29 00:46:15 | METOP-C | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 55862317-20a6-389c-9358-c2053c4069d8 | -14.5622 | -45.737499 | 2024-09-29 00:46:15 | METOP-C | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 4c28f74a-c241-3921-a3fa-b223b020ccd5 | -14.5639 | -45.744598 | 2024-09-29 00:46:15 | METOP-C | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 91bb74e2-05a1-339c-9b64-1645a4d964eb | -14.5655 | -45.751801 | 2024-09-29 00:46:15 | METOP-C | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 96ac4cc3-5727-3ae6-9568-18149d81b8b3 | -14.3948 | -45.189602 | 2024-09-29 00:46:15 | METOP-C | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 08fd62de-c8ad-32fd-be01-73c1c7116d96 | -16.938801 | -57.889999 | 2024-09-29 00:46:15 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 9ed0deb3-d783-38b5-81e6-255bf5560e96 | -16.943899 | -57.9202 | 2024-09-29 00:46:15 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| d0b0f09e-93ad-375b-be96-f1d8859b518d | -16.9291 | -57.891602 | 2024-09-29 00:46:15 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 72984d5f-ea7f-3c05-96b2-c1bff845df27 | -16.914499 | -57.863201 | 2024-09-29 00:46:16 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| dda6613f-adbb-3fb3-a628-fe6517c13b7d | -16.9195 | -57.893299 | 2024-09-29 00:46:16 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 58aa11c2-8351-34e7-952e-e15aec71e7e6 | -16.924601 | -57.923599 | 2024-09-29 00:46:16 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| a3be0eed-2108-388b-aadd-66929a426cce | -16.909901 | -57.895 | 2024-09-29 00:46:16 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 88b706c9-0be2-3893-a66b-e32780c72a25 | -16.9149 | -57.925301 | 2024-09-29 00:46:16 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 3f71a48c-a1cb-3e9c-baaf-c4a03fba96b7 | -16.9053 | -57.926899 | 2024-09-29 00:46:16 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| acf43beb-b939-3069-97f7-2c41781b7225 | -16.895599 | -57.9286 | 2024-09-29 00:46:16 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 7e1c5f62-b820-34a8-88b3-d571f9731152 | -14.3616 | -46.0331 | 2024-09-29 00:46:19 | METOP-C | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| ad7a333f-46d6-34f9-9991-e4a8a68c697e | -14.3632 | -46.040199 | 2024-09-29 00:46:19 | METOP-C | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| c4107a47-0254-3774-8585-7264b157c2fd | -13.3532 | -42.045399 | 2024-09-29 00:46:20 | METOP-C | ÉRICO CARDOSO | BAHIA | Brasil | 2900504 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 87b4220c-2cb8-34bf-86f3-3f43f65b2ec9 | -13.7806 | -44.330601 | 2024-09-29 00:46:22 | METOP-C | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 609018f5-b93f-376f-b092-7b8f88b4d81b | -13.7825 | -44.338501 | 2024-09-29 00:46:22 | METOP-C | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| c11355c7-4047-3836-9d38-bee214e47baf | -13.7843 | -44.346298 | 2024-09-29 00:46:22 | METOP-C | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| bbaa50e3-acef-3b4b-85d9-6faf8f211534 | -13.5458 | -43.431599 | 2024-09-29 00:46:22 | METOP-C | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 7c55d7da-e87b-3d9f-8f23-78a4d4a0f4c9 | -13.5479 | -43.4403 | 2024-09-29 00:46:22 | METOP-C | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 893bf11e-8c03-37cf-b0ba-a93867b3175c | -14.1745 | -46.4347 | 2024-09-29 00:46:23 | METOP-C | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 6b777842-8e87-31af-a612-1f3d5bb0980a | -14.1761 | -46.4417 | 2024-09-29 00:46:23 | METOP-C | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 532725b3-8a15-3e1b-afb5-8ff1bcb1db66 | -14.1777 | -46.448799 | 2024-09-29 00:46:23 | METOP-C | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 41aa8e9f-c04d-361b-ba76-ce06712d0be1 | -15.7825 | -54.164001 | 2024-09-29 00:46:23 | METOP-C | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| f6cb7031-8796-3dcc-b346-cec01585d1e2 | -15.7856 | -54.180302 | 2024-09-29 00:46:23 | METOP-C | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| b72a15b0-4d69-30d9-9334-3adbc0571245 | -14.1663 | -46.444 | 2024-09-29 00:46:24 | METOP-C | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 93fb954e-8f26-38f6-9b61-161896db62f6 | -14.1679 | -46.451099 | 2024-09-29 00:46:24 | METOP-C | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 2a89047a-4d6c-3b3d-872d-ce648917c45e | -15.7727 | -54.165901 | 2024-09-29 00:46:24 | METOP-C | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 0065cf90-2740-3324-b846-48cb9a9b6138 | -15.7758 | -54.182201 | 2024-09-29 00:46:24 | METOP-C | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 57b97182-a45c-3a31-ace6-61d6f367889b | -15.7789 | -54.198502 | 2024-09-29 00:46:24 | METOP-C | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| c4aeafbb-3f29-3b2d-9a3c-27072082d72d | -13.4376 | -44.017101 | 2024-09-29 00:46:26 | METOP-C | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 3664d9b2-0535-3ee7-b489-0877f7e4d6df | -13.4279 | -44.019501 | 2024-09-29 00:46:26 | METOP-C | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 112c5d47-11d7-3e93-8073-fb93c4d51e95 | -13.4298 | -44.027699 | 2024-09-29 00:46:26 | METOP-C | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 77ac8ba6-c933-3b15-8771-e622515f32b9 | -12.7373 | -43.466301 | 2024-09-29 00:46:35 | METOP-C | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 1d25aee1-9a33-319f-afd7-e5c80ce2a968 | -13.3618 | -46.306099 | 2024-09-29 00:46:36 | METOP-C | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 823c80bb-766f-3166-ac8e-734f17a00e16 | -13.3504 | -46.3013 | 2024-09-29 00:46:36 | METOP-C | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 53c36afd-3213-38fe-848a-db453422a371 | -13.352 | -46.308399 | 2024-09-29 00:46:36 | METOP-C | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 6de3561d-a048-37c9-b985-5796ba1c5e50 | -13.3536 | -46.315399 | 2024-09-29 00:46:36 | METOP-C | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 18e4e7d3-b9d2-3477-9b35-9cca2bbeff16 | -15.6189 | -57.4473 | 2024-09-29 00:46:36 | METOP-C | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README3.md)
