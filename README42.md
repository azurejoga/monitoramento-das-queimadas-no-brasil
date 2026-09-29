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

## Dados Diários - Página 42

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 93cdbb8c-0e50-3965-94fd-85a59c9e371f | -6.162 | -52.82337 | 2026-09-29 04:51:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cff709e0-b2e5-3eaa-8a5d-245bf6b0d63d | -11.46264 | -49.74281 | 2026-09-29 04:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8452fa50-ca53-3188-aad6-ce919432d688 | -8.65919 | -48.88662 | 2026-09-29 04:51:00 | NPP-375D | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1fb8d2f5-f11a-3078-a8fa-d006208ad6c7 | -12.6089 | -47.27987 | 2026-09-29 04:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ce2ff08f-9344-3160-a6e7-0f36a3631e87 | -11.61035 | -46.7901 | 2026-09-29 04:51:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f6c161da-c5f5-331a-bdc6-01b79db5319f | -12.74345 | -47.27567 | 2026-09-29 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 25.1 |
| cafec380-6dc9-338e-9245-f07d5c64a64d | -14.0801 | -46.31476 | 2026-09-29 04:51:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c179138c-f50c-3362-b987-d4eab441ddaa | -11.50685 | -47.39717 | 2026-09-29 04:51:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 05a13f80-de6d-3271-a3aa-dccc8ca7abd4 | -11.42617 | -43.45369 | 2026-09-29 04:51:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| f783d081-11ae-3c99-926d-60aaa26663ca | -11.61851 | -44.15303 | 2026-09-29 04:51:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4b5febad-1387-3cb8-b783-d00935d7d926 | -6.70039 | -45.68817 | 2026-09-29 04:51:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e8203edd-7938-3690-be35-b92589cb8628 | -8.65451 | -45.34036 | 2026-09-29 04:51:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9a4f0ddd-a6d7-390c-9c12-f5483fb9370e | -12.6609 | -46.99823 | 2026-09-29 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| fdd0f0ca-eb9b-359a-9096-8c4b20d70644 | -12.90746 | -52.0635 | 2026-09-29 04:51:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e6b41eff-7101-3986-9698-7ddf70cca045 | -12.00205 | -44.92657 | 2026-09-29 04:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 538fcb6c-1e1e-3ad9-bdd8-c30a9cb0547d | -12.01001 | -50.93156 | 2026-09-29 04:51:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 38942b11-c386-3989-8c25-100ef183a8d2 | -11.99607 | -50.95461 | 2026-09-29 04:51:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| cda2508a-446a-3521-a7a4-ee0a2573b67f | -11.36328 | -54.04418 | 2026-09-29 04:51:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 059a9124-14ff-32a7-b505-e8cb804feb61 | -11.90863 | -50.61032 | 2026-09-29 04:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| fc950653-d14b-3397-9d96-3b77459164c9 | -6.69587 | -45.64132 | 2026-09-29 04:51:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2f4f3eb7-9dda-35a9-80e7-9ee2c9593a6c | -11.80577 | -49.05296 | 2026-09-29 04:51:00 | NPP-375D | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 9e4b8070-8468-3be5-947c-721a6ae556e7 | -11.13745 | -50.07719 | 2026-09-29 04:51:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 05ddd55c-39c6-375d-970c-f0b6c6dfd8f5 | -9.95856 | -50.15455 | 2026-09-29 04:51:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0a264b95-025b-3f47-a49d-be0ca78c5680 | -9.14015 | -49.98047 | 2026-09-29 04:51:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3c28356a-06bf-367b-aab9-837990a1a302 | -10.71822 | -44.43133 | 2026-09-29 04:51:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 211dcc4d-3983-3d92-9f1e-da4e70740c7d | -10.7993 | -48.7521 | 2026-09-29 04:51:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| d36325b5-c5cd-3ad5-bef8-767cbe47ab60 | -10.9518 | -49.59632 | 2026-09-29 04:51:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 51cab174-757c-3632-a708-2fe6a37c0f49 | -12.01299 | -50.97178 | 2026-09-29 04:51:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 430d88ca-34c1-37bb-9278-b5a8106600ce | -11.41287 | -43.44693 | 2026-09-29 04:51:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a88e4832-1665-376b-84b6-7aa7702742ed | -12.04138 | -50.94386 | 2026-09-29 04:51:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 6.4 |
| e08b1c0d-e615-3d8f-a733-fa124bdc7f4b | -12.74589 | -47.28492 | 2026-09-29 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 45653856-1e72-3bc4-99a7-5a09a5190021 | -10.71845 | -49.02906 | 2026-09-29 04:51:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0ffa3443-ddba-3f8d-81ef-8602862a681d | -10.79533 | -48.75517 | 2026-09-29 04:51:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 461cfc3c-6ca6-3a1f-ad1d-87e3c74a07ac | -14.11345 | -46.28881 | 2026-09-29 04:51:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 12faf1ba-2fd4-3c22-86d0-438398ed32ef | -7.39294 | -42.63992 | 2026-09-29 04:51:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 8515c35b-8223-3c6e-acd6-dbe77d5663a8 | -13.71086 | -48.83092 | 2026-09-29 04:51:00 | NPP-375D | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 087994f7-b34e-3dad-8cb0-d9afe3f132e5 | -11.12911 | -50.06497 | 2026-09-29 04:51:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c6098104-9b85-3154-a9c8-e8aeb2e283b1 | -9.04656 | -49.63508 | 2026-09-29 04:51:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 886a6655-7c49-371b-82c8-c0894216570b | -12.88052 | -44.80729 | 2026-09-29 04:51:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d97da214-e7e5-3535-a4cd-975a6cb08d0d | -11.45008 | -43.48675 | 2026-09-29 04:51:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 408e1d8f-d61b-3b8c-b58f-3185fe807d1c | -7.00907 | -45.30182 | 2026-09-29 04:51:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| a3dc16f2-f685-3b24-8f4d-2ec9a65247bc | -9.05042 | -45.00224 | 2026-09-29 04:51:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d5b84535-e313-3cea-a67d-85d0071b1c21 | -6.14406 | -51.73479 | 2026-09-29 04:51:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 17c4e201-ba56-3cc3-8ed3-df521fbd2074 | -9.13682 | -49.97994 | 2026-09-29 04:51:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ab65fc8c-3027-3030-96c0-57fdc446d594 | -9.79225 | -44.82181 | 2026-09-29 04:51:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e64b760d-5949-30b9-8fa8-1839f18331f6 | -10.78626 | -48.74598 | 2026-09-29 04:51:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 33f08090-f9f5-3ec9-9ee9-5eb40a955635 | -11.8052 | -49.05668 | 2026-09-29 04:51:00 | NPP-375D | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 943ddd62-502f-3d67-b2ee-963c16c65a1a | -12.90469 | -52.05928 | 2026-09-29 04:51:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9ef9f58f-518e-3ccd-969c-8cc368b8f849 | -11.1677 | -48.32356 | 2026-09-29 04:51:00 | NPP-375D | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| df3a38e0-e932-3109-bfd3-fa4873f37c68 | -11.42877 | -43.43415 | 2026-09-29 04:51:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 8.4 |
| f0e1b6b3-690b-3890-b0ce-82a5db68118f | -14.11649 | -46.28772 | 2026-09-29 04:51:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| d8895fb9-57fe-36c9-b442-f27a1911d086 | -12.05307 | -50.9349 | 2026-09-29 04:51:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ff0b198d-1f77-3dcc-ae3d-b4a5c07d5d9f | -12.75942 | -47.29592 | 2026-09-29 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 4ce14930-a4df-33f7-98b2-cb94670356ef | -9.78919 | -48.20144 | 2026-09-29 04:51:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1a7a01c4-c306-3bae-bb25-88dfaab72186 | -12.10594 | -47.39199 | 2026-09-29 04:51:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1ea0472a-5870-3aad-b0d7-14eac1a6918f | -9.04991 | -45.00584 | 2026-09-29 04:51:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f036fa37-a2e0-3ae0-88f9-f3109053e2dc | -7.4103 | -42.61793 | 2026-09-29 04:51:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 831171c3-6df1-3694-80ae-9b665b97d8e4 | -11.3846 | -54.04185 | 2026-09-29 04:51:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 807d1d8e-858c-368d-b07d-ae2d5cd60ef9 | -10.42052 | -53.83168 | 2026-09-29 04:51:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 729bf054-eb93-3a47-ade1-7888404dcc34 | -12.47488 | -47.48471 | 2026-09-29 04:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| d6a5dc56-cfe8-37f8-82d8-255a45be83bc | -10.81069 | -48.72348 | 2026-09-29 04:51:00 | NPP-375D | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fd8bb5bf-2e64-31af-ae94-6d56896f1f8c | -8.21746 | -45.46922 | 2026-09-29 04:51:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9e02527f-f257-3b27-ad79-29bcdc059774 | -13.16477 | -48.53812 | 2026-09-29 04:51:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 32601b7a-9eb0-316f-bb53-0caa528fc710 | -6.99947 | -45.33937 | 2026-09-29 04:51:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 55a75d29-caf9-360e-a0f7-9afab0c1f065 | -11.99274 | -50.95406 | 2026-09-29 04:51:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1cf6b0ac-e98e-39dd-a42c-6c93243d6d1c | -10.72062 | -44.4334 | 2026-09-29 04:51:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 46f88777-01ff-3486-9812-3ddb17916ad2 | -11.36214 | -47.44281 | 2026-09-29 04:51:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3e3946da-78ff-3350-9973-4485740784af | -9.79638 | -44.82238 | 2026-09-29 04:51:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c6c93afc-cefa-3a72-9e14-0abea590117a | -9.28931 | -49.64172 | 2026-09-29 04:51:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a4d31775-d563-3a0e-a3cc-a85002d4b6a4 | -10.90206 | -44.65583 | 2026-09-29 04:51:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e285408f-cc46-3981-8ab9-89a565b6a303 | -14.11248 | -46.28725 | 2026-09-29 04:51:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 7ed9178f-f6dd-3f00-9208-8060a80b8b5c | -7.24169 | -43.37434 | 2026-09-29 04:51:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| eb0d4f7b-3100-36a2-8da8-a27b1c9c105a | -11.35592 | -54.04287 | 2026-09-29 04:51:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 999c06c4-585c-32b1-b8a3-6a18f50f6bd7 | -9.77626 | -44.81565 | 2026-09-29 04:51:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f29bd437-e741-3846-9f38-ae2e03a0f659 | -12.72291 | -46.99446 | 2026-09-29 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c81cf987-2998-3995-85a9-029675aab361 | -10.80956 | -48.73085 | 2026-09-29 04:51:00 | NPP-375D | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6df97886-f573-37ab-ac1a-f73f2fd974c2 | -12.73974 | -47.27512 | 2026-09-29 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 25.1 |
| a4293e08-e9da-3696-a197-fa1b78f19f43 | -11.09478 | -47.11413 | 2026-09-29 04:51:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 971f3a89-8067-3611-94e6-f6a25f7d6833 | -11.42422 | -43.46832 | 2026-09-29 04:51:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 20.6 |
| 8acf56f9-43a3-33be-8320-20650df266c0 | -11.13005 | -48.33773 | 2026-09-29 04:51:00 | NPP-375D | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 2b9ee25a-159e-35c7-a726-9a5ad23e9f55 | -13.86824 | -43.99909 | 2026-09-29 04:51:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d0cafce5-0074-3ccb-8fd3-7d3b39ad20d8 | -12.04636 | -50.95551 | 2026-09-29 04:51:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 52d1920e-039a-3794-a2dc-ff03be940639 | -13.16078 | -48.56504 | 2026-09-29 04:51:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 399499b5-45bb-3bd6-85db-d0fae99bd35f | -11.16636 | -50.0456 | 2026-09-29 04:51:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bae5d7bb-2190-356d-a4e2-3cb4283e09be | -12.00464 | -50.98129 | 2026-09-29 04:51:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 82c876ac-22a1-3655-9f47-83e868dae7b3 | -9.40293 | -46.84102 | 2026-09-29 04:51:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 28e7f463-48ac-38e9-b34e-dca64abda4a1 | -7.53239 | -45.89228 | 2026-09-29 04:51:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 13b5f5b4-5978-3101-aaa8-55908776ed1f | -7.00592 | -45.2965 | 2026-09-29 04:51:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f4178e29-5dd2-3228-b921-2c13f0aa1e76 | -10.71748 | -44.42468 | 2026-09-29 04:51:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cd26c475-2b26-35bd-8ccd-b7dd993c8ff6 | -11.17425 | -48.06549 | 2026-09-29 04:51:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0d37f4a5-b802-37c2-9e47-daaf9ac2ba2d | -12.79486 | -54.01415 | 2026-09-29 04:51:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c7132a3f-830e-370b-88b4-d9c65c829ab8 | -6.72191 | -45.62177 | 2026-09-29 04:51:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b35c24bd-58b5-319f-881a-59222e0f24ee | -11.3808 | -43.40247 | 2026-09-29 04:51:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b86c6a11-ac5f-3955-8254-cbad4ab1304d | -12.00067 | -51.00605 | 2026-09-29 04:51:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8f473a4c-12ac-37b7-8186-0b1068dd6889 | -11.61543 | -46.78149 | 2026-09-29 04:51:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a8d15d3a-993c-3a18-a7b5-c58f2fd9c4ee | -13.53608 | -49.17823 | 2026-09-29 04:51:00 | NPP-375D | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e9159104-66aa-3eee-bab3-b8eef5d3ca46 | -11.14412 | -50.07826 | 2026-09-29 04:51:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 28678343-77bf-3ecd-80fb-9531a2135fa4 | -11.40086 | -43.43031 | 2026-09-29 04:51:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| dae3ba43-94bd-35e8-b877-5da17ae3ebac | -12.61324 | -47.27599 | 2026-09-29 04:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fb6b2c38-b02c-34ef-9f83-21deae801abf | -13.54008 | -49.17502 | 2026-09-29 04:51:00 | NPP-375D | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |


[Clique aqui para ver as próximas entradas](README43.md)
