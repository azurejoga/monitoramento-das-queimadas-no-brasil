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

## Dados Diários - Página 46

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6351879a-e8f7-3e42-b3ce-cc35a32b1d87 | -7.72923 | -50.28622 | 2025-08-29 04:40:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 21efb17d-eee1-365c-a010-7726df9a3158 | -6.37631 | -44.33004 | 2025-08-29 04:40:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 543aa116-2f83-3539-b98a-e8b0918f45c8 | -10.72328 | -47.01603 | 2025-08-29 04:40:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| abc63bfd-d597-3945-ab38-dc278dd66b0c | -6.08548 | -43.87426 | 2025-08-29 04:40:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 5f1d22a7-bf92-3ba9-8f49-3b86b2ef8a51 | -6.53251 | -44.10612 | 2025-08-29 04:40:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6def9287-0159-33e5-ab39-dcfbbed9057b | -11.34616 | -43.56883 | 2025-08-29 04:40:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8ea31f3c-c6db-38f9-b238-283d09ea220f | -8.44804 | -43.65386 | 2025-08-29 04:40:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c8fa918c-6448-3f8a-9d83-50bac3b56b94 | -12.82858 | -48.1674 | 2025-08-29 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| c7192588-2340-3a41-86eb-0df38c0e2d4c | -12.6879 | -48.18874 | 2025-08-29 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 25.9 |
| b74c8d8c-3266-31c0-8f07-19263fa27d87 | -9.77943 | -64.24854 | 2025-08-29 04:40:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 12.4 |
| d7c3352d-a6cc-3ae1-b527-cff7796e0feb | -11.61419 | -46.2041 | 2025-08-29 04:40:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 5a9bc871-5dd3-3643-be29-56b0594eb93d | -11.35672 | -43.56011 | 2025-08-29 04:40:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 09b402b9-6120-3284-8ceb-37cf5f87372b | -7.62323 | -60.84945 | 2025-08-29 04:40:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bcd6b43d-9611-39bd-b653-fce4b768ef5f | -10.07756 | -48.86074 | 2025-08-29 04:40:00 | NOAA-21 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a69bc975-c854-3e54-a595-dcdc84713da6 | -7.63516 | -46.5545 | 2025-08-29 04:40:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8a6f6cd1-cab2-30d5-aa4f-d806a7da7a3d | -11.55958 | -47.61829 | 2025-08-29 04:40:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f8d946dd-6607-3819-8b42-199f71ba9d10 | -11.23837 | -44.97821 | 2025-08-29 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a014feac-3297-35a3-af7e-5dc039ffa044 | -11.51264 | -57.99118 | 2025-08-29 04:40:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8eb4a987-2802-3a6a-a173-606ce0b6e5b0 | -11.32957 | -43.56001 | 2025-08-29 04:40:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 09444691-8f67-316b-98cf-9142af7a9359 | -7.22136 | -45.31205 | 2025-08-29 04:40:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 91b532fd-0a86-3eb3-9616-89f07bbdd784 | -7.72756 | -50.27526 | 2025-08-29 04:40:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 16b6a636-ba9c-3e76-a042-57712ecfd4f3 | -9.15395 | -59.58065 | 2025-08-29 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| fe965530-c1fd-34cc-b069-c189f2ad3ad6 | -10.96896 | -46.84362 | 2025-08-29 04:40:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fc558fb0-9cd9-3231-8753-f1ec2be23a39 | -11.23115 | -55.05578 | 2025-08-29 04:40:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d65fcd97-a8dc-3785-86bb-a2ac5e044153 | -9.20517 | -59.54188 | 2025-08-29 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6839e193-4f7d-3203-9ff0-967525f1668b | -6.14551 | -44.4297 | 2025-08-29 04:40:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d790fb30-3ead-3592-a06e-f34bde10c9d5 | -6.26396 | -43.80744 | 2025-08-29 04:40:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b55c893f-112a-3056-aec9-308c4c97a1e9 | -10.02495 | -48.06854 | 2025-08-29 04:40:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 05e6dd78-df4b-363f-8201-19644dfdf74d | -9.43018 | -47.64183 | 2025-08-29 04:40:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 42ed2aa4-7af0-3ddd-8ef2-477807d5f984 | -12.70389 | -48.15358 | 2025-08-29 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 788e4cb8-80e5-34c0-ba8b-91b39a37a1b5 | -7.63579 | -46.55027 | 2025-08-29 04:40:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5f37a516-e32f-3204-b130-fc8706102bc5 | -10.37047 | -57.83078 | 2025-08-29 04:40:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 46c2e307-e90d-3902-867d-f7ff670ac0d5 | -8.69488 | -62.47088 | 2025-08-29 04:40:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c8497c63-8df0-3cde-9421-33dbb1084401 | -6.38515 | -45.58389 | 2025-08-29 04:40:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 851aacbf-9450-3b4d-927d-b016f130e9d0 | -12.90103 | -48.139 | 2025-08-29 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 1e8cc0a5-6f91-3901-97c4-1c1c47b21c89 | -8.10369 | -45.0089 | 2025-08-29 04:40:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0692f6b6-9d32-347c-8d9b-331bc7e67a65 | -10.83589 | -47.50192 | 2025-08-29 04:40:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 18062b16-9531-3d83-85e3-79533134ca93 | -10.28825 | -64.48837 | 2025-08-29 04:40:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b63a6b0f-c3fe-3bc0-877d-cc9608958015 | -12.89271 | -48.12079 | 2025-08-29 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a1dd1605-9585-35dc-8bfb-99c7d61ce767 | -10.6831 | -47.08596 | 2025-08-29 04:40:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 4dce9294-3e58-3090-8a64-d7f92a5db8a5 | -6.70612 | -49.45768 | 2025-08-29 04:40:00 | NOAA-21 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5fe8bde0-1e4f-3fd4-93ac-26a95c51fe17 | -9.8245 | -44.89904 | 2025-08-29 04:40:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 51081be9-2f5e-3d03-892e-73e79bf5674f | -6.19771 | -43.32088 | 2025-08-29 04:40:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| dc5f83c8-4002-31c6-bce2-5160f7d00f7a | -10.98012 | -46.91237 | 2025-08-29 04:40:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 48.4 |
| 0682b0f6-8727-33b3-bcea-951dbc84750c | -9.67827 | -48.32245 | 2025-08-29 04:40:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3a36b020-0780-3cb5-8240-7d57d7f76960 | -10.85723 | -60.81435 | 2025-08-29 04:40:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 2f628e42-8410-322d-af99-9a29df218994 | -6.5498 | -43.92365 | 2025-08-29 04:40:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| bed67e97-f273-3af3-8e3c-abd72d3c0e0f | -11.22073 | -55.0565 | 2025-08-29 04:40:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e975674b-3d90-33f0-af83-b1a4cb65cae3 | -10.99 | -46.85598 | 2025-08-29 04:40:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f967cb3f-2e28-342b-946f-2125aa3e8631 | -7.61074 | -42.69418 | 2025-08-29 04:40:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| ce32ac88-5c4a-35ea-ac2d-013f7bfaa96d | -7.74794 | -50.27498 | 2025-08-29 04:40:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 12256fa0-d275-35e8-b3fc-d63b5208014b | -10.6186 | -54.9086 | 2025-08-29 04:40:00 | NOAA-21 | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| d15c76fa-aa1e-38f4-afd2-7fd337d5169e | -7.75124 | -50.27551 | 2025-08-29 04:40:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 74a7e131-95a8-3190-ba8d-87cb12d2ba0b | -11.31965 | -43.56351 | 2025-08-29 04:40:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ad60e877-6145-3791-bfa3-a68aebc15e90 | -7.07647 | -44.28936 | 2025-08-29 04:40:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a217ca00-d662-3aae-b077-7e1efa5b5e47 | -10.36641 | -57.79985 | 2025-08-29 04:40:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 872c9720-3c0b-327f-95b7-c3fea6fa81c5 | -11.58168 | -46.26499 | 2025-08-29 04:40:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| a9961f04-0bd9-3464-88ad-76fdc545f3dd | -6.14067 | -44.42978 | 2025-08-29 04:40:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c958f422-821d-3447-b557-e98cf2e0c13b | -6.71165 | -49.46562 | 2025-08-29 04:40:00 | NOAA-21 | SAPUCAIA | PARÁ | Brasil | 1507755 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 16ab8b5a-08c5-39bc-a5af-e2dd1cebce0a | -11.574 | -49.51794 | 2025-08-29 04:40:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 218886ce-2511-3475-a993-c96151cb8401 | -9.41339 | -60.57031 | 2025-08-29 04:40:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 1ba11ce8-30a6-3938-a4fe-1ce6e9338f72 | -9.51833 | -46.54324 | 2025-08-29 04:40:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 8bb9feba-99fa-391d-b7e1-ae21744d1629 | -10.68739 | -47.08221 | 2025-08-29 04:40:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ab4f1551-4c56-3d7b-8a07-9cc196c492ab | -6.12032 | -43.30071 | 2025-08-29 04:40:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.5 |
| d29fc5e1-06ec-34c1-aa4d-623db81401d7 | -9.45111 | -60.55675 | 2025-08-29 04:40:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 45.2 |
| 9364899a-d98c-369b-8a03-f58bd6bef2b9 | -11.22564 | -55.06469 | 2025-08-29 04:40:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| bf9378dd-8abc-39b1-bab0-260f47dcfb74 | -6.40955 | -44.66775 | 2025-08-29 04:40:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7f3dcc84-b7ec-3577-bf3e-d8e8df092f93 | -6.81368 | -44.3206 | 2025-08-29 04:40:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| defaa711-fb09-3dc0-9d55-3f61987ea469 | -9.45526 | -60.56601 | 2025-08-29 04:40:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 010e96bf-fe16-3285-b757-21ea5fb8ed99 | -7.05434 | -44.35551 | 2025-08-29 04:40:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 7a90a159-40bf-32b6-82d9-c33134d8c411 | -10.86287 | -47.49328 | 2025-08-29 04:40:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 15523a76-b1ab-3198-b932-23b8a894525f | -10.02901 | -48.06517 | 2025-08-29 04:40:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 30c69091-807f-3764-b998-4c8cd0a5cbbd | -7.72538 | -50.28915 | 2025-08-29 04:40:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 217233b5-7441-3b0f-8b8a-60b426d45a24 | -12.96361 | -44.57788 | 2025-08-29 04:40:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 877ea403-fe17-3556-b931-c1d27d506b76 | -11.94032 | -46.70559 | 2025-08-29 04:40:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 4bbf9c3f-0230-322a-8ae5-6ab525657326 | -10.36728 | -57.79498 | 2025-08-29 04:40:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a8846ac1-70e8-343e-8683-21f017db74dc | -6.23524 | -43.82732 | 2025-08-29 04:40:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| fb7f40ba-c7c0-3cc8-9349-4b75a24da353 | -9.67371 | -48.32933 | 2025-08-29 04:40:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 36dc33ce-662e-3c4f-9e35-9396adc73f77 | -12.67086 | -45.29658 | 2025-08-29 04:40:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1fdce986-e5ae-3481-b7e4-053de56afc06 | -11.16713 | -47.14875 | 2025-08-29 04:40:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d9acb012-832e-39eb-a7e8-e388b1786820 | -11.40926 | -46.91203 | 2025-08-29 04:40:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8500a250-d8d0-3ae3-b4b5-61753834357a | -7.04233 | -44.3807 | 2025-08-29 04:40:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5bbdf710-699e-3b63-9e6d-bdba1bce41a4 | -6.54448 | -43.93087 | 2025-08-29 04:40:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 26.8 |
| 1347aaea-b086-3f41-9153-05e9fcf27d55 | -6.25194 | -44.43806 | 2025-08-29 04:40:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8c8bad45-c275-3877-92fc-a801fea7e0c6 | -6.81327 | -44.99912 | 2025-08-29 04:40:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c657e6dc-af89-3877-9625-e4013d32b9dc | -9.4198 | -60.56746 | 2025-08-29 04:40:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 67a872d5-2858-3927-8e1d-7c0612065679 | -10.93963 | -46.86231 | 2025-08-29 04:40:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e92884f1-3ab6-3a7b-ae0d-8c306752e88b | -7.6435 | -42.66378 | 2025-08-29 04:40:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 454453a7-d329-3510-b43a-daa3d56c5373 | -12.68556 | -48.15475 | 2025-08-29 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 8df22bf3-ae5e-366d-bd7f-ed3498525f08 | -12.9507 | -46.14577 | 2025-08-29 04:40:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7b030351-89d1-351b-9981-3730757f31eb | -8.75019 | -47.39814 | 2025-08-29 04:40:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 30d1579d-142e-3841-bc7b-632c05c797b6 | -6.52332 | -42.99805 | 2025-08-29 04:40:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 606b4e48-1621-32fb-bae7-f524cd07baa4 | -12.7092 | -48.1919 | 2025-08-29 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 09378409-f4ac-301f-be68-0fdb3984b119 | -12.69143 | -48.1894 | 2025-08-29 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 25.9 |
| 926b8e8f-ff08-33e4-a693-31954df89709 | -10.36553 | -57.80473 | 2025-08-29 04:40:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| f3751d90-bfba-348f-8bc3-deaed452438e | -6.35065 | -44.47851 | 2025-08-29 04:40:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9c3a5738-a07b-3d0d-b074-b059ea6ffae8 | -6.48567 | -44.40533 | 2025-08-29 04:40:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a374ae73-4b7d-3ede-bccd-4814fa492d10 | -6.55348 | -43.92808 | 2025-08-29 04:40:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d637e627-38e8-33cf-a5b9-31596480cf07 | -9.16052 | -59.57501 | 2025-08-29 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ea94283c-1935-3173-8882-026e94c1b575 | -8.90537 | -47.32643 | 2025-08-29 04:40:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |


[Clique aqui para ver as próximas entradas](README47.md)
