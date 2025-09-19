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

## Dados Diários - Página 33

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e2f7274d-34f5-37fc-8050-2edbae96e2be | -10.35186 | -47.87177 | 2025-09-19 05:14:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 836c9ffb-f7db-314b-925c-2328df294aa6 | -8.029 | -45.70481 | 2025-09-19 05:14:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 08a20943-6293-3909-a609-b649dcde6439 | -6.51814 | -51.20698 | 2025-09-19 05:14:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 2706a051-66e6-3d4b-9fdd-ac44efce670d | -10.29255 | -50.22104 | 2025-09-19 05:14:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8b95c78e-a671-39ac-a6c5-af7b1beb38ca | -7.57001 | -45.48877 | 2025-09-19 05:14:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 62e1f2c3-c00a-349b-a509-ead5fb42e5a9 | -8.04538 | -45.73568 | 2025-09-19 05:14:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a543b759-801c-3493-96ac-8fdfa406030c | -12.09765 | -44.81422 | 2025-09-19 05:14:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ac33cc39-d9b9-3283-925e-49b9802503f3 | -9.6893 | -46.72636 | 2025-09-19 05:14:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4a18b236-84ed-34fa-ba82-5c237bda28a8 | -6.93008 | -44.75558 | 2025-09-19 05:14:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 15c9f1ae-234a-3811-a3ce-0e416e8282d4 | -7.22975 | -46.60007 | 2025-09-19 05:14:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8a1c0a0a-eaff-3f8d-8317-b01018bf8be4 | -8.0468 | -45.7246 | 2025-09-19 05:14:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 65c79240-2332-306f-a642-35802728ddbc | -6.95884 | -44.75813 | 2025-09-19 05:14:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8982f32e-4f0d-3204-ac2e-91398f1d35d2 | -12.10815 | -44.84954 | 2025-09-19 05:14:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| edcba6c1-197a-39f2-a376-c5fcc6ca62ed | -11.21376 | -49.62825 | 2025-09-19 05:14:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0b025e12-56e1-33d1-a147-fb3d70ff1787 | -8.0397 | -45.72878 | 2025-09-19 05:14:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c43f9978-6f45-3719-b606-43cd8afab884 | -10.29605 | -50.23298 | 2025-09-19 05:14:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| b88e4860-fd86-321a-8d2b-2e741d31f403 | -7.18457 | -44.41882 | 2025-09-19 05:14:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 772cd4b6-8085-3369-8950-ef76a72d569b | -10.29764 | -50.21947 | 2025-09-19 05:14:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| f5f2b480-5232-3fb3-af17-ea5e1cd626cf | -8.02263 | -45.70329 | 2025-09-19 05:14:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7f803eb7-4f54-3a2e-8d33-0a1163e7ee25 | -8.03898 | -45.73447 | 2025-09-19 05:14:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 88e1b9e9-8469-323a-b630-35b0fbe79ffe | -10.96601 | -49.57246 | 2025-09-19 05:14:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bdf23e47-a981-3aa2-8197-254258fed416 | -6.9047 | -44.77113 | 2025-09-19 05:14:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| af81759d-77a1-3e24-88da-daea5c7c7277 | -7.56935 | -45.49381 | 2025-09-19 05:14:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| a0adeaa1-c98a-30f2-a7dc-e854a730fe1e | -7.33171 | -44.57308 | 2025-09-19 05:14:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 0c8421cf-1297-33fb-b385-4c83b8295957 | -8.14535 | -46.78643 | 2025-09-19 05:14:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 7fc7a069-83ca-39a7-a163-5e3e55a75ab7 | -8.01832 | -45.74218 | 2025-09-19 05:14:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4128ad94-f22d-31f8-a86d-822551e6a559 | -7.23578 | -46.60102 | 2025-09-19 05:14:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1581ac72-10fa-3972-8685-3fae6e297c39 | -7.85539 | -45.62601 | 2025-09-19 05:14:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 28a271d9-5d75-3a88-b699-37a85551598a | -5.5464 | -51.36899 | 2025-09-19 05:14:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 984a749d-f0f1-3a1e-b40b-eb65b3ccb4bc | -10.35713 | -47.87677 | 2025-09-19 05:14:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| bd6b1cc6-631f-3b6b-9ab1-50de8e07b674 | -10.29191 | -50.22442 | 2025-09-19 05:14:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| e7298986-7731-3cce-bed5-cecfa4161ca0 | -6.58212 | -45.58799 | 2025-09-19 05:14:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9963d86e-0d32-3bd1-9b56-030dbaca8d34 | -10.29678 | -50.22736 | 2025-09-19 05:14:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 6fc97bf3-0acf-34d8-b38e-8d5585c22868 | -6.51812 | -51.20507 | 2025-09-19 05:14:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| da6b4b11-99aa-38ca-86ad-7801d735dff9 | -8.15263 | -46.7779 | 2025-09-19 05:14:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| cdf8c569-ae78-3501-8352-c6d12a25a7d6 | -7.86831 | -45.62808 | 2025-09-19 05:14:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a66c4934-7dae-3e88-9791-0a904893f775 | -8.01904 | -45.73653 | 2025-09-19 05:14:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 474a78c3-cf08-3eba-88d9-dbb7de761660 | -6.33402 | -56.18373 | 2025-09-19 05:14:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cbdcfb5e-bff9-3a6b-95da-a28300e3f203 | -7.57783 | -45.47963 | 2025-09-19 05:14:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 04d1b635-1738-3ba9-a80d-48716a7aaeb1 | -6.33739 | -56.18427 | 2025-09-19 05:14:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2c5365ff-400a-3515-b4b5-4425ee3802c7 | -12.09832 | -44.80825 | 2025-09-19 05:14:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| de573bbd-d31b-336b-a748-3c0d2dd575c9 | -9.16971 | -45.32176 | 2025-09-19 05:14:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a2b22f10-21cc-37af-9e36-0cc3fbb0eded | -9.14234 | -44.85896 | 2025-09-19 05:14:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 42cb6e8d-31c5-3b6c-ab21-e647389fe101 | -6.58928 | -45.58309 | 2025-09-19 05:14:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2f88e807-e440-383d-88cc-694b22ed9ee6 | -6.90388 | -44.77711 | 2025-09-19 05:14:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 65e58ef6-2388-39b7-9152-62e320ac15ce | -8.03522 | -45.71249 | 2025-09-19 05:14:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0b8752ed-f9f3-30a5-ac53-6c2385989017 | -8.01677 | -45.7025 | 2025-09-19 05:14:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3e996fbd-b9c5-3e7e-b9f1-1e60df58ab60 | -6.33065 | -56.1832 | 2025-09-19 05:14:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6571ef73-fad7-32f0-8cb0-fb902c6f34fd | -10.29114 | -50.23004 | 2025-09-19 05:14:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 4ba48f27-e3b9-39e9-a18f-518d6925cdfd | -10.29037 | -50.23565 | 2025-09-19 05:14:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 7932b280-5ae3-3a7b-a3e7-8ce96ea9cf97 | -6.58023 | -45.58737 | 2025-09-19 05:14:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ff98cbda-996d-3bc0-a58f-ca4f91d1643f | -10.28389 | -50.24619 | 2025-09-19 05:14:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 01a74a39-f776-3939-9d11-b561816d235f | -12.08899 | -44.82694 | 2025-09-19 05:14:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 1da3044b-f22b-3618-8488-d5df0d0dcf3f | -7.71523 | -61.51703 | 2025-09-19 05:14:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e9b0a370-05e3-3625-bd74-0fb6a82f6a76 | -11.2129 | -49.63805 | 2025-09-19 05:14:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7c01c443-b632-3edb-a0d2-1d6109853fb1 | -8.03836 | -45.73297 | 2025-09-19 05:14:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 65898bbc-1e49-33d8-a8e1-2e697b5d37f0 | -7.35818 | -44.5904 | 2025-09-19 05:14:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 40a9e281-8810-372f-830f-d37134025e32 | -12.09138 | -44.83852 | 2025-09-19 05:14:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 33ea0a87-3dc6-3025-bde6-76720913ae92 | -8.01564 | -45.70645 | 2025-09-19 05:14:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f49259cf-7344-3cd5-aece-aec8b6389559 | -10.28465 | -50.24059 | 2025-09-19 05:14:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6c3340f2-49e4-35b2-abdf-ff974ef7fa66 | -8.1344 | -46.77608 | 2025-09-19 05:14:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1e891275-bb44-39e3-817c-793ea7faf90f | -8.13928 | -46.78578 | 2025-09-19 05:14:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| e2524418-98e6-3542-9053-6341f26b46d9 | -9.18386 | -45.31755 | 2025-09-19 05:14:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 2767eb10-6579-3353-92ff-98ccc20f9ce0 | -8.01195 | -45.74073 | 2025-09-19 05:14:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| baa8d4d3-cfd4-3d75-a052-85c60e6a9e42 | -7.57718 | -45.48457 | 2025-09-19 05:14:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 9811e98b-60c4-34e1-8abb-747abae45da4 | -10.04593 | -49.20048 | 2025-09-19 05:14:00 | NPP-375D | MONTE SANTO DO TOCANTINS | TOCANTINS | Brasil | 1713700 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7b44de12-f1de-301c-a701-d9a5fce28eac | -6.51122 | -51.19333 | 2025-09-19 05:14:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5cdf1608-c773-3f34-b8e3-e0ed699a0ffb | -7.57133 | -45.47867 | 2025-09-19 05:14:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 45c402d2-7cdf-329c-9f6f-04cfffe5119f | -9.18311 | -45.32353 | 2025-09-19 05:14:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 42a4ed7c-4425-3e22-b909-079c4611d37e | -7.58369 | -45.48547 | 2025-09-19 05:14:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 10896276-139d-3bc2-84fd-3152d9611e5e | -8.37462 | -44.68262 | 2025-09-19 05:14:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 1f69fab8-c2f7-38df-9635-462046f316fc | -6.33347 | -56.18731 | 2025-09-19 05:14:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b316ae02-a47c-39f1-ad2f-c1934431a72b | -11.21415 | -49.62848 | 2025-09-19 05:14:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 79c32456-0dd8-3d82-ad75-7284e2e04519 | -7.36501 | -44.59152 | 2025-09-19 05:14:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7cd93af9-30f5-3184-b6c2-ae36e6b229ff | -7.54186 | -45.50159 | 2025-09-19 05:14:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e9e2dc60-bebe-325b-ba47-23d2062e06d4 | -8.02881 | -45.71124 | 2025-09-19 05:14:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6e9e0fe2-8642-3cad-a0ab-1cd1146bf07a | -6.51186 | -51.18904 | 2025-09-19 05:14:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 434f6e3e-f56e-3e67-8434-74c8b6b7cd10 | -10.35135 | -47.87584 | 2025-09-19 05:14:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 02d4749a-6372-3829-b038-811fe53c7bdf | -5.86428 | -51.63438 | 2025-09-19 05:14:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 970bf572-86e7-3a00-bfb4-3e96bec89202 | -6.21916 | -55.64075 | 2025-09-19 05:14:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 16f33324-4c96-3570-9872-b8064df30713 | -9.72592 | -45.92478 | 2025-09-19 05:14:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 95f2a0c7-428e-3ad1-8848-d5778f4175a9 | -9.17715 | -45.31669 | 2025-09-19 05:14:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 6.2 |
| f4ea81d8-a90e-3eb8-b659-5cb6e63c892e | -5.90141 | -57.73421 | 2025-09-19 05:14:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ac9bad4f-1b59-387f-ab1d-399fe5c2a409 | -8.37513 | -44.67717 | 2025-09-19 05:14:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 51d75ca8-fb3c-3f45-9a9c-d48ce71bcc8e | -10.29751 | -50.22173 | 2025-09-19 05:14:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 9fa42b4a-c69f-32eb-937e-1725c23308be | -10.2961 | -50.23071 | 2025-09-19 05:14:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 9.7 |
| eb74e2af-065f-3542-bc0b-023a36ac213c | -10.19211 | -59.44566 | 2025-09-19 05:14:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8e6833fe-338d-3422-9e86-b2a929634896 | -6.9006 | -44.77102 | 2025-09-19 05:14:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 81e0dbb4-183b-3c95-92f3-432da9f507fb | -7.84976 | -45.61854 | 2025-09-19 05:14:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 89cfa5ff-0e42-3b24-ae96-1f5e4151042b | -11.21337 | -49.63145 | 2025-09-19 05:14:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 68c8e3c8-9200-32f7-bb28-1cdeda8c8424 | -7.57851 | -45.47451 | 2025-09-19 05:14:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| d2d09985-a70f-358c-aa80-1c884120f2df | -12.10487 | -44.84758 | 2025-09-19 05:14:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5803d147-13ba-374c-8307-a51ad622c5f6 | -7.71899 | -61.51768 | 2025-09-19 05:14:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4f6e281d-71c7-3cf4-a8aa-255169ee14b2 | -10.29182 | -50.22667 | 2025-09-19 05:14:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 15.9 |
| e5289fa5-f27d-3359-99e3-ca3f2140b44e | -11.15831 | -57.19528 | 2025-09-19 05:14:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4ae8b845-7eca-3c08-af2f-581d5211b0b0 | -8.15203 | -46.78248 | 2025-09-19 05:14:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a203dfb2-a13e-36c4-9999-d3799849eab4 | -6.90816 | -44.76567 | 2025-09-19 05:14:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 0f724768-094f-3824-8ff2-1df93ee6c306 | -12.09395 | -44.8473 | 2025-09-19 05:14:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ec957e32-07b5-308a-af1c-0247c1a2c4f3 | -11.21896 | -49.63238 | 2025-09-19 05:14:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 5f88e4a5-0100-32aa-89f5-3e61e386d3fb | -12.0912 | -44.80714 | 2025-09-19 05:14:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |


[Clique aqui para ver as próximas entradas](README34.md)
