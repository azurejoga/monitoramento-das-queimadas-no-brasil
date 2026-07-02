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
| c937d864-585f-3402-a189-e4ee85531263 | -11.35776 | -55.43554 | 2026-07-02 00:01:00 | TERRA_M-M | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 28.2 |
| 333fc755-d651-3532-a3e0-4e6da25c1da8 | -8.66194 | -49.70629 | 2026-07-02 00:01:00 | TERRA_M-M | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 30282ce3-a899-3260-8a81-f5e9360017ff | -12.52193 | -48.29619 | 2026-07-02 00:01:00 | TERRA_M-M | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 17.3 |
| 55a18695-d4ce-3f80-af20-f4410705a3cd | -7.10376 | -46.51627 | 2026-07-02 00:01:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 10.8 |
| d9416b0d-3cc9-3412-a94f-31aa40eb22f6 | -6.91945 | -43.72289 | 2026-07-02 00:01:00 | TERRA_M-M | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 4f156f5e-c3e0-3749-ab8e-43eae28d7fc1 | -9.75172 | -47.87851 | 2026-07-02 00:01:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| dfe3a206-e8ac-3277-86ef-45612ae699cd | -12.73702 | -44.48303 | 2026-07-02 00:01:00 | TERRA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 25.3 |
| 3a18b436-289a-30a1-a17e-df5ac5a13fdb | -12.85673 | -44.34269 | 2026-07-02 00:01:00 | TERRA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 674.2 |
| 2793e06b-c2e7-3a43-9202-6ea1d4ed5f9d | -11.90769 | -43.39084 | 2026-07-02 00:01:00 | TERRA_M-M | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 7.6 |
| e4311799-1709-3176-9fdb-06edb86cc41c | -10.95301 | -43.0492 | 2026-07-02 00:01:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 141.9 |
| ab945ef4-4925-3ce7-9e1f-5ef5c254be24 | -9.16725 | -47.23718 | 2026-07-02 00:01:00 | TERRA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 26030820-ff15-37ed-bf87-9b03e91f1df3 | -12.74936 | -44.50188 | 2026-07-02 00:01:00 | TERRA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 25.1 |
| d16bf845-bed4-3351-b75f-41ba210c20c0 | -9.53297 | -47.75726 | 2026-07-02 00:01:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 65f226a7-4365-3b4a-8f1d-5a789302aa06 | -10.13293 | -52.09815 | 2026-07-02 00:01:00 | TERRA_M-M | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 29.1 |
| ecbaa32a-ac43-37d1-8ebf-eb160b1cb788 | -12.74787 | -44.49173 | 2026-07-02 00:01:00 | TERRA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 571.2 |
| 22686f7f-66f0-3a71-aa91-3541b4b47269 | -12.85482 | -44.39554 | 2026-07-02 00:01:00 | TERRA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 33.1 |
| 6796d5ee-23f7-3977-917a-3bd033617e3f | -11.52401 | -43.23315 | 2026-07-02 00:01:00 | TERRA_M-M | MORPARÁ | BAHIA | Brasil | 2921609 | 29 | 33 | nan | nan | nan | Caatinga | 8.3 |
| f515877d-9074-3e6f-8498-d4296911911d | -12.75086 | -44.51203 | 2026-07-02 00:01:00 | TERRA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 9eb3a746-ba93-332a-98b1-bed2993a6874 | -11.86811 | -45.60775 | 2026-07-02 00:01:00 | TERRA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 2efcf10a-36ba-3f10-a63e-eaa094476a0c | -10.8011 | -48.56403 | 2026-07-02 00:01:00 | TERRA_M-M | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 19.7 |
| 5c5880fb-b34a-3a2b-bfd5-1e0e6c346724 | -12.86913 | -44.3618 | 2026-07-02 00:01:00 | TERRA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 124.6 |
| ea033da6-37b8-3f36-8366-5a5aa580d0f1 | -7.90572 | -48.24263 | 2026-07-02 00:01:00 | TERRA_M-M | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 0b529406-3ed3-30be-a5b7-821a25357a72 | -12.76657 | -44.48883 | 2026-07-02 00:01:00 | TERRA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 74.8 |
| 8902d236-7f2f-321f-9667-c5b337cdf652 | -9.20958 | -45.31698 | 2026-07-02 00:01:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 6195a86f-f85d-3ceb-be2a-6da045dcb011 | -9.96737 | -47.76537 | 2026-07-02 00:01:00 | TERRA_M-M | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 100.9 |
| b8f60933-b3cf-3c92-ad63-2ccd3d9729aa | -11.35922 | -55.44048 | 2026-07-02 00:01:00 | TERRA_M-M | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 26.5 |
| 9d039879-30e9-3bd3-ae6a-d3e96087bc07 | -9.15718 | -47.22955 | 2026-07-02 00:01:00 | TERRA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 5c76c8a1-6f12-3a74-99b2-db1e32dfc06d | -8.80046 | -47.31422 | 2026-07-02 00:01:00 | TERRA_M-M | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 89f7994c-52e3-3e51-88e0-7ecd044537f5 | -12.83941 | -44.35594 | 2026-07-02 00:01:00 | TERRA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 29.5 |
| 315087dd-2991-3267-8bb2-0c0430ae5171 | -12.74002 | -44.50332 | 2026-07-02 00:01:00 | TERRA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 3a4f7182-0e71-3b6c-b675-75817be63e5c | -11.85341 | -48.24416 | 2026-07-02 00:01:00 | TERRA_M-M | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 26.2 |
| fd189701-77dd-3305-9517-8c9baee16afb | -9.28037 | -50.22511 | 2026-07-02 00:01:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| c90202dc-35bf-33a3-bd62-29327f1b52e7 | -12.7774 | -44.49752 | 2026-07-02 00:01:00 | TERRA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 755a1700-75bd-37b4-bbf0-b50dcbb023ec | -10.11977 | -52.08466 | 2026-07-02 00:01:00 | TERRA_M-M | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 8b76bf93-8918-332a-8ea2-36c9110c7bba | -9.75145 | -49.03234 | 2026-07-02 00:01:00 | TERRA_M-M | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| d1575ac4-48c4-371e-85df-0cb1724c898f | -11.79574 | -57.03204 | 2026-07-02 00:01:00 | TERRA_M-M | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 37.6 |
| 535b7f7d-8065-3bd3-ae74-99c30518a6ce | -12.85973 | -44.36329 | 2026-07-02 00:01:00 | TERRA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 108.8 |
| bd34e3e5-69e0-3fe9-99ff-3b8694d526bc | -9.98078 | -54.43919 | 2026-07-02 00:01:00 | TERRA_M-M | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 25.5 |
| c3e16691-f18c-380f-872e-549d257f09c5 | -8.49965 | -47.2034 | 2026-07-02 00:01:00 | TERRA_M-M | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 71555da4-c26e-31ef-892b-b4ab01cc19e2 | -12.75722 | -44.49029 | 2026-07-02 00:01:00 | TERRA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 802.4 |
| 9679bd42-145e-3dcc-82f8-4720043e08a1 | -10.94451 | -43.06387 | 2026-07-02 00:01:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 1db57e85-957e-305c-ace1-e073c451288b | -9.20026 | -45.31844 | 2026-07-02 00:01:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 80.8 |
| ad778b0a-d997-378d-b357-f3a9bd423eb5 | -11.00111 | -47.17887 | 2026-07-02 00:01:00 | TERRA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 0e17634b-33a8-3837-8693-9b97e9cf6f85 | -5.75889 | -47.04543 | 2026-07-02 00:03:00 | TERRA_M-M | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 9e54941d-1ade-3366-aa5e-5136ef55b2b8 | -5.48089 | -44.10435 | 2026-07-02 00:03:00 | TERRA_M-M | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 54b43816-d159-391a-b33b-78a3d91387f5 | -5.3522 | -45.18547 | 2026-07-02 00:03:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 8eecd434-ca15-30af-869e-2b495aa75fb7 | -3.41642 | -41.71887 | 2026-07-02 00:03:00 | TERRA_M-M | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Caatinga | 46.3 |
| 26874557-e4d0-333e-ba29-221f65cf5949 | -5.76786 | -47.04412 | 2026-07-02 00:03:00 | TERRA_M-M | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 9834c815-9a89-35ab-8860-c7a3b8aaadfd | -6.43561 | -48.54321 | 2026-07-02 00:03:00 | TERRA_M-M | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 424e4d49-9c99-3dcc-af16-a9314925fceb | -5.37432 | -43.39164 | 2026-07-02 00:03:00 | TERRA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 8e07b1ce-2e7f-38f8-9768-bd9bdccaa9d5 | -5.81657 | -43.81101 | 2026-07-02 00:03:00 | TERRA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 19.5 |
| c20cc4f9-ea00-3153-b5df-222f71a461d7 | -3.51003 | -48.03588 | 2026-07-02 00:03:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 126.2 |
| 7fa0208e-c52d-3fa2-9fea-614f3a585d93 | -5.8866 | -46.96838 | 2026-07-02 00:03:00 | TERRA_M-M | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| e4d02d55-9638-3c11-a9c7-0b932a71b3e2 | -5.79447 | -45.04983 | 2026-07-02 00:03:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 20.5 |
| 9ccabf77-67d4-3c39-9d75-59b8ea312e84 | -5.47679 | -44.11068 | 2026-07-02 00:03:00 | TERRA_M-M | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 32d53577-32ae-3099-878b-ca82028864f1 | -3.51125 | -48.04472 | 2026-07-02 00:03:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 31.0 |
| 0b1c61b8-a621-3489-b450-d86bd468cd85 | -4.28337 | -48.36428 | 2026-07-02 00:03:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 9bac5086-e6e4-30a4-8181-27b55d006055 | -5.79112 | -45.03318 | 2026-07-02 00:03:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 0f9fdc38-28ca-3c8d-9a90-bfca2de22009 | -3.66765 | -48.98362 | 2026-07-02 00:03:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 961cc558-2b5c-390e-ab6d-45832c454406 | -3.52011 | -48.04347 | 2026-07-02 00:03:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 53f60cee-8908-34b2-8f0b-68d7af549de6 | -4.00148 | -48.06249 | 2026-07-02 00:03:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 22.9 |
| 6b4472ea-7814-3b97-b3a6-5cc0de2e29e0 | -5.7927 | -45.04445 | 2026-07-02 00:03:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 30.0 |
| 3394b4b9-c020-3e40-8478-acb44067697a | -6.83108 | -49.28348 | 2026-07-02 00:03:00 | TERRA_M-M | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 68a2eb34-7dc9-381c-b715-6358aa195498 | -5.37207 | -43.37669 | 2026-07-02 00:03:00 | TERRA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 18.6 |
| a5e66e42-3ca6-392d-8fb2-da207d8eacae | -4.57857 | -48.02894 | 2026-07-02 00:03:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 43f34fae-210b-3241-9edc-a71132dc1926 | -6.25834 | -49.87776 | 2026-07-02 00:03:00 | TERRA_M-M | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 16.0 |
| 94850e8a-3509-3ba7-9622-6c890ec65fd8 | -4.94798 | -48.24599 | 2026-07-02 00:03:00 | TERRA_M-M | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 22.0 |
| 538c3cf0-1cda-3fb3-9a72-8cedea8b524b | -4.01258 | -48.06409 | 2026-07-02 00:03:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 41.3 |
| d2d4a64a-a06f-318a-8ac1-cbd1a37a8a8e | -5.79281 | -45.03859 | 2026-07-02 00:03:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 41.9 |
| de76faaf-f9c2-3d7a-9234-f5a5d20fa8fb | -4.01136 | -48.05525 | 2026-07-02 00:03:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 18.0 |
| 21634d7c-9277-35f4-b681-e0f0bc1e3064 | -3.41322 | -41.69722 | 2026-07-02 00:03:00 | TERRA_M-M | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Caatinga | 50.0 |
| 84336135-ecd8-3efd-a01b-51fefc62f92c | -5.37321 | -43.38219 | 2026-07-02 00:03:00 | TERRA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 29.5 |
| 3f7d8942-be16-3593-8714-895e66e291d6 | -3.51889 | -48.03465 | 2026-07-02 00:03:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 30.1 |
| d47780b6-5d53-3f57-bbc5-46e66baab198 | -2.43129 | -47.03332 | 2026-07-02 00:03:00 | TERRA_M-M | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 4a9c1d9c-4c76-3281-b43c-03176d787737 | -5.81454 | -43.79733 | 2026-07-02 00:03:00 | TERRA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 127.4 |
| 5570bd90-b1ad-3ced-8fa8-547b4fd54b96 | -5.29454 | -43.71228 | 2026-07-02 00:03:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 26.7 |
| 93798603-d1d4-31a3-828d-e4ef21445ae1 | -6.25966 | -49.88746 | 2026-07-02 00:03:00 | TERRA_M-M | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 9ef735bd-6c7d-3101-a704-268773b7b2f1 | -5.29249 | -43.69814 | 2026-07-02 00:03:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 13.0 |
| c35e5551-e43c-3d22-9d4c-dcb6ea1842c1 | -6.51899 | -49.83358 | 2026-07-02 00:03:00 | TERRA_M-M | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 3dbac122-847f-3949-a1e1-94543536a9a8 | -5.80271 | -45.03708 | 2026-07-02 00:03:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| b3f93b08-4904-3539-a1f2-adaa79485833 | -4.34877 | -47.76615 | 2026-07-02 00:03:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 52.9 |
| 6e9dea0a-2426-35da-a75b-ea14c8b03c40 | -21.7823 | -56.2976 | 2026-07-02 00:10:00 | GOES-19 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 145.9 |
| 66b654dc-7760-398b-b9e3-94fd79a345b1 | -21.7827 | -56.2762 | 2026-07-02 00:10:00 | GOES-19 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 120.6 |
| 8fb9bbd4-d7bc-37f5-a252-7d8323d2653a | -3.5228 | -48.0383 | 2026-07-02 00:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 70.7 |
| b5e8420c-2101-3aec-be09-bf1ea1980724 | -10.9593 | -43.0326 | 2026-07-02 00:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 93.9 |
| 8e06644e-d742-330b-823f-3425f1b9b834 | -4.0046 | -48.0618 | 2026-07-02 00:10:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 74.2 |
| cce2a632-5dd5-35f2-8d5f-5abea289f410 | -21.7622 | -56.2795 | 2026-07-02 00:10:00 | GOES-19 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 71.5 |
| 7ed2c90a-e907-3b5c-90d2-c7c37bf494dd | -8.7208 | -48.3441 | 2026-07-02 00:10:00 | GOES-19 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 66.5 |
| 20108463-2f18-39e6-8ba9-26efe22b3a1e | -10.9588 | -43.0565 | 2026-07-02 00:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 92.0 |
| f1e9f9e3-b2f5-3a25-b32d-2b6f3e904334 | -10.9397 | -43.0593 | 2026-07-02 00:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 182.3 |
| fd012b85-50fd-3c5c-82ae-7906b2dd241a | -11.4147 | -56.0726 | 2026-07-02 00:10:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 66.2 |
| 83b38ecc-3113-32d0-a366-e35978a497ee | -10.9401 | -43.0355 | 2026-07-02 00:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 205.0 |
| f1171a33-32ab-3c14-87ca-3af058c799aa | -11.8007 | -57.0032 | 2026-07-02 00:10:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 64.3 |
| a9aa0018-39df-3945-a9e8-76df4df4b568 | -3.5043 | -48.039 | 2026-07-02 00:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 89.1 |
| c151c6f5-7c4f-366a-9c3f-12494da4e1a2 | -21.7617 | -56.301 | 2026-07-02 00:10:00 | GOES-19 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 83.2 |
| dc948d27-c6a4-3e2c-b8c5-d73ec7604d0c | -11.4149 | -56.0525 | 2026-07-02 00:10:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 70.4 |
| 2d76135e-434f-3bb8-b7d4-fd827eb801b8 | -12.5135 | -48.2802 | 2026-07-02 00:10:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 95.3 |
| 7aa5e945-90a4-3c79-905d-9f21f4c4e00d | -9.1933 | -45.3114 | 2026-07-02 00:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 52.8 |
| badb969b-0024-3e77-93bb-aba92515c347 | -10.9397 | -43.0593 | 2026-07-02 00:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 196.1 |
| 86a07d10-0932-3c51-aaf5-ff393f1b9c2d | -21.7823 | -56.2976 | 2026-07-02 00:20:00 | GOES-19 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 144.0 |


[Clique aqui para ver as próximas entradas](README3.md)
