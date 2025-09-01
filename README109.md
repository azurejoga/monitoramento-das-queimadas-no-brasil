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

## Dados Diários - Página 109

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ab807164-f330-318a-9113-13a3d298e904 | -8.9857 | -48.2096 | 2025-09-01 13:50:00 | GOES-19 | TUPIRAMA | TOCANTINS | Brasil | 1721257 | 17 | 33 | nan | nan | nan | Cerrado | 91.5 |
| a8c23bfb-b03c-3929-9e1c-ee00912ea38d | -6.9317 | -45.5578 | 2025-09-01 13:50:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 84.4 |
| b265da71-f6f8-381d-8c1a-5e2e53698721 | -13.4977 | -46.997 | 2025-09-01 13:50:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 64.0 |
| 8bf99ad9-508a-39be-9f53-747c74c7d62d | -11.9631 | -45.797 | 2025-09-01 13:50:00 | GOES-19 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 61.5 |
| 1f1d8e3d-00fb-3775-9a72-3e38c9e753e2 | -9.2453 | -47.0602 | 2025-09-01 13:50:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 194.8 |
| a79b6fb1-39d8-356f-9bce-1c4035740c0a | -11.7993 | -46.4114 | 2025-09-01 13:50:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 117.1 |
| df9fdff5-3f2f-3764-8787-c80f918f5050 | -8.6673 | -62.8369 | 2025-09-01 13:50:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 55.2 |
| cb61bf86-52e0-396a-9cd7-92fe9af08d9e | -11.3701 | -43.6104 | 2025-09-01 13:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 128.2 |
| 72ca8e2c-274b-34b8-b221-187503a72a6d | -12.9575 | -48.1076 | 2025-09-01 13:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 67.3 |
| 75f80846-4093-3d11-9554-d237f1ec9e86 | -7.9351 | -46.4559 | 2025-09-01 13:50:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 77.1 |
| 6e5b0c55-5540-304e-a10d-b7380173544a | -7.0572 | -44.3393 | 2025-09-01 13:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 137.7 |
| 9fd7053d-5efa-3de1-b116-cd8d4bf8fa1b | -11.0849 | -44.611 | 2025-09-01 13:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 102.3 |
| 7127a914-eb19-385d-ba73-e4d07a37d06c | -9.2264 | -47.0622 | 2025-09-01 13:50:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 158.6 |
| 65c738b6-720c-3a0d-9204-be1eaeb24ba9 | -8.8437 | -47.5217 | 2025-09-01 13:50:00 | GOES-19 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 204.5 |
| 335c2c1b-c749-337e-a683-adf8642f9837 | -13.3439 | -46.9757 | 2025-09-01 13:50:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 61.4 |
| 03a33295-f0f7-35ea-8acb-f51d8ee0efff | -6.7626 | -43.7881 | 2025-09-01 13:50:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 139.0 |
| 31b4809e-2762-3889-b5fe-40b56d1b1b65 | -7.076 | -44.3376 | 2025-09-01 13:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 216.5 |
| d713f564-e8c8-330b-a5a6-4ea258efd29c | -11.0841 | -44.6575 | 2025-09-01 13:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 77.5 |
| 0034f862-1f25-3eee-9fc4-8f07b7c3fe59 | -13.5171 | -46.994 | 2025-09-01 13:50:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 61.0 |
| 7c0c0a88-08c4-3579-80fd-546cf2286c6a | -4.3197 | -48.0908 | 2025-09-01 13:50:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 107.9 |
| 2075facb-d58c-317b-8a87-cd6f08265d14 | -12.9764 | -48.1272 | 2025-09-01 13:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 92.6 |
| 3b35dc0f-e91d-3a8a-84df-dfbceb5d0f43 | -7.9539 | -46.4542 | 2025-09-01 13:50:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 132.5 |
| 66fed1f3-bd34-3327-9768-1aa83314597c | -12.996 | -48.1022 | 2025-09-01 13:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 59.5 |
| 4787660f-7958-3d73-b924-ff1538fc6d31 | -7.6783 | -61.0908 | 2025-09-01 13:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 66.7 |
| 0d7b090b-6f25-3eff-adff-5852019c555b | -12.9768 | -48.1049 | 2025-09-01 13:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 114.7 |
| c7fb2f1b-6983-3e01-8fb7-6a43705390c7 | -8.8936 | -45.1168 | 2025-09-01 13:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 109.6 |
| bfaf41eb-b40e-35c1-b775-00faf9379d41 | -7.3992 | -47.4333 | 2025-09-01 13:50:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 100.5 |
| 666b63f2-3bb6-344d-9e9f-7ecc411c067c | -6.8279 | -52.8348 | 2025-09-01 13:50:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 58.3 |
| 2c22dbe6-e7c7-3219-b50c-98a6e0b59cda | -6.1853 | -43.3257 | 2025-09-01 13:50:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 97.3 |
| 88a689f7-abee-3489-ad4a-20720ce8e988 | -13.3245 | -46.9787 | 2025-09-01 13:50:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 74.4 |
| 264691cd-2c92-3e7b-bc72-b8c00e29ad3c | -6.7038 | -42.2665 | 2025-09-01 13:50:00 | GOES-19 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 76.4 |
| 02c41f9c-770e-3629-84d0-3b7eaf18d1e3 | -14.0508 | -44.5543 | 2025-09-01 13:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 147.5 |
| 2611d3d3-e413-3cfa-ac66-c3852aeb32b9 | -7.0946 | -44.3589 | 2025-09-01 13:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 110.5 |
| 3b99ba57-61d4-3e65-bb8f-ff512f4cba33 | -6.9314 | -45.5803 | 2025-09-01 13:50:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 100.9 |
| 336e0f27-01b2-3d0c-a636-bab6cad5babc | -6.824 | -43.3168 | 2025-09-01 13:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 130.9 |
| 1351cab6-c073-3f78-83f7-d8041d0d96cc | -4.9124 | -43.187 | 2025-09-01 13:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 539.3 |
| 2895eb42-df2f-3e06-865e-53fb687418a3 | -11.3709 | -43.5631 | 2025-09-01 13:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 121.6 |
| c63d6e2e-5d4e-315a-8662-bcad93e8f8be | -7.0948 | -44.3358 | 2025-09-01 13:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 98.2 |
| 74462d11-4024-39dc-acf3-dc5029a2f47e | -11.0568 | -45.146 | 2025-09-01 13:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 146.9 |
| 82571fdb-11e9-3ef3-bc0c-751811f4cf10 | -6.7438 | -43.7898 | 2025-09-01 13:50:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 153.1 |
| bfb91911-b2b4-3c3d-a758-0a3a1500a710 | -10.8935 | -45.8084 | 2025-09-01 13:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 132.0 |
| 9f12f4b5-8516-3a82-8df1-68e5d4d7fdeb | -6.9324 | -42.0299 | 2025-09-01 13:50:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 134.6 |
| 072cdd2e-a2f3-34cb-abc1-d65443d67963 | -8.1943 | -46.788 | 2025-09-01 13:50:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 85.3 |
| eac14f44-7275-3620-b780-5b6ada9c06a6 | -8.8625 | -47.5198 | 2025-09-01 13:50:00 | GOES-19 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 100.2 |
| bd4e7be5-ae3b-3df9-a727-41cb5947d90f | -6.8281 | -52.8143 | 2025-09-01 13:50:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 84.3 |
| b043b379-62c8-3d08-b931-4e4b51104091 | -6.333 | -43.5697 | 2025-09-01 13:50:00 | GOES-19 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 75.9 |
| a5c4b11b-9400-3128-b803-4fbe74fd0eae | -7.9536 | -46.4765 | 2025-09-01 13:50:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 483.7 |
| 68188acb-5a3a-3dc1-b732-de22b02b63f8 | -5.8882 | -42.9988 | 2025-09-01 13:50:00 | GOES-19 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 75.6 |
| bff86bb0-2a28-31fd-9354-c13cffe67927 | -7.9348 | -46.4783 | 2025-09-01 13:50:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 282.8 |
| 6d84cc19-4cc3-3d72-a627-ee8fe8adff1a | -11.0377 | -45.1487 | 2025-09-01 13:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 132.3 |
| 9ddef19c-3f46-3b68-bcc8-ef8ff2a6dd7b | -11.8185 | -46.4087 | 2025-09-01 13:50:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 97.7 |
| 4498a867-74ef-335e-97fa-c994a5bf14e6 | -13.3271 | -46.8426 | 2025-09-01 13:50:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 49.1 |
| 3201be59-b614-32ff-a2e3-c7dd5921b3cc | -11.3701 | -43.6104 | 2025-09-01 14:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 156.1 |
| e20ec6fb-1f8b-390c-a2e6-b552f9c61363 | -6.8281 | -52.8143 | 2025-09-01 14:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 101.2 |
| b568cd65-a5b4-34f4-8bea-70a797c47dbc | -8.8248 | -47.5235 | 2025-09-01 14:00:00 | GOES-19 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 66.2 |
| 5842dd8c-48c7-349b-9cbb-6da86e31c6fe | -12.5769 | -44.7814 | 2025-09-01 14:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 71.5 |
| 2d350357-a188-317d-a7c6-ea8ef902e633 | -4.3197 | -48.0908 | 2025-09-01 14:00:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 92.3 |
| dafef26c-abfd-340b-9933-d655d7950a4b | -7.9539 | -46.4542 | 2025-09-01 14:00:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 119.9 |
| 78c1df4d-bdaf-32c6-8e8c-4ba52aac04b4 | -8.8625 | -47.5198 | 2025-09-01 14:00:00 | GOES-19 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 131.2 |
| 6736fda7-e47c-3816-8c7f-26186850c284 | -7.1089 | -44.7703 | 2025-09-01 14:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 99.6 |
| 10d11588-f54e-3cc7-b72a-4024e396001e | -13.4977 | -46.997 | 2025-09-01 14:00:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 59.7 |
| dd5a0ece-4157-3120-a04a-33f919b0d847 | -12.996 | -48.1022 | 2025-09-01 14:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 57.3 |
| 5260a6cb-14b0-3e30-a087-4a706794a0e1 | -6.9516 | -42.0042 | 2025-09-01 14:00:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 81.4 |
| 0f241ed5-1817-3420-abab-844951ec001d | -12.392 | -46.4626 | 2025-09-01 14:00:00 | GOES-19 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 51.2 |
| 9e474945-f63b-399c-ae1d-1d70ce1a7a82 | -9.2453 | -47.0602 | 2025-09-01 14:00:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 112.9 |
| ae171d2d-614c-3e73-8500-971fbf84f205 | -6.333 | -43.5697 | 2025-09-01 14:00:00 | GOES-19 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 82.4 |
| a14c054f-81e7-3c5b-b9c7-84f2bc30c483 | -6.9327 | -42.006 | 2025-09-01 14:00:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 128.2 |
| f9e81589-33fc-3f15-a921-44e03f2e787d | -11.0849 | -44.611 | 2025-09-01 14:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 82.7 |
| 0a5850cc-0539-3b24-9005-85a0f46edaa9 | -6.8428 | -43.3151 | 2025-09-01 14:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 114.7 |
| 1ad35693-2575-3093-93e6-8e18a2c67404 | -8.8437 | -47.5217 | 2025-09-01 14:00:00 | GOES-19 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 199.6 |
| 17b7bf20-3404-3d06-9949-a417e75e624c | -11.3696 | -43.6341 | 2025-09-01 14:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 78.5 |
| 17e426e2-20ff-3ab3-9d30-642e27be0a14 | -12.9575 | -48.1076 | 2025-09-01 14:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 67.4 |
| d9064066-405a-3e8d-ac90-260d45b89ea7 | -11.0377 | -45.1487 | 2025-09-01 14:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 107.2 |
| 3069946e-b144-31b1-b291-01653f12df8c | -6.1853 | -43.3257 | 2025-09-01 14:00:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 73.2 |
| 733f3245-5efe-3249-bcbd-77aed5f33c48 | -11.9623 | -45.8428 | 2025-09-01 14:00:00 | GOES-19 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 66.1 |
| f5c894d8-a76e-3f1d-b51c-33570373d706 | -6.8426 | -43.3385 | 2025-09-01 14:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 101.2 |
| 0821fde8-b810-33fd-a67e-b667e75c5fd6 | -14.0508 | -44.5543 | 2025-09-01 14:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 101.9 |
| c3e2407d-bb80-334b-ac97-6d4b1d4f755a | -7.0948 | -44.3358 | 2025-09-01 14:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 97.1 |
| f1f90393-6fdf-3282-85fe-aa9010d6ac4c | -11.0845 | -44.6343 | 2025-09-01 14:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 186.2 |
| 156bbb65-b148-3c49-807c-0341ce8ebab9 | -11.3705 | -43.5868 | 2025-09-01 14:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 329.7 |
| a67ecbd1-48a9-397c-ba88-64c42cc3e6bb | -11.7985 | -46.4567 | 2025-09-01 14:00:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 113.6 |
| e326aa2d-af84-3f1d-98b1-b5f6f6d67e21 | -12.9768 | -48.1049 | 2025-09-01 14:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 119.3 |
| 393a9fca-09dc-3dcb-bf42-fb8f0f7c1565 | -13.3245 | -46.9787 | 2025-09-01 14:00:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 60.6 |
| 85d98b94-c380-36f8-82c5-9c1e450a5a27 | -7.2293 | -44.0697 | 2025-09-01 14:00:00 | GOES-19 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 117.5 |
| c5c1e782-9ff7-3138-b71b-46d1ca5fe069 | -9.1567 | -45.2243 | 2025-09-01 14:00:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 104.8 |
| 04e5cf26-9c3d-3da3-b0d4-f21e5f1b065f | -6.2583 | -43.5294 | 2025-09-01 14:00:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 81.5 |
| 24169f3c-4d4b-3f08-a3e9-c2edb02c482f | -6.1665 | -43.3273 | 2025-09-01 14:00:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 83.3 |
| 77836867-baa9-3bdd-a70a-687a11adb04f | -14.0502 | -44.5779 | 2025-09-01 14:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 132.8 |
| 065339e8-d112-3647-a875-bfaca59c2cd6 | -4.9122 | -43.2103 | 2025-09-01 14:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 373.2 |
| 48679fb0-0c8b-3ae1-864c-d6ce57bee834 | -9.6505 | -47.8128 | 2025-09-01 14:00:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 68.3 |
| e294a44d-3c4b-3f24-abbf-fa351e9d64f4 | -8.6673 | -62.8369 | 2025-09-01 14:00:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 53.5 |
| 329413c4-a707-3bcf-980c-2359a01861ca | -13.2876 | -46.894 | 2025-09-01 14:00:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 112.0 |
| ad35fdb6-9006-3cf7-8d73-13ff115744a9 | -7.0946 | -44.3589 | 2025-09-01 14:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 100.8 |
| acdf223d-daaf-374a-9c27-de2067643428 | -11.3709 | -43.5631 | 2025-09-01 14:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 124.9 |
| 2f31a703-c009-325c-b522-92cb6e43acdf | -8.8622 | -47.5418 | 2025-09-01 14:00:00 | GOES-19 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 88.7 |
| 7b7fa6e5-e45a-3a15-82e4-28db3e1cc7c1 | -11.7989 | -46.4341 | 2025-09-01 14:00:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 152.3 |
| 245f898f-726c-3f05-9c45-e6073c452a97 | -11.815 | -51.4572 | 2025-09-01 14:00:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 121.2 |
| 54e6c3e6-86b7-367d-a322-eec095f39745 | -10.8935 | -45.8084 | 2025-09-01 14:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 145.9 |
| 2d71bda6-4439-3cd3-bcde-325757155582 | -10.0623 | -48.0978 | 2025-09-01 14:00:00 | GOES-19 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 57.9 |
| f711423a-96fb-31f9-9da8-1fd5b0e5806b | -6.8466 | -52.8132 | 2025-09-01 14:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 84.5 |


[Clique aqui para ver as próximas entradas](README110.md)
