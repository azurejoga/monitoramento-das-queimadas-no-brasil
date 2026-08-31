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

## Dados Diários - Página 92

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| be526e47-2fad-3212-88ee-fa65652ac462 | -7.3118 | -60.5897 | 2026-08-31 14:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 161.9 |
| c77ca012-ac09-3204-972e-2a81d6dda349 | -11.2485 | -45.0963 | 2026-08-31 14:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 127.9 |
| 8facc226-e2d0-3912-9b33-b89c226fadb3 | -7.5845 | -61.3423 | 2026-08-31 14:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 92.7 |
| b500ea01-4d88-3983-bae1-468a02c9fa1b | -11.229 | -45.1221 | 2026-08-31 14:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 96.3 |
| 22662dfa-8abd-3b07-93c9-088dda69a2a5 | -11.2295 | -51.2667 | 2026-08-31 14:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 65.8 |
| fc953f87-a7e4-36fe-8830-8a263d1efbc4 | -13.4379 | -51.4348 | 2026-08-31 14:20:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 59.6 |
| 93736661-b33a-3dc7-b01d-b9bd897247a1 | -7.5843 | -61.3803 | 2026-08-31 14:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 84.2 |
| 29cca926-fad3-35c8-b374-72780e2470d3 | -5.8967 | -59.9719 | 2026-08-31 14:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 67.2 |
| 26e8c931-d4da-3461-92d5-905197eb052e | -10.1084 | -50.299 | 2026-08-31 14:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 128.3 |
| f922caf5-a60c-365c-b64a-3c46f4441da2 | -7.5844 | -61.3613 | 2026-08-31 14:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 71.2 |
| d9d2ceaf-3bdb-3469-b132-6330d41d7dc1 | -12.9032 | -45.8382 | 2026-08-31 14:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 122.8 |
| d7ea9e63-311d-3064-b29b-bda134c4c1a8 | -7.917 | -61.3481 | 2026-08-31 14:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 51.1 |
| c25855a0-e20d-36b1-988f-84f801475571 | -14.1456 | -52.8082 | 2026-08-31 14:20:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 86.9 |
| 2b0e1f0e-5eca-3756-b5cf-513e60039fc8 | -10.7596 | -54.0384 | 2026-08-31 14:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 145.1 |
| 89665bf9-a8ea-37a4-842c-c813809ec889 | -11.3615 | -45.1955 | 2026-08-31 14:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 170.9 |
| 34d9c282-4b22-39ec-88c1-a1b5eb2907c6 | -18.2704 | -52.6851 | 2026-08-31 14:20:00 | GOES-19 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 165.4 |
| 43eb0ff3-6003-3c93-bced-3fe8494775c0 | -15.8649 | -56.4841 | 2026-08-31 14:20:00 | GOES-19 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 67.7 |
| 00cecadf-f470-36ac-af7e-1bf72f1ca34f | -11.9186 | -45.0685 | 2026-08-31 14:20:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 110.7 |
| b1061ba9-34c4-3348-b6ef-52f344f61ef5 | -11.1726 | -51.2728 | 2026-08-31 14:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 51.5 |
| c53eeb30-5a1a-365d-a80f-f03691bede40 | -9.5961 | -47.6424 | 2026-08-31 14:20:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 118.7 |
| c4c8191e-84f6-3ee6-bdd5-8215b933d204 | -7.9907 | -46.5177 | 2026-08-31 14:20:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 143.8 |
| 74a21b1e-3621-35dc-b86a-a8d84ab7d2a4 | -10.8046 | -50.5046 | 2026-08-31 14:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 70.8 |
| 946ab516-4eb4-3b6c-b4e2-7a8ef110b8f2 | -11.5475 | -45.4906 | 2026-08-31 14:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 130.9 |
| fd1d4606-a5bf-3267-9903-a94fd391270e | -11.3806 | -45.1928 | 2026-08-31 14:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 222.6 |
| 486c5555-a546-3c86-9686-c6a5246ebe43 | -6.1109 | -57.684 | 2026-08-31 14:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 114.2 |
| 17087b66-be0c-35ca-8775-493c4c14fc65 | -9.862 | -64.9771 | 2026-08-31 14:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 50.9 |
| 3cd97117-17c1-3910-b9f6-25ddff44de6c | -10.1538 | -45.6982 | 2026-08-31 14:20:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 148.9 |
| 8ad605ac-724f-3712-92db-652053025a3d | -7.1189 | -42.2025 | 2026-08-31 14:20:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 101.0 |
| af311dde-1087-3b29-84c1-b15b0b8db792 | -14.5868 | -54.1153 | 2026-08-31 14:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 102.8 |
| 5fd4aa90-4eb1-3d07-9cf8-5019a68a5f51 | -11.1634 | -50.5727 | 2026-08-31 14:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 87.4 |
| e438f943-7386-34e1-9968-f003556a583b | -7.1126 | -42.749 | 2026-08-31 14:20:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 111.2 |
| 1b5311a7-fb98-38d3-bb67-f41e7fb33375 | -5.2548 | -55.8907 | 2026-08-31 14:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 77.4 |
| a1d7a108-ff4f-3bb9-980d-9a744c9821a8 | -11.9378 | -45.0656 | 2026-08-31 14:20:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 120.6 |
| 27c4f38a-35c1-380b-866d-248087dcd823 | -15.4601 | -52.806 | 2026-08-31 14:20:00 | GOES-19 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 154.9 |
| 1874d565-286d-37d8-b008-c6379e0888a1 | -11.3236 | -45.1778 | 2026-08-31 14:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 102.2 |
| f8894081-e447-3546-b6a1-3e15b7be2f6e | -14.1263 | -52.8106 | 2026-08-31 14:20:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 86.5 |
| b57246ba-9cee-3120-8d00-3d2c0d40bfb4 | -8.87 | -66.8935 | 2026-08-31 14:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 66.3 |
| af7ce1d0-02c9-3db9-a0f4-7cdae835daf8 | -9.1711 | -59.618 | 2026-08-31 14:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 48.7 |
| c50ef1d6-0acf-30bb-999f-c07e3bb52033 | -7.6149 | -44.8833 | 2026-08-31 14:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 124.5 |
| e934555b-c399-3922-865b-94ce32f5ae8d | -6.7832 | -59.4401 | 2026-08-31 14:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 55.8 |
| 25f762a1-3d74-3b9e-aa3f-4f9baec17e72 | -9.5967 | -47.5983 | 2026-08-31 14:20:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 135.7 |
| c6043030-6c87-3a3f-99e7-367bbdb76667 | -9.5964 | -47.6204 | 2026-08-31 14:20:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 273.5 |
| 7c227187-8dab-3d65-ad6d-26698f388650 | -6.9176 | -55.7166 | 2026-08-31 14:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 76.9 |
| d8d7288e-f338-361e-82c2-80c777cf493d | -7.9797 | -44.2962 | 2026-08-31 14:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 183.1 |
| 42f76b58-52e5-3b4f-bd5b-eb149b559776 | -7.3117 | -60.6089 | 2026-08-31 14:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 64.4 |
| af965cfb-dacd-3e8a-9b09-55fca1337b86 | -7.9172 | -61.329 | 2026-08-31 14:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 55.1 |
| 94ff0cb2-bbb5-3e9f-b224-1ced2925ee46 | -11.5479 | -45.4676 | 2026-08-31 14:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 104.8 |
| a164976f-3467-3f89-9703-2f6c4c84c380 | -18.2904 | -52.6818 | 2026-08-31 14:20:00 | GOES-19 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 109.1 |
| 0e063816-b840-3dac-875d-6981495de33e | -6.9177 | -55.6967 | 2026-08-31 14:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 52.1 |
| b2a2e2ca-8a25-3cd9-a4c1-c25f5087326b | -14.2792 | -52.8758 | 2026-08-31 14:20:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 112.3 |
| 182ce80d-535b-37f4-b832-f6ee26240cb1 | -7.3301 | -60.6081 | 2026-08-31 14:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 57.8 |
| 8652cbcc-11b7-3f0a-be70-dae65b8bf16d | -7.9605 | -44.3212 | 2026-08-31 14:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 189.4 |
| 712b87e2-15a4-3401-b4ff-ff4e3daec46a | -9.4721 | -57.0156 | 2026-08-31 14:20:00 | GOES-19 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 71.8 |
| 6051cc1e-a701-31e1-9469-f579f609366e | -18.27 | -52.7068 | 2026-08-31 14:20:00 | GOES-19 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 148.1 |
| c31428f4-7d5d-3f73-9a16-d160a8696051 | -11.0747 | -51.5153 | 2026-08-31 14:20:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 87.7 |
| 51930d5a-2753-31df-8ffb-640a8abff632 | -14.5871 | -54.0944 | 2026-08-31 14:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 70.3 |
| 69e02733-b5b4-34e3-aaa5-dd1144d72f73 | -10.7598 | -54.0179 | 2026-08-31 14:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 82.2 |
| 431239f3-acf6-3a14-950c-7a33f0fb3846 | -10.7409 | -54.0196 | 2026-08-31 14:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 65.6 |
| 09e65434-065d-3f39-9b89-975b09463434 | -7.5846 | -61.3232 | 2026-08-31 14:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 61.5 |
| d2e6a6dd-875d-38f9-9ae2-9c2cbb048b99 | -11.2294 | -45.099 | 2026-08-31 14:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 117.4 |
| 3a4627f7-3b14-3b24-a180-3f8da02b1dfd | -12.1905 | -50.5194 | 2026-08-31 14:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 56.8 |
| 76408fc8-0b96-342c-894f-bb906481d503 | -10.8541 | -48.3587 | 2026-08-31 14:20:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 63.6 |
| 756d8e51-9214-3ed4-8d37-4d46669daf84 | -7.6251 | -55.2987 | 2026-08-31 14:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 54.8 |
| d255ae46-59a1-3ee7-bc62-4ceb4d5e12e7 | -8.7628 | -46.4642 | 2026-08-31 14:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 124.2 |
| 2cb94807-d64f-37bb-a0ab-dab0b0f7573e | -14.4004 | -52.5438 | 2026-08-31 14:20:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 83.1 |
| 2ebafe2e-6d42-3bde-b6d6-26912f770215 | -8.7631 | -46.4418 | 2026-08-31 14:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 105.5 |
| fdfa29ef-1a14-3259-8dab-48d47ac0880e | -11.2298 | -51.2456 | 2026-08-31 14:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 90.3 |
| 2f7b4fc8-04b8-392a-8dc5-fd285f041f60 | -11.1545 | -51.2112 | 2026-08-31 14:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 66.1 |
| d904e621-6c54-3165-994e-2cd52827e858 | -7.5658 | -61.3811 | 2026-08-31 14:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 84.6 |
| 68f8794b-2460-333e-a027-de8e6a27db62 | -8.7439 | -46.4661 | 2026-08-31 14:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 87.1 |
| 99e17c7e-9e75-312c-acf6-aefa4d2fc6ff | -18.2695 | -52.7284 | 2026-08-31 14:20:00 | GOES-19 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 55.1 |
| 51225023-7d64-3a00-895b-6d604b88b98e | -11.0936 | -51.5134 | 2026-08-31 14:20:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 66.5 |
| 79aa47b8-9f38-3394-87ba-cb29cc2eb668 | -7.2933 | -60.5905 | 2026-08-31 14:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 92.4 |
| afac3ed5-98f2-319d-883a-1bafc3123aef | -11.1916 | -51.2708 | 2026-08-31 14:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 61.6 |
| 327bde9c-26da-3133-8d7a-a7e45659ad97 | -14.2796 | -52.8547 | 2026-08-31 14:20:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 74.9 |
| e05ada31-e8da-3c25-a6b9-6bfef5f6404c | -10.7407 | -54.0401 | 2026-08-31 14:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 153.7 |
| 08b6e3b9-9850-3463-a278-5a9a8ecc48e5 | -6.1295 | -57.6637 | 2026-08-31 14:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 89.0 |
| 6a9dfced-ef61-336d-bdea-54b8bde734f2 | -5.8537 | -57.5576 | 2026-08-31 14:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 53.2 |
| 0b34f23a-d872-3a26-8117-45427360ea01 | -11.1821 | -50.592 | 2026-08-31 14:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 139.7 |
| 44658d37-5ecf-382f-8815-411a2edaba7e | -7.9425 | -44.2538 | 2026-08-31 14:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 101.0 |
| 8343cb91-feb7-3e4c-ad2b-e74614d24af3 | -5.2362 | -55.9112 | 2026-08-31 14:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 89.1 |
| b1fde5dd-9deb-38d7-8751-a20df5bf5328 | -5.2547 | -55.9105 | 2026-08-31 14:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 176.8 |
| 7fded66b-e4bf-3a57-99a9-c8bec0b507d1 | -3.6076 | -59.0769 | 2026-08-31 14:20:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 54.3 |
| b9265538-5035-3860-8714-c11e3d32ec14 | -5.8966 | -59.9911 | 2026-08-31 14:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 59.9 |
| 2d773c43-b370-3827-b480-12f11215012a | -14.1902 | -45.3008 | 2026-08-31 14:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 95.3 |
| 87463cad-c6ce-3ef2-b11a-81552b5a86b9 | -3.6398 | -60.5656 | 2026-08-31 14:20:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 56.0 |
| d98d056d-b4b1-30ea-b80e-091f3cd2cff2 | -10.3394 | -49.9547 | 2026-08-31 14:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 75.9 |
| 1686af93-4670-36ca-9965-9cffae38f28b | -11.2503 | -54.0146 | 2026-08-31 14:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 72.0 |
| 6808b968-bbd8-3b68-b670-01afb4ebbf86 | -15.346 | -53.7912 | 2026-08-31 14:20:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 90.8 |
| 88142d71-940e-3bc7-838a-31dfb239b266 | -11.0744 | -51.5365 | 2026-08-31 14:20:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 70.3 |
| 3195049f-c9ec-3e31-8487-1c57c63fcd63 | -6.9367 | -55.636 | 2026-08-31 14:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 94.1 |
| 30b75366-2cd8-3afd-8d3a-b9b5dd3fb420 | -3.6215 | -60.566 | 2026-08-31 14:20:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 119.6 |
| d786808f-82bd-39e4-bc7f-8cffafc2ad4e | -7.9794 | -44.3193 | 2026-08-31 14:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 441.7 |
| 19292fbb-0066-39fc-9ebd-e81bff3717ca | -9.4342 | -45.6704 | 2026-08-31 14:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 105.0 |
| e1e74871-20fa-3124-96f8-31e6662943a0 | -6.389 | -45.5116 | 2026-08-31 14:20:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 107.5 |
| 5767a327-e4ef-3f13-a2fd-26948fd086cc | -10.1087 | -50.2776 | 2026-08-31 14:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 177.2 |
| fd02401e-1a5b-3fbf-b664-9b958dd9c4e4 | -4.9604 | -55.8424 | 2026-08-31 14:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 65.5 |
| 2d832cd4-927a-35d9-b682-1ec855e271ad | -14.4007 | -52.5226 | 2026-08-31 14:20:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 78.0 |
| b79b4e55-416f-36cd-8187-5cd897e1e6f7 | -11.1824 | -50.5706 | 2026-08-31 14:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 152.3 |
| e73bf90d-8344-3755-8fbc-18243bd6cc58 | -11.2103 | -45.1017 | 2026-08-31 14:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 77.2 |


[Clique aqui para ver as próximas entradas](README93.md)
