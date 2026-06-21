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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5b633818-aefa-31ec-a207-fbeb9269916d | -5.813 | -45.0799 | 2026-06-21 00:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 70.0 |
| 6296a607-f17c-3dea-ade8-2ecc81aa34ee | -12.4229 | -54.1888 | 2026-06-21 00:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 43.5 |
| e98e7ee1-e1a4-375f-9705-12a55507048a | -12.5131 | -48.3024 | 2026-06-21 00:00:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 80.8 |
| 9cf59e30-5503-3c98-8231-c461f12998c4 | -11.6309 | -48.5277 | 2026-06-21 00:00:00 | GOES-19 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 90.9 |
| 59a8b067-62c5-307f-adeb-672e81c28404 | -11.6309 | -48.5277 | 2026-06-21 00:10:00 | GOES-19 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 58.1 |
| 47278286-1cf6-36ef-b164-4c9bc6382c79 | -5.813 | -45.0799 | 2026-06-21 00:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 79.2 |
| 8e199b3d-09b8-3914-b6ce-79de9b48539e | -12.5131 | -48.3024 | 2026-06-21 00:10:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 64.6 |
| 80911b8f-216f-3808-a935-cddb9b979d08 | -11.2983 | -54.726 | 2026-06-21 00:10:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 39.0 |
| 891f31bb-ea45-30e0-8f76-ffa7cbd64b37 | -11.65 | -48.5253 | 2026-06-21 00:10:00 | GOES-19 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 75.4 |
| f673426d-0f22-3121-936b-b314ffbd7659 | -5.813 | -45.0799 | 2026-06-21 00:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 66.1 |
| 74bc3ccf-593f-3a50-a69b-6dd4726c07da | -12.5131 | -48.3024 | 2026-06-21 00:20:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 71.3 |
| 227b4709-d248-3f6a-a2c2-57e984f98179 | -11.65 | -48.5253 | 2026-06-21 00:20:00 | GOES-19 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 63.2 |
| d60b34d0-9465-3a86-ba31-54a049cedb53 | -11.0976 | -54.1516 | 2026-06-21 00:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 75.5 |
| 018e266f-efa5-3d2a-a515-9297879eb1ed | -5.813 | -45.0799 | 2026-06-21 00:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 68.6 |
| 5a52f8ac-b273-3fe6-a975-082d8f8ea000 | -11.65 | -48.5253 | 2026-06-21 00:30:00 | GOES-19 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 64.9 |
| 24510a99-3d46-388a-b117-ecdaa6576baa | -11.0979 | -54.1311 | 2026-06-21 00:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 57.4 |
| b6756474-a2f3-3c8c-ab55-30f284922234 | -12.5131 | -48.3024 | 2026-06-21 00:30:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 62.2 |
| dbaff589-b4a6-3e42-a437-c04f3d6dc6bf | -11.1165 | -54.1499 | 2026-06-21 00:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 40.7 |
| edeacbf9-cc41-3604-acaa-c6e07e81fbbf | -11.0976 | -54.1516 | 2026-06-21 00:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 73.1 |
| a71a99f2-434c-34eb-9449-4c22b02317e9 | -5.813 | -45.0799 | 2026-06-21 00:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 63.4 |
| 2f86926b-ebe9-3a6f-a467-07d0d9f2ebd3 | -11.0979 | -54.1311 | 2026-06-21 00:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 100.5 |
| 2c39d715-7d6a-3405-9c92-5ee784d2849f | -11.1165 | -54.1499 | 2026-06-21 00:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 50.1 |
| 8c647a6a-5b79-3abb-aaf3-f24a5c977ee5 | -11.1168 | -54.1294 | 2026-06-21 00:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 63.4 |
| 872c60c8-4e79-3baa-9450-155c7753e04d | -9.5347 | -40.3033 | 2026-06-21 00:40:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 70.1 |
| e6710ecd-1155-3b7e-8f63-784b4a7677b0 | -12.5131 | -48.3024 | 2026-06-21 00:40:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 68.3 |
| dc909fe9-f209-3c51-bef9-4823e7b25215 | -12.5131 | -48.3024 | 2026-06-21 00:50:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 64.7 |
| 89bd6835-09bc-3920-9ef9-a5023647212f | -5.813 | -45.0799 | 2026-06-21 00:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 59.7 |
| cecce71c-dfe3-3646-bc44-b7955c0ad4f2 | -9.2878 | -40.2392 | 2026-06-21 01:00:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 64.5 |
| 2cf64795-a8d6-3e82-9cde-522558a77646 | -11.1165 | -54.1499 | 2026-06-21 01:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 67.3 |
| d2f6c2e1-de49-347a-b1f4-1635dc0c8fdf | -11.0976 | -54.1516 | 2026-06-21 01:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 114.1 |
| 2dcdaab0-e93c-3599-be7d-a945894d6722 | -5.813 | -45.0799 | 2026-06-21 01:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 62.3 |
| c6cb3546-2685-3c46-b97e-2ec9ce665055 | -12.5131 | -48.3024 | 2026-06-21 01:00:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 57.2 |
| f7e39590-a7d5-3088-ba5d-f93836d48db3 | -11.0979 | -54.1311 | 2026-06-21 01:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 110.7 |
| 8071e11d-318b-3567-ae56-36a8d051b3c1 | -11.1168 | -54.1294 | 2026-06-21 01:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 64.6 |
| 9df5f4a4-e385-300c-95e1-4f52a2dd86b0 | -12.4187 | -54.18361 | 2026-06-21 01:02:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 41.7 |
| 357e61fe-e700-3355-815c-867f377c0150 | -10.93266 | -56.84677 | 2026-06-21 01:05:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 9.2 |
| ca3787d4-33bf-3dd1-8870-223bd99a73b5 | -9.18356 | -58.04925 | 2026-06-21 01:05:00 | TERRA_M-M | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 10.3 |
| eebfcff2-9663-33d8-ad14-1bec11f5790f | -9.18571 | -58.06348 | 2026-06-21 01:05:00 | TERRA_M-M | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 21.6 |
| d5478ce5-9ca7-3e7d-8161-5cd0f0f39708 | -10.68651 | -60.75095 | 2026-06-21 01:05:00 | TERRA_M-M | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 119076ce-ab55-310d-b402-f48af4b5c45c | -12.5131 | -48.3024 | 2026-06-21 01:10:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 54.9 |
| d78d1058-e80a-3c22-bb77-bddf1c26527b | -11.0979 | -54.1311 | 2026-06-21 01:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 47.3 |
| c011838e-06df-3e3a-842d-9c7d22822e38 | -11.0781 | -54.104 | 2026-06-21 01:15:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4d626d74-009b-3e16-9115-e9ca7b16ae70 | -11.102 | -54.155201 | 2026-06-21 01:15:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| fd83a35f-9b25-37b4-ad6c-245fe23301b0 | -11.1045 | -54.125702 | 2026-06-21 01:15:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3d54174c-af6b-31ff-9b75-34c97af04a66 | -11.0949 | -54.128399 | 2026-06-21 01:15:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 91480aaa-cfeb-3f1b-a99e-15c4425306d1 | -11.0877 | -54.101398 | 2026-06-21 01:15:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 70dfda33-d2ff-3f71-a6b5-57fbdd9ad245 | -11.0853 | -54.131001 | 2026-06-21 01:15:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c9d27aa6-d420-34f0-879c-9c827033c315 | -12.5131 | -48.3024 | 2026-06-21 01:20:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 52.5 |
| 9f227e70-b6d8-35fb-b8d9-f2872a0c60b1 | -12.5131 | -48.3024 | 2026-06-21 01:30:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 54.8 |
| 4531eb10-5f62-31c6-9bdf-f39a297d79fb | -11.1168 | -54.1294 | 2026-06-21 01:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 133.9 |
| 710c0bd4-13d4-3a2c-a8c6-e97e3e344cf8 | -11.0979 | -54.1311 | 2026-06-21 01:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 151.4 |
| 39093adc-f457-3e2a-80e8-622b4eabfb8e | -11.1165 | -54.1499 | 2026-06-21 01:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 154.0 |
| fed9db5d-7e28-386b-9217-b275756e7fd7 | -11.0976 | -54.1516 | 2026-06-21 01:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 185.1 |
| 391314f8-8172-37bd-a650-5834996d8027 | -11.0976 | -54.1516 | 2026-06-21 01:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 196.7 |
| 5e5f9be5-846b-3964-b1f4-dc5172da15ef | -11.1168 | -54.1294 | 2026-06-21 01:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 118.8 |
| 5ddb86c2-bbc3-396a-bdf8-e0c6078877ca | -11.0979 | -54.1311 | 2026-06-21 01:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 208.3 |
| 44214487-9ca3-3669-ba5a-a9c53549aaf9 | -11.1165 | -54.1499 | 2026-06-21 01:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 115.5 |
| 266cef98-b246-3395-afc6-dda683cbf646 | -11.0724 | -54.174301 | 2026-06-21 01:42:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| aa043898-313a-311f-9160-e7309bd57f36 | -11.0705 | -54.1278 | 2026-06-21 01:42:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| af8d889a-f555-3675-9941-c979b2ed0a4a | -11.057 | -54.154999 | 2026-06-21 01:42:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 24d9cdf7-69f1-307d-8f6d-3870c30e501f | -11.0763 | -54.149799 | 2026-06-21 01:42:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ee988a61-8258-3701-86f5-f9c6b0514090 | -9.1444 | -58.063099 | 2026-06-21 01:42:00 | METOP-C | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 41d92f0f-d55a-33b4-b290-34c41b2a08aa | -11.0608 | -54.130402 | 2026-06-21 01:42:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8cae5d5e-d200-3f7e-994b-5570c3ce9e0d | -10.2347 | -60.554901 | 2026-06-21 01:42:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 19a40d33-3288-3988-869f-7fb153976682 | -11.0512 | -54.132999 | 2026-06-21 01:42:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b643f6e7-a488-3793-840d-9e0a708ddb46 | -11.0666 | -54.152401 | 2026-06-21 01:42:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b3437603-8f93-392f-95ba-261ed839aaf2 | -11.1168 | -54.1294 | 2026-06-21 01:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 143.3 |
| 8fbaedab-d51b-3f65-b572-291a742113e3 | -11.1165 | -54.1499 | 2026-06-21 01:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 115.0 |
| e81c455d-442b-31cb-bb5a-b5eb065255e7 | -11.0979 | -54.1311 | 2026-06-21 01:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 195.6 |
| b16e9133-3d39-33a3-9ff4-b82eca16ac07 | -12.5131 | -48.3024 | 2026-06-21 01:50:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 57.1 |
| 7d2ea002-f5af-3294-aed9-68271e50feac | -11.0976 | -54.1516 | 2026-06-21 01:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 163.5 |
| d5a620f8-0aaf-3317-8f59-ac44d8666b4c | -11.0976 | -54.1516 | 2026-06-21 02:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 220.3 |
| 9d6bafc9-aa4f-3568-bae2-f098950094fd | -11.1165 | -54.1499 | 2026-06-21 02:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 130.7 |
| debb4059-5974-3c37-b832-b564fae0ba2d | -11.0979 | -54.1311 | 2026-06-21 02:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 203.4 |
| 97775dc4-1d70-3623-bd2f-ab989dc2eff9 | -11.1168 | -54.1294 | 2026-06-21 02:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 121.0 |
| bf1fe6fb-fc1c-3a84-b68d-a70cff1c2522 | -11.0979 | -54.1311 | 2026-06-21 02:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 89.6 |
| dfd5c7f8-3236-3811-bed1-178f5936d316 | -11.1168 | -54.1294 | 2026-06-21 02:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 61.4 |
| 46b54224-998d-3a90-9187-e79cd6b7cfe0 | -11.1165 | -54.1499 | 2026-06-21 02:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 46.6 |
| d4b3c27e-f0ac-3e91-9a1c-1dc6c100dd5c | -11.0976 | -54.1516 | 2026-06-21 02:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 85.0 |
| d299f232-fb3f-3a89-9495-304b446633e6 | -11.1165 | -54.1499 | 2026-06-21 02:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 44.4 |
| 40be886c-8850-384e-a5d0-4e27c8cb3b03 | -11.0976 | -54.1516 | 2026-06-21 02:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 77.9 |
| 070cf0c9-c11a-33a3-b857-136cb273d13a | -11.1168 | -54.1294 | 2026-06-21 02:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 41.3 |
| d8b973dd-0cea-3cf6-bd25-2f66af0551cd | -11.0979 | -54.1311 | 2026-06-21 02:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 74.8 |
| d6263423-d154-3077-8524-6111208511fe | -11.0976 | -54.1516 | 2026-06-21 02:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 53.4 |
| 56732b96-3628-3ca2-9d69-80f441de12f0 | -11.0979 | -54.1311 | 2026-06-21 02:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 44.5 |
| 847d1122-2ee5-3469-a235-43285c6323ad | -11.1168 | -54.1294 | 2026-06-21 02:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 71.5 |
| efa9fac7-bdad-3b15-b0de-3c8fd789b3d3 | -11.1165 | -54.1499 | 2026-06-21 02:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 53.9 |
| b293f44b-ecb3-3bed-ae59-ab84f62ef23c | -11.0976 | -54.1516 | 2026-06-21 02:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 81.0 |
| fe421717-6ca4-348e-85bb-b0df9dcc9758 | -11.0979 | -54.1311 | 2026-06-21 02:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 101.2 |
| a5c01d20-94f6-3141-83f9-c09376256580 | -11.1168 | -54.1294 | 2026-06-21 02:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 74.2 |
| 448de3c4-f32f-3e59-85a5-c746a2503429 | -11.0976 | -54.1516 | 2026-06-21 02:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 110.2 |
| 07fb1412-bbb4-336b-93fd-2e5e23cf7863 | -11.0979 | -54.1311 | 2026-06-21 02:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 110.9 |
| fad93a57-c69e-39cd-8505-9bd17d6db06f | -11.1165 | -54.1499 | 2026-06-21 02:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 71.7 |
| a3653548-39c4-30f7-902c-76d913a7d168 | -11.0979 | -54.1311 | 2026-06-21 03:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 83.9 |
| 7a3a28c4-7489-36a1-a822-06cf734f997a | -11.1165 | -54.1499 | 2026-06-21 03:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 59.9 |
| 942334bd-de3d-3d68-8d6c-b0e602156195 | -11.0976 | -54.1516 | 2026-06-21 03:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 77.3 |
| cb222d43-574a-3152-9f5f-f27160111f38 | -11.1168 | -54.1294 | 2026-06-21 03:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 72.8 |
| 3a0213e5-25e1-360f-91fd-8f7ea880d257 | -11.1165 | -54.1499 | 2026-06-21 03:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 103.1 |
| b7e76baf-d4c0-3a24-b002-135a829463ef | -11.0976 | -54.1516 | 2026-06-21 03:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 136.5 |
| bd62d1aa-710c-3999-98fc-d07770f144dd | -11.0979 | -54.1311 | 2026-06-21 03:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 126.1 |


[Clique aqui para ver as próximas entradas](README2.md)
