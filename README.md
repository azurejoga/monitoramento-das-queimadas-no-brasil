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
| 76c8673f-a153-3f38-a3a2-466a884b3257 | -7.0799 | -59.1964 | 2025-08-12 00:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 61.1 |
| b643cc46-be92-324f-9add-96ea09b6a247 | -6.7272 | -43.5822 | 2025-08-12 00:00:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 78.8 |
| f709f9a9-c207-3009-a7b9-fbd3a5081930 | -8.579 | -54.696 | 2025-08-12 00:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 55.7 |
| 35ec0301-3d0e-3eae-80f3-367362b82507 | -7.1483 | -60.1174 | 2025-08-12 00:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 195.8 |
| 195f011c-36c2-3897-ad75-541ee5b3209f | -16.2957 | -52.923 | 2025-08-12 00:00:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 88.1 |
| efff08b4-2132-3c02-b702-069e495328c4 | -9.723 | -49.4806 | 2025-08-12 00:00:00 | GOES-19 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 119.2 |
| 7facd18a-1a1f-3c59-a29c-8502b863b272 | -6.5856 | -44.564 | 2025-08-12 00:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 86.3 |
| 55c5ddc4-8a64-34c8-ad3b-749d029ffce5 | -7.13 | -60.099 | 2025-08-12 00:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 63.3 |
| cd092237-6284-3b4d-bc06-3bb20fbcfcd7 | -6.9686 | -59.2783 | 2025-08-12 00:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 66.4 |
| a5d4b555-72b5-3d4b-b793-fd149e13c9c7 | -7.1299 | -60.1182 | 2025-08-12 00:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 279.6 |
| 251dc594-86a7-330d-b318-067f31cd5d10 | -7.1482 | -60.1366 | 2025-08-12 00:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 85.8 |
| b03d2e2a-46c3-32c6-8019-aed2f6aeb850 | -9.1894 | -59.6558 | 2025-08-12 00:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 42.4 |
| a8bdd0bc-61df-3b9f-9113-e07a0beeb096 | -9.3806 | -61.5315 | 2025-08-12 00:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 57.2 |
| 19f83e8f-295f-3822-8ad2-8ec1bc9f75c9 | -19.2907 | -48.4291 | 2025-08-12 00:00:00 | GOES-19 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 43.2 |
| 7dc77d60-6c1a-39fc-b522-23fd1723fe5c | -16.2961 | -52.9016 | 2025-08-12 00:00:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 110.9 |
| bc53c44c-895c-3a19-a19f-fb02aaf734f0 | -7.1298 | -60.1374 | 2025-08-12 00:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 104.9 |
| b5421ed0-1567-3026-952a-e8ea4bcac654 | -10.3065 | -54.1592 | 2025-08-12 00:00:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 43.3 |
| 58731178-fe7d-375b-9609-783a224f0587 | -8.5211 | -43.3063 | 2025-08-12 00:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 89.8 |
| 9090f116-7316-3f38-8c12-feeaea897b8f | -8.9215 | -60.7297 | 2025-08-12 00:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 58.0 |
| 45a4f7ad-13e5-3543-9281-219c2bd64fa2 | -10.3253 | -54.1576 | 2025-08-12 00:00:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 55.5 |
| 72916720-f36c-3d5f-92c3-3abbccffe788 | -14.6894 | -53.7272 | 2025-08-12 00:00:00 | GOES-19 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 41.0 |
| 4d772429-24af-37a8-b2bd-47b695171e64 | -8.9401 | -60.7288 | 2025-08-12 00:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 94.6 |
| 6d304c2c-0d7f-3a9d-9e82-807296cf2df3 | -12.7759 | -45.4445 | 2025-08-12 00:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 90.5 |
| 38cbc2c5-c278-36c3-a796-bea5f633c2fd | -8.5788 | -54.7162 | 2025-08-12 00:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 111.2 |
| 6252f2b2-3988-3001-8f50-6c05ee19a77b | -8.9399 | -60.7481 | 2025-08-12 00:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 48.8 |
| e06b5194-9eba-3507-acb9-f2d89b4bb4ce | -8.5602 | -54.7175 | 2025-08-12 00:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 56.8 |
| efffe191-f575-365e-9f3d-9499f6419fdc | -19.3109 | -48.4248 | 2025-08-12 00:00:00 | GOES-19 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 49.5 |
| e83a4195-dd6a-309b-a5e9-6c82797f4be2 | -7.1484 | -60.0982 | 2025-08-12 00:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 44.8 |
| bea2abb6-d321-3e3d-9cbb-93b6e2b06ac0 | -7.1482 | -60.1366 | 2025-08-12 00:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 60.9 |
| c9fcaf3b-4775-33a9-88b5-675351983fa9 | -8.9401 | -60.7288 | 2025-08-12 00:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 83.5 |
| 2e1ad610-24a6-3280-844b-614067ba6de3 | -12.7759 | -45.4445 | 2025-08-12 00:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 68.0 |
| 05a363bf-104f-3ace-9b65-f97f2fc500ed | -9.723 | -49.4806 | 2025-08-12 00:10:00 | GOES-19 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 109.1 |
| 50bdbc49-ffdc-3aef-b7bb-7beaf2ef75c4 | -9.7041 | -49.4825 | 2025-08-12 00:10:00 | GOES-19 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 84.6 |
| f33abc9e-47ee-3162-8ce5-022bee88a363 | -7.0799 | -59.1964 | 2025-08-12 00:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 57.6 |
| 49abc3b9-1251-354f-97dd-176e186e8e84 | -14.6894 | -53.7272 | 2025-08-12 00:10:00 | GOES-19 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 32.3 |
| 3a464654-607a-3372-8e89-45c1575ed2fd | -7.1483 | -60.1174 | 2025-08-12 00:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 152.2 |
| a2d8fec0-9eec-35f7-9140-8a58f7f2f2f4 | -8.5602 | -54.7175 | 2025-08-12 00:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 72.5 |
| 8951cda2-d824-384b-9917-f66e8137b32a | -15.4029 | -53.8678 | 2025-08-12 00:10:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 50.4 |
| 4982806a-734f-3f97-bec7-7f2c9ea7c662 | -9.1892 | -59.6752 | 2025-08-12 00:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 37.7 |
| e07cd11c-7e7c-3d36-bb84-a87d85acb212 | -9.1894 | -59.6558 | 2025-08-12 00:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 77.0 |
| 467fa234-ab25-38bf-b666-0cb8d587d922 | -7.1299 | -60.1182 | 2025-08-12 00:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 348.3 |
| fad4f19f-dddc-3022-ab73-01078c829a30 | -8.9215 | -60.7297 | 2025-08-12 00:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 75.3 |
| 2ea7bf69-4420-3963-8fd8-34aa574d86e3 | -15.4025 | -53.8888 | 2025-08-12 00:10:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 56.5 |
| d78448ca-52b9-397b-9c01-42ec5c741149 | -9.3806 | -61.5315 | 2025-08-12 00:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 45.3 |
| e3086364-a1c4-3ef5-94e2-7f11f9c16531 | -16.2961 | -52.9016 | 2025-08-12 00:10:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 92.3 |
| 54ce0e8c-f5df-3178-93f0-a0e8d1b18c6e | -15.4219 | -53.8863 | 2025-08-12 00:10:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 42.5 |
| b99f8b2a-08c0-3874-b4ae-9d013e30345f | -6.9686 | -59.2783 | 2025-08-12 00:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 59.1 |
| f922a978-2cb9-301c-ab5b-1acbb0fdeff6 | -8.5788 | -54.7162 | 2025-08-12 00:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 105.1 |
| 70433c8c-50c0-3316-bf8d-8f29f9761634 | -7.1298 | -60.1374 | 2025-08-12 00:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 114.1 |
| 8ad8b37e-fb06-34e6-992a-5a5c3a633d00 | -8.5211 | -43.3063 | 2025-08-12 00:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 86.0 |
| bed4a25d-996f-35f0-b786-bed47f31297b | -19.3109 | -48.4248 | 2025-08-12 00:10:00 | GOES-19 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 54.3 |
| e6f0c3a7-984b-3852-8e2b-11568811c586 | -6.5856 | -44.564 | 2025-08-12 00:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 88.8 |
| 19d7411f-995c-347a-836b-b5af1a6b4922 | -7.1114 | -60.1189 | 2025-08-12 00:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 32.8 |
| 76ed5cbd-1e83-3c8b-8e72-3575121eb1d1 | -16.2957 | -52.923 | 2025-08-12 00:10:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 91.7 |
| ed3a438b-6ee5-3607-8808-4663d7459c46 | -9.723 | -49.4806 | 2025-08-12 00:20:00 | GOES-19 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 106.5 |
| 37bb5b28-59b9-3baa-83ff-621d94d6a29e | -9.3806 | -61.5315 | 2025-08-12 00:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 53.5 |
| 31e2e4d1-23e1-37f6-abb5-27ef30146eba | -7.1482 | -60.1366 | 2025-08-12 00:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 66.4 |
| 896a4a21-3bd9-3b13-b334-1813d704c923 | -8.9399 | -60.7481 | 2025-08-12 00:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 50.5 |
| dccb52a2-7e0b-3d16-a7fa-20fe162428d0 | -9.5147 | -40.3558 | 2025-08-12 00:20:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 70.8 |
| 2d341551-c698-3c3b-be37-0b2f0d40b82d | -7.1298 | -60.1374 | 2025-08-12 00:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 90.5 |
| 75421c06-a865-3d6f-98eb-9b4ba750c4bd | -6.9686 | -59.2783 | 2025-08-12 00:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 58.9 |
| 233003b5-b015-38b2-89e2-63ced20f6a60 | -7.1483 | -60.1174 | 2025-08-12 00:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 160.1 |
| fe127ef3-e2e8-386f-b571-7a32bf2781c0 | -19.2907 | -48.4291 | 2025-08-12 00:20:00 | GOES-19 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 64.8 |
| f04e529f-f28c-332c-ac6c-a4d094df09d1 | -19.7148 | -46.2151 | 2025-08-12 00:20:00 | GOES-19 | CAMPOS ALTOS | MINAS GERAIS | Brasil | 3111507 | 31 | 33 | nan | nan | nan | Cerrado | 62.3 |
| 1e73faaf-b144-3b0f-8415-d9ad28ec40d9 | -15.4025 | -53.8888 | 2025-08-12 00:20:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 82.7 |
| f96bc593-b337-3b72-a4cd-fb6b4c949e78 | -16.2961 | -52.9016 | 2025-08-12 00:20:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 85.2 |
| 5a122ecf-c089-3406-ad8b-bd4568f75a6d | -12.7759 | -45.4445 | 2025-08-12 00:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 78.3 |
| 79bf296b-6d64-3d58-8d82-24c237745f8e | -15.4029 | -53.8678 | 2025-08-12 00:20:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 90.3 |
| 2ee88b74-bb44-303b-80f5-4a20ce5efc99 | -8.9213 | -60.7489 | 2025-08-12 00:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 41.8 |
| 6e22a3a9-468a-3150-bc20-95bfcd897537 | -8.5788 | -54.7162 | 2025-08-12 00:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 97.7 |
| 1d21ee54-3a5f-3e4c-a9b6-ad3c3ec47204 | -7.13 | -60.099 | 2025-08-12 00:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 46.9 |
| 31efb5dc-f403-3657-a965-48915134a6ba | -8.5211 | -43.3063 | 2025-08-12 00:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 82.1 |
| 243f6bae-a7a1-3734-b6bb-4a0e4f0c2f33 | -8.5602 | -54.7175 | 2025-08-12 00:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 54.9 |
| 6b107258-e7b7-3de6-b3be-388f6be1e7a9 | -7.1299 | -60.1182 | 2025-08-12 00:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 257.4 |
| 243de194-96e2-31b4-bc51-95a6bd1f655b | -16.2957 | -52.923 | 2025-08-12 00:20:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 77.7 |
| be3df5b9-1942-3212-9a1e-a87dd7f36ad3 | -8.579 | -54.696 | 2025-08-12 00:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 49.0 |
| 161d3b07-4bfe-33d8-8f0e-b4b2a2acf021 | -15.4219 | -53.8863 | 2025-08-12 00:20:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 61.2 |
| b8c00af4-6643-3fb4-814f-42dc85d161ba | -9.496 | -40.3337 | 2025-08-12 00:20:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 66.8 |
| bea2941f-4977-30fa-96d6-ecf08fdb37b9 | -8.9215 | -60.7297 | 2025-08-12 00:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 60.9 |
| b0fb32e8-0468-312c-bc0b-4a79f76cbeee | -9.1894 | -59.6558 | 2025-08-12 00:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 35.9 |
| bedd4d7a-b1e9-3dc9-ae3c-8689e9216e30 | -15.4223 | -53.8653 | 2025-08-12 00:20:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 46.0 |
| d0deec8e-801d-3230-ad30-76a6788d8d73 | -6.5856 | -44.564 | 2025-08-12 00:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 116.9 |
| 31fd70b2-f5da-3e15-9d0f-99cf10a940ef | -8.9401 | -60.7288 | 2025-08-12 00:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 94.0 |
| db7d4042-c7fe-3c95-903b-8e215712d166 | -7.0799 | -59.1964 | 2025-08-12 00:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 57.7 |
| 97de76ad-43dc-3bd8-a484-c1aa8deec0b7 | -19.3109 | -48.4248 | 2025-08-12 00:20:00 | GOES-19 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 43.1 |
| 1e5cc217-24cd-3471-8e43-db42da3e7746 | -9.5152 | -40.331 | 2025-08-12 00:20:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 80.0 |
| c01c91a3-ac5b-3ecc-b1fb-8e3acd7525dd | -16.2957 | -52.923 | 2025-08-12 00:30:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 81.1 |
| 470301cd-554e-30d2-b883-b6f21d047cdb | -6.9686 | -59.2783 | 2025-08-12 00:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 53.7 |
| e9dfceff-6c9f-3a68-8606-87dcf52aede9 | -15.4029 | -53.8678 | 2025-08-12 00:30:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 171.4 |
| 1926b28b-995c-382e-a453-8b27c9b28750 | -15.4025 | -53.8888 | 2025-08-12 00:30:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 159.8 |
| 0e3664a4-e3af-3be8-8539-58cd21a27137 | -6.5858 | -44.541 | 2025-08-12 00:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 56.4 |
| c6c56a12-1d1e-36bf-a0d8-cfbef507abc3 | -12.7759 | -45.4445 | 2025-08-12 00:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 70.1 |
| f4b0624b-eb1c-3c26-8f4d-5699cbb62403 | -7.1483 | -60.1174 | 2025-08-12 00:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 125.9 |
| 8b01d35a-2b24-3d15-8b87-771bdfbce725 | -8.5788 | -54.7162 | 2025-08-12 00:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 85.3 |
| 52a6c7db-6bfb-3dca-8539-9ce9a6d7f9c5 | -7.13 | -60.099 | 2025-08-12 00:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 50.7 |
| 214aa7af-5c82-3f21-bc3b-2c4eb5ab64e0 | -14.6894 | -53.7272 | 2025-08-12 00:30:00 | GOES-19 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 36.0 |
| 60466970-369c-3229-a80a-b4bdae8492f5 | -19.3109 | -48.4248 | 2025-08-12 00:30:00 | GOES-19 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 69.2 |
| b28c8f06-be9e-3f51-8a1e-0326a86b251d | -22.6353 | -54.9867 | 2025-08-12 00:30:00 | GOES-19 | CAARAPÓ | MATO GROSSO DO SUL | Brasil | 5002407 | 50 | 33 | nan | nan | nan | Mata Atlântica | 46.5 |
| 97455a92-5ef4-3472-b56d-dee32bda1338 | -7.1298 | -60.1374 | 2025-08-12 00:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 117.6 |
| 9c9f3b79-af59-3c6e-90f3-b16069ee56d3 | -15.4223 | -53.8653 | 2025-08-12 00:30:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 75.9 |


[Clique aqui para ver as próximas entradas](README2.md)
