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
| a2509af6-9a4b-3426-9898-d3f77cf37032 | -6.10118 | -40.01935 | 2025-12-15 03:23:00 | NOAA-20 | ARNEIROZ | CEARÁ | Brasil | 2301505 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 6f001095-7889-3567-914f-0223ebac4756 | -6.47545 | -38.8263 | 2025-12-15 03:23:00 | NOAA-20 | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| b2bb3c18-e4c0-31a6-9bb7-d9213d39421d | -8.88725 | -35.45474 | 2025-12-15 03:23:00 | NOAA-20 | JACUÍPE | ALAGOAS | Brasil | 2703502 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| f58d998b-8d41-3f76-8157-609251a81ab6 | -3.30113 | -42.53754 | 2025-12-15 03:23:00 | NOAA-20 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bfaf08bd-ffd7-393f-b553-3e0edb90216a | -6.88632 | -35.6493 | 2025-12-15 03:23:00 | NOAA-20 | ARARA | PARAÍBA | Brasil | 2500908 | 25 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 8a83edbb-733b-3b72-bf05-413981719ded | -8.79852 | -36.95258 | 2025-12-15 03:23:00 | NOAA-20 | PEDRA | PERNAMBUCO | Brasil | 2610806 | 26 | 33 | nan | nan | nan | Caatinga | 1.1 |
| fba57776-8b88-3e36-ac57-7095cfed5401 | -6.16648 | -35.17469 | 2025-12-15 03:23:00 | NOAA-20 | ARÊS | RIO GRANDE DO NORTE | Brasil | 2401206 | 24 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 23f899de-4bf8-3ba1-a07b-d09f103fedae | -6.47594 | -38.82351 | 2025-12-15 03:23:00 | NOAA-20 | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 99246606-fd81-34c6-a2b7-9de8f7bf4ee7 | -3.96061 | -41.53151 | 2025-12-15 03:23:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| fa7fd7e7-d5d5-3cbf-a738-cc2d5100dddb | -3.96287 | -40.93425 | 2025-12-15 03:23:00 | NOAA-20 | IBIAPINA | CEARÁ | Brasil | 2305308 | 23 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 04d78f37-2b75-3949-bdd7-9b00de7318fb | -11.14584 | -43.32804 | 2025-12-15 03:25:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 5.7 |
| f215c4b8-6680-3e93-97f5-606833d30c86 | -6.5631 | -51.1126 | 2025-12-15 03:40:00 | GOES-19 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 56.5 |
| 099366e3-d0eb-3129-8f21-1898c4b3bbdc | -6.5631 | -51.1126 | 2025-12-15 04:00:00 | GOES-19 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 54.7 |
| 5ae3f3c5-f05f-381c-9a62-ee9f44529ca3 | -12.6301 | -55.7827 | 2025-12-15 04:00:00 | GOES-19 | SORRISO | MATO GROSSO | Brasil | 5107925 | 51 | 33 | nan | nan | nan | Cerrado | 51.0 |
| 6bf46939-334f-3a1b-8f82-9780283bbfbd | -12.6301 | -55.7827 | 2025-12-15 04:10:00 | GOES-19 | SORRISO | MATO GROSSO | Brasil | 5107925 | 51 | 33 | nan | nan | nan | Cerrado | 50.8 |
| 9995feaa-f728-3dcf-8f7a-7e6ca76f8676 | -1.89389 | -45.75779 | 2025-12-15 04:12:00 | NOAA-21 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c1253447-7bd5-34eb-ad6f-daed621519c4 | -1.53719 | -45.8563 | 2025-12-15 04:12:00 | NOAA-21 | GODOFREDO VIANA | MARANHÃO | Brasil | 2104305 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 064220f9-7bef-3b95-9625-27f7c8b27256 | -3.05287 | -52.82593 | 2025-12-15 04:14:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 49aec29c-eab3-3235-8280-666f4263ec31 | -9.10968 | -35.45483 | 2025-12-15 04:14:00 | NOAA-21 | PORTO DE PEDRAS | ALAGOAS | Brasil | 2707404 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 8aa66e44-19b3-3ab7-ba4f-6fc84104b82d | -3.2052 | -46.83125 | 2025-12-15 04:14:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cd083834-ae92-3b9d-b215-019827131d85 | -3.72361 | -44.50216 | 2025-12-15 04:14:00 | NOAA-21 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 34a7c209-fbdd-3eae-8110-384bab27b2d4 | -2.75854 | -42.63921 | 2025-12-15 04:14:00 | NOAA-21 | PAULINO NEVES | MARANHÃO | Brasil | 2108058 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2a978659-bda4-363d-8ee0-e0c8f568237e | -3.7141 | -44.58457 | 2025-12-15 04:14:00 | NOAA-21 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 8b17b2a2-3348-32df-b5e3-23e750084050 | -6.32199 | -39.85123 | 2025-12-15 04:14:00 | NOAA-21 | CATARINA | CEARÁ | Brasil | 2303600 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 41d31538-a3e3-3d94-9338-04f11eeb3982 | -2.58466 | -45.14407 | 2025-12-15 04:14:00 | NOAA-21 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 37fcc2ec-cb2c-39e0-972b-69cfea9b83c6 | -2.41117 | -45.68606 | 2025-12-15 04:14:00 | NOAA-21 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9088f8a1-16e3-3a79-aab7-6794486c2a38 | -2.70047 | -49.11935 | 2025-12-15 04:14:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e5d4eccc-8dac-342f-b69a-45a5b8200fd7 | -6.10895 | -45.8534 | 2025-12-15 04:14:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0626a27c-b8bc-390b-a3b6-74572057046c | -2.16595 | -45.93101 | 2025-12-15 04:14:00 | NOAA-21 | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cea95676-5f00-3481-98e8-d14d9720e9b7 | -2.35445 | -45.61755 | 2025-12-15 04:14:00 | NOAA-21 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| da177fd2-b639-3060-92c1-56340983c367 | -3.72136 | -44.49421 | 2025-12-15 04:14:00 | NOAA-21 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fc2a8644-31e2-3d51-a4d0-a410b1b2c233 | -3.79991 | -47.0609 | 2025-12-15 04:14:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7d6ae67e-a813-3c63-8c07-479c49e9f1b1 | -9.10978 | -35.45661 | 2025-12-15 04:14:00 | NOAA-21 | PORTO DE PEDRAS | ALAGOAS | Brasil | 2707404 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 83edaf41-3d3d-36b0-a605-2f032f650312 | -5.49262 | -45.38067 | 2025-12-15 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fa850837-9853-3e67-a98a-752d6d450b45 | -4.45546 | -43.91613 | 2025-12-15 04:14:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d8beb6e5-ca7d-3e17-a14b-e6c6ec583915 | -7.64554 | -43.94248 | 2025-12-15 04:14:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 6ffae012-78e7-362d-b6a7-a96605dba6ba | -7.76316 | -35.10526 | 2025-12-15 04:14:00 | NOAA-21 | ARAÇOIABA | PERNAMBUCO | Brasil | 2601052 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| b75a7d7e-01e0-396a-a958-433b28d594af | -3.02042 | -45.34585 | 2025-12-15 04:14:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2a9479f0-0405-3f7f-a5dc-8b78821c136c | -2.75908 | -42.63578 | 2025-12-15 04:14:00 | NOAA-21 | PAULINO NEVES | MARANHÃO | Brasil | 2108058 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 11f7595b-f001-3b4e-8ec4-f88840cbff5a | -4.81175 | -38.98063 | 2025-12-15 04:14:00 | NOAA-21 | QUIXADÁ | CEARÁ | Brasil | 2311306 | 23 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 45d059a0-2f08-3c03-85b8-495e3bc0bb79 | -4.69224 | -43.25551 | 2025-12-15 04:14:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f3bd4b9f-39f1-3409-a115-726f3715723c | -4.69941 | -43.25309 | 2025-12-15 04:14:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c4010844-f700-33cb-9239-3cb743874eb7 | -6.61057 | -44.37423 | 2025-12-15 04:14:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| da49b157-9bbd-364d-8f45-2a4f7f128904 | -3.02171 | -45.33775 | 2025-12-15 04:14:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 7eb88b8a-f9c5-3f54-8176-70613a20d242 | -4.03888 | -41.91174 | 2025-12-15 04:14:00 | NOAA-21 | BRASILEIRA | PIAUÍ | Brasil | 2201960 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 0475a0a0-378b-3ffc-afa4-3713ce17c378 | -5.49908 | -42.16422 | 2025-12-15 04:14:00 | NOAA-21 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| f89f3857-b3cf-3887-bee2-651b3ef88a85 | -5.48503 | -45.38336 | 2025-12-15 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 59ac0e98-9c31-3a71-9162-6f29357bd3c4 | -2.834 | -46.73279 | 2025-12-15 04:14:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 6c757c56-0a4e-35c3-8134-1b580af29080 | -4.41019 | -42.14737 | 2025-12-15 04:14:00 | NOAA-21 | BOA HORA | PIAUÍ | Brasil | 2201770 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 2438235e-9057-3372-8f4e-ac97248cb782 | -5.02691 | -41.30049 | 2025-12-15 04:14:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 96f0919b-8b47-3274-8e80-b8c87471794a | -4.40205 | -44.10102 | 2025-12-15 04:14:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7c98cc65-78f4-3716-9c6c-d6e15c31ebfa | -3.98495 | -46.98262 | 2025-12-15 04:14:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e48b56b5-fc04-3847-9f8f-fa4011f9d88c | -3.20441 | -46.83608 | 2025-12-15 04:14:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8194a7b1-291b-328a-a1bb-28e83353caf1 | -5.03029 | -41.30103 | 2025-12-15 04:14:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| cce1cbe1-e67b-3d1a-b22f-69e89fcc534a | -3.71735 | -44.49739 | 2025-12-15 04:14:00 | NOAA-21 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cd3bd151-e22b-3208-a040-27296947e196 | -4.06686 | -46.59159 | 2025-12-15 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bdc77200-659c-3ac9-b46a-8233e01b6d6b | -4.14836 | -40.64639 | 2025-12-15 04:14:00 | NOAA-21 | RERIUTABA | CEARÁ | Brasil | 2311702 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 30e669f5-4b7e-3dfe-a180-71db435b612e | -3.71334 | -44.50058 | 2025-12-15 04:14:00 | NOAA-21 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 328068b7-5989-305e-a8d6-84bbce048eef | -1.90814 | -46.59143 | 2025-12-15 04:14:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e7d3dd95-8649-390a-b80d-9b91d3db05a4 | -6.71533 | -39.99855 | 2025-12-15 04:14:00 | NOAA-21 | ANTONINA DO NORTE | CEARÁ | Brasil | 2300804 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 560bf0d2-6236-30a6-8a88-637f1c41d18a | -2.83863 | -46.72856 | 2025-12-15 04:14:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| e1310ce8-91f9-30b0-90da-62d46dc01d87 | -3.7242 | -44.49845 | 2025-12-15 04:14:00 | NOAA-21 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ffceada8-7cde-3c0c-9f1d-56744be262e2 | -8.79847 | -36.95289 | 2025-12-15 04:14:00 | NOAA-21 | PEDRA | PERNAMBUCO | Brasil | 2610806 | 26 | 33 | nan | nan | nan | Caatinga | 1.1 |
| c6ac5005-0b5b-311f-b406-6ea92550dcc0 | -2.22498 | -45.65465 | 2025-12-15 04:14:00 | NOAA-21 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| b2f38940-b403-3a87-83da-f16d69c6c266 | -3.96944 | -41.52867 | 2025-12-15 04:14:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 559d1c9d-e71b-3c80-8aaa-95b7c9da6c0d | -6.10542 | -45.85283 | 2025-12-15 04:14:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 78762b80-f3fe-3008-88c0-ce1beb78c5b7 | -3.96365 | -40.93263 | 2025-12-15 04:14:00 | NOAA-21 | IBIAPINA | CEARÁ | Brasil | 2305308 | 23 | 33 | nan | nan | nan | Caatinga | 3.0 |
| ffc778bf-ae11-35fd-91f5-31accd799fbb | -6.48182 | -38.82487 | 2025-12-15 04:14:00 | NOAA-21 | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 2.8 |
| fcd39738-3453-3561-8bb3-4a96e1a4e189 | -2.93436 | -41.14424 | 2025-12-15 04:14:00 | NOAA-21 | BARROQUINHA | CEARÁ | Brasil | 2302057 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 0ba029ae-d56f-30fc-8a85-e58c4aaba256 | -2.63243 | -47.29434 | 2025-12-15 04:14:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e6307e0d-e8fe-3ccf-9ba1-7c7a06de578d | -4.40598 | -44.09798 | 2025-12-15 04:14:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3279ab65-b153-3a4a-8aef-0bd35f8b7229 | -3.9661 | -41.52816 | 2025-12-15 04:14:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 699d1323-8117-3798-8ff1-8178db92a641 | -3.71794 | -44.49369 | 2025-12-15 04:14:00 | NOAA-21 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7d79d223-b94a-3447-9f64-09e3cd7a6b38 | -5.90559 | -44.36064 | 2025-12-15 04:14:00 | NOAA-21 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5b4d4752-c282-3a4d-a22e-436816ab393a | -10.14613 | -36.59925 | 2025-12-15 04:14:00 | NOAA-21 | IGREJA NOVA | ALAGOAS | Brasil | 2703205 | 27 | 33 | nan | nan | nan | Caatinga | 1.3 |
| d44e5b91-c62b-3e1e-9797-218ed534b7fa | -3.4105 | -44.17506 | 2025-12-15 04:14:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 23972182-2d19-3cdd-8036-3174feea3f05 | -3.96834 | -41.5357 | 2025-12-15 04:14:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 59d8ea8b-f082-30de-8e6c-90573368dc3c | -6.47961 | -38.82619 | 2025-12-15 04:14:00 | NOAA-21 | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 3.0 |
| e3aaaa88-22cf-322b-befc-e58678353c17 | -3.20829 | -46.83668 | 2025-12-15 04:14:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 40cabc40-6a6a-38f1-b89f-8a22fade1b87 | -3.30183 | -42.53426 | 2025-12-15 04:14:00 | NOAA-21 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 388fb178-79fc-3177-a8e0-7fee2fbee1c0 | -4.10128 | -46.3988 | 2025-12-15 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 910f706b-d781-3ef0-bb7c-7b6164560522 | -3.7196 | -44.50533 | 2025-12-15 04:14:00 | NOAA-21 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 29186a9f-5f85-3ef7-9021-3d419da89184 | -2.28407 | -53.70815 | 2025-12-15 04:14:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 0bb3c0cf-05db-36f7-a17d-14e0883e8259 | -7.76213 | -35.10531 | 2025-12-15 04:14:00 | NOAA-21 | ARAÇOIABA | PERNAMBUCO | Brasil | 2601052 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| a1e2ab86-4a91-3277-ad12-745423329b53 | -4.17285 | -44.02154 | 2025-12-15 04:14:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8ddadb26-bdcd-34b9-9099-5b9d3fd44042 | -4.5152 | -47.43622 | 2025-12-15 04:14:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 45c2102d-e4b3-3ff7-b6d4-5faa8ca36039 | -4.15747 | -43.73513 | 2025-12-15 04:14:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d105e150-de9d-3de3-895c-99759cbc576a | -3.72078 | -44.49791 | 2025-12-15 04:14:00 | NOAA-21 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d0914361-ef9c-377e-be78-ff47f21c28c9 | -6.1067 | -45.84491 | 2025-12-15 04:14:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c99bb379-6cfe-309e-a29e-3f3c3ca85338 | -4.23375 | -46.31208 | 2025-12-15 04:14:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| aa4c861b-cdbd-3277-94f9-bbf2ea98a057 | -2.01467 | -45.7533 | 2025-12-15 04:14:00 | NOAA-21 | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9a439552-3d96-3ec8-bb83-9344b4eab8be | -6.4522 | -39.78469 | 2025-12-15 04:14:00 | NOAA-21 | SABOEIRO | CEARÁ | Brasil | 2311900 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 084a32de-d53b-3c96-904f-44d9b038c043 | -2.83477 | -46.72794 | 2025-12-15 04:14:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| f79d747b-edea-386b-8e78-e5959b4ed1fe | -3.12813 | -41.77662 | 2025-12-15 04:14:00 | NOAA-21 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| a1058304-197c-38c1-96d5-e7bfed4c2827 | -3.05777 | -52.83219 | 2025-12-15 04:14:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 54a40401-70aa-3a45-b689-9e376bdf7c67 | -3.30574 | -42.53488 | 2025-12-15 04:14:00 | NOAA-21 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 95918931-cebc-360b-af96-64cfce0a9c2a | -2.50579 | -48.03691 | 2025-12-15 04:14:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2f62b5f2-c222-3d9d-9be4-67d3c70832bd | -3.71393 | -44.49688 | 2025-12-15 04:14:00 | NOAA-21 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 13a297a5-c4cb-3428-be25-dfa360bc0222 | -2.85119 | -46.83231 | 2025-12-15 04:14:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bc7ea521-ce47-32d9-9580-19a66a4c9a6e | -2.22566 | -45.65037 | 2025-12-15 04:14:00 | NOAA-21 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |


[Clique aqui para ver as próximas entradas](README4.md)
