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

## Dados Diários - Página 44

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 180cea03-6793-321f-95e7-95e3a05bcc17 | -20.45567 | -45.26707 | 2025-10-25 04:21:00 | NOAA-20 | ITAPECERICA | MINAS GERAIS | Brasil | 3133501 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| c3150afa-bd49-304c-9b88-c69551463607 | -17.41794 | -46.87868 | 2025-10-25 04:21:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 49818230-6d22-3d83-a571-56404c6c2231 | -13.90194 | -48.42216 | 2025-10-25 04:21:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| da41a49c-b838-36d1-a2e9-700492e7fff5 | -16.58425 | -43.50173 | 2025-10-25 04:21:00 | NOAA-20 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 8.3 |
| a2410b4f-b6b3-30e1-bdcd-553eba885335 | -15.23046 | -47.92801 | 2025-10-25 04:21:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 8de3ad4a-f210-3d88-bd53-c0340992f16c | -16.58481 | -50.38028 | 2025-10-25 04:21:00 | NOAA-20 | FIRMINÓPOLIS | GOIÁS | Brasil | 5207808 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 626fcbdf-b918-3623-a31a-aeda0821e39e | -14.18263 | -47.30974 | 2025-10-25 04:21:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 68118692-6165-3ec5-a60e-82f9852cb637 | -18.16947 | -51.75159 | 2025-10-25 04:21:00 | NOAA-20 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 9.6 |
| ddbbc2f1-6078-3ae5-865d-1c90500daa2f | -14.45719 | -47.75557 | 2025-10-25 04:21:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d058fedd-1ee6-3f9a-b656-4346ddfd6f92 | -15.46017 | -42.98614 | 2025-10-25 04:21:00 | NOAA-20 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 0.8 |
| b8f10455-a94e-33c5-b55c-98b313b129b3 | -20.41518 | -50.1043 | 2025-10-25 04:21:00 | NOAA-20 | VALENTIM GENTIL | SÃO PAULO | Brasil | 3556107 | 35 | 33 | nan | nan | nan | Cerrado | 4.7 |
| e24e9273-f334-3bf0-a365-edf4b12b80a7 | -14.98434 | -43.5485 | 2025-10-25 04:21:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 89139435-353d-37a1-a05d-1240107f38fa | -14.20379 | -47.30581 | 2025-10-25 04:21:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c90c12b6-b737-323e-862d-9b454f17ca21 | -14.43834 | -48.06867 | 2025-10-25 04:21:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cfc563b5-db23-3170-9b90-2e5ab83aa383 | -15.52867 | -45.7107 | 2025-10-25 04:21:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f4a8a1b0-805e-33ee-b525-59e0057bd407 | -18.55763 | -50.27474 | 2025-10-25 04:21:00 | NOAA-20 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |
| bd0b2cce-5ff3-3251-9816-e802ec5edee4 | -18.5647 | -50.27608 | 2025-10-25 04:21:00 | NOAA-20 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Mata Atlântica | 28.9 |
| 0bbbf651-e1be-3f9c-a593-432ec117b1be | -18.55691 | -50.27887 | 2025-10-25 04:21:00 | NOAA-20 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |
| 8a441c91-569b-3db0-8320-3fad5d92fb1e | -14.38562 | -51.53175 | 2025-10-25 04:21:00 | NOAA-20 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c71199c0-fb6c-39cd-85d7-0856f27f94da | -16.58726 | -43.50671 | 2025-10-25 04:21:00 | NOAA-20 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 24.6 |
| aea98aee-823c-3c88-9948-86092df7e193 | -21.20501 | -46.71781 | 2025-10-25 04:21:00 | NOAA-20 | GUAXUPÉ | MINAS GERAIS | Brasil | 3128709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| f118f72d-fc07-32ff-a662-cc7ea1364853 | -14.88824 | -52.44231 | 2025-10-25 04:21:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 3211b58f-cd59-3644-9b5d-cbdaaa5c094a | -17.33726 | -45.70105 | 2025-10-25 04:21:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7ca5d6e4-fecb-3b05-8562-07512673aefa | -19.76442 | -48.29661 | 2025-10-25 04:21:00 | NOAA-20 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 8.1 |
| f43e5614-3919-3f82-98f8-a4904a67b77d | -20.96624 | -45.58087 | 2025-10-25 04:21:00 | NOAA-20 | BOA ESPERANÇA | MINAS GERAIS | Brasil | 3107109 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d9a22b26-a51c-38db-9ba3-ca9adba00251 | -14.93671 | -48.12958 | 2025-10-25 04:21:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 90418832-4b86-36c2-b0fb-eb266294e783 | -21.20165 | -46.71725 | 2025-10-25 04:21:00 | NOAA-20 | GUAXUPÉ | MINAS GERAIS | Brasil | 3128709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| f1cc4f3f-52c2-35c1-a4c1-d513ce2bf487 | -14.18321 | -47.30617 | 2025-10-25 04:21:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5071e56e-cd1b-35ce-b826-c465f61c7629 | -14.87012 | -48.09098 | 2025-10-25 04:21:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| ad9bca65-85fb-3efc-807d-421ab486005a | -14.87075 | -48.08721 | 2025-10-25 04:21:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 2963fb0b-3752-3edd-81d6-9e801a2d9226 | -14.93098 | -48.52507 | 2025-10-25 04:21:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| b41378dd-a9ab-3cd0-87a3-28a9b7218bed | -14.45381 | -47.93361 | 2025-10-25 04:21:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 07b27fd3-f6d1-3f67-a5ee-0a47642b3294 | -14.86887 | -48.09852 | 2025-10-25 04:21:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 92af5336-46f5-3ac4-aa32-5176667562e5 | -13.65287 | -48.18721 | 2025-10-25 04:21:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 53b639bf-1482-3571-83f0-c820b52f015a | -14.86463 | -48.08225 | 2025-10-25 04:21:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| a90a4cfd-f65b-3fff-8e5c-19ba28ee06ac | -20.75695 | -43.23029 | 2025-10-25 04:21:00 | NOAA-20 | PRESIDENTE BERNARDES | MINAS GERAIS | Brasil | 3153103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| f9e629bc-11d5-3411-81be-dc0dd56c3f24 | -15.2761 | -50.7623 | 2025-10-25 04:21:00 | NOAA-20 | MATRINCHÃ | GOIÁS | Brasil | 5212956 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| aaee0540-665c-3d8f-b826-249afbb59e0f | -15.52978 | -45.70343 | 2025-10-25 04:21:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6ef2f4cd-6d12-38c5-894e-adbd0996ada5 | -13.92056 | -50.26389 | 2025-10-25 04:21:00 | NOAA-20 | MUNDO NOVO | GOIÁS | Brasil | 5214051 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 08efab65-c510-345f-b887-e2d47ed15f76 | -20.39758 | -42.89249 | 2025-10-25 04:21:00 | NOAA-20 | PONTE NOVA | MINAS GERAIS | Brasil | 3152105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 30bf3541-fcb6-3411-87bb-df78da55f106 | -18.16475 | -51.75572 | 2025-10-25 04:21:00 | NOAA-20 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 410c1be4-ceec-38a8-9b76-9dc9e193faae | -19.17306 | -43.52562 | 2025-10-25 04:21:00 | NOAA-20 | SANTANA DO RIACHO | MINAS GERAIS | Brasil | 3159001 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 46a76d7c-dc95-304a-9517-136f2ba509fd | -13.88039 | -48.40286 | 2025-10-25 04:21:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 0d2445f4-7eb5-3d4e-95e3-8754416aa8cb | -14.92757 | -48.52444 | 2025-10-25 04:21:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 9942be83-6bbd-3d3c-b96d-aa2bfeb52886 | -14.38161 | -51.53099 | 2025-10-25 04:21:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8c3baee7-be12-3c5e-9e2e-caaefb3ff532 | -15.82367 | -53.59796 | 2025-10-25 04:21:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 37c64e7d-51ab-3f37-8ac2-df37713b9035 | -15.83075 | -49.08655 | 2025-10-25 04:21:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d10bb244-8931-31e5-a539-9e10afb392a0 | -17.3676 | -45.49826 | 2025-10-25 04:21:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d5d8e72c-1e92-333f-a416-11caf7ff1ec4 | -19.33278 | -49.08637 | 2025-10-25 04:21:00 | NOAA-20 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7ecba486-04c3-37ad-9f57-b317c8b584d9 | -14.864 | -48.08603 | 2025-10-25 04:21:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 8.6 |
| f862ca80-9d6c-324b-9eb7-565a4b3ef10f | -17.33389 | -45.70051 | 2025-10-25 04:21:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 51cb6b2f-fd58-3f46-99fc-c4e129af0efc | -19.76288 | -48.28497 | 2025-10-25 04:21:00 | NOAA-20 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 88bb2edc-460c-3ab6-989a-b314a683096f | -14.74454 | -46.60146 | 2025-10-25 04:21:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ca490209-6125-3f7a-8cc1-f4202949c7e1 | -15.58007 | -43.21997 | 2025-10-25 04:21:00 | NOAA-20 | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 4342333a-f0ed-3f51-8d41-ca0d4f6fd1e8 | -16.09633 | -45.18084 | 2025-10-25 04:21:00 | NOAA-20 | PINTÓPOLIS | MINAS GERAIS | Brasil | 3150570 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 666cd697-8536-32ea-9a23-e09e0c52fed6 | -19.17681 | -43.52617 | 2025-10-25 04:21:00 | NOAA-20 | SANTANA DO RIACHO | MINAS GERAIS | Brasil | 3159001 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0a941889-d77e-3139-8416-6e7522fe9c2d | -18.36102 | -51.70984 | 2025-10-25 04:21:00 | NOAA-20 | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d3e50214-8919-31ef-9474-19f4e61f0ff9 | -19.32604 | -49.08512 | 2025-10-25 04:21:00 | NOAA-20 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| fac4baff-ccb4-3959-98e4-af18eaca2a49 | -19.87331 | -46.98029 | 2025-10-25 04:21:00 | NOAA-20 | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 23d6a2be-e3a7-35b7-b839-2a534159107a | -15.31937 | -52.99976 | 2025-10-25 04:21:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1a5bbebd-f3b3-303f-95dc-727ff961aa16 | -19.62771 | -46.13163 | 2025-10-25 04:21:00 | NOAA-20 | CAMPOS ALTOS | MINAS GERAIS | Brasil | 3111507 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 0fe7d62d-7f64-3c91-83c9-75cfc7d1fb46 | -15.24021 | -47.91075 | 2025-10-25 04:21:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 39e59803-1a1a-3bd1-a13e-b144e3e110aa | -16.36444 | -49.93837 | 2025-10-25 04:21:00 | NOAA-20 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 23ba8a07-4cfc-37e0-9f76-2237fcd977be | -14.45781 | -47.93046 | 2025-10-25 04:21:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8733abce-eda0-3652-a973-035a332da90d | -16.26561 | -43.6183 | 2025-10-25 04:21:00 | NOAA-20 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f527a83b-19b2-3d5f-8dd1-8952ac12bb3e | -14.92349 | -48.14657 | 2025-10-25 04:21:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2a62cc43-ea32-35ca-9f55-3b054e3aeb6b | -14.56405 | -49.83858 | 2025-10-25 04:21:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 72ff7f89-09fa-3c44-8621-33881cbe3907 | -14.86612 | -48.09416 | 2025-10-25 04:21:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 56a984aa-0c94-3971-93a8-61b2d41ba69f | -18.78653 | -48.03846 | 2025-10-25 04:21:00 | NOAA-20 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 11b550fb-5f58-3bfb-955b-d74f632c871d | -14.18205 | -47.31333 | 2025-10-25 04:21:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e0098bd9-5993-374d-a6c1-267c5e2bb2c5 | -15.94351 | -56.11737 | 2025-10-25 04:21:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 932c8a35-916f-341e-a7ed-3d4faabd8888 | -14.5839 | -44.13422 | 2025-10-25 04:21:00 | NOAA-20 | MANGA | MINAS GERAIS | Brasil | 3139300 | 31 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 8f1635bd-bf06-3a3d-bac8-418bd3dc63bd | -19.17745 | -43.52145 | 2025-10-25 04:21:00 | NOAA-20 | SANTANA DO RIACHO | MINAS GERAIS | Brasil | 3159001 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 84893224-e16c-3aeb-bbe0-4227b658fc92 | -18.23931 | -44.16463 | 2025-10-25 04:21:00 | NOAA-20 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bbdbf880-bdda-333f-a5e0-c0f5b6abe8cf | -13.91006 | -48.4159 | 2025-10-25 04:21:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9efb42ac-73eb-33dd-91f6-5574aef3cd1d | -15.23657 | -47.93283 | 2025-10-25 04:21:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| b1530232-05c3-3721-ae68-cb526d48bb56 | -14.56391 | -49.84161 | 2025-10-25 04:21:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| d51387af-84f3-3d40-9353-f0448d47972d | -14.87288 | -48.0953 | 2025-10-25 04:21:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 4f3b3df9-fbce-33d1-9c91-f7c1c10810d2 | -15.24114 | -47.92604 | 2025-10-25 04:21:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 7463c931-67a3-36f0-9345-26f81060e8ff | -18.80017 | -44.80949 | 2025-10-25 04:21:00 | NOAA-20 | FELIXLÂNDIA | MINAS GERAIS | Brasil | 3125705 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 71c095fe-2271-34e6-a9b6-d0d77c8824c1 | -17.36816 | -45.49449 | 2025-10-25 04:21:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e0f52c35-aa84-35aa-9063-999fbfed9098 | -20.7009 | -44.25673 | 2025-10-25 04:21:00 | NOAA-20 | DESTERRO DE ENTRE RIOS | MINAS GERAIS | Brasil | 3121407 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 810c150a-e6c3-3e5a-80ee-dc6bbcb8d600 | -16.21454 | -46.47562 | 2025-10-25 04:21:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8e9e9894-5d1f-3106-abd5-50602894b2b5 | -18.80368 | -44.81001 | 2025-10-25 04:21:00 | NOAA-20 | FELIXLÂNDIA | MINAS GERAIS | Brasil | 3125705 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ea203d3f-9355-3db3-9e65-87d0b4ee5b24 | -15.00004 | -49.98987 | 2025-10-25 04:21:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 9eccc7c0-a6dc-3622-924f-6571b510052f | -14.86675 | -48.09039 | 2025-10-25 04:21:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 7b2c199b-7aad-3a1d-8826-31ba87d38951 | -14.51237 | -49.13418 | 2025-10-25 04:21:00 | NOAA-20 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9c894653-9f45-34a4-8ad4-8bbcf0b3dba2 | -14.47352 | -47.89841 | 2025-10-25 04:21:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| cbdd5b27-2c1b-3ab5-8ae1-0f1b97a1eca2 | -18.25001 | -44.19254 | 2025-10-25 04:21:00 | NOAA-20 | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2af85252-02dc-334d-abae-1fe687236a93 | -19.92492 | -47.3921 | 2025-10-25 04:21:00 | NOAA-20 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0fbb2af5-eb86-376f-a83d-97bfcb1e4d73 | -14.54044 | -48.04034 | 2025-10-25 04:21:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2faff920-daa4-3840-809f-327a3f764ba9 | -15.66 | -46.15621 | 2025-10-25 04:21:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 0fd70060-02dc-3a7c-9dec-a9f2d7b54e7e | -20.1085 | -45.85571 | 2025-10-25 04:21:00 | NOAA-20 | BAMBUÍ | MINAS GERAIS | Brasil | 3105103 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| e8b32890-6830-344e-8e22-0e3aa51d14b1 | -14.94846 | -47.6996 | 2025-10-25 04:21:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7981579c-44af-3eeb-b912-795a04badc94 | -20.28167 | -50.22479 | 2025-10-25 04:21:00 | NOAA-20 | FERNANDÓPOLIS | SÃO PAULO | Brasil | 3515509 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| f63a6096-bfe7-3e7a-9330-1cec34921d97 | -16.21785 | -46.47618 | 2025-10-25 04:21:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 8.7 |
| b5d598d6-a116-332b-a5c8-2316942a6fc1 | -14.44109 | -48.07308 | 2025-10-25 04:21:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6020796d-a121-3e6f-a205-dd587454f610 | -14.53644 | -48.04358 | 2025-10-25 04:21:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5c5ebb64-76db-32ae-a365-fce8e80fed47 | -20.54127 | -45.76689 | 2025-10-25 04:21:00 | NOAA-20 | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 71d88653-b882-358f-bd7c-8b93e88a6952 | -15.23108 | -47.9243 | 2025-10-25 04:21:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |


[Clique aqui para ver as próximas entradas](README45.md)
