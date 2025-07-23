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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ad806e8d-c2dd-3564-8f12-6b0f55af03d8 | -3.94761 | -41.48859 | 2025-07-23 04:32:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 8f2fd67c-f60e-3b7c-8511-94ab3c4d77a8 | -5.35911 | -36.89754 | 2025-07-23 04:32:00 | NOAA-21 | CARNAUBAIS | RIO GRANDE DO NORTE | Brasil | 2402501 | 24 | 33 | nan | nan | nan | Caatinga | 2.8 |
| d468b007-f8fe-3065-8fa0-48c9a3b4ef28 | -6.02661 | -44.04352 | 2025-07-23 04:32:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0d023d05-b64c-3122-b972-2447adb5d696 | -3.20255 | -49.16872 | 2025-07-23 04:32:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 48337386-b256-3218-82b7-ed9e1d92cc13 | -4.64032 | -45.60161 | 2025-07-23 04:32:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 17d6201e-6e39-3c46-b45a-3b566bd64eef | -6.18821 | -44.38707 | 2025-07-23 04:32:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| feafed99-3e90-3306-b6fd-28f3e76e6776 | -3.17908 | -49.44711 | 2025-07-23 04:32:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 54566f25-9c7d-3188-a95c-301c27ae7d69 | -4.08997 | -46.928 | 2025-07-23 04:32:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| d3007a78-8683-3bc8-a2aa-b355ca04c08a | -5.3651 | -36.89842 | 2025-07-23 04:32:00 | NOAA-21 | CARNAUBAIS | RIO GRANDE DO NORTE | Brasil | 2402501 | 24 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 1ccff88f-3dc5-3650-816a-68562fd235eb | -5.83285 | -44.10349 | 2025-07-23 04:32:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| dfbf7bae-26d0-3324-a45a-4ed992b9a278 | -6.94464 | -43.95998 | 2025-07-23 04:32:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 29091767-f968-31bc-940d-03a3763c7c36 | -3.03549 | -49.42562 | 2025-07-23 04:32:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 666a59a8-db64-325b-9910-05d38292ed5a | -3.75108 | -49.04853 | 2025-07-23 04:32:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ecf0770c-de40-3ca0-acc4-c9fafd9874cb | -2.92173 | -48.2405 | 2025-07-23 04:32:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9d744b60-ef27-3ee8-852c-268a57a16262 | -5.6871 | -43.67573 | 2025-07-23 04:32:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 1f55341a-3396-359b-bb4e-a7748c421b9d | -6.85186 | -42.80354 | 2025-07-23 04:32:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| f6bb73b5-96b2-3124-b4cc-c905339880a0 | -3.17727 | -49.45844 | 2025-07-23 04:32:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 39.5 |
| 0e9694ac-b80e-3b4a-9e87-64f0c1085ccc | -4.77918 | -45.34061 | 2025-07-23 04:32:00 | NOAA-21 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3831391c-c499-30ab-a7fb-4a649d08bade | -6.93386 | -43.95351 | 2025-07-23 04:32:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d8fb0df7-fc5e-3553-ba97-1e521f422885 | -5.83658 | -44.10405 | 2025-07-23 04:32:00 | NOAA-21 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e57cc295-d26e-3b1c-97eb-a7073ffe42d8 | -5.83458 | -44.10631 | 2025-07-23 04:32:00 | NOAA-21 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7f64a7b3-558a-3461-9e88-5aa538629db7 | -3.59089 | -41.65226 | 2025-07-23 04:32:00 | NOAA-21 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 9ba38b09-f9bf-39d6-a496-131ff4d6eba0 | -3.58667 | -41.65162 | 2025-07-23 04:32:00 | NOAA-21 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 33878483-dc75-3e07-be99-4b10a17f687e | -4.89942 | -44.96344 | 2025-07-23 04:32:00 | NOAA-21 | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e15dbed1-294c-3ef1-8eb1-13fe33d46779 | -3.04307 | -47.38042 | 2025-07-23 04:32:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0936eb18-c4ae-38e5-a630-f5601b8527e6 | -5.67973 | -43.66648 | 2025-07-23 04:32:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f7cf3387-7178-3f8f-b547-156fd1b62b6e | -4.1046 | -48.20456 | 2025-07-23 04:32:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ee4de56d-2958-3fb1-aa05-d322df6c0422 | -6.93647 | -44.30772 | 2025-07-23 04:32:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fc37f182-a1b1-33d3-b3e7-54f1aa09675f | -5.68737 | -43.66771 | 2025-07-23 04:32:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 2308ee06-924d-3df6-b07d-f919e8bd04d5 | -3.32255 | -48.71964 | 2025-07-23 04:32:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 74083ec3-2fa8-3644-8e53-4c1c53dcf70b | -3.82645 | -43.02328 | 2025-07-23 04:32:00 | NOAA-21 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f7f969ec-8643-3308-9bbf-c6a397c238cd | -6.61094 | -42.40757 | 2025-07-23 04:32:00 | NOAA-21 | ARRAIAL | PIAUÍ | Brasil | 2201002 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 4238cdbc-e060-36ff-8684-0c0cea789704 | -3.13124 | -47.01441 | 2025-07-23 04:32:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 73c8c599-151b-3120-b114-0c0221fb56c9 | -3.47495 | -39.57288 | 2025-07-23 04:32:00 | NOAA-21 | ITAPIPOCA | CEARÁ | Brasil | 2306405 | 23 | 33 | nan | nan | nan | Caatinga | 5.3 |
| cc3fc277-bdde-35c1-b0ac-23f07cb9b987 | -5.65742 | -44.15836 | 2025-07-23 04:32:00 | NOAA-21 | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 599a4b39-1855-30ac-af6a-bc34a419cba7 | -5.68328 | -43.67512 | 2025-07-23 04:32:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| c98101aa-773c-3fb6-b9cc-154eac6843a2 | -5.51137 | -47.49704 | 2025-07-23 04:32:00 | NOAA-21 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fc503893-788c-3e8a-b354-6ae44e760f97 | -5.67709 | -43.66446 | 2025-07-23 04:32:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| de4e7fb2-a507-3494-85dc-7f7ee685cf4e | -6.93498 | -43.952 | 2025-07-23 04:32:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ef45bb06-522d-3f39-8b0d-16539cabff1a | -5.36246 | -36.89389 | 2025-07-23 04:32:00 | NOAA-21 | CARNAUBAIS | RIO GRANDE DO NORTE | Brasil | 2402501 | 24 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 02823f1f-20c9-317d-9dba-44c793edeadb | -5.89155 | -45.20259 | 2025-07-23 04:32:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5d3fa6ab-8dae-3370-97fe-b54f675ef7b2 | -3.03626 | -47.85913 | 2025-07-23 04:32:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 768bfd99-4ecf-34fe-9886-eab40f7348d4 | -5.72512 | -44.50539 | 2025-07-23 04:32:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| aa12ea17-a516-35ae-ab31-e425bb536035 | -5.68781 | -43.67104 | 2025-07-23 04:32:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 16942cd2-de50-32f4-8bd6-586e35f70a34 | -5.67591 | -43.66586 | 2025-07-23 04:32:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e1f61c24-9357-3fbf-8301-fa83cba9cc3b | -5.73369 | -44.49807 | 2025-07-23 04:32:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d38a8888-ab79-3db0-b0b8-b935223d27b9 | -3.32312 | -48.71606 | 2025-07-23 04:32:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c99856f9-263d-36fc-9d2e-a8506463a59b | -6.93031 | -44.2976 | 2025-07-23 04:32:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 19c5dc2f-8f97-33dc-9e98-c8208a386cb7 | -6.18688 | -44.39589 | 2025-07-23 04:32:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 085eddd2-1e25-358e-8ba9-b7571c608f12 | -5.684 | -43.67042 | 2025-07-23 04:32:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 8113d7a8-3f4b-30d2-819a-701e5c507ac2 | -3.17787 | -49.45465 | 2025-07-23 04:32:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| f2084694-456a-31f1-a8de-dcd3a91cea49 | -3.04691 | -47.3775 | 2025-07-23 04:32:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 487a8e2d-63ae-3b5e-9f48-3a7e4d1843e8 | -6.88351 | -42.75951 | 2025-07-23 04:32:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 0c3b0e88-5287-3ccf-a7b9-71845fa4ca64 | -4.48351 | -46.07679 | 2025-07-23 04:32:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f6284140-4e17-38bd-bcaf-ee2bb5b8e217 | -3.2027 | -49.16515 | 2025-07-23 04:32:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 82aad92b-571e-3055-bbb5-67a6a69adc0b | -3.47808 | -39.57385 | 2025-07-23 04:32:00 | NOAA-21 | ITAPIPOCA | CEARÁ | Brasil | 2306405 | 23 | 33 | nan | nan | nan | Caatinga | 5.7 |
| b48f9845-113c-3763-bac6-e875b8ba6968 | -5.98655 | -45.36547 | 2025-07-23 04:32:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cebe1a3a-01aa-30bb-a03d-73c4313bc8d0 | -3.17382 | -49.45789 | 2025-07-23 04:32:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 39.5 |
| 4bd343ef-e225-3061-ae1e-903fddb8bd7c | -6.61105 | -42.3483 | 2025-07-23 04:32:00 | NOAA-21 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 65f2f6cc-a60b-3573-a8a9-dcc19328de25 | -2.44319 | -47.47611 | 2025-07-23 04:32:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0c615db1-0d8e-36f9-a7da-cdccaafe0b4d | -4.10792 | -48.20508 | 2025-07-23 04:32:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f3f05bc2-a38a-3664-a62c-7bd93f86ed4b | -4.30453 | -48.10148 | 2025-07-23 04:32:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 199e656c-879d-3b07-b992-2883c726e6a4 | -3.17158 | -49.4498 | 2025-07-23 04:32:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 44.2 |
| 348a0c18-c8b3-3de0-a02a-2632bca25067 | -9.43441 | -48.85785 | 2025-07-23 04:34:00 | NOAA-21 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9512485a-6982-3c64-bb7a-47a949a84b9c | -11.52334 | -43.24707 | 2025-07-23 04:34:00 | NOAA-21 | MORPARÁ | BAHIA | Brasil | 2921609 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| d0ae1ed4-b2c1-3b5e-9651-d876fa428604 | -8.08879 | -50.08743 | 2025-07-23 04:34:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4bc42f4d-dbc1-3028-ba98-2a844f6cb881 | -7.2222 | -49.5961 | 2025-07-23 04:34:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 863adb50-2437-355d-9685-b626e945cbed | -9.67645 | -43.7212 | 2025-07-23 04:34:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 41765e49-bbae-34a2-b7d4-e3e05e1ce7a5 | -9.12148 | -60.74948 | 2025-07-23 04:34:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e4e695fe-7059-31fa-9d4b-cc0d720eb842 | -10.88621 | -44.36208 | 2025-07-23 04:34:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5e942fd1-5028-3216-ac32-973c3323a3a6 | -13.69845 | -45.69616 | 2025-07-23 04:34:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 0e9ededb-ce3a-302f-ae9f-c2555b864eb2 | -13.69158 | -45.69037 | 2025-07-23 04:34:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 767ad47b-6a09-3a21-89b3-dc53822ad062 | -9.6772 | -43.72428 | 2025-07-23 04:34:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| fc7f8f1c-5bc5-33ec-a366-5df62f12f90f | -10.43915 | -56.63022 | 2025-07-23 04:34:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b0a96120-8fb8-3562-9077-f3db28040607 | -10.72087 | -49.48106 | 2025-07-23 04:34:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 361e08d3-d4b8-3607-b468-50c7b4f415f4 | -7.2759 | -44.36657 | 2025-07-23 04:34:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ded9c801-1497-366c-aaba-f5af3b88fe79 | -8.9129 | -47.35597 | 2025-07-23 04:34:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c660221c-8160-3e9b-ac97-815b5045cba4 | -12.5781 | -56.97659 | 2025-07-23 04:34:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1585414d-052a-3469-86d1-fa93d870e6e8 | -9.05585 | -45.07008 | 2025-07-23 04:34:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 0aab9621-1994-377f-9a26-ad160ea29da9 | -7.89399 | -45.55591 | 2025-07-23 04:34:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2ecfe4f5-d4cb-33b9-bf0d-82ee18c6f334 | -9.76719 | -48.57932 | 2025-07-23 04:34:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 09f028a3-e028-393c-84f9-5fcf944d2b33 | -10.00399 | -48.12577 | 2025-07-23 04:34:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 18dea066-5f16-3fe5-8c55-671d13d5267e | -13.70532 | -45.70195 | 2025-07-23 04:34:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 33b2ae54-c508-3e59-9144-4ab2165f1067 | -8.05719 | -49.97388 | 2025-07-23 04:34:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| edf33611-aa8e-32b0-a4d0-e6bec75f055b | -7.52917 | -42.42397 | 2025-07-23 04:34:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 8d9f60d9-767f-360f-9960-b1e73f91cbd3 | -10.05482 | -59.09645 | 2025-07-23 04:34:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| faa5b1fb-83e7-3d6b-acf3-23c1fc2f01b9 | -10.62043 | -45.23537 | 2025-07-23 04:34:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 04d5cae9-5092-3fa7-bbff-27c6e6e5ea2f | -8.94948 | -44.43225 | 2025-07-23 04:34:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fda1274a-6e20-32e0-bb38-27b92cc695ea | -7.89045 | -45.55686 | 2025-07-23 04:34:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a05ac058-402c-3e8b-870b-18c939b1f570 | -8.27894 | -46.08291 | 2025-07-23 04:34:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c6e595b6-2426-369d-911b-0c5fcd7bbc76 | -7.5698 | -44.57866 | 2025-07-23 04:34:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c4a3f499-e4f1-3f78-a725-c43ceb4b0725 | -12.49481 | -57.77697 | 2025-07-23 04:34:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d93f13f2-9aca-3d43-a4fe-960cea42cd1e | -7.91593 | -49.64455 | 2025-07-23 04:34:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 29a2a9fe-87dd-3729-b461-eb50f0e91551 | -13.65631 | -45.72305 | 2025-07-23 04:34:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9da82de7-d946-3caf-a89e-b221229f03c7 | -10.43877 | -56.63248 | 2025-07-23 04:34:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 03fe4f78-4b3b-3441-bcc3-461a0b4ae0e6 | -7.25452 | -60.18661 | 2025-07-23 04:34:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4baf6a67-897f-372b-9ac6-523b6bed182f | -7.894 | -45.55738 | 2025-07-23 04:34:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 33e1b6c2-75f9-366c-be3d-17163c5e3092 | -12.65224 | -45.05231 | 2025-07-23 04:34:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 63dc8fe4-e1d3-3f4b-9282-ed2ba87d5639 | -14.30302 | -43.80125 | 2025-07-23 04:34:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b2841371-63c5-369b-bd36-dea806f3f046 | -12.66585 | -45.03922 | 2025-07-23 04:34:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |


[Clique aqui para ver as próximas entradas](README10.md)
