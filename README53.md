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

## Dados Diários - Página 53

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 264f88d5-0b1b-3890-b717-0a7908fe7e43 | -1.23953 | -47.09286 | 2024-11-17 04:29:00 | NOAA-20 | CAPANEMA | PARÁ | Brasil | 1502202 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 60508376-caa9-3d07-9ee7-742405c8f2fe | -3.87031 | -50.9864 | 2024-11-17 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0e5daf80-c228-3160-bdf7-c3e9c3c2520b | -3.50347 | -51.01808 | 2024-11-17 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2fa631b4-d5d2-353b-96bd-87aae118f584 | -3.14279 | -45.98201 | 2024-11-17 04:29:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 0ae30328-0fea-3a6a-a7d3-edd5567aba95 | -2.62925 | -46.8326 | 2024-11-17 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 05bd69ae-eb2a-390e-a568-1395791ac9d3 | -3.03818 | -47.98888 | 2024-11-17 04:29:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9e2ef6c2-d440-3f00-9de5-34a5af2bafcb | -2.90232 | -46.84687 | 2024-11-17 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0c056c67-644f-3875-9deb-9ced7008d5bd | -3.01923 | -47.44267 | 2024-11-17 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1d8f31ae-a362-3655-b5b2-fef0fa2c42eb | -4.49239 | -48.4613 | 2024-11-17 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 35565b0e-40b7-30d2-9f1c-41de590c4c92 | -2.27218 | -48.98699 | 2024-11-17 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1150f11a-1998-3793-98f6-56fff7e168f8 | -4.63689 | -42.9115 | 2024-11-17 04:29:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 9adc03ba-f8be-3599-8bc5-0bd80175f2d5 | -3.5296 | -50.26156 | 2024-11-17 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 23.1 |
| 11d86ec9-dbd1-3c70-8e76-24abf1ffc172 | -2.77405 | -45.99732 | 2024-11-17 04:29:00 | NOAA-20 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ceef887d-5c09-37c6-bbfe-8ebca266e92f | -2.63282 | -48.57174 | 2024-11-17 04:29:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 18a353d4-57d2-34fe-87ec-e265ff2f1199 | -3.00516 | -45.4232 | 2024-11-17 04:29:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 2ed7149e-2c2b-3d9c-9af2-1e70edf9835e | -2.54156 | -47.32544 | 2024-11-17 04:29:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 32182e10-1228-3ae0-804c-b4272987ccbd | -4.03817 | -47.20841 | 2024-11-17 04:29:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 7fbc8e11-c0dd-3012-b88a-b255092c54e4 | -2.2985 | -49.1338 | 2024-11-17 04:29:00 | NOAA-20 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c4776b57-2cc9-3aab-b70e-f76c48014a32 | -2.90176 | -48.31329 | 2024-11-17 04:29:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6f7e3ade-8893-3e1a-b502-e2ce1cfbd7bc | -4.59562 | -44.58051 | 2024-11-17 04:29:00 | NOAA-20 | PEDREIRAS | MARANHÃO | Brasil | 2108207 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| be8e25c1-6e3a-351a-a9cf-f8f59d1ea748 | -4.22719 | -50.68118 | 2024-11-17 04:29:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ae372fb7-b6eb-3d74-9119-bc2d927c0b0a | -3.249 | -46.52001 | 2024-11-17 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1e6e3611-b192-3ec2-b98a-e4e0a9ed16ae | -4.1345 | -43.92888 | 2024-11-17 04:29:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8f2e6904-f4d3-37de-9400-906bbca8279c | -2.66412 | -46.17704 | 2024-11-17 04:29:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0798d785-dae2-3ca9-9f5d-c31551874e8f | -1.18578 | -46.54683 | 2024-11-17 04:29:00 | NOAA-20 | AUGUSTO CORRÊA | PARÁ | Brasil | 1500909 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f271b317-a8a1-3504-92ac-cc040b9e442d | -0.90636 | -51.72895 | 2024-11-17 04:29:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 469220fc-8f54-3acf-8223-daea40c33e0c | -0.89601 | -51.74198 | 2024-11-17 04:29:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6d06a358-6f86-3b18-b20b-7ffa2ab3d4d7 | -5.58107 | -44.87593 | 2024-11-17 04:29:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| b2390b86-c05f-3ff1-9c31-41ff33400642 | -0.1101 | -51.60083 | 2024-11-17 04:29:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c94b8ef4-c146-332f-bdcb-cc79f917d1e8 | -2.62298 | -46.02751 | 2024-11-17 04:29:00 | NOAA-20 | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e888d9fc-8012-35c0-8cd0-d48ec6b2aa5f | -4.51759 | -49.65879 | 2024-11-17 04:29:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 8478b496-20e5-3e0b-9465-1c84fde3feda | -3.76155 | -50.78408 | 2024-11-17 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bebba296-bbcf-3507-8a7f-6814252212ba | -2.67857 | -46.19352 | 2024-11-17 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 8e68babf-49e2-38e0-8d3f-bbc22dd6622e | -3.52348 | -50.51626 | 2024-11-17 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ce8f2f73-b513-3518-8137-2911bd71d09d | -2.1648 | -46.4146 | 2024-11-17 04:29:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8928928b-046a-32c4-b816-db20ebf2fa43 | -2.80225 | -52.99461 | 2024-11-17 04:29:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 63dd8b95-dbca-3a9c-b1ed-1c499e474f4e | -4.44041 | -46.57049 | 2024-11-17 04:29:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1c69561f-c0d6-37e2-94fa-cf5ae3299094 | -2.50789 | -46.39386 | 2024-11-17 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0bc80cfa-c773-3f36-9f35-455c98cde740 | -2.92781 | -46.72759 | 2024-11-17 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| bff29992-7898-35da-8309-dae45632c231 | -5.33842 | -44.99553 | 2024-11-17 04:29:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f5ce09ce-4066-3d4d-a755-455d05f78e0c | -2.66814 | -46.84577 | 2024-11-17 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f417630e-3da6-389a-968f-09b8b3e546fd | -0.9479 | -51.73121 | 2024-11-17 04:29:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9906cf78-8df8-3604-a03b-94b50f9ebeed | -2.64489 | -45.43544 | 2024-11-17 04:29:00 | NOAA-20 | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bfd1fe0c-213d-3ad2-82c6-ddb1fbd9ac0b | -3.85484 | -46.44732 | 2024-11-17 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c665c4c9-b5b5-3c71-9072-f243f4e89695 | -2.80288 | -46.65877 | 2024-11-17 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 12dc9275-24f8-334c-8661-3494007fe4b6 | -3.94848 | -47.0003 | 2024-11-17 04:29:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b202d293-002e-3f22-8a46-babf187e0efc | -3.52665 | -50.25692 | 2024-11-17 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 23.1 |
| 4483ef12-d503-3572-a1ed-e0a349ded877 | -3.35796 | -46.08395 | 2024-11-17 04:29:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| dd6a42b0-7c90-3e71-8582-ca368f8c3439 | -1.70357 | -46.23687 | 2024-11-17 04:29:00 | NOAA-20 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 35679caa-4bbc-35f9-a730-eea8131f8f84 | -2.84917 | -46.66595 | 2024-11-17 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 40742034-d278-392b-9c0c-eedb1a5bed70 | -3.79606 | -51.37191 | 2024-11-17 04:29:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 233f3192-6d86-3e28-9921-3dcaea41f8ab | -2.59958 | -47.56056 | 2024-11-17 04:29:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 288d3faa-67d8-3950-8329-6abfa0e5fbbb | -3.19111 | -46.54292 | 2024-11-17 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0560c028-e9ef-338f-bc03-cd4ea74cb07a | -3.2058 | -46.47078 | 2024-11-17 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 302d1cf7-96cf-3b11-b6c2-ae4353721b23 | -2.24346 | -46.84558 | 2024-11-17 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2153ab6f-1637-3bbf-b1c0-c35d8acf26e1 | -2.66914 | -46.18851 | 2024-11-17 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0bc2e6d9-86ea-348b-879a-a3da4d6b7fb7 | -2.37751 | -48.91904 | 2024-11-17 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| e7d6eb3d-ffcd-36f5-a56f-f596bf0ef1b7 | -3.24561 | -45.38526 | 2024-11-17 04:29:00 | NOAA-20 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1d0e213a-2a9e-369b-a412-ff1992976c44 | -1.16882 | -48.8459 | 2024-11-17 04:29:00 | NOAA-20 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 559e47a8-ec0d-3ba4-b053-0e8e0b7f3274 | -4.66357 | -49.51521 | 2024-11-17 04:29:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8e7be05d-92ab-3ade-b7f2-0494605339d6 | -2.80624 | -52.91666 | 2024-11-17 04:29:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d002fe99-e957-39ac-8aa0-2d6e5d35b534 | -1.24799 | -47.16822 | 2024-11-17 04:29:00 | NOAA-20 | CAPANEMA | PARÁ | Brasil | 1502202 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9416adb0-860a-32b9-b644-3efb1e2c0bea | -4.68455 | -49.62658 | 2024-11-17 04:29:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 60ec2cd1-85c1-35ba-abb4-719a5c1de316 | -2.84971 | -46.66251 | 2024-11-17 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e335c0aa-7303-3df0-9649-c4635f04d158 | -3.94244 | -46.71311 | 2024-11-17 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b04099b9-4843-3304-98db-dcd84fe80017 | -3.59093 | -49.35735 | 2024-11-17 04:29:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d8ef0bc6-1192-305e-bb7f-5f59c5e3ebda | -6.94249 | -42.82279 | 2024-11-17 04:29:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 6bf170b7-f190-3d4f-bd79-e35e6d47437a | -3.52502 | -50.24395 | 2024-11-17 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| df0f0fd5-ae7d-3e6f-9cb3-55bc302af41b | -3.96834 | -46.48243 | 2024-11-17 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ed60c4f8-c812-3459-aff4-fb3c69f0bf34 | -0.91848 | -51.65071 | 2024-11-17 04:29:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a183243b-61f0-345b-af84-c5887b2f9763 | -2.29937 | -48.48728 | 2024-11-17 04:29:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1ef0718b-1948-3289-b639-bc73c428db53 | -4.29827 | -48.10049 | 2024-11-17 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 2905b200-8451-3fe1-b84e-b59ef4ff6f8a | -2.62223 | -46.18452 | 2024-11-17 04:29:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2cc25a70-3f94-37a1-82d8-d48ef6ec01ff | -3.65803 | -50.61024 | 2024-11-17 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e953a222-8006-315d-aaca-a42f0991976b | -2.20888 | -48.31866 | 2024-11-17 04:29:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1838e10f-3cad-3ae0-9bea-52c9c1b8953c | -3.59099 | -47.26503 | 2024-11-17 04:29:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 901d874d-6387-3bac-bd0b-7b1ea4969658 | -0.90007 | -51.74263 | 2024-11-17 04:29:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9faf8b66-2d1d-37c6-b6c1-81f16f616eb9 | -6.49235 | -47.50188 | 2024-11-17 04:29:00 | NOAA-20 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 4b60f294-4890-3d90-a706-1dcad985f1f2 | -3.69655 | -45.05407 | 2024-11-17 04:29:00 | NOAA-20 | IGARAPÉ DO MEIO | MARANHÃO | Brasil | 2105153 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ffa8df46-d768-37b1-b47e-61576b3bce21 | -2.63117 | -48.56039 | 2024-11-17 04:29:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 38aef40a-595e-3ce0-9c08-072ee88b90e3 | -5.31595 | -45.45198 | 2024-11-17 04:29:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 773074e2-00b5-38da-9f8d-6aff18410122 | -1.40407 | -48.28983 | 2024-11-17 04:29:00 | NOAA-20 | MARITUBA | PARÁ | Brasil | 1504422 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 62f3c814-e67f-399c-a574-8b1439394637 | -4.73109 | -46.83998 | 2024-11-17 04:29:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 13f0ac80-27a7-3ad9-b13e-8881f1f5ba89 | -2.3893 | -47.94455 | 2024-11-17 04:29:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a0d5dbef-102a-3502-bddb-c83a5992e8a8 | -3.56462 | -50.26202 | 2024-11-17 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ac569161-13f1-3dac-b384-ac53613bdcd8 | -2.80986 | -52.92131 | 2024-11-17 04:29:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| dad67993-d274-38ea-9ddc-e14cc4e7ae78 | -2.1653 | -48.77627 | 2024-11-17 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0ddfbba7-8cef-383f-87d8-452000dfd436 | -4.23083 | -50.68177 | 2024-11-17 04:29:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 938066be-2cc2-377e-a676-057e5d23683a | -2.99358 | -51.03308 | 2024-11-17 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cb0c0a0a-18bc-3a9d-b8a3-dab61d741c04 | -2.66921 | -46.20988 | 2024-11-17 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 100f04d5-85c5-3dc7-96e5-34ceb84e5cb7 | -1.47066 | -52.30421 | 2024-11-17 04:29:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 07f2d7c8-afcc-3029-ac93-535bb9188a23 | -3.09398 | -45.97061 | 2024-11-17 04:29:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fc52d42f-01d5-3b33-8972-f78f11d8d713 | -2.79029 | -46.64998 | 2024-11-17 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1301d641-45c9-3cbc-92ec-5bc740d871a3 | -2.69481 | -49.28711 | 2024-11-17 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| bc72bd25-0132-3b48-9dee-12704b4e0971 | -4.47611 | -48.11458 | 2024-11-17 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 901edf69-4b46-32e1-9eee-4f9bf34b6f7e | -3.37198 | -52.72017 | 2024-11-17 04:29:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| af0665ae-8f80-389a-b734-3b9ba1ef702c | -2.22506 | -53.61323 | 2024-11-17 04:29:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9db81119-32ce-3bf0-bb6b-415892ae3c88 | -4.813 | -44.48227 | 2024-11-17 04:29:00 | NOAA-20 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 8500aef7-c5ca-3295-a6bb-37f57f51729a | -3.99861 | -46.39779 | 2024-11-17 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5d13dd23-ad86-3af8-aa46-1b28f7606434 | -6.4775 | -47.51018 | 2024-11-17 04:29:00 | NOAA-20 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |


[Clique aqui para ver as próximas entradas](README54.md)
