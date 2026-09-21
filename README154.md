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

## Dados Diários - Página 154

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2e244f2e-6df9-3c5f-8030-b0cd83385ad2 | -11.90132 | -50.08622 | 2026-09-21 16:01:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 14.6 |
| c464334a-4597-37b8-a7ef-a31f5f43aaa1 | -9.27515 | -45.92059 | 2026-09-21 16:01:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 8b56b2dd-06a4-36a7-978e-eb2e058906a4 | -9.54181 | -47.963 | 2026-09-21 16:01:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 52.5 |
| 88f667f0-7af5-38a0-8847-f3092cdcb23c | -12.0781 | -50.03421 | 2026-09-21 16:01:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 8549cc12-f22b-32a9-9abd-3233fce6cd3a | -13.5568 | -44.89629 | 2026-09-21 16:01:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4078884c-4a6a-30b2-96d7-d71ae47d5c56 | -8.46412 | -45.0829 | 2026-09-21 16:01:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 17.9 |
| 11b389d4-f2f8-3616-abad-da83336f6267 | -8.70934 | -45.44364 | 2026-09-21 16:01:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 53c41367-fed2-3f8a-8b2e-a4068bb16ece | -8.95006 | -49.05612 | 2026-09-21 16:01:00 | NOAA-21 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 1a44fd22-5754-3b59-b97f-91f547bc1672 | -9.81202 | -46.08768 | 2026-09-21 16:01:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 20.0 |
| 269c88e5-923a-3a00-a1b2-cd7be816ab94 | -10.47565 | -50.26859 | 2026-09-21 16:01:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 15.0 |
| a07ebe8c-1fc4-3f98-b251-25d6c34f3201 | -9.58323 | -46.54875 | 2026-09-21 16:01:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 28.2 |
| adc87b3d-7bdb-3c13-bb36-bb9414e6626a | -14.75864 | -48.43332 | 2026-09-21 16:01:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 21.9 |
| b476b9b6-5ffe-3f62-a675-969e5c36bd9d | -9.54793 | -46.52815 | 2026-09-21 16:01:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| d434d239-7bd6-365d-87cb-4c641d1688b9 | -9.53433 | -47.95113 | 2026-09-21 16:01:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 30.8 |
| d968f7ea-2570-3487-8314-09f7ee1c34d7 | -11.43321 | -45.36729 | 2026-09-21 16:01:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 9.1 |
| bfe38a92-49fa-3cce-b37d-75156d9d7fe7 | -11.93429 | -46.50249 | 2026-09-21 16:01:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 17.3 |
| 1f6a6ce4-ad75-3403-979b-12e9f149e37d | -9.98217 | -50.26089 | 2026-09-21 16:01:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 19.9 |
| 5ef03616-e641-3d8f-94e3-b4c6fb5076e5 | -12.43144 | -47.03661 | 2026-09-21 16:01:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| bc306246-cecc-3b00-a10d-8e914b6e1fcf | -12.43662 | -47.06747 | 2026-09-21 16:01:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 48.0 |
| ba4d9193-924a-3af2-b298-2e3353f566e9 | -12.29901 | -50.6731 | 2026-09-21 16:01:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 22.8 |
| d3accb10-e321-3971-b8d6-849010a27a93 | -9.24417 | -46.24696 | 2026-09-21 16:01:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 54a54e34-2238-3c0a-a2e8-162974962b7d | -10.48296 | -45.09341 | 2026-09-21 16:01:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 74844198-a30b-3d80-8023-a3113346d308 | -12.8269 | -44.21146 | 2026-09-21 16:01:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 25273350-5d72-321d-9d6d-ac7c568ea6e8 | -11.09828 | -48.30398 | 2026-09-21 16:01:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 118504ed-4a18-32b4-ada8-6722407d99ec | -9.35763 | -46.38065 | 2026-09-21 16:01:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| ef1af345-553c-31eb-83dc-b07196e55fd9 | -13.91761 | -48.58612 | 2026-09-21 16:01:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 210cee4a-5e35-37f8-9fbb-6c37ed97743d | -10.96816 | -49.71119 | 2026-09-21 16:01:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 2b7c4c82-b1ab-3fda-b0bd-be26bd25d3b8 | -10.79741 | -50.74176 | 2026-09-21 16:01:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 11a3ddde-d4e4-3d83-b505-40e8e9610eb5 | -12.30638 | -50.70615 | 2026-09-21 16:01:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 11.9 |
| bbb31fb8-c414-3157-a613-ed6bee011a97 | -9.96484 | -45.73425 | 2026-09-21 16:01:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 40.3 |
| 71391d59-302b-3113-ba31-8e06e60d4103 | -10.6874 | -50.76309 | 2026-09-21 16:01:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 47.0 |
| b784f8f1-072f-36a3-927b-d49ddd340293 | -11.66368 | -43.44939 | 2026-09-21 16:01:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 411d8c68-dc53-3024-9a37-99d05b7bd0e8 | -9.39143 | -48.28462 | 2026-09-21 16:01:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 03997955-532a-3230-a033-a3cdb4404ddf | -9.81244 | -46.09095 | 2026-09-21 16:01:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 20.0 |
| 394f8930-04e2-3bdd-bc93-d1a219928486 | -13.13384 | -42.58144 | 2026-09-21 16:01:00 | NOAA-21 | MACAÚBAS | BAHIA | Brasil | 2919801 | 29 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 223d53a1-1114-3eab-8455-ff55229a5ddc | -10.98209 | -48.21769 | 2026-09-21 16:01:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 535aa257-2a41-3c0f-bf3a-19892183505b | -11.09926 | -48.31778 | 2026-09-21 16:01:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 54397133-1b09-3999-94e8-2567a2812dfc | -11.20035 | -42.85954 | 2026-09-21 16:01:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 7.8 |
| f26c7437-7eed-334f-9ae6-7d48c63ce01f | -12.30617 | -50.67242 | 2026-09-21 16:01:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 22.8 |
| 3f064883-204a-36ef-a3d5-05ab51d84a54 | -10.75787 | -46.33984 | 2026-09-21 16:01:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 86d80f21-91dc-3858-abf3-70b0c31a14f4 | -11.64824 | -47.79316 | 2026-09-21 16:01:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 13.8 |
| d37fb6f0-daf8-3493-8d55-33d4d7fb17a5 | -11.03615 | -49.73654 | 2026-09-21 16:01:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 8a37506b-55f4-3d5b-aa74-80a19833214f | -11.83783 | -46.81821 | 2026-09-21 16:01:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 85bebac7-bd92-349a-b12a-d3a128a17626 | -10.56162 | -46.54285 | 2026-09-21 16:01:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 814abd81-961d-3d15-a3c3-a4921971b1b4 | -9.38219 | -46.40557 | 2026-09-21 16:01:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 35.1 |
| f6bfede1-61a1-31ed-9de5-5ff9eacfb00a | -9.86199 | -48.40751 | 2026-09-21 16:01:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 5c84d77f-e9c7-3b94-ab34-5f50e2881575 | -9.88469 | -48.44184 | 2026-09-21 16:01:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 21.1 |
| b7107a07-57c7-351d-9032-53d632df087d | -10.12873 | -45.93181 | 2026-09-21 16:01:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| c197342f-a7f1-3ec3-b10f-f15f0b5b182d | -11.65634 | -47.78111 | 2026-09-21 16:01:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 51112ef2-3629-37d5-a61a-7189dfc580df | -10.07097 | -50.23881 | 2026-09-21 16:01:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 54.1 |
| 1939f46a-eb66-30f0-8e06-78cccd0b5c79 | -9.16359 | -50.01017 | 2026-09-21 16:01:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 22.3 |
| 08756b39-ea22-3d95-9750-211094790b31 | -13.35136 | -40.70825 | 2026-09-21 16:01:00 | NOAA-21 | MARACÁS | BAHIA | Brasil | 2920502 | 29 | 33 | nan | nan | nan | Caatinga | 16.6 |
| 1eb76de6-dbea-3e7b-8e75-5b8a8c35f265 | -10.38008 | -48.92264 | 2026-09-21 16:01:00 | NOAA-21 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 37.2 |
| 7ddd3c8f-de0c-3a2d-b949-3088563f546e | -11.8236 | -50.02051 | 2026-09-21 16:01:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 30.1 |
| 8255c992-2746-3882-bddb-fadc3896399a | -9.88586 | -48.45138 | 2026-09-21 16:01:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 25.7 |
| 8f82a116-2820-3753-bf40-2da99b09529f | -12.31333 | -50.67175 | 2026-09-21 16:01:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 11.5 |
| cafbe445-722f-3b40-b070-7c24ff082881 | -10.07149 | -45.85366 | 2026-09-21 16:01:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 10.9 |
| a19d2cb0-b68c-3e87-a7af-7fd1acded47b | -9.81297 | -48.30637 | 2026-09-21 16:01:00 | NOAA-21 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 13.1 |
| b19d0f68-be08-327e-88fd-084f60d50755 | -10.73438 | -48.80276 | 2026-09-21 16:01:00 | NOAA-21 | FÁTIMA | TOCANTINS | Brasil | 1707553 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| e24b0ef5-dc57-3044-9ea3-cd02268384a5 | -8.7808 | -44.3033 | 2026-09-21 16:01:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 44.5 |
| 784890f7-397f-316b-8f82-f6ebd2a29747 | -12.43538 | -47.0691 | 2026-09-21 16:01:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 20.5 |
| 97e5babb-84e9-3cd2-990b-efedbbb2a546 | -10.01978 | -45.21607 | 2026-09-21 16:01:00 | NOAA-21 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 849d8daa-a48c-3285-8617-a1995d7b57a3 | -9.02244 | -44.91292 | 2026-09-21 16:01:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 20.7 |
| cdc6afd6-088e-323c-9d05-065e14dd649f | -9.61035 | -43.92905 | 2026-09-21 16:01:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 38.8 |
| f7ed14ed-a410-3ae5-bb87-bec620b6998f | -11.47664 | -47.7494 | 2026-09-21 16:01:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 1446cf06-f5d6-3b0e-b52a-09ba66f61b5d | -10.84122 | -50.14553 | 2026-09-21 16:01:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 134.2 |
| 5a49df76-3de9-305d-9ef6-25e34624a4f8 | -11.09877 | -48.31375 | 2026-09-21 16:01:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| e307d738-487d-325d-a15a-45c2895cd1bc | -11.10076 | -48.32547 | 2026-09-21 16:01:00 | NOAA-21 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 13.5 |
| ce650029-c1ba-3ef2-84b9-2d777ce402de | -12.4257 | -47.03729 | 2026-09-21 16:01:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 24.4 |
| da27bf65-37b0-3969-a1d4-fa41f30e1d71 | -11.6775 | -43.41574 | 2026-09-21 16:01:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 25.7 |
| 8a958a99-1e06-3cc4-b1af-edc24c6d550b | -12.23704 | -41.14612 | 2026-09-21 16:01:00 | NOAA-21 | WAGNER | BAHIA | Brasil | 2933406 | 29 | 33 | nan | nan | nan | Caatinga | 6.2 |
| f19948ad-969b-3f5e-a1f2-ad60b105b5c4 | -12.77854 | -47.11707 | 2026-09-21 16:01:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 4484c31e-89e2-3828-ad33-7ccc2fba6f99 | -13.35249 | -40.71028 | 2026-09-21 16:01:00 | NOAA-21 | MARACÁS | BAHIA | Brasil | 2920502 | 29 | 33 | nan | nan | nan | Caatinga | 17.6 |
| 8161e40f-6277-318e-81c1-d7334a5284da | -9.69923 | -45.88457 | 2026-09-21 16:01:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 9774ea6f-24c2-3cb3-98ef-77c1c5688d86 | -11.67305 | -43.41634 | 2026-09-21 16:01:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 25.7 |
| fcfd60f2-9e97-3faf-bb25-9d38aa0c10ae | -10.76509 | -49.26033 | 2026-09-21 16:01:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 0b855b9b-7598-3106-8401-32a51f958c5b | -8.76905 | -45.87631 | 2026-09-21 16:01:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 5a925781-fbe2-33d1-a222-2bd0a1bb1e82 | -9.57799 | -45.47355 | 2026-09-21 16:01:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 2456aadd-b7f0-398a-91a5-f741394af1b3 | -8.70664 | -45.44223 | 2026-09-21 16:01:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 8.5 |
| c13a33cb-f608-3439-89e2-ad55ec0070a9 | -11.62657 | -50.19847 | 2026-09-21 16:01:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 10.5 |
| c3f3f799-5f8e-36fb-82e6-82b76d7f4eb0 | -9.38261 | -46.40882 | 2026-09-21 16:01:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 21.0 |
| e8d61aba-8473-3e8f-9f29-4641dafcc6bc | -12.80301 | -44.21442 | 2026-09-21 16:01:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| b422719b-6044-3dd6-9851-0821cd0d774f | -10.76452 | -46.30545 | 2026-09-21 16:01:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 0680bf1b-f3d1-3cc3-8ccb-0d03a3480ef9 | -11.65684 | -43.4225 | 2026-09-21 16:01:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 65.0 |
| 1fa0b733-85d1-3031-ad76-333867b97407 | -10.09362 | -50.29548 | 2026-09-21 16:01:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 792dd104-bb4c-3e34-b78b-2499b177d719 | -11.14835 | -42.79292 | 2026-09-21 16:01:00 | NOAA-21 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 7.6 |
| 0b16e190-10ce-38cb-841f-71437263c11e | -10.75312 | -50.60187 | 2026-09-21 16:01:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 18.0 |
| 38353140-6e83-36ba-a07e-75e7acc12cae | -11.86184 | -49.98087 | 2026-09-21 16:01:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 21.4 |
| 6a17bc00-4672-32cd-9366-c753571535c8 | -13.04011 | -46.98302 | 2026-09-21 16:01:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 7226cc8f-ecb7-30d6-8932-a20df919deb8 | -11.3713 | -46.76686 | 2026-09-21 16:01:00 | NOAA-21 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 7cec0d07-ef05-3b2d-8433-9571f07276bf | -10.55751 | -46.55369 | 2026-09-21 16:01:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 26933ba8-cada-3a57-8cc0-c65c83a61472 | -14.33268 | -45.20554 | 2026-09-21 16:01:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 63e44999-6859-3071-b4eb-58fd539909a0 | -11.94586 | -46.50982 | 2026-09-21 16:01:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 10.7 |
| edb6698a-dd7e-39f3-b30f-563e1259d21f | -11.80283 | -49.83948 | 2026-09-21 16:01:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 13.6 |
| e6bd2746-fc95-3f5d-83dd-0e5799a481bd | -8.6995 | -45.44471 | 2026-09-21 16:01:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 126.3 |
| ed7dffdd-65d3-304d-b484-04f4d28623cc | -11.93304 | -46.4967 | 2026-09-21 16:01:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| f369e9df-4d9d-3b9d-9756-65cf0887d958 | -14.12402 | -42.11289 | 2026-09-21 16:01:00 | NOAA-21 | LAGOA REAL | BAHIA | Brasil | 2918753 | 29 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 50b3cda0-a1d8-3c94-8e2f-efdc4094b451 | -10.2596 | -50.28231 | 2026-09-21 16:01:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| ce6af6cd-8631-3bb1-9724-947e88ff4425 | -11.67566 | -43.46099 | 2026-09-21 16:01:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 137.1 |
| eeaf3995-f642-34e9-b4ab-015013e39d72 | -11.81733 | -50.01729 | 2026-09-21 16:01:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 13.6 |


[Clique aqui para ver as próximas entradas](README155.md)
