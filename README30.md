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

## Dados Diários - Página 30

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 92623296-04ee-3506-8389-a9b04d7bd8fe | -7.67977 | -54.85141 | 2026-09-28 04:34:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e42059ed-2a32-30ef-b910-7e1b26cda384 | -10.89923 | -45.10892 | 2026-09-28 04:34:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f2fdd43e-fe51-3dc9-a999-b422b4f310b3 | -9.85374 | -44.9532 | 2026-09-28 04:34:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ea923384-7ba9-3f23-83a5-ca22e5882069 | -13.56472 | -46.3577 | 2026-09-28 04:34:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 7839a7a3-0d15-3dbf-9612-5ed6d31fb4f6 | -6.67496 | -45.6208 | 2026-09-28 04:34:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 469d8b19-2a74-34a5-b53c-5ee76e92be4c | -11.49246 | -47.38667 | 2026-09-28 04:34:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 2a497928-9b09-32c5-8138-e553a9165b1b | -6.94407 | -41.61206 | 2026-09-28 04:34:00 | NOAA-21 | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| ae9a8878-defc-30cc-9849-ccc1b58f27ff | -11.4483 | -44.91219 | 2026-09-28 04:34:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e30002f6-a278-3cab-9abb-7d551ad30bbe | -9.82397 | -45.26423 | 2026-09-28 04:34:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e8f18fa7-4ba8-3992-bcd2-9ae3e589cf40 | -6.93955 | -42.86386 | 2026-09-28 04:34:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 8a0a647b-4701-3535-abba-d58130a7e5ac | -10.70869 | -50.47268 | 2026-09-28 04:34:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0131122d-dc2f-3b0f-8a1f-8be22589acc8 | -6.08335 | -57.79728 | 2026-09-28 04:34:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 428bca32-25ed-3a7f-96a1-7f397407ad12 | -6.00568 | -47.39124 | 2026-09-28 04:34:00 | NOAA-21 | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 10.7 |
| eb4d659a-36f7-313d-9118-ce0d925dbe07 | -12.73034 | -47.28345 | 2026-09-28 04:34:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 01571e87-eca3-3cbf-b9aa-55449f835ce8 | -11.10565 | -51.3367 | 2026-09-28 04:34:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1a3922c8-8e08-3f2c-bfed-670c2e1e0185 | -13.10433 | -47.41 | 2026-09-28 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| ac71687e-b614-337b-a116-5e7ce49526d3 | -9.82766 | -45.26471 | 2026-09-28 04:34:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 16c6d908-5781-3839-be2f-19f1de4699ea | -11.1451 | -50.04697 | 2026-09-28 04:34:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a7be9608-f290-393b-b34e-108d9ea01204 | -8.10506 | -44.00623 | 2026-09-28 04:34:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 01319d9d-6927-37b8-b8f4-a3323c55d025 | -6.76653 | -45.3681 | 2026-09-28 04:34:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e2a6ad15-f5d2-302b-b094-a5d20e148869 | -9.77951 | -44.82242 | 2026-09-28 04:34:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0e09ce82-4c53-357b-81d6-c8c453f9b9f6 | -9.16393 | -61.40778 | 2026-09-28 04:34:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 20.4 |
| b052b3bd-4d5f-3224-8268-1e239228fb06 | -10.22561 | -49.988 | 2026-09-28 04:34:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dba98b59-db89-3824-b453-294fd5e85aed | -6.18887 | -44.12212 | 2026-09-28 04:34:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e381a031-4447-3c71-921e-a2f0f5bb2c6f | -10.59548 | -49.99337 | 2026-09-28 04:34:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9f637184-7caf-3e34-a6b7-abda4c4e9a4c | -7.15852 | -39.31539 | 2026-09-28 04:34:00 | NOAA-21 | JUAZEIRO DO NORTE | CEARÁ | Brasil | 2307304 | 23 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 53ace478-c47a-3adf-abd4-789189019d72 | -11.44629 | -44.92677 | 2026-09-28 04:34:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| fa959d77-00da-3e13-8663-f9d93f7f3b91 | -13.07805 | -47.44486 | 2026-09-28 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 17.8 |
| e0de2ded-5b1f-3639-ba8a-524b006c2865 | -7.04655 | -42.87148 | 2026-09-28 04:34:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 2b58d530-fdcb-3463-b2be-80790b8fd492 | -11.30727 | -55.10968 | 2026-09-28 04:34:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 39dda939-cf02-3abd-8dc2-21f00f7110f0 | -10.95343 | -49.60275 | 2026-09-28 04:34:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| f57de5ea-cd26-30bc-93bb-32f4be8acd70 | -12.62631 | -47.27615 | 2026-09-28 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| c692b3a8-d1e3-3335-a983-1b7bd8a80eee | -12.68169 | -45.02204 | 2026-09-28 04:34:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 42a96c89-0a40-339a-9bed-1d4b7f898685 | -11.47458 | -46.85189 | 2026-09-28 04:34:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6aa7a6b8-090c-3194-8e07-e7e95496ff8a | -8.09732 | -44.00511 | 2026-09-28 04:34:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| fe66bb34-84cb-38ee-9e46-621e438bbecd | -7.53035 | -43.97819 | 2026-09-28 04:34:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 2e2a46b4-cb0e-3bca-a77d-5de9e5cd5cd5 | -7.34226 | -42.07526 | 2026-09-28 04:34:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| e0216561-69e2-3bce-a672-1f73ddd4b113 | -9.165 | -61.40223 | 2026-09-28 04:34:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 14.9 |
| 2aee27d7-0882-3968-90d8-9141f76fb35e | -11.37825 | -43.41532 | 2026-09-28 04:34:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8ddffc2c-6ac1-363a-9ca1-74f413542962 | -13.205 | -48.32616 | 2026-09-28 04:34:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5fd6a561-b8de-3fba-a787-6ef59a86150d | -9.12643 | -45.60844 | 2026-09-28 04:34:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 058524ee-10ce-3bdc-962e-c5ef34745b20 | -9.92396 | -49.37843 | 2026-09-28 04:34:00 | NOAA-21 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c3da5cfa-704d-3743-b5a7-47c626ca8c20 | -10.4068 | -53.81119 | 2026-09-28 04:34:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| efe4996e-e12b-3145-bbec-f34ececf5ec7 | -8.28973 | -45.42011 | 2026-09-28 04:34:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 88f3e50d-6487-3aaa-88d3-95c99c8f4ca8 | -9.19484 | -45.85445 | 2026-09-28 04:34:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 400fafa4-aade-3035-8d99-b164aa4d7eab | -9.9831 | -50.16511 | 2026-09-28 04:34:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b9e9f25e-e818-3514-a84a-d6d0e2aa47b7 | -12.60918 | -51.96184 | 2026-09-28 04:34:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6ee89f2e-eb4d-364f-b43c-790301f011a1 | -11.705 | -44.52832 | 2026-09-28 04:34:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 3bee555a-8dda-32d4-8ccc-c575484a6a39 | -11.03674 | -54.04145 | 2026-09-28 04:34:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 11d44d26-d5fb-3b23-aa82-0846f3d16f11 | -6.65089 | -55.10849 | 2026-09-28 04:34:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3e900b7a-073d-3cba-bd2d-11034981e358 | -12.71019 | -47.28138 | 2026-09-28 04:34:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 5d06f57d-a2b4-3d4d-abc3-ca7c3e417e3c | -6.07769 | -57.80179 | 2026-09-28 04:34:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8fac643e-fe0b-3210-bd33-15d5196c3b37 | -7.71206 | -54.76721 | 2026-09-28 04:34:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| aade3875-2dbf-3d9c-92da-608e14cd84f9 | -10.23449 | -49.99675 | 2026-09-28 04:34:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a04aa697-f93c-37a8-a747-17d92251c508 | -11.70088 | -44.53156 | 2026-09-28 04:34:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3f3e5cf0-c4ce-3710-b07c-028a9eea9588 | -8.72682 | -47.982 | 2026-09-28 04:34:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2117c134-a147-355e-8e7e-9a14f51c9e4c | -13.07574 | -47.4367 | 2026-09-28 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f01c2cd1-ae1c-3270-b7d2-c667e2eb1e99 | -11.37243 | -43.42664 | 2026-09-28 04:34:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 8eb04aed-a618-3ce0-a739-884f6bd26af4 | -10.12909 | -45.14012 | 2026-09-28 04:34:00 | NOAA-21 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| a559917f-b13f-381e-8a84-843f5cb12779 | -13.15468 | -48.54441 | 2026-09-28 04:34:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| caa21699-1095-3b2f-9107-d2a0a471c147 | -7.06295 | -55.48017 | 2026-09-28 04:34:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 34d5f4b2-1e3f-3b4d-8876-9b6454f6025c | -6.6959 | -45.64785 | 2026-09-28 04:34:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a9fcc558-52e0-34aa-8b7a-7693b4d2bd74 | -9.0768 | -49.868 | 2026-09-28 04:34:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6a4144b7-d6b2-37cc-b94b-669fff19db36 | -10.22782 | -49.99567 | 2026-09-28 04:34:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6d032d71-597d-3c9e-955c-d6889fc41de9 | -8.42249 | -44.87265 | 2026-09-28 04:34:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fac5bc7a-3fdb-3584-a3d7-c41d68b2aab4 | -7.83015 | -55.13577 | 2026-09-28 04:34:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9eea982a-66ca-3ca1-8027-9049b06a10e7 | -10.2 | -49.99849 | 2026-09-28 04:34:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4c8f73ff-05ad-3c99-903b-e4dd99dbc066 | -5.42254 | -49.17886 | 2026-09-28 04:34:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 77a5f67a-b2f2-3d51-b45d-5d6772257919 | -10.21951 | -49.98336 | 2026-09-28 04:34:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3fdaa8b4-b4d2-36f9-91ca-c6203163b08a | -11.69871 | -44.54684 | 2026-09-28 04:34:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 367729b4-80fc-3607-8be6-72219862a7f7 | -12.72603 | -47.36121 | 2026-09-28 04:34:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c5db2c9b-94cd-3f97-afb2-eda60f374e72 | -13.15188 | -48.54037 | 2026-09-28 04:34:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2ccf3a8c-8c8a-3382-b161-9de3b461e456 | -6.94008 | -42.86021 | 2026-09-28 04:34:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 37bd27d5-c465-3d6e-9554-6bdc72752292 | -10.71615 | -44.43964 | 2026-09-28 04:34:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 75e5a84e-dbdd-3180-a55a-900881901bfd | -8.2407 | -45.4049 | 2026-09-28 04:34:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 7b834f1d-382a-37e1-b9d7-31ae38523d29 | -11.70686 | -44.54422 | 2026-09-28 04:34:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 2792361a-ce9d-3362-9451-96c379da5687 | -11.70481 | -44.53214 | 2026-09-28 04:34:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| abb339d5-2cbe-32cd-9e5f-e555b31f7a13 | -9.99046 | -50.14048 | 2026-09-28 04:34:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 2a7e0cae-f01d-38d2-95a5-a8c5963499eb | -12.14206 | -50.34953 | 2026-09-28 04:34:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 88670c0e-f0d1-3d9e-84fc-51bb7fcfd2a8 | -9.09507 | -49.90394 | 2026-09-28 04:34:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1b33043c-8d51-3e61-a1dd-d83707b1f932 | -8.66202 | -45.41534 | 2026-09-28 04:34:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 12effb9a-08d9-3dbd-a71e-4dcdd795afd1 | -12.57796 | -43.50697 | 2026-09-28 04:34:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 646d8965-b48c-3386-bd01-0c95584956a3 | -7.71141 | -54.77019 | 2026-09-28 04:34:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| efd3fd25-8420-3d23-a739-c6935b4b8fed | -10.40591 | -53.81633 | 2026-09-28 04:34:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c519a4a3-3654-33ae-9b46-ee2d60e9f932 | -10.81223 | -60.74412 | 2026-09-28 04:34:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 0aab6a27-5a16-38c1-a24b-0984e91a501b | -12.68672 | -46.98287 | 2026-09-28 04:34:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| e48d4012-2216-31c8-9284-a27c40b5bb50 | -11.4815 | -46.85301 | 2026-09-28 04:34:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bb103ee2-c578-310a-a106-befdafd47001 | -11.70409 | -44.53723 | 2026-09-28 04:34:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| e833a3af-84b4-3c15-a36e-867137a090f7 | -11.03734 | -54.03797 | 2026-09-28 04:34:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 34c7107d-abc0-33c8-a3d0-43823fcd3f54 | -10.21611 | -50.00475 | 2026-09-28 04:34:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| fb630c40-b929-3880-8ac9-df9ef9bbd21c | -11.08645 | -47.50304 | 2026-09-28 04:34:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 30f65811-fcde-3f95-8419-846571a0d270 | -13.39067 | -44.36992 | 2026-09-28 04:34:00 | NOAA-21 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 04c03f79-b109-3fa1-a21c-8a48290b2665 | -8.59805 | -54.64921 | 2026-09-28 04:34:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 20afdace-88fa-334b-9324-9e9887a83556 | -12.38551 | -47.4854 | 2026-09-28 04:34:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| b42233b7-4782-3ba9-9034-253bd6b8606d | -12.74077 | -44.77007 | 2026-09-28 04:34:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2341dc9b-ba54-3489-8cd8-2bc2619f5c32 | -10.11933 | -43.95638 | 2026-09-28 04:34:00 | NOAA-21 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 853c88bc-dd6c-377f-b2ab-253fbe7e2cbd | -7.87194 | -61.18235 | 2026-09-28 04:34:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 7.4 |
| c0658647-62e9-3bf0-bbad-5529ba31fb43 | -11.10971 | -51.33344 | 2026-09-28 04:34:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0e0f9c1f-c502-3912-93f2-4e8d2ed0e08d | -7.71531 | -44.90371 | 2026-09-28 04:34:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d9a2d6bd-e1c6-38df-bbfd-c7ec01d82873 | -11.18667 | -44.79876 | 2026-09-28 04:34:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 40.8 |


[Clique aqui para ver as próximas entradas](README31.md)
