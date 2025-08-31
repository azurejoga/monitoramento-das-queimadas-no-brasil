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

## Dados Diários - Página 32

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5eb5aff5-6ac3-39d0-b3b5-01c8ceaba8b8 | -6.30542 | -43.52186 | 2025-08-31 04:27:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1dbfc982-f57e-3bab-9898-d13111b10940 | -8.88825 | -45.08538 | 2025-08-31 04:27:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d7f81879-c9c4-3376-af7e-9865918b7eb3 | -7.41326 | -42.0559 | 2025-08-31 04:27:00 | NPP-375D | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 015ed5b3-a563-38e7-83d8-c4cf5b119e4f | -8.55267 | -51.30154 | 2025-08-31 04:27:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| cf720a59-217d-3ed3-b7e0-9b8e47ae9588 | -8.29598 | -46.31841 | 2025-08-31 04:27:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a6ae156c-6583-34cd-a54f-0e8358242023 | -7.97298 | -46.41779 | 2025-08-31 04:27:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 04b3c7e0-587c-3a76-977e-570794560c2e | -6.33444 | -53.43637 | 2025-08-31 04:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5f6deb34-e374-3359-9aea-1858ac9edbf4 | -6.93229 | -45.57034 | 2025-08-31 04:27:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 34d9038a-123c-3980-b958-95e7e1ffd975 | -6.17039 | -44.00412 | 2025-08-31 04:27:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3fa0c057-8bc0-30f6-a0f6-4c8434116435 | -6.30587 | -43.54231 | 2025-08-31 04:27:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 924eefa1-d6d8-3369-9e5f-f17173dc0686 | -6.26953 | -43.85062 | 2025-08-31 04:27:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 738f7a7d-c9e6-3da6-970f-bf4f9ae84db1 | -8.38385 | -47.38977 | 2025-08-31 04:27:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 06c732c5-9b6a-396d-8c4e-3c0b079da69a | -6.17561 | -43.99321 | 2025-08-31 04:27:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d5f8f464-7749-3629-a176-812e68e2d14e | -6.44599 | -43.98724 | 2025-08-31 04:27:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 50b64dab-e3d4-3df6-b34f-d114b0644493 | -7.58467 | -42.72415 | 2025-08-31 04:27:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 8ff5fc03-b564-3d4b-a5eb-7c1e9ceb3626 | -7.1145 | -44.7604 | 2025-08-31 04:27:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3148e54b-8506-3eb9-a34c-7df46b98ffe1 | -4.14738 | -46.45021 | 2025-08-31 04:27:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 412625ff-5b5a-3cf5-a876-603027a32931 | -6.10047 | -43.1882 | 2025-08-31 04:27:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 8e543db6-0893-333a-97ce-a10448dd5d65 | -6.43794 | -43.97031 | 2025-08-31 04:27:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9c2722ad-194b-3cd5-b124-2673b0e079cd | -6.96997 | -40.94672 | 2025-08-31 04:27:00 | NPP-375D | ALAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2200251 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| c1867279-566f-3551-9d22-b7b663867a00 | -7.95797 | -46.38337 | 2025-08-31 04:27:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3a3d2571-0e3c-375b-b7f9-32feefec9cd2 | -8.78417 | -46.59324 | 2025-08-31 04:27:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0cda17d8-689c-37a6-a620-57a86cfe7815 | -8.29683 | -44.91693 | 2025-08-31 04:27:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 44c86aa9-e340-34eb-9dad-20f3b8492af5 | -6.55361 | -43.68608 | 2025-08-31 04:27:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2d258a70-23db-3c19-ac63-cc058dd0b52d | -7.57127 | -45.1201 | 2025-08-31 04:27:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3242a574-eec7-39a5-bc7e-592c318abab4 | -6.53923 | -44.4416 | 2025-08-31 04:27:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 804da4c6-9c62-3586-b357-48e6f19af7b5 | -7.39679 | -45.92991 | 2025-08-31 04:27:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b0e126d6-73b8-3173-b9d4-05c6b5bc8ead | -9.51008 | -45.39814 | 2025-08-31 04:27:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4095129d-4959-350b-aae6-3557ce7a4aff | -6.12605 | -42.94682 | 2025-08-31 04:27:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 7.6 |
| 29933d22-ebb0-3576-b55f-b1d3d4ed9070 | -6.28756 | -43.54379 | 2025-08-31 04:27:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3f3f8d77-80a9-34b4-8c9c-ba5ce2687f53 | -6.7104 | -51.41517 | 2025-08-31 04:27:00 | NPP-375D | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 0fd1fc0e-b347-35ee-a226-af5716a44d9a | -7.96688 | -46.41326 | 2025-08-31 04:27:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c97e1e2c-048a-3e38-8f1a-72deac5f930a | -5.73076 | -45.53324 | 2025-08-31 04:27:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d1f89bac-bb37-3df4-9907-78a57f75ba64 | -5.80852 | -43.8693 | 2025-08-31 04:27:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 4ee5ffd7-1942-3521-902a-f7393b8f675b | -9.51292 | -45.40229 | 2025-08-31 04:27:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6d785da6-900d-365c-9e26-09ac5b710834 | -8.72894 | -50.3808 | 2025-08-31 04:27:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 758ccab7-6df6-3254-855a-ffe34b28f8c3 | -5.9115 | -45.54352 | 2025-08-31 04:27:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 15d5843a-580d-3359-b0d0-d12a62e4d608 | -7.7278 | -50.26432 | 2025-08-31 04:27:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 10563d86-3ab5-3fc6-9c85-4c392ad6e2df | -7.58295 | -42.7101 | 2025-08-31 04:27:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 165ade75-9cc2-37e8-b569-9f3aa12dc836 | -6.53648 | -42.96465 | 2025-08-31 04:27:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 005cfda6-3d31-3360-8716-3cd4b26c68d3 | -7.6363 | -46.55671 | 2025-08-31 04:27:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d2ceef71-ac77-3b56-987c-5fc2606a3c70 | -8.15866 | -42.30546 | 2025-08-31 04:27:00 | NPP-375D | PEDRO LAURENTINO | PIAUÍ | Brasil | 2207934 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 26b9fb81-f0f7-34c9-b856-1813e8cd0b5a | -6.17206 | -43.56691 | 2025-08-31 04:27:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b7a2a279-6012-3334-bed8-ea0aa64daf3f | -7.20733 | -45.43665 | 2025-08-31 04:27:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d614071f-36e7-33c5-b829-4305dc1d068e | -4.73761 | -44.44746 | 2025-08-31 04:27:00 | NPP-375D | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 8fa876a4-5efe-3458-b780-319c3be2f034 | -6.42345 | -43.97195 | 2025-08-31 04:27:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f87667d9-5a1d-3c52-9b16-ec2a1675f702 | -7.21973 | -43.6386 | 2025-08-31 04:27:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0a8db290-a52b-3acb-8f6e-74450588fe5f | -6.58181 | -43.69011 | 2025-08-31 04:27:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 45857a6a-98f0-3553-be0e-5dbc432390d8 | -7.19729 | -45.43504 | 2025-08-31 04:27:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7474cbac-72bd-321e-902a-f9968addc855 | -7.85642 | -46.96011 | 2025-08-31 04:27:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c0369894-018e-3541-a666-9859860bdc3d | -7.41417 | -44.08553 | 2025-08-31 04:27:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a92ccdc6-9ca9-3759-8224-fae990b571b4 | -5.55215 | -43.73789 | 2025-08-31 04:27:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9c8d0a68-4834-3e04-930b-007005a9f1f8 | -7.95139 | -46.42508 | 2025-08-31 04:27:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d996633c-bcc6-371d-bca0-be69058cca32 | -8.46385 | -43.63217 | 2025-08-31 04:27:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 2f6ae0c9-aa0e-38c7-bba4-81be784a0302 | -7.70595 | -50.2757 | 2025-08-31 04:27:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f7b92a35-ebcc-32de-a626-69470a1cd22c | -7.41857 | -42.04663 | 2025-08-31 04:27:00 | NPP-375D | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| f670c812-21fb-348d-bc1e-fbf01f210de2 | -6.48721 | -44.07436 | 2025-08-31 04:27:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 97140212-0153-3822-9bd1-e93233fc480c | -4.50211 | -42.89973 | 2025-08-31 04:27:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f80c33d3-be3c-3727-8269-748ba19ad33a | -9.45145 | -40.68256 | 2025-08-31 04:27:00 | NPP-375D | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 0.7 |
| a417daea-c51d-3d1c-a89c-65281957f4af | -8.33029 | -47.42453 | 2025-08-31 04:27:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b063d210-3098-3874-9d26-c39d7922cb77 | -6.9485 | -44.30064 | 2025-08-31 04:27:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.2 |
| 2ce44ac5-1dec-3bfd-b4e0-4015b7d37f41 | -6.36365 | -43.56184 | 2025-08-31 04:27:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 041eebb0-45d0-3ca9-a0c4-a828dfa6530e | -6.85947 | -44.44422 | 2025-08-31 04:27:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4191fd88-e037-3300-a451-32ef1bc4dcf6 | -6.99799 | -44.36176 | 2025-08-31 04:27:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fb4c2616-5966-3bea-9d07-1938d6faebb8 | -8.83805 | -47.48831 | 2025-08-31 04:27:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2440306e-007d-30b6-983f-bb9cde1c3382 | -5.48265 | -44.39475 | 2025-08-31 04:27:00 | NPP-375D | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8c1d093f-719a-37db-87f3-f2d8b4b88841 | -5.82193 | -42.4897 | 2025-08-31 04:27:00 | NPP-375D | BARRO DURO | PIAUÍ | Brasil | 2201408 | 22 | 33 | nan | nan | nan | Caatinga | 21.2 |
| 4918059d-e0e9-3fde-b9f7-1b2c6eaf29c9 | -7.95078 | -46.38581 | 2025-08-31 04:27:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 74ea8ed1-459e-3c81-a23f-bbf26c350b1d | -7.2129 | -45.42302 | 2025-08-31 04:27:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 150e1ce2-89ec-32ed-9726-b9911424218d | -7.58975 | -42.71575 | 2025-08-31 04:27:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| ee3be55f-d171-35a7-aacf-10cf5dece086 | -6.43237 | -45.60701 | 2025-08-31 04:27:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e43b6bee-ad12-3aa5-a9e7-3d11bac15bfd | -7.62924 | -42.65723 | 2025-08-31 04:27:00 | NPP-375D | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| fd04634c-44a1-3baf-8adb-50bfdb2549f2 | -7.37459 | -43.40377 | 2025-08-31 04:27:00 | NPP-375D | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8fb806c4-a85e-3d28-9445-e016b855b67b | -5.69792 | -45.95829 | 2025-08-31 04:27:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0dcfdbbd-544c-3e10-8b54-8164ff32be20 | -6.98136 | -51.26342 | 2025-08-31 04:27:00 | NPP-375D | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1e63fd31-9105-3ce2-bf05-b483e5cf538a | -8.00965 | -44.05613 | 2025-08-31 04:27:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| da9c95c3-ff02-345b-9dfd-4efb2312a7d8 | -7.57071 | -45.1237 | 2025-08-31 04:27:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b1a4ce69-a9b9-3591-a5ca-9b9750afd8f6 | -8.86588 | -45.74829 | 2025-08-31 04:27:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f745a1e7-2882-376e-af1f-32b2e6c933ef | -7.10346 | -44.30781 | 2025-08-31 04:27:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cec39dab-021a-34c0-b4c3-962e1d1b2cb1 | -4.07109 | -47.95522 | 2025-08-31 04:27:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d30b48db-1979-30a1-99e6-3c52d466febc | -6.16626 | -44.16911 | 2025-08-31 04:27:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3b67be61-f53f-346e-8f25-302f6ed56b35 | -6.86004 | -44.44052 | 2025-08-31 04:27:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2e3e8a45-1100-35cc-8949-52115a905204 | -6.1369 | -43.32112 | 2025-08-31 04:27:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.5 |
| ddb096fc-625f-3447-9d94-8700a2910a4d | -6.16185 | -43.32492 | 2025-08-31 04:27:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4d59191b-e4f9-392f-b907-47b8fe756162 | -7.1023 | -44.31541 | 2025-08-31 04:27:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 34dcfbf0-5ffc-3e13-9c2c-f286c0b1ca01 | -6.56301 | -43.67163 | 2025-08-31 04:27:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a20bf61b-6b70-3daf-81fa-a1a21a365c4d | -8.46366 | -45.17084 | 2025-08-31 04:27:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bc756194-df3d-3c56-b148-6bb163537175 | -8.85857 | -45.72899 | 2025-08-31 04:27:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1e1f3994-19e9-3bd7-bdbe-89f12325c6f1 | -4.22459 | -47.21198 | 2025-08-31 04:27:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 49681a8e-8701-326f-9986-51ebbd0b3146 | -3.81764 | -41.55381 | 2025-08-31 04:27:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 10ecfc60-8c39-3d1a-89ab-baacf035713d | -6.55008 | -43.68555 | 2025-08-31 04:27:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 43f5c536-04ed-33a1-8d89-ac9404a7c497 | -7.71939 | -50.26422 | 2025-08-31 04:27:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4fd8dede-d959-31e7-9526-9664e2ae547e | -6.1766 | -43.3478 | 2025-08-31 04:27:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6ac58b5b-0d6f-3232-8378-ff8a6af5b806 | -6.53524 | -44.44482 | 2025-08-31 04:27:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8b7f2bbf-f44a-31aa-bd2b-66f1b25e4823 | -4.01426 | -47.72074 | 2025-08-31 04:27:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1f654ed6-4865-30e7-9274-249869c878e9 | -6.3135 | -43.60688 | 2025-08-31 04:27:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ead2f457-a423-3d15-b1f9-2c1203c06e95 | -3.80425 | -47.56881 | 2025-08-31 04:27:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e8888469-6c81-3515-9be6-267c12cbb683 | -7.44533 | -44.80729 | 2025-08-31 04:27:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b450328d-246e-3c6c-a5c5-7f4551d13e79 | -6.51511 | -43.54013 | 2025-08-31 04:27:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 39cfc566-29e1-39db-bbcb-35a113f912e7 | -7.63837 | -42.6515 | 2025-08-31 04:27:00 | NPP-375D | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |


[Clique aqui para ver as próximas entradas](README33.md)
