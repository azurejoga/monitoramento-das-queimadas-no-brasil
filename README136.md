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

## Dados Diários - Página 136

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 017a05dd-0d16-351a-9342-cdab2c379cbc | -6.1981 | -55.4534 | 2026-09-20 15:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 51.1 |
| 2ad9de98-be2e-3070-8005-471b81ac35da | -10.8367 | -50.9266 | 2026-09-20 15:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 227.4 |
| 21423d19-4d2b-34ea-8868-55852099b76c | -11.3796 | -51.3777 | 2026-09-20 15:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 106.3 |
| 9a6a7c29-ef94-35d4-b773-e48e7005f510 | -13.4139 | -51.7358 | 2026-09-20 15:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 105.5 |
| b6756c85-eab0-37d7-98dc-68154d318b71 | -10.8856 | -56.2161 | 2026-09-20 15:10:00 | GOES-19 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 57.1 |
| b6d80268-fe1d-30aa-8976-17d4c36e576e | -10.2598 | -50.2624 | 2026-09-20 15:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 94.7 |
| 7699cf67-0c45-3ecc-a7a5-f65ee34d5353 | -2.9326 | -58.3397 | 2026-09-20 15:10:00 | GOES-19 | SILVES | AMAZONAS | Brasil | 1304005 | 13 | 33 | nan | nan | nan | Amazônia | 65.5 |
| 58698093-6a29-3cf4-9529-85996b4ac9ad | -6.1112 | -57.645 | 2026-09-20 15:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 51.7 |
| e00ba563-e838-3316-8643-75de3e6f76b5 | -10.7463 | -50.6172 | 2026-09-20 15:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 218.4 |
| 2450d867-ab3f-34b8-bbd1-ebb3228b74e4 | -11.398 | -51.418 | 2026-09-20 15:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 142.7 |
| 721acc05-a29a-30b1-a2f6-1b97a93d909b | -10.8177 | -50.9286 | 2026-09-20 15:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 116.7 |
| 66dda699-c92c-3c5f-9534-9a5deda2a5d2 | -11.0256 | -48.3164 | 2026-09-20 15:10:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 104.1 |
| c83a3323-4b0a-3181-bb67-e65f69af21cd | -6.4302 | -59.9724 | 2026-09-20 15:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 174.3 |
| 81961e0f-2062-3985-b009-310feb5471e0 | -3.7347 | -59.4002 | 2026-09-20 15:10:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 57.3 |
| 210d1ccf-9d45-3222-8dd9-158640a602f6 | -10.0956 | -48.4226 | 2026-09-20 15:10:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 133.3 |
| 48912652-dda1-3fbe-8919-824dc9c7c0cc | -11.0223 | -54.1379 | 2026-09-20 15:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 68.8 |
| 3ff08b82-87eb-30d4-8401-b983c0890a65 | -8.0894 | -55.331 | 2026-09-20 15:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 113.4 |
| 7961437d-5bca-3e1d-80b6-ee8747aa60c5 | -10.4547 | -51.2405 | 2026-09-20 15:10:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 86.7 |
| b6fd16d9-a5e5-3128-893e-0eb015cda519 | -13.8924 | -48.5698 | 2026-09-20 15:10:00 | GOES-19 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 53.2 |
| 52794049-cb1a-3b19-adc3-b3fd6177d127 | -6.3471 | -58.2973 | 2026-09-20 15:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 48.2 |
| c39e64fb-2757-369f-ade9-f6c698a14431 | -11.0506 | -54.9309 | 2026-09-20 15:10:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 429.0 |
| e293caf7-6b59-3173-a949-abd842efa73e | -12.0454 | -50.0424 | 2026-09-20 15:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 72.7 |
| 5c0d1cfa-5b96-33bf-8579-b82755aa564a | -10.9665 | -49.7583 | 2026-09-20 15:10:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 113.1 |
| a71623c0-6dfa-3224-9954-d52b38b93aa5 | -9.3609 | -48.3251 | 2026-09-20 15:10:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 95.1 |
| dc9868a6-b087-3ee5-95f5-2f835e9a9c56 | -9.84 | -46.4136 | 2026-09-20 15:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 105.4 |
| bd8556a0-e02e-3915-a6e4-6379616d87c1 | -3.3358 | -58.1384 | 2026-09-20 15:10:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 58.1 |
| 325cc01c-8b1b-3343-bb9b-47e6cc7f5999 | -10.88 | -50.17 | 2026-09-20 15:15:00 | MSG-03 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 31719fe6-62c8-3cac-a7eb-57c14628da24 | -10.38 | -50.24 | 2026-09-20 15:15:00 | MSG-03 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9c84f015-de8a-3057-b161-3b89c8fcbda1 | -10.72 | -50.72 | 2026-09-20 15:15:00 | MSG-03 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 957f80fb-8dea-3e91-b640-cf0102165ca3 | -6.92 | -42.94 | 2026-09-20 15:15:00 | MSG-03 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| e7e8c4e4-0648-32d9-8a1f-e1e08601e5bc | -8.77 | -44.28 | 2026-09-20 15:15:00 | MSG-03 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 16d4e466-c9c3-39d3-a0d6-4904cb19b82f | -11.65 | -43.45 | 2026-09-20 15:15:00 | MSG-03 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 5f1e198a-abbf-3192-9799-6be1607a8228 | -11.04 | -54.9 | 2026-09-20 15:15:00 | MSG-03 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4a49d031-d9f6-3a22-afef-8f3e21bef319 | -6.9 | -43.74 | 2026-09-20 15:15:00 | MSG-03 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 185a55a8-1139-31d4-a60b-f27dc688d110 | -6.93 | -43.74 | 2026-09-20 15:15:00 | MSG-03 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| ddfad498-e908-36a4-b14a-299ab3165896 | -10.35 | -50.23 | 2026-09-20 15:15:00 | MSG-03 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f39add69-87a4-3eb1-8c23-4231d010f0f8 | -11.07 | -54.91 | 2026-09-20 15:15:00 | MSG-03 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f6d29338-8568-3c1c-a25c-5488fd96c47d | -10.85 | -50.16 | 2026-09-20 15:15:00 | MSG-03 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 64a447ec-57e7-3db3-a049-b32b5bda5840 | -9.04 | -48.77 | 2026-09-20 15:15:00 | MSG-03 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 3ed93311-6628-3a26-943d-1aa408b01276 | -9.86 | -48.45 | 2026-09-20 15:15:00 | MSG-03 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 98b9bdec-2f1c-3084-8ba7-8157a1170913 | -6.92 | -42.89 | 2026-09-20 15:15:00 | MSG-03 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 194e3f1a-8828-36a0-aa01-10b3b415362a | -11.04 | -54.96 | 2026-09-20 15:15:00 | MSG-03 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 86d91717-ea01-3229-9a79-0cf5e18f2fde | -8.77 | -44.23 | 2026-09-20 15:15:00 | MSG-03 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| aa83d97f-e948-3350-ac72-810784a7013a | -10.77 | -50.57 | 2026-09-20 15:15:00 | MSG-03 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7b2d063b-60aa-3901-b718-6871c5ed44e7 | -11.65 | -43.4 | 2026-09-20 15:15:00 | MSG-03 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 7569c764-291a-342d-8f2d-6c5401eea3c3 | -12.52 | -50.04 | 2026-09-20 15:15:00 | MSG-03 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6619806e-d6e0-34ee-b5a9-f7ff8f7bb9e5 | -6.9 | -43.69 | 2026-09-20 15:15:00 | MSG-03 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 951073ff-a304-3dd1-be34-33556276daa2 | -17.22 | -51.74 | 2026-09-20 15:15:00 | MSG-03 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 0429c660-2fd4-3d9e-b475-3c5e75e7617f | -10.84 | -50.93 | 2026-09-20 15:15:00 | MSG-03 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 77f5351e-14b0-3637-aa05-038d72990349 | -11.11 | -54.03 | 2026-09-20 15:15:00 | MSG-03 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c38d0955-1cff-38e0-b6ed-5be5b5fb7811 | -10.48 | -50.99 | 2026-09-20 15:15:00 | MSG-03 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 70839a82-10bf-3bb4-9fb9-c0adad04e2aa | -9.86 | -48.4 | 2026-09-20 15:15:00 | MSG-03 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 86f8ea16-4f83-39fa-9088-848117623001 | -10.8364 | -50.9479 | 2026-09-20 15:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 238.6 |
| c1ec8de9-538c-3a08-8af0-f05ebf8795d1 | -8.3578 | -47.2599 | 2026-09-20 15:20:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 58.7 |
| ee3825a0-fbe8-3e7f-994f-1bd560dc2b54 | -6.8433 | -55.7602 | 2026-09-20 15:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 81.8 |
| 0623600f-2751-3b0d-9c9e-ad2f85d71502 | -6.1109 | -57.684 | 2026-09-20 15:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 71.7 |
| 8844c6c1-b772-3f33-aff5-de14ba253dbc | -10.7842 | -50.6133 | 2026-09-20 15:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 105.0 |
| 67655ac6-566d-3bbe-a7cb-3d7b0226df80 | -3.3311 | -59.8101 | 2026-09-20 15:20:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 55.0 |
| ef6794ae-b146-3a89-a89b-6ce5cc962748 | -9.6855 | -54.3114 | 2026-09-20 15:20:00 | GOES-19 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 63.5 |
| f58ccc0d-76e6-3196-a7b5-ecb5c25f271c | -5.9815 | -57.7672 | 2026-09-20 15:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 60.6 |
| 2998fa2e-c48e-3a9d-b1ea-2f3628a42859 | -10.279 | -50.2391 | 2026-09-20 15:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 101.7 |
| 7501c9d6-cce9-3d69-a7d3-a7d78f0e1d2c | -2.8779 | -58.2828 | 2026-09-20 15:20:00 | GOES-19 | SILVES | AMAZONAS | Brasil | 1304005 | 13 | 33 | nan | nan | nan | Amazônia | 61.1 |
| 77f3e080-cbc0-386a-9bad-a3bf11f5873b | -6.4302 | -59.9724 | 2026-09-20 15:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 165.4 |
| d59fa6b5-fec8-3138-87dd-f338db9a8e1e | -6.7666 | -59.1129 | 2026-09-20 15:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 92.9 |
| 668e0ba4-3d7a-3ee1-8360-23781b351d4c | -6.2831 | -59.9394 | 2026-09-20 15:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 46.9 |
| 3dc1f8a0-92d0-3a45-bf96-b1523c446300 | -6.0927 | -57.6457 | 2026-09-20 15:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 52.1 |
| 8e2860ec-d665-3fc6-87b6-f6b31f962730 | -2.8792 | -57.7796 | 2026-09-20 15:20:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 60.7 |
| 6c9c0300-9253-3c34-86ff-8704d0b99cf3 | -11.7162 | -54.5654 | 2026-09-20 15:20:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 82.8 |
| 0d7649a6-2b27-39a6-b8b8-9465fd215e6f | -9.0239 | -48.1622 | 2026-09-20 15:20:00 | GOES-19 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 78.9 |
| 3f33f250-8e90-33a0-9e35-876bb474279d | -12.0267 | -50.0231 | 2026-09-20 15:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 87.8 |
| 9841f285-510f-339e-aaa1-51fa4844f031 | -11.1225 | -49.4601 | 2026-09-20 15:20:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 108.3 |
| 37bb71e5-c5ea-3594-b9ea-c17f0e5ecd5f | -8.169 | -54.7231 | 2026-09-20 15:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 46.2 |
| 8352e69d-6a23-3da8-a2ee-d34b1d95c2df | -6.2026 | -57.7778 | 2026-09-20 15:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 57.3 |
| 69b0aa38-f199-3805-becd-e3796db380c6 | -11.0614 | -49.7477 | 2026-09-20 15:20:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 142.9 |
| 0e75644b-589b-31e2-b41c-3aa1308ce6a2 | -13.5911 | -51.458 | 2026-09-20 15:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 105.0 |
| 389abc56-ebb4-38fb-b6a9-68f397f5a73a | -11.4537 | -45.3892 | 2026-09-20 15:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 158.3 |
| 85593161-04d3-3dcd-a498-f2147e2b9287 | -3.0352 | -61.277 | 2026-09-20 15:20:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 49.4 |
| 232b104d-2088-345e-80b4-d19c5d802804 | -7.5703 | -57.6962 | 2026-09-20 15:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 51.1 |
| 4a3971b0-814d-3341-8b17-ae76624d5f8f | -3.3494 | -59.8097 | 2026-09-20 15:20:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 66.4 |
| 3f2b7a43-f033-3245-aa78-fe76ffc473d7 | -9.2567 | -46.2098 | 2026-09-20 15:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 123.6 |
| 2433305e-92e0-3e13-aac0-9262406837c7 | -13.0177 | -46.9125 | 2026-09-20 15:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 61.6 |
| b2b68781-56a6-3c22-aaa8-28e5abbbfa78 | -6.4587 | -58.1373 | 2026-09-20 15:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 45.4 |
| 4cd1e796-d830-34b3-8739-c36db99693c0 | 2.2003 | -50.8773 | 2026-09-20 15:20:00 | GOES-19 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 79.3 |
| de7792c5-73af-3303-9dcf-d73f52acccf8 | -9.8313 | -48.4073 | 2026-09-20 15:20:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 191.4 |
| 390ed605-549b-386b-b3b2-00ea705f46c5 | -10.4103 | -48.9112 | 2026-09-20 15:20:00 | GOES-19 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 95.6 |
| 1db14db5-6110-3983-9eaf-79288727f22e | -10.837 | -50.9054 | 2026-09-20 15:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 99.9 |
| 8d8d850e-d2f5-3e9c-9293-1ccf46bb4442 | -11.9543 | -49.7728 | 2026-09-20 15:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 221.8 |
| 7af73bd5-abaa-3579-8543-6b3438326507 | -10.0953 | -48.4445 | 2026-09-20 15:20:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 172.4 |
| 7fc21f1b-1a60-3312-8571-61ee7bba2e5a | -11.4541 | -45.3662 | 2026-09-20 15:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 97.6 |
| 1e50c050-f246-3a7c-b9cb-a9647783bbba | -13.5907 | -51.4794 | 2026-09-20 15:20:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 118.5 |
| 7fb97777-25de-35e5-9a38-2853c68a985c | -3.5894 | -59.0581 | 2026-09-20 15:20:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 61.2 |
| 4ce9569b-1714-37c4-ad16-b0f0652fd233 | -6.3655 | -58.316 | 2026-09-20 15:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 80.5 |
| 48ca8335-334d-387f-9287-25da662553a7 | -6.4671 | -59.9711 | 2026-09-20 15:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 176.7 |
| c2a6e817-5f60-389e-b5e9-e6ebf03b919d | -10.9694 | -57.1881 | 2026-09-20 15:20:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 62.0 |
| 79ed87a4-b163-3961-84f8-ae707972c5df | -2.9326 | -58.3397 | 2026-09-20 15:20:00 | GOES-19 | SILVES | AMAZONAS | Brasil | 1304005 | 13 | 33 | nan | nan | nan | Amazônia | 59.2 |
| b1606557-3b6d-3991-90f0-23235c8b9619 | -6.8216 | -59.1686 | 2026-09-20 15:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 57.6 |
| 16bb60c0-578b-3ec5-8405-e3d428381a0f | -10.4547 | -51.2405 | 2026-09-20 15:20:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 106.4 |
| 9eec1eb4-ed5d-34a6-b5b2-2bba2c5faa33 | -12.0454 | -50.0424 | 2026-09-20 15:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 167.2 |
| ccc600e5-ae87-36dc-aae3-e3a0cfdfbd78 | -2.9709 | -57.7197 | 2026-09-20 15:20:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 49.8 |
| bacaf1a0-8842-3ad6-8257-749626c9449d | -11.7354 | -54.5431 | 2026-09-20 15:20:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 123.2 |


[Clique aqui para ver as próximas entradas](README137.md)
