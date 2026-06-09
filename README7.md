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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ef464ad9-2538-3404-92bf-a2f368fd682d | -11.32204 | -44.61018 | 2026-06-09 04:17:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e0c97050-e279-3ef1-9abf-56e792407011 | -18.15321 | -39.78683 | 2026-06-09 04:17:00 | NOAA-21 | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 3725056e-4162-3db8-a6ae-8749868bf9a6 | -21.71383 | -47.13948 | 2026-06-09 04:17:00 | NOAA-21 | CASA BRANCA | SÃO PAULO | Brasil | 3510807 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b4f6dab6-29ab-30e1-9754-cc1d913bf9e9 | -11.55402 | -52.7786 | 2026-06-09 04:17:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| cd83f294-51fc-3a8a-9079-af0cd57b3957 | -14.30199 | -49.24699 | 2026-06-09 04:17:00 | NOAA-21 | NOVA IGUAÇU DE GOIÁS | GOIÁS | Brasil | 5214879 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 784f8c9a-18ad-3c40-8323-aaf803304d72 | -12.85026 | -44.39109 | 2026-06-09 04:17:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0bcd93c4-0fb3-30f7-9959-107a094fa51b | -23.02152 | -46.67739 | 2026-06-09 04:17:00 | NOAA-21 | ATIBAIA | SÃO PAULO | Brasil | 3504107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 703fbcb7-0bf2-3275-a5d3-bb6175f414ef | -19.91485 | -47.97566 | 2026-06-09 04:17:00 | NOAA-21 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| a3db112e-a355-37a1-9bb4-44887f5583ad | -19.91082 | -47.97887 | 2026-06-09 04:17:00 | NOAA-21 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| ab694b5c-78e5-3ce4-8739-e3a057e3b802 | -10.43027 | -49.44364 | 2026-06-09 04:17:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3c0ba4ad-5776-3b0e-bbe9-5c817c0d53af | -22.38441 | -49.79166 | 2026-06-09 04:17:00 | NOAA-21 | LUPÉRCIO | SÃO PAULO | Brasil | 3527801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| a52c34e5-fe24-31d6-8f63-372140421433 | -12.92789 | -43.62207 | 2026-06-09 04:17:00 | NOAA-21 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| da9f0985-4702-39e8-a36f-f54eaa7079e4 | -10.77525 | -54.10014 | 2026-06-09 04:17:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e46e35d7-3742-3208-a93c-bf9a3e363340 | -13.11096 | -51.71954 | 2026-06-09 04:17:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8c69a6d9-7e5c-39cf-882a-8570f6ffb856 | -11.26984 | -44.52932 | 2026-06-09 04:17:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e39379e8-c368-3c93-9e33-2ae3930e18c4 | -12.36873 | -47.89205 | 2026-06-09 04:17:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 19861614-7dca-3533-90cf-ba8baff16732 | -19.78902 | -47.92908 | 2026-06-09 04:17:00 | NOAA-21 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0a513c3b-0538-3300-b94c-98af6eed26cd | -22.67378 | -43.47807 | 2026-06-09 04:17:00 | NOAA-21 | NOVA IGUAÇU | RIO DE JANEIRO | Brasil | 3303500 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 49465020-8bcb-310e-ac63-9338e6e0f980 | -11.55346 | -52.78162 | 2026-06-09 04:17:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 0602e057-854a-3805-bb50-4e12bbe4c551 | -19.52774 | -49.55137 | 2026-06-09 04:17:00 | NOAA-21 | CAMPINA VERDE | MINAS GERAIS | Brasil | 3111101 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 05a0a8de-a31b-36a5-a150-5fc57da234f3 | -11.57477 | -54.58013 | 2026-06-09 04:17:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 097584c3-0950-3297-8418-1e9edb95ea7b | -22.96348 | -46.96243 | 2026-06-09 04:17:00 | NOAA-21 | VALINHOS | SÃO PAULO | Brasil | 3556206 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| c6dde584-345b-3e86-94ce-3a7b76b5cb70 | -9.07247 | -50.60204 | 2026-06-09 04:17:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 5d275795-328c-3c1b-a6d7-9909b7318d5f | -9.07704 | -50.60282 | 2026-06-09 04:17:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 8fd927e8-ffea-30ae-916b-b2627ff8fb27 | -19.28423 | -49.7356 | 2026-06-09 04:17:00 | NOAA-21 | CAMPINA VERDE | MINAS GERAIS | Brasil | 3111101 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3f4778df-f232-3298-9772-b6db7d2b9969 | -9.07331 | -50.59731 | 2026-06-09 04:17:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| ff136ded-63d7-3a39-b7ec-210a481c632a | -21.73063 | -46.38281 | 2026-06-09 04:17:00 | NOAA-21 | BANDEIRA DO SUL | MINAS GERAIS | Brasil | 3105301 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 83e5bf29-c5e0-3bea-9a47-766bf07450c8 | -12.77499 | -46.82314 | 2026-06-09 04:17:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d806d891-a978-3587-8e80-fefb2b879bb0 | -11.26683 | -53.97071 | 2026-06-09 04:17:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4fe7e2f1-d0f1-3480-9400-6b99e814c641 | -12.04283 | -45.27937 | 2026-06-09 04:17:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8b186bf2-8fe7-3ec6-9920-869bb67593b9 | -13.25794 | -44.39589 | 2026-06-09 04:17:00 | NOAA-21 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 16.0 |
| d2bfbb2e-36b7-3125-b875-26fb513c1206 | -12.85303 | -44.3736 | 2026-06-09 04:17:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 24.8 |
| 889790f9-c1a0-3adb-9b4a-5e373c188c3a | -15.59229 | -41.79633 | 2026-06-09 04:17:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 60360a7b-31c9-3443-aaee-4cec1ba70e9a | -12.04169 | -45.28651 | 2026-06-09 04:17:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 73a86107-bc81-384a-a4f5-0dc74b828651 | -13.36554 | -43.19939 | 2026-06-09 04:17:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 523153dd-1e92-34fa-a125-3c1ea03eb2c1 | -10.86158 | -53.73658 | 2026-06-09 04:17:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8bb4b37f-0ca3-36dd-9a4a-262e8da28886 | -13.36499 | -43.20305 | 2026-06-09 04:17:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 2fb13464-abc4-330b-a994-41159d8bfae8 | -11.02764 | -44.31831 | 2026-06-09 04:17:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 334ea0a7-7c4c-3793-9ec2-3060fbca2ee8 | -21.87867 | -46.01664 | 2026-06-09 04:17:00 | NOAA-21 | SÃO JOÃO DA MATA | MINAS GERAIS | Brasil | 3162302 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| f672d5ae-dfbd-351e-94e0-911ec40c5c15 | -19.90743 | -47.97825 | 2026-06-09 04:17:00 | NOAA-21 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3cc5b684-bb1a-3071-bac3-593bc2f4db9b | -9.5439 | -47.76468 | 2026-06-09 04:17:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 95d97083-a927-3bab-89a5-d363873a7ab3 | -20.1459 | -48.93213 | 2026-06-09 04:17:00 | NOAA-21 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ae0d9824-2949-3cbc-875d-b8c586788349 | -12.03423 | -47.80324 | 2026-06-09 04:17:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 73bfedb4-59e8-30cc-82ce-edfad56c6d5d | -10.8534 | -53.7454 | 2026-06-09 04:17:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 576e6700-1d20-3862-a944-d35076be9d1d | -12.05695 | -49.76364 | 2026-06-09 04:17:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 16.3 |
| c53c807a-9844-3814-8372-c1023b255696 | -19.28058 | -49.73479 | 2026-06-09 04:17:00 | NOAA-21 | GURINHATÃ | MINAS GERAIS | Brasil | 3129103 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3adcac3c-1dbe-31a8-8451-6f9e062bc88f | -10.91974 | -54.11329 | 2026-06-09 04:17:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 314aa724-de40-399f-9ef7-754363994876 | -11.83377 | -49.43744 | 2026-06-09 04:17:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f93ba026-295a-34a8-9b74-7f20293a9dfe | -21.4284 | -48.64477 | 2026-06-09 04:17:00 | NOAA-21 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dd484f19-38ef-373b-ad54-dd8cf3cc37d2 | -9.33946 | -47.91605 | 2026-06-09 04:17:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| bb572fc4-739f-3066-9419-49ef8e26b99d | -14.39923 | -43.80313 | 2026-06-09 04:17:00 | NOAA-21 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 00ae7bdd-30f3-313e-9047-3a7a47f19f1c | -12.8508 | -44.38758 | 2026-06-09 04:17:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6f722c8d-2cb3-32ac-b97d-2b761efdf95c | -9.89392 | -47.85908 | 2026-06-09 04:17:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 2e6d05f8-b9ce-32d3-ac5a-440875fe2fa0 | -22.80244 | -49.34898 | 2026-06-09 04:17:00 | NOAA-21 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d5342a16-cc4c-3bd5-a5c5-70fd3a11492f | -11.65247 | -52.8613 | 2026-06-09 04:17:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 566302f9-2576-3a66-b0ba-48b1d756d23b | -10.89789 | -49.35295 | 2026-06-09 04:17:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2127f852-0adc-313d-b0bf-60c056ee50c3 | -15.2256 | -50.85843 | 2026-06-09 04:17:00 | NOAA-21 | MATRINCHÃ | GOIÁS | Brasil | 5212956 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| bc8c61d2-7a87-3e6d-9c4f-1f0f11ff4dea | -12.48322 | -46.26755 | 2026-06-09 04:17:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 365e8180-3540-34db-8106-2c6f2717e395 | -12.36433 | -47.89576 | 2026-06-09 04:17:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 25e007cc-daa1-3048-8fe3-53e6eedaebd7 | -19.47544 | -49.56953 | 2026-06-09 04:17:00 | NOAA-21 | CAMPINA VERDE | MINAS GERAIS | Brasil | 3111101 | 31 | 33 | nan | nan | nan | Cerrado | 5.0 |
| bac36df0-4b59-3e3e-b760-dbb49d6bcbe4 | -22.38089 | -49.79091 | 2026-06-09 04:17:00 | NOAA-21 | LUPÉRCIO | SÃO PAULO | Brasil | 3527801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| a2d363a6-395f-3eb6-8358-eb2eb3a63139 | -12.0556 | -49.77118 | 2026-06-09 04:17:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 34b5bda5-08a2-38e3-aa31-582d367910b9 | -20.75394 | -41.88919 | 2026-06-09 04:17:00 | NOAA-21 | CAIANA | MINAS GERAIS | Brasil | 3110103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 0f85a300-74ba-395e-8c6a-af6c3206bb2b | -9.5445 | -47.76253 | 2026-06-09 04:17:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9e79db14-b7d5-39af-9917-2735ae5d8e56 | -12.48876 | -46.27656 | 2026-06-09 04:17:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5ec3ce6a-17c6-36ed-bb19-24c5f61ea47c | -11.6474 | -52.86034 | 2026-06-09 04:17:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2f3c3d2e-7561-33a1-977d-e367f4b18413 | -12.48258 | -46.27151 | 2026-06-09 04:17:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| caf51c2d-ee34-3e7b-85d5-1368180bdc22 | -13.96291 | -46.18916 | 2026-06-09 04:17:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9eef3fb8-60c9-3f9a-a704-e73aa32297f5 | -9.08076 | -50.60836 | 2026-06-09 04:17:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9d13d060-4229-3e79-8df8-e129c33bf94e | -16.6073 | -43.33661 | 2026-06-09 04:17:00 | NOAA-21 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 87ec8195-2637-3c56-bd78-4f374db9fe74 | -12.46998 | -55.12972 | 2026-06-09 04:17:00 | NOAA-21 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 011b8529-a7b5-3eb9-b159-f8ac0ea861ac | -11.43956 | -41.65602 | 2026-06-09 04:17:00 | NOAA-21 | AMÉRICA DOURADA | BAHIA | Brasil | 2901155 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 5617ac91-ef73-3869-976e-58102b9da203 | -12.0379 | -47.8038 | 2026-06-09 04:17:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 3190552d-27be-3e79-8219-ac12bf911470 | -22.45039 | -47.15301 | 2026-06-09 04:17:00 | NOAA-21 | CONCHAL | SÃO PAULO | Brasil | 3512209 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b07816ef-6a1f-36c8-b939-a1e0aec84314 | -21.09257 | -43.8243 | 2026-06-09 04:17:00 | NOAA-21 | RESSAQUINHA | MINAS GERAIS | Brasil | 3154408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| ffc9eeaf-a20f-323a-8bcc-68cc07ddec52 | -13.36445 | -43.2067 | 2026-06-09 04:17:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 8c7fe23c-4a09-3eab-a483-6e81fd8bab19 | -14.39978 | -43.79952 | 2026-06-09 04:17:00 | NOAA-21 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1f488ede-7a80-3c42-a2a8-5df1650c14dc | -10.23394 | -47.42618 | 2026-06-09 04:17:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0d65413f-6034-3fdb-ab25-b2caa858f4d2 | -15.17688 | -43.85235 | 2026-06-09 04:17:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ca4d7ded-d5c1-30ff-9b99-d6c04531f0a1 | -10.85472 | -53.73837 | 2026-06-09 04:17:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bdce8d3a-ac2d-3db9-8ab9-a63c0eb1d268 | -11.95248 | -43.39864 | 2026-06-09 04:17:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 42133691-3f3f-362e-ac1a-0e763ad2afb3 | -12.05628 | -49.76741 | 2026-06-09 04:17:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 9bd25b48-6155-3e40-9033-e047957912cb | -12.47492 | -55.13512 | 2026-06-09 04:17:00 | NOAA-21 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a1fea098-c7be-3e09-8520-f9d0fd6a1431 | -10.15113 | -47.64935 | 2026-06-09 04:17:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9eb72ed6-49f9-3c86-9a35-a06fac836a94 | -21.23479 | -44.01322 | 2026-06-09 04:17:00 | NOAA-21 | BARBACENA | MINAS GERAIS | Brasil | 3105608 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| aa0d4efa-5caf-370a-bc48-6a000e5b51fd | -11.55343 | -52.80993 | 2026-06-09 04:17:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 81aaacfe-7c53-3187-8d3d-70f09c89c9b9 | -15.58975 | -41.79822 | 2026-06-09 04:17:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 768651f7-0811-3a6f-84d0-6271fefb7621 | -10.6454 | -49.38459 | 2026-06-09 04:17:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 34.1 |
| ee450b66-1e56-3b71-ab6d-09c7fc55799e | -18.42067 | -54.54812 | 2026-06-09 04:17:00 | NOAA-21 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 42a6e136-40b8-327e-a6d8-51dae30f3dd9 | -12.46737 | -51.46293 | 2026-06-09 04:17:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7679a5d3-e28d-3b32-98a3-1247c2efaf14 | -13.05178 | -44.18623 | 2026-06-09 04:17:00 | NOAA-21 | CANÁPOLIS | BAHIA | Brasil | 2906105 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a144c7a8-38da-38bd-be91-ea5315cac58e | -16.60786 | -43.33274 | 2026-06-09 04:17:00 | NOAA-21 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2c9a9861-0ea3-3f23-a916-fcf0c4256356 | -14.30285 | -49.24215 | 2026-06-09 04:17:00 | NOAA-21 | NOVA IGUAÇU DE GOIÁS | GOIÁS | Brasil | 5214879 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f9ba105b-237a-3883-87e5-4768af73a3a5 | -22.80315 | -49.34483 | 2026-06-09 04:17:00 | NOAA-21 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9ecde316-1532-32e9-91ec-c9f93cff567d | -11.26721 | -53.96868 | 2026-06-09 04:17:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9db2f0ca-1847-388d-a492-04498d85ac61 | -11.54161 | -52.78893 | 2026-06-09 04:17:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| db8e9c05-5dee-3bcd-8628-25f5f51a58d8 | -21.20637 | -48.52131 | 2026-06-09 04:17:00 | NOAA-21 | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 3f346c76-76a5-39cb-bd47-f4aab5c405a6 | -17.59086 | -46.64754 | 2026-06-09 04:19:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 809f3850-194f-348a-aadc-ad9270d0c18d | -17.58693 | -46.65063 | 2026-06-09 04:19:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 18.1 |
| 710251b1-55c9-35f8-bfa5-4fb6e56ffa52 | -17.45164 | -47.192 | 2026-06-09 04:19:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |


[Clique aqui para ver as próximas entradas](README8.md)
