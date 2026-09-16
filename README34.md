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

## Dados Diários - Página 34

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e2f7e69a-4b9c-3e00-a020-71cd281a8391 | -6.40065 | -44.05619 | 2026-09-16 04:57:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7a7110c8-ce34-3e57-886b-9b78a70052a9 | -6.15236 | -52.74456 | 2026-09-16 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1109d9ec-c9f2-3af1-aa48-f65657d32dac | -5.63861 | -51.69121 | 2026-09-16 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 7498c0eb-86c1-37ad-9c46-69a86cdfdb67 | -5.78116 | -45.09124 | 2026-09-16 04:57:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 293b52a7-3c82-3078-b82e-531568eb1f7c | -6.70687 | -56.88185 | 2026-09-16 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 3e5dd60c-7b17-3eb1-96c7-8c6a466d4d61 | -6.34689 | -55.55733 | 2026-09-16 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 010b60d4-5f5e-3556-bdd7-88bed3110f13 | -6.37265 | -55.8288 | 2026-09-16 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| fcf41d02-ab9d-34f9-bfab-4c9859944c48 | -6.77254 | -58.80512 | 2026-09-16 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| bb9ab541-f04e-3cd8-a62f-d92f5503e976 | -6.77024 | -58.80714 | 2026-09-16 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 14529e4a-fe25-3d1a-aaa6-55cc58058566 | -5.15203 | -55.93197 | 2026-09-16 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 17.8 |
| f24a9190-394a-338d-bdd0-ef8f3df6839f | -3.76272 | -51.1409 | 2026-09-16 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 06a5a1fd-1f2a-3754-b5cf-b7114abf84ca | -3.48208 | -54.67592 | 2026-09-16 04:57:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 21bb6b41-881d-3f1e-ac65-7e52fa9c824f | -5.14007 | -55.94139 | 2026-09-16 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1d17b2a4-883d-3ac9-b9a8-4c1228879a31 | -5.13781 | -55.93358 | 2026-09-16 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 16778c6f-3d59-34b9-bdc4-cef94a90a413 | -6.09826 | -53.53942 | 2026-09-16 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c75a3915-bc77-332e-a242-4b078286fb10 | -6.69455 | -56.41276 | 2026-09-16 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| dcd85bd8-8dbf-329f-990c-7a34c12cba4d | -6.27209 | -55.29945 | 2026-09-16 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4490aaa9-4c79-3c2a-affc-9e5adee9f7f5 | -8.85578 | -44.90728 | 2026-09-16 04:57:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 62f603e7-c3b4-3a39-b4d2-1408401382fe | -6.35023 | -55.55787 | 2026-09-16 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a26d04ea-3eb4-3d8b-8f0b-de9431d39123 | -6.72895 | -48.11368 | 2026-09-16 04:57:00 | NOAA-21 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 2cedf995-acc9-3645-9bf7-6f4594155eea | -4.35937 | -50.85649 | 2026-09-16 04:57:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5a2538ec-dc06-3eaf-9fc7-926491b3dffd | -4.52475 | -54.96863 | 2026-09-16 04:57:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b812ea43-7c22-3edd-8aca-33ebbc67e5b9 | -3.77731 | -58.84841 | 2026-09-16 04:57:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6a4c6f31-7a46-3760-8282-6bf752832ab2 | -4.51809 | -54.96761 | 2026-09-16 04:57:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fc9ad888-eabe-3692-9b4a-7eb558046ebd | -8.55112 | -44.50195 | 2026-09-16 04:57:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 292ef387-a720-37e5-975b-8f3bc8c43809 | -5.90893 | -52.10754 | 2026-09-16 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4935ae0f-44de-383c-b7c1-a53112f09ad1 | -6.02591 | -57.77145 | 2026-09-16 04:57:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| f41ead44-70a8-34e4-aaf1-777460dfdb29 | -8.85673 | -44.8997 | 2026-09-16 04:57:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1e163ccf-bd77-3d64-b740-dd44ebe636ea | -2.10467 | -52.05474 | 2026-09-16 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| dddc0783-2df7-3da3-89e6-be5003183376 | -5.88706 | -52.08881 | 2026-09-16 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 894b2586-ad12-3ce4-8035-0c028db08c74 | -8.79197 | -50.5473 | 2026-09-16 04:57:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 584b47de-b790-3499-8e81-b491505cd378 | -9.10965 | -45.73184 | 2026-09-16 04:57:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 7.3 |
| a52e8048-96ae-3306-af6a-6aae715cc6f9 | -2.90928 | -50.39183 | 2026-09-16 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bf8e2cbe-10aa-3abd-ac6b-9801457e323f | -6.81081 | -59.17599 | 2026-09-16 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 7fb86111-3063-35df-a3de-7098ab830f56 | -6.10396 | -57.6353 | 2026-09-16 04:57:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 857d83df-7d61-3aed-bca5-6f34a80adf90 | -2.91226 | -50.39656 | 2026-09-16 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3fa129ac-3821-3dd2-8709-36e6ce526c73 | -8.47836 | -44.56653 | 2026-09-16 04:57:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| a554a499-f465-370f-8460-3a384d87e047 | -2.82526 | -51.33952 | 2026-09-16 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 68db24f0-4c1c-305b-80d9-c768892cb439 | -3.156 | -58.63581 | 2026-09-16 04:57:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 437f5935-f02d-37db-b94d-4c642d490a02 | -2.9066 | -50.43393 | 2026-09-16 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 67f964bf-e196-3a7c-aac3-c47150b73101 | -8.84312 | -44.8915 | 2026-09-16 04:57:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 46836e0b-66b2-3a22-aacd-920c60ed0cd4 | -9.4663 | -45.4521 | 2026-09-16 04:57:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 878bb6f6-d6ac-321f-80c5-4307320aa518 | -6.3862 | -55.24545 | 2026-09-16 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2ac26aa9-f70e-3032-8377-69f0c5ddb9af | -6.10158 | -53.53994 | 2026-09-16 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ae80bd0c-66f9-3400-a3be-3f97c8d9da7f | -7.44516 | -49.47256 | 2026-09-16 04:57:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e42cfd80-d145-31c7-ad9a-19a0650cc709 | -2.90551 | -50.41679 | 2026-09-16 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9d71d863-865e-3c99-b57d-aa3284bc0d65 | -2.90425 | -50.42509 | 2026-09-16 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7db1c05c-a33f-3919-a432-22bde8eee785 | -9.54927 | -45.42001 | 2026-09-16 04:57:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d5190224-69c3-3016-bba4-e033d1e09eb7 | -2.98787 | -54.16101 | 2026-09-16 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e74a7349-b457-3f7a-a030-811f451f33e6 | -2.26098 | -47.006 | 2026-09-16 04:57:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7da7a366-63a1-35ff-9ffe-7d08a8a0e74b | -9.11501 | -45.7326 | 2026-09-16 04:57:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 7.3 |
| d27b43dd-e917-38c6-a520-bfc9efb51c22 | -5.24126 | -59.98386 | 2026-09-16 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bcb406dd-b615-3b58-9641-1631f1be9f50 | -3.0213 | -51.34089 | 2026-09-16 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 105da60c-72e5-3a2f-aca2-efc4bdf5e8e9 | -4.51475 | -54.96709 | 2026-09-16 04:57:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2419202d-a165-37de-9728-52df40c6ea58 | -6.34751 | -62.70088 | 2026-09-16 04:57:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 22e49fc4-d0a9-3ec0-b38d-3e104d8ccca7 | -5.99345 | -52.10416 | 2026-09-16 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 0fd1d07b-dcca-3e38-abd9-d204ba40d6ef | -2.91633 | -50.41846 | 2026-09-16 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 708a3d2f-9e15-3f75-ba63-35e4b372dea0 | -6.3172 | -59.96423 | 2026-09-16 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 7a0b23f3-64c9-3664-ac31-4a4e570b17e5 | -6.32972 | -62.68727 | 2026-09-16 04:57:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| d66acae6-8c31-3c8d-ac99-bdf3f0cc8b53 | -2.90002 | -50.42868 | 2026-09-16 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6f61e744-c84e-385c-9996-2d1a40d69453 | -6.2773 | -50.94267 | 2026-09-16 04:57:00 | NOAA-21 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ee09e09f-fdf2-3269-9ab9-584b22af902e | -1.61426 | -55.57193 | 2026-09-16 04:57:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 628fb5cb-2a0a-3ea9-a899-f25e49f21c3d | -6.71167 | -58.80261 | 2026-09-16 04:57:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.8 |
| f04368c7-5164-348c-98e7-57af2eca4925 | -3.76213 | -51.14484 | 2026-09-16 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 13355016-2cfc-335c-b287-91d250c7bb92 | -8.47202 | -44.57051 | 2026-09-16 04:57:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d770282d-edfe-3ad8-a2cb-9771f55bb091 | -2.89107 | -50.41457 | 2026-09-16 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9fd62433-e4cc-386f-af5a-ec921dc28ac3 | -8.47257 | -44.5661 | 2026-09-16 04:57:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d872ff66-3bb9-3eaf-a028-e680a02a7734 | -3.59946 | -59.06764 | 2026-09-16 04:57:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7b473087-c614-33eb-add0-abb0c7c217cd | -5.71736 | -46.19364 | 2026-09-16 04:57:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 47934557-293e-3075-ba89-1876d0340e3a | -9.09406 | -45.72583 | 2026-09-16 04:57:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 24.2 |
| 2347c4af-2312-382b-8d08-604c9c674467 | -4.46637 | -55.05697 | 2026-09-16 04:57:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c0c17d1c-201a-3fc8-b1fb-104746d9e3b9 | -3.4782 | -54.67889 | 2026-09-16 04:57:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a03aada9-2bea-3851-b419-c02dc8cc6dfe | -4.83722 | -55.76994 | 2026-09-16 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 10f5cd31-8eb5-37dd-bca1-88831bfabf93 | -5.85679 | -51.94484 | 2026-09-16 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 789ae0c8-e43f-3172-9155-b20878e4dd06 | -5.88369 | -52.09259 | 2026-09-16 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 640fe040-dbce-31fc-9c87-eec07dce8001 | -1.744 | -55.25806 | 2026-09-16 04:57:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8edb86ed-26ca-3c90-86ff-787a57a34c2a | -5.88482 | -52.08528 | 2026-09-16 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 55f8288b-65cd-3fb2-97fc-d8a0d6c9704b | -6.33424 | -62.69106 | 2026-09-16 04:57:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| cec8f997-6b99-39e4-8abb-0dbb559fb468 | -5.35851 | -55.89262 | 2026-09-16 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 15df2798-9db7-3701-b607-3b2c06a91f67 | -6.37207 | -55.83242 | 2026-09-16 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 688e90b0-7f8b-3905-9c13-2fd1b68b6bfe | -3.18112 | -61.10843 | 2026-09-16 04:57:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ff8964f4-ba98-3603-8c10-22b5f9966338 | -5.14065 | -55.93772 | 2026-09-16 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fc68c953-0dd6-3870-8b03-d30b2c1f5235 | -3.90356 | -55.87844 | 2026-09-16 04:57:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6f74f392-3821-33cb-9fb1-d25fee9276e3 | -4.46788 | -55.24254 | 2026-09-16 04:57:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e3cfba95-187e-326d-a068-7c5ef14c80b5 | -3.38061 | -50.84212 | 2026-09-16 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 07f99219-be77-30b3-acbd-2f2d3d062909 | -6.22636 | -55.65155 | 2026-09-16 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 69e0f646-adfa-3b5f-b615-c1d61f216a7c | -6.26499 | -43.2832 | 2026-09-16 04:57:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 4d375b9a-9c5d-30ae-9a81-7cd4069872a7 | -7.16327 | -52.71338 | 2026-09-16 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 47bcccd3-45b7-3b3b-b8ca-323fcced9c6f | -6.32462 | -59.99702 | 2026-09-16 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 33c54409-2abc-344f-9e64-d36930ee46b8 | -5.46119 | -60.2213 | 2026-09-16 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 75cda093-ca79-37ec-8df7-b521bd402671 | -2.05652 | -52.08408 | 2026-09-16 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b37c6fda-aeec-3a82-87d8-1d77a7e12761 | -2.90488 | -50.42095 | 2026-09-16 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d02cb445-74c8-385d-99bc-ff4b12774449 | -6.80687 | -59.17537 | 2026-09-16 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| eb367849-c442-3a7c-9065-3f6193e15424 | -5.88651 | -52.09243 | 2026-09-16 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e86254d2-01b9-32a6-b6ff-1015296c9a11 | -2.801 | -49.41665 | 2026-09-16 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 038caa9f-ed2b-36fe-b119-2933a17c5fdc | -5.86182 | -52.12019 | 2026-09-16 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 99607ec8-b1a5-3d39-8b93-0fcbb71ffb86 | -2.56318 | -54.7416 | 2026-09-16 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ed8055c0-fe69-3b81-9d73-f7ccac31e3b6 | -6.79422 | -58.79374 | 2026-09-16 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9350198c-3c94-34cb-ba1a-ca91fc27e6ea | -9.3408 | -44.38583 | 2026-09-16 04:57:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 6412b3e1-089c-3fde-9965-c02e2a4f03e3 | -6.32644 | -55.25772 | 2026-09-16 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |


[Clique aqui para ver as próximas entradas](README35.md)
