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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| aa331487-9d29-3e81-9a85-4d4d9aaecc09 | -10.3437 | -49.6321 | 2025-11-09 01:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 64.4 |
| 66b6af3d-403f-34c3-a01b-243c01351e0e | -4.4534 | -44.6447 | 2025-11-09 01:40:00 | GOES-19 | TRIZIDELA DO VALE | MARANHÃO | Brasil | 2112233 | 21 | 33 | nan | nan | nan | Cerrado | 75.6 |
| 1a7701c0-7a86-3d1f-b09c-41cdd124eff3 | -3.337 | -44.3577 | 2025-11-09 01:40:00 | GOES-19 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 45.8 |
| 1cea279e-ac67-3691-ad06-db77844edf70 | -3.5946 | -41.6577 | 2025-11-09 01:40:00 | GOES-19 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 46.7 |
| 95790a06-dae3-3ec7-b0d6-36a99d30278f | -2.6113 | -49.2263 | 2025-11-09 01:40:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 64.3 |
| 1bf22829-3340-3b0f-bcc6-03818d43808a | -3.3369 | -44.3806 | 2025-11-09 01:40:00 | GOES-19 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 73.3 |
| c863a0d4-b119-3390-a461-4fafdff83c2c | -5.2722 | -44.9585 | 2025-11-09 01:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 58.5 |
| c703f57c-676d-31c3-ad39-db90bc4b513b | -2.9435 | -49.3443 | 2025-11-09 01:40:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 45.5 |
| c65a7459-6bf2-3f45-a2e3-3b86c9f9e80e | -5.2908 | -44.9572 | 2025-11-09 01:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 61.1 |
| b2a8a7bd-fa98-3031-bc3b-fb5033458a3f | -2.5929 | -49.2268 | 2025-11-09 01:40:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 53.9 |
| 87c024c6-32f4-36b1-bbf1-12323b68e678 | -3.337 | -44.3577 | 2025-11-09 01:50:00 | GOES-19 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 44.7 |
| f25c79e8-d9de-39b3-996d-c5d2c07c336f | -2.9434 | -49.3655 | 2025-11-09 01:50:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 49.8 |
| 5e423f88-9247-3eec-ad00-9f094e5691d8 | -3.3369 | -44.3806 | 2025-11-09 01:50:00 | GOES-19 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 62.6 |
| d883e6ba-a36a-3ada-a9c3-aa7c9f3e6d10 | -10.3437 | -49.6321 | 2025-11-09 01:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 66.2 |
| c41126e9-bbd9-3503-9f68-a03a5f15a3cd | -5.2722 | -44.9585 | 2025-11-09 01:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 54.3 |
| 4259e845-9c68-3686-ba37-c8fc2a2ee4fc | -2.6113 | -49.2263 | 2025-11-09 01:50:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 59.5 |
| 3046c92d-bd44-3eea-bee1-2a7f58d18671 | -2.5929 | -49.2268 | 2025-11-09 01:50:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 48.6 |
| 724b329b-3026-32a8-8c87-d238cd4a0156 | -4.4534 | -44.6447 | 2025-11-09 01:50:00 | GOES-19 | TRIZIDELA DO VALE | MARANHÃO | Brasil | 2112233 | 21 | 33 | nan | nan | nan | Cerrado | 59.3 |
| ed12e630-8647-35ba-ab45-50465f1af699 | -10.3248 | -49.6341 | 2025-11-09 01:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 52.0 |
| bc32d639-ce58-3d33-ad8e-f25e43b24e95 | -5.2908 | -44.9572 | 2025-11-09 01:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 58.7 |
| c0e9000e-879a-3756-91c6-fc64d90353b8 | -5.2908 | -44.9572 | 2025-11-09 02:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 63.2 |
| 66d2f1cf-6672-3c99-8840-c87c7fdce219 | -4.4534 | -44.6447 | 2025-11-09 02:00:00 | GOES-19 | TRIZIDELA DO VALE | MARANHÃO | Brasil | 2112233 | 21 | 33 | nan | nan | nan | Cerrado | 55.6 |
| 39b1af17-dfbd-3152-b8a7-0c099c6fb856 | -2.6113 | -49.2263 | 2025-11-09 02:00:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 50.7 |
| 0d7acbe2-325a-34e5-87aa-d69affa6fb31 | -3.3369 | -44.3806 | 2025-11-09 02:00:00 | GOES-19 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 63.5 |
| 4369d2c5-8ae6-3799-b1ae-b211a40b8b83 | -2.9434 | -49.3655 | 2025-11-09 02:00:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 47.2 |
| 86ff5bcd-0272-3392-b0b9-d78d7e3e8002 | -3.337 | -44.3577 | 2025-11-09 02:00:00 | GOES-19 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 47.4 |
| a295b743-9eec-3600-a169-f71930a3ffb4 | -3.3369 | -44.3806 | 2025-11-09 02:10:00 | GOES-19 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 70.3 |
| d87c7bb0-5297-3f38-9326-3473e7801b9e | -4.4534 | -44.6447 | 2025-11-09 02:10:00 | GOES-19 | TRIZIDELA DO VALE | MARANHÃO | Brasil | 2112233 | 21 | 33 | nan | nan | nan | Cerrado | 67.2 |
| 4d5abdb4-c25a-3b69-829a-450659ee6525 | -9.4535 | -59.2143 | 2025-11-09 02:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 51.0 |
| 508274ab-ad95-388c-86d8-e14073769acd | -4.1203 | -47.2951 | 2025-11-09 02:10:00 | GOES-19 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 43.7 |
| 2c72ea2f-2734-3df0-9f50-b2b6d3d6a815 | -5.2722 | -44.9585 | 2025-11-09 02:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 57.3 |
| f26b0fdc-b50b-3746-965f-b6d7481a4bfb | -3.337 | -44.3577 | 2025-11-09 02:10:00 | GOES-19 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 39.3 |
| ef3fc425-11a9-3abe-abfa-a57fe59fdd92 | -3.337 | -44.3577 | 2025-11-09 02:20:00 | GOES-19 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 41.0 |
| 27f11d3f-c62e-3e74-aac2-7dacea74b310 | -4.1203 | -47.2951 | 2025-11-09 02:20:00 | GOES-19 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 67.2 |
| 8084b89f-5694-3369-8f1d-d0bd8e305b0e | -3.3369 | -44.3806 | 2025-11-09 02:20:00 | GOES-19 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 74.9 |
| df5cd42e-610d-3146-99a8-e516ba60496d | -4.4534 | -44.6447 | 2025-11-09 02:20:00 | GOES-19 | TRIZIDELA DO VALE | MARANHÃO | Brasil | 2112233 | 21 | 33 | nan | nan | nan | Cerrado | 58.0 |
| e5c47549-3222-34d9-b0ff-20a1549d2a0b | -9.4535 | -59.2143 | 2025-11-09 02:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 50.9 |
| d0659961-78f6-38e0-8f83-4b6051584f17 | -5.2722 | -44.9585 | 2025-11-09 02:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 57.4 |
| 6e5f70d8-048b-36e1-bc30-5d85f2610abc | -5.2908 | -44.9572 | 2025-11-09 02:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 57.2 |
| 974e9da4-c83f-3aec-ab02-b3f947824788 | -4.4534 | -44.6447 | 2025-11-09 02:30:00 | GOES-19 | TRIZIDELA DO VALE | MARANHÃO | Brasil | 2112233 | 21 | 33 | nan | nan | nan | Cerrado | 47.4 |
| b042933b-8d30-3319-9474-e78bda3e4491 | -3.3369 | -44.3806 | 2025-11-09 02:30:00 | GOES-19 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 68.3 |
| 6c637fef-7f15-393a-98b1-28d8798f7ff4 | -3.337 | -44.3577 | 2025-11-09 02:40:00 | GOES-19 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 48.0 |
| ae08245b-d450-3474-8a9d-545873386b5c | -9.4349 | -59.2154 | 2025-11-09 02:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 47.0 |
| 2c0c17f7-9085-32ed-b742-bbc707acce28 | -4.4534 | -44.6447 | 2025-11-09 02:40:00 | GOES-19 | TRIZIDELA DO VALE | MARANHÃO | Brasil | 2112233 | 21 | 33 | nan | nan | nan | Cerrado | 55.4 |
| 3104ae85-609c-3db2-ba4b-c6eafb0d0418 | -3.3369 | -44.3806 | 2025-11-09 02:40:00 | GOES-19 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 88.3 |
| a2209da7-94e5-3f33-af66-6f95fecb748c | -3.337 | -44.3577 | 2025-11-09 02:50:00 | GOES-19 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 43.3 |
| 1210fd84-583c-3bba-9acc-6bfbcbf376ca | -4.4534 | -44.6447 | 2025-11-09 02:50:00 | GOES-19 | TRIZIDELA DO VALE | MARANHÃO | Brasil | 2112233 | 21 | 33 | nan | nan | nan | Cerrado | 53.3 |
| c261315b-4f1d-3a8a-8182-f8ea4ecd6130 | -4.1203 | -47.2951 | 2025-11-09 02:50:00 | GOES-19 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 45.0 |
| 78ee43aa-fade-313e-af82-7cdd64acba48 | -3.3369 | -44.3806 | 2025-11-09 02:50:00 | GOES-19 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 85.5 |
| 2e4f1f25-6309-392e-9e14-6483c17faf99 | -7.84214 | -38.43858 | 2025-11-09 02:57:00 | NOAA-20 | SERRA TALHADA | PERNAMBUCO | Brasil | 2613909 | 26 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 5b189c22-6eba-3dcd-80a2-e6e683dd6f7f | -4.1203 | -47.2951 | 2025-11-09 03:00:00 | GOES-19 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 55.7 |
| 2553a3e6-8ec1-36d4-aa51-4df4e216d8ea | -4.4534 | -44.6447 | 2025-11-09 03:00:00 | GOES-19 | TRIZIDELA DO VALE | MARANHÃO | Brasil | 2112233 | 21 | 33 | nan | nan | nan | Cerrado | 60.4 |
| 36f18836-66d7-3e6f-9218-6c3e07dd303b | -3.3369 | -44.3806 | 2025-11-09 03:00:00 | GOES-19 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 87.1 |
| 01a65deb-54e9-3bc8-96a8-1ccd4c673fd9 | -3.337 | -44.3577 | 2025-11-09 03:10:00 | GOES-19 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 47.2 |
| 1b55c9ac-48cc-36dc-bd6f-48b585189c0e | -3.3369 | -44.3806 | 2025-11-09 03:10:00 | GOES-19 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 120.2 |
| 6a650f03-97b5-3b49-bc20-72ffd55f3a0b | -3.3182 | -44.3814 | 2025-11-09 03:10:00 | GOES-19 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 63.8 |
| bba2a077-cf91-34aa-af58-bbf2b1372ca0 | -3.337 | -44.3577 | 2025-11-09 03:20:00 | GOES-19 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 60.8 |
| 1e3400d5-a480-3b24-9254-27b2ed63ba81 | -3.3369 | -44.3806 | 2025-11-09 03:20:00 | GOES-19 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 125.2 |
| e696b92b-e237-3309-a252-8b952472019c | -19.761 | -58.1269 | 2025-11-09 03:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 76.2 |
| 11f886f3-d7a2-37a3-a7d1-96de4c340752 | -4.4534 | -44.6447 | 2025-11-09 03:20:00 | GOES-19 | TRIZIDELA DO VALE | MARANHÃO | Brasil | 2112233 | 21 | 33 | nan | nan | nan | Cerrado | 56.4 |
| 95c195be-18d6-3733-a04f-b9f933b419c5 | -3.3369 | -44.3806 | 2025-11-09 03:30:00 | GOES-19 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 121.7 |
| 031d0d53-ee93-3e13-92d1-2d71cc5a757e | -19.761 | -58.1269 | 2025-11-09 03:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 56.9 |
| eba3a188-b8b5-3fec-b837-01d7cd8ee945 | -4.4534 | -44.6447 | 2025-11-09 03:30:00 | GOES-19 | TRIZIDELA DO VALE | MARANHÃO | Brasil | 2112233 | 21 | 33 | nan | nan | nan | Cerrado | 57.9 |
| 42505212-acc6-36ec-afde-8f6605f8d85a | -3.337 | -44.3577 | 2025-11-09 03:30:00 | GOES-19 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 50.1 |
| 42aefa4a-5fa4-3e58-a37f-994f8b48a01a | -4.4534 | -44.6447 | 2025-11-09 03:40:00 | GOES-19 | TRIZIDELA DO VALE | MARANHÃO | Brasil | 2112233 | 21 | 33 | nan | nan | nan | Cerrado | 58.2 |
| f38af02f-759b-32f8-b956-f428bd5a227f | -3.3182 | -44.3814 | 2025-11-09 03:40:00 | GOES-19 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 42.4 |
| 683ea29a-c3a7-3ba7-9eb6-ff445c34e390 | -19.761 | -58.1269 | 2025-11-09 03:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 94.4 |
| ec525109-2bee-31dd-90b3-6ac8e1497b26 | -3.3369 | -44.3806 | 2025-11-09 03:40:00 | GOES-19 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 95.8 |
| 2779d840-d528-33e6-8d30-ba6c806501fc | -4.96637 | -37.9544 | 2025-11-09 03:46:00 | NOAA-21 | RUSSAS | CEARÁ | Brasil | 2311801 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 8a0ec5f0-567a-3175-a405-10d89567bad3 | -3.51238 | -40.36026 | 2025-11-09 03:46:00 | NOAA-21 | MASSAPÊ | CEARÁ | Brasil | 2308005 | 23 | 33 | nan | nan | nan | Caatinga | 4.1 |
| bc00dd08-415e-3c05-a934-dc08f4af5c38 | -4.33722 | -39.36221 | 2025-11-09 03:46:00 | NOAA-21 | CANINDÉ | CEARÁ | Brasil | 2302800 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 111f74c2-046f-306d-a009-528a77ef4480 | -3.76992 | -44.29278 | 2025-11-09 03:46:00 | NOAA-21 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0d272e28-cf6f-3939-820d-150c1419c0ee | -3.58453 | -41.65662 | 2025-11-09 03:46:00 | NOAA-21 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 0b488bce-4e50-3789-80c4-3b0153f10132 | -3.42337 | -43.16499 | 2025-11-09 03:46:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ca276486-18ce-301f-8675-8a6aa9bef722 | -2.74207 | -45.16407 | 2025-11-09 03:46:00 | NOAA-21 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b3334894-b387-3ca7-aeac-708286b5e3be | -2.60604 | -49.22252 | 2025-11-09 03:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| c632ffbe-5bc7-349f-8394-7ac6417bfd94 | -3.33904 | -44.37159 | 2025-11-09 03:46:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 163cdbdb-b896-3136-b366-1ad9ad777480 | -8.84165 | -40.07227 | 2025-11-09 03:46:00 | NOAA-21 | SANTA MARIA DA BOA VISTA | PERNAMBUCO | Brasil | 2612604 | 26 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 68738e0f-49d1-328e-a1d1-03f0cea0a537 | -6.22447 | -47.01693 | 2025-11-09 03:46:00 | NOAA-21 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 0b5be2f7-4c3f-3cf3-b82a-3454f51b013d | -6.87782 | -47.2445 | 2025-11-09 03:46:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6ed66582-4495-3cec-b9f2-16f7bd979acc | -8.19015 | -46.20724 | 2025-11-09 03:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 98105393-3606-3db1-8643-c157fe10c673 | -2.63856 | -47.30355 | 2025-11-09 03:46:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 61e7000a-5c21-39a5-b96c-bd4785aee472 | -2.94469 | -49.35172 | 2025-11-09 03:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 18.0 |
| 25cd3256-601b-339f-a8b8-dbda2cd675bc | -3.45514 | -45.64949 | 2025-11-09 03:46:00 | NOAA-21 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 24475c77-cd8a-3f16-9c0a-d72584a72550 | -7.55512 | -45.85725 | 2025-11-09 03:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ce71425f-be84-32f8-b64c-82a80256f2cf | -3.76919 | -40.51139 | 2025-11-09 03:46:00 | NOAA-21 | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 97f73cc2-8cc3-3ee3-9b92-8992312b4cec | -8.9823 | -40.54713 | 2025-11-09 03:46:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.3 |
| d35dba26-93c7-305f-a9f0-afd29170ce4e | -7.49328 | -46.60801 | 2025-11-09 03:46:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 312a080b-0858-36f2-86db-1fb0ce30e79b | -2.61191 | -49.2303 | 2025-11-09 03:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| dce398c0-595b-3c59-afa4-97f30b7edb61 | -2.64054 | -47.30162 | 2025-11-09 03:46:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 22237a64-09ca-3d4e-992b-6956a77d8ff2 | -6.99207 | -42.78469 | 2025-11-09 03:46:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 5ca3a1e1-8080-36ef-a2c2-7bcabcc80b4d | -7.17527 | -41.73767 | 2025-11-09 03:46:00 | NOAA-21 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 10.3 |
| 2b41bd7d-78e0-3dc0-bfa7-66da972ee69a | -3.32641 | -44.36359 | 2025-11-09 03:46:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 1e1698e3-8a92-349b-aec5-533eb85178b0 | -2.74264 | -45.16063 | 2025-11-09 03:46:00 | NOAA-21 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 72eaa2e9-5e76-3e8c-af7c-870b8dcd9960 | -7.55045 | -45.85319 | 2025-11-09 03:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3390d569-46a8-32b6-8b9b-a5dfc5931271 | -3.83496 | -42.51563 | 2025-11-09 03:46:00 | NOAA-21 | SÃO JOÃO DO ARRAIAL | PIAUÍ | Brasil | 2209971 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4c379037-7717-305c-8a49-f9f2b309c68e | -7.56743 | -45.87912 | 2025-11-09 03:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 37c36483-91cd-3e25-8bac-e01b568b409d | -8.41934 | -36.25356 | 2025-11-09 03:46:00 | NOAA-21 | TACAIMBÓ | PERNAMBUCO | Brasil | 2614709 | 26 | 33 | nan | nan | nan | Caatinga | 6.4 |
| 403c8f95-1b00-3631-83dc-726d04680e7f | -2.92186 | -40.00158 | 2025-11-09 03:46:00 | NOAA-21 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 6697ad3f-defd-343b-8d6c-631c0fa7f1cf | -6.03028 | -46.56276 | 2025-11-09 03:46:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README8.md)
