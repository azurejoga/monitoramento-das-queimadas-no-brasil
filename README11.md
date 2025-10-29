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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e763d6a8-e930-30d5-8595-c801b924593b | -5.66561 | -41.11288 | 2025-10-29 03:53:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| ec861d7c-1362-39ec-ae32-cc698c2b3f17 | -6.26596 | -41.80904 | 2025-10-29 03:53:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 633fb1f0-ef87-3c0e-ab53-8a4f0f0ce845 | -7.27171 | -46.89052 | 2025-10-29 03:53:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8f20b880-3eaf-32ad-998b-e78b2f0bddfd | -8.0099 | -46.20579 | 2025-10-29 03:53:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| a4955125-7c6f-3bb2-b759-9790c069cdbc | -8.04367 | -41.11347 | 2025-10-29 03:53:00 | NOAA-21 | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| f8f0542a-1cbf-3468-89ce-e8920db1ebb0 | -5.41598 | -45.21518 | 2025-10-29 03:53:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 525c7683-90a8-300b-9cb0-de2deb66382f | -4.60375 | -45.74318 | 2025-10-29 03:53:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bd84190f-c47a-3569-a8ff-3f99017fd7c1 | -6.30315 | -41.87737 | 2025-10-29 03:53:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 16.2 |
| 1bcb746f-ad27-3963-89f5-d1ff09b9a9ef | -4.84361 | -40.71946 | 2025-10-29 03:53:00 | NOAA-21 | ARARENDÁ | CEARÁ | Brasil | 2301257 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 95911775-4052-3e33-8d4c-85bfb44d68ca | -4.70801 | -46.10494 | 2025-10-29 03:53:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 00c6178a-e0a9-312e-b7c3-0bf259980c06 | -7.74811 | -44.72445 | 2025-10-29 03:53:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a432599c-a07f-3eec-8fbf-1b40f41d0761 | -5.56722 | -42.16957 | 2025-10-29 03:53:00 | NOAA-21 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| cb98ea60-c1b8-39cd-b982-6f79576691cc | -6.24238 | -42.57065 | 2025-10-29 03:53:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| bdea0f99-b3cc-3a76-8d38-06ae7fae9a3f | -7.42489 | -41.85896 | 2025-10-29 03:53:00 | NOAA-21 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 1357c1c9-82da-3f52-968d-4fc9d7649216 | -3.78349 | -45.5945 | 2025-10-29 03:53:00 | NOAA-21 | TUFILÂNDIA | MARANHÃO | Brasil | 2112274 | 21 | 33 | nan | nan | nan | Amazônia | 13.8 |
| ac29624a-911d-34f9-96dd-9f3038136867 | -7.19336 | -46.75158 | 2025-10-29 03:53:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e5ffc236-7bca-3b9a-b664-a4b364ed3f17 | -4.67843 | -43.26311 | 2025-10-29 03:53:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6dcb1544-7f30-3849-ad46-6d0167a3de30 | -6.14494 | -41.55908 | 2025-10-29 03:53:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| a82fcc59-28a8-3b59-b1d8-d432eb2530e5 | -2.52852 | -47.2989 | 2025-10-29 03:53:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7bbe5c4a-6ed2-3750-9c6a-3702a9a1b44f | -6.91039 | -42.86158 | 2025-10-29 03:53:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 2eb7ac35-720c-314f-83e4-5b07bd54b62f | -6.11499 | -42.43124 | 2025-10-29 03:53:00 | NOAA-21 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 567a44cb-79c9-37e5-af0c-e477c7e99484 | -5.64296 | -41.20699 | 2025-10-29 03:53:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 20598a5c-6098-3d43-867f-7c2b128e4bda | -2.80626 | -49.14828 | 2025-10-29 03:53:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 667d720e-bb38-37e5-972c-187d437fd42b | -8.68698 | -40.38033 | 2025-10-29 03:53:00 | NOAA-21 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 1.0 |
| e31285a9-2db7-30b8-92ac-bb89bae76f16 | -4.66176 | -46.40558 | 2025-10-29 03:53:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7381280c-ef25-3533-a0e8-09a1bd5cd97f | -6.50108 | -42.23288 | 2025-10-29 03:53:00 | NOAA-21 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 481195b8-00f6-35ce-b94a-f7ce5f149512 | -7.34565 | -42.46423 | 2025-10-29 03:53:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 6.3 |
| 609dd5bf-37e8-3456-a7d8-923f36f2e8ab | -6.70779 | -38.2039 | 2025-10-29 03:53:00 | NOAA-21 | SOUSA | PARAÍBA | Brasil | 2516201 | 25 | 33 | nan | nan | nan | Caatinga | 2.0 |
| d60ad4ba-52c8-3f99-bafd-ed818f30ae72 | -6.10494 | -42.46845 | 2025-10-29 03:53:00 | NOAA-21 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 14.0 |
| 261e919d-d241-32c2-be42-659f61b1df88 | -4.99132 | -44.9107 | 2025-10-29 03:53:00 | NOAA-21 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1e82124e-7b1b-3ca0-ab4e-76103bd82af9 | -5.24013 | -45.20038 | 2025-10-29 03:53:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| de31ebdb-c395-3a29-bba4-f68e50395910 | -7.34408 | -42.4735 | 2025-10-29 03:53:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 8b7c166b-5d58-30af-8a75-5cb51951506c | -5.57153 | -46.53088 | 2025-10-29 03:53:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6f5b1bda-0489-36be-9a18-f2dfea0bd302 | -7.60327 | -43.6011 | 2025-10-29 03:53:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 09bb867d-3623-3c67-8a9c-f965193909d2 | -7.34521 | -43.90983 | 2025-10-29 03:53:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 02fe7254-1a10-38fc-8450-3f032f91cced | -6.16641 | -43.75671 | 2025-10-29 03:53:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 2027f1e3-d55b-32ae-9ba4-616c09b02e3b | -6.47245 | -42.24247 | 2025-10-29 03:53:00 | NOAA-21 | FRANCINÓPOLIS | PIAUÍ | Brasil | 2204006 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| ba4279f4-91fd-3a7b-a0ff-0b13a38d5c56 | -7.08121 | -44.94049 | 2025-10-29 03:53:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 284e0258-66c9-36ad-b922-d2b9bf1ab85d | -8.56241 | -45.70742 | 2025-10-29 03:53:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| ce5ba925-3823-3a49-ae12-ac29a0630fc4 | -3.59673 | -47.51972 | 2025-10-29 03:53:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2ace45eb-6275-3700-83c3-e7c59dc59937 | -6.17122 | -43.75363 | 2025-10-29 03:53:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| bec9f004-c643-34a3-82d5-c5dcd12a98b3 | -7.45612 | -45.47392 | 2025-10-29 03:53:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d80f2c4a-7c93-3aa9-9ca8-fdcf6575ff28 | -6.14225 | -41.69118 | 2025-10-29 03:53:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 481c469f-7b79-3809-a7e2-649e139fd3ae | -5.80202 | -42.56933 | 2025-10-29 03:53:00 | NOAA-21 | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| a5b9b54a-1f64-37df-8783-857d0f4879d5 | -8.03443 | -47.40744 | 2025-10-29 03:53:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 23234efb-2bdf-37e1-8661-a6d9cc0a6944 | -7.61378 | -43.58817 | 2025-10-29 03:53:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a31ca5ed-b5ff-3c5a-bda9-41afecb7bb18 | -6.56692 | -41.59605 | 2025-10-29 03:53:00 | NOAA-21 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| e91d6283-9d99-3f79-ac20-ab7da61bfa5e | -6.13881 | -41.85315 | 2025-10-29 03:53:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| ab0ae922-2d88-3e97-9542-1d6ec55d7ab8 | -7.27662 | -46.89223 | 2025-10-29 03:53:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9b1efdcd-bb1d-3aa9-bbdb-45eaf226f13e | -4.2094 | -50.08527 | 2025-10-29 03:53:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 25.7 |
| 8cdacce5-d847-3437-9bc8-0bcd72772261 | -7.86402 | -44.23062 | 2025-10-29 03:53:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 989c4333-dd69-3cc9-b4df-3670c030462f | -6.10945 | -41.73061 | 2025-10-29 03:53:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| ce4d7784-eb05-3acf-9821-061f6bfd382b | -7.85984 | -44.22992 | 2025-10-29 03:53:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e1d326aa-de3f-30dc-88bf-12b81e1534d4 | -4.02266 | -42.87862 | 2025-10-29 03:53:00 | NOAA-21 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Caatinga | 1.1 |
| c39294c4-756e-3d75-a175-c89d7eb34e5f | -5.64174 | -41.53741 | 2025-10-29 03:53:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| a38f8a7b-fc78-3c3d-a820-3c814ef9ba97 | -7.32365 | -44.74268 | 2025-10-29 03:53:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9e2490f3-6e05-3949-b3e4-0e3619fa333f | -8.83289 | -40.97348 | 2025-10-29 03:53:00 | NOAA-21 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| bcc4fd18-6ad4-3fe6-9713-ae730828f6c8 | -5.48439 | -46.44118 | 2025-10-29 03:53:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 075f56eb-1be5-3131-bdaf-7ed6e1bf2040 | -5.18516 | -44.35984 | 2025-10-29 03:53:00 | NOAA-21 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e9c19e0f-f384-339e-a583-9c9047500105 | -7.59831 | -46.79544 | 2025-10-29 03:53:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 69f70fd9-befb-3a0b-bbe3-ea3c03ed93d9 | -7.9628 | -46.74777 | 2025-10-29 03:53:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| baa39563-d425-3420-a206-9d770c0073c8 | -5.3298 | -41.21584 | 2025-10-29 03:53:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| a1a4ff85-ecbf-3877-a9ac-963e7ce80dc9 | -4.70296 | -46.10431 | 2025-10-29 03:53:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d2ec3ae0-7f9a-3453-9b9e-ab74db11a6c8 | -7.8968 | -45.68316 | 2025-10-29 03:53:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 68284d20-7fc9-3994-ac14-410b1bec481b | -6.15171 | -41.81277 | 2025-10-29 03:53:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 7bdc112b-538d-349f-a616-7bcced7dd1a9 | -7.20255 | -44.15738 | 2025-10-29 03:53:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a1dd428d-4bb2-370a-8506-cdc1519717a2 | -6.92187 | -46.02921 | 2025-10-29 03:53:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ccc84ddd-4286-3c3f-b928-976da8816650 | -4.7075 | -46.10791 | 2025-10-29 03:53:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 919b73d5-24fb-3507-89b2-e77d73e4534e | -6.84114 | -35.31701 | 2025-10-29 03:53:00 | NOAA-21 | ARAÇAGI | PARAÍBA | Brasil | 2500809 | 25 | 33 | nan | nan | nan | Caatinga | 0.9 |
| f2318cc7-a6ab-3168-94bf-d7d92add2fc8 | -7.30738 | -45.67984 | 2025-10-29 03:53:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 559e01bc-4530-36be-b254-25aa769f3a70 | -7.4393 | -45.12685 | 2025-10-29 03:53:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c9189ce0-a054-357e-9913-11dd7b560a83 | -8.76243 | -40.60756 | 2025-10-29 03:53:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 98658dc0-8d57-33ec-86c0-503434a5e71e | -7.80682 | -46.46193 | 2025-10-29 03:53:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| a323807a-2e16-372d-99ba-4f32f5810a60 | -6.11161 | -41.71737 | 2025-10-29 03:53:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 47d1d2f0-2287-392d-9cad-eec67e4f90d9 | -7.78629 | -46.46441 | 2025-10-29 03:53:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 5d99bd04-afcd-32d5-b2e2-7e844550b7bb | -5.59887 | -45.3574 | 2025-10-29 03:53:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 11eff0b3-1341-3ed8-99b4-e22c6e325bb7 | -8.04716 | -41.11403 | 2025-10-29 03:53:00 | NOAA-21 | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 3a029e3b-ccfb-3144-a330-624f658e1fa5 | -8.30867 | -46.83216 | 2025-10-29 03:53:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 87b66c8d-a27e-31b2-ba68-45ba02cbf9e5 | -4.65857 | -46.57968 | 2025-10-29 03:53:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4b1eb1dd-a92c-3646-aa08-2a38f638308e | -4.84769 | -47.53471 | 2025-10-29 03:53:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a05fad90-011c-34cd-bf15-687b215e958f | -4.89122 | -40.4468 | 2025-10-29 03:53:00 | NOAA-21 | TAMBORIL | CEARÁ | Brasil | 2313203 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 0933c225-ce7d-359c-a38b-7ceaa9f0dc63 | -6.11116 | -42.4306 | 2025-10-29 03:53:00 | NOAA-21 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| f54cd4bd-3871-3226-9d9d-3ce22bbce31b | -3.03213 | -42.64845 | 2025-10-29 03:53:00 | NOAA-21 | PAULINO NEVES | MARANHÃO | Brasil | 2108058 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 530fc000-791a-348f-ab77-a9b37435cf77 | -4.47623 | -43.44124 | 2025-10-29 03:53:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 4de67022-bbd3-3adc-b286-a9a0edb9d04a | -6.14661 | -41.68752 | 2025-10-29 03:53:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 7bef3603-48b0-3bd0-9071-f2852c42be55 | -6.30056 | -44.69263 | 2025-10-29 03:53:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 5772ab0b-a77a-3846-b0c3-fe1cbfc3e6b1 | -6.60865 | -43.34309 | 2025-10-29 03:53:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 7.8 |
| b1d0932b-e9da-3aa1-893b-37200ab56d25 | -3.99783 | -43.65807 | 2025-10-29 03:53:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8f1e55fd-5500-39fe-9616-acd4ecd65d68 | -6.86448 | -43.44212 | 2025-10-29 03:53:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 844ff2b5-dc7f-3753-9f86-42f1467173f7 | -2.63762 | -47.9606 | 2025-10-29 03:53:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c08d3ef2-1e8b-303e-b7c9-e036040c9a39 | -6.99058 | -46.2295 | 2025-10-29 03:53:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 468cead4-2f71-3bf5-8f65-01b919b3a881 | -6.12475 | -41.70617 | 2025-10-29 03:53:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 6.7 |
| 7c7ad8d6-2053-3dd0-b20a-de82fc5a1114 | -7.32439 | -44.7384 | 2025-10-29 03:53:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e258c888-13f0-3f9c-bbd8-628dce62a6fa | -4.48043 | -43.4419 | 2025-10-29 03:53:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 14.8 |
| c4f0d4bb-46f0-3efd-8f1b-42d9fead3bac | -3.67623 | -47.12056 | 2025-10-29 03:53:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3d76bf52-922e-3d7b-99f1-57cdf385fa07 | -7.59923 | -43.60049 | 2025-10-29 03:53:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4ebe33f9-d520-3282-bc12-f696bf27f9a0 | -4.5488 | -46.34194 | 2025-10-29 03:53:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 749214f7-f472-30d9-bf55-f3f5700831bd | -4.67432 | -43.26238 | 2025-10-29 03:53:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a156dc3f-7a9f-3041-8599-72c9ed70dad2 | -6.85835 | -43.44849 | 2025-10-29 03:53:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d7beadca-6edf-3e6c-a956-ac6492a26955 | -5.74747 | -41.90043 | 2025-10-29 03:53:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |


[Clique aqui para ver as próximas entradas](README12.md)
