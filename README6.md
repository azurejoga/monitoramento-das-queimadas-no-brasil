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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7831c792-47ae-3ad6-8fc4-6cead0619786 | -4.08028 | -46.79835 | 2024-12-22 04:25:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cdfb99d1-5d1c-37f7-be1e-f8a3d86ea51f | -2.58246 | -49.47171 | 2024-12-22 04:25:00 | NOAA-21 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 84c59793-eeb2-31fe-8a81-b1233e967b0c | -4.06238 | -46.71715 | 2024-12-22 04:25:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6e631d0e-febd-398e-869c-c27f480baf2b | -2.84194 | -48.10942 | 2024-12-22 04:25:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fa624ed6-c738-37d4-8854-5cff253f8414 | -3.88768 | -46.52935 | 2024-12-22 04:25:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 18d32dc5-1ba0-3938-80f2-6c3cc3348fac | -2.48967 | -49.04989 | 2024-12-22 04:25:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fe9238bf-6e68-3c3a-abcd-0a95411928a0 | -3.40642 | -44.11793 | 2024-12-22 04:25:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9914a6f5-c7b5-3b29-a0e8-7c3f442f554e | -2.57504 | -49.4631 | 2024-12-22 04:25:00 | NOAA-21 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 05a61577-d6ef-3db6-9dea-0e44e4a34b61 | -2.74782 | -44.76561 | 2024-12-22 04:25:00 | NOAA-21 | BACURITUBA | MARANHÃO | Brasil | 2101350 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a89d78f2-590b-30c0-86cc-4a6a8396bcad | -4.60335 | -45.4525 | 2024-12-22 04:25:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7f73e047-f6f8-3ab7-b20f-695dc6d27738 | -2.38102 | -47.42976 | 2024-12-22 04:25:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0184920e-d41f-354f-9669-1be92cb762d6 | -2.97365 | -48.07794 | 2024-12-22 04:25:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1b07e25c-59ff-388b-8086-ed0fc7a3f4ab | -4.0022 | -46.55788 | 2024-12-22 04:25:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 44e3dc12-6383-35bd-a444-1a8c559ff42a | -3.98155 | -46.68975 | 2024-12-22 04:25:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 116011ad-8b9d-3478-8163-79394ddef97c | -2.68471 | -54.84703 | 2024-12-22 04:25:00 | NOAA-21 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3d9a8682-6905-3259-8a7c-61c72bbc51a3 | -4.09029 | -46.82145 | 2024-12-22 04:25:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9de16039-4465-3c79-99f0-77cc0c03b2f1 | -1.72015 | -52.57528 | 2024-12-22 04:25:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 068ffe11-7da8-35d1-9105-a1a1dc7eb1fe | -4.54004 | -45.88074 | 2024-12-22 04:25:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 1a02c489-127b-3bc4-9580-62d3045bfc49 | -2.76924 | -47.39209 | 2024-12-22 04:25:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 614e0f68-b7ee-3b0d-a803-b8a5aa82ca06 | -4.05905 | -44.05077 | 2024-12-22 04:25:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 95d62a4f-0e04-3b49-8bcc-4582d07f1cc2 | -3.91679 | -46.66906 | 2024-12-22 04:25:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d32d7ad4-178a-3bcf-af29-ba26bfec5926 | -2.69251 | -54.84629 | 2024-12-22 04:25:00 | NOAA-21 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 250cdb95-bcb5-393b-a551-afb79fff1e2d | -4.11287 | -43.35193 | 2024-12-22 04:25:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 406ec1b7-f8cb-3cbb-a104-6b30bee517d7 | -1.17944 | -52.54676 | 2024-12-22 04:25:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 11123096-b53e-33ff-a9ab-7ccdba64f069 | -3.84925 | -43.93282 | 2024-12-22 04:25:00 | NOAA-21 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| af2b0159-5ec8-3ce4-a460-c75e761d26fb | -2.63311 | -48.05395 | 2024-12-22 04:25:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 75275b72-11e3-3afa-abc3-66478df17273 | -4.11266 | -46.72149 | 2024-12-22 04:25:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0a7fc99e-8026-3a80-bae4-a74ac57063db | -3.92153 | -46.89862 | 2024-12-22 04:25:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9116431d-2f12-3a1d-ad80-2335c9642c08 | -2.51803 | -54.22797 | 2024-12-22 04:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| bdc80887-69dd-3d87-9f34-ae4debd6e91e | -3.81014 | -46.72008 | 2024-12-22 04:25:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5c4f77fa-77a2-33d4-a80d-10ad79bc8134 | -4.09393 | -46.81852 | 2024-12-22 04:25:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5690a208-c4cd-369a-9a75-80f9671a79ba | -3.92318 | -46.88811 | 2024-12-22 04:25:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 45642cf8-736c-3943-8eea-0505a119eb14 | -3.79641 | -46.85043 | 2024-12-22 04:25:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3d66e04a-2268-3f62-a616-763fc05289e8 | -2.67375 | -46.93508 | 2024-12-22 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bdeb59df-f42d-3200-aebc-e0caee53e75d | -4.00557 | -46.90497 | 2024-12-22 04:25:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 41c82ecd-f1c3-3d49-96c7-afba2fb0b5d2 | -3.86132 | -46.58922 | 2024-12-22 04:25:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 565cdc4f-a1e8-32ee-9afd-3fb19f6bec0c | -1.40981 | -52.03828 | 2024-12-22 04:25:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 7e59c959-0e28-3096-bd6e-3754ed594ebd | -1.3022 | -47.7512 | 2024-12-22 04:25:00 | NOAA-21 | SÃO FRANCISCO DO PARÁ | PARÁ | Brasil | 1507409 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5b07ade1-70ee-312d-a73b-16159f930cd1 | -3.75634 | -47.19132 | 2024-12-22 04:25:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0b66f2b0-9025-3bc0-991e-55a4cecbc8fa | -4.8397 | -43.28664 | 2024-12-22 04:25:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9d2c17c4-8425-311c-8a4f-63af473a6e81 | -4.32638 | -47.78292 | 2024-12-22 04:25:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5de989c6-67c9-32f6-a5cf-83e1c2833a09 | -3.91823 | -46.91964 | 2024-12-22 04:25:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 486a3c21-fc26-325d-b71f-528153dc10af | -3.99946 | -46.92206 | 2024-12-22 04:25:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cee48f51-e5d8-3744-adcf-fb90aa24e2bd | -2.72164 | -46.17662 | 2024-12-22 04:25:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1d9c8a72-8452-3b38-99a6-41d29b0c50d8 | -4.06838 | -47.08775 | 2024-12-22 04:25:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cd5d1fdb-2e5a-38de-95d5-b579c5428211 | -3.79696 | -46.84692 | 2024-12-22 04:25:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8d6c7190-29bc-375b-874d-4c7adaf016cd | -3.16923 | -53.95641 | 2024-12-22 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b3ba6450-24af-345e-bc8d-a3dd0460aa01 | -3.86849 | -46.58677 | 2024-12-22 04:25:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 26ebff81-f3bc-320e-b9c6-59bb316ae840 | -2.93026 | -46.77631 | 2024-12-22 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 29e19a93-11fa-3662-a70e-a46e48bf975b | -2.50298 | -49.06075 | 2024-12-22 04:25:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4dd29d27-06bf-3640-9995-a0b405a83abc | -3.95767 | -41.48965 | 2024-12-22 04:25:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 0df7ddf1-effb-3177-8495-d5acec19d45a | -1.02419 | -50.87079 | 2024-12-22 04:25:00 | NOAA-21 | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9316f12e-1c3c-380b-b843-da1ae2e2bbda | -1.36275 | -53.68443 | 2024-12-22 04:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3a789f57-7dbf-3191-8c2b-e830f882fa17 | -4.01945 | -46.90353 | 2024-12-22 04:25:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 63b45f81-a0d4-32ca-a45c-472b91be3e39 | -3.98096 | -46.67187 | 2024-12-22 04:25:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ed73c0ef-3fc0-321a-8df7-8322ce251f79 | -2.24082 | -46.2711 | 2024-12-22 04:25:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 70f555a4-c558-3764-8129-8744249a1dfa | -3.80308 | -46.85145 | 2024-12-22 04:25:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 848c0e08-5cd0-3462-a18e-d31f242b2c74 | -4.04998 | -47.09578 | 2024-12-22 04:25:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f1eea840-30ee-3ab7-982f-b0c8b67c204b | -3.92572 | -46.35127 | 2024-12-22 04:25:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e3d0c418-d5e4-3f2d-b582-f1ecc6587fda | -3.84868 | -43.93651 | 2024-12-22 04:25:00 | NOAA-21 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e4bd4270-cf87-385a-b2bf-5c3e6d9e17d0 | -1.40394 | -48.21298 | 2024-12-22 04:25:00 | NOAA-21 | SANTA IZABEL DO PARÁ | PARÁ | Brasil | 1506500 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b972f8cc-ae4d-34f1-973b-52f53069e122 | -2.86929 | -45.25277 | 2024-12-22 04:25:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b3917b5b-fa92-346e-8c62-1e404b368c0d | -4.12335 | -44.24834 | 2024-12-22 04:25:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9f8650ba-e501-39e6-91a0-a30a348bf875 | -2.67039 | -46.93457 | 2024-12-22 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 52b791cc-769a-3bf1-8957-5a1b985785b7 | -2.37025 | -47.54168 | 2024-12-22 04:25:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 73ec8d90-14de-3494-b166-2a1e4e7ee36f | -2.74103 | -46.20437 | 2024-12-22 04:25:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dd80ad01-0064-3321-ae97-c5a89e6341b5 | -4.0149 | -46.80256 | 2024-12-22 04:25:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0fdb79b3-9b0b-3971-ab93-490de9763ba7 | -4.0168 | -47.05075 | 2024-12-22 04:25:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 13c46363-7be4-34dc-b573-eb161fbf5990 | -2.78183 | -47.28978 | 2024-12-22 04:25:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 835e217d-74e8-35b2-9883-635c4938e5b9 | -3.91875 | -46.8946 | 2024-12-22 04:25:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bbe1daf0-6b5b-350e-b20c-6312714e1e09 | -4.10167 | -46.8126 | 2024-12-22 04:25:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 64b3743f-37f1-3293-82dd-455fb83b9055 | -1.29872 | -47.75066 | 2024-12-22 04:25:00 | NOAA-21 | SÃO FRANCISCO DO PARÁ | PARÁ | Brasil | 1507409 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 43ed4cef-280e-3016-95d1-e1283c5af128 | -3.84526 | -43.93599 | 2024-12-22 04:25:00 | NOAA-21 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 770ab37d-9384-36db-80fc-f0cbd9692cfe | -2.67431 | -46.93151 | 2024-12-22 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 191d4703-0e61-3c1e-834e-81b09ff3598b | -4.05906 | -46.71662 | 2024-12-22 04:25:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5dc65a15-9230-38d7-8e2d-559a827caa95 | -3.90496 | -47.00399 | 2024-12-22 04:25:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9b2367d6-0b88-30ce-b4ce-96988f13e85d | -4.93018 | -41.3212 | 2024-12-22 04:25:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 06176ac0-6173-3417-bcd1-84a4220889ba | -3.92432 | -46.90262 | 2024-12-22 04:25:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 70350c17-c76c-39d9-8d2a-7072a345c647 | -4.60389 | -45.44901 | 2024-12-22 04:25:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 26ad6d9b-4e82-3ca8-8048-d79230bc92e0 | -2.56988 | -49.47153 | 2024-12-22 04:25:00 | NOAA-21 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3b6c36fd-114b-3304-afe9-779db88b6d1e | -2.44845 | -49.02592 | 2024-12-22 04:25:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 58e4c2a2-4d95-3f22-896c-bed210b64806 | -1.25712 | -53.48125 | 2024-12-22 04:25:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3cbf2d3c-e353-321f-a4aa-192c65a57e05 | -3.75354 | -47.18723 | 2024-12-22 04:25:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3101a52a-8eb7-326c-8cf4-eaa1f2ce64ae | -3.91723 | -49.03368 | 2024-12-22 04:25:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ffb788c7-f551-3f67-be55-f2b888941ba9 | -3.97307 | -46.61375 | 2024-12-22 04:25:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3c5d3007-f5e3-3427-bd14-e48c8cf908c9 | -4.08039 | -48.20739 | 2024-12-22 04:25:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d9789e51-fd81-35f6-bafa-830e6ed9c10d | -2.22894 | -53.79532 | 2024-12-22 04:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| d6af34b0-7161-3ce2-b5ca-47953b9b7543 | -2.18222 | -45.40566 | 2024-12-22 04:25:00 | NOAA-21 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d55e37b3-7100-3355-8d55-c74c09a9d7b6 | -4.01655 | -38.81196 | 2024-12-22 04:25:00 | NOAA-21 | MARANGUAPE | CEARÁ | Brasil | 2307700 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| f8c124c7-dc06-33f4-9644-7b755fef4bf2 | -2.72055 | -46.18353 | 2024-12-22 04:25:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f9c92c0c-24f1-3c43-9bec-752a32f012a7 | -4.06392 | -47.09428 | 2024-12-22 04:25:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cc42768d-8abd-372f-b7c2-200d0cfddbf3 | -2.56847 | -49.48054 | 2024-12-22 04:25:00 | NOAA-21 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 94d33402-bb89-3a64-a2b6-dd54fb29ed68 | -3.86241 | -46.58226 | 2024-12-22 04:25:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8b11d89b-0378-3ece-8725-42aaacfe3b72 | -4.08097 | -46.62033 | 2024-12-22 04:25:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 012ffde8-7598-3f78-87a2-bd55c534ebe6 | -1.71704 | -52.59479 | 2024-12-22 04:25:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 5fd837d8-fe9c-3b35-a65b-e3c17b5e8015 | -3.91402 | -46.66507 | 2024-12-22 04:25:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 21f43ca0-36bf-39fd-a3ff-06295749326c | -3.92263 | -46.89162 | 2024-12-22 04:25:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 409acd24-5f09-3fbd-af93-d6f0b4da0739 | -2.97652 | -48.08232 | 2024-12-22 04:25:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 0e00ffc6-21ae-36c8-8f61-01607e59c6fc | -3.86186 | -46.58574 | 2024-12-22 04:25:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dbd5afc8-1144-3e98-bd27-7010e1b36f7c | -3.75913 | -47.19542 | 2024-12-22 04:25:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README7.md)
