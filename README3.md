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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1d03aced-d904-35df-bf79-f857bd4f9172 | -1.0694 | -52.3876 | 2024-11-19 00:28:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0a72e1a9-5cd5-32a0-a66a-552178b0b7de | -3.7652 | -50.679401 | 2024-11-19 00:28:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fd67d9e6-b4a3-3923-bbe6-96b3e6eb02ff | -3.78 | -51.067101 | 2024-11-19 00:28:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f291e5e3-1efc-3a5e-8e0b-204cd0e94847 | -1.4776 | -52.095901 | 2024-11-19 00:28:00 | METOP-B | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e2207d06-d28f-3ec4-8ed8-c36a9d82de09 | -10.7542 | -44.3503 | 2024-11-19 00:28:00 | METOP-B | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 0404f9ec-8058-336a-92d2-3fba65df7f83 | -9.3302 | -36.007999 | 2024-11-19 00:28:00 | METOP-B | CAPELA | ALAGOAS | Brasil | 2701704 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 84985b2b-5b31-3cf7-a225-e9dba2cf683f | -2.0174 | -52.069801 | 2024-11-19 00:28:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 985749ae-bb97-303f-8864-375b246d9d5d | -3.248 | -50.394699 | 2024-11-19 00:28:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 70dd4d18-b589-3984-8b7e-367d71978d63 | -3.2765 | -50.612598 | 2024-11-19 00:28:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 69f084d8-9775-3b9f-87d4-aa3934d846d9 | -3.3188 | -50.480099 | 2024-11-19 00:28:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4699add0-ea15-3bcd-b250-42a562014eb8 | -3.3731 | -52.795502 | 2024-11-19 00:28:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 94f000f0-69ae-3ff6-ae0a-10195aa2c9de | -20.099501 | -47.4576 | 2024-11-19 00:28:00 | METOP-B | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| edf5213a-3002-3169-b203-2e5edd6a5397 | -6.3948 | -44.724499 | 2024-11-19 00:28:00 | METOP-B | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e79f5cae-b14a-31c7-909a-d3d2d28c6dda | -5.9734 | -45.348099 | 2024-11-19 00:28:00 | METOP-B | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 097806b9-83c7-301a-a5ab-6ecaf26b130e | -9.244 | -44.9967 | 2024-11-19 00:28:00 | METOP-B | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| e80abfa5-7959-383e-a2dc-6d58ba9bb355 | -2.3808 | -45.805801 | 2024-11-19 00:28:00 | METOP-B | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| c4c2ec3e-3647-3684-ab2d-fbeeaf82f2c0 | -3.039 | -49.466599 | 2024-11-19 00:28:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| eb92abd8-c338-35ae-b9bf-8c9f946e73e4 | -3.2013 | -52.439499 | 2024-11-19 00:28:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4d6152d7-b014-3810-97f6-92bd20d1d39b | -3.6162 | -54.216702 | 2024-11-19 00:28:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a4fd33ae-6c14-305b-a3e1-a324d27cc47e | -2.7388 | -54.056198 | 2024-11-19 00:28:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6c63a47f-1f99-31e5-9168-ddebd04f3ce4 | -4.8635 | -50.525101 | 2024-11-19 00:28:00 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d34808ac-6bcc-3028-9aa5-b4ad026fcc45 | -9.2538 | -44.9944 | 2024-11-19 00:28:00 | METOP-B | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| f4f429ce-d152-38db-ab74-38a3105a0dc7 | -4.221 | -47.182301 | 2024-11-19 00:28:00 | METOP-B | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 614c23ae-6577-3669-b78b-b2b79a4158ed | -10.9913 | -49.0116 | 2024-11-19 00:28:00 | METOP-B | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 172e2df6-b7ce-35bf-a16c-6519a168d198 | -1.4069 | -52.423199 | 2024-11-19 00:28:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a6a75729-c73f-348f-8586-100534881d2b | -3.76 | -52.4081 | 2024-11-19 00:28:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5a645703-b13f-3cd3-b665-7bac3bfe9f61 | -2.6446 | -48.543701 | 2024-11-19 00:28:00 | METOP-B | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 06b182ec-126b-3f55-985f-380ab79c0590 | -2.3395 | -48.425098 | 2024-11-19 00:28:00 | METOP-B | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dbfd0139-42d7-304c-8d51-09b520074956 | -1.9266 | -46.52 | 2024-11-19 00:28:00 | METOP-B | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| eceefb46-8b6c-3977-9814-525e4ba843fc | -2.1305 | -53.631802 | 2024-11-19 00:28:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 817b66a5-6166-3624-b226-5cfa36493663 | -2.6566 | -51.7061 | 2024-11-19 00:28:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7acc7f90-0d36-3350-be42-7aa7a06abe55 | -6.2799 | -47.349201 | 2024-11-19 00:28:00 | METOP-B | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 60e4fe60-1f48-35e4-9a0c-7fa7a65fa282 | -2.1578 | -51.961601 | 2024-11-19 00:28:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 445ee658-f9aa-3404-94cc-877e4c0535bc | -7.3923 | -42.756802 | 2024-11-19 00:28:00 | METOP-B | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| ebbcf1c0-7f4b-3dce-9336-156cba214d11 | -3.6586 | -50.433899 | 2024-11-19 00:28:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 04f4f89e-71f2-307e-872f-7a316fa42235 | -1.9848 | -44.797798 | 2024-11-19 00:28:00 | METOP-B | MIRINZAL | MARANHÃO | Brasil | 2106805 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| c24ae6db-f40c-3a05-87c5-666211a8a1bb | -9.2322 | -44.990398 | 2024-11-19 00:28:00 | METOP-B | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 82d6d6bf-34cc-3649-b8c9-99c1d5523dfb | -3.5095 | -50.228802 | 2024-11-19 00:28:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8409d63b-56b7-356f-ad35-c406e169ab90 | -4.9821 | -44.3237 | 2024-11-19 00:28:00 | METOP-B | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| cdd52d86-c5ec-3092-ba1b-0a468d5b8d47 | -2.9192 | -49.119099 | 2024-11-19 00:28:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5091b4f4-0ff2-3c71-a5e2-851dfa92d340 | -4.1843 | -48.5606 | 2024-11-19 00:28:00 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fa432808-6269-3fc3-b295-53b63bdbbbf7 | -1.3679 | -52.066299 | 2024-11-19 00:28:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6ec1a271-8bfa-35c4-bd9b-ac9aeda2154e | -3.5565 | -50.254398 | 2024-11-19 00:28:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7d471f9b-c5bf-38c9-9eb4-b43cae5feed4 | -2.7641 | -52.601101 | 2024-11-19 00:28:00 | METOP-B | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 512095c3-f0e3-3055-ba62-254227c47470 | 0.3872 | -50.861698 | 2024-11-19 00:28:00 | METOP-B | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 7a3263dc-7b6e-3bf7-a820-0205db1e7ae1 | -3.3219 | -50.493801 | 2024-11-19 00:28:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0d0ce1ec-ff2e-37dd-a5a1-d2bcc8c40434 | -2.6743 | -46.2328 | 2024-11-19 00:28:00 | METOP-B | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| c8275cc0-251e-37fc-a738-1e10eded37d4 | -3.6021 | -54.199299 | 2024-11-19 00:28:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ba852ce4-302f-341f-ba69-4b02b33e9cd6 | -2.4846 | -49.02 | 2024-11-19 00:28:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 570eb9ad-9c65-3f0a-aa94-91ca7a9e9805 | -3.7816 | -51.0742 | 2024-11-19 00:28:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8bcce7a3-404a-31d4-a1be-f7fa544e63de | -8.25 | -44.018799 | 2024-11-19 00:28:00 | METOP-B | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| fbe47b60-06ee-3ef0-9e4e-13ad9ae5bf02 | -2.7526 | -52.595402 | 2024-11-19 00:28:00 | METOP-B | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5d8377ae-dd01-36db-a10a-741bb3ca03e6 | -2.9818 | -45.151901 | 2024-11-19 00:28:00 | METOP-B | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| fcdfc613-683c-3274-b81f-ffc9011aa72d | -4.8117 | -43.685101 | 2024-11-19 00:28:00 | METOP-B | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ce15b231-0167-3acc-8720-3074cfe71583 | -4.3495 | -45.2784 | 2024-11-19 00:28:00 | METOP-B | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 4dead7dc-6d6a-3b99-9e2d-2433705621b9 | -4.865 | -50.532101 | 2024-11-19 00:28:00 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8e6fa18f-0740-3e03-a1de-73499a8fde90 | -4.9846 | -44.334301 | 2024-11-19 00:28:00 | METOP-B | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e1567c83-114a-3950-ab0a-15649114c1a0 | -2.7606 | -52.5854 | 2024-11-19 00:28:00 | METOP-B | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 909edef0-7708-39a4-b57d-ba8d437600b8 | -2.8943 | -53.0467 | 2024-11-19 00:28:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c7715c93-f7f1-3699-9ff8-b09b7f15d775 | -5.9268 | -39.6474 | 2024-11-19 00:28:00 | METOP-B | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 2ae6f173-fb32-3aec-a0b7-94ef8dc70b1c | -1.0677 | -52.380199 | 2024-11-19 00:28:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fc8180ea-db40-32fd-99ad-225428ea1c05 | -9.9746 | -44.7229 | 2024-11-19 00:28:00 | METOP-B | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 5a536f6c-b64d-39de-a570-27bbe085c406 | -10.835 | -44.255299 | 2024-11-19 00:28:00 | METOP-B | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 5f50fb33-facb-325e-a7ad-f8d19bf12c2c | -2.7876 | -48.6744 | 2024-11-19 00:28:00 | METOP-B | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1a2adb72-9012-31e1-8a03-04db7949d4be | -3.1644 | -44.295898 | 2024-11-19 00:28:00 | METOP-B | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 48202d26-c234-3670-8d93-9ebb1f179d6d | -3.3122 | -52.706799 | 2024-11-19 00:28:00 | METOP-B | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cb77d50c-509f-32bc-9ed4-1e69391657f5 | -3.5777 | -50.669701 | 2024-11-19 00:28:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| db136765-de09-30cc-901a-0de89956ee86 | -5.5043 | -46.439899 | 2024-11-19 00:28:00 | METOP-B | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a70c8dfb-55c1-3b36-aef7-56e4bc7d58fa | -2.6829 | -51.869301 | 2024-11-19 00:28:00 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 31d5ca89-c7a9-3d30-9f93-1d26a1a9d7eb | -1.9363 | -46.517799 | 2024-11-19 00:28:00 | METOP-B | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7463332e-dcc0-3b80-af8f-7620a59a286c | -6.0513 | -44.051399 | 2024-11-19 00:28:00 | METOP-B | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ff072f28-9074-3d8c-9d1e-273902b00cde | -2.4409 | -49.145901 | 2024-11-19 00:28:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8f3d6baa-9976-3e56-962c-614f787e6ac1 | -13.26 | -56.785198 | 2024-11-19 00:28:00 | METOP-B | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 471b12b6-4ffb-3654-8d53-c479fd9260d1 | -4.543 | -48.006599 | 2024-11-19 00:28:00 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 24051d66-98cb-3289-96cb-f14a8d63af18 | -4.295 | -46.740398 | 2024-11-19 00:28:00 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| f1a3112b-2293-39eb-b449-031030ed5267 | -3.4997 | -50.230999 | 2024-11-19 00:28:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e0ab08c9-8232-39b0-baec-98e53c092377 | -1.237 | -52.034 | 2024-11-19 00:28:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 24a89ef5-f9b5-3fa6-8293-35ae450f71a5 | -1.6951 | -45.8223 | 2024-11-19 00:28:00 | METOP-B | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 60b4b914-fa78-361b-ab24-6a471066069f | -2.8448 | -51.5811 | 2024-11-19 00:28:00 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 449f5ae9-2feb-3cf1-998b-ec82c4fcd246 | -13.2464 | -56.766499 | 2024-11-19 00:28:00 | METOP-B | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 441759a6-3c19-3b3a-a903-f2217c8e0f93 | -9.8426 | -48.565201 | 2024-11-19 00:28:00 | METOP-B | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f1fc6a0f-9d6c-38f2-b94f-8e68b4602e7c | -1.7531 | -46.301399 | 2024-11-19 00:28:00 | METOP-B | BOA VISTA DO GURUPI | MARANHÃO | Brasil | 2101970 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 3805c883-8b23-33b0-8120-aa11893a35c7 | -3.0276 | -49.462002 | 2024-11-19 00:28:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e2fbcb23-d585-3c57-8259-06f344c05543 | -2.483 | -49.0131 | 2024-11-19 00:28:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f91f893e-15f3-306d-a8cd-e5d9a8d139c6 | -2.3213 | -45.680901 | 2024-11-19 00:28:00 | METOP-B | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| d8881504-85a0-3ec4-b65d-75eb28cc3fab | -1.9815 | -45.5452 | 2024-11-19 00:28:00 | METOP-B | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| c846f509-0e87-3bad-a0f0-0d6ab020dc53 | -1.0579 | -52.382301 | 2024-11-19 00:28:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 04847c9c-170b-3309-be24-500f2cc8ca7b | -2.8363 | -46.669998 | 2024-11-19 00:28:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5b71e528-6063-3b89-8631-a10f276ad4ed | -3.5644 | -51.438099 | 2024-11-19 00:28:00 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 153aadb4-e9b2-321e-8828-3255ff3ff2bb | -9.2342 | -44.999001 | 2024-11-19 00:28:00 | METOP-B | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| b9fb5ee2-a7c8-33ba-9da4-b0e481d9508d | -3.755 | -51.923401 | 2024-11-19 00:28:00 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b6013d6f-d6f1-31ce-a403-a04acad7eaac | -1.1449 | -46.749401 | 2024-11-19 00:28:00 | METOP-B | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3ada8da7-b4ec-32d0-adbe-0a9a89037180 | -2.9841 | -45.1619 | 2024-11-19 00:28:00 | METOP-B | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 747e88a1-7756-37f1-b34d-cef7d2b6b494 | -3.5663 | -50.2523 | 2024-11-19 00:28:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d3dc3480-f87c-3269-905c-5999b711ab6b | -10.9622 | -44.531898 | 2024-11-19 00:28:00 | METOP-B | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 0547d68b-173a-3c01-be2c-767820898d62 | -1.6106 | -53.284599 | 2024-11-19 00:28:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a2d22bf2-bfe7-3e67-bf70-afb0566cf5b7 | -10.9643 | -44.540501 | 2024-11-19 00:28:00 | METOP-B | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| bf3a9760-49a7-3fa1-93a3-a08b49a1fcda | -5.9776 | -45.366001 | 2024-11-19 00:28:00 | METOP-B | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 933fcdb4-eddc-3596-8d50-79ad9a36542b | -0.1114 | -51.427898 | 2024-11-19 00:28:00 | METOP-B | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| a702f827-cd2d-3f89-8f4d-9c7461faa820 | -2.3787 | -45.796501 | 2024-11-19 00:28:00 | METOP-B | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README4.md)
