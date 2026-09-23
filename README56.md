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

## Dados Diários - Página 56

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 186ccd08-f827-3cc1-b647-4bfc99e9accf | -11.79789 | -42.63125 | 2026-09-23 04:27:00 | NOAA-21 | IPUPIARA | BAHIA | Brasil | 2914109 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 4b60c3bb-e0a1-3a1f-b110-af937844dd71 | -5.30059 | -56.09798 | 2026-09-23 04:27:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 434ebaa5-9fb3-372a-a3a9-33273e6b73bc | -7.93516 | -45.65499 | 2026-09-23 04:27:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 12a02a16-e8d9-386d-8415-6c6d2fb7f30a | -6.62553 | -59.93224 | 2026-09-23 04:27:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 1b4a01c5-6f98-3b7e-ac94-d0d0daf9a422 | -6.17676 | -52.05202 | 2026-09-23 04:27:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 23c18bb4-fabe-3ccd-98e8-9a4c956e9b3a | -11.93351 | -38.29161 | 2026-09-23 04:27:00 | NOAA-21 | INHAMBUPE | BAHIA | Brasil | 2913705 | 29 | 33 | nan | nan | nan | Mata Atlântica | 11.9 |
| 51b1acc6-738f-31a0-b7c4-4c5efcdb33aa | -7.41308 | -44.72867 | 2026-09-23 04:27:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 930aaddf-f836-3eb1-ac29-d56c17c47a7e | -9.12747 | -45.92667 | 2026-09-23 04:27:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e4aea6e6-d4ad-3c7f-833e-02950ff3e8a9 | -7.08867 | -52.7483 | 2026-09-23 04:27:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6e280ce6-05d2-369c-802e-c68061634d66 | -8.33059 | -47.55259 | 2026-09-23 04:27:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 61905d7f-cc7f-3163-83c9-5793c781da6a | -6.67479 | -55.06281 | 2026-09-23 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0ed9c381-6c63-3547-af7d-2acaebab036e | -12.41848 | -46.96197 | 2026-09-23 04:27:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| f8dca298-2c48-3f9c-854b-caeef0bedb56 | -14.62702 | -45.64551 | 2026-09-23 04:27:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 22.4 |
| b172e426-93c7-3cd6-9b7c-fae7a7072cd6 | -12.12778 | -47.39398 | 2026-09-23 04:27:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| cab18111-7b8e-36eb-9688-db4f92a59fa4 | -13.30148 | -47.89343 | 2026-09-23 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 682610cb-1353-364a-884a-d3ea73a2f96a | -8.20345 | -54.71893 | 2026-09-23 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 6d7c7d76-7773-3466-9b33-f42907e4fa2d | -6.67982 | -55.05304 | 2026-09-23 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 5b325d3d-e3c0-36d9-85db-1e54ffb2cc79 | -11.68451 | -43.45151 | 2026-09-23 04:27:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| de1f90e2-ca54-30b9-b3d5-2b2fee797dc8 | -7.55794 | -48.68134 | 2026-09-23 04:27:00 | NOAA-21 | PAU D'ARCO | TOCANTINS | Brasil | 1716307 | 17 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 29eadbf9-623b-3bdc-9aa1-ad4bbe97ee14 | -8.58659 | -53.1152 | 2026-09-23 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3f59eb1f-3ed5-3f78-beae-beba64a97310 | -11.75642 | -47.61817 | 2026-09-23 04:27:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 46d4a499-4545-3f5f-8673-b87382f2d6eb | -14.70328 | -45.59039 | 2026-09-23 04:27:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 4f8c945f-381e-3cfe-9257-440b476c9027 | -13.30533 | -47.89044 | 2026-09-23 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2660d0ea-24df-3c4f-ba21-5b33ba7b5d68 | -8.7669 | -45.83826 | 2026-09-23 04:27:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0b76032d-816f-370b-8f94-1b45be80b6d8 | -13.30588 | -47.88692 | 2026-09-23 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ec68601d-a2e2-328a-b1be-a4273185ea17 | -12.46627 | -47.02794 | 2026-09-23 04:27:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b621b4cf-2cfb-3709-a11c-b5a966e97683 | -10.44921 | -45.09572 | 2026-09-23 04:27:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ce98ba3f-2cf2-3491-94d0-f85f20365cf6 | -11.40957 | -44.03617 | 2026-09-23 04:27:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f5995111-f310-3f0d-8441-6a97bcf24aea | -10.51873 | -44.87822 | 2026-09-23 04:27:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ee5372d8-6413-347c-acda-b50dfe6ea49b | -9.56385 | -46.53758 | 2026-09-23 04:27:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7fe762f1-f9af-330c-b9e6-3c1fa467782d | -11.30667 | -51.3658 | 2026-09-23 04:27:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c2cc958c-0992-367a-ba1d-bb1964910eb8 | -13.93712 | -47.83007 | 2026-09-23 04:27:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 83dd5f6f-9669-3676-873a-2e2a86bb0ff9 | -12.48936 | -46.98748 | 2026-09-23 04:27:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7de1ac3c-13d1-31be-86af-b07c8d9e6b7f | -9.94087 | -48.47271 | 2026-09-23 04:27:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| facbc70d-3a13-3e06-adce-67bb7d96f0f5 | -14.59693 | -45.62522 | 2026-09-23 04:27:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6566f817-0476-32c2-91f5-86336deb633c | -10.2981 | -50.52505 | 2026-09-23 04:27:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6404d070-a971-360d-a871-405d35f07958 | -6.65948 | -50.8851 | 2026-09-23 04:27:00 | NOAA-21 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b4a3cb06-a0cb-3310-ae57-013d25a706b3 | -8.34623 | -50.86131 | 2026-09-23 04:27:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9dacf595-0a66-3f72-8329-910668a99bf8 | -6.37743 | -55.28843 | 2026-09-23 04:27:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 26b11102-db10-38b6-b3da-e34fe52b62cf | -11.28818 | -51.33949 | 2026-09-23 04:27:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 99a07f1a-e827-3075-97d1-adc2e85f4781 | -10.71771 | -48.71997 | 2026-09-23 04:27:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 20bd7c2a-a66d-36fe-b74b-a08b6d69ccb4 | -6.63891 | -59.93556 | 2026-09-23 04:27:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 8.1 |
| a875bfc6-09b1-32e0-a416-d1f2c6c13b7a | -11.4634 | -47.7502 | 2026-09-23 04:27:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ec645698-fbe6-3c10-8ce3-1b2904c736d0 | -14.61859 | -45.64926 | 2026-09-23 04:27:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 9.3 |
| f1d69761-6ae4-3ab7-a559-3c5e632928e2 | -10.2451 | -45.49828 | 2026-09-23 04:27:00 | NOAA-21 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0e3c9841-3bd8-3cd4-b85e-ca40fb8378e5 | -8.73533 | -47.5967 | 2026-09-23 04:27:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 60b76f0e-c2d1-3afb-8159-7a3d9ea884ad | -12.82002 | -50.87091 | 2026-09-23 04:27:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fe53bb81-eb2e-3a0d-8a7e-894dcfafff3e | -10.71888 | -48.71272 | 2026-09-23 04:27:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1ffcc678-fb8e-3dba-a36f-c2f6a9183780 | -12.05385 | -50.34651 | 2026-09-23 04:27:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d019878b-ffe7-35b7-b7ec-bf2a3c9c5048 | -12.4108 | -46.98996 | 2026-09-23 04:27:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5e44850a-844d-33ed-82df-c226c58c849d | -7.65193 | -45.44009 | 2026-09-23 04:27:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fd67a2c9-299f-3aac-97e1-83c7487db778 | -14.69329 | -45.58463 | 2026-09-23 04:27:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 8c580002-9a13-3ce1-a7e2-3aee1bb9cfbe | -7.52981 | -45.21172 | 2026-09-23 04:27:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 061849b2-1f15-37a8-84c0-af7fc294f5d5 | -9.27791 | -45.91739 | 2026-09-23 04:27:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 560c9ead-2b85-3127-ac85-32b30daf4ce2 | -12.50904 | -49.98108 | 2026-09-23 04:27:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0dcc3941-e121-3d54-bd2c-4b8fe4dd2a8f | -7.41651 | -44.72919 | 2026-09-23 04:27:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 21bca10f-a376-332f-bdd2-794f50a59621 | -6.17979 | -52.79522 | 2026-09-23 04:27:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fa31b131-d79c-30ae-981c-75a6c6d7120a | -12.60021 | -47.87742 | 2026-09-23 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 30358ca3-03c2-3c3f-9cdc-21967768c792 | -6.66651 | -55.06882 | 2026-09-23 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 33aa80b0-44c5-3dbb-acbb-de9c29675a5b | -9.57047 | -46.53861 | 2026-09-23 04:27:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 54777894-4659-383a-9265-73965ea2b458 | -11.65585 | -47.80319 | 2026-09-23 04:27:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 99ed8cad-40dd-38ec-9735-717ddc5fe652 | -8.81279 | -44.27517 | 2026-09-23 04:27:00 | NOAA-21 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 5882e715-aae8-34a3-87c4-e172f3906967 | -13.53939 | -47.67544 | 2026-09-23 04:27:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a0f2796a-66ea-300a-8040-3e260e6dc9fa | -9.36788 | -50.26736 | 2026-09-23 04:27:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 188deaa8-6f14-32fb-bcdb-289d13520033 | -8.25327 | -54.77763 | 2026-09-23 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| c647f91c-8f00-31b7-9f32-55abf1a42dfe | -6.30553 | -57.74828 | 2026-09-23 04:27:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 7438bb2a-dde0-3822-b960-81dbe5f16080 | -8.80453 | -44.28218 | 2026-09-23 04:27:00 | NOAA-21 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c0736956-2e27-380f-a408-e456db3f2af8 | -13.29818 | -47.8929 | 2026-09-23 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d6d679f5-7ea4-377c-ba83-5ed6ce6b2c4a | -6.66919 | -55.06487 | 2026-09-23 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| bdedd4be-97b3-3e2d-8e50-1301a0608c39 | -5.89716 | -52.08959 | 2026-09-23 04:27:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3db0ded9-abff-3c0a-b328-460c36205603 | -7.42173 | -49.83397 | 2026-09-23 04:27:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| d444c2e2-a010-3966-9e26-08c652f180e7 | -12.81113 | -50.9246 | 2026-09-23 04:27:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 4440c385-b4f4-3e0f-948d-a96149796426 | -6.6138 | -59.95694 | 2026-09-23 04:27:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 517e374c-9a70-3593-87a1-739143b79e10 | -6.17907 | -52.79953 | 2026-09-23 04:27:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ae0a2a34-60d9-3bde-9d22-e98cfed215a6 | -11.8031 | -50.03926 | 2026-09-23 04:27:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 13cf3b48-b696-386f-abd1-f61d2942150d | -11.7362 | -40.41248 | 2026-09-23 04:27:00 | NOAA-21 | MUNDO NOVO | BAHIA | Brasil | 2922102 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 27d0ced5-6f0e-3693-a723-d7a820e1c24a | -13.92501 | -47.84262 | 2026-09-23 04:27:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9e7b138b-2c8f-39b6-8dd1-fe57946a1b24 | -10.82505 | -48.47682 | 2026-09-23 04:27:00 | NOAA-21 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 44e75b39-6f5e-3280-beb5-d4c632b9ec20 | -13.86712 | -48.56235 | 2026-09-23 04:27:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 62e6eac6-ee39-3c10-a498-e4c5366f410b | -10.69759 | -48.71679 | 2026-09-23 04:27:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 14e6062e-9607-3956-870c-bde90cc11f36 | -14.61453 | -45.62785 | 2026-09-23 04:27:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| bb2e581f-29e4-32a9-9285-d0220230419e | -10.16526 | -47.67643 | 2026-09-23 04:27:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2434da43-cd8f-3587-a1bd-67a430117706 | -10.44575 | -45.09521 | 2026-09-23 04:27:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d34c2e0b-e89b-3d6d-9636-bef707266ddb | -9.84265 | -46.383 | 2026-09-23 04:27:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 4e6571f0-75d9-315a-8758-6f2b280f9b3d | -12.47216 | -49.9906 | 2026-09-23 04:27:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 33eaf216-2687-3fb0-820c-1beffa218a54 | -8.3365 | -50.82671 | 2026-09-23 04:27:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 0bcd588d-af5f-3230-b13a-3338da6ad345 | -6.13441 | -51.70225 | 2026-09-23 04:27:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ca7745c4-3247-3f11-849a-b33aa0541f0d | -12.42018 | -46.9732 | 2026-09-23 04:27:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a4e18296-8996-30c3-bdd7-79bc8e4974d4 | -11.30227 | -51.34649 | 2026-09-23 04:27:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| fad76c23-d16a-341c-8eee-be88f1e9cdbf | -6.10296 | -57.67977 | 2026-09-23 04:27:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| e48dd87b-288b-3f15-9731-165c17b6cafc | -12.30375 | -46.39854 | 2026-09-23 04:27:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 96a2470a-9ff8-3b92-971b-113acde65be2 | -5.93189 | -59.91706 | 2026-09-23 04:27:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d601897b-7884-3dc4-9318-4f8642178752 | -11.08961 | -48.33057 | 2026-09-23 04:27:00 | NOAA-21 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| de9e2439-dc7f-3afd-b106-cfccc3521a4c | -14.61274 | -45.64008 | 2026-09-23 04:27:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 20.4 |
| 3a0e55a6-463f-34ed-bbfe-74e9ed9c5899 | -14.70269 | -45.59447 | 2026-09-23 04:27:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 57480417-6795-35ce-9a6d-7ac383829e4a | -11.35574 | -43.37537 | 2026-09-23 04:27:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e94c6505-8d28-3028-9e55-cf788d0ba864 | -8.79908 | -48.76091 | 2026-09-23 04:27:00 | NOAA-21 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 2bc15ede-9c2e-372b-8704-61b45dbf93f6 | -5.747 | -53.47254 | 2026-09-23 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b8cfb5a1-3a15-314a-961f-afd8e7faaadb | -12.10273 | -50.03262 | 2026-09-23 04:27:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 593d7031-5f4e-33be-a396-8cf3e777c632 | -8.68081 | -49.40911 | 2026-09-23 04:27:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |


[Clique aqui para ver as próximas entradas](README57.md)
