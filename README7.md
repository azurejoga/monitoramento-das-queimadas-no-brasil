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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6221f996-9fb7-3ae2-9e07-a15f3725c201 | -7.7025 | -48.8667 | 2026-09-29 02:00:00 | GOES-19 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 97.8 |
| e5a64065-4e3d-3596-a836-ac09c503cf1f | -6.3101 | -52.6184 | 2026-09-29 02:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 81.9 |
| 3ce6f47b-d78a-3af2-aef2-0ba12b89e6f5 | -5.6081 | -45.0038 | 2026-09-29 02:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 321.7 |
| 308a8eb2-6bb3-35fa-b057-39e78fcc7bc6 | -15.4585 | -46.1367 | 2026-09-29 02:00:00 | GOES-19 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 98.5 |
| b75abfa7-abc6-3b22-b77c-0d0afcac8dd4 | 1.6932 | -55.9223 | 2026-09-29 02:00:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 54.5 |
| b005fc77-e33e-3c82-8c4c-8ccbdbdf470a | 1.6566 | -55.903 | 2026-09-29 02:00:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 60.0 |
| ef0e55bc-711e-3417-94f3-4d81079befef | -9.1584 | -61.4082 | 2026-09-29 02:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 52.2 |
| eae0b176-5088-3d8d-9faf-9c879048e403 | -7.3825 | -72.4621 | 2026-09-29 02:00:00 | GOES-19 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 45.7 |
| 0088baf6-8cd6-3cb1-91e1-2df6276feda8 | -5.627 | -44.9797 | 2026-09-29 02:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 65.9 |
| 0eb61aa6-b9fc-308b-9382-eb6e05db4fb5 | -9.9568 | -59.2629 | 2026-09-29 02:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 48.2 |
| cb0650a0-427e-335a-b9a1-757c5fb10284 | -7.8486 | -45.8138 | 2026-09-29 02:00:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 220.0 |
| b4388a7c-1c91-32b7-9254-2f4b21482914 | 1.6932 | -55.942 | 2026-09-29 02:00:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 54.1 |
| d3b16580-1bf8-3f60-9703-85e2e1784658 | 1.6749 | -55.9225 | 2026-09-29 02:00:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 58.7 |
| 5ad3a1fd-ed26-3ebc-9fcf-03eae37b58bd | -9.177 | -61.4073 | 2026-09-29 02:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 82.1 |
| 12bcb45e-2f69-3c4a-b02d-fd68bd24728e | -7.8488 | -45.7912 | 2026-09-29 02:10:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 56.9 |
| 54e83737-d686-34b5-99c2-33b1c9e9affc | -6.1672 | -47.2858 | 2026-09-29 02:10:00 | GOES-19 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 68.0 |
| 9afc3b97-22fc-3595-babf-963800e89d88 | -3.8202 | -55.899 | 2026-09-29 02:10:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 58.5 |
| df589e80-0e8c-3566-9afd-6ebfdce7bba2 | -7.8297 | -45.8156 | 2026-09-29 02:10:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 128.8 |
| fb59df4e-64e4-32b4-b2b1-245b26476b02 | 1.675 | -55.9028 | 2026-09-29 02:10:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 92.2 |
| c48f5d29-642d-3423-99bf-5f77c880d956 | -5.6268 | -45.0025 | 2026-09-29 02:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 113.6 |
| 4583f778-5746-3cde-ad14-9dded4242c13 | -5.627 | -44.9797 | 2026-09-29 02:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 71.4 |
| 0c9a86d7-1d59-3aa2-8586-e56d1a8cf016 | -5.6081 | -45.0038 | 2026-09-29 02:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 270.9 |
| 06efda2e-5934-3b75-b9b5-2dca1419134d | -6.1483 | -47.3091 | 2026-09-29 02:10:00 | GOES-19 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 83.2 |
| 6ad7eea3-ce2e-34ca-95ad-a7b96f0ffd01 | -7.8483 | -45.8363 | 2026-09-29 02:10:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 57.6 |
| 51278345-8572-3065-9de8-0a2e16699fa4 | -7.7025 | -48.8667 | 2026-09-29 02:10:00 | GOES-19 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 104.4 |
| 5298600f-6f82-37d8-9e37-052e1ff8a1c9 | 1.6932 | -55.942 | 2026-09-29 02:10:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 48.7 |
| 23ae99f7-4c62-37ee-9e99-00efa97ef696 | -9.1584 | -61.4082 | 2026-09-29 02:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 62.9 |
| 604da889-8102-3f80-a82e-28cd377e0b3f | -3.7166 | -54.2297 | 2026-09-29 02:10:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 51.6 |
| 98dbd346-77f4-3942-8469-a2ceebb2bb97 | -6.1485 | -47.2871 | 2026-09-29 02:10:00 | GOES-19 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 197.7 |
| f6294ccb-396c-3ddd-bb61-aafe5e731b15 | -15.4585 | -46.1367 | 2026-09-29 02:10:00 | GOES-19 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 109.2 |
| d17e9a7b-ebeb-3f2a-a24a-14d15ed14661 | 1.6566 | -55.903 | 2026-09-29 02:10:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 59.4 |
| 41d3d346-9699-3a2e-8996-aa2b9e4d405a | -7.8486 | -45.8138 | 2026-09-29 02:10:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 183.2 |
| eeb82866-8aba-3a42-a4bd-3b08a81f47f1 | -5.6083 | -44.9811 | 2026-09-29 02:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 176.5 |
| 67cb1b26-c3ff-3d8c-9419-611a2c99e80e | -9.9595 | -50.1431 | 2026-09-29 02:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 58.3 |
| 7cdfcd5a-3142-3445-a832-e0e4010083db | 1.675 | -55.8831 | 2026-09-29 02:10:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 69.8 |
| 0422f870-1537-3277-aaeb-1c4f75491737 | 1.6567 | -55.8833 | 2026-09-29 02:10:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 89.3 |
| f0df6715-86a7-36a8-b267-e4aa22140e4d | -11.98 | -50.96 | 2026-09-29 02:15:00 | MSG-03 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 06508c05-ea74-3e02-bebf-183def91db0e | -11.42 | -43.43 | 2026-09-29 02:15:00 | MSG-03 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ccc8c5e5-307e-342c-b5b9-1b5d2237cd50 | -5.61 | -44.98 | 2026-09-29 02:15:00 | MSG-03 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e634523b-7c76-34ea-afd6-98745f760f44 | -5.62 | -45.03 | 2026-09-29 02:15:00 | MSG-03 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1fc201b7-6b14-3ef9-98fc-2298e0bc68ca | -11.45 | -43.49 | 2026-09-29 02:15:00 | MSG-03 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| b10043b7-ba56-35a2-afde-71c3d2891bbb | -11.42 | -43.48 | 2026-09-29 02:15:00 | MSG-03 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 220155ba-59f3-330d-a722-4d4a47106dfd | -11.98 | -51.02 | 2026-09-29 02:15:00 | MSG-03 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| f242e3a9-5175-3297-a8d4-9f9cef52a306 | -12.01 | -50.97 | 2026-09-29 02:15:00 | MSG-03 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 7fd63ddc-a138-3962-aa8c-1136f566e3dd | -5.6083 | -44.9811 | 2026-09-29 02:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 152.7 |
| e1646445-b227-314a-8e6f-0eacb40788b3 | -12.0123 | -50.9678 | 2026-09-29 02:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 104.8 |
| e7438a35-e619-3b12-a5b2-7d42c75b330c | -7.6838 | -48.8682 | 2026-09-29 02:20:00 | GOES-19 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 57.7 |
| 74b574a2-97f0-30af-87d6-65556eaf6c28 | -12.0314 | -50.9656 | 2026-09-29 02:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 75.2 |
| e043d313-c45a-35a4-b661-d791ba1290c7 | -6.1672 | -47.2858 | 2026-09-29 02:20:00 | GOES-19 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 76.6 |
| 86efbf10-c748-34fa-9d30-3d3de002cb09 | -6.1485 | -47.2871 | 2026-09-29 02:20:00 | GOES-19 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 104.0 |
| ce5e1130-9e6a-313a-a38e-cf8d24a35d62 | 1.6566 | -55.903 | 2026-09-29 02:20:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 53.7 |
| 9576fd2f-744b-39b5-b9de-6eddaa696dd4 | -7.7025 | -48.8667 | 2026-09-29 02:20:00 | GOES-19 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 101.6 |
| 834a90ca-5389-3807-a3ea-820b603bd7c6 | -12.012 | -50.9891 | 2026-09-29 02:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 72.1 |
| 5e247244-1b6e-32c4-aa38-e9923d4d07a5 | -5.6081 | -45.0038 | 2026-09-29 02:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 251.0 |
| f238b614-0196-3014-857f-40c81775715b | -11.3823 | -54.0434 | 2026-09-29 02:20:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 103.8 |
| d3230df4-8c91-3b3f-9fce-8b02bb42d8e2 | -9.177 | -61.4073 | 2026-09-29 02:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 65.8 |
| 922d0df1-69f3-3a59-b1d6-7b4926471e36 | -11.9929 | -50.9913 | 2026-09-29 02:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 71.6 |
| 0b4ea3ee-bec6-3e15-ac60-2cfa14846f4b | 1.675 | -55.9028 | 2026-09-29 02:20:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 85.0 |
| c6f201ab-f672-3048-9e02-99a53dfb5486 | -11.9926 | -51.0126 | 2026-09-29 02:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 90.2 |
| 5c52b25b-de6c-39b3-acb1-23c8f66b813c | -9.9595 | -50.1431 | 2026-09-29 02:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 58.8 |
| 410cf396-34c4-3a68-b563-781bfb0b3653 | -9.9593 | -50.1644 | 2026-09-29 02:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 40.8 |
| 7fcbc2a6-1008-3260-9c1d-9a4bf02b865e | -15.4585 | -46.1367 | 2026-09-29 02:20:00 | GOES-19 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 86.9 |
| c2f6e6c7-6f8f-38f2-989d-f167e28af847 | -11.4012 | -54.0417 | 2026-09-29 02:20:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 73.7 |
| ca31a2d7-02b1-3cb7-84b7-4c612c0296ab | -7.8486 | -45.8138 | 2026-09-29 02:20:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 174.4 |
| 73565abd-6fc8-312a-bd44-58daf99221b9 | -3.8202 | -55.899 | 2026-09-29 02:20:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 66.5 |
| a41ccd1f-c1de-3e39-ac0e-d90e060519ae | 1.675 | -55.8831 | 2026-09-29 02:20:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 61.9 |
| 7ee03283-b683-39f6-b8b2-969614fd6f26 | 1.6567 | -55.8833 | 2026-09-29 02:20:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 67.6 |
| ff1a3268-4381-3e11-9b90-8a4b5283669f | -7.8297 | -45.8156 | 2026-09-29 02:20:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 132.0 |
| 583e4d89-4008-38b7-804d-a574e9df52d9 | -3.8202 | -55.9187 | 2026-09-29 02:20:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 55.4 |
| fb4fb93d-2d5b-38a7-9d06-1e13e03b1168 | -12.0126 | -50.9464 | 2026-09-29 02:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 89.3 |
| 475ac78a-367d-3d17-9746-ee58f2dcd171 | -5.6268 | -45.0025 | 2026-09-29 02:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 57.3 |
| 421f41b1-33d8-37ec-bf2a-0ee157618054 | -9.1584 | -61.4082 | 2026-09-29 02:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 72.1 |
| b3b24973-484b-3e83-9c6b-df60399ba126 | -9.1584 | -61.4082 | 2026-09-29 02:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 69.1 |
| 275c1f1b-a93b-3802-a143-155fe868e0f1 | 1.6567 | -55.8833 | 2026-09-29 02:30:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 67.4 |
| d4391875-31bf-3566-b49f-a506faac72c7 | -7.7025 | -48.8667 | 2026-09-29 02:30:00 | GOES-19 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 104.3 |
| e6815548-9e64-324e-a67f-5bc975013101 | -7.8486 | -45.8138 | 2026-09-29 02:30:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 171.7 |
| f763f42f-b443-34fa-85c8-181e3343cd08 | -9.9595 | -50.1431 | 2026-09-29 02:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 55.9 |
| 1f276838-e3f9-3bb1-ad28-7e701af81004 | 1.675 | -55.9028 | 2026-09-29 02:30:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 86.0 |
| 1d9573f1-c302-314a-b744-080bf218a61d | -7.8297 | -45.8156 | 2026-09-29 02:30:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 119.7 |
| c117d5cd-ea6f-3a4d-adf2-8477bea90f1f | -11.4012 | -54.0417 | 2026-09-29 02:30:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 120.0 |
| 363ea9f2-dc16-394d-8498-8a64e587596b | -12.0126 | -50.9464 | 2026-09-29 02:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 101.4 |
| 8200d852-72bc-3190-9a77-2a90b80c3f19 | -5.6081 | -45.0038 | 2026-09-29 02:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 193.0 |
| ec985265-d255-3410-a4b2-5457dc3808f9 | -12.0314 | -50.9656 | 2026-09-29 02:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 244.6 |
| 60751bc1-915b-39de-af71-2e4dc07625df | -11.3823 | -54.0434 | 2026-09-29 02:30:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 150.8 |
| 964dff8e-59b7-3e8a-a933-eb442fad0e80 | -12.0123 | -50.9678 | 2026-09-29 02:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 146.0 |
| 112d4bc9-4fa3-3556-bc25-b777f90f4095 | -10.8424 | -60.7622 | 2026-09-29 02:30:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 54.2 |
| a084f3b7-0526-35c6-ab92-c219427cc1f9 | -9.9593 | -50.1644 | 2026-09-29 02:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 41.5 |
| bd1919c4-ff3d-3560-a3fc-a9abe1e1e829 | -3.8202 | -55.9187 | 2026-09-29 02:30:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 61.0 |
| ce9ddc4b-0789-39d5-b900-8147d95f089c | -5.6083 | -44.9811 | 2026-09-29 02:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 106.4 |
| 8a4ced57-149a-3423-a36f-eddcb2c6e601 | -12.0317 | -50.9442 | 2026-09-29 02:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 133.7 |
| 91d1b7d6-adaa-3811-b657-2edabdb9e094 | -3.8202 | -55.899 | 2026-09-29 02:30:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 71.0 |
| 896a7f06-4796-3a5a-871d-9cb8d9959184 | -3.8386 | -55.8985 | 2026-09-29 02:30:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 52.5 |
| 7975f99e-7a3c-36ed-bdc5-34d40036b468 | -8.2479 | -45.4583 | 2026-09-29 02:30:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 59.3 |
| 89888815-f846-399c-9a8a-d3713ba11505 | -11.382 | -54.064 | 2026-09-29 02:30:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 72.2 |
| 4f91b180-da79-3f76-b4cf-8adc3f6a25d1 | -12.7606 | -50.6857 | 2026-09-29 02:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 73.3 |
| 18c72ee4-b377-30f9-a674-f80a2b1152d9 | -9.177 | -61.4073 | 2026-09-29 02:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 72.2 |
| 45af2373-4143-3514-84ed-b4b849d3d6fd | -7.8483 | -45.8363 | 2026-09-29 02:30:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 57.4 |
| a096ed6e-d127-348b-bf42-c7ff67c30b91 | 1.675 | -55.8831 | 2026-09-29 02:30:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 67.1 |
| b7f860fd-93e3-31bf-84ab-5a8f392bce8c | -15.4585 | -46.1367 | 2026-09-29 02:30:00 | GOES-19 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 76.6 |
| ef5a8be5-8ae5-354d-960a-f4b1b53a3d19 | 1.6567 | -55.8833 | 2026-09-29 02:40:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 74.6 |


[Clique aqui para ver as próximas entradas](README8.md)
