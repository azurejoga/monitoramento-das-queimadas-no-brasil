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

## Dados Diários - Página 75

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fa9eba47-1396-38e9-8764-cdf4de1e50c8 | -11.7713 | -50.5472 | 2025-09-14 10:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 109.0 |
| 71585a9b-4876-3eb5-8427-ef3aedb39910 | -11.7525 | -50.528 | 2025-09-14 10:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 118.9 |
| 551fb1e9-6b12-3842-a7bc-2c1a3dd1510b | -7.1912 | -44.1195 | 2025-09-14 10:30:00 | GOES-19 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 86.4 |
| d723bdad-0072-3ee1-b00e-99669f29684b | -11.7522 | -50.5494 | 2025-09-14 10:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 110.2 |
| c8a4f871-73f5-3315-b886-1f4ae14e53c1 | -11.7716 | -50.5258 | 2025-09-14 10:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 169.7 |
| d4d27efd-b917-316a-8ae7-06b37d05732c | -7.1909 | -44.1426 | 2025-09-14 10:30:00 | GOES-19 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 107.3 |
| 44cbde36-1d5d-3e3f-9b64-9f5d6c1866e7 | -11.7713 | -50.5472 | 2025-09-14 10:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 106.3 |
| 82f6653f-1480-3e9e-8cb5-1efe9f17bc19 | -11.7716 | -50.5258 | 2025-09-14 10:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 160.4 |
| 4885e587-65ee-3fda-a6fd-81804df57d86 | -11.7525 | -50.528 | 2025-09-14 10:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 107.1 |
| ff9b889b-e8a3-389c-8d1b-024c30c37418 | -21.7007 | -48.9039 | 2025-09-14 10:40:00 | GOES-19 | IBITINGA | SÃO PAULO | Brasil | 3519600 | 35 | 33 | nan | nan | nan | Cerrado | 129.8 |
| 243cbd4c-b471-3b81-877f-f3ca51b0804f | -10.7687 | -46.4808 | 2025-09-14 10:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 101.8 |
| c749f59d-b969-35f1-9b4f-63aff927262d | -11.7522 | -50.5494 | 2025-09-14 10:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 129.6 |
| 643e31b8-09ff-3043-971e-1286b0982da4 | -10.75 | -46.4607 | 2025-09-14 10:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 145.3 |
| 9a0f74c8-4c51-307e-9837-157598c1313a | -11.7713 | -50.5472 | 2025-09-14 10:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 111.8 |
| 539c31a3-e96b-33d4-9306-495dffca11af | -11.7716 | -50.5258 | 2025-09-14 10:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 237.6 |
| 2fdf63b8-1e8b-3f85-b78f-33ccee49ed4a | -11.7525 | -50.528 | 2025-09-14 10:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 151.1 |
| 44cff878-4cdf-30e8-98df-3cdcddd71851 | -11.7719 | -50.5043 | 2025-09-14 10:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 115.0 |
| 9a595158-45cd-380c-839b-fc789a2b3d8e | -12.8212 | -47.1445 | 2025-09-14 11:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 97.0 |
| 5efea3b8-1269-36bd-a3d1-81e7b257cee6 | -10.7496 | -46.4832 | 2025-09-14 11:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 97.4 |
| 9e2207cf-6d61-3780-b2a1-f87e0afd2185 | -10.7687 | -46.4808 | 2025-09-14 11:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 96.1 |
| 96aca5e3-7b83-372e-81de-6128c1cc9765 | -10.75 | -46.4607 | 2025-09-14 11:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 105.1 |
| 4fdfeb73-8ab5-30a6-a06e-fbf2a231993f | -12.7867 | -47.9986 | 2025-09-14 11:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 90.6 |
| 4da5334c-4f94-38b2-b4b5-c19583c690c7 | -12.7871 | -47.9764 | 2025-09-14 11:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 94.8 |
| 20615699-46f5-3248-ad19-e6df84370ebd | -12.7675 | -48.0013 | 2025-09-14 11:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 111.3 |
| b99e41a0-ebe9-3846-ab85-d1ee9d6a10fd | -8.9979 | -45.7871 | 2025-09-14 11:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 99.5 |
| 37472394-9c21-3e46-af5f-4e1ec0139d61 | -12.7671 | -48.0236 | 2025-09-14 11:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 103.8 |
| 1a279d6a-197e-3499-b2d5-3b1ecceb17a3 | -12.7867 | -47.9986 | 2025-09-14 11:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 86.7 |
| 84163ff9-acaa-3ea2-9891-16b13da6e070 | -10.7496 | -46.4832 | 2025-09-14 11:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 98.5 |
| 7ca83b57-4dec-3450-87f8-3c528718925a | -12.7871 | -47.9764 | 2025-09-14 11:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 86.5 |
| 37c3b5d4-2a88-331b-a704-a54421b78530 | -10.7687 | -46.4808 | 2025-09-14 11:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 122.5 |
| 70dda17f-e6c9-3d65-b9bc-ddbe07bd3c41 | -10.75 | -46.4607 | 2025-09-14 11:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 124.2 |
| d348345d-f369-3e7e-a3e4-b005d2ea478a | -12.7675 | -48.0013 | 2025-09-14 11:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 91.4 |
| c3350ebc-2091-3428-9142-65a111afac90 | -12.7671 | -48.0236 | 2025-09-14 11:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 82.0 |
| 6eeebada-240c-355d-b362-9276b4abe91c | -10.7496 | -46.4832 | 2025-09-14 11:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 113.8 |
| 0d95d06d-ff9b-3371-bc09-3c1f080787ae | -10.75 | -46.4607 | 2025-09-14 11:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 131.5 |
| 9809c8e2-3555-30fb-a9b8-4267aff45252 | -10.7503 | -46.4381 | 2025-09-14 11:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 110.1 |
| 1a1b7cb3-5e60-3ef8-97b0-114ffa75aed2 | -10.7687 | -46.4808 | 2025-09-14 11:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 153.8 |
| f7bb4f81-3e77-3f9c-b5cd-6fe091813622 | -12.7867 | -47.9986 | 2025-09-14 11:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 131.8 |
| 2daaaeb2-6a2f-3925-a64d-cc31713a1a9a | -10.7313 | -46.4405 | 2025-09-14 11:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 90.0 |
| cbf259b2-ba96-30f5-a537-b484d05dc16a | -12.7871 | -47.9764 | 2025-09-14 11:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 129.1 |
| e8a69241-5615-3e2e-8697-d0d2b70f48d6 | -8.9979 | -45.7871 | 2025-09-14 11:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 115.1 |
| 1a5584be-7aeb-3732-9957-1969f41170d5 | -10.7687 | -46.4808 | 2025-09-14 11:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 125.6 |
| a34e3931-210a-3167-ac91-054e26f3e72b | -12.7671 | -48.0236 | 2025-09-14 11:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 106.0 |
| c5fd65ea-ead7-3ea0-b113-6024dfef26b8 | -10.75 | -46.4607 | 2025-09-14 11:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 128.7 |
| a8a87f76-ea9f-3ef5-aaca-4a2623f2a455 | -12.7871 | -47.9764 | 2025-09-14 11:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 78.1 |
| fe62015c-97fd-39f0-88eb-20113a96a14a | -8.9079 | -45.457 | 2025-09-14 11:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 84.9 |
| c88ed613-d5e4-35a5-9448-032513d335fe | -8.9979 | -45.7871 | 2025-09-14 11:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 182.4 |
| bb1f57ed-c736-39ea-87a3-8c44d822be40 | -12.9294 | -54.7333 | 2025-09-14 11:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 90.2 |
| 0d2647a1-34e7-3f53-8554-7c3a2c55e84a | -10.7496 | -46.4832 | 2025-09-14 11:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 112.1 |
| 78a77e08-c54d-36ee-b86f-eb0b62259e82 | -11.3831 | -47.3429 | 2025-09-14 11:40:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 132.1 |
| 8f8bf8cf-ffed-3002-8f99-b679e1e89555 | -10.7687 | -46.4808 | 2025-09-14 11:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 136.4 |
| 1a1aa2ef-9dca-3d41-aaf8-7add0decb79d | -8.9976 | -45.8098 | 2025-09-14 11:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 136.2 |
| 5efff006-99ca-3d98-97bf-9ab3b6601d26 | -8.8893 | -45.4363 | 2025-09-14 11:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 123.4 |
| 84501732-fdbc-380f-99af-4fefa4f879f3 | -11.4022 | -47.3405 | 2025-09-14 11:40:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 85.8 |
| 4f841787-d9b4-3eb7-ba73-a09ed2dfb699 | -8.9079 | -45.457 | 2025-09-14 11:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 96.4 |
| 5f45467c-8581-3721-a581-8053d2ca6c0e | -8.9173 | -46.179 | 2025-09-14 11:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 115.4 |
| b40c79e0-021a-3aa8-929d-2db10ea4bd63 | -8.979 | -45.7892 | 2025-09-14 11:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 90.7 |
| 9761d914-2e2c-3ed9-83c6-7e769a619b18 | -12.9294 | -54.7333 | 2025-09-14 11:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 87.6 |
| bacb473d-56d5-38a9-b8cf-49b81436c020 | -11.2349 | -44.7751 | 2025-09-14 11:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 101.5 |
| 4a35fde6-4f60-38ae-81cf-5374e380a7b2 | -8.9979 | -45.7871 | 2025-09-14 11:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 147.0 |
| 095ddaef-7aa2-3f04-be1b-0ed3dad60784 | -8.9079 | -45.457 | 2025-09-14 11:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 125.3 |
| c508a7af-b829-3346-a4bf-f81c9f4b3e62 | -12.7675 | -48.0013 | 2025-09-14 11:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 72.3 |
| 6af9cb92-8dec-361e-8b2e-2a7d47d5eadb | -11.3831 | -47.3429 | 2025-09-14 11:50:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 89.6 |
| fcedd3c4-12cc-3960-a9f5-9d14bd2fa5ad | -10.7503 | -46.4381 | 2025-09-14 11:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 100.5 |
| 399428b2-118a-3490-b772-4b8b22c38a44 | -12.7871 | -47.9764 | 2025-09-14 11:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 72.4 |
| 7ac8fc64-06cf-3c40-88ec-7b305e075e91 | -14.3285 | -46.1088 | 2025-09-14 11:50:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 155.4 |
| 99771c87-dca0-380a-a20f-19bb2a2eede6 | -9.7389 | -46.8728 | 2025-09-14 11:50:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 96.8 |
| cebf6175-5b67-3ac4-a2a6-564ee6cd2073 | -12.8019 | -47.1474 | 2025-09-14 11:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 103.4 |
| 3a8a8b76-666f-34f4-94ce-4e42ac5081f2 | -10.7687 | -46.4808 | 2025-09-14 11:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 89.4 |
| cf843e9a-0f02-380c-9211-83c68be07b78 | -12.8212 | -47.1445 | 2025-09-14 11:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 127.8 |
| e8dc1b08-3b1f-3468-bc86-552eb351b5fe | -10.75 | -46.4607 | 2025-09-14 11:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 110.9 |
| d991f7ff-a975-38db-865f-403713cd2510 | -14.3095 | -46.089 | 2025-09-14 11:50:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 149.9 |
| ea062137-9fd8-3dfc-9fa4-5445718a1fe0 | -11.8675 | -50.4718 | 2025-09-14 11:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 103.1 |
| 980b83d2-5b22-3726-855a-5290d736041a | -8.9976 | -45.8098 | 2025-09-14 11:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 109.9 |
| e6401c82-8642-34e9-b604-1a4a85c74467 | -14.329 | -46.0857 | 2025-09-14 11:50:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 205.3 |
| 8a5e86fa-4ec6-338d-8e60-61546814bf9a | -8.9176 | -46.1565 | 2025-09-14 11:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 93.5 |
| eb6c325e-6a45-3fcb-885a-241caa4ea0c5 | -14.309 | -46.1121 | 2025-09-14 11:50:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 78.4 |
| 181dc5d9-5f0a-3fb3-8427-60c71339b82c | -8.8893 | -45.4363 | 2025-09-14 11:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 79.5 |
| fedfcc7b-cb40-3b6d-afba-2591b1e3b98a | -8.9976 | -45.8098 | 2025-09-14 12:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 152.0 |
| c2b2e004-f3e8-38ff-9cb3-e48d814e7e4a | -14.3095 | -46.089 | 2025-09-14 12:00:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 163.3 |
| 65fdf8ef-2784-327b-b34e-aad2197ed683 | -8.9979 | -45.7871 | 2025-09-14 12:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 171.6 |
| d41399c0-297e-3079-8478-cc35eae298ef | -11.3831 | -47.3429 | 2025-09-14 12:00:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 129.6 |
| 5ee659e0-45b3-3ee6-9bdd-fb1424fdd8eb | -13.9473 | -44.8541 | 2025-09-14 12:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 121.4 |
| cf2d0118-7d17-360e-b2fe-ecf41057a4be | -14.2107 | -46.1749 | 2025-09-14 12:00:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 85.7 |
| ffa18eda-4992-3638-be9e-16efd0856bb4 | -12.7675 | -48.0013 | 2025-09-14 12:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 68.9 |
| 7da46b53-f1ae-3b39-baf6-bec22a17d267 | -12.8208 | -47.1671 | 2025-09-14 12:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 148.3 |
| 70d116f4-dbfb-3791-939c-b6b6d527fc07 | -8.9173 | -46.179 | 2025-09-14 12:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 155.0 |
| 2730c34e-2e6a-3a0e-aecb-434b3b1ddd28 | -14.3285 | -46.1088 | 2025-09-14 12:00:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 77.3 |
| f505a52a-6962-34f4-94cd-cadcce118799 | -14.2102 | -46.1979 | 2025-09-14 12:00:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 83.6 |
| 1732b895-cad9-31f1-b35e-9eea21cdd2af | -15.7786 | -53.482 | 2025-09-14 12:00:00 | GOES-19 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 74.0 |
| 928a4513-4bb7-3d2b-bcff-01fceb96bada | -8.9176 | -46.1565 | 2025-09-14 12:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 111.1 |
| 81d9f975-9aa1-3203-8fc0-9e4daa8d53d0 | -8.9079 | -45.457 | 2025-09-14 12:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 96.5 |
| 6c319b97-5fd5-3794-81e9-401b2436ab9e | -13.5876 | -51.6715 | 2025-09-14 12:00:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 89.2 |
| cac9e3cb-e1dc-3534-be8a-b9eecab72877 | -10.7313 | -46.4405 | 2025-09-14 12:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 77.8 |
| 04a666ef-063f-39e0-9c73-71874f4fa153 | -12.8212 | -47.1445 | 2025-09-14 12:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 114.2 |
| 8e70fdca-c637-3e10-a01f-665df9183ed3 | -12.9294 | -54.7333 | 2025-09-14 12:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 94.7 |
| 90325497-00c5-3e85-97f4-3a50a82e27c5 | -10.7503 | -46.4381 | 2025-09-14 12:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 117.2 |
| 752d76a2-a7cc-3d55-9292-1f9df0e07143 | -12.8019 | -47.1474 | 2025-09-14 12:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 69.8 |
| a904c265-8790-34f6-a13d-563063596d32 | -14.329 | -46.0857 | 2025-09-14 12:00:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 140.3 |
| adf6adf4-7142-3635-9bf5-62831966bcb2 | -10.75 | -46.4607 | 2025-09-14 12:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 138.9 |


[Clique aqui para ver as próximas entradas](README76.md)
