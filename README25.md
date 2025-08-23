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

## Dados Diários - Página 25

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| aae68adb-a8c8-33e2-9342-fb269850685d | -6.60824 | -44.5616 | 2025-08-23 04:00:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 28.2 |
| f80294c0-81d5-3c9a-a39d-be950a35352b | -5.37356 | -41.21664 | 2025-08-23 04:00:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 98b5d1e2-dc90-3f89-bd3d-bad9c356e6c6 | -7.87429 | -46.29448 | 2025-08-23 04:00:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cb26e872-a3e9-3125-9aab-b2483f982571 | -6.50274 | -43.11564 | 2025-08-23 04:00:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 56571a7c-e174-3839-8dc5-d95603ac4d3e | -3.43528 | -49.04066 | 2025-08-23 04:00:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 0e252a11-a1de-3ecd-bb2a-45d5111283c7 | -6.16185 | -45.03663 | 2025-08-23 04:00:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a1c719f6-c840-3a94-af79-2d712fcecb54 | -7.08478 | -44.59564 | 2025-08-23 04:00:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4f8ee6b0-8dbc-33fe-9fe1-5c70d43879e1 | -6.37248 | -42.67283 | 2025-08-23 04:00:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 61ed78d5-0148-3ec3-8e8a-831fb386674b | -6.60272 | -44.57065 | 2025-08-23 04:00:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 22.1 |
| 63b1ca20-4d7f-3c03-b5de-0f8566462374 | -2.54945 | -47.71455 | 2025-08-23 04:00:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 05aa2f10-760e-3c3b-898e-82855e622b10 | -7.13585 | -44.16522 | 2025-08-23 04:00:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 9863b36b-064f-3205-8c42-d48ac6e9f80e | -2.70538 | -48.21369 | 2025-08-23 04:00:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f48d839a-1a06-3470-9f61-49c50addb8cd | -6.3859 | -45.52234 | 2025-08-23 04:00:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ae8c9319-d1dc-3edd-b6e4-2102b3c21678 | -7.67671 | -45.41058 | 2025-08-23 04:00:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| db853ab3-bdc4-3474-8921-aba179f645c8 | -8.01378 | -45.49035 | 2025-08-23 04:00:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3fe1ebc1-339b-3c8e-b848-111b41bcd63c | -3.43404 | -49.04788 | 2025-08-23 04:00:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 694a4e6f-296b-3b65-af57-6434666cff03 | -6.61133 | -44.56708 | 2025-08-23 04:00:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 49878020-8eee-3af2-ad6b-209c5ed60234 | -12.99478 | -45.23097 | 2025-08-23 04:02:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 18.9 |
| c196a98b-5c3f-35cc-8f04-89b37c87e87e | -14.91466 | -47.31448 | 2025-08-23 04:02:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 6aa37941-28ac-33bf-b9d6-da8711a912e9 | -10.62479 | -50.15691 | 2025-08-23 04:02:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 970dadf4-0ac3-34bd-a712-a6fe3e177be8 | -8.84687 | -49.86742 | 2025-08-23 04:02:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fe6addad-a361-3ba0-ac36-a14e81e2f81d | -11.78373 | -46.4084 | 2025-08-23 04:02:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 61d11989-aebe-3c0e-a74a-088202820917 | -12.98895 | -45.22067 | 2025-08-23 04:02:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| af03af08-e4c8-350a-88c4-97a8fe0af252 | -11.12005 | -44.76438 | 2025-08-23 04:02:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 04bbd7d9-63bc-320c-ad26-50bca4068984 | -8.85161 | -49.87174 | 2025-08-23 04:02:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fe59e3dc-897b-3202-9671-e13d04d39bc8 | -12.78635 | -48.7237 | 2025-08-23 04:02:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 8e8b7108-7c98-3a56-931f-b8502f729593 | -15.55746 | -42.68046 | 2025-08-23 04:02:00 | NOAA-20 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| c01bce93-0c27-3acd-bc49-338788f5a889 | -14.82288 | -47.95559 | 2025-08-23 04:02:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 17371c0f-96ec-3a21-a082-37902c142294 | -10.74897 | -48.24899 | 2025-08-23 04:02:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f2da0523-c126-333b-a937-223d4092a510 | -14.96636 | -48.6769 | 2025-08-23 04:02:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f5b31ec3-90a3-3738-86f8-c3aafc160c53 | -13.50951 | -47.05593 | 2025-08-23 04:02:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ab9c8c25-51b7-3297-8b65-8fb31a76ed34 | -11.18409 | -55.04869 | 2025-08-23 04:02:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f78b0edb-989d-3165-9104-d356238a221b | -15.06752 | -48.4947 | 2025-08-23 04:02:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4fd4d259-acf6-3cb4-8a77-9eda8f92effb | -11.1245 | -44.76057 | 2025-08-23 04:02:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 99ae1b5d-7640-3a68-9f45-b5f23fd65881 | -10.63315 | -50.1414 | 2025-08-23 04:02:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 979a22e0-f226-33ef-8995-267881aed436 | -13.42078 | -46.27245 | 2025-08-23 04:02:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 46.0 |
| 40c62c66-8ef5-3989-9e03-9d59d39f6027 | -12.30663 | -49.98874 | 2025-08-23 04:02:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 61212a68-9b49-3f27-979b-306a24ab4fb4 | -12.29873 | -50.0029 | 2025-08-23 04:02:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4f96a34b-b810-3b81-b698-f69097990752 | -8.28895 | -47.26532 | 2025-08-23 04:02:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 17d795b4-bdd9-321d-8648-d1797cb8f7fc | -8.29431 | -47.26142 | 2025-08-23 04:02:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| c2c6c9aa-4702-3cb6-8a80-14c7e6e9ba4d | -13.3733 | -46.22223 | 2025-08-23 04:02:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b311684c-e30c-367b-94fa-e9df958b61a6 | -11.31897 | -47.84257 | 2025-08-23 04:02:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c7dc3f62-71e7-37eb-a3db-1dfd722b0ec1 | -13.376 | -46.207 | 2025-08-23 04:02:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 10.7 |
| dcca1d10-ad3b-3361-8513-2be10df5b84f | -14.8793 | -47.95845 | 2025-08-23 04:02:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d503ce24-80cd-34a7-a78c-dd43271c382a | -13.45051 | -47.03149 | 2025-08-23 04:02:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 62640668-9029-34a6-a3c1-bdcd328f7d27 | -12.94519 | -46.29597 | 2025-08-23 04:02:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d7a9f866-03b3-3505-bff4-7ff38706e5ea | -13.42047 | -46.25107 | 2025-08-23 04:02:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 24eea194-b55e-3ab1-b2f9-7c21a1bb86fa | -15.70757 | -41.92414 | 2025-08-23 04:02:00 | NOAA-20 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 820c6484-6f78-3045-abd5-6244ebf74663 | -11.12232 | -44.75106 | 2025-08-23 04:02:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a9055fe5-37a7-3158-b501-e2777487e071 | -11.13492 | -44.74411 | 2025-08-23 04:02:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f2985eaa-1f17-3725-afe6-0cffe94ab03d | -11.32273 | -47.84729 | 2025-08-23 04:02:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 54cae536-8c71-374d-acef-c0d2362567dc | -12.77722 | -48.71358 | 2025-08-23 04:02:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 2e7116cb-5738-39b1-8e69-757c42c68f38 | -8.66442 | -51.27973 | 2025-08-23 04:02:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8d5ad151-746c-31a5-9a4f-33d181e87e30 | -11.12668 | -44.77011 | 2025-08-23 04:02:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5100170f-d256-3c0a-a38b-ba441b722e51 | -11.12156 | -44.75552 | 2025-08-23 04:02:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e900e702-b170-31f2-addb-325456fcde28 | -13.45459 | -47.03226 | 2025-08-23 04:02:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 92b8c571-63af-368d-8031-c3b27423ad3e | -13.12428 | -46.8896 | 2025-08-23 04:02:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 678ff1a1-eb3a-398c-a518-f43931373400 | -13.38482 | -47.51431 | 2025-08-23 04:02:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 306e8223-e649-3ff9-8dbb-b9bfd5dc23cf | -12.301 | -49.99076 | 2025-08-23 04:02:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d51ef7bb-cc82-306d-ba7e-2f57ab776def | -13.49177 | -47.03685 | 2025-08-23 04:02:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e1f29ae1-3da7-33fd-941c-b2194ad564e6 | -12.7809 | -48.71943 | 2025-08-23 04:02:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 62a55579-b155-3774-a353-61855c935bd4 | -15.06859 | -47.15808 | 2025-08-23 04:02:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0fab31f9-a6dd-3b46-ac9d-ad8bdf970dfc | -8.65857 | -51.27856 | 2025-08-23 04:02:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 451cd542-2941-393a-9d5a-98fad02554e0 | -11.1386 | -44.74479 | 2025-08-23 04:02:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| a1da7c18-2646-3799-a649-d243e59f5c4c | -12.5102 | -44.73353 | 2025-08-23 04:02:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f1a47997-972e-3595-a782-b8cd43ed66ee | -9.93914 | -48.90308 | 2025-08-23 04:02:00 | NOAA-20 | MONTE SANTO DO TOCANTINS | TOCANTINS | Brasil | 1713700 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 92e9d3ee-04db-3aa3-a04a-feef7964c0c4 | -10.64675 | -50.12695 | 2025-08-23 04:02:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 31d1e953-3580-3491-9445-292c899405bb | -14.8068 | -47.94768 | 2025-08-23 04:02:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 08325769-a312-3866-9628-4aa72755cd21 | -11.18272 | -55.04306 | 2025-08-23 04:02:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 40e91582-6b12-330d-91a7-af3c8b55a63e | -12.31505 | -49.99992 | 2025-08-23 04:02:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 003c2f70-6953-362a-a310-d846f40a407b | -15.07188 | -48.49561 | 2025-08-23 04:02:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 25895dd3-a224-3a04-98fb-1368ab5711e1 | -8.89864 | -47.33141 | 2025-08-23 04:02:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9d3c8d3f-68c5-33d5-8c6d-8d317a3b4403 | -12.99264 | -45.22134 | 2025-08-23 04:02:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 72f4f62d-d307-3210-a083-af6caea1a341 | -11.13038 | -44.77076 | 2025-08-23 04:02:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3e52fbf2-c64f-33d1-94cb-1121f6d7acdb | -12.70674 | -48.10315 | 2025-08-23 04:02:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 00767c73-d660-32b0-8762-d3c19ae9e324 | -10.27809 | -46.75146 | 2025-08-23 04:02:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f5781c21-9335-3ff1-a110-fc2401b71e79 | -11.18696 | -55.03479 | 2025-08-23 04:02:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 22885c17-6b93-31be-aff4-23c0b523e22e | -11.12884 | -44.77979 | 2025-08-23 04:02:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 5f609019-b030-3671-b549-bc716056d457 | -11.32645 | -47.85219 | 2025-08-23 04:02:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| cff35f21-dada-3ce6-aae9-9b0276dd609b | -14.90665 | -47.99583 | 2025-08-23 04:02:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b4551772-848a-348c-8cc4-3f1b46e4fa8a | -13.47379 | -46.90211 | 2025-08-23 04:02:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fb85d382-4715-38b1-bad6-2cca840e950d | -12.31382 | -49.99561 | 2025-08-23 04:02:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 163618f0-326e-365f-9462-df3ac1f0189c | -14.78266 | -45.48591 | 2025-08-23 04:02:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a443d242-d226-3d7c-8005-bb365a85777b | -14.78071 | -45.45602 | 2025-08-23 04:02:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 46600095-cd20-3277-9eab-da84cb4643ff | -8.04489 | -47.31267 | 2025-08-23 04:02:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 19e3a20c-c384-31a2-8f08-1419567d6a0e | -13.45539 | -47.02783 | 2025-08-23 04:02:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 10ad3838-16db-338e-ae1f-529f3738b4dc | -10.22496 | -47.56799 | 2025-08-23 04:02:00 | NOAA-20 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7ee03a6b-34bf-352a-a6f8-37744cc1ca8d | -11.32379 | -44.95719 | 2025-08-23 04:02:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6471d2a7-79c0-361a-985b-928eae26685a | -10.84983 | -45.20769 | 2025-08-23 04:02:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 93164e19-6e26-3ad9-a677-0dc8d2c51342 | -13.38741 | -46.25616 | 2025-08-23 04:02:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| eefa8b87-d99e-3d21-b135-8b974d27f765 | -12.31323 | -49.99865 | 2025-08-23 04:02:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f7c8f345-f9fa-3868-8a64-ef5ce30d2399 | -13.4167 | -51.79887 | 2025-08-23 04:02:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2520373e-5b9f-3bb6-90a1-da01209b78ef | -12.67243 | -43.97405 | 2025-08-23 04:02:00 | NOAA-20 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 6a3ce2c0-742f-3fd2-9bb8-21634c380a00 | -12.99633 | -45.222 | 2025-08-23 04:02:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| af3f58dd-c617-352e-9c9e-683648d72879 | -8.53337 | -48.86345 | 2025-08-23 04:02:00 | NOAA-20 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8bd6cf11-0843-3051-ac80-1ecaf3d50721 | -10.75365 | -48.2496 | 2025-08-23 04:02:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d923f5e8-47ec-3522-99c4-f67b6951a753 | -12.77519 | -48.7062 | 2025-08-23 04:02:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 68dc4041-d5db-3e76-99db-13aeefe532de | -10.68322 | -50.1319 | 2025-08-23 04:02:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 93ff453d-00d4-3a05-9703-b2a67f29a0f3 | -8.30255 | -47.26761 | 2025-08-23 04:02:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| f8ab3950-e5a4-3f17-a160-9968650f110e | -12.54629 | -45.62169 | 2025-08-23 04:02:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |


[Clique aqui para ver as próximas entradas](README26.md)
