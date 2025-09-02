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

## Dados Diários - Página 87

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a447a925-478c-3a0f-adea-4f64574015c3 | -17.90192 | -47.16405 | 2025-09-02 06:16:00 | AQUA_M-M | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 22.2 |
| 7b720562-d779-319e-a6de-83cc729b674a | -17.89043 | -47.15545 | 2025-09-02 06:16:00 | AQUA_M-M | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 15.7 |
| e1b05af4-9a43-34e1-bda3-42dfd0d48317 | -17.88909 | -47.16228 | 2025-09-02 06:16:00 | AQUA_M-M | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 603141ed-d41d-3301-a958-d8ba1398d860 | -11.1037 | -44.6315 | 2025-09-02 06:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 60.6 |
| 567fd537-d51d-3d01-8fd3-f375e87c9fa8 | -11.1033 | -44.6548 | 2025-09-02 06:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 62.5 |
| b83636af-0f34-3136-986a-34838fe54f58 | -10.0623 | -48.0978 | 2025-09-02 06:20:00 | GOES-19 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 63.0 |
| 5933b20b-ec0f-3200-b31c-2d3cdf803392 | -11.1037 | -44.6315 | 2025-09-02 06:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 61.6 |
| 988b62b2-8017-34fb-a8d1-2c07d987bb11 | -15.5661 | -48.3694 | 2025-09-02 06:30:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 38.2 |
| 5095a6b3-8e7f-31a4-b69f-32c6879a1a2c | -11.1033 | -44.6548 | 2025-09-02 06:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 66.8 |
| 59df763d-1e1b-3eaf-b339-1a4c9c05d4ae | -15.5671 | -48.3244 | 2025-09-02 06:40:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 55.5 |
| 14daa1ad-c858-3841-bbad-7fcbfd9d1d4f | -10.0623 | -48.0978 | 2025-09-02 06:40:00 | GOES-19 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 62.0 |
| 6b29f727-9203-35f2-beeb-488c4a67c55c | -7.9912 | -46.473 | 2025-09-02 06:40:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 69.7 |
| 31027f2a-6286-333f-9e69-596859edb5b9 | -15.5666 | -48.3469 | 2025-09-02 06:40:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 37.0 |
| 1592dd4a-133b-3909-884a-559a4209ca9a | -9.17697 | -71.635 | 2025-09-02 06:46:00 | NOAA-21 | JORDÃO | ACRE | Brasil | 1200328 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b155274d-121a-3de8-abaf-f5fe2b24ba60 | -9.17122 | -71.63422 | 2025-09-02 06:46:00 | NOAA-21 | JORDÃO | ACRE | Brasil | 1200328 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b099ec01-b68a-357a-8413-ef17a6e95dc8 | -10.0623 | -48.0978 | 2025-09-02 06:50:00 | GOES-19 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 51.4 |
| dd537596-70e5-33da-9d54-bf05c2c43451 | -7.9912 | -46.473 | 2025-09-02 07:10:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 66.8 |
| 53f448a7-c1c7-3cbc-94b1-82517dd326c6 | -10.0623 | -48.0978 | 2025-09-02 07:10:00 | GOES-19 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 55.1 |
| 1e9baf80-f090-3b38-8e22-2deebfd075af | -10.0623 | -48.0978 | 2025-09-02 07:20:00 | GOES-19 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 53.5 |
| 800cba02-41bc-3a86-a155-68cc3da85621 | -12.9386 | -48.0881 | 2025-09-02 07:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 84.0 |
| 7aedd7e3-f6e2-34d7-8c21-fed3ff9fda79 | -12.0428 | -49.0013 | 2025-09-02 07:30:00 | GOES-19 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 55.7 |
| 05276751-a459-37f1-8286-cdc248f88cd9 | -12.9579 | -48.0854 | 2025-09-02 07:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 78.1 |
| 2b3d16af-6fb5-3092-bcdc-358e9ba6ce16 | -11.672 | -52.168 | 2025-09-02 07:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 73.7 |
| 22128647-f917-3e2b-a5b5-f3274d86cd5d | -11.6712 | -52.231 | 2025-09-02 07:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 60.1 |
| f806209a-a340-3565-bbf4-ece1b805175d | -11.653 | -52.17 | 2025-09-02 07:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 54.7 |
| 6b8ca8c9-02c3-3f90-bc99-f83002cc8451 | -11.6717 | -52.189 | 2025-09-02 07:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 135.3 |
| 4bf58063-622a-3053-abc0-05e97f65fc47 | -11.6715 | -52.21 | 2025-09-02 07:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 152.2 |
| 699a8b8a-e173-35f5-a00f-1501a7fcc906 | -11.6527 | -52.191 | 2025-09-02 07:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 82.1 |
| d71c6a1b-aa3e-3332-991a-97d6a316ce4e | -11.6527 | -52.191 | 2025-09-02 08:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 84.4 |
| 29fe9735-df91-3722-8bc6-b3eecd443102 | -11.6717 | -52.189 | 2025-09-02 08:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 110.7 |
| 0e177c99-8178-366a-bb2a-4650edfc5e3e | -11.6905 | -52.208 | 2025-09-02 08:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 61.3 |
| 17977af2-2fcf-3bb9-8357-bac28e43d74d | -11.6715 | -52.21 | 2025-09-02 08:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 117.0 |
| 45c0162e-b85f-305b-a9df-7cf9eb6b640c | -11.672 | -52.168 | 2025-09-02 08:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 58.6 |
| c1281f7b-0523-36c0-9f2b-34e9d87c2b49 | -11.653 | -52.17 | 2025-09-02 08:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 55.2 |
| 2eec4eff-6138-3439-b400-e8b2b5e9c743 | -11.8527 | -51.4742 | 2025-09-02 08:10:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 59.7 |
| db31d3f4-5925-34f3-b4df-affa97bc2529 | -10.0623 | -48.0978 | 2025-09-02 08:10:00 | GOES-19 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 51.2 |
| 231fd424-4e62-3c16-9f71-2efca9866c0b | -11.6527 | -52.191 | 2025-09-02 08:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 75.2 |
| 49e8a0af-a2ba-3ba4-a2c1-8897640e0dbd | -11.653 | -52.17 | 2025-09-02 08:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 47.9 |
| 00b6f76c-e9cf-39ae-899f-44d813697465 | -11.6717 | -52.189 | 2025-09-02 08:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 107.5 |
| 9a080bc4-b2f8-31a6-839b-93314565b1d9 | -11.6905 | -52.208 | 2025-09-02 08:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 58.1 |
| 5a0595cd-2d20-3f7c-86e9-0b74b83aefa5 | -14.5995 | -48.0367 | 2025-09-02 08:20:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 48.8 |
| 43be3582-98df-366e-9af1-ca3a6914beeb | -11.6715 | -52.21 | 2025-09-02 08:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 118.2 |
| a91daa2e-a0ef-3063-b133-ea06bad41c48 | -11.672 | -52.168 | 2025-09-02 08:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 57.3 |
| c20626b9-8dc1-3082-919c-2a578236a702 | -11.8527 | -51.4742 | 2025-09-02 08:20:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 62.5 |
| c3944ac0-584f-31b0-9e06-fd94e91ceebc | -9.757 | -46.9376 | 2025-09-02 08:20:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 63.5 |
| 3527d670-3b08-3cd5-a4bd-b4dbf6f74cea | -10.0623 | -48.0978 | 2025-09-02 08:30:00 | GOES-19 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 57.7 |
| 4232df99-329e-3f39-bc97-019733167763 | -11.672 | -52.168 | 2025-09-02 08:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 60.7 |
| e6b4bde7-d0d2-33e0-b769-2e633a8f6288 | -15.5661 | -48.3694 | 2025-09-02 08:30:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 48.5 |
| 8bdfd2a1-cffe-3458-a03a-b897e6693a21 | -11.6712 | -52.231 | 2025-09-02 08:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 55.7 |
| 55b44e87-36ca-3fd9-b596-2fa4f00c082a | -11.6527 | -52.191 | 2025-09-02 08:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 66.9 |
| 43b06f1d-aaec-37e6-b7a4-14d6994e010f | -11.6715 | -52.21 | 2025-09-02 08:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 148.1 |
| 794cbe6d-12ed-32f2-b65d-14de986e3f65 | -11.6717 | -52.189 | 2025-09-02 08:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 117.5 |
| da42edb4-e0f1-327c-8def-9cecd58f6845 | -11.672 | -52.168 | 2025-09-02 08:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 58.5 |
| a1e19049-42ed-3ca2-90e3-b023ccac2511 | -11.6717 | -52.189 | 2025-09-02 08:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 125.4 |
| a8df299c-8f27-38c8-9eda-391cf9e20cd1 | -11.6527 | -52.191 | 2025-09-02 08:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 71.0 |
| 5b9665b0-c163-308b-9fcf-ed1a7b2b9d22 | -11.6712 | -52.231 | 2025-09-02 08:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 84.9 |
| d9fd9aef-caf5-3aa3-9bbe-eb1c836e7160 | -11.6715 | -52.21 | 2025-09-02 08:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 201.9 |
| 2c195f9d-09d6-3633-85d3-5839d452fc18 | -16.6245 | -50.1892 | 2025-09-02 08:40:00 | GOES-19 | TURVÂNIA | GOIÁS | Brasil | 5221502 | 52 | 33 | nan | nan | nan | Cerrado | 56.4 |
| 8e690ad7-ba46-3f37-aa81-2f52de2042db | -11.6905 | -52.208 | 2025-09-02 08:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 52.3 |
| 9ae6fec3-2661-33ad-bfbe-7d8e7b32bf3b | -11.6715 | -52.21 | 2025-09-02 09:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 138.9 |
| bad1d757-30be-33c3-a1c4-dbe0cc53ec2f | -11.6717 | -52.189 | 2025-09-02 09:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 117.6 |
| e3839b13-f09e-3cc7-b8ad-8f61367edc33 | -11.6717 | -52.189 | 2025-09-02 09:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 117.8 |
| 57d49832-278a-3462-9f53-7c6ee7146dd3 | -11.6715 | -52.21 | 2025-09-02 09:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 135.5 |
| e8486f21-a6f5-320e-affe-d96860951035 | -11.6717 | -52.189 | 2025-09-02 10:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 119.9 |
| e8da7592-bccb-307a-bd0e-0df9603366da | -11.6715 | -52.21 | 2025-09-02 10:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 138.8 |
| 35adca6d-8df5-3fa7-b81d-dabc3a51d178 | -11.6717 | -52.189 | 2025-09-02 10:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 125.0 |
| 5dd365af-7425-3f9c-937b-82a353f457c3 | -11.6715 | -52.21 | 2025-09-02 10:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 140.5 |
| 36043a0f-a579-3369-82fa-4c9bd3b9158d | -11.6715 | -52.21 | 2025-09-02 10:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 153.4 |
| 2c2a1b73-5849-32ba-b34c-5bf0c8ee7e02 | -11.6717 | -52.189 | 2025-09-02 10:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 132.9 |
| 22d0d5cf-c674-3251-9b15-6891848b3d18 | -11.6715 | -52.21 | 2025-09-02 10:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 172.8 |
| 90e41d7a-5d5e-3ba4-974b-1fb4a7fd0bd5 | -11.6717 | -52.189 | 2025-09-02 10:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 147.0 |
| 85e28901-70d6-31f8-b501-7108a1bd3dd4 | -11.6717 | -52.189 | 2025-09-02 10:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 136.7 |
| d2ce217d-3798-3c1c-b5d9-2affbe56adfb | -11.4874 | -46.7922 | 2025-09-02 10:40:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 101.2 |
| 43a94e58-518b-3eb9-aacf-70b03200ba97 | -11.6715 | -52.21 | 2025-09-02 10:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 159.1 |
| 2c010506-4f13-315b-b9c0-44c692c7c6f5 | -11.6527 | -52.191 | 2025-09-02 10:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 83.4 |
| aacf93b4-44c5-3f3f-ad46-5ee300c719cc | -11.6715 | -52.21 | 2025-09-02 10:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 140.6 |
| fe416c01-249e-3c6b-bfbe-fd48cb02fbfd | -11.6717 | -52.189 | 2025-09-02 10:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 128.2 |
| a3932154-e054-3149-a7e7-25c768a1fc35 | -15.5666 | -48.3469 | 2025-09-02 10:50:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 105.0 |
| b0b8b8ae-d487-3dcd-90f8-bdc77fd4be3f | -15.5671 | -48.3244 | 2025-09-02 10:50:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 142.2 |
| 10f76f95-d2dd-352f-b168-c7cdbf2c3666 | -15.5867 | -48.321 | 2025-09-02 10:50:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 94.3 |
| a453c96c-6672-378e-8343-586bbb4b8c17 | -11.4874 | -46.7922 | 2025-09-02 11:00:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 103.2 |
| 6407e956-c39b-3eb6-975f-eab82cef2668 | -10.8487 | -47.4546 | 2025-09-02 11:00:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 98.5 |
| a900c134-3ea6-3ffa-90cf-a9763c4240c1 | -11.6527 | -52.191 | 2025-09-02 11:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 83.2 |
| 010c7995-13c2-3310-9262-9df5c464489a | -11.6717 | -52.189 | 2025-09-02 11:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 142.0 |
| 799910f3-86aa-365b-a164-14049e6ea968 | -11.6715 | -52.21 | 2025-09-02 11:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 151.3 |
| 6c247988-8d9e-3573-954b-d80b494961fa | -8.8659 | -45.7788 | 2025-09-02 11:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 76.9 |
| a6c92f24-311f-3760-adf1-072a229d53ce | -8.8848 | -45.7767 | 2025-09-02 11:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 100.1 |
| f65fdda8-77f2-34ad-8d7e-6909c37e4b36 | -11.6715 | -52.21 | 2025-09-02 11:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 168.3 |
| f4a73996-0f44-3a60-8677-e1880721add0 | -15.5671 | -48.3244 | 2025-09-02 11:10:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 93.1 |
| d66fb858-4163-3f08-8279-03aff615080b | -11.6717 | -52.189 | 2025-09-02 11:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 148.2 |
| e1ec46b4-7053-394e-8469-dbea55ae4f47 | -11.6527 | -52.191 | 2025-09-02 11:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 85.9 |
| dfe0d567-a183-3a8d-8944-f28317686b56 | -11.6717 | -52.189 | 2025-09-02 11:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 145.3 |
| 5da10fb7-674f-312b-96ac-53ad1071eda8 | -11.6715 | -52.21 | 2025-09-02 11:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 171.4 |
| 7089f8bf-ea43-3705-8653-1e67fc89456d | -11.6527 | -52.191 | 2025-09-02 11:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 84.3 |
| ac8cf112-d544-37f9-bc29-b5e0cdd6f0e1 | -6.8911 | -45.8538 | 2025-09-02 11:20:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 114.7 |
| bed993f4-6cc1-356d-b366-6f751d318b1b | -6.0514 | -45.6048 | 2025-09-02 11:30:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 74.5 |
| 9607afbc-2d61-34e4-9fa9-49a7d5492e04 | -11.6715 | -52.21 | 2025-09-02 11:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 160.5 |
| f5129bf3-b361-30cc-b5f9-c0cc33a0e273 | -6.8911 | -45.8538 | 2025-09-02 11:30:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 109.7 |
| f6b8a6ca-d1e7-386a-9ad2-eba5e662b398 | -11.6527 | -52.191 | 2025-09-02 11:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 79.8 |
| 40977bf7-7e06-33c1-8ca8-8c1b53a3c3b0 | -15.5671 | -48.3244 | 2025-09-02 11:30:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 89.4 |


[Clique aqui para ver as próximas entradas](README88.md)
