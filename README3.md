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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f20e0194-0fb7-3e71-90ff-17c7414a7b74 | -2.9925 | -51.0242 | 2026-09-30 00:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 72.9 |
| 0095e5d9-6890-3de0-8d93-6a02d2268ffe | -12.2518 | -50.2543 | 2026-09-30 00:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 48.4 |
| ada1efa4-0634-34d1-a0c8-186b810011b8 | -7.7317 | -72.4779 | 2026-09-30 00:30:00 | GOES-19 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 83.6 |
| 7ad9ce38-bc4a-3cd2-9ea3-c6225c89e1ab | -7.5251 | -44.5255 | 2026-09-30 00:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 70.2 |
| f467114a-6ae8-346c-a338-215d5df5a472 | -10.6752 | -50.2834 | 2026-09-30 00:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 69.2 |
| 9855251d-841a-387b-97e2-a9467cc55b00 | -2.9924 | -51.045 | 2026-09-30 00:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 100.5 |
| c465d2f6-50a9-3b0e-8611-a79b13b17351 | -11.7182 | -43.4386 | 2026-09-30 00:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 158.6 |
| ee28a9d6-ace2-328a-abff-75e11f5b3b93 | -11.4307 | -43.4358 | 2026-09-30 00:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 75.7 |
| 29fd6ab9-9d19-3585-891c-529e51460afa | -6.9138 | -43.7049 | 2026-09-30 00:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 77.7 |
| d1834754-6c8f-3147-afde-9a36ff84607d | -11.64 | -43.5218 | 2026-09-30 00:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 62.6 |
| f0bf7690-6041-30bc-84f8-24c4ed310ac2 | -3.2313 | -46.9596 | 2026-09-30 00:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 77.1 |
| 7e402e44-2f39-3fb6-a48f-047af582b027 | -7.8295 | -45.8381 | 2026-09-30 00:30:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 127.7 |
| 03032084-3e59-36a9-a934-f3c499a56cec | -11.8812 | -64.9513 | 2026-09-30 00:30:00 | GOES-19 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 66.3 |
| ae69fa0a-683b-390d-9f6e-8189563e9a59 | -12.3085 | -47.9539 | 2026-09-30 00:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 176.5 |
| 904690f3-ebe3-393c-bf6e-56087982fa0a | -2.9739 | -51.0663 | 2026-09-30 00:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 47.4 |
| c314a396-4f03-3074-8a76-f6e0b271d3f6 | -7.7317 | -72.4779 | 2026-09-30 00:40:00 | GOES-19 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 76.4 |
| 8f16ce70-0747-3185-af79-df77b0cc6b86 | -2.9924 | -51.045 | 2026-09-30 00:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 112.8 |
| 30e13597-371a-32fc-b88e-d419c22f31d8 | -4.4507 | -47.9112 | 2026-09-30 00:40:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 77.6 |
| 8130e3a6-bf51-39d5-bdbb-39c486687f3e | -3.2313 | -46.9596 | 2026-09-30 00:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 71.0 |
| 9842782b-9c97-39f5-95d8-261875dd9b70 | -9.1257 | -67.8322 | 2026-09-30 00:40:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 56.1 |
| 05cfb13e-e3a6-3ba4-bf85-9d0b2c80115a | -7.8107 | -45.8399 | 2026-09-30 00:40:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 65.4 |
| bcc84278-0223-3a64-b531-3b8e8d554af2 | -7.8297 | -45.8156 | 2026-09-30 00:40:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 256.1 |
| f91039ef-282e-38de-9716-db675f6dc6ba | -6.895 | -43.7066 | 2026-09-30 00:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 125.8 |
| 69320705-053c-38ce-8ddf-9ca6510f9149 | -7.8486 | -45.8138 | 2026-09-30 00:40:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 193.5 |
| 62648b73-30b4-3b65-aa07-ae2a00132c6a | -2.974 | -51.0247 | 2026-09-30 00:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 124.2 |
| dbcec0b8-8f37-3638-9a45-185701253953 | -7.8295 | -45.8381 | 2026-09-30 00:40:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 124.6 |
| 0ebac191-76a3-3b18-928f-928e6ff88aa1 | -5.7374 | -45.176 | 2026-09-30 00:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 52.6 |
| 14b2f9ca-f9d2-30fb-87b0-f96b21cf4b69 | -12.3277 | -47.9513 | 2026-09-30 00:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 80.0 |
| 51b7dfb3-f6f6-398e-9125-958e308c9c4f | -3.2314 | -46.9376 | 2026-09-30 00:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 286.2 |
| 61902c10-5c7d-3855-9058-6709224760ba | -11.4307 | -43.4358 | 2026-09-30 00:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 92.3 |
| a57e8128-e985-3b74-8729-7ecd01e4c0bd | -2.8899 | -54.0912 | 2026-09-30 00:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 59.0 |
| 542a836c-4f46-3bc6-a1d2-603cf6b60b30 | -7.8483 | -45.8363 | 2026-09-30 00:40:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 123.6 |
| 7f8ee611-8c0e-3ad6-8282-8bdbe1561924 | -11.8812 | -64.9513 | 2026-09-30 00:40:00 | GOES-19 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 54.8 |
| 29485192-f39d-3ec8-89e9-7c11e56432cf | -6.9138 | -43.7049 | 2026-09-30 00:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 73.4 |
| 8d8391dc-5509-3b4f-95a6-d6c2eb173c8a | -3.2129 | -46.9383 | 2026-09-30 00:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 85.5 |
| 5d8323dc-8f1e-34bf-bbb9-1e0b86aa82e2 | -10.0779 | -63.0804 | 2026-09-30 00:40:00 | GOES-19 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 62.7 |
| 82d64115-40e6-3289-8613-530aad9eb8be | -5.7561 | -45.1747 | 2026-09-30 00:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 81.7 |
| 8e190e00-13ab-3696-b6bb-c264f3d405b2 | -2.9925 | -51.0242 | 2026-09-30 00:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 71.2 |
| d7a21e9e-8069-3515-bf2b-5832e6948426 | -11.699 | -43.4416 | 2026-09-30 00:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 86.7 |
| 44b63353-a817-317d-bc6f-cd99e560d9c5 | -2.9082 | -54.0907 | 2026-09-30 00:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 88.1 |
| fd8fd12f-01ab-3a91-9234-606afa20efd2 | -11.8488 | -50.4526 | 2026-09-30 00:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 81.0 |
| a86af343-6230-3cf3-aac5-87d114ea82d0 | -11.7182 | -43.4386 | 2026-09-30 00:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 132.0 |
| 49159aa6-0ae0-38f8-bc66-dab2e47f9a86 | -3.3801 | -50.95 | 2026-09-30 00:40:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 70.7 |
| 0917958d-d168-3692-b706-3eb44b4a016e | -4.4506 | -47.9329 | 2026-09-30 00:40:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 72.3 |
| f048df5a-ebea-3762-a929-1c6c5a919fa1 | -12.3085 | -47.9539 | 2026-09-30 00:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 160.5 |
| c8686231-d3ea-3dce-b4a0-ee26ba63f926 | -2.9739 | -51.0455 | 2026-09-30 00:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 168.6 |
| 1ed46afc-e933-3a91-886e-46a0e8e75b89 | -7.8109 | -45.8173 | 2026-09-30 00:40:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 126.2 |
| 5ec9ec05-31d9-357c-8486-eb1864658c59 | -3.2315 | -46.9156 | 2026-09-30 00:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 98.4 |
| 1b912f3d-d831-381d-8ae9-cb3dd796aed6 | 3.2742 | -60.6105 | 2026-09-30 00:40:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 70.9 |
| 2e38226b-454b-356c-9749-775aab46e5a4 | -11.4499 | -43.4329 | 2026-09-30 00:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 82.8 |
| f22c9928-533c-3d2e-a0a5-8ce19eaeecda | -10.6752 | -50.2834 | 2026-09-30 00:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 82.3 |
| b311b724-138b-3b5b-b8cc-a5347cbaa618 | -11.7178 | -43.4623 | 2026-09-30 00:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 67.8 |
| 6bea6f73-054e-3c4d-9ce6-c195b3584f03 | -7.8295 | -45.8381 | 2026-09-30 00:50:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 101.9 |
| 3782538d-ed4d-31d7-9cf9-42f1c3447cec | -4.4507 | -47.9112 | 2026-09-30 00:50:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 78.5 |
| fc85cd1c-2a33-3777-89c8-8333984e0455 | -4.4506 | -47.9329 | 2026-09-30 00:50:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 65.7 |
| c42b9368-57d2-3f1c-a3ef-ad446213633a | -6.9138 | -43.7049 | 2026-09-30 00:50:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 75.5 |
| 8ebbe694-6e8a-37e3-8e27-045c5799f268 | -11.8491 | -50.4311 | 2026-09-30 00:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 61.5 |
| 0868a1d8-527f-3135-bd54-d5ae4c26ea9d | -3.3801 | -50.95 | 2026-09-30 00:50:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 63.8 |
| 9fe00e04-a4b9-30ba-9497-45171ca81bba | -11.699 | -43.4416 | 2026-09-30 00:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 76.8 |
| f958b2dc-0604-3c24-a77f-189d5bd62170 | -3.2315 | -46.9156 | 2026-09-30 00:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 89.3 |
| 23cfafe8-d1c5-30f5-b326-a04ccb04e5cf | -2.9924 | -51.045 | 2026-09-30 00:50:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 97.4 |
| 391e06ed-7b3c-35e9-8787-e134e5593d61 | -12.3085 | -47.9539 | 2026-09-30 00:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 178.2 |
| 40cf3745-e97b-3104-85d1-e1e73fec5289 | -2.9739 | -51.0455 | 2026-09-30 00:50:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 161.5 |
| 3408ead1-e0db-3e64-8133-4d809b8bd553 | -3.2314 | -46.9376 | 2026-09-30 00:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 278.4 |
| 63e4ce06-682e-3994-923e-ecd40a2dad32 | -7.8483 | -45.8363 | 2026-09-30 00:50:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 113.1 |
| 548149da-cab6-37d0-a84d-01eb83eea7f3 | 3.2924 | -60.6101 | 2026-09-30 00:50:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 60.6 |
| d6467cb8-b48c-3f2f-8222-68aa82ed2f22 | -7.8297 | -45.8156 | 2026-09-30 00:50:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 268.6 |
| be2f81ae-b2c1-34b7-afe8-2c134b4fe1d9 | -18.2627 | -53.0528 | 2026-09-30 00:50:00 | GOES-19 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 148.4 |
| a78cecf8-1f46-318d-bf56-250ea562b66d | -7.8486 | -45.8138 | 2026-09-30 00:50:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 203.5 |
| ae10bffb-ecb8-3cf1-a19f-0f14c7f458a2 | -9.1257 | -67.8322 | 2026-09-30 00:50:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 58.8 |
| f6054985-ee79-3cc8-8547-6201b282b50a | -5.7374 | -45.176 | 2026-09-30 00:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 54.6 |
| fec490a7-a956-37c0-93e2-a70128384df8 | -11.7182 | -43.4386 | 2026-09-30 00:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 102.9 |
| 7bdc1fe5-bff3-38d5-a7aa-372c642f5b44 | -2.974 | -51.0247 | 2026-09-30 00:50:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 116.8 |
| a4a18208-564c-3728-abe4-25d9bd989aa4 | -2.9925 | -51.0242 | 2026-09-30 00:50:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 62.7 |
| 842b9651-4d7e-32c9-b925-9c2e268c32da | -12.3277 | -47.9513 | 2026-09-30 00:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 88.4 |
| 7006436c-8bfd-3533-8591-ce047df391ec | -10.0779 | -63.0804 | 2026-09-30 00:50:00 | GOES-19 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 67.4 |
| be8ce3ba-320e-3530-96f5-97c93375c0f9 | -4.8582 | -42.9332 | 2026-09-30 00:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 83.1 |
| c4cd1441-d1aa-3a15-84c2-bf8c7639f481 | -18.2831 | -53.028 | 2026-09-30 00:50:00 | GOES-19 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 136.4 |
| 9b308c17-3283-3f21-8611-e91684e98f34 | -11.7178 | -43.4623 | 2026-09-30 00:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 65.0 |
| 61279957-bce0-3ec4-859f-1d7f68fd5e73 | -18.2632 | -53.0312 | 2026-09-30 00:50:00 | GOES-19 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 138.7 |
| a30889f4-c224-3e3c-9962-a29152b01576 | -6.895 | -43.7066 | 2026-09-30 00:50:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 125.3 |
| 8298893d-4e4d-300e-8b7b-c45beb42c993 | -11.8678 | -50.4504 | 2026-09-30 00:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 65.9 |
| 412dd026-9d68-3cf4-b0c0-34ba0d8735ef | -11.8488 | -50.4526 | 2026-09-30 00:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 122.8 |
| 4ac01781-080f-36a5-ba8b-1fcf32143418 | -3.2313 | -46.9596 | 2026-09-30 00:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 60.7 |
| 2a9f228f-aa14-3234-b61f-ec84a4561fcb | -2.9082 | -54.0907 | 2026-09-30 00:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 77.0 |
| c42c6185-2328-3f63-9b95-eb18e634c59a | -18.2827 | -53.0496 | 2026-09-30 00:50:00 | GOES-19 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 196.2 |
| d58ed0da-79da-3933-9d58-33bcedda4127 | -2.9739 | -51.0663 | 2026-09-30 00:50:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 47.0 |
| 117f410c-545b-338b-aae7-570568b3b97a | -5.7561 | -45.1747 | 2026-09-30 00:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 92.9 |
| 08c4f2c5-ac79-3b13-923e-f2564c974a20 | -3.2129 | -46.9383 | 2026-09-30 00:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 80.3 |
| d2acec63-30d5-3321-b001-287ab2bec8bb | -7.8109 | -45.8173 | 2026-09-30 00:50:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 136.3 |
| 5b0a6407-9d89-33ec-abe8-48eb2245d61d | -3.2315 | -46.9156 | 2026-09-30 01:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 77.8 |
| 88ef18a4-11cf-3631-ba2c-e85542262e63 | -11.699 | -43.4416 | 2026-09-30 01:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 92.8 |
| 97d4e7b9-a7d3-39c9-8548-8c6b6d3b4318 | -10.0779 | -63.0804 | 2026-09-30 01:00:00 | GOES-19 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 65.6 |
| 5e637acf-9683-35bc-adfb-3b9194ed2369 | -2.9739 | -51.0663 | 2026-09-30 01:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 37.3 |
| 4ec8599c-496c-3890-928a-193d458d9628 | -11.64 | -43.5218 | 2026-09-30 01:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 69.7 |
| 91848a1e-7340-3f16-85bb-43d5052763ce | -9.1257 | -67.8322 | 2026-09-30 01:00:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 59.4 |
| a3642ce1-80ab-3cb7-ae72-fcf8190c4b19 | -6.9138 | -43.7049 | 2026-09-30 01:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 73.3 |
| 39de91ca-eda8-31ec-ae96-13d8ffda3dac | -5.1621 | -55.9931 | 2026-09-30 01:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 62.5 |
| 7ed5f8e1-7a44-39d3-a4e3-c1b338c5f8f8 | -11.8488 | -50.4526 | 2026-09-30 01:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 141.3 |
| 5d9df400-c043-3fd6-bda3-4157dac5d801 | -12.3277 | -47.9513 | 2026-09-30 01:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 72.1 |


[Clique aqui para ver as próximas entradas](README4.md)
