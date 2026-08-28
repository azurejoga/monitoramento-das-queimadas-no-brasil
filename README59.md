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

## Dados Diários - Página 59

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bb0f97a3-1c57-3766-a1af-0c3c91f6c09f | -10.94523 | -50.5429 | 2026-08-28 05:12:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 547a72f0-4f8d-3b68-b369-a9ee109c8ec6 | -11.63987 | -46.73285 | 2026-08-28 05:12:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e385ec41-408f-3ae2-b076-00eba5dec552 | -10.78429 | -61.41801 | 2026-08-28 05:12:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fb8850cf-1362-3150-a716-b558f43b292e | -11.7196 | -54.53168 | 2026-08-28 05:12:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 2bee296e-7a46-351c-9b11-9da0944af370 | -11.19226 | -55.09048 | 2026-08-28 05:12:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 953409d7-d14d-3956-a72b-ce650281ba60 | -10.7968 | -50.64373 | 2026-08-28 05:12:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2fce1cbb-befc-3507-9b9a-92aba5424cb7 | -11.7502 | -54.51989 | 2026-08-28 05:12:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4c12ca1b-bc81-32c3-a6fe-ce77cf4207a0 | -10.79181 | -53.99882 | 2026-08-28 05:12:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 15058599-c28b-3b9f-9462-d405e96cea4f | -12.79264 | -46.45382 | 2026-08-28 05:12:00 | NOAA-20 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 1aae1425-b481-31bc-aa70-57ffb00d0a33 | -13.60119 | -45.78484 | 2026-08-28 05:12:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b078e471-458e-3ab8-8a43-cf38fe8c7f1e | -10.79943 | -54.01127 | 2026-08-28 05:12:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 38fd2cd2-4d56-3552-8912-565392156716 | -14.51265 | -59.81923 | 2026-08-28 05:12:00 | NOAA-20 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a6878809-d472-3343-86d5-aedf5508d50e | -11.73078 | -54.52925 | 2026-08-28 05:12:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 16c1ee50-71c5-3e01-9ec1-a3596cdb0352 | -11.7149 | -54.53916 | 2026-08-28 05:12:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 11.2 |
| c643ac28-54ed-3500-bcaf-bc58b7635613 | -13.45901 | -54.0149 | 2026-08-28 05:12:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| afe6bb4f-3948-352d-a97f-e25749788d60 | -11.73018 | -54.53328 | 2026-08-28 05:12:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e5ad42b3-ac9d-3d6c-b475-7914acec3e81 | -14.93074 | -52.60627 | 2026-08-28 05:12:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 84954db1-ef56-3ddc-ac94-01e5dea49304 | -13.47115 | -57.0459 | 2026-08-28 05:12:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9129083f-5e90-3147-b3f4-24830532f08e | -13.60495 | -45.77858 | 2026-08-28 05:12:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ad908cc7-04ef-320a-b257-811a9dcbaaab | -10.79586 | -54.01072 | 2026-08-28 05:12:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| db5d1ca0-2493-3662-a0d7-05fafe51fdfe | -9.52146 | -67.16265 | 2026-08-28 05:12:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7bcaf4e4-285d-3b28-b40c-7ef6f9011a07 | -11.28627 | -54.01995 | 2026-08-28 05:12:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| e8878c93-a73e-3f8a-aab2-f98346985dd3 | -14.42187 | -53.37823 | 2026-08-28 05:12:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 1bd115f0-3441-36d3-a84c-c587f3bb63bd | -13.43637 | -53.98894 | 2026-08-28 05:12:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7073c72b-d89f-3404-a602-7e8cd65e8cb9 | -10.39093 | -61.2443 | 2026-08-28 05:12:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 4eeaf47a-48cd-352f-91db-423ed57481f2 | -10.75975 | -53.96849 | 2026-08-28 05:12:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c22dbbb5-bb6a-3372-8cf5-b1c8ec39a5ad | -11.51419 | -58.51048 | 2026-08-28 05:12:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| d8038b17-28e2-3082-8b4a-f22c952d0542 | -11.28268 | -54.01939 | 2026-08-28 05:12:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 0ac5fe1f-4e75-3541-b966-57ea3d3fbe16 | -11.01866 | -49.66086 | 2026-08-28 05:12:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b88cc3b3-7bc7-33a6-92b6-4843d6175915 | -11.19799 | -55.09911 | 2026-08-28 05:12:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b9922c2c-99da-3858-8e2b-c6d1610f905f | -12.28616 | -50.59229 | 2026-08-28 05:12:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 1cc9a14c-1361-3efc-9102-49b58350126f | -11.83253 | -47.21581 | 2026-08-28 05:12:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 198cff8a-1cba-3487-afb9-47f4a6590686 | -11.82455 | -47.21831 | 2026-08-28 05:12:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6981cdc4-d239-3d00-85ca-5a96fd114f89 | -13.59809 | -45.78279 | 2026-08-28 05:12:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d0bed5fe-8e5d-392e-bc3e-6e18529e13e7 | -11.19569 | -55.09101 | 2026-08-28 05:12:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 99e14847-4b6e-3de3-9045-4033b775578b | -11.1959 | -51.24248 | 2026-08-28 05:12:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4eb3a3e4-35e7-39c7-91f8-1d21697475ab | -9.84445 | -65.02136 | 2026-08-28 05:12:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5f308b00-7f88-3e37-a4ea-51de2902eaef | -8.98693 | -65.43468 | 2026-08-28 05:12:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 358c0896-faed-3836-8caf-faacc0270bde | -8.99173 | -65.44347 | 2026-08-28 05:12:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 64746d6b-b1c8-3542-bf51-2289486c1754 | -10.76606 | -50.63938 | 2026-08-28 05:12:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 16080db9-cdff-3ce2-8fef-e478331a20bd | -11.28443 | -54.03241 | 2026-08-28 05:12:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| a230e2c0-4be1-37cc-8ae3-a319443ec89e | -10.94079 | -50.54228 | 2026-08-28 05:12:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 12.4 |
| f059409c-6bc9-3f08-ad98-da3a07c996e1 | -8.99291 | -65.43714 | 2026-08-28 05:12:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0bd770ff-6e59-3a54-a859-2619a9661929 | -14.87506 | -52.59205 | 2026-08-28 05:12:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 2499ddaf-1ed0-36c3-b288-83b25e0d1407 | -10.79706 | -54.00248 | 2026-08-28 05:12:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7b9584e6-8bc3-3c28-9b8e-884cc0de3c6d | -14.87456 | -52.59568 | 2026-08-28 05:12:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 5a8160fc-0919-3912-b599-28854370f993 | -12.1601 | -60.75484 | 2026-08-28 05:12:00 | NOAA-20 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5df5fbb4-025b-35e8-897d-69024726ce6f | -10.96076 | -50.29855 | 2026-08-28 05:12:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b75dfd62-e1e0-3e90-ac95-b214cb41e878 | -15.81859 | -56.42585 | 2026-08-28 05:12:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d49fb0a3-32f1-3c50-bc38-cd5c66041f3b | -11.20786 | -53.9924 | 2026-08-28 05:12:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 949ea244-ab73-3cef-acc9-e985beb3602b | -9.86112 | -60.26532 | 2026-08-28 05:12:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 7148738f-b5f8-39f6-a465-4a0355657b6e | -12.25191 | -50.57354 | 2026-08-28 05:12:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| bda7a92d-07e7-3973-8388-689e4bb61f65 | -10.92871 | -50.53161 | 2026-08-28 05:12:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 5c3bc625-79e1-3bb4-bb56-959f23292c9c | -13.59242 | -45.77663 | 2026-08-28 05:12:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 98558647-92d4-397b-813b-6c3d19859c48 | -11.76684 | -44.91421 | 2026-08-28 05:12:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8ef2560e-86ba-3734-a4a2-c36046c3d851 | -13.46451 | -57.04482 | 2026-08-28 05:12:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8ee8a465-25be-374e-ae2d-06465f9962d2 | -14.92805 | -52.59519 | 2026-08-28 05:12:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 008b5d45-c960-3f44-bc17-395881774bb3 | -14.42255 | -53.37332 | 2026-08-28 05:12:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7effc366-8911-30b6-ad47-fdab6a30e012 | -10.77008 | -54.04603 | 2026-08-28 05:12:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f0732225-7b82-3864-9fc5-2cc18d8fc263 | -11.2306 | -53.99866 | 2026-08-28 05:12:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ea292b73-23a3-343d-92c6-c4edca76f3c5 | -12.28945 | -50.60208 | 2026-08-28 05:12:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 8cff89f8-63cc-3f41-9802-0bf40736142f | -12.91265 | -59.88403 | 2026-08-28 05:12:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c4bf7773-1e7c-3710-8cda-97be0921ac94 | -11.70775 | -47.80255 | 2026-08-28 05:12:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 1b8856db-4ed0-32a5-94e3-6ce006227bfc | -14.98637 | -52.59573 | 2026-08-28 05:12:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 985f6f95-885d-35a0-b8c8-4a16c2e5668f | -14.45028 | -53.35368 | 2026-08-28 05:12:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7083795e-e037-3550-bbd3-aa06237621ec | -11.22818 | -54.00403 | 2026-08-28 05:12:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 85cf3448-6922-399d-b08e-b434f576feed | -10.76122 | -54.03206 | 2026-08-28 05:12:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ea989aae-b554-33b9-8244-ea509b74f439 | -10.7579 | -53.98093 | 2026-08-28 05:12:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f516f1e5-c179-3444-9210-72dfa7d87bcb | -11.79764 | -47.67212 | 2026-08-28 05:12:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1acbc815-78bb-3b1f-9f04-bd289f32aad7 | -8.98984 | -65.44833 | 2026-08-28 05:12:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 91b5dc88-4e16-32d9-b596-d75ce6d81936 | -11.19855 | -51.22775 | 2026-08-28 05:12:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 22.3 |
| 64ffc829-562a-3d34-afca-1a1d4cf8b31f | -10.79348 | -54.00193 | 2026-08-28 05:12:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e0fd1521-1c24-3488-aa09-a281315baa08 | -11.77258 | -54.515 | 2026-08-28 05:12:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1561a876-f176-328a-a664-78a818964db7 | -12.26874 | -50.58522 | 2026-08-28 05:12:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a2fff942-b7f4-3b02-abc1-62035db6ebc4 | -14.88571 | -52.60033 | 2026-08-28 05:12:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 6d3cc3ae-a695-355b-a2ee-0eb7aafaae29 | -11.81422 | -47.20919 | 2026-08-28 05:12:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 3c49edf5-d354-36b7-9872-450306e3f1b3 | -11.77123 | -47.66148 | 2026-08-28 05:12:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2f12280c-d1f0-3e1a-aa03-2bcf05bfe8b5 | -8.87456 | -66.91075 | 2026-08-28 05:12:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1540c620-cd65-3baf-9fe3-afc8896db75a | -10.78422 | -50.63755 | 2026-08-28 05:12:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c5ae1708-e60c-3515-936c-6f1f0bac225d | -11.19381 | -51.22586 | 2026-08-28 05:12:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 6.8 |
| a5db91c1-00cf-3f83-9745-d0449ecf405c | -8.99098 | -65.44198 | 2026-08-28 05:12:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 41c20ebc-b115-3b5e-a7f4-190e520f2d33 | -9.85435 | -65.02338 | 2026-08-28 05:12:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d214129e-7e86-3caa-b847-a6cb40315603 | -10.9659 | -50.29459 | 2026-08-28 05:12:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d2b57740-25d1-3c7b-aec5-36a3d3c9cc42 | -9.88749 | -60.2654 | 2026-08-28 05:12:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5bb22506-4037-35f8-a1a0-0721f2e65d12 | -8.9875 | -65.43153 | 2026-08-28 05:12:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 354c7a54-d523-38c5-a411-ecdbd66a4536 | -11.83207 | -47.21943 | 2026-08-28 05:12:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 59d9ef9f-63e9-3ba6-a228-2e668e55f42f | -14.89435 | -52.59797 | 2026-08-28 05:12:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 4c9287fa-3887-38b2-82aa-757c8408891a | -14.88163 | -52.59969 | 2026-08-28 05:12:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 9aea0d6e-4624-3206-b65e-af3c867a6d48 | -10.57594 | -57.48521 | 2026-08-28 05:12:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ba48eaa2-2b60-3376-9b5e-68a94dedc24a | -15.60243 | -46.57773 | 2026-08-28 05:12:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 70b06dbe-a737-355b-a142-308bcb0f1292 | -15.62664 | -55.97709 | 2026-08-28 05:12:00 | NOAA-20 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| b5e7bff3-2b29-363b-8327-556504c8eaa3 | -10.79414 | -54.00763 | 2026-08-28 05:12:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d08ac36b-9214-3aa5-8204-311990a1653b | -10.89827 | -50.52285 | 2026-08-28 05:12:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a234308c-d90f-3edb-b6c9-3c3f9b2dffcb | -14.51544 | -59.82365 | 2026-08-28 05:12:00 | NOAA-20 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4ee652a7-6d0a-3677-8524-51952e58caec | -14.18837 | -52.84909 | 2026-08-28 05:12:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f78b00d6-d9ad-3263-b2d9-ffad8053af87 | -10.26515 | -64.50851 | 2026-08-28 05:12:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 269c6926-7270-3329-b68a-3da88392fe9f | -11.23238 | -54.01169 | 2026-08-28 05:12:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| f8e9158a-63ec-3280-8a5c-cb8a4299bede | -14.97049 | -52.58982 | 2026-08-28 05:12:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 19242b35-d2be-3fce-880c-e4f4fc308f26 | -10.76356 | -54.04086 | 2026-08-28 05:12:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5c4f071f-f2b2-3158-8ec4-29d9316a4998 | -11.76874 | -47.63615 | 2026-08-28 05:12:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |


[Clique aqui para ver as próximas entradas](README60.md)
