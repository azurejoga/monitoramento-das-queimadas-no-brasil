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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 865b0618-a051-31f6-bc16-3c7db513769d | -10.5511 | -47.0456 | 2026-06-16 14:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 89.6 |
| 4a3bdde8-1602-391d-844f-f75d139d8040 | -8.9449 | -46.9582 | 2026-06-16 14:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 114.3 |
| a60dd211-4f6f-3e48-8830-245a88586d88 | -6.9793 | -42.8798 | 2026-06-16 14:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 91.7 |
| f7cc5fec-1c88-31af-8bb9-782f837e6b51 | -10.7777 | -54.0983 | 2026-06-16 14:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 61.3 |
| a32e1d3e-ba9f-3c6c-ac2c-ca259db5b57a | -12.9175 | -54.2202 | 2026-06-16 14:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 56.6 |
| 4ba0cf29-7240-3e05-88a0-834a4b4bbd8f | -8.9641 | -46.934 | 2026-06-16 14:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 80.1 |
| b294da2f-de78-3555-acdf-91f90b9c5067 | -10.7024 | -49.6797 | 2026-06-16 14:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 55.5 |
| b6a2f779-8c5f-3a3d-b94a-c6adaa4f4674 | -11.5933 | -55.33 | 2026-06-16 14:30:00 | GOES-19 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 60.5 |
| 6d9ce2e0-0753-3794-aefe-57b7947d8473 | -10.7777 | -54.0983 | 2026-06-16 14:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 60.2 |
| 34cb37f2-30c5-34d7-91e9-35315299b3d1 | -10.5511 | -47.0456 | 2026-06-16 14:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 87.9 |
| aa7c4871-f7e3-3a5e-b6f4-c021429b8da6 | -8.9641 | -46.934 | 2026-06-16 14:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 87.1 |
| 83045a18-27f0-3ed0-be42-9ab24d9b58b1 | -10.7024 | -49.6797 | 2026-06-16 14:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 56.1 |
| 9d5a609d-cbf6-35f7-933e-cb9871bd4307 | -7.7724 | -47.5773 | 2026-06-16 14:40:00 | GOES-19 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 82.4 |
| 6ba005fe-5473-3563-ab1e-982d3b70fd83 | -12.5557 | -57.1998 | 2026-06-16 14:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 59.4 |
| 0286b7d6-9768-3e9b-8f84-092825a1f46b | -12.9366 | -54.2182 | 2026-06-16 14:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 74.8 |
| da1e482c-cda8-3150-8520-aaed5228ab3d | -11.5933 | -55.33 | 2026-06-16 14:40:00 | GOES-19 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 74.2 |
| c8904d33-3c54-30fb-87ea-403a4a9b92e2 | -8.8695 | -46.966 | 2026-06-16 14:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 130.4 |
| 7aec5602-7f51-385a-8b5d-eff6229d3290 | -12.9175 | -54.2202 | 2026-06-16 14:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 74.8 |
| 7574f733-9062-39b1-a979-b773fa4ea0de | -8.9446 | -46.9805 | 2026-06-16 14:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 220.2 |
| 9ca59c5a-7a7e-3ffd-adf1-58ca5487b11f | -8.9641 | -46.934 | 2026-06-16 14:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 89.1 |
| bc861d58-9e3f-30ac-960c-be3a0589b850 | -8.9449 | -46.9582 | 2026-06-16 14:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 188.5 |
| e67f88fe-2eef-325f-8e93-2afe63865719 | -12.9175 | -54.2202 | 2026-06-16 14:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 95.9 |
| 804ea3f1-fa84-3855-bdaa-356804cc8834 | -11.5933 | -55.33 | 2026-06-16 14:50:00 | GOES-19 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 64.2 |
| 6f39b2c0-6b04-3181-91ec-31baf49237c1 | -10.7777 | -54.0983 | 2026-06-16 14:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 58.0 |
| e12d4033-84bf-3395-9b1a-1374328c9150 | -8.9638 | -46.9563 | 2026-06-16 14:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 335.2 |
| b1103282-d950-3961-9f22-d721b0cce0d3 | -12.9366 | -54.2182 | 2026-06-16 14:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 72.5 |
| 04c3310e-4258-394a-a1da-0aef9b72811f | -6.1754 | -48.5045 | 2026-06-16 14:50:00 | GOES-19 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 63.7 |
| 33ceb8f8-c99f-3044-8930-cf3d63ebb95f | -12.9366 | -54.2182 | 2026-06-16 15:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 61.2 |
| 8c0db892-d4c7-3fab-b52f-3df1a9c6a77d | -7.7724 | -47.5773 | 2026-06-16 15:00:00 | GOES-19 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 69.6 |
| 15d3bcd9-9909-3705-88de-5b47c6c38027 | -10.7777 | -54.0983 | 2026-06-16 15:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 64.4 |
| 06bc720a-3052-3ec6-8fa8-2dd168c50bff | -10.5511 | -47.0456 | 2026-06-16 15:00:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 89.4 |
| 0f7f3d83-1070-3b45-acfb-226ce268b36c | -8.9446 | -46.9805 | 2026-06-16 15:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 175.4 |
| b9a7e625-ab45-3812-a71c-4c40ea271ec2 | -8.9638 | -46.9563 | 2026-06-16 15:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 289.1 |
| e8ef0913-6b7d-3081-b3a4-30b12cff8a63 | -11.5933 | -55.33 | 2026-06-16 15:00:00 | GOES-19 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 61.1 |
| 119a9fbc-59e3-3578-a0ac-57ea1a8461e7 | -8.9449 | -46.9582 | 2026-06-16 15:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 165.4 |
| 21caa05b-293b-350a-984d-de379171271a | -8.8695 | -46.966 | 2026-06-16 15:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 73.9 |
| 12c49f9f-2880-397e-9b4a-f51799772a2b | -8.9641 | -46.934 | 2026-06-16 15:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 94.0 |
| 9df0ee05-8750-339c-a66e-820336291225 | -11.5933 | -55.33 | 2026-06-16 15:10:00 | GOES-19 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 65.0 |
| e92ac18e-ca6e-325f-8fce-9352c970ade0 | -12.9366 | -54.2182 | 2026-06-16 15:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 91.8 |
| e78906b5-79f2-3049-913c-537bfb21fd61 | -8.8695 | -46.966 | 2026-06-16 15:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 146.4 |
| 348f5cc2-595e-3832-aa12-e1b133c6bf16 | -7.7724 | -47.5773 | 2026-06-16 15:10:00 | GOES-19 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 59.1 |
| 8e89e073-243d-3a40-8074-85923298b75e | -10.5511 | -47.0456 | 2026-06-16 15:10:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 86.4 |
| 13cef419-200c-3907-871e-18350d4d7df9 | -12.9366 | -54.2182 | 2026-06-16 15:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 144.9 |
| 7067dddf-06fb-3aa7-9665-9918d00ae8ce | -11.5933 | -55.33 | 2026-06-16 15:20:00 | GOES-19 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 73.1 |
| d9756cd2-1100-3a3f-bff6-6187518054b0 | -7.7724 | -47.5773 | 2026-06-16 15:20:00 | GOES-19 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 59.0 |
| 7fea3935-fed9-3af3-8267-86a94e4bc691 | -8.8222 | -44.8043 | 2026-06-16 15:20:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 73.1 |
| 3080d9b8-7758-314a-a2f9-0528deeb9090 | -10.7024 | -49.6797 | 2026-06-16 15:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 54.9 |
| 96407aab-cd70-3db8-88d4-46f4c0ebf703 | -10.5511 | -47.0456 | 2026-06-16 15:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 146.7 |
| 71bab094-5649-3141-93c3-c4361c0c107b | -8.8695 | -46.966 | 2026-06-16 15:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 153.1 |
| d0fe7348-c90f-36cb-bbff-fe989f3f9229 | -9.3662 | -46.4895 | 2026-06-16 15:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 74.3 |
| 62140f66-4650-3cd2-b96c-ac6abe60babb | -8.8222 | -44.8043 | 2026-06-16 15:30:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 73.8 |
| e0ae4131-6c15-33d1-b11f-73f66f25496b | -8.9641 | -46.934 | 2026-06-16 15:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 135.0 |
| 5120b8cb-7085-3fa1-b180-4b35a6a1c9a9 | -11.5933 | -55.33 | 2026-06-16 15:30:00 | GOES-19 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 83.6 |
| 732e0b28-0785-3639-bbac-28ec3b66ead8 | -8.8695 | -46.966 | 2026-06-16 15:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 212.9 |
| f5306e46-8e59-3957-8e57-747b150f4c61 | -8.9449 | -46.9582 | 2026-06-16 15:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 137.9 |
| 19d18cf9-823f-3dca-873e-68dd827a1d0f | -7.7724 | -47.5773 | 2026-06-16 15:30:00 | GOES-19 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 57.0 |
| 5424e092-0fe2-3406-970d-728bb4cbc416 | -8.9446 | -46.9805 | 2026-06-16 15:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 108.0 |
| a82e72c5-fa51-3286-a110-1c0f2f9e707a | -12.9366 | -54.2182 | 2026-06-16 15:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 166.1 |
| 66fe8c08-0162-3353-aa90-3dab19a02739 | -8.9638 | -46.9563 | 2026-06-16 15:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 312.5 |
| 63e32fc6-f2ed-3de3-88bc-dc8c1f03ab10 | -10.5514 | -47.0233 | 2026-06-16 15:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 84.3 |
| 28f83013-2501-3c00-9b4f-a77c21bbceaf | -8.8222 | -44.8043 | 2026-06-16 15:40:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 92.3 |
| e7086e4a-f573-38a2-8c39-50cf03b2441f | -12.9366 | -54.2182 | 2026-06-16 15:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 89.2 |
| 58dfb97b-6c0d-30fe-bd3a-575ae6c3e4bd | -8.8695 | -46.966 | 2026-06-16 15:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 187.3 |
| a6965562-09c5-323f-8b95-a745974a4bf5 | -8.8695 | -46.966 | 2026-06-16 15:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 240.7 |
| aa83bd39-a44c-3251-b8fb-ce882642e44e | -8.8222 | -44.8043 | 2026-06-16 15:50:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 91.0 |
| 2a83d044-b773-3217-936a-6e78fce6b410 | -12.9366 | -54.2182 | 2026-06-16 15:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 49.3 |
| a2deaefa-9833-39d5-a740-3e43b7a519b1 | -8.8695 | -46.966 | 2026-06-16 16:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 68.6 |
| d6fbc637-0735-3af2-a920-487e3a349c34 | -8.8222 | -44.8043 | 2026-06-16 16:00:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 101.8 |
| 7bed2f54-9f3e-3810-8d6c-2e69b4469650 | -10.5511 | -47.0456 | 2026-06-16 16:00:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 100.8 |
| 5eab44c9-0d56-32c7-9af1-c3ff21699da5 | -8.9641 | -46.934 | 2026-06-16 16:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 104.0 |
| 8b396a4f-04c9-3ebf-ad68-232f57bfb421 | -12.1114 | -51.9944 | 2026-06-16 16:10:00 | GOES-19 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 49.8 |
| 09fd05ff-0191-3a16-ac50-c5d440d454f4 | -8.9446 | -46.9805 | 2026-06-16 16:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 155.9 |
| ff93b47a-75ca-3a50-a893-bee35a5a3583 | -8.9449 | -46.9582 | 2026-06-16 16:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 152.1 |
| 4613cac4-703e-3db2-818e-1da967203787 | -8.9452 | -46.936 | 2026-06-16 16:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 91.1 |
| 7147f1d4-07a7-3843-a843-6ef9c183ac19 | -8.8695 | -46.966 | 2026-06-16 16:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 204.0 |
| c145896e-4ab2-3252-86a9-a9a5bfa9ff04 | -8.9641 | -46.934 | 2026-06-16 16:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 147.5 |
| 4952227a-3bfc-3187-a6eb-a8b1752c506f | -8.8695 | -46.966 | 2026-06-16 16:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 160.8 |
| 3508d4db-0ff2-3291-86af-85333fff1d24 | -12.9366 | -54.2182 | 2026-06-16 16:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 142.0 |
| cbed3094-22db-3589-9161-f49364f84f64 | -8.8222 | -44.8043 | 2026-06-16 16:20:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 68.4 |
| 3e49fb97-b538-3a9c-ab0c-02dacd47a951 | -8.9449 | -46.9582 | 2026-06-16 16:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 129.4 |
| 3bb71e8b-aaa8-35ce-a040-55da18d943f6 | -11.3606 | -51.3797 | 2026-06-16 16:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 52.1 |
| fa12549b-af24-3b2d-bf9e-bb923ca746bb | -10.5511 | -47.0456 | 2026-06-16 16:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 120.0 |
| 55dca096-a785-3fb5-807e-14358bac8a19 | -8.9638 | -46.9563 | 2026-06-16 16:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 274.7 |
| 6158a6a4-ca64-3f68-92ef-cebf9b30394f | -11.5933 | -55.33 | 2026-06-16 16:30:00 | GOES-19 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 60.8 |
| 5e28eece-bfc3-3afd-b9ec-94d869d4c372 | -8.8222 | -44.8043 | 2026-06-16 16:30:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 81.1 |
| 52dfe905-1ef2-3f2e-9201-e5a43681aac5 | -8.9641 | -46.934 | 2026-06-16 16:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 105.5 |
| 3c72b5e8-30b8-305f-b2b5-62c5d9d029ac | -12.1114 | -51.9944 | 2026-06-16 16:30:00 | GOES-19 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 53.1 |
| 26294274-ce0d-34e5-b5e4-fc12a8a79b95 | -8.9449 | -46.9582 | 2026-06-16 16:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 113.5 |
| ebe5faf5-3430-35dc-9a81-e4edcf752682 | -8.8695 | -46.966 | 2026-06-16 16:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 103.9 |
| e0e133cd-dd6e-3aee-9abd-069a02d7690e | -11.3606 | -51.3797 | 2026-06-16 16:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 55.3 |
| 775d9cf5-876b-3f8d-b672-744c4b41ca07 | -8.9638 | -46.9563 | 2026-06-16 16:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 211.5 |
| 2f8ec93f-401b-3094-b08c-3006a6163ac9 | -8.9641 | -46.934 | 2026-06-16 16:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 109.3 |
| 5b7a1a76-fff5-3cba-bd66-ea0bd22b3b2a | -12.1114 | -51.9944 | 2026-06-16 16:40:00 | GOES-19 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 62.9 |
| fc213764-7832-3dd8-99d0-d1fe057b6e10 | -8.8695 | -46.966 | 2026-06-16 16:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 134.0 |
| 011e2f21-c6a8-31b4-a5cf-c476060275b8 | -8.9449 | -46.9582 | 2026-06-16 16:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 136.6 |
| 1208d0f7-bd63-39aa-a06f-32b032ff105f | -6.1752 | -48.5261 | 2026-06-16 16:40:00 | GOES-19 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 66.4 |
| f7e5272c-c5f7-37f3-892f-4ecb9d0a21f3 | -8.9452 | -46.936 | 2026-06-16 16:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 79.2 |
| aeb7922f-f475-3c42-9bb1-9b36386415d3 | -10.5514 | -47.0233 | 2026-06-16 16:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 81.6 |
| e9accbfc-c8b1-3798-a9c1-01d2a52770f2 | -12.0923 | -51.9966 | 2026-06-16 16:40:00 | GOES-19 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 49.0 |
| 876effdb-17de-337c-a9cd-f58f9115de74 | -12.9366 | -54.2182 | 2026-06-16 16:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 72.4 |


[Clique aqui para ver as próximas entradas](README17.md)
