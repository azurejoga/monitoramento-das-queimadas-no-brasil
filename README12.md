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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7276b75e-e9e7-3a4b-b44c-e817c6802676 | -8.0703 | -43.0981 | 2025-11-16 01:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 95.7 |
| 0d8ed4d3-58d5-30bf-b64f-879ad7d129be | -3.9538 | -47.1932 | 2025-11-16 01:40:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 63.0 |
| d3d4a085-b3b8-37a3-a631-7aa30844b0fd | -8.0513 | -43.1001 | 2025-11-16 01:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 82.3 |
| 9fbf3cdd-1a30-36b0-85f7-ea6562c4ab49 | -4.7395 | -46.3821 | 2025-11-16 01:40:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 63.8 |
| aa79b358-901f-32f2-ab35-9c3b66ca68f5 | -2.5053 | -47.812 | 2025-11-16 01:40:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 61.5 |
| d620d269-2d1f-362d-8c95-75c2cc455635 | -12.0 | -49.2901 | 2025-11-16 01:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 99.0 |
| ae76f251-0416-39c5-baa4-a760898f7244 | -2.5238 | -47.8332 | 2025-11-16 01:40:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 69.5 |
| bd79ab8f-f120-3e71-9ada-0614fa4e8d97 | -12.0004 | -49.2683 | 2025-11-16 01:40:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 146.8 |
| b3483bdd-89d2-3562-bece-f83dc6c66c07 | -3.9536 | -47.2151 | 2025-11-16 01:40:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 55.6 |
| 40ce7503-b8fc-334e-9a03-aecc119b275c | -12.6672 | -47.167 | 2025-11-16 01:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 74.8 |
| 6f3adc50-e761-3bf7-ab3a-41b56998d012 | -2.8925 | -53.2842 | 2025-11-16 01:40:00 | GOES-19 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 48.2 |
| 434babf1-14cd-370d-a4b8-416e34b90130 | -12.2047 | -49.6121 | 2025-11-16 01:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 102.9 |
| 9b6c74a2-9900-3474-b17d-0acd1c2ebe77 | -4.4246 | -43.4038 | 2025-11-16 01:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 37.5 |
| aac147cc-89c3-304c-a23b-101c7fb2a580 | -8.1092 | -46.0363 | 2025-11-16 01:40:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 59.8 |
| 5f2dfc30-45e9-396d-8654-25bd7bc622ca | -4.7027 | -46.3176 | 2025-11-16 01:40:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 54.9 |
| 0ee66eaa-e724-3c74-b5ba-dd33836ce441 | -12.0195 | -49.2659 | 2025-11-16 01:50:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 77.5 |
| 90bc9807-bd06-3bea-b30d-c3bb641bceff | -2.5238 | -47.8115 | 2025-11-16 01:50:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 175.6 |
| 87f653b8-32fb-39b5-982c-2c6120c27e61 | -12.2047 | -49.6121 | 2025-11-16 01:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 85.6 |
| 89b8faea-01f7-3d47-888f-260ffd72a02f | -12.6672 | -47.167 | 2025-11-16 01:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 68.5 |
| eccddab6-aabc-3ea8-8598-4e20b4777376 | -8.0513 | -43.1001 | 2025-11-16 01:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 77.5 |
| e1053454-351f-3f7e-8050-85d89f4bd96b | -8.0703 | -43.0981 | 2025-11-16 01:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 118.2 |
| 0befb87e-9a1a-3714-8cb0-dc36787e5016 | -5.3162 | -35.9204 | 2025-11-16 01:50:00 | GOES-19 | PARAZINHO | RIO GRANDE DO NORTE | Brasil | 2408805 | 24 | 33 | nan | nan | nan | Caatinga | 85.5 |
| 9ec6f7a8-5867-3674-83d4-321433c7e0f1 | -12.0004 | -49.2683 | 2025-11-16 01:50:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 130.9 |
| 188605c1-ece4-3dad-b60a-4935b74f0412 | -12.0 | -49.2901 | 2025-11-16 01:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 96.7 |
| 74e45202-db17-30ee-8aba-ad4978279931 | -2.5053 | -47.812 | 2025-11-16 01:50:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 59.2 |
| 2a3dc22b-9f16-3e48-956c-2f7b335f24e4 | -4.7395 | -46.3821 | 2025-11-16 01:50:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 65.7 |
| 6722ecc3-bd9b-30ab-96c6-12a7f762c751 | -2.5238 | -47.8332 | 2025-11-16 01:50:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 76.9 |
| 052ec4b7-1af9-3ac1-bbfe-3e316f462b4b | -2.8925 | -53.2842 | 2025-11-16 01:50:00 | GOES-19 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 51.6 |
| 6a86f20f-5988-339e-86ce-fa5170745fd6 | -12.0 | -49.2901 | 2025-11-16 02:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 114.5 |
| 553238fa-1c1e-3fb0-8da8-e0351eaf2ef2 | -12.2047 | -49.6121 | 2025-11-16 02:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 86.8 |
| c953bf61-0c41-3870-bd1d-debbf2aec8e0 | -2.5238 | -47.8332 | 2025-11-16 02:00:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 76.8 |
| 3796453b-6770-39a9-a9f9-9ad149f184fd | -8.0703 | -43.0981 | 2025-11-16 02:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 89.4 |
| 627f4fa7-681c-3896-aab9-30cbbaeccd70 | -2.5053 | -47.812 | 2025-11-16 02:00:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 56.8 |
| b0fb8203-bebc-3a46-9d86-bd12f65d5458 | -2.5238 | -47.8115 | 2025-11-16 02:00:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 136.7 |
| 7f30fd13-bfd3-336e-a8b4-273bfd717b62 | -4.7027 | -46.3176 | 2025-11-16 02:00:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 50.7 |
| fe3dabd6-9cea-395f-8bea-48d14544e25a | -4.7395 | -46.3821 | 2025-11-16 02:00:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 75.2 |
| a367d247-1ae5-37a9-bd82-944b2c475976 | -12.0004 | -49.2683 | 2025-11-16 02:00:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 135.3 |
| 1a78fd62-a7f2-33c6-b2ff-8197d55a983e | -8.0513 | -43.1001 | 2025-11-16 02:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 74.1 |
| f82c5e4b-8695-3b6c-9b0e-43c31d0543e0 | -12.6672 | -47.167 | 2025-11-16 02:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 71.0 |
| 39b3549a-30a8-3d62-bbff-1c7e32f62efd | -12.2047 | -49.6121 | 2025-11-16 02:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 82.9 |
| 11add948-138c-3a30-8470-f5089bd17b16 | -6.3121 | -43.7804 | 2025-11-16 02:10:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 51.8 |
| 387452f0-7149-39f5-9c6d-eb7c94ccf9de | -2.5238 | -47.8115 | 2025-11-16 02:10:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 137.5 |
| 23cef159-1d8a-3a3a-8875-5b405800a48b | -12.0004 | -49.2683 | 2025-11-16 02:10:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 140.5 |
| aed8b9dd-5a6e-3cd5-a22b-c78e4c6f45ec | -2.8925 | -53.2842 | 2025-11-16 02:10:00 | GOES-19 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 55.1 |
| a64cbc48-9e75-3ec6-9f9d-c6b571e56a6b | -2.5238 | -47.8332 | 2025-11-16 02:10:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 54.1 |
| 414edef6-148b-3707-8d9e-15cfe9adcf6d | -8.0703 | -43.0981 | 2025-11-16 02:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 81.0 |
| 73cf0ba9-0d99-30ae-82cc-a1b3339160a8 | -8.0513 | -43.1001 | 2025-11-16 02:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 84.8 |
| 2f39c0a0-4742-3600-a3ab-ae5425c815e6 | -4.7395 | -46.3821 | 2025-11-16 02:10:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 109.8 |
| 221d9fe6-cd54-3b3c-a987-168adaf81c07 | -4.4246 | -43.4038 | 2025-11-16 02:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 68.2 |
| b9de81ee-f921-3598-9840-2c7918bee115 | -12.6672 | -47.167 | 2025-11-16 02:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 66.0 |
| c6184185-ceaa-3c3e-b0b5-3029533e19e1 | -2.5053 | -47.812 | 2025-11-16 02:10:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 65.6 |
| 7bb96f17-4bc7-3c7b-a081-13bcbfc04abe | -12.0 | -49.2901 | 2025-11-16 02:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 106.1 |
| 82ace1e9-7463-3b2d-9e8d-00adc7f8f531 | -4.4246 | -43.4038 | 2025-11-16 02:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 69.7 |
| 20576cf3-7616-3a2a-a770-818604cb94f3 | -8.0703 | -43.0981 | 2025-11-16 02:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 66.5 |
| cf271f98-333b-3312-9232-237d194e81fb | -12.2047 | -49.6121 | 2025-11-16 02:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 85.3 |
| c97154b5-b763-3c09-961a-38a60e071a28 | -2.5238 | -47.8332 | 2025-11-16 02:20:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 52.7 |
| be6cda39-00e2-3de3-8a72-712834e921fd | -12.0004 | -49.2683 | 2025-11-16 02:20:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 136.1 |
| 9dc32366-d578-3cb4-8963-9bff3743f2d4 | -12.0 | -49.2901 | 2025-11-16 02:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 97.7 |
| 5f261cb0-33f6-3f75-b7a5-bc2564cec4c1 | -8.0513 | -43.1001 | 2025-11-16 02:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 66.5 |
| 3b00b011-d957-3bab-954d-884c3ca0e3c2 | -4.7395 | -46.3821 | 2025-11-16 02:20:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 77.8 |
| 2e1614f2-b1e3-3dfb-a882-be1e93c1aba2 | -2.5238 | -47.8115 | 2025-11-16 02:20:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 114.5 |
| 49415af4-0fd4-399c-b91e-6ce943f8135e | -2.5053 | -47.812 | 2025-11-16 02:20:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 52.8 |
| e3497374-2e85-377e-8af2-f75ca9074bd0 | -12.6672 | -47.167 | 2025-11-16 02:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 65.4 |
| 6af3e734-d6c7-3a0a-8a82-26835dd391bd | -8.0513 | -43.1001 | 2025-11-16 02:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 73.2 |
| 5e7a1336-3d38-36fc-8512-d577256721ad | -12.6672 | -47.167 | 2025-11-16 02:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 66.2 |
| afe04519-ab50-38a8-8fc4-56704e81d581 | -12.0 | -49.2901 | 2025-11-16 02:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 112.2 |
| 30c2a069-5c0c-3ddd-bdf7-b0456f206d5f | -4.7395 | -46.3821 | 2025-11-16 02:30:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 60.4 |
| 2a886221-34e7-30d8-a81f-46dc11ca78b5 | -8.0703 | -43.0981 | 2025-11-16 02:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 59.5 |
| 0ff13f09-0df3-3b5e-be78-c3702e89a36c | -2.5238 | -47.8332 | 2025-11-16 02:30:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 60.2 |
| 049dc256-540d-39a6-aaae-bb5a67afabbf | -12.0004 | -49.2683 | 2025-11-16 02:30:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 119.6 |
| b6140e58-b5ee-3abc-8077-a7460a30e1c8 | -4.4246 | -43.4038 | 2025-11-16 02:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 41.6 |
| f14b0033-6551-39ed-becb-7113115f2cfa | -12.2047 | -49.6121 | 2025-11-16 02:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 77.8 |
| d9f1001a-85a8-3b0c-976c-e8f4afc32c0d | -2.5238 | -47.8115 | 2025-11-16 02:30:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 107.1 |
| b193dcdc-df5d-3109-b498-6285dcf31c91 | -2.5053 | -47.812 | 2025-11-16 02:30:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 54.3 |
| 61222b14-d869-3365-a834-d00ff976f994 | -5.3442 | -43.0402 | 2025-11-16 02:30:00 | GOES-19 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 57.3 |
| 745626a0-d47a-39c4-8f20-4d1a5c2da399 | -12.2047 | -49.6121 | 2025-11-16 02:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 77.8 |
| f41999db-1cf0-3e23-9237-2d58bc9f6db0 | -4.4246 | -43.4038 | 2025-11-16 02:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 37.1 |
| ff0d0486-c3c5-3ef6-af33-bceaabf7ab62 | -12.0004 | -49.2683 | 2025-11-16 02:40:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 108.4 |
| aeb97a70-5646-37aa-9727-75d0fe244fcf | -2.5238 | -47.8332 | 2025-11-16 02:40:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 64.3 |
| 09cd6a0e-0090-3a13-85f2-a36ca1850f94 | -2.5238 | -47.8115 | 2025-11-16 02:40:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 105.1 |
| e1628504-1556-3641-962f-7524d203a4d2 | -5.3442 | -43.0402 | 2025-11-16 02:40:00 | GOES-19 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 66.0 |
| 04d8a92f-9119-3475-a4d9-cc6752bc35f8 | -8.0513 | -43.1001 | 2025-11-16 02:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 63.9 |
| 4a417f49-b816-3a24-a561-94a91469385c | -4.7395 | -46.3821 | 2025-11-16 02:40:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 55.3 |
| a42892b1-471f-3270-a2b6-db8d26429748 | -12.0 | -49.2901 | 2025-11-16 02:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 102.6 |
| 3add9db1-d7a8-312b-88ff-3fe796dbc309 | -12.0 | -49.2901 | 2025-11-16 02:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 98.2 |
| 12dc3fd8-9451-3415-8028-3fbfdb5af40f | -2.5053 | -47.812 | 2025-11-16 02:50:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 52.2 |
| 1d95e544-3cd0-3d3b-838f-5034b675158d | -6.3121 | -43.7804 | 2025-11-16 02:50:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 54.1 |
| 9e8d4bc3-774b-3138-8517-9a46a71470ef | -8.0513 | -43.1001 | 2025-11-16 02:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 67.7 |
| 5106cb6c-ddcc-3157-b1b7-f8aedc37b558 | -4.7395 | -46.3821 | 2025-11-16 02:50:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 54.2 |
| b2f2fe9e-57f1-3c0e-9665-ef5d4098799d | -12.0004 | -49.2683 | 2025-11-16 02:50:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 116.0 |
| b7c881bc-cde8-327f-98d8-d5511d329a05 | -2.5238 | -47.8332 | 2025-11-16 02:50:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 55.1 |
| a33d6901-d1c0-3146-8738-f1c10c7510cb | -2.5238 | -47.8115 | 2025-11-16 02:50:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 114.4 |
| 6e60b3e0-7140-3a02-aef2-a1cd968a8a1d | -8.0513 | -43.1001 | 2025-11-16 03:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 61.7 |
| 2f08b21c-4aeb-3ab6-95d7-1f9cfe5eb8bc | -2.5053 | -47.812 | 2025-11-16 03:00:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 55.3 |
| 1383e408-9142-3cd4-b7d7-9fd662c31021 | -9.7436 | -43.9542 | 2025-11-16 03:00:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 63.9 |
| d0d27025-ad56-3f91-ae7c-3252b5ce2bf9 | -4.4246 | -43.4038 | 2025-11-16 03:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 68.2 |
| d111f713-e437-3278-ab0a-8982662f68cf | -2.5238 | -47.8115 | 2025-11-16 03:00:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 112.0 |
| 7263250b-8e3f-3336-a01c-f1a43edeb799 | -7.0554 | -39.6227 | 2025-11-16 03:00:00 | GOES-19 | NOVA OLINDA | CEARÁ | Brasil | 2309201 | 23 | 33 | nan | nan | nan | Caatinga | 55.2 |
| 014ad51f-1044-3de7-ba69-17f306139d00 | -5.3442 | -43.0402 | 2025-11-16 03:00:00 | GOES-19 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 62.8 |
| f74be472-1427-3a80-9ea5-f723f47274d9 | -12.0 | -49.2901 | 2025-11-16 03:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 89.1 |


[Clique aqui para ver as próximas entradas](README13.md)
