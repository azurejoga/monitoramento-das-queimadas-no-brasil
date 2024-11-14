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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 27623773-2bb9-393b-8332-718ee7a55919 | -4.77103 | -45.73618 | 2024-11-14 03:46:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 47f9b8c8-3df9-3987-8606-ad3d6d09459e | -5.35109 | -43.54433 | 2024-11-14 03:46:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 3af7b5d5-f202-31a5-b7be-b0e0b289f3db | -5.19597 | -44.35518 | 2024-11-14 03:46:00 | NOAA-20 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 639f029b-6d6b-3d4f-9e81-286836571149 | -3.99869 | -45.57271 | 2024-11-14 03:46:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 4.7 |
| da2978b3-231d-3eca-96a5-6bdc0e2a7017 | -4.92106 | -45.71669 | 2024-11-14 03:46:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5c6cd92a-08d2-3610-b54e-6ef77f7e4d7e | -6.04282 | -44.03985 | 2024-11-14 03:46:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 30.2 |
| 13e22949-7522-36a0-a705-d267dfac4724 | -8.39754 | -35.2925 | 2024-11-14 03:46:00 | NOAA-20 | ESCADA | PERNAMBUCO | Brasil | 2605202 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| ae6d7a83-33d1-38e9-a153-5ffd37f9e1e1 | -4.15756 | -45.77399 | 2024-11-14 03:46:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 841cfcfc-82e1-33e9-ae04-4f841726f5e3 | -2.63826 | -46.18106 | 2024-11-14 03:46:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 486da13a-0660-3c38-baa4-c25bc248b48a | -4.4504 | -43.97881 | 2024-11-14 03:46:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1274cdf8-1c07-3a2d-8a27-4f791db1a992 | -6.59431 | -38.93258 | 2024-11-14 03:46:00 | NOAA-20 | CEDRO | CEARÁ | Brasil | 2303808 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| c0b47dff-99ca-35fc-ba2c-c831be0a3446 | -3.1709 | -45.44321 | 2024-11-14 03:46:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| adef22e0-7a4a-3e40-a359-a2da57b57fe4 | -2.63893 | -46.18304 | 2024-11-14 03:46:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c9d60fb8-a119-38b8-8b8a-c097cba26159 | -2.01955 | -46.50843 | 2024-11-14 03:46:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 989b50ac-4d6e-3ed0-bd70-77612164bda6 | -6.95647 | -39.42656 | 2024-11-14 03:46:00 | NOAA-20 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| b5357c85-14ce-34ff-8dac-9e70d4465dba | -6.6242 | -35.1881 | 2024-11-14 03:46:00 | NOAA-20 | JACARAÚ | PARAÍBA | Brasil | 2507309 | 25 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| 48b5c0ac-25ec-3fd3-a850-15c2fb852692 | -2.11032 | -46.53289 | 2024-11-14 03:46:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3081aa21-8050-356e-b5ea-6998f035c8fc | -2.64084 | -46.16518 | 2024-11-14 03:46:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7259f434-e73a-366d-87d8-f90d7b2d7f8b | -4.43796 | -45.95693 | 2024-11-14 03:46:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 667c62f4-67a9-3914-9d04-9ec47fc81d5d | -4.55798 | -48.02073 | 2024-11-14 03:46:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| eacef74b-1af7-328d-869c-ca87e948a8de | -3.05457 | -45.53211 | 2024-11-14 03:46:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 993b4063-ada6-37c3-9410-12aeb8b7cf72 | -7.43691 | -39.01488 | 2024-11-14 03:46:00 | NOAA-20 | BREJO SANTO | CEARÁ | Brasil | 2302503 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| c31b7e40-e489-39ff-8fed-a994bee3e8d1 | -4.02874 | -44.68469 | 2024-11-14 03:46:00 | NOAA-20 | SÃO MATEUS DO MARANHÃO | MARANHÃO | Brasil | 2111508 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9548872e-9bcd-3859-99c6-6bd69af19e8d | -4.10329 | -38.74035 | 2024-11-14 03:46:00 | NOAA-20 | GUAIÚBA | CEARÁ | Brasil | 2304954 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| cf764cb2-377e-3c84-b526-f3dbfd82dbc1 | -4.28475 | -46.88194 | 2024-11-14 03:46:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 20d01885-488a-35a0-9635-f510df1fb37d | -3.17575 | -45.4477 | 2024-11-14 03:46:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5bbf8e8b-dd6e-3ece-b05f-f6cdc5ddf950 | -2.19294 | -46.35934 | 2024-11-14 03:46:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b7fdbdb3-03fe-3a48-b743-6afde8733b51 | -4.7941 | -43.66409 | 2024-11-14 03:46:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e5f68b31-e18d-378e-b52c-9212ae866432 | -1.85341 | -46.28706 | 2024-11-14 03:46:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7ca9a3c8-4029-3394-926e-3bb7197632c1 | -4.19275 | -42.33329 | 2024-11-14 03:46:00 | NOAA-20 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 9f0b77e4-36a9-3243-be4c-cf701e8d91b8 | -4.14944 | -46.2497 | 2024-11-14 03:46:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 04f35102-d282-3e35-8087-670730223971 | -5.56351 | -45.36856 | 2024-11-14 03:46:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9b1704c0-dfca-3576-ba41-80c6d7d8afc1 | -9.1633 | -50.5465 | 2024-11-14 03:46:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ec7835d4-e918-3f6c-894b-20038370f837 | -5.07454 | -45.51293 | 2024-11-14 03:46:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 899c350d-a662-3dca-ab7d-e6f00cfd12d9 | -2.67308 | -46.82903 | 2024-11-14 03:46:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c565fae4-390b-3dc5-9806-c9109f5b85da | -4.00524 | -45.56678 | 2024-11-14 03:46:00 | NOAA-20 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 4650212f-4d9c-3a36-a1b5-279bd9736ea9 | -6.04839 | -44.03566 | 2024-11-14 03:46:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |
| c8e71564-a573-3dfb-9315-c90a181e996b | -4.15208 | -45.77314 | 2024-11-14 03:46:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 10.3 |
| e768af32-d084-3078-8c30-d2424bd5e4f5 | -2.88626 | -46.87197 | 2024-11-14 03:46:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ee824482-a0a1-30fb-b435-0924f9499314 | -2.19227 | -46.36354 | 2024-11-14 03:46:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 69895be1-ee9a-3837-a921-5fe3f906c866 | -6.62364 | -35.19172 | 2024-11-14 03:46:00 | NOAA-20 | JACARAÚ | PARAÍBA | Brasil | 2507309 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 8131b644-b22b-3e58-820c-f68c5931314a | -2.6389 | -46.1771 | 2024-11-14 03:46:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 68f24554-8783-317c-8432-3e457583cc71 | -4.37044 | -48.08969 | 2024-11-14 03:46:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 553f71b3-3c07-369c-987c-fbd59cc85c02 | -3.71762 | -40.97072 | 2024-11-14 03:46:00 | NOAA-20 | TIANGUÁ | CEARÁ | Brasil | 2313401 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 5b5c1e77-e24c-3189-8bbc-4cf5412aed2c | -4.16578 | -46.25593 | 2024-11-14 03:46:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9292de80-061c-3198-807e-c444b6413112 | -7.06928 | -38.88068 | 2024-11-14 03:46:00 | NOAA-20 | BARRO | CEARÁ | Brasil | 2302008 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 5d8c3a08-eb2e-3be2-9880-6db07656d0d9 | -2.02367 | -46.94638 | 2024-11-14 03:46:00 | NOAA-20 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| e3783d7d-f99f-32a0-930c-c0c790754aa2 | -4.04906 | -47.23115 | 2024-11-14 03:46:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 77adc5bd-ee2f-30f2-b82b-d3f7093a6764 | -4.16645 | -46.25205 | 2024-11-14 03:46:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f0ded718-bad2-3ea2-8eb6-14b34f960f9e | -4.28405 | -46.88597 | 2024-11-14 03:46:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 94396c68-046a-33ba-80cd-14fa8e406b55 | -4.05328 | -47.23209 | 2024-11-14 03:46:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| dcbb7f99-a5ec-3b94-96fe-4db059070386 | -3.88856 | -46.09204 | 2024-11-14 03:46:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 068ea708-7850-3533-b1bb-c249128930a0 | -4.36799 | -48.08775 | 2024-11-14 03:46:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 8c7e6f85-4f9e-306e-925c-e5bcf6c55758 | -6.13565 | -43.96148 | 2024-11-14 03:46:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 81ab625d-00c8-3793-85de-21fa4d72dc99 | -4.02924 | -44.68169 | 2024-11-14 03:46:00 | NOAA-20 | SÃO MATEUS DO MARANHÃO | MARANHÃO | Brasil | 2111508 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f4b8c1f2-afda-3c6c-aabd-71a497b4095a | -5.56408 | -45.36538 | 2024-11-14 03:46:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4e0eaac6-aec9-3b89-85dd-3ac7bf91f945 | -5.92311 | -42.97438 | 2024-11-14 03:46:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 6.3 |
| 6d0b3dae-5b21-3417-a7f0-00c01a1e0b17 | -4.25652 | -44.14593 | 2024-11-14 03:46:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 114bf13f-0bb3-3818-a7ea-ded25b949cb7 | -4.45342 | -45.36373 | 2024-11-14 03:46:00 | NOAA-20 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f3df74c1-15bf-3d68-bcc8-200e7cfff3fa | -2.89969 | -46.86533 | 2024-11-14 03:46:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6053d11a-7cfc-3163-a9b3-42ebe751078f | -5.55029 | -44.32812 | 2024-11-14 03:46:00 | NOAA-20 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| cc696b96-dbbc-33b1-bbef-a8db03b93d28 | -3.99927 | -45.56926 | 2024-11-14 03:46:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 3840655d-acc4-34b2-8559-ad0ac5d5b2ac | -4.58479 | -46.62752 | 2024-11-14 03:46:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 751d8a0f-d655-37ea-be84-cce09955c18e | -4.51381 | -46.48124 | 2024-11-14 03:46:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7a29af5b-d40b-3671-a05e-9f4d09934fb3 | -4.37148 | -48.57647 | 2024-11-14 03:46:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| bc7a0740-657c-3f0b-a334-15e1176a1d25 | -4.43856 | -45.95344 | 2024-11-14 03:46:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2f0a25c4-ff3e-308e-ade5-72619bed2844 | -8.4876 | -35.43503 | 2024-11-14 03:46:00 | NOAA-20 | RIBEIRÃO | PERNAMBUCO | Brasil | 2611804 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| d01aea89-8e01-34d2-b49b-0f1dd722af89 | -3.76651 | -41.60144 | 2024-11-14 03:46:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 5c42815e-6dd4-30c8-94f8-0e504104f2e5 | -5.54724 | -44.32536 | 2024-11-14 03:46:00 | NOAA-20 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 6bd4786b-aaf0-30ea-8804-5e88620d9f8c | -4.0525 | -47.23674 | 2024-11-14 03:46:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 60cef0de-6316-3d01-92c9-49b39750855e | -2.11696 | -46.52955 | 2024-11-14 03:46:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d549ae17-7935-3f12-b48c-6598d22e0605 | -4.14204 | -43.85594 | 2024-11-14 03:46:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| a87133fe-560e-3d9c-a50e-d5f3ebf020b0 | -5.34378 | -46.02946 | 2024-11-14 03:46:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8a1cb2c5-0384-3f56-9fef-a1a5a5d02497 | -3.26105 | -46.27925 | 2024-11-14 03:46:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 3d7126b8-7641-3d52-b317-667a6bb20c88 | -5.47393 | -47.00788 | 2024-11-14 03:46:00 | NOAA-20 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3976824c-3a6d-35b9-b889-8bace0d3e7d0 | -5.91875 | -42.97351 | 2024-11-14 03:46:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 6.3 |
| df8d56ad-691b-3fc3-ad84-8fdb17c9c81f | -4.29969 | -48.10648 | 2024-11-14 03:46:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 502608c2-2bc2-339e-907d-8dbc30d5930f | -5.19776 | -44.35964 | 2024-11-14 03:46:00 | NOAA-20 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 3b0eea82-68af-3b46-90d7-c3502a5f0193 | -6.04367 | -44.03494 | 2024-11-14 03:46:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 97487376-3887-3043-b8b6-f026b2d1a2a1 | -5.35571 | -43.54503 | 2024-11-14 03:46:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 9172978f-94da-3bba-87a3-e5942710d898 | -9.54191 | -36.93379 | 2024-11-14 03:49:00 | NOAA-20 | MAJOR ISIDORO | ALAGOAS | Brasil | 2704401 | 27 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 1f596be2-57c1-3822-8ca5-e2b51abb2ee2 | -10.25374 | -36.45829 | 2024-11-14 03:49:00 | NOAA-20 | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| d4ff803b-117e-3632-9620-9a0dc1d9b3c2 | -9.16195 | -50.5441 | 2024-11-14 03:49:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 29627b2b-84a5-3e86-8b29-1a48b570f99b | -10.38995 | -39.12947 | 2024-11-14 03:49:00 | NOAA-20 | EUCLIDES DA CUNHA | BAHIA | Brasil | 2910701 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| f9a5b862-7ee7-33e1-ac2a-92194f3a52bf | -9.93083 | -37.61787 | 2024-11-14 03:49:00 | NOAA-20 | POÇO REDONDO | SERGIPE | Brasil | 2805406 | 28 | 33 | nan | nan | nan | Caatinga | 0.3 |
| bafff7e2-e0d0-3ede-b9a6-d861e2c9a7ae | -9.93414 | -37.6184 | 2024-11-14 03:49:00 | NOAA-20 | POÇO REDONDO | SERGIPE | Brasil | 2805406 | 28 | 33 | nan | nan | nan | Caatinga | 0.3 |
| 0f882ed4-fbe8-3a35-93e7-8a60fd82b3a2 | -20.69146 | -48.80672 | 2024-11-14 03:49:00 | NOAA-20 | OLÍMPIA | SÃO PAULO | Brasil | 3533908 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |
| fffff0e9-e71b-3011-b338-6d042437985a | -10.18365 | -36.1854 | 2024-11-14 03:49:00 | NOAA-20 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| a0504ad5-a514-3776-8a1a-70d2be4b03c0 | -9.28697 | -35.95234 | 2024-11-14 03:49:00 | NOAA-20 | MURICI | ALAGOAS | Brasil | 2705507 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 16279795-0d78-3a4c-995b-6ebdcc6b430f | -8.39686 | -48.05996 | 2024-11-14 03:49:00 | NOAA-20 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 196b4214-ee92-3f02-8c59-2dad348f7d08 | -10.95095 | -37.13159 | 2024-11-14 03:49:00 | NOAA-20 | SÃO CRISTÓVÃO | SERGIPE | Brasil | 2806701 | 28 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| bce84e52-2ed5-3336-a339-f7e73e166966 | -10.05199 | -36.35778 | 2024-11-14 03:49:00 | NOAA-20 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 437dbe5b-f863-3adf-ad76-b8e7ff4422e2 | -8.39606 | -48.06432 | 2024-11-14 03:49:00 | NOAA-20 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 20a9c61d-20f6-3e49-b8e8-3b7791fecd46 | -9.73568 | -37.45482 | 2024-11-14 03:49:00 | NOAA-20 | PÃO DE AÇÚCAR | ALAGOAS | Brasil | 2706406 | 27 | 33 | nan | nan | nan | Caatinga | 1.2 |
| a53d8ab3-0982-3e5d-a9ae-0f832becee30 | -10.25709 | -36.45881 | 2024-11-14 03:49:00 | NOAA-20 | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| aa83bafe-0d00-39ea-a2ef-02b509c18fe8 | -9.29035 | -35.95282 | 2024-11-14 03:49:00 | NOAA-20 | MURICI | ALAGOAS | Brasil | 2705507 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| dc9a88f1-328c-3065-9c08-67502a3357ea | -9.45218 | -37.85191 | 2024-11-14 03:49:00 | NOAA-20 | OLHO D'ÁGUA DO CASADO | ALAGOAS | Brasil | 2705804 | 27 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 842aedf6-0505-315c-9187-b0ff9158d142 | -9.37469 | -37.26534 | 2024-11-14 03:49:00 | NOAA-20 | SANTANA DO IPANEMA | ALAGOAS | Brasil | 2708006 | 27 | 33 | nan | nan | nan | Caatinga | 0.8 |
| fab563ce-149c-3da8-abb4-6e73eb9f7c01 | -10.25318 | -36.46187 | 2024-11-14 03:49:00 | NOAA-20 | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| 43dd94fe-5eee-3cbe-aa22-465aaa216762 | -9.73238 | -37.45429 | 2024-11-14 03:49:00 | NOAA-20 | PÃO DE AÇÚCAR | ALAGOAS | Brasil | 2706406 | 27 | 33 | nan | nan | nan | Caatinga | 1.2 |


[Clique aqui para ver as próximas entradas](README22.md)
