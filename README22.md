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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 15a45a88-aa63-3a26-8684-bb8a9809ebd6 | -10.62694 | -47.88629 | 2025-10-29 03:55:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 1444dfe5-cf81-3e68-84db-6506e4bee510 | -14.32383 | -46.51505 | 2025-10-29 03:55:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1d0b9711-d4fc-340f-8b29-77035de3df2c | -12.35865 | -50.15493 | 2025-10-29 03:55:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 96771d1a-3485-3035-953a-73542d6cc9b0 | -10.8549 | -47.90101 | 2025-10-29 03:55:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e9d8fad5-8f3a-3c3d-ba2c-e7a61c1c92a9 | -10.77575 | -45.05349 | 2025-10-29 03:55:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 981a6e50-8e36-3cfd-9aa1-4c6a6ebb0bdc | -13.01692 | -48.76882 | 2025-10-29 03:55:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 31ba4ea7-9542-3248-bfec-d0edabb5e365 | -9.7563 | -45.00706 | 2025-10-29 03:55:00 | NOAA-21 | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 765e725a-d38e-3687-a3d2-f5c3894c617c | -15.18442 | -47.21006 | 2025-10-29 03:55:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d31d7f7a-6b53-302e-91c8-4c6bd8637987 | -9.80026 | -47.75331 | 2025-10-29 03:55:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 7b0611b5-5b15-389c-9fc1-e38372a69d9d | -13.57156 | -49.61611 | 2025-10-29 03:55:00 | NOAA-21 | BONÓPOLIS | GOIÁS | Brasil | 5203575 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 68fc9fe5-b6e8-32a0-9908-e1abc713f1ee | -13.57567 | -49.61526 | 2025-10-29 03:55:00 | NOAA-21 | BONÓPOLIS | GOIÁS | Brasil | 5203575 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8892feba-94c1-3d71-88d3-48f020563c87 | -10.76672 | -47.83017 | 2025-10-29 03:55:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 76752df0-a58c-302b-b234-8244a6a2b354 | -13.56616 | -47.15351 | 2025-10-29 03:55:00 | NOAA-21 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 405e6471-3e66-3867-9d65-8908dac45657 | -9.01913 | -45.0964 | 2025-10-29 03:55:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1724f8b6-ab03-3b95-b5aa-c697ce5ee8e5 | -11.14344 | -44.94089 | 2025-10-29 03:55:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2723639d-6703-3d84-a551-798fd4bb0149 | -8.69279 | -47.13894 | 2025-10-29 03:55:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8211e6f1-530a-3cf7-aaa2-337a13bb0581 | -12.35995 | -44.06682 | 2025-10-29 03:55:00 | NOAA-21 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3f36c991-9c00-3493-af0d-94c0ac36c1a1 | -9.54766 | -46.92506 | 2025-10-29 03:55:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 34200489-0f9e-3f3b-9597-0d387b6a1558 | -12.68784 | -48.44155 | 2025-10-29 03:55:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 161de961-7006-3a81-896d-256ec00030aa | -13.32078 | -47.43425 | 2025-10-29 03:55:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 110cff34-31c6-369b-86bc-11efeb528b02 | -14.48334 | -43.94505 | 2025-10-29 03:55:00 | NOAA-21 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 84ad0b65-970d-3b35-bf6e-0e8d1897a8fc | -15.17381 | -47.21689 | 2025-10-29 03:55:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 304e0d68-64e6-3709-862a-b557e394f50c | -12.4373 | -43.75475 | 2025-10-29 03:55:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 0eec1f24-8379-353f-a092-076cc2afe820 | -12.12201 | -45.2017 | 2025-10-29 03:55:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1caa9f8a-da67-3b32-9e22-5ea9805dc854 | -13.47538 | -47.81973 | 2025-10-29 03:55:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b326b1a1-146a-3774-8256-3418c7f2d888 | -9.57281 | -44.71363 | 2025-10-29 03:55:00 | NOAA-21 | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e6ce39bf-2580-39ba-8f84-d949d613e192 | -10.52279 | -47.74883 | 2025-10-29 03:55:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 64194d3f-d468-3631-86c1-9b68e66a3224 | -13.60968 | -46.47521 | 2025-10-29 03:55:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f5e6b8bf-69fe-3369-a3c0-d6ee03ae975f | -10.85655 | -47.89231 | 2025-10-29 03:55:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f06e2b4e-6701-3c12-8956-6e8062da5f72 | -13.79144 | -43.74195 | 2025-10-29 03:55:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e4ec752e-f786-3fe1-a205-afc598a5b1bc | -13.33148 | -47.48236 | 2025-10-29 03:55:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| e3dbe8ea-bd82-389b-9460-1aa947a444af | -10.57975 | -49.75505 | 2025-10-29 03:55:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 713d66f2-26c7-3220-b01b-347512f4f567 | -14.31496 | -48.01353 | 2025-10-29 03:55:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| fdd63305-f578-38e3-9bdf-14d264ee4a60 | -12.14627 | -45.20995 | 2025-10-29 03:55:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1a1d2faf-a339-3ffa-98ce-8c14546c304c | -10.54549 | -45.05089 | 2025-10-29 03:55:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d4733542-c780-37a6-900f-035592443f4a | -9.75331 | -45.00631 | 2025-10-29 03:55:00 | NOAA-21 | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 5a17b9e7-7456-39b2-9f35-9bf03c212c03 | -15.19506 | -47.20296 | 2025-10-29 03:55:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b32fd733-b8a8-36df-90c0-fa7d22e70ebc | -8.56007 | -47.01514 | 2025-10-29 03:55:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 90bf0510-a477-3274-b02c-1b354cbff967 | -13.60887 | -46.47972 | 2025-10-29 03:55:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b3e386a1-8e4a-3ad2-9c05-e42b88606707 | -13.8687 | -48.48755 | 2025-10-29 03:55:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3826cde9-703b-31ea-8dda-3797e977128d | -13.63895 | -47.04218 | 2025-10-29 03:55:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 0f4bd83a-180c-3f7d-870f-a1acaeba2d14 | -15.33951 | -42.00704 | 2025-10-29 03:55:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 050ea2ff-94ad-3c2c-a2e7-577ca9fed88d | -13.63697 | -46.49729 | 2025-10-29 03:55:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 90c5ddd0-8b0a-329c-926a-ab673a74a57c | -10.5154 | -47.73206 | 2025-10-29 03:55:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8b545560-2eaf-3bb6-b60d-72f7bd4dfbf6 | -8.88842 | -47.53559 | 2025-10-29 03:55:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| dbea030d-e42f-32b5-8802-a20cc360549e | -15.34226 | -42.01146 | 2025-10-29 03:55:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| e6b1ac70-7bda-3755-991b-195f1f6e7895 | -13.48648 | -47.45039 | 2025-10-29 03:55:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1108b3d4-330f-3d74-98ec-4018ce164b2f | -14.23993 | -48.11843 | 2025-10-29 03:55:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 50481e10-f3a4-303b-af3e-0048570eb0c1 | -14.88614 | -46.76397 | 2025-10-29 03:55:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| eb1311ee-2574-391c-8bf4-ec9304b497ea | -9.01637 | -43.97522 | 2025-10-29 03:55:00 | NOAA-21 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b0666dbf-ad95-30e8-9032-de0389c2cb37 | -14.27615 | -47.30489 | 2025-10-29 03:55:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 14.4 |
| d1d3cfc5-16ca-3276-a2c6-f5a5ffddd5e2 | -8.50721 | -48.27641 | 2025-10-29 03:55:00 | NOAA-21 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 23f09920-c848-3640-bf41-f0688cb895ff | -14.27014 | -47.31152 | 2025-10-29 03:55:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e0e73648-d5ca-34e5-a12d-2f0cb0eaccaf | -12.08001 | -46.38353 | 2025-10-29 03:55:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 135d8698-5e50-36b0-ad45-fc82ccbf8b11 | -13.37247 | -46.63446 | 2025-10-29 03:55:00 | NOAA-21 | DIVINÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5208301 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 588dc709-c608-34d7-bf92-5be306a229df | -12.37115 | -50.15852 | 2025-10-29 03:55:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 18ae2468-4162-3af5-a0d8-57b794c86314 | -11.57753 | -47.93959 | 2025-10-29 03:55:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cd7b901e-59c8-315f-b608-dd34b7c419f1 | -9.33904 | -43.09856 | 2025-10-29 03:55:00 | NOAA-21 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| b2b74293-5b2e-35ce-9ff0-8e9537ffb9bc | -13.23636 | -47.72813 | 2025-10-29 03:55:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 321b0cdd-42d0-38db-b9f0-c5e2ab1a06dc | -10.96108 | -47.61301 | 2025-10-29 03:55:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7e892a61-a762-37de-855e-557eaf745386 | -10.87425 | -48.62554 | 2025-10-29 03:55:00 | NOAA-21 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| b272f7f0-922d-3d57-8024-7eef68365aeb | -10.94339 | -47.62496 | 2025-10-29 03:55:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 279628bc-ceb9-3263-aabd-52a66efcfb69 | -10.92083 | -47.60777 | 2025-10-29 03:55:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d1794185-c437-3ba2-9610-16bdc0804f6a | -11.36677 | -47.02097 | 2025-10-29 03:55:00 | NOAA-21 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 03cfb87c-1db0-377d-9810-f1422f7e2b48 | -14.60513 | -48.40298 | 2025-10-29 03:55:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| c3ec77ac-960c-3596-b34a-9655d6ab2398 | -12.55944 | -44.96131 | 2025-10-29 03:55:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 01a3cb11-b4eb-3d4a-be66-3eed890e5c09 | -12.04983 | -47.81742 | 2025-10-29 03:55:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 6f640811-bb4e-34bf-b532-99bbbb975046 | -9.88299 | -44.88298 | 2025-10-29 03:55:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0251ed57-3200-3ae1-b607-afaa715435bb | -9.16188 | -50.13814 | 2025-10-29 03:55:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3d230a3e-8d46-3789-adb0-31783dab29db | -10.62744 | -47.88354 | 2025-10-29 03:55:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5b407c9c-936e-3f97-98f1-9b7f84b90157 | -11.79103 | -44.39354 | 2025-10-29 03:55:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b02774e4-3c3c-3722-b113-11c472b5cbb9 | -10.95345 | -47.62634 | 2025-10-29 03:55:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6f41ce88-0d59-3640-ab84-527badba2e5c | -14.88969 | -46.76923 | 2025-10-29 03:55:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8bbd1bc1-48b6-3b48-b12c-04ad04d8c28e | -13.81598 | -41.69482 | 2025-10-29 03:55:00 | NOAA-21 | DOM BASÍLIO | BAHIA | Brasil | 2910107 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 22bde211-76a5-3a15-bbff-3a8fd9ada1d6 | -8.56058 | -47.01228 | 2025-10-29 03:55:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f7f09b77-5a10-3b09-acfa-beabafbeb2af | -13.86153 | -48.49786 | 2025-10-29 03:55:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 209eb9cb-7743-335f-893a-cc2a77b4d65f | -14.98892 | -47.87389 | 2025-10-29 03:55:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 072d7f34-233c-3114-9936-7eb59479e7a9 | -11.58762 | -47.94137 | 2025-10-29 03:55:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 285aedfd-474d-3391-b83b-3f76a270143f | -13.56057 | -47.32757 | 2025-10-29 03:55:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 37feeef6-d822-356b-9d53-197a245bb9cf | -12.64419 | -46.7154 | 2025-10-29 03:55:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ce49c361-2d6c-3cb2-a544-3ddc2b1387c8 | -14.12778 | -41.7665 | 2025-10-29 03:55:00 | NOAA-21 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 1c534bc2-a7ba-3854-a3f8-6c3a97bb6e0f | -9.58082 | -46.93663 | 2025-10-29 03:55:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e24ec562-9110-31db-b9e3-33698d3c57fd | -9.9277 | -47.67643 | 2025-10-29 03:55:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2a77ed22-73c4-3d6f-955e-32085b5437e9 | -12.56398 | -44.93536 | 2025-10-29 03:55:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 61df7188-b298-3497-a889-8cc69bdc7b56 | -13.86099 | -48.50068 | 2025-10-29 03:55:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 050e069e-4ae3-38de-8694-e984f7415583 | -10.89964 | -48.37646 | 2025-10-29 03:55:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9feac851-3593-3e5f-baa4-b290256524cc | -14.2739 | -47.31682 | 2025-10-29 03:55:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 81c1fa2d-decc-3e36-a28b-efe6e5aca3d0 | -10.52954 | -47.74055 | 2025-10-29 03:55:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0fc687c0-12f1-3289-a9d5-4b5d8022aa47 | -12.69524 | -46.31309 | 2025-10-29 03:55:00 | NOAA-21 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 75f0bf91-9a11-338c-8b58-2fecf7a6b3d4 | -9.52996 | -46.93917 | 2025-10-29 03:55:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| c6a21dde-56fe-3498-ac90-68e6e656db15 | -13.41509 | -47.38108 | 2025-10-29 03:55:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 662bc7a6-bb2f-3d49-b74f-08a5fd1d1233 | -13.66583 | -47.17745 | 2025-10-29 03:55:00 | NOAA-21 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a38de225-f7de-38b4-a974-c23e465f2761 | -13.56433 | -47.34528 | 2025-10-29 03:55:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7d9725cf-9706-305c-b01a-c2c17c1fd099 | -13.95014 | -48.46695 | 2025-10-29 03:55:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3896d910-62d5-3070-8220-1080d3849cbf | -12.18861 | -46.72226 | 2025-10-29 03:55:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 2ad8c7f3-a40d-30f2-b336-3485a1175f83 | -9.08683 | -47.81039 | 2025-10-29 03:55:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 16c648a1-bc11-32b7-bad8-c01ac41b3e13 | -13.57005 | -47.34044 | 2025-10-29 03:55:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 21368292-15fd-345c-81ac-532983e4e9b1 | -10.51876 | -47.74222 | 2025-10-29 03:55:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b62425e2-7160-3299-8852-5d699ad21379 | -14.99089 | -47.86337 | 2025-10-29 03:55:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 3ff6c806-bc49-3ed9-9e76-e043f8d58cef | -10.56969 | -49.83905 | 2025-10-29 03:55:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |


[Clique aqui para ver as próximas entradas](README23.md)
