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

## Dados Diários - Página 80

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b07b6a05-0893-344d-b184-ae8846f34d94 | -13.3792 | -51.5061 | 2026-08-28 14:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 105.9 |
| d8e57460-a336-3be1-bd2e-84e1761a0fed | -12.2086 | -50.5815 | 2026-08-28 14:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 108.9 |
| 19418786-e3b8-32b7-bb38-b2fb1853e478 | -11.8246 | -47.1729 | 2026-08-28 14:50:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 74.1 |
| b15749a6-244b-3851-9217-512202a9ffb1 | -13.4132 | -51.7784 | 2026-08-28 14:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 82.3 |
| 8313316b-c5f9-37df-8aa7-ecf17594a24a | -6.6357 | -45.1752 | 2026-08-28 14:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 57.8 |
| 8e6624d0-c016-3b24-84a6-da82819ba1b5 | -6.8017 | -59.4394 | 2026-08-28 14:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 68.3 |
| b5f35332-dd1a-36ec-aadb-60361d2e0580 | -6.7513 | -55.6853 | 2026-08-28 14:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 61.8 |
| 105f4783-822f-381b-be6a-049fe622104e | -13.3988 | -51.4824 | 2026-08-28 14:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 99.9 |
| b218976a-85d3-36ba-85b9-63c9dab34d9d | -9.1525 | -49.9639 | 2026-08-28 14:50:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 88.7 |
| cccabe6e-4554-319e-a3b8-d5750a848010 | -13.2294 | -51.2904 | 2026-08-28 14:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 74.4 |
| 47ee2e3f-17d3-3799-80d8-73a50caa2df5 | -12.2281 | -50.5578 | 2026-08-28 14:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 190.1 |
| 4b03aa41-a8e1-34db-b5d0-7d259828ebcb | -10.7975 | -54.0146 | 2026-08-28 14:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 62.5 |
| 7d943716-68e1-33f5-8481-e54a89e4a95d | -11.7165 | -54.5449 | 2026-08-28 14:50:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 71.6 |
| 396843ee-8c7a-3c03-9a7f-1a317bd03989 | -11.843 | -47.2152 | 2026-08-28 14:50:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 143.0 |
| 2b6324ae-c0f1-3afc-a8f8-b335df07a816 | -11.7782 | -47.6697 | 2026-08-28 14:50:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 83.3 |
| 3d9ba2cd-81d2-3860-bfda-479af58b661e | -12.0733 | -47.1614 | 2026-08-28 14:50:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 219.5 |
| bac54d4d-9245-3a4e-b361-118f8648ecc0 | -11.2109 | -51.2476 | 2026-08-28 14:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 116.8 |
| 62db29c7-fe5e-310d-892a-23d788aa1fc7 | -13.3789 | -51.5275 | 2026-08-28 14:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 143.7 |
| 3735d97e-ad95-3730-9820-81b2e33aac9c | -8.0551 | -45.839 | 2026-08-28 14:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 94.9 |
| ee818f53-8cca-35aa-a473-6d794daad394 | -13.5797 | -45.7753 | 2026-08-28 14:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 66.1 |
| 644d52a6-11d7-36e6-87a8-a49ff5674c85 | -10.3895 | -61.231 | 2026-08-28 14:50:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 51.6 |
| 354aef8d-a195-3bd8-ba3d-576d96a98003 | -8.0301 | -48.0145 | 2026-08-28 14:50:00 | GOES-19 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 94.8 |
| b4d36e27-ff8a-3f5b-92df-683c8d62ed32 | -11.2302 | -45.0528 | 2026-08-28 14:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 64.2 |
| 4df8510c-f496-396b-845b-dc12637e346f | -6.6397 | -53.173 | 2026-08-28 14:50:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 58.3 |
| 6e1ac488-759f-3a05-9876-81d638a1c488 | -13.3447 | -46.9304 | 2026-08-28 14:50:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 77.5 |
| ef1e39ad-9ce6-34ef-a22a-f03f1b290654 | -11.2493 | -45.0501 | 2026-08-28 14:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 139.8 |
| 30ac4b9d-49a3-3d67-9db3-068fcf2943e3 | -14.1645 | -52.8269 | 2026-08-28 14:50:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 85.1 |
| cecc282f-137a-37a6-81dc-960acb43be01 | -10.7598 | -54.0179 | 2026-08-28 14:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 88.1 |
| ce9aa880-16df-31e3-8410-02896362e814 | -6.2692 | -53.1526 | 2026-08-28 14:50:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 112.2 |
| 34fda35e-e01e-3416-b18c-68701fe3fef5 | -10.9592 | -50.2744 | 2026-08-28 14:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 106.2 |
| ad8c6f34-b447-3b2a-b202-2bd240aa0676 | -12.0729 | -47.1838 | 2026-08-28 14:50:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 75.7 |
| 34bd254f-2df1-3f3f-bcd7-772e57ec7c29 | -11.2111 | -51.2264 | 2026-08-28 14:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 95.0 |
| e3e27346-a864-3683-9a53-7ac4c2fcbb1d | -10.5779 | -50.4857 | 2026-08-28 14:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 94.8 |
| f1199b46-e4dc-3c26-99fb-f7e84dd01c70 | -10.5598 | -50.4236 | 2026-08-28 14:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 104.7 |
| b27b8485-944f-33bb-ad10-5fec7aa78a96 | -11.7594 | -47.6499 | 2026-08-28 14:50:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 108.4 |
| 96153f1e-eb4a-3aa9-8372-a9d6e3ca3a59 | -10.3202 | -49.9782 | 2026-08-28 14:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 124.8 |
| bb2ff5be-9fab-359a-8b48-3c720be5022b | -10.9589 | -50.2958 | 2026-08-28 14:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 100.0 |
| f0c45a02-248f-3427-9bb2-e53fdb07d468 | -8.0918 | -47.527 | 2026-08-28 14:50:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 81.8 |
| 3822fa0f-aee6-34f5-94bd-fd202cc01c28 | -6.8019 | -59.4008 | 2026-08-28 14:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 65.0 |
| 16d6290a-ebad-30f6-a12e-5c3082a3dfbb | -10.8996 | -46.6216 | 2026-08-28 14:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 98.9 |
| 9a9c0bb9-1306-3bfb-a91f-5c64ab22b9c0 | -13.3985 | -51.5037 | 2026-08-28 14:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 114.5 |
| c33bc13d-0258-30cd-b999-75e806b0ac47 | -12.2277 | -50.5792 | 2026-08-28 14:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 117.1 |
| 0e9a7963-3e51-32fe-8581-a1fe784df967 | -15.4788 | -53.9628 | 2026-08-28 14:50:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 75.8 |
| e08fa8e6-0f2e-3db4-942f-4e0f3f044e9f | -11.6773 | -50.4724 | 2026-08-28 14:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 72.2 |
| 0fbffd79-d123-3994-9b12-4a869907d37e | -6.6396 | -53.1934 | 2026-08-28 14:50:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 64.5 |
| e3253216-5678-3d7b-bed8-f0db36175e0e | -14.6024 | -53.1508 | 2026-08-28 14:50:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 114.7 |
| d7d9fd30-33ca-3f4a-aa8b-1fef51a19d9c | -10.8801 | -50.5179 | 2026-08-28 14:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 87.2 |
| 915f5ff2-c258-3a65-b00e-3d7749a38477 | -10.559 | -50.4876 | 2026-08-28 14:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 156.3 |
| c6aec1ff-40d4-3598-9a53-e743d06b7f51 | -8.5964 | -54.8361 | 2026-08-28 14:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 87.7 |
| 5560b576-f204-3b32-be3f-b24cf14ed76e | -8.8184 | -49.6308 | 2026-08-28 14:50:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 61.1 |
| 2e126b63-73a1-391e-8a64-9ceea00338ce | -12.209 | -50.5601 | 2026-08-28 14:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 140.2 |
| c84f7be6-988f-3fdb-9d32-ca97abc20262 | -11.7786 | -47.6474 | 2026-08-28 14:50:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 230.6 |
| 3cc1025e-3c5b-3517-be64-74e2e1344659 | -10.3205 | -49.9567 | 2026-08-28 14:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 106.9 |
| 38b9a386-7632-3d7e-ac84-cda9ba20c4f4 | -10.498 | -64.5193 | 2026-08-28 14:50:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 47.7 |
| 66a667c5-6e07-3c24-8caf-4e29e6231636 | -10.5593 | -50.4663 | 2026-08-28 14:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 105.9 |
| 6287ece6-bf3d-3e96-9fb8-503e5178ed58 | -14.4842 | -52.1512 | 2026-08-28 14:50:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 262.2 |
| bc7e210c-6169-368e-9dcf-274741593ebe | -9.9708 | -53.9419 | 2026-08-28 14:50:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 209.6 |
| 457c422d-89b3-3fbc-a0e4-57a4382e5e8c | -6.6167 | -45.1994 | 2026-08-28 14:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 60.3 |
| 0258634d-15d1-322a-b4f9-cdd2b300450e | -12.3038 | -50.5915 | 2026-08-28 14:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 188.3 |
| 929bc89e-c567-3c7d-85ed-b22c8267a2cd | -8.5971 | -54.7553 | 2026-08-28 14:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 68.2 |
| db74c8b9-eb16-34a8-800b-9f9d573e3af6 | -11.8243 | -47.1954 | 2026-08-28 14:50:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 139.2 |
| f31179bc-a5db-384e-ab40-09b040546334 | -8.7757 | -50.083 | 2026-08-28 14:50:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 86.9 |
| 16f9ee2a-184f-30ce-85be-52fe002bc969 | -14.4838 | -52.1725 | 2026-08-28 14:50:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 76.7 |
| e550882d-6129-3bec-b58c-eb7572da1f86 | -13.3597 | -51.5299 | 2026-08-28 14:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 101.6 |
| e41b3042-3cb9-3e47-8e55-00c7b6c338f9 | -8.948 | -62.3894 | 2026-08-28 14:50:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 131.4 |
| cb01fb09-b82b-3363-b38a-d8fb82e28f0c | -6.7832 | -59.4401 | 2026-08-28 14:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 74.5 |
| 8475c8d3-c8b7-3c95-b613-7bf43754731f | -10.7407 | -54.0401 | 2026-08-28 14:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 49.5 |
| d0b40c95-a1bb-3c53-8d18-90888d52a9c2 | -10.7596 | -54.0384 | 2026-08-28 14:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 175.5 |
| 78351d8b-e8db-3ab2-8006-2c9e2eb911e9 | -10.3391 | -49.9762 | 2026-08-28 14:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 91.5 |
| 8a098abf-2c82-39b9-a291-a8f60c7be864 | -9.4329 | -51.6926 | 2026-08-28 14:50:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 84.6 |
| 2b832d6d-f73c-3c16-867d-e28e6def1d1e | -10.9187 | -46.6192 | 2026-08-28 14:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 131.0 |
| 77f2c298-2038-3068-a469-8e8254be4ac9 | -10.8992 | -46.6442 | 2026-08-28 14:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 93.6 |
| 39a310be-2f80-33d0-934f-f96f0c9ef4d7 | -12.3041 | -50.5701 | 2026-08-28 14:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 151.6 |
| 20f1a3c1-8089-3570-9348-cb054e69cba5 | -6.769 | -58.7066 | 2026-08-28 14:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 90.7 |
| eeeb93ca-a90d-3697-8d93-78749cb41517 | -8.2414 | -54.9601 | 2026-08-28 14:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 59.0 |
| 88eec1c8-6309-370a-b767-6b6ad9639802 | -6.2693 | -53.1322 | 2026-08-28 14:50:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 156.9 |
| b7b89316-2e71-3f0b-815c-73f99c11e33c | -6.9521 | -58.9506 | 2026-08-28 14:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 77.5 |
| 7f6b31c5-e1f6-35c4-a4e2-4ea0d59f1d43 | -8.776 | -50.0616 | 2026-08-28 14:50:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 96.4 |
| f56ee0ba-583f-3698-a413-4c0514c6eb8a | -9.2282 | -51.5428 | 2026-08-28 14:50:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 85.7 |
| c7702756-8c2f-389a-8a1f-c1a327b4c303 | -12.0541 | -47.164 | 2026-08-28 14:50:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 119.8 |
| d7de9aab-268f-3169-b061-7917c1972c65 | -8.6017 | -70.0173 | 2026-08-28 14:50:00 | GOES-19 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 59.3 |
| e2fd52ea-f357-3c71-a6db-fe6e7166a4b2 | -12.0538 | -47.1865 | 2026-08-28 14:50:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 72.1 |
| 85e3c76c-27d5-3ebf-a750-cffaafe8b159 | -11.7167 | -54.5244 | 2026-08-28 14:50:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 60.5 |
| 19176552-029b-31a6-ac40-838c117a5ecc | -14.8624 | -52.6318 | 2026-08-28 14:50:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 85.2 |
| d76eea01-0a77-3834-b51e-900015e612bf | -8.9478 | -62.4084 | 2026-08-28 14:50:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 136.4 |
| bc9c51fa-f7f0-37e3-a009-6250489a4753 | -10.4981 | -64.5005 | 2026-08-28 14:50:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 99.1 |
| 4a5eff09-e300-3328-8055-c686b79584e3 | -14.3182 | -51.7046 | 2026-08-28 14:50:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 147.4 |
| 46557253-e84e-360e-a285-a85d2562b5f1 | -12.2277 | -50.5792 | 2026-08-28 15:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 262.7 |
| 6c8c8644-ea8c-3130-94bd-37c76ef1c283 | -8.164 | -46.1657 | 2026-08-28 15:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 69.1 |
| bd594692-18f4-37e7-8264-94193ee7a178 | -5.9467 | -44.7745 | 2026-08-28 15:00:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 64.2 |
| 77f7dbd0-efbb-3672-b0a4-1efb488df6cb | -10.3205 | -49.9567 | 2026-08-28 15:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 85.9 |
| aaeca9c4-2fec-37df-8fb4-2f6534d37a8b | -13.8752 | -54.1153 | 2026-08-28 15:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 65.6 |
| fef271bb-6596-36ec-ae3f-967e291ad7be | -8.9478 | -62.4084 | 2026-08-28 15:00:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 152.9 |
| 86d7a279-1238-3575-8fda-b7fca11923f0 | -13.3792 | -51.5061 | 2026-08-28 15:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 108.3 |
| fe2f0f2c-2ecc-3999-9bc9-1b9fa787835c | -10.559 | -50.4876 | 2026-08-28 15:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 122.2 |
| eeba5f7a-3505-3643-87be-336581ed4803 | -6.2693 | -53.1322 | 2026-08-28 15:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 181.6 |
| 893368e1-5e52-3c2d-868e-30e0b5e6458d | -11.2111 | -51.2264 | 2026-08-28 15:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 104.1 |
| a7fdc910-16a4-3db8-a928-806b93c49aa6 | -6.2692 | -53.1526 | 2026-08-28 15:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 129.4 |
| 9c9cd496-52b6-3608-8eb7-6ffb30479d7f | -14.1645 | -52.8269 | 2026-08-28 15:00:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 103.5 |
| d5ba2b67-bb62-329d-a811-8b7d4bf0d7e7 | -12.209 | -50.5601 | 2026-08-28 15:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 179.5 |


[Clique aqui para ver as próximas entradas](README81.md)
