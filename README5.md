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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fcd421e2-e034-3dfd-a5f4-a47111ae4e5d | -5.2384 | -45.2085 | 2025-07-30 00:48:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 93e2e1f6-89af-35c4-8294-736980543bca | -11.3231 | -48.928398 | 2025-07-30 00:48:00 | METOP-C | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| db38ed25-a74e-3814-8fe8-07f830b6c509 | -6.5328 | -56.179401 | 2025-07-30 00:48:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 45f07f1a-bb02-3990-a5d4-51a6dc3194a2 | -10.6977 | -48.857498 | 2025-07-30 00:48:00 | METOP-C | OLIVEIRA DE FÁTIMA | TOCANTINS | Brasil | 1715507 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 72c03aff-01df-3ba8-bdc6-1e84cc1a413f | -7.7838 | -44.989601 | 2025-07-30 00:48:00 | METOP-C | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 025861ec-7210-30a3-8a07-30238cfad613 | -6.523 | -56.181499 | 2025-07-30 00:48:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9e122b29-1e1c-3c16-af4a-7f7ec380218a | -2.8967 | -48.247799 | 2025-07-30 00:48:00 | METOP-C | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f44300c5-e20c-3f8a-9969-5f4ff2946f12 | -6.5082 | -56.207199 | 2025-07-30 00:48:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d59d6054-3803-37be-9354-68f2849e6010 | -11.5326 | -44.267899 | 2025-07-30 00:48:00 | METOP-C | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 1a2356ec-ace5-3c78-be4f-dd583253b7ee | -6.5622 | -56.1731 | 2025-07-30 00:48:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a3da1964-f38f-3665-b099-339b98244d77 | -8.6781 | -51.213799 | 2025-07-30 00:48:00 | METOP-C | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fba04e1c-be2f-3237-80d0-e441909c9739 | -9.1513 | -49.850601 | 2025-07-30 00:48:00 | METOP-C | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3d88566d-69e1-3cc9-8ef6-a3955cfd969e | -9.4022 | -45.486801 | 2025-07-30 00:48:00 | METOP-C | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 6184dfed-6abd-304b-9882-7fb18781cab3 | -2.8091 | -48.667999 | 2025-07-30 00:48:00 | METOP-C | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4acc45d9-796a-3638-8107-f2df0618f849 | -6.39 | -53.355999 | 2025-07-30 00:48:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e62f846c-ba07-3548-8b96-52f093911687 | -9.6236 | -48.544998 | 2025-07-30 00:48:00 | METOP-C | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 85151133-47d0-33b6-9fff-e6dcb62c1abe | -13.0833 | -47.304298 | 2025-07-30 00:48:00 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5c324b24-64a6-3403-bfa0-4ea7b35222e6 | -10.6215 | -45.230598 | 2025-07-30 00:48:00 | METOP-C | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 3d03161d-df13-3ab4-b707-e2ef3aa069fc | -2.9065 | -48.245499 | 2025-07-30 00:48:00 | METOP-C | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0a97a73c-5bae-3aab-999f-23c54d7e0c0d | -11.9224 | -44.547401 | 2025-07-30 00:48:00 | METOP-C | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 477631fe-825f-31d2-a34f-0688f4a13b58 | -8.9505 | -46.743401 | 2025-07-30 00:48:00 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b6437550-b87a-3bb4-a7c9-4b4dfe3bc859 | -6.3849 | -53.333302 | 2025-07-30 00:48:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e82156ce-d221-3757-af53-f1374f435902 | -7.8546 | -46.739201 | 2025-07-30 00:48:00 | METOP-C | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3bb30947-bf5b-3751-8da7-7ac48d50c6f8 | -9.6351 | -48.550098 | 2025-07-30 00:48:00 | METOP-C | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ae1a641d-ff65-3442-bc26-3e206b6ebbbd | -2.8071 | -48.659801 | 2025-07-30 00:48:00 | METOP-C | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8189ec19-caba-309a-8bf3-4413f94d9b57 | -11.9885 | -46.6968 | 2025-07-30 00:48:00 | METOP-C | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1da44f00-fa9b-30b5-ad82-281df218f7ee | -6.5035 | -56.185699 | 2025-07-30 00:48:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cf56e0fe-5e1d-39b2-bd43-606de8b53400 | -11.4676 | -45.096401 | 2025-07-30 00:48:00 | METOP-C | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 5b1d068b-65f7-38d0-9ad5-a9bd74851287 | -11.5463 | -44.240002 | 2025-07-30 00:48:00 | METOP-C | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 7023865c-31dd-344e-a709-af53086c5cca | -6.5645 | -56.183899 | 2025-07-30 00:48:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a05e6ac8-84fe-3b97-9946-bfca3628172b | -6.4961 | -56.198502 | 2025-07-30 00:48:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a00a041e-2533-3cb5-8348-f365c0c62e5a | -11.3536 | -51.250099 | 2025-07-30 00:48:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 6749ac9d-431e-3108-b640-f44ea1cd31a3 | -17.489799 | -46.744301 | 2025-07-30 00:48:00 | METOP-C | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| ca7238b7-1e0f-3eb6-af79-e503ff56a2c6 | -11.3296 | -48.911999 | 2025-07-30 00:48:00 | METOP-C | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4d477756-5b08-36a8-94cb-c87ec0549181 | -9.2331 | -48.5975 | 2025-07-30 00:48:00 | METOP-C | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| cc21b810-6d25-3c8e-83b6-561fc66a7899 | -6.5301 | -56.213799 | 2025-07-30 00:48:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4d3da53e-31e0-32e0-97fd-3316d9dc5be7 | -6.4194 | -53.349602 | 2025-07-30 00:48:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a21da85f-bc4b-38ea-8214-18e2cd7c8cb8 | -4.3807 | -49.038101 | 2025-07-30 00:48:00 | METOP-C | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 08765cd3-7830-3fdd-a152-ad0d26adbc06 | -7.7866 | -45.001202 | 2025-07-30 00:48:00 | METOP-C | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 1546368a-b4df-30f2-9c54-77a33e139b9b | -8.0143 | -47.6726 | 2025-07-30 00:48:00 | METOP-C | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| cd965c23-d799-37e7-87fc-ee5c7d446827 | -9.1627 | -49.855301 | 2025-07-30 00:48:00 | METOP-C | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e12014c7-173e-37b9-ba95-f0a1bf6cdca6 | -14.7376 | -46.298302 | 2025-07-30 00:48:00 | METOP-C | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 1c9c1dd8-8d0d-3246-8218-c645a83dd829 | -8.0181 | -47.6889 | 2025-07-30 00:48:00 | METOP-C | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| fb4d85b4-b7fe-38b2-b6b8-1e0ea655e82b | -11.3215 | -48.921398 | 2025-07-30 00:48:00 | METOP-C | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 262e507a-26f2-35df-9285-0906edcb0bcb | -10.2852 | -46.923801 | 2025-07-30 00:48:00 | METOP-C | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 41152a4a-747c-3625-9a9e-5c23ed2bd4ee | -11.9197 | -44.536598 | 2025-07-30 00:48:00 | METOP-C | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| a8c8e7a0-b4ff-37d8-9275-46a710a8ecda | -11.5394 | -44.253899 | 2025-07-30 00:48:00 | METOP-C | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 4dc04cfa-80ab-3d74-9a11-c1013a9bfa4f | -9.7433 | -48.571098 | 2025-07-30 00:48:00 | METOP-C | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 81109708-8570-31b5-b770-98f9586e4fbb | -9.1865 | -43.1478 | 2025-07-30 00:48:00 | METOP-C | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 5b4fda0b-4578-3dff-892d-85ff11b45b0e | -10.2754 | -46.926102 | 2025-07-30 00:48:00 | METOP-C | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7f72b426-0194-31e4-8318-8c39f04b2e49 | -4.6487 | -43.114799 | 2025-07-30 00:48:00 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c2e9d95e-f972-3e7d-98ab-588ca06b106f | -8.5167 | -43.3162 | 2025-07-30 00:48:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 8a9f6f5f-4d35-3f05-9987-d384188d4650 | -8.9603 | -46.7411 | 2025-07-30 00:48:00 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3151147b-3c8c-35e9-879b-4e4a651895d9 | -11.2821 | -52.466301 | 2025-07-30 00:48:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e15b8272-51b2-32a1-aad8-57bbb8cd6222 | -4.3771 | -49.022701 | 2025-07-30 00:48:00 | METOP-C | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a66326ad-2226-3890-9202-66de1c8a1e4d | -3.5886 | -52.540501 | 2025-07-30 00:48:00 | METOP-C | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ec40bad6-a3b3-3c2c-8fab-8750a73b501c | -9.1497 | -49.8437 | 2025-07-30 00:48:00 | METOP-C | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 76c6486e-85a3-3aaf-ac46-1f00d249a6ae | -9.4205 | -40.354198 | 2025-07-30 00:48:00 | METOP-C | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| dd8e5856-a6b7-399b-ad90-a9462bf4f64d | -6.5059 | -56.1964 | 2025-07-30 00:48:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2c5b78ba-5e30-32a1-b3c9-142246f2f5ba | -8.6292 | -45.878399 | 2025-07-30 00:48:00 | METOP-C | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 411a421d-2977-35c9-b50e-3e10f9e410bd | -11.5435 | -44.2285 | 2025-07-30 00:48:00 | METOP-C | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 3fd01728-d647-3580-9ab8-fabf38c1af47 | -10.7075 | -48.855202 | 2025-07-30 00:48:00 | METOP-C | OLIVEIRA DE FÁTIMA | TOCANTINS | Brasil | 1715507 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 78938560-86c7-39fe-abf5-6ffadfb1a449 | -12.8143 | -45.442902 | 2025-07-30 00:48:00 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| c3c671ba-3f9d-37d0-9cf4-2cc422e9fb13 | -20.299999 | -50.953899 | 2025-07-30 00:48:00 | METOP-C | SANTA FÉ DO SUL | SÃO PAULO | Brasil | 3546603 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 38c21435-6288-31b6-80ed-0bcb5c3d9b20 | -9.436 | -40.374199 | 2025-07-30 00:48:00 | METOP-C | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 26236f0d-27d1-3665-b110-e72125b58f8e | -11.4726 | -45.116699 | 2025-07-30 00:48:00 | METOP-C | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 22d33f89-79e9-306d-9de2-48b9babb19cf | -12.7118 | -47.791801 | 2025-07-30 00:48:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c851775e-601f-3c96-9875-a664448862fd | -6.4015 | -53.3615 | 2025-07-30 00:48:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5fcdf5d0-a15e-3e6b-9d6a-65f51f3ce931 | -7.9429 | -44.080898 | 2025-07-30 00:48:00 | METOP-C | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| b335d4a6-4f0d-3c82-96f9-dacf4435c047 | -8.8852 | -47.337101 | 2025-07-30 00:48:00 | METOP-C | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4475ff6e-af9b-30f8-a2e5-8b7cb080bfdc | -8.9582 | -46.7323 | 2025-07-30 00:48:00 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a1d7e8da-1fa3-377c-a0cc-2bdf71e333a1 | -17.9601 | -50.390499 | 2025-07-30 00:48:00 | METOP-C | MAURILÂNDIA | GOIÁS | Brasil | 5213004 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 787d9eb8-203f-34d1-9f50-13c68eacb01f | -11.8192 | -44.255699 | 2025-07-30 00:48:00 | METOP-C | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 866a302a-95e6-36ed-b4d5-4ab2accd8383 | -11.3312 | -48.919102 | 2025-07-30 00:48:00 | METOP-C | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e3639c0f-7bc3-3bf3-903e-8a9bc9119db6 | -11.5492 | -44.2514 | 2025-07-30 00:48:00 | METOP-C | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 39f00eea-de71-3971-a9a5-8eb8bd659eab | -10.6993 | -48.864601 | 2025-07-30 00:48:00 | METOP-C | OLIVEIRA DE FÁTIMA | TOCANTINS | Brasil | 1715507 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| fbf98b77-58c4-370a-ac1a-28a31c5b90ff | -17.4863 | -46.729198 | 2025-07-30 00:48:00 | METOP-C | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| acf4f506-34f1-3720-8e6d-e51fbf7457a7 | -9.1611 | -49.8484 | 2025-07-30 00:48:00 | METOP-C | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a258d1fc-5d79-3265-8b38-30ddb646bbda | -9.1481 | -49.8367 | 2025-07-30 00:48:00 | METOP-C | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3f69bcd1-24cb-340d-93f9-fb6210db42dc | -12.4743 | -47.264099 | 2025-07-30 00:48:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| df46a759-420f-382c-9beb-8afa9a888a57 | -4.6444 | -43.097301 | 2025-07-30 00:48:00 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ccaf3dc4-50f3-32f1-bbea-2cfdf79c01c6 | -7.8524 | -46.730099 | 2025-07-30 00:48:00 | METOP-C | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 724dfa1b-792c-3a63-a545-58884e885dd8 | -8.0241 | -47.6703 | 2025-07-30 00:48:00 | METOP-C | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 982a7f52-bd0a-3e6f-bf63-55df96d58593 | -4.8898 | -44.957699 | 2025-07-30 00:48:00 | METOP-C | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d916a534-7e17-3272-8ed3-95330d63fa01 | -8.0279 | -47.6866 | 2025-07-30 00:48:00 | METOP-C | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| eb911e6a-2914-3485-bf1d-bd4aa1430ad7 | -10.6265 | -45.251099 | 2025-07-30 00:48:00 | METOP-C | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 9a93747c-9c9d-36cb-9ad9-8c9f90d53c7a | -19.9305 | -49.907101 | 2025-07-30 00:48:00 | METOP-C | SÃO FRANCISCO DE SALES | MINAS GERAIS | Brasil | 3161304 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 2851b3d1-4fa4-32f5-b289-140b7657a848 | -11.4578 | -45.098801 | 2025-07-30 00:48:00 | METOP-C | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| fcf3d1fc-eefc-3c3d-bde1-fa72434d9547 | -6.518 | -56.205101 | 2025-07-30 00:48:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4914f785-bdc5-32a5-a0ac-260f4277b349 | -11.5533 | -44.226101 | 2025-07-30 00:48:00 | METOP-C | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e268cd24-8294-33ee-8a72-c5e7f28a906d | -11.8095 | -44.258099 | 2025-07-30 00:48:00 | METOP-C | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 84f1c63d-bc99-32f7-bd9c-4d4f02bbd852 | -10.6092 | -45.222801 | 2025-07-30 00:48:00 | METOP-C | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| c4d80a94-5860-346f-a8a4-9698760c583c | -4.3789 | -49.030399 | 2025-07-30 00:48:00 | METOP-C | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 01718c75-3810-3fb1-8462-51b8ecf95f0e | -9.1762 | -48.841202 | 2025-07-30 00:48:00 | METOP-C | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| bb17f15a-dfa4-37b5-9078-c195a37199f8 | -12.4586 | -44.080502 | 2025-07-30 00:48:00 | METOP-C | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 3a8da2d2-f597-3492-a986-398514a76bf6 | -7.7332 | -51.0924 | 2025-07-30 00:48:00 | METOP-C | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bb29bc55-d1a6-35a4-a58c-5f4f10bd361b | -4.639 | -43.1171 | 2025-07-30 00:48:00 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e8ec4a30-bcff-3414-b3a2-046bac17ab65 | -5.2414 | -45.220798 | 2025-07-30 00:48:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0af77a5c-5a3f-35c3-961e-1cf66bd2436b | -10.0917 | -46.979099 | 2025-07-30 00:48:00 | METOP-C | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| eb98717e-86ce-3211-bc9f-c0ac2ad99a55 | -18.562901 | -44.422401 | 2025-07-30 00:48:00 | METOP-C | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README6.md)
