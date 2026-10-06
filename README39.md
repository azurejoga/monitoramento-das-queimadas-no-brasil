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

## Dados Diários - Página 39

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2d6e5ccf-eb99-3a49-b54c-df4a9b38f3ac | -2.99243 | -54.12088 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 19418da5-e59e-3841-9e51-c7d5559c5ed1 | -5.46196 | -45.51971 | 2026-10-06 04:38:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 46cd18ab-d47d-3623-8ef9-b424ea98960b | -3.84325 | -50.31902 | 2026-10-06 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1fa4ee6f-a775-34c1-aaa7-d9037db78197 | -3.16332 | -50.60168 | 2026-10-06 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| ddd8a82a-e0ad-3807-8ed7-0f1ec1061bc7 | 2.47126 | -50.83142 | 2026-10-06 04:38:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 87c9890e-6cd6-3191-a615-4e614f5248ea | -3.7179 | -48.88208 | 2026-10-06 04:38:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 3b13791d-92de-3c88-856c-b439a278bdd8 | -3.13291 | -53.72242 | 2026-10-06 04:38:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c5da8a68-5d84-3ce9-88a5-33e64d044d58 | -2.78262 | -54.11105 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| b1f99a21-3707-3c04-8bce-a065530a50ea | -2.80231 | -54.13509 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2e5a28d0-e9c5-3964-8873-90d3bf1c7f58 | -3.49413 | -53.44397 | 2026-10-06 04:38:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 23c347e8-e7a4-3052-b0ff-ba09569c8115 | -2.86638 | -54.14585 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| ed429e9a-6dc2-30a5-9062-ed450914ba67 | -3.06465 | -54.16914 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 15fd4446-3ffb-3b81-88e4-697c0f3b174c | -5.43952 | -43.44667 | 2026-10-06 04:38:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 8c8c476c-bffa-3f99-b9ac-ac4fd961b772 | -4.5077 | -43.69316 | 2026-10-06 04:38:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2578411e-8113-3b57-a28d-8e5f1daf5769 | -2.77724 | -57.65783 | 2026-10-06 04:38:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2097f44f-09a2-3e41-9e67-8e910a1a597d | -2.84429 | -54.07978 | 2026-10-06 04:38:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5e420de9-c062-37d8-96a0-10b85c15adf4 | -5.9595 | -41.3503 | 2026-10-06 04:38:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 7a164918-d906-3e2b-a81f-2c2c7fc7ae63 | -3.02322 | -53.90077 | 2026-10-06 04:38:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 27.6 |
| 6000b9c3-56f7-3e5d-937d-864c4ee70af4 | -4.06227 | -54.04851 | 2026-10-06 04:38:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 712dff0c-0620-33a3-bd1f-d25f375802cd | -3.11293 | -53.70572 | 2026-10-06 04:38:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| df4849c1-5ca8-36f4-ab46-3f5c23d5650e | -5.22512 | -48.39836 | 2026-10-06 04:38:00 | NOAA-20 | SÃO SEBASTIÃO DO TOCANTINS | TOCANTINS | Brasil | 1720309 | 17 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1387018b-0991-37d0-8dd0-a6406c65fbe1 | -2.78471 | -57.68451 | 2026-10-06 04:38:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 7aa09e9e-7bc1-340c-a4df-45695380df59 | -3.10286 | -53.76679 | 2026-10-06 04:38:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| a0a2ecf0-b70c-3e6a-8b67-e82ef3ff90da | -2.85501 | -51.30278 | 2026-10-06 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 70014f87-054c-3c5f-aac4-c750701e9c6a | -3.04553 | -54.22851 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| dba032d5-a690-3fb9-a58a-b8ab99186346 | -3.0791 | -54.25084 | 2026-10-06 04:38:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 20.6 |
| 3343061e-6cdf-338a-87f5-caaa50dff97b | -2.90055 | -54.08176 | 2026-10-06 04:38:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6ddbccb0-676f-35af-bbd8-21f688934f82 | -5.23165 | -48.39975 | 2026-10-06 04:38:00 | NOAA-20 | SÃO SEBASTIÃO DO TOCANTINS | TOCANTINS | Brasil | 1720309 | 17 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d5805795-2318-3b30-abdd-cdf088cf598a | -4.5045 | -42.06919 | 2026-10-06 04:38:00 | NOAA-20 | BOQUEIRÃO DO PIAUÍ | PIAUÍ | Brasil | 2201945 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 471f9604-07d8-3e9d-98b0-364178d0b601 | -3.68453 | -55.95123 | 2026-10-06 04:38:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| c023c894-c94d-3730-b203-77a6c94dd6d6 | -3.84681 | -50.31953 | 2026-10-06 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5164f9f4-0a2a-3368-bf0d-f85a11be185f | -3.73647 | -48.87399 | 2026-10-06 04:38:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 15a2d0b3-4648-3cc0-8ad8-d57fc379c4a9 | -3.05123 | -54.39756 | 2026-10-06 04:38:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f61ae8ff-466d-31ec-86e6-d914909a9923 | 0.99019 | -50.02117 | 2026-10-06 04:38:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a57a563e-ef7a-3212-9ddc-aabfbd748178 | -5.94617 | -41.31652 | 2026-10-06 04:38:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 4d8a055d-8b08-3761-9385-766ec76f6019 | -3.37273 | -58.19224 | 2026-10-06 04:38:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 6721ffab-78a2-38f6-8283-79684ee22634 | -2.9392 | -54.13118 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| acc1f911-a18f-3396-b56a-d0baca3841a9 | -3.69316 | -55.96234 | 2026-10-06 04:38:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f9b294aa-c7c9-3dbf-b5f1-511d267ffc5e | -3.46561 | -50.10205 | 2026-10-06 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7add5622-f8bd-3c4d-949c-139ade87dc4b | -3.16264 | -50.6059 | 2026-10-06 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| a6976611-4745-3263-823a-64cbc152c4bd | -4.35602 | -47.7743 | 2026-10-06 04:38:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 868c5faa-5f71-3be8-87fd-0b9a1661763e | -6.6227 | -37.88925 | 2026-10-06 04:38:00 | NOAA-20 | LAGOA | PARAÍBA | Brasil | 2508109 | 25 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 4b52af3d-791f-350c-b332-004178aed8f0 | -2.94983 | -54.15219 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6c70e269-2796-34b4-90a3-35d0fb8bc911 | -3.09389 | -53.73831 | 2026-10-06 04:38:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 29a3c134-fa98-3f67-b969-21813ff61350 | -4.05409 | -54.04258 | 2026-10-06 04:38:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d6eac190-5597-3bb5-9b4b-a52364f79d09 | -3.26978 | -50.40087 | 2026-10-06 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| e4606a9a-fd1b-37d0-a33d-7635a87e8ea7 | -2.98254 | -54.12418 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 009c9d24-f260-3d09-875f-367a6c7a8a15 | -4.05264 | -54.05136 | 2026-10-06 04:38:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f207793e-6807-3061-922d-68a54a4866e8 | -3.0997 | -54.18462 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 3572f5a9-2f6f-36fe-b34d-63e900af1541 | -2.98582 | -48.5913 | 2026-10-06 04:38:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 6462f227-e240-3e78-a66b-4ec44bc9d7b3 | -2.86792 | -54.13632 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7bf79be7-71a7-3fb4-aa71-8fb20461ee0c | -2.99087 | -54.10155 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a1607cde-26a0-330e-8e2f-323846afd2a9 | -3.49779 | -54.61755 | 2026-10-06 04:38:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ea6a0e58-8fff-320b-b86a-f94025e4657a | -3.22585 | -54.30315 | 2026-10-06 04:38:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 68e75dcc-898f-341e-a6eb-461071231182 | -2.88011 | -54.14812 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ce7526ae-205c-3ba8-928f-d202fcdb8761 | -3.03922 | -54.26706 | 2026-10-06 04:38:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7c76d1d1-5fc6-3257-a16a-b49cb0e89e8b | -3.78059 | -41.59748 | 2026-10-06 04:38:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| aa555b36-76d3-31f3-8154-249ab557cd98 | -3.06846 | -54.17456 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| e423690e-b291-3376-811d-5ea204e0c08f | -2.91947 | -54.10871 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8ac9ed57-3576-3386-9b39-1e3d11a08f5a | -3.1085 | -53.70503 | 2026-10-06 04:38:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 84354a78-d74b-3865-a86d-eeeeccdbca75 | -3.09281 | -54.1691 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 2c2e7f04-50bc-326b-b960-d5becf4d7901 | -2.99932 | -54.13636 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 98f5a6cb-06ca-3324-99b4-23dbf91c7bc4 | -3.02018 | -53.89107 | 2026-10-06 04:38:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 32.7 |
| 74c46040-99a7-3271-b0c7-8b17bd1f9d33 | -2.98788 | -54.12299 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| f4903f44-d121-3c70-a3f8-a48d0b1cbc72 | -3.10131 | -53.74853 | 2026-10-06 04:38:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d3834bff-fd02-3c63-93b7-34cdd2bd19c7 | -4.71983 | -44.08433 | 2026-10-06 04:38:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c342ecd7-22ad-30b5-9273-a1bc64f1b728 | -0.5784 | -50.4431 | 2026-10-06 04:38:00 | NOAA-20 | AFUÁ | PARÁ | Brasil | 1500305 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cf522089-856b-3084-b1c6-f68f521c40b7 | -3.07603 | -54.15688 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0c15cc2d-13e8-303e-94ab-edc55f1c96eb | -2.91111 | -54.10261 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6904bd43-b505-31d8-bf24-7269900af167 | -3.83798 | -50.31077 | 2026-10-06 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| ec1ad9e4-62b5-3525-a6f8-22e8096402aa | -3.06921 | -54.16993 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 3d3ad223-d323-3c05-a23d-2b560bd19502 | -3.05778 | -54.21125 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 1fa843b7-9294-3202-9fef-8ba03a182a90 | -3.09478 | -54.18589 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 8f44a310-acb1-3f72-8981-aedd7bb1498e | -3.74548 | -49.39128 | 2026-10-06 04:38:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8dd9391f-8313-3eee-80a0-8ae8bf792f9e | -3.11835 | -53.75581 | 2026-10-06 04:38:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8705c6a9-0d95-347a-beee-25e66a82644c | -5.96648 | -41.36487 | 2026-10-06 04:38:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 88a0affe-5cd9-3a30-a33e-20e132240489 | -1.1029 | -54.15892 | 2026-10-06 04:38:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bf6c8d10-b3f2-3b47-9745-ed3bdefe4b9c | -2.99166 | -54.12836 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 4368d4bb-4f3c-3209-aec0-883429accd74 | -4.7705 | -50.81013 | 2026-10-06 04:38:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cff79657-8013-3277-a04e-6d975403dd3c | -3.50535 | -51.67327 | 2026-10-06 04:38:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bea44fa6-90d4-32b5-b395-cb5bc0e5f28d | -3.0959 | -54.17905 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 872206f3-07aa-3cf2-861c-c7147254e8f5 | -4.45454 | -47.92441 | 2026-10-06 04:38:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 17.9 |
| 86d4ce82-9f75-314c-9e51-180e40f082a0 | -3.09379 | -53.71152 | 2026-10-06 04:38:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 572568ca-acb4-30d6-bc5d-f378167efd69 | -3.96557 | -56.1273 | 2026-10-06 04:38:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6fac0b8e-9b2d-3581-a122-330007377acc | -1.05355 | -53.58957 | 2026-10-06 04:38:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5ec92796-454c-3ea0-bc81-497315cf7ab3 | -5.88339 | -43.45944 | 2026-10-06 04:38:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 60b5a11d-e866-3f80-9cd4-7aa91b9f1dc6 | -3.39803 | -44.48549 | 2026-10-06 04:38:00 | NOAA-20 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| e8f2b9f9-d7bf-305c-856e-96ecda617d23 | -3.07685 | -54.1807 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 00bb872d-496d-3835-9e7d-3cf8092f33a8 | -2.59841 | -47.352 | 2026-10-06 04:38:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 612629c4-f302-3277-9c42-b39096a947e7 | -1.099 | -54.1531 | 2026-10-06 04:38:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4022fd83-e45a-38c8-a8b6-b360cb95f4d1 | -3.46914 | -50.10262 | 2026-10-06 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 07fa52d8-ac3c-3061-8a82-7cceeae36ca5 | -2.13508 | -56.70041 | 2026-10-06 04:38:00 | NOAA-20 | FARO | PARÁ | Brasil | 1503002 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4678daab-471d-3536-a562-4df4d761c1b8 | -2.95669 | -54.11028 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 740979c0-eca2-374a-abc1-ddbf910e742e | 1.72378 | -55.64225 | 2026-10-06 04:38:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2a54afaf-4c41-3760-8c7b-13eb1551a171 | -3.71175 | -51.14136 | 2026-10-06 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f3e11840-62ea-3eb0-b6f0-0b17cbaf8d7c | -2.8989 | -54.11958 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 90ae2e7b-0028-3465-a1ca-5804dd3b446c | -3.88524 | -55.8036 | 2026-10-06 04:38:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5701868a-c0c7-3928-ac6f-5962d4f96833 | -4.25525 | -50.79782 | 2026-10-06 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f8adf15d-de96-301b-90d0-05b76445abe0 | -2.85122 | -51.30217 | 2026-10-06 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f900122a-6422-35bc-9142-8fe0aeae5822 | 1.79384 | -55.54451 | 2026-10-06 04:38:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README40.md)
