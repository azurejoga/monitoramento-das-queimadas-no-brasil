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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 64bc2f38-9d55-33ae-85eb-967ee7c9f0cc | -11.69243 | -50.35801 | 2026-07-23 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4cd35844-ab39-35a7-8caa-95e02801fbce | -11.93479 | -50.37211 | 2026-07-23 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0035386d-d236-3acd-8f85-0f9588883e73 | -11.5804 | -48.39808 | 2026-07-23 04:46:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4fc123ae-d054-34e5-8bea-28798c03ad85 | -11.88974 | -43.82766 | 2026-07-23 04:46:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| face24dd-54a2-3046-8e33-8a30fdd70a59 | -12.40685 | -50.39352 | 2026-07-23 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7ae2d426-b935-37a5-90de-1e2b53b6e580 | -11.66979 | -50.35075 | 2026-07-23 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 47d5d724-40b1-34fa-b1ad-0891001d86ce | -11.78026 | -50.38325 | 2026-07-23 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 540c8857-fa8b-3353-83b5-0598758a4206 | -11.88939 | -43.82848 | 2026-07-23 04:46:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| d98f715b-c65a-3f86-91af-3d0fa7961ab2 | -11.68857 | -50.36099 | 2026-07-23 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 61f31805-1ee8-3442-b4a2-905f4ea4b980 | -11.81396 | -47.3353 | 2026-07-23 04:46:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6e40ad6a-245e-3a8f-a325-5ea02af70d66 | -11.96572 | -50.36986 | 2026-07-23 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 5cb7449f-6781-35cc-8d9d-5f3e391c23a1 | -11.69464 | -50.36558 | 2026-07-23 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| db8a2adf-0587-36f3-93d2-001cb9f3de98 | -12.88101 | -58.28961 | 2026-07-23 04:46:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 81dfc043-21a5-3386-b02c-d220eb1c3dbc | -11.94528 | -50.37018 | 2026-07-23 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 55f3942e-531d-323c-8c8a-fa59f0c16a7c | -11.95964 | -50.36526 | 2026-07-23 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 19.5 |
| eafba4e5-443f-3f3f-87e3-978826f00e20 | -9.12413 | -61.05624 | 2026-07-23 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 01bb7df0-6d4a-3dd9-8c37-cfafbe49c348 | -12.31614 | -50.05819 | 2026-07-23 04:46:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b54443d2-c857-326a-888a-951f5ce23332 | -11.79892 | -47.10239 | 2026-07-23 04:46:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9028793d-69ff-390d-9276-835e8922d521 | -13.33543 | -54.31118 | 2026-07-23 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 35e836d5-2f43-32dc-beed-b9bcb3b337ee | -11.69409 | -50.34745 | 2026-07-23 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| a3c6f205-6a3e-3f53-9573-efe70aa4f7ab | -17.57046 | -47.50172 | 2026-07-23 04:46:00 | NOAA-20 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f72c24bc-7e35-3aef-9464-ee3c46c78d2d | -13.99102 | -49.59056 | 2026-07-23 04:46:00 | NOAA-20 | MARA ROSA | GOIÁS | Brasil | 5212808 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a4ef5ed0-c561-339a-bb80-1df837151e2d | -11.95578 | -50.36826 | 2026-07-23 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d8f2a13d-f880-3e87-89b2-b7dfa8e85b0c | -17.57368 | -47.50741 | 2026-07-23 04:46:00 | NOAA-20 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 570cf31e-bb41-3ca1-b16c-48976d472416 | -13.32468 | -54.30927 | 2026-07-23 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d35f9791-7c37-3a68-b5fe-641910e9572e | -13.33613 | -54.30703 | 2026-07-23 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 314c3a98-17b7-3ee7-b8a0-0c79240fb513 | -13.37249 | -54.29888 | 2026-07-23 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 73511b25-c1e5-3d40-a989-da23e63e5018 | -11.70075 | -50.37043 | 2026-07-23 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 395389d9-9237-3d72-ada7-bffd8f80c77c | -11.95246 | -50.36773 | 2026-07-23 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 7e49ccd9-076f-3065-99cf-e5136c73ee01 | -11.68801 | -50.34286 | 2026-07-23 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9363317a-a662-376f-ae25-3b8981f94ebe | -11.93424 | -50.37563 | 2026-07-23 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f4a3db30-43b6-3142-90d2-c0bbb65316af | -8.82613 | -63.90394 | 2026-07-23 04:46:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c24bf1c3-499c-3c11-90cb-836e0bc4c8b9 | -12.398 | -50.38483 | 2026-07-23 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f91224ad-95c4-33d7-b6cb-2464dedac249 | -11.9497 | -50.36366 | 2026-07-23 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 632ab660-4327-3d2a-895f-71e783a81b53 | -11.95025 | -50.36013 | 2026-07-23 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 5d4109ae-e1df-3033-bec9-b9724a7e7300 | -11.94583 | -50.36665 | 2026-07-23 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| ca0ef2b7-9385-3dc2-9a47-a7e86f118187 | -11.91988 | -50.38055 | 2026-07-23 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2b9af050-5e14-3217-b023-7ef72c3fd77d | -17.26019 | -48.28384 | 2026-07-23 04:46:00 | NOAA-20 | PIRES DO RIO | GOIÁS | Brasil | 5217401 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7c4729fb-6223-3f78-9a4a-530e3d230031 | -11.5441 | -48.27267 | 2026-07-23 04:46:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4ab49b97-47c4-3c13-9b8f-1c22e33a51fb | -11.65598 | -50.33049 | 2026-07-23 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d23b43da-415d-3fe5-a846-f31029e27693 | -12.13871 | -48.26082 | 2026-07-23 04:46:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a9d69a95-d41f-372e-b8b3-78071aa90862 | -11.95467 | -50.37532 | 2026-07-23 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 94a5f6a8-4cb0-369a-96f7-a5a553807e76 | -12.41349 | -50.39458 | 2026-07-23 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| df754422-ab02-3503-a56f-fd96ae1d91a6 | -11.69519 | -50.36206 | 2026-07-23 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 2c3caf8f-08cb-3f3a-a38b-6b23a04a92d0 | -11.70407 | -50.37096 | 2026-07-23 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 79cdfb1c-60c2-3de6-b3d3-7243bad87d3a | -11.94142 | -50.37318 | 2026-07-23 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 154662d7-bbe2-3c8d-a5f6-916c02a8f548 | -11.33135 | -62.22287 | 2026-07-23 04:46:00 | NOAA-20 | ALVORADA D'OESTE | RONDÔNIA | Brasil | 1100346 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| be6b734c-c66f-331e-9e1a-c734e70cdabf | -11.68581 | -50.35694 | 2026-07-23 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 6ca385b2-d072-3713-a90f-148567f0d220 | -11.78342 | -47.10467 | 2026-07-23 04:46:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 20.3 |
| e59e3a10-c158-3785-a613-fdb11ff265e9 | -11.68028 | -50.34883 | 2026-07-23 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6d9d9037-ddbd-3195-bbb8-b78251d6bd47 | -12.0347 | -50.36219 | 2026-07-23 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 33779a6f-5fff-35b8-bf2b-dc624069b4ee | -9.11753 | -61.09091 | 2026-07-23 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f0c6830e-b9fe-343a-983e-2546c2054f04 | -11.56939 | -48.40037 | 2026-07-23 04:46:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f89d5e00-aa1a-320d-a96d-4efa90d5f3ca | -11.8146 | -47.33092 | 2026-07-23 04:46:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 9ef6f848-83ee-3533-ac77-0bbe0fa5a587 | -12.66528 | -48.21673 | 2026-07-23 04:46:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a68f4a0d-d1b2-3bf3-bbfc-138a01c4310b | -11.95191 | -50.37125 | 2026-07-23 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 126be98b-ae08-3903-8cb6-c0e1148a01d9 | -11.94749 | -50.37777 | 2026-07-23 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5bc9033a-0cf4-3340-8754-b53f921780e1 | -11.9508 | -50.35661 | 2026-07-23 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6ea2a3e8-3db6-38fd-a732-e5da1cf16385 | -11.94693 | -50.3596 | 2026-07-23 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| a1aeb582-09f6-32ae-acc8-57bfbcd4b141 | -12.52368 | -48.24611 | 2026-07-23 04:46:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e069a3c4-4c88-3ea1-842e-4eebc178affc | -11.57635 | -48.40144 | 2026-07-23 04:46:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fc30dae3-a227-39a1-b117-13008227ec2b | -11.66648 | -50.35022 | 2026-07-23 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 22.2 |
| dc0ec028-f13e-3a6d-94ae-eb8428fc7d97 | -11.96185 | -50.35115 | 2026-07-23 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 9595458f-9f17-38f3-b1ee-920fd90b4b1f | -13.43561 | -43.84829 | 2026-07-23 04:46:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 03963b29-3817-3896-9633-191f4bb6ce9f | -17.73524 | -52.7427 | 2026-07-23 04:46:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 90e1e818-ea04-38bb-803d-5f410b50aadf | -11.97235 | -50.37093 | 2026-07-23 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5e9b2afc-903b-3551-ae3b-f0063738c81f | -12.52955 | -48.25526 | 2026-07-23 04:46:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a493b06f-4f20-3068-a19a-58aed4cde158 | -11.79585 | -47.09735 | 2026-07-23 04:46:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| b434d76d-db05-3b74-9602-0ad19ef160ef | -11.6974 | -50.36963 | 2026-07-23 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 11.9 |
| e2d6ae0e-a9f4-382c-bc57-0dc9e9d45626 | -11.96019 | -50.36174 | 2026-07-23 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 19.5 |
| 9ee776df-3e39-3719-8fac-0391454f0948 | -11.95301 | -50.3642 | 2026-07-23 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4ac8f71d-21e0-38fa-8865-c179db6c4f4e | -11.67973 | -50.35235 | 2026-07-23 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 12.5 |
| cd5b0794-6f20-3796-80f6-8e104393d6bf | -11.67255 | -50.3548 | 2026-07-23 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 110f5fa3-eefe-3b46-b790-88e5eb55feaf | -12.3272 | -50.00869 | 2026-07-23 04:46:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f37bde05-e028-34da-8281-fefcf33ea7df | -11.63406 | -48.53749 | 2026-07-23 04:46:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 55d11a6e-169a-3df4-bfc4-70516b8c75e8 | -11.94362 | -50.35907 | 2026-07-23 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| a9d329c9-93d0-3055-a057-4186fe982562 | -11.77971 | -47.10413 | 2026-07-23 04:46:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 7ef0f766-9ccb-391f-8fd1-1331b2022d35 | -13.3211 | -54.30862 | 2026-07-23 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| efd0fc11-c7f6-3c03-95e3-ef666119e5ad | -11.96074 | -50.35821 | 2026-07-23 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 801230f3-e345-3de6-af38-2d31a8fffb33 | -10.95617 | -49.81051 | 2026-07-23 04:46:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 90ed3d5f-9032-3caf-9433-a0ae43d3bb59 | -11.70738 | -50.3715 | 2026-07-23 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| aef9276c-0574-3d0f-bc3e-52e2666a4951 | -13.32538 | -54.3051 | 2026-07-23 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f398ca74-5ebb-3834-bb6f-e982c484b47b | -11.68967 | -50.35395 | 2026-07-23 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c41e3aab-65a0-374a-9331-7bd31a9f0df5 | -11.69188 | -50.36152 | 2026-07-23 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 23ca5192-eb45-38da-942c-252a9d43b722 | -9.12247 | -61.06492 | 2026-07-23 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f979f930-eba6-34b4-93d7-9174bef6e302 | -11.33077 | -62.22423 | 2026-07-23 04:46:00 | NOAA-20 | ALVORADA D'OESTE | RONDÔNIA | Brasil | 1100346 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 38dedba6-3cc6-3736-b1f2-207effa8125a | -11.96241 | -50.36933 | 2026-07-23 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5445395d-1dfe-3c7b-8559-4ebc02ec7ab9 | -9.12165 | -61.06924 | 2026-07-23 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cf572799-a7b0-3925-84e6-19e0663d0aed | -11.95522 | -50.35009 | 2026-07-23 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e75a9b4f-c36c-362d-801f-08e07ad2c615 | -8.82479 | -63.9105 | 2026-07-23 04:46:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9dab16d7-34d6-3862-baee-52fd150442e5 | -11.66703 | -50.3467 | 2026-07-23 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8bbf0df5-0287-337b-ae43-20f8e2faa93a | -12.84836 | -44.3791 | 2026-07-23 04:46:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 42200db1-a2bc-3d0e-a250-821f9d22211a | -13.31109 | -54.32417 | 2026-07-23 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1f919df8-ae56-3e96-9685-8790660c7d43 | -11.69409 | -50.3691 | 2026-07-23 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 24fa6867-3e24-3eb3-8918-6936e55a162b | -13.37535 | -54.30368 | 2026-07-23 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 120dbd9f-0cd5-3376-b8a3-6b6647967a61 | -11.96627 | -50.36633 | 2026-07-23 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 149ae6cb-94d3-3e19-975e-ce246203b3bc | -12.10601 | -44.93521 | 2026-07-23 04:46:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a56c4c22-78fe-32b2-8be5-809df2552e59 | -11.69133 | -50.36504 | 2026-07-23 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| b62a1ab7-33d8-31a1-8d44-756e27d53693 | -11.69078 | -50.34692 | 2026-07-23 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 8053a542-e900-3a89-9cfb-bc9b9f0617c7 | -17.58081 | -47.51362 | 2026-07-23 04:46:00 | NOAA-20 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |


[Clique aqui para ver as próximas entradas](README16.md)
