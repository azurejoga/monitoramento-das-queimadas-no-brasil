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

## Dados Diários - Página 47

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 65be6def-19a1-3d70-bf48-b3e5675aac75 | -3.86464 | -43.35302 | 2025-10-28 04:42:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 24aa5bcb-718b-385e-9b48-d817e766453b | -2.99437 | -51.03888 | 2025-10-28 04:42:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 12a3ec70-f8be-3002-b9c8-a89c0245ef55 | -3.58263 | -43.62393 | 2025-10-28 04:42:00 | NPP-375D | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6344c027-cb41-3a16-b710-8d98b97acf03 | -7.36779 | -47.79373 | 2025-10-28 04:42:00 | NPP-375D | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2ff7ee39-81a1-3d0e-927c-dff62e0591f0 | -8.09987 | -45.68371 | 2025-10-28 04:42:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 38835e77-837e-3017-8b4e-05242bf751df | -5.66114 | -41.1381 | 2025-10-28 04:42:00 | NPP-375D | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 32092b92-ff37-3093-971e-528af2e22274 | -5.56919 | -50.0972 | 2025-10-28 04:42:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2d36406b-8cba-3a4b-8709-46e05617e782 | -5.42378 | -44.80795 | 2025-10-28 04:42:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 94cc9cba-2790-3237-a8fb-8d9640517c70 | -2.22577 | -48.37328 | 2025-10-28 04:42:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 37af4131-eada-380a-80d4-d75a471e2bce | -2.86133 | -48.67776 | 2025-10-28 04:42:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3ec0b534-1913-3350-898d-16147b28e94b | -7.03284 | -47.61889 | 2025-10-28 04:42:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1d389ed5-322a-388b-8bb7-18f33302b72e | -1.86334 | -54.5197 | 2025-10-28 04:42:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a5eadad8-f1bf-3e86-bbf9-d9e26865b132 | -7.34335 | -50.77429 | 2025-10-28 04:42:00 | NPP-375D | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 419bc971-eb3a-3519-857b-aaddf9992f79 | -7.97403 | -46.74072 | 2025-10-28 04:42:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 9e1aa062-723f-3047-9066-e22e38dc868d | -8.10056 | -45.67891 | 2025-10-28 04:42:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 06ba148d-e7f8-3828-9629-0a605328f1f1 | -7.38823 | -45.12355 | 2025-10-28 04:42:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 74985df0-c7ee-3acc-b64f-8057febdf9e1 | -7.86542 | -46.39236 | 2025-10-28 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5293ad9b-0290-3b36-bce3-f5df1ccf2bbc | -5.4683 | -47.26203 | 2025-10-28 04:42:00 | NPP-375D | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b09e9200-fe7f-3bf0-8524-5b8dca948fcb | -8.07918 | -45.95799 | 2025-10-28 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 524c0f76-e8ad-3849-bfd2-39b706cabd70 | -7.81334 | -46.44806 | 2025-10-28 04:42:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 7f54c898-a832-30b3-b0b3-c48a63e0d1a3 | -3.54759 | -54.69233 | 2025-10-28 04:42:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a67e9e10-3dfc-3f0a-85b8-0e2233951c40 | -4.88074 | -47.54502 | 2025-10-28 04:42:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c8a571a1-1e64-336b-9152-d3fbe10043eb | -5.61589 | -51.78933 | 2025-10-28 04:42:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 23a58bcd-05c5-3a89-931e-68fbabd52a9e | -3.42724 | -54.53598 | 2025-10-28 04:42:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0da328a7-0cb3-3ce5-995c-4cacd4a9ba2a | -3.20976 | -48.95547 | 2025-10-28 04:42:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e44e0b37-de7d-34b4-bb83-9a678d4925e1 | -4.57369 | -46.49158 | 2025-10-28 04:42:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f553281c-a6fb-3cbf-a8f7-5c78cec03659 | -6.65009 | -44.60321 | 2025-10-28 04:42:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cc4893a7-5bf1-3257-97f6-8d6899573694 | -7.2144 | -46.71623 | 2025-10-28 04:42:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 964d78d1-0671-343c-bc65-dc3d3c84602d | -5.3637 | -50.5661 | 2025-10-28 04:42:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b9ed8d93-2c9f-3a07-a3dd-3a90537fba54 | -7.96003 | -47.2364 | 2025-10-28 04:42:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a8c6c661-0fbb-36c5-abdb-c1fa932e4bb8 | -7.51197 | -46.29669 | 2025-10-28 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5a705915-f6a7-3e86-8358-77415ad010eb | -6.69487 | -42.04181 | 2025-10-28 04:42:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 11.4 |
| e80a3cb2-538d-3d66-989f-2e805c51803a | -6.87817 | -43.58735 | 2025-10-28 04:42:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c9e1f421-a21f-347c-a892-878dea377b96 | -3.70986 | -47.64616 | 2025-10-28 04:42:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7c52b231-aa57-3413-a7c0-1960ecf6b4ee | -2.83122 | -49.40376 | 2025-10-28 04:42:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| c616e0a0-e971-3b15-9945-3020cb1c47d6 | -4.37172 | -49.67182 | 2025-10-28 04:42:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 46d1ac09-33e7-3924-b19b-773a6dcd0b42 | -3.57411 | -49.02364 | 2025-10-28 04:42:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 99f280e1-7cc0-3f10-89ad-eb90fcd46fa3 | -4.25473 | -53.54228 | 2025-10-28 04:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a41dd67f-cd33-32e1-a6d1-097c836a82a4 | -7.8108 | -46.46498 | 2025-10-28 04:42:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 83c10c2a-3003-3161-ad1e-5a47733b0ea1 | -3.28337 | -41.09423 | 2025-10-28 04:42:00 | NPP-375D | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 45b309a7-a3ab-3e26-b81d-9d5719865144 | -3.70367 | -47.64161 | 2025-10-28 04:42:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4a8640fd-7edd-3d28-8942-16adee7f4789 | -7.94683 | -45.49992 | 2025-10-28 04:42:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| acbbb1c9-8d74-3d69-8f24-c0be18c46351 | -5.4408 | -47.39959 | 2025-10-28 04:42:00 | NPP-375D | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8efffb21-1856-3cd3-860c-7cf9a8bc725f | -7.95244 | -45.51557 | 2025-10-28 04:42:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| db46fe46-5e1e-3dae-bd7b-3324fbae36b3 | -7.80841 | -46.456 | 2025-10-28 04:42:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 4e0bcb5b-70dc-399b-92fb-951acf3cc28f | -3.22635 | -50.74153 | 2025-10-28 04:42:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1e93a042-4fef-3953-9996-b5f792b7586e | -7.95175 | -45.46659 | 2025-10-28 04:42:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 04812f0e-e640-3a42-8d3e-9a77e390419f | -4.08323 | -44.42824 | 2025-10-28 04:42:00 | NPP-375D | SÃO MATEUS DO MARANHÃO | MARANHÃO | Brasil | 2111508 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fcd78bec-1333-3e02-b128-1f51bad509c7 | -8.18602 | -45.7114 | 2025-10-28 04:42:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b5d5d420-e6c8-3849-94f6-13a7b3cce5a9 | -5.91738 | -48.17076 | 2025-10-28 04:42:00 | NPP-375D | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5e0b7f8a-9591-3da9-b2b3-4cead8b7c46b | -8.18725 | -44.44187 | 2025-10-28 04:42:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 61cd2447-9b20-3424-80bf-2e36450b5c3e | -7.2307 | -44.99445 | 2025-10-28 04:42:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1f3cd6e3-5243-3698-b35c-fc4c699129a9 | -6.74639 | -48.69127 | 2025-10-28 04:42:00 | NPP-375D | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5d136280-40ca-34b6-818d-e14fc3052f47 | -6.69413 | -42.04708 | 2025-10-28 04:42:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 11.4 |
| ee5bac7d-2612-3b8e-9a2a-ca2b0187b46f | -7.81529 | -46.43511 | 2025-10-28 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 24d7546a-6d11-3cc6-be04-54370d1c3486 | -2.7206 | -49.15841 | 2025-10-28 04:42:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c857106f-397e-3d83-98a5-6ca954845992 | -3.3913 | -50.38638 | 2025-10-28 04:42:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 455ebfd2-94ad-3dd2-9a4f-fbfa1af56dcb | -3.10681 | -50.17896 | 2025-10-28 04:42:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2407bce2-1772-3e8c-a958-7e777399ce0f | -7.96479 | -45.45894 | 2025-10-28 04:42:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 6.3 |
| f23d9c61-e5b2-3a05-a7a4-cd39a3cb7f86 | -5.91791 | -45.39539 | 2025-10-28 04:42:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ce1e252c-0187-370d-bf4a-72f92d600af5 | -6.62634 | -44.62522 | 2025-10-28 04:42:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f0359417-10fd-387d-b94a-06de021e9826 | -7.12499 | -47.02537 | 2025-10-28 04:42:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 0bd2f67b-2613-3983-839b-3cd01496922d | -4.14766 | -47.65866 | 2025-10-28 04:42:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ae403734-11ce-3079-a8c4-83fceaa76e1b | -3.83732 | -50.19779 | 2025-10-28 04:42:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 797867bb-7784-3f80-8511-f58ff90ddd3f | -6.55649 | -41.61039 | 2025-10-28 04:42:00 | NPP-375D | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| eeb881af-640b-3e30-90f6-93f1db8767bc | -1.49851 | -53.12177 | 2025-10-28 04:42:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d5fa2d58-22ee-3a49-8bf1-d0ea76181b63 | -7.81382 | -46.46979 | 2025-10-28 04:42:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 2077f75b-980a-3a8e-b3e6-6b5bf567fcfa | -4.22208 | -48.37012 | 2025-10-28 04:42:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1958b8d7-bd8b-3ee3-a98b-7f6ba00f7a16 | -5.57093 | -47.5023 | 2025-10-28 04:42:00 | NPP-375D | SÃO MIGUEL DO TOCANTINS | TOCANTINS | Brasil | 1720200 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| eba7193f-6fbd-3ed2-b438-73278eebbfcf | -7.47235 | -47.15415 | 2025-10-28 04:42:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 47c67663-edf4-349a-830f-7caccbf2ced7 | -7.45907 | -47.02613 | 2025-10-28 04:42:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 2b17f660-e9b4-36ed-8fc9-00382e531ffe | -7.83211 | -46.3982 | 2025-10-28 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 37af4452-ac34-38f3-84ee-c550635b9d6a | -7.95488 | -45.52579 | 2025-10-28 04:42:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 8fecdf07-2a7a-34c9-b142-cadba87b680a | -6.12565 | -42.44504 | 2025-10-28 04:42:00 | NPP-375D | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 40c143a9-1030-30ff-b140-6e25ec595149 | -1.49634 | -53.12338 | 2025-10-28 04:42:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 64486d08-1d26-3b87-86b2-b91478ad926a | -7.30154 | -45.06187 | 2025-10-28 04:42:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 7929d711-4251-348b-8750-4b9bfcbb1de0 | -7.83254 | -46.4202 | 2025-10-28 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7f10e97d-4ba6-3c26-9f82-e7433786b6cb | -4.10062 | -48.02541 | 2025-10-28 04:42:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 827d8d61-d68a-36ba-932e-9ea9d29da79b | -3.57134 | -49.01966 | 2025-10-28 04:42:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4b27ec33-03bc-3ac3-9b61-6abc6772e3ae | -4.72651 | -43.2006 | 2025-10-28 04:42:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b25c1ba4-c20e-3673-af15-b6ea0e093dda | -2.80868 | -49.13675 | 2025-10-28 04:42:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 935293bd-d993-307e-bdbe-23db453362fd | -3.57497 | -43.61898 | 2025-10-28 04:42:00 | NPP-375D | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 480aaba6-1ab1-3bea-b7fe-e51b5b6256e2 | -7.35664 | -46.98716 | 2025-10-28 04:42:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0dd4bf1f-3747-378a-84f9-e95804267999 | -3.32255 | -50.77144 | 2025-10-28 04:42:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3d168815-a7d2-36c3-b528-23d2dae7037c | -8.19774 | -46.9333 | 2025-10-28 04:42:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ba7bcc20-971c-3575-b89a-6d0f97145c84 | -7.27747 | -45.00665 | 2025-10-28 04:42:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f00ad2b0-fd58-3276-869c-4603a5fc244f | -4.90961 | -42.90523 | 2025-10-28 04:42:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 95559df5-d404-3768-b118-7f1b7ec677c7 | -2.91084 | -49.81224 | 2025-10-28 04:42:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0ec469ee-87e9-37a2-8986-ace278704f77 | -5.61651 | -51.78544 | 2025-10-28 04:42:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a153dd94-c9b5-3ace-8799-dd79fa421195 | -6.89262 | -51.72749 | 2025-10-28 04:42:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| afdd5724-561e-33ea-a26f-a6f01fb88c25 | -4.89734 | -47.6624 | 2025-10-28 04:42:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6b43f10d-8303-3b05-828e-163b65c75f75 | -5.66777 | -47.82421 | 2025-10-28 04:42:00 | NPP-375D | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 085be472-b76c-38f0-ab98-d78126685a60 | -8.16213 | -46.99888 | 2025-10-28 04:42:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b9cd429c-0724-38cb-b66f-b906c82de5b3 | -5.587 | -45.34277 | 2025-10-28 04:42:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0f48cabb-ef5c-327f-8882-e8dcf556b710 | -4.46276 | -43.23369 | 2025-10-28 04:42:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 17.6 |
| 5ac10fe0-95e3-3ebc-a08d-93919b679c46 | -7.82024 | -46.42714 | 2025-10-28 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 321665b7-b8e6-35e2-9c7b-cb84a2bfe048 | -6.16434 | -41.67499 | 2025-10-28 04:42:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 49c75592-0b54-387f-9873-47d9f1bc5573 | -3.49747 | -50.04594 | 2025-10-28 04:42:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cd47add8-79f1-37c8-8d02-540770498f24 | -6.4837 | -42.22637 | 2025-10-28 04:42:00 | NPP-375D | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 52983b18-b536-36c7-922d-c2db0ba7110d | -7.60219 | -43.58735 | 2025-10-28 04:42:00 | NPP-375D | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |


[Clique aqui para ver as próximas entradas](README48.md)
