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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1e1becb1-429c-3954-801c-eb50686ce393 | -3.29 | -50.4306 | 2024-10-04 00:45:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 86.3 |
| 250dff00-099d-3fea-a150-7ac2121059ca | -3.3083 | -50.4719 | 2024-10-04 00:45:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 74.5 |
| 9087c566-691f-3c6e-bb47-f97e3602ff21 | -3.3084 | -50.451 | 2024-10-04 00:45:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 158.3 |
| 81f4be03-d9d6-3423-849a-0891d3ee9215 | -3.3085 | -50.43 | 2024-10-04 00:45:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 59.0 |
| 1246942b-6448-343d-ab92-94a051bb1652 | -3.7993 | -51.1726 | 2024-10-04 00:45:27 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0b2e49ab-5533-3a89-9154-3f01e6f6b559 | -3.8011 | -51.180698 | 2024-10-04 00:45:27 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9dfae315-9cf7-3036-b523-b28892bcda70 | -2.7265 | -46.795399 | 2024-10-04 00:45:28 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2d117815-bde1-3b1d-b874-0fafda3a7254 | -4.0763 | -48.4902 | 2024-10-04 00:45:29 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 82.1 |
| c43cea9d-49eb-3362-bee0-02ea5060a26f | -4.0949 | -48.4894 | 2024-10-04 00:45:29 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 78.0 |
| db71e796-ab5c-346f-81bb-d5d7b10ad6db | -3.7849 | -51.655399 | 2024-10-04 00:45:29 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 87124fdf-51e7-3d42-8150-a7f1154a22f2 | -3.7868 | -51.663898 | 2024-10-04 00:45:29 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0d0fc0eb-5f6c-33ee-9b50-1f8de02d8c8b | -2.619 | -46.910301 | 2024-10-04 00:45:30 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ae51de02-0e81-367a-873a-8a6e675a57f6 | -2.6206 | -46.9174 | 2024-10-04 00:45:30 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f9f0de11-6e69-3516-b9d8-db211245e7a2 | -3.8197 | -52.175201 | 2024-10-04 00:45:30 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d2db2acf-b4ea-3dc3-819e-efff470b04af | -3.8217 | -52.184299 | 2024-10-04 00:45:30 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| eda95a49-07b6-3522-8ad2-306fba261c16 | -4.4657 | -42.8877 | 2024-10-04 00:45:31 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 74.8 |
| 502e2cfc-5ca7-3dcf-853e-92fc181379c0 | -4.5375 | -43.304 | 2024-10-04 00:45:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 142.5 |
| e12fea75-bfd1-3694-8d8c-d9f87a6315f4 | -3.3912 | -50.597401 | 2024-10-04 00:45:31 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f88d8cef-51d6-3e40-a285-a44f0e517abc | -3.4871 | -50.793201 | 2024-10-04 00:45:31 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| aa55d774-338e-3790-a995-ea0cf66a3053 | -3.4889 | -50.800999 | 2024-10-04 00:45:31 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fe1d7504-cb54-385d-ab73-2afb52462547 | -3.4906 | -50.808701 | 2024-10-04 00:45:31 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c4c6bc0b-9c4c-3545-b2c8-f03ba00efe1a | -3.4808 | -50.810799 | 2024-10-04 00:45:31 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ce6352cd-ba4a-3982-9051-c569699b643b | -3.8158 | -52.340401 | 2024-10-04 00:45:31 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1e20e494-ad70-3b52-b2a7-6855e5b15695 | -4.5949 | -45.7436 | 2024-10-04 00:45:32 | GOES-16 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 29.6 |
| 38216a4d-4c0c-3fb9-b9e0-d5dfd43e2ebc | -4.6684 | -45.8961 | 2024-10-04 00:45:32 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 52.7 |
| 3301b355-b8e7-3d27-a585-c8543264a362 | -4.6686 | -45.8738 | 2024-10-04 00:45:32 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 117.3 |
| 0898466e-cffa-3875-bb8b-79ccc4f5799a | -4.687 | -45.8951 | 2024-10-04 00:45:32 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 67.7 |
| 4599c21d-2d71-3fbe-aeed-415f9be69a8a | -4.6872 | -45.8727 | 2024-10-04 00:45:32 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 196.3 |
| b5c9a40e-df3b-346c-b3eb-0c9240f9337f | -4.6873 | -45.8504 | 2024-10-04 00:45:32 | GOES-16 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 31.1 |
| 2d0f9aee-6dd1-3b53-9933-c28cc85854db | -3.6872 | -52.043201 | 2024-10-04 00:45:32 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 63970426-4000-3f64-b7bc-9a244101778c | -3.6893 | -52.0522 | 2024-10-04 00:45:32 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a3a43f9a-8497-3680-adc8-5bc252e713d1 | -3.2931 | -50.437401 | 2024-10-04 00:45:32 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 91b5ecbf-bdc3-3429-b708-b25032d7a381 | -3.2948 | -50.444901 | 2024-10-04 00:45:32 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c8984104-e25c-3fee-8a53-f4665a0a6dda | -3.2965 | -50.4524 | 2024-10-04 00:45:32 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7dc7e881-814b-36df-9a57-e7d04adade59 | -3.2982 | -50.4599 | 2024-10-04 00:45:32 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a5130e1f-e9ad-3fc6-8d5a-bbf96b25edc1 | -3.2833 | -50.439602 | 2024-10-04 00:45:33 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cc21a871-3c7e-3e8e-baeb-f85933150ce0 | -3.285 | -50.446999 | 2024-10-04 00:45:33 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bd6d5871-44b7-3c22-a80f-d7d03e411a22 | -3.2867 | -50.454498 | 2024-10-04 00:45:33 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dd94da29-70bf-3792-9996-f9e7582b7a8b | -3.2884 | -50.462002 | 2024-10-04 00:45:33 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6f2624b5-f75b-3997-8ee9-d5d914b39e67 | -3.2451 | -50.362202 | 2024-10-04 00:45:33 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5e2656d5-c67d-3ed1-8444-0e790296968c | -3.2336 | -50.3568 | 2024-10-04 00:45:33 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ad9d09f9-4599-3233-a73d-94600b4c9df2 | -3.2353 | -50.3643 | 2024-10-04 00:45:33 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| df494cd8-e709-38c1-8ecb-aaa4035f5f01 | -3.2369 | -50.3717 | 2024-10-04 00:45:33 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8defe20a-8241-3322-ae8d-7f3a7d24c186 | -3.2386 | -50.379101 | 2024-10-04 00:45:33 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4610391d-58bf-3eee-ba85-0bb40d283389 | -3.2932 | -50.7551 | 2024-10-04 00:45:34 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d20adc8c-2eeb-3ec4-8b81-97e2e2818499 | -3.2817 | -50.749599 | 2024-10-04 00:45:34 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1c6c61b9-a3be-388c-9040-41781aa4a9f7 | -3.2834 | -50.757301 | 2024-10-04 00:45:34 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 05b81d0b-fc0b-3424-ae0c-d49916e744da | -3.2852 | -50.764999 | 2024-10-04 00:45:34 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 271b9242-d987-3b46-a798-78f6cab7bc44 | -3.1034 | -50.463699 | 2024-10-04 00:45:36 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4cb1d30c-30f6-3034-8fbf-18c6576373d9 | -3.1051 | -50.471199 | 2024-10-04 00:45:36 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b0c02011-5bd9-3836-bd7a-9bb1f5d28fb2 | -3.1068 | -50.4786 | 2024-10-04 00:45:36 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9f243259-b1c1-33bf-81aa-132bf7419cca | -5.5033 | -48.8046 | 2024-10-04 00:45:37 | GOES-16 | SÃO DOMINGOS DO ARAGUAIA | PARÁ | Brasil | 1507151 | 15 | 33 | nan | nan | nan | Amazônia | 83.5 |
| ed9675c7-1673-3b55-b0ff-19ad80fd0d81 | -2.3888 | -47.656399 | 2024-10-04 00:45:37 | METOP-C | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 18a5ec94-4fbe-311e-86cb-9f8ede25f96a | -5.8214 | -44.1426 | 2024-10-04 00:45:39 | GOES-16 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 61.5 |
| d1931360-08d3-3ad6-b6fa-5a432fb0d39f | -5.8216 | -44.1196 | 2024-10-04 00:45:39 | GOES-16 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 74.8 |
| 9d7647f2-6f36-3cfd-9c6d-536fa45493ab | -2.8913 | -50.707901 | 2024-10-04 00:45:40 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2e3fa630-11c2-3890-ad79-bb153212cee0 | -2.893 | -50.7155 | 2024-10-04 00:45:40 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 85f64769-6b56-3143-abf9-cc2b81a39f22 | -2.8797 | -50.702499 | 2024-10-04 00:45:40 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| babd251b-414f-32d0-9d95-130e9db19b8a | -2.8814 | -50.710098 | 2024-10-04 00:45:40 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 662752b5-1ad1-3dcb-8ee1-8cafc7be6d77 | -6.2524 | -44.132 | 2024-10-04 00:45:41 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 75.3 |
| 7800dbee-90d3-3c13-b964-63d6486bb22d | -1.7286 | -47.118099 | 2024-10-04 00:45:45 | METOP-C | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| df4b460e-9f51-3748-868f-a37676d88d1e | -1.7302 | -47.125198 | 2024-10-04 00:45:45 | METOP-C | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6e230be2-4be0-3aa4-b2f1-739a781ecd8a | -7.8539 | -45.3611 | 2024-10-04 00:45:50 | GOES-16 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 82.4 |
| 0f21b703-eb82-34ff-a114-8670e4137df1 | -7.8541 | -45.3384 | 2024-10-04 00:45:50 | GOES-16 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 76.4 |
| c7ab6c92-8f77-3384-89f1-0e2bf451367b | -1.4901 | -47.336102 | 2024-10-04 00:45:50 | METOP-C | BONITO | PARÁ | Brasil | 1501600 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 92c4b5ed-d4b6-3e1b-aebc-59f57d4ebac2 | -1.4917 | -47.343201 | 2024-10-04 00:45:50 | METOP-C | BONITO | PARÁ | Brasil | 1501600 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 08b82f85-0c28-3423-ac55-44ed7078f645 | -8.1244 | -44.7871 | 2024-10-04 00:45:52 | GOES-16 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 60.2 |
| 071c9639-7dab-31ce-8ae3-67dc01a979c1 | -2.1313 | -50.987999 | 2024-10-04 00:45:53 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e5497408-1303-3d87-8bec-ff13e01fcb83 | -8.6448 | -50.0518 | 2024-10-04 00:45:55 | GOES-16 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 100.1 |
| 1875ef30-db4d-30fb-8ea2-b3d7db7f0952 | -8.6636 | -50.0501 | 2024-10-04 00:45:55 | GOES-16 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 79.9 |
| 56eaaad1-1cb8-37d3-a8f8-854fea52f13f | -8.6492 | -66.621 | 2024-10-04 00:45:56 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 56.3 |
| c2dd63bb-b9db-3098-8974-f5fd292f7b4b | -8.6676 | -66.6391 | 2024-10-04 00:45:56 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 53.7 |
| 843ab622-07ca-304e-9257-5d7901e233d1 | -8.6677 | -66.6205 | 2024-10-04 00:45:56 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 58.0 |
| df1603ba-4489-30ec-ad78-3a4be66edea8 | -9.1158 | -51.5315 | 2024-10-04 00:45:58 | GOES-16 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 53.5 |
| 54342125-094b-3655-bbfc-e3783c21e793 | -9.55 | -64.2179 | 2024-10-04 00:46:01 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 52.4 |
| 358220ea-f062-3ca1-a294-9322be0bf6e8 | -9.5686 | -64.2171 | 2024-10-04 00:46:01 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 83.8 |
| 0baa3274-7df8-363d-94bc-26f05bd5ad21 | -9.5687 | -64.1983 | 2024-10-04 00:46:01 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 48.3 |
| 8cbdca4c-5914-3212-aad6-f20d8a88898b | -9.8349 | -46.7726 | 2024-10-04 00:46:01 | GOES-16 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 129.9 |
| 1c8b7b61-84bb-36ac-ab27-672fa5e407a5 | -9.8353 | -46.7502 | 2024-10-04 00:46:01 | GOES-16 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 124.9 |
| 15dfb7aa-9f4b-3a54-b3ef-f3eaad859f6c | -9.8539 | -46.7704 | 2024-10-04 00:46:01 | GOES-16 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 70.7 |
| 1d333e6b-aa89-39c7-bfd7-323aa321c1b4 | -9.9747 | -64.7661 | 2024-10-04 00:46:03 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 52.5 |
| 3a85a02f-af97-3d15-a0b1-95970843ad0e | -10.4424 | -50.7336 | 2024-10-04 00:46:05 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 96.1 |
| 02da45c5-daa0-33d9-ae40-240f45d5b6be | -10.4613 | -50.7317 | 2024-10-04 00:46:05 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 93.1 |
| a50ce7b5-25e6-33a0-8bd5-37ae72aaa3cc | -11.0532 | -46.5344 | 2024-10-04 00:46:08 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 77.9 |
| 85041b86-f3b7-30d6-9cc7-284e1319cd1c | -11.0536 | -46.5118 | 2024-10-04 00:46:08 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 104.4 |
| 652bf71a-1805-33ef-8f18-02c38af8da42 | -11.5238 | -65.0615 | 2024-10-04 00:46:12 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 60.7 |
| f1cef680-f1bd-3d8b-ae8d-ce1ab3990716 | -11.5425 | -65.0607 | 2024-10-04 00:46:12 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 69.4 |
| f2c79380-80dd-3866-ac26-3e65766cf8bb | -11.5991 | -65.0204 | 2024-10-04 00:46:12 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 61.9 |
| 176b8159-cdba-3611-85d4-ff7b9d81de75 | -11.5992 | -65.0015 | 2024-10-04 00:46:12 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 81.5 |
| 15ec9a8d-1a79-382c-8c70-8e9e0410ebb2 | -11.618 | -65.0007 | 2024-10-04 00:46:12 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 66.0 |
| 2f5e34b2-7c59-3198-9e11-002f3c578c2f | -11.6181 | -64.9818 | 2024-10-04 00:46:12 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 90.6 |
| 62542856-ac49-30a9-b359-77df21e8b2c4 | -11.6369 | -64.981 | 2024-10-04 00:46:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 89.8 |
| bda269fc-df34-37a1-bb25-a2ae83bba301 | -11.6932 | -64.9785 | 2024-10-04 00:46:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 127.7 |
| ab6291cd-7fb6-3351-bd20-620001d0e781 | -11.8052 | -56.6024 | 2024-10-04 00:46:13 | GOES-16 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 63.4 |
| e7f82a49-7703-374f-9658-7b9cd74b5877 | -11.8242 | -56.6009 | 2024-10-04 00:46:13 | GOES-16 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 98.8 |
| 20de2bfb-0222-3759-ae48-47407eb73551 | -11.8244 | -56.5808 | 2024-10-04 00:46:13 | GOES-16 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 62.1 |
| c5707855-fac6-3d24-aaca-4575595406a1 | -12.5898 | -53.1359 | 2024-10-04 00:46:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 110.6 |
| 78b0bf08-0f21-3a10-9b24-399ecfd62f66 | -12.5901 | -53.115 | 2024-10-04 00:46:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 151.0 |
| 2190d8ce-1533-3be0-b4b1-d88673f82a57 | -12.8049 | -62.497 | 2024-10-04 00:46:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 87.2 |
| e55cf830-98cb-39d9-8ecf-06905a38d765 | -12.8051 | -62.4777 | 2024-10-04 00:46:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 136.0 |


[Clique aqui para ver as próximas entradas](README19.md)
