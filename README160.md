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

## Dados Diários - Página 160

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 927790b3-4302-3e5d-8247-5f84567c8e2a | -11.1757 | -47.2134 | 2025-10-01 14:10:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 160.5 |
| 2ea868f5-a241-33f7-8b47-aeb14429a0f7 | -11.0994 | -49.7434 | 2025-10-01 14:10:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 72.9 |
| e037fe7b-7804-3f86-ae74-5f1afbe7a71d | -7.6463 | -45.4262 | 2025-10-01 14:10:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 62.8 |
| ebce36b1-5d8f-3872-811c-8456411015dc | -13.7872 | -48.0077 | 2025-10-01 14:10:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 94.2 |
| a846c75a-2d9f-3625-a5e7-5489e8eef3f9 | -9.9031 | -45.978 | 2025-10-01 14:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 86.0 |
| b1a2383c-98d4-3249-bda1-9bbfffd31a73 | -6.2875 | -42.4941 | 2025-10-01 14:10:00 | GOES-19 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 73.8 |
| bf78c5ea-cc08-3946-8855-cdc3031b26cf | -5.3248 | -43.1118 | 2025-10-01 14:10:00 | GOES-19 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 166.6 |
| 04a69d4e-a9d6-3d4a-9f81-3fb855370a28 | -6.1166 | -42.6742 | 2025-10-01 14:10:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 77.0 |
| bbb03767-0e5c-3e63-9f8d-787faf2eb0f2 | -9.9581 | -43.5987 | 2025-10-01 14:10:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 119.8 |
| 74599db8-a92b-3381-9315-05f2b26a55ea | -7.8165 | -46.9781 | 2025-10-01 14:10:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 77.4 |
| e0dc003c-ec1b-3a24-bebe-ba2e9491d1e4 | -15.2823 | -47.9461 | 2025-10-01 14:10:00 | GOES-19 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 64.0 |
| d684e5ff-93e2-3552-9455-f847cb54e734 | -5.4964 | -42.7707 | 2025-10-01 14:10:00 | GOES-19 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 85.4 |
| e6b088c0-0777-352f-85e6-d654e8f0bc36 | -10.1231 | -47.8051 | 2025-10-01 14:10:00 | GOES-19 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 83.2 |
| cae34ffd-228e-3926-b81a-0db14c0ec181 | -13.6707 | -48.0476 | 2025-10-01 14:10:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 100.1 |
| cacd4b21-5c7a-3795-8b9f-64dcc99dca0d | -9.4194 | -54.697 | 2025-10-01 14:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 68.2 |
| 39c7c3b0-e7a4-3320-a23e-f2ec2cf25be2 | -15.5379 | -45.2375 | 2025-10-01 14:10:00 | GOES-19 | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 129.6 |
| 5ae1acef-2c4e-39a8-8208-7d0350c7536d | -16.0221 | -50.8989 | 2025-10-01 14:10:00 | GOES-19 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 170.5 |
| 484f483c-45a6-3fe4-a953-266e7a46ec81 | -11.8482 | -48.0595 | 2025-10-01 14:10:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 87.6 |
| b801dede-7ed9-3c0b-b38c-d8b7d1ef0795 | -6.214 | -44.2272 | 2025-10-01 14:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 104.6 |
| fd8e32ad-6396-3751-8988-6dc853b1d023 | -11.4596 | -45.0433 | 2025-10-01 14:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 250.4 |
| d259533f-3d85-37ca-b4be-0cf6b353c730 | -9.9035 | -45.9553 | 2025-10-01 14:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 106.9 |
| c966787f-998b-37a9-b9cc-5ce603980767 | -8.5587 | -44.7414 | 2025-10-01 14:10:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 151.2 |
| 1b80c84e-f975-3036-8e1b-b41106653f78 | -11.383 | -45.0543 | 2025-10-01 14:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 120.1 |
| fa0de9be-521f-346c-aa7e-aa44f04dfc16 | -5.17 | -43.7276 | 2025-10-01 14:10:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 94.3 |
| 854441ac-d885-3f46-a8ae-c8555114faa0 | -11.8438 | -44.964 | 2025-10-01 14:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 103.2 |
| 308c6b9e-ae00-3324-af7d-7539efc9f22d | -13.3278 | -47.8313 | 2025-10-01 14:10:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 69.3 |
| 6d75bd02-4f42-39d7-b544-c161736fdb80 | -7.1812 | -41.7172 | 2025-10-01 14:10:00 | GOES-19 | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 76.0 |
| 70f64be6-0a33-3e4d-b367-790879b088c9 | -12.2627 | -44.107 | 2025-10-01 14:10:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 400.4 |
| fa816825-404a-3f38-9f96-2dbb46be397f | -7.8735 | -45.2911 | 2025-10-01 14:10:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 125.1 |
| d030643b-0f47-3bc3-9399-ae0bca12f984 | -6.2998 | -45.0433 | 2025-10-01 14:10:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 80.2 |
| 66622905-dacf-34f0-9ed0-4bbce479262b | -9.4192 | -54.7172 | 2025-10-01 14:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 71.5 |
| 5eae57df-e521-3268-a0d6-539112a414d1 | -11.4784 | -45.0637 | 2025-10-01 14:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 97.1 |
| 11f32dbe-f419-3420-a032-af63c662341c | -13.3808 | -48.0908 | 2025-10-01 14:10:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 138.6 |
| fbcfc324-5797-381e-9696-9a8e3216dedf | -9.8845 | -45.9576 | 2025-10-01 14:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 126.1 |
| cc747e36-9297-3c3a-a21c-ac6ec4a084e7 | -8.9081 | -51.6743 | 2025-10-01 14:10:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 106.0 |
| 53e67d89-3173-3497-a898-bf48e0a870cc | -12.8831 | -46.9101 | 2025-10-01 14:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 135.6 |
| b0bc31b4-9c24-3d68-9d38-d2631da15453 | -11.1181 | -49.7629 | 2025-10-01 14:10:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 63.6 |
| 134c8e1e-de8f-372c-83f7-c7f7accd5589 | -10.0187 | -48.5183 | 2025-10-01 14:10:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 136.0 |
| 6faa12c1-fc5d-3af8-8e36-792fdbfe42d5 | -12.2623 | -44.1306 | 2025-10-01 14:10:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 290.8 |
| 59145033-a826-3203-93e4-78e2964d68b6 | -8.9115 | -46.6276 | 2025-10-01 14:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 163.1 |
| 3f2f6b6d-9f44-3517-a7df-62ac9a8a1f60 | -12.254 | -47.7837 | 2025-10-01 14:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 54.7 |
| 97cdd8b9-e695-3be0-b1cc-16211b3c835b | -8.163 | -46.2554 | 2025-10-01 14:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 82.4 |
| 142536ab-3140-3128-ad80-22f5cc1d8a7c | -9.8842 | -45.9802 | 2025-10-01 14:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 95.1 |
| fd515fc4-d10e-3948-99e2-1fd503d93d2d | -7.8549 | -45.2702 | 2025-10-01 14:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 99.4 |
| 01472270-5e41-34e1-bc8b-fb72cf1d35e5 | -9.4007 | -54.6984 | 2025-10-01 14:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 69.3 |
| affb8214-c25e-3307-9cac-60291c74013d | -12.3863 | -50.1947 | 2025-10-01 14:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 83.5 |
| ec38966d-456c-3dcc-b151-dd0511a43c8d | -11.9445 | -48.0026 | 2025-10-01 14:10:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 58.9 |
| bd42481e-0825-3e18-90ef-88feeca88713 | -16.2742 | -42.5406 | 2025-10-01 14:10:00 | GOES-19 | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 83.7 |
| 392ad258-fa0f-3ca6-b318-69283220eb13 | -11.1178 | -49.7845 | 2025-10-01 14:10:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 105.2 |
| 422a77be-6d08-316c-9a05-b3ec7cbefea8 | -11.4592 | -45.0664 | 2025-10-01 14:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 112.2 |
| 248231d4-adb8-34e4-94c1-04fbe8361a3e | -6.0811 | -42.4644 | 2025-10-01 14:10:00 | GOES-19 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 89.0 |
| a1613346-fa42-31fd-8873-1196cb0889a2 | -4.9591 | -42.0284 | 2025-10-01 14:10:00 | GOES-19 | JATOBÁ DO PIAUÍ | PIAUÍ | Brasil | 2205276 | 22 | 33 | nan | nan | nan | Caatinga | 90.0 |
| 61a57e43-ba99-3eeb-ae31-0a1c895e9b1e | -7.1815 | -41.6931 | 2025-10-01 14:10:00 | GOES-19 | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 92.4 |
| 83474a4a-c6da-3242-9d3a-c508d4de169a | -5.6412 | -45.4989 | 2025-10-01 14:10:00 | GOES-19 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 63.0 |
| 65e0f257-fdc4-313a-ae51-75ab706fb5ac | -8.8923 | -46.6519 | 2025-10-01 14:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 197.8 |
| 237bc538-00f1-362b-b488-3ab4f734ee75 | -14.8884 | -47.2226 | 2025-10-01 14:10:00 | GOES-19 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 76.4 |
| 825982da-877c-32cb-88b6-945ce17ea1fa | -8.8609 | -47.6521 | 2025-10-01 14:10:00 | GOES-19 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 86.1 |
| bbd42f54-3d61-3b61-8234-6f4fdc5d9e9a | -10.9182 | -44.3092 | 2025-10-01 14:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 107.4 |
| c33b94f6-798c-3f9f-97bf-ca958b290b24 | -7.4656 | -46.476 | 2025-10-01 14:10:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 54.5 |
| 411e9db9-db83-3e20-a614-954dcfcaecea | -9.1434 | -47.6457 | 2025-10-01 14:10:00 | GOES-19 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 68.6 |
| 17fa3e40-3f10-36f8-88c8-3d7fd4ce2b1b | -14.3524 | -45.8974 | 2025-10-01 14:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 151.7 |
| d5358e18-cd09-3edb-bc55-de2222a000f1 | -9.8201 | -47.8386 | 2025-10-01 14:10:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 99.7 |
| b7b1f1fc-fe74-38a6-a3ca-235b3c728622 | -13.7869 | -51.2404 | 2025-10-01 14:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 252.5 |
| 2feb82ac-bd3b-3485-b134-552fb8fecbf5 | -13.6711 | -48.0253 | 2025-10-01 14:10:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 103.8 |
| e1efe651-ba98-3976-976a-447210e10dcf | -11.8622 | -45.0075 | 2025-10-01 14:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 93.4 |
| a6401406-800b-3a37-90fc-c2c2fb309d32 | -11.7984 | -47.6003 | 2025-10-01 14:10:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 85.4 |
| 50f1e755-0055-3299-8e4f-91b81a2a49ce | -12.2536 | -47.806 | 2025-10-01 14:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 137.8 |
| 4df094ff-c092-3bc8-8611-af39ec72a1dc | -5.8064 | -43.728 | 2025-10-01 14:10:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 94.3 |
| c5c80de1-34aa-3ead-a470-e646949c5180 | -13.7549 | -48.7008 | 2025-10-01 14:10:00 | GOES-19 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 77.1 |
| f9af5fc9-92b7-3f41-ad36-a04b269d6b7c | -6.5546 | -43.9221 | 2025-10-01 14:10:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 131.0 |
| 4d291d66-6a33-3138-84be-4344af999f03 | -5.7581 | -42.8682 | 2025-10-01 14:10:00 | GOES-19 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 89.9 |
| 39bc2933-6757-325d-879e-fb0a87149de1 | -8.9182 | -47.5803 | 2025-10-01 14:10:00 | GOES-19 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 67.8 |
| d129fd24-56ab-3e7d-a7cd-70bb710b29cc | -6.079 | -42.6773 | 2025-10-01 14:10:00 | GOES-19 | SANTO ANTÔNIO DOS MILAGRES | PIAUÍ | Brasil | 2209450 | 22 | 33 | nan | nan | nan | Caatinga | 85.6 |
| afc5a24c-ab79-3615-bbd5-c785b2f01b8a | -8.6911 | -47.6906 | 2025-10-01 14:10:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 68.0 |
| 040929e3-b7bd-3008-96e4-71a3bc74f2c9 | -6.2813 | -45.022 | 2025-10-01 14:10:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 102.5 |
| e6b1b643-544d-3b05-9924-2296f3a16583 | -14.9738 | -46.8668 | 2025-10-01 14:10:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 120.1 |
| b3f011ae-419d-32df-a9f1-27392ebc2f5b | -6.7168 | -44.5758 | 2025-10-01 14:10:00 | GOES-19 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 82.0 |
| 161a021a-23e0-37d4-986b-4c21bd706566 | -8.8926 | -46.6296 | 2025-10-01 14:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 152.3 |
| 2770b3fe-33c7-30a4-a383-1cb691e2bca2 | -7.6272 | -45.4507 | 2025-10-01 14:10:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 92.5 |
| 94ea2b58-9aa8-36f2-956e-fab67849b625 | -8.6908 | -47.7126 | 2025-10-01 14:10:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 74.9 |
| 70e08c05-188e-35a1-917c-922a0f206cf9 | -5.9744 | -45.8574 | 2025-10-01 14:10:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 66.3 |
| acf1d7df-f9ac-386a-81bc-be100c1e9dcb | -16.0225 | -50.8771 | 2025-10-01 14:10:00 | GOES-19 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 216.2 |
| 0e5d6500-113c-3cb7-9652-56267b18f0e6 | -6.0999 | -42.4628 | 2025-10-01 14:10:00 | GOES-19 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 103.1 |
| 6561c4a1-7633-3249-b0e8-d62c369356b4 | -9.9189 | -43.6743 | 2025-10-01 14:10:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 796.1 |
| 4ff21da6-b743-3cb5-87b0-175c38593227 | -11.1368 | -49.7823 | 2025-10-01 14:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 58.3 |
| 1ce1aedf-9e8e-35c1-b957-c281a793af80 | -11.0225 | -49.8167 | 2025-10-01 14:10:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 63.3 |
| 0fdd4db2-8c60-32e1-8d6b-dc20979cb3e8 | -13.3274 | -47.8536 | 2025-10-01 14:10:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 187.1 |
| 7e1540c8-815f-376b-9363-0c15e8d10a01 | -11.176 | -47.1911 | 2025-10-01 14:10:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 105.9 |
| 2beff0b6-e6c5-3468-8edc-2922aabb8e06 | -5.9557 | -45.8588 | 2025-10-01 14:10:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 103.0 |
| bca45762-04fc-3ed5-b4de-1d8b79b5435f | -11.3486 | -48.3211 | 2025-10-01 14:10:00 | GOES-19 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 640.3 |
| a8f58259-643e-3f27-8bda-8e92419529ed | -9.9959 | -43.6172 | 2025-10-01 14:10:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 181.5 |
| 2b554ac3-42b7-3e6c-84ec-6731a7d7fa44 | -12.282 | -44.1039 | 2025-10-01 14:10:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 307.5 |
| 1648b44b-3298-3e94-a6d8-3093f9c5f905 | -15.3792 | -47.0689 | 2025-10-01 14:10:00 | GOES-19 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 61.4 |
| 0e58c732-efdc-30f3-a7a9-55500b384fb8 | -15.3596 | -47.0724 | 2025-10-01 14:10:00 | GOES-19 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 77.9 |
| ddddb024-2fb2-3239-8a91-5582367ace6e | -5.8418 | -43.9566 | 2025-10-01 14:10:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 106.8 |
| 729ad7ee-5448-3a76-a746-77a9aec5ba85 | -11.0988 | -49.7866 | 2025-10-01 14:10:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 75.7 |
| 71403fe1-ae34-3310-a69b-9a93f3591a80 | -7.4758 | -47.2728 | 2025-10-01 14:10:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 64.9 |
| 43d74daf-39c7-3bcd-892a-8a355267d455 | -8.5016 | -47.8184 | 2025-10-01 14:10:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 86.8 |
| a44283e1-7c2f-360c-b023-0073c6178ab2 | -14.9084 | -47.1965 | 2025-10-01 14:10:00 | GOES-19 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 124.6 |
| 702d2918-4d28-3ec4-89f1-cd8b9e8e37bd | -10.8421 | -46.6514 | 2025-10-01 14:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 101.6 |


[Clique aqui para ver as próximas entradas](README161.md)
