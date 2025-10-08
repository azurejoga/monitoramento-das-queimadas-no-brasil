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

## Dados Diários - Página 102

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ed634ade-ee5c-3415-a80e-f247c7df821b | -11.1833 | -54.8787 | 2025-10-08 12:50:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 316.5 |
| 8053a9d0-f3fa-3bad-8aba-8c0746f21771 | -13.2662 | -48.0409 | 2025-10-08 12:50:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 61.8 |
| 798dcb28-c7e3-3304-a1de-50ba6e23be7a | -11.7275 | -50.9363 | 2025-10-08 12:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 119.1 |
| 22633870-714f-30c9-95c3-0b3edf1a7387 | -15.1311 | -52.7656 | 2025-10-08 12:50:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 74.6 |
| 1219857c-67bd-3568-80c3-bc9aefffdf8e | -13.8117 | -45.7826 | 2025-10-08 12:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 173.8 |
| e130a982-fe38-396b-b79b-72f7a2076ad8 | -8.8531 | -46.7674 | 2025-10-08 12:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 112.9 |
| 94c42ec4-081f-3c40-88ee-2eabf2858576 | -13.2855 | -48.0381 | 2025-10-08 12:50:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 94.1 |
| d4d7e0ad-71c4-3f7f-8486-71f8eb919fb9 | -11.1457 | -54.8617 | 2025-10-08 12:50:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 82.4 |
| 429d20ad-448e-3c96-b290-a7e4a7f13b1b | -11.7466 | -50.9342 | 2025-10-08 12:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 103.8 |
| f46e3c79-be1c-392f-8b82-26c9439ede38 | -9.0016 | -45.5148 | 2025-10-08 12:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 68.5 |
| b505cded-cadc-3181-9705-df7fc75dca03 | -13.3517 | -47.5818 | 2025-10-08 12:50:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 60.5 |
| e07fbf3c-e799-356a-88ac-3ecc5f355d4c | -11.183 | -54.8991 | 2025-10-08 12:50:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 389.6 |
| f1b71826-42e9-3c0d-a166-d8d19169180e | -8.4824 | -46.2912 | 2025-10-08 12:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 74.3 |
| b3a27b8a-adcf-34fc-91ee-c1bad4e98360 | -13.3967 | -47.2382 | 2025-10-08 12:50:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 60.4 |
| 024b0541-4c6c-30b2-b96d-3e3a456b529c | -14.7174 | -46.1098 | 2025-10-08 12:50:00 | GOES-19 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 126.4 |
| 81e58e17-bd4e-3fb0-a3bd-7a2357b0ef13 | -13.8112 | -45.8057 | 2025-10-08 12:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 107.5 |
| 0fa538d4-e810-3c6e-bc50-6c571842e68c | -13.3513 | -47.6042 | 2025-10-08 12:50:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 137.3 |
| ce24277d-42df-39e8-b3d5-1c5e841f9816 | -14.7184 | -46.0636 | 2025-10-08 12:50:00 | GOES-19 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 150.4 |
| 4c400467-0ffe-372a-a612-17469a45f719 | -9.3343 | -48.9364 | 2025-10-08 12:50:00 | GOES-19 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 133.9 |
| 87ba4517-a21a-33ea-b75c-ca2e8b04c36d | -9.2096 | -46.9084 | 2025-10-08 12:50:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 51.1 |
| e6e8c3e4-8c7e-3ad7-9e86-5a791da391c5 | -15.6393 | -52.5688 | 2025-10-08 12:50:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 91.9 |
| 985bc1ca-9d03-3942-a749-33b674d071da | -8.9309 | -46.5809 | 2025-10-08 12:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 83.5 |
| e376575d-f973-3d40-8649-30466141f505 | -8.872 | -46.7655 | 2025-10-08 12:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 100.2 |
| 392be8f3-4298-32d3-9263-3a7e50dd3af7 | -8.6295 | -45.1 | 2025-10-08 12:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 137.8 |
| d707d820-15fb-36bc-b556-aac927daa78b | -10.1871 | -46.0116 | 2025-10-08 13:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 69.2 |
| c47312c9-727c-38d8-92c9-0120397f6790 | -12.4916 | -54.7364 | 2025-10-08 13:00:00 | GOES-19 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 102.6 |
| 50223165-3c5e-33f2-b9a6-206ae5e87d9c | -10.4245 | -45.3907 | 2025-10-08 13:00:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 652.5 |
| 4567a473-2ae9-32bd-949e-89b1be78794f | -8.2449 | -44.1991 | 2025-10-08 13:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 115.6 |
| 3d61e8af-ea66-38f4-a65f-74630b3c8b76 | -12.5107 | -54.7345 | 2025-10-08 13:00:00 | GOES-19 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 133.7 |
| 265bb74f-b055-310c-affa-633997c8b6c6 | -12.0314 | -45.1901 | 2025-10-08 13:00:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 140.5 |
| a2e9c950-d76f-3d05-9a50-114e38e91167 | -8.8618 | -46.0949 | 2025-10-08 13:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 91.9 |
| ca1e618f-b367-3edd-99eb-9c33b18f37c3 | -12.1274 | -50.9118 | 2025-10-08 13:00:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 86.9 |
| 7279635b-7ba3-3a89-8309-666b6e3ee972 | -8.2452 | -44.176 | 2025-10-08 13:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 96.8 |
| ea571a31-a024-3534-a6bf-9985ba3bcaff | -8.9118 | -46.6052 | 2025-10-08 13:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 55.5 |
| ad536a10-8940-3280-bb28-3b6a0345a139 | -8.6295 | -45.1 | 2025-10-08 13:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 145.2 |
| 9913e2e7-18f2-396c-9277-44f3aa5a15ff | -8.4636 | -46.2931 | 2025-10-08 13:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 73.0 |
| c4b2d35b-8c54-3cd1-a614-0645607b5175 | -13.2438 | -47.1714 | 2025-10-08 13:00:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 73.8 |
| cf4d1a3d-c1a4-3fc8-a158-2cf0a3b9bb6f | -8.691 | -44.727 | 2025-10-08 13:00:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 140.7 |
| fe1d1aef-d957-3819-8571-d9ca486c1abb | -8.9306 | -46.6033 | 2025-10-08 13:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 86.2 |
| 25b6d961-cd50-3a03-b949-f1de30ae0963 | -13.3517 | -47.5818 | 2025-10-08 13:00:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 52.3 |
| 57324fc1-8225-3e51-b2f5-60d26c292650 | -14.7174 | -46.1098 | 2025-10-08 13:00:00 | GOES-19 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 133.0 |
| 731c427c-c23d-38ba-b742-ef3cfe030ecb | -11.1646 | -54.86 | 2025-10-08 13:00:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 103.7 |
| 9f093a9f-3443-3abb-acea-4188a6017dc0 | -15.6393 | -52.5688 | 2025-10-08 13:00:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 111.5 |
| a3d729b1-239d-3e3f-9ac1-0bce30f26238 | -8.1807 | -43.321 | 2025-10-08 13:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 114.5 |
| f77cdd17-38e5-3bce-8e8c-46dd5c0c3081 | -14.7184 | -46.0636 | 2025-10-08 13:00:00 | GOES-19 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 171.1 |
| 2e72811a-8d71-3ea5-98ad-964e6199481e | -12.2525 | -47.8728 | 2025-10-08 13:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 69.6 |
| 05d7f8e6-232b-3682-ba75-ef1013cb33cd | -12.5297 | -54.7326 | 2025-10-08 13:00:00 | GOES-19 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 112.1 |
| 8c3d8df8-b8e0-3f0b-8657-f102aec78675 | -11.183 | -54.8991 | 2025-10-08 13:00:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 483.7 |
| 58482fda-48de-31d3-858b-ea041f6f4e96 | -14.7179 | -46.0867 | 2025-10-08 13:00:00 | GOES-19 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 296.2 |
| 11bfc4e5-00b9-36b7-983d-7889c768a6ae | -14.4079 | -46.026 | 2025-10-08 13:00:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 83.1 |
| 41f010ff-07c4-3e03-aae1-cc117ea46fe6 | -13.7368 | -45.6569 | 2025-10-08 13:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 87.4 |
| 4a20bd4e-0fd5-39a7-9087-c20b64f33c89 | -8.5398 | -46.2181 | 2025-10-08 13:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 95.7 |
| 0bd96bac-6f44-3df0-8ccd-236483739b71 | -13.2434 | -47.194 | 2025-10-08 13:00:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 101.9 |
| f35a3d18-79c5-3dd7-b4e6-63d420d894a8 | -9.3343 | -48.9364 | 2025-10-08 13:00:00 | GOES-19 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 98.2 |
| ed924ff5-8d3f-3a9b-8842-64b532dda114 | -14.3884 | -46.0294 | 2025-10-08 13:00:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 98.4 |
| e63baf1a-3de8-359c-8af0-da14257346e1 | -12.4262 | -45.6366 | 2025-10-08 13:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 231.5 |
| 58111f99-690a-371c-ba24-7f9a9c768401 | -8.1804 | -43.3445 | 2025-10-08 13:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 141.3 |
| 6819e1bd-7050-3143-9e11-a19c2972551d | -12.0122 | -45.1929 | 2025-10-08 13:00:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 277.4 |
| d6680f97-3ea0-328c-9f2c-27bac0ec59fe | -13.2855 | -48.0381 | 2025-10-08 13:00:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 67.0 |
| 68e12833-d32f-380e-bfa4-259f8682caff | -12.5109 | -54.714 | 2025-10-08 13:00:00 | GOES-19 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 102.6 |
| bc59411d-dcd1-3468-91f5-95bd2fd36a0c | -10.8732 | -47.0953 | 2025-10-08 13:00:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 95.9 |
| 681153ed-78d1-3fe5-8770-54b1d600d31f | -12.0118 | -45.2161 | 2025-10-08 13:00:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 87.7 |
| 3ca902e0-fbe6-3735-a6e6-c0ceb7cca60e | -11.1266 | -54.8837 | 2025-10-08 13:00:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 111.5 |
| 77a9517f-0d91-34d5-b992-911a6f440568 | -13.3513 | -47.6042 | 2025-10-08 13:00:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 93.3 |
| 58454c3e-300b-3ba9-b82f-0766b68fe30b | -12.1576 | -51.4399 | 2025-10-08 13:00:00 | GOES-19 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Cerrado | 67.6 |
| d2b76d1c-92f1-36d4-b80f-9117839530ee | -13.7359 | -45.7031 | 2025-10-08 13:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 114.2 |
| fb1083f1-78ac-3e1a-be6c-5480df24acd8 | -14.211 | -43.4573 | 2025-10-08 13:00:00 | GOES-19 | IUIU | BAHIA | Brasil | 2917334 | 29 | 33 | nan | nan | nan | Cerrado | 125.4 |
| abf41072-30a4-31f5-9f89-f813ce599aa0 | -18.4125 | -45.2155 | 2025-10-08 13:00:00 | GOES-19 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 88.7 |
| 93c9bda3-6e67-3679-b0d8-0ee2f421e1cf | -11.1833 | -54.8787 | 2025-10-08 13:00:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 370.4 |
| 0b81fea9-53c2-3eb9-836f-aa0426bcb372 | -8.1993 | -43.3424 | 2025-10-08 13:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 155.0 |
| 6e037822-4957-37ca-bb12-98ee3c2c33b8 | -10.1874 | -45.9889 | 2025-10-08 13:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 101.9 |
| ba4a929e-32a6-3f28-8fe8-35c6fd78060b | -13.8117 | -45.7826 | 2025-10-08 13:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 146.4 |
| 2b9dafd4-6b00-303d-a7a7-ccce20a3b5b6 | -11.1457 | -54.8617 | 2025-10-08 13:00:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 78.6 |
| 564a2469-1b58-34eb-8ba7-fabf914eaedf | -15.6198 | -52.5715 | 2025-10-08 13:00:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 111.2 |
| 8dbe5d0f-1ef8-3da4-b7b6-76913f0c9459 | -17.5828 | -47.1762 | 2025-10-08 13:00:00 | GOES-19 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 105.3 |
| e71444a4-86c9-3378-9e89-1202af64c025 | -8.9121 | -46.5829 | 2025-10-08 13:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 101.7 |
| c09ff93b-de28-3860-b8cf-3d068ed0cbd6 | -10.9106 | -47.1353 | 2025-10-08 13:00:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 56.4 |
| 43c8d01e-95cf-3e18-9e2f-b1598e590136 | -14.3889 | -46.0063 | 2025-10-08 13:00:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 180.4 |
| 7642dfe9-c5aa-3475-af31-8e291d895d8e | -12.4267 | -45.6136 | 2025-10-08 13:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 219.9 |
| c807fbb4-eb99-306b-b44f-d398f174fdf0 | -15.1311 | -52.7656 | 2025-10-08 13:00:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 76.4 |
| 190dd13a-5db3-3aab-a43b-7717345fd386 | -17.954 | -44.4124 | 2025-10-08 13:00:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 91.6 |
| fee3dc33-d830-3019-afac-5b5dceb72065 | -10.4251 | -46.591 | 2025-10-08 13:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 99.1 |
| 01183c31-06c1-3d37-be4f-738155522768 | -13.8112 | -45.8057 | 2025-10-08 13:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 67.7 |
| a61db7e4-949d-3964-93f0-803715ae848b | -8.9309 | -46.5809 | 2025-10-08 13:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 189.9 |
| 87ea4302-77f3-3908-ba30-72c864fe2afe | -9.2096 | -46.9084 | 2025-10-08 13:00:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 52.9 |
| ea217a51-1bd9-355d-8604-db2a13c6eb1d | -8.8621 | -46.0724 | 2025-10-08 13:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 101.6 |
| e3618733-9af2-3084-bec6-5194dbf7fc55 | -8.2452 | -44.176 | 2025-10-08 13:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 137.3 |
| d30c4bbc-d4ed-3be2-98e5-49809f26dd13 | -15.7696 | -46.2401 | 2025-10-08 13:10:00 | GOES-19 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 84.7 |
| 498a7571-bc60-374c-82f9-fee9fa1b5118 | -12.5107 | -54.7345 | 2025-10-08 13:10:00 | GOES-19 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 137.9 |
| a5901333-4787-399f-befa-78c480551c5d | -8.226 | -44.2012 | 2025-10-08 13:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 288.2 |
| 3fc5d568-bcc7-3f51-b4fa-479fc1ac10d6 | -14.4079 | -46.026 | 2025-10-08 13:10:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 88.7 |
| b85b1616-24a1-38f6-8627-fb9ad045b2d9 | -8.6295 | -45.1 | 2025-10-08 13:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 407.9 |
| 8aac089a-3496-3bb7-ab47-32b4007f0d73 | -13.2855 | -48.0381 | 2025-10-08 13:10:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 95.2 |
| e446d7f3-6cce-30e6-803a-bd7e2a0705b6 | -12.5109 | -54.714 | 2025-10-08 13:10:00 | GOES-19 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 122.9 |
| 2f9cdcd8-1004-3832-b809-151a38c5d6e6 | -8.9306 | -46.6033 | 2025-10-08 13:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 55.3 |
| c716c7e5-3803-3ea1-b5e6-3491a7666719 | -9.3343 | -48.9364 | 2025-10-08 13:10:00 | GOES-19 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 110.2 |
| 107b7b98-db8a-3a58-9588-2955d63d4b07 | -13.3513 | -47.6042 | 2025-10-08 13:10:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 92.1 |
| 6526e8c1-671a-3bbe-ad57-8056b74bba02 | -12.4916 | -54.7364 | 2025-10-08 13:10:00 | GOES-19 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 77.3 |
| 826902e3-1499-344c-be77-ade193bf4d5e | -8.2071 | -44.2032 | 2025-10-08 13:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 151.3 |
| ccd9b8ef-1282-34df-b768-027941044744 | -8.9121 | -46.5829 | 2025-10-08 13:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 70.3 |


[Clique aqui para ver as próximas entradas](README103.md)
