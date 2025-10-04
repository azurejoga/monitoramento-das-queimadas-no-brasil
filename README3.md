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
| 1ffe8277-f0ae-337a-83e0-8c04b29d82a8 | -2.9014 | -50.7142 | 2025-10-04 00:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 42.4 |
| 8d2a0795-03ec-3997-843e-2be85b17a2d1 | -4.4259 | -43.2175 | 2025-10-04 00:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 23.7 |
| 041e4d3d-2835-3da4-8780-9338473fede5 | -8.6136 | -54.9961 | 2025-10-04 00:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 46.6 |
| 5dbd57d7-1882-3244-91de-f1a2cf9ebbb2 | -13.9965 | -48.1763 | 2025-10-04 00:40:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 73.6 |
| 36e8c551-b0ac-3e07-8162-a1dcccc6faa9 | -5.1967 | -45.0541 | 2025-10-04 00:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 65.4 |
| b860afc5-9f97-3546-88de-f9d09e5caf70 | -16.0408 | -50.9395 | 2025-10-04 00:40:00 | GOES-19 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 76.4 |
| bfa6e5b5-df49-3573-a2df-ec09bac1c395 | -6.0433 | -42.4912 | 2025-10-04 00:40:00 | GOES-19 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 64.7 |
| 23b2612b-f96b-3cdf-a7a4-3734c81ac015 | -13.996 | -48.1987 | 2025-10-04 00:40:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 91.7 |
| 81dbe77f-4fd5-3214-b0ec-3b8779a2508f | -2.9013 | -50.7351 | 2025-10-04 00:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 53.6 |
| d396adde-345e-36a0-a269-5f94fad0453d | -12.3813 | -54.4603 | 2025-10-04 00:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 71.9 |
| 71f89037-c207-32c1-8714-9099290a9b2c | -4.3197 | -48.0908 | 2025-10-04 00:40:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 58.9 |
| 102eaf79-066f-3758-adee-a22374e84e2f | -16.0212 | -50.9425 | 2025-10-04 00:40:00 | GOES-19 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 149.1 |
| 24993f46-5fe5-3999-a42c-28adab36905d | -4.4445 | -43.2397 | 2025-10-04 00:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 518.9 |
| ec5859d5-6e3a-3ea6-a32b-0cc4638610c8 | -11.9147 | -46.3726 | 2025-10-04 00:40:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 181.4 |
| 57161735-00f5-3523-9074-1247b475349a | -4.9541 | -45.0468 | 2025-10-04 00:40:00 | GOES-19 | SÃO ROBERTO | MARANHÃO | Brasil | 2111672 | 21 | 33 | nan | nan | nan | Cerrado | 71.6 |
| e53ee442-c27e-3504-8297-dff203ba6ec7 | -6.0621 | -42.4897 | 2025-10-04 00:40:00 | GOES-19 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 88.7 |
| 78487a22-6969-3a6a-ad87-a635eed4f640 | -9.3464 | -54.5201 | 2025-10-04 00:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 137.7 |
| 51c0b836-5e33-3438-aefe-e258f7f8ef2b | -15.6019 | -52.4888 | 2025-10-04 00:40:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 92.0 |
| 79183528-d9e6-3da5-ba75-c880a0806e66 | -15.6023 | -52.4675 | 2025-10-04 00:40:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 49.4 |
| 0474daef-c1eb-3f72-bfd6-cf32e6ec8aa4 | -8.2316 | -46.8066 | 2025-10-04 00:40:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 135.2 |
| 60cf843d-2755-3fe3-95bc-e9ecd5446d90 | -4.954 | -45.0694 | 2025-10-04 00:40:00 | GOES-19 | SÃO ROBERTO | MARANHÃO | Brasil | 2111672 | 21 | 33 | nan | nan | nan | Cerrado | 182.4 |
| d8d96519-feca-3831-98ef-9549f6d26298 | -5.1965 | -45.0768 | 2025-10-04 00:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 60.5 |
| 5a233222-53ac-383b-bb41-e88bf0743785 | -5.4849 | -44.0982 | 2025-10-04 00:40:00 | GOES-19 | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 69.4 |
| 2a364657-1135-381f-82ee-5292b5d0cb92 | -3.8384 | -41.5729 | 2025-10-04 00:40:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 58.1 |
| aae5990f-3b9d-34d2-aabe-42355489fd46 | -4.4258 | -43.2408 | 2025-10-04 00:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 88.1 |
| a2ece4b2-d7bf-3e44-9132-09b29a5e3c1d | -9.3276 | -54.5215 | 2025-10-04 00:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 138.1 |
| 504f40f7-be62-3e8e-954c-93be2d7beb08 | -4.4845 | -42.8631 | 2025-10-04 00:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 41.8 |
| 925c8f8d-ac01-3fc2-8ea8-c2388bd16be3 | -13.3225 | -48.1216 | 2025-10-04 00:40:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 102.8 |
| 2acae25e-15ff-3e0f-97d1-f72eadcf4779 | -6.8774 | -47.2334 | 2025-10-04 00:40:00 | GOES-19 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 71.6 |
| ee57887d-bf6d-3531-9ef1-2dd8b18ab0c8 | -3.8572 | -41.5719 | 2025-10-04 00:40:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 86.7 |
| bc14e9b9-49a6-3ea1-ac07-961676d449a9 | -8.6322 | -54.9949 | 2025-10-04 00:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 76.6 |
| e7c094a5-2735-312e-a23d-3d5cefd8d575 | -9.3274 | -54.5418 | 2025-10-04 00:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 81.3 |
| ee7a1c0a-fdd0-3b8f-8efe-de737c57b436 | -11.9151 | -46.3499 | 2025-10-04 00:40:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 113.5 |
| ae775472-5b3c-3499-bfa3-31094c113655 | -4.4443 | -43.263 | 2025-10-04 00:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 198.9 |
| c738738c-15c8-3315-976e-9d21e84bbf22 | -15.7297 | -46.2707 | 2025-10-04 00:40:00 | GOES-19 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 77.3 |
| 28e7e0ae-58c8-3ced-be8e-d8dce7e174d6 | -8.2128 | -46.8084 | 2025-10-04 00:40:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 87.3 |
| 8f74f8e2-3618-3742-ad7a-8bfee02a8069 | -17.0855 | -43.3564 | 2025-10-04 00:40:00 | GOES-19 | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 64.1 |
| e4acd7a4-457c-3302-bb02-980f04290892 | -6.043 | -42.5149 | 2025-10-04 00:40:00 | GOES-19 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 115.2 |
| 174155cf-22b8-3385-87de-41082daf1765 | -17.0903 | -46.2347 | 2025-10-04 00:40:00 | GOES-19 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 97.1 |
| a6c8e5be-0937-318e-909e-7c8ce5189d66 | -4.4632 | -43.2386 | 2025-10-04 00:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 77.8 |
| e3eb6212-fb32-3c32-bf01-4d78f0e21872 | -8.2319 | -46.7844 | 2025-10-04 00:40:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 62.9 |
| 8c781d50-0214-339e-93dd-9567fe9755f2 | -4.4446 | -43.2164 | 2025-10-04 00:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 108.7 |
| 69049213-9b95-33d0-8d16-01d92ac45b82 | -13.3221 | -48.1439 | 2025-10-04 00:40:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 91.6 |
| daa99cfd-4bff-3381-bd20-5be47004e8eb | -6.0618 | -42.5133 | 2025-10-04 00:40:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 172.3 |
| 329996ce-6a6d-3a1e-8675-8b2bdffbaaf3 | -17.0704 | -46.2388 | 2025-10-04 00:40:00 | GOES-19 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 61.0 |
| 49b85272-0db7-390d-b793-ca53b6b511df | -9.3276 | -54.5215 | 2025-10-04 00:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 128.2 |
| a50146e3-9d31-32ae-84a0-dc385961ae39 | -3.8384 | -41.5729 | 2025-10-04 00:50:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 57.0 |
| ac9e2812-f458-3219-badf-ca166cbb5b4e | -17.7044 | -47.0821 | 2025-10-04 00:50:00 | GOES-19 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 52.7 |
| 8e59e35b-a055-39c9-8e1c-13b2e50adaa6 | -8.2316 | -46.8066 | 2025-10-04 00:50:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 113.7 |
| 1ffc7dd7-c0ef-31ca-8674-3b4e6e78c7b4 | -11.9339 | -46.3699 | 2025-10-04 00:50:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 80.1 |
| 8fdcfdf2-91c7-3136-89a6-9f43ac22069b | -13.996 | -48.1987 | 2025-10-04 00:50:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 83.2 |
| 4fb27fc5-83bd-3f95-b464-e636af176565 | -4.4443 | -43.263 | 2025-10-04 00:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 153.3 |
| 2ccc2c3c-9ce4-3f15-b280-bd87d8dab144 | -13.3028 | -48.1467 | 2025-10-04 00:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 66.6 |
| 6a64d9aa-8905-344e-a5e1-b681d8f0d6c7 | -8.6136 | -54.9961 | 2025-10-04 00:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 51.0 |
| e08ff983-bb33-3a10-ba07-8d945857df3b | -6.8774 | -47.2334 | 2025-10-04 00:50:00 | GOES-19 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 84.4 |
| adc5bc40-974b-3a2e-a520-64e13bbb0ea5 | -4.4258 | -43.2408 | 2025-10-04 00:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 85.2 |
| b21397a4-6d7c-357b-abe1-8a7b81ec000a | -11.9147 | -46.3726 | 2025-10-04 00:50:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 208.9 |
| 3a4a8bab-eb73-34bb-9f2b-8b2502018eab | -4.9541 | -45.0468 | 2025-10-04 00:50:00 | GOES-19 | SÃO ROBERTO | MARANHÃO | Brasil | 2111672 | 21 | 33 | nan | nan | nan | Cerrado | 59.2 |
| 5ecb2452-6dca-3558-9298-c02f8f6dad88 | -4.954 | -45.0694 | 2025-10-04 00:50:00 | GOES-19 | SÃO ROBERTO | MARANHÃO | Brasil | 2111672 | 21 | 33 | nan | nan | nan | Cerrado | 166.0 |
| 6e67a0af-6857-354c-942e-ab3b4d35b039 | -9.3274 | -54.5418 | 2025-10-04 00:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 83.9 |
| a75aa085-f4b4-3f58-b7b2-17933992b556 | -3.8572 | -41.5719 | 2025-10-04 00:50:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 78.3 |
| ecda1b24-7cca-3b32-9ffe-afeaf7db3b77 | -4.4445 | -43.2397 | 2025-10-04 00:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 426.9 |
| 829faafd-44ae-342d-9c03-791e691c23f4 | -11.9151 | -46.3499 | 2025-10-04 00:50:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 137.1 |
| b2bd5fd0-6dea-37d5-a3da-dc230b48ed96 | -13.3229 | -48.0993 | 2025-10-04 00:50:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 85.9 |
| cee7fe65-0115-38d3-a95f-58340af44be1 | -13.3422 | -48.0965 | 2025-10-04 00:50:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 59.4 |
| 22464483-acec-3df4-9dea-cdf4dd63c57c | -15.2205 | -56.8414 | 2025-10-04 00:50:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 86.0 |
| d40d7f35-8128-3e17-87b0-8f1eee3d32d7 | -9.3464 | -54.5201 | 2025-10-04 00:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 128.3 |
| 76cfd803-c4e7-3884-8f6f-60d892d2f414 | -5.1967 | -45.0541 | 2025-10-04 00:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 69.1 |
| e4eb03e4-c4e3-321a-8dcf-84a5415d1827 | -4.4446 | -43.2164 | 2025-10-04 00:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 54.5 |
| a67f1a6a-f69d-3d2f-b435-ff0ae1df527a | -14.2321 | -46.0794 | 2025-10-04 00:50:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 71.5 |
| edb18615-b02f-3b1f-ae64-b75f7f007be8 | -17.0903 | -46.2347 | 2025-10-04 00:50:00 | GOES-19 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 78.1 |
| ed18dcd9-f864-39fd-87ea-531819f560bc | -13.3032 | -48.1244 | 2025-10-04 00:50:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 68.8 |
| 28f0de44-2150-3ea3-a414-280736d741d1 | -13.3225 | -48.1216 | 2025-10-04 00:50:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 148.8 |
| bfb396ca-bd39-3b7d-9bfd-b15557898956 | -5.1965 | -45.0768 | 2025-10-04 00:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 74.6 |
| 1484e7f7-693f-3b45-9b5c-59d364ed94b1 | -4.4632 | -43.2386 | 2025-10-04 00:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 62.8 |
| db79fa25-1765-3d38-bb0e-cb679fac4c6b | -16.0212 | -50.9425 | 2025-10-04 00:50:00 | GOES-19 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 161.1 |
| 0de17b2d-2810-340e-af1b-bed65c8a0d8c | -8.2128 | -46.8084 | 2025-10-04 00:50:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 84.1 |
| 977f8413-bbc5-3500-a2ea-af5f665acce1 | -2.9013 | -50.7351 | 2025-10-04 00:50:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 55.1 |
| 276f590b-e4b3-348a-8ec6-16d8cbbf0e43 | -4.6133 | -43.1594 | 2025-10-04 00:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 32.6 |
| b045ea72-fcee-372f-bcb6-0e7a8414e414 | -8.6322 | -54.9949 | 2025-10-04 00:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 68.1 |
| 4c458391-b636-3d7c-b4c8-bef9aef7ef22 | -4.4845 | -42.8631 | 2025-10-04 00:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 96.2 |
| 275bc62b-365a-376a-ba79-b3e1d680acbd | -5.4849 | -44.0982 | 2025-10-04 00:50:00 | GOES-19 | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 72.1 |
| 26a23084-fc06-3b82-98f5-caa6f76d7148 | -11.9343 | -46.3472 | 2025-10-04 00:50:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 69.9 |
| b6cfff78-c6eb-34b9-97ba-5c091303811b | -8.7589 | -49.9139 | 2025-10-04 00:50:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 61.1 |
| 50ef96d0-e4a8-3a99-b64b-54e82e002fd1 | -13.3221 | -48.1439 | 2025-10-04 00:50:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 112.0 |
| 9d1d4964-33a0-3e0c-91a7-e25aeac1b686 | -6.0618 | -42.5133 | 2025-10-04 00:50:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 75.4 |
| e273f32b-17eb-3fff-b696-9e41e7c3ff89 | -12.3813 | -54.4603 | 2025-10-04 00:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 71.0 |
| cd9816ac-5b05-30c9-aff4-e3405c915f68 | -9.3276 | -54.5215 | 2025-10-04 01:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 119.5 |
| aeff213e-982c-3233-93b3-8a3b27bd81f4 | -5.1965 | -45.0768 | 2025-10-04 01:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 68.8 |
| 714f6cba-b948-385e-a2f4-31e850b8bbc0 | -4.9541 | -45.0468 | 2025-10-04 01:00:00 | GOES-19 | SÃO ROBERTO | MARANHÃO | Brasil | 2111672 | 21 | 33 | nan | nan | nan | Cerrado | 62.6 |
| b422b203-254f-3947-9472-1f51b1ce427d | -4.4632 | -43.2386 | 2025-10-04 01:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 77.0 |
| b63b4b42-f6dc-3e76-8c10-17346e203632 | -4.6133 | -43.1594 | 2025-10-04 01:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 206.6 |
| ec0574d8-7179-34a0-adfe-efd82fe93f96 | -4.4443 | -43.263 | 2025-10-04 01:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 180.6 |
| d19d5159-f97e-3ff1-b55c-87495b67337f | -8.6322 | -54.9949 | 2025-10-04 01:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 76.5 |
| 80295096-087e-3212-8159-0ad4f5e27196 | -4.4446 | -43.2164 | 2025-10-04 01:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 70.3 |
| e038d18c-3f22-3b30-8c29-30840f9dbd10 | -13.3426 | -48.0742 | 2025-10-04 01:00:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 62.7 |
| 49a4a7aa-8ea0-3ae5-895a-c57a5ba434a9 | -13.3229 | -48.0993 | 2025-10-04 01:00:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 66.5 |
| 1db20790-1a1a-3e7b-87e4-bb6a6627d0ee | -5.4849 | -44.0982 | 2025-10-04 01:00:00 | GOES-19 | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 96.9 |
| b49d4e00-217c-3278-9100-b627fb6c0876 | -4.5948 | -43.1372 | 2025-10-04 01:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 33.4 |
| 7e4e4043-36a4-3ac3-a4c7-f40b4d480a37 | -4.954 | -45.0694 | 2025-10-04 01:00:00 | GOES-19 | SÃO ROBERTO | MARANHÃO | Brasil | 2111672 | 21 | 33 | nan | nan | nan | Cerrado | 171.1 |


[Clique aqui para ver as próximas entradas](README4.md)
