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

## Dados Diários - Página 206

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d8e38687-730b-3963-9df1-788a1639291c | -3.49377 | -39.50437 | 2026-10-07 16:37:00 | NPP-375 | ITAPIPOCA | CEARÁ | Brasil | 2306405 | 23 | 33 | nan | nan | nan | Caatinga | 7.9 |
| daf42b85-0439-3c28-8c4c-41407fe81dbf | -8.72461 | -48.06842 | 2026-10-07 16:37:00 | NPP-375 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| f6b37eb6-2ebe-308f-ab75-81fc6ad6a1d3 | -8.58686 | -44.86432 | 2026-10-07 16:37:00 | NPP-375 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 146.9 |
| 0a63060c-3468-3953-bb6f-0377505537b6 | -7.17578 | -44.30504 | 2026-10-07 16:37:00 | NPP-375 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 55d526d4-692c-367d-bc71-5c0058dd5683 | -7.81529 | -44.5801 | 2026-10-07 16:37:00 | NPP-375 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 9.0 |
| b00a7f1e-d3ae-3c38-8585-a878d482cb0e | -3.42113 | -41.22339 | 2026-10-07 16:37:00 | NPP-375 | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 4.1 |
| f448e6be-849d-37b3-aa93-90eac6d0c8b4 | -7.21557 | -44.32666 | 2026-10-07 16:37:00 | NPP-375 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 7a5fd05c-2c78-32d4-8363-d333351ba8f6 | -14.9008 | -40.33216 | 2026-10-07 16:37:00 | NPP-375 | PLANALTO | BAHIA | Brasil | 2925006 | 29 | 33 | nan | nan | nan | Mata Atlântica | 19.1 |
| cd98b8f2-9548-30d5-b9b6-f203a6f6f45c | -6.81716 | -38.53521 | 2026-10-07 16:37:00 | NPP-375 | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 48.8 |
| 9ba73225-b45f-3aab-b236-43a1e6e50d7f | -14.80088 | -42.16071 | 2026-10-07 16:37:00 | NPP-375 | JACARACI | BAHIA | Brasil | 2917409 | 29 | 33 | nan | nan | nan | Caatinga | 5.2 |
| bf16dc2a-2030-3080-8360-0ed53891a90e | -5.24603 | -50.91492 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 43.5 |
| ad88141b-e8a6-3e3b-9ed0-b33b967167c2 | -5.90328 | -53.50352 | 2026-10-07 16:37:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 26.5 |
| 51dd8464-d00b-3c35-81d2-441704b7c581 | -3.77314 | -41.77509 | 2026-10-07 16:37:00 | NPP-375 | SÃO JOSÉ DO DIVINO | PIAUÍ | Brasil | 2210052 | 22 | 33 | nan | nan | nan | Caatinga | 12.0 |
| bb4b6592-8e5d-3b52-8cfe-d8f1645a6508 | -6.49965 | -43.97746 | 2026-10-07 16:37:00 | NPP-375 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 4b25548c-48d0-3590-870e-2fb182af7940 | -5.73987 | -41.73242 | 2026-10-07 16:37:00 | NPP-375 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 15.6 |
| 3bd70471-23e6-30eb-a2ba-c0ad714b8368 | -10.46198 | -46.83918 | 2026-10-07 16:37:00 | NPP-375 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 31516592-b472-39b4-a187-c8701221a6e7 | -6.22551 | -52.83567 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 6a3e3d14-033d-34cf-bed8-adc73f2746ef | -6.3689 | -42.91137 | 2026-10-07 16:37:00 | NPP-375 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 254cd45e-700d-3fc3-ad63-76da12f00138 | -9.0331 | -46.88066 | 2026-10-07 16:37:00 | NPP-375 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 38.5 |
| d684e3ef-9dac-3e49-a673-2be4c158b0c2 | -5.27139 | -47.91155 | 2026-10-07 16:37:00 | NPP-375 | SAMPAIO | TOCANTINS | Brasil | 1718808 | 17 | 33 | nan | nan | nan | Cerrado | 26.9 |
| 99d3ef44-db9b-36c8-9ee7-5136f4f02bcd | -14.31918 | -39.41328 | 2026-10-07 16:37:00 | NPP-375 | AURELINO LEAL | BAHIA | Brasil | 2902401 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 036374e4-1d4a-3067-9d53-f64479841c4b | -6.21547 | -52.83983 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 17.2 |
| d04d5b8e-b3d9-3796-b78a-e844d6ee6b8e | -17.24487 | -47.48219 | 2026-10-07 16:37:00 | NPP-375 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 65e2b818-05eb-3c6d-a262-38e5773e7eb5 | -6.81935 | -38.53856 | 2026-10-07 16:37:00 | NPP-375 | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 66.7 |
| d8b221a4-0416-3610-8432-1997a163e339 | -6.25098 | -53.45748 | 2026-10-07 16:37:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 19.1 |
| 43947152-7d37-3d8d-88c2-2b542d4aa24b | -6.32161 | -43.34644 | 2026-10-07 16:37:00 | NPP-375 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 13.8 |
| fad24781-1cea-32bc-b7d6-de3a5b5b98cf | -9.03191 | -46.89838 | 2026-10-07 16:37:00 | NPP-375 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 10.0 |
| d1b8cfd4-aef8-3656-ad1e-fe373104e8c3 | -3.40281 | -44.00041 | 2026-10-07 16:37:00 | NPP-375 | PRESIDENTE VARGAS | MARANHÃO | Brasil | 2109304 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| fc3af2cd-32a4-3eb3-bfc9-4c191627eb02 | -5.8797 | -45.96981 | 2026-10-07 16:37:00 | NPP-375 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| fd739f54-19e0-39b5-b949-b2ad7f23b955 | -7.08372 | -52.67844 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| d157257d-d2b2-3090-a56c-2c9ab9a33e2d | -7.00574 | -44.0573 | 2026-10-07 16:37:00 | NPP-375 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 7be10f64-6b38-3888-828c-74b9b08b5dd4 | -3.8044 | -42.22151 | 2026-10-07 16:37:00 | NPP-375 | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 27.3 |
| c38a3acc-6848-33bf-b7d1-67a72dca700a | -7.5033 | -45.77884 | 2026-10-07 16:37:00 | NPP-375 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 9ecaf352-eb0b-3d8f-a31a-980ff10602bb | -3.80465 | -40.45623 | 2026-10-07 16:37:00 | NPP-375 | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 16.9 |
| 6b2ca956-9a59-31a3-9261-2e6455c5fa09 | -7.87474 | -55.0091 | 2026-10-07 16:37:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 9b48b1fa-9904-373f-93ae-b23c95bf75c0 | -3.66057 | -45.34976 | 2026-10-07 16:37:00 | NPP-375 | SANTA INÊS | MARANHÃO | Brasil | 2109908 | 21 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 92bb29e8-ee3e-3074-855e-b1f530dc8531 | -8.31585 | -50.37526 | 2026-10-07 16:37:00 | NPP-375 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 64c5226f-c044-388d-9bad-f9f514942457 | -6.93659 | -45.27662 | 2026-10-07 16:37:00 | NPP-375 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 54336062-735e-3717-8fba-bc7ac1c5e534 | -5.74042 | -45.16012 | 2026-10-07 16:37:00 | NPP-375 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 77.0 |
| e0ebf74f-6020-3989-a10e-1139b43669ef | -10.1758 | -46.71502 | 2026-10-07 16:37:00 | NPP-375 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 25.1 |
| 6f45fbb9-091e-379a-8a81-9ccdb435d424 | -14.92537 | -41.82894 | 2026-10-07 16:37:00 | NPP-375 | CORDEIROS | BAHIA | Brasil | 2909000 | 29 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 715e4b33-6666-3c45-a183-d8ed367dbcdc | -4.21666 | -44.61259 | 2026-10-07 16:37:00 | NPP-375 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Cerrado | 29.0 |
| 1ece9d91-5ab6-34ec-9958-8bb28773479f | -4.69993 | -40.27795 | 2026-10-07 16:37:00 | NPP-375 | CATUNDA | CEARÁ | Brasil | 2303659 | 23 | 33 | nan | nan | nan | Caatinga | 8.4 |
| 6133cf35-089f-3d1b-bbd9-93c3c4995e13 | -7.29705 | -47.29141 | 2026-10-07 16:37:00 | NPP-375 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| cda6f1a6-b3ee-3d5a-a5c6-1efcd869b9dd | -9.96076 | -43.48568 | 2026-10-07 16:37:00 | NPP-375 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 20.0 |
| fe2b6f3e-a900-302d-a716-dcdbf974690a | -8.99271 | -45.93806 | 2026-10-07 16:37:00 | NPP-375 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 3923020f-0015-3100-a474-2cd4cb8fd611 | -6.83004 | -48.84164 | 2026-10-07 16:37:00 | NPP-375 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 0d15bf4b-1e73-350c-bcb0-23995a477797 | -5.87805 | -51.20167 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 71930a8a-2986-33c3-aa7c-4063e2beaced | -10.49236 | -47.29515 | 2026-10-07 16:37:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 25.5 |
| 7f42ccd7-e254-3279-aae0-294549dbe67f | -4.58557 | -40.77016 | 2026-10-07 16:37:00 | NPP-375 | IPUEIRAS | CEARÁ | Brasil | 2305902 | 23 | 33 | nan | nan | nan | Caatinga | 7.2 |
| 754284c9-f0d7-3a5e-a5a5-d6d89e1c5c00 | -3.8988 | -44.10061 | 2026-10-07 16:37:00 | NPP-375 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| e146c2d9-29b1-317f-96bb-0e754f777432 | -5.98647 | -40.94055 | 2026-10-07 16:37:00 | NPP-375 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 31.3 |
| 34cc83f9-bb4c-38ee-9607-0f45d7255b19 | -3.38773 | -42.71145 | 2026-10-07 16:37:00 | NPP-375 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 3dae31cb-4622-3843-a410-6a85921c8639 | -15.87736 | -40.75796 | 2026-10-07 16:37:00 | NPP-375 | ALMENARA | MINAS GERAIS | Brasil | 3101706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| b73566b0-009c-3807-8d1c-7b3b0d40ec26 | -6.61301 | -53.0215 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c2997ee3-3f1b-36d5-a25c-556c6cf6c3fd | -10.7598 | -46.71329 | 2026-10-07 16:37:00 | NPP-375 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| eaa8abf7-e0ee-3789-916d-8ce8be60dce8 | -9.94819 | -43.55931 | 2026-10-07 16:37:00 | NPP-375 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 232.2 |
| 86b1c884-490f-32d1-ad22-552baea8e6a7 | -10.78552 | -46.53584 | 2026-10-07 16:37:00 | NPP-375 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 12.9 |
| d0548acc-982c-3cff-925e-0b80f56e5254 | -9.67663 | -47.8996 | 2026-10-07 16:37:00 | NPP-375 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 431e8b42-f97e-3c56-a82d-3308b3f2190b | -5.57277 | -41.03621 | 2026-10-07 16:37:00 | NPP-375 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 6.4 |
| 73cf24f8-e040-3a81-b27b-b82ad2c353bc | -6.38604 | -45.049 | 2026-10-07 16:37:00 | NPP-375 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 02bca9f7-9ac5-329a-9bf6-c4953eb9e872 | -6.43877 | -44.84235 | 2026-10-07 16:37:00 | NPP-375 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 92776088-96b1-3ff3-9535-1de04edc7c95 | -3.76522 | -44.66339 | 2026-10-07 16:37:00 | NPP-375 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 20.0 |
| abf8741d-0416-3f0d-bbd1-6f40cb397313 | -4.7971 | -42.74969 | 2026-10-07 16:37:00 | NPP-375 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 46.2 |
| 24d8d7b2-8ad8-3813-86fe-13c12fce6175 | -7.39073 | -46.22345 | 2026-10-07 16:37:00 | NPP-375 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 23.6 |
| e8970de2-86de-362f-9f5a-9425a59c53cb | -7.88401 | -54.98404 | 2026-10-07 16:37:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 24.2 |
| 5c4742e1-72b1-3ae7-b205-4851ee174d10 | -6.59886 | -53.02783 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 25cd3611-f7c4-3d4b-ac06-c876e96fdc15 | -4.28379 | -44.65186 | 2026-10-07 16:37:00 | NPP-375 | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 61c93ba6-3cd7-374c-998e-d82054e16eea | -3.20651 | -42.8013 | 2026-10-07 16:37:00 | NPP-375 | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 84138d28-8c04-3a7c-97d6-93310d9cca75 | -5.83556 | -53.53409 | 2026-10-07 16:37:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| eb7fcb9f-1692-3156-be5d-4a7455030ae5 | -9.95815 | -43.55777 | 2026-10-07 16:37:00 | NPP-375 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 34.7 |
| 90a05904-6cd7-3bd8-877c-3866fe90ba92 | -6.14802 | -51.73541 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 29c71584-29da-32bb-9a7a-df33de93465b | -11.1088 | -47.59656 | 2026-10-07 16:37:00 | NPP-375 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 31.7 |
| 808274d1-e333-3139-8d42-5cb0a39ba363 | -4.28432 | -44.65532 | 2026-10-07 16:37:00 | NPP-375 | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b1b01fa8-fa97-34b8-8fd8-54c7eb45e82a | -11.49531 | -49.72237 | 2026-10-07 16:37:00 | NPP-375 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| e46c3b46-d4b9-377c-afe1-a3d190fd39b9 | -6.67964 | -52.95581 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 67e37a87-09d6-3169-8e44-0eaead2a96c4 | -5.69249 | -53.482 | 2026-10-07 16:37:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 36.2 |
| 5bdb8a0c-3e03-35a6-8cb9-ef3f4d91f338 | -6.81899 | -42.97785 | 2026-10-07 16:37:00 | NPP-375 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 8.3 |
| b82de22a-b625-3541-ac7e-cf3bf39ab6d9 | -9.88674 | -48.7409 | 2026-10-07 16:37:00 | NPP-375 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d6a3d8cf-d2c3-39a5-ab59-5212435ae5e7 | -10.52676 | -47.29016 | 2026-10-07 16:37:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 50.0 |
| 2a8dd900-c2ce-38e2-ac10-96a83dcc8d94 | -5.81449 | -53.8343 | 2026-10-07 16:37:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| a5146da6-0e45-396a-986e-f12638ab1681 | -6.36969 | -55.15572 | 2026-10-07 16:37:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| b8461d25-aebe-3816-bfe6-564e9c7f1a1e | -5.23262 | -50.90073 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| c4135ead-2917-3221-bd47-f3628ba0d3d4 | -7.22743 | -44.29271 | 2026-10-07 16:37:00 | NPP-375 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| c01e719f-9bfd-3c30-9ad6-7516f895d50f | -5.68307 | -44.27456 | 2026-10-07 16:37:00 | NPP-375 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 1b47688b-4cac-3a48-a3f5-0979e2f80cc5 | -11.01404 | -45.443 | 2026-10-07 16:37:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 33.8 |
| 11e10e63-0a41-36f3-b378-2ac84e7ada07 | -5.84917 | -53.47181 | 2026-10-07 16:37:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| c8deb603-b835-327c-b5e6-0e19248fc65f | -6.7025 | -44.01728 | 2026-10-07 16:37:00 | NPP-375 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 17.6 |
| 98a86bd4-237a-35a7-af38-d51c17e5aff6 | -6.06532 | -44.38412 | 2026-10-07 16:37:00 | NPP-375 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| b3eb700a-afb1-3bce-bb2e-c624c856fefa | -3.13642 | -40.07896 | 2026-10-07 16:37:00 | NPP-375 | MARCO | CEARÁ | Brasil | 2307809 | 23 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 689a9718-29cc-3595-a7f8-1e585e3b0517 | -11.11131 | -45.69289 | 2026-10-07 16:37:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 6a82d583-3a21-3364-aedf-72d82336cb64 | -14.70638 | -41.26465 | 2026-10-07 16:37:00 | NPP-375 | CARAÍBAS | BAHIA | Brasil | 2906899 | 29 | 33 | nan | nan | nan | Caatinga | 166.8 |
| 72aecd81-71e0-3332-b1ed-4059bd610144 | -5.9535 | -46.3675 | 2026-10-07 16:37:00 | NPP-375 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 0636a25b-abe3-36bd-9256-0223bf64bfe8 | -5.88444 | -52.50634 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c831879d-e308-374c-bea1-da03b0bf0bfa | -5.97392 | -40.95531 | 2026-10-07 16:37:00 | NPP-375 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 193.1 |
| 7407197d-68fa-3ec1-9602-73fc6d734d3a | -9.58416 | -48.91842 | 2026-10-07 16:37:00 | NPP-375 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 4c8eeb76-7cb8-3173-b2bf-a0134851ca89 | -9.51583 | -46.84731 | 2026-10-07 16:37:00 | NPP-375 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| d65ea1f9-deea-387b-98d3-0efa64369a57 | -6.91022 | -51.17266 | 2026-10-07 16:37:00 | NPP-375 | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| d5cf5948-440b-39df-95f6-8b31c1750a5f | -5.67895 | -42.58485 | 2026-10-07 16:37:00 | NPP-375 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 8.9 |
| a072b866-5b51-3f7a-a6c4-ef7630562e14 | -3.81081 | -42.21657 | 2026-10-07 16:37:00 | NPP-375 | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 40.2 |


[Clique aqui para ver as próximas entradas](README207.md)
