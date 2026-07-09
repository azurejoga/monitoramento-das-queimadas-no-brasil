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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5105fb42-ec35-35b5-adc1-9c386799e9d8 | -1.82194 | -54.4816 | 2026-07-09 05:25:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ae31df07-e9bf-3cbd-b954-d0a91b91e6ed | -4.34581 | -47.77126 | 2026-07-09 05:25:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 79597a30-a80c-38b9-9295-11bed5a7fad5 | -2.63765 | -47.99003 | 2026-07-09 05:25:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 01bbafa2-8201-3552-9d9c-2c69a762e484 | -1.81889 | -54.47662 | 2026-07-09 05:25:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 263ca770-f79c-3b77-8c16-e9ebe5618509 | 0.87417 | -59.70632 | 2026-07-09 05:25:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 350b03be-b3ae-3d97-a625-17d58e9f0352 | -4.83673 | -45.34512 | 2026-07-09 05:25:00 | NPP-375D | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4ebfdb8f-922e-3211-82c5-140cba78fdf6 | -4.34646 | -47.76668 | 2026-07-09 05:25:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a241a460-e93d-37fb-bb05-edbee13f1bf6 | -1.9095 | -54.21484 | 2026-07-09 05:25:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 92bb066c-a687-3803-997f-1b9349b16905 | -2.98735 | -54.60342 | 2026-07-09 05:25:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a766ddde-d9b1-357d-8f02-b72fb7a65732 | -4.2197 | -56.08099 | 2026-07-09 05:25:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 09a2cf1a-984e-3f9c-8bca-1c63299c50b3 | -4.82967 | -45.34422 | 2026-07-09 05:25:00 | NPP-375D | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| af2b628e-1376-3af2-b110-b7961403dfc8 | 0.87764 | -59.70577 | 2026-07-09 05:25:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 84614b6a-2b5c-3a53-9404-bd62ffea13b8 | -1.81821 | -54.48103 | 2026-07-09 05:25:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| dc5c5f9e-c8ee-3bf4-80a6-e400c436daab | -1.82262 | -54.47718 | 2026-07-09 05:25:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7ba420a9-9274-36ef-93d9-490d0f397d46 | -9.18602 | -58.06922 | 2026-07-09 05:27:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9ed8c5dc-36ab-34df-a3d8-29d282f9baba | -6.12526 | -55.80839 | 2026-07-09 05:27:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b0250d85-128c-31eb-8dd3-793cc2d55790 | -9.5688 | -49.10928 | 2026-07-09 05:27:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b4848a3e-a01d-3552-b464-0d04437174fe | -9.22451 | -48.58383 | 2026-07-09 05:27:00 | NPP-375D | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1f346ba7-c539-3232-a828-9306ab6ba596 | -10.86671 | -47.59959 | 2026-07-09 05:27:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d0e8f2db-5a20-376e-89c6-7a52c5fdd50f | -12.35556 | -47.42458 | 2026-07-09 05:27:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6b40fd35-fb24-31c7-b9f9-b57fd47c84ed | -12.34861 | -47.4265 | 2026-07-09 05:27:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6b4feee0-ff1a-3dff-9fea-b4e5e9966578 | -6.42823 | -55.7973 | 2026-07-09 05:27:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f38bf946-1ba1-34fe-9043-524df1c5a9ac | -12.34871 | -47.42384 | 2026-07-09 05:27:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 7c6cf5d7-e801-37ae-a4a1-8626a925f585 | -8.36757 | -48.23439 | 2026-07-09 05:27:00 | NPP-375D | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0e632983-7d0d-346a-a8ed-33b9ad1e0d94 | -8.12402 | -47.09658 | 2026-07-09 05:27:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a971bf30-231a-3395-b978-4326f6c20d86 | -8.96646 | -48.01649 | 2026-07-09 05:27:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| fe0b734b-8396-33cf-be92-f87a11d1a543 | -9.18659 | -58.06551 | 2026-07-09 05:27:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 207ca305-f7cf-3fa7-819a-118abcbf6281 | -8.11665 | -47.10125 | 2026-07-09 05:27:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bbd0f6fa-a406-39e7-a66b-2477e81a6cc1 | -10.06029 | -60.4957 | 2026-07-09 05:27:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2d0b8e5e-6787-32d7-81bd-e26f46ebed1e | -9.36093 | -65.74548 | 2026-07-09 05:27:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f5f09d44-5a0d-32aa-b522-8f5bdcaa94c2 | -9.54604 | -46.50101 | 2026-07-09 05:27:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 266835a5-0bf2-378b-9c44-42304898cafa | -9.21894 | -48.57856 | 2026-07-09 05:27:00 | NPP-375D | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 840b7994-6cac-37d2-a222-083e7a30f497 | -9.01871 | -63.53742 | 2026-07-09 05:27:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 166ed5c4-1f39-37d2-b074-385961981915 | -6.66881 | -47.51973 | 2026-07-09 05:27:00 | NPP-375D | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e5b9fe81-3807-30e0-9faf-270c0716419f | -12.34929 | -47.42017 | 2026-07-09 05:27:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 37d66071-b5e4-371c-a0cb-bcd752c63406 | -7.28995 | -46.25788 | 2026-07-09 05:27:00 | NPP-375D | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ccf4be4d-ddb8-3042-b2c6-f8f5d1d64a5f | -8.7058 | -54.53811 | 2026-07-09 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 084bf041-ea1d-3d82-8ab8-eef66662ba35 | -11.45048 | -47.58738 | 2026-07-09 05:27:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 9b0a0b1c-39c6-3bce-a7f9-8f67714e3a30 | -8.36815 | -48.2384 | 2026-07-09 05:27:00 | NPP-375D | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 11195bad-62b1-3ed5-b3de-2e6c02b9a69b | -8.95824 | -48.01458 | 2026-07-09 05:27:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| dd2c99e8-de9b-3d44-a639-b0caadfd23b8 | -7.28304 | -46.2571 | 2026-07-09 05:27:00 | NPP-375D | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0589d7af-39d6-380a-b1b6-153a37bffb53 | -8.96013 | -48.01561 | 2026-07-09 05:27:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ef8a24be-531f-3c4e-9a9f-7a833fedc751 | -8.71429 | -48.34137 | 2026-07-09 05:27:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 61b4bf54-17b2-37cd-b16e-fb82b5850762 | -9.84978 | -46.75444 | 2026-07-09 05:27:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a0e001b9-869e-3660-8018-25e2edab01a7 | -9.01505 | -63.53904 | 2026-07-09 05:27:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9ef239c8-1383-3e58-9e82-dfcaa3d04a43 | -10.86007 | -47.59863 | 2026-07-09 05:27:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f3f09c9e-b135-3b56-ae3e-a5476fa090e2 | -12.35614 | -47.4209 | 2026-07-09 05:27:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9d9247dd-8179-3857-9a85-238b3af4b666 | -9.01497 | -63.53682 | 2026-07-09 05:27:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 196f7bd7-a839-3aea-9a7b-c89d837bfafd | -9.22512 | -48.57902 | 2026-07-09 05:27:00 | NPP-375D | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2e6efb59-9841-30ca-a019-fa187a19286b | -6.66981 | -47.52604 | 2026-07-09 05:27:00 | NPP-375D | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| cd419e81-3f4b-3a7c-92ee-b216ce95c0b0 | -7.28937 | -46.25694 | 2026-07-09 05:27:00 | NPP-375D | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| c04ef5a3-b7a5-3e40-a6ae-63086be6d6c9 | -10.89885 | -56.85381 | 2026-07-09 05:27:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5b5d67e5-52de-3e89-8c44-90d58dc77e19 | -11.01665 | -60.86505 | 2026-07-09 05:27:00 | NPP-375D | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0fb4dbcd-b5cd-3fbe-bb3d-b9f64d4d288c | -7.2908 | -46.25159 | 2026-07-09 05:27:00 | NPP-375D | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 69698947-1a1a-3251-89a7-075ed45b98d1 | -8.72049 | -48.34212 | 2026-07-09 05:27:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2f19c7ea-a02b-3046-a99b-69b3d12ea82a | -6.6681 | -47.52487 | 2026-07-09 05:27:00 | NPP-375D | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 702896e6-ed56-3d69-ae97-922a89d9fb54 | -8.70528 | -54.54176 | 2026-07-09 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7fd513ff-aabb-35c3-b1d4-f4b63302074f | -8.96457 | -48.01545 | 2026-07-09 05:27:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 137d47b5-b266-3da2-9173-242af11a63bb | -8.70121 | -54.54114 | 2026-07-09 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0a494f05-f565-3a10-84f9-0ede9e8a1751 | -8.36877 | -48.2337 | 2026-07-09 05:27:00 | NPP-375D | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8e3aaf74-40af-34fa-bc56-8a262cf40062 | -9.01957 | -63.53515 | 2026-07-09 05:27:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 81d9dc6b-50b9-3b89-be4f-635d073cfb27 | -8.7273 | -48.33805 | 2026-07-09 05:27:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 43adf4e1-c17f-3185-b5ea-8559d4d6d0eb | -10.86343 | -47.59856 | 2026-07-09 05:27:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 8823bbbf-0e04-3734-a506-b2c4fc75c6d5 | -11.46154 | -52.92648 | 2026-07-09 05:27:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| aec26b9d-11d2-3311-9cae-9786e1b2f9d7 | -11.4568 | -52.92583 | 2026-07-09 05:27:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 85a3881e-b680-3ef8-ba22-e673e5e1b639 | -9.21836 | -48.5832 | 2026-07-09 05:27:00 | NPP-375D | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9b909c76-cc1e-3642-9169-db7cad1eccc5 | -8.12109 | -47.10253 | 2026-07-09 05:27:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6107332f-c524-3944-9ec0-69142b03a615 | -9.5215 | -58.35727 | 2026-07-09 05:27:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 767799a1-aa5a-37b1-adc6-fcc9ee7362ff | -8.72113 | -48.33708 | 2026-07-09 05:27:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3a490d09-2559-3fa1-83f9-74d9ad8f4699 | -9.01583 | -63.53454 | 2026-07-09 05:27:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9b0ce4d5-4c8f-30d4-a7c5-b1465a130a6c | -11.83443 | -48.24213 | 2026-07-09 05:27:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f3407e95-5717-31de-a5f0-79daf6c17afe | -8.11451 | -47.10134 | 2026-07-09 05:27:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 95fb8139-8021-33e5-9aae-d55d7613fb9e | -6.42757 | -55.80158 | 2026-07-09 05:27:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d7e93dda-9568-3819-a29e-1410c0322d95 | -12.9277 | -49.48395 | 2026-07-09 05:27:00 | NPP-375D | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fd4c6809-2012-3b2e-b843-ee6c87313f0b | -11.18071 | -55.01967 | 2026-07-09 05:27:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 355bbaaf-02b1-3375-888f-610c0d673926 | -8.97883 | -49.88677 | 2026-07-09 05:27:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 938155cb-d19e-326c-b1f2-a8246dc079cd | -5.03089 | -56.19344 | 2026-07-09 05:27:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3e3e7a7f-8260-37c1-bb83-7509da597e2a | -12.93377 | -49.48469 | 2026-07-09 05:27:00 | NPP-375D | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a99c30a1-f4f5-37e3-9bbb-a874a691a032 | -6.67048 | -47.52095 | 2026-07-09 05:27:00 | NPP-375D | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5871ee3e-7915-3239-adf2-7cdad6782ceb | -10.06306 | -60.49977 | 2026-07-09 05:27:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 83aeff0d-69c2-3185-9fd7-2ba2fe4c4358 | -8.70172 | -54.53749 | 2026-07-09 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2de4b89d-ebe2-3ab2-aba7-5ada18710b60 | -11.44926 | -47.59796 | 2026-07-09 05:27:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 6da60e10-805a-3b8b-b64a-90ec806bf50e | -11.44982 | -47.59315 | 2026-07-09 05:27:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 56b50d37-f88b-3464-b391-bca1580640d6 | -7.91594 | -55.40578 | 2026-07-09 05:27:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2efcdd23-2d9b-32c5-a295-1920f55893ae | -10.26487 | -59.031 | 2026-07-09 05:27:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 487d8fa7-718f-3529-89f9-e435bd65ebb4 | -8.1159 | -47.1069 | 2026-07-09 05:27:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 58982855-2898-3561-b801-7aa5265ed385 | -18.02665 | -54.36082 | 2026-07-09 05:29:00 | NPP-375D | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 48ea916b-2df7-3a18-bfb5-c38b5de111da | -13.28939 | -54.41787 | 2026-07-09 05:29:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d2b238b8-57ef-3723-a5e5-ad50839ff6ff | -13.34368 | -54.37914 | 2026-07-09 05:29:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c6d49ae0-915d-339a-acb9-4cba744c933b | -13.28881 | -54.42215 | 2026-07-09 05:29:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6c28c45f-5d71-38e7-bf41-e0ed95567cb9 | -13.29922 | -54.34453 | 2026-07-09 05:29:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8a09a0f7-e0c9-3b2c-9711-2abaf3631ce0 | -13.35859 | -54.36807 | 2026-07-09 05:29:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3a5c48ff-89bb-38bf-bda1-ab3de5e998ef | -13.3569 | -54.381 | 2026-07-09 05:29:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f330eff8-eb66-3984-81a5-a482549d8b12 | -13.285 | -54.41725 | 2026-07-09 05:29:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e0aaca66-4ffd-30fb-a917-f31d3ee800b0 | -13.35746 | -54.37668 | 2026-07-09 05:29:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d518762f-3cfd-3925-827a-46b8fad70538 | -18.11271 | -54.00575 | 2026-07-09 05:29:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1e5c1f0e-cac0-35ed-ac92-c1fedfff818e | -14.15112 | -52.88705 | 2026-07-09 05:29:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 7201b8d5-ba2d-3f23-b5c0-32b9bd08a863 | -18.16749 | -53.22304 | 2026-07-09 05:29:00 | NPP-375D | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 779e0ba7-4303-3708-ad0b-6740fdbc6262 | -18.02326 | -54.36177 | 2026-07-09 05:29:00 | NPP-375D | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3942d575-eb10-3702-ab66-5b9fd7ca332f | -13.29481 | -54.34385 | 2026-07-09 05:29:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README12.md)
