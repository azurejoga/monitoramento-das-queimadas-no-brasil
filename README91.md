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

## Dados Diários - Página 91

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 593a1a18-d066-3a8f-a791-069aa8671db9 | -6.39087 | -54.88274 | 2026-09-23 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6c530792-e159-3ec5-9ad0-52ca7110cffd | -8.73205 | -47.59633 | 2026-09-23 05:04:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d3abe1f1-fd73-3bc8-8cca-87fb0df57e1a | -11.11248 | -51.05398 | 2026-09-23 05:04:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c13cfd94-719a-34d4-896b-e37c2aca0d42 | -6.8494 | -45.55541 | 2026-09-23 05:04:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 80da1917-2959-3282-9e51-ee2d86c818a8 | -6.63225 | -59.93734 | 2026-09-23 05:04:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 30.0 |
| 95ce5c2c-0806-3b3e-82b9-314563fe5ef0 | -6.00186 | -57.71194 | 2026-09-23 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9c555beb-2888-37e6-8137-d43307b4814f | -6.77663 | -59.62907 | 2026-09-23 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3b3c622b-f3ab-39a8-8ccd-4b9ff467cc2e | -3.78788 | -60.75048 | 2026-09-23 05:04:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3512f5ef-8898-3347-a3a4-bb2179b29125 | -5.60026 | -60.20344 | 2026-09-23 05:04:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 1e00be38-9b15-3f61-b6e7-699d8a35ebcc | -6.2585 | -55.43126 | 2026-09-23 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 15753ba6-a094-394d-8cd3-0723aa5b99e1 | -6.04456 | -52.77141 | 2026-09-23 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 59d78b5e-4190-3d70-a43a-1b009285548f | -11.67779 | -50.97739 | 2026-09-23 05:04:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d0f70cd0-c657-3519-8912-e3a0cbcf6f06 | -11.40363 | -44.02413 | 2026-09-23 05:04:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b570d9db-55ea-3536-82e4-3496b1504710 | -5.12832 | -46.05767 | 2026-09-23 05:04:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ac5d1b60-319d-312d-9e79-154d8a0da926 | -6.06444 | -57.8084 | 2026-09-23 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8d3f4739-b96e-352f-8baf-7f5c36df04e5 | -10.45198 | -46.27722 | 2026-09-23 05:04:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 010e8eaf-3e8c-3edb-8926-6bf4ce27505c | -6.7434 | -45.45201 | 2026-09-23 05:04:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| fbfd5e71-dfdb-3321-bafc-6491e9ea4caa | -8.37153 | -45.60571 | 2026-09-23 05:04:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 04cf0737-66ae-3eb8-824d-ff943d5c534a | -6.42665 | -59.99098 | 2026-09-23 05:04:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| faf255cc-d086-3591-8143-ee2640c6dd03 | -5.80357 | -49.15533 | 2026-09-23 05:04:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 93dbaf36-06f0-3a88-83de-13f1fefa170c | -11.75404 | -47.61929 | 2026-09-23 05:04:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| fa4d96f2-a263-3119-9d08-ad7468bb2368 | -6.30686 | -59.94493 | 2026-09-23 05:04:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b8fcaf9f-f8ce-365f-94c2-af441a2ddbf5 | -8.34553 | -50.86163 | 2026-09-23 05:04:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b4443200-52f2-367b-b9f8-144fbae9e17c | -7.60769 | -57.60958 | 2026-09-23 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ce2e8777-18bf-3b71-bfdf-25c6dd4c15f8 | -5.42244 | -60.24786 | 2026-09-23 05:04:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a892d680-5673-3c62-afe2-352b8dbfbf9a | -5.41342 | -60.2127 | 2026-09-23 05:04:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a7c90c7c-9c02-360b-a7e0-63d032167260 | -8.48816 | -44.75087 | 2026-09-23 05:04:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2ef57f28-1f24-3b6f-a28b-eebe3d3ac4a3 | -6.617 | -59.91409 | 2026-09-23 05:04:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 6.7 |
| fd946e4f-4456-34da-8583-2a2cfb8d9f45 | -5.21822 | -60.05154 | 2026-09-23 05:04:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d67d00bf-ce40-31da-9516-1c93fb39d5e0 | -6.6225 | -59.99239 | 2026-09-23 05:04:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e222191c-2df0-3067-9ea4-2fbcd21118ca | -7.49552 | -44.32458 | 2026-09-23 05:04:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 431e0fc8-145b-3434-a380-d688860e43f6 | -6.67289 | -55.05668 | 2026-09-23 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 98863e09-eeac-34a3-9d4f-1095b325f3f2 | -5.75625 | -45.11033 | 2026-09-23 05:04:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 5a7c43fe-2f66-3d43-b16d-baa19301bdb0 | -8.37829 | -45.59199 | 2026-09-23 05:04:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3ec891f1-6c7c-3005-ab7a-d0eed94790f2 | -9.28551 | -50.32733 | 2026-09-23 05:04:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8a01f13a-be9a-3376-8cdf-236cbb5e2734 | -7.33272 | -55.59358 | 2026-09-23 05:04:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dae0f671-ca62-3298-a324-f259fdc4d438 | -4.54171 | -54.9366 | 2026-09-23 05:04:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5d2e6b66-4eba-316f-8b24-b89e8d61a342 | -5.41831 | -60.21354 | 2026-09-23 05:04:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f07131af-9edb-37cd-996e-ddf449a07f3a | -8.1148 | -48.23581 | 2026-09-23 05:04:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 15075b5b-0bf3-3708-bef2-13bca2377d92 | -11.12015 | -51.05106 | 2026-09-23 05:04:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cfd41966-41c3-344e-b5f2-1a476a4c38fd | -3.90077 | -60.58842 | 2026-09-23 05:04:00 | NPP-375D | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b3b9af6b-3cb9-3f6d-8624-428f964bae20 | -9.92506 | -48.47659 | 2026-09-23 05:04:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b401c781-7043-387d-9b76-e08c3dc14a5d | -6.89642 | -46.56768 | 2026-09-23 05:04:00 | NPP-375D | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 193d1886-7f1a-3280-9680-7dab6a4895bd | -6.66751 | -58.55413 | 2026-09-23 05:04:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 23328e4e-cab6-37f1-8a07-91d6c7f29a64 | -6.30854 | -57.74184 | 2026-09-23 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 96c41eef-91d1-3194-8949-e8bcfbd5445c | -10.16405 | -47.67244 | 2026-09-23 05:04:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 43245adc-cd00-3476-af85-e69029f75ca9 | -11.78081 | -50.98316 | 2026-09-23 05:04:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 79d3732d-4472-3d59-82cf-04655e48ecf2 | -6.67684 | -50.94985 | 2026-09-23 05:04:00 | NPP-375D | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d732c2eb-22d0-3450-94e2-ce0fac79d0c4 | -11.34998 | -43.37474 | 2026-09-23 05:04:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8be18a51-4adc-3d1b-aa9d-5d92ed9f8042 | -3.68658 | -60.58704 | 2026-09-23 05:04:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 15536934-8289-3bc7-bdfe-50c92329ff30 | -8.83715 | -50.48865 | 2026-09-23 05:04:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 77b4eafd-c6f3-38a1-9dea-2681a218670f | -3.68501 | -60.56472 | 2026-09-23 05:04:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 4913c2dc-fdce-34d8-92a4-39d9a6952833 | -5.74459 | -51.93025 | 2026-09-23 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fc7e4746-a33d-3e9f-a2df-47341e3e6082 | -8.28105 | -54.76506 | 2026-09-23 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2cc67221-5619-3003-896d-c619662347f0 | -9.97315 | -50.25318 | 2026-09-23 05:04:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ec7f6744-080e-315e-a61c-d5690f2974c4 | -5.62036 | -43.36132 | 2026-09-23 05:04:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f88c860f-9bdf-3e82-b178-e216c1f85827 | -8.91124 | -50.90509 | 2026-09-23 05:04:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fb93f9aa-ad01-32f8-b0d3-feaca1b11abf | -6.60492 | -43.7469 | 2026-09-23 05:04:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 26397709-5b06-35e0-86e5-51b72dddc93b | -8.32835 | -50.82795 | 2026-09-23 05:04:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6b247db8-1a4b-3303-8107-9e69d8f59dbf | -8.48589 | -46.86874 | 2026-09-23 05:04:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a67942cb-cebf-3653-9a0f-602718595416 | -3.9049 | -60.5954 | 2026-09-23 05:04:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 0efdfb06-fcca-319a-91f7-63ad90cc2f44 | -6.15924 | -57.71144 | 2026-09-23 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c72f963d-b0e1-3777-806f-1a5d94af8d1e | -4.34084 | -55.65429 | 2026-09-23 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2f68b46b-1273-316d-bc6d-edea56c37677 | -10.70594 | -48.71552 | 2026-09-23 05:04:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 2bb6170b-8d0c-3865-9e2d-d97ad5d7bf6c | -5.81398 | -57.73672 | 2026-09-23 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ce45174a-197b-30c6-b1f5-afdbcdcd8440 | -11.68813 | -43.4494 | 2026-09-23 05:04:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ba174276-9b3e-3a21-8b92-ce2d074a8dfc | -11.46535 | -47.37693 | 2026-09-23 05:04:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| b95c7920-f865-3c08-a2b0-6e349947dafe | -11.47693 | -47.35815 | 2026-09-23 05:04:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b9383fe9-f300-34ba-8bc8-57545ccab574 | -11.44612 | -46.72789 | 2026-09-23 05:04:00 | NPP-375D | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9f86ede9-9292-3337-8514-3a3b25f3cb08 | -5.45573 | -60.14236 | 2026-09-23 05:04:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 81112d82-0899-3d71-b652-dbc2fd83d6dd | -5.87899 | -52.12657 | 2026-09-23 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 46224877-40de-39da-b5ed-95b93c43caab | -5.6529 | -60.21817 | 2026-09-23 05:04:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| cb1300d3-dc4e-32da-b0c9-62f7aca905c7 | -3.60861 | -60.57689 | 2026-09-23 05:04:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1376ef6e-af57-39bb-a5cb-1144a23de327 | -6.74388 | -55.08811 | 2026-09-23 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5ceb759e-ddb6-3e05-b21a-b98504bba75d | -6.96957 | -42.59963 | 2026-09-23 05:04:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 6bbae7c7-0576-3271-8f36-13134fe8a56c | -6.73909 | -55.09543 | 2026-09-23 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 73b6f1ce-1180-368f-99f5-a77cc5990eb0 | -6.66877 | -55.05995 | 2026-09-23 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| b75f214b-5c13-3488-a501-ab90489832c9 | -6.09068 | -55.56828 | 2026-09-23 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c1b16b40-e3f5-3ed9-a0d6-f32cc0f289aa | -6.1606 | -59.94371 | 2026-09-23 05:04:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 34b11d0f-b874-32cb-bc92-1ec868a7195e | -6.19378 | -57.78065 | 2026-09-23 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1bcf92a8-d7af-3ac8-abc4-c82ad81850da | -11.65006 | -50.95289 | 2026-09-23 05:04:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0b47eab2-183c-34bc-ab11-4dba555d641f | -6.03816 | -53.27507 | 2026-09-23 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 55145481-cf94-3e5b-a0c4-d7b4cd9b49d8 | -5.19671 | -50.08861 | 2026-09-23 05:04:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1b7fd68b-b04e-36d9-9409-ebbc395230d8 | -6.78011 | -59.63181 | 2026-09-23 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 38f27081-a41e-3804-86de-8f91611309e4 | -3.39313 | -61.06085 | 2026-09-23 05:04:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a9a06df7-277d-30ec-8484-fc4b1a5d6004 | -6.58072 | -44.14547 | 2026-09-23 05:04:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 02aabd92-c114-3d65-b358-944340653896 | -8.36678 | -45.60487 | 2026-09-23 05:04:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 227f3759-070c-3dd0-bf00-3ea8e262db11 | -11.1231 | -51.05561 | 2026-09-23 05:04:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cd4ecf3b-0e36-398f-845c-381302bdf20a | -5.88811 | -52.28461 | 2026-09-23 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ad2437da-fee6-3a36-9b61-6ae5365e91a3 | -3.20492 | -61.06863 | 2026-09-23 05:04:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d2096b97-15f6-3ebe-af4a-829f5930b50b | -11.63504 | -50.97991 | 2026-09-23 05:04:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 820af3d4-821b-377e-85dd-6daabbb0a2d8 | -6.13908 | -43.83865 | 2026-09-23 05:04:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 38266c4a-4ad2-3cde-8c13-219e0f93a1a7 | -8.80772 | -44.27737 | 2026-09-23 05:04:00 | NPP-375D | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b62b4421-2204-3696-9e3c-07435b80d67e | -8.45933 | -48.68938 | 2026-09-23 05:04:00 | NPP-375D | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 22.1 |
| a7a68224-1167-3291-822f-881280b6e464 | -6.68627 | -55.06287 | 2026-09-23 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6c2b6400-e483-347b-9a81-dc1b6620fe5c | -6.65923 | -50.88296 | 2026-09-23 05:04:00 | NPP-375D | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1d1daf35-ed58-39f6-8fc4-43a31b72c8f7 | -3.5433 | -62.07745 | 2026-09-23 05:04:00 | NPP-375D | CODAJÁS | AMAZONAS | Brasil | 1301308 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cd2f1a99-7fdf-3380-a60c-0162ac3936e2 | -6.67228 | -55.06049 | 2026-09-23 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 25d6f5c1-5a8c-3f07-b04d-e7c0d0291fc6 | -6.75024 | -55.09319 | 2026-09-23 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| aa24675d-751e-3aee-ab5b-49dcf3f4fd41 | -3.60701 | -60.57902 | 2026-09-23 05:04:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |


[Clique aqui para ver as próximas entradas](README92.md)
