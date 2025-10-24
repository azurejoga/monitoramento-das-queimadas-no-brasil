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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8f4098a5-d252-36e4-bb1d-2ea9808b7dd4 | -18.24848 | -44.19287 | 2025-10-24 03:51:00 | NOAA-21 | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e1a4a598-c5e2-34ab-be40-95db271dfef7 | -18.91725 | -47.17934 | 2025-10-24 03:51:00 | NOAA-21 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 54080007-f0c1-3069-be21-0a1b5a6bc925 | -19.79858 | -44.12371 | 2025-10-24 03:51:00 | NOAA-21 | RIBEIRÃO DAS NEVES | MINAS GERAIS | Brasil | 3154606 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 342e1a45-f0a3-337f-b0bc-b4d917777274 | -20.6513 | -55.0812 | 2025-10-24 03:51:00 | NOAA-21 | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 054b16da-aba2-3b9c-9923-04aa41975974 | -16.9554 | -53.22844 | 2025-10-24 03:51:00 | NOAA-21 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 354c1a46-7098-399e-b6eb-3a7af863b37a | -20.70613 | -46.27477 | 2025-10-24 03:51:00 | NOAA-21 | SÃO JOSÉ DA BARRA | MINAS GERAIS | Brasil | 3162948 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6b2c0353-fdbd-3677-8d69-112c90ba742a | -20.98216 | -44.31141 | 2025-10-24 03:51:00 | NOAA-21 | RITÁPOLIS | MINAS GERAIS | Brasil | 3156106 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 018f7f37-9542-3f07-84ee-c9104f7241b8 | -18.60402 | -51.78707 | 2025-10-24 03:51:00 | NOAA-21 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e03e78b8-3198-3e52-a3f1-b0c5886e65c5 | -17.09893 | -46.18751 | 2025-10-24 03:51:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c0cbf0dd-4fa0-3efb-803a-b6b359360ace | -19.46835 | -41.57445 | 2025-10-24 03:51:00 | NOAA-21 | POCRANE | MINAS GERAIS | Brasil | 3151909 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 87f89f61-56b8-30e7-83da-db0dae176b67 | -17.59701 | -46.62635 | 2025-10-24 03:51:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 7295a594-e9d1-316d-937f-2cd58c77efa2 | -17.23958 | -44.11575 | 2025-10-24 03:51:00 | NOAA-21 | ENGENHEIRO NAVARRO | MINAS GERAIS | Brasil | 3123809 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e11f7d47-cec5-3e3e-bb55-6708aabf7237 | -22.75391 | -52.19003 | 2025-10-24 03:51:00 | NOAA-21 | INAJÁ | PARANÁ | Brasil | 4110300 | 41 | 33 | nan | nan | nan | Mata Atlântica | 9.8 |
| 688b6dce-a864-3e79-9c8c-67a4f19dcbab | -23.38545 | -46.415 | 2025-10-24 03:51:00 | NOAA-21 | GUARULHOS | SÃO PAULO | Brasil | 3518800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 775c2aa6-ada5-3083-bfaf-cbbef4ee431d | -19.93768 | -45.76825 | 2025-10-24 03:51:00 | NOAA-21 | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 602610de-9406-357f-885e-b1dd945e87e7 | -28.62168 | -50.62273 | 2025-10-24 03:53:00 | NOAA-21 | BOM JESUS | RIO GRANDE DO SUL | Brasil | 4302303 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 264c8db9-84a1-345b-a48f-d75831ced138 | -24.77154 | -50.964 | 2025-10-24 03:53:00 | NOAA-21 | RESERVA | PARANÁ | Brasil | 4121703 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 59265064-03f6-3bf9-b5c2-e14495a547ba | -28.62045 | -50.62832 | 2025-10-24 03:53:00 | NOAA-21 | BOM JESUS | RIO GRANDE DO SUL | Brasil | 4302303 | 43 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| d32536a8-dda3-3892-981e-7e0b437c5139 | -26.34894 | -52.31791 | 2025-10-24 03:53:00 | NOAA-21 | CLEVELÂNDIA | PARANÁ | Brasil | 4105706 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 32b1a60b-6ac4-34ed-bd0a-87025a0c078d | -26.34255 | -52.32053 | 2025-10-24 03:53:00 | NOAA-21 | CLEVELÂNDIA | PARANÁ | Brasil | 4105706 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 1e61e030-bf34-30ca-a7a9-19f81502085b | -27.15745 | -51.29153 | 2025-10-24 03:53:00 | NOAA-21 | TANGARÁ | SANTA CATARINA | Brasil | 4217907 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| b6090b14-cdd2-326d-a9b3-ea20f8291c3a | -24.18524 | -51.68394 | 2025-10-24 03:53:00 | NOAA-21 | JARDIM ALEGRE | PARANÁ | Brasil | 4112504 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 52b37a36-7628-3960-b9ad-37229ddc3f86 | -26.34355 | -52.31628 | 2025-10-24 03:53:00 | NOAA-21 | CLEVELÂNDIA | PARANÁ | Brasil | 4105706 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| d8cd7c02-548e-3c3b-a02b-cc0b44b77455 | -24.77072 | -50.96762 | 2025-10-24 03:53:00 | NOAA-21 | RESERVA | PARANÁ | Brasil | 4121703 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 17a46c78-f9f6-3b96-9dc8-9e96a5283ebb | -24.52061 | -51.45858 | 2025-10-24 03:53:00 | NOAA-21 | CÂNDIDO DE ABREU | PARANÁ | Brasil | 4104402 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| e9d5181c-f124-3e3b-be46-d56c2482a8b7 | -28.22478 | -50.35829 | 2025-10-24 03:53:00 | NOAA-21 | LAGES | SANTA CATARINA | Brasil | 4209300 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| f779886c-335c-3c7d-9e98-8602ac9867cb | -28.22942 | -50.35962 | 2025-10-24 03:53:00 | NOAA-21 | LAGES | SANTA CATARINA | Brasil | 4209300 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 0fd29640-dd96-3f41-8bdb-1e2ca9d4f1d1 | -25.04066 | -52.56311 | 2025-10-24 03:53:00 | NOAA-21 | NOVA LARANJEIRAS | PARANÁ | Brasil | 4117057 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| b74bd765-b80e-3e68-9c5d-4c8edf2405e8 | -9.6061 | -46.9099 | 2025-10-24 04:00:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 129.8 |
| 4f59f9a2-f58a-35b3-9282-edaddeeda8a4 | -9.6061 | -46.9099 | 2025-10-24 04:10:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 87.3 |
| 93165e15-b16e-3b00-a4e9-146af4b8d3d8 | -3.15858 | -49.17315 | 2025-10-24 04:17:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 5cc63412-091a-3b7b-a353-2a7a8cd0a25a | -2.80211 | -51.35977 | 2025-10-24 04:17:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4266173d-cefd-3f7f-97c4-9c982d9e05ae | -10.8978 | -44.74051 | 2025-10-24 04:17:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9693dc37-5c53-3475-8dd7-f24e98703d03 | -10.00785 | -47.10791 | 2025-10-24 04:17:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 66729513-18af-35d2-8335-add86ab73f01 | -2.47025 | -49.22829 | 2025-10-24 04:17:00 | NPP-375D | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 025cd904-0c81-31ca-a29b-28804748238a | -9.26269 | -45.34636 | 2025-10-24 04:17:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ef24edec-e618-3f9a-bcfc-fada78af8a91 | -11.35778 | -45.95576 | 2025-10-24 04:17:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 248a1a9e-f89b-38b3-be3e-d80900b0a811 | -9.93379 | -47.46072 | 2025-10-24 04:17:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d2fc2076-7a1c-3bb0-92b4-c6bd9d209d05 | -2.41666 | -48.43937 | 2025-10-24 04:17:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 014ac0f3-1fdc-3745-8e23-8b7f3e73649f | -4.4681 | -49.10202 | 2025-10-24 04:17:00 | NPP-375D | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 70801799-7a67-35aa-b45a-f3cbb7593b2a | -3.12381 | -49.10172 | 2025-10-24 04:17:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 5d118ddf-57aa-3d50-8300-d595fe6b3ef5 | -11.36363 | -45.94147 | 2025-10-24 04:17:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 079b802f-2a0b-316c-a7c0-7dd99440df0d | -3.23973 | -48.76254 | 2025-10-24 04:17:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 25de2b17-be06-37b9-9429-c788017d4484 | -3.25052 | -52.9103 | 2025-10-24 04:17:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 527dd3e7-d6d7-341a-8b6d-2d7e8917647c | -12.31721 | -47.26651 | 2025-10-24 04:17:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 5afd3751-2a1f-3dec-ab08-8332a68071c7 | -2.4212 | -49.27553 | 2025-10-24 04:17:00 | NPP-375D | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| e60c1adb-b6c5-349b-8239-dcdf78eabd3c | -3.29965 | -43.49747 | 2025-10-24 04:17:00 | NPP-375D | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b05f76cf-4178-3b16-81c4-3161de4d3663 | -11.04533 | -45.40516 | 2025-10-24 04:17:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 05a9fe2b-1051-3aeb-8013-a5e613fbc3ab | -11.79771 | -42.84457 | 2025-10-24 04:17:00 | NPP-375D | BROTAS DE MACAÚBAS | BAHIA | Brasil | 2904506 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 11544a17-2195-3eca-8dc8-9a64fa59783d | -10.11032 | -47.7431 | 2025-10-24 04:17:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e8c2011b-449a-3096-b1cc-8a65aa6d4b2d | -9.20117 | -44.53791 | 2025-10-24 04:17:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ea3aec0e-ba20-316f-9f06-f541750fa342 | -5.90357 | -39.75685 | 2025-10-24 04:17:00 | NPP-375D | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| b41915fc-10a5-3721-8681-49691a670b7d | -3.70617 | -47.65514 | 2025-10-24 04:17:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d0a2c80a-f13d-3980-a7ff-c3da4d2741dc | -11.02314 | -45.06316 | 2025-10-24 04:17:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 14c8139b-0470-3a3b-8f90-bad4012cd84a | -2.8139 | -49.13226 | 2025-10-24 04:17:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6138de81-a8a4-3655-b97a-cc128cba9222 | -3.70271 | -47.65078 | 2025-10-24 04:17:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2882aa22-8976-3df1-a36e-8c7211cb4add | -9.22719 | -45.60566 | 2025-10-24 04:17:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ca1ab173-0993-3d2a-8616-8d47c61e0b31 | -11.00811 | -47.90395 | 2025-10-24 04:17:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 715ffa66-2a22-3c76-9788-d6fde5c10528 | -10.01412 | -47.07025 | 2025-10-24 04:17:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 6a6ee25d-fd45-33c7-8708-2a9971a2e46e | -4.31457 | -48.2303 | 2025-10-24 04:17:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 8a8bfe34-d0e1-31de-9180-a39b4a57ee24 | -9.23636 | -51.83646 | 2025-10-24 04:17:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fc233a13-c3d9-3ccc-9318-ffb51674644b | -12.06446 | -47.9864 | 2025-10-24 04:17:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 39acec12-083c-35e8-8585-d0594f87cd11 | -4.84118 | -47.80361 | 2025-10-24 04:17:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 654f1434-3f81-32cb-a0dc-ee53a0b6c301 | -11.73317 | -45.23404 | 2025-10-24 04:17:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 801093fd-fb2e-3451-ae06-786bdde748ed | -5.59192 | -47.32019 | 2025-10-24 04:17:00 | NPP-375D | DAVINÓPOLIS | MARANHÃO | Brasil | 2103752 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2ea1b9f9-a515-3afb-803e-0b2e8bd4a30b | -6.84475 | -41.55474 | 2025-10-24 04:17:00 | NPP-375D | SÃO JOSÉ DO PIAUÍ | PIAUÍ | Brasil | 2210201 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| fd1aeae8-b676-39d4-8817-9b4bd444f83d | -11.35499 | -45.95148 | 2025-10-24 04:17:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 018d8d6e-4461-3582-866e-bf4c403efd29 | -2.77198 | -48.5998 | 2025-10-24 04:17:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| c2dc7ea7-5163-3c57-9c59-14d1355254d2 | -2.26669 | -47.8473 | 2025-10-24 04:17:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7e3d6754-e62c-3f44-8724-27eeba21ab8e | -3.48429 | -43.98043 | 2025-10-24 04:17:00 | NPP-375D | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0c6467a6-e352-3a53-834a-b0bce610ce73 | -4.24487 | -48.54929 | 2025-10-24 04:17:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e89bf6ce-dd82-3004-868e-003370fd9ef2 | -3.0191 | -49.45206 | 2025-10-24 04:17:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| a52fb544-3df2-3662-96ec-a2ad3f833985 | -3.14786 | -50.16081 | 2025-10-24 04:17:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e8e97f59-35f2-3e48-b415-6e60338469e7 | -6.30966 | -41.85556 | 2025-10-24 04:17:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| d994ca15-4e12-37d5-81fd-3c82f31ebef3 | -10.89126 | -46.0709 | 2025-10-24 04:17:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8b9f9bc6-8f8c-337c-9822-5e8f336938cd | -11.97688 | -49.18165 | 2025-10-24 04:17:00 | NPP-375D | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7e621ca5-b628-361c-97b7-12d0a251ca2f | -4.84082 | -47.80377 | 2025-10-24 04:17:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5b837cd2-c886-38c9-bf41-698784d7de1a | -12.05774 | -46.41852 | 2025-10-24 04:17:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 52a50e66-e7a9-3da6-94c7-52cd279e46b9 | -2.87058 | -45.25522 | 2025-10-24 04:17:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 5.7 |
| e08719df-f7ca-33a4-90a2-0c63d90f2f74 | -6.36934 | -41.74301 | 2025-10-24 04:17:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 339215b4-1ace-3214-9c27-31215d8f9f3b | -9.60714 | -44.62166 | 2025-10-24 04:17:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 00451d43-9abc-3c48-8574-2b9da7c6663f | -6.30913 | -41.88109 | 2025-10-24 04:17:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 5f5ef3ae-9fef-3b39-b32c-2d6fbd29189b | -3.11116 | -51.20752 | 2025-10-24 04:17:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9973bcea-d82d-3535-967e-1910e34548d8 | -2.96171 | -48.59409 | 2025-10-24 04:17:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| aee0170b-e738-3366-985e-d0a66c778136 | -12.6467 | -44.12286 | 2025-10-24 04:17:00 | NPP-375D | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 255b26d0-8795-3e3c-be77-ba6f23ab8daf | -2.73153 | -49.56377 | 2025-10-24 04:17:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a886993e-96bb-3da8-9c04-ea4995248235 | -4.20906 | -48.60569 | 2025-10-24 04:17:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 4289f174-0801-3582-8993-1e8a4301db3e | -2.42584 | -49.27629 | 2025-10-24 04:17:00 | NPP-375D | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 11ea6992-8a03-387f-94aa-24f1ecc31c9f | -3.12261 | -49.10374 | 2025-10-24 04:17:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| b9a57693-66cd-38ef-aa87-81a1e516efb2 | -11.99252 | -43.326 | 2025-10-24 04:17:00 | NPP-375D | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1fa2782f-c06c-33b9-93b0-994f8d3907ac | -6.51861 | -37.48048 | 2025-10-24 04:17:00 | NPP-375D | SÃO BENTO | PARAÍBA | Brasil | 2513901 | 25 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 2ddd90a5-cd65-3b9f-b412-d4a3acdfe3a4 | -5.61016 | -41.12371 | 2025-10-24 04:17:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| f35cf278-9772-3aa1-9401-8685119982bb | -4.69649 | -47.90104 | 2025-10-24 04:17:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b1e7844c-17ea-3e1f-ae1b-f20a10e4d1ee | -4.34585 | -50.59399 | 2025-10-24 04:17:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a03beac1-f803-3575-8710-a9a1ed5f468d | -3.60222 | -48.98503 | 2025-10-24 04:17:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c10627e7-af8c-3faa-bf78-97f2a56f3a7a | -11.03038 | -47.908 | 2025-10-24 04:17:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4d6fd807-d49c-3d9a-824e-38daa65d2b5f | -4.64311 | -42.51632 | 2025-10-24 04:17:00 | NPP-375D | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| f5a0b984-6917-3e33-a3e9-8d7d23c04eae | -10.88875 | -46.04348 | 2025-10-24 04:17:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7eaf8190-4c1d-3a97-bee8-5b51c8e9c18d | -4.84487 | -47.80438 | 2025-10-24 04:17:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9cd074c4-c96d-395e-b4cc-1a97d378fb17 | -3.25361 | -52.91697 | 2025-10-24 04:17:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |


[Clique aqui para ver as próximas entradas](README15.md)
