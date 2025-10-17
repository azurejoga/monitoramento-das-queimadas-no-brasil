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

## Dados Diários - Página 121

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0eaecc3f-ccb5-3738-a92c-267bb589d0e4 | -13.4219 | -47.9511 | 2025-10-17 12:40:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 87.8 |
| cab07342-018c-3955-8f71-1ba0a844a1bd | -11.5729 | -44.0501 | 2025-10-17 12:40:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 112.2 |
| 791fd367-2b2b-33e3-80f4-5ec1c48d64e3 | -13.0483 | -47.3356 | 2025-10-17 12:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 102.9 |
| 05ef4429-f131-3045-802e-6f74c310953d | -11.1021 | -45.8717 | 2025-10-17 12:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 76.5 |
| 736acb18-70c5-32de-8a8b-1ed316601b80 | -10.6172 | -45.2282 | 2025-10-17 12:40:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 76.7 |
| c38c6442-46da-3918-a195-2da8276662cd | -12.4678 | -45.4694 | 2025-10-17 12:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 135.6 |
| 37038e0c-75a7-318c-9f31-c30b5c743c8c | -12.9414 | -47.9322 | 2025-10-17 12:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 117.6 |
| 1e1b92af-6faa-3355-8e23-8bb14baf769a | -11.5917 | -44.0707 | 2025-10-17 12:40:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 119.6 |
| a655e7a9-1f6c-3f49-ab45-7d4597d2d368 | -13.4412 | -47.9483 | 2025-10-17 12:40:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 110.6 |
| a0c47eb0-a025-39d9-aafd-389cc6f733d7 | -10.938 | -45.4146 | 2025-10-17 12:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 148.7 |
| 54e8ed74-da54-38c2-b332-0ca884810b2a | -13.4408 | -47.9706 | 2025-10-17 12:40:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 80.7 |
| 49f69d6a-1e2d-35c0-a1fd-641a6a440026 | -15.82036 | -53.61044 | 2025-10-17 12:40:00 | TERRA_M-T | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 4ec99d15-907e-3777-b7b0-0adf361bc6b3 | -14.82297 | -57.78215 | 2025-10-17 12:40:00 | TERRA_M-T | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 71dc6676-4d81-338f-895b-1d2f2562fb97 | -16.30552 | -53.96353 | 2025-10-17 12:40:00 | TERRA_M-T | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 6.4 |
| cd43ba0d-64e1-3fd7-a3b1-bd6de90c14b1 | -16.90466 | -53.02349 | 2025-10-17 12:40:00 | TERRA_M-T | SANTA RITA DO ARAGUAIA | GOIÁS | Brasil | 5219407 | 52 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 745ea57e-43c0-3510-967f-1618b7e23f17 | -15.83054 | -53.60253 | 2025-10-17 12:40:00 | TERRA_M-T | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 6d50f73b-fc68-3b81-81f0-027e476f2baa | -18.26921 | -51.30712 | 2025-10-17 12:40:00 | TERRA_M-T | APARECIDA DO RIO DOCE | GOIÁS | Brasil | 5201454 | 52 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 94db2587-692c-3723-ac96-fe3417019076 | -15.55291 | -50.13328 | 2025-10-17 12:40:00 | TERRA_M-T | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 6768a955-5535-3fcf-879c-bc5a9bc70e56 | -15.15371 | -56.45132 | 2025-10-17 12:40:00 | TERRA_M-T | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 1fea02d2-7e6e-30d1-ab40-1e37db12c7e2 | -18.38725 | -55.4539 | 2025-10-17 12:40:00 | TERRA_M-T | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 33.8 |
| b98a981d-630c-3794-b3a1-e35870a6f756 | -18.34267 | -51.69156 | 2025-10-17 12:40:00 | TERRA_M-T | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 19.9 |
| 493c0ad2-1b51-3974-97e8-a3ec7cb7df67 | -15.82166 | -53.60117 | 2025-10-17 12:40:00 | TERRA_M-T | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 20.6 |
| 52e9d967-60a2-368e-a25c-c19162143dcb | -18.27075 | -51.29488 | 2025-10-17 12:40:00 | TERRA_M-T | APARECIDA DO RIO DOCE | GOIÁS | Brasil | 5201454 | 52 | 33 | nan | nan | nan | Cerrado | 32.1 |
| edd36f72-fa66-3039-866b-d895a9cb69be | -16.91376 | -53.02483 | 2025-10-17 12:40:00 | TERRA_M-T | SANTA RITA DO ARAGUAIA | GOIÁS | Brasil | 5219407 | 52 | 33 | nan | nan | nan | Cerrado | 8.1 |
| a1cb87eb-03f2-3bb5-947c-94d43128a10e | -19.34768 | -50.3544 | 2025-10-17 12:40:00 | TERRA_M-T | UNIÃO DE MINAS | MINAS GERAIS | Brasil | 3170438 | 31 | 33 | nan | nan | nan | Cerrado | 76.6 |
| ba59f8b9-19b8-3a81-84b2-c60ef8224dd9 | -19.34598 | -50.36928 | 2025-10-17 12:40:00 | TERRA_M-T | UNIÃO DE MINAS | MINAS GERAIS | Brasil | 3170438 | 31 | 33 | nan | nan | nan | Cerrado | 72.0 |
| 14f0b1cf-5387-3fbb-9a9a-0650358fa8ae | -18.72779 | -51.71395 | 2025-10-17 12:40:00 | TERRA_M-T | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 7.4 |
| e3e42bfc-8100-32e1-830b-e0b04679c76c | -18.34278 | -51.69815 | 2025-10-17 12:40:00 | TERRA_M-T | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 22.8 |
| 83ff0b23-1b80-30d0-b7bc-e80cfbd5ecdf | -15.15213 | -56.46161 | 2025-10-17 12:40:00 | TERRA_M-T | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| b31c313c-14a2-3984-bf0a-aadb825b5437 | -18.34113 | -51.70346 | 2025-10-17 12:40:00 | TERRA_M-T | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 14.0 |
| e4228264-52a3-38d2-91fd-bd3c95c6aa71 | -19.24579 | -48.79317 | 2025-10-17 12:40:00 | TERRA_M-T | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 26.2 |
| 2816a51e-eec9-3760-97cd-fbb95f80ed30 | -20.28374 | -56.04187 | 2025-10-17 12:42:00 | TERRA_M-T | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 11.5 |
| 4dd75a11-ca1e-3dc2-b266-19dd8acb2573 | -23.21164 | -52.26847 | 2025-10-17 12:42:00 | TERRA_M-T | NOVA ESPERANÇA | PARANÁ | Brasil | 4116901 | 41 | 33 | nan | nan | nan | Mata Atlântica | 14.8 |
| 6350f683-8a50-3e6d-9935-eda23dc30c72 | -19.45311 | -55.91926 | 2025-10-17 12:42:00 | TERRA_M-T | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 9.3 |
| 8ee3197e-8c72-3763-8224-1b07e2e812d5 | -20.75496 | -57.86013 | 2025-10-17 12:42:00 | TERRA_M-T | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 10.9 |
| ef5e54a5-7552-399e-b7b6-c39de56fbb9f | -11.5917 | -44.0707 | 2025-10-17 12:50:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 155.0 |
| 0bf8890e-19e4-3f31-b172-5d43abf7bb88 | -13.9127 | -45.5808 | 2025-10-17 12:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 71.0 |
| ebaeb747-4c2c-3bc7-a559-555aea2a23be | -12.4866 | -45.4895 | 2025-10-17 12:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 89.2 |
| 12e089c0-3c1d-35f9-8af4-ac28c66ea178 | -11.3988 | -44.1464 | 2025-10-17 12:50:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 110.7 |
| 2e016845-3132-3fc5-8f97-9f20be672c44 | -9.9828 | -47.0234 | 2025-10-17 12:50:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 218.6 |
| 290d88e5-5af7-3257-b681-f8be9dc5778d | -9.9638 | -47.0256 | 2025-10-17 12:50:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 83.8 |
| 5eab24dc-d6f3-3959-be1d-a2226dcc095e | -13.4412 | -47.9483 | 2025-10-17 12:50:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 100.8 |
| dcd9d7bd-e2f4-3b58-b9a9-12a24415357b | -11.4731 | -44.2756 | 2025-10-17 12:50:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 115.9 |
| 01bd2721-aa69-3f49-bbbc-d43ad863aee1 | -13.4408 | -47.9706 | 2025-10-17 12:50:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 76.5 |
| 52d94204-f96a-3139-b4a6-a05ad090f2bd | -11.5921 | -44.0472 | 2025-10-17 12:50:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 117.2 |
| 928213e7-ef4e-3bac-9732-b7bc6052b5f8 | -12.487 | -45.4664 | 2025-10-17 12:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 156.4 |
| 1f4a90e3-99aa-3b5a-8549-990d9a8a9984 | -11.3992 | -44.1229 | 2025-10-17 12:50:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 104.9 |
| f8e6e4dd-6dc6-353b-b8f7-54e278bfd689 | -13.4794 | -47.9649 | 2025-10-17 12:50:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 79.0 |
| 713e5524-2c4c-3473-bf05-d35e4bff21e4 | -12.9414 | -47.9322 | 2025-10-17 12:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 79.8 |
| 6a3620d7-831f-3987-8f74-7172e47bcbda | -11.1021 | -45.8717 | 2025-10-17 12:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 77.7 |
| a6599fae-ba5d-3fb2-ad2f-95f013fd0118 | -11.496 | -44.0617 | 2025-10-17 12:50:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 118.2 |
| 42e3912f-8ff5-314e-8dd2-5d3b7d793f17 | -10.938 | -45.4146 | 2025-10-17 12:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 198.4 |
| 43cfb7bd-49d2-39f0-83dc-ae59ea9cce6c | -12.9607 | -47.9294 | 2025-10-17 12:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 123.2 |
| ff8804d4-a4dd-33d5-96c7-ff7807962cd8 | -12.4678 | -45.4694 | 2025-10-17 12:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 94.4 |
| 4a1bd09d-2574-3b10-874a-6d75ea70b4b1 | -11.1212 | -45.8691 | 2025-10-17 12:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 105.2 |
| b8d7ea4f-f6c8-3a1f-9f79-f77e7309a814 | -13.0483 | -47.3356 | 2025-10-17 12:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 104.9 |
| 41b12e2a-388c-39f8-b29a-01c5dbbd212d | -11.1403 | -45.8665 | 2025-10-17 12:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 82.8 |
| b05495a0-163e-32b8-93b3-aca8594fce9e | -10.1063 | -47.6525 | 2025-10-17 12:50:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 76.9 |
| 247789b3-b686-38cd-bf4e-12091f36647c | -11.5729 | -44.0501 | 2025-10-17 12:50:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 108.3 |
| 17d56663-3c47-3f28-bfb4-7a0a96e1a07b | -10.9189 | -45.4171 | 2025-10-17 12:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 68.7 |
| e315cc46-10fa-37fc-b874-be864a20d3f7 | -10.6172 | -45.2282 | 2025-10-17 12:50:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 97.3 |
| 13548797-6850-3468-a156-4fb0c34afa26 | -13.4416 | -47.9259 | 2025-10-17 12:50:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 77.2 |
| f2091bfa-cdd0-3944-984f-de9902269cb4 | -9.9831 | -47.0011 | 2025-10-17 12:50:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 140.2 |
| 3f661313-eb6a-3506-a9a1-050125322ba0 | -10.9748 | -47.9042 | 2025-10-17 12:50:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 58.3 |
| c00e6bda-8c3a-3065-b968-c49c8dcad640 | -13.4219 | -47.9511 | 2025-10-17 12:50:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 78.9 |
| f6eaf7ed-a20a-35d3-832f-df32d6e02763 | -13.0488 | -47.3131 | 2025-10-17 12:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 153.5 |
| ffc52b8a-e829-3852-974f-6053027bec87 | -10.6028 | -47.3955 | 2025-10-17 13:00:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 117.9 |
| 9d9ac1ff-4691-3c5f-84d9-55447e855218 | -10.534 | -49.5471 | 2025-10-17 13:00:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 75.6 |
| 8b6b028e-1510-3c41-8472-e2d744e1f6bb | -10.1326 | -44.6008 | 2025-10-17 13:00:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 78.8 |
| 4dca8af5-c12a-3694-948d-f705c1d87bff | -11.2837 | -45.2754 | 2025-10-17 13:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 90.6 |
| c114f35a-2a92-3eb3-a057-ee4a2b53e7e8 | -10.9748 | -47.9042 | 2025-10-17 13:00:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 68.3 |
| ce94faba-34b0-39d2-bf42-f218558eb279 | -10.5136 | -43.4052 | 2025-10-17 13:00:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 66.7 |
| 08faf232-fd16-314b-a277-ce7b2a7f2529 | -11.1021 | -45.8717 | 2025-10-17 13:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 146.4 |
| 6e316ec5-cf8e-319f-a41c-fad54ba53f79 | -11.2642 | -45.3011 | 2025-10-17 13:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 76.5 |
| 4c76f811-0a15-389f-b23c-f2a4bb3952dc | -10.938 | -45.4146 | 2025-10-17 13:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 152.0 |
| e81af315-0d81-3e33-ad33-ca4b2e0ff12f | -11.5729 | -44.0501 | 2025-10-17 13:00:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 129.6 |
| 328d4ec0-1f4b-3c91-8031-a629658d10b1 | -11.5917 | -44.0707 | 2025-10-17 13:00:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 152.7 |
| 7b731fb6-d27a-3584-afe1-5198250ebf17 | -13.4219 | -47.9511 | 2025-10-17 13:00:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 79.7 |
| 57fba910-729a-3033-a6ba-548058f1e48b | -12.4678 | -45.4694 | 2025-10-17 13:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 96.1 |
| 8a5a4e2b-35b6-3bab-a582-f267402e91f3 | -11.1399 | -45.8893 | 2025-10-17 13:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 92.9 |
| 274f1971-22b1-399a-a197-a50e192105e0 | -12.9607 | -47.9294 | 2025-10-17 13:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 79.8 |
| 7df9e505-27da-3373-9ee5-a590a998bc62 | -10.5132 | -43.4289 | 2025-10-17 13:00:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 190.4 |
| 73031818-d47d-315a-80ea-f0b393207ea1 | -9.9828 | -47.0234 | 2025-10-17 13:00:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 161.7 |
| 8a4c9d90-1de7-3b68-a7dd-c0b2ef4ce641 | -11.1212 | -45.8691 | 2025-10-17 13:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 121.2 |
| ab73b9a5-8c2d-3ad8-b29f-fa185b73dbca | -9.9831 | -47.0011 | 2025-10-17 13:00:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 128.2 |
| 9ce3d389-269b-3885-a74b-f667f8da9941 | -9.9638 | -47.0256 | 2025-10-17 13:00:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 65.4 |
| 30e9d202-5859-3adf-a4fe-fade81d2ca4a | -12.487 | -45.4664 | 2025-10-17 13:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 92.0 |
| 55a012a5-cb66-3d45-9b3c-4732970be4fb | -13.4412 | -47.9483 | 2025-10-17 13:00:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 91.2 |
| 9adc860e-2013-3e55-9efb-97e66cd2c0a5 | -13.4794 | -47.9649 | 2025-10-17 13:00:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 70.5 |
| 7c2cd736-4130-3682-81d1-35936e487508 | -11.9257 | -46.845 | 2025-10-17 13:00:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 69.6 |
| 67b50408-6c00-36ed-8205-97893577bf15 | -11.5921 | -44.0472 | 2025-10-17 13:00:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 144.6 |
| d2430de7-f22e-3d4d-87b8-7ecbb26fe80f | -9.898 | -47.6758 | 2025-10-17 13:00:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 68.4 |
| 72e113c1-f29d-38a4-8e3b-3c56945e2641 | -11.5724 | -44.0736 | 2025-10-17 13:00:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 105.8 |
| 2eb24065-14e6-35e6-b8cb-a57658115ab4 | -10.6172 | -45.2282 | 2025-10-17 13:00:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 81.2 |
| 828c1a1f-cd93-336d-a839-6f36a91c0f0b | -11.1403 | -45.8665 | 2025-10-17 13:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 160.1 |
| 0cbabe8b-6f98-310a-a934-d15d5edcaa4d | -10.9189 | -45.4171 | 2025-10-17 13:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 94.5 |
| 148b49b2-c8d7-3937-a8a6-a781d2dc8765 | -12.1678 | -45.0771 | 2025-10-17 13:00:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 79.4 |
| 3388c4a0-e9e9-3b30-bfa0-363416bd65fd | -10.4941 | -43.4315 | 2025-10-17 13:00:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 121.3 |
| b01f9f1e-8e21-3ccf-953a-f07fbf63f32c | -10.5128 | -43.4525 | 2025-10-17 13:00:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 81.7 |
| 610796f1-c26d-31c5-8493-dbba05ce8f05 | -10.6028 | -47.3955 | 2025-10-17 13:10:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 57.7 |


[Clique aqui para ver as próximas entradas](README122.md)
