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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 94517f22-2065-3ea9-90a0-da8df8b46499 | -8.65182 | -38.14142 | 2025-09-06 03:49:00 | NOAA-21 | FLORESTA | PERNAMBUCO | Brasil | 2605707 | 26 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 896ef42e-2c80-37ae-bb51-4ed4dff1520f | -11.39896 | -43.61752 | 2025-09-06 03:49:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 03db67b8-30ae-3f2d-9a7b-e5b7918a20c2 | -7.00515 | -44.94513 | 2025-09-06 03:49:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fab0ccce-d2b8-32af-b9f8-000313ef06ba | -8.03724 | -44.06991 | 2025-09-06 03:49:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a3be4b90-b371-32a8-acb2-464ef1aeb9db | -6.01406 | -46.68961 | 2025-09-06 03:49:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 13a896ce-6feb-367e-99d0-f4ccda5f0ca3 | -13.01164 | -45.22534 | 2025-09-06 03:49:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| aeb70a90-b6e3-3d7e-8ddb-4764663bb234 | -11.90896 | -46.64463 | 2025-09-06 03:49:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e204c19b-5d5d-325d-a034-837d847a4a0b | -14.15781 | -41.67549 | 2025-09-06 03:49:00 | NOAA-21 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| cd5ce931-5a5e-3391-9b99-6188beeade1a | -5.72962 | -49.28422 | 2025-09-06 03:49:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d1533212-0b5f-3471-8b00-9d53d16605c0 | -6.60885 | -43.98484 | 2025-09-06 03:49:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b8431973-cab2-313e-ab74-8d0f9af4182e | -10.30867 | -46.41636 | 2025-09-06 03:49:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| daf8bd40-2867-3aa0-818b-fbac7fe9ca57 | -6.61431 | -43.98055 | 2025-09-06 03:49:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0047b9f9-184d-3173-a073-5002304120ed | -7.80383 | -45.42839 | 2025-09-06 03:49:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 2368a220-fffc-3610-816b-078e8b564c7b | -7.41743 | -44.95135 | 2025-09-06 03:49:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 01ed11e9-c22f-3e3b-b72d-ca692c1c5862 | -11.22023 | -46.17856 | 2025-09-06 03:49:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| abba0861-c644-3f55-aec5-842f08408154 | -8.90695 | -45.11372 | 2025-09-06 03:49:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 69ab0905-cac8-3510-a869-9c16a09c5f0e | -8.36586 | -48.27591 | 2025-09-06 03:49:00 | NOAA-21 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 70c68ac3-94b7-392f-9c1d-942a816c0fe9 | -9.71043 | -49.48899 | 2025-09-06 03:49:00 | NOAA-21 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 25.6 |
| 7dcf6ee4-0672-3834-94e6-f73e1f0d9aed | -12.2991 | -49.99884 | 2025-09-06 03:49:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ce5eb3c9-be41-3d80-a0c0-263b2aa48466 | -12.9482 | -46.56896 | 2025-09-06 03:49:00 | NOAA-21 | NOVO ALEGRE | TOCANTINS | Brasil | 1715150 | 17 | 33 | nan | nan | nan | Cerrado | 15.9 |
| be64dafe-d322-34a2-ab2e-b56509fd9980 | -6.60684 | -43.96902 | 2025-09-06 03:49:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 93cb8013-c4bc-3379-89c9-8cfeaad9b5a0 | -10.16858 | -46.24831 | 2025-09-06 03:49:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 34fa7bfb-ede6-3745-a82e-890efc14cfc6 | -13.00439 | -45.21453 | 2025-09-06 03:49:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c771c50b-e7cf-355a-b539-677432c81170 | -5.7286 | -49.28996 | 2025-09-06 03:49:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 78a28891-d4ad-3f9a-9c51-e846547ef092 | -12.91691 | -48.01866 | 2025-09-06 03:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0c609b52-9615-3dfd-96a9-fe23f7f2b890 | -9.18057 | -46.03533 | 2025-09-06 03:49:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b8f7031b-a795-3ede-bdf0-470d5372aa35 | -8.77483 | -49.63607 | 2025-09-06 03:49:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7af2cae8-f22d-3129-b33f-0c64185230cb | -8.63847 | -45.75061 | 2025-09-06 03:49:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 30a82e2f-0db3-3605-911f-ab9118e86294 | -7.33445 | -48.49537 | 2025-09-06 03:49:00 | NOAA-21 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 786d1711-3c7b-3512-bc8d-2d6005c1da1f | -12.73235 | -45.09373 | 2025-09-06 03:49:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 55d00fe2-7ccc-3c20-a109-5b020640878f | -13.71057 | -46.88333 | 2025-09-06 03:49:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 93d59684-fb84-3b55-8cab-38a26bcf0d54 | -6.39889 | -46.09789 | 2025-09-06 03:49:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b9fdadbb-b52d-3496-b325-c95b0fb95d07 | -11.93092 | -46.66617 | 2025-09-06 03:49:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5b3667ba-6b0a-3b17-b855-9ec3a3d9adf4 | -7.1633 | -43.88682 | 2025-09-06 03:49:00 | NOAA-21 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c48b65d1-c298-3818-b8b8-93b0b8d46ee6 | -6.8107 | -45.65728 | 2025-09-06 03:49:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5c229d30-863f-3018-8ec6-a50055d55b28 | -7.73165 | -50.31694 | 2025-09-06 03:49:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| b3e7df5c-4b15-3490-9f1e-22e40ac816ee | -9.08768 | -47.01754 | 2025-09-06 03:49:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| ea28a491-eb54-3ae8-8219-e2f626e5bbe5 | -11.13273 | -46.34584 | 2025-09-06 03:49:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6c13f446-4e7f-3d47-933c-e82f45c11e98 | -8.87866 | -47.9155 | 2025-09-06 03:49:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a22853ff-b306-330e-82b7-93b786788395 | -7.73911 | -47.42546 | 2025-09-06 03:49:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 8334a763-bd46-329e-97bb-93cc781d04b7 | -8.44772 | -45.03399 | 2025-09-06 03:49:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c1570ce6-fe8d-306d-8f82-42c9a442735f | -11.39758 | -43.62518 | 2025-09-06 03:49:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1f7a10c7-6a3e-35c8-bf51-ab75c71e7871 | -6.40013 | -46.09101 | 2025-09-06 03:49:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 461f8e29-7f6b-3c6c-83d1-c6cf7ee79d7f | -8.09036 | -45.32424 | 2025-09-06 03:49:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a434a977-bf21-3c9a-9899-269c79263d65 | -12.68761 | -44.96632 | 2025-09-06 03:49:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cbdb5abf-8c00-3f9f-bc90-5a2dbd36c46b | -11.54953 | -47.31975 | 2025-09-06 03:49:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a8c86f36-0e25-3800-b663-27d3845fc232 | -12.93405 | -48.04546 | 2025-09-06 03:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e5a1dadb-f137-3c65-a9ac-4e394c3bba30 | -7.25593 | -41.89236 | 2025-09-06 03:49:00 | NOAA-21 | WALL FERRAZ | PIAUÍ | Brasil | 2211704 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| bf5f480e-f2f0-3ff0-bd59-99bb8f472f87 | -8.02459 | -45.42806 | 2025-09-06 03:49:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e9980737-8ba1-3b9c-b20e-e08209ce2782 | -12.94927 | -46.56334 | 2025-09-06 03:49:00 | NOAA-21 | NOVO ALEGRE | TOCANTINS | Brasil | 1715150 | 17 | 33 | nan | nan | nan | Cerrado | 15.9 |
| eddb5b47-afe7-3f0a-83f4-ba9b25c44e50 | -8.43956 | -47.31852 | 2025-09-06 03:49:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 851e6a26-3160-30a7-b1d3-596141b22115 | -12.99695 | -48.05026 | 2025-09-06 03:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 741953f6-0c8e-3225-8e5b-2ed4a446706e | -9.09027 | -47.00354 | 2025-09-06 03:49:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8a943609-8d4b-3032-aa71-082fa566e235 | -12.92222 | -48.02006 | 2025-09-06 03:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| eca9b431-5d1b-3a8b-b5c9-6792ef43ab35 | -10.60849 | -44.32493 | 2025-09-06 03:49:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 126.2 |
| ac4842b3-d1db-38da-8033-328c34a00a4f | -8.91043 | -45.8168 | 2025-09-06 03:49:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9b4fffcf-c29b-3ca1-8481-e2cc62706895 | -9.08107 | -46.99307 | 2025-09-06 03:49:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ebe2441b-edea-3905-a563-8eb4e7b50be6 | -7.33355 | -48.50026 | 2025-09-06 03:49:00 | NOAA-21 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 1698f364-4242-3d06-9c82-ae1ddb003ece | -7.83353 | -46.21159 | 2025-09-06 03:49:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 57a8d59f-5ae8-3279-af7f-37154e349fdb | -9.84293 | -48.83599 | 2025-09-06 03:49:00 | NOAA-21 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ecbe631c-1099-3399-91ae-64b678e333f8 | -10.16063 | -46.23933 | 2025-09-06 03:49:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 80a7adda-30f3-3926-9efe-6eafd4aa5def | -10.15162 | -46.23169 | 2025-09-06 03:49:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| df7f7cbb-529f-3f97-a12e-8bfaa857b259 | -10.78349 | -47.75324 | 2025-09-06 03:49:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| eb21ab39-3053-3e70-be1d-9bc2846ee700 | -9.87869 | -46.54274 | 2025-09-06 03:49:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5fefab26-40ae-3c11-9c7f-d69d7763f1ee | -8.76845 | -49.63485 | 2025-09-06 03:49:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a3cea045-184c-3409-87f3-dba82e16e005 | -12.93935 | -48.04695 | 2025-09-06 03:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fe63eef2-e989-3ca3-b482-196dd9a3710a | -9.34492 | -40.39054 | 2025-09-06 03:49:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 9651b8a7-7ee5-363b-ba35-091cbf881e96 | -7.21244 | -43.98767 | 2025-09-06 03:49:00 | NOAA-21 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a9cb3cea-6d8c-3ca9-9184-126485dbf2d9 | -12.8952 | -48.88791 | 2025-09-06 03:49:00 | NOAA-21 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 9c008226-2caf-3b40-8d86-ef2bd866a8b1 | -10.98182 | -46.82212 | 2025-09-06 03:49:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c10e8fbc-e0aa-3141-ab35-14cad40517ce | -10.31483 | -46.41137 | 2025-09-06 03:49:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 593865e0-ebb8-3bc1-9637-475dea057ac9 | -10.76505 | -48.27752 | 2025-09-06 03:49:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 492ff2d1-2076-3d09-bcee-57ac4b64c41a | -10.08803 | -48.08676 | 2025-09-06 03:49:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b0bc3943-c5e7-3fb4-8617-5fea6e554cbc | -13.06297 | -47.10211 | 2025-09-06 03:49:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 83feec2b-19bc-3e69-99b2-7e9f037d31dc | -9.30747 | -45.4126 | 2025-09-06 03:49:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 535a259c-c941-36ce-8601-f353c4e55b1e | -10.16013 | -46.2379 | 2025-09-06 03:49:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 95bffb2f-494a-337a-978e-143885ad68b2 | -7.34047 | -48.49691 | 2025-09-06 03:49:00 | NOAA-21 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| c4869bc3-90bd-3501-9620-cc74142c818c | -7.28078 | -43.70198 | 2025-09-06 03:49:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d4443271-b7aa-350a-ab5c-9eafc0b5e476 | -6.00847 | -46.68882 | 2025-09-06 03:49:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d536e996-077a-3c27-8ced-82759b895118 | -7.34226 | -43.94624 | 2025-09-06 03:49:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 03b5e5ab-665f-3480-8406-9ef863cd6b5c | -10.76818 | -48.27252 | 2025-09-06 03:49:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 83271584-842b-3299-b030-818792ed3bf6 | -6.40542 | -46.09203 | 2025-09-06 03:49:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6c9c46e4-101b-3a22-bcb1-559ff7668de9 | -13.18617 | -44.48404 | 2025-09-06 03:49:00 | NOAA-21 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 50961fd7-354b-3ee0-b15d-04d9730d6fa7 | -6.64309 | -43.41325 | 2025-09-06 03:49:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4b3a47f1-6cc9-36f3-8349-8a00f9b26b26 | -10.13919 | -46.01675 | 2025-09-06 03:49:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| cf88512e-e16b-3085-82c8-30cd45319339 | -10.03038 | -48.13253 | 2025-09-06 03:49:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c21d9ad0-cec3-3e28-b1da-38529e73322d | -11.39942 | -43.62605 | 2025-09-06 03:49:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 727dd3e3-9100-3124-8796-36734b83abc0 | -9.37932 | -48.18478 | 2025-09-06 03:49:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 34a7d69c-6ad0-33b0-999a-513556292b36 | -10.94961 | -44.83092 | 2025-09-06 03:49:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4b8eeacc-0c56-36a8-96d7-9dd21bc45adc | -11.64718 | -47.14898 | 2025-09-06 03:49:00 | NOAA-21 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 909eaa53-8206-3ec5-a212-809a66097cda | -7.8341 | -46.20841 | 2025-09-06 03:49:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c2ef8984-e4c6-3c1d-bf1d-31cec79aecc7 | -9.84891 | -48.83713 | 2025-09-06 03:49:00 | NOAA-21 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 501f47ce-40e1-3807-bf16-28799b22a6f6 | -10.16117 | -46.23634 | 2025-09-06 03:49:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7f109e09-c5ff-3bce-a91e-7e12e51d4c58 | -9.68234 | -51.0844 | 2025-09-06 03:49:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 14c17ea1-312c-3c15-8a4f-3e363989c34b | -10.75554 | -46.34522 | 2025-09-06 03:49:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 101132ea-a020-3d88-96ef-e7de6dbe6125 | -7.96593 | -44.94306 | 2025-09-06 03:49:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 939448ae-34b9-3abe-9f65-8fbe199c2c62 | -7.68489 | -50.29448 | 2025-09-06 03:49:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| e0770373-d1bb-3b44-b6c6-b5f2e421b361 | -7.23252 | -43.862 | 2025-09-06 03:49:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 647d3eaf-fd28-3f54-a831-18a6de09151c | -9.0541 | -50.45239 | 2025-09-06 03:49:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| b6dffe69-1fd7-3f71-ae04-015049e1154c | -12.92412 | -48.03896 | 2025-09-06 03:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |


[Clique aqui para ver as próximas entradas](README23.md)
