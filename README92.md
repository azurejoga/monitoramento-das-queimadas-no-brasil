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

## Dados Diários - Página 92

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 34ccec42-f68e-3efd-9e61-b9254e111783 | -6.2956 | -43.5496 | 2025-08-31 14:10:00 | GOES-19 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 82.8 |
| 75dc9da1-07c9-3a21-8341-9dca67956453 | -12.1969 | -50.1102 | 2025-08-31 14:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 80.7 |
| 2f80fb87-6831-3666-9cb1-467ee3f7256a | -7.3985 | -44.0768 | 2025-08-31 14:10:00 | GOES-19 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 101.1 |
| 88fb5541-4e62-30d8-b2bd-22bdbe24ba66 | -6.1855 | -43.3023 | 2025-08-31 14:10:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 89.6 |
| 1d729efe-a23d-3bc5-a0d0-75aeae3566eb | -15.7098 | -48.9702 | 2025-08-31 14:10:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 119.0 |
| a516104e-1239-32b8-a194-92c7e8c7d12c | -6.2411 | -43.3677 | 2025-08-31 14:10:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 124.4 |
| f7cff13f-0084-3173-8d4c-6cb1d4fdbc71 | -13.3443 | -46.953 | 2025-08-31 14:10:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 80.0 |
| 11b7cad0-4441-3b3f-8d3c-fde50b663a54 | -11.0658 | -44.6137 | 2025-08-31 14:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 170.6 |
| 3a746779-b11b-32f5-89f3-97750d4722fa | -14.8013 | -46.7371 | 2025-08-31 14:10:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 132.3 |
| d2c3f06b-61a4-33d0-867b-1224f5bae41c | -11.2462 | -44.1221 | 2025-08-31 14:10:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 92.6 |
| 40828b68-3a97-35e4-a053-a9d30cb34c5c | -16.2221 | -52.6778 | 2025-08-31 14:10:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 84.5 |
| f6309c41-cacf-3307-8ff9-24863c21b2f4 | -7.4174 | -44.0749 | 2025-08-31 14:10:00 | GOES-19 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 89.1 |
| 78411760-2e0e-3b4b-bc2f-36d8a0005c9d | -6.2959 | -43.5263 | 2025-08-31 14:10:00 | GOES-19 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 89.1 |
| 3f3029e5-b610-306c-8e17-f62062302249 | -6.5758 | -43.6885 | 2025-08-31 14:10:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 85.8 |
| 105e9abc-e4cb-33fa-9edf-73695da61ab9 | -9.245 | -47.0824 | 2025-08-31 14:10:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 136.3 |
| 141118d1-dd38-385b-ba45-e2b5ee8532df | -11.3709 | -43.5631 | 2025-08-31 14:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 120.9 |
| ae87111f-dc04-35d4-92c7-8478976c286b | -6.9446 | -44.3264 | 2025-08-31 14:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 97.7 |
| cf9b8b7d-ab26-3ac1-a9e4-e23608197346 | -13.4982 | -46.9743 | 2025-08-31 14:10:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 61.5 |
| 312b0b41-9a9a-30bc-941e-25fb612d3428 | -6.1853 | -43.3257 | 2025-08-31 14:10:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 166.7 |
| a9db2e10-6c56-3cd3-a65c-654e6711e52f | -13.3439 | -46.9757 | 2025-08-31 14:10:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 66.8 |
| a0a25e81-12a8-330f-be30-aedcc460d939 | -14.3343 | -51.8944 | 2025-08-31 14:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 87.5 |
| 6d05b73d-013b-363d-8097-0f72fdff4a79 | -6.2597 | -43.3895 | 2025-08-31 14:10:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 80.2 |
| eb44ccf8-f145-370d-861a-a407909ab1d5 | -15.7107 | -48.9255 | 2025-08-31 14:10:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 75.7 |
| f672b31c-b624-3c5f-8cbb-b3d03f50b5ce | -15.6944 | -52.7525 | 2025-08-31 14:10:00 | GOES-19 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 54.7 |
| 46d8ae5a-8738-38e7-ac89-0b281118cb8f | -6.5209 | -43.5537 | 2025-08-31 14:10:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 108.1 |
| ec3c8e9a-3671-3c2e-a9a4-380fcc057c87 | -14.8208 | -46.7337 | 2025-08-31 14:10:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 129.2 |
| b13a5265-0a2f-372d-8e95-9d0a2cdd14bf | -11.8357 | -46.5194 | 2025-08-31 14:10:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 92.0 |
| f2165fac-f0f3-38e1-a922-0a6816f8100c | -17.1536 | -46.0817 | 2025-08-31 14:10:00 | GOES-19 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 90.4 |
| 63006d3e-01ef-3e47-befc-61ea0bf9b521 | -4.7346 | -44.4457 | 2025-08-31 14:10:00 | GOES-19 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 175.9 |
| 4f20eeef-172f-3951-9857-fabd555b245e | -14.3536 | -51.8918 | 2025-08-31 14:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 60.8 |
| ebfe1e78-aea1-354a-8595-446b800a9b78 | -13.3636 | -46.95 | 2025-08-31 14:10:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 76.8 |
| 84f7ab0c-2425-304a-9f2d-6c6bc06d4a91 | -11.3705 | -43.5868 | 2025-08-31 14:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 227.9 |
| f0d2ab8d-8c66-328b-b696-730cc67fda79 | -7.8541 | -46.9747 | 2025-08-31 14:10:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 128.7 |
| a7520745-c34c-3e56-aa3b-606f6b1849de | -7.6597 | -42.7172 | 2025-08-31 14:10:00 | GOES-19 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 73.6 |
| ca77c25b-24cb-3909-9617-397c6e651a19 | -14.3346 | -51.873 | 2025-08-31 14:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 172.8 |
| fb0ddccd-4a87-320b-b8e2-d02a02f00633 | -6.9634 | -44.3247 | 2025-08-31 14:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 89.3 |
| 28651c72-199d-3dce-b9d3-db9606dd8332 | -6.1855 | -43.3023 | 2025-08-31 14:20:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 95.5 |
| 374b1654-bc2f-3b37-a531-a02e9cb94b87 | -6.2597 | -43.3895 | 2025-08-31 14:20:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 76.4 |
| bc31f46d-4fa4-3d2e-b5fa-2d2e8e7832d0 | -11.0849 | -44.611 | 2025-08-31 14:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 155.8 |
| 18445561-2ea0-3341-bfeb-480a337eeefa | -12.1778 | -50.1126 | 2025-08-31 14:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 79.8 |
| 1d21e14f-ee2e-3faf-93d6-999930204703 | -11.0658 | -44.6137 | 2025-08-31 14:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 137.8 |
| 20527321-fe58-3335-a927-f43e8e6bfd18 | -10.0244 | -48.1019 | 2025-08-31 14:20:00 | GOES-19 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 62.0 |
| bc5eebed-0002-38cb-80c0-1e771e5236c8 | -9.245 | -47.0824 | 2025-08-31 14:20:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 86.5 |
| c07f69b3-d5d2-3f44-aa23-299518674413 | -12.1965 | -50.1318 | 2025-08-31 14:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 68.8 |
| c5599533-7589-3f89-9142-27abe0d0edd8 | -14.8208 | -46.7337 | 2025-08-31 14:20:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 139.3 |
| fdecd3b6-3ea8-3be3-97c1-4be6db55e2a9 | -16.2221 | -52.6778 | 2025-08-31 14:20:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 59.9 |
| 6a8f4cee-596b-3ab8-b761-65368dd7b00d | -14.5642 | -51.9917 | 2025-08-31 14:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 62.5 |
| 29b538ff-fc41-3fc7-8cd7-f653b61425d4 | -14.8013 | -46.7371 | 2025-08-31 14:20:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 185.8 |
| b47adbd9-3b30-3a80-8150-6874ebd3dd7c | -7.1139 | -44.3111 | 2025-08-31 14:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 181.6 |
| 24a0ddfd-7a6a-397b-8d19-bac9c09bd0f8 | -11.3701 | -43.6104 | 2025-08-31 14:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 211.3 |
| 0be4d97e-59ee-3198-b860-6a613852e192 | -11.8181 | -46.4314 | 2025-08-31 14:20:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 93.5 |
| cb831bd0-6be8-352d-8ec6-94ca3d1a6a7f | -11.3526 | -43.5187 | 2025-08-31 14:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 159.3 |
| e17707e9-340c-3801-98f3-cb937cd706df | -5.7694 | -43.6845 | 2025-08-31 14:20:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 102.0 |
| 5019d484-a93c-3dc8-bfb8-afb5609c2f6c | -13.4788 | -46.9774 | 2025-08-31 14:20:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 65.2 |
| 48c9cac3-23bc-3ef8-9d45-34c7d481dbbe | -6.5209 | -43.5537 | 2025-08-31 14:20:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 137.2 |
| 56b70b5a-5b52-34dc-9b7e-42e24e01c4ff | -9.0009 | -50.0843 | 2025-08-31 14:20:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 103.3 |
| 9c9de0a7-5d6f-3d70-840c-8dc9b34c29b4 | -8.8936 | -45.1168 | 2025-08-31 14:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 72.9 |
| a3216fb3-bd8a-3dbf-beda-f6bff147b0ae | -13.4006 | -47.0347 | 2025-08-31 14:20:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 98.4 |
| 3ab64021-335c-37dd-8d75-7c772e310e20 | -9.2639 | -47.0804 | 2025-08-31 14:20:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 149.3 |
| 414d655e-edbe-306e-895d-e6452586a95f | -8.421 | -48.2847 | 2025-08-31 14:20:00 | GOES-19 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 188.7 |
| f635d9bd-2679-3f8f-81c5-81a50abc8569 | -6.5021 | -43.5553 | 2025-08-31 14:20:00 | GOES-19 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 112.5 |
| 4a563d7c-e22d-3d5a-aff8-05e011f874de | -15.7098 | -48.9702 | 2025-08-31 14:20:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 180.0 |
| f7351966-0d98-33ac-bf21-a358964c8550 | -5.8696 | -42.9768 | 2025-08-31 14:20:00 | GOES-19 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 206.1 |
| cc9c7ea5-fd5e-3a33-bcf1-e53a547a1efd | -14.3346 | -51.873 | 2025-08-31 14:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 107.5 |
| 113b597d-75d5-302d-874d-95290d103ef8 | -14.0307 | -44.5814 | 2025-08-31 14:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 158.2 |
| 69bf8d58-0830-325b-a235-e72b62a23bc1 | -11.3705 | -43.5868 | 2025-08-31 14:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 178.5 |
| f2094396-6058-3f62-b249-d21f1ebcc5e0 | -11.3317 | -43.6162 | 2025-08-31 14:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 146.0 |
| 44e78562-d581-3a08-be94-7f2c31c55e7a | -7.4178 | -47.4537 | 2025-08-31 14:20:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 140.3 |
| 1b2c524e-04fd-3677-aefe-3a6f6c513234 | -7.0628 | -43.8305 | 2025-08-31 14:20:00 | GOES-19 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 91.2 |
| 0d5d808e-b2e5-3074-a807-5ff566a8dccd | -15.7107 | -48.9255 | 2025-08-31 14:20:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 78.1 |
| 79020ffe-2702-3b26-b1d9-8cca60f0d611 | -6.1853 | -43.3257 | 2025-08-31 14:20:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 180.4 |
| fbc48677-15d8-325c-a3b7-2f4bfe817258 | -15.7294 | -48.9669 | 2025-08-31 14:20:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 47.6 |
| f1d7f78f-6e17-3f78-834f-c3bd934467a5 | -5.8884 | -42.9753 | 2025-08-31 14:20:00 | GOES-19 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 99.9 |
| 6c054887-a3f5-35f5-bca6-47f8b9838edd | -17.1536 | -46.0817 | 2025-08-31 14:20:00 | GOES-19 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 74.6 |
| c0d1d686-a461-30f3-9147-dfbcf14abdb6 | -15.7093 | -48.9925 | 2025-08-31 14:20:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 73.8 |
| 0fd2df53-939f-3637-aeaa-8ca16b9b4239 | -8.875 | -45.0961 | 2025-08-31 14:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 200.5 |
| e7916211-c7cb-3226-83b3-273c74f5b219 | -11.8357 | -46.5194 | 2025-08-31 14:20:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 84.1 |
| ee35b142-3125-3033-9712-1a84812efe7d | -6.2956 | -43.5496 | 2025-08-31 14:20:00 | GOES-19 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 81.0 |
| 8485a628-cde1-3bee-af42-8243ef574991 | -12.1969 | -50.1102 | 2025-08-31 14:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 119.1 |
| 214b8827-4cf5-3a69-8e50-dd2dd864e9bf | -6.5211 | -43.5304 | 2025-08-31 14:20:00 | GOES-19 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 82.3 |
| d22f6f4c-d04c-3f9f-a9ac-b684ba8991d7 | -6.5758 | -43.6885 | 2025-08-31 14:20:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 89.1 |
| a64a0870-487d-3c82-9c8e-408f16d76b93 | -9.2636 | -47.1027 | 2025-08-31 14:20:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 93.3 |
| d73701c4-932f-3d4b-a1fd-df08a1bdd054 | -6.2411 | -43.3677 | 2025-08-31 14:20:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 117.9 |
| be8001f7-c1dd-32aa-9a09-fdebddd725e1 | -14.3343 | -51.8944 | 2025-08-31 14:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 89.2 |
| c45504c6-dd16-3545-98ee-6cba4bba8440 | -7.3985 | -44.0768 | 2025-08-31 14:20:00 | GOES-19 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 148.2 |
| c6bd4ed2-616f-3e7a-92e3-f8fb7339bd6e | -14.0508 | -44.5543 | 2025-08-31 14:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 92.7 |
| f540fe82-4307-3c79-9d86-ba1d0fb6f595 | -13.3443 | -46.953 | 2025-08-31 14:20:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 81.1 |
| cd2a1c93-4128-3706-bf86-51953e5c4cdd | -11.3509 | -43.6133 | 2025-08-31 14:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 188.3 |
| d88e3d9f-b44b-32cd-be52-4d836d4abcd0 | -11.3521 | -43.5423 | 2025-08-31 14:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 146.2 |
| 6adb0357-6770-3838-a9d2-7bf64378cb6f | -6.0553 | -45.1754 | 2025-08-31 14:20:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 114.2 |
| 4223c865-c727-31c3-bee1-21d2f8e87379 | -9.6758 | -65.0214 | 2025-08-31 14:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 56.7 |
| 3b1ee6f5-00d7-3ce9-9a1c-b61ea696d582 | -8.8939 | -45.094 | 2025-08-31 14:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 88.9 |
| 1e89f3d5-5de3-3860-80b5-e67dfdcd08bd | -12.1774 | -50.1342 | 2025-08-31 14:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 67.0 |
| 4ed38b21-b2f2-3e63-a929-11a02af2d39c | -5.4824 | -44.3969 | 2025-08-31 14:20:00 | GOES-19 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 131.4 |
| 38694468-b016-368a-8257-1bff34aedc88 | -13.3439 | -46.9757 | 2025-08-31 14:20:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 65.9 |
| 62f6d1c6-7bba-380f-a90f-04c3bcd54505 | -15.6948 | -52.7312 | 2025-08-31 14:20:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 56.8 |
| 11019607-d995-3542-83ef-52d4bbbf488b | -14.3536 | -51.8918 | 2025-08-31 14:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 112.5 |
| 0955ac10-8587-3449-abb5-9b833073e04b | -6.2409 | -43.3911 | 2025-08-31 14:20:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 187.0 |
| 81f883b4-6e51-3abe-8606-59ca36667972 | -15.7112 | -48.9032 | 2025-08-31 14:20:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 50.5 |
| e3bdd291-687d-3989-8308-55e4b86a862a | -7.4174 | -44.0749 | 2025-08-31 14:20:00 | GOES-19 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 121.9 |


[Clique aqui para ver as próximas entradas](README93.md)
