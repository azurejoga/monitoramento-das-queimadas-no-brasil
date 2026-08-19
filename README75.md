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

## Dados Diários - Página 75

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4a56ef43-a957-3500-bb27-0365168ce3c0 | -8.503 | -54.8625 | 2026-08-19 13:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 64.1 |
| f13dfbaf-de20-3eb9-879d-5b395a1aa5f3 | -5.9272 | -49.2719 | 2026-08-19 13:20:00 | GOES-19 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 102.8 |
| 821cc38d-e835-3891-8b2e-cb7dedeb642d | -15.3838 | -52.7315 | 2026-08-19 13:20:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 158.8 |
| 5dcd7478-354d-32c0-838b-1e4b8b6c94fa | -11.9319 | -49.9914 | 2026-08-19 13:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 82.9 |
| 8598b40b-c41c-3fb5-bc01-15ca6e89ed79 | -11.4036 | -47.2511 | 2026-08-19 13:20:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 80.8 |
| b08771b7-528c-3876-83bd-528ce207b64d | -11.0431 | -51.0535 | 2026-08-19 13:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 122.1 |
| fb31d528-818c-3f57-b225-77e38468f027 | -14.2021 | -52.8854 | 2026-08-19 13:20:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 70.2 |
| 1f7a7531-b003-304a-a651-b40a44096d8c | -16.5374 | -54.6831 | 2026-08-19 13:20:00 | GOES-19 | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 87.8 |
| 713dcc8e-ea98-3dc3-b8af-54c472731088 | -15.1879 | -52.8427 | 2026-08-19 13:30:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 106.2 |
| dff802e5-9b90-3a5c-b411-d5c27981c388 | -6.073 | -45.2873 | 2026-08-19 13:30:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 71.7 |
| e59938a4-8444-374f-8f90-d37202fb5767 | -9.4366 | -48.2955 | 2026-08-19 13:30:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 73.3 |
| 007c7a0f-90a4-351d-a121-4ddb4b507139 | -5.9088 | -49.2517 | 2026-08-19 13:30:00 | GOES-19 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 62.6 |
| e886fc7d-c29b-389f-8132-4d9e49ca9f52 | -11.404 | -47.2287 | 2026-08-19 13:30:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 91.2 |
| 83bd66c6-da4b-3755-8f35-fa5b4064bc54 | -5.4317 | -48.4212 | 2026-08-19 13:30:00 | GOES-19 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 94.9 |
| e12961e2-6452-3c96-a3cb-52dade652950 | -5.9086 | -49.273 | 2026-08-19 13:30:00 | GOES-19 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 74.5 |
| 1252fe5d-8b03-3aad-8cd6-6f5de7078080 | -8.9938 | -50.7004 | 2026-08-19 13:30:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 74.1 |
| a6390d8d-5892-33ed-9fd6-75391af01893 | -7.6171 | -49.9226 | 2026-08-19 13:30:00 | GOES-19 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 66.3 |
| 895065b1-f048-36a4-8131-580d4e0d4154 | -15.3834 | -52.7528 | 2026-08-19 13:30:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 97.5 |
| 2ec2632f-5337-3020-a2b5-40d8e6e779f7 | -15.2073 | -52.8401 | 2026-08-19 13:30:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 64.6 |
| 3da571a5-50d9-3422-ba5d-3f9bf1b8d07d | -16.5374 | -54.6831 | 2026-08-19 13:30:00 | GOES-19 | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 128.0 |
| 20272c81-62a0-3d84-8927-d56229339e63 | -14.2763 | -51.902 | 2026-08-19 13:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 83.3 |
| 88ad98cd-84d6-3a8b-97e5-9c144bcb21e6 | -11.0431 | -51.0535 | 2026-08-19 13:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 192.6 |
| 957a07d1-81b3-3f15-b525-76bf4163e5eb | -11.4036 | -47.2511 | 2026-08-19 13:30:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 104.4 |
| de3f5a77-8de7-3115-94c0-d90e92dec4c2 | -11.9961 | -53.4475 | 2026-08-19 13:30:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 69.5 |
| ac7b1b3e-f264-38bc-81fe-b7827c8f7ccf | -15.3838 | -52.7315 | 2026-08-19 13:30:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 178.7 |
| 1ec8c774-f9b5-32d8-b747-708e2ad83c36 | -6.0912 | -57.9187 | 2026-08-19 13:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 117.0 |
| 8205cd5e-b871-3304-9ac8-656b994a18d6 | -5.9274 | -49.2505 | 2026-08-19 13:30:00 | GOES-19 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 76.3 |
| 22bb26ef-3475-30d9-ab34-476899ed1956 | -6.3909 | -51.7475 | 2026-08-19 13:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 61.6 |
| 11956596-7755-39ae-be95-b7451b908c5f | -8.503 | -54.8625 | 2026-08-19 13:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 110.2 |
| aa5a2dba-03e6-3c48-8bdc-609eaefcc7cf | -9.1078 | -46.046 | 2026-08-19 13:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 69.4 |
| 8bd7a7b5-ae6f-3268-b641-43e83aa541ea | -8.3688 | -46.3473 | 2026-08-19 13:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 79.8 |
| cba0016c-fece-3577-8760-bac4d8ec6c4e | -5.9272 | -49.2719 | 2026-08-19 13:30:00 | GOES-19 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 88.5 |
| 19a2bcef-facf-38e3-a8db-bbc7b0189f4a | -7.6171 | -49.9226 | 2026-08-19 13:40:00 | GOES-19 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 72.5 |
| 707c3c6b-4d7a-3bec-8f2d-576a389500ab | -11.9961 | -53.4475 | 2026-08-19 13:40:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 70.3 |
| ae18166a-b832-357d-88c4-61a0bd11fafd | -14.5272 | -53.0341 | 2026-08-19 13:40:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 77.2 |
| 6c32d62b-3df6-354a-a0ef-5c5d76339407 | -14.2763 | -51.902 | 2026-08-19 13:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 100.1 |
| ecb0e4cd-1623-333c-bd86-9e2900d4d95b | -9.7537 | -43.2962 | 2026-08-19 13:40:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 77.4 |
| a256a124-bd3a-3d0e-b4b3-e4820f0378ac | -13.5862 | -51.7568 | 2026-08-19 13:40:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 71.9 |
| 2c55e778-86b2-369c-8274-b139896e4d8e | -11.0431 | -51.0535 | 2026-08-19 13:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 141.1 |
| 4d528a0d-6656-3ac5-b8cb-0b56c4bf02a2 | -8.3688 | -46.3473 | 2026-08-19 13:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 74.9 |
| d481f7c0-884d-36ef-8838-67e46a487dfa | -16.5178 | -54.6857 | 2026-08-19 13:40:00 | GOES-19 | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 96.8 |
| 68cbac3d-e421-328b-9922-d6f937387881 | -15.3838 | -52.7315 | 2026-08-19 13:40:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 80.7 |
| 4abf2b08-bf9d-3bf3-a27e-cefd0dcfd0d8 | -8.503 | -54.8625 | 2026-08-19 13:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 94.6 |
| 24cd96c2-7670-33f1-b0e2-61b09fb5ca0b | -14.4704 | -51.8337 | 2026-08-19 13:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 64.9 |
| 8a402d56-e830-3c4e-b845-d5ffefacc148 | -15.1875 | -52.8639 | 2026-08-19 13:40:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 71.6 |
| b83383df-7462-370a-91da-09accfe8fcc4 | -3.1278 | -60.6889 | 2026-08-19 13:40:00 | GOES-19 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 97.3 |
| ff394632-877a-358d-a562-fcae502ed04c | -11.4036 | -47.2511 | 2026-08-19 13:40:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 117.8 |
| 2a5f0f3f-39da-3a38-a3b2-694816d9cff4 | -14.2017 | -52.9065 | 2026-08-19 13:40:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 97.4 |
| d9564f64-bad6-3fa2-8e4d-1259832d703c | -15.2073 | -52.8401 | 2026-08-19 13:40:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 79.7 |
| d870f3b1-5b02-34db-aa61-15d7693d0dfe | -5.9274 | -49.2505 | 2026-08-19 13:40:00 | GOES-19 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 81.1 |
| 6c37e767-92af-3ea1-9650-bb84372fd118 | -14.221 | -52.9041 | 2026-08-19 13:40:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 293.7 |
| eba91a88-becd-3987-96fa-bd517bbb8a22 | -5.9088 | -49.2517 | 2026-08-19 13:40:00 | GOES-19 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 67.9 |
| 2e42d7f2-da97-3069-8c80-2b7b53c8775f | -13.5858 | -51.7781 | 2026-08-19 13:40:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 137.3 |
| 902938d3-c51c-3388-a324-6fe100050be9 | -6.0912 | -57.9187 | 2026-08-19 13:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 115.4 |
| 7d6bc2cf-77e9-3a8e-a902-efae7788c250 | -11.8911 | -50.1686 | 2026-08-19 13:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 143.4 |
| afc0501c-f5e3-34a6-abb0-f2b9003080da | -9.7533 | -43.3199 | 2026-08-19 13:40:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 78.4 |
| ddccc0c5-b16e-312f-ab95-9e7c4d528711 | -5.4317 | -48.4212 | 2026-08-19 13:40:00 | GOES-19 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 77.0 |
| f7e46c36-94a7-31f9-81ca-9c7000014436 | -11.404 | -47.2287 | 2026-08-19 13:40:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 77.1 |
| 68b7f002-99b6-315b-9a96-0b5adfe48075 | -6.073 | -45.2873 | 2026-08-19 13:40:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 59.5 |
| fab029a9-4640-3d45-8ce5-90db9d8bf862 | -14.2956 | -51.8995 | 2026-08-19 13:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 80.5 |
| 2293dd13-24d1-3d7c-b0b0-765f9c9beee7 | -16.5374 | -54.6831 | 2026-08-19 13:40:00 | GOES-19 | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 151.8 |
| 4e662b2c-adeb-3722-90fe-3a3ca83184fd | -15.1879 | -52.8427 | 2026-08-19 13:40:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 138.7 |
| aaaeff30-9a56-3eb6-b8a6-ae5126e570b7 | -11.9319 | -49.9914 | 2026-08-19 13:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 66.3 |
| 218a2bea-83bb-3315-abc3-12bd1826ca9a | -5.9086 | -49.273 | 2026-08-19 13:40:00 | GOES-19 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 73.9 |
| 7b459896-9949-3dba-8c7c-81459510e0ac | -14.2213 | -52.883 | 2026-08-19 13:40:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 98.1 |
| 56f23e84-4c75-3f16-a42b-882256535c3e | -14.5272 | -53.0341 | 2026-08-19 13:50:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 79.6 |
| e933f159-60ea-33b8-b207-e5d5310cd5c2 | -14.221 | -52.9041 | 2026-08-19 13:50:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 255.0 |
| 152662e1-0761-3b9f-ab69-48181d96cedf | -13.5858 | -51.7781 | 2026-08-19 13:50:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 78.1 |
| 462114f7-5c69-30f5-a0b0-0a0325586e64 | -11.0431 | -51.0535 | 2026-08-19 13:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 165.5 |
| fb864392-0506-3c1f-a238-d2e8ad5af023 | -5.9086 | -49.273 | 2026-08-19 13:50:00 | GOES-19 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 74.7 |
| 3cfb30ac-963f-35c8-af74-aa8ab88357b6 | -10.8075 | -50.2907 | 2026-08-19 13:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 94.7 |
| 5496eb1e-8dbf-312b-a57b-11f2898a0b40 | -14.2213 | -52.883 | 2026-08-19 13:50:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 92.3 |
| 87823671-fd58-3e1d-8bf9-3239952088d8 | -15.2073 | -52.8401 | 2026-08-19 13:50:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 86.6 |
| 42c86dc4-6b96-32b2-86b6-2944f7e76971 | -9.4366 | -48.2955 | 2026-08-19 13:50:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 73.0 |
| d0708e9d-cb9d-3829-9d2d-46fdf57f7289 | -9.7537 | -43.2962 | 2026-08-19 13:50:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 67.1 |
| 0e87b98d-6a3c-376e-b1ac-11f0cdffab93 | -3.1278 | -60.6889 | 2026-08-19 13:50:00 | GOES-19 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 64.0 |
| c52aa6f8-914e-326b-83f0-da142647d17d | -6.3909 | -51.7475 | 2026-08-19 13:50:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 91.9 |
| 69a0f2ab-3f01-3f76-81b9-5f07c0ec1764 | -9.7533 | -43.3199 | 2026-08-19 13:50:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 68.2 |
| 29e3d6fc-f5ec-3cd7-8027-96d6e1002f2a | -11.9319 | -49.9914 | 2026-08-19 13:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 72.3 |
| 815eb1cc-a2fc-3151-82d7-32c70b006555 | -5.9272 | -49.2719 | 2026-08-19 13:50:00 | GOES-19 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 143.1 |
| ef003213-7ce8-37a7-847e-66f037d4d6b0 | -7.6171 | -49.9226 | 2026-08-19 13:50:00 | GOES-19 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 66.0 |
| 6449db46-0c07-3e27-bb9b-26790897d65a | -5.4317 | -48.4212 | 2026-08-19 13:50:00 | GOES-19 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 74.3 |
| 14148aeb-9278-3af7-8d0f-14cfae3d0441 | -6.0912 | -57.9187 | 2026-08-19 13:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 104.1 |
| 2b7cdc3b-72e5-3b56-a4c3-b9d86cab78e1 | -9.1078 | -46.046 | 2026-08-19 13:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 72.0 |
| 488a9d4c-c77e-32cd-a22b-b4fd46059890 | -11.4036 | -47.2511 | 2026-08-19 13:50:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 94.0 |
| 2d3dec99-4c30-3408-8592-aa2fe0820b3a | -14.2017 | -52.9065 | 2026-08-19 13:50:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 105.8 |
| 1a7151b5-c310-38aa-8701-1a959b632b17 | -15.1879 | -52.8427 | 2026-08-19 13:50:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 156.8 |
| 6e2ed9e2-6e06-3535-93b1-a8718745cbe5 | -8.3688 | -46.3473 | 2026-08-19 13:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 71.1 |
| 8c7bfeb9-28bf-3be3-942c-16d467753749 | -5.9274 | -49.2505 | 2026-08-19 13:50:00 | GOES-19 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 101.8 |
| f92f2081-08e0-37bf-85b3-6ab15cedd82e | -14.2763 | -51.902 | 2026-08-19 13:50:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 73.7 |
| 33b43848-49f0-3d80-914a-2e6ba5552ce3 | -10.8072 | -50.3121 | 2026-08-19 13:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 127.3 |
| be8b4579-7b0a-31f1-aabf-ce07e46a415c | -15.1875 | -52.8639 | 2026-08-19 13:50:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 76.1 |
| bb96cd09-8061-3273-82dc-012f51263a0d | -14.2021 | -52.8854 | 2026-08-19 13:50:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 76.4 |
| 63ec1a9d-e44f-3e3f-ac4c-17489c7f00b7 | -8.503 | -54.8625 | 2026-08-19 13:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 99.8 |
| e7401aa5-f2b0-3993-ab55-8baede8d83b7 | -16.5374 | -54.6831 | 2026-08-19 13:50:00 | GOES-19 | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 93.0 |
| 64fd89cd-de49-390b-b305-9efcac3f66fe | -9.4366 | -48.2955 | 2026-08-19 14:00:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 78.2 |
| 3ddabe78-5c76-3efd-be4e-80c1fc4506b3 | -13.4509 | -51.8162 | 2026-08-19 14:00:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 45.4 |
| 415b026c-a570-3710-b727-da0e6cee3716 | -11.853 | -50.1731 | 2026-08-19 14:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 69.9 |
| acbe615c-c65d-3650-9b29-8a8cfa877981 | -6.073 | -45.2873 | 2026-08-19 14:00:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 67.7 |
| dfecbcd4-5afe-37d3-b955-a8ef0b6f724c | -8.503 | -54.8625 | 2026-08-19 14:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 108.8 |


[Clique aqui para ver as próximas entradas](README76.md)
