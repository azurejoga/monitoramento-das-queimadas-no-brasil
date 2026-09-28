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

## Dados Diários - Página 98

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a439b1b8-d330-315e-83bc-d72bb1aea918 | -12.38564 | -50.23513 | 2026-09-28 16:24:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 67998298-c90c-3c73-be6d-0d8520cbc57d | -13.01016 | -49.05375 | 2026-09-28 16:24:00 | NOAA-20 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 6c508bbf-59c1-3881-b9ea-a6b7a74f4a79 | -11.91316 | -47.00437 | 2026-09-28 16:24:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 4ce7c099-f80f-3c15-944b-a86b125bbc6e | -11.56574 | -47.39899 | 2026-09-28 16:24:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 65582160-8fc6-3863-9aa3-d69a7b2da830 | -13.07563 | -47.45405 | 2026-09-28 16:24:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 8c839a52-77e7-3a8d-8a95-7a17b3da6839 | -12.90815 | -52.83682 | 2026-09-28 16:24:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 52f30660-6dbb-33d6-8b88-e5e4af7d7084 | -16.15035 | -42.85249 | 2026-09-28 16:24:00 | NOAA-20 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 6c568312-e1f7-3dd5-b2e2-51b70b8f1bbb | -12.05093 | -46.49148 | 2026-09-28 16:24:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 48ca3dc6-966e-3a64-9752-0e2b2f5ee9c5 | -11.38212 | -43.38933 | 2026-09-28 16:24:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 409a7f4d-b928-3f2d-a2e8-ad76ebad93b0 | -14.74978 | -41.96078 | 2026-09-28 16:24:00 | NOAA-20 | CONDEÚBA | BAHIA | Brasil | 2908705 | 29 | 33 | nan | nan | nan | Caatinga | 91.6 |
| 9b9637c9-2901-3e9b-8adc-26b445fad2ae | -14.09247 | -46.32375 | 2026-09-28 16:24:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| a20fff8c-2f92-3cb2-84f4-9253815ad703 | -15.43019 | -47.56577 | 2026-09-28 16:24:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 44254ba8-9e1d-3a6f-bba7-f480cc2444a1 | -15.48008 | -46.13823 | 2026-09-28 16:24:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 9.7 |
| f79eca30-d3a7-3faf-8f6e-5cd8deb55f51 | -14.48132 | -53.64294 | 2026-09-28 16:24:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 49578022-a597-38ec-9095-11c7bd1b55af | -14.4895 | -45.2399 | 2026-09-28 16:24:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 56.2 |
| 0b56ebe0-baa8-34de-959d-049c21d70e88 | -13.69666 | -48.81989 | 2026-09-28 16:24:00 | NOAA-20 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 16.2 |
| 767e8bc0-7fe8-318d-a6f4-260b405acdd8 | -11.21968 | -44.79586 | 2026-09-28 16:24:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 21.2 |
| f8a7ca9f-ca7f-3026-8f41-b27da7713b1f | -12.75655 | -47.31739 | 2026-09-28 16:24:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 53c3c6df-fbbc-3268-8366-8fddc67db6df | -13.88969 | -42.21938 | 2026-09-28 16:24:00 | NOAA-20 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 4.8 |
| dfb0ab7e-116e-39c6-b5ee-d4dd63730ef9 | -13.48016 | -48.60159 | 2026-09-28 16:24:00 | NOAA-20 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 19.2 |
| ecfaacef-f5c3-3e55-adef-73a8eabd2043 | -13.07997 | -47.45348 | 2026-09-28 16:24:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 20fa8f86-d05d-39d7-8686-2f2f7070eb87 | -12.28791 | -50.26709 | 2026-09-28 16:24:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| fe6fa06c-715f-38a9-a2af-dccc46e3b28a | -13.97936 | -54.00893 | 2026-09-28 16:24:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 19.8 |
| eee0a856-291a-3850-863a-f808c2ef4315 | -13.70694 | -48.82402 | 2026-09-28 16:24:00 | NOAA-20 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 972c4bf1-adb7-358e-8646-0aa702854c32 | -13.37641 | -44.02585 | 2026-09-28 16:24:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 15.9 |
| fecf8e30-e722-3403-af10-599dcf788bef | -15.18146 | -46.13269 | 2026-09-28 16:24:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 13.6 |
| c9e3e0bd-d16d-30ad-992a-e702764ce443 | -12.06339 | -50.21856 | 2026-09-28 16:24:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 15.1 |
| ca9abe36-8b16-30ef-8213-7c4b99e241e7 | -13.56381 | -49.0843 | 2026-09-28 16:24:00 | NOAA-20 | MUTUNÓPOLIS | GOIÁS | Brasil | 5214101 | 52 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 7c359bdc-4d79-35c6-8627-682a3e11753f | -11.38035 | -43.40099 | 2026-09-28 16:24:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 15.2 |
| aaf4c86b-b314-3e1f-8666-6b878c6c90ef | -14.50714 | -48.32136 | 2026-09-28 16:24:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| e6773263-a1d0-3771-9467-1f690258733c | -11.86111 | -47.1019 | 2026-09-28 16:24:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 9754dca4-7e44-3f52-9aed-0d1da945275e | -15.63091 | -43.52222 | 2026-09-28 16:24:00 | NOAA-20 | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 7e50faf2-3ba4-3530-ad03-8284bc9361c0 | -16.33159 | -39.86633 | 2026-09-28 16:24:00 | NOAA-20 | GUARATINGA | BAHIA | Brasil | 2911808 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| c31699e4-6685-3bf9-9186-154edaf9aed8 | -11.90331 | -47.0252 | 2026-09-28 16:24:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| a310e689-675f-3859-b62c-fe18d27c8159 | -15.16607 | -43.57604 | 2026-09-28 16:24:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 38.2 |
| cdf01b5f-fd05-38d6-97f8-6515eff4d2e8 | -11.14672 | -40.30043 | 2026-09-28 16:24:00 | NOAA-20 | CAÉM | BAHIA | Brasil | 2905107 | 29 | 33 | nan | nan | nan | Caatinga | 3.6 |
| b31662e5-38c0-3e39-8587-4edebede05ef | -16.06885 | -47.91713 | 2026-09-28 16:24:00 | NOAA-20 | CIDADE OCIDENTAL | GOIÁS | Brasil | 5205497 | 52 | 33 | nan | nan | nan | Cerrado | 15.5 |
| a3ac2b7b-fbb6-3239-aa7a-b1ee14bb2745 | -15.68715 | -48.10679 | 2026-09-28 16:24:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 7ae8ddc2-2dfc-3ed6-88b2-a735b20af5c4 | -14.46758 | -47.05803 | 2026-09-28 16:24:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 55a198b6-a6c1-37a3-b8c6-b96917fda564 | -11.18173 | -44.79998 | 2026-09-28 16:24:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 161.3 |
| 9b045864-73ec-3ebd-84b5-54ecf88539d3 | -13.44894 | -48.59708 | 2026-09-28 16:24:00 | NOAA-20 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 8.8 |
| dc532ffd-9a30-3671-95fc-91a9c5c8cac4 | -12.94141 | -46.64031 | 2026-09-28 16:24:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 58.3 |
| e47221e5-a729-3b66-a2e2-643f44f39eeb | -11.77131 | -41.14898 | 2026-09-28 16:24:00 | NOAA-20 | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 5.1 |
| b4757f3e-3230-3636-8a09-ddffd7c563fe | -12.39159 | -50.24083 | 2026-09-28 16:24:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 26.1 |
| 4214ce5f-4f3f-3d25-9332-5195361eb945 | -16.6402 | -48.47556 | 2026-09-28 16:24:00 | NOAA-20 | SILVÂNIA | GOIÁS | Brasil | 5220603 | 52 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 7af1fe65-0db5-3aff-9e96-fcdbbee9c1ae | -15.453 | -41.44695 | 2026-09-28 16:24:00 | NOAA-20 | NINHEIRA | MINAS GERAIS | Brasil | 3144656 | 31 | 33 | nan | nan | nan | Mata Atlântica | 13.5 |
| 4c8d860a-b40a-3e1b-b500-2b514704f2ae | -14.73882 | -41.05072 | 2026-09-28 16:24:00 | NOAA-20 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 10.3 |
| e5531063-5c5b-3d5b-9982-bc170511ed67 | -11.53402 | -47.38715 | 2026-09-28 16:24:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 20.4 |
| 47c3cfc6-63a9-3efe-8c3b-7da9dd6d039d | -15.39746 | -47.90847 | 2026-09-28 16:24:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 7438c486-57e6-3972-be12-abb0a378be1f | -13.26055 | -48.4814 | 2026-09-28 16:24:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 146f5e45-1e24-321b-be0b-ae31ebe34a38 | -11.63948 | -43.49981 | 2026-09-28 16:24:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 39.1 |
| bfb68711-84f5-3f5c-8d7b-515406e66180 | -13.27045 | -39.87608 | 2026-09-28 16:24:00 | NOAA-20 | SANTA INÊS | BAHIA | Brasil | 2927903 | 29 | 33 | nan | nan | nan | Mata Atlântica | 8.9 |
| 9381ac33-9cab-3ac1-95fe-db19d41e4bab | -15.25477 | -40.62957 | 2026-09-28 16:24:00 | NOAA-20 | ITAMBÉ | BAHIA | Brasil | 2915809 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| d1ee7ed1-3a8b-3495-99cb-642996731b0a | -12.29676 | -50.25308 | 2026-09-28 16:24:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 7dd10277-556f-3433-a32a-535577934936 | -13.65139 | -42.89079 | 2026-09-28 16:24:00 | NOAA-20 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 11.7 |
| ca9ef503-345e-378a-9506-10ca083de3fe | -13.55985 | -46.3694 | 2026-09-28 16:24:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 1ec489ea-f161-3421-b077-896c04a03e31 | -14.53464 | -48.31229 | 2026-09-28 16:24:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 3c5230dc-1cf1-387e-b659-9f59d3ba8cfe | -11.20208 | -40.58773 | 2026-09-28 16:24:00 | NOAA-20 | JACOBINA | BAHIA | Brasil | 2917508 | 29 | 33 | nan | nan | nan | Caatinga | 9.9 |
| a067b2b7-d543-36ef-9ae1-81dc1794e6f9 | -12.15115 | -50.3749 | 2026-09-28 16:24:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 5c53568a-71cb-3ea1-89d8-5f9e17be3d12 | -16.64294 | -48.4743 | 2026-09-28 16:24:00 | NOAA-20 | SILVÂNIA | GOIÁS | Brasil | 5220603 | 52 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 823545f8-591c-3c8f-ac62-1ab5a2f165b5 | -12.66921 | -46.98816 | 2026-09-28 16:24:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 545b6b04-8e0a-3dac-80d9-1e082835c1d8 | -12.3185 | -46.40958 | 2026-09-28 16:24:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 9f40a497-2523-3b28-916c-bb6d18573cb3 | -12.68837 | -46.97256 | 2026-09-28 16:24:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| bf149bbb-fac4-355e-8886-6e0c78cc1dbb | -11.50287 | -47.37914 | 2026-09-28 16:24:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 24.0 |
| 3128df39-0c1b-3cc4-af40-c0751d0de77e | -15.25097 | -43.66475 | 2026-09-28 16:24:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 7.1 |
| c76976b4-b2f7-3abb-9587-484d17830a90 | -11.57051 | -47.40237 | 2026-09-28 16:24:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| b064ebf8-98fb-3e78-8f9c-a4cd3a70637e | -14.42517 | -41.08473 | 2026-09-28 16:24:00 | NOAA-20 | ARACATU | BAHIA | Brasil | 2902005 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 9f14d1e2-b1d7-3ea5-b7dd-8f7266993425 | -12.75038 | -50.68579 | 2026-09-28 16:24:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 18.5 |
| d77f861b-d8c9-3e38-b04c-c088d966d8f7 | -12.75301 | -50.68493 | 2026-09-28 16:24:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 7e0ef27d-7ef0-3e89-9494-29ddbb54c070 | -12.73615 | -51.5816 | 2026-09-28 16:24:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 8.7 |
| f2e89481-79c5-3f98-821c-786ddb720f1a | -11.52979 | -47.3877 | 2026-09-28 16:24:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 11.8 |
| c30fb757-3512-327a-bc9a-cf11b2687dc1 | -15.1543 | -43.61874 | 2026-09-28 16:24:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 73.8 |
| a92c9f0b-03d8-3a90-bba6-7b314e112cc6 | -11.6355 | -43.49656 | 2026-09-28 16:24:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 39.1 |
| 1782b3a9-f746-3ff9-b3ab-493c1f1d67cb | -11.64069 | -43.48425 | 2026-09-28 16:24:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 7.1 |
| c86a4630-23c8-3525-a7dd-2b458709cc95 | -13.17201 | -48.55544 | 2026-09-28 16:24:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 11.2 |
| a8dae6da-f02a-322b-8c5d-7c920c1c58da | -14.20925 | -42.06523 | 2026-09-28 16:24:00 | NOAA-20 | RIO DO ANTÔNIO | BAHIA | Brasil | 2926806 | 29 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 510637be-d911-3231-9943-2b6fd7a08ad6 | -12.67338 | -45.04108 | 2026-09-28 16:24:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 19.8 |
| dc983c7c-f196-369b-a178-c3895603ccf5 | -12.17293 | -50.41795 | 2026-09-28 16:24:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 1c1cc165-7581-3462-9f64-e4967b45d29e | -11.52926 | -47.38376 | 2026-09-28 16:24:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 11.8 |
| a2a00fb5-6bf9-3100-bed0-26df0f805271 | -16.16538 | -49.23631 | 2026-09-28 16:24:00 | NOAA-20 | PETROLINA DE GOIÁS | GOIÁS | Brasil | 5216809 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0e8d410b-17c2-340e-8d8b-c15ddebdc09f | -12.79223 | -54.06964 | 2026-09-28 16:24:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 16.2 |
| 7b5015ea-f8e8-36e1-802d-9f3392381c5f | -12.42436 | -44.15629 | 2026-09-28 16:24:00 | NOAA-20 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 01eecdf3-b70c-33c7-ad9c-46d70c9076ad | -15.0383 | -49.58763 | 2026-09-28 16:24:00 | NOAA-20 | NOVA GLÓRIA | GOIÁS | Brasil | 5214861 | 52 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 632abaeb-f219-388c-af77-15c203505e73 | -15.19351 | -46.13526 | 2026-09-28 16:24:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 4.7 |
| e5f80496-e169-3644-be61-be17d055bbf7 | -13.33124 | -46.81128 | 2026-09-28 16:24:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 23.0 |
| 1881f349-e616-34f8-a2d8-efa03876b9d0 | -13.26672 | -47.43974 | 2026-09-28 16:24:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 11.0 |
| af9966eb-4a62-3774-a580-b2c401084e35 | -12.37901 | -50.23625 | 2026-09-28 16:24:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 19.4 |
| 8c6f7618-584d-37a0-a6b4-61f570e2dfaa | -11.99458 | -41.18816 | 2026-09-28 16:24:00 | NOAA-20 | UTINGA | BAHIA | Brasil | 2932804 | 29 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 954607cb-ac0f-34cc-b4a3-647439e86ffb | -16.41502 | -43.50932 | 2026-09-28 16:24:00 | NOAA-20 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 6a60e645-2c1a-3380-bd65-e71c8c32d0ab | -11.90178 | -47.01375 | 2026-09-28 16:24:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 4ac1591c-c7c6-3c4b-bf95-c0bc8a9bc719 | -11.35939 | -43.40034 | 2026-09-28 16:24:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 35.4 |
| 0ae3baa0-99ad-3e6d-a01b-fda6697c85a5 | -14.12322 | -46.30528 | 2026-09-28 16:24:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 28.3 |
| d93aea3a-c49b-3a5d-9434-da9b3bd9d0f0 | -13.08486 | -47.45712 | 2026-09-28 16:24:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 38370d17-d1a1-306d-8067-b2e37785f307 | -12.48186 | -47.1652 | 2026-09-28 16:24:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 45fa8856-bb97-342a-8e85-a8a0eae1b31c | -12.39121 | -50.23765 | 2026-09-28 16:24:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 12.9 |
| b0f90656-7381-3804-b7c4-630064138c9d | -15.0915 | -54.72005 | 2026-09-28 16:24:00 | NOAA-20 | CAMPO VERDE | MATO GROSSO | Brasil | 5102678 | 51 | 33 | nan | nan | nan | Cerrado | 21.7 |
| d4829a4c-4c7b-39e7-90ab-8c1b8a7d1db5 | -12.37045 | -50.24029 | 2026-09-28 16:24:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 4903ac6d-d21c-3cb6-a8ab-143f181e9fc9 | -13.5639 | -46.36877 | 2026-09-28 16:24:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 47947019-e92c-363b-8d25-4c71c254fa6e | -14.32008 | -44.81921 | 2026-09-28 16:24:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 39.1 |
| 53faf1a5-7471-3d43-81ed-9374de1fda0b | -13.4896 | -48.60043 | 2026-09-28 16:24:00 | NOAA-20 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 22.4 |


[Clique aqui para ver as próximas entradas](README99.md)
