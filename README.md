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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 04a7953a-b292-3401-b17f-d1b027c45a75 | -7.2747 | -46.8036 | 2026-09-12 00:00:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 60.8 |
| 429e9bbc-1c7c-3d31-86fd-ec796ab447db | -13.4162 | -42.4755 | 2026-09-12 00:00:00 | GOES-19 | BOTUPORÃ | BAHIA | Brasil | 2904209 | 29 | 33 | nan | nan | nan | Caatinga | 161.7 |
| 58f9c35e-7604-386a-a38f-e42eb7e011aa | -5.7569 | -45.084 | 2026-09-12 00:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 455.7 |
| 7d3a2820-a0a0-36b7-86b1-c09a32a59ccd | -6.2703 | -62.7301 | 2026-09-12 00:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 59.5 |
| a80b0985-b8b9-334e-85bd-c344f437b788 | -10.7015 | -54.1663 | 2026-09-12 00:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 235.5 |
| ccd65331-ad94-3b76-9685-9a72eb855d94 | -10.6829 | -54.1475 | 2026-09-12 00:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 76.1 |
| 9b46b86e-6ad2-3e0f-8b75-43cf5696429b | -2.7148 | -57.6274 | 2026-09-12 00:00:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 64.7 |
| 3d422966-dae6-32c6-ab9a-ae912a0952fe | -9.7134 | -64.945 | 2026-09-12 00:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 51.0 |
| daf7f428-bfc1-3947-89bf-781cb91eab39 | -6.9612 | -44.5316 | 2026-09-12 00:00:00 | GOES-19 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 81.0 |
| 3bc2729f-977c-369a-a78b-bb4f88199e9a | -10.6827 | -54.1679 | 2026-09-12 00:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 355.0 |
| 6284722e-ed64-399a-81ea-5498a6189eed | -5.7756 | -45.0826 | 2026-09-12 00:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 547.6 |
| 940b07c0-4e34-3cf7-994a-b24f275a4ca0 | -6.1845 | -57.72 | 2026-09-12 00:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 67.2 |
| b410add5-ee34-3fec-b29e-436f1b7c9ae4 | -9.7132 | -64.9825 | 2026-09-12 00:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 67.5 |
| 77aab80f-df73-3244-a3fd-55e949bcda01 | -12.8543 | -44.386 | 2026-09-12 00:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 50.7 |
| bb85e00b-f89c-30c3-9849-c1ed88072fc9 | -3.7462 | -61.7552 | 2026-09-12 00:00:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 68.0 |
| b9786ca6-5fe2-384b-88d1-f1e5abbea674 | -12.1501 | -64.1414 | 2026-09-12 00:00:00 | GOES-19 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 83.2 |
| 01a48937-44b8-3cb0-9c7f-fd01c72f72fe | -2.7331 | -57.6271 | 2026-09-12 00:00:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 76.8 |
| 42373267-8ce0-3b13-b001-da232c125533 | -5.7754 | -45.1053 | 2026-09-12 00:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 591.6 |
| 6463e18a-e85c-3eb0-adcc-aed4fa5092ae | -9.6947 | -64.9644 | 2026-09-12 00:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 54.6 |
| 3d488097-f168-392e-9ae8-40657183cf16 | -9.7319 | -64.9631 | 2026-09-12 00:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 58.7 |
| 4ea22681-c81a-347a-ab8f-34abbbf9f54c | -5.7941 | -45.104 | 2026-09-12 00:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 86.9 |
| 2fac05a1-555d-3b31-bcdd-7c7726eab0d2 | -6.2887 | -62.7296 | 2026-09-12 00:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 62.8 |
| 1e55346e-8eb8-3ef7-b83f-4c55bbba3d2d | -13.4157 | -42.4999 | 2026-09-12 00:00:00 | GOES-19 | BOTUPORÃ | BAHIA | Brasil | 2904209 | 29 | 33 | nan | nan | nan | Caatinga | 67.5 |
| 6e98e3bb-d0d6-31d2-a904-3e014f04a148 | -6.6021 | -58.849 | 2026-09-12 00:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 54.4 |
| 00ca7c35-dbcb-3f0f-8ad7-81de0b5ac945 | -5.8206 | -53.8052 | 2026-09-12 00:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 47.8 |
| a4e067e1-7bf4-370a-8251-0669404c8213 | -5.7943 | -45.0813 | 2026-09-12 00:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 76.5 |
| 5eae5248-6116-3a11-a3cf-b46d4f614fc4 | -2.7331 | -57.6465 | 2026-09-12 00:00:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 103.2 |
| 46a78a48-576a-33f2-877f-c06572a64062 | -6.961 | -44.5546 | 2026-09-12 00:00:00 | GOES-19 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 89.3 |
| 3362927f-5a37-3dde-a837-19afa030a344 | -6.2429 | -51.6939 | 2026-09-12 00:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 162.0 |
| 9b125d07-4796-31d8-98c3-ffe36bd8d658 | -6.2427 | -51.7146 | 2026-09-12 00:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 83.4 |
| d0d7e1e6-7456-3c45-b27d-93e899a0b13c | -3.2313 | -46.9596 | 2026-09-12 00:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 97.2 |
| d880e8f6-451c-3011-a53a-20ee3299de73 | -6.2243 | -51.6949 | 2026-09-12 00:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 87.5 |
| be66d66a-0dd0-329e-9248-04338101ff5c | -10.7018 | -54.1458 | 2026-09-12 00:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 51.1 |
| 697f6ffa-b734-3bf0-a06e-07f491a75c5e | -5.7567 | -45.1067 | 2026-09-12 00:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 478.4 |
| 017ef046-3a47-3bcc-9752-a8daac296b4a | -3.728 | -61.7555 | 2026-09-12 00:00:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 49.0 |
| cf63383e-f434-3ec8-840c-a3c13c5e5112 | -9.7133 | -64.9637 | 2026-09-12 00:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 108.6 |
| e9b2b395-83b9-3ac6-9b46-8108da67ac4e | -2.7148 | -57.6274 | 2026-09-12 00:10:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 68.1 |
| d2b18b7e-308c-3646-a06a-040699f9914f | -5.7941 | -45.104 | 2026-09-12 00:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 66.2 |
| 4a60d3e7-cfeb-3126-ba19-a915683ae244 | -2.7331 | -57.6271 | 2026-09-12 00:10:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 75.8 |
| d60f9bfb-89dc-3f39-abc1-6694bf046f6e | -6.2429 | -51.6939 | 2026-09-12 00:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 145.2 |
| b58e28c7-ca56-3bca-b143-48f9bf43f7d4 | -12.1501 | -64.1414 | 2026-09-12 00:10:00 | GOES-19 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 80.3 |
| 42edac35-cab3-3a37-8ee6-c0271828db01 | -7.2747 | -46.8036 | 2026-09-12 00:10:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 56.4 |
| b4e630c4-ed6a-3bd9-aafa-3be803e4e0a7 | -3.2313 | -46.9596 | 2026-09-12 00:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 96.2 |
| 695d072a-c7b7-397e-98cf-317cbee6151d | -12.8543 | -44.386 | 2026-09-12 00:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 56.4 |
| 95c6ea2b-ed84-35f7-b9b9-a3f0b883e23b | -6.2243 | -51.6949 | 2026-09-12 00:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 73.7 |
| 945eccf9-2ed0-31e7-8154-3c72e58bd1aa | -10.7015 | -54.1663 | 2026-09-12 00:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 211.0 |
| 9bc09af5-5f1f-3ec1-a599-6bdd42e38bdf | -6.2427 | -51.7146 | 2026-09-12 00:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 69.6 |
| 2291f205-4b13-3ddc-b6d4-e89f18ef8e8b | -9.7133 | -64.9637 | 2026-09-12 00:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 67.8 |
| a60f1c23-8cfa-30d2-abdb-2e636627caf7 | -6.961 | -44.5546 | 2026-09-12 00:10:00 | GOES-19 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 79.3 |
| ec441173-9bff-3781-8a9f-2c46c4d50d5f | -6.6206 | -58.8483 | 2026-09-12 00:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 65.0 |
| 04839453-32fc-34ef-b5c5-3d3eaa031d51 | -5.7943 | -45.0813 | 2026-09-12 00:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 60.9 |
| 6ceabfb9-a5ff-3b6e-84ac-b3d741a1a723 | -10.6829 | -54.1475 | 2026-09-12 00:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 86.6 |
| bac1bfbe-7da9-36a9-987e-d146c1e8597e | -6.9612 | -44.5316 | 2026-09-12 00:10:00 | GOES-19 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 65.7 |
| 44832104-acc2-3125-9b0f-5f77c74eb56d | -13.4162 | -42.4755 | 2026-09-12 00:10:00 | GOES-19 | BOTUPORÃ | BAHIA | Brasil | 2904209 | 29 | 33 | nan | nan | nan | Caatinga | 99.3 |
| 1c374be3-a3ea-382c-a4fe-40cf0b550282 | -3.7462 | -61.7552 | 2026-09-12 00:10:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 65.5 |
| 5db81605-63c1-323f-acf7-30d57b731773 | -2.7331 | -57.6465 | 2026-09-12 00:10:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 96.1 |
| 6c7cfb59-8db6-3ac3-84cf-1e4a334af5b4 | -10.7018 | -54.1458 | 2026-09-12 00:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 56.7 |
| f1832e8d-59cf-32a8-a036-244eeed3c6cf | -5.7756 | -45.0826 | 2026-09-12 00:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 543.1 |
| 0f8b60b0-8cba-3002-9883-ba09810f1d20 | -5.7567 | -45.1067 | 2026-09-12 00:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 379.9 |
| ced1b3e0-3eda-339d-9e7e-9b0c55e7a50e | -5.7569 | -45.084 | 2026-09-12 00:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 364.5 |
| 275b9e78-78ab-3444-a7b2-12fe2d74fe27 | -10.6827 | -54.1679 | 2026-09-12 00:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 312.9 |
| 7461ade3-5c5d-3ff8-8b82-d13ec7feb9d5 | -6.1845 | -57.72 | 2026-09-12 00:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 70.2 |
| b64dbed5-b796-3bf4-beb2-a98897a5b262 | -5.7754 | -45.1053 | 2026-09-12 00:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 595.5 |
| f00cf26d-92bb-3110-8e2d-6c8ac0e26925 | -10.69 | -54.2 | 2026-09-12 00:15:00 | MSG-03 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3ae362e9-5640-3587-be1a-efe380f277aa | -2.94 | -50.4 | 2026-09-12 00:15:00 | MSG-03 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1fa46c4a-21de-332f-98c2-c3380343787f | -2.97 | -50.35 | 2026-09-12 00:15:00 | MSG-03 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f83b395c-982c-3604-abac-bbb91948ee39 | -2.97 | -50.4 | 2026-09-12 00:15:00 | MSG-03 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3fd2a747-9e76-3fad-9b1b-8fcd61e0c3e8 | -5.76 | -45.14 | 2026-09-12 00:15:00 | MSG-03 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 24237a5c-b703-3e2e-b811-48c755dce564 | -5.79 | -45.1 | 2026-09-12 00:15:00 | MSG-03 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 83745693-ce6e-3e36-bf78-f498727e8e29 | -5.76 | -45.09 | 2026-09-12 00:15:00 | MSG-03 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 01c4c934-13e6-3bbb-b1df-9a03930bbc99 | -2.94 | -50.35 | 2026-09-12 00:15:00 | MSG-03 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 47cee73a-4a63-3994-b290-2b76b9ea2339 | -10.7018 | -54.1458 | 2026-09-12 00:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 121.4 |
| 04d9c844-3996-32bb-88fc-a9f140731021 | -6.2427 | -51.7146 | 2026-09-12 00:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 60.8 |
| 903a5cb3-db2f-3617-a437-b1a12495509f | -6.2243 | -51.6949 | 2026-09-12 00:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 79.1 |
| b9927fc0-bffd-327c-964d-064263914a65 | -6.2429 | -51.6939 | 2026-09-12 00:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 141.0 |
| 55460790-c789-3f08-8a19-7134ebd19dbf | -10.7013 | -54.1868 | 2026-09-12 00:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 60.3 |
| 9b14b518-77ce-3aa2-b488-d6bb03033415 | -9.6451 | -49.6817 | 2026-09-12 00:20:00 | GOES-19 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 60.4 |
| a3615d1e-8b17-3a69-8b14-e37afb35802e | -5.7569 | -45.084 | 2026-09-12 00:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 446.6 |
| 78b0501f-d858-369e-9ecf-1c5c81a036ff | -6.9612 | -44.5316 | 2026-09-12 00:20:00 | GOES-19 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 81.8 |
| 614107dc-a5ad-387f-b98b-709baf9090ad | -3.7462 | -61.7552 | 2026-09-12 00:20:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 61.0 |
| 050f3808-7c1d-3f24-8eda-3f7a819877a7 | -10.6829 | -54.1475 | 2026-09-12 00:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 80.2 |
| e273f2dc-174d-3be6-b7a3-caa2e03d2cd3 | -3.2313 | -46.9596 | 2026-09-12 00:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 119.8 |
| 358d79c6-3b06-370c-a0c8-db41c52936f7 | -13.4162 | -42.4755 | 2026-09-12 00:20:00 | GOES-19 | BOTUPORÃ | BAHIA | Brasil | 2904209 | 29 | 33 | nan | nan | nan | Caatinga | 84.1 |
| facb5a7d-e0c9-3a2a-a936-f234a9852be5 | -3.728 | -61.7555 | 2026-09-12 00:20:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 51.7 |
| 7d9b80af-f63d-30c0-bbe8-f8edf8b06efd | -6.6021 | -58.849 | 2026-09-12 00:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 59.6 |
| a8cb1189-d537-38bd-8b14-3cb0c8de3de8 | -5.7756 | -45.0826 | 2026-09-12 00:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 548.8 |
| ce208004-7ffb-35ab-889d-585ee6872e7b | -10.7015 | -54.1663 | 2026-09-12 00:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 312.3 |
| ce0f3709-db61-37d4-853f-80bbd022608a | -9.7133 | -64.9637 | 2026-09-12 00:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| d8a129a6-6407-3ca2-a572-84f6469e670c | -5.7941 | -45.104 | 2026-09-12 00:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 70.2 |
| e726299b-87ab-3ab4-8197-6d87fad443c8 | -6.961 | -44.5546 | 2026-09-12 00:20:00 | GOES-19 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 83.3 |
| e9b333fb-98e6-3c17-a7e9-cc5f8385690e | -5.7567 | -45.1067 | 2026-09-12 00:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 362.8 |
| f7a72aec-1469-3913-997f-592c87cc2f49 | -10.6827 | -54.1679 | 2026-09-12 00:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 204.0 |
| 6d002c1e-5d63-3057-9207-bb75163b3a3c | -2.7148 | -57.6274 | 2026-09-12 00:20:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 62.0 |
| 69cd60d5-c49a-39ba-9b7a-2767ab7df319 | -5.7943 | -45.0813 | 2026-09-12 00:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 79.9 |
| 1c2bdd82-8aab-30a4-b9ca-8710dc56f1c3 | -12.8543 | -44.386 | 2026-09-12 00:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 51.3 |
| eaa36bea-bd29-3d5b-b35d-7a3f3e478dc6 | -5.7754 | -45.1053 | 2026-09-12 00:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 466.2 |
| 889eb9c4-25d3-3504-8e85-aea4fe21823e | -2.7331 | -57.6271 | 2026-09-12 00:20:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 71.7 |
| 23a2b320-bab5-3a05-a457-5886dd817063 | -2.7331 | -57.6465 | 2026-09-12 00:20:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 104.4 |
| 44fd3d11-c0b8-33fe-9863-ad41bbf7e9f1 | -12.8543 | -44.386 | 2026-09-12 00:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 50.8 |
| dd5f6439-53eb-3a5c-b94c-69d657f431c9 | -2.7331 | -57.6465 | 2026-09-12 00:30:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 92.5 |


[Clique aqui para ver as próximas entradas](README2.md)
