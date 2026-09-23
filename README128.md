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

## Dados Diários - Página 128

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 97b840ae-c3ae-35e8-be29-a8f9b7358cbe | -9.34023 | -65.72769 | 2026-09-23 06:46:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 862c9fd4-a5c7-3115-8c56-9d730ad97dfe | -9.56234 | -65.98502 | 2026-09-23 06:46:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2d6b0e8c-4a22-3e90-a483-eb5f9a1eeacd | -8.77131 | -72.77204 | 2026-09-23 06:46:00 | NPP-375D | MARECHAL THAUMATURGO | ACRE | Brasil | 1200351 | 12 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9a85f298-4b73-322d-b244-9d4973670d80 | -9.55783 | -65.99634 | 2026-09-23 06:46:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 69d594d8-29cd-3e22-a732-b47bbb322273 | -8.61617 | -66.73315 | 2026-09-23 06:46:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| cff3f473-995c-382d-90c0-64944a2afc1d | -8.61681 | -66.72808 | 2026-09-23 06:46:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| d2eb5f1b-b892-3b61-a61d-531ba6acf743 | -8.92382 | -72.82214 | 2026-09-23 06:46:00 | NPP-375D | MARECHAL THAUMATURGO | ACRE | Brasil | 1200351 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 56c8413d-df51-3de9-ac12-ca8fbfd5d5d5 | -8.61442 | -66.72688 | 2026-09-23 06:46:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 8c80cfaa-dae1-323b-8452-645d9b6744fb | -9.55855 | -65.99061 | 2026-09-23 06:46:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| be86b6b3-33a7-389a-b97b-3910f94ddb5a | -8.61376 | -66.73194 | 2026-09-23 06:46:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| ebb968a4-6cad-344c-84b0-b7bcb360a706 | -8.97567 | -72.61314 | 2026-09-23 06:46:00 | NPP-375D | MARECHAL THAUMATURGO | ACRE | Brasil | 1200351 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9c69683e-ed43-3eff-a3af-52f19be698ff | -9.55257 | -65.98395 | 2026-09-23 06:46:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4272b99e-7be2-3ff5-b3a5-2034c70fe203 | -9.04421 | -65.41269 | 2026-09-23 06:46:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c418c6cc-16b3-312b-af37-bcad8e0b6115 | -9.56164 | -65.99088 | 2026-09-23 06:46:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c5d886db-3d25-3c9d-9001-7a22afe21e80 | -9.04343 | -65.41907 | 2026-09-23 06:46:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ed4f0c80-2b0d-3155-82e3-944efdbff1a8 | -9.04264 | -65.42545 | 2026-09-23 06:46:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 31c937cf-ee57-3b52-986c-7dd798022dab | -9.045 | -65.40629 | 2026-09-23 06:46:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 11b235d3-4de5-3a50-a261-bb0a1a38d7ce | -9.05033 | -65.41995 | 2026-09-23 06:46:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ca5cf4cf-08c1-3b08-bd3c-9fb5b4e00229 | -9.33341 | -65.72694 | 2026-09-23 06:46:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3f109b1a-4230-3c90-b7aa-cd216a9495fe | -9.04954 | -65.42633 | 2026-09-23 06:46:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 263b1481-cc18-36fc-b417-d3b01f9a4904 | -11.9908 | -52.4485 | 2026-09-23 06:50:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 60.7 |
| b4db6f6b-757c-38e1-83a2-672b9e98f542 | -9.1025 | -61.4299 | 2026-09-23 06:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 54.5 |
| eeaf3cc0-7e09-3aef-8555-08e009b10ad2 | -11.9906 | -52.4695 | 2026-09-23 06:50:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 64.7 |
| a1dc6608-edf1-3d86-b48d-6e4ebf5f709d | -8.935 | -61.495 | 2026-09-23 07:00:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 49.1 |
| 39ca4b41-9da2-3c30-81d3-fa219bd6e690 | -14.6297 | -45.6635 | 2026-09-23 07:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 80.8 |
| 166520f6-7525-3a9f-a9ed-920044a0449c | -8.9164 | -61.4958 | 2026-09-23 07:00:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 48.6 |
| 2e3fa0f9-64ce-3420-90e3-98e51dd4d905 | -11.285 | -51.3666 | 2026-09-23 07:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 72.7 |
| 0fd8d387-d0ba-3355-a256-2540be300ba0 | -10.23 | -50.25 | 2026-09-23 07:00:00 | MSG-03 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e3ee6a8b-cae5-3375-9ecb-c0a543de9ca2 | -10.23 | -50.2 | 2026-09-23 07:00:00 | MSG-03 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| cf1bb827-2867-30fc-953d-39b86a90feb7 | -6.6331 | -59.9265 | 2026-09-23 07:10:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 98.7 |
| 236bd012-0a2f-366f-8bca-fd9fc3476133 | -14.6297 | -45.6635 | 2026-09-23 07:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 95.7 |
| 9cddcaf5-c17b-3b5a-a9bf-57c15b4dd268 | -6.6145 | -59.9464 | 2026-09-23 07:10:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 56.7 |
| d7b6bab8-281b-3308-9a3d-1fa49b939d43 | -6.6515 | -59.9258 | 2026-09-23 07:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 51.3 |
| 865aaccc-e70c-380d-a90c-66e6b9e40b7a | -9.1024 | -61.4491 | 2026-09-23 07:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 44.4 |
| 451cfe29-4874-3e35-89e4-85a92ae12c62 | -11.6913 | -50.8126 | 2026-09-23 07:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 73.8 |
| edb01292-e8a9-3589-aa3a-21e04e23a820 | -6.6148 | -59.908 | 2026-09-23 07:10:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 52.2 |
| 5a7742bd-3660-37f1-8edf-d4ab3d5e2128 | -6.633 | -59.9457 | 2026-09-23 07:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 68.4 |
| 7c242101-7da3-3b50-a173-14c92e8aa1bb | -8.9164 | -61.4958 | 2026-09-23 07:10:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 49.5 |
| b6e25f00-647c-35a0-ab1b-a344b5791d8c | -6.6146 | -59.9272 | 2026-09-23 07:10:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 110.9 |
| ed975c34-777b-38fa-ad00-3fb9ddda1175 | -10.23 | -50.25 | 2026-09-23 07:15:00 | MSG-03 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a22232c0-d49b-3b07-8fb8-5342a750d164 | -12.0149 | -50.7969 | 2026-09-23 07:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 162.8 |
| 8fb7009d-0d98-30c6-849f-bddf680bece5 | -9.1025 | -61.4299 | 2026-09-23 07:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 49.9 |
| a45a6b8f-dca5-3777-a94c-5c877424d9d5 | -11.9958 | -50.7991 | 2026-09-23 07:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 69.7 |
| 8ff9ea96-47da-3fec-b83b-0ad171f78a8e | -6.633 | -59.9457 | 2026-09-23 07:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 72.1 |
| e3d3c89a-8569-3aec-aa09-188cda20a6ae | -6.6331 | -59.9265 | 2026-09-23 07:20:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 98.0 |
| 864e7e0e-48f8-3f86-bc6d-901466ff9078 | -6.6145 | -59.9464 | 2026-09-23 07:20:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 54.1 |
| 03a070de-12ca-3ba0-9979-f087c999cd8e | -11.285 | -51.3666 | 2026-09-23 07:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 63.4 |
| 25b63e1b-efba-35b7-85a9-c57b537c6bbd | -12.0343 | -50.7732 | 2026-09-23 07:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 99.2 |
| 035ec09e-164d-31b7-a42e-90d99668c819 | -6.6146 | -59.9272 | 2026-09-23 07:20:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 92.3 |
| d1ff4362-83f7-342f-b9bd-330f2064bcc2 | -12.053 | -50.7924 | 2026-09-23 07:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 97.3 |
| 978489a8-ba47-33c7-9bd3-d1d2d5f8b2a9 | -12.0339 | -50.7946 | 2026-09-23 07:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 158.8 |
| d6ee5e29-93ed-3d2f-a045-a6730c7488c6 | -12.0152 | -50.7755 | 2026-09-23 07:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 115.1 |
| ec1e0112-09c8-3557-a900-34e8c246f3ab | -6.633 | -59.9457 | 2026-09-23 07:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 68.7 |
| 074978c1-bbac-37f4-9143-66915ee5fcae | -6.6145 | -59.9464 | 2026-09-23 07:30:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 51.1 |
| 945d0c92-3b68-310a-bbd8-290e0195ac3a | -6.6331 | -59.9265 | 2026-09-23 07:30:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 97.1 |
| f8e57c8b-c543-304c-8bde-f9212d06f94e | -11.9908 | -52.4485 | 2026-09-23 07:30:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 53.0 |
| 7e08ba8d-b9f8-3a8e-aa52-3dca45e61c42 | -6.6148 | -59.908 | 2026-09-23 07:30:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 45.2 |
| 4f0a53fc-11c4-3bd7-9e4f-4867492050b6 | -8.9164 | -61.4958 | 2026-09-23 07:30:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 46.8 |
| 2b6cb78b-cbd1-3700-a1ff-ba55dcb5d4e4 | -9.1025 | -61.4299 | 2026-09-23 07:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 51.0 |
| 0cf267ba-503a-396e-bbd4-643461c70d80 | -6.6146 | -59.9272 | 2026-09-23 07:30:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 86.4 |
| 8eaa000e-dc21-3459-99a5-8cf2dd2527db | -10.23 | -50.25 | 2026-09-23 07:30:00 | MSG-03 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 53e835d6-029a-3161-92f8-1ad0c80f3f45 | -10.23 | -50.2 | 2026-09-23 07:30:00 | MSG-03 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8ea11007-f512-3e57-afa5-ac3ffe0f5af3 | -6.633 | -59.9457 | 2026-09-23 07:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 61.4 |
| 807e7b64-33d5-3191-ab0c-a2695eb14449 | -10.2565 | -50.5185 | 2026-09-23 07:40:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 127.5 |
| 15c6ba2d-7f1e-33e3-85e1-f54d6fe434c3 | -6.6331 | -59.9265 | 2026-09-23 07:40:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 80.2 |
| 8a3882fc-e9c8-310d-99af-ebfb774ab4ca | -8.9164 | -61.4958 | 2026-09-23 07:40:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 45.7 |
| 7941b57b-e353-3bf1-ab4e-47319329cb86 | -6.6146 | -59.9272 | 2026-09-23 07:40:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 82.8 |
| 0f61bb85-d5a5-3e57-af84-847569136bf1 | -6.6145 | -59.9464 | 2026-09-23 07:40:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 50.4 |
| e905f07d-65e4-32fe-9955-ec89c4c35ce6 | -10.2562 | -50.5398 | 2026-09-23 07:40:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 70.9 |
| 7ea83c93-1320-3e7d-9db4-aef55317a9a9 | -11.285 | -51.3666 | 2026-09-23 07:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 76.4 |
| 7e2ad37b-bf3e-3cbf-b14f-132280c8c1cf | -12.4216 | -46.9551 | 2026-09-23 07:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 62.2 |
| 2cd5444f-71d3-395f-bf9c-a8bcd49338fb | -11.6913 | -50.8126 | 2026-09-23 07:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 72.7 |
| b11a66ec-1898-3043-b4df-51f18c1d72c9 | -6.6148 | -59.908 | 2026-09-23 07:40:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 44.8 |
| 7dd84a3f-aaad-3f76-b07a-96983ee02bb4 | -12.4212 | -46.9777 | 2026-09-23 07:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 62.6 |
| f8db2244-8b26-3225-9a0f-9ee3c997df62 | -10.23 | -50.25 | 2026-09-23 07:45:00 | MSG-03 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6d62c7d1-8a80-38a1-8eb2-ab2d2c092d6f | -12.0 | -50.8 | 2026-09-23 07:45:00 | MSG-03 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| dce47fe0-565d-3aef-9698-92fa132ac7b3 | -10.2562 | -50.5398 | 2026-09-23 07:50:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 63.2 |
| ef99bb3d-191c-33b7-a0a8-7a58951a82f3 | -6.6331 | -59.9265 | 2026-09-23 07:50:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 88.7 |
| d6249b81-a292-3468-8695-568ea29b75b2 | -10.0151 | -50.2229 | 2026-09-23 07:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 134.2 |
| 42259942-1743-3602-a0f0-1ef9620fec2a | -12.4212 | -46.9777 | 2026-09-23 07:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 61.5 |
| a94a5dbc-147a-3d5d-9fbc-a48d1e45d0a4 | -12.0595 | -50.3634 | 2026-09-23 07:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 59.8 |
| 7acbef01-574b-39d0-a701-2c4fc8a4dacc | -6.6148 | -59.908 | 2026-09-23 07:50:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 41.4 |
| 29ee9a9b-0a55-315b-9f84-0cd487e499e9 | -11.285 | -51.3666 | 2026-09-23 07:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 74.5 |
| 0e46d2a3-ce43-3fc5-aafc-1d251baf2e6e | -6.6146 | -59.9272 | 2026-09-23 07:50:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 76.6 |
| 7e3b32bb-fd74-3f26-8e2c-4735e8dd4719 | -10.2376 | -50.5204 | 2026-09-23 07:50:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 58.4 |
| 83eccff1-2053-3acf-945a-3b1f10b26d75 | -11.2847 | -51.3878 | 2026-09-23 07:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 79.9 |
| 757eb710-2c16-34c4-b005-af8bdbb1888a | -10.0153 | -50.2016 | 2026-09-23 07:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 73.8 |
| 79ea12ab-e46d-37c1-b5df-fea2f9e0ecd3 | -6.6145 | -59.9464 | 2026-09-23 07:50:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 43.7 |
| d1689bc2-fc12-370d-aa2b-a11f9e0ea53a | -12.4216 | -46.9551 | 2026-09-23 07:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 66.9 |
| ef89269b-ca25-30c8-9023-e61a8e54c79c | -6.633 | -59.9457 | 2026-09-23 07:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 57.2 |
| 1f748e98-6b67-3b4b-b25c-da9db48399a8 | -11.6913 | -50.8126 | 2026-09-23 07:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 74.8 |
| b82507d1-2aae-37c1-bdce-b68c372fa7bc | -6.6515 | -59.9258 | 2026-09-23 07:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 42.9 |
| bfb7fb78-f4c9-3793-877e-b0e8cf01c8db | -10.2565 | -50.5185 | 2026-09-23 07:50:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 107.3 |
| d187b6a4-b51b-371c-9c56-0a371ed43dbb | -10.0151 | -50.2229 | 2026-09-23 08:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 107.8 |
| 80443ea9-19fc-3f7c-94be-4a5de48f9ab7 | -10.2565 | -50.5185 | 2026-09-23 08:00:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 60.2 |
| ef07700b-29fa-3838-8d01-b1146b305407 | -12.0343 | -50.7732 | 2026-09-23 08:00:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 81.7 |
| c45f9c27-0d65-3561-87d1-28fb4cbae525 | -6.6331 | -59.9265 | 2026-09-23 08:00:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 83.7 |
| 45eb9bce-3720-3fbc-9eff-9b99ffd8467e | -11.6913 | -50.8126 | 2026-09-23 08:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 75.1 |
| 49a9741c-ba65-3207-ae46-b255b80ad2fd | -11.9961 | -50.7777 | 2026-09-23 08:00:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 124.3 |
| 5d455c33-bbeb-3f24-b335-07742057215e | -10.0339 | -50.2211 | 2026-09-23 08:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 55.4 |


[Clique aqui para ver as próximas entradas](README129.md)
