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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b6b90740-860f-389b-938c-1e5fc46c8e28 | -7.7252 | -50.3174 | 2025-09-04 01:00:00 | GOES-19 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 82.6 |
| c776e77e-fdf5-3055-819c-49e892590106 | -22.6567 | -43.6825 | 2025-09-04 01:00:00 | GOES-19 | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 110.8 |
| 36006267-13b9-349e-9e12-4f237ca623e0 | -12.9006 | -56.9488 | 2025-09-04 01:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 206.5 |
| b4450a24-a568-340a-bd18-960a7533d7d7 | -13.75 | -46.9346 | 2025-09-04 01:00:00 | GOES-19 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 66.0 |
| 9555313f-7f80-3ea9-bdad-868b92e5ac6a | -12.8818 | -56.9304 | 2025-09-04 01:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 65.9 |
| b774cc3c-d1f3-3536-89d2-c163b55ee66c | -5.9081 | -57.7116 | 2025-09-04 01:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 63.4 |
| 9b4376c2-64c9-35ae-9205-a2e87fc9201e | -6.7782 | -44.0876 | 2025-09-04 01:00:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 113.7 |
| 9c0a4035-3218-3144-965b-439802d693c9 | -12.967 | -54.7705 | 2025-09-04 01:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 46.0 |
| ca15407a-b61b-3c3e-b49c-7fb38bc19565 | -11.5779 | -52.115 | 2025-09-04 01:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 85.5 |
| 65ac35f8-5778-32e1-a369-20dd4f7abbd3 | -12.9199 | -56.927 | 2025-09-04 01:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 46.7 |
| d6887617-5be8-3bd0-b01b-62ef136edae2 | -5.5892 | -45.0278 | 2025-09-04 01:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 137.3 |
| 2254741c-1ec9-31cd-b48f-0e31b2a73631 | -16.4622 | -49.5095 | 2025-09-04 01:00:00 | GOES-19 | CATURAÍ | GOIÁS | Brasil | 5205208 | 52 | 33 | nan | nan | nan | Cerrado | 53.4 |
| 39bdeb41-b6de-33dd-b310-9a0bced573d1 | -12.9009 | -56.9287 | 2025-09-04 01:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 133.1 |
| bccd1b74-34b5-3601-8b65-1c9a55e506a7 | -8.6603 | -68.7657 | 2025-09-04 01:00:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 41.8 |
| eec2fcf2-02fb-3c31-a382-999b34250c02 | -12.4977 | -48.0832 | 2025-09-04 01:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 56.5 |
| e72ef67b-68b8-300f-87c2-77e7dd74e708 | -10.4472 | -50.3713 | 2025-09-04 01:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 149.4 |
| a7d1e0fa-ac66-3859-8ed6-3dc00f8e69d0 | -6.7649 | -63.1292 | 2025-09-04 01:00:00 | GOES-19 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 139.0 |
| 967ca0e4-12d3-3e79-8b30-e2f259db867a | -6.7465 | -63.1297 | 2025-09-04 01:00:00 | GOES-19 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 64.3 |
| 0d1674ff-7473-35d7-8a44-f0de33b7b6db | -11.6601 | -54.5093 | 2025-09-04 01:00:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 41.7 |
| a6e3d9b1-b596-3089-a50c-041a6b74cd58 | -5.8896 | -57.7318 | 2025-09-04 01:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 62.2 |
| a8ecc89e-c8fc-3d21-b106-062efce2aa76 | -10.4469 | -50.3926 | 2025-09-04 01:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 123.0 |
| e8a7bfab-9414-3380-b6b0-1be658146fc2 | -7.7066 | -50.3188 | 2025-09-04 01:00:00 | GOES-19 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 71.1 |
| 694cda66-d8b7-31f3-b36e-335d8069cf27 | -6.1859 | -47.2845 | 2025-09-04 01:00:00 | GOES-19 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 57.7 |
| 4c859382-a723-39cb-a2cb-d57e8a36d709 | -12.9197 | -56.9471 | 2025-09-04 01:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 53.8 |
| 82c6a455-025c-3a9d-8f8d-ebd8862a1a37 | -4.9951 | -56.256 | 2025-09-04 01:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 77.7 |
| c7c39c26-432c-3a7c-b9ab-97290af60574 | -12.9861 | -54.7685 | 2025-09-04 01:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 39.4 |
| 9ab739c0-dc8d-3010-8bfa-a91a32a5b069 | -6.797 | -44.0859 | 2025-09-04 01:00:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 81.0 |
| 7357c30b-261c-3b90-8bc3-edca26a70582 | -5.9079 | -57.7506 | 2025-09-04 01:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 62.3 |
| 2356d692-9296-321b-b9d9-1cdb02af53fc | -12.4981 | -48.061 | 2025-09-04 01:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 82.7 |
| f706467e-8869-3138-87f8-479df9df4b67 | -5.6081 | -45.0038 | 2025-09-04 01:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 97.7 |
| 0afb9e31-f235-3dc9-b6f2-43963a7a276e | -5.6266 | -45.0252 | 2025-09-04 01:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 86.1 |
| a2914df6-ab46-34cc-ba2b-50bad61d25b9 | -6.7648 | -63.1479 | 2025-09-04 01:00:00 | GOES-19 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 66.4 |
| 539047ff-93c0-34b3-a4b7-69fae1093461 | -8.6604 | -68.7473 | 2025-09-04 01:00:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 44.2 |
| e64aabab-558d-39dc-a1ea-fd0d834d9ebf | -11.0565 | -45.1691 | 2025-09-04 01:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 63.6 |
| 2fd4bdc5-28b4-3489-bebf-cd2ac865bdcb | -6.7782 | -44.0876 | 2025-09-04 01:10:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 94.2 |
| b81142b5-647c-3b38-85f9-4c6110ab13f8 | -11.6599 | -54.5297 | 2025-09-04 01:10:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 68.0 |
| e552dd9d-690c-372e-ba80-e95ebadd8847 | -11.5779 | -52.115 | 2025-09-04 01:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 70.1 |
| 448e4b85-7b43-3e7d-8b07-6c39ada937dc | -12.8816 | -56.9505 | 2025-09-04 01:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 80.8 |
| 3f42a75c-1a54-33ae-9f9b-95c559a9139b | -2.962 | -49.3437 | 2025-09-04 01:10:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 61.5 |
| 17818282-66ab-38bb-9b37-76be6ad175ad | -5.6081 | -45.0038 | 2025-09-04 01:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 86.3 |
| cbd00bd0-2721-3a5b-808f-7576d3d51e0f | -12.9199 | -56.927 | 2025-09-04 01:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 35.9 |
| c584a6a1-f846-3c61-a073-96dd68549353 | -5.6266 | -45.0252 | 2025-09-04 01:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 62.4 |
| 4e0b6c0d-2e53-35a3-b0d8-f31fa088eafb | -11.6409 | -54.5315 | 2025-09-04 01:10:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 42.4 |
| 466aabc1-2d1f-3c7e-b3e1-009595da3361 | -20.0979 | -50.0105 | 2025-09-04 01:10:00 | GOES-19 | CARDOSO | SÃO PAULO | Brasil | 3510708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 50.9 |
| a8a8fcd6-2366-3bde-91d7-858aaf4645a4 | -5.5892 | -45.0278 | 2025-09-04 01:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 144.3 |
| 06bbea68-5aac-3912-8378-aa2d91beb38e | -12.9009 | -56.9287 | 2025-09-04 01:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 100.0 |
| 86c6fd61-0f5e-31cf-8446-c438cc42c463 | -10.428 | -50.3946 | 2025-09-04 01:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 65.2 |
| 83c72a7c-bc8d-3460-a43d-a27f346f5736 | -11.6601 | -54.5093 | 2025-09-04 01:10:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 34.5 |
| 6d499c5a-b001-374a-8387-7ec7065ba2c6 | -12.9197 | -56.9471 | 2025-09-04 01:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 46.5 |
| d10e9a48-b4ed-30fa-ae22-f823b2989f72 | -12.8818 | -56.9304 | 2025-09-04 01:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 49.4 |
| 7db72a61-df12-35a3-86cb-2471e28b7a00 | -11.0568 | -45.146 | 2025-09-04 01:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 227.2 |
| 147ad25c-2c8d-3f53-abe1-78fcf19e09a3 | -6.1672 | -47.2858 | 2025-09-04 01:10:00 | GOES-19 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 54.1 |
| 8b729a5f-7f3b-313b-97fa-cd9e87b8c6f8 | -11.0377 | -45.1487 | 2025-09-04 01:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 105.2 |
| d7853971-417a-3fca-975d-1a35e90b30d5 | -11.0565 | -45.1691 | 2025-09-04 01:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 60.6 |
| b10d4dc8-5f08-388f-bb60-8ac9cc1a78a1 | -10.4469 | -50.3926 | 2025-09-04 01:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 104.6 |
| 3a2d78c2-32bc-3eaa-bd6a-6a3f0a730cf7 | -12.9859 | -54.7891 | 2025-09-04 01:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 52.8 |
| 62d59267-c1da-3812-8b02-13b22aa155ba | -5.6079 | -45.0265 | 2025-09-04 01:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 320.9 |
| 27cb67cd-7095-3eb8-b806-0c35ae015c31 | -12.9006 | -56.9488 | 2025-09-04 01:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 156.4 |
| a5ae663f-6851-348e-86b2-6e009ec22faa | -4.9951 | -56.256 | 2025-09-04 01:10:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 91.2 |
| f02998c7-e4b3-3063-87a2-88b19e39181c | -10.4472 | -50.3713 | 2025-09-04 01:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 103.3 |
| 0c417afa-3ded-314a-8580-d6487fd59236 | -11.0572 | -45.123 | 2025-09-04 01:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 65.2 |
| 03105c64-51de-3dd6-af8d-0ce095a50f1c | -6.7649 | -63.1292 | 2025-09-04 01:10:00 | GOES-19 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 69.3 |
| 8c7c3e1c-2217-3a57-8174-060928b0f8d7 | -2.9619 | -49.365 | 2025-09-04 01:10:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 96.3 |
| 56e31dec-26ba-3a8a-95b3-58a81e91bc9e | -22.6567 | -43.6825 | 2025-09-04 01:10:00 | GOES-19 | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 75.4 |
| fff21790-d190-3953-98a9-ab6e70c4b68b | -6.797 | -44.0859 | 2025-09-04 01:10:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 86.7 |
| 2d1bdff6-964f-3eb0-9808-95621d5953a1 | -4.9951 | -56.256 | 2025-09-04 01:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 74.7 |
| 2da4a6ed-4058-3e25-9926-52f481d60b21 | -8.0799 | -45.339 | 2025-09-04 01:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 59.9 |
| 2fae2051-c7d9-3b6e-adb4-e1a274cea878 | -6.797 | -44.0859 | 2025-09-04 01:20:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 81.1 |
| f672f275-4554-393c-adcb-f91a17c663a6 | -5.6081 | -45.0038 | 2025-09-04 01:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 77.2 |
| 81ac394d-79b8-3981-bf91-4127aaafd872 | -10.4472 | -50.3713 | 2025-09-04 01:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 96.1 |
| f6f15fb6-7794-35f8-8a5c-2a53af4bc967 | -5.6079 | -45.0265 | 2025-09-04 01:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 224.9 |
| 91731c71-e6ab-3423-93ad-438037be4add | -10.428 | -50.3946 | 2025-09-04 01:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 67.3 |
| 0dbf5567-8f1f-355e-b636-a146edac8e0d | -5.7924 | -43.2171 | 2025-09-04 01:20:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 69.2 |
| 85105cbc-8d8d-3a34-9312-3ecf75d68bfc | -5.5892 | -45.0278 | 2025-09-04 01:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 88.1 |
| 5fe30183-aa14-352f-9cde-405cdb8f18e5 | -6.7649 | -63.1292 | 2025-09-04 01:20:00 | GOES-19 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 98.5 |
| 124b5ce9-c099-368a-9d48-b31400ac8d94 | -11.0565 | -45.1691 | 2025-09-04 01:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 55.8 |
| 66136251-16af-348a-8833-12913f644f0d | -11.0572 | -45.123 | 2025-09-04 01:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 62.6 |
| abb10f9b-f3dd-396d-a2e0-8a79d40e7b8f | -6.7782 | -44.0876 | 2025-09-04 01:20:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 100.7 |
| ed634646-4a1e-389f-aefb-4253e41f3bd8 | -11.0568 | -45.146 | 2025-09-04 01:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 276.2 |
| fe34e718-5eed-33e7-a434-76a50b68058e | -5.6266 | -45.0252 | 2025-09-04 01:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 73.0 |
| cc442892-a797-389f-8456-813ed8e918c5 | -12.4981 | -48.061 | 2025-09-04 01:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 69.2 |
| 470b2c4c-6319-30ed-9c44-bad85b4ad913 | -10.6124 | -55.3928 | 2025-09-04 01:20:00 | GOES-19 | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 38.8 |
| ba7e5808-224d-3bf9-ae49-f4487acc892a | -10.4469 | -50.3926 | 2025-09-04 01:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 105.8 |
| d2391b48-2bd5-3289-b244-b996cb62228a | -12.9197 | -56.9471 | 2025-09-04 01:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 36.0 |
| 7ecee9ba-4775-38e1-b85f-fa77c71dbc23 | -2.9619 | -49.365 | 2025-09-04 01:20:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 75.9 |
| 2f2d570b-74e0-34b9-be65-d00f549652be | -11.0377 | -45.1487 | 2025-09-04 01:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 81.3 |
| f8a4a857-5630-3892-8b31-2abfbac4dd9a | -12.8816 | -56.9505 | 2025-09-04 01:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 46.1 |
| d25fd8fa-01eb-3e77-b0f7-07d0e07d40ea | -11.5779 | -52.115 | 2025-09-04 01:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 79.1 |
| 2e82a20d-0226-32c8-b34b-b8f0f0405391 | -10.6122 | -55.413 | 2025-09-04 01:20:00 | GOES-19 | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 47.3 |
| cda77878-7383-3d7b-9dc0-b94f94c1e487 | -11.6599 | -54.5297 | 2025-09-04 01:20:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 65.6 |
| 44958eb3-cd88-3dd9-9b59-f70fc580829c | -12.9006 | -56.9488 | 2025-09-04 01:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 119.5 |
| 4917c820-9870-3028-8551-cfc4407b8be5 | -2.962 | -49.3437 | 2025-09-04 01:20:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 51.3 |
| f4ef73e4-f331-338a-bafd-4a9fed487c06 | -12.9009 | -56.9287 | 2025-09-04 01:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 76.2 |
| 01ae056c-65fc-391d-bd4c-1390fd302320 | -13.5727 | -48.1291 | 2025-09-04 01:20:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 68.5 |
| 84785006-7068-3c32-85ba-d7ad0f871ae5 | -6.7833 | -63.1286 | 2025-09-04 01:20:00 | GOES-19 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 64.6 |
| 80c13f83-f777-3752-b616-8f3d1ed5a1c9 | -15.6069 | -52.89507 | 2025-09-04 01:26:00 | TERRA_M-M | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 37.1 |
| a6d30d67-6747-3bd6-8819-500702b9d7d3 | -15.595 | -52.8917 | 2025-09-04 01:26:00 | TERRA_M-M | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 18.3 |
| 14a2776c-92c0-32b3-ac54-c0bb601c361a | -16.815 | -51.33723 | 2025-09-04 01:26:00 | TERRA_M-M | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 31.8 |
| 7014db23-d2ea-3959-a9dc-ce1e6efa5183 | -22.2283 | -55.96822 | 2025-09-04 01:26:00 | TERRA_M-M | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 17cfaf9c-6b52-3e01-bed7-edb7b52e4a8f | -18.14343 | -51.80077 | 2025-09-04 01:26:00 | TERRA_M-M | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 59.8 |


[Clique aqui para ver as próximas entradas](README10.md)
