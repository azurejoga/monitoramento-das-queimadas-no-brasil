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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 592eacca-5b02-3362-9e51-a1eb67b43f30 | -10.04223 | -47.10427 | 2025-10-24 04:17:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 34fadd9c-331c-37fd-b846-34fe67178ad2 | -8.44549 | -48.7489 | 2025-10-24 04:17:00 | NPP-375D | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e07e6cb0-bd34-3f08-95f0-91bdb6a397f8 | -10.63347 | -48.079 | 2025-10-24 04:17:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 91bea2a7-bfcd-37be-8636-457deead9eed | -6.84134 | -41.55419 | 2025-10-24 04:17:00 | NPP-375D | SÃO JOSÉ DO PIAUÍ | PIAUÍ | Brasil | 2210201 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| c12802fb-205b-3c5c-949c-053979923074 | -4.84583 | -47.80067 | 2025-10-24 04:17:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 218dd49d-99a5-3bc2-85ec-3ad7e5113dae | -5.41092 | -46.40999 | 2025-10-24 04:17:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d43b4371-c2d1-358c-9dfc-fee8f29fba27 | -4.87472 | -47.54352 | 2025-10-24 04:17:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 608449bb-6d55-327b-8f4b-6ca856dd6729 | -2.80906 | -51.3508 | 2025-10-24 04:17:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 82ca021b-c7c1-397a-b0ac-cfc10ddb6492 | -11.36329 | -45.92224 | 2025-10-24 04:17:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 49ca1439-ba9b-30bc-b78f-bdef94d348ec | -9.63507 | -46.9001 | 2025-10-24 04:17:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 45bef111-6be0-3589-802a-26e338d0af84 | -12.61951 | -44.25294 | 2025-10-24 04:17:00 | NPP-375D | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 529f6c00-4cfc-3366-a3c8-1e6641db40e8 | -2.871 | -50.72343 | 2025-10-24 04:17:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 15d40764-6c7d-3687-8762-2aedc75a89be | -10.87708 | -45.08316 | 2025-10-24 04:17:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 71912aab-f417-33fc-9b51-f3ed06923751 | -3.81551 | -42.4674 | 2025-10-24 04:17:00 | NPP-375D | SÃO JOÃO DO ARRAIAL | PIAUÍ | Brasil | 2209971 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 89898dd8-23b8-39e1-b980-376aa8f3c85a | -11.99658 | -45.42457 | 2025-10-24 04:17:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 48d9882b-f5cc-359a-b3af-bae1bce309ad | -12.06833 | -46.44004 | 2025-10-24 04:17:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 11.3 |
| c76e5759-e830-3f15-803e-01fdff1acf31 | -4.15159 | -47.67509 | 2025-10-24 04:17:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 080c7923-f788-35eb-b272-5369469cf753 | -3.37534 | -42.46897 | 2025-10-24 04:17:00 | NPP-375D | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 29c10d3d-80eb-37c2-a0ef-645ea5933394 | -10.58863 | -49.64472 | 2025-10-24 04:17:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 56698b28-6450-3141-a963-b17f30f8d471 | -3.24345 | -48.76756 | 2025-10-24 04:17:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 257cc13f-fc5a-3431-baf7-750cbbd02977 | -10.94957 | -50.3738 | 2025-10-24 04:17:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b52a1934-8a7e-399a-aadf-0d07351bc321 | -11.05659 | -45.39965 | 2025-10-24 04:17:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 3c0cf914-e009-3b31-ae7b-35fc38834520 | -9.0954 | -46.53238 | 2025-10-24 04:17:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8d58e4d7-0919-3549-8641-6da709ffb5f6 | -1.53825 | -55.40601 | 2025-10-24 04:17:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fdb79e50-5c71-3d66-8f20-762f70b9f9ec | -4.64036 | -40.19026 | 2025-10-24 04:17:00 | NPP-375D | CATUNDA | CEARÁ | Brasil | 2303659 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 95d7fa88-fe98-3ebc-9739-6b3e5bfeb5da | -6.09015 | -46.23271 | 2025-10-24 04:17:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 83152d1f-af0a-318f-a4a3-d7771f000994 | -2.73301 | -49.56067 | 2025-10-24 04:17:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 673f24ac-0993-3291-bf99-189033ddde73 | -6.1471 | -44.58385 | 2025-10-24 04:17:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fbd3192a-01cc-38de-98c8-7c1e40fd374b | -0.83156 | -47.96243 | 2025-10-24 04:17:00 | NPP-375D | SÃO JOÃO DA PONTA | PARÁ | Brasil | 1507466 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b26b5aa6-8694-3ecd-b410-8529e5769fd9 | -5.45335 | -45.40944 | 2025-10-24 04:17:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 13.3 |
| da536753-6cf9-3946-97c7-3140a2a39d56 | -4.46496 | -43.23685 | 2025-10-24 04:17:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 26.8 |
| 668459b0-d10c-37e2-9248-a53cfe838c27 | -6.31022 | -41.85198 | 2025-10-24 04:17:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 593ffb2f-ce74-3e22-b8e7-d27ec8a5194e | 0.40636 | -50.95424 | 2025-10-24 04:17:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 34ce0099-4b85-3eef-a55c-0dc1744459ee | -12.06054 | -46.42297 | 2025-10-24 04:17:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ad42e367-8fa9-3f8b-ac8b-cdbf97714fee | -4.24422 | -48.55326 | 2025-10-24 04:17:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5bb3016f-9442-329f-b41b-3e28c3d7f8cb | -5.96852 | -44.12564 | 2025-10-24 04:17:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 460234d3-aa37-3eee-94a5-32e6c54be587 | -6.07174 | -42.14665 | 2025-10-24 04:17:00 | NPP-375D | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 32123ca8-8a7b-3945-8f13-61133e94c45a | -4.85928 | -46.73183 | 2025-10-24 04:17:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ea01dd62-3ec2-318a-9d84-08f005c97b9c | -4.28438 | -48.25683 | 2025-10-24 04:17:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ed65809d-1038-3361-92ff-e49623ae6d23 | 1.35649 | -50.70182 | 2025-10-24 04:17:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 182db76d-4a76-3efd-af8c-77875392c07d | -4.31039 | -48.22958 | 2025-10-24 04:17:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 314fe288-6daf-3eff-868a-820239c48b21 | -2.47488 | -49.22902 | 2025-10-24 04:17:00 | NPP-375D | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 60b16c58-b3b8-3797-876e-b6607783ebfd | -11.51293 | -47.22066 | 2025-10-24 04:17:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fc344f12-595b-3638-9dcf-0f53c56c49c5 | -11.60612 | -47.73281 | 2025-10-24 04:17:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9bd5d018-5c67-3baf-9aa6-c64b910f271d | -6.1858 | -41.53009 | 2025-10-24 04:17:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 0.2 |
| 7c86ed28-2b7a-336f-85da-3a2b64992f72 | -9.51367 | -46.79985 | 2025-10-24 04:17:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4cf991c9-ee7c-3bb7-b138-cb55183dc058 | -3.23601 | -48.75755 | 2025-10-24 04:17:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 647bda0f-01bf-38e6-bb10-79fed202dd08 | -9.20004 | -44.54497 | 2025-10-24 04:17:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 06eb951c-6f8b-3573-904d-dab1c7c5b401 | -4.10003 | -43.21123 | 2025-10-24 04:17:00 | NPP-375D | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fdd47f3e-4d68-3b69-9a7b-ee23288eb0b4 | -2.86742 | -50.71369 | 2025-10-24 04:17:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 823b75e4-17a9-320b-8cb6-ce286b91b425 | -9.23504 | -45.62209 | 2025-10-24 04:17:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b00dafa9-cbe4-3002-a6cd-57d741c40c47 | -4.05682 | -46.74502 | 2025-10-24 04:17:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a87edb1a-f8ca-3f1b-94b7-67b39a9cd9a0 | -3.47241 | -43.24457 | 2025-10-24 04:17:00 | NPP-375D | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9196a24d-f222-374e-9c25-c7290d31495c | -9.30961 | -45.20791 | 2025-10-24 04:17:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 45d0760e-5600-36f3-be19-12dbcb3fbf96 | -4.41118 | -42.14195 | 2025-10-24 04:17:00 | NPP-375D | BOA HORA | PIAUÍ | Brasil | 2201770 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 9eaae6ed-0ba0-3606-b991-8d1ca28a6a9d | -5.44401 | -40.8899 | 2025-10-24 04:17:00 | NPP-375D | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| fd03d60c-00f2-3276-b956-a12a0b604170 | -2.85471 | -50.74102 | 2025-10-24 04:17:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 211103e8-40d7-38e0-94d2-a2806f9db222 | -5.9646 | -44.12866 | 2025-10-24 04:17:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c4e5e31d-ca90-3a52-aa9a-eeabc0db4af5 | -11.35997 | -45.96374 | 2025-10-24 04:17:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 791717c8-ab40-3d93-9f3e-06e1e0997d7c | -3.02367 | -49.48265 | 2025-10-24 04:17:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6f696f40-ba08-319f-8645-dfdc1b131bdb | -12.02096 | -46.9227 | 2025-10-24 04:17:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 26a402be-2797-3c08-9121-6b5a7a206107 | -6.32266 | -39.7183 | 2025-10-24 04:17:00 | NPP-375D | SABOEIRO | CEARÁ | Brasil | 2311900 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 49f2428b-b13c-32e3-af66-6a86634462d4 | -5.56537 | -43.61437 | 2025-10-24 04:17:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 908b2455-b378-3cfe-bc2a-6c71c22d554e | -9.86943 | -47.72817 | 2025-10-24 04:17:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0ea64f95-98a8-3bf3-80ea-64ab66e91d67 | -11.05322 | -45.39908 | 2025-10-24 04:17:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f47c28b6-0164-3be6-a3f1-9684b4f88d89 | -5.62607 | -42.58897 | 2025-10-24 04:17:00 | NPP-375D | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 19905321-a966-38b3-b63e-abfe95921d68 | -4.45775 | -43.23927 | 2025-10-24 04:17:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 7e296cbb-c679-3177-a226-66baf35711ea | -6.1297 | -41.73314 | 2025-10-24 04:17:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 643620d7-7d93-3630-b932-cddc5e347c4d | -9.86558 | -44.89622 | 2025-10-24 04:17:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7059530d-45c1-3262-a7a5-554ccd11a943 | -12.00812 | -46.78292 | 2025-10-24 04:17:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 12b34526-77b7-36da-ac99-78ca1859b421 | -10.66453 | -54.31683 | 2025-10-24 04:17:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 09c6b0d6-118a-398d-941c-69a33c3caa3b | -3.47277 | -52.99139 | 2025-10-24 04:17:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4c5c9eb4-e3b5-38bc-822f-a55ef1105185 | -12.06647 | -46.40839 | 2025-10-24 04:17:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 954f06b4-114a-3475-aed4-b15e878a1f5e | -3.83212 | -51.74194 | 2025-10-24 04:17:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5954e4e9-34de-30a3-bf63-bcca540e6c98 | -1.54618 | -55.41499 | 2025-10-24 04:17:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| f2811e48-d547-392d-b908-22bc6f26ced3 | -12.0796 | -46.41449 | 2025-10-24 04:17:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 88dbd6ff-dc4c-34f6-8656-97cad5352a86 | -12.06914 | -46.62955 | 2025-10-24 04:17:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 2a224484-6282-3311-8fcc-ec97388d133a | -5.44985 | -45.40885 | 2025-10-24 04:17:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 13.3 |
| e5da68c0-e589-30de-ae92-97f22eff4ccc | -11.05717 | -45.39605 | 2025-10-24 04:17:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 3371dfb2-5dba-308b-8287-7b3d37a07640 | -3.42034 | -44.81616 | 2025-10-24 04:17:00 | NPP-375D | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e88c4267-6bb0-3308-a3c5-8ab7a0bac508 | -9.30121 | -45.19554 | 2025-10-24 04:17:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4e2412c2-1236-3ccb-ae20-6da5f9ac7afb | -5.6495 | -46.57571 | 2025-10-24 04:17:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9d3d75da-0b9d-3073-ad58-d192edaad1b3 | -10.47029 | -49.0995 | 2025-10-24 04:17:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 067712e5-c3b1-37ca-a3f9-054e7307e840 | -5.58417 | -41.31525 | 2025-10-24 04:17:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| ce6f328b-aa7c-3024-8e75-5d16f4e255d6 | -4.96686 | -48.67167 | 2025-10-24 04:17:00 | NPP-375D | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| af05b779-e7e0-3fe5-935d-4b833470b105 | -4.82279 | -48.67586 | 2025-10-24 04:17:00 | NPP-375D | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 67153c54-5dbd-3b54-8b09-a81c0c800c4d | -3.12304 | -49.10631 | 2025-10-24 04:17:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 7ae72183-72f0-39c4-be9c-681377fa04bd | -5.53655 | -41.35348 | 2025-10-24 04:17:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 08647ddd-c7a6-37b6-89cf-f87620d199d3 | -4.04153 | -51.16151 | 2025-10-24 04:17:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4c2a87a5-095f-3f15-8bd6-74148e49b1d1 | -6.78003 | -38.57164 | 2025-10-24 04:17:00 | NPP-375D | SANTA HELENA | PARAÍBA | Brasil | 2513307 | 25 | 33 | nan | nan | nan | Caatinga | 1.2 |
| cd7032ae-d10f-399a-91f5-707b9bbb0c5d | -4.85138 | -42.9565 | 2025-10-24 04:17:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e1401208-5b70-3582-8141-1eb6a9717492 | -9.60425 | -46.90773 | 2025-10-24 04:17:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 18.7 |
| cf043eb5-76cb-3ddf-a2ac-ab8dffa50f92 | -11.04869 | -45.40573 | 2025-10-24 04:17:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 06fe333c-b4e1-3ef7-8f55-5a9c80cc3789 | -3.14299 | -50.15996 | 2025-10-24 04:17:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3b24c73f-406f-39ad-bf13-bd9ef0f45c03 | -9.62209 | -46.88921 | 2025-10-24 04:17:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 22d5c749-9154-3155-844b-4a10e2241b41 | 1.35701 | -50.70525 | 2025-10-24 04:17:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 0.4 |
| de804dc6-7495-3a35-9432-e56c28a6c2d5 | -9.59927 | -46.91549 | 2025-10-24 04:17:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 3acfe2ab-81c0-3108-8eac-beca4ae8ee6e | -9.64426 | -46.88908 | 2025-10-24 04:17:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0ce451ee-eb71-33c1-8db4-4fe08bc3b2d2 | -8.57768 | -47.01573 | 2025-10-24 04:17:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 40f1997a-a40a-3af9-8738-1c2b95bc71ec | -11.37045 | -45.94255 | 2025-10-24 04:17:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |


[Clique aqui para ver as próximas entradas](README19.md)
