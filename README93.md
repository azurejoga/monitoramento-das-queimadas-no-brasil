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

## Dados Diários - Página 93

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1d9e413e-3917-383f-aedd-303936e64eba | -14.354 | -51.8705 | 2025-08-31 14:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 96.7 |
| 62915b3e-6f2b-34e1-aa83-cd9fb0985a88 | -10.0434 | -48.0998 | 2025-08-31 14:20:00 | GOES-19 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 152.8 |
| 6d295d27-a89c-343d-9a93-52b85f284886 | -7.8729 | -46.973 | 2025-08-31 14:20:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 131.5 |
| 3d8e0421-49b9-3262-981a-e52cfba8e3f6 | -6.5812 | -44.9979 | 2025-08-31 14:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 232.0 |
| c4ee3d84-4fe8-3eb8-a8e2-706e7535e633 | -12.3287 | -45.7201 | 2025-08-31 14:20:00 | GOES-19 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 134.8 |
| 5a7c8e6b-285d-3c9f-a680-a56a2dcb0baa | -15.7102 | -48.9479 | 2025-08-31 14:20:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 127.6 |
| 59afed9c-1c77-3e54-8ed9-0c2fa93471a0 | -4.7346 | -44.4457 | 2025-08-31 14:20:00 | GOES-19 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 187.6 |
| 920fe810-e63c-305f-83c3-e2f7c0d55d42 | -4.9124 | -43.187 | 2025-08-31 14:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 81.7 |
| 26a1d4e3-bd83-3a37-a8a1-36320a7a6741 | -6.185 | -43.3491 | 2025-08-31 14:20:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 113.6 |
| f553f6bb-5a6d-3eac-ba54-f60fec1bbf36 | -6.1663 | -43.3506 | 2025-08-31 14:20:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 253.9 |
| 350f3eab-9708-383d-8308-098669565d0e | -10.7862 | -60.7655 | 2025-08-31 14:20:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 65.2 |
| 3c79a1fb-7f70-39ef-b710-bcad1466f160 | -8.6649 | -48.3057 | 2025-08-31 14:20:00 | GOES-19 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 87.4 |
| 2185d304-023a-35be-81b6-2666c6c7b22c | -11.0845 | -44.6343 | 2025-08-31 14:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 185.8 |
| 6e9ed64e-8bd7-349c-9be6-2ee26edf6122 | -7.0951 | -44.3128 | 2025-08-31 14:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 120.3 |
| 0fa60978-f06c-3129-b7dc-bf3aadf19c6c | -6.4833 | -43.557 | 2025-08-31 14:20:00 | GOES-19 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 85.3 |
| 0408b032-acfd-33f8-94a2-d169e4e20972 | -11.3709 | -43.5631 | 2025-08-31 14:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 124.8 |
| f5ad0d7d-7fb7-3279-93f5-a2ba85032451 | -13.3636 | -46.95 | 2025-08-31 14:20:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 74.5 |
| 07821681-b67f-3ca9-b5d8-089fabde464b | -12.3287 | -45.7201 | 2025-08-31 14:30:00 | GOES-19 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 108.1 |
| 2f2e0ecd-f285-378d-b2fd-81f0cd26136f | -11.8553 | -46.494 | 2025-08-31 14:30:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 101.2 |
| 9b020605-9950-359d-adc9-68f750a91a33 | -11.3334 | -43.5216 | 2025-08-31 14:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 140.0 |
| 623b6370-48ca-3a6e-a4fa-689e66b98f9c | -5.4824 | -44.3969 | 2025-08-31 14:30:00 | GOES-19 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 167.6 |
| e01c60af-4fcb-387c-ada6-cb25bb83d368 | -9.1381 | -45.2036 | 2025-08-31 14:30:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 92.1 |
| c9530485-3a6f-3810-b0d7-b8959d680605 | -14.354 | -51.8705 | 2025-08-31 14:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 68.2 |
| 6a8198da-9424-3d6c-b19c-1ed1f67a906f | -5.6573 | -43.6465 | 2025-08-31 14:30:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 129.1 |
| e69cabc7-5d47-3688-81d3-acc05d8a8580 | -6.2409 | -43.3911 | 2025-08-31 14:30:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 168.8 |
| 99b6c822-3abf-3fd3-af60-c0c22c87e4b6 | -8.8936 | -45.1168 | 2025-08-31 14:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 89.6 |
| eeb4e544-20d1-32b1-a0bd-6e4d92f9c833 | -6.5758 | -43.6885 | 2025-08-31 14:30:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 86.9 |
| d43ba1a7-a5c4-38b0-aed9-4bcd5e104ed4 | -11.0658 | -44.6137 | 2025-08-31 14:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 169.5 |
| 271f75c3-d8ac-3de9-9efb-54f147cb0431 | -11.3317 | -43.6162 | 2025-08-31 14:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 148.5 |
| 86d7d9c6-20b3-3904-8003-3451639bb248 | -14.5832 | -52.0104 | 2025-08-31 14:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 63.9 |
| ad399f89-f5c0-3132-abe9-20f55e0d3e50 | -7.063 | -43.8073 | 2025-08-31 14:30:00 | GOES-19 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 116.7 |
| d72f1d0e-34e0-3bcb-929b-e6002bdf50bc | -7.8729 | -46.973 | 2025-08-31 14:30:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 113.7 |
| a42fa7ff-71c6-35a3-88b8-02683a21faf3 | -14.3346 | -51.873 | 2025-08-31 14:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 96.5 |
| d8bd6774-7928-3c87-979f-55e52666d493 | -6.9488 | -45.7141 | 2025-08-31 14:30:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 127.1 |
| af2ffe67-2ddd-3c8d-a651-67e047a49332 | -14.3536 | -51.8918 | 2025-08-31 14:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 81.8 |
| 5d19e016-d874-3d91-a8f8-d7143bb85a89 | -9.2636 | -47.1027 | 2025-08-31 14:30:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 106.1 |
| a9019780-29cf-36e1-8db8-e00b1fca5972 | -15.7102 | -48.9479 | 2025-08-31 14:30:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 187.0 |
| 35b99247-65ab-3789-9558-8c3fd6ddba71 | -5.8884 | -42.9753 | 2025-08-31 14:30:00 | GOES-19 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 93.0 |
| 2b2a8b89-347e-3d60-ad55-917fa1cc0da7 | -4.9124 | -43.187 | 2025-08-31 14:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 86.5 |
| af32b272-1751-3ab6-bedd-cdafdd39d78e | -8.875 | -45.0961 | 2025-08-31 14:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 180.7 |
| e660f3e3-9507-33b4-b08a-e58784a4c269 | -6.5209 | -43.5537 | 2025-08-31 14:30:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 123.5 |
| 06016f10-b60b-3d25-9872-701b41ac8406 | -7.3985 | -44.0768 | 2025-08-31 14:30:00 | GOES-19 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 160.8 |
| 97f81a3f-22ed-31f3-9749-9e9abfd732cc | -7.0628 | -43.8305 | 2025-08-31 14:30:00 | GOES-19 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 117.7 |
| d162c4b8-2c55-3dac-97d0-05226882b09e | -15.7098 | -48.9702 | 2025-08-31 14:30:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 218.7 |
| 02d30e27-2ab9-3ecc-89c7-38307d233e93 | -15.7107 | -48.9255 | 2025-08-31 14:30:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 79.4 |
| d445bb66-c1eb-3f49-87d1-1c14ae2abeaf | -6.9675 | -45.7125 | 2025-08-31 14:30:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 92.8 |
| b269a30f-c867-3c04-bb3e-eb402867eb82 | -6.1663 | -43.3506 | 2025-08-31 14:30:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 206.5 |
| e0f49663-85b1-3775-950d-6e769f184a4d | -14.5642 | -51.9917 | 2025-08-31 14:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 101.0 |
| 2b6a35c8-44e3-3cea-8555-00791cac20dd | -7.1139 | -44.3111 | 2025-08-31 14:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 178.8 |
| 751b11cc-ee38-3a37-aed5-79834ef3ad15 | -5.7694 | -43.6845 | 2025-08-31 14:30:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 120.1 |
| 78f5d5b3-1b2c-32c3-96c1-98f104b38869 | -13.3065 | -46.9137 | 2025-08-31 14:30:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 86.4 |
| 36ac4e6f-a02f-3d38-9076-dcdb41280b49 | -6.2411 | -43.3677 | 2025-08-31 14:30:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 136.2 |
| f46a035d-f686-3ab8-9131-5c2084f20372 | -13.3443 | -46.953 | 2025-08-31 14:30:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 77.7 |
| 50c78fa1-0f16-336e-9c58-52820808d796 | -11.3713 | -43.5394 | 2025-08-31 14:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 117.5 |
| dcfd3646-a7eb-3822-a058-f86a8522d889 | -11.8549 | -46.5167 | 2025-08-31 14:30:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 88.1 |
| 4d3210aa-81c4-3e30-aab1-cf8a961fa2f2 | -14.0307 | -44.5814 | 2025-08-31 14:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 126.0 |
| 7f9f69d1-a938-3a2e-b73e-be9bcdeb47a9 | -13.4982 | -46.9743 | 2025-08-31 14:30:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 63.6 |
| c65b2bbf-840c-3d96-820c-6c8db552cb7b | -14.3343 | -51.8944 | 2025-08-31 14:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 76.4 |
| c6901c45-2e62-3487-a8ab-2d564d474b74 | -11.3701 | -43.6104 | 2025-08-31 14:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 185.9 |
| 92c76e87-4056-3abb-b3ad-5c2195e24d7f | -10.7862 | -60.7655 | 2025-08-31 14:30:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 69.3 |
| 9002b983-a2e3-3ba0-b6ea-2ffa82d04d4e | -11.3705 | -43.5868 | 2025-08-31 14:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 165.4 |
| 1668054f-e5d8-382e-8174-d9d27de5a5d4 | -13.4788 | -46.9774 | 2025-08-31 14:30:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 89.7 |
| 8529c027-c956-385c-a1ab-146bf931f987 | -11.3526 | -43.5187 | 2025-08-31 14:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 140.7 |
| 3fb7f866-fa3a-3166-8283-d6e46d21987b | -11.8181 | -46.4314 | 2025-08-31 14:30:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 97.6 |
| c0e12f9d-7beb-3016-a019-39f1a098004a | -11.8361 | -46.4967 | 2025-08-31 14:30:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 272.2 |
| 3028ce5d-bff7-33aa-bfcf-7627455a1c61 | -12.1965 | -50.1318 | 2025-08-31 14:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 119.3 |
| 1004510a-d242-376a-b4cc-5b20b3f5c585 | -7.0951 | -44.3128 | 2025-08-31 14:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 111.8 |
| 596b6a43-1f5d-31dd-8d26-d10ad1b75609 | -6.1586 | -44.1395 | 2025-08-31 14:30:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 103.2 |
| 1d14f4a7-8234-30dd-aeb2-22da2ed57368 | -11.3509 | -43.6133 | 2025-08-31 14:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 168.4 |
| dbbde34f-9bdf-3222-a0ee-04ecd0e0acd4 | -11.0849 | -44.611 | 2025-08-31 14:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 192.8 |
| 4d254afe-0dc8-3300-bccf-b0601141c553 | -5.8696 | -42.9768 | 2025-08-31 14:30:00 | GOES-19 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 231.3 |
| b66c48b3-faa6-30b6-af63-57d959d83159 | -9.245 | -47.0824 | 2025-08-31 14:30:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 94.7 |
| 65ebb6f8-eecb-337c-9b37-3f562ab9ae4a | -6.0553 | -45.1754 | 2025-08-31 14:30:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 81.6 |
| f9e4d649-3946-31c0-8601-d69ae998b98e | -14.8013 | -46.7371 | 2025-08-31 14:30:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 162.1 |
| 914bcc7b-ce84-32e9-bdcb-631d208d7b03 | -15.7112 | -48.9032 | 2025-08-31 14:30:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 44.6 |
| 387377d5-b7e2-39e9-a08a-fc99321cbb64 | -6.1855 | -43.3023 | 2025-08-31 14:30:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 94.6 |
| 00f42dc4-13d0-37f3-9aef-2a4a955e2b50 | -6.185 | -43.3491 | 2025-08-31 14:30:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 117.5 |
| 14a3b9b1-b2a0-39d5-a4be-249015480ad4 | -6.4833 | -43.557 | 2025-08-31 14:30:00 | GOES-19 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 104.2 |
| 3fc961ce-e40e-3fc3-a151-990805f6a60c | -6.5812 | -44.9979 | 2025-08-31 14:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 136.5 |
| b00d276c-fc83-32a5-87e0-4110c322bafc | -11.0845 | -44.6343 | 2025-08-31 14:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 221.9 |
| b97a4996-f6ba-367a-a223-a6b8edea1c72 | -6.1853 | -43.3257 | 2025-08-31 14:30:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 179.8 |
| e9bf193f-bcd2-3c5a-b9c0-1f210fba6cc3 | -8.421 | -48.2847 | 2025-08-31 14:30:00 | GOES-19 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 119.0 |
| 4642b638-63a2-3031-82d6-7a1bfa32d62b | -12.1778 | -50.1126 | 2025-08-31 14:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 102.4 |
| 9bebf643-2be8-3ab8-b522-f9c79d231c75 | -11.3709 | -43.5631 | 2025-08-31 14:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 161.2 |
| fea43b33-57ca-31c6-bdd6-ff274a9fa9ad | -5.7696 | -43.6613 | 2025-08-31 14:30:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 111.3 |
| bc192803-760d-37a9-b36c-644e16ed0ec8 | -8.6649 | -48.3057 | 2025-08-31 14:30:00 | GOES-19 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 73.2 |
| 39dfdb6c-b6b2-3e16-b2e7-ad56c72a2e8f | -10.7714 | -48.8273 | 2025-08-31 14:30:00 | GOES-19 | FÁTIMA | TOCANTINS | Brasil | 1707553 | 17 | 33 | nan | nan | nan | Cerrado | 87.6 |
| b01d1e7f-e4da-3eae-ba91-bf0cf16c80aa | -10.0434 | -48.0998 | 2025-08-31 14:30:00 | GOES-19 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 100.1 |
| 96fdc4ae-a171-33eb-ab3a-c7729c9efcf4 | -15.7298 | -48.9446 | 2025-08-31 14:30:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 43.8 |
| a984c187-bbc5-3ead-9651-149c72bef2c4 | -13.4199 | -47.0317 | 2025-08-31 14:30:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 79.2 |
| 5da5b96d-8eb4-3953-bfe4-9231d64d82d0 | -12.0744 | -50.6403 | 2025-08-31 14:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 85.9 |
| dde7ad72-0fcb-3ba9-b2e6-c32f95a0c426 | -7.4174 | -44.0749 | 2025-08-31 14:30:00 | GOES-19 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 136.1 |
| 27944cc4-a7e7-3e8a-bfa8-b131714153e6 | -12.1774 | -50.1342 | 2025-08-31 14:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 112.2 |
| 23627697-9361-3db4-a41f-0ffd490a1b1e | -5.8052 | -43.867 | 2025-08-31 14:30:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 106.3 |
| 5e5aee92-9e42-30f3-a951-5b8daf244b32 | -14.8208 | -46.7337 | 2025-08-31 14:30:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 128.6 |
| cba0c2dd-9f38-3209-b94d-842b6de2cfdf | -12.1969 | -50.1102 | 2025-08-31 14:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 207.4 |
| d27bc728-c883-317a-afc7-0bdb506e13d6 | -6.7724 | -44.6397 | 2025-08-31 14:30:00 | GOES-19 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 83.4 |
| 6460a6d0-fb3b-3663-9502-429b76c9d3bc | -11.8357 | -46.5194 | 2025-08-31 14:30:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 331.5 |
| 2f104787-41b1-30cc-9d8e-64cdd53e3c9c | -6.2956 | -43.5496 | 2025-08-31 14:30:00 | GOES-19 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 89.2 |
| 500066db-637d-3c6b-afeb-4a4eccf70d82 | -11.3521 | -43.5423 | 2025-08-31 14:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 122.6 |


[Clique aqui para ver as próximas entradas](README94.md)
