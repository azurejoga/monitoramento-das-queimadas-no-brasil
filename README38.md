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

## Dados Diários - Página 38

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8db85219-1305-38a4-a532-7cdce814483d | -16.02383 | -44.28875 | 2025-10-04 03:53:00 | NPP-375D | JAPONVAR | MINAS GERAIS | Brasil | 3135357 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5b80b4eb-4b78-3c10-a11e-f4677ed2cdbf | -14.69648 | -48.09643 | 2025-10-04 03:53:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 40702a4f-92fd-3aad-96a4-866c0fdf3e9e | -12.0762 | -45.19027 | 2025-10-04 03:53:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8938afc1-fb16-38cc-baa9-7a7ba20a7bbc | -14.63077 | -48.25575 | 2025-10-04 03:53:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 7793a64f-1e3e-3f79-8322-7cd0fc51b665 | -15.72305 | -46.28893 | 2025-10-04 03:53:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 63c6e354-07e3-3a0b-bbc6-e86727daad04 | -16.01393 | -50.93674 | 2025-10-04 03:53:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 7588191a-07a3-32f0-851a-719aa6d593f0 | -13.25653 | -47.26846 | 2025-10-04 03:53:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 55106cd2-ae78-3e9b-a238-d4b93b74ce55 | -14.92424 | -46.86762 | 2025-10-04 03:53:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 06e2e7cf-7823-3117-af6c-86414605607e | -17.08182 | -46.25594 | 2025-10-04 03:53:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e9b15eef-9ebc-3781-8859-94be4f2684e8 | -15.35245 | -47.95514 | 2025-10-04 03:53:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2052a81a-40c1-30c1-838d-6484d7f4072d | -14.66859 | -48.28968 | 2025-10-04 03:53:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9ce2935c-6894-356d-99c3-a5d5d3a1c5c5 | -16.02951 | -50.94368 | 2025-10-04 03:53:00 | NPP-375D | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1f33bf90-b84f-3f8d-90c5-04ce6d993d2e | -14.65982 | -48.30542 | 2025-10-04 03:53:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 3e79e476-d174-3c16-a98b-89f783e8a583 | -13.58315 | -48.17718 | 2025-10-04 03:53:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9abbface-c734-3bc9-a642-faf8e4050b45 | -14.45872 | -46.33812 | 2025-10-04 03:53:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 67a271cf-a7fe-3747-a1c0-a6878fb3e7bc | -11.79362 | -46.82265 | 2025-10-04 03:53:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 4691ecd6-2082-3384-9dbe-49267a30c513 | -15.2073 | -47.19148 | 2025-10-04 03:53:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 672e6fe6-e845-3de6-82df-573e287376b3 | -15.71943 | -46.28279 | 2025-10-04 03:53:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 306818de-031b-328a-86e3-89de5e523adf | -11.49812 | -46.75743 | 2025-10-04 03:53:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| dfa78b4f-654f-32b6-b9ea-89502253f0e8 | -11.70452 | -47.5113 | 2025-10-04 03:53:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d8e22c21-c249-3e16-8d1c-186d5d6783c3 | -14.67929 | -48.26439 | 2025-10-04 03:53:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7761300f-a6b8-384b-9e48-7cb2304081b5 | -14.60579 | -46.73028 | 2025-10-04 03:53:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 04841c86-6360-3190-8a6d-22e1fc6b1943 | -13.58895 | -48.17681 | 2025-10-04 03:53:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 0d1ca646-9126-339e-9f4d-daa5eca84ed0 | -15.34586 | -47.82563 | 2025-10-04 03:53:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| a62347c6-f4ad-375b-8893-dd559440b305 | -13.99572 | -48.19087 | 2025-10-04 03:53:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| fa0e9db1-c008-3e76-ae26-d576d22f856b | -14.865 | -48.35918 | 2025-10-04 03:53:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2e66967f-676d-337a-8127-78347d6d6a8c | -17.15573 | -47.02633 | 2025-10-04 03:53:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e32baeec-aefb-3701-9cc9-89a2236b326c | -13.32592 | -47.19156 | 2025-10-04 03:53:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8f964ee3-8654-3e2d-a1cd-b3d62b86b57f | -15.28399 | -47.92025 | 2025-10-04 03:53:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 0d08211f-451e-3ba4-b6d5-cec27e40ebdb | -15.27812 | -47.14629 | 2025-10-04 03:53:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b913aa7d-9a7c-3b6e-b50b-8a82d95d1549 | -12.7068 | -48.56535 | 2025-10-04 03:53:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1d9b157c-db3a-3c57-a1a8-1ffe5ebef3d7 | -12.81503 | -46.86651 | 2025-10-04 03:53:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8b69989f-9f53-35c7-ba46-cb4742b50a89 | -13.16882 | -47.88752 | 2025-10-04 03:53:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 83029ac8-a590-307f-a2de-13f95c674d2f | -13.33388 | -48.08866 | 2025-10-04 03:53:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1ddf710a-645f-3e8b-9a33-78a099579495 | -13.12379 | -47.83258 | 2025-10-04 03:53:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| ab4e15e8-e686-36c7-8c41-811a5d0585ab | -12.86793 | -46.99033 | 2025-10-04 03:53:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 0e2ba211-1e80-34b1-9e8e-a6ffeacd979b | -13.31615 | -47.79694 | 2025-10-04 03:53:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c8f81100-330a-3115-8cb9-61859352fd86 | -16.00067 | -50.92813 | 2025-10-04 03:53:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 321faf28-3aac-3808-ae4f-2f01318c8c15 | -13.34033 | -47.61481 | 2025-10-04 03:53:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| efd00cb8-1c24-3a94-bad4-30b92c6f4580 | -13.50862 | -47.27504 | 2025-10-04 03:53:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7360b848-6b51-3637-8566-cd475b52bda4 | -12.03132 | -45.20154 | 2025-10-04 03:53:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 5c9e23e2-bade-3302-9b9b-389b28fe4ad1 | -14.35476 | -46.10966 | 2025-10-04 03:53:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 5222867a-bad0-3779-85c9-fa8e28d0334f | -14.92308 | -46.87372 | 2025-10-04 03:53:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b7d535b6-1d1b-34c0-a716-63d6db7eb1ac | -13.99193 | -48.18188 | 2025-10-04 03:53:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b00d4feb-8105-3bd4-82a2-70bbc543e3c0 | -14.45779 | -46.34289 | 2025-10-04 03:53:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 649cd2d5-ae1f-3ec2-b5b1-031736cf7f7e | -11.84445 | -44.93938 | 2025-10-04 03:53:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2d796165-7ddd-3584-b1dc-9ce08cfb2f8b | -16.02126 | -50.95182 | 2025-10-04 03:53:00 | NPP-375D | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 59e896e1-e1a5-3b41-8b77-4c73dbca5324 | -11.79774 | -45.01756 | 2025-10-04 03:53:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 570d0281-a044-397a-a9f6-c82ff0e6ab78 | -13.57795 | -48.1752 | 2025-10-04 03:53:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 151adfcd-0fba-3bb3-aa56-c567ac432be3 | -16.75667 | -43.96625 | 2025-10-04 03:53:00 | NPP-375D | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c7ed7b18-5cb9-32be-a6a9-f47c5c68d5f7 | -14.8476 | -48.28008 | 2025-10-04 03:53:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a713454d-89b2-30b9-bcb1-26331cc93908 | -11.55831 | -47.67982 | 2025-10-04 03:53:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 32219f93-66e7-3f13-882f-905a98670dda | -13.14707 | -47.94154 | 2025-10-04 03:53:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 07c0cca6-6723-34c9-a960-f231d2c6e3d6 | -13.99496 | -48.19463 | 2025-10-04 03:53:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7a897ab3-348c-3593-995f-2d390a44a33b | -17.58347 | -44.4967 | 2025-10-04 03:53:00 | NPP-375D | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| fe5471a8-648e-3d19-82f6-fb8d2b7b0bc9 | -13.54589 | -47.24748 | 2025-10-04 03:53:00 | NPP-375D | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 91bcdde0-85d2-3688-95b0-0d08ca8aaf8b | -11.77829 | -46.81908 | 2025-10-04 03:53:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3ff392bb-236b-3c3f-b2f2-12eaa6c0076e | -14.90283 | -48.28239 | 2025-10-04 03:53:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c8fb4b47-4a18-3628-90c1-3d67bf81b451 | -14.85079 | -48.28228 | 2025-10-04 03:53:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 11e018e9-eff0-32ca-b9f1-e8025e658f0f | -15.74113 | -46.26976 | 2025-10-04 03:53:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| eecb0e9d-266a-35dc-bb4b-d82a071a0271 | -17.08002 | -46.24078 | 2025-10-04 03:53:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| db7f8be3-74fd-373e-9818-9c6b43aa0997 | -13.99256 | -48.2064 | 2025-10-04 03:53:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 51e03ae8-748e-37cd-b3db-e50119fb453e | -11.78935 | -46.83802 | 2025-10-04 03:53:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d3ec1d7f-5806-3a55-9037-f77c83680d72 | -15.53291 | -46.81582 | 2025-10-04 03:53:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 24e1842d-a424-3d7d-8012-a05abe716e86 | -16.35381 | -49.40001 | 2025-10-04 03:53:00 | NPP-375D | BRAZABRANTES | GOIÁS | Brasil | 5203609 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 299a1aaf-bb79-31b2-99ab-21117037b9ae | -11.84318 | -45.04886 | 2025-10-04 03:53:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 854639ad-ef5c-332e-8d29-0eff0fe962d5 | -13.23714 | -48.48997 | 2025-10-04 03:53:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 18eef143-ed44-3dbe-9e94-92f5a755d703 | -13.21466 | -47.82361 | 2025-10-04 03:53:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 65445ead-a3f3-3c09-ad9e-fa581831cb77 | -16.75368 | -43.96024 | 2025-10-04 03:53:00 | NPP-375D | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 07360afc-8c69-3282-a821-7de031a78723 | -13.50936 | -47.2712 | 2025-10-04 03:53:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 484e33db-b580-309a-9bde-03e898570140 | -15.62227 | -46.93786 | 2025-10-04 03:53:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0d39e2fc-9417-3598-b1c9-9771f35682d2 | -15.16175 | -44.07577 | 2025-10-04 03:53:00 | NPP-375D | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 14e40c6c-36cf-3a51-acfc-f897e4586538 | -13.62624 | -48.6718 | 2025-10-04 03:53:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b14c1632-2de5-31a0-bc8b-a501896f27bc | -14.65233 | -48.28711 | 2025-10-04 03:53:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5e22b47e-a1c9-30fe-8686-1a6b291b8e48 | -11.82888 | -44.92206 | 2025-10-04 03:53:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1b0fd24d-e40b-39e3-92d7-45fd94100b23 | -11.78603 | -46.82713 | 2025-10-04 03:53:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| a937f39a-2ad3-3afd-960d-088aeb088ca6 | -13.51366 | -47.27662 | 2025-10-04 03:53:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| bdad94f3-e3f1-342e-9fc8-b4f6a71f62cc | -14.63657 | -48.24684 | 2025-10-04 03:53:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b85c7bf4-da4d-32c1-a833-903c8df77d34 | -17.16882 | -47.03699 | 2025-10-04 03:53:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 2343d4e0-8a19-3b34-935b-09ff075af8ae | -13.88239 | -46.51297 | 2025-10-04 03:53:00 | NPP-375D | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 8263ba47-554a-38e7-abbc-79bfc437765f | -13.31991 | -48.13084 | 2025-10-04 03:53:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 67d975ae-35cc-364b-961d-6be87388d24b | -13.57581 | -48.18581 | 2025-10-04 03:53:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 9665bb79-bd10-3d1a-bfae-f4c90fe8885d | -11.55764 | -47.68327 | 2025-10-04 03:53:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a1cbd93b-ce46-3ba8-bf5f-32f8be4d9b25 | -15.2833 | -47.92368 | 2025-10-04 03:53:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 06b69431-0157-3c79-bef8-ed1e82593ec1 | -17.57751 | -44.46169 | 2025-10-04 03:53:00 | NPP-375D | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d4f94c77-9754-3f4c-8166-54540c606829 | -12.41014 | -45.16151 | 2025-10-04 03:53:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1b281daf-f433-3557-9c8b-717f4c47c28c | -14.23485 | -46.0927 | 2025-10-04 03:53:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7c48d8e7-4401-346c-9583-98401de2e593 | -11.91372 | -46.25066 | 2025-10-04 03:53:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 02494432-3442-30e3-bbce-38f4c484deef | -14.97982 | -46.84951 | 2025-10-04 03:53:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 15c550aa-1ea5-36c6-a547-f107b1ed2392 | -13.11711 | -47.8381 | 2025-10-04 03:53:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6c4f3b5e-db94-3dbf-886e-b7636423138b | -15.28311 | -47.14533 | 2025-10-04 03:53:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3a0c51e1-b046-3321-90fb-064dfb1ff1b1 | -12.64321 | -46.97955 | 2025-10-04 03:53:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| c5465214-f2f7-318d-a1d1-b93d32a326be | -17.15361 | -47.03915 | 2025-10-04 03:53:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 48c193a8-f881-34d0-90ea-dcdee9a39dbb | -13.97318 | -48.18681 | 2025-10-04 03:53:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3730b911-ce04-3e94-b9b5-d937cfe3a27e | -17.08129 | -43.35605 | 2025-10-04 03:53:00 | NPP-375D | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 07dfe329-d2a5-3559-b17a-acef37d408e9 | -13.11872 | -47.94291 | 2025-10-04 03:53:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 22.2 |
| 054a7959-2f05-39c5-a197-9cd7581b2b90 | -15.02988 | -49.45595 | 2025-10-04 03:53:00 | NPP-375D | NOVA GLÓRIA | GOIÁS | Brasil | 5214861 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 62b88c23-50c3-301d-a8ae-bc6131a4b5bb | -13.2361 | -47.837 | 2025-10-04 03:53:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 98a0b606-8b4f-3dd7-b35b-94bb1adcb742 | -14.33123 | -45.86304 | 2025-10-04 03:53:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 35d38b25-7c97-3f68-bf31-fd94c50959f5 | -14.91786 | -46.88149 | 2025-10-04 03:53:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |


[Clique aqui para ver as próximas entradas](README39.md)
