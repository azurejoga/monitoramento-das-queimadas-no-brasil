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

## Dados Diários - Página 42

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9d63df7e-498b-3a5a-af7f-b1fc8ba86137 | -7.49127 | -42.55727 | 2025-11-15 04:25:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| f90e7683-42dd-3542-844f-d6baaa29cb1b | -3.28296 | -45.46331 | 2025-11-15 04:25:00 | NOAA-20 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9e7f42e9-d1e2-32d3-a88f-c72f51e7aa3b | -7.53261 | -47.14652 | 2025-11-15 04:25:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 57180f97-e4d4-3576-843b-faba32e918d0 | -5.75913 | -42.7316 | 2025-11-15 04:25:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 5eb5b476-872e-3e20-873b-9c634fc90323 | -2.87028 | -51.47456 | 2025-11-15 04:25:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a0b884f5-c306-3250-b4ae-313349502942 | -8.30693 | -46.22431 | 2025-11-15 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 8cd477d7-2c39-30ec-8575-78ecede86012 | -9.81941 | -45.33328 | 2025-11-15 04:25:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 6e2f8f0d-f03b-3370-bf30-280219becc86 | -4.04143 | -46.12584 | 2025-11-15 04:25:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3bb22615-4936-3c06-8153-0adc026d604d | -9.96976 | -44.94209 | 2025-11-15 04:25:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ea9f486e-8c34-317c-b0eb-4f52dc71eddd | -4.10691 | -50.06434 | 2025-11-15 04:25:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| d1af6b88-399d-35d7-8d81-be78a7fa3db0 | -4.56942 | -45.70848 | 2025-11-15 04:25:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| cd3aa38b-cba4-3eec-bf73-5d810ecab60c | -3.0106 | -49.43103 | 2025-11-15 04:25:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1025d21f-23b3-3a21-8561-51c887ee9423 | -5.02479 | -44.51147 | 2025-11-15 04:25:00 | NOAA-20 | SÃO JOSÉ DOS BASÍLIOS | MARANHÃO | Brasil | 2111250 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9f456216-125b-3db3-97d6-bfbab0daba5e | -3.35744 | -52.14273 | 2025-11-15 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d330f1c1-b2dd-3feb-a34c-8f84fe69c227 | -5.74571 | -42.72148 | 2025-11-15 04:25:00 | NOAA-20 | AGRICOLÂNDIA | PIAUÍ | Brasil | 2200103 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 98a68471-7e28-3c81-a706-943deaf44883 | -7.52165 | -47.19487 | 2025-11-15 04:25:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 699d4289-bb7f-38f0-8483-1cbdc3d5f379 | -2.73304 | -45.31015 | 2025-11-15 04:25:00 | NOAA-20 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 91f9883a-ee6c-3623-9a5f-37c9955b9914 | -4.53873 | -43.21753 | 2025-11-15 04:25:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| e0f21522-75a8-3594-b221-40cfcc5f724a | -7.34503 | -46.01119 | 2025-11-15 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6079f13d-1e7f-3899-99b7-89ea25925436 | -5.51743 | -40.97623 | 2025-11-15 04:25:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 2868ba3d-e4c8-3167-b7f6-4fd32dd59115 | -5.99736 | -44.06382 | 2025-11-15 04:25:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e4ce21b8-4663-391b-a4b3-27da232d3e7d | -5.02302 | -46.83576 | 2025-11-15 04:25:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a3b023bb-1372-3250-8df5-0a266db5bdb2 | -2.20377 | -46.54648 | 2025-11-15 04:25:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7bdf6b89-202f-3cac-b925-1215f3880c30 | -1.83331 | -53.80445 | 2025-11-15 04:25:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 32d30c93-43d3-3af1-8a29-b2dc7c8af43f | -3.52914 | -53.00282 | 2025-11-15 04:25:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 505e6c3d-88b2-3fa4-8ba1-7f47a1e8ae50 | -4.38611 | -50.42751 | 2025-11-15 04:25:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3e186b50-9a17-3cfc-93b6-de6a818069c3 | -3.22159 | -45.48527 | 2025-11-15 04:25:00 | NOAA-20 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 6.8 |
| d35b8a14-a275-3eeb-9bb7-31bf8905d7cd | -7.33049 | -42.88894 | 2025-11-15 04:25:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| c1441b49-f9ad-3a37-a1b9-9bcf77b8149a | -2.681 | -49.86403 | 2025-11-15 04:25:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7f875816-b15e-3532-b14a-ce4d67dc86c0 | -9.0136 | -44.18249 | 2025-11-15 04:25:00 | NOAA-20 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 897e2d68-2af9-3f9e-9fe3-653fbe849bd0 | -4.8196 | -47.60284 | 2025-11-15 04:25:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| cb15ec8d-c2f7-3ae5-8271-fe82c87c0d68 | -4.53812 | -43.22147 | 2025-11-15 04:25:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 10.7 |
| c2308454-e456-3d42-9322-4876417cefd4 | -5.77312 | -44.38057 | 2025-11-15 04:25:00 | NOAA-20 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4f3b3710-de99-33a4-8346-2517dd770222 | -3.47405 | -45.65197 | 2025-11-15 04:25:00 | NOAA-20 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 65ad6d47-a64b-393a-ba18-a9314776d988 | -8.9954 | -44.18367 | 2025-11-15 04:25:00 | NOAA-20 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d6d784da-4fd1-3465-a95c-e8c51e421c69 | -8.29832 | -43.84233 | 2025-11-15 04:25:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 796d70ce-3119-3f3b-9cbd-a65001973dbd | -5.32997 | -43.03949 | 2025-11-15 04:25:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 347a2250-3ca9-3d83-a421-b5fd5db089b5 | -4.21249 | -50.40674 | 2025-11-15 04:25:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e293fab6-47f0-3caa-bfbb-c6482ca433e9 | -6.30008 | -41.82584 | 2025-11-15 04:25:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 6a1e0a1c-1ec7-33fb-b0ec-9bd7b6b90658 | -6.14843 | -48.04469 | 2025-11-15 04:25:00 | NOAA-20 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| f44aafc2-edee-3b07-84e9-8f64da7fba1d | -3.14219 | -49.23796 | 2025-11-15 04:25:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c42c9464-15d7-3d23-99a9-fc6a65455e0c | -4.73018 | -47.15735 | 2025-11-15 04:25:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 25.8 |
| aeb9db66-5e97-3e16-876b-3fe1612a0b59 | -7.88765 | -48.40061 | 2025-11-15 04:25:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d9b45f58-c39e-3422-b226-9de6cfc97217 | -6.09118 | -47.94159 | 2025-11-15 04:25:00 | NOAA-20 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ae056ff1-1533-3455-946c-c530e4c4329d | -7.88086 | -48.39946 | 2025-11-15 04:25:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| f6cf31fc-6e30-34c1-b742-276f9340acc2 | -9.18534 | -45.70469 | 2025-11-15 04:25:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 13b5bf65-bdcd-3d19-a8ed-0f9137852834 | -3.79744 | -52.01198 | 2025-11-15 04:25:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 08be0c5c-ca76-3c14-80cc-d12a3a7344bb | -7.26926 | -48.03151 | 2025-11-15 04:25:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| dacb9ee3-8bf1-36dc-9ad7-7a1fbfeb3b29 | -9.62929 | -45.17928 | 2025-11-15 04:25:00 | NOAA-20 | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 843b2bbe-3d4b-3f62-ada1-51321ea5bce1 | -5.8857 | -42.27309 | 2025-11-15 04:25:00 | NOAA-20 | SÃO MIGUEL DA BAIXA GRANDE | PIAUÍ | Brasil | 2210383 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 6160de0c-c85f-3d25-a024-d50f5fde5ab1 | -7.44578 | -42.76395 | 2025-11-15 04:25:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 89fea423-1a6d-3f15-9f20-edae0fb2fdf0 | -9.86348 | -44.71374 | 2025-11-15 04:25:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e47fc3f7-a902-3ce7-a65b-a5766826e93c | -7.53088 | -47.19987 | 2025-11-15 04:25:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0176f434-7285-3ed1-a464-274623e9b057 | -2.55227 | -45.33474 | 2025-11-15 04:25:00 | NOAA-20 | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 337d0502-be2e-3baa-b227-888dd148e07b | -4.34925 | -48.64188 | 2025-11-15 04:25:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 76c39498-8e67-353b-b970-6f7945a2a1fd | -6.29944 | -48.65619 | 2025-11-15 04:25:00 | NOAA-20 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e8c29cef-5927-372a-9920-45b91367e459 | -9.02449 | -48.74569 | 2025-11-15 04:25:00 | NOAA-20 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 40d4c341-03c3-3ccc-a820-e1568a1f6d91 | -6.0179 | -41.96312 | 2025-11-15 04:25:00 | NOAA-20 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 11.7 |
| 49fd698a-4641-39fc-ba11-64ba4321d1da | -4.41785 | -50.82753 | 2025-11-15 04:25:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a124528b-4da7-3a02-be6b-be1840bd47c7 | -3.47459 | -45.64854 | 2025-11-15 04:25:00 | NOAA-20 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0dd76429-8983-306b-93de-e41bc28e6ab9 | -3.45636 | -50.11634 | 2025-11-15 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 1a4aef08-ae2b-38f4-8ca1-6e501227a3d3 | -5.66662 | -46.52807 | 2025-11-15 04:25:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7a6d37e6-69ea-3d30-9386-477f7527e535 | -3.47735 | -45.65249 | 2025-11-15 04:25:00 | NOAA-20 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 098a8678-9207-317f-bc8f-7e4ea8f8194b | -3.40869 | -46.90268 | 2025-11-15 04:25:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ac1694c5-6974-3781-95e9-cfa8f3452366 | -8.89832 | -44.29905 | 2025-11-15 04:25:00 | NOAA-20 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e584a36e-e00d-3157-bd13-d8515c296a25 | -3.86905 | -48.04327 | 2025-11-15 04:25:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 34587861-f237-3015-8e2e-dba3fc98f112 | -7.49279 | -47.33374 | 2025-11-15 04:25:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d645c6f6-3da7-3a02-933e-faf40a987b9c | -2.72974 | -45.30964 | 2025-11-15 04:25:00 | NOAA-20 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ec7ba126-f832-3789-b551-604935492faa | -6.08377 | -47.04682 | 2025-11-15 04:25:00 | NOAA-20 | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 9d0a2317-636e-3062-916a-07d8e9f95d1f | -5.62694 | -43.92432 | 2025-11-15 04:25:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6a1e3a63-a0a0-3049-9713-feb1eadc52da | -3.45903 | -50.12006 | 2025-11-15 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 5c042fea-b6eb-30cf-b2af-f9e5582f555f | -3.86187 | -47.99925 | 2025-11-15 04:25:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1c01d521-df81-3100-842e-adeec6e9cd07 | -5.03524 | -43.6079 | 2025-11-15 04:25:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 9133352f-9def-3ed5-966c-57ff1f3a1ab9 | -5.6298 | -43.92864 | 2025-11-15 04:25:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e9e830ee-1cfa-371d-bb77-94fd32034daa | -5.74471 | -46.27167 | 2025-11-15 04:25:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 13711e60-0fe4-354b-8e8a-ee690b9b836a | -2.73851 | -45.29693 | 2025-11-15 04:25:00 | NOAA-20 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0ce51723-ade2-3a3e-8320-abc34e3ed4d0 | -8.53682 | -49.58834 | 2025-11-15 04:25:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3f79dc67-f196-3a1d-ba6a-727367f7cce6 | -4.79008 | -48.67096 | 2025-11-15 04:25:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 559df86c-2857-3638-a312-e75032d5f228 | -4.25307 | -48.65131 | 2025-11-15 04:25:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d3695a42-b4c2-323c-b70b-20c910f8eb6f | -7.06159 | -48.32196 | 2025-11-15 04:25:00 | NOAA-20 | CARMOLÂNDIA | TOCANTINS | Brasil | 1703883 | 17 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d318a655-b6f1-3b12-8ad1-d586a7e2d803 | -4.41326 | -50.8304 | 2025-11-15 04:25:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9dd6f322-6c8e-31f0-98b3-28b3d43d2108 | -2.86963 | -51.47861 | 2025-11-15 04:25:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 141f9146-bf8e-3d0b-b80d-7e72b4c6b829 | -4.43863 | -43.65555 | 2025-11-15 04:25:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 36a26b01-664f-32c1-93aa-9bf61b88797c | -5.38022 | -44.72021 | 2025-11-15 04:25:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 79b5b6de-2a4b-342b-8528-d2a5b3175bf3 | -4.24832 | -48.21174 | 2025-11-15 04:25:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c1c05eb3-2bc9-3967-90c7-67c952fbb91e | -4.33137 | -45.90327 | 2025-11-15 04:25:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 8b5be45f-ee91-38be-b89a-edefe1df89f7 | -3.26432 | -43.61462 | 2025-11-15 04:25:00 | NOAA-20 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| fd21a5df-1660-3412-b6ca-7c311f8bed52 | -4.69141 | -45.68927 | 2025-11-15 04:25:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 155f8270-7751-3dae-95aa-73d979856238 | -7.45121 | -42.76645 | 2025-11-15 04:25:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 5d727335-8d16-317b-a51d-6e5fe290380b | -6.88884 | -42.06235 | 2025-11-15 04:25:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| adfdcc8b-ca05-31c3-872b-2b846a4a0edc | -3.78659 | -42.44723 | 2025-11-15 04:25:00 | NOAA-20 | SÃO JOÃO DO ARRAIAL | PIAUÍ | Brasil | 2209971 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cdd3b68e-8f57-3166-aeb8-d0f260a23d87 | -4.16142 | -46.14095 | 2025-11-15 04:25:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9db9799a-b180-3e5e-a779-6451c4fa1d68 | -9.21107 | -48.59047 | 2025-11-15 04:25:00 | NOAA-20 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 58b95855-da73-3205-8809-3f5bbaee926b | -4.33198 | -45.29645 | 2025-11-15 04:25:00 | NOAA-20 | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 835f6200-d127-343c-a44d-4d6ecfd68c8c | -4.80406 | -45.42715 | 2025-11-15 04:25:00 | NOAA-20 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f954e702-e8bd-37f4-b25b-c4297f26743f | -2.80343 | -52.97079 | 2025-11-15 04:25:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d08395ff-5698-3791-9878-e2ad7e30c275 | -7.43282 | -45.22872 | 2025-11-15 04:25:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cef0e23e-4a28-376b-9bb9-c39cd083fafe | -4.86218 | -43.25602 | 2025-11-15 04:25:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f2ccb991-8410-33f9-838e-9d9daba5e3a3 | -3.98766 | -48.00298 | 2025-11-15 04:25:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| db4ab596-26ab-37d9-88bf-717a9a6b0f8c | -5.0671 | -43.68969 | 2025-11-15 04:25:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |


[Clique aqui para ver as próximas entradas](README43.md)
