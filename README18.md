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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 44625e4c-ced5-3f41-9f88-017ccedc3135 | -4.60615 | -45.61189 | 2025-08-14 04:46:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 0.2 |
| 0fe2f16c-625e-334e-a166-b60761c09272 | -2.49274 | -47.56934 | 2025-08-14 04:46:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| bb425b37-c4fb-3c32-8851-fff9781e8e72 | -6.9464 | -44.54977 | 2025-08-14 04:46:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c7ac0346-525a-37e6-bb49-191eefb6ac02 | -7.35179 | -46.25581 | 2025-08-14 04:46:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d8291c83-0d7d-3425-ba2e-48f8290f5cf0 | -3.99929 | -47.07877 | 2025-08-14 04:46:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ab341902-8507-31c2-9ca3-14bb37fd5262 | -5.98199 | -44.14769 | 2025-08-14 04:46:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 6719d21a-1c6b-306c-865d-1a86416feda4 | -4.14529 | -38.27352 | 2025-08-14 04:46:00 | NPP-375D | CASCAVEL | CEARÁ | Brasil | 2303501 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| b8d5fe4d-6b29-3898-ba93-eb31025f8c24 | -6.95084 | -44.55058 | 2025-08-14 04:46:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 7c56f74b-dd2f-303e-baa8-ad2347ef5283 | -3.91468 | -46.4514 | 2025-08-14 04:46:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e2526651-4ace-3f1e-9a4b-68d92a554cdf | -2.48863 | -47.57269 | 2025-08-14 04:46:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 15b136cb-312f-3dd9-9a8d-01d464d5dce0 | -6.99768 | -45.62013 | 2025-08-14 04:46:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 5e101e38-1198-378e-ba4c-191bcfc1b6cd | -7.25724 | -46.05602 | 2025-08-14 04:46:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cdb6c5df-55f0-3a72-ac89-ab3f75f78069 | -2.90598 | -48.25295 | 2025-08-14 04:46:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 21711fb3-a6de-3f3c-9993-0582b45b7981 | -6.18889 | -43.31242 | 2025-08-14 04:46:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e8f288f1-23dc-33a0-a238-1e006fbbf890 | -3.82001 | -41.56092 | 2025-08-14 04:46:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| a51b7c90-f751-3a7b-b9fd-c67a6c7f3d9b | -4.22792 | -47.21395 | 2025-08-14 04:46:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6a17ed7d-ca67-3964-bda0-b5b0e8a56c23 | -5.8896 | -57.73976 | 2025-08-14 04:46:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 45c0efa7-df3b-3a39-9fa8-f47a0e6e9926 | -4.146 | -38.26842 | 2025-08-14 04:46:00 | NPP-375D | CASCAVEL | CEARÁ | Brasil | 2303501 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| d03b8420-ce4d-37ed-90a7-5155d5869e0a | -6.9515 | -44.54601 | 2025-08-14 04:46:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 16.6 |
| f5a4eb9f-4364-3143-890a-0e908f4abc4d | -6.5482 | -44.01509 | 2025-08-14 04:46:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7da78b39-ba63-3f9c-ac83-7fd7370dd9aa | -4.06493 | -47.98144 | 2025-08-14 04:46:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c3cfaf07-143d-3647-9996-933ba0ce9df4 | -2.37087 | -51.91205 | 2025-08-14 04:46:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cc3b1cd6-623c-3409-837c-f4887ad295d9 | -6.95018 | -44.55514 | 2025-08-14 04:46:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 93e794cc-eed8-38a6-af6a-f6e3ec97149a | -6.43841 | -45.9091 | 2025-08-14 04:46:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 79085eeb-9f90-3d3e-b1dc-d110f13d8114 | -5.88424 | -57.74355 | 2025-08-14 04:46:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 00dd9523-6611-3282-a2f0-14de534e59c9 | -4.77656 | -45.33136 | 2025-08-14 04:46:00 | NPP-375D | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| e18c15cc-e545-31ba-a765-1e57ce7393f0 | -6.18411 | -43.31154 | 2025-08-14 04:46:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5aee0975-f660-3b03-a833-384a92a78d48 | -6.21342 | -43.33861 | 2025-08-14 04:46:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d80fd677-27b0-3ace-939e-f804e15b4d0c | -4.06553 | -47.97755 | 2025-08-14 04:46:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d838e85f-a0d3-3cba-b7c0-657f01dd4ea5 | -5.19102 | -50.64601 | 2025-08-14 04:46:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| be3dda99-ba89-3e9a-bace-e264a69eca86 | -2.48803 | -47.57658 | 2025-08-14 04:46:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d861e98b-850c-315f-8527-0c9c0a0dfd43 | -2.90655 | -48.24927 | 2025-08-14 04:46:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8f1ec48c-3413-3664-8bfe-752ea79f892d | -7.13338 | -44.22337 | 2025-08-14 04:46:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f66ffdc5-0751-3a3f-a010-f9781b8cd35a | -4.59974 | -43.31125 | 2025-08-14 04:46:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 038b47da-9ae7-3a9f-a008-1c33172a05af | -3.82047 | -41.55774 | 2025-08-14 04:46:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 0e153f5b-dcb3-399f-80e1-d6d768be3035 | -6.90734 | -45.21128 | 2025-08-14 04:46:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a1034047-4dc9-369b-b736-56df13adc6c8 | -6.61744 | -43.88515 | 2025-08-14 04:46:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 5e441a88-5ed1-3147-8140-bbed86e4dc58 | -3.82094 | -41.55455 | 2025-08-14 04:46:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 60043e7f-8713-3ff8-9c38-7af9008ef14d | -2.91281 | -48.29935 | 2025-08-14 04:46:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 17.9 |
| dd458f25-6618-33e2-bb50-7fd400f21fe4 | -5.75438 | -46.66761 | 2025-08-14 04:46:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8ffeedad-b640-34e3-ad3d-f6c0f6dab2db | -2.90256 | -48.25242 | 2025-08-14 04:46:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8d34449a-7576-33f9-8c99-470af10ce1b7 | -4.29775 | -48.05946 | 2025-08-14 04:46:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 36a4ca9c-63b3-3d1b-a96a-5e3b93d22c11 | -5.88461 | -43.92562 | 2025-08-14 04:46:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 657843bf-c4c1-33b6-b074-e6394f6dc758 | -5.47181 | -36.78716 | 2025-08-14 04:46:00 | NPP-375D | IPANGUAÇU | RIO GRANDE DO NORTE | Brasil | 2404705 | 24 | 33 | nan | nan | nan | Caatinga | 3.8 |
| dd682d4b-a7a3-3d1f-b77c-f1d8f19e594c | -3.91432 | -46.45447 | 2025-08-14 04:46:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| fc2080e0-92a6-33c5-a43c-1df1aa93e636 | -6.94574 | -44.55437 | 2025-08-14 04:46:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 9db64465-ae2c-3277-bcf8-16792c92d4f6 | -4.06843 | -47.98198 | 2025-08-14 04:46:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6049d9cd-39f4-3477-835d-7da3e8bc9c3e | -5.88886 | -57.74424 | 2025-08-14 04:46:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 95c9f48f-177c-3124-ac3c-3cc5d33d567c | -8.26446 | -45.05835 | 2025-08-14 04:49:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4eb56213-b574-37f7-84a7-bc110edd1c80 | -6.87613 | -59.15283 | 2025-08-14 04:49:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| d87e9927-4629-396d-b237-81064f484f4f | -7.33812 | -60.62414 | 2025-08-14 04:49:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 66b36ed5-5b71-3311-92cf-a64a82bf6fa6 | -7.38552 | -56.69046 | 2025-08-14 04:49:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 26487bc8-d07d-3556-ab31-620c00228fa6 | -5.74576 | -59.87045 | 2025-08-14 04:49:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 05135e1c-411f-37f7-a4a7-f2e97122e94a | -7.3157 | -60.62245 | 2025-08-14 04:49:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| aa66cd35-4fd7-3894-9c83-c214b86ef8f1 | -7.32596 | -60.62815 | 2025-08-14 04:49:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 2f28c4e5-5c8c-3a29-b3de-e0694e841643 | -6.88209 | -59.14811 | 2025-08-14 04:49:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| b380307c-e07b-3ce7-8764-6b1dca85e498 | -5.73852 | -59.89595 | 2025-08-14 04:49:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b1722b1e-3ffb-31f1-b0f2-549f8f738858 | -7.12793 | -60.12724 | 2025-08-14 04:49:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0128c4f7-5e4a-3293-b297-19811a194f89 | -6.53339 | -56.2066 | 2025-08-14 04:49:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5b9510c2-ba4e-3c0c-b190-4527f5a4167e | -5.76223 | -59.88631 | 2025-08-14 04:49:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6ec83b84-e995-3ba0-bc01-0864da1776b8 | -5.73967 | -59.88949 | 2025-08-14 04:49:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5575a144-f780-390b-a24e-4e4d86895593 | -6.53277 | -56.21028 | 2025-08-14 04:49:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7683c77a-bacd-30d2-82de-ecabbc49a0b2 | -5.73374 | -59.8919 | 2025-08-14 04:49:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4ab0539f-2aea-33b9-ac8f-bb03cf1b2d47 | -6.86079 | -59.96798 | 2025-08-14 04:49:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| aa4c33fa-c9f9-3dad-b7b6-2c2df1b3f3aa | -7.12108 | -59.41595 | 2025-08-14 04:49:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9e94dec1-3982-3ab5-a695-a632e08ed47a | -6.11063 | -59.92619 | 2025-08-14 04:49:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6a23f05d-2912-3618-b7f9-80318159d9c4 | -6.0982 | -59.93451 | 2025-08-14 04:49:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 50431b8a-53de-3cb4-8ad6-b92ed876e4d3 | -6.88601 | -59.88624 | 2025-08-14 04:49:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b380133f-76ea-3916-bc64-bba37d214912 | -6.89106 | -59.15556 | 2025-08-14 04:49:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 16.9 |
| d981040a-d80c-3686-a721-3a539ee6ecaf | -5.74979 | -59.89445 | 2025-08-14 04:49:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 792f1e0e-3466-3afb-aea7-4d2dbab2fc38 | -7.42399 | -60.03436 | 2025-08-14 04:49:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0963e859-8640-3624-ae59-ca69c20342fb | -5.76106 | -59.89293 | 2025-08-14 04:49:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cc25dc3e-2644-3858-99cd-4c804891d645 | -5.74182 | -59.89359 | 2025-08-14 04:49:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f433b723-f857-3baf-8dce-b793434ba11d | -6.09646 | -59.94442 | 2025-08-14 04:49:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f1dd308e-7e0d-34e9-b8ba-a4c50d996659 | -6.79025 | -58.78602 | 2025-08-14 04:49:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 41f78ac7-2fb6-34b9-ae98-3e5c8da869eb | -6.10413 | -59.93199 | 2025-08-14 04:49:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b1e2ee11-deaa-35da-a68c-5c40cf807e5a | -7.46078 | -59.88948 | 2025-08-14 04:49:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 759f075e-f34c-3259-94e6-c1ca5f638a44 | -7.32723 | -60.62087 | 2025-08-14 04:49:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 12dcd699-2257-3c0b-bcd2-b5623507521a | -6.08754 | -59.93275 | 2025-08-14 04:49:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6c7cbe48-9652-3e83-92c2-40b2d4ecf943 | -7.32112 | -60.62471 | 2025-08-14 04:49:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 84073180-d70d-3da5-978d-f066dafb11c9 | -6.89004 | -59.13208 | 2025-08-14 04:49:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 99119fad-d29d-3f44-839a-e4793aa5a837 | -5.73986 | -59.87289 | 2025-08-14 04:49:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f7a0315e-6831-3517-986c-cad49fe72468 | -7.91997 | -45.9067 | 2025-08-14 04:49:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 68170e9a-f665-383a-a70f-b7d818514836 | -7.26343 | -60.63113 | 2025-08-14 04:49:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a251a7f8-c1b2-3961-acec-db38bb9ffe60 | -6.54344 | -56.19696 | 2025-08-14 04:49:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 72171821-7af5-3dce-95fb-db5fe70e282b | -7.09265 | -60.02572 | 2025-08-14 04:49:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4b68c912-4413-3721-b4e1-aad2ac1aa0c4 | -7.23748 | -57.64724 | 2025-08-14 04:49:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2c6cecef-ea59-306b-8f8d-960a0a03b55c | -6.89204 | -59.14994 | 2025-08-14 04:49:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 50e5df56-df39-340f-aea4-fde8cdef9635 | -5.74238 | -59.89032 | 2025-08-14 04:49:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1899a594-7fd9-3e2d-920f-ef7358f33f32 | -7.12889 | -59.63718 | 2025-08-14 04:49:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cb3ef80e-c445-34aa-995b-3970b97b1455 | -7.2547 | -59.98917 | 2025-08-14 04:49:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 371ae68d-6435-3581-ace8-2260c7453c20 | -7.09321 | -60.02248 | 2025-08-14 04:49:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 55b00490-c172-362a-b893-4001641b20d0 | -5.73592 | -59.89595 | 2025-08-14 04:49:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 572a5d5f-01a9-3373-9c70-7896d56d7c0d | -6.13614 | -57.82865 | 2025-08-14 04:49:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 82e0b872-a6ba-3463-b8ce-8819890e632f | -6.79229 | -58.7872 | 2025-08-14 04:49:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 43f5f1bd-5902-3e0c-91ba-7b47d3e63394 | -7.42501 | -60.0327 | 2025-08-14 04:49:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 222abce5-4b21-3517-9d47-1b56fc244931 | -6.88407 | -59.13688 | 2025-08-14 04:49:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4390484c-a8aa-31f9-94a2-15698cbf11b9 | -7.12028 | -59.62614 | 2025-08-14 04:49:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c93b4220-4d51-301a-978f-951c2449d953 | -6.89501 | -59.13298 | 2025-08-14 04:49:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 360287c6-ef6c-34da-b5ed-2154f36b3e15 | -6.90794 | -59.14703 | 2025-08-14 04:49:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 13.2 |


[Clique aqui para ver as próximas entradas](README19.md)
