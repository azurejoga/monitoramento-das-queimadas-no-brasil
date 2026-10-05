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

## Dados Diários - Página 81

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 33f97000-4cfd-3646-b968-ab39f454d890 | -7.25365 | -37.26083 | 2026-10-05 16:37:00 | NOAA-21 | TEIXEIRA | PARAÍBA | Brasil | 2516706 | 25 | 33 | nan | nan | nan | Caatinga | 8.2 |
| 2c2d69e6-05bf-3404-94bf-8b3824f55c15 | -11.83449 | -43.53957 | 2026-10-05 16:37:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| c487ee14-8b8e-3f84-abb6-8b11b3fae3f2 | -7.54003 | -45.399 | 2026-10-05 16:37:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| ea490f54-cab5-37b1-88d7-61118c5be90e | -9.57107 | -46.8522 | 2026-10-05 16:37:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 7d3ecc10-3e36-3b08-8a42-22f7d991a0e0 | -7.57014 | -46.19707 | 2026-10-05 16:37:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| c035e760-c4b2-3719-8315-8d3faa645124 | -9.40946 | -47.30948 | 2026-10-05 16:37:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 74.0 |
| 211c3041-e2b6-370b-b17b-2a1477e48992 | -9.03532 | -45.17577 | 2026-10-05 16:37:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 43.7 |
| d149eeef-3417-30b6-a962-de2c186db369 | -9.77892 | -44.79559 | 2026-10-05 16:37:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 6ab125b7-5fa3-3603-b34e-d37262153504 | -11.9619 | -46.39591 | 2026-10-05 16:37:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| e72ed43f-0a49-3581-96c4-f38a1e176743 | -8.01127 | -38.78963 | 2026-10-05 16:37:00 | NOAA-21 | MIRANDIBA | PERNAMBUCO | Brasil | 2609303 | 26 | 33 | nan | nan | nan | Caatinga | 4.4 |
| a2e1b35c-61a2-31b4-a7a6-a96154068efb | -7.24418 | -39.26833 | 2026-10-05 16:37:00 | NOAA-21 | BARBALHA | CEARÁ | Brasil | 2301901 | 23 | 33 | nan | nan | nan | Caatinga | 29.2 |
| 5c307362-fff3-3f4d-acdb-e897d64995e0 | -8.54491 | -54.58541 | 2026-10-05 16:37:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| c74256f8-d515-3495-8e18-eab301b3ae3f | -6.80651 | -39.29928 | 2026-10-05 16:37:00 | NOAA-21 | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 15.2 |
| 6e8ed2e5-74c7-341b-b822-43b2630fd744 | -11.20406 | -47.13627 | 2026-10-05 16:37:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 9.8 |
| fc41aa9d-1473-353e-9852-4f781ca2de43 | -11.81054 | -43.52638 | 2026-10-05 16:37:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 430b5612-f155-39a2-9fd4-42f51e974382 | -12.56175 | -46.67832 | 2026-10-05 16:37:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 8966d9b5-57a2-3d6a-8229-27ef7bf6bf4c | -9.03355 | -45.16463 | 2026-10-05 16:37:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 69892cea-2173-3245-8b73-83d8201a32d6 | -11.23971 | -45.2632 | 2026-10-05 16:37:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.6 |
| c0fddeb2-28e2-3999-b62a-8aa292556732 | -11.36727 | -47.70988 | 2026-10-05 16:37:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 1ff5fd44-bf73-30ee-8b77-5f9edfe8ff09 | -13.6897 | -49.08797 | 2026-10-05 16:37:00 | NOAA-21 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 2fd27c0d-b582-3daa-bb44-067e76c1319a | -6.85815 | -38.68294 | 2026-10-05 16:37:00 | NOAA-21 | IPAUMIRIM | CEARÁ | Brasil | 2305704 | 23 | 33 | nan | nan | nan | Caatinga | 10.3 |
| 2390af43-ecb0-36af-bc7b-b4f1eb303f2f | -11.43896 | -47.68425 | 2026-10-05 16:37:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 31823f38-354d-3715-9d58-de384b49c475 | -7.18194 | -42.00433 | 2026-10-05 16:37:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 8.5 |
| d499acb4-52cb-3a59-870e-5e3c4f6d2a24 | -14.34122 | -47.09594 | 2026-10-05 16:37:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 083504dc-8c5c-383b-b7ee-ba9b7518fbcd | -11.21141 | -41.57702 | 2026-10-05 16:37:00 | NOAA-21 | JOÃO DOURADO | BAHIA | Brasil | 2918357 | 29 | 33 | nan | nan | nan | Caatinga | 10.1 |
| 53f29f78-fe6a-3311-a573-5407a1cc288a | -10.50916 | -46.05297 | 2026-10-05 16:37:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 6dfc3778-2f0e-3cf6-b2a9-7951064126cc | -10.97219 | -45.44302 | 2026-10-05 16:37:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 5f3e8799-d3aa-3878-9c5a-636dc19c3f84 | -13.5048 | -40.84392 | 2026-10-05 16:37:00 | NOAA-21 | IRAMAIA | BAHIA | Brasil | 2914307 | 29 | 33 | nan | nan | nan | Caatinga | 35.1 |
| 36177501-a7ce-326a-950d-b8e71daccbea | -12.24369 | -51.22766 | 2026-10-05 16:37:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e933185d-4058-347d-b479-055c4e0baee0 | -10.6881 | -54.17268 | 2026-10-05 16:37:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 15a6aed0-e1a3-38b8-b8cd-cfd378de4cce | -11.19933 | -46.27532 | 2026-10-05 16:37:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| fa92f6d4-728f-3aef-8ad6-e72640cb20da | -9.02675 | -45.16576 | 2026-10-05 16:37:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 1e39ca00-8222-313b-b938-34e45c7801dc | -6.92433 | -44.56331 | 2026-10-05 16:37:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 7bf1b066-881a-324b-8c52-374969df613c | -8.53873 | -54.57585 | 2026-10-05 16:37:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| a0f60e40-4643-3fa4-adcc-b610f145e48c | -9.76641 | -44.80534 | 2026-10-05 16:37:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 2992945f-a013-3e35-ae55-eb79d499e5d3 | -9.62434 | -47.69962 | 2026-10-05 16:37:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 823440dd-21a9-38e3-9c51-dcb8ef2d2eb3 | -12.08641 | -43.41442 | 2026-10-05 16:37:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 17.1 |
| fe0774f3-99d5-36ff-adf7-f5eab5dfd369 | -6.92725 | -44.5587 | 2026-10-05 16:37:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 39b1bb69-e4dd-36a5-bdf9-b52592d51d4b | -7.55792 | -39.08694 | 2026-10-05 16:37:00 | NOAA-21 | PORTEIRAS | CEARÁ | Brasil | 2311108 | 23 | 33 | nan | nan | nan | Caatinga | 9.3 |
| 28cedc2a-e6e7-30a5-8c3c-711fe8eaf174 | -9.81154 | -44.80195 | 2026-10-05 16:37:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 16.4 |
| e792754d-e3e6-383b-82c9-61cfeca9f281 | -10.97163 | -45.43945 | 2026-10-05 16:37:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.8 |
| d31de51e-3d73-3341-8ce6-2f26970bb372 | -13.78595 | -43.50776 | 2026-10-05 16:37:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 66e4b0f6-9a6a-3e07-9eda-03356099ff6b | -7.0236 | -43.42852 | 2026-10-05 16:37:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 26.0 |
| 82b81799-c694-3d9e-bca6-f272cfe45daa | -12.35111 | -47.06408 | 2026-10-05 16:37:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| ce1c0518-3a9f-3e35-9f3a-2d622df87b7c | -7.18031 | -39.73147 | 2026-10-05 16:37:00 | NOAA-21 | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 53a345b8-c109-3969-8806-ca5122f0b6fe | -6.99696 | -43.21764 | 2026-10-05 16:37:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 12.3 |
| cea9e56a-cab9-349d-b457-023618b055ba | -10.40448 | -47.53417 | 2026-10-05 16:37:00 | NOAA-21 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 12.5 |
| fb88eede-8f7d-33e1-a850-1c91ca50441d | -18.00584 | -39.73017 | 2026-10-05 16:37:00 | NOAA-21 | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 6.2 |
| 5faf65ad-1309-3994-abfa-0c20bdc7e252 | -6.70695 | -45.2335 | 2026-10-05 16:37:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 117.6 |
| 999c4165-c9af-3733-8897-0d73e4afa808 | -9.40999 | -47.31297 | 2026-10-05 16:37:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 74.0 |
| e1f09f4f-ccb3-3ef2-ade9-6be1ffa8d8e4 | -11.72676 | -43.50256 | 2026-10-05 16:37:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 1166a87b-67ca-30d4-b346-d99f1c6020c3 | -11.27837 | -44.29172 | 2026-10-05 16:37:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 373.6 |
| 79f73f0e-5dd4-3b4a-bad8-6dd658ffe5e2 | -11.74315 | -43.42413 | 2026-10-05 16:37:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 12.1 |
| c0395c97-0669-3916-b048-82dca7c00e2b | -9.74901 | -48.1698 | 2026-10-05 16:37:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 9ccd3722-6a1b-32e0-93af-5e5d86151fe9 | -6.7116 | -45.24061 | 2026-10-05 16:37:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 206.8 |
| e8a96685-930e-35d9-a6f3-7c1e8b52e276 | -12.04726 | -43.44221 | 2026-10-05 16:37:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 00782e30-d6fe-351d-a42e-78a3f6bc943d | -11.81474 | -43.52985 | 2026-10-05 16:37:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 10.5 |
| d2e0e9e0-e5a1-393b-981b-5e6d052cb3b9 | -6.92017 | -38.33205 | 2026-10-05 16:37:00 | NOAA-21 | NAZAREZINHO | PARAÍBA | Brasil | 2510006 | 25 | 33 | nan | nan | nan | Caatinga | 6.9 |
| a152a598-1ff2-32be-9d5e-2bfbe3ea9ec2 | -10.95825 | -45.39758 | 2026-10-05 16:37:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 14.7 |
| bc02df00-8f58-31f6-9be5-a9a7a5a535c2 | -6.33935 | -42.54736 | 2026-10-05 16:37:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 7.2 |
| a4841938-fd05-3fc2-8764-458603e13901 | -6.72603 | -44.27752 | 2026-10-05 16:37:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 68.0 |
| ba80c1e8-ca12-3fab-8fa0-754596868c57 | -9.62382 | -47.69608 | 2026-10-05 16:37:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b60784a3-8454-3f3f-98ba-4be05c97b669 | -10.97497 | -45.43891 | 2026-10-05 16:37:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 25.5 |
| cac2d019-aa8b-38fd-ba85-3d2d584be3c9 | -8.66031 | -54.57258 | 2026-10-05 16:37:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 14.8 |
| 483ad928-0d15-30f8-8ffe-fbcc1b623df8 | -8.02654 | -46.97403 | 2026-10-05 16:37:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 1b31d382-1768-37b7-a194-9f37cc3c668f | -11.01171 | -53.99804 | 2026-10-05 16:37:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 11.0 |
| cd5d7e49-6653-317e-b821-07732b97a22b | -11.68605 | -43.65397 | 2026-10-05 16:37:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 2c2172c9-ec74-3820-8ccb-446e10d0a2d7 | -6.80481 | -39.28932 | 2026-10-05 16:37:00 | NOAA-21 | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 8c64cd82-e189-39f3-b5d0-efe31c44a20f | -11.15883 | -43.49295 | 2026-10-05 16:37:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 17.0 |
| a6c34019-7b03-3c2f-9e6b-6e03d90162b7 | -11.01856 | -41.27834 | 2026-10-05 16:37:00 | NOAA-21 | VÁRZEA NOVA | BAHIA | Brasil | 2933158 | 29 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 055a39ba-5673-354f-9a63-793b753e2f78 | -8.54591 | -54.58731 | 2026-10-05 16:37:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| d9681c73-90cb-3123-9318-2a31cb040e46 | -8.78027 | -47.5518 | 2026-10-05 16:37:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 0c26699b-a9e3-38cd-a92e-adea612b3e26 | -11.64206 | -43.62808 | 2026-10-05 16:37:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 87bae89a-5050-3ec3-8211-3020016c4c8f | -10.96717 | -45.41083 | 2026-10-05 16:37:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 9.8 |
| a642acdb-9ddc-37ce-8c39-e4b9a4ac4327 | -7.14424 | -44.69314 | 2026-10-05 16:37:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 10.4 |
| db08c88f-8c7d-37c6-b359-3038a1f40523 | -8.66095 | -54.57037 | 2026-10-05 16:37:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 16.1 |
| 676d8b4b-be79-33fc-a91b-979a1ec6d11f | -12.23969 | -51.22821 | 2026-10-05 16:37:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ea35359b-db5f-31fa-b7dc-60ee242bc5b8 | -17.92196 | -39.42503 | 2026-10-05 16:37:00 | NOAA-21 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 8.1 |
| b61cc335-cfc2-3eb3-a7b6-f619ce900a4a | -9.91754 | -47.59234 | 2026-10-05 16:37:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6bb2b895-ed66-3cf3-801e-453141b86bd5 | -9.82475 | -44.79647 | 2026-10-05 16:37:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 5.9 |
| f4cc8b22-a7f5-3759-a2bb-841a0675da54 | -7.25058 | -37.25889 | 2026-10-05 16:37:00 | NOAA-21 | TEIXEIRA | PARAÍBA | Brasil | 2516706 | 25 | 33 | nan | nan | nan | Caatinga | 6.9 |
| b9f6d109-7781-3e63-a4f5-434916786b49 | -11.6414 | -43.62404 | 2026-10-05 16:37:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.7 |
| a54953fb-2189-3e61-9b37-ac840b7e9e85 | -6.90608 | -40.41251 | 2026-10-05 16:37:00 | NOAA-21 | CAMPOS SALES | CEARÁ | Brasil | 2302701 | 23 | 33 | nan | nan | nan | Caatinga | 3.0 |
| f617042c-f934-3c4e-9cdd-946b7c1653a2 | -6.64875 | -43.77513 | 2026-10-05 16:37:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 66d0d06c-14a3-3cff-8e70-2443094c807b | -11.83165 | -43.54435 | 2026-10-05 16:37:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 78.2 |
| d0b371fe-3c3f-3125-a092-b4208dae8cae | -11.34843 | -46.67427 | 2026-10-05 16:37:00 | NOAA-21 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 4a2860b1-605a-31a0-82d7-39eec67a6fff | -8.54968 | -54.58481 | 2026-10-05 16:37:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 21.1 |
| ef73568c-7ebe-3216-a8b8-6a369bb846a7 | -11.6851 | -43.67055 | 2026-10-05 16:37:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 21551eb6-3acc-3982-a4db-7eb63eadf896 | -9.9413 | -45.50809 | 2026-10-05 16:37:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 11.9 |
| ed77f894-79bf-3f4f-8f30-93c8de51fd08 | -11.55753 | -41.74048 | 2026-10-05 16:37:00 | NOAA-21 | LAPÃO | BAHIA | Brasil | 2919157 | 29 | 33 | nan | nan | nan | Caatinga | 9.7 |
| b1e685c6-4db7-3aef-afea-279012adb937 | -11.8225 | -43.53283 | 2026-10-05 16:37:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 4c791437-9875-3458-879b-7fa04a56f4dc | -11.81275 | -47.36843 | 2026-10-05 16:37:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 10.5 |
| a3a92c97-d25d-334a-9ad8-49da86f88b20 | -9.70952 | -39.65865 | 2026-10-05 16:37:00 | NOAA-21 | CURAÇÁ | BAHIA | Brasil | 2909901 | 29 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 8a7eeb30-d138-384c-8707-bc3266949f4b | -9.03414 | -45.16835 | 2026-10-05 16:37:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 12.9 |
| d77874c5-e597-377b-9365-abc61389b706 | -6.1163 | -38.32917 | 2026-10-05 16:37:00 | NOAA-21 | ENCANTO | RIO GRANDE DO NORTE | Brasil | 2403301 | 24 | 33 | nan | nan | nan | Caatinga | 43.2 |
| f5035d0d-fa4f-3201-b6f4-10310a656db2 | -7.94746 | -43.84863 | 2026-10-05 16:37:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 56273803-c7d5-3a34-a81c-ace170ef7174 | -11.7168 | -43.50842 | 2026-10-05 16:37:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 20.7 |
| 6ee80083-b732-306b-af36-abeedf68ea15 | -8.52801 | -54.60345 | 2026-10-05 16:37:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 37.1 |
| cba39b33-ecd7-3c8c-ae4e-243d7dd8dcc8 | -6.60731 | -41.57234 | 2026-10-05 16:37:00 | NOAA-21 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 35.7 |
| 1d5d71c4-2306-3d8c-a960-6c073338bfb8 | -7.73061 | -45.47518 | 2026-10-05 16:37:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |


[Clique aqui para ver as próximas entradas](README82.md)
