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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5e0f042c-a5fb-3a17-a720-4e1bf8794e23 | -12.0623 | -49.7673 | 2026-06-09 00:25:00 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e4965b18-7a73-385d-904a-e5c86251691f | -11.5547 | -52.775799 | 2026-06-09 00:25:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 103268fc-8b0b-386e-b2ca-7a9589675568 | -11.655 | -52.857399 | 2026-06-09 00:25:00 | METOP-B | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| aadd6232-cc3d-3f65-93b0-08f3003e94e9 | -21.546 | -47.029099 | 2026-06-09 00:25:00 | METOP-B | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 62fafc61-5c1e-3f80-b131-f9409408950d | -12.0357 | -47.8036 | 2026-06-09 00:25:00 | METOP-B | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 56ffbd21-dbbf-3b07-9c0a-2e276b87908c | -12.439 | -58.4618 | 2026-06-09 00:25:00 | METOP-B | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 47b6ce88-f44d-390b-aa1c-a980b4f57b16 | -20.4191 | -51.271599 | 2026-06-09 00:25:00 | METOP-B | ILHA SOLTEIRA | SÃO PAULO | Brasil | 3520442 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 6b908680-2733-3e76-9d82-ca6d8921ed6d | -21.4366 | -48.6395 | 2026-06-09 00:25:00 | METOP-B | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| ccd02737-95df-305a-a047-e75009577ceb | -7.0952 | -46.490898 | 2026-06-09 00:25:00 | METOP-B | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 06422b6e-dcd5-36d3-ac1a-bde482d5f38b | -5.8039 | -45.109402 | 2026-06-09 00:25:00 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 51c236b9-05b1-3a91-a1fa-391d5c333086 | -11.021 | -49.417599 | 2026-06-09 00:25:00 | METOP-B | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c89f704a-c159-3553-a302-04695ec7b152 | -7.0982 | -46.5037 | 2026-06-09 00:25:00 | METOP-B | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| bdd520f3-062d-3402-814d-acd416295fed | -21.276899 | -48.617001 | 2026-06-09 00:25:00 | METOP-B | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| cf9006db-1582-398f-95a2-44da714be077 | -11.5531 | -52.768799 | 2026-06-09 00:25:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 42fd197e-1d87-30c6-bb4b-dcc38f6e3f49 | -7.1111 | -46.514198 | 2026-06-09 00:25:00 | METOP-B | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 843afa96-31b9-3a61-80ec-6ed9a7a2535a | -12.4693 | -55.115898 | 2026-06-09 00:25:00 | METOP-B | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a725aaa4-a416-3bb3-9f6b-b295e4340c20 | -9.0768 | -50.608002 | 2026-06-09 00:25:00 | METOP-B | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 96ca9eed-49c4-324d-b800-10bb259575ad | -21.2752 | -48.6096 | 2026-06-09 00:25:00 | METOP-B | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 0f8c7309-bf60-342b-b7a5-7c9a6720e256 | -12.8553 | -44.359501 | 2026-06-09 00:25:00 | METOP-B | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 91e9b8ca-29d4-3969-8701-d45eda392b22 | -12.0605 | -49.7598 | 2026-06-09 00:25:00 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 01c48b02-5f6e-35c6-a560-af109d86e338 | -15.1775 | -43.8438 | 2026-06-09 00:25:00 | METOP-B | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| ed938619-30ea-3b57-89d8-4aeec3cd579e | -17.591801 | -46.637402 | 2026-06-09 00:25:00 | METOP-B | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| c197504c-3078-3811-81e6-d6618cfcff94 | -11.5758 | -54.576698 | 2026-06-09 00:25:00 | METOP-B | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7dbc46ef-a334-3178-a8d7-69e0f31801d5 | -7.1013 | -46.516499 | 2026-06-09 00:25:00 | METOP-B | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6fba4b9c-e8a9-3aef-b44c-25a4cdf8ff80 | -10.9011 | -49.3465 | 2026-06-09 00:25:00 | METOP-B | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 55b8ec3b-9089-3fd3-8c69-51ee5eaabb59 | -11.5449 | -52.778 | 2026-06-09 00:25:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| bba8aaa7-162b-369c-a9e0-5b9a850d3af8 | -17.452101 | -47.18 | 2026-06-09 00:25:00 | METOP-B | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 37e39671-1dfe-33a5-be46-23caca4ec8d3 | -9.0751 | -50.6007 | 2026-06-09 00:25:00 | METOP-B | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2e4d6bbb-f61b-3f89-bc78-a17f30f0c7bc | -12.3652 | -47.884998 | 2026-06-09 00:25:00 | METOP-B | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 01ddc0f8-a7a0-3eea-89e7-0b1f491b99f2 | -9.3424 | -47.9034 | 2026-06-09 00:25:00 | METOP-B | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 760749f2-97e3-3f67-9c9e-45c5a7ef75d2 | -11.6534 | -52.8503 | 2026-06-09 00:25:00 | METOP-B | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2b34b749-3f8c-309e-9757-0d7ade918ac3 | -12.0588 | -49.752399 | 2026-06-09 00:25:00 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5348a37b-e43a-3a39-ba30-272fd355ba66 | -10.6498 | -49.3834 | 2026-06-09 00:30:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 54.0 |
| 24e98840-d41f-3bbb-96f7-d2e9d33b20a1 | -12.0498 | -49.7612 | 2026-06-09 00:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 54.3 |
| edc38caf-9fd0-3e23-a648-9eacb0d51ce5 | -9.3045 | -45.4809 | 2026-06-09 00:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 65.1 |
| 6f3f7e73-210e-3247-a07e-20f701c89bb6 | -5.7941 | -45.104 | 2026-06-09 00:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 62.4 |
| 2b169b63-fe3d-36a1-81b5-c9345b2bb69c | -7.1092 | -46.5065 | 2026-06-09 00:30:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 102.5 |
| adbd4492-9083-3e69-9308-f73c1fd67aef | -12.0689 | -49.7589 | 2026-06-09 00:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 62.7 |
| bd1b8c64-8e52-347f-a4cc-3cc9c68a6413 | -11.5502 | -52.7659 | 2026-06-09 00:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 63.1 |
| 40080df0-5894-357f-a02b-d61fb86dd395 | -5.8128 | -45.1026 | 2026-06-09 00:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 64.3 |
| d053fe6b-dc41-37da-b2f9-64ecfdaa7e10 | -17.5961 | -46.6415 | 2026-06-09 00:30:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 47.3 |
| de005160-329e-3a63-a04a-e818f5fb47ae | -11.5499 | -52.7867 | 2026-06-09 00:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 117.7 |
| 500adadd-2820-37dc-a8af-9599b16ceb9d | -12.4464 | -58.4825 | 2026-06-09 00:30:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 40.4 |
| 7fe01703-248c-3e0f-a057-a2e4a3072bc0 | -12.4466 | -58.4627 | 2026-06-09 00:30:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 47.5 |
| 1e2f1532-b9db-37d1-b607-00027a580716 | -9.0699 | -50.6091 | 2026-06-09 00:40:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 51.3 |
| 40d36f2f-7492-3a38-9c6d-89e49a1877e4 | -9.3045 | -45.4809 | 2026-06-09 00:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 39.5 |
| c74e62a6-7c5d-3924-a6e1-7c9c11af09d3 | -12.0498 | -49.7612 | 2026-06-09 00:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 57.0 |
| f121dd38-f6da-3abf-8713-cfc2a8fdafd9 | -10.6498 | -49.3834 | 2026-06-09 00:40:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 64.1 |
| 01dde54f-db14-3aac-8410-d0bee5c43636 | -5.7941 | -45.104 | 2026-06-09 00:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 68.1 |
| cc7b7d85-e221-39b4-ac48-98c8e2be44c9 | -7.1092 | -46.5065 | 2026-06-09 00:40:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 84.6 |
| 5dfa4e7e-e268-3b48-bb6c-ccfb332cd7a4 | -11.5309 | -52.7887 | 2026-06-09 00:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 32.9 |
| 0bdf95a9-58f7-3d77-92a1-40d2129b15ac | -11.5499 | -52.7867 | 2026-06-09 00:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 126.3 |
| 0fcd47c8-4942-3011-899d-9d8a99092a9d | -11.5502 | -52.7659 | 2026-06-09 00:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 47.1 |
| a0a4983f-ff11-31e0-89bf-5b914efb5b7c | -12.4466 | -58.4627 | 2026-06-09 00:40:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 49.2 |
| 492d28c5-f8a0-3bba-91a7-3917b28dcb90 | -12.0689 | -49.7589 | 2026-06-09 00:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 55.1 |
| f8ecb85e-3292-3efe-b1fd-e4735d2ca143 | -17.5961 | -46.6415 | 2026-06-09 00:50:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 56.8 |
| 923a3862-bd23-3747-b3cc-ed4ff60d7787 | -9.3045 | -45.4809 | 2026-06-09 00:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 45.0 |
| 5743915d-3264-362e-ae28-020817cbf610 | -10.6498 | -49.3834 | 2026-06-09 00:50:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 49.3 |
| 84bb518a-9f9b-30a4-a74d-3be5fb5049f7 | -11.5499 | -52.7867 | 2026-06-09 00:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 102.5 |
| 498753dd-1a19-323d-8327-df62ba627045 | -11.5309 | -52.7887 | 2026-06-09 00:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 37.2 |
| 208f508a-ad8d-329f-b432-e6c8d29f7e33 | -5.8128 | -45.1026 | 2026-06-09 00:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 59.7 |
| 3a78e5bd-fa63-3053-abf1-7a432b890051 | -12.0498 | -49.7612 | 2026-06-09 00:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 66.0 |
| 130f965a-d0f0-3e7f-96ce-41abd62fb235 | -11.5688 | -52.7848 | 2026-06-09 00:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 33.5 |
| 92936356-9daf-3ace-8f2a-e8474459fe4f | -11.5502 | -52.7659 | 2026-06-09 00:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 43.9 |
| c1fd7621-e9e0-393e-bbff-fc92b805b21f | -12.0498 | -49.7612 | 2026-06-09 01:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 57.7 |
| fc5229ea-037c-357b-95a7-7e752cb6d75e | -11.5499 | -52.7867 | 2026-06-09 01:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 120.9 |
| 641d3910-3ef2-3197-841a-27d30bc071fd | -7.1092 | -46.5065 | 2026-06-09 01:00:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 51.6 |
| 7cadd987-77bb-37ba-9f1e-35ee9daefb8f | -10.6498 | -49.3834 | 2026-06-09 01:00:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 68.7 |
| 59b84430-2a8e-3cd3-9d8c-de1be5db2b54 | -17.5961 | -46.6415 | 2026-06-09 01:00:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 42.9 |
| d3840bba-702f-306b-b39f-63670edb1e50 | -9.3045 | -45.4809 | 2026-06-09 01:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 47.3 |
| c1c2c910-886f-3af2-b519-ae419ce3e9b1 | -12.4466 | -58.4627 | 2026-06-09 01:00:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 45.5 |
| 24bade12-5137-3f10-9d2f-5c27d7f2b5e4 | -9.0699 | -50.6091 | 2026-06-09 01:00:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 55.8 |
| 9adb9ea4-12b7-3c95-841a-bfe94d1b3cf5 | -11.5502 | -52.7659 | 2026-06-09 01:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 41.5 |
| a355c3f1-2630-3ae2-a9c9-6e8942589110 | -12.0689 | -49.7589 | 2026-06-09 01:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 49.1 |
| cdbd5269-4c06-335d-87c1-80b89369cb41 | -5.8128 | -45.1026 | 2026-06-09 01:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 60.4 |
| 9126218d-4d7c-3d2f-9c40-d35a60517778 | -12.4466 | -58.4627 | 2026-06-09 01:10:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 44.5 |
| f28560d0-d08c-31e5-8e73-d5a2738a048c | -9.3045 | -45.4809 | 2026-06-09 01:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 53.9 |
| ee39bd8b-0b9a-3a41-a709-44cf6b6e1897 | -17.5961 | -46.6415 | 2026-06-09 01:10:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 65.8 |
| 7c7b1e36-94b4-32e4-949a-33312a761968 | -11.5502 | -52.7659 | 2026-06-09 01:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 45.8 |
| 09cf763e-a28b-37b8-81eb-d84214662f8f | -5.7941 | -45.104 | 2026-06-09 01:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 60.0 |
| acd19fdc-054e-394a-8d1c-cc7d98590b12 | -9.0699 | -50.6091 | 2026-06-09 01:10:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 50.1 |
| 922b88c2-9bef-3a55-b5d3-6c348b362b4b | -12.0689 | -49.7589 | 2026-06-09 01:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 55.4 |
| 538f5078-ec4d-3440-8903-b2ad6fe9a0a5 | -11.5499 | -52.7867 | 2026-06-09 01:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 105.4 |
| a55e2356-5a12-3773-9cc5-0e52009f8bdd | -10.6498 | -49.3834 | 2026-06-09 01:10:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 67.6 |
| d5d00d8b-0c15-3dbe-b01c-09a6638d5e6a | -12.0498 | -49.7612 | 2026-06-09 01:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 52.4 |
| 7806b131-d7c8-3ee2-8b47-05d1908da41c | -10.6498 | -49.3834 | 2026-06-09 01:20:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 63.6 |
| 27bd1cb4-ca48-30af-a208-46ab4ae17052 | -17.5961 | -46.6415 | 2026-06-09 01:20:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 45.7 |
| f9e62327-c768-35a8-bb5a-30fafc6ad120 | -9.3045 | -45.4809 | 2026-06-09 01:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 59.9 |
| d9ba7aa9-68be-38e5-9a40-f748f7e72ac0 | -7.1092 | -46.5065 | 2026-06-09 01:20:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 69.4 |
| d3c1a673-9ba4-3328-8d8e-2d48ca842330 | -11.5499 | -52.7867 | 2026-06-09 01:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 107.2 |
| 92578a5c-c367-3471-b2a4-2cda9a6f33c2 | -12.0498 | -49.7612 | 2026-06-09 01:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 55.6 |
| c351709d-5189-30e5-b01a-d9fcfe07b3e2 | -11.5502 | -52.7659 | 2026-06-09 01:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 42.0 |
| 6e15a814-b3d1-3bc6-aba5-1c85f93c4fd9 | -12.44215 | -58.47087 | 2026-06-09 01:24:00 | TERRA_M-M | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 53.4 |
| 062dfedd-c1f8-3040-90a0-24823da0b839 | -12.44476 | -58.47717 | 2026-06-09 01:24:00 | TERRA_M-M | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 40.4 |
| 3b16617b-4a4d-3a7f-834b-8543315723f1 | -9.2855 | -45.483 | 2026-06-09 01:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 53.1 |
| e949cbe5-8eda-3456-a830-9bcda823c633 | -12.0498 | -49.7612 | 2026-06-09 01:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 62.1 |
| 7c781a7b-1abb-306b-b8e2-b0add127e175 | -9.2858 | -45.4602 | 2026-06-09 01:30:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 53.2 |
| 1612297b-41fb-346c-8045-e2b4ceaf6ee3 | -9.3045 | -45.4809 | 2026-06-09 01:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 84.2 |
| 16eb216c-9213-3566-950a-6499cb6667ba | -21.2188 | -48.5069 | 2026-06-09 01:30:00 | GOES-19 | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Cerrado | 42.6 |
| c273e8a6-2a0f-351f-ab7a-60e99909ed83 | -7.1092 | -46.5065 | 2026-06-09 01:30:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 68.0 |


[Clique aqui para ver as próximas entradas](README3.md)
