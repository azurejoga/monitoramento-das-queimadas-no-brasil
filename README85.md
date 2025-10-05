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

## Dados Diários - Página 85

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5045363e-10f4-3bd9-af0c-0c3144498edf | -11.62419 | -52.25039 | 2025-10-05 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1ece6522-3d1c-3cec-b276-6a0f5ac6800d | -13.35149 | -47.19743 | 2025-10-05 04:46:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f692af67-c556-3432-b45b-ebeaae8d10c7 | -7.0415 | -42.76228 | 2025-10-05 04:46:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| c61b8e5f-b868-3810-9bd9-a04c218de830 | -12.30855 | -55.13787 | 2025-10-05 04:46:00 | NOAA-21 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 444749f7-a950-3a56-858b-7d94ea00db98 | -9.37057 | -43.02814 | 2025-10-05 04:46:00 | NOAA-21 | VÁRZEA BRANCA | PIAUÍ | Brasil | 2211357 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| e1bb595c-b0d4-3c10-a85a-6f5218fc3a27 | -7.51122 | -41.27197 | 2025-10-05 04:46:00 | NOAA-21 | JAICÓS | PIAUÍ | Brasil | 2205201 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 14c43436-a879-335a-849c-54657d10ed7b | -11.8392 | -45.07573 | 2025-10-05 04:46:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 86a8a98c-66d0-3692-a17c-42a8085d9da8 | -11.57886 | -46.76769 | 2025-10-05 04:46:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 2c0bdc05-8326-3ffc-90e5-59e3190e285a | -13.7035 | -47.35907 | 2025-10-05 04:46:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ba54b234-acd2-37b1-ac68-f92dfcf5c8be | -13.30151 | -48.12336 | 2025-10-05 04:46:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3be5207a-099c-3cce-861d-d6976ecb19a8 | -10.80025 | -51.00141 | 2025-10-05 04:46:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4cfabd21-65ba-3146-b4ee-d33fac4be9cc | -8.1735 | -55.07084 | 2025-10-05 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 31b38a18-b538-3f37-badf-665a40c0a902 | -11.96239 | -51.4719 | 2025-10-05 04:46:00 | NOAA-21 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 965e2591-169e-38e4-93dd-823279ae0865 | -11.51748 | -47.67216 | 2025-10-05 04:46:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8350a626-68c4-3335-854d-9932072e4bcc | -13.49128 | -47.27106 | 2025-10-05 04:46:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4a257e2a-d0c2-392f-81b7-a6dc917cb9af | -6.98989 | -44.21519 | 2025-10-05 04:46:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a257ea92-02c0-30bd-9540-322259cc9781 | -7.01241 | -40.3201 | 2025-10-05 04:46:00 | NOAA-21 | CAMPOS SALES | CEARÁ | Brasil | 2302701 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 8659608d-9093-33f4-9eba-de4b3dcebc22 | -10.9447 | -47.09121 | 2025-10-05 04:46:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 767c13c0-7e2d-3dd6-9d0b-d0811c5b9dff | -8.85797 | -46.83828 | 2025-10-05 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 695fbafd-3717-36f5-a698-a9b8f393d863 | -10.94761 | -47.06996 | 2025-10-05 04:46:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4d9029af-8043-3d66-98d9-f3e984ea674f | -7.19154 | -42.93505 | 2025-10-05 04:46:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| af4c754f-ca39-300c-9188-6ab18e1ad284 | -7.11017 | -45.09464 | 2025-10-05 04:46:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c999d929-81f0-3491-be19-7bbd01cf4ee5 | -13.31834 | -47.56345 | 2025-10-05 04:46:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4adc3dd9-5a30-3fc2-802f-421b41791792 | -8.89479 | -47.97659 | 2025-10-05 04:46:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| f483983c-231c-36f4-8215-46cb9f84a7df | -9.52453 | -45.58219 | 2025-10-05 04:46:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6fda6e9a-c970-3b65-8f8f-385dbbf0e98b | -13.39035 | -47.55663 | 2025-10-05 04:46:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 87dbdf0b-1a73-33b4-8d1c-3f716974b9e6 | -8.13212 | -44.11369 | 2025-10-05 04:46:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e54bfd41-42f2-326d-bbb9-81fc0686dd56 | -5.62154 | -51.93941 | 2025-10-05 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0f4ceb9c-6229-3596-95d2-43076f4b061a | -13.33614 | -47.18676 | 2025-10-05 04:46:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 63ac3bab-6b9c-36e9-9bfa-429cb23cfffc | -6.68663 | -42.85101 | 2025-10-05 04:46:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 3ec2ceaa-2db5-3543-aeb4-a6dd9667d2e5 | -11.25981 | -47.78543 | 2025-10-05 04:46:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3a64758f-61f8-34b5-878c-0b53952ca41a | -13.11222 | -47.86672 | 2025-10-05 04:46:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 598404a9-839c-3a61-8faa-33d1385ad88d | -13.35767 | -47.58681 | 2025-10-05 04:46:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 4f2f635b-24cd-3a35-92ea-8d178af1312f | -13.28672 | -47.58532 | 2025-10-05 04:46:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 36a9ae92-5f51-3573-9ce5-73ef1ed54388 | -13.4644 | -47.28422 | 2025-10-05 04:46:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b4b6771c-5cab-30f6-89f3-15796d8a874a | -11.11483 | -49.85862 | 2025-10-05 04:46:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4a267ddd-4a2c-31f8-932f-6540efdf1918 | -8.55189 | -44.781 | 2025-10-05 04:46:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 294a3e0b-fa91-30f0-8835-7e8ea06564a6 | -12.81582 | -50.53268 | 2025-10-05 04:46:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d735bef7-7758-3b9a-942f-061ff1f64b09 | -8.87071 | -46.72069 | 2025-10-05 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 98c29241-24a5-39e8-a8d7-147822d040ec | -12.60143 | -48.13738 | 2025-10-05 04:46:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d0670f48-d5b5-3854-a705-e3d504fb918a | -6.29525 | -45.93219 | 2025-10-05 04:46:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 4abfa14b-95b0-3360-b657-51d347bf970c | -8.56074 | -46.26856 | 2025-10-05 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 4ef6a986-48d1-38b0-961d-26a58dab02f8 | -13.08608 | -47.91132 | 2025-10-05 04:46:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 518a5ab9-82c5-3af0-941d-ac19de6b7cdc | -12.39148 | -51.09011 | 2025-10-05 04:46:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cfb48673-4157-3507-a37d-fe426956c45d | -8.54057 | -46.32128 | 2025-10-05 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 75e6465c-eb8a-3b35-885b-697681ad34c9 | -7.76934 | -42.6202 | 2025-10-05 04:46:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 34f579d5-9742-3ebe-b912-4dc66febc66e | -9.90733 | -45.95369 | 2025-10-05 04:46:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 529e7a3e-b997-3dd5-9782-7124948ea93f | -12.88685 | -47.28689 | 2025-10-05 04:46:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 78c30607-a366-3cf4-bb68-a7fcf6a42e8e | -11.78818 | -47.91865 | 2025-10-05 04:46:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 45245ef1-4d1b-3e63-a95a-bd859af034b4 | -13.34675 | -47.59482 | 2025-10-05 04:46:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| a09da113-8c1b-302a-8e0c-be1ab93d0e6d | -13.43555 | -47.78307 | 2025-10-05 04:46:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 004dc0e8-874c-3626-8376-67ead90ee95b | -13.08991 | -47.9434 | 2025-10-05 04:46:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 699601c5-507d-3e81-bfc6-2af4a046fff7 | -12.53449 | -54.74261 | 2025-10-05 04:46:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5915604c-aae9-385c-a56f-db532ff9a40f | -6.11747 | -47.05353 | 2025-10-05 04:46:00 | NOAA-21 | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4d5e1871-740a-322a-97fc-6bea73a3670b | -12.30569 | -55.13326 | 2025-10-05 04:46:00 | NOAA-21 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7252413c-2ea7-39c4-8d8b-d7d2d2997349 | -8.16872 | -47.19294 | 2025-10-05 04:46:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| e32a07c6-a89c-3868-b2bf-383d920cabe5 | -8.54167 | -47.68547 | 2025-10-05 04:46:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| cf3bad17-4cd5-3550-9fcb-f5a1df51cafe | -8.60531 | -46.27484 | 2025-10-05 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| b313caaa-d84c-32e0-8dd6-debf253ceb22 | -7.42809 | -46.49643 | 2025-10-05 04:46:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ab1a8c2e-88ff-3b56-b626-357b8324ff87 | -11.54718 | -47.68705 | 2025-10-05 04:46:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d1df9a2a-bd83-3832-9937-fdba19c86654 | -10.57881 | -48.68593 | 2025-10-05 04:46:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1d409f5d-dca6-3728-a83b-8d7a189b3f66 | -7.80317 | -42.56467 | 2025-10-05 04:46:00 | NOAA-21 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 78839fef-3c99-3776-b933-e9452b9cd640 | -12.32634 | -55.14416 | 2025-10-05 04:46:00 | NOAA-21 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8f5b06e0-d35f-3561-9a61-ba717f47eff2 | -8.65431 | -54.95757 | 2025-10-05 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ac7c6e28-bd65-307e-8518-eeca0503824c | -13.68777 | -47.35211 | 2025-10-05 04:46:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 93850f62-af12-348d-a03b-b07e7c164140 | -7.21047 | -46.8604 | 2025-10-05 04:46:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| ec72d52e-f892-37f5-abfb-b56a7e6b5525 | -8.77742 | -49.89586 | 2025-10-05 04:46:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ad6165dd-8efb-36e0-b469-db929256fa0d | -13.34716 | -47.59191 | 2025-10-05 04:46:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 1591ccc7-430e-32f9-8cca-0767299df372 | -11.77908 | -47.94039 | 2025-10-05 04:46:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 70957a62-a87d-31ac-a104-b829876deee8 | -7.78037 | -42.60699 | 2025-10-05 04:46:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| af6c44ee-09e2-364c-b058-81d97b1ddde8 | -10.31089 | -50.37927 | 2025-10-05 04:46:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d0be573a-8960-322c-adc1-01ffd56fbcc2 | -7.23978 | -44.88696 | 2025-10-05 04:46:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 02158712-d86c-3650-8be0-7f68ae9700ae | -8.58035 | -46.30408 | 2025-10-05 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| c1589b72-f4d9-3ec6-8721-e92d42b7d699 | -10.00863 | -48.26575 | 2025-10-05 04:46:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6c2c8d33-53db-3733-8087-4e2dd2b492e7 | -12.31052 | -55.12583 | 2025-10-05 04:46:00 | NOAA-21 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 051f8e5a-9980-36b6-9428-f8ae816746ec | -6.95559 | -50.33031 | 2025-10-05 04:46:00 | NOAA-21 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3edc3c12-452a-3993-8647-d3b8efed5b59 | -13.3794 | -47.54642 | 2025-10-05 04:46:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 0a0f0cb5-18f0-32fd-b701-43a3e05cea47 | -10.74489 | -47.89289 | 2025-10-05 04:46:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9c44cb95-17f2-3b79-bf2d-9f1816e63309 | -8.55863 | -47.67419 | 2025-10-05 04:46:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0e1b080e-bcb3-311d-843e-ca754808252e | -8.61923 | -54.96185 | 2025-10-05 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8d6dee25-524f-3f9f-b24e-4c908a949c3e | -9.26119 | -51.80487 | 2025-10-05 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 12190353-937b-336d-9329-cfef0feca161 | -8.55437 | -44.78421 | 2025-10-05 04:46:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 96e9f375-c1e8-3f1e-b6d1-cbc15fa5ac02 | -6.55962 | -46.00657 | 2025-10-05 04:46:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d3dc5fa2-9600-312a-bd92-a59bef2ac9be | -11.87071 | -44.96589 | 2025-10-05 04:46:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7c6eb6ca-226e-3b4e-99ab-4be287c6e477 | -10.84012 | -57.18845 | 2025-10-05 04:46:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| eb618c95-67a4-3bf7-8200-78967104ee3e | -7.75396 | -46.32151 | 2025-10-05 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4cb3e198-bf32-3d2e-b29d-56b25c0f4397 | -13.29519 | -47.81941 | 2025-10-05 04:46:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9908fec8-bd81-3d4b-8722-ae286254f26a | -11.67168 | -43.89941 | 2025-10-05 04:46:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 29fc1e67-4ad2-3313-b13f-3b0d14f63569 | -11.45036 | -51.50723 | 2025-10-05 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6a61b55c-53f8-314d-bbc9-6c383bbc2b64 | -9.30968 | -60.54575 | 2025-10-05 04:46:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e1c6d4e6-3b27-319f-8b38-bfd92e4f91f4 | -11.00203 | -57.04662 | 2025-10-05 04:46:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f5fd5ccb-9905-3501-b43c-8ecfc8e18f58 | -13.29451 | -47.61811 | 2025-10-05 04:46:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 92932fc5-d690-3373-8379-389c56d097af | -10.34174 | -50.39108 | 2025-10-05 04:46:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e301febd-141f-3b14-af71-9b237490a2b0 | -13.12955 | -47.97404 | 2025-10-05 04:46:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 40cd4100-3e30-31ef-9cfd-9bb3206f3b97 | -8.90464 | -46.683 | 2025-10-05 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 1132d68e-fd4a-371b-9016-a4f7218b8c85 | -11.45644 | -51.51181 | 2025-10-05 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 88f7c260-d904-35ed-adb4-49adf92cba88 | -11.14982 | -47.17131 | 2025-10-05 04:46:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| da0a5142-acc0-3ee9-afa9-138bacb2e104 | -11.13786 | -47.92839 | 2025-10-05 04:46:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| f409b46c-db16-3e36-aad4-ef3e3cf417d9 | -12.41489 | -51.1089 | 2025-10-05 04:46:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 137f3bdb-ada6-3e9c-89ae-de370365cd55 | -12.89915 | -47.31841 | 2025-10-05 04:46:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |


[Clique aqui para ver as próximas entradas](README86.md)
