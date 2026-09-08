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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ee1d14eb-f6e3-35ba-8e7f-d483a5a79747 | -2.97345 | -47.33803 | 2026-09-08 04:08:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7d92ca50-7404-382e-b910-c211b1b03318 | -9.71301 | -43.46327 | 2026-09-08 04:08:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 6124d2f7-2d40-3052-af5c-a872a510a67f | -7.67406 | -46.04674 | 2026-09-08 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1a3de479-8f1d-39b8-a7c1-dc14d223ab54 | -2.86835 | -41.74128 | 2026-09-08 04:08:00 | NOAA-21 | PARNAÍBA | PIAUÍ | Brasil | 2207702 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0e1f7e41-98be-3965-ac53-e878fd1ed3de | -9.76193 | -43.47845 | 2026-09-08 04:08:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 77cef3b2-63e0-3cdc-9ad8-4189806a526d | -9.74411 | -43.4829 | 2026-09-08 04:08:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 7a63a08b-867a-3191-bdb4-709afa44f5f9 | -5.78061 | -47.16875 | 2026-09-08 04:08:00 | NOAA-21 | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0ccdc19c-71d5-3b71-a875-4e29457d2539 | -9.70462 | -43.47288 | 2026-09-08 04:08:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 092c00cf-f78d-3037-9dea-967debbfe5d0 | -6.16957 | -47.08379 | 2026-09-08 04:08:00 | NOAA-21 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 265598db-ebef-3766-aa70-9e16af669f5f | -7.61121 | -47.28915 | 2026-09-08 04:08:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 40ed5eae-247c-3ad0-bcc6-a930a4a4287e | -7.66948 | -46.05083 | 2026-09-08 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 19.8 |
| b978eeae-5db8-337f-b641-831742ce412a | -9.71088 | -43.43378 | 2026-09-08 04:08:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 14.5 |
| e418471e-b89d-34c8-a6a1-97b97db21f2e | -2.87891 | -50.46134 | 2026-09-08 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9140a4e9-ac68-3583-92d5-c03a9180979a | -9.71031 | -43.43732 | 2026-09-08 04:08:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 7.1 |
| a1eca464-bf6c-30b1-8950-5ba700212f01 | -4.11303 | -49.06517 | 2026-09-08 04:08:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| e667b9bf-ca43-3b59-a61d-7cb988d5c208 | -5.15815 | -42.75163 | 2026-09-08 04:08:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 61878b5c-2c4b-3e41-9c29-6baeee55f640 | -3.2464 | -47.24508 | 2026-09-08 04:08:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e54e1f5c-ee45-32ce-ab95-833576e5d9f1 | -8.27889 | -46.38123 | 2026-09-08 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4a1b7bbc-0098-33dc-a523-f69d196bb9b6 | -2.96765 | -49.55855 | 2026-09-08 04:08:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 07c942cb-f6ba-3901-aa5c-f3d7c7db4a5c | -4.78087 | -44.40152 | 2026-09-08 04:08:00 | NOAA-21 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f23dbbb0-8223-3a6b-b354-be7e484923d0 | -9.72685 | -43.48378 | 2026-09-08 04:08:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a0c2570b-b629-3c18-9385-33be2fe960e2 | -9.74745 | -43.48344 | 2026-09-08 04:08:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 94a1a505-c330-3efa-bd38-1a6146844028 | -9.73737 | -43.50372 | 2026-09-08 04:08:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 526c39d9-154e-3cc5-b853-6a29d2388831 | -2.83392 | -48.65056 | 2026-09-08 04:08:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 8684b6ac-ffb6-357a-940e-11db02a18a92 | -4.98031 | -50.6429 | 2026-09-08 04:08:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f43cf56c-89b8-3cc4-8001-fd1b57182c10 | -7.61183 | -47.28547 | 2026-09-08 04:08:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e3576ea0-2896-36e8-89f2-e67565f5b0b2 | -9.71577 | -43.46737 | 2026-09-08 04:08:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4bbbc301-309e-3ff1-b770-aba55b4f5bef | -4.03888 | -50.8764 | 2026-09-08 04:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| bc843b0b-def5-3676-a299-92fe744f4859 | -2.98083 | -49.26711 | 2026-09-08 04:08:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 6df8679b-12d7-3474-ae68-403dc84302a8 | -6.38576 | -43.74976 | 2026-09-08 04:08:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3ffbb779-25b1-3f75-a9bf-81eb91cf1fc6 | -9.72826 | -43.3892 | 2026-09-08 04:08:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 9.6 |
| 35629d23-e190-3d09-a004-9f8279072738 | -9.29924 | -44.3508 | 2026-09-08 04:08:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 3cdc810d-61e7-30f9-adf8-263a790036c8 | -2.63481 | -46.77307 | 2026-09-08 04:08:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3396583c-2dfc-3f00-a5ba-e322a55bdaf0 | -10.25381 | -40.47814 | 2026-09-08 04:08:00 | NOAA-21 | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 0d6b7af0-8a58-383f-becd-75d962153a6e | -7.67026 | -46.04614 | 2026-09-08 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 352e58ed-0000-376f-b11f-1550ea2d9090 | -9.70519 | -43.46932 | 2026-09-08 04:08:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 6b53cb6e-729f-323c-a21f-804d16e6bb48 | -2.83305 | -48.65593 | 2026-09-08 04:08:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 85b35b1c-1935-3c36-8c37-dcfed4f21234 | -3.44534 | -47.27188 | 2026-09-08 04:08:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 5e8a9a22-934a-3d50-b5e3-d0e7d98da9a0 | -6.41633 | -46.60841 | 2026-09-08 04:08:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d8872e07-e3b3-3bea-8c1f-1600384b605d | -8.73156 | -36.89555 | 2026-09-08 04:08:00 | NOAA-21 | PEDRA | PERNAMBUCO | Brasil | 2610806 | 26 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 24059f16-75ce-3b62-b21b-589063857715 | -2.75475 | -49.47694 | 2026-09-08 04:08:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c30aeda6-3e54-35a3-ba11-c866f90d0281 | -6.02904 | -42.64474 | 2026-09-08 04:08:00 | NOAA-21 | SÃO GONÇALO DO PIAUÍ | PIAUÍ | Brasil | 2209807 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 1f767c8c-57f9-304f-96b7-3b5305fba908 | -9.71365 | -43.43785 | 2026-09-08 04:08:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 81a29e40-93a9-35f8-9233-7ddafaae763e | -4.04567 | -50.87004 | 2026-09-08 04:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| eac08f85-b44d-3b5c-93aa-f74508f95640 | -9.71081 | -43.4556 | 2026-09-08 04:08:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 94792c10-93fe-3d7d-8ace-072fcf04eb96 | -9.75576 | -43.49572 | 2026-09-08 04:08:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 72380891-db04-351a-b37b-23e08c6b12de | -6.61987 | -44.72047 | 2026-09-08 04:08:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a713d569-1f08-3c27-bee2-bf9477a7d24c | -2.95819 | -48.70505 | 2026-09-08 04:08:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2006bfe3-d057-3383-9079-e1cf1bccdf4d | -3.03098 | -41.80995 | 2026-09-08 04:08:00 | NOAA-21 | PARNAÍBA | PIAUÍ | Brasil | 2207702 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| cade5f8a-8edc-334e-b808-5bf739780dfa | -5.49618 | -48.17109 | 2026-09-08 04:08:00 | NOAA-21 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c9d474c4-d6d2-36ee-89b0-5aa984f77494 | -3.26737 | -50.02623 | 2026-09-08 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d501af98-5ee1-3912-ab74-76e82bb5c904 | -7.3724 | -47.01656 | 2026-09-08 04:08:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| c95cfd08-2340-3929-8a06-fc44472215e3 | -9.7609 | -43.44186 | 2026-09-08 04:08:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 406e03d7-dcfd-37d1-80ce-8fbbb686414a | -4.97133 | -44.89388 | 2026-09-08 04:08:00 | NOAA-21 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1018e524-bd06-3825-898a-6f9243e8d0f2 | -9.72578 | -43.469 | 2026-09-08 04:08:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 0d09ebb3-1d2d-3a5a-9a68-62e648c6282e | -9.73416 | -43.45941 | 2026-09-08 04:08:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c7f5a15d-8d92-3b94-9ce4-be84aea6c3a1 | -6.61629 | -44.71994 | 2026-09-08 04:08:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 35eab5a6-f730-3d4e-8795-2e2986342106 | -9.77096 | -43.4216 | 2026-09-08 04:08:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| d2f5ea32-f660-39de-8cbb-d8ffa287e375 | -2.63052 | -46.77237 | 2026-09-08 04:08:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 58627ff0-04c8-39ab-9d5a-153ce379c7e1 | -6.03238 | -42.64527 | 2026-09-08 04:08:00 | NOAA-21 | SÃO GONÇALO DO PIAUÍ | PIAUÍ | Brasil | 2209807 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 5712d4a2-10cf-345e-8277-d510d8e57030 | -5.89162 | -49.06761 | 2026-09-08 04:08:00 | NOAA-21 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 412b295b-747d-3869-afaf-17d328a4ff73 | -9.76819 | -43.4175 | 2026-09-08 04:08:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0bb85a65-3d05-3452-8b5c-16a81bf35155 | -3.32431 | -44.59221 | 2026-09-08 04:08:00 | NOAA-21 | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 679969e4-ee2b-3ac3-88b5-142e6d1d8d77 | -9.74858 | -43.47632 | 2026-09-08 04:08:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8062cd01-ee1e-3d26-aa31-0acdd8dcb648 | -6.16893 | -47.0875 | 2026-09-08 04:08:00 | NOAA-21 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 62.1 |
| 668f11c0-8a84-3691-867d-2ac8ccaae038 | -9.74071 | -43.50425 | 2026-09-08 04:08:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 16949324-38f6-3541-afb5-addc587085e3 | -3.24201 | -47.2444 | 2026-09-08 04:08:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 8e386b6e-eb3b-3dff-af30-57c81ba4e450 | -4.10813 | -49.06436 | 2026-09-08 04:08:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 23dedcdb-5ec6-3024-8067-4102f06b32f3 | -9.71195 | -43.44848 | 2026-09-08 04:08:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| b1edcc06-27f3-329e-82ef-6b0919efd6fc | -1.87031 | -47.98376 | 2026-09-08 04:08:00 | NOAA-21 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 6b4dff83-0444-3f19-8709-4cd606458466 | -6.38233 | -43.74921 | 2026-09-08 04:08:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1a57ba3b-de04-300c-9baf-8b5835e63a2f | -2.63706 | -46.77684 | 2026-09-08 04:08:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1e96e3fa-444b-3a9a-ab74-0b8011c35cc2 | -7.56178 | -47.81677 | 2026-09-08 04:08:00 | NOAA-21 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0a6b8b8b-605e-3ece-b0a6-b4af82e6caad | -3.06626 | -49.51884 | 2026-09-08 04:08:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 967c47e3-6546-33dd-b38e-b94936b57d1d | -4.05055 | -50.87476 | 2026-09-08 04:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 89d7c8e3-b314-3b26-9dea-f112a49b2705 | -2.97936 | -49.26974 | 2026-09-08 04:08:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| bece7e39-9082-3eca-9f9f-f3faaf92290a | -9.76763 | -43.42107 | 2026-09-08 04:08:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 24bc3d09-fed6-3fef-961b-b0f471c73788 | -9.71144 | -43.43024 | 2026-09-08 04:08:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 14.5 |
| 4e4964db-027d-36eb-aa08-9331b2dbab58 | -4.05118 | -50.87109 | 2026-09-08 04:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7118da0a-846f-3595-9869-c8ca74e1eb5e | -9.71933 | -43.40232 | 2026-09-08 04:08:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 11.6 |
| d5218a21-740d-306f-8c75-a6dea49dfbe7 | -2.03432 | -48.57938 | 2026-09-08 04:08:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d16f687e-544d-39cd-9fe3-f105b816d8c7 | -9.31371 | -40.20657 | 2026-09-08 04:08:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 7669c714-485b-3ec1-9bbe-3dc9915004e9 | -8.27969 | -46.37648 | 2026-09-08 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 09e2ea48-21b2-3de0-b72e-8c9bfd7d8648 | -2.63774 | -46.77275 | 2026-09-08 04:08:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| db9626b6-f911-33ad-a802-2288d7e1a891 | -2.96093 | -48.70734 | 2026-09-08 04:08:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f2c5e5d4-80fd-3b59-bca5-e9e3b03d01f4 | -9.7385 | -43.4966 | 2026-09-08 04:08:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8353e4ac-0fb4-35fa-a704-05d691c0817b | -3.54933 | -48.18197 | 2026-09-08 04:08:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 72.8 |
| 18c84a58-e16b-3455-b47b-e95473575b4e | -9.76414 | -43.48611 | 2026-09-08 04:08:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 8be1bdb9-66ba-3b60-b57c-34a251e81049 | -7.37278 | -47.01776 | 2026-09-08 04:08:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| badfcdc9-ce5a-3f99-86fa-0061ee87dc4c | -3.27268 | -50.02707 | 2026-09-08 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5cd888f3-8c44-38c0-bef0-d7945ac749ae | -4.98627 | -50.64035 | 2026-09-08 04:08:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 33d5bec9-dd06-324e-86ff-f32a8c20c113 | -3.55013 | -48.1771 | 2026-09-08 04:08:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 72.8 |
| b97495b8-f44a-3d9a-8366-2c19b5e81c6e | -9.32059 | -40.20763 | 2026-09-08 04:08:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 48.8 |
| 29f44ab5-8d5d-3e23-ba33-151a4342ea45 | -9.76532 | -43.45714 | 2026-09-08 04:08:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 05cac410-d07a-3b6f-bf68-35ba1a114472 | -5.6217 | -44.25087 | 2026-09-08 04:08:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5a0e4685-e5e8-3a5d-aac5-e243466c028e | -4.04993 | -50.87843 | 2026-09-08 04:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7dbf27bc-52a8-38a9-b2dd-bef4b0a65c7a | -3.55479 | -48.1778 | 2026-09-08 04:08:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 69280949-7bdb-3ce6-a6c0-8ef9ecff6d2e | -3.54467 | -48.18129 | 2026-09-08 04:08:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 72.8 |
| 60707acd-466b-3f58-979d-4ec627849246 | -2.63346 | -46.77206 | 2026-09-08 04:08:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 59fb5105-424c-3def-9070-45e133b78a23 | -3.06576 | -49.52186 | 2026-09-08 04:08:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |


[Clique aqui para ver as próximas entradas](README12.md)
