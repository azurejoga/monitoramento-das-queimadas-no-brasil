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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 53ade5ce-fe6f-33f9-a692-e4dfd5768fc9 | -22.59971 | -42.09035 | 2025-03-07 00:13:00 | TERRA_M-M | CABO FRIO | RIO DE JANEIRO | Brasil | 3300704 | 33 | 33 | nan | nan | nan | Mata Atlântica | 25.1 |
| 5cb5cbcf-19f5-30a5-a8c1-406ab42189fa | -22.65417 | -42.89424 | 2025-03-07 00:13:00 | TERRA_M-M | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 14.1 |
| 617e2fbd-c7eb-3821-a437-8d5cdf257a53 | -10.72071 | -42.33064 | 2025-03-07 00:17:00 | TERRA_M-M | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 27.1 |
| a6ad4cec-621b-3a7c-a1f4-382937176e99 | -12.90936 | -45.0811 | 2025-03-07 00:17:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 36.7 |
| 79c60f78-aa50-3ebc-a400-78190057a3c9 | -13.41813 | -44.37853 | 2025-03-07 00:17:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 827c6ebf-f312-395d-81d8-e88525e1bc4b | -12.84583 | -43.83743 | 2025-03-07 00:17:00 | TERRA_M-M | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 14.8 |
| b09aca66-4704-3b44-ba4a-51db2ee593ba | -10.66326 | -44.40265 | 2025-03-07 00:17:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 10.9 |
| b8e71bde-20ac-3fda-a9cc-b9088ae293ed | -10.71137 | -42.33193 | 2025-03-07 00:17:00 | TERRA_M-M | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 13.6 |
| 75eeed2c-417b-3b53-9776-b4de6f7dc08a | -12.84417 | -43.82429 | 2025-03-07 00:17:00 | TERRA_M-M | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 1ebe8337-21ad-39fc-8ccc-c84a54226d9a | -10.72206 | -42.34069 | 2025-03-07 00:17:00 | TERRA_M-M | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 6b28a6c4-0a05-3bce-a565-dc9bbd3f4bff | -22.607201 | -42.086498 | 2025-03-07 00:51:00 | METOP-C | CABO FRIO | RIO DE JANEIRO | Brasil | 3300704 | 33 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 5894f143-c404-3d67-a4f1-85a3f6acdcbf | -23.202801 | -50.8092 | 2025-03-07 00:51:00 | METOP-C | URAÍ | PARANÁ | Brasil | 4128401 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 723357f2-5b67-3829-9b12-e76ea1c63236 | -30.366501 | -51.966499 | 2025-03-07 00:51:00 | METOP-C | SÃO JERÔNIMO | RIO GRANDE DO SUL | Brasil | 4318408 | 43 | 33 | nan | nan | nan | Pampa | nan |
| b5476af0-8eec-37c8-9d76-4d885754dc0b | -10.7285 | -42.3209 | 2025-03-07 00:51:00 | METOP-C | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 4958678e-2f9d-34d2-ba8d-d3b2c2cff65e | -26.0166 | -49.170601 | 2025-03-07 00:51:00 | METOP-C | CAMPO ALEGRE | SANTA CATARINA | Brasil | 4203303 | 42 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 2bcf5acf-5956-30c3-abae-b2eccaeba319 | -26.0084 | -49.181499 | 2025-03-07 00:51:00 | METOP-C | CAMPO ALEGRE | SANTA CATARINA | Brasil | 4203303 | 42 | 33 | nan | nan | nan | Mata Atlântica | nan |
| d14dd80d-81b4-3e10-ad8f-0d26ad66907e | -24.0396 | -50.497101 | 2025-03-07 00:51:00 | METOP-C | CURIÚVA | PARANÁ | Brasil | 4107009 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |
| f3135c4d-f204-3bf3-adb4-f19f5e55c49f | -10.3967 | -47.988499 | 2025-03-07 00:51:00 | METOP-C | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0d50dcd3-c4d5-3f8f-b6f5-60339961a900 | -22.717699 | -42.318401 | 2025-03-07 00:51:00 | METOP-C | ARARUAMA | RIO DE JANEIRO | Brasil | 3300209 | 33 | 33 | nan | nan | nan | Mata Atlântica | nan |
| c0d12e9b-a95c-3933-92d1-9698068b0d36 | -12.9138 | -45.0672 | 2025-03-07 00:51:00 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e367d024-739e-3031-abbf-4f16a584eee6 | -26.0068 | -49.172901 | 2025-03-07 00:51:00 | METOP-C | CAMPO ALEGRE | SANTA CATARINA | Brasil | 4203303 | 42 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 0170b920-9f1d-3325-9502-62458d71dcd0 | -22.720301 | -42.328899 | 2025-03-07 00:51:00 | METOP-C | ARARUAMA | RIO DE JANEIRO | Brasil | 3300209 | 33 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 4efaafe9-b5fa-362f-8ba0-b0315f853e0c | -12.9162 | -45.077099 | 2025-03-07 00:51:00 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 6afe9166-ee6f-31b9-afdf-dae2bd9b50e8 | -30.3643 | -51.952599 | 2025-03-07 00:51:00 | METOP-C | SÃO JERÔNIMO | RIO GRANDE DO SUL | Brasil | 4318408 | 43 | 33 | nan | nan | nan | Pampa | nan |
| ac9e832f-b2bb-3fa0-bb99-6473cf49607c | -10.7189 | -42.323399 | 2025-03-07 00:51:00 | METOP-C | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 45e3fbc6-5ce2-30f4-8304-b3f691a85da5 | -23.201 | -50.7999 | 2025-03-07 00:51:00 | METOP-C | URAÍ | PARANÁ | Brasil | 4128401 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |
| a86c06b4-9164-3a7c-b9c5-224e8ed0232b | -30.37252 | -51.97497 | 2025-03-07 01:49:00 | TERRA_M-M | SÃO JERÔNIMO | RIO GRANDE DO SUL | Brasil | 4318408 | 43 | 33 | nan | nan | nan | Pampa | 22.6 |
| 48c80285-7599-306b-b5ea-c02316ef571c | -9.4964 | -40.3088 | 2025-03-07 01:50:00 | GOES-16 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 86.0 |
| 2b56820b-85ed-3386-a01f-1bb9387006c8 | -9.4964 | -40.3088 | 2025-03-07 02:00:00 | GOES-16 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 74.9 |
| 12c272c2-36ef-3422-8b1f-6d08460f9522 | -22.7308 | -51.258 | 2025-03-07 02:40:00 | GOES-16 | ALVORADA DO SUL | PARANÁ | Brasil | 4100806 | 41 | 33 | nan | nan | nan | Mata Atlântica | 98.8 |
| 704ad9bc-9a1a-372c-9afb-bebe859c0aa7 | -4.72156 | -37.36092 | 2025-03-07 03:25:00 | NOAA-20 | ICAPUÍ | CEARÁ | Brasil | 2305357 | 23 | 33 | nan | nan | nan | Caatinga | 4.5 |
| f2d5ae0c-c68b-36a8-809a-6012e691814a | -4.72586 | -37.36267 | 2025-03-07 03:25:00 | NOAA-20 | ICAPUÍ | CEARÁ | Brasil | 2305357 | 23 | 33 | nan | nan | nan | Caatinga | 4.0 |
| b4b9f4d6-d1d2-3434-8f0f-f9f474f93276 | -4.72578 | -37.36165 | 2025-03-07 03:25:00 | NOAA-20 | ICAPUÍ | CEARÁ | Brasil | 2305357 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 3190536b-d289-30da-8d32-05fa52169f76 | -4.05515 | -40.0164 | 2025-03-07 03:25:00 | NOAA-20 | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| fc294f41-6409-3042-a2f9-67e811ff26f5 | -4.0527 | -40.01705 | 2025-03-07 03:25:00 | NOAA-20 | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| c82e69b5-f128-39f2-84fa-c2a1c1601b13 | -4.72164 | -37.36195 | 2025-03-07 03:25:00 | NOAA-20 | ICAPUÍ | CEARÁ | Brasil | 2305357 | 23 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 57d6629e-7eed-37c6-82ce-1ef1bd0e621e | -5.18871 | -35.83382 | 2025-03-07 03:27:00 | NOAA-20 | PEDRA GRANDE | RIO GRANDE DO NORTE | Brasil | 2409506 | 24 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 18e80577-2b18-3386-88c7-411c7410fc7c | -10.71447 | -42.33229 | 2025-03-07 03:27:00 | NOAA-20 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| bd1ab693-dd59-3783-b532-9f56df4f0e70 | -11.84523 | -37.58727 | 2025-03-07 03:27:00 | NOAA-20 | CONDE | BAHIA | Brasil | 2908606 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| b78a94b9-b464-32fb-8570-3c44535eb371 | -5.18829 | -35.83115 | 2025-03-07 03:27:00 | NOAA-20 | PEDRA GRANDE | RIO GRANDE DO NORTE | Brasil | 2409506 | 24 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 1a02b889-5d1c-32f6-ac21-49af35824518 | -10.7198 | -42.33336 | 2025-03-07 03:27:00 | NOAA-20 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 79fb1d7b-4062-3f75-93a2-8617896aaae1 | -10.72513 | -42.33442 | 2025-03-07 03:27:00 | NOAA-20 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 3a049c56-a9fe-3d38-b470-331734245bc3 | -10.72577 | -42.331 | 2025-03-07 03:27:00 | NOAA-20 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 0f545af7-c5c6-359e-abcb-36677ff74626 | -11.84375 | -37.5849 | 2025-03-07 03:27:00 | NOAA-20 | CONDE | BAHIA | Brasil | 2908606 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| edabf5ba-f13a-3918-902c-4d404259c488 | -11.84293 | -37.58976 | 2025-03-07 03:27:00 | NOAA-20 | CONDE | BAHIA | Brasil | 2908606 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| e0458085-aa88-39ca-9a2e-b539e4bec612 | -10.69518 | -37.05016 | 2025-03-07 03:27:00 | NOAA-20 | ROSÁRIO DO CATETE | SERGIPE | Brasil | 2806107 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| e70705df-c1d6-3fe2-b9d8-3d834df7ca38 | -12.90702 | -45.08123 | 2025-03-07 03:29:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 6e5144c2-5ff6-3a75-9f64-eeb36c94239a | -12.90605 | -45.08601 | 2025-03-07 03:29:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| d9364948-38b6-3163-aaf5-bb7f526d39a4 | -13.72456 | -47.71474 | 2025-03-07 03:29:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f9f627af-9a97-3e93-9bc7-ed19a9f53c54 | -13.72303 | -47.72172 | 2025-03-07 03:29:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 00d55c4d-d478-3b45-aff1-0effcf710c53 | -17.78143 | -42.8124 | 2025-03-07 03:29:00 | NOAA-20 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fe4eb5ee-5c32-321f-826d-589f7916a364 | -17.09432 | -43.80649 | 2025-03-07 03:29:00 | NOAA-20 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 46b8168d-4bb0-364b-9930-8bd8ac0d7332 | -12.84477 | -43.832 | 2025-03-07 03:29:00 | NOAA-20 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 9f49d4c3-4bd8-326f-bb2c-17213e895ad4 | -12.90799 | -45.07645 | 2025-03-07 03:29:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| b4cd9919-2efc-35d1-a047-483ee5e17b2f | -22.9 | -42.85119 | 2025-03-07 03:32:00 | NOAA-20 | MARICÁ | RIO DE JANEIRO | Brasil | 3302700 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 591322f4-b0a3-3f6e-b03e-1949e471be45 | -23.25921 | -47.13073 | 2025-03-07 03:32:00 | NOAA-20 | CABREÚVA | SÃO PAULO | Brasil | 3508405 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 13e8a4de-1a7f-3ce1-8277-3f8d5052783f | -23.25463 | -47.13194 | 2025-03-07 03:32:00 | NOAA-20 | CABREÚVA | SÃO PAULO | Brasil | 3508405 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 8c6ab113-5c9f-30d9-8e16-ec725fadb4b3 | -22.97336 | -43.58072 | 2025-03-07 03:32:00 | NOAA-20 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| fcfac0f3-ff3c-3285-9771-cbe532826ad7 | -19.7002 | -44.77789 | 2025-03-07 03:32:00 | NOAA-20 | ONÇA DE PITANGUI | MINAS GERAIS | Brasil | 3145802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 4f1a4ee4-e1fc-3ab5-ab0c-8f33b87a951e | -20.41825 | -41.68725 | 2025-03-07 03:32:00 | NOAA-20 | IÚNA | ESPÍRITO SANTO | Brasil | 3203007 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 73db5a9d-4cb6-3669-81c8-1e1bdcaf586c | -18.61166 | -44.25726 | 2025-03-07 03:32:00 | NOAA-20 | INIMUTABA | MINAS GERAIS | Brasil | 3131109 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5c9e496b-981a-3ace-94e7-c28f8e574b9b | -19.89774 | -43.90875 | 2025-03-07 03:32:00 | NOAA-20 | BELO HORIZONTE | MINAS GERAIS | Brasil | 3106200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| d2663ed4-1aee-31cf-b542-c3bfdfdab2d6 | -18.91078 | -39.94245 | 2025-03-07 03:32:00 | NOAA-20 | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 57e385cb-bf1d-3b22-bcbf-8bb234344fe2 | -23.25362 | -47.12908 | 2025-03-07 03:32:00 | NOAA-20 | CABREÚVA | SÃO PAULO | Brasil | 3508405 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 3951c9d9-820d-3fae-94ff-60900d3d8d28 | -22.65448 | -42.8917 | 2025-03-07 03:32:00 | NOAA-20 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 9332e45a-65c0-34ac-b338-967e2ad87507 | -19.71556 | -40.35345 | 2025-03-07 03:32:00 | NOAA-20 | JOÃO NEIVA | ESPÍRITO SANTO | Brasil | 3203130 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| bb428a4b-6411-3b68-aa21-bfe1655e61bc | -19.89835 | -43.90575 | 2025-03-07 03:32:00 | NOAA-20 | BELO HORIZONTE | MINAS GERAIS | Brasil | 3106200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| dbee9c2c-df5b-3c04-93e6-324cd6fbba08 | -22.65104 | -42.88593 | 2025-03-07 03:32:00 | NOAA-20 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| bad0fe34-3ca2-3610-8372-4475e5f3daef | -23.20012 | -50.81406 | 2025-03-07 03:32:00 | NOAA-20 | URAÍ | PARANÁ | Brasil | 4128401 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 9240edd8-35ff-3ec8-9089-1f7f34e196c7 | -22.69518 | -43.43264 | 2025-03-07 03:32:00 | NOAA-20 | NOVA IGUAÇU | RIO DE JANEIRO | Brasil | 3303500 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 127291a6-352c-3935-ae44-072503fd6b7a | -22.85469 | -42.98236 | 2025-03-07 03:32:00 | NOAA-20 | SÃO GONÇALO | RIO DE JANEIRO | Brasil | 3304904 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 17ee792c-2f53-323a-a16f-3c8ddb3b7991 | -22.65201 | -42.88121 | 2025-03-07 03:32:00 | NOAA-20 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 54bdd3a6-ae50-3d60-a636-83cff7641d77 | -30.36892 | -51.96899 | 2025-03-07 03:34:00 | NOAA-20 | SÃO JERÔNIMO | RIO GRANDE DO SUL | Brasil | 4318408 | 43 | 33 | nan | nan | nan | Pampa | 5.7 |
| 7f36b878-bd37-3e27-84a4-b65b2b071a8a | -28.08747 | -51.44603 | 2025-03-07 03:34:00 | NOAA-20 | CAPÃO BONITO DO SUL | RIO GRANDE DO SUL | Brasil | 4304622 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 5fad9cc3-54b7-3637-9bd1-42de1013140d | -30.36749 | -51.97416 | 2025-03-07 03:34:00 | NOAA-20 | SÃO JERÔNIMO | RIO GRANDE DO SUL | Brasil | 4318408 | 43 | 33 | nan | nan | nan | Pampa | 5.7 |
| 58a14fda-e9e8-3606-8ee4-dd043b3694f8 | -28.08591 | -51.4519 | 2025-03-07 03:34:00 | NOAA-20 | CAPÃO BONITO DO SUL | RIO GRANDE DO SUL | Brasil | 4304622 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 8cdf96d1-be16-393c-b11f-9b425b6878b0 | -30.36609 | -51.97337 | 2025-03-07 03:34:00 | NOAA-20 | SÃO JERÔNIMO | RIO GRANDE DO SUL | Brasil | 4318408 | 43 | 33 | nan | nan | nan | Pampa | 10.6 |
| 27add663-45d9-32c3-9477-d482c235bfce | -28.53655 | -51.82465 | 2025-03-07 03:34:00 | NOAA-20 | SÃO DOMINGOS DO SUL | RIO GRANDE DO SUL | Brasil | 4318051 | 43 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| a9e31c8d-2bf3-3178-98f6-168ddf0f7e3d | -4.057 | -40.01664 | 2025-03-07 04:21:00 | NOAA-21 | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| d1926188-f768-3ef7-aeb8-7c362274e27a | -4.05733 | -40.019 | 2025-03-07 04:21:00 | NOAA-21 | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 5e8c2c5d-8f3b-377f-810b-e187242b8117 | -12.90651 | -45.07465 | 2025-03-07 04:23:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1de2a700-7008-3b04-bf29-8b855a436550 | -10.39894 | -47.98327 | 2025-03-07 04:23:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d223fefb-e7b2-362e-b846-9d162aaa865f | -15.91331 | -43.91301 | 2025-03-07 04:23:00 | NOAA-21 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Caatinga | 0.6 |
| d1648efb-38bc-302d-9230-2243171743f7 | -22.32854 | -48.53481 | 2025-03-07 04:23:00 | NOAA-21 | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| e604d267-00b5-3bbe-a3e5-c05d17e8395a | -10.76517 | -51.84652 | 2025-03-07 04:23:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 39797cea-915e-32e9-aaae-835e80d4c97d | -22.5764 | -44.89521 | 2025-03-07 04:23:00 | NOAA-21 | LAVRINHAS | SÃO PAULO | Brasil | 3526605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 6cf5bc92-773b-354a-8669-f7956670d094 | -16.6128 | -43.34132 | 2025-03-07 04:23:00 | NOAA-21 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5dabe1ff-9d61-3285-8021-63374fb6def8 | -20.63275 | -47.39043 | 2025-03-07 04:23:00 | NOAA-21 | FRANCA | SÃO PAULO | Brasil | 3516200 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 297e33d9-c0ec-3700-a1ed-efd4c317395f | -22.8203 | -42.44158 | 2025-03-07 04:23:00 | NOAA-21 | ARARUAMA | RIO DE JANEIRO | Brasil | 3300209 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 986de0e1-e1da-3a88-b6b4-81194b9c8fec | -23.12007 | -46.38359 | 2025-03-07 04:23:00 | NOAA-21 | NAZARÉ PAULISTA | SÃO PAULO | Brasil | 3532405 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 5feca71e-ff3e-39eb-82aa-2968288a1dc6 | -16.11142 | -47.9811 | 2025-03-07 04:23:00 | NOAA-21 | VALPARAÍSO DE GOIÁS | GOIÁS | Brasil | 5221858 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d98aa45d-0ce4-38c9-99fd-753612de4192 | -15.56828 | -46.26818 | 2025-03-07 04:23:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5d4e8389-7790-3c41-8133-838395e4c580 | -15.57104 | -46.27231 | 2025-03-07 04:23:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e733548b-2b5e-39d6-bfba-929ad80953fa | -17.09398 | -43.80352 | 2025-03-07 04:23:00 | NOAA-21 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e0c0a935-fd1b-32a4-8f13-f11496ea3b81 | -12.3042 | -47.27136 | 2025-03-07 04:23:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 924e8ae5-2b34-399d-a163-da76c9b88408 | -23.20354 | -50.80723 | 2025-03-07 04:23:00 | NOAA-21 | URAÍ | PARANÁ | Brasil | 4128401 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| ad5c36e8-e520-397a-9b7d-44b8151bedb3 | -15.57056 | -47.85543 | 2025-03-07 04:23:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9d110d11-bc22-3b51-a7c7-dcf0b27d08f2 | -16.75709 | -47.73376 | 2025-03-07 04:23:00 | NOAA-21 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 0fb2fa3b-aa4b-3f6d-b6f8-49f17a45284c | -10.7254 | -42.32988 | 2025-03-07 04:23:00 | NOAA-21 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 9b512e92-7766-3a4a-b676-d35ae92d879e | -20.99751 | -51.79675 | 2025-03-07 04:23:00 | NOAA-21 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |


[Clique aqui para ver as próximas entradas](README2.md)
