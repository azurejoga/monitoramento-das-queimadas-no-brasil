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

## Dados Diários - Página 125

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| acda8f9d-50e0-3463-88d2-417572bd9c32 | -6.27962 | -53.33826 | 2026-08-28 17:28:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| c2c06e0c-8eec-312b-a75f-8554a10f00dc | -2.78645 | -43.63489 | 2026-08-28 17:28:00 | NPP-375 | HUMBERTO DE CAMPOS | MARANHÃO | Brasil | 2105005 | 21 | 33 | nan | nan | nan | Cerrado | 24.4 |
| 34d0adac-ffe2-3931-8625-b24ebf7debf4 | -7.48109 | -61.40384 | 2026-08-28 17:28:00 | NPP-375 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 75ab1a66-b6bf-381c-b541-115491cf8e9a | -8.56878 | -64.17101 | 2026-08-28 17:28:00 | NPP-375 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 59d3ba20-a3ea-3562-b474-519498cb94fd | -11.41022 | -62.11852 | 2026-08-28 17:28:00 | NPP-375 | NOVA BRASILÂNDIA D'OESTE | RONDÔNIA | Brasil | 1100148 | 11 | 33 | nan | nan | nan | Amazônia | 31.3 |
| e226328c-ef46-3181-90a5-26cde18b4037 | -6.8426 | -59.9369 | 2026-08-28 17:28:00 | NPP-375 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 30.4 |
| d4702925-30b0-361d-b878-b52db7f54272 | -10.04864 | -68.82817 | 2026-08-28 17:28:00 | NPP-375 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 26.9 |
| a35ebd65-3f43-3960-bf11-3d331eea9f1f | -4.91283 | -56.26896 | 2026-08-28 17:28:00 | NPP-375 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 86434830-7c1f-3d23-b179-1781cdd17d0a | -5.14965 | -56.26807 | 2026-08-28 17:28:00 | NPP-375 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 55132d78-8367-3a39-a2f2-3f25ce185bbe | -2.85294 | -48.55572 | 2026-08-28 17:28:00 | NPP-375 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| d304a4fc-7e65-3137-9319-7c0dd7324b5d | -6.89855 | -43.64011 | 2026-08-28 17:28:00 | NPP-375 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 18.1 |
| 7efffea9-f014-3ccf-ad6f-15f4c4a62073 | -10.49335 | -64.4931 | 2026-08-28 17:28:00 | NPP-375 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 28.0 |
| 10e91329-b9a3-3193-bef8-394688256e3c | -1.70295 | -45.77398 | 2026-08-28 17:28:00 | NPP-375 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 2c312852-edd8-3f53-8c51-f8e2cf6dcaab | -9.43202 | -51.58717 | 2026-08-28 17:28:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 33c3f4dd-4dd5-3429-b259-4161513cc5d3 | -6.70986 | -47.80074 | 2026-08-28 17:28:00 | NPP-375 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| abce3045-ee5d-3c05-b16d-995f4c5fac64 | -2.72074 | -47.03582 | 2026-08-28 17:28:00 | NPP-375 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 51.9 |
| 8b45a4ea-b396-3ecd-b09a-472e0e3935b9 | -9.09103 | -50.5986 | 2026-08-28 17:28:00 | NPP-375 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 49ee7d82-f89c-35da-9df9-dcb53e8629e3 | -10.75188 | -54.00259 | 2026-08-28 17:28:00 | NPP-375 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 11.7 |
| f2db7f8e-c712-3532-8310-46444dca561d | -6.77987 | -55.6876 | 2026-08-28 17:28:00 | NPP-375 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 19.5 |
| 3aa8d36e-1146-347b-b6e5-ab94388d75fd | -8.59642 | -54.82741 | 2026-08-28 17:28:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 6291566d-c095-3f31-86dd-1e52808cec4b | -6.15793 | -57.8014 | 2026-08-28 17:28:00 | NPP-375 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 19.3 |
| 719f4951-ec09-339b-b34f-2f5c2655a72c | -3.5922 | -50.67476 | 2026-08-28 17:28:00 | NPP-375 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| b1ee51bb-9f7b-3b02-82be-5b9ec758945b | -5.79732 | -55.71862 | 2026-08-28 17:28:00 | NPP-375 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 7beac901-4147-3ed3-8270-f949cd0af8da | -9.50955 | -70.52225 | 2026-08-28 17:28:00 | NPP-375 | SANTA ROSA DO PURUS | ACRE | Brasil | 1200435 | 12 | 33 | nan | nan | nan | Amazônia | 13.3 |
| f9d46074-7dfa-37b5-8a38-b8034fffa734 | -6.83597 | -59.94213 | 2026-08-28 17:28:00 | NPP-375 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 16.4 |
| e1cf6414-a37f-3bf9-ab77-8e6d8c63b834 | -10.49374 | -64.49611 | 2026-08-28 17:28:00 | NPP-375 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 13.7 |
| eaf04a55-1ffa-3697-81f5-7c8b31460940 | -6.6039 | -55.45339 | 2026-08-28 17:28:00 | NPP-375 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 3f462620-f459-3b81-8acd-b577d1fb8dd9 | -9.66697 | -55.08957 | 2026-08-28 17:28:00 | NPP-375 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| f375c0fe-7052-39fb-976e-cc4986a75494 | -6.92072 | -59.48621 | 2026-08-28 17:28:00 | NPP-375 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 62.6 |
| 0e68bc02-aa8e-3480-adc1-510eea2b2fdb | -2.71757 | -47.03361 | 2026-08-28 17:28:00 | NPP-375 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 52.3 |
| cf14e55f-4c63-34ac-b062-c9327b337b2b | -7.2848 | -49.9575 | 2026-08-28 17:28:00 | NPP-375 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| b2fa5fbc-4ec0-3e84-9fa2-bc0ec1ad8f39 | -6.9066 | -43.64525 | 2026-08-28 17:28:00 | NPP-375 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 8.3 |
| f49295a6-2cf7-3b00-a211-86eed64a8d8d | -6.1651 | -57.78892 | 2026-08-28 17:28:00 | NPP-375 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 1ed2d9aa-4704-391c-b090-d790cdbc5c2a | -8.45269 | -70.42016 | 2026-08-28 17:28:00 | NPP-375 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 7e706ebb-17be-3c80-8aaa-a7e07ae1ce10 | -9.96966 | -53.93372 | 2026-08-28 17:28:00 | NPP-375 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 81.1 |
| e5f0283f-6519-30f1-afff-932fc21afbd2 | -10.75959 | -53.97004 | 2026-08-28 17:28:00 | NPP-375 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 15.0 |
| 13510740-e9ae-383d-93a0-c42eff7d3f27 | -7.07009 | -59.23212 | 2026-08-28 17:28:00 | NPP-375 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.3 |
| c356a843-4314-323b-8e25-ae6eb01b66b6 | -8.23454 | -54.96892 | 2026-08-28 17:28:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| ff102275-585a-327f-8c82-e920f4350f2b | -6.58465 | -55.4415 | 2026-08-28 17:28:00 | NPP-375 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| b7e1e794-2f67-30a9-8a9f-d3cc7fd5c65b | -9.50982 | -48.03416 | 2026-08-28 17:28:00 | NPP-375 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 3eb5cc7b-b248-3b31-afcd-d45d9d412099 | -6.17514 | -57.7874 | 2026-08-28 17:28:00 | NPP-375 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 14.7 |
| 017e2ba9-8244-3937-898f-954ae8693299 | -6.00404 | -57.83622 | 2026-08-28 17:28:00 | NPP-375 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| d30e0472-a3a5-3795-b456-322f3910239d | -8.44345 | -70.70222 | 2026-08-28 17:28:00 | NPP-375 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 26.5 |
| 0002096a-76b1-3bd1-b9b6-c714927ac685 | -4.47192 | -55.40421 | 2026-08-28 17:28:00 | NPP-375 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 96cd8387-47ad-3f75-a0a9-8776bfe55278 | -6.82698 | -51.89765 | 2026-08-28 17:28:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 3fc2b7f3-4131-3379-883d-1f387cd8b118 | -7.00838 | -59.57146 | 2026-08-28 17:28:00 | NPP-375 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 2f768275-0fee-344b-83d5-965e7333f8d5 | -3.67671 | -56.78157 | 2026-08-28 17:28:00 | NPP-375 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 5cb4087e-5e74-3bcf-b9b2-d84756153ca8 | -4.19796 | -55.23774 | 2026-08-28 17:28:00 | NPP-375 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 7309f80b-42c1-3109-9943-156578906481 | -5.98014 | -61.46799 | 2026-08-28 17:28:00 | NPP-375 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 24.8 |
| 668162d7-d99b-3693-8289-83a3f1f282e7 | -9.3442 | -48.16773 | 2026-08-28 17:28:00 | NPP-375 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| cbbefc17-a6aa-34fc-82cf-2e6757a25bbc | -6.94227 | -58.95585 | 2026-08-28 17:28:00 | NPP-375 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 26.9 |
| c7d03c85-790f-3b46-bd31-e735f939167e | -7.44338 | -65.17094 | 2026-08-28 17:28:00 | NPP-375 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 184b8aa6-6402-3231-8265-9971b18a355e | -9.07371 | -61.40984 | 2026-08-28 17:28:00 | NPP-375 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| eb37f14c-4c1a-3b65-86ff-d307659b8bcc | -9.20458 | -61.10984 | 2026-08-28 17:28:00 | NPP-375 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 23afd625-ea0f-333d-a7ee-f3aa336efbd7 | -5.8916 | -57.76402 | 2026-08-28 17:28:00 | NPP-375 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 112.1 |
| 1ef1c98f-144a-33fc-8bf2-d35d7a3a5ddb | -9.18537 | -59.63707 | 2026-08-28 17:28:00 | NPP-375 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 8bc1951c-69cf-3201-bcbe-a8fb11ce6f1a | -8.03397 | -48.01812 | 2026-08-28 17:28:00 | NPP-375 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d8094dea-c32c-35c8-9ba1-f447e65d2535 | -9.16517 | -59.57455 | 2026-08-28 17:28:00 | NPP-375 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 857ce3b2-830f-367e-b7bf-e5ebdcb88cbc | -7.57491 | -61.30544 | 2026-08-28 17:28:00 | NPP-375 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 261b4b2b-b1d0-35b4-8c9f-0087e8eed9b5 | -7.2738 | -49.86309 | 2026-08-28 17:28:00 | NPP-375 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 49.1 |
| f56cf4a6-3647-35f6-b230-5123a559cbf8 | -6.2398 | -53.47903 | 2026-08-28 17:28:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 555c5a03-f937-3274-892b-2f9a1e497334 | -10.75862 | -53.97812 | 2026-08-28 17:28:00 | NPP-375 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 20.0 |
| 9fea015a-7311-34fb-b949-fa8281509953 | -7.33784 | -55.68957 | 2026-08-28 17:28:00 | NPP-375 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| e451602b-4b2e-3df9-9a45-51aa76e92011 | -8.82679 | -49.59616 | 2026-08-28 17:28:00 | NPP-375 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 75672bee-49dd-3d5b-bc72-a5e73e951e0b | -6.27328 | -53.39365 | 2026-08-28 17:28:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 8a64ff79-0456-31ad-a8ab-2650ee591b51 | -10.77117 | -53.97598 | 2026-08-28 17:28:00 | NPP-375 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| d87a74ee-b017-3e22-b5f7-a8df2b311c63 | -5.20976 | -49.17866 | 2026-08-28 17:28:00 | NPP-375 | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 5952ff5b-6f0c-3d02-a462-8d7474061e6d | -2.72146 | -47.04007 | 2026-08-28 17:28:00 | NPP-375 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 51.9 |
| 979204f4-73ce-36fa-bb74-5840395f1f3a | -3.50604 | -56.85564 | 2026-08-28 17:28:00 | NPP-375 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 7653f3d9-887d-30c3-a2ed-973a211dfbd4 | -7.49843 | -55.2848 | 2026-08-28 17:28:00 | NPP-375 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 17.1 |
| 41723c83-efd5-3ed6-adf4-26fc8737079f | -9.40764 | -60.57422 | 2026-08-28 17:28:00 | NPP-375 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| cd6bf3db-4f9c-30db-92a4-9e4683d433af | -6.89285 | -59.02938 | 2026-08-28 17:28:00 | NPP-375 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 48a3e199-9d54-3df9-83f5-a105bce6ee2e | -8.56307 | -54.90398 | 2026-08-28 17:28:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 30.6 |
| aedb2b0c-4fdd-3a61-9af2-11d22f32604b | -8.33385 | -70.71715 | 2026-08-28 17:28:00 | NPP-375 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 24.6 |
| 16780d67-8683-3c1b-a5ab-3330d3393f2e | -6.82394 | -55.61019 | 2026-08-28 17:28:00 | NPP-375 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 35.5 |
| c9023db3-fdbe-3112-aa92-9d7610718d7d | -7.22585 | -51.69476 | 2026-08-28 17:28:00 | NPP-375 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 90244f88-77e6-38f3-af78-1c62c75ba596 | -6.39121 | -57.47089 | 2026-08-28 17:28:00 | NPP-375 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 5c7f6a07-4eb6-383f-b211-320549172635 | -4.90892 | -56.26591 | 2026-08-28 17:28:00 | NPP-375 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 5999125c-d138-3697-ad2d-4e33917f61a0 | -6.80898 | -59.60856 | 2026-08-28 17:28:00 | NPP-375 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 6714c66e-6b35-3e23-8d41-08202a73ecd3 | -10.56859 | -57.48448 | 2026-08-28 17:28:00 | NPP-375 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 2a41e98e-4253-3f39-b3eb-ac270f7dc67d | -7.73945 | -61.0896 | 2026-08-28 17:28:00 | NPP-375 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 13b64a43-9554-3017-ad51-e4cff89c16d9 | -10.77055 | -53.97218 | 2026-08-28 17:28:00 | NPP-375 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 77d4d46c-f71b-3b1b-b425-f4a6368688a3 | -6.79295 | -56.31932 | 2026-08-28 17:28:00 | NPP-375 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 1c503c06-a986-3c3e-8d63-4eba43803697 | -8.02044 | -48.01196 | 2026-08-28 17:28:00 | NPP-375 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 23a652ee-6d92-3150-8ade-360615a8247f | -5.34415 | -45.1573 | 2026-08-28 17:28:00 | NPP-375 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 2a0dc16a-bc31-3462-af3b-44862092b604 | -5.84833 | -57.74909 | 2026-08-28 17:28:00 | NPP-375 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 0c5700dc-e94f-3bb4-b939-5c498bfc4fe1 | -8.09261 | -51.65947 | 2026-08-28 17:28:00 | NPP-375 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 41c58aa2-ef0b-3a90-86c1-3832e39fbc43 | -6.17632 | -57.70467 | 2026-08-28 17:28:00 | NPP-375 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d6d82c14-343a-3155-8dae-b3af796a15f5 | -8.33328 | -70.7176 | 2026-08-28 17:28:00 | NPP-375 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 25.9 |
| bad8600d-6789-325d-a8f8-641ab9cced77 | -4.30522 | -59.4681 | 2026-08-28 17:28:00 | NPP-375 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 9.6 |
| f5caa73f-3d26-3bc9-9c68-42efc0d71019 | -8.59817 | -55.28133 | 2026-08-28 17:28:00 | NPP-375 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 9bd3a6e9-fbec-311f-a0ea-2fe05f7ba79c | -8.43467 | -70.33575 | 2026-08-28 17:28:00 | NPP-375 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 31.9 |
| eef6d6ef-0bb1-32a7-8e72-308a71e32c8e | -6.75747 | -58.72262 | 2026-08-28 17:28:00 | NPP-375 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 90dbe058-e193-3289-a42a-84a9f03ca5cd | -9.17309 | -59.57788 | 2026-08-28 17:28:00 | NPP-375 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 14.4 |
| 0503b0a5-4cfc-33a1-bd11-c4b720f0efaa | -7.43484 | -56.14754 | 2026-08-28 17:28:00 | NPP-375 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 69a9b34b-5566-37cf-a9fe-401fe78323ff | -10.39158 | -61.20289 | 2026-08-28 17:28:00 | NPP-375 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 57038b6e-b494-3862-950b-fbfbd481c013 | -4.16336 | -57.55176 | 2026-08-28 17:28:00 | NPP-375 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 2020a448-f1ab-3119-aa02-23d88b42f604 | -4.30233 | -59.47238 | 2026-08-28 17:28:00 | NPP-375 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 23.6 |
| 263ac005-0de1-380f-b5ee-8e05ce453a26 | -2.71965 | -47.04641 | 2026-08-28 17:28:00 | NPP-375 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 89.9 |
| 1bcd2dd9-4525-32ee-8fae-6627bd69332a | -6.25397 | -55.42337 | 2026-08-28 17:28:00 | NPP-375 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |


[Clique aqui para ver as próximas entradas](README126.md)
