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

## Dados Diários - Página 74

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4088658d-7179-3673-a1d4-52a49e74b4b7 | -21.57901 | -46.62943 | 2024-10-07 04:04:00 | NOAA-20 | CACONDE | SÃO PAULO | Brasil | 3508702 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 654f0e9e-318e-31c9-b4ec-c7e314b79361 | -21.57822 | -46.6339 | 2024-10-07 04:04:00 | NOAA-20 | CACONDE | SÃO PAULO | Brasil | 3508702 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| c8f2b439-fd3b-3fb8-9bd8-cd6a451964ac | -21.57542 | -46.62885 | 2024-10-07 04:04:00 | NOAA-20 | CACONDE | SÃO PAULO | Brasil | 3508702 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 4d10d633-a36f-36d3-b922-17432c43430b | -21.57463 | -46.6333 | 2024-10-07 04:04:00 | NOAA-20 | CACONDE | SÃO PAULO | Brasil | 3508702 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| c2ad9630-404e-33ae-b0f1-1602fe15303e | -21.40329 | -45.34789 | 2024-10-07 04:04:00 | NOAA-20 | TRÊS PONTAS | MINAS GERAIS | Brasil | 3169406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 09114ff0-e060-33b1-a15d-1aad5a6cdf7e | -21.39988 | -45.34725 | 2024-10-07 04:04:00 | NOAA-20 | TRÊS PONTAS | MINAS GERAIS | Brasil | 3169406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| b17e3a3d-8f12-34b5-8841-812c5e2b5c94 | -21.39922 | -45.3512 | 2024-10-07 04:04:00 | NOAA-20 | TRÊS PONTAS | MINAS GERAIS | Brasil | 3169406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| c9cf742a-e485-34dc-a647-44464c9560c5 | -21.38896 | -45.61541 | 2024-10-07 04:04:00 | NOAA-20 | TRÊS PONTAS | MINAS GERAIS | Brasil | 3169406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 8fbcd0d1-66e0-3e0d-86a8-a7c12b0602a7 | -21.14537 | -45.82543 | 2024-10-07 04:04:00 | NOAA-20 | CAMPO DO MEIO | MINAS GERAIS | Brasil | 3111309 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.5 |
| 819180b6-0086-3f90-bea3-c1a1493620da | -21.14466 | -45.82952 | 2024-10-07 04:04:00 | NOAA-20 | CAMPO DO MEIO | MINAS GERAIS | Brasil | 3111309 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.5 |
| bec04391-d6ff-3b6e-834f-b9b744b704ac | -21.14118 | -45.8289 | 2024-10-07 04:04:00 | NOAA-20 | CAMPO DO MEIO | MINAS GERAIS | Brasil | 3111309 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 9821e19a-85cc-3285-bf69-5a42d98a01f2 | -21.1377 | -45.82827 | 2024-10-07 04:04:00 | NOAA-20 | CAMPO DO MEIO | MINAS GERAIS | Brasil | 3111309 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 118e54fb-a813-3927-afbe-475cd0e2fd87 | -21.12552 | -46.62194 | 2024-10-07 04:04:00 | NOAA-20 | SÃO PEDRO DA UNIÃO | MINAS GERAIS | Brasil | 3163904 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 3c7f9021-6526-39e3-8a94-09b404e019d0 | -20.99714 | -46.09256 | 2024-10-07 04:04:00 | NOAA-20 | CARMO DO RIO CLARO | MINAS GERAIS | Brasil | 3114402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| a26f31f6-d172-3acc-ab77-06b387ad4889 | -20.99642 | -46.09663 | 2024-10-07 04:04:00 | NOAA-20 | CARMO DO RIO CLARO | MINAS GERAIS | Brasil | 3114402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| c13a3215-1d34-3ebc-8da1-cc482031fb63 | -20.99363 | -46.09182 | 2024-10-07 04:04:00 | NOAA-20 | CARMO DO RIO CLARO | MINAS GERAIS | Brasil | 3114402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| 86e824a3-962e-38b3-88d2-0793a616c2cb | -20.99291 | -46.09597 | 2024-10-07 04:04:00 | NOAA-20 | CARMO DO RIO CLARO | MINAS GERAIS | Brasil | 3114402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.5 |
| a1a8cbed-3209-35b3-aa7b-9750ae61ed09 | -20.99154 | -46.08303 | 2024-10-07 04:04:00 | NOAA-20 | CARMO DO RIO CLARO | MINAS GERAIS | Brasil | 3114402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| cf6c743e-bfe2-37d6-bc2e-a3638459c8a6 | -20.99084 | -46.08702 | 2024-10-07 04:04:00 | NOAA-20 | CARMO DO RIO CLARO | MINAS GERAIS | Brasil | 3114402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| ae93eef1-c96c-3bb8-8402-d2937be1a278 | -20.99012 | -46.09117 | 2024-10-07 04:04:00 | NOAA-20 | CARMO DO RIO CLARO | MINAS GERAIS | Brasil | 3114402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| 4cde4165-3901-3578-b011-ee682b806fdc | -20.98802 | -46.08239 | 2024-10-07 04:04:00 | NOAA-20 | CARMO DO RIO CLARO | MINAS GERAIS | Brasil | 3114402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 7a2b6a03-63c2-312f-97d0-eab4034193d9 | -20.98584 | -46.09485 | 2024-10-07 04:04:00 | NOAA-20 | CARMO DO RIO CLARO | MINAS GERAIS | Brasil | 3114402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| f7b3e607-08b0-3a92-80a7-819a09239cb9 | -20.9852 | -46.07779 | 2024-10-07 04:04:00 | NOAA-20 | CARMO DO RIO CLARO | MINAS GERAIS | Brasil | 3114402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 31c80ac4-e85f-399e-943c-2e6634240491 | -20.9851 | -46.09903 | 2024-10-07 04:04:00 | NOAA-20 | CARMO DO RIO CLARO | MINAS GERAIS | Brasil | 3114402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| 80edf5ec-fff5-33e8-8106-75df37e9f886 | -20.98448 | -46.08186 | 2024-10-07 04:04:00 | NOAA-20 | CARMO DO RIO CLARO | MINAS GERAIS | Brasil | 3114402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| b8d3365a-31bd-3c14-bc40-04b06d54c675 | -20.98377 | -46.08593 | 2024-10-07 04:04:00 | NOAA-20 | CARMO DO RIO CLARO | MINAS GERAIS | Brasil | 3114402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.8 |
| dcd6ec7b-88ca-396a-b3b9-6a32cb0bffb2 | -20.98303 | -46.09013 | 2024-10-07 04:04:00 | NOAA-20 | CARMO DO RIO CLARO | MINAS GERAIS | Brasil | 3114402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.8 |
| 0e965bcb-2b57-37fc-9971-398d46751389 | -20.98229 | -46.09439 | 2024-10-07 04:04:00 | NOAA-20 | CARMO DO RIO CLARO | MINAS GERAIS | Brasil | 3114402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| 048af92a-7ec2-3a99-8871-60229c19f90d | -20.98166 | -46.07722 | 2024-10-07 04:04:00 | NOAA-20 | CARMO DO RIO CLARO | MINAS GERAIS | Brasil | 3114402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 6ce5c5c4-adfd-3da7-b6d3-54b20aa05d03 | -20.98094 | -46.08135 | 2024-10-07 04:04:00 | NOAA-20 | CARMO DO RIO CLARO | MINAS GERAIS | Brasil | 3114402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 902889f3-eaf0-33ea-bcc7-186f937524a4 | -20.98021 | -46.0855 | 2024-10-07 04:04:00 | NOAA-20 | CARMO DO RIO CLARO | MINAS GERAIS | Brasil | 3114402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| cbf8f9bd-eca7-363b-b63c-9a3729f9ed1d | -20.97948 | -46.08968 | 2024-10-07 04:04:00 | NOAA-20 | CARMO DO RIO CLARO | MINAS GERAIS | Brasil | 3114402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| be0618f8-20fd-3725-9c2f-a896dd2c2f9d | -23.44175 | -47.05325 | 2024-10-07 04:04:00 | NOAA-20 | ARAÇARIGUAMA | SÃO PAULO | Brasil | 3502754 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 3ac3e954-a3f6-3b19-83ee-06adc7caeb2c | -23.44095 | -47.05771 | 2024-10-07 04:04:00 | NOAA-20 | ARAÇARIGUAMA | SÃO PAULO | Brasil | 3502754 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 0fecd84a-e725-330d-a1da-88599b9189fa | -23.4382 | -47.05249 | 2024-10-07 04:04:00 | NOAA-20 | ARAÇARIGUAMA | SÃO PAULO | Brasil | 3502754 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 4cb35d22-a080-3421-b708-2b6ffa6a2ae9 | -23.4374 | -47.05695 | 2024-10-07 04:04:00 | NOAA-20 | ARAÇARIGUAMA | SÃO PAULO | Brasil | 3502754 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| b6e795dd-884d-3aa9-bf71-674ce199abdf | -23.33869 | -46.77488 | 2024-10-07 04:04:00 | NOAA-20 | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| bb7aa764-382b-3ba2-b50e-8f8534fbbdea | -22.73584 | -47.03937 | 2024-10-07 04:04:00 | NOAA-20 | CAMPINAS | SÃO PAULO | Brasil | 3509502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| b8eab3b3-6137-34db-809e-59bf41a59016 | -22.53794 | -46.73683 | 2024-10-07 04:04:00 | NOAA-20 | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 10e78451-53f4-3c0e-9220-47f7908b1b33 | -14.12 | -45.54 | 2024-10-07 04:04:04 | MSG-03 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| d6ef31d7-28f4-3262-9b8b-f74f41967e14 | -14.09 | -45.48 | 2024-10-07 04:04:04 | MSG-03 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| d9a0c069-24c2-3158-b22f-c8625799bdc6 | -14.09 | -45.53 | 2024-10-07 04:04:04 | MSG-03 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 9cdffccf-9a21-3ffe-a709-21bab8480342 | -1.0365 | -53.7389 | 2024-10-07 04:05:12 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 58.8 |
| 9ab96b21-3ba0-38b7-98bb-600088bcc7f5 | -2.8753 | -52.9192 | 2024-10-07 04:05:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 73.8 |
| 5ab4c1c5-8324-32a0-9a7e-a6e7e28e5b2f | -2.8754 | -52.8989 | 2024-10-07 04:05:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 71.4 |
| c8a47bb3-06fa-31ba-8a3c-d93e43058f68 | -4.2728 | -43.7601 | 2024-10-07 04:05:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 50.5 |
| b923221d-1d16-37c7-a273-887b822c0427 | -4.2729 | -43.737 | 2024-10-07 04:05:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 103.4 |
| c9428a86-1b2f-3b6e-b7e3-294c173446d6 | -8.1942 | -43.7403 | 2024-10-07 04:05:52 | GOES-16 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Caatinga | 91.8 |
| 74d0bed6-4f73-3863-bdd3-07f171e1bde3 | -8.1945 | -43.717 | 2024-10-07 04:05:52 | GOES-16 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Caatinga | 125.9 |
| d17a9be4-9d84-3abf-b3c7-3fdd29f2431a | -28.58357 | -49.44156 | 2024-10-07 04:06:00 | NOAA-20 | SIDERÓPOLIS | SANTA CATARINA | Brasil | 4217600 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 0100523a-75c4-368c-9328-6dfd67ea6c8a | -26.93431 | -51.11219 | 2024-10-07 04:06:00 | NOAA-20 | RIO DAS ANTAS | SANTA CATARINA | Brasil | 4214409 | 42 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| 612f1fdd-86d9-37aa-90af-77a9bdca2a8b | -10.8337 | -68.3636 | 2024-10-07 04:06:08 | GOES-16 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 46.8 |
| 00993950-5ea5-3b90-9103-e7240b67287c | -10.8754 | -63.9169 | 2024-10-07 04:06:08 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 53.0 |
| be1a3ec0-9392-316b-9755-ab6d001bc7a9 | -10.8755 | -63.8979 | 2024-10-07 04:06:08 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 57.4 |
| df41000c-9ea8-33ee-9610-7947e33ef112 | -11.247 | -51.3706 | 2024-10-07 04:06:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 73.9 |
| 61ed0280-68b6-38ec-9805-2d018404e402 | -11.266 | -51.3686 | 2024-10-07 04:06:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 73.0 |
| c99e652f-ab49-33ea-ad89-fe201f836df5 | -11.2847 | -51.3878 | 2024-10-07 04:06:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 94.8 |
| d2d68dd0-cac7-357f-ae7b-dc6363510f63 | -11.285 | -51.3666 | 2024-10-07 04:06:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 104.0 |
| 60b54d89-58a4-3142-a3a7-672db465dcd3 | -11.3037 | -51.3858 | 2024-10-07 04:06:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 67.3 |
| 37968c31-eb10-3469-b81e-6afb0c3324ff | -11.304 | -51.3646 | 2024-10-07 04:06:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 65.3 |
| cd52ead6-185b-3f48-8d2c-0e98cce87d9d | -14.0703 | -45.4611 | 2024-10-07 04:06:25 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 87.0 |
| 73c01263-3ab7-3c99-8c6f-0605a7d716fe | -14.0898 | -45.4577 | 2024-10-07 04:06:25 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 91.5 |
| fb90f9ff-8013-3587-a7c0-0da16de56d20 | -14.1073 | -45.5473 | 2024-10-07 04:06:25 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 64.8 |
| 3e1836d2-2d1f-39b7-be70-60e8fc13b86a | -14.1078 | -45.5241 | 2024-10-07 04:06:25 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 202.7 |
| dd2db5ad-848b-3c43-8305-ec47abe83948 | -14.1083 | -45.5008 | 2024-10-07 04:06:25 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 143.5 |
| 80dc6322-e8fc-3d67-8dca-8ebfdc606b38 | -14.1268 | -45.5439 | 2024-10-07 04:06:25 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 85.1 |
| bf452786-3801-3d4c-b9fc-f1abf8e62ba4 | -14.1273 | -45.5207 | 2024-10-07 04:06:25 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 238.1 |
| 0800154e-2ff2-38dc-8233-9ef4a5630067 | -14.1278 | -45.4974 | 2024-10-07 04:06:25 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 114.3 |
| 5aa9c677-d15b-30e0-93ca-0243ec033807 | -16.5072 | -57.7387 | 2024-10-07 04:06:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 100.0 |
| cd89cc16-1e7f-3026-ba22-00dfef4a7662 | -16.5075 | -57.7183 | 2024-10-07 04:06:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 77.4 |
| 9ec533ef-8a74-3d02-83a4-329d6f00905a | -16.5267 | -57.7365 | 2024-10-07 04:06:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 113.9 |
| a9864d00-ab49-3d0c-b1cf-3109c080c825 | -16.5745 | -57.16 | 2024-10-07 04:06:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 113.6 |
| f09ac9c6-de77-3ac7-b9bf-b5500d083b60 | -16.5749 | -57.1395 | 2024-10-07 04:06:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 104.4 |
| f001adda-8361-3082-98f5-93c5accb2cd2 | -16.6136 | -57.1555 | 2024-10-07 04:06:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 103.6 |
| f5814112-892a-350e-953a-ccb20da630b2 | -16.614 | -57.135 | 2024-10-07 04:06:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 100.6 |
| 08e39afd-eee2-37b4-bb40-d9de62b97acc | -16.6332 | -57.1533 | 2024-10-07 04:06:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 139.9 |
| dc78e699-7b89-3fa3-bba8-170898943e5c | -16.6335 | -57.1328 | 2024-10-07 04:06:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 120.1 |
| 4cf27ea4-1607-3f15-a2e2-e3156de139d6 | -17.0985 | -57.4062 | 2024-10-07 04:06:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 73.2 |
| 8531c37d-f874-3554-b232-41baacc6bd41 | -17.0982 | -57.4267 | 2024-10-07 04:06:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 80.3 |
| 0dd079ea-012e-3298-965f-417a74c88fb5 | -17.1433 | -51.7206 | 2024-10-07 04:06:42 | GOES-16 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 86.8 |
| 8f98feff-b58e-3861-8463-1ff32210fdc1 | -17.1185 | -57.3834 | 2024-10-07 04:06:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 57.8 |
| 6b0ed221-e9e6-3e7b-816a-cc0286251214 | -17.012 | -56.698 | 2024-10-07 04:06:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 96.0 |
| 0808d73b-8c7a-3d52-afe6-2e067187b9e1 | -17.0123 | -56.6773 | 2024-10-07 04:06:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 91.1 |
| 5051f55d-d385-342b-b41d-4ec22f40e219 | -17.0319 | -56.6749 | 2024-10-07 04:06:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 91.9 |
| 46035b76-13cc-3280-bfe7-5017940a70fe | -17.1182 | -57.4039 | 2024-10-07 04:06:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 46.7 |
| d123f999-efc1-3cc9-8a9c-8596b573239a | -17.0989 | -57.3857 | 2024-10-07 04:06:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 54.4 |
| 96ac6bbf-f469-3f6f-bc79-3c67ba3ee3f4 | -17.1584 | -57.3377 | 2024-10-07 04:06:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 83.6 |
| 4ec8ac62-3fa6-3786-99ba-2b0bd8c87fa7 | -17.1581 | -57.3582 | 2024-10-07 04:06:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 81.9 |
| fd9016a4-8850-3254-b625-dc0ea7f34da8 | -17.1375 | -57.4221 | 2024-10-07 04:06:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 50.4 |
| ecf2a897-d1b9-3cf6-8838-0ecb807722a7 | -17.178 | -57.3354 | 2024-10-07 04:06:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 45.3 |
| 7f66395e-33e3-3943-8a48-c8b819e038e6 | -17.1777 | -57.3559 | 2024-10-07 04:06:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 46.8 |
| 326facea-637e-32fd-9ec9-338c20fbf6ae | -17.7922 | -53.7889 | 2024-10-07 04:06:46 | GOES-16 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 165.6 |
| e16b4989-1c96-318e-8ce4-b552e7f3f3e2 | -17.8314 | -53.8043 | 2024-10-07 04:06:46 | GOES-16 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 91.4 |
| 080ad7cf-38d7-3fff-b386-0ad9461e4af1 | -17.7724 | -53.7918 | 2024-10-07 04:06:46 | GOES-16 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 106.2 |
| 0b8cafe5-e22f-3f14-98ad-35d09dd7705d | -17.8319 | -53.7829 | 2024-10-07 04:06:46 | GOES-16 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 116.6 |
| 952d61f9-b8c6-37f8-9702-d87b1d9ed0c6 | -17.772 | -53.8132 | 2024-10-07 04:06:46 | GOES-16 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 98.7 |
| 86f82550-0673-38df-a21b-b0214a2033fd | -17.7918 | -53.8102 | 2024-10-07 04:06:46 | GOES-16 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 178.0 |
| 28db9cb8-845e-3357-a4f7-b1a3f58fef24 | -18.6391 | -57.2578 | 2024-10-07 04:06:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 62.2 |
| 5df55bb7-be94-381b-860c-ad83dbe201ea | -18.659 | -57.2552 | 2024-10-07 04:06:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 60.3 |
| e595e891-9e2b-336d-8975-ed254804a40a | -18.7176 | -57.3097 | 2024-10-07 04:06:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 129.2 |


[Clique aqui para ver as próximas entradas](README75.md)
