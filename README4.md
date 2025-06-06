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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a207fc31-fb1c-3278-aaff-c2098912a9ad | -8.9508 | -50.01151 | 2025-06-06 04:14:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1ddb7e75-6622-38fa-840e-8f6b7c6ed425 | -7.73188 | -44.18346 | 2025-06-06 04:14:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 0f8dc5b3-e139-35d4-8644-519424450723 | -8.09075 | -46.75209 | 2025-06-06 04:14:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| dc6a4484-d53f-3e13-871f-e2d9694c03a0 | -6.19973 | -48.54641 | 2025-06-06 04:14:00 | NOAA-21 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 40a48cb8-ac85-38e8-8a42-34a4f17f59f1 | -6.23906 | -48.56414 | 2025-06-06 04:14:00 | NOAA-21 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 96b6ce97-ba4f-302a-ac20-66c52d31622a | -8.46424 | -46.48573 | 2025-06-06 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f4a75b24-eb6b-36e1-b1dd-1dd3d7881276 | -7.01437 | -44.61049 | 2025-06-06 04:14:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 0d5f35e3-7576-3c59-b490-4ffde4ad21ff | -10.65909 | -44.48757 | 2025-06-06 04:14:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 2f7d1f8a-6109-3559-9578-5d3e55befc38 | -7.50118 | -43.31284 | 2025-06-06 04:14:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c2173dcd-3417-3f28-95c4-c90466a62643 | -7.55387 | -45.83006 | 2025-06-06 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1abceff9-b924-3c86-b062-7bf5e09f1084 | -8.7277 | -47.98972 | 2025-06-06 04:14:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a9259a9d-a1f0-3f19-af30-09e1d141e2af | -6.23844 | -48.56791 | 2025-06-06 04:14:00 | NOAA-21 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 072482b5-68be-3d98-a198-af89fbe31fb0 | -10.46068 | -47.95468 | 2025-06-06 04:14:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 062aa4e7-e7b8-34a9-bf36-688bcc755521 | -7.01159 | -44.6064 | 2025-06-06 04:14:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| ef90733e-903e-376a-a370-07f9713f945e | -10.29105 | -47.03701 | 2025-06-06 04:14:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3074488b-e0b2-38e9-902f-7424bcdb22da | -4.97413 | -47.81518 | 2025-06-06 04:14:00 | NOAA-21 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e974efa2-e000-33e4-86d1-c4d4f5be29b8 | -9.84104 | -48.61039 | 2025-06-06 04:14:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 61c90119-e8aa-3554-a3a7-1162e30fad93 | -6.05235 | -44.17063 | 2025-06-06 04:14:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5b701642-6bfc-3dd9-a334-43096f6c3f87 | -7.67383 | -41.97077 | 2025-06-06 04:14:00 | NOAA-21 | CAMPINAS DO PIAUÍ | PIAUÍ | Brasil | 2202109 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 382ab5e0-5fb7-3f87-b35b-a77c2b16e01b | -3.99616 | -43.24513 | 2025-06-06 04:14:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4a3e05b6-8fd5-3f36-bb71-5c1df22c7dab | -5.82922 | -47.0402 | 2025-06-06 04:14:00 | NOAA-21 | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ed2ba85b-be45-3f87-a8b3-a61d30ee9d24 | -7.55449 | -45.82625 | 2025-06-06 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 593cf1df-d4ea-3394-9e3e-1235dbd5bf52 | -8.72675 | -47.90171 | 2025-06-06 04:14:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 43f70cb1-3e38-3869-b79b-1c3a74cbcf79 | -7.67328 | -41.97438 | 2025-06-06 04:14:00 | NOAA-21 | CAMPINAS DO PIAUÍ | PIAUÍ | Brasil | 2202109 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 42e3c7c8-ad8c-30b2-9e54-68855e810e6e | -9.05522 | -48.80223 | 2025-06-06 04:14:00 | NOAA-21 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Amazônia | 0.7 |
| dde2ee70-22fe-3111-8cae-50cb8cb2e0ac | -7.01606 | -44.5998 | 2025-06-06 04:14:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 77a44732-7909-36eb-87a3-113dd2fa2701 | -8.47162 | -49.60891 | 2025-06-06 04:14:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.2 |
| 9fe23740-4917-3c76-b2bc-411770ef1a6c | -10.46145 | -47.95015 | 2025-06-06 04:14:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 11.3 |
| d45c6686-3f91-3614-870c-caf573d30230 | -9.05014 | -47.02372 | 2025-06-06 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 67bb54a6-fc54-32b5-80c7-9ce60aaffb96 | -3.40387 | -47.58366 | 2025-06-06 04:14:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5fac1ebd-42df-396f-916e-23b6cd781739 | -6.21169 | -55.64876 | 2025-06-06 04:14:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c6ac958f-f685-3d40-aee5-81f52ed184a1 | -9.52678 | -54.77374 | 2025-06-06 04:14:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 63412271-15ab-3264-ba7b-40a03c0af737 | -7.01941 | -44.60034 | 2025-06-06 04:14:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7f144b85-d1b7-39dd-bf11-bb3b3fa71c68 | -10.46517 | -47.95077 | 2025-06-06 04:14:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 53c1940b-b3f5-3586-8c07-bad875ee9ee4 | -8.72294 | -47.90107 | 2025-06-06 04:14:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 71c838ef-4ccd-37d9-bdc8-af6babec4216 | -8.47554 | -46.4827 | 2025-06-06 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 38678685-86a5-30ce-a49d-7a28ef4096d2 | -5.90081 | -44.13972 | 2025-06-06 04:14:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d90a3825-00fe-3ede-8855-a15d644062a4 | -6.2081 | -43.33352 | 2025-06-06 04:14:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 17fd8991-28e2-3299-9a41-4bb1de335356 | -6.98795 | -47.08892 | 2025-06-06 04:14:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f5eda1e8-e433-31b5-870f-c68f00f7e4e6 | -8.4607 | -46.48513 | 2025-06-06 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9362ebd9-b559-3fd3-97f7-3ca090edd4cc | -9.21789 | -48.8594 | 2025-06-06 04:14:00 | NOAA-21 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 67fb5edd-df27-3457-8da6-fa9e3bd92817 | -3.40791 | -47.58427 | 2025-06-06 04:14:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 34adecfc-59e9-3374-b3b5-e1480257671d | -6.2114 | -43.33404 | 2025-06-06 04:14:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b6e170f1-0fa8-39d5-a577-54c982285bb1 | -4.00332 | -43.2427 | 2025-06-06 04:14:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6eb6cb9d-c436-3250-9a6d-0b8a4bf62e6b | -5.68174 | -41.40274 | 2025-06-06 04:14:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 04e882af-afc4-3749-9563-285d183b46c2 | -7.01215 | -44.60283 | 2025-06-06 04:14:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| e1d81128-494d-3439-b589-fad9bc1d4f4d | -3.9967 | -43.24168 | 2025-06-06 04:14:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| da3db9e1-5d9c-36c9-b81b-d55423309b77 | -7.01324 | -44.61761 | 2025-06-06 04:14:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8c7db421-89b8-3ac0-9469-ee7cc0809f84 | -9.07431 | -47.14634 | 2025-06-06 04:14:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d5d5c447-f148-3a93-abc2-6457c261aefd | -7.90788 | -50.36896 | 2025-06-06 04:14:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 2eab44c6-b9b0-325f-bf72-4e6ef673ccfe | -7.19532 | -43.13694 | 2025-06-06 04:14:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 2b4be602-f12d-3d16-8bab-98899012aa53 | -10.46441 | -47.95528 | 2025-06-06 04:14:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| c9d3947c-e5e9-3970-8195-c6feac927c20 | -7.72636 | -44.17543 | 2025-06-06 04:14:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 1b2510a5-2e7c-32c1-9826-eb4feabe38b2 | -9.07793 | -47.14695 | 2025-06-06 04:14:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 41cf9c20-f00b-31a1-93a8-81b9342086cf | -6.19586 | -48.56931 | 2025-06-06 04:14:00 | NOAA-21 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| a9e3d85c-2abe-3e5c-aa93-d35b01b3f13b | -7.00766 | -44.60949 | 2025-06-06 04:14:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| b4ca83d6-830f-38df-9599-26ee7a40a3ea | -9.60528 | -49.01916 | 2025-06-06 04:14:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 58e8c528-c037-3e81-ae29-ec78533b027f | -8.67239 | -44.26332 | 2025-06-06 04:14:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 750401b7-5c42-3da3-87f4-736e5c22903a | -7.01102 | -44.60997 | 2025-06-06 04:14:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| e66323b8-7833-3c6d-b8eb-1599e6448282 | -9.67019 | -48.71354 | 2025-06-06 04:14:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c5b9f205-cff4-3299-9232-fa4727d77098 | -7.43907 | -37.21053 | 2025-06-06 04:14:00 | NOAA-21 | SÃO JOSÉ DO EGITO | PERNAMBUCO | Brasil | 2613602 | 26 | 33 | nan | nan | nan | Caatinga | 1.8 |
| c807a904-31e6-3241-8fd7-fa26dd51cf94 | -6.20062 | -48.56623 | 2025-06-06 04:14:00 | NOAA-21 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a052216b-e1ec-39a1-9fc3-8f1ad9aa2885 | -10.85614 | -46.84907 | 2025-06-06 04:14:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 262c1e6c-c141-3566-9e53-5fd91702f43c | -7.02219 | -44.60447 | 2025-06-06 04:14:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 59211914-81b0-3f57-8785-49358552981c | -9.70232 | -49.48014 | 2025-06-06 04:14:00 | NOAA-21 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0a67a56a-7cbc-3ff4-936f-7bb3508f973f | -7.0088 | -44.60234 | 2025-06-06 04:14:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 44216926-5922-341b-a6e2-494a9993ae2c | -7.72305 | -44.17491 | 2025-06-06 04:14:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 9.8 |
| f5300aed-72ef-33d6-911a-58467e431bc8 | -16.37961 | -48.85579 | 2025-06-06 04:17:00 | NOAA-21 | ANÁPOLIS | GOIÁS | Brasil | 5201108 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d7e2c0a4-9082-3a82-935e-0acd520e08f9 | -14.23459 | -45.48732 | 2025-06-06 04:17:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b6a6bd8b-933d-33ee-9c8b-8d41310121b3 | -14.74424 | -45.10292 | 2025-06-06 04:17:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 352f23e4-0998-34dc-95af-e6ed43d6781f | -12.95397 | -46.77356 | 2025-06-06 04:17:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| b9056dba-9066-38e9-b96f-5485f8be5567 | -17.25541 | -43.64256 | 2025-06-06 04:17:00 | NOAA-21 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0aad43ba-0781-35db-9a72-e26256348acf | -14.12296 | -44.83371 | 2025-06-06 04:17:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 29f12c57-dd36-3c45-ac61-3aa265189500 | -12.5253 | -58.35968 | 2025-06-06 04:17:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 48c376e9-67f7-394f-b018-0d76e253ca08 | -13.88286 | -54.68055 | 2025-06-06 04:17:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| ded9239e-9ec7-3e51-bd86-a3a7b8c0b5b6 | -13.51992 | -56.5747 | 2025-06-06 04:17:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 5aa91553-8c89-39a3-b4cf-f1fbf4931863 | -10.70744 | -48.78254 | 2025-06-06 04:17:00 | NOAA-21 | FÁTIMA | TOCANTINS | Brasil | 1707553 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a887dd38-e49e-3f91-b360-3e56b69e36d0 | -17.75695 | -42.89504 | 2025-06-06 04:17:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1cf2e64b-1bbc-3623-9616-7b0bec7c73ce | -14.22354 | -45.49277 | 2025-06-06 04:17:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 63e66ce7-6354-3361-9541-4967b2fcd8a7 | -11.92483 | -54.82392 | 2025-06-06 04:17:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 15.4 |
| 68f942b8-b669-353e-9032-bee1acedf09a | -16.5698 | -54.51945 | 2025-06-06 04:17:00 | NOAA-21 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4e0f421a-a702-3497-9af2-e9ef319ae53e | -13.88355 | -54.67711 | 2025-06-06 04:17:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| bb1ecbf2-5a3f-3225-8a6e-4eb598cc433f | -14.22411 | -45.48922 | 2025-06-06 04:17:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 61ed7f15-4fff-3253-b537-5dae6f7a06e5 | -11.38327 | -56.55509 | 2025-06-06 04:17:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| a23b25bf-2e01-33a8-b574-e73a2393c99c | -12.53228 | -58.36082 | 2025-06-06 04:17:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 6aa5eea0-cfce-3a90-b25c-245550d7115f | -12.38523 | -47.31293 | 2025-06-06 04:17:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 85dd8236-c1e5-340b-8282-87551abf94ac | -12.96019 | -46.77858 | 2025-06-06 04:17:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 70405d65-b5d7-3525-9029-eb9317da7358 | -12.28553 | -43.53986 | 2025-06-06 04:17:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2be3ce2c-f989-3172-99b2-bbbbaf286390 | -11.51376 | -49.81821 | 2025-06-06 04:17:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 26cb9195-5d5f-336a-b1d3-83ac031ab721 | -12.66991 | -58.21799 | 2025-06-06 04:17:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c81486fb-e36f-3f3b-96fd-c55f23a35fc3 | -11.38962 | -56.55639 | 2025-06-06 04:17:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 15b6e3d4-d05c-31de-ba8f-b774a18aaf2f | -12.96424 | -46.77534 | 2025-06-06 04:17:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8d5c71ee-3538-368c-a688-5842812a514e | -12.27118 | -55.07679 | 2025-06-06 04:17:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 414a70d3-8b9b-3a1f-aba7-133995ab90fc | -11.11965 | -54.66256 | 2025-06-06 04:17:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1e52ed5f-fc53-3a87-b099-dd74da7987eb | -10.99263 | -49.02182 | 2025-06-06 04:17:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 652914ca-3172-3a29-b17e-8a096dff0543 | -13.57155 | -44.26535 | 2025-06-06 04:17:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 74faedb3-4e8c-31bc-ba67-35c2766fc10a | -12.53278 | -58.35537 | 2025-06-06 04:17:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 1bb376cd-623d-3a70-9e80-0dc776fef2b6 | -12.83791 | -47.38719 | 2025-06-06 04:17:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| bdd1bf1c-1bd5-3535-ade5-a4d2d8bbe401 | -10.87082 | -49.54559 | 2025-06-06 04:17:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 73984ee0-d6f1-3b77-9f1f-0b7c9823270b | -10.704 | -57.64373 | 2025-06-06 04:17:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 7.9 |


[Clique aqui para ver as próximas entradas](README5.md)
