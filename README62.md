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

## Dados Diários - Página 62

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 45d90c1f-9727-3204-81a2-8087d892c9e5 | -9.2415 | -47.3487 | 2026-09-27 15:00:00 | GOES-19 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 76.6 |
| 252cbd8c-116a-3a68-b612-e50fb21b7145 | -12.0158 | -50.7327 | 2026-09-27 15:00:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 116.0 |
| 416a241f-f212-35e7-b5e4-82f12bd094e4 | -11.7522 | -50.5494 | 2026-09-27 15:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 81.4 |
| c8d95256-d94a-3f6d-bad0-776aa93a0e38 | -15.9869 | -54.9419 | 2026-09-27 15:00:00 | GOES-19 | JACIARA | MATO GROSSO | Brasil | 5104807 | 51 | 33 | nan | nan | nan | Cerrado | 95.9 |
| df56197e-55fa-3ac8-a1fb-763a05ccfb71 | -12.1751 | -50.2851 | 2026-09-27 15:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 91.9 |
| 25f75879-f95b-363b-a012-3b3089ed2ff8 | 1.2978 | -50.8715 | 2026-09-27 15:00:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 73.7 |
| 2774c4b1-b8b3-30bc-8d52-a250236c3410 | -12.6655 | -47.257 | 2026-09-27 15:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 114.9 |
| 69a24638-835d-3da4-9ef4-233c82c4d9f6 | -11.3739 | -43.3972 | 2026-09-27 15:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 184.2 |
| f1b48606-9729-377b-8b22-7c3003a71980 | -11.3547 | -43.4001 | 2026-09-27 15:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 148.9 |
| defbb4d6-7765-3fc2-bfc7-58efe09e038c | -11.9971 | -50.7135 | 2026-09-27 15:00:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 101.0 |
| fc78fdfa-fc8c-3a0d-bd09-a1b4774a0ec1 | -12.9269 | -51.0505 | 2026-09-27 15:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 66.2 |
| 84a1ddf7-ae76-308f-b6ba-a2061f490e97 | -11.81 | -50.4999 | 2026-09-27 15:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 67.1 |
| 8bce0140-8e16-3a46-9498-4c882b0618fe | -12.9461 | -51.0481 | 2026-09-27 15:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 76.0 |
| ca3c95b3-f211-3b49-9f4c-34f8365f6e24 | -12.2911 | -50.1849 | 2026-09-27 15:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 87.1 |
| ac249605-1e4c-3083-b825-97c7df94e354 | -12.1754 | -50.2635 | 2026-09-27 15:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 77.3 |
| d3ad754d-9c82-3277-87c8-9c43e8f59e4f | -12.289 | -50.3143 | 2026-09-27 15:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 84.0 |
| 3411ba80-5233-3f3f-90a7-e677a1bf3bd1 | -12.7868 | -54.0275 | 2026-09-27 15:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 48.2 |
| fbc94ad8-155e-352b-b13f-1013c1975703 | -11.8078 | -50.6499 | 2026-09-27 15:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 70.5 |
| e440321b-661d-3a95-b852-327c12dc710b | -8.4296 | -54.7262 | 2026-09-27 15:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 62.7 |
| b536dd5e-5203-3815-821e-8f770cf4e97c | -17.0529 | -56.59 | 2026-09-27 15:00:00 | GOES-19 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 42.2 |
| ffae2aa2-87bb-3260-9053-ae0138dbaed7 | -12.2723 | -50.1657 | 2026-09-27 15:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 84.4 |
| 41eab1f2-17c1-3e85-acb2-6e820fb5c919 | -14.7289 | -45.576 | 2026-09-27 15:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 98.5 |
| c1d8ad26-018e-3e99-a920-0f47dde0031f | -8.8735 | -49.7328 | 2026-09-27 15:00:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 67.0 |
| a01d5cc5-66f7-31d1-a88c-71fd0dc8fd94 | -12.1747 | -50.3066 | 2026-09-27 15:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 90.4 |
| 565f0268-a755-3e4d-a00f-cdbf66f0171a | -17.5697 | -46.9019 | 2026-09-27 15:00:00 | GOES-19 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 91.5 |
| b1db4cce-93d8-3f62-89ad-3d5538ad3dd7 | -6.8408 | -43.5021 | 2026-09-27 15:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 104.9 |
| 40757bd6-2382-3942-88d6-c5da8f5750ae | -12.6463 | -47.2598 | 2026-09-27 15:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 70.8 |
| 7fd46607-1297-37bd-87f8-0ecf4c65597d | -11.0238 | -54.0148 | 2026-09-27 15:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 81.0 |
| f1ea644e-4dab-364a-b021-409673552faa | -11.9612 | -50.568 | 2026-09-27 15:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 84.0 |
| c2d851b3-0a5c-37b8-a62d-aafbe25ae725 | -8.4483 | -54.725 | 2026-09-27 15:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 83.0 |
| 2d78d365-00bd-3826-9c95-35e298b1a30b | 1.6201 | -55.8641 | 2026-09-27 15:00:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 60.4 |
| f239ef69-0c18-34b0-a5d5-8af347f611b3 | -11.9132 | -49.9721 | 2026-09-27 15:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 66.4 |
| 04998ead-8d32-3715-971e-a82c4d9e714c | -12.1376 | -50.2466 | 2026-09-27 15:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 74.8 |
| e34f5f2d-f4d6-3b8f-a618-798eda5e7bd7 | -12.2643 | -50.682 | 2026-09-27 15:10:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 73.8 |
| 949cd54f-35b2-3a84-a79d-e27ff791732b | -12.1751 | -50.2851 | 2026-09-27 15:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 89.9 |
| c8bc2632-a809-37b8-846b-62a8c5465945 | -12.9269 | -51.0505 | 2026-09-27 15:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 78.4 |
| 2e7f9c80-14f1-3050-8fd7-ea5f3e3e076a | -12.2887 | -50.3358 | 2026-09-27 15:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 68.4 |
| e24592a8-0689-38be-b92a-e9804b7a775f | -11.764 | -51.0386 | 2026-09-27 15:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 53.6 |
| 8c123af3-67f6-39a2-a5a4-5bd10d6d1f80 | -11.0991 | -54.0285 | 2026-09-27 15:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 88.5 |
| b9230aba-35fe-3e53-97b8-b015409b6043 | -1.4116 | -49.0384 | 2026-09-27 15:10:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 79.6 |
| 6d36a157-fec0-3f92-a732-83efb5567982 | -8.6171 | -54.6126 | 2026-09-27 15:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 78.2 |
| 13d2fc09-a47b-3210-8f10-8731c6715e89 | 1.6566 | -55.9424 | 2026-09-27 15:10:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 222.3 |
| 8efdcab4-f02d-33f1-b13d-6de2cab3e254 | -12.6463 | -47.2598 | 2026-09-27 15:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 155.5 |
| ad8b0ff5-be5a-3d3c-9857-3b9a72dd5cf3 | -11.8097 | -50.5214 | 2026-09-27 15:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 68.2 |
| f1bdf5cb-1e2f-3bb1-8638-a4fb812f7e6c | -11.6374 | -50.6053 | 2026-09-27 15:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 83.1 |
| ab61302a-7edf-3359-acf6-970519e411f3 | -11.2284 | -51.3515 | 2026-09-27 15:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 69.2 |
| 076a98e3-a8bb-39d9-8bfb-36e008c2e4a2 | -11.2088 | -51.3958 | 2026-09-27 15:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 66.8 |
| 216ab96f-7dad-3294-888f-382efcef3cdf | -11.6567 | -50.5817 | 2026-09-27 15:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 68.4 |
| 260b5edf-b724-3ef6-a2fc-2fc04d9d8943 | -12.1754 | -50.2635 | 2026-09-27 15:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 74.9 |
| f856f8e3-12e5-3829-80b4-2211d25e1d7a | -12.4351 | -44.1497 | 2026-09-27 15:10:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 142.1 |
| fd36b33d-b646-31d1-96f6-15d274717d97 | -12.9457 | -51.0695 | 2026-09-27 15:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 136.3 |
| 1e73b626-07e9-33d0-ad43-2dbcf5e5fea3 | -12.1188 | -50.2274 | 2026-09-27 15:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 64.6 |
| bd75a2b4-11b8-30de-a546-9e038ac4de6a | -11.9964 | -50.7563 | 2026-09-27 15:10:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 83.8 |
| 57a3da6e-76cc-3378-8b74-bcb4c8027207 | -1.4301 | -49.0382 | 2026-09-27 15:10:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 75.4 |
| 22fe8b7b-d4b8-3257-889a-2350a616bcf0 | -11.6186 | -50.5861 | 2026-09-27 15:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 71.3 |
| cfe1a85c-4e4b-3e57-bcb3-ba534346d1f9 | -10.7157 | -48.7464 | 2026-09-27 15:10:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 63.2 |
| 9f94ba89-9a4e-3607-b506-26e2c08f1fd1 | -11.1183 | -54.0062 | 2026-09-27 15:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 101.5 |
| 67172f0d-0ed6-357b-b7d5-7725114b0d8b | -2.9525 | -57.72 | 2026-09-27 15:10:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 53.6 |
| fe8e5b24-6299-3f0d-b7df-ad6fb376ac82 | -2.9341 | -57.7786 | 2026-09-27 15:10:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 164.5 |
| 246436db-62be-380e-ba4e-f635f7a27fd7 | -12.8059 | -54.0255 | 2026-09-27 15:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 97.7 |
| fe93a854-f4f2-352b-9141-7115c69aac33 | -12.206 | -50.7531 | 2026-09-27 15:10:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 81.5 |
| 5f06d178-c31a-3155-b484-6925d9a76fa9 | -11.6183 | -50.6075 | 2026-09-27 15:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 76.0 |
| 83f42bd4-b2c4-3a5d-9a89-3670b9d6ce72 | -12.9461 | -51.0481 | 2026-09-27 15:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 78.7 |
| 24c0ee6d-5226-3709-adc6-3f7d9b241b25 | -8.5984 | -54.6139 | 2026-09-27 15:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 79.4 |
| b148d5db-f927-35fd-aec1-26692007de6c | -9.7874 | -44.8289 | 2026-09-27 15:10:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 268.9 |
| d4043b70-a5eb-3027-a675-45668a9f09d0 | -12.6608 | -50.9549 | 2026-09-27 15:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 85.2 |
| d02f6a85-abbc-31eb-8fdd-7fce74141701 | -11.7903 | -50.545 | 2026-09-27 15:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 104.3 |
| 1d4018c2-7d16-3705-93d5-219efa128453 | -11.9612 | -50.568 | 2026-09-27 15:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 68.2 |
| cae91bb7-96e3-3ec6-8174-160807fe54f2 | -11.1714 | -50.0151 | 2026-09-27 15:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 87.0 |
| 8d51f9d2-c4c5-34d0-adeb-4350d9de6287 | -10.8051 | -60.745 | 2026-09-27 15:10:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 45.0 |
| e6e73b52-f486-3713-ab10-43386da186af | -17.5697 | -46.9019 | 2026-09-27 15:10:00 | GOES-19 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 77.1 |
| 735c8945-e3f1-374d-ad95-cc3f9960a426 | -11.9132 | -49.9721 | 2026-09-27 15:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 61.0 |
| 4f47c0da-aee1-382d-96bc-f0114d117be0 | -12.6796 | -50.974 | 2026-09-27 15:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 80.9 |
| 98c8d845-ddb0-3a8f-8575-c90ae4a406a3 | -8.5982 | -54.6341 | 2026-09-27 15:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 77.0 |
| b8453edd-ddaa-321c-ac94-2899404a0a75 | -11.2278 | -51.3938 | 2026-09-27 15:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 101.9 |
| 10e44000-056f-3150-8457-e9d8dd621a7e | -11.8094 | -50.5428 | 2026-09-27 15:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 96.9 |
| f1dbb764-4afd-3fb9-852d-b2d18ed6cf0f | -11.6377 | -50.5839 | 2026-09-27 15:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 74.9 |
| ce4b49d5-d878-3b39-aec6-1c15aa3f824a | 1.6015 | -56.0022 | 2026-09-27 15:10:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 80.6 |
| fb876f6d-6f00-39d5-8652-d38460c9937f | -11.9845 | -50.2864 | 2026-09-27 15:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 58.1 |
| df0a0289-fd4b-36cb-b67d-fd22000d2509 | -11.2281 | -51.3727 | 2026-09-27 15:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 112.7 |
| 81da1cd6-a5b2-36d6-80bb-1339eb460fd9 | -11.1924 | -54.1225 | 2026-09-27 15:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 64.6 |
| 08a44ad8-3e30-3b06-8fcc-bb657cd678c9 | -11.9783 | -50.6943 | 2026-09-27 15:10:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 82.5 |
| 7ab5f15d-5f1e-3149-9812-2880c6fcefcc | -11.7313 | -50.68 | 2026-09-27 15:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 57.0 |
| aff84907-b436-373c-9604-7c1b49c90f32 | -10.7624 | -50.8282 | 2026-09-27 15:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 53.2 |
| 95472ad4-d085-331f-a2c6-e1ad957ab0fa | -10.4237 | -53.7809 | 2026-09-27 15:10:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 47.8 |
| d75c4223-6c18-3102-90e0-a77c348e62ec | -12.1553 | -50.3305 | 2026-09-27 15:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 80.0 |
| 818a96d8-b856-31e2-8bf1-e1df603ef3cf | -12.7868 | -54.0275 | 2026-09-27 15:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 46.2 |
| 2f583691-77d4-3ce2-b7cb-a9d5b07a4cde | -11.1524 | -50.0172 | 2026-09-27 15:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 97.1 |
| ac2f2c94-e14a-374d-8182-2dc2e697e833 | -10.2827 | -49.9606 | 2026-09-27 15:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 87.5 |
| 2badcf20-986c-30b8-945c-86124c416507 | 1.6383 | -55.9427 | 2026-09-27 15:10:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 78.3 |
| aa93c1c4-ec85-3c2d-9dee-b4982b3abbf5 | -11.0238 | -54.0148 | 2026-09-27 15:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 76.3 |
| 6d71959a-2a0b-3843-93b9-eb1b75696f7d | 1.8876 | -50.6541 | 2026-09-27 15:10:00 | GOES-19 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 85.8 |
| 4fd07223-dd74-35ac-ac17-7102ae21ef2e | -12.7032 | -47.2964 | 2026-09-27 15:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 91.6 |
| 578c777e-198f-39e8-9a9b-f14d17e80978 | -8.39 | -44.16 | 2026-09-27 15:15:00 | MSG-03 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| d503b369-e9ba-3181-8ebb-8e0b4f8cd5fa | -8.36 | -44.16 | 2026-09-27 15:15:00 | MSG-03 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 566f5f51-a758-34d3-b528-72aa7cd45499 | -11.04 | -54.01 | 2026-09-27 15:15:00 | MSG-03 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4ee6b3c8-7b99-3399-97d5-bcc3abcca653 | -11.91 | -50.49 | 2026-09-27 15:15:00 | MSG-03 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 77317b79-27f6-3b17-8d6f-d127d7e1614c | -6.67 | -45.6 | 2026-09-27 15:15:00 | MSG-03 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0804d73d-8834-3a50-8e81-0d422b12a699 | -10.02 | -50.14 | 2026-09-27 15:15:00 | MSG-03 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 21dd7e47-0163-33f7-a1eb-42ec7addd3e1 | -11.01 | -54.0 | 2026-09-27 15:15:00 | MSG-03 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README63.md)
