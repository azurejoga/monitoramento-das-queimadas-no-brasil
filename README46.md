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
| b80c7b9c-3735-3af0-a3d1-8eb934bb585c | -7.0065 | -59.1223 | 2026-10-08 01:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 34.0 |
| ae0aba92-343c-3f49-9bd6-2336cbbad94d | -6.3351 | -43.3598 | 2026-10-08 01:30:00 | GOES-19 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 57.1 |
| 6cbc769b-caef-3ff2-9209-f468238adedc | -4.4506 | -47.9329 | 2026-10-08 01:30:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 61.0 |
| 2be1ac8b-7123-3ba4-a5e7-655f1512cf9e | -2.4032 | -57.8848 | 2026-10-08 01:30:00 | GOES-19 | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 83.4 |
| 609c6dc8-7571-317c-820a-692163af6713 | -11.3937 | -46.6922 | 2026-10-08 01:30:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 79.5 |
| 5ff4bb30-d4c7-34ba-bd3a-6c27197b127e | -3.478 | -59.5779 | 2026-10-08 01:30:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 61.1 |
| ce92cf21-61b3-350b-8626-29b1d5147f2a | -8.0895 | -55.311 | 2026-10-08 01:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 85.0 |
| 204f5f58-2f6a-339d-acf8-824615ae5b1f | -3.0373 | -53.9469 | 2026-10-08 01:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 59.8 |
| f6966d72-707d-3979-b56d-4b15b64bf067 | -3.2157 | -50.5586 | 2026-10-08 01:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 68.0 |
| d40cf97f-fc4a-382a-ba78-1bb220e0acb1 | -2.3848 | -57.9044 | 2026-10-08 01:30:00 | GOES-19 | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 46.4 |
| 92c11669-5221-3b48-8af0-833781d2db7c | -11.3933 | -46.7148 | 2026-10-08 01:30:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 65.9 |
| b3651a78-6409-3ef5-8782-6e0f6e07e9e8 | -2.7612 | -54.1142 | 2026-10-08 01:30:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 41.7 |
| e2841ff1-f3f4-3d68-acc3-45c5c4ef8002 | -3.478 | -59.597 | 2026-10-08 01:30:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 32.2 |
| 337a65af-da6a-39ca-913d-156bd92e49e6 | -6.2529 | -52.847 | 2026-10-08 01:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 61.6 |
| 00ba8ec9-adf5-3d11-8ad1-8976fa6b2b0c | -3.5515 | -59.4807 | 2026-10-08 01:30:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 55.9 |
| a6e32180-6680-39c8-8365-45da872c148d | -9.4749 | -64.3713 | 2026-10-08 01:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 67.8 |
| c2b49eb7-e529-31cc-9c51-cdbcb71f53b9 | -10.4147 | -47.2846 | 2026-10-08 01:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 46.3 |
| 7dd85082-e3e6-3b61-b4e4-e29472c7cfc3 | -4.3658 | -43.8011 | 2026-10-08 01:30:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 80.4 |
| 0c6aab9e-cff4-3199-9ceb-51e4cf0dae53 | -2.4805 | -56.1072 | 2026-10-08 01:30:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 70.7 |
| c530bb33-ae42-33b0-bc97-0d9e55e30931 | -2.7613 | -54.0941 | 2026-10-08 01:30:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 44.7 |
| ddd5aa92-1376-3bdf-93bd-6b1e345ffe0e | -3.8567 | -55.9769 | 2026-10-08 01:30:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 30.0 |
| 6932e115-1998-35d5-897e-db2eaf9b67a6 | -3.1298 | -53.7834 | 2026-10-08 01:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 66.2 |
| d9a2cbf9-2c93-304c-b9d9-2a6dacc1a5e9 | -2.4031 | -57.9041 | 2026-10-08 01:30:00 | GOES-19 | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 89.4 |
| d22c8967-909e-3b02-aeb0-ac74b0bccdb2 | -5.6934 | -53.4667 | 2026-10-08 01:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 70.4 |
| e8978b0a-eeee-3c20-9283-308f944ab005 | -8.7228 | -45.1812 | 2026-10-08 01:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 201.4 |
| 1a7d0725-2900-3f74-a9f1-f67399ab061a | -2.572 | -56.1646 | 2026-10-08 01:30:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 108.2 |
| 6db71a05-7998-3d33-a52a-230ad1b4f7ed | -3.11 | -54.1862 | 2026-10-08 01:30:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 85.4 |
| d143a59f-f062-3790-b4c3-d2700f0b3156 | -4.4507 | -47.9112 | 2026-10-08 01:30:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 75.0 |
| 974beb52-ecf1-30b0-bbe7-1fd2dd5fb846 | -2.9448 | -54.1501 | 2026-10-08 01:30:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 36.7 |
| d45b3455-310a-3574-8e2d-9658944fca04 | -2.4987 | -56.1659 | 2026-10-08 01:30:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 76.6 |
| 505fa823-4335-3fad-8b96-fcadc599a484 | -4.0628 | -59.8328 | 2026-10-08 01:30:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 58.0 |
| 6c383b08-a7bf-311a-a2dc-c3f58688a0d2 | -5.7498 | -41.7534 | 2026-10-08 01:30:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 71.0 |
| 8b660b6c-f8ee-3ea4-a8ad-096f0d35446a | -2.7797 | -54.0736 | 2026-10-08 01:30:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 73.6 |
| f85adef9-23be-3e62-a073-740871495880 | -8.7225 | -45.204 | 2026-10-08 01:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 40.7 |
| a4322336-70fe-3650-a0bb-55d371ee68c6 | -6.2342 | -52.8685 | 2026-10-08 01:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 100.7 |
| e4aec030-af5a-37ea-9e80-e94cea358dbb | -4.3471 | -43.8021 | 2026-10-08 01:30:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 109.0 |
| d4f522e5-9e03-3049-814a-3c537523e3b0 | -3.1601 | -50.6021 | 2026-10-08 01:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 43.2 |
| 68e4c6d3-47a7-3f25-8c00-00c15d126744 | -5.6931 | -53.5073 | 2026-10-08 01:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 116.3 |
| 2eeca0da-b2d8-3588-8c70-58bfea900a3d | -8.7231 | -45.1583 | 2026-10-08 01:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 175.5 |
| 76a4c3ae-3371-3642-8c63-a43184d05b58 | -6.3165 | -43.3381 | 2026-10-08 01:30:00 | GOES-19 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 56.6 |
| 281b1bfc-6c9c-343f-b9b6-9e9c3977ade5 | -2.9449 | -54.13 | 2026-10-08 01:30:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 33.7 |
| 00c7ff1d-9e56-3c22-bbeb-5cb64e75b3e2 | -3.5698 | -59.4803 | 2026-10-08 01:30:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 42.7 |
| 44dd7845-426c-36ce-baa0-cf54ee2cf32f | -2.4988 | -56.1462 | 2026-10-08 01:30:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 64.8 |
| 28889673-7742-3477-b9a5-dbba6651809e | -3.1972 | -50.5592 | 2026-10-08 01:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 115.3 |
| 6e762fc1-5d6a-34f5-b8f7-7786d741be77 | -3.1101 | -54.1661 | 2026-10-08 01:30:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 107.2 |
| 62a33705-43b2-3146-a93f-778affe40227 | -3.1114 | -53.7839 | 2026-10-08 01:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 104.5 |
| e875ad71-8688-37c3-9ead-d3db3f70fe6e | -10.4151 | -47.2623 | 2026-10-08 01:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 42.5 |
| d56c9b9f-7ef7-3fc7-b025-ee068e9f1c5d | -5.6932 | -53.487 | 2026-10-08 01:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 235.4 |
| 4a3d572c-77d5-3775-a24f-366b57b21faa | -9.4935 | -64.3706 | 2026-10-08 01:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 65.9 |
| e3c40d56-1d55-34d0-beab-7a9f2ec7d0d3 | -3.1879 | -58.6433 | 2026-10-08 01:30:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 38.6 |
| f781473d-7bfe-3a1c-95d7-1c7cbc3f5948 | -9.475 | -64.3525 | 2026-10-08 01:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 95.7 |
| d079c032-ecd4-3459-8bd8-acd349031f0e | -2.9447 | -54.1702 | 2026-10-08 01:30:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 28.5 |
| 1b95b11f-c565-37e1-a191-036d1c1e3a52 | -3.5514 | -59.4999 | 2026-10-08 01:30:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 36.9 |
| 5031dd14-97f2-3ba1-a6b4-04ad5ac0cd09 | -3.2499 | -46.9589 | 2026-10-08 01:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 77.4 |
| 74498a5f-5427-3005-9032-9ba759d66cd7 | -6.1689 | -39.4391 | 2026-10-08 01:30:00 | GOES-19 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 78.0 |
| 9bec12b0-89cf-3035-a5ca-10cf0f2fef85 | -2.5903 | -56.1642 | 2026-10-08 01:30:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 52.6 |
| 1f8b15b2-4fd9-3279-9968-953c8b8482ca | -6.3163 | -43.3614 | 2026-10-08 01:30:00 | GOES-19 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 55.9 |
| 8fba4183-8b98-307b-bfbe-64fd8d66348c | -8.3882 | -46.3006 | 2026-10-08 01:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 83.6 |
| de8fe351-fbc9-3a3d-a21f-1a0e0c3076b7 | -6.2343 | -52.848 | 2026-10-08 01:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 106.9 |
| d6b58f7d-ac04-3a5b-ad48-955ba6cae85a | -5.7117 | -53.4862 | 2026-10-08 01:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 204.9 |
| 238d13cc-aff0-3117-bd22-3385eec84cfa | -9.4936 | -64.3518 | 2026-10-08 01:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 95.1 |
| 9263cc76-9c17-3a6a-be3b-41db76cc0806 | 1.6937 | -55.6263 | 2026-10-08 01:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 74.6 |
| 69cc7c26-7f6a-3dd5-9e7f-140d534c0848 | -8.7417 | -45.1791 | 2026-10-08 01:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 73.9 |
| ab95d78c-6759-3ebd-8003-7ed525f33e0f | -2.517 | -56.1656 | 2026-10-08 01:30:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 62.1 |
| c0edea5c-e7cd-3e8a-9274-f545700af5f6 | -6.2527 | -52.8675 | 2026-10-08 01:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 83.0 |
| 5cf782ac-7b9a-39dd-a4bf-ea70629ad991 | -2.3849 | -57.885 | 2026-10-08 01:30:00 | GOES-19 | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 44.4 |
| ce9981a6-ce03-3a86-ad43-008b5d36740f | -3.1285 | -54.1657 | 2026-10-08 01:30:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 74.9 |
| 8846574c-9f8b-3ef4-85ae-2ec22f15cf90 | -6.8764 | -43.685 | 2026-10-08 01:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 75.7 |
| dffddb92-dbfb-3d56-bfc4-86fa0a630abd | -5.7116 | -53.5065 | 2026-10-08 01:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 139.0 |
| 2c43be32-73a6-3178-b668-8cb8f8e4346b | -3.8566 | -55.9967 | 2026-10-08 01:30:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 27.8 |
| e3e7337f-9cfe-333a-ae3a-93783cc3ff7b | -3.8383 | -55.9774 | 2026-10-08 01:30:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 30.9 |
| bdb260c8-37d6-39b6-889a-f68c11e9bab9 | -2.4988 | -56.1266 | 2026-10-08 01:30:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 60.9 |
| fafc2f18-147f-32ce-8e8c-c8af083ea014 | -4.2954 | -49.0807 | 2026-10-08 01:30:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 84.6 |
| e4b217fb-69a6-3ff7-a994-6d18fb7d0402 | -6.8952 | -43.6833 | 2026-10-08 01:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 67.3 |
| 773871de-6c75-3db6-bae5-8bdaf5accdc6 | -2.4805 | -56.1269 | 2026-10-08 01:30:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 64.3 |
| 18716801-5a27-3fee-a8e3-26f620d89ca2 | -2.572 | -56.1842 | 2026-10-08 01:30:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 92.9 |
| 498544e2-aa91-337a-9b9f-51fc8267ec82 | -3.1697 | -58.6244 | 2026-10-08 01:30:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 35.2 |
| a52a4c82-6898-34b4-b23c-4bbb90d54401 | -10.4337 | -47.2824 | 2026-10-08 01:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 94.1 |
| dd31581e-a846-373a-8672-3995bf37606b | -10.434 | -47.2601 | 2026-10-08 01:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 76.2 |
| 31c9c153-e108-32f8-a7f4-31e1eebeb2b0 | -3.1697 | -58.6437 | 2026-10-08 01:30:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 38.1 |
| 1f676c44-bc0a-3e34-9ccb-36c34e9b086b | -2.7981 | -54.0732 | 2026-10-08 01:30:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 44.2 |
| b4380c23-1de9-389b-9c5b-5b98b6e2b190 | -2.499 | -56.0675 | 2026-10-08 01:30:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 58.8 |
| db3d2b6c-3ba4-3f51-ab42-6221173466a1 | -3.0374 | -53.9268 | 2026-10-08 01:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 67.3 |
| 32871751-c059-3487-93be-008591084766 | -8.742 | -45.1563 | 2026-10-08 01:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 107.4 |
| 24ae906c-b181-3107-bafb-581f80fe882b | -9.0592 | -65.9209 | 2026-10-08 01:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 64.1 |
| c339a739-baae-3439-8fe4-f0cffc0b4694 | -8.53748 | -66.9929 | 2026-10-08 01:34:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 15.2 |
| 92fdb261-d93f-32ec-bef3-1d5ac35f7841 | -9.48266 | -64.3533 | 2026-10-08 01:34:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 93.0 |
| 0e7c6838-e6ff-3f2a-9c38-bb32801e9099 | -9.34423 | -65.46391 | 2026-10-08 01:34:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 16.2 |
| b6f3e7cb-b514-367e-91b6-c30f24bb2acb | -8.52802 | -67.01365 | 2026-10-08 01:34:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 22.7 |
| 4fde3ce1-e43f-3de7-a911-b8142fb24a2b | -9.46994 | -64.36227 | 2026-10-08 01:34:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 60.0 |
| 7d0e157e-9c54-3de3-8582-705496b179f3 | -9.65782 | -63.76823 | 2026-10-08 01:34:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 35.5 |
| 8b3288eb-be84-324e-99fa-c852a4083a14 | -8.61803 | -67.01823 | 2026-10-08 01:34:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 23.2 |
| 9ac64fe8-f44b-3b77-b4fa-0b8058f76187 | -8.52642 | -67.01967 | 2026-10-08 01:34:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 14.4 |
| 3bbb234b-4f6d-3e5d-a202-86c442647913 | -9.46756 | -64.35589 | 2026-10-08 01:34:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 37.5 |
| d6cd3bc7-8223-3be0-adda-cf28d79e6e12 | -9.4876 | -64.38244 | 2026-10-08 01:34:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 35.3 |
| 94ec4d65-0570-332d-8f4b-01fd80310345 | -9.64842 | -63.77527 | 2026-10-08 01:34:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 24.7 |
| 7bba3f62-ea4f-3213-856f-0f5a05e9395d | -8.52356 | -67.00089 | 2026-10-08 01:34:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 22.1 |
| d1549171-a970-39f4-b2f2-fde89b7e2f37 | -9.48503 | -64.35963 | 2026-10-08 01:34:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 102.9 |
| 71c8fb7f-f70b-30f2-b9fe-093077c05deb | -9.05361 | -65.94176 | 2026-10-08 01:34:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 27.6 |
| 806c8338-59f9-3826-890d-768ee42507e5 | -7.43989 | -63.55385 | 2026-10-08 01:34:00 | TERRA_M-M | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 29.1 |


[Clique aqui para ver as próximas entradas](README47.md)
