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
| a41fa654-e2f2-31bd-a887-f7c7b0040e24 | -10.0728 | -51.6349 | 2026-05-31 01:10:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 90.8 |
| 77dc2323-042c-397d-b855-8baa6d5ca3ce | -10.0534 | -51.6786 | 2026-05-31 01:20:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 115.0 |
| d8153229-22c9-3ef8-a1c3-cc481ecdc3a7 | -7.9949 | -55.5169 | 2026-05-31 01:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 79.2 |
| e7048f41-e3af-3a62-b734-4077ec4f1871 | -10.0723 | -51.6769 | 2026-05-31 01:20:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 220.3 |
| 2171ecef-d231-353e-b0fc-cc1c0c1ffedb | -8.7211 | -48.3222 | 2026-05-31 01:20:00 | GOES-19 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 48.3 |
| 1cdaff00-7871-3982-8850-16c46a589390 | -10.0728 | -51.6349 | 2026-05-31 01:20:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 80.7 |
| 281de16b-9153-3a73-97d8-40cc513a1111 | -10.0537 | -51.6576 | 2026-05-31 01:20:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 120.0 |
| 5c1a071a-6490-334d-9839-76dcc73ee90a | -8.7399 | -48.3205 | 2026-05-31 01:20:00 | GOES-19 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 80.5 |
| 63166f60-096f-30f7-bec1-2f800c3cd7d9 | -10.0725 | -51.6559 | 2026-05-31 01:20:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 314.1 |
| 6f1f9a3e-8c9c-3ac1-89d3-a477fbeb663f | -10.0725 | -51.6559 | 2026-05-31 01:30:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 275.7 |
| 531d1fbe-1084-38c8-8d02-9b91760678c6 | -10.0534 | -51.6786 | 2026-05-31 01:30:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 114.5 |
| db0eee27-675e-3539-a7b4-d5c6ed4feb01 | -8.7211 | -48.3222 | 2026-05-31 01:30:00 | GOES-19 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 58.1 |
| 286c4efd-7504-37de-9ba3-30eb0c434879 | -10.0728 | -51.6349 | 2026-05-31 01:30:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 71.6 |
| 755e8303-2cfc-34e6-a56b-cc369c37e587 | -10.0723 | -51.6769 | 2026-05-31 01:30:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 187.5 |
| 54815abe-5bd2-3ac1-ab2e-4939be12be65 | -10.0537 | -51.6576 | 2026-05-31 01:30:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 146.0 |
| d0199b7a-26ec-340f-9ad6-567a9429a3be | -8.7399 | -48.3205 | 2026-05-31 01:30:00 | GOES-19 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 77.9 |
| c9e06669-6537-343b-ba26-9ac409d89a61 | -10.0723 | -51.6769 | 2026-05-31 01:40:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 155.8 |
| cc9852eb-c54e-381c-8fc9-42a5a2559941 | -10.0728 | -51.6349 | 2026-05-31 01:40:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 70.8 |
| 22586b92-7dc1-3471-a1ed-b2ebb994bcb9 | -10.0534 | -51.6786 | 2026-05-31 01:40:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 110.2 |
| 5eedd0c0-f26e-3368-847f-a658d18bc0a1 | -10.0537 | -51.6576 | 2026-05-31 01:40:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 148.6 |
| 3d3cfecb-6ed0-3681-92f1-139a60e2ec9f | -10.0725 | -51.6559 | 2026-05-31 01:40:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 241.1 |
| 279223d9-01ce-311b-a5da-9a567cb2f00f | -10.0914 | -51.6541 | 2026-05-31 01:40:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 71.5 |
| 52104c64-7eff-3880-8c99-0430b37db14f | -10.0723 | -51.6769 | 2026-05-31 01:50:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 160.4 |
| 5d11ebc4-8b88-3ea4-905e-10f442669265 | -10.0537 | -51.6576 | 2026-05-31 01:50:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 115.7 |
| 4ebf190d-2c75-340f-99e0-64206c206d74 | -10.0725 | -51.6559 | 2026-05-31 01:50:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 239.5 |
| 78e05556-e07c-3d2e-a564-cb34bebb8853 | -8.7399 | -48.3205 | 2026-05-31 01:50:00 | GOES-19 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 52.3 |
| 6b9dd8ac-991f-3a3a-8c35-5d1e0cd7b90d | -10.0534 | -51.6786 | 2026-05-31 01:50:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 105.4 |
| 9ec43570-be0c-3dd7-84a6-d0fc16f6b89b | -10.0728 | -51.6349 | 2026-05-31 01:50:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 73.0 |
| 5a5ad917-5800-339c-ac2d-ffb0abdaa3bb | -10.0725 | -51.6559 | 2026-05-31 02:00:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 231.5 |
| 052b3309-5d4d-33d3-9bfc-d9b4947b25f9 | -10.0534 | -51.6786 | 2026-05-31 02:00:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 112.4 |
| 69e34f91-7424-3f5c-b2ef-5845787b41a3 | -10.0723 | -51.6769 | 2026-05-31 02:00:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 155.9 |
| d6fcd754-4044-3e36-bb32-27a6cd819f66 | -10.0537 | -51.6576 | 2026-05-31 02:00:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 121.4 |
| 37a8978a-ef4f-3806-9b5b-a1085e9e0c80 | -10.0723 | -51.6769 | 2026-05-31 02:10:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 157.8 |
| fbeee110-599e-3249-aabb-033da497c33a | -10.0534 | -51.6786 | 2026-05-31 02:10:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 84.4 |
| 9b477a35-2066-36aa-87c2-f144261e3d00 | -10.0537 | -51.6576 | 2026-05-31 02:10:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 103.8 |
| fb7acb66-f9d6-39b2-8221-e29c6ff1679c | -10.0725 | -51.6559 | 2026-05-31 02:10:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 257.4 |
| 92162f02-6093-3f54-a59c-dd85345cd638 | -10.0728 | -51.6349 | 2026-05-31 02:10:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 77.6 |
| 57632bdf-ac52-3d6c-9a20-874b7b57c390 | -10.0728 | -51.6349 | 2026-05-31 02:20:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 71.8 |
| 73a9a9f5-460f-37d0-85e5-1c619d5a2470 | -10.0537 | -51.6576 | 2026-05-31 02:20:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 101.9 |
| ffd7e138-fad8-3f85-8f00-eccdc1ddc147 | -10.0723 | -51.6769 | 2026-05-31 02:20:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 161.4 |
| a316aaa5-a92a-3451-8e4d-ec49351b2430 | -10.0534 | -51.6786 | 2026-05-31 02:20:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 84.1 |
| a10aeb14-f8da-3f8a-8c82-59b62436d928 | -10.0725 | -51.6559 | 2026-05-31 02:20:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 248.2 |
| d6bf7860-333f-3ef1-af2e-b5d5d6e517a4 | -10.0534 | -51.6786 | 2026-05-31 02:30:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 90.2 |
| f680c9e6-3f23-3e9c-8053-f47e43fa17bc | -10.0725 | -51.6559 | 2026-05-31 02:30:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 221.4 |
| 889d4881-56f9-35c6-abcf-fbfe1c06e6ab | -10.0723 | -51.6769 | 2026-05-31 02:30:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 150.0 |
| 0b97e2cd-8284-33a4-89df-e246330f4e00 | -10.0537 | -51.6576 | 2026-05-31 02:30:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 93.3 |
| d8a6410d-5fbd-371f-8598-022c33a4500e | -10.0534 | -51.6786 | 2026-05-31 02:40:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 79.4 |
| a299e299-3cda-33b6-aa19-8fb12659ffe5 | -10.0537 | -51.6576 | 2026-05-31 02:40:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 97.1 |
| 19ba3236-cd53-39da-9ce5-520c8ad9415f | -10.0728 | -51.6349 | 2026-05-31 02:40:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 68.4 |
| c34ab31a-ef4e-3175-ade6-d5a14470e2f0 | -10.0723 | -51.6769 | 2026-05-31 02:40:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 131.1 |
| 4906164a-0c58-382a-b870-6336362a5dd1 | -10.0725 | -51.6559 | 2026-05-31 02:40:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 206.0 |
| 5e11e764-779f-30fa-b59a-b2e7272c4113 | -10.0534 | -51.6786 | 2026-05-31 02:50:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 79.7 |
| 6c9ee89b-fe8e-33cd-9a09-3821ed80ba3c | -10.0723 | -51.6769 | 2026-05-31 02:50:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 137.1 |
| af5a1b71-d648-345c-859c-6b8f932d8b4d | -10.0537 | -51.6576 | 2026-05-31 02:50:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 79.0 |
| d3422e82-357a-325f-b082-d2110f19c575 | -10.0725 | -51.6559 | 2026-05-31 02:50:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 187.3 |
| 8a435b11-c6a0-3f05-9178-a025077ce532 | -10.0537 | -51.6576 | 2026-05-31 03:00:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 79.0 |
| 68a0ad95-dc32-38ca-b856-13bf3e425181 | -10.0534 | -51.6786 | 2026-05-31 03:00:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 68.8 |
| 9a8de2d3-e4e3-3e1f-bcee-e73a8956df08 | -10.0723 | -51.6769 | 2026-05-31 03:00:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 120.4 |
| e54e35f4-c921-393c-8ca5-c5f421e4ee5e | -10.0725 | -51.6559 | 2026-05-31 03:00:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 179.1 |
| c9e62ec3-6952-3981-86b4-7a7e0f860c1c | -10.0534 | -51.6786 | 2026-05-31 03:10:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 67.5 |
| 08617a80-7082-32cb-8570-edc12dfe07ab | -10.0537 | -51.6576 | 2026-05-31 03:10:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 74.5 |
| 1c2bea0c-71dc-39d7-8c37-4fe2a14bdf1d | -10.0725 | -51.6559 | 2026-05-31 03:10:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 145.4 |
| f74d9154-50c7-39b1-b370-118dbe0cb47b | -10.0723 | -51.6769 | 2026-05-31 03:10:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 106.6 |
| 87f51da7-c4b8-38a9-b5a8-c0aca4b6f543 | -10.0725 | -51.6559 | 2026-05-31 03:20:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 165.6 |
| 24a0aa4c-f29f-3ea1-baa8-28da2783bffc | -10.0723 | -51.6769 | 2026-05-31 03:20:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 115.1 |
| 749f9674-10cc-3027-8a82-4ab14b067c1d | -10.0537 | -51.6576 | 2026-05-31 03:20:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 77.3 |
| f3feacd4-0698-31a6-81a5-d3f081e84b62 | -10.0534 | -51.6786 | 2026-05-31 03:20:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 70.8 |
| 72d1ccd8-340e-3c16-b51f-a4d32cb5b62b | -10.0537 | -51.6576 | 2026-05-31 03:30:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 88.2 |
| 454d4c7e-9d07-3dd2-9a48-d1f17e4710dd | -10.0723 | -51.6769 | 2026-05-31 03:30:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 108.4 |
| b227aad2-1b5c-3563-b928-d467aae3dbca | -10.0534 | -51.6786 | 2026-05-31 03:30:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 75.6 |
| 4c24f4d7-6c13-379d-86f4-f08504d18071 | -10.0725 | -51.6559 | 2026-05-31 03:30:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 144.3 |
| abfcc6f9-40fb-3211-bef3-cd7fda1e6e51 | -10.0723 | -51.6769 | 2026-05-31 03:40:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 103.1 |
| 863b53eb-e49a-3b3e-99c9-fef287c858f0 | -10.0725 | -51.6559 | 2026-05-31 03:40:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 161.3 |
| af9f7235-4554-37a1-a323-7ce5fd8979e9 | -10.0534 | -51.6786 | 2026-05-31 03:40:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 73.3 |
| 076f1e0c-0bd6-3eb0-9f23-d6eac7634fbf | -10.0537 | -51.6576 | 2026-05-31 03:40:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 84.1 |
| 507e838d-4617-3a99-aeff-4c3c818b80f9 | -5.80387 | -45.13085 | 2026-05-31 03:42:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| bdde5384-40e1-360e-b2af-f075b383a18f | -5.80174 | -45.13083 | 2026-05-31 03:42:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 074687f5-ad9a-38f6-86f9-4f686c7ea6d3 | -5.61201 | -37.53088 | 2026-05-31 03:42:00 | NOAA-21 | CARAÚBAS | RIO GRANDE DO NORTE | Brasil | 2402303 | 24 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 1fa3dacd-2174-3665-9e2e-78d6c8ebc862 | -5.52108 | -37.62294 | 2026-05-31 03:42:00 | NOAA-21 | FELIPE GUERRA | RIO GRANDE DO NORTE | Brasil | 2403707 | 24 | 33 | nan | nan | nan | Caatinga | 1.0 |
| cf49ab15-17f0-3abf-bb0b-445ce5321790 | -5.49536 | -37.24585 | 2026-05-31 03:42:00 | NOAA-21 | UPANEMA | RIO GRANDE DO NORTE | Brasil | 2414605 | 24 | 33 | nan | nan | nan | Caatinga | 0.8 |
| aee73508-0070-359b-900d-a1853155f693 | -10.14324 | -48.08098 | 2026-05-31 03:45:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 72b8c06e-5891-3bcc-9a3e-dab138f4624a | -8.26429 | -43.93045 | 2026-05-31 03:45:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 67008251-f0e4-33ca-afa6-d23302328027 | -8.26937 | -43.9311 | 2026-05-31 03:45:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b8426388-8750-3aaf-9cbd-094ccd159b11 | -10.63257 | -48.32927 | 2026-05-31 03:45:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0e69c606-d7f1-319b-9a23-b1f7986ce6e4 | -8.99703 | -37.60624 | 2026-05-31 03:45:00 | NOAA-21 | MATA GRANDE | ALAGOAS | Brasil | 2705002 | 27 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 9acfc639-7cc3-34cf-a536-ffd271bb3d9c | -6.84158 | -47.93877 | 2026-05-31 03:45:00 | NOAA-21 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c954a0fb-fef7-317d-96ca-14bc72028816 | -9.49184 | -48.65903 | 2026-05-31 03:45:00 | NOAA-21 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 226264aa-cc2e-3620-8668-a4faad41c9c0 | -6.04501 | -47.8953 | 2026-05-31 03:45:00 | NOAA-21 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ab5f8235-0af0-3d76-9e44-49364587f5fd | -13.55544 | -43.59254 | 2026-05-31 03:45:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 99236ca5-6c5c-3599-8134-699305d5a2c8 | -8.08556 | -39.55806 | 2026-05-31 03:45:00 | NOAA-21 | PARNAMIRIM | PERNAMBUCO | Brasil | 2610400 | 26 | 33 | nan | nan | nan | Caatinga | 1.2 |
| c361bc4e-cdfa-33ff-aad8-48d7e05a94bc | -8.27041 | -43.93012 | 2026-05-31 03:45:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f9e34d7a-037d-3f12-be94-229b9137d5dc | -6.99394 | -42.88183 | 2026-05-31 03:45:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 3abb4c3a-d53c-3d8d-b81d-48d9733a50d0 | -8.26532 | -43.9295 | 2026-05-31 03:45:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 1ff8ada6-f1e2-3f0a-85a8-6393d955140b | -6.84271 | -47.93268 | 2026-05-31 03:45:00 | NOAA-21 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| abac9778-aec6-3235-acf2-af47a6fb2e12 | -8.2583 | -48.23762 | 2026-05-31 03:45:00 | NOAA-21 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| d7d9f850-771b-3cc5-8d95-e9d45618b869 | -10.63366 | -48.32381 | 2026-05-31 03:45:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b92ae2b7-28ca-3e79-8cc5-e9bf33ac346d | -9.41593 | -40.37181 | 2026-05-31 03:45:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 6c29815f-0614-3b61-8a32-4e077fb6f89d | -8.08935 | -39.55869 | 2026-05-31 03:45:00 | NOAA-21 | PARNAMIRIM | PERNAMBUCO | Brasil | 2610400 | 26 | 33 | nan | nan | nan | Caatinga | 1.2 |
| b6d12bda-4f59-3fbf-a961-9c9ff59d6ade | -8.26483 | -43.92744 | 2026-05-31 03:45:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| ce98e6fc-b214-3c01-b196-26cfdf0a28d6 | -8.25942 | -48.23183 | 2026-05-31 03:45:00 | NOAA-21 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |


[Clique aqui para ver as próximas entradas](README4.md)
