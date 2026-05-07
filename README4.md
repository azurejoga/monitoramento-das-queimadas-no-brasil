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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0b868351-fe05-3880-94a6-db163d7bcbe1 | -9.34734 | -47.08863 | 2026-05-07 04:34:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c15c064f-c510-3948-901f-04e3ea920f0e | -8.74987 | -48.92936 | 2026-05-07 04:34:00 | NOAA-21 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 56f349fb-0740-373e-b552-e5d15966887e | -10.55471 | -42.43537 | 2026-05-07 04:34:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 5e988c19-e9b5-3e97-b76d-2844510b0e82 | -9.67371 | -48.52682 | 2026-05-07 04:34:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9794a3c7-42a8-3f2b-bb64-ca2dc544c29a | -11.61489 | -54.17775 | 2026-05-07 04:34:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 9612afd8-cd6a-3d9d-9b67-ef2697a79fcc | -6.78553 | -46.82221 | 2026-05-07 04:34:00 | NOAA-21 | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| d4ffe325-7fe3-39c0-8f7d-aa24f14c5be1 | -9.46601 | -47.80416 | 2026-05-07 04:34:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e446484b-5ba5-3cf3-ac5c-f5836c5dcbc7 | -10.63747 | -48.01056 | 2026-05-07 04:34:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 8709330b-0d58-30f6-b263-1c38e6d4ab87 | -8.84701 | -36.55514 | 2026-05-07 04:34:00 | NOAA-21 | GARANHUNS | PERNAMBUCO | Brasil | 2606002 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| afd52aca-67f6-3360-9801-921f31740d0e | -13.13493 | -42.96871 | 2026-05-07 04:34:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 793d6840-df8f-3c1d-ae4c-59de2cc3a067 | -7.27916 | -46.79696 | 2026-05-07 04:34:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 11cc4c2b-821b-3e5a-8586-f920d5ff1ed5 | -11.61553 | -54.17408 | 2026-05-07 04:34:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 76b69e45-c0bb-3f84-9624-561078c15f4a | -9.4059 | -50.68612 | 2026-05-07 04:34:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4ca322cd-fc93-3950-89a5-1c8cacdfd92b | -5.78102 | -45.12566 | 2026-05-07 04:34:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6331552b-ccda-3195-8f2d-31e885f86959 | -13.95988 | -47.5455 | 2026-05-07 04:36:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e342e022-544c-3241-afad-46c0b53f6f10 | -11.83999 | -57.84833 | 2026-05-07 04:36:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 04008f0c-4ded-3f29-b6a2-7f64c4d9b5a3 | -13.89148 | -47.53317 | 2026-05-07 04:36:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c4527c3f-ccec-342f-96d7-1b95d31e99f7 | -12.4997 | -58.4821 | 2026-05-07 04:36:00 | NOAA-21 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6e6d61c5-e64c-3db3-8c23-297cd5e10882 | -14.90292 | -45.18349 | 2026-05-07 04:36:00 | NOAA-21 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 884810dc-8aab-3fce-b903-a031455daeaa | -11.72641 | -54.80722 | 2026-05-07 04:36:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 5212d3ba-534d-3178-941d-7fb38a81665a | -11.73974 | -54.80547 | 2026-05-07 04:36:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4516ac12-486d-3d3a-a0f4-260d2142a3c6 | -18.16898 | -51.10571 | 2026-05-07 04:36:00 | NOAA-21 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0c5dd7ad-865a-3549-af8e-f2d14e953877 | -13.99185 | -47.58912 | 2026-05-07 04:36:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 4996df55-eaa9-337d-969f-05bc319e889a | -16.46687 | -49.12768 | 2026-05-07 04:36:00 | NOAA-21 | NERÓPOLIS | GOIÁS | Brasil | 5214507 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 721aa3ac-4d79-3a27-82ea-925202084387 | -14.86247 | -48.55582 | 2026-05-07 04:36:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b72ee63a-7a30-3b55-b1ab-f59b0654b959 | -13.86817 | -48.18692 | 2026-05-07 04:36:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7d98c984-f3e0-3a7c-8e7d-98a0442da532 | -18.67072 | -48.21424 | 2026-05-07 04:36:00 | NOAA-21 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 5191b947-50f2-38ed-8e36-8268b7a401a4 | -14.86581 | -48.55637 | 2026-05-07 04:36:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2069986b-cf78-3c54-891b-b87a958bd1d1 | -14.13974 | -45.34111 | 2026-05-07 04:36:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 436574ea-ca86-3303-bd02-445d4bf557e0 | -16.10781 | -49.23325 | 2026-05-07 04:36:00 | NOAA-21 | PETROLINA DE GOIÁS | GOIÁS | Brasil | 5216809 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3b7a0a2d-88a3-374b-95e7-46da09a80fbd | -12.50035 | -58.47881 | 2026-05-07 04:36:00 | NOAA-21 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e3f2d98a-4ae2-3706-8c5f-d01a49df0f50 | -13.95592 | -47.5487 | 2026-05-07 04:36:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 834e35f1-1033-34dd-9d21-d5817d0f7d8d | -12.50163 | -58.47899 | 2026-05-07 04:36:00 | NOAA-21 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b5883b92-3c90-33ac-8942-479f91229c83 | -12.49572 | -58.4812 | 2026-05-07 04:36:00 | NOAA-21 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 53c1cda2-53e3-33e0-8838-fa28e4bddc75 | -14.07142 | -47.78409 | 2026-05-07 04:36:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 124a5f32-3301-3f35-b7e0-79bd8263b455 | -12.49759 | -58.47136 | 2026-05-07 04:36:00 | NOAA-21 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 2f50000e-4ccd-3c2f-bba2-abbdaad9c4b5 | -16.16467 | -58.49657 | 2026-05-07 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 51f9eb6e-118d-342d-a441-8f843288267b | -12.7773 | -59.00956 | 2026-05-07 04:36:00 | NOAA-21 | CAMPOS DE JÚLIO | MATO GROSSO | Brasil | 5102686 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1e776a6d-47fe-3740-b848-e9d7e145c36b | -12.55931 | -49.38388 | 2026-05-07 04:36:00 | NOAA-21 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 25cbed78-c68c-35ee-8f6d-a1d4a14c85c1 | -12.501 | -58.48228 | 2026-05-07 04:36:00 | NOAA-21 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cea3d420-8b45-3fec-b5c3-f3c6beb5c9ff | -13.29914 | -49.99931 | 2026-05-07 04:36:00 | NOAA-21 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8c5c1268-db36-3d57-84a9-fa1173e215e4 | -14.86192 | -48.55944 | 2026-05-07 04:36:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b1904b99-1a51-34a3-9b87-c793ce9335f2 | -12.50099 | -58.47555 | 2026-05-07 04:36:00 | NOAA-21 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 68f7afc8-7109-31dc-a7ff-a2bd1fba2fb0 | -14.13594 | -45.34055 | 2026-05-07 04:36:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b75be358-e315-3127-8a0a-921732462036 | -11.73694 | -54.79671 | 2026-05-07 04:36:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 941d33c3-8791-3434-915d-dd7a24a1a3c5 | -16.16581 | -58.49075 | 2026-05-07 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 8872e598-57d6-3b85-aacd-5e115f4e73a7 | -14.13895 | -45.34293 | 2026-05-07 04:36:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 66fc88ad-0198-3e17-9392-c580bcaf392c | -13.63164 | -47.82008 | 2026-05-07 04:36:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dcf6e4c2-05ae-3cc6-bb57-31e58a586f54 | -16.06488 | -49.73416 | 2026-05-07 04:36:00 | NOAA-21 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f8aace7a-cf19-306f-8567-2082d0afad48 | -14.86526 | -48.55999 | 2026-05-07 04:36:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6b2b9a88-dcb3-3102-a9c8-fa07e9f1db5b | -16.17076 | -58.49177 | 2026-05-07 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| cf7b0f97-a290-36e1-9a2b-0e12ebe76795 | -11.73203 | -54.79995 | 2026-05-07 04:36:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1b76ad46-991b-350b-af15-0d279954c0c8 | -12.77802 | -59.00592 | 2026-05-07 04:36:00 | NOAA-21 | CAMPOS DE JÚLIO | MATO GROSSO | Brasil | 5102686 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f492b6e5-6562-3cc7-ad13-5f940c806200 | -19.13379 | -44.62241 | 2026-05-07 04:36:00 | NOAA-21 | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 48991ed1-b065-3f6e-aab2-b92d22c3bd2d | -11.74464 | -54.8023 | 2026-05-07 04:36:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0d111c33-74e6-3ef4-b111-e75f9660f05e | -16.60513 | -58.24058 | 2026-05-07 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 9e882709-4fa6-393f-a1b4-fb683e06c6ad | -14.03898 | -47.60298 | 2026-05-07 04:36:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 84b6e832-efe7-3587-b930-3d6909e29ad9 | -14.04526 | -47.60768 | 2026-05-07 04:36:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ceebf001-3967-32ea-bf74-befa7bd05ba6 | -11.80195 | -56.96412 | 2026-05-07 04:36:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cba42ada-16a4-3872-a7e2-09c08f2b92b8 | -13.69195 | -52.58774 | 2026-05-07 04:36:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 18beb8f8-d2a6-3277-81ba-49f6ad8156a8 | -19.13428 | -44.6183 | 2026-05-07 04:36:00 | NOAA-21 | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 25e96d66-c7e9-3d71-acc9-74020dcd5ead | -12.50225 | -58.47572 | 2026-05-07 04:36:00 | NOAA-21 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 35eaf917-c873-3c2c-a579-ec10cd39c5b8 | -16.47322 | -55.07069 | 2026-05-07 04:36:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 928444ce-7d91-358e-9872-bf9c5ebb14f8 | -13.69554 | -52.58836 | 2026-05-07 04:36:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cb3b1c18-cf06-3ab4-8e41-f38cfac1ef68 | -16.4702 | -49.12823 | 2026-05-07 04:36:00 | NOAA-21 | NERÓPOLIS | GOIÁS | Brasil | 5214507 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 3319dd29-e312-35f6-b910-3e559fcfedeb | -12.49634 | -58.47789 | 2026-05-07 04:36:00 | NOAA-21 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 84414fe2-647c-3920-98e7-9850256f88f2 | -12.49103 | -58.47698 | 2026-05-07 04:36:00 | NOAA-21 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 31153f8f-30d3-3e9b-bb36-7da4d6e7d7f5 | -14.03797 | -47.60743 | 2026-05-07 04:36:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f205638f-d130-370d-afe3-6b01ae05a9c1 | -11.79709 | -56.96324 | 2026-05-07 04:36:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c4979393-6fb0-362e-b828-0fa45f035c9f | -14.12635 | -45.35364 | 2026-05-07 04:36:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2d3a7017-3ac5-3476-b8df-eed1b51c4f35 | -17.42895 | -47.85136 | 2026-05-07 04:36:00 | NOAA-21 | CAMPO ALEGRE DE GOIÁS | GOIÁS | Brasil | 5204805 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| eec5f657-825a-3850-ba77-7278ccd2a0bf | -11.73904 | -54.80945 | 2026-05-07 04:36:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 858ade2e-af91-3f63-af5c-b509c2c5eb8b | -13.86198 | -48.18246 | 2026-05-07 04:36:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 84694122-1f93-3350-8271-3a19ab057fc2 | -13.88914 | -47.52532 | 2026-05-07 04:36:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 8d917f6a-d13a-3763-84a3-f3d6564d5e22 | -12.49905 | -58.48541 | 2026-05-07 04:36:00 | NOAA-21 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7167e4c5-759c-370f-9a7f-f44f49ddf0b5 | -16.6003 | -58.23958 | 2026-05-07 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 3dcf442b-0aed-3a9a-af92-c4c1f9835700 | -14.1346 | -45.35006 | 2026-05-07 04:36:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b58a40bb-e2a5-3d4a-9834-37837ec66c69 | -14.86137 | -48.56306 | 2026-05-07 04:36:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ba5a046d-101c-30e0-9806-615a39c33710 | -14.26076 | -45.24055 | 2026-05-07 04:36:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 23c072a1-3d40-3310-8b3c-1ed6f6c6f966 | -13.87249 | -46.97265 | 2026-05-07 04:36:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a3bea2df-f06b-3d66-a816-ab3554fdb33b | -13.54211 | -49.90412 | 2026-05-07 04:36:00 | NOAA-21 | BONÓPOLIS | GOIÁS | Brasil | 5203575 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| bec761fd-65a0-30bc-8697-8677cd780003 | -14.86471 | -48.56361 | 2026-05-07 04:36:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5cfcc51e-5787-3252-a427-3f020eadb69a | -14.40809 | -44.58543 | 2026-05-07 04:36:00 | NOAA-21 | MONTALVÂNIA | MINAS GERAIS | Brasil | 3142700 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 68c83028-d95a-3978-9ad2-141badfe1f2d | -12.49697 | -58.47461 | 2026-05-07 04:36:00 | NOAA-21 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 5cec8364-7ded-3120-b7e4-900b354a8e51 | -12.49508 | -58.48455 | 2026-05-07 04:36:00 | NOAA-21 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7beb775e-d30d-3943-8d12-5fd801e918ef | -12.50163 | -58.47229 | 2026-05-07 04:36:00 | NOAA-21 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 288b5212-79d4-3f68-b9db-3652324780b5 | -14.12256 | -45.35304 | 2026-05-07 04:36:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 544968a2-6498-3494-a3b3-6e84a5602957 | -14.03853 | -47.60369 | 2026-05-07 04:36:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d534695d-7a36-307c-90fd-2e94b850b017 | -14.15039 | -52.89263 | 2026-05-07 04:36:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 14abe602-a6ee-3df4-9c83-b5d6383b0ae3 | -11.84059 | -57.84517 | 2026-05-07 04:36:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d19eaeb5-fb3d-3e49-8168-4723d1f485e9 | -13.95962 | -47.33373 | 2026-05-07 04:36:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d8680374-baca-35dc-9aa6-5be6f9eb09b2 | -14.13147 | -45.34475 | 2026-05-07 04:36:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 09527eb8-09ad-3192-ad7c-f9b4554d5374 | -13.63219 | -47.8164 | 2026-05-07 04:36:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f2701bb8-d2ad-306a-b066-5cd072f30427 | -14.85913 | -48.55528 | 2026-05-07 04:36:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0d96c3d7-ceca-30d9-8c8b-6a86e90f3123 | -14.13081 | -45.34949 | 2026-05-07 04:36:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a09669da-9e37-36dc-8ade-b44dd68f2d85 | -18.48713 | -51.6893 | 2026-05-07 04:36:00 | NOAA-21 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 30f12890-c168-31a7-b451-ae75fa4f2eac | -14.03843 | -47.6067 | 2026-05-07 04:36:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| adedb313-4fb8-3bc5-94a0-07c3cf507d9b | -12.50038 | -58.48559 | 2026-05-07 04:36:00 | NOAA-21 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 22b44149-83bf-3fab-a08c-ed59fd47d18e | -14.14966 | -52.89696 | 2026-05-07 04:36:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 941489f1-39b3-39f3-ade6-78c672f15c9e | -16.16085 | -58.48974 | 2026-05-07 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |


[Clique aqui para ver as próximas entradas](README5.md)
