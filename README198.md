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

## Dados Diários - Página 198

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5a44f17b-5daa-300e-9746-ad01e650458f | -6.3618 | -55.8632 | 2026-08-31 19:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 86.0 |
| c930f88d-a31d-3b56-97c4-ef8d7508c20f | -11.1809 | -55.0821 | 2026-08-31 19:30:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 75.3 |
| 8f1aa396-41dd-39c9-aac1-edeca74c912d | -11.6972 | -54.5672 | 2026-08-31 19:30:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 61.9 |
| 8bb5422a-8bff-3f0e-975b-23d2afcb033d | -9.1709 | -59.6374 | 2026-08-31 19:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 54.6 |
| 0896ca7e-b13a-3985-a0a1-25c97b1b9596 | -5.9451 | -57.6906 | 2026-08-31 19:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 109.4 |
| bb8a928a-b8ca-338b-a858-65ca222e3cd2 | -14.1263 | -52.8106 | 2026-08-31 19:30:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 134.2 |
| 3f9a3ada-24bd-3e4a-8ac7-77657614989a | -11.0744 | -51.5365 | 2026-08-31 19:30:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 92.7 |
| 5afd1e8d-2d0a-3d5c-bad7-e8ffc7078445 | -15.015 | -52.7599 | 2026-08-31 19:30:00 | GOES-19 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 82.1 |
| 4b062de9-6966-39fe-8be6-d069511f3dd4 | -11.478 | -45.0868 | 2026-08-31 19:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 98.3 |
| 1efab804-f733-3692-a5d4-c26cda98aef9 | -6.4054 | -49.9441 | 2026-08-31 19:30:00 | GOES-19 | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 96b41e78-ab56-3c17-be6a-353e10c2d1c2 | -14.6335 | -53.6086 | 2026-08-31 19:30:00 | GOES-19 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 84.6 |
| 65b60464-f822-3771-b46b-c69299c67795 | -9.862 | -64.9771 | 2026-08-31 19:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 46.8 |
| cc86c7d9-a25e-31fc-bd42-df12149f3f01 | -9.5716 | -60.8319 | 2026-08-31 19:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 42.6 |
| cd1ed39e-0b7b-3705-beee-c8cada33f9f4 | -11.0747 | -51.5153 | 2026-08-31 19:30:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 109.0 |
| 4c5fe1dc-f116-397f-bfcf-423da7a604ce | -9.4906 | -57.0342 | 2026-08-31 19:30:00 | GOES-19 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 59.3 |
| 66cfa4e3-b0bf-38b3-ad14-8b232bf6d55a | -9.4719 | -57.0354 | 2026-08-31 19:30:00 | GOES-19 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 86.2 |
| 5fa40f33-630c-3191-bdc6-12faeb7a150b | -11.0933 | -51.5345 | 2026-08-31 19:30:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 230.0 |
| b74d38f6-af51-3ab7-b0b0-be913eb0f960 | -15.0244 | -48.1689 | 2026-08-31 19:30:00 | GOES-19 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 89.7 |
| b9ba8133-39c1-313c-ad03-95a96485dc3c | -8.6852 | -62.9496 | 2026-08-31 19:30:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 48.9 |
| fa58a26c-fd11-3c7f-9019-128dd511be12 | -5.4876 | -57.1416 | 2026-08-31 19:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 48.8 |
| 6d1fd02b-6bf0-3399-a1da-dfd6accb8150 | -14.1456 | -52.8082 | 2026-08-31 19:30:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 82.0 |
| fd9c4fc3-d67c-3f61-ab96-8fc62e47af5f | -10.2743 | -64.4907 | 2026-08-31 19:30:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 56.1 |
| c7049ff8-cc4a-32ed-a13a-cab80849cf10 | -6.137 | -53.5259 | 2026-08-31 19:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 51.3 |
| 991630d4-01e3-3b20-8198-08e67b766385 | -11.7973 | -47.6672 | 2026-08-31 19:30:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 94.7 |
| 5ae401f2-a166-32f5-b473-c701bd042f28 | -8.4988 | -55.3252 | 2026-08-31 19:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 59.1 |
| abd9efb7-0941-3592-9a0d-2a167cc604d0 | -5.9635 | -57.6899 | 2026-08-31 19:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 113.0 |
| 952f1641-d6fb-3045-9ed5-885a613cdc65 | -12.0733 | -44.999 | 2026-08-31 19:30:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 207.3 |
| 51accec8-d261-374d-a6ea-956dd6c42cc6 | -14.4831 | -52.2151 | 2026-08-31 19:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 146.3 |
| 25c1b9db-47ee-3705-965c-55ebbabd9dd1 | -16.0348 | -54.4143 | 2026-08-31 19:30:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 136.9 |
| 5c9751d9-afb7-3c39-9bb1-815bf4c5b3e8 | -10.7405 | -54.0606 | 2026-08-31 19:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 71.9 |
| 1ea4a324-8148-31df-aa5c-73acfd65141a | -16.5577 | -52.5219 | 2026-08-31 19:30:00 | GOES-19 | DOVERLÂNDIA | GOIÁS | Brasil | 5207253 | 52 | 33 | nan | nan | nan | Cerrado | 226.1 |
| 983ffb12-d546-3499-85e5-637129419a5c | -6.2537 | -55.4308 | 2026-08-31 19:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 57.3 |
| a4240b5f-499c-3fbd-8ba7-981b7e2849d1 | -13.9282 | -54.42 | 2026-08-31 19:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 60.4 |
| 3cd3190b-62f0-37f7-881d-66c4a7cab31d | -9.6939 | -65.1145 | 2026-08-31 19:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 59.6 |
| 763c43ce-2454-39a6-8a1c-12918db41b6a | -8.8706 | -66.7636 | 2026-08-31 19:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 167.6 |
| c52c1b47-cc52-38fe-8f51-eb0b847d04a8 | -14.6338 | -53.5876 | 2026-08-31 19:30:00 | GOES-19 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 100.3 |
| 4e4ff451-ce99-3c29-8e4e-13158bea79b0 | -15.8844 | -56.4819 | 2026-08-31 19:30:00 | GOES-19 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 80.2 |
| 027bbe57-b9da-3a4a-8664-dd34d49032c3 | -12.0929 | -44.9728 | 2026-08-31 19:30:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 69.1 |
| 651b56c9-c3ea-3d54-9573-2f44f0f6cc30 | -18.2704 | -52.6851 | 2026-08-31 19:30:00 | GOES-19 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 295.4 |
| 4489e7d9-92eb-31da-9793-68581f004299 | -6.6233 | -58.383 | 2026-08-31 19:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 102.1 |
| 3fad49ca-76c4-3eff-8f61-02ba026ff7d4 | -7.0703 | -52.7175 | 2026-08-31 19:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 83.8 |
| 76bcc876-3579-3d08-8210-8f4fffd957ce | -7.4369 | -73.2446 | 2026-08-31 19:40:00 | GOES-19 | MÂNCIO LIMA | ACRE | Brasil | 1200336 | 12 | 33 | nan | nan | nan | Amazônia | 64.0 |
| 697d0218-b5d9-3fcd-9da8-1556e8fead4b | -17.3228 | -42.6878 | 2026-08-31 19:40:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 276.1 |
| 85ff3d40-da89-3186-aaac-a7879c9e9ec9 | -3.4002 | -61.3465 | 2026-08-31 19:40:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 56.8 |
| c9fc8944-e116-39fe-bc50-a034dd0d3d4f | -5.9635 | -57.6899 | 2026-08-31 19:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 114.5 |
| a5cffd76-37db-366d-8bea-15e870eb1da4 | -11.478 | -45.0868 | 2026-08-31 19:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 125.6 |
| fdb13481-5a7f-3b4f-b9ca-e938aff29a7b | -3.4185 | -61.3273 | 2026-08-31 19:40:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 74.0 |
| 05c45cc9-d789-31d5-945c-3f87aa8dbf91 | -9.1897 | -59.6171 | 2026-08-31 19:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 68.2 |
| e4a7f382-a079-3660-a104-e2701933d41c | -16.5577 | -52.5219 | 2026-08-31 19:40:00 | GOES-19 | DOVERLÂNDIA | GOIÁS | Brasil | 5207253 | 52 | 33 | nan | nan | nan | Cerrado | 87.6 |
| 93262c34-d3c7-34af-bde6-8eda69080555 | -5.9636 | -57.6704 | 2026-08-31 19:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 83.5 |
| 9d04a556-328c-3cbf-8647-4d2b0816ae68 | -10.2743 | -64.4907 | 2026-08-31 19:40:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 62.7 |
| 40b4bd87-5a2e-3f9a-9d53-4740dad4fe94 | -6.1109 | -57.684 | 2026-08-31 19:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 67.6 |
| 2d45edb4-41f6-3e91-8ccb-d8877f03f9d3 | -12.0925 | -44.996 | 2026-08-31 19:40:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 136.9 |
| 784d7fa0-152e-32eb-b932-0b4e59961da0 | -10.7405 | -54.0606 | 2026-08-31 19:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 97.1 |
| a7fc99d1-c3d7-3cdb-a4fc-bb1bf5282f15 | -11.5283 | -45.4933 | 2026-08-31 19:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 98.2 |
| 1416a75f-a4c1-3adc-9480-f9b46389d928 | -7.6251 | -55.2987 | 2026-08-31 19:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 237.2 |
| 6bf945f2-39fe-3cb7-9808-3d8d94f74424 | -7.685 | -63.3255 | 2026-08-31 19:40:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 46.4 |
| 63113df1-7f88-3593-adb2-e23914203131 | -3.6076 | -59.0769 | 2026-08-31 19:40:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 88.0 |
| 7f0c3b98-281c-3b74-9ff6-25016a13f142 | -10.1321 | -45.8825 | 2026-08-31 19:40:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 332.3 |
| 905df5f5-e485-3824-bafe-057c831b736c | -10.382 | -48.2376 | 2026-08-31 19:40:00 | GOES-19 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 132.6 |
| 3b5adbf4-d454-3de9-99a5-41f4b240cec2 | -10.1324 | -45.8598 | 2026-08-31 19:40:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 265.7 |
| 0a543dd8-7527-3ab3-aa4e-453648772280 | -7.492 | -61.3839 | 2026-08-31 19:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 54.5 |
| 6680d93e-30fa-3562-935a-6eb74f146524 | -10.1341 | -45.7461 | 2026-08-31 19:40:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 195.5 |
| c026f13f-6e5e-35b3-a039-248b4b5c4708 | -7.9048 | -44.2577 | 2026-08-31 19:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 59.3 |
| 401bab8c-469e-386b-a518-7dc6bb2a1d1e | -9.2086 | -59.5773 | 2026-08-31 19:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 63.0 |
| 07f77810-70ab-32d8-81e1-01439452ed46 | -13.5729 | -55.1382 | 2026-08-31 19:40:00 | GOES-19 | SORRISO | MATO GROSSO | Brasil | 5107925 | 51 | 33 | nan | nan | nan | Cerrado | 72.6 |
| b6f68744-9e93-32bf-9caf-286ce435b541 | -7.0292 | -55.6511 | 2026-08-31 19:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 110.6 |
| f1b2d5b6-e390-35bd-9df9-cc98bfae2db9 | -4.9788 | -55.8417 | 2026-08-31 19:40:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 79.8 |
| e1dee42d-3df6-39fe-a0a9-601f7dd4839e | -4.7941 | -55.967 | 2026-08-31 19:40:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 88.8 |
| 166435fe-6319-3b67-ae7a-314bd1d31a0d | -11.4972 | -45.084 | 2026-08-31 19:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 123.9 |
| 9dc1b056-8638-32c1-a507-f26e58884bb4 | -12.9589 | -45.944 | 2026-08-31 19:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 64.1 |
| 7f58bccc-e27b-35bc-a669-27046d8d2507 | -16.0352 | -54.3933 | 2026-08-31 19:40:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 135.5 |
| 14d9e464-4f0b-3671-829a-72e2aa60745d | -15.6336 | -56.3876 | 2026-08-31 19:40:00 | GOES-19 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 77.9 |
| aef35e37-f0ab-3140-84df-b37968451186 | -6.8569 | -59.4564 | 2026-08-31 19:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 50.9 |
| b1084ecf-bbff-3153-8056-3dcb76fafb61 | -4.9603 | -55.8622 | 2026-08-31 19:40:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 59.0 |
| 740e1120-ba82-331a-8543-700e7e707ed3 | -15.9703 | -55.9583 | 2026-08-31 19:40:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 71.7 |
| 0593b895-fcfe-313d-977f-c288d1054442 | -7.917 | -61.3481 | 2026-08-31 19:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 59.0 |
| 22ca7181-f91e-3b8d-b55a-490a871f1f87 | -13.471 | -57.0373 | 2026-08-31 19:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 77.3 |
| 5117e899-8d8a-31ec-aa55-55662feb4acd | -10.5906 | -57.4936 | 2026-08-31 19:40:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 61.0 |
| 0a056553-683c-321c-ae55-c26833db1c6c | -9.1901 | -59.5589 | 2026-08-31 19:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 60.8 |
| e41811e4-686d-3186-9b07-888c7fdcc837 | -3.6399 | -60.5466 | 2026-08-31 19:40:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 58.9 |
| 0fe01d84-5413-3bf5-a278-3f561429d4ba | -10.7407 | -54.0401 | 2026-08-31 19:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 223.5 |
| 9df239bc-aa06-3624-a1e9-e32ef962a209 | -6.9368 | -55.6161 | 2026-08-31 19:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 73.6 |
| eea044b4-4f12-31bb-b174-5d3b8b614f01 | -11.0936 | -51.5134 | 2026-08-31 19:40:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 298.3 |
| f9830862-6b15-3885-bbc1-b9b78ec7a054 | -14.1456 | -52.8082 | 2026-08-31 19:40:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 82.9 |
| d3d59bad-9941-3200-a76b-2e897fa1bc91 | -10.7598 | -54.0179 | 2026-08-31 19:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 86.9 |
| 22c850aa-e10b-3a27-81b3-bc37f090565f | -14.1459 | -52.7871 | 2026-08-31 19:40:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 75.6 |
| e8d4faf2-adc9-3976-94f3-95a86bfec6ce | -8.8706 | -66.7636 | 2026-08-31 19:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 206.6 |
| 495b6b82-9fff-361c-9d58-b8bbd326b998 | -3.6215 | -60.566 | 2026-08-31 19:40:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 241.3 |
| cdf12897-98c1-3fda-bafa-e18a5491f021 | -2.7119 | -47.043 | 2026-08-31 19:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 60.5 |
| 5224e2b0-75c3-3c74-a91b-146c78f54a70 | -11.4776 | -45.1099 | 2026-08-31 19:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 84.1 |
| 1b50f688-9c93-321a-8fbd-7b96a5b33672 | -8.6674 | -62.8179 | 2026-08-31 19:40:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 61.7 |
| ff65fd72-f76d-3e08-bc8e-207f05ed060e | -7.6149 | -44.8833 | 2026-08-31 19:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 80.0 |
| 9027c57e-af93-31f7-818e-1af9025f854d | -5.8879 | -52.0652 | 2026-08-31 19:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 53.7 |
| 9b1b962a-48f3-3833-8b4f-b5c291a99bff | -17.3027 | -42.6926 | 2026-08-31 19:40:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 73.8 |
| 2aa643c1-46a0-3d1e-a140-7d55460b158b | -5.8537 | -57.5576 | 2026-08-31 19:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 92.2 |
| e5be8f5e-be33-33ea-a471-a838656b9edb | -12.9225 | -45.8352 | 2026-08-31 19:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 66.5 |
| fa6a39b6-a77d-3c17-95ae-283e4b1fc69a | -2.7304 | -47.0424 | 2026-08-31 19:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 57.4 |
| 5268eb79-4b0a-3827-bbb6-fd823ebee3ac | -3.3871 | -59.3883 | 2026-08-31 19:40:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 67.1 |
| 5d12fa5d-5844-30a7-b3ff-90606b8ecc1a | -6.3877 | -54.7445 | 2026-08-31 19:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 67.3 |


[Clique aqui para ver as próximas entradas](README199.md)
