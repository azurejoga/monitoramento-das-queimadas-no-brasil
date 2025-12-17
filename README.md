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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dedb625a-8233-3d1d-9202-2ca4fc7db1ae | -3.3126 | -45.4912 | 2025-12-17 00:00:00 | GOES-19 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 71.9 |
| b55f6828-2ff2-3104-8888-ac51d415f5f7 | -3.3125 | -45.5136 | 2025-12-17 00:00:00 | GOES-19 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 98.4 |
| 092b517c-1320-3993-a57b-f8d0341bf823 | -2.4204 | -45.6343 | 2025-12-17 00:00:00 | GOES-19 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 123.9 |
| 7317f8ce-3e78-3738-b212-388285c71340 | -3.2939 | -45.5144 | 2025-12-17 00:00:00 | GOES-19 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 53.3 |
| 42979d0d-84cb-3855-bace-f7a0ce3f6f81 | -3.3502 | -45.4223 | 2025-12-17 00:00:00 | GOES-19 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 60.7 |
| 6662b889-db53-37c5-9027-a576c71b8df7 | -2.4203 | -45.6567 | 2025-12-17 00:00:00 | GOES-19 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 49.5 |
| 70633e69-1ab7-3652-a5a3-7d3420c3ac88 | -2.9875 | -52.3859 | 2025-12-17 00:00:00 | GOES-19 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 96.3 |
| c73c46d6-6068-3586-b893-82f0172b0a74 | -10.1002 | -36.4721 | 2025-12-17 00:00:00 | GOES-19 | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Caatinga | 46.0 |
| 5f2f65c0-825e-303f-9dbe-4b2804f66977 | -2.4017 | -45.6573 | 2025-12-17 00:00:00 | GOES-19 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 60.1 |
| 4e006ebd-6fb1-3c54-a289-17b9b63f1cc0 | -3.313 | -45.4238 | 2025-12-17 00:00:00 | GOES-19 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 59.4 |
| 5c1008e7-ff29-35de-a400-8c62fbaa213b | -3.3311 | -45.5129 | 2025-12-17 00:00:00 | GOES-19 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 48.3 |
| a35eebdc-2c6a-3867-8f49-99440663a805 | -0.7077 | -51.9931 | 2025-12-17 00:00:00 | GOES-19 | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 65.2 |
| 74fafdb3-ad41-3b99-b27d-fe530963fc88 | -2.4019 | -45.6125 | 2025-12-17 00:00:00 | GOES-19 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 74.4 |
| b883688e-ec01-3fc5-b08b-db5635bef982 | -2.9876 | -52.3654 | 2025-12-17 00:00:00 | GOES-19 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 104.1 |
| e6780a32-2707-3b05-afd1-09e06326075a | -2.4205 | -45.6119 | 2025-12-17 00:00:00 | GOES-19 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 60.7 |
| fcf11b18-7c29-3686-9be8-46ed74014278 | -3.0345 | -45.3447 | 2025-12-17 00:00:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 60.1 |
| 06083f11-7332-3f8b-8444-2be56f82cf23 | -3.3317 | -45.4005 | 2025-12-17 00:00:00 | GOES-19 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 61.7 |
| 803b93d9-78ff-3145-b749-2672dc7093ac | -3.3316 | -45.423 | 2025-12-17 00:00:00 | GOES-19 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 142.2 |
| 2db01178-1549-397a-aa5c-8526395fd69a | -2.4018 | -45.6349 | 2025-12-17 00:00:00 | GOES-19 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 166.6 |
| 66d69185-e6fb-384d-a389-0d972ffce691 | -3.3316 | -45.423 | 2025-12-17 00:10:00 | GOES-19 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 140.2 |
| 9cbc3b2f-2196-3e64-a786-4a727e433f09 | -3.3125 | -45.5136 | 2025-12-17 00:10:00 | GOES-19 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 113.6 |
| fa9f415a-78f9-399c-8f09-ec644c3c6d0b | -2.9876 | -52.3654 | 2025-12-17 00:10:00 | GOES-19 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 103.7 |
| b83ba0bc-9305-3ab4-9ffe-6a695168fdee | -3.3126 | -45.4912 | 2025-12-17 00:10:00 | GOES-19 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 103.3 |
| d7d04462-404c-342e-ae2e-3e5ddf57369a | -2.4204 | -45.6343 | 2025-12-17 00:10:00 | GOES-19 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 70.1 |
| e2653819-bde2-3123-ab8c-a427d19bac81 | -3.294 | -45.4919 | 2025-12-17 00:10:00 | GOES-19 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 56.6 |
| 4d0a1c08-3f1d-32ae-bd60-b76d58c3899d | -2.3632 | -51.9084 | 2025-12-17 00:10:00 | GOES-19 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 71.0 |
| 71669185-65dd-33cc-b668-667b831c83a3 | -0.7077 | -51.9931 | 2025-12-17 00:10:00 | GOES-19 | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 67.0 |
| 1790b448-d1ed-3957-b0dc-95f739ca07d4 | -3.3317 | -45.4005 | 2025-12-17 00:10:00 | GOES-19 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 63.8 |
| b64af0db-1525-3385-8b6b-5a3563c0eb4a | -2.4018 | -45.6349 | 2025-12-17 00:10:00 | GOES-19 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 99.4 |
| a51fc3d7-a9b6-37a0-8f68-802fec7530dc | -2.9875 | -52.3859 | 2025-12-17 00:10:00 | GOES-19 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 72.9 |
| 85e0e281-372e-37c1-8dc8-f1da9b6aab89 | -3.2939 | -45.5144 | 2025-12-17 00:10:00 | GOES-19 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 57.1 |
| b1108d68-7df9-3341-b82b-ce22ebfaddb3 | -3.0345 | -45.3447 | 2025-12-17 00:10:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 52.9 |
| 47529fc1-1f42-3012-b724-e2d70ff62c0b | -1.4175 | -46.0589 | 2025-12-17 00:10:00 | GOES-19 | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 49.1 |
| 0f5bc82b-a0a3-39e8-bdc6-f2eaaad562bf | -3.313 | -45.4238 | 2025-12-17 00:10:00 | GOES-19 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 63.6 |
| ce6d485b-043f-304e-962b-2fe0b0fb814c | -2.3816 | -51.908 | 2025-12-17 00:10:00 | GOES-19 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 62.4 |
| ec85ba64-51a1-3f27-80e2-28af839d68b1 | -3.3502 | -45.4223 | 2025-12-17 00:10:00 | GOES-19 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 71.9 |
| 0a7b5640-b7b6-34cd-a230-363a6534db86 | -7.2168 | -43.0853 | 2025-12-17 00:14:00 | METOP-B | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 94112b60-5bc6-32a9-baa4-eec4a7efcb92 | -3.1289 | -54.161598 | 2025-12-17 00:14:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2fd206ef-f4a3-39ef-aec8-729fccb3c668 | -2.9877 | -49.108898 | 2025-12-17 00:14:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fecb6a72-ebed-3af8-8823-94dda09458f2 | -2.9833 | -52.365501 | 2025-12-17 00:14:00 | METOP-B | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a9a2dd7c-8a5d-3e84-85b5-8c1255260b61 | -1.4206 | -52.555801 | 2025-12-17 00:14:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1a0d5f9b-af01-3215-acaf-5def366a5e24 | -2.8921 | -49.5037 | 2025-12-17 00:14:00 | METOP-B | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cceedcde-25c3-3641-9ddd-3d35a38bd733 | -2.0539 | -50.712601 | 2025-12-17 00:14:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 56d4a1f3-5f9d-372a-bfc0-1577d7df7c7c | -3.8573 | -40.444698 | 2025-12-17 00:14:00 | METOP-B | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| bbdaecf9-c948-3f2b-9a48-ba31550cb386 | -3.8348 | -47.051102 | 2025-12-17 00:14:00 | METOP-B | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 90b00610-d3bb-32a1-871e-bf7d18815807 | -3.3347 | -45.4259 | 2025-12-17 00:14:00 | METOP-B | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 249ffd00-43b6-3c26-872c-e681c99661bc | -0.9905 | -47.129799 | 2025-12-17 00:14:00 | METOP-B | PRIMAVERA | PARÁ | Brasil | 1506104 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2431a18d-bcfb-3735-941e-d083a903a98c | -2.1255 | -46.246799 | 2025-12-17 00:14:00 | METOP-B | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| c5514a7e-1982-3cd7-882d-e3ffcd893f6b | -2.4872 | -49.309399 | 2025-12-17 00:14:00 | METOP-B | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| eb758090-b6a5-3022-bd54-39046c766933 | -2.3748 | -51.9034 | 2025-12-17 00:14:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cc58605b-6ea6-3f24-9355-770e85faf6af | -12.6674 | -46.767799 | 2025-12-17 00:14:00 | METOP-B | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5ede27b6-af00-3a73-b088-011a23a7f280 | -2.9073 | -49.1637 | 2025-12-17 00:14:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4a8974ff-b2de-3edf-93a8-e0e4e93df6e8 | -2.8971 | -45.579601 | 2025-12-17 00:14:00 | METOP-B | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 592c9996-89e9-3c5e-a8e3-aa6d679027bc | -2.8223 | -49.197601 | 2025-12-17 00:14:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3ebf44ea-d9ab-3b88-98c6-24a63cd973a4 | -2.6959 | -51.638302 | 2025-12-17 00:14:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 65567e87-5c62-3811-a0f2-982ecb6748a6 | -1.7753 | -53.9445 | 2025-12-17 00:14:00 | METOP-B | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7d917ddc-435a-37cc-aa3a-960a71dffeec | -3.3 | -45.4977 | 2025-12-17 00:14:00 | METOP-B | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 77739e0d-9837-3b1f-9356-bef706cda0f4 | -2.0443 | -45.4496 | 2025-12-17 00:14:00 | METOP-B | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 598afe66-9f64-34d7-a626-f5f801312035 | -2.4856 | -49.302399 | 2025-12-17 00:14:00 | METOP-B | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0e0aa2eb-7fec-3dee-a0e1-b853c7076845 | -4.2914 | -45.600399 | 2025-12-17 00:14:00 | METOP-B | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| cb5ee11c-18c0-3ed2-85a7-586a5ecc66db | -3.8193 | -48.870098 | 2025-12-17 00:14:00 | METOP-B | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9ca12af9-c01a-365a-b7ca-00df58219d75 | -2.1749 | -53.8475 | 2025-12-17 00:14:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 68845f15-8eb4-346d-ad33-1ac0ba591af8 | -3.8177 | -48.863098 | 2025-12-17 00:14:00 | METOP-B | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9377851a-5b36-3781-befb-076ef52aea7f | -4.3974 | -45.746201 | 2025-12-17 00:14:00 | METOP-B | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| c25e72df-3cff-35b2-9d96-cc3541859cea | -2.4477 | -48.865101 | 2025-12-17 00:14:00 | METOP-B | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 405d656a-b932-37aa-baeb-6075ee4cdc58 | -3.2194 | -49.357399 | 2025-12-17 00:14:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9a15fc10-24a8-3e86-bec2-7516bc3cc03b | -4.3877 | -45.748402 | 2025-12-17 00:14:00 | METOP-B | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| d81660c9-a832-3899-abbf-2d8ac0819e4d | -6.1839 | -39.711201 | 2025-12-17 00:14:00 | METOP-B | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 325d658b-f17f-3329-9b81-ef4df333f678 | -2.4044 | -45.628502 | 2025-12-17 00:14:00 | METOP-B | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| debc8d4e-4f37-3733-be0f-0d0f9c63af6f | -4.3899 | -45.757702 | 2025-12-17 00:14:00 | METOP-B | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 07332941-3a33-3e28-889d-3dc04a1fa18e | -3.4 | -49.2001 | 2025-12-17 00:14:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 37bcf546-7a44-3bda-a6a3-cfc160a32004 | -2.0095 | -46.011398 | 2025-12-17 00:14:00 | METOP-B | MARACAÇUMÉ | MARANHÃO | Brasil | 2106326 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 56b376ad-c161-363a-b8e9-6f8c88bb6073 | -3.3225 | -45.418098 | 2025-12-17 00:14:00 | METOP-B | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| e29e5a7c-a562-3a34-a327-b8d29eb11238 | -5.4358 | -43.512798 | 2025-12-17 00:14:00 | METOP-B | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 83ce9f10-abc8-3b60-9e29-7e293982bf5a | -5.4718 | -45.407001 | 2025-12-17 00:14:00 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ac0bc1b3-b945-3c14-9088-e368d5a9cb0a | -2.6943 | -51.631199 | 2025-12-17 00:14:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2692b890-6b8f-3517-913e-0537d29b4908 | -4.4297 | -46.283501 | 2025-12-17 00:14:00 | METOP-B | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| c28f60af-4424-3b1f-b86a-76b9ec9498e1 | -2.3905 | -49.382401 | 2025-12-17 00:14:00 | METOP-B | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d07652f6-91f2-3e8c-a6a2-bf92c7aaf608 | -3.3097 | -45.495499 | 2025-12-17 00:14:00 | METOP-B | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| af77a32e-78b8-3acc-a394-19b8e98d4293 | -2.3764 | -51.9105 | 2025-12-17 00:14:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8afe2cd0-2c2e-3e90-aa57-1397fb8de72d | -0.9925 | -47.1385 | 2025-12-17 00:14:00 | METOP-B | PRIMAVERA | PARÁ | Brasil | 1506104 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bc7fd174-4421-378f-820e-5d7a8e575957 | -3.312 | -45.505501 | 2025-12-17 00:14:00 | METOP-B | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 6b8f59b6-c10e-3bba-a16a-2c603cbfb37c | -3.2178 | -49.350498 | 2025-12-17 00:14:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4a617e9d-e8a6-3362-8313-57fd74292014 | -7.2266 | -43.082901 | 2025-12-17 00:14:00 | METOP-B | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 42b40620-c56d-3929-b617-639a5e5e4e7e | -3.1651 | -50.2066 | 2025-12-17 00:14:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| aff24fbd-9160-36aa-817a-824c75d86d76 | -1.3256 | -45.809601 | 2025-12-17 00:14:00 | METOP-B | LUÍS DOMINGUES | MARANHÃO | Brasil | 2106201 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 7db730f0-5d10-397c-a3c7-27a6a9f8ca43 | -1.7772 | -53.952999 | 2025-12-17 00:14:00 | METOP-B | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 837edd1a-c985-3713-abfc-637bbeda4911 | -1.816 | -54.0341 | 2025-12-17 00:14:00 | METOP-B | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d248c111-6c61-375d-b597-c3fbad0bfb74 | -3.3073 | -45.485401 | 2025-12-17 00:14:00 | METOP-B | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 7a616b21-d741-3c88-ad56-805e4aa69fa7 | -3.33 | -45.405602 | 2025-12-17 00:14:00 | METOP-B | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 9bebbb39-815b-3677-9688-18f95f3a19f1 | -2.0321 | -45.4412 | 2025-12-17 00:14:00 | METOP-B | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| fe9010db-2e42-395f-9754-f89521b5b0f5 | -0.7043 | -51.9841 | 2025-12-17 00:14:00 | METOP-B | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 093ecf88-727f-31ca-abae-d5d327eb2328 | -3.3249 | -45.4282 | 2025-12-17 00:14:00 | METOP-B | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| ba356bf7-f224-3d7d-9618-11435be49eba | -4.4277 | -46.2747 | 2025-12-17 00:14:00 | METOP-B | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| c2a838da-9335-39d7-b13b-0d1e6085ca52 | -2.985 | -52.372898 | 2025-12-17 00:14:00 | METOP-B | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 69170cd2-34e7-3aff-b1ff-1ac7f601b5d5 | -2.8046 | -51.800598 | 2025-12-17 00:14:00 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 61983474-b545-3291-906d-3a945636e172 | -2.7057 | -51.636101 | 2025-12-17 00:14:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4ae62da1-e192-34ee-b084-9f623e2cdcef | -3.0181 | -45.347599 | 2025-12-17 00:14:00 | METOP-B | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 0f1102d5-1292-329c-98dc-1a1a66a38393 | -2.1768 | -53.855999 | 2025-12-17 00:14:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 27437623-7d15-32d0-969d-6e2060a27121 | -2.9931 | -52.3633 | 2025-12-17 00:14:00 | METOP-B | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README2.md)
