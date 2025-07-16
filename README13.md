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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2a754e0d-67d6-32ef-841c-f6410c1ece16 | -5.05712 | -43.86331 | 2025-07-16 04:12:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 057e87e9-7756-36b4-b776-334a75902fbd | -2.91869 | -48.23353 | 2025-07-16 04:12:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b657d013-7b2c-3ad0-be9b-c30ef6f9a9e3 | -6.12795 | -42.95757 | 2025-07-16 04:12:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| cd16b585-fc90-3dfb-ad31-41508894f651 | -5.78731 | -45.08567 | 2025-07-16 04:12:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| f7337973-3ebb-3992-a187-2c9829e1c617 | -4.29087 | -48.06092 | 2025-07-16 04:12:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 1b3eae1c-e251-38a3-93c9-b0220cc2665c | -3.84422 | -47.75602 | 2025-07-16 04:12:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 345c2e5b-7b3f-3ae0-bfdd-a402e58ba860 | -6.3935 | -42.45593 | 2025-07-16 04:12:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 1be2414d-baa1-3fe6-b49c-8102a52e42d3 | -3.8447 | -47.75581 | 2025-07-16 04:12:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d9dda661-e3ad-3e57-bbe6-d4517a6c9e6e | -4.7795 | -45.33814 | 2025-07-16 04:12:00 | NOAA-20 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| e423224e-af77-374e-83e8-a224fd546a93 | -4.86559 | -43.22751 | 2025-07-16 04:12:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9e332da2-3d58-31a7-a633-2a61a99971c2 | -3.21696 | -48.97247 | 2025-07-16 04:12:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 3e76ed24-520e-3485-9cae-58f1997e3e99 | -4.1075 | -48.20692 | 2025-07-16 04:12:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7ef7902d-5cf9-3f5b-b1fb-98b68493d57b | -5.46161 | -45.34087 | 2025-07-16 04:12:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 77fd79cf-675e-3af3-81b8-4c8b45c263ac | -6.34182 | -43.43314 | 2025-07-16 04:12:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e017ea02-24ee-365c-b8c1-303df3cdd621 | -3.03115 | -47.85978 | 2025-07-16 04:12:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 095f5fb9-1c4e-34e0-8a2f-df062dc89455 | -4.02775 | -48.05975 | 2025-07-16 04:12:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 2f58616d-07c7-32a0-8d19-7a59b7640013 | -5.77986 | -45.0883 | 2025-07-16 04:12:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3f80c29d-259f-3cfc-af1f-537bc100c55a | -4.60231 | -43.32421 | 2025-07-16 04:12:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 60a5d76f-007d-36c7-9482-bc05c16b821d | -2.91804 | -48.23746 | 2025-07-16 04:12:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b5e8331e-e07d-3b5d-9d55-2ae21418a37f | -2.44181 | -47.32632 | 2025-07-16 04:12:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4e40819b-4193-33f3-ac35-51c10e875a8b | -3.03467 | -47.86419 | 2025-07-16 04:12:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| b1264ed5-61e4-3dbe-bd4b-e0a50feb79c8 | -3.04347 | -48.98108 | 2025-07-16 04:12:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f89cb1c6-652c-31bd-afc1-1c730a5c6690 | -5.79192 | -45.07875 | 2025-07-16 04:12:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b2cfeb6a-5b0e-3992-9d29-7cdeeed4d836 | -4.30138 | -48.07389 | 2025-07-16 04:12:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| efe5e20f-73bb-3e58-a914-f161e56f4f6e | -3.0497 | -41.12286 | 2025-07-16 04:12:00 | NOAA-20 | BARROQUINHA | CEARÁ | Brasil | 2302057 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 12c975c2-86df-3da6-8dc2-4cf0f2bd9ebd | -5.53192 | -43.89182 | 2025-07-16 04:12:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ff1dcedc-8c11-3aa1-b074-b285a9906656 | -5.5483 | -45.19896 | 2025-07-16 04:12:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ac9d7e99-0b04-31e3-9109-75a96ce9f845 | -3.58676 | -48.94183 | 2025-07-16 04:12:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 77e28dc8-780f-3543-a676-fd5eb39b7dcd | -5.35758 | -36.89119 | 2025-07-16 04:12:00 | NOAA-20 | CARNAUBAIS | RIO GRANDE DO NORTE | Brasil | 2402501 | 24 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 1a1dd6ee-0665-3cfe-802a-4fbf566db07b | -6.44351 | -42.80856 | 2025-07-16 04:12:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| a6aba169-a517-357b-9a8b-7f941083bb92 | -5.05517 | -43.27545 | 2025-07-16 04:12:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 77dcf10d-9c8e-301f-a705-0efaa03f3f0d | -4.58665 | -47.26308 | 2025-07-16 04:12:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 24095389-d47b-32e3-8b79-614ecc46b20f | -5.53358 | -43.88131 | 2025-07-16 04:12:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 30899850-3993-33dd-9eeb-45dbf76fb8af | -2.91316 | -48.2407 | 2025-07-16 04:12:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3b216a3a-32f4-3634-b7cb-addc8a5ff9c3 | -6.43581 | -42.81446 | 2025-07-16 04:12:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 5d31b0dd-660a-3297-b43d-dea1824debeb | -6.28839 | -43.40701 | 2025-07-16 04:12:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cc231259-93e2-32c0-89eb-d0526d42507a | -5.66828 | -43.71686 | 2025-07-16 04:12:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 981fa6f1-4037-34d5-932a-160b479ee645 | -3.33005 | -48.71732 | 2025-07-16 04:12:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2f24b3ed-7275-3bc0-b32c-c671da83491c | -6.00235 | -44.33089 | 2025-07-16 04:12:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| be8d1c80-f7e7-3ea2-b270-2e72f5de74f3 | -2.92228 | -48.23815 | 2025-07-16 04:12:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 987f772c-5f13-3afc-bba4-fd7d5fb69a65 | -3.84529 | -47.75223 | 2025-07-16 04:12:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1bfdb178-e111-3b73-a360-898514f26fc7 | -4.29148 | -48.05724 | 2025-07-16 04:12:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 24f4aa02-9a9b-3908-89da-869f801d6a2b | -3.51812 | -48.4356 | 2025-07-16 04:12:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 215c0ee5-4480-3831-96cf-279bf6068542 | -5.53247 | -43.88832 | 2025-07-16 04:12:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 9ea7cfff-488c-3e9b-892c-69dca1098cff | -5.79535 | -45.0793 | 2025-07-16 04:12:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| acf956d8-855f-3830-8a40-6da2f88a8e20 | -2.91381 | -48.23677 | 2025-07-16 04:12:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c05ab16e-fad4-37bc-ade9-c69aa334fade | -2.91674 | -48.24535 | 2025-07-16 04:12:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 45725ecb-ea77-38c3-b16f-ff0d4d9ae3d2 | -7.05895 | -38.85671 | 2025-07-16 04:12:00 | NOAA-20 | BARRO | CEARÁ | Brasil | 2302008 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| a2713aa4-228f-34a2-ad93-41e0bbe0b254 | -2.91739 | -48.2414 | 2025-07-16 04:12:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fe4cfdcd-86b7-36a9-a2a1-45fd9395bd52 | -3.84479 | -47.75243 | 2025-07-16 04:12:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f80bc004-0b94-37d0-8f78-c02c8d8f3b13 | -3.3828 | -47.49304 | 2025-07-16 04:12:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c2d30c2f-2e84-3ba4-b53c-9ef42c7bdfe9 | -4.03187 | -48.06038 | 2025-07-16 04:12:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 0c51c97b-3a4a-3a87-88c2-9aaafe4ffd78 | -3.38338 | -47.48952 | 2025-07-16 04:12:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4faa27a9-5a01-34df-9872-9c02908d5a75 | -5.73546 | -44.51124 | 2025-07-16 04:12:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e1a30fef-6481-37b7-a23d-73bba4274d2c | -4.10863 | -48.72663 | 2025-07-16 04:12:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 63fb9f72-1705-37be-ab63-3fe4e908697e | -4.77888 | -45.34206 | 2025-07-16 04:12:00 | NOAA-20 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 8f421cf6-a8ad-3a63-a15e-068613cac717 | -5.79475 | -45.08304 | 2025-07-16 04:12:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 67ccf385-e65f-3327-9a29-b1a5cc5a40cc | -3.38109 | -47.47841 | 2025-07-16 04:12:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 524e36a4-7e4d-3112-99f6-fdeaf6659cdc | -4.02715 | -48.06336 | 2025-07-16 04:12:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| ca7189b3-4521-3c3a-a511-ea413b174d9b | -5.66496 | -43.71634 | 2025-07-16 04:12:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ed46051a-77e6-37e7-9360-873fee1cbc57 | -6.43635 | -42.811 | 2025-07-16 04:12:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 9352c7d1-ad8e-3717-8816-535b6ba10267 | -3.3257 | -48.71659 | 2025-07-16 04:12:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2924d35b-61f8-3b41-9c1e-223bafa4f7ae | -6.13444 | -44.07721 | 2025-07-16 04:12:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 61462ec0-6b91-3928-8fa4-f53d8ddf072d | -5.42602 | -47.1428 | 2025-07-16 04:12:00 | NOAA-20 | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6ad3bfce-0f3f-3821-a0ce-5366dee4f82c | -5.55443 | -44.11119 | 2025-07-16 04:12:00 | NOAA-20 | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e17c093e-ed0d-3a6a-90a6-c5c809a3e150 | -6.34073 | -39.85706 | 2025-07-16 04:12:00 | NOAA-20 | CATARINA | CEARÁ | Brasil | 2303600 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| bfaee243-9806-39dd-ad23-973e437dbcbc | -5.8747 | -42.40671 | 2025-07-16 04:12:00 | NOAA-20 | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 9154cfac-fbb5-3c09-a27c-c4fcb5414329 | -2.44527 | -47.33046 | 2025-07-16 04:12:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 88c1d378-fb94-3ba0-8ec8-a2bc57be8781 | -6.28526 | -43.40351 | 2025-07-16 04:12:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 380b164d-9b3a-37c2-8088-e9fce237c6bb | -5.78448 | -45.08139 | 2025-07-16 04:12:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| e1fabdbf-24ce-309c-878f-3f2d258250b5 | -3.3868 | -47.49368 | 2025-07-16 04:12:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c6b5e302-6ddc-3665-966a-7a1c0e49f2ad | -5.53303 | -43.88482 | 2025-07-16 04:12:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 2dcf5504-c9d2-3cf8-9007-f2344e0bc066 | -5.7885 | -45.07821 | 2025-07-16 04:12:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9b808c30-791e-31b6-b0e2-f1808d91768b | -4.03126 | -48.06403 | 2025-07-16 04:12:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 4cd83fa9-e9ad-3451-a585-1073f3e63711 | -5.78388 | -45.08512 | 2025-07-16 04:12:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 064560aa-ff8e-3b6a-a0e0-1a61513f95d0 | -5.71888 | -44.83238 | 2025-07-16 04:12:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5b79a7f7-1b27-3a40-ab4e-7046484547c2 | -4.58747 | -47.25819 | 2025-07-16 04:12:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7f1b1552-d6ed-3178-9858-23b2b7683ef8 | -6.33487 | -42.37485 | 2025-07-16 04:12:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| aa51f90c-8484-3f45-aa3a-7a11ad8cbd89 | -6.43766 | -42.67255 | 2025-07-16 04:12:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| d4af4998-75d5-3bff-8343-aa1d4490dba9 | -3.5828 | -47.52161 | 2025-07-16 04:12:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 89b55022-7c78-33a1-b976-fd38e246fe0b | -6.40071 | -42.4534 | 2025-07-16 04:12:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| a9102e22-515f-3fd2-8eca-5776ce0bbd87 | -2.58577 | -51.92402 | 2025-07-16 04:12:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0d2fc319-f350-3c4c-94c0-8f5ff0319b5b | -4.78299 | -45.33873 | 2025-07-16 04:12:00 | NOAA-20 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| df7f2da6-0111-3bd3-8494-6ef1ed8b55a9 | -5.5749 | -46.52612 | 2025-07-16 04:12:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d6b03383-9abc-3c9a-9fd7-f5b4237e93bd | -4.03065 | -48.06773 | 2025-07-16 04:12:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| adba89f9-8763-356b-9c9c-afb261cd193c | -5.79073 | -45.08623 | 2025-07-16 04:12:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| d18f78b2-aac1-382f-86f3-aa0be6f2375b | -4.78095 | -45.33791 | 2025-07-16 04:12:00 | NOAA-20 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 084d364d-3927-32a5-b728-176dc4ba2e29 | -4.03538 | -48.06469 | 2025-07-16 04:12:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 95abd122-28bb-3028-bafd-bd80c9678922 | -3.99724 | -43.23914 | 2025-07-16 04:12:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f3d77271-e952-3271-adff-e69e0488c790 | -4.03599 | -48.06102 | 2025-07-16 04:12:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f0aa06fd-31b2-35c4-924f-3ef3d7eac1f4 | -4.10685 | -48.2108 | 2025-07-16 04:12:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b391444d-988a-3cf7-bcd7-e0f1b3d5ae98 | -5.52429 | -42.51894 | 2025-07-16 04:12:00 | NOAA-20 | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 908cbdc1-cef9-3bf2-9bcc-0cb660fccc6b | -5.57123 | -46.52554 | 2025-07-16 04:12:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5dd05932-b10e-3c64-927b-9a781b3e8181 | -3.33072 | -48.71317 | 2025-07-16 04:12:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 72b1ed04-a239-36bd-b0a0-c0988a627e98 | -2.91446 | -48.23287 | 2025-07-16 04:12:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 83311a76-8d9b-3981-8b35-acce26609ccc | -5.78671 | -45.08941 | 2025-07-16 04:12:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d82f6579-aa92-35d2-a90f-f9dbd366a9b5 | -6.30536 | -38.90924 | 2025-07-16 04:12:00 | NOAA-20 | ORÓS | CEARÁ | Brasil | 2309508 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 0cc15d3b-2fff-3dd7-bd7b-344e92fd1390 | -2.44125 | -47.32983 | 2025-07-16 04:12:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 90041919-d9cf-3ba0-93a7-ea99f9a755bf | -2.92652 | -48.23881 | 2025-07-16 04:12:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 27dd15a0-7b5b-3a4a-a3e4-89c9febfea56 | -2.44583 | -47.32696 | 2025-07-16 04:12:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |


[Clique aqui para ver as próximas entradas](README14.md)
