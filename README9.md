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
| 2c78bbd9-5274-3ef6-9a65-3b3468ab6dcb | -4.8847 | -45.843201 | 2024-10-20 00:59:30 | METOP-B | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 51692a3b-0c39-3507-9f08-51680d2a527d | -4.8703 | -45.825699 | 2024-10-20 00:59:30 | METOP-B | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 74106f6e-f999-3231-a01c-7b9f21c4c179 | -4.875 | -45.845501 | 2024-10-20 00:59:30 | METOP-B | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 0acd93f1-5963-33f3-9eee-4776d8355ae4 | -4.8606 | -45.828098 | 2024-10-20 00:59:30 | METOP-B | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| e187c84a-f3c0-3733-88b1-079ed703b024 | -4.8653 | -45.8479 | 2024-10-20 00:59:30 | METOP-B | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 13af165b-1ba8-38af-8321-6800d8b48c56 | -4.8314 | -45.8769 | 2024-10-20 00:59:31 | METOP-B | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 200dedf3-8b01-38db-8ffa-a87812fbf3a4 | -4.4566 | -44.754799 | 2024-10-20 00:59:32 | METOP-B | IGARAPÉ GRANDE | MARANHÃO | Brasil | 2105203 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| eb9c97df-d83d-33b9-bdc8-7599c8690d69 | -4.4624 | -44.778599 | 2024-10-20 00:59:32 | METOP-B | IGARAPÉ GRANDE | MARANHÃO | Brasil | 2105203 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 770840d0-2658-3a31-bdbb-a435de4abcb7 | -4.6719 | -45.852699 | 2024-10-20 00:59:33 | METOP-B | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| ceab969a-db91-3427-9694-9febdf576107 | -5.4758 | -50.580299 | 2024-10-20 00:59:38 | METOP-B | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2c7dad66-7adf-3a81-9268-1e84ad160421 | -5.478 | -50.589699 | 2024-10-20 00:59:38 | METOP-B | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bca0e452-8d6a-30c3-a3ed-2562c5e52be8 | -4.8746 | -48.285301 | 2024-10-20 00:59:39 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b969f5c6-2d0d-3c95-bd1b-4edb0de4ebbd | -4.8649 | -48.287601 | 2024-10-20 00:59:39 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 70771459-cdbf-3d38-8d66-f4b3862eba4e | -5.1369 | -50.7178 | 2024-10-20 00:59:44 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3938af04-0fcc-3bdf-8341-e202df099899 | -4.1626 | -46.6315 | 2024-10-20 00:59:44 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| ed82cf25-7b34-3542-8ce3-c62cba6ebfae | -4.1668 | -46.649399 | 2024-10-20 00:59:44 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 77f55f16-e35b-3175-bb5e-fa28686eaeba | -3.8778 | -45.742401 | 2024-10-20 00:59:46 | METOP-B | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 67f2eaaf-cff3-306c-bc1d-641a926cff51 | -3.8828 | -45.763199 | 2024-10-20 00:59:46 | METOP-B | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| afccf8fe-3da8-33c2-82b3-052352c4eea9 | -3.8347 | -45.818401 | 2024-10-20 00:59:47 | METOP-B | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 769f21f0-4d0c-3a89-b305-bab08291d9e3 | -3.8396 | -45.839001 | 2024-10-20 00:59:47 | METOP-B | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 9a9cc823-3b34-3b0a-8083-fa767ed3a917 | -3.825 | -45.820702 | 2024-10-20 00:59:47 | METOP-B | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| dfdb748f-d570-320c-86bf-617774e3bbe9 | -3.8299 | -45.841301 | 2024-10-20 00:59:47 | METOP-B | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 7ab26912-437a-3a2e-9788-aecbce5a0860 | -4.99 | -50.8395 | 2024-10-20 00:59:47 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 278a6137-348a-3b89-8be3-af4bbcce2f56 | -4.0117 | -46.944302 | 2024-10-20 00:59:48 | METOP-B | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 8fd44229-20f4-39ab-b720-0988c85814fa | -4.002 | -46.946602 | 2024-10-20 00:59:48 | METOP-B | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 927dcf3f-bf8b-3c25-93bb-d5c6b1965291 | -4.3119 | -48.557301 | 2024-10-20 00:59:49 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 10cd6362-8640-3c9f-bfc2-5573a6651ebe | -4.315 | -48.5704 | 2024-10-20 00:59:49 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c0c4967e-117f-3e67-b17b-904d13ad8aa0 | -4.3181 | -48.5835 | 2024-10-20 00:59:49 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| aa510656-0fec-3c74-aec6-293e24e4b48a | -4.3052 | -48.572701 | 2024-10-20 00:59:50 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 42f5a015-cf15-30d0-8e6b-be02637386b3 | -4.3047 | -48.614101 | 2024-10-20 00:59:50 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c40bbef0-25a1-3c98-abe1-9bf50a78167e | -4.3077 | -48.626999 | 2024-10-20 00:59:50 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6e87be6e-8d90-368e-9b1c-ba85942b3125 | -4.2949 | -48.616402 | 2024-10-20 00:59:50 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 016c2868-848e-33cd-a258-11a6c1c200c7 | -4.2979 | -48.629299 | 2024-10-20 00:59:50 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 16d059ee-45f9-38d5-b193-3b1151434902 | -3.5102 | -45.8302 | 2024-10-20 00:59:52 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| dfda5b80-bda3-3ff2-9cf3-a6000b70100e | -6.1939 | -57.7673 | 2024-10-20 00:59:53 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f5d4a3b4-9dcc-38ff-92ff-6769a537fc8e | -4.5598 | -50.672298 | 2024-10-20 00:59:53 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f7bc23b2-de4f-34b8-ae88-84a63f5504af | -4.562 | -50.6819 | 2024-10-20 00:59:53 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 908e9a03-12e2-3f32-90d1-4bc92877aaac | -4.4569 | -50.451199 | 2024-10-20 00:59:54 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 246e7afa-5c58-3316-bca6-94103762f91b | -4.4471 | -50.453499 | 2024-10-20 00:59:54 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 328febc1-e3a0-332e-baf8-f36d3650fb19 | -4.4374 | -50.455799 | 2024-10-20 00:59:55 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 04889c40-a908-3344-8cd6-51969bb5a14e | -3.8019 | -48.880199 | 2024-10-20 00:59:59 | METOP-B | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 455ccd52-e662-38d1-beb0-510d92864753 | -3.8048 | -48.892899 | 2024-10-20 00:59:59 | METOP-B | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d0fa4766-08c4-36fe-80cd-1fff052121cb | -3.7892 | -48.869801 | 2024-10-20 00:59:59 | METOP-B | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cfce9e13-f823-3223-a311-cf39646dbf00 | -3.7921 | -48.8825 | 2024-10-20 00:59:59 | METOP-B | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6d674644-495c-38c6-ab7e-605511f03adb | -3.8098 | -48.958099 | 2024-10-20 00:59:59 | METOP-B | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b6548569-c42a-3a72-875d-678c42b7dad5 | -3.8128 | -48.9706 | 2024-10-20 00:59:59 | METOP-B | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4a628fc6-7fa4-3d82-aad3-42e2c97fd527 | -3.8001 | -48.9604 | 2024-10-20 00:59:59 | METOP-B | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a4be3b5f-a3b7-34c8-9095-cc169c4925a2 | -3.8031 | -48.9729 | 2024-10-20 00:59:59 | METOP-B | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 51fdac7c-6dbd-341b-9d91-f139ee7c9378 | -4.2327 | -50.994202 | 2024-10-20 01:00:00 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 055eb1d4-8644-3d9d-8c30-303ee96f9d6e | -4.2207 | -50.987099 | 2024-10-20 01:00:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 79a0e087-6a9c-31c6-8a6f-c209e15170f6 | -4.2229 | -50.996399 | 2024-10-20 01:00:00 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4cf48f72-7cba-3f90-925a-a9fa76cb879b | -4.225 | -51.0056 | 2024-10-20 01:00:00 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4fbbbf5f-189e-3b0d-b21f-602f4e715b73 | -3.8736 | -49.9799 | 2024-10-20 01:00:02 | METOP-B | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fe216a9f-18e2-3668-9dc9-877f8609ef14 | -3.8761 | -49.990601 | 2024-10-20 01:00:02 | METOP-B | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a9a866c7-c920-3430-8949-156b075e33e3 | -3.8786 | -50.001301 | 2024-10-20 01:00:02 | METOP-B | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4f03bced-63d4-32c0-bff3-d873357d953f | -3.8664 | -49.992802 | 2024-10-20 01:00:02 | METOP-B | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 19ae8b74-a5a1-32dc-9bbf-e652d6bd9f0a | -3.6445 | -49.791302 | 2024-10-20 01:00:05 | METOP-B | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8d0bbd9f-6bcb-340c-8796-1b73ca955b73 | -3.6471 | -49.802299 | 2024-10-20 01:00:05 | METOP-B | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e04d2824-1afc-3c42-b46b-e4d028679676 | -3.8223 | -50.689701 | 2024-10-20 01:00:05 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 432443c1-f1aa-3c38-95b5-5f91f9542540 | -3.8373 | -50.9772 | 2024-10-20 01:00:06 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9ed2f30d-c7ca-3a3c-90f1-f6c59bf9b259 | -3.8395 | -50.9865 | 2024-10-20 01:00:06 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8d77d2ba-f7a6-39b5-aee6-e68a7871636e | -3.6952 | -50.718899 | 2024-10-20 01:00:08 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6a220c2a-3d41-3b01-823f-41ad7b9cedac | -3.3806 | -49.540798 | 2024-10-20 01:00:08 | METOP-B | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 72d135a1-1807-37a5-a09e-13d8834fffc8 | -3.3708 | -49.542999 | 2024-10-20 01:00:08 | METOP-B | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d3ac5894-a6aa-3d10-8faf-9fb310168b29 | -3.5293 | -50.313999 | 2024-10-20 01:00:09 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b7167c0a-6b34-30a2-acf3-a6352d397355 | -3.5172 | -50.305901 | 2024-10-20 01:00:09 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ce09c03d-3c31-30a1-960c-47fae20e2092 | -3.5196 | -50.316299 | 2024-10-20 01:00:09 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9877961b-de31-3c8c-b57a-08812d35b7d8 | -3.5806 | -50.5797 | 2024-10-20 01:00:09 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7858cb47-3f39-34dc-b279-9eb8d92138dd | -3.5829 | -50.5896 | 2024-10-20 01:00:09 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6bc4eed6-0cef-3879-901a-b97c59dfe08b | -3.5731 | -50.591801 | 2024-10-20 01:00:09 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 345774ba-9f62-3220-8ddf-b44d52f3e171 | -3.3993 | -49.975201 | 2024-10-20 01:00:10 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 794f0ab1-c081-3562-bd2d-202a4dbe480b | -3.4476 | -50.494099 | 2024-10-20 01:00:11 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1644f0ca-9203-371d-8ac5-3874f240cae7 | -4.7013 | -56.135101 | 2024-10-20 01:00:11 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a2bf91ab-589b-3246-b377-c1a63d9f73d1 | -4.7029 | -56.1422 | 2024-10-20 01:00:11 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b0d98de1-02f4-35b4-af68-e6f88b882b21 | -4.6915 | -56.137199 | 2024-10-20 01:00:11 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f3b760d7-e83b-3bf1-a6c9-b2451056e4b4 | -4.6931 | -56.144299 | 2024-10-20 01:00:11 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 23db48ff-9732-35fe-8f65-c69df00ab158 | -3.5227 | -51.1758 | 2024-10-20 01:00:12 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6e65de62-f9a6-37ce-8acd-ca3904c8b96e | -3.3626 | -50.660801 | 2024-10-20 01:00:13 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8cd04251-67a6-3163-a309-1e6f4a96e5fb | -3.3649 | -50.6707 | 2024-10-20 01:00:13 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 05b458f5-fa98-3041-b2e1-8369a9ab22e9 | -3.3672 | -50.680599 | 2024-10-20 01:00:13 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7b7a3d84-7b06-3224-a3ee-091781eaa3ff | -3.3528 | -50.663101 | 2024-10-20 01:00:13 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9f3ed086-17f5-332e-b5e1-69e04b86f144 | -3.3551 | -50.673 | 2024-10-20 01:00:13 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ff95dde4-e535-384a-9bf7-3255ca65894f | -3.3574 | -50.682899 | 2024-10-20 01:00:13 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5a1b5100-c692-31e1-9c95-6e16971cabc8 | -3.365 | -50.8046 | 2024-10-20 01:00:13 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 985df99b-c676-3bfc-9f66-4b7ad8322a71 | -4.0454 | -53.774101 | 2024-10-20 01:00:13 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4ac18d0a-7563-3475-b7c1-e687f5fae547 | -3.521 | -51.525902 | 2024-10-20 01:00:13 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 253789d2-beca-39c4-8438-5dd9ff4319bb | -3.615 | -52.024399 | 2024-10-20 01:00:14 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8ecf06eb-fd74-3b0d-840d-39ddffac9395 | -3.6169 | -52.0326 | 2024-10-20 01:00:14 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5badc011-649e-3d3c-89f9-03a7786e4fa5 | -2.7684 | -48.677101 | 2024-10-20 01:00:15 | METOP-B | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5131ad2e-0363-3c93-8a37-a066fc73d266 | -2.7715 | -48.690701 | 2024-10-20 01:00:15 | METOP-B | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 01305b59-ebad-3521-a825-95a13142e7ff | -2.7747 | -48.704201 | 2024-10-20 01:00:15 | METOP-B | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 89e95b23-28d2-3f18-bad3-1ba65f38e448 | -2.7586 | -48.679401 | 2024-10-20 01:00:15 | METOP-B | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 83871f1d-55d0-363b-bfcd-9e453a9f0b5e | -2.7617 | -48.693001 | 2024-10-20 01:00:15 | METOP-B | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 84a0f792-f1f8-3c8e-bd50-1e98ed7b06ba | -4.3081 | -55.437599 | 2024-10-20 01:00:15 | METOP-B | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 40e30f72-3c94-34e7-9b92-e3fbccddf7c1 | -4.3096 | -55.444401 | 2024-10-20 01:00:15 | METOP-B | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1d0dc769-3915-3478-b7a0-fedc1622965d | -3.2108 | -50.850101 | 2024-10-20 01:00:16 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 45d6f584-c9b2-330c-b25a-9009c278e65a | -3.7451 | -53.4049 | 2024-10-20 01:00:17 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 109a0ed5-d4c5-3ba6-a5e0-8cc5f70204c9 | -3.7467 | -53.412102 | 2024-10-20 01:00:17 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2250e030-8569-3bb5-94e7-ea74669d0ffa | -3.4074 | -52.062698 | 2024-10-20 01:00:17 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 326715f6-e5af-3d27-83d2-36dbc5447fc9 | -2.7577 | -49.292999 | 2024-10-20 01:00:17 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README10.md)
