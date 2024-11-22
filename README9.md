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
| 772117e1-5f0c-34b3-9fd7-36c31e58f1c4 | -3.82748 | -52.26937 | 2024-11-22 01:06:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| af53a64e-12c4-386b-b8ca-c00ddf4ae302 | -0.91618 | -51.74131 | 2024-11-22 01:06:00 | TERRA_M-M | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 54a42b02-a032-3be2-9f2f-044ec5d1859d | -3.5215 | -53.7872 | 2024-11-22 01:06:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 3b38465b-74e7-337e-952a-e3054cb34d96 | -1.61432 | -52.58987 | 2024-11-22 01:06:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 20.0 |
| 071ae0df-df7c-3f3f-831d-902d9b862294 | -4.63961 | -49.54045 | 2024-11-22 01:06:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 14.7 |
| af35cd4e-7453-3554-8688-56e0a4820ff8 | -0.05369 | -51.23558 | 2024-11-22 01:06:00 | TERRA_M-M | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 68.0 |
| f978db28-312b-3e42-808d-cae3edb8f8d3 | 1.38264 | -55.94221 | 2024-11-22 01:09:00 | TERRA_M-M | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 16.5 |
| d6c43b85-36c8-3ba0-8623-75934a36f0ef | 2.33849 | -51.6541 | 2024-11-22 01:09:00 | TERRA_M-M | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 5.6 |
| aed47c44-46bb-3afa-a58f-d6f85aac946f | 1.90436 | -55.87753 | 2024-11-22 01:09:00 | TERRA_M-M | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 14.2 |
| c3da425c-ae4f-3bcc-9f10-d57841912926 | 0.57496 | -50.82019 | 2024-11-22 01:09:00 | TERRA_M-M | ITAUBAL | AMAPÁ | Brasil | 1600253 | 16 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 0896c28d-8ef1-3655-a041-7ace0b28ff78 | 0.46541 | -51.34884 | 2024-11-22 01:09:00 | TERRA_M-M | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 15552da0-fdce-318f-93f1-086e43684ca2 | 2.38004 | -50.76439 | 2024-11-22 01:09:00 | TERRA_M-M | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 14.4 |
| c928ff0e-1b11-3e65-87b8-7bd77223fd0a | 0.87304 | -54.63308 | 2024-11-22 01:09:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| bc760d10-08f9-3220-ba96-9da7bb5cda5f | 1.36983 | -55.96263 | 2024-11-22 01:09:00 | TERRA_M-M | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 92.2 |
| a52f07f7-15ac-394a-97ed-a750238c7b2f | 0.57634 | -50.81026 | 2024-11-22 01:09:00 | TERRA_M-M | ITAUBAL | AMAPÁ | Brasil | 1600253 | 16 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 26945412-de2e-363f-b489-b754475cee0d | 3.68321 | -51.39185 | 2024-11-22 01:09:00 | TERRA_M-M | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 262dd172-6eb5-394f-aa15-3326009af5bd | 1.35851 | -55.9722 | 2024-11-22 01:09:00 | TERRA_M-M | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 32.5 |
| f5458f1f-4941-3b26-83fb-8a8559dc2704 | 1.90286 | -55.8881 | 2024-11-22 01:09:00 | TERRA_M-M | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 26199b95-cfa6-3934-b93d-bb1f139bc37b | 1.36678 | -55.98449 | 2024-11-22 01:09:00 | TERRA_M-M | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| ad550afe-22be-38ce-910c-e6e82f712a6e | 0.75644 | -50.24413 | 2024-11-22 01:09:00 | TERRA_M-M | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 8268d68d-7ee6-3bd0-a35c-5eed9bfefc5a | 1.36831 | -55.97356 | 2024-11-22 01:09:00 | TERRA_M-M | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 46.1 |
| f68aca66-218c-391b-b889-ae533975ee07 | 3.68461 | -51.3818 | 2024-11-22 01:09:00 | TERRA_M-M | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 69b9ba5d-aae8-36d9-ba60-38e46734ed59 | 1.38113 | -55.95311 | 2024-11-22 01:09:00 | TERRA_M-M | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 43.6 |
| 047d5202-3caa-3e2f-b378-cc1148d7ff2d | 1.37136 | -55.95172 | 2024-11-22 01:09:00 | TERRA_M-M | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 77.4 |
| b708a051-230b-3336-ace4-6d785a191417 | 1.40831 | -55.91854 | 2024-11-22 01:09:00 | TERRA_M-M | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| f08cef8c-d35f-3d5d-8711-0b72ac34a981 | 0.46674 | -51.33943 | 2024-11-22 01:09:00 | TERRA_M-M | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 21.1 |
| a2a7bfa4-efe5-3f73-94fe-a4a8a02347fe | -3.4592 | -45.9104 | 2024-11-22 01:10:00 | GOES-16 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 105.0 |
| 473ecc96-4def-3f8f-9f5e-82be4ca0c653 | -3.4778 | -45.9096 | 2024-11-22 01:10:00 | GOES-16 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 66.2 |
| 236aaad1-73b4-3963-8e60-e38d148e9dd6 | -3.8355 | -52.2576 | 2024-11-22 01:10:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 75.5 |
| 01fd8af0-fdf7-3f17-a202-9e340c035823 | -1.1103 | -53.3953 | 2024-11-22 01:10:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 68.1 |
| 32af2872-ef78-38a9-9ae7-ab4508b1cef6 | -2.504 | -54.1397 | 2024-11-22 01:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 59.9 |
| 9c7d6cb9-4dcf-3ccc-97c0-6c7fed70dac2 | -5.9557 | -48.0425 | 2024-11-22 01:10:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 52.8 |
| 82b0e18a-57eb-314e-b53c-e6fae49487f6 | -1.1857 | -51.9685 | 2024-11-22 01:10:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 58.1 |
| d2a12b47-4aa5-3dee-a685-d853cd16f763 | -3.3452 | -50.4917 | 2024-11-22 01:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 102.4 |
| ee985eb9-d7c6-3c30-896c-319eae044385 | -1.1857 | -51.948 | 2024-11-22 01:10:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 99.3 |
| d4d4b5b2-4c87-3acf-9ce3-121e2f82063d | -1.2041 | -51.9683 | 2024-11-22 01:10:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 96.1 |
| 19725a52-7f06-307d-8f2a-3825651d8edb | -3.2055 | -48.5885 | 2024-11-22 01:10:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 49.4 |
| b9be165f-9ec9-3361-823a-2695b862c037 | -3.1831 | -54.3247 | 2024-11-22 01:10:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 85.2 |
| 909de5e8-87d3-3c47-a883-b4e56b3490c9 | -3.516 | -53.793 | 2024-11-22 01:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 99.3 |
| abe5afbe-cc0f-31a6-8c37-744066b65f94 | -3.4976 | -53.7935 | 2024-11-22 01:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 87.9 |
| 80d7b71b-04f8-32e5-a909-2c9edf91c001 | 1.3636 | -55.9654 | 2024-11-22 01:10:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 64.5 |
| 8e9a66ce-bfd5-3190-b90f-d099f293c47a | -2.3549 | -48.5493 | 2024-11-22 01:10:00 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 40.8 |
| 391ccda8-8d1d-3c18-85f7-c845f1f621ae | -1.2042 | -51.9272 | 2024-11-22 01:10:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 43.6 |
| d0a231a2-144b-30b4-8d9c-bbc61dfb25c7 | -1.1287 | -53.4153 | 2024-11-22 01:10:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 62.1 |
| 8848d383-b36c-3c21-ba99-8a65a0f367e0 | -3.4975 | -53.8137 | 2024-11-22 01:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 104.0 |
| 8d12eac3-bbbb-38c9-b825-c3fe4ef27079 | -4.2424 | -48.6334 | 2024-11-22 01:10:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 90.6 |
| c2379158-18a4-3fa7-9cdf-92a254c7183f | -3.3451 | -50.5126 | 2024-11-22 01:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 108.7 |
| 645e1008-5bee-300c-8702-06477d30614f | -3.7554 | -46.1204 | 2024-11-22 01:10:00 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 146.6 |
| 04a66e9b-dca4-39d8-9c8c-e2ebbc760e10 | -2.504 | -54.1598 | 2024-11-22 01:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 62.3 |
| e4b55b60-4a2d-3afa-ae24-c5b7d4ff3405 | -3.5159 | -53.8132 | 2024-11-22 01:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 112.9 |
| dc41660a-ff82-3e9a-a4bb-5fb280e00482 | -3.774 | -46.1196 | 2024-11-22 01:10:00 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 88.7 |
| 33691326-abdc-36e9-bc45-f31b3ae9301a | -5.9556 | -48.0642 | 2024-11-22 01:10:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 56.5 |
| aa544f15-7542-376b-aa4e-a1d2fd0fed80 | -1.2041 | -51.9478 | 2024-11-22 01:10:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 162.3 |
| 0009c723-7a64-32e7-ba51-1d12e9bd88f7 | -1.1287 | -53.3951 | 2024-11-22 01:10:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 91.5 |
| b555252d-0ddb-3d94-afd0-50e7dc9d92ad | -3.3451 | -50.5126 | 2024-11-22 01:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 115.8 |
| 0dee36f6-85c4-38e0-b39c-a05c4233a41f | -3.8355 | -52.2576 | 2024-11-22 01:20:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 75.5 |
| 2898c1f3-4801-3da3-afe5-974e0e387bb0 | -3.3452 | -50.4917 | 2024-11-22 01:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 89.2 |
| 6634703c-bcd4-38ad-b979-d592bdb66feb | -3.1831 | -54.3247 | 2024-11-22 01:20:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 86.5 |
| 8ac4f24c-dba8-3a17-8d0d-cdefed76648b | -3.2943 | -45.447 | 2024-11-22 01:20:00 | GOES-16 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 54.8 |
| ad784b96-d8a2-317c-a367-f8107bc3daeb | -3.7554 | -46.1204 | 2024-11-22 01:20:00 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 128.4 |
| b9dff16b-9ae8-39f3-8dc0-1b5ab1cfa092 | -3.5159 | -53.8132 | 2024-11-22 01:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 120.8 |
| a06fb515-26fd-3d32-9390-e0487444514a | -1.1857 | -51.948 | 2024-11-22 01:20:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 74.5 |
| 1fec2f5d-6111-3fbb-bad2-9f988bf7f4aa | -3.4976 | -53.7935 | 2024-11-22 01:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 94.5 |
| 81f069c4-e64c-38a7-9686-84acc252b0ed | -1.1103 | -53.3953 | 2024-11-22 01:20:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 83.6 |
| 7dc94f28-dfb2-315b-a1e0-09d3f7be7a9e | -3.4592 | -45.9104 | 2024-11-22 01:20:00 | GOES-16 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 106.4 |
| c4c6fff5-6301-3a85-9596-577e6845d18b | -1.2041 | -51.9478 | 2024-11-22 01:20:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 106.5 |
| 1877f57a-1bfd-3524-a072-16398490cd01 | -1.1287 | -53.3951 | 2024-11-22 01:20:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 99.8 |
| 2e4bcf9e-fb19-3b44-b521-1db741314c9c | -2.504 | -54.1598 | 2024-11-22 01:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 55.8 |
| 37754eec-4f76-3594-a3eb-7c1a4ed28d54 | -2.3549 | -48.5493 | 2024-11-22 01:20:00 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 48.1 |
| 54d76f29-87c5-3b2d-84fe-4e93f91147a2 | -3.4975 | -53.8137 | 2024-11-22 01:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 97.3 |
| bb8fda60-5a5f-355d-808a-9476def75f34 | -3.516 | -53.793 | 2024-11-22 01:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 105.6 |
| 1d551a3f-afc8-34c1-83d4-0a64ff4e70c7 | -1.2041 | -51.9683 | 2024-11-22 01:20:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 82.9 |
| 5d7584b6-22e5-3f00-b00b-3b2a953ffcc2 | -4.2424 | -48.6334 | 2024-11-22 01:20:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 78.9 |
| ed9b9186-b7b2-39db-95d9-9c999829b886 | -1.2041 | -51.9683 | 2024-11-22 01:30:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 62.8 |
| 4ffdcc02-4a48-3276-8f8e-de082d6df67e | -1.5266 | -47.0497 | 2024-11-22 01:30:00 | GOES-16 | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 52.2 |
| b440956f-4cbc-331c-aee8-b6ed53310404 | -3.5159 | -53.8132 | 2024-11-22 01:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 110.6 |
| c5a01613-1875-345d-b3e8-8e93a83402b0 | -1.1287 | -53.3951 | 2024-11-22 01:30:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 97.0 |
| f4b6bca6-6df0-3d06-a1e5-1e4ac2c71f73 | -3.3451 | -50.5126 | 2024-11-22 01:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 77.6 |
| 6abfc227-1935-3892-8cd4-3cf82cf90040 | -2.504 | -54.1598 | 2024-11-22 01:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 43.1 |
| 19b346af-913d-342b-bfd7-b0fcea9d723c | -3.4975 | -53.8137 | 2024-11-22 01:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 91.2 |
| 31837370-5e52-3609-b28b-feac438cd771 | -3.3452 | -50.4917 | 2024-11-22 01:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 77.7 |
| d520683c-6dab-3c0e-867a-4d2dacb88ddf | -3.1831 | -54.3247 | 2024-11-22 01:30:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 82.7 |
| f83d727c-03b3-3f81-a695-8f5b170bb1b2 | -3.4778 | -45.9096 | 2024-11-22 01:30:00 | GOES-16 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 72.0 |
| 96cc3f60-ee53-34dc-bf8b-157df095b518 | -3.7554 | -46.1204 | 2024-11-22 01:30:00 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 113.1 |
| 94f4a92a-7a0d-3226-9410-85e8d2b8636d | -1.2041 | -51.9478 | 2024-11-22 01:30:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 95.6 |
| 43eda8e7-ad27-30fa-b345-ee75d990607c | -3.4976 | -53.7935 | 2024-11-22 01:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 78.1 |
| 7c409f98-adf3-3947-be04-8cc3ac296e86 | -1.1287 | -53.4153 | 2024-11-22 01:30:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 64.9 |
| 0b71f834-dfb9-34cd-a9a2-ec31bd98e10f | -1.5265 | -47.0716 | 2024-11-22 01:30:00 | GOES-16 | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 57.8 |
| 773e420d-b0ac-3431-b909-232a62b68882 | -3.516 | -53.793 | 2024-11-22 01:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 94.2 |
| 287afdcc-baea-31f0-a82b-476ad7e60e8b | -1.1857 | -51.948 | 2024-11-22 01:30:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 63.2 |
| a25248df-97fe-3809-897a-a1e3099edeb1 | -2.5223 | -54.1594 | 2024-11-22 01:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 36.9 |
| 8a331a9a-beaf-3495-96b8-9d665229781c | -4.2424 | -48.6334 | 2024-11-22 01:30:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 81.3 |
| e40fd59a-6f58-37ae-a4f8-e2d1ac70304c | -3.774 | -46.1196 | 2024-11-22 01:30:00 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 84.3 |
| 3c52957e-6173-32f6-bc7d-33d98e712eec | -3.4592 | -45.9104 | 2024-11-22 01:30:00 | GOES-16 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 107.0 |
| be66cf4d-23b9-3c8d-882a-44688e636722 | -1.1103 | -53.3953 | 2024-11-22 01:30:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 70.0 |
| 09e5a1e8-81e4-3ec7-8293-df1e3d5bbc2d | -2.9983 | -45.1433 | 2024-11-22 01:40:00 | GOES-16 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 56.2 |
| a8944e77-892c-3762-b104-cf3520813ee7 | -3.4778 | -45.9096 | 2024-11-22 01:40:00 | GOES-16 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 70.2 |
| d9521a72-0b03-329d-a991-c99d2c470a1b | -3.4975 | -53.8137 | 2024-11-22 01:40:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 82.0 |
| 5a83f514-ab68-3bd4-81ce-880f52a84bb9 | -3.774 | -46.1196 | 2024-11-22 01:40:00 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 75.7 |
| 2548c4f2-4070-3252-a893-f8c1459b177e | -3.3451 | -50.5126 | 2024-11-22 01:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 102.8 |


[Clique aqui para ver as próximas entradas](README10.md)
