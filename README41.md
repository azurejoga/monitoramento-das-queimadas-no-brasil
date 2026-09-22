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

## Dados Diários - Página 41

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cfb1160f-6491-3fba-9a6b-dd77541afc9f | -18.73857 | -46.94355 | 2026-09-22 04:04:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 23.3 |
| 9af7316c-8642-3011-a53c-ee1f3cc97b10 | -17.94978 | -46.81563 | 2026-09-22 04:04:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8fcaf300-760e-3023-a8ff-04884c15089a | -17.9013 | -42.68539 | 2026-09-22 04:04:00 | NOAA-20 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 4c9e5ca6-bff1-3c39-ba6b-fc6d81ca34a2 | -11.70006 | -51.00381 | 2026-09-22 04:04:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 942033ca-bb80-31d8-a004-623b251ab107 | -11.68303 | -50.99547 | 2026-09-22 04:04:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 226fd9f7-a2a6-3f76-8fa6-20649ad43269 | -13.9186 | -48.57179 | 2026-09-22 04:04:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 72c07408-356a-3095-9db9-86f06bef2c73 | -14.1754 | -47.87125 | 2026-09-22 04:04:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 4b268f77-1f01-359a-8cdb-7424bf00db60 | -13.02664 | -50.60547 | 2026-09-22 04:04:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8daec7d2-f860-366d-861c-5383846c4d12 | -13.51931 | -51.52378 | 2026-09-22 04:04:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4823984a-4d11-32a2-9d5d-9731b1e51f34 | -15.44507 | -48.48567 | 2026-09-22 04:04:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 53268128-1d99-35fc-b4b4-7195e6e0f228 | -13.92448 | -48.56779 | 2026-09-22 04:04:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 13daf95d-33d3-354a-ae85-8d49d463a7bf | -14.7605 | -48.44763 | 2026-09-22 04:04:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e0b65d25-daed-339c-92ca-4f870b84ec2c | -11.31889 | -54.05474 | 2026-09-22 04:04:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 10.8 |
| c35200bf-12e0-324c-a6bc-b73630c51da3 | -14.75397 | -48.42981 | 2026-09-22 04:04:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 821f5722-bdca-3ea6-b6ec-d8d802baed08 | -15.85462 | -49.89333 | 2026-09-22 04:04:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f69e8a9f-05f5-3b49-a28d-28c5efd4b170 | -13.33361 | -51.28418 | 2026-09-22 04:04:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c1d54812-4afa-3eb1-a2d2-87ed8892666c | -15.56742 | -48.79537 | 2026-09-22 04:04:00 | NOAA-20 | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 46619570-0890-3a08-88aa-ae8aa3f13286 | -12.67329 | -50.96066 | 2026-09-22 04:04:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 04ad4faa-7bee-37ab-82de-bfba398be4c6 | -11.75736 | -50.82245 | 2026-09-22 04:04:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c3563570-9774-3506-b702-89ab9cfa021d | -13.02258 | -50.59616 | 2026-09-22 04:04:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ecb1e96c-b9ad-39b4-b5d1-dd7d1e740201 | -15.44151 | -48.47844 | 2026-09-22 04:04:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f70938a6-665c-3b53-9807-a73383d985b0 | -17.87003 | -44.40776 | 2026-09-22 04:04:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7f52cc67-c991-382d-bffa-76e2d1e3e2f1 | -13.3327 | -51.28862 | 2026-09-22 04:04:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fbf21336-1c51-36e7-8da1-1060127ce215 | -15.85527 | -49.89012 | 2026-09-22 04:04:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a42b98cd-dee1-3852-a6fc-fb211ea98338 | -12.29496 | -50.72149 | 2026-09-22 04:04:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 35d964b8-2a26-3595-a75b-0e4126fe881c | -14.66218 | -45.66657 | 2026-09-22 04:04:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 3f6a0065-5d11-3e96-aa99-493a0227930f | -13.3268 | -51.28731 | 2026-09-22 04:04:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b7a16121-e859-3d9e-9ec8-a276cd22c099 | -17.16865 | -40.77863 | 2026-09-22 04:04:00 | NOAA-20 | CRISÓLITA | MINAS GERAIS | Brasil | 3120151 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| e54936ad-1ca2-36fc-92b8-e0cda6182b70 | -15.05363 | -39.00148 | 2026-09-22 04:04:00 | NOAA-20 | ILHÉUS | BAHIA | Brasil | 2913606 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| 7c3df562-f251-3eb5-b545-c587fbfd7794 | -19.405 | -46.40594 | 2026-09-22 04:04:00 | NOAA-20 | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9f5f3e66-c222-37b2-85fa-a3af7908f284 | -12.2958 | -50.71724 | 2026-09-22 04:04:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 720bd670-caf1-3e84-998c-9f5c61171878 | -14.17413 | -47.86836 | 2026-09-22 04:04:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 70d45533-3ac4-32cd-a510-075e733e51dd | -14.68165 | -45.67416 | 2026-09-22 04:04:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cd30ae7b-d893-34f5-9afe-cbbd01fc5fea | -15.44357 | -48.46769 | 2026-09-22 04:04:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 76e65409-ae45-3c57-ad2b-079cee56c716 | -11.75385 | -50.82422 | 2026-09-22 04:04:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 73fcdc7a-bccb-30ba-952b-ae43d2ac5fca | -11.31327 | -54.04573 | 2026-09-22 04:04:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 1a38e3ee-a673-362c-8ce1-3cffae4aca93 | -19.21812 | -46.80283 | 2026-09-22 04:04:00 | NOAA-20 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| fb1bde37-c736-333f-aa65-9d0ebe557df6 | -14.04383 | -52.06044 | 2026-09-22 04:04:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8d2859e2-ad12-3f4a-b406-a80afb8e7d7c | -18.80866 | -47.55837 | 2026-09-22 04:04:00 | NOAA-20 | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2b2de9bb-337d-307b-9f47-bcefc12f955b | -14.66958 | -45.67177 | 2026-09-22 04:04:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 7ea9d474-970d-3cc0-a6b1-c6163013cd74 | -18.03288 | -50.92544 | 2026-09-22 04:04:00 | NOAA-20 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 53d9f127-4c79-3238-82c0-703ef0d251a6 | -13.71733 | -48.7854 | 2026-09-22 04:04:00 | NOAA-20 | CAMPINORTE | GOIÁS | Brasil | 5204706 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cd829a96-7077-31af-9266-c9f81750a491 | -16.65979 | -40.66774 | 2026-09-22 04:04:00 | NOAA-20 | FELISBURGO | MINAS GERAIS | Brasil | 3125606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 8d933b67-b9e4-38be-b63d-1478685b6a22 | -16.50895 | -49.40219 | 2026-09-22 04:04:00 | NOAA-20 | GOIANIRA | GOIÁS | Brasil | 5208806 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0d642775-d6ba-384d-9285-680020aa6bec | -19.65077 | -44.9006 | 2026-09-22 04:04:00 | NOAA-20 | PITANGUI | MINAS GERAIS | Brasil | 3151404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 371c3c6b-c334-3e47-947a-f6df9557ed76 | -15.26723 | -47.60501 | 2026-09-22 04:04:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ccd64b14-9c3e-3d1d-8651-80cf960222c5 | -11.32251 | -54.04659 | 2026-09-22 04:04:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 69237278-dc5e-3baa-aa34-61006768d8ae | -14.67295 | -45.67624 | 2026-09-22 04:04:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c5d79719-5a5b-319c-bf6c-b81356e8139e | -13.33951 | -51.28548 | 2026-09-22 04:04:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c0112b99-f8e3-3924-9ef5-4d67ef7233dd | -13.63071 | -42.48296 | 2026-09-22 04:04:00 | NOAA-20 | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 64680e6d-92cc-39c5-a474-2c33126ea5b2 | -11.689 | -50.99675 | 2026-09-22 04:04:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 34c54162-095d-3577-ab3a-2093149d5fed | -20.38706 | -42.55605 | 2026-09-22 04:04:00 | NOAA-20 | JEQUERI | MINAS GERAIS | Brasil | 3135506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 4e105eef-dea0-3025-b2a0-b36f4c40ae54 | -13.27358 | -51.79117 | 2026-09-22 04:04:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 98b93e85-52d3-367d-ab4f-f156c9359384 | -15.61966 | -48.32688 | 2026-09-22 04:04:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4e40538a-6f68-3b85-b564-2e7e176e7b41 | -14.63274 | -42.07378 | 2026-09-22 04:04:00 | NOAA-20 | GUAJERU | BAHIA | Brasil | 2911659 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 7aacbfef-1fa3-3ba5-8a8f-37cd5547b03c | -13.51242 | -51.52697 | 2026-09-22 04:04:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 63e2a1a1-1d2a-34ad-8779-bff5c4d652a2 | -17.37267 | -46.76008 | 2026-09-22 04:04:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b7834d0a-cdbb-3421-9e6b-22adece07650 | -13.86613 | -48.57831 | 2026-09-22 04:04:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 3adc21b0-7581-37e7-b5e1-05a5c5e9d786 | -14.63606 | -45.67282 | 2026-09-22 04:04:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 4b353cda-0b52-386a-b865-cd05543bdc68 | -17.56315 | -44.39855 | 2026-09-22 04:04:00 | NOAA-20 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8015e38c-7162-37ce-811a-0932b1ec49f2 | -14.68972 | -41.13823 | 2026-09-22 04:04:00 | NOAA-20 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| fc5a3ccc-a81e-3d9a-92a6-d04a1fe8036a | -18.02084 | -46.7233 | 2026-09-22 04:04:00 | NOAA-20 | LAGAMAR | MINAS GERAIS | Brasil | 3137106 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c156d2aa-cbdf-3909-ae3b-913a80ef051f | -13.85872 | -51.85102 | 2026-09-22 04:04:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 734e0b4f-289f-3e1b-b297-c82ad6189814 | -15.72291 | -41.57608 | 2026-09-22 04:04:00 | NOAA-20 | ÁGUAS VERMELHAS | MINAS GERAIS | Brasil | 3101003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| f40ea36a-30ba-3a84-9640-c7cf127e0c4a | -16.50368 | -40.6679 | 2026-09-22 04:04:00 | NOAA-20 | JEQUITINHONHA | MINAS GERAIS | Brasil | 3135803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 08fb933f-9ab1-3eb7-a667-de4f5dca324c | -18.65279 | -52.1655 | 2026-09-22 04:04:00 | NOAA-20 | APORÉ | GOIÁS | Brasil | 5201504 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 31043897-fade-37fc-bd16-3ec8d56340bf | -12.35574 | -50.23245 | 2026-09-22 04:04:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 02979959-83a5-3029-b235-86e26f228fc5 | -12.95038 | -50.92265 | 2026-09-22 04:04:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d6b9a900-6685-3e41-84a6-25a38042cba0 | -18.8921 | -46.84076 | 2026-09-22 04:04:00 | NOAA-20 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 49713e6d-baa0-3022-94fc-7a251ba381d1 | -11.32045 | -54.04721 | 2026-09-22 04:04:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 12011110-2702-311b-b5a4-fec056afe351 | -15.44979 | -53.12942 | 2026-09-22 04:04:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8db65810-a003-3522-b112-78718af1768d | -15.56773 | -42.63771 | 2026-09-22 04:04:00 | NOAA-20 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 6368181f-48fa-36b0-bdde-fe3c0a691307 | -12.29502 | -50.71651 | 2026-09-22 04:04:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d41570d6-8b42-370e-bac4-1ac5fc2a72cd | -15.99967 | -47.80856 | 2026-09-22 04:04:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 391c5a47-8bf1-30c1-b0ce-376795a0e161 | -20.39188 | -42.52639 | 2026-09-22 04:04:00 | NOAA-20 | JEQUERI | MINAS GERAIS | Brasil | 3135506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| c53ce0ac-5af6-3d5a-9d51-f415155f45aa | -13.94004 | -42.96844 | 2026-09-22 04:04:00 | NOAA-20 | MATINA | BAHIA | Brasil | 2921054 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 1c451cd2-103f-330a-87c2-46a2e5d5d053 | -11.75471 | -50.81981 | 2026-09-22 04:04:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d42bda87-03eb-3a34-901b-c4ff6680b1ca | -14.04481 | -52.05576 | 2026-09-22 04:04:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| acce795b-7624-379d-bd6c-60f25727df91 | -13.8517 | -51.85433 | 2026-09-22 04:04:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 482d8a62-5672-3d27-aa89-784b3740e9ea | -13.93151 | -47.84845 | 2026-09-22 04:04:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f41b7976-59fb-357e-8912-311122275a6a | -15.45106 | -43.81709 | 2026-09-22 04:04:00 | NOAA-20 | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c5503741-d9c3-3c4e-9d6d-e331c5e2612e | -14.75173 | -48.44129 | 2026-09-22 04:04:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ca7f79ee-0219-3f1c-8b21-f66ed9e964ea | -15.95942 | -42.96014 | 2026-09-22 04:04:00 | NOAA-20 | RIACHO DOS MACHADOS | MINAS GERAIS | Brasil | 3154507 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| aa9bc1c3-e322-3d3d-aacf-d9fbe0dbcb0c | -13.85366 | -51.84494 | 2026-09-22 04:04:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 0e1bd9ec-5fe7-3b5a-b4b1-fc84e642b1af | -15.43801 | -48.44526 | 2026-09-22 04:04:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 6c47b8e1-00e7-3bd8-a398-9dead18e9be6 | -11.68392 | -50.99094 | 2026-09-22 04:04:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 988ced6d-04ed-3478-92bb-bfb99fd727ef | -11.31533 | -54.04512 | 2026-09-22 04:04:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 57f2e4e0-3ae1-339a-93c7-b1a1abcc6c1e | -18.97976 | -47.11388 | 2026-09-22 04:04:00 | NOAA-20 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c15c365b-af5d-3162-ab6b-4718c968332c | -14.76404 | -48.45521 | 2026-09-22 04:04:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 2c1dca6a-be9b-3cea-92a3-bf04d9954039 | -18.97567 | -47.11296 | 2026-09-22 04:04:00 | NOAA-20 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 91d6ee8b-08dc-3ae9-97d3-93043f48af20 | -15.59835 | -48.32884 | 2026-09-22 04:04:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 72df97dc-57d3-3265-a234-6e11ecbace45 | -12.98981 | -44.80024 | 2026-09-22 04:04:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4844042a-0a7d-39e8-b2d7-a73350bf8f2e | -15.75152 | -43.30516 | 2026-09-22 04:04:00 | NOAA-20 | NOVA PORTEIRINHA | MINAS GERAIS | Brasil | 3145059 | 31 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 880ffe63-3914-36db-81a3-03286ca4e9dc | -17.07191 | -43.19788 | 2026-09-22 04:04:00 | NOAA-20 | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| d31bf369-64e1-3282-bf13-1d68e60568cd | -18.6537 | -52.16138 | 2026-09-22 04:04:00 | NOAA-20 | APORÉ | GOIÁS | Brasil | 5201504 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 842cd13e-be3b-3481-b8a7-12f1c636ab58 | -18.74309 | -45.59538 | 2026-09-22 04:04:00 | NOAA-20 | BIQUINHAS | MINAS GERAIS | Brasil | 3107000 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0509e0e1-97fa-3bc3-9328-ad0b5aecc36f | -15.43972 | -48.46202 | 2026-09-22 04:04:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| e707cf4f-1117-33c8-9303-3d8d7787917f | -19.87122 | -42.63615 | 2026-09-22 04:04:00 | NOAA-20 | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 44a51727-3c03-33f7-8c66-fc5f9a8059d6 | -12.95447 | -50.93243 | 2026-09-22 04:04:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 01760d27-d010-3fe1-8298-714d14fec32e | -16.04282 | -49.98323 | 2026-09-22 04:04:00 | NOAA-20 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README42.md)
