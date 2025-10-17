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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a027a1b1-f178-302e-83d3-bda15aad838f | -10.5831 | -47.4423 | 2025-10-17 00:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 69.4 |
| 60064fd0-f71d-333a-9d72-6431d964c83f | -14.303 | -51.4715 | 2025-10-17 00:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 58.0 |
| 4b45d2a0-79b8-3007-b137-c7ff2543adea | -4.9548 | -44.956 | 2025-10-17 00:30:00 | GOES-19 | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | 150.8 |
| bad5f631-5943-30be-bb6d-f3c468c3567f | -10.5834 | -47.42 | 2025-10-17 00:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 158.3 |
| e3e285de-62fd-3a45-93a8-3f454f9a0208 | -10.2939 | -44.0221 | 2025-10-17 00:30:00 | GOES-19 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 157.5 |
| 921d192c-701c-35d9-b244-28498a90d202 | -4.4246 | -43.4038 | 2025-10-17 00:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 318.0 |
| 0f703abf-b5a1-3f2b-84cd-6dea9d2bc2c6 | -18.0898 | -42.4475 | 2025-10-17 00:30:00 | GOES-19 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 72.6 |
| 3a6c21ab-fdcb-368d-a802-09ae3d46ce10 | -9.7302 | -48.9183 | 2025-10-17 00:30:00 | GOES-19 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 67.6 |
| 08e85198-94d3-3552-b38d-e92bb6a18763 | -4.3874 | -43.3827 | 2025-10-17 00:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 90.0 |
| 285a4f26-5785-3ad0-bac2-259909faacb7 | -10.4945 | -43.4079 | 2025-10-17 00:30:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 40.0 |
| bf289af5-fed8-3a37-8bfe-5d17408c0b73 | -3.2359 | -45.9862 | 2025-10-17 00:30:00 | GOES-19 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 221.8 |
| 57eec366-d0e1-3ac9-af87-f635e402abc9 | -2.7585 | -49.3922 | 2025-10-17 00:30:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 56.9 |
| ce1a65b4-b45d-3fef-b699-61be251dd23f | -11.4748 | -44.1819 | 2025-10-17 00:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 96.5 |
| f6fd4dbc-862a-3437-b694-f5b2b2a65664 | -9.0821 | -48.0252 | 2025-10-17 00:30:00 | GOES-19 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 80.3 |
| ffdf02ef-4e03-37ef-a087-d80d156c3b0a | -3.236 | -45.9639 | 2025-10-17 00:40:00 | GOES-19 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 312.1 |
| 8b7db1a6-25b9-3f57-a6fb-195a6b0c399c | -10.2745 | -44.0481 | 2025-10-17 00:40:00 | GOES-19 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 133.7 |
| c611e4fd-8d94-3083-91af-5a93c6614fb4 | -10.5132 | -43.4289 | 2025-10-17 00:40:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 69.8 |
| 2ef44593-235e-30ba-ac03-20d2c6c5556b | -4.4059 | -43.4049 | 2025-10-17 00:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 608.3 |
| a3ebcaed-328a-3db0-ae89-240950b06c64 | -7.9442 | -44.115 | 2025-10-17 00:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 65.4 |
| 499df9f7-d64b-3d6a-97dc-f41af0c4baf9 | -11.4748 | -44.1819 | 2025-10-17 00:40:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 110.9 |
| d9549ccd-18c4-34ed-9edc-15ec58d2200f | -11.5917 | -44.0707 | 2025-10-17 00:40:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 169.3 |
| c685be00-7ebe-3c5b-9018-7c4d7eb6c716 | -4.3871 | -43.4292 | 2025-10-17 00:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 100.9 |
| 568cc1e4-9aa7-37a6-8a73-f17f2e2acfa5 | -3.2545 | -45.9855 | 2025-10-17 00:40:00 | GOES-19 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 108.3 |
| 8e2286b2-a201-3417-9521-7eecbd51e9b6 | -4.4246 | -43.4038 | 2025-10-17 00:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 297.9 |
| c11fd303-8c66-304c-98e2-f52bba8fb8b5 | -11.5729 | -44.0501 | 2025-10-17 00:40:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 79.7 |
| 0afe5cb8-6d8f-308e-83ef-e067ad9893cc | -11.5921 | -44.0472 | 2025-10-17 00:40:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 103.7 |
| bc2a317e-ccfe-3e4d-93d7-e10bf5a27518 | -16.0125 | -43.4996 | 2025-10-17 00:40:00 | GOES-19 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 83.3 |
| 25755949-2eb6-3517-b116-7baefff9fc46 | -9.0821 | -48.0252 | 2025-10-17 00:40:00 | GOES-19 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 98.7 |
| 3cdce095-5bb9-3cd5-a1d0-50845d541d05 | -9.1378 | -46.6261 | 2025-10-17 00:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 63.0 |
| 4a945a4b-77c9-399b-afd4-9216281930c5 | -3.5028 | -52.4938 | 2025-10-17 00:40:00 | GOES-19 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 195.4 |
| 5f3f2689-f2d9-3bdf-afce-a2f2d5525ced | -8.3887 | -46.2557 | 2025-10-17 00:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 55.3 |
| 20c27bf2-aaf7-33cf-9e74-481c058b5971 | -4.9735 | -44.9549 | 2025-10-17 00:40:00 | GOES-19 | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | 87.5 |
| 4b5019f7-e4c3-3593-9302-0769f21b56a1 | -9.1375 | -46.6485 | 2025-10-17 00:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 58.0 |
| 5de57108-30db-3d20-a9d2-96850af40229 | -12.4448 | -51.343 | 2025-10-17 00:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 86.0 |
| 2344edcf-477d-3f9d-a871-4bc7a288aa88 | -4.4061 | -43.3816 | 2025-10-17 00:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 222.5 |
| 37cbcaf9-2920-36f6-a84a-444e346a0959 | -10.5641 | -47.4445 | 2025-10-17 00:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 51.7 |
| 3e29c67a-79b4-37fb-9219-e211d89cb380 | -10.4941 | -43.4315 | 2025-10-17 00:40:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 44.7 |
| 55cc60ed-7ca1-3464-b714-9af1eefaa9f7 | -9.898 | -47.6758 | 2025-10-17 00:40:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 64.9 |
| bb6e19bf-0a4c-3a0a-b8cd-ad8ffdc4d332 | -4.9546 | -44.9787 | 2025-10-17 00:40:00 | GOES-19 | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | 71.5 |
| cc2a72a8-67f2-3a07-b0c2-a79c60a14516 | -4.4245 | -43.4271 | 2025-10-17 00:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 53.8 |
| 7df03b17-9c91-308d-a57c-ee0473bbc64a | -3.5028 | -52.4734 | 2025-10-17 00:40:00 | GOES-19 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 112.5 |
| 09236495-6f52-37e0-bc0d-60e3646d318a | -2.7441 | -48.3022 | 2025-10-17 00:40:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 60.0 |
| fa4d0a41-d5fe-3c95-8c2b-82059ad0683b | -4.9548 | -44.956 | 2025-10-17 00:40:00 | GOES-19 | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | 158.8 |
| f71aafc7-9b65-3185-bfc0-e2f7a8cca9fe | -3.2359 | -45.9862 | 2025-10-17 00:40:00 | GOES-19 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 288.0 |
| 9d3884ba-640b-33db-85eb-f308b051eec6 | -2.7585 | -49.3922 | 2025-10-17 00:40:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 51.8 |
| d5a67430-04df-3557-b48e-1a9f35511919 | -3.5027 | -52.5143 | 2025-10-17 00:40:00 | GOES-19 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 35.2 |
| f8f5055b-2ff4-352e-9c89-cb692cc01b4d | -10.2939 | -44.0221 | 2025-10-17 00:40:00 | GOES-19 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 143.3 |
| 6c0e98c1-917c-3fd1-a3b9-2bbf3ff41507 | -9.879 | -47.6779 | 2025-10-17 00:40:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 95.7 |
| d176a8ae-ac61-3c08-9140-e34a79d8bfc8 | -4.484 | -42.9335 | 2025-10-17 00:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 56.9 |
| 478fc7ba-64db-3a8c-bfc2-7830e002ae02 | -10.2748 | -44.0247 | 2025-10-17 00:40:00 | GOES-19 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 178.8 |
| 3fc21840-5633-3855-ad5e-28a0ac9e7776 | -3.5213 | -52.4728 | 2025-10-17 00:40:00 | GOES-19 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 53.1 |
| 34fb0f10-0cdf-369b-b499-53d1b5f0f27e | -8.1996 | -43.3189 | 2025-10-17 00:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 69.5 |
| 1a7092f6-99a0-365a-8f2a-2cb411c6fef3 | -10.5136 | -43.4052 | 2025-10-17 00:40:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 48.8 |
| 564c033b-899e-37ba-bb4a-c34e415a28cd | -10.534 | -49.5471 | 2025-10-17 00:40:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 79.9 |
| 2bfb7292-89a2-3ef2-8ac5-9722249feabe | -4.4058 | -43.4282 | 2025-10-17 00:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 152.3 |
| 84a67017-20b7-3eef-8f3f-e72f00041c40 | -11.5724 | -44.0736 | 2025-10-17 00:40:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 64.1 |
| 7b1c339f-0aa4-3d55-b656-1a8cc5fe39bc | -10.2935 | -44.0455 | 2025-10-17 00:40:00 | GOES-19 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 119.0 |
| f19632dc-26d5-30a4-bf84-fe8acbd0f3e9 | -10.5644 | -47.4223 | 2025-10-17 00:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 128.3 |
| 07264d14-642a-3168-b8c3-023d0d34fbb9 | -16.0324 | -43.4953 | 2025-10-17 00:40:00 | GOES-19 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 134.8 |
| 931de940-4f57-3ec9-8201-37c1847b9c6b | -10.4945 | -43.4079 | 2025-10-17 00:40:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 33.5 |
| 3de37ee8-845d-371a-bce1-6cad39861601 | -14.3223 | -51.4689 | 2025-10-17 00:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 87.7 |
| 1ccf940f-1c57-3df5-b724-e75a5708debb | -4.3872 | -43.406 | 2025-10-17 00:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 224.6 |
| 62e99804-6c68-351c-b92c-f17e60797776 | -11.4939 | -44.179 | 2025-10-17 00:40:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 76.4 |
| 8c3fa416-649e-33d9-9110-73a8c13deb2c | -3.5212 | -52.4932 | 2025-10-17 00:40:00 | GOES-19 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 84.0 |
| 8624e875-7a52-3f11-9451-01eb1c3d6a20 | -2.7401 | -49.3927 | 2025-10-17 00:40:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 73.0 |
| 3d6650b6-1c00-3e1d-bd66-63da805958d4 | -4.4248 | -43.3805 | 2025-10-17 00:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 138.6 |
| 7667f81a-b7ff-3dfe-9dce-6c243da63382 | -8.3885 | -46.2782 | 2025-10-17 00:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 56.2 |
| c3ca0a93-216f-3457-a198-1b1784276bfc | -11.5733 | -48.5568 | 2025-10-17 00:40:00 | GOES-19 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 83.6 |
| 2c7818f3-2f56-3f04-8997-8f7cce32cf9a | -12.4451 | -51.3217 | 2025-10-17 00:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 99.1 |
| f275a5e9-c4f7-3fd8-82ce-98cd72e32321 | -16.033 | -43.471 | 2025-10-17 00:40:00 | GOES-19 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 83.4 |
| 4ce6ae91-8bfa-379a-a44c-dfad6aef6838 | -10.1528 | -44.5289 | 2025-10-17 00:40:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 77.4 |
| da08fbea-ca3a-324e-8b69-a95050343679 | -3.2546 | -45.9632 | 2025-10-17 00:40:00 | GOES-19 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 120.7 |
| ed05689a-eb10-3cdb-8083-363fc317b048 | -4.3874 | -43.3827 | 2025-10-17 00:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 79.4 |
| 3d885b65-2400-3d1f-982b-f7707fe7379a | -10.4302 | -45.0232 | 2025-10-17 00:40:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 61.8 |
| c2ba1e4b-a804-38af-ae21-6c749e8d3d52 | -10.5834 | -47.42 | 2025-10-17 00:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 160.1 |
| 10a02fff-2c7d-3500-af1f-ec17718253fb | -14.3227 | -51.4475 | 2025-10-17 00:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 67.0 |
| f7755894-3456-386b-9e7d-843dcbc0a913 | -14.303 | -51.4715 | 2025-10-17 00:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 78.3 |
| 885e675c-7fb6-351c-8577-e6e6f346f630 | -10.5831 | -47.4423 | 2025-10-17 00:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 61.8 |
| 0d607817-6854-3184-bc6f-5e3da4f1e889 | -10.4941 | -43.4315 | 2025-10-17 00:50:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 67.5 |
| ecb05bf8-6f8b-3eea-a9a4-d05bf2bda6cf | -4.4058 | -43.4282 | 2025-10-17 00:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 122.7 |
| b74b2255-fd36-3f25-96b9-19dc876d43c8 | -10.4945 | -43.4079 | 2025-10-17 00:50:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 41.6 |
| bb70a4b7-5c5a-30f1-afb1-511c3d90f572 | -11.5733 | -48.5568 | 2025-10-17 00:50:00 | GOES-19 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 90.2 |
| 167dbd43-8407-3c7b-8350-a2dc2a9653c0 | -4.9735 | -44.9549 | 2025-10-17 00:50:00 | GOES-19 | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | 62.7 |
| aaf58d3c-e6c2-36b2-8511-3df45cdc076a | -4.4248 | -43.3805 | 2025-10-17 00:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 113.8 |
| e9526598-b5d6-3eb6-b37e-415aed277fe8 | -4.3871 | -43.4292 | 2025-10-17 00:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 67.3 |
| 8c384319-4a0e-3500-aea3-346950a83499 | -10.5644 | -47.4223 | 2025-10-17 00:50:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 67.1 |
| 7bd9e0b0-b5a8-371d-b8d5-06e79ebf2456 | -3.5028 | -52.4938 | 2025-10-17 00:50:00 | GOES-19 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 121.4 |
| 01dd30f5-a97b-3c9c-8067-f1fda09da627 | -11.5917 | -44.0707 | 2025-10-17 00:50:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 446.8 |
| add28e31-20f8-3910-9def-ccd5f648363b | -10.2748 | -44.0247 | 2025-10-17 00:50:00 | GOES-19 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 209.2 |
| 3af46cd8-5bae-3647-a64b-c4dc5de5995a | -4.4246 | -43.4038 | 2025-10-17 00:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 260.3 |
| 030dd204-6a6a-3b11-b0e5-072603ac2a51 | -11.4748 | -44.1819 | 2025-10-17 00:50:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 91.8 |
| d28be2dd-db5e-314e-8161-66b7822467c7 | -4.3874 | -43.3827 | 2025-10-17 00:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 91.3 |
| 9a2e4812-ecfc-37fa-a8e3-92b98f4a3efd | -11.5724 | -44.0736 | 2025-10-17 00:50:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 144.4 |
| 914525ce-dc90-3803-bb1b-c191a10c7e09 | -6.7592 | -42.3564 | 2025-10-17 00:50:00 | GOES-19 | CAJAZEIRAS DO PIAUÍ | PIAUÍ | Brasil | 2202075 | 22 | 33 | nan | nan | nan | Caatinga | 58.7 |
| 8c90fc3a-c0f3-3618-834d-789c8292c97e | -3.2546 | -45.9632 | 2025-10-17 00:50:00 | GOES-19 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 183.0 |
| 9ce1fcc0-993d-3419-86df-dc7fdb008c35 | -3.4843 | -52.4944 | 2025-10-17 00:50:00 | GOES-19 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 25.6 |
| 4780712a-1bcf-363b-932a-35441fe48236 | -12.1151 | -45.8662 | 2025-10-17 00:50:00 | GOES-19 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 44.1 |
| fef983a1-f1f6-3c49-9af7-553c6b56395b | -2.7441 | -48.3022 | 2025-10-17 00:50:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 56.6 |
| 7a7840dd-447e-36fa-8cf7-91c4a7c20eda | -11.4581 | -44.0439 | 2025-10-17 00:50:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 65.9 |
| eaa61747-3686-385a-95e4-0d1d24efafc2 | -16.0324 | -43.4953 | 2025-10-17 00:50:00 | GOES-19 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 83.9 |


[Clique aqui para ver as próximas entradas](README15.md)
