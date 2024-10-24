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

## Dados Diários - Página 46

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| da543310-347a-3398-8435-48b5d73d414f | -11.60626 | -48.54836 | 2024-10-24 04:34:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| af0d0d40-14f7-37a4-ae02-0f96cb71da14 | -11.60349 | -48.54432 | 2024-10-24 04:34:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 79fd36ce-b2df-3362-824c-4e7e4c38660a | -11.60337 | -48.45776 | 2024-10-24 04:34:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| d7c05903-656e-3d39-a2db-7939b2cd4e1c | -11.60295 | -48.54784 | 2024-10-24 04:34:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0db877f7-ca66-3759-91ae-cdf90a4ab35b | -11.60246 | -48.59455 | 2024-10-24 04:34:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c63f68b1-52f1-350e-adbd-b5591d6a9669 | -11.59958 | -48.50404 | 2024-10-24 04:34:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f23fecf9-c018-3a39-96b6-c532bcf04d15 | -11.59915 | -48.59402 | 2024-10-24 04:34:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c3b9e79a-ff05-3ae3-92e0-d18e5c95ce5d | -11.59909 | -48.55082 | 2024-10-24 04:34:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 8e7c4193-0f73-3bdd-b136-ecd620379585 | -11.5986 | -48.59753 | 2024-10-24 04:34:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 152a8272-1bf1-3251-a1cf-62ce60f5b5b4 | -11.59854 | -48.55434 | 2024-10-24 04:34:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| af37f664-9ac3-33db-82e9-0793ab210399 | -11.598 | -48.55785 | 2024-10-24 04:34:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 00c7bd87-29cd-31da-9926-38445a8760d9 | -11.59584 | -48.59349 | 2024-10-24 04:34:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4d52d69e-4b55-380f-aec6-f29ad3fee649 | -11.59578 | -48.5503 | 2024-10-24 04:34:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| d474f2ef-557a-350a-8937-d57578521faf | -11.59572 | -48.50704 | 2024-10-24 04:34:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 04a798c5-b2d1-3f9e-8719-9de299309be7 | -11.59529 | -48.597 | 2024-10-24 04:34:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 56fc2084-cb3f-3f8b-9cdc-d11c5f7ddb28 | -11.59524 | -48.55381 | 2024-10-24 04:34:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 165b73c8-a955-373f-8d93-831196a7c2a4 | -11.59469 | -48.55732 | 2024-10-24 04:34:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| a9ed060b-a9a9-35e5-9f67-e01fb958ef98 | -11.57317 | -48.54307 | 2024-10-24 04:34:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 7e19c074-35ea-346a-9eaa-c3b6d824e10e | -11.57168 | -48.66156 | 2024-10-24 04:34:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c8821ca8-e060-3054-8e8d-1835787c4b3e | -11.55891 | -48.59119 | 2024-10-24 04:34:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 676b5596-f705-337b-90c7-41cacf0176c7 | -11.53514 | -48.54779 | 2024-10-24 04:34:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 471fd67c-aae1-30ca-9267-92b87524a16b | -11.79678 | -47.88707 | 2024-10-24 04:34:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 86bda9ed-09d2-35a9-9772-245d43442f66 | -11.79344 | -47.88654 | 2024-10-24 04:34:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d4d28ef0-fc2a-39db-9536-0a3ae0f1c15d | -11.79289 | -47.89013 | 2024-10-24 04:34:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4f822b84-fcc8-3dbb-a569-d1b14ae9923e | -11.79009 | -47.886 | 2024-10-24 04:34:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 086a6af6-ce92-3a2c-8f0d-90634c4b3c7f | -11.78954 | -47.88959 | 2024-10-24 04:34:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e624da24-1a53-3404-bb6f-e939ecaa0544 | -11.7862 | -47.88906 | 2024-10-24 04:34:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ebf8a160-ac28-3dd1-95d7-e2498330c115 | -11.5752 | -48.06897 | 2024-10-24 04:34:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8937eef2-f202-3042-9d48-cd61e3675c8c | -11.57132 | -48.07201 | 2024-10-24 04:34:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 50e53130-4203-3d36-a82e-5709b2ad2375 | -11.39575 | -47.75479 | 2024-10-24 04:34:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ce8ccc18-8206-3c1d-885e-684cc2c292b6 | -11.24497 | -48.0715 | 2024-10-24 04:34:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 46f4b6af-b6d8-3d60-939c-d25e9a4a87b8 | -11.17608 | -47.76886 | 2024-10-24 04:34:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| aed93582-37de-34ac-86ac-41dca327f8c8 | -11.1461 | -48.09595 | 2024-10-24 04:34:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 4113cdb2-664c-3596-8d7d-f7ec91860878 | -11.10488 | -47.70231 | 2024-10-24 04:34:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b49665da-2f99-31dc-981b-2ccd6c4fcffa | -11.10154 | -47.70178 | 2024-10-24 04:34:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c468d8b2-a9b4-3557-b15c-12409bb66dba | -11.07806 | -47.91806 | 2024-10-24 04:34:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3273d0c5-fa84-3031-a971-65f5d6666e0b | -11.07635 | -47.90688 | 2024-10-24 04:34:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 50795198-3b0f-3599-9c63-6a62a84b049a | -11.07581 | -47.91046 | 2024-10-24 04:34:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| defcb970-53d1-3dd1-99a7-38a863433182 | -12.95883 | -48.64202 | 2024-10-24 04:34:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9d9528a2-9fd5-3e07-a479-43b9ee989bbd | -12.92094 | -48.51264 | 2024-10-24 04:34:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e4fbd2f9-90e9-307a-86b9-94dbe510cbd8 | -12.88999 | -48.51472 | 2024-10-24 04:34:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| d1d34b7c-8570-3d3c-b44b-77555dcbb3b9 | -12.88944 | -48.51827 | 2024-10-24 04:34:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 75dc6b19-62ff-308c-ae56-ca015c64dff8 | -12.8889 | -48.52182 | 2024-10-24 04:34:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 6358eae8-33d2-32f0-9cc8-9e81d6ad255f | -12.88667 | -48.51419 | 2024-10-24 04:34:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 11089df6-5660-3969-9ef7-0317db3a5038 | -12.88612 | -48.51773 | 2024-10-24 04:34:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| aa722798-930a-31ba-a33e-12ec1f47f5da | -12.83531 | -48.56058 | 2024-10-24 04:34:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| eec06593-b367-3a5e-8371-06977e80803f | -12.83258 | -48.57838 | 2024-10-24 04:34:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| fc2a2777-2f90-322f-8fac-3ec80efe500b | -12.7698 | -49.20141 | 2024-10-24 04:34:00 | NOAA-21 | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0961cee8-fe86-370c-a370-4367fc0f6a33 | -12.66354 | -49.48705 | 2024-10-24 04:34:00 | NOAA-21 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 95bd6fba-b38b-392e-ba70-8c3f70bbe324 | -12.64427 | -49.4803 | 2024-10-24 04:34:00 | NOAA-21 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| dde83862-28fe-3ff3-8eb8-ddb246b4f445 | -12.62059 | -49.48005 | 2024-10-24 04:34:00 | NOAA-21 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 043b89c0-28f1-3063-909b-f35ad74e3b4e | -12.62004 | -49.48357 | 2024-10-24 04:34:00 | NOAA-21 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 86a26f82-76c3-3b46-a72b-2d369ff577c0 | -12.27066 | -49.45512 | 2024-10-24 04:34:00 | NOAA-21 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 09d7fb3f-e405-38d2-ab98-2df7876371f3 | -12.62629 | -48.39591 | 2024-10-24 04:34:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| adfabdf3-f326-3629-9e39-5a6ae31e22b9 | -12.60979 | -48.52452 | 2024-10-24 04:34:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ad1f7dae-f34c-3634-90d0-6397fc8409ce | -12.60647 | -48.524 | 2024-10-24 04:34:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1694f8f4-bef7-3402-8589-57c283a64496 | -12.59528 | -48.77224 | 2024-10-24 04:34:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a6fbb696-9821-3bd1-85cd-04b81d8b5125 | -12.59474 | -48.77576 | 2024-10-24 04:34:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 24f43d8f-38e4-3429-a8da-d533382520e9 | -12.59197 | -48.77171 | 2024-10-24 04:34:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 51600b4b-1105-3fdf-b6aa-b0a1c1182db8 | -12.59143 | -48.77523 | 2024-10-24 04:34:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 92c22800-b31e-35d3-84b6-6590446173e2 | -6.48914 | -48.74031 | 2024-10-24 04:34:00 | NOAA-21 | PIÇARRA | PARÁ | Brasil | 1505635 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d1870e16-9c56-3e97-bf1e-99ddbbddff7e | -5.99645 | -48.39312 | 2024-10-24 04:34:00 | NOAA-21 | PALESTINA DO PARÁ | PARÁ | Brasil | 1505494 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5afe0d21-8542-369b-abcf-ec60cfa0251c | -5.69625 | -49.29654 | 2024-10-24 04:34:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bc265772-40b5-30f3-b187-3893c63800c9 | -5.69287 | -49.29601 | 2024-10-24 04:34:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 91c3b233-9f7a-3a9f-95f8-685854517da7 | -5.5697 | -49.40697 | 2024-10-24 04:34:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| f6f7a177-2226-39b5-85ee-f56c495b7227 | -5.56911 | -49.41064 | 2024-10-24 04:34:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| cdbada10-20dd-32c2-945a-8a3eb35e6156 | -5.56631 | -49.40642 | 2024-10-24 04:34:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| e0333339-e60c-3c33-a2e6-ae788ed38e9c | -5.56572 | -49.41011 | 2024-10-24 04:34:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a0c4f491-68da-3fb9-9991-e7172fe4151f | -5.49414 | -49.50809 | 2024-10-24 04:34:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8fad72fc-5258-33c6-875d-416a3fb32c0a | -5.49073 | -49.50755 | 2024-10-24 04:34:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 27919f2c-f694-342c-a6db-196f26972b6b | -5.41549 | -48.9862 | 2024-10-24 04:34:00 | NOAA-21 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| facb199c-190e-3933-9434-2c0cf3a90d8e | -5.39462 | -49.20424 | 2024-10-24 04:34:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 54687074-5596-39bc-b57d-26c7c53161c5 | -5.32401 | -48.3396 | 2024-10-24 04:34:00 | NOAA-21 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6ae61ae1-a2ef-39a1-8162-d89c40a3d01b | -5.28918 | -48.32345 | 2024-10-24 04:34:00 | NOAA-21 | SÃO SEBASTIÃO DO TOCANTINS | TOCANTINS | Brasil | 1720309 | 17 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fbd9ef93-bc6c-3c40-950b-b6306d864415 | -7.17871 | -49.30373 | 2024-10-24 04:34:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a69409ae-dbfb-3ed5-83df-4e2fefe37eb2 | -7.11251 | -49.14367 | 2024-10-24 04:34:00 | NOAA-21 | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1929d51a-d4fe-37f2-a0a0-af1ca8ce1fc6 | -7.10911 | -49.16497 | 2024-10-24 04:34:00 | NOAA-21 | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 08880319-7a98-3a1c-8215-206c8fd59a2d | -7.10854 | -49.16852 | 2024-10-24 04:34:00 | NOAA-21 | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8612b30b-be97-3655-8a4e-3a31a4cb13ac | -7.10633 | -49.16088 | 2024-10-24 04:34:00 | NOAA-21 | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f3da61c1-7693-3fbd-aaec-5bf7eb58e2f4 | -7.10576 | -49.16443 | 2024-10-24 04:34:00 | NOAA-21 | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2910ca9f-2ee7-3488-a8e4-63d1528bacb9 | -7.1052 | -49.16799 | 2024-10-24 04:34:00 | NOAA-21 | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5dea2496-188e-3a40-b156-f1449192b2d6 | -7.10185 | -49.16746 | 2024-10-24 04:34:00 | NOAA-21 | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e8bd6fff-0eae-371c-af14-04365603a25f | -7.10136 | -49.14916 | 2024-10-24 04:34:00 | NOAA-21 | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cd387bbc-c62e-3954-ae5e-d509ee946d9e | -7.09908 | -49.16337 | 2024-10-24 04:34:00 | NOAA-21 | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 03025795-9db6-3db3-9f06-ab931d4ad5e8 | -7.09851 | -49.16693 | 2024-10-24 04:34:00 | NOAA-21 | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d463bfa5-6fdc-346f-975c-c462d7660d21 | -7.09802 | -49.14863 | 2024-10-24 04:34:00 | NOAA-21 | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5e69edd4-ba6a-390f-8ebd-37aacf1050c3 | -7.07975 | -49.11304 | 2024-10-24 04:34:00 | NOAA-21 | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ffb8855f-58e4-322e-a8d6-eed5ddec4305 | -7.00683 | -49.33883 | 2024-10-24 04:34:00 | NOAA-21 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 686b1015-96de-38f6-902f-c443647c9826 | -7.00626 | -49.34242 | 2024-10-24 04:34:00 | NOAA-21 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a83414bb-6fd5-3261-9229-e9ca2d1dcaab | -6.99464 | -49.4586 | 2024-10-24 04:34:00 | NOAA-21 | SAPUCAIA | PARÁ | Brasil | 1507755 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7ac5af76-0b4e-334e-98fd-931811c0fa97 | -6.99127 | -49.45805 | 2024-10-24 04:34:00 | NOAA-21 | SAPUCAIA | PARÁ | Brasil | 1507755 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8d12b032-8173-39a6-abdc-7e7de25e90fb | -6.7617 | -49.05841 | 2024-10-24 04:34:00 | NOAA-21 | PIÇARRA | PARÁ | Brasil | 1505635 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 688087e5-e967-3fd7-977e-acb679829bac | -6.75639 | -48.77251 | 2024-10-24 04:34:00 | NOAA-21 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9c09fd09-b959-32ae-857d-f56b1cbefd1f | -6.6924 | -48.74738 | 2024-10-24 04:34:00 | NOAA-21 | PIÇARRA | PARÁ | Brasil | 1505635 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0efe9d19-edab-3066-a870-d4642228f410 | -6.69185 | -48.75087 | 2024-10-24 04:34:00 | NOAA-21 | PIÇARRA | PARÁ | Brasil | 1505635 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e8708c9e-0fa1-3e78-a2b0-5653077b0fb2 | -6.68908 | -48.74685 | 2024-10-24 04:34:00 | NOAA-21 | PIÇARRA | PARÁ | Brasil | 1505635 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| d2324aa1-f891-3ce2-9c76-a2566076139f | -7.82969 | -48.72281 | 2024-10-24 04:34:00 | NOAA-21 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 347e62c6-b81e-3552-91fc-be3d586bde39 | -7.82583 | -48.72576 | 2024-10-24 04:34:00 | NOAA-21 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5bf9ac7c-0de5-3da8-9657-c79a06a72802 | -7.76869 | -48.97807 | 2024-10-24 04:34:00 | NOAA-21 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3e5a7882-0ded-3a33-af8f-5aed0d4b9627 | -7.70634 | -48.85685 | 2024-10-24 04:34:00 | NOAA-21 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 2.3 |


[Clique aqui para ver as próximas entradas](README47.md)
