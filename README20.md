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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 646c8b2d-1404-3c3f-b61d-194d227221c0 | -5.44664 | -48.08817 | 2025-11-09 04:18:00 | NPP-375D | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e7310b6f-e1ac-3297-bff5-831b5677965f | -6.70332 | -39.68172 | 2025-11-09 04:18:00 | NPP-375D | TARRAFAS | CEARÁ | Brasil | 2313252 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| a820f6f4-9b6b-3fab-9bb0-d9ea707f43b3 | -6.01693 | -43.77228 | 2025-11-09 04:18:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 97a18443-b6ab-39c8-b962-b992c20c05d6 | -10.33922 | -49.63837 | 2025-11-09 04:18:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| a3509fa3-1f21-3ac0-bcdd-fd3558458a79 | -6.52036 | -43.60913 | 2025-11-09 04:18:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c61e3f98-2f95-3171-9eee-45f6a955af49 | -8.84014 | -40.0736 | 2025-11-09 04:18:00 | NPP-375D | SANTA MARIA DA BOA VISTA | PERNAMBUCO | Brasil | 2612604 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 8e53d6ec-f459-3df1-80dc-c28bc11287b6 | -5.43642 | -47.56831 | 2025-11-09 04:18:00 | NPP-375D | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 18578a1b-ce4c-3f23-9bca-3c8b13b7af69 | -8.01779 | -38.55297 | 2025-11-09 04:18:00 | NPP-375D | SERRA TALHADA | PERNAMBUCO | Brasil | 2613909 | 26 | 33 | nan | nan | nan | Caatinga | 1.3 |
| f5a02e54-6fe7-3e04-bfdf-8f8105599208 | -6.87579 | -47.2416 | 2025-11-09 04:18:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 390fde28-a2ec-3d18-b7fd-651854380361 | -6.17676 | -44.38622 | 2025-11-09 04:18:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1b0ab55c-dbe1-3e3a-8719-2821c35e2e3c | -6.99212 | -42.78347 | 2025-11-09 04:18:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 2f276423-3d5a-364f-ad38-bc31e035cada | -5.78013 | -49.83617 | 2025-11-09 04:18:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 06dbd517-4698-3119-964c-34d780dcabfc | -5.73062 | -46.4684 | 2025-11-09 04:18:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 51c8deff-77bb-37c2-b21f-c6b90cf91da4 | -10.96932 | -47.94341 | 2025-11-09 04:18:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9bd673de-0a33-300e-8a34-d3c29654c451 | -5.40144 | -47.26493 | 2025-11-09 04:18:00 | NPP-375D | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 96e773ed-af23-3e1c-8a30-17083140cc13 | -5.84566 | -46.45027 | 2025-11-09 04:18:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 29c3f029-8b75-366f-9d4f-2b3ba6469785 | -7.55385 | -45.85838 | 2025-11-09 04:18:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 097b8019-27e9-3078-9480-4c532bb369e0 | -5.57309 | -47.12526 | 2025-11-09 04:18:00 | NPP-375D | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e7582541-4aa2-350b-940c-87d4de301fed | -9.47585 | -48.74164 | 2025-11-09 04:18:00 | NPP-375D | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| bf242334-7be9-30db-a02c-ae593a3e07b3 | -5.9457 | -46.6511 | 2025-11-09 04:18:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b1f3bc16-36a9-32ea-9a49-089052f8cac4 | -6.34495 | -46.76387 | 2025-11-09 04:18:00 | NPP-375D | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b5950bce-54a4-35ef-a505-d6eb65f3e258 | -6.71948 | -39.99883 | 2025-11-09 04:18:00 | NPP-375D | ANTONINA DO NORTE | CEARÁ | Brasil | 2300804 | 23 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 4d12c73e-66b1-33b5-8c6c-52be641f9ede | -7.17482 | -41.73911 | 2025-11-09 04:18:00 | NPP-375D | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 960c4d1a-505f-389e-872f-4f800512aa51 | -11.92086 | -44.18216 | 2025-11-09 04:18:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 13ef48a5-4cb7-3a99-b726-dfd2d1b99f72 | -6.08278 | -42.69371 | 2025-11-09 04:18:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| c5752f82-0e2d-34db-8ffa-0ebf8d81c1a5 | -10.97304 | -47.9441 | 2025-11-09 04:18:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b6ed2e5f-2eeb-36ea-ab11-5fa8700094f8 | -7.17538 | -41.73547 | 2025-11-09 04:18:00 | NPP-375D | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 92f573ef-9e2a-3310-8c9d-f313e607dd22 | -6.06422 | -44.19564 | 2025-11-09 04:18:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1c28f89a-b35e-344d-afb6-0e69c1d1c6ce | -6.43768 | -44.20362 | 2025-11-09 04:18:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1d7f18ca-e1e4-33d1-9e68-36e2dc192f35 | -6.01749 | -43.76878 | 2025-11-09 04:18:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 78caab04-2a27-3ecf-a754-240a4d2b112d | -5.43724 | -47.56327 | 2025-11-09 04:18:00 | NPP-375D | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f842c651-ba40-336f-a232-69510548937a | -7.54333 | -45.85666 | 2025-11-09 04:18:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7e15dfc1-3451-3d37-811e-3a020c7fda17 | -8.42212 | -36.25216 | 2025-11-09 04:18:00 | NPP-375D | TACAIMBÓ | PERNAMBUCO | Brasil | 2614709 | 26 | 33 | nan | nan | nan | Caatinga | 3.3 |
| e3bb5e48-7d94-370c-af16-0b523e780488 | -5.65571 | -45.98875 | 2025-11-09 04:18:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1133e2cd-eac5-3684-a0a3-cd90fedd2c9c | -7.40542 | -40.06861 | 2025-11-09 04:18:00 | NPP-375D | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 0e712217-cc84-3e6b-a2df-d497c654f69f | -6.87503 | -47.24622 | 2025-11-09 04:18:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 9a345377-8b23-3ee0-8de6-df069517e3c6 | -10.34406 | -49.63533 | 2025-11-09 04:18:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 18.0 |
| 994a9a4c-baa0-356a-8b4e-31c06e5d0a38 | -6.26646 | -42.23608 | 2025-11-09 04:18:00 | NPP-375D | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 00069c19-4d5b-340b-a3a6-a06511d68ce8 | -8.01454 | -46.99247 | 2025-11-09 04:18:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fa3f7f02-8546-3f32-ab5b-833a9a1e1959 | -10.33154 | -49.63305 | 2025-11-09 04:18:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 18.7 |
| 2ba0df63-e4b8-3c71-b097-7b6b1f4d4e3e | -6.03119 | -46.57066 | 2025-11-09 04:18:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 372c55d5-d4c6-3f07-a30a-dbb955be821e | -6.14943 | -43.29715 | 2025-11-09 04:18:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 935a8bcb-c347-3623-a784-c5bf4c8fe6fa | -6.32132 | -46.20844 | 2025-11-09 04:18:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 36a59556-7c5d-395b-8db0-be2f512fc761 | -19.761 | -58.1269 | 2025-11-09 04:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 92.1 |
| 5fe8b252-8a92-368b-bd26-5174dc32fc73 | -3.3369 | -44.3806 | 2025-11-09 04:20:00 | GOES-19 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 49.9 |
| e516949f-6a85-3c6b-aa8c-8aafbdaefffa | -11.62694 | -49.41953 | 2025-11-09 04:21:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 425c83a8-cf62-3fe0-a564-ab8c4832df9a | -11.61663 | -48.49991 | 2025-11-09 04:21:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e5591c6b-1204-392a-b718-d135b83d7e19 | -11.63097 | -49.42028 | 2025-11-09 04:21:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7654f2a1-2bb1-3448-b907-19136434263d | -12.73903 | -43.46477 | 2025-11-09 04:21:00 | NPP-375D | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 980386a0-7ad4-318e-909f-c6be8b0adbe9 | -13.20711 | -44.56456 | 2025-11-09 04:21:00 | NPP-375D | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 68796f64-d990-373d-adbb-20c99d6a4c7b | -12.94345 | -43.43005 | 2025-11-09 04:21:00 | NPP-375D | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 347baa97-1ecb-3d59-b20a-7e6f6e00821b | -15.73009 | -43.48505 | 2025-11-09 04:21:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 02b4ff12-6d71-379f-bbc5-a5b4d30dd5c7 | -11.94802 | -46.25462 | 2025-11-09 04:21:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3799506b-cd25-33f3-82f3-fe906eae9c0f | -11.94863 | -46.25086 | 2025-11-09 04:21:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 54c0e3cf-73c8-3004-a9a4-77901279d47f | -11.63085 | -49.42096 | 2025-11-09 04:21:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d7a1d0d7-4cfa-3e32-846a-80e0406b992f | -14.4155 | -43.18766 | 2025-11-09 04:21:00 | NPP-375D | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 607fca85-c0f5-32fb-a052-33cbf579f770 | -11.5511 | -48.55028 | 2025-11-09 04:21:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d21706ab-7745-3023-baa8-ec65f1e54bc3 | -11.46105 | -48.65877 | 2025-11-09 04:21:00 | NPP-375D | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f0b619bf-1965-3d85-9cbb-6f75c3fb81c0 | -15.78804 | -41.46479 | 2025-11-09 04:21:00 | NPP-375D | ÁGUAS VERMELHAS | MINAS GERAIS | Brasil | 3101003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 0ddb44e2-03f5-3cb5-aa6c-ae8a911a181b | -13.46301 | -44.03331 | 2025-11-09 04:21:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3a3b58b6-f266-3c6f-8c4f-cc330ac3b1ae | -11.62044 | -48.50059 | 2025-11-09 04:21:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| aa9d199f-5c46-3ade-8dfc-a9051f2ff875 | -12.36966 | -43.6646 | 2025-11-09 04:21:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f16cff95-2876-3f60-8baa-de02bb7e9a03 | -11.62683 | -49.4202 | 2025-11-09 04:21:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1b571678-a5e0-3008-ab4c-9766c9e6adf0 | -12.13728 | -47.6688 | 2025-11-09 04:21:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 98953cfd-2c07-33b6-9006-04f0fad07903 | -11.61961 | -48.50538 | 2025-11-09 04:21:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3aef8f01-0b70-3881-8369-495ba0358bac | -15.72951 | -43.48884 | 2025-11-09 04:21:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1eb64f4d-c85f-3141-bc7f-0cfa24a3717d | -15.72667 | -43.4845 | 2025-11-09 04:21:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 76d3daf4-1b00-3f79-8b63-1040672a7497 | -15.72609 | -43.48831 | 2025-11-09 04:21:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 827d51ad-e829-3425-8eb1-0bcd7c980576 | -15.73066 | -43.48124 | 2025-11-09 04:21:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 988be4ad-c5e8-3d95-ab1b-203ded409f9d | -13.21043 | -44.5651 | 2025-11-09 04:21:00 | NPP-375D | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| aadeb363-64b8-396c-b7ec-5d4e572dd2d3 | -19.7646 | -58.1119 | 2025-11-09 04:23:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| bd7488fb-a422-3a98-b9fb-98a1c3b92f41 | -19.76288 | -58.09126 | 2025-11-09 04:23:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 5a9e3c71-4ca5-3a48-a571-ea0e7818b47f | -19.7145 | -58.10886 | 2025-11-09 04:23:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.3 |
| 7784454e-14e3-38e7-ab5a-1c6313e1e166 | -19.77059 | -58.11348 | 2025-11-09 04:23:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| c1ad9482-7e5a-32cb-b473-61a9f7e29ae0 | -19.76246 | -58.12146 | 2025-11-09 04:23:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| ef7c0920-70bb-3291-933f-416cbca438be | -19.75754 | -58.1151 | 2025-11-09 04:23:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 5e804a51-8c51-3bae-b248-8a4c05d22d6d | -20.65168 | -51.98727 | 2025-11-09 04:23:00 | NPP-375D | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 049b8ece-6ea4-3a9b-8b38-de168c017394 | -19.58536 | -51.08138 | 2025-11-09 04:23:00 | NPP-375D | PARANAÍBA | MATO GROSSO DO SUL | Brasil | 5006309 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e45e2f28-d0ac-3af1-bef7-9f772dbc04a6 | -19.75262 | -58.10876 | 2025-11-09 04:23:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 80a88209-f5c0-3ae5-9cef-cba9f1f19a87 | -19.7494 | -58.12307 | 2025-11-09 04:23:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 2af13515-f763-33ac-8653-b358c4a3254e | -19.72865 | -58.10245 | 2025-11-09 04:23:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| a8c048aa-6900-3cdd-ba3d-78da6ca5d55c | -19.73572 | -58.09925 | 2025-11-09 04:23:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| f69d370e-5745-3ee9-80ab-702d6d1a9355 | -19.58927 | -51.08224 | 2025-11-09 04:23:00 | NPP-375D | PARANAÍBA | MATO GROSSO DO SUL | Brasil | 5006309 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 76755a37-d2dd-3a29-892b-511b350441b6 | -19.74064 | -58.10559 | 2025-11-09 04:23:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 5176a4b4-93c0-3c84-a6aa-f915355179ac | -19.75009 | -58.0952 | 2025-11-09 04:23:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 11570672-7c06-3c18-aba1-52f9f58fb5a0 | -19.74984 | -58.09288 | 2025-11-09 04:23:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 5446b3e4-7b60-3bb2-b5a2-6e6855752246 | -19.76256 | -58.12368 | 2025-11-09 04:23:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.3 |
| b1a0a2be-fade-3283-8dd8-c3af70a057d0 | -19.76353 | -58.11668 | 2025-11-09 04:23:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 3f46342f-f29c-3942-a23d-d5b74a3f5534 | -19.75047 | -58.11831 | 2025-11-09 04:23:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| a6e3d460-b6f4-352d-b64e-943be90bcc22 | -19.75369 | -58.10398 | 2025-11-09 04:23:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| dd6ec308-eabb-3b08-959e-87333ed0fbf9 | -19.74079 | -58.10792 | 2025-11-09 04:23:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| ae7ba642-dadc-3fe6-af77-149f5b8998b5 | -19.7359 | -58.1016 | 2025-11-09 04:23:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.6 |
| 6a24f3d6-5905-34c4-8d11-fbb765cd3848 | -19.7434 | -58.1215 | 2025-11-09 04:23:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| e9015845-3c8e-3462-97b4-927074bb5bb6 | -19.75432 | -58.12945 | 2025-11-09 04:23:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 56adff53-5d09-3042-a047-fb6bd3985f69 | -19.75968 | -58.10556 | 2025-11-09 04:23:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 1dcfdde8-754b-394e-8545-c9868fcd0508 | -19.75647 | -58.11988 | 2025-11-09 04:23:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 117f7f96-9158-30b9-bc0a-4cec436f916a | -19.76139 | -58.12624 | 2025-11-09 04:23:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 66aba36b-447a-39f5-9409-d93e330072a2 | -18.51182 | -55.52162 | 2025-11-09 04:23:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| eb088438-a393-31cb-a836-577e5f8aa257 | -19.75539 | -58.12466 | 2025-11-09 04:23:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 34fe3552-854e-3caa-9584-3b9a8ea8a5c9 | -19.73368 | -58.11114 | 2025-11-09 04:23:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |


[Clique aqui para ver as próximas entradas](README21.md)
