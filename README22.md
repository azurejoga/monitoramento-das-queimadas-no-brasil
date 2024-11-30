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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| afcd0374-fd28-3e48-a0aa-12e0b1641706 | -6.24128 | -39.857 | 2024-11-30 03:46:00 | NOAA-20 | CATARINA | CEARÁ | Brasil | 2303600 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| b705c59b-d1c1-316a-ac49-c906ddec4d34 | -5.30692 | -44.71657 | 2024-11-30 03:46:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9ee75ca2-9ada-3927-8b0a-91f686e1b1e2 | -5.22594 | -44.91549 | 2024-11-30 03:46:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 86cb90ae-b17f-3f1d-a8c1-bae4200e933b | -4.87291 | -41.27433 | 2024-11-30 03:46:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 12.4 |
| d376c93a-f6c1-3091-8e66-a8b29019f97f | -4.15049 | -49.00075 | 2024-11-30 03:46:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| efe26e21-1aec-33b6-8f05-eadf491eac73 | -2.59331 | -46.57203 | 2024-11-30 03:46:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 601fe704-f2e7-32db-954a-20307155b95d | -3.03513 | -45.11855 | 2024-11-30 03:46:00 | NOAA-20 | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 16342cac-9c17-309c-93ee-d8d04115ed4e | -2.62834 | -46.88187 | 2024-11-30 03:46:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 37af66ea-41c1-3d35-a037-fc4506e6c18a | -3.19553 | -46.56394 | 2024-11-30 03:46:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5528c1ee-e8bc-3644-b052-60bb5b1898eb | -6.9037 | -43.56545 | 2024-11-30 03:46:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9606c625-788b-3ba4-a567-264498586f55 | -4.70171 | -42.38269 | 2024-11-30 03:46:00 | NOAA-20 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| d58a202d-d5fd-35c5-924c-66f4019926cd | -2.24321 | -46.45313 | 2024-11-30 03:46:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 82b5446c-bbd0-3d20-9319-97b21518e344 | -3.12144 | -46.05255 | 2024-11-30 03:46:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f9512a56-4bae-33ed-bd39-992298892e82 | -5.03939 | -45.2454 | 2024-11-30 03:46:00 | NOAA-20 | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 1520a803-7db7-34ae-8433-e6d5a247d278 | -5.74684 | -46.1868 | 2024-11-30 03:46:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| aed82fde-ddba-3c82-8625-40af0a76cf68 | -3.98291 | -41.51099 | 2024-11-30 03:46:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 41e0f49b-2135-3441-89d8-7ee9b3ee7f8e | -2.62996 | -46.88086 | 2024-11-30 03:46:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 74aae345-e95a-30ca-a0f2-719236217667 | -4.86949 | -41.29495 | 2024-11-30 03:46:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 8c4d0925-f108-3c79-8185-ded041d57d0d | -3.98582 | -41.51908 | 2024-11-30 03:46:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| b3dd95eb-f5cb-39d4-8547-a475da75a148 | -2.275 | -46.44498 | 2024-11-30 03:46:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4253039a-3c50-3d14-bca1-468d75941f58 | -4.4334 | -46.58123 | 2024-11-30 03:46:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 53b9afeb-df49-3ee1-870e-d42c5445e4f4 | -6.93673 | -42.83676 | 2024-11-30 03:46:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 31d4bed2-ab4a-3b6b-a370-3526cb45890a | -6.93604 | -42.84088 | 2024-11-30 03:46:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 13e9f71c-a553-3e47-98e9-8cffd2f7cdac | -6.13347 | -43.95121 | 2024-11-30 03:46:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| f6d15dd1-e7af-38e7-bde9-1fce385250af | -4.86728 | -41.3083 | 2024-11-30 03:46:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 8a29f605-3de2-3a4f-ac03-e17233c08d5f | -6.37925 | -44.76018 | 2024-11-30 03:46:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2d0da061-dabc-3bc7-a00a-67d8dbaab8d2 | -4.08321 | -47.03151 | 2024-11-30 03:46:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 826649bb-510d-3ac7-b90d-e95be6b22d4b | -2.86447 | -46.83403 | 2024-11-30 03:46:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e1d77fc1-fdd2-32ad-800b-a6ffc6e38ac0 | -5.96691 | -43.37017 | 2024-11-30 03:46:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 9.8 |
| 253ddcce-870c-3a5b-adbf-703f8fe000ca | -3.0815 | -49.21909 | 2024-11-30 03:46:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8e4a7fa6-fd20-3932-b117-da1c876fd0ee | -6.67507 | -39.70324 | 2024-11-30 03:46:00 | NOAA-20 | TARRAFAS | CEARÁ | Brasil | 2313252 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| a6a12d38-619b-34b7-a20d-c4354ca606ec | -4.13818 | -42.15379 | 2024-11-30 03:46:00 | NOAA-20 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 4ce608e5-d06b-3744-8e2b-376277264ba9 | -2.84678 | -46.68556 | 2024-11-30 03:46:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 80b80b3b-adec-330e-b644-8fd6f22fd7d5 | -2.96572 | -48.04308 | 2024-11-30 03:46:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 34f4ba5a-e5d2-3bc5-871e-0a276b647e47 | -3.46547 | -48.92891 | 2024-11-30 03:46:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2c9bf386-3208-387d-bf1e-72182a32417b | -4.35854 | -43.7002 | 2024-11-30 03:46:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a6826a22-6225-3624-a1c5-ef237046ac71 | -8.00914 | -35.05753 | 2024-11-30 03:46:00 | NOAA-20 | SÃO LOURENÇO DA MATA | PERNAMBUCO | Brasil | 2613701 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| ebdbc09c-196c-3bb3-83ca-11effccf6bbe | -6.99601 | -35.25237 | 2024-11-30 03:46:00 | NOAA-20 | SAPÉ | PARAÍBA | Brasil | 2515302 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 79e49b79-2ca7-3334-80dc-96279603a442 | -1.92154 | -47.90967 | 2024-11-30 03:46:00 | NOAA-20 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 758b2828-b21f-3fe1-8049-7e41cc5bbc21 | -7.21955 | -39.0498 | 2024-11-30 03:46:00 | NOAA-20 | MILAGRES | CEARÁ | Brasil | 2308302 | 23 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 6e0a8e34-d7e6-3398-8e03-7f6b5766ca86 | -6.0322 | -38.12577 | 2024-11-30 03:46:00 | NOAA-20 | FRANCISCO DANTAS | RIO GRANDE DO NORTE | Brasil | 2403905 | 24 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 3d3f0648-4bb5-3fd0-a729-1ff05a47cddc | -5.07313 | -44.992 | 2024-11-30 03:46:00 | NOAA-20 | SÃO ROBERTO | MARANHÃO | Brasil | 2111672 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dd5c3b52-1468-3924-a5d2-a332f22a86fc | -4.85648 | -41.29883 | 2024-11-30 03:46:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 3dc2ea86-2663-3b77-87b8-10eea739280d | -3.70824 | -45.6919 | 2024-11-30 03:46:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| fcc540ba-503e-3169-b905-1b7ed55a18a3 | -5.30644 | -44.71943 | 2024-11-30 03:46:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 18d829c1-337f-33a1-86ed-ccd21ffb7451 | -2.31461 | -44.8244 | 2024-11-30 03:46:00 | NOAA-20 | BEQUIMÃO | MARANHÃO | Brasil | 2101905 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9a193b01-858d-3ed6-957e-b828f3c2a242 | -2.63128 | -46.20378 | 2024-11-30 03:46:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e769d9ba-66da-3a6c-a39d-0decd1cc4342 | -4.8746 | -41.28899 | 2024-11-30 03:46:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 12.0 |
| 0507b4a2-ce50-3e5e-9c7b-fe926aa25c26 | -4.87914 | -41.28642 | 2024-11-30 03:46:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 12.0 |
| c422c436-3301-320d-9ccf-ff7755d8d218 | -4.67843 | -46.3723 | 2024-11-30 03:46:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 5.5 |
| d3ba4ab1-09d1-3077-b816-44d6d0a65802 | -1.50834 | -45.8992 | 2024-11-30 03:46:00 | NOAA-20 | LUÍS DOMINGUES | MARANHÃO | Brasil | 2106201 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3df69be2-f514-3d45-a779-b701038efa30 | -1.82877 | -46.30799 | 2024-11-30 03:46:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a02744a7-193a-3d96-938c-a3fa57862851 | -6.21197 | -44.50482 | 2024-11-30 03:46:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 70351eb4-a416-39ab-9681-6eaef3df5b3e | -4.8707 | -41.31252 | 2024-11-30 03:46:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 7.1 |
| 2ff375a8-c41f-3cca-ad3d-48863fbd40cb | -4.53336 | -46.41949 | 2024-11-30 03:46:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ebf302f3-0304-30af-a05e-21f53a2406f3 | -3.62216 | -42.737 | 2024-11-30 03:46:00 | NOAA-20 | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 40a4d7ae-655c-3918-be17-5e7270704f84 | -3.83988 | -46.52866 | 2024-11-30 03:46:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| a924b1c0-5663-3302-9682-be3321e9cfea | -8.71426 | -44.01658 | 2024-11-30 03:46:00 | NOAA-20 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8a7e65c7-8097-3c70-9141-a63b9e59d493 | -4.29128 | -40.61073 | 2024-11-30 03:46:00 | NOAA-20 | PIRES FERREIRA | CEARÁ | Brasil | 2310951 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 823ffe21-92c5-3734-bbe0-939d9bf4abed | -3.82472 | -46.54934 | 2024-11-30 03:46:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 85d65aae-ecca-3bab-b44e-22869668a1a8 | -4.83351 | -41.25362 | 2024-11-30 03:46:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| c5d22ec3-a6f4-3dfb-84db-dbda34f5dcfb | -3.70585 | -47.14431 | 2024-11-30 03:46:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 63d69d4c-d56b-325f-83e6-58ada03e922b | -3.67187 | -47.12475 | 2024-11-30 03:46:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 19.7 |
| 9bd7dc77-0ea0-36e9-906d-0abf18626143 | -3.70273 | -45.69095 | 2024-11-30 03:46:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| e752266f-8ae3-3327-9bea-a2953c904a0d | -6.06915 | -48.04999 | 2024-11-30 03:46:00 | NOAA-20 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| e8ac08ff-4c8a-32e2-bdf4-507ab67f0650 | -3.62027 | -42.73899 | 2024-11-30 03:46:00 | NOAA-20 | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| eb4a3f43-c048-3318-84a0-46d50491795f | -7.2138 | -39.77662 | 2024-11-30 03:46:00 | NOAA-20 | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 13.7 |
| e9a055ba-3011-3ad0-a018-8bfcd5d87afd | -3.97633 | -41.52528 | 2024-11-30 03:46:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| f16bd7bd-5cac-3691-87e3-618c5a884188 | -4.36559 | -45.52612 | 2024-11-30 03:46:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 7d7dc835-b64d-35cd-ae3b-66d6b58558fb | -2.3509 | -49.01595 | 2024-11-30 03:46:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| dbc3e0e7-86c3-3080-ba31-15194abe5cf0 | -6.92708 | -43.56472 | 2024-11-30 03:46:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9768f378-88e8-380c-9d64-a8c28542531f | -3.03399 | -45.12532 | 2024-11-30 03:46:00 | NOAA-20 | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 01ba9c52-76ea-3b77-8adf-99d44efb4496 | -1.83328 | -46.30596 | 2024-11-30 03:46:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c742b360-5bd4-3e49-ac44-c0720fc7ab48 | -4.26345 | -40.70198 | 2024-11-30 03:46:00 | NOAA-20 | IPU | CEARÁ | Brasil | 2305803 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 7593e545-f11e-3985-a3ad-1814f51f9756 | -4.87124 | -41.30927 | 2024-11-30 03:46:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 10.4 |
| 1246ca15-17ca-32c9-aae6-6fb7fecfc22c | -4.86893 | -41.29835 | 2024-11-30 03:46:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| f1bf49da-d449-33f5-8cce-94925f246533 | -3.98107 | -41.52218 | 2024-11-30 03:46:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| ab91be23-7615-31a9-8cda-f0cb4a2b5c39 | -5.49186 | -46.77489 | 2024-11-30 03:46:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c5235b16-badf-36b2-afcb-ed9dae9ee514 | -4.86497 | -41.29733 | 2024-11-30 03:46:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 83ef94bc-3db1-3488-8576-5d78d6efc610 | -3.70335 | -45.68735 | 2024-11-30 03:46:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 7f470365-ddcf-3718-b312-03b53b26a834 | -2.58562 | -48.204 | 2024-11-30 03:46:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 28196375-82cc-3c2f-a7b2-d2af7ccfd768 | -1.77437 | -46.12558 | 2024-11-30 03:46:00 | NOAA-20 | BOA VISTA DO GURUPI | MARANHÃO | Brasil | 2101970 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8cf22051-ae78-3666-9a1d-33273e64ad4a | -6.89623 | -43.55472 | 2024-11-30 03:46:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 126a9491-dd0c-31d9-be17-66ad2e09de9d | -4.85534 | -41.30568 | 2024-11-30 03:46:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 862e325b-f65a-363b-95a5-2644428ea110 | -4.85876 | -41.30993 | 2024-11-30 03:46:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| a4f9b690-fa9a-3685-a489-bb99e51574f1 | -11.84097 | -43.7226 | 2024-11-30 03:46:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 00f45b1c-93bb-3a1f-ad89-a7412b426134 | -4.09182 | -44.85699 | 2024-11-30 03:46:00 | NOAA-20 | LAGO VERDE | MARANHÃO | Brasil | 2105906 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1c4008eb-dbe6-321c-b71b-d9e9cf691ab0 | -4.08399 | -47.02688 | 2024-11-30 03:46:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 5a0224d9-de6d-3903-bd49-2f11b0d80fb3 | -5.07365 | -44.98903 | 2024-11-30 03:46:00 | NOAA-20 | SÃO ROBERTO | MARANHÃO | Brasil | 2111672 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 73b74287-a569-381f-84bf-bc8163056fdf | -3.45767 | -48.93368 | 2024-11-30 03:46:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a8602dd0-043e-3485-8bc3-c5076873fd23 | -5.42217 | -44.85807 | 2024-11-30 03:46:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 554fbcc3-6068-3634-8f3e-6de52b9913ef | -2.71553 | -46.12538 | 2024-11-30 03:46:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f8bc9077-31bc-36cb-acea-bfd4b008dbea | -6.07568 | -48.04454 | 2024-11-30 03:46:00 | NOAA-20 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 6a0a8d10-7989-396a-b0e7-056248ad41f3 | -4.87857 | -41.28988 | 2024-11-30 03:46:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 12.0 |
| a820c372-98aa-35ad-a1b1-69c6be278154 | -6.90074 | -43.55553 | 2024-11-30 03:46:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5435cff8-0d21-3d3c-8dfa-7109ae3a1dbd | -8.80778 | -37.1235 | 2024-11-30 03:46:00 | NOAA-20 | BUÍQUE | PERNAMBUCO | Brasil | 2602803 | 26 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 798b051f-4f56-3463-9602-707c2f303471 | -20.12614 | -41.23505 | 2024-11-30 03:49:00 | NOAA-20 | BREJETUBA | ESPÍRITO SANTO | Brasil | 3201159 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 6f4c92ed-cc8b-38f0-ba14-034624f7ee40 | -20.24355 | -41.18243 | 2024-11-30 03:49:00 | NOAA-20 | AFONSO CLÁUDIO | ESPÍRITO SANTO | Brasil | 3200102 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| a747b560-5383-30d1-af9f-b634f45b3d3b | -10.4495 | -44.94631 | 2024-11-30 03:49:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| aefb4925-38b3-3b91-98a6-37551d3b3247 | -20.12551 | -41.23889 | 2024-11-30 03:49:00 | NOAA-20 | BREJETUBA | ESPÍRITO SANTO | Brasil | 3201159 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |


[Clique aqui para ver as próximas entradas](README23.md)
