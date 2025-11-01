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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 62b5cd70-d4c0-3d26-9a2d-4410713af9c0 | -4.91828 | -45.59236 | 2025-11-01 03:49:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 1e2c93f9-4b85-3ddf-b682-662ff3c06d7f | -4.33674 | -44.53376 | 2025-11-01 03:49:00 | NOAA-20 | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c1683c9a-e4e0-3607-87e3-ecb99b9ffb1c | -5.18632 | -44.91129 | 2025-11-01 03:49:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f6963151-ddc6-3895-839e-fe22e66bcf4e | -5.88472 | -44.52593 | 2025-11-01 03:49:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 7244c4b3-6255-3e5e-ac91-c1884e44c708 | -10.40757 | -44.33403 | 2025-11-01 03:49:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 88e17c96-3d0f-33b7-b9e1-dd5ac8a8fe68 | -5.83385 | -44.0666 | 2025-11-01 03:49:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 23.5 |
| 75700053-b936-3c44-92c9-d85ad3e89032 | -13.58595 | -42.90002 | 2025-11-01 03:49:00 | NOAA-20 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 2cd3aa72-9539-310d-83e2-4f8a66362685 | -5.3546 | -45.03371 | 2025-11-01 03:49:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d7b74135-2c7c-3c22-afed-b150da4efa53 | -5.08577 | -45.42621 | 2025-11-01 03:49:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bc2408dc-bb9b-32b3-91f8-86753b472838 | -11.43565 | -45.14468 | 2025-11-01 03:49:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 09f9c3b7-7ca7-3c22-ae00-87d35aa6a6b9 | -13.52804 | -47.11024 | 2025-11-01 03:49:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 58e0227b-3547-3ec0-aea7-0f37b89225a2 | -14.02581 | -43.26486 | 2025-11-01 03:49:00 | NOAA-20 | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 98b860af-9200-31d2-b306-b4d9b17b8112 | -6.32575 | -43.63035 | 2025-11-01 03:49:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 035de2a1-1c5e-300c-8b25-1793225e1fb1 | -6.46624 | -43.30458 | 2025-11-01 03:49:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 157120f7-c0e3-34dc-add8-6f052ab3dd11 | -5.46366 | -44.88859 | 2025-11-01 03:49:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 44521350-23fb-3a71-aae0-eeb2e2958863 | -12.51246 | -43.81907 | 2025-11-01 03:49:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a0cdd6ff-3e66-36dc-b1c0-7d018caebfcb | -5.35246 | -45.03271 | 2025-11-01 03:49:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 33921c3b-3a5b-321a-9170-87f86069664c | -4.74874 | -44.4672 | 2025-11-01 03:49:00 | NOAA-20 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 853bb6dc-d7ba-383e-80fb-7d4609a00248 | -12.3024 | -48.05133 | 2025-11-01 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 81748005-d234-3435-b0e9-e1bcf5917867 | -4.60617 | -44.4291 | 2025-11-01 03:49:00 | NOAA-20 | LIMA CAMPOS | MARANHÃO | Brasil | 2106003 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f9901e8a-e170-3f9c-a59a-87d4c0ea0c43 | -5.53681 | -44.52632 | 2025-11-01 03:49:00 | NOAA-20 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 52416401-9c11-3ec3-8871-92f794afee35 | -4.82922 | -45.7874 | 2025-11-01 03:49:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f238ed8a-9fcc-3dfa-a7a4-b1d9d6d6b9dc | -5.47216 | -44.32034 | 2025-11-01 03:49:00 | NOAA-20 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0eb97e0a-ee9f-3339-b8d8-a7c11aa57a72 | -3.88424 | -47.18385 | 2025-11-01 03:49:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 67148f48-a2c6-3bf3-96c4-a5168f62bdc6 | -4.9177 | -45.59577 | 2025-11-01 03:49:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 11.4 |
| a33d2a61-b8aa-31e3-ad07-6a9db97bec1e | -4.79709 | -46.47646 | 2025-11-01 03:49:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| abfa6f4d-b27c-363a-94c8-51e49608d5e8 | -4.09009 | -44.03954 | 2025-11-01 03:49:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0e292ff6-2fb6-3e65-915d-811436584b98 | -4.29314 | -46.26145 | 2025-11-01 03:49:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6f0d7b47-b2b6-3e42-8064-b3cdbe23af7d | -5.25949 | -44.31466 | 2025-11-01 03:49:00 | NOAA-20 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 42fa6cd4-46c1-3548-88cd-80b78890d1e1 | -14.68983 | -42.81591 | 2025-11-01 03:49:00 | NOAA-20 | URANDI | BAHIA | Brasil | 2932606 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 813bde1b-887f-3f2b-ac52-6795a419efd4 | -11.9278 | -38.32736 | 2025-11-01 03:49:00 | NOAA-20 | INHAMBUPE | BAHIA | Brasil | 2913705 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 06ce276e-0443-343f-b5a1-03448305c6ee | -5.2992 | -45.34831 | 2025-11-01 03:49:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c2cbc9c8-c210-350a-8a31-fa8dc9a9154d | -4.658 | -41.96385 | 2025-11-01 03:49:00 | NOAA-20 | COCAL DE TELHA | PIAUÍ | Brasil | 2202711 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| b33257c3-25d0-3aed-9e13-af9b4d36f30b | -5.26588 | -44.72112 | 2025-11-01 03:49:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6dd01e24-7d88-3422-b56b-693046e7db18 | -13.35888 | -43.09035 | 2025-11-01 03:49:00 | NOAA-20 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 9e0f5149-5e9f-3e01-9936-ccaf196af070 | -11.44657 | -48.18413 | 2025-11-01 03:49:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f076b3b1-adbb-3374-ae6e-e3f91ec499c8 | -5.48531 | -43.0949 | 2025-11-01 03:49:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6261ec62-9906-362f-b7c6-1b5455659682 | -12.29683 | -48.0504 | 2025-11-01 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| e88d6e8c-1acf-35db-95ed-128992a10aba | -13.4827 | -46.59982 | 2025-11-01 03:49:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| de96e0b2-3b32-339e-adba-c7da9266da6e | -13.3335 | -43.18806 | 2025-11-01 03:49:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 27296cf4-d478-363f-9742-199f4b6e407e | -11.27734 | -41.73769 | 2025-11-01 03:49:00 | NOAA-20 | JOÃO DOURADO | BAHIA | Brasil | 2918357 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 5eb27101-f966-30f9-b5dd-80ce3d25a653 | -11.39013 | -43.20131 | 2025-11-01 03:49:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| b980950c-e7a3-3461-92bf-bc8dfb875c1d | -5.46315 | -44.8916 | 2025-11-01 03:49:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c30327e2-4fa2-3a71-a6d9-fcd060e3bedb | -11.07388 | -45.19936 | 2025-11-01 03:49:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b0aefe78-21cd-3524-8dbe-84a05e6ac22b | -5.08518 | -45.42958 | 2025-11-01 03:49:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6c2b9411-599c-316f-9113-201e559d4be1 | -5.23677 | -45.05993 | 2025-11-01 03:49:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 793906e9-8dbb-384a-93fc-7baf95cf77d6 | -13.38801 | -43.68359 | 2025-11-01 03:49:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d1bc0ad8-65ad-348b-8487-3076aa607b0e | -10.89917 | -47.50781 | 2025-11-01 03:49:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 12868005-f78f-359e-85c9-fa9d05ebbc5f | -4.44817 | -44.20914 | 2025-11-01 03:49:00 | NOAA-20 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| fda08a6c-90bb-3251-9917-fe844b50b7e1 | -11.83169 | -46.01404 | 2025-11-01 03:49:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 10.7 |
| e0631e38-0a0a-316f-b8b1-ccee73cc8cc5 | -15.73378 | -43.16061 | 2025-11-01 03:49:00 | NOAA-20 | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Caatinga | 1.0 |
| bfd5e91f-0f9f-3df3-8ae3-1347056db33f | -5.48163 | -43.08955 | 2025-11-01 03:49:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bb587145-b1a5-32a8-a9dc-33c103406289 | -13.29346 | -41.92965 | 2025-11-01 03:49:00 | NOAA-20 | RIO DO PIRES | BAHIA | Brasil | 2926905 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| bad1fcac-51a5-3ce1-b74f-6509e51a4180 | -7.39602 | -38.46308 | 2025-11-01 03:49:00 | NOAA-20 | CONCEIÇÃO | PARAÍBA | Brasil | 2504405 | 25 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 1d3730ae-ae4d-3e08-8a4d-42b9b297cf3b | -5.53546 | -44.5255 | 2025-11-01 03:49:00 | NOAA-20 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e32664c7-376d-3ac9-9f39-9d2ff339801d | -6.55406 | -40.18792 | 2025-11-01 03:49:00 | NOAA-20 | AIUABA | CEARÁ | Brasil | 2300408 | 23 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 904b9744-4a06-3cad-9c6a-4801a36d90c3 | -5.21224 | -45.83817 | 2025-11-01 03:49:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 50543bb0-d45e-35f3-9a68-a9bed4d08c47 | -13.00546 | -43.85646 | 2025-11-01 03:49:00 | NOAA-20 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1b54606d-bff8-3cd7-a4fa-389bf4cc6c79 | -4.81057 | -45.75798 | 2025-11-01 03:49:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3ee4afd5-ebab-3ce6-a354-d1a1f991a704 | -7.02975 | -37.24562 | 2025-11-01 03:49:00 | NOAA-20 | PATOS | PARAÍBA | Brasil | 2510808 | 25 | 33 | nan | nan | nan | Caatinga | 9.8 |
| 8c521f21-98cf-39d6-8344-35b73e9aeffd | -5.11362 | -43.39493 | 2025-11-01 03:49:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5c63e6eb-a4e8-34aa-9296-f74c6efe15aa | -5.12821 | -43.39259 | 2025-11-01 03:49:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3200b04e-566f-3dc9-a1d2-4ca0be3b9bca | -13.63388 | -43.17533 | 2025-11-01 03:49:00 | NOAA-20 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 47dc6fa2-78e1-3238-974c-6623c690a9d3 | -5.11902 | -43.39099 | 2025-11-01 03:49:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a1ef67fe-df14-33d8-b9fc-7968d90e281c | -13.51936 | -47.11372 | 2025-11-01 03:49:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d2eefa7a-9cc3-3237-bd79-c09ae971cf6c | -4.8033 | -45.87172 | 2025-11-01 03:49:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bd48c97c-f955-326c-b169-61c229ece46c | -5.79563 | -43.97548 | 2025-11-01 03:49:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e93b40fa-c865-3913-803d-a92878883c33 | -4.77109 | -46.50248 | 2025-11-01 03:49:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f41deca2-8669-311e-8b61-dd45ca6c5c09 | -13.37529 | -43.58948 | 2025-11-01 03:49:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d56c74fa-cda7-393e-9750-803355a7d58b | -6.45976 | -43.56184 | 2025-11-01 03:49:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 21c0a247-76ec-3700-aa07-f44741fbb03a | -6.32123 | -43.6292 | 2025-11-01 03:49:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| ce23c1eb-d93c-3fb5-93a2-9db2720bdaad | -13.35495 | -43.08957 | 2025-11-01 03:49:00 | NOAA-20 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 0cb5c965-d1a3-320c-b1c1-dc689f6c486a | -5.22097 | -44.80165 | 2025-11-01 03:49:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 99c7080c-c653-3b65-beb8-6c6a6076d6b8 | -5.59084 | -45.03872 | 2025-11-01 03:49:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| aeab3205-0f64-3a5d-9646-d18fb4b31b84 | -3.52517 | -47.5573 | 2025-11-01 03:49:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f1a2714f-087b-3f96-aeb7-3f3b821d49e6 | -5.21807 | -43.7551 | 2025-11-01 03:49:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3c2cc45b-7eb6-3369-9c87-0550ad48b0d4 | -4.44481 | -46.04285 | 2025-11-01 03:49:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4f156843-6a7e-3fab-849c-2a6e995bcee4 | -5.83391 | -44.06919 | 2025-11-01 03:49:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 4ca8d781-cf25-3654-9bae-d77a8668c15d | -5.83062 | -44.34266 | 2025-11-01 03:49:00 | NOAA-20 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 17cd80e6-d772-3f2d-923c-7fa15de4d0d4 | -6.03831 | -40.25032 | 2025-11-01 03:49:00 | NOAA-20 | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| ab5ddd05-f55c-3f03-a644-e3b026564b6d | -13.03051 | -48.2593 | 2025-11-01 03:49:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7f82899b-158a-37a7-b187-b5adda1a05b0 | -10.79566 | -44.43659 | 2025-11-01 03:49:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c3f6dd46-13bd-337b-a1c6-a704d3034484 | -6.13469 | -45.93959 | 2025-11-01 03:49:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2930969e-35c1-32d1-9eff-172bdfd50f14 | -6.12868 | -45.94226 | 2025-11-01 03:49:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 64ef7d47-3d94-3522-835f-a40c6401ea08 | -13.02496 | -48.2582 | 2025-11-01 03:49:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 74a3d049-348c-3397-a441-43440ab690e0 | -5.451 | -45.40583 | 2025-11-01 03:49:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 534caf0d-3a09-3fdb-931a-91685d8964c8 | -5.35406 | -45.03675 | 2025-11-01 03:49:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9f437829-1af1-39d5-a724-239429baf535 | -5.8291 | -44.06576 | 2025-11-01 03:49:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6820c681-33d8-3cca-bcf9-2dac13b68d25 | -5.19013 | -43.41814 | 2025-11-01 03:49:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 660786d6-35cc-36a1-9958-9e032baf22ce | -13.29267 | -41.93419 | 2025-11-01 03:49:00 | NOAA-20 | RIO DO PIRES | BAHIA | Brasil | 2926905 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 1197a12c-260e-3e55-b09f-ecb6c98f23fd | -5.22126 | -46.1727 | 2025-11-01 03:49:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 613e1582-58e2-3571-82f3-6d50297332c1 | -7.02644 | -37.2451 | 2025-11-01 03:49:00 | NOAA-20 | PATOS | PARAÍBA | Brasil | 2510808 | 25 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 94b27ec6-09e8-3625-aef5-1059e545bf95 | -15.52398 | -41.67363 | 2025-11-01 03:49:00 | NOAA-20 | ÁGUAS VERMELHAS | MINAS GERAIS | Brasil | 3101003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 8c43aacc-9d53-3597-841c-b6293d5ae9d9 | -4.67799 | -45.80613 | 2025-11-01 03:49:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ec6013f0-732c-32c3-8b0c-d25df55f83e4 | -11.7307 | -47.46971 | 2025-11-01 03:49:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 7f8c4b06-e67d-3a5c-9cb5-fe068c9c10ad | -15.60845 | -41.36979 | 2025-11-01 03:49:00 | NOAA-20 | ÁGUAS VERMELHAS | MINAS GERAIS | Brasil | 3101003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| beabd423-ad5e-3b23-a3b2-1fefe134da85 | -4.57002 | -45.8769 | 2025-11-01 03:49:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4cd24ffe-79bb-3c52-88de-89ea6283b0c8 | -13.71353 | -43.78284 | 2025-11-01 03:49:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cafa0339-2f94-386c-8129-cee8f454aa70 | -5.86016 | -43.99706 | 2025-11-01 03:49:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 92ef8714-3afb-3e7c-bd65-a64d913fc32d | -15.613 | -42.39278 | 2025-11-01 03:49:00 | NOAA-20 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |


[Clique aqui para ver as próximas entradas](README15.md)
