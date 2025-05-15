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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 64eb34fe-79d6-3315-a0d5-16870dfb1950 | -8.16214 | -46.49771 | 2025-05-15 04:25:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a9b19cd5-b379-3e34-9cbb-83116a439303 | -6.18353 | -48.06543 | 2025-05-15 04:25:00 | NOAA-21 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f9863d03-75fe-384e-8a45-7ec19efe9c4f | -6.55615 | -44.49652 | 2025-05-15 04:25:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8443c427-40dd-3ebe-b45f-a0f67563a4d3 | -5.76143 | -43.49554 | 2025-05-15 04:25:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 71a48b4a-6b34-3661-85f4-cfb2e0283a0b | -5.74263 | -47.98898 | 2025-05-15 04:25:00 | NOAA-21 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0400a071-fd79-3913-8fac-264ff2dc84fa | -8.86755 | -37.78944 | 2025-05-15 04:25:00 | NOAA-21 | MATA GRANDE | ALAGOAS | Brasil | 2705002 | 27 | 33 | nan | nan | nan | Caatinga | 0.7 |
| df9d8148-0417-30cb-bea5-dd0bc1d71c5e | -9.65632 | -47.55967 | 2025-05-15 04:25:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2d73db31-192c-3476-832f-8053a31951cd | -6.1739 | -48.06012 | 2025-05-15 04:25:00 | NOAA-21 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 16.1 |
| f8684236-a79f-3969-847b-2f9667b21011 | -6.17672 | -48.06432 | 2025-05-15 04:25:00 | NOAA-21 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 16.1 |
| c31a0032-a1ff-3d19-bb39-6fb00bbc28ba | -8.80295 | -49.81688 | 2025-05-15 04:25:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d24a857b-2ba5-33c7-859b-b5a7f75c8348 | -8.71287 | -50.25125 | 2025-05-15 04:25:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 4e826b24-39b6-3399-9127-8d457cc32ba0 | -6.64955 | -41.99382 | 2025-05-15 04:25:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 0ec0caba-86bc-3062-915b-dc49de03a400 | -8.72177 | -47.97672 | 2025-05-15 04:25:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 115ff2f5-3832-3df9-a2a7-66e9e1415aa0 | -6.04948 | -47.96081 | 2025-05-15 04:25:00 | NOAA-21 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9dc9af3f-978c-3b94-945d-3a575f9a6c16 | -6.17614 | -48.06802 | 2025-05-15 04:25:00 | NOAA-21 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| d92b833e-63f8-3147-8627-82ae2d81dd17 | -7.07332 | -44.39227 | 2025-05-15 04:25:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| f05d4fca-c652-357f-85f5-e5e7627e5a96 | -8.71358 | -50.24693 | 2025-05-15 04:25:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 699f069a-438e-37b8-86b7-d91238b869ef | -6.65412 | -41.98954 | 2025-05-15 04:25:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 27.3 |
| 8f5651e3-a9a4-3134-b50b-2dd502a55eea | -8.86799 | -37.78615 | 2025-05-15 04:25:00 | NOAA-21 | MATA GRANDE | ALAGOAS | Brasil | 2705002 | 27 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 08af1726-6c1d-3102-b758-cf24d267ec52 | -6.1773 | -48.06066 | 2025-05-15 04:25:00 | NOAA-21 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 46e9994b-cf5b-3885-9af2-6a38f4ff4e50 | -11.95042 | -46.58829 | 2025-05-15 04:27:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 90f9296c-9fb4-39d7-8ee6-06dd70c121a8 | -13.53466 | -44.05052 | 2025-05-15 04:27:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0570154f-84d9-38bb-8fad-836d8cf2f967 | -11.77812 | -47.35177 | 2025-05-15 04:27:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 0808a9af-8c9d-35d0-8c07-460081bcf37c | -13.62691 | -47.70923 | 2025-05-15 04:27:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 95783a2b-bf5d-3aba-b9cb-52df50f8bc56 | -13.27702 | -45.43756 | 2025-05-15 04:27:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1ea0f1b3-2b75-379d-8ad7-894f4054d63b | -13.68972 | -47.76622 | 2025-05-15 04:27:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| aaa40b0b-d740-359d-ac57-3ccf66a8d5bb | -11.78748 | -47.35686 | 2025-05-15 04:27:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 30081078-d603-3fb0-b2c1-bdebe6d6f57a | -13.07202 | -52.01531 | 2025-05-15 04:27:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1f26681d-42bd-3c89-b0fc-af0b62e3628c | -11.55562 | -47.62037 | 2025-05-15 04:27:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c0b75e27-e668-3dfc-ac7b-ec4be87ed27e | -11.2457 | -49.4916 | 2025-05-15 04:27:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 64ba343a-c663-3d02-b0af-e16396f02857 | -11.96685 | -48.1202 | 2025-05-15 04:27:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bcad0253-0679-3cbd-813b-0efd1c0879ed | -9.78789 | -56.13049 | 2025-05-15 04:27:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 011f3387-56fb-31a0-9f9a-303412d19a4d | -10.34193 | -47.67783 | 2025-05-15 04:27:00 | NOAA-21 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 32465ce3-11c2-3bb8-b767-8816caaca1d0 | -10.4733 | -49.14032 | 2025-05-15 04:27:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2b1258c1-9707-3ad8-a988-523cb4b5f9fc | -11.65319 | -58.2614 | 2025-05-15 04:27:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1b393363-7c2a-30cc-9474-b698be4aca42 | -12.72598 | -54.97067 | 2025-05-15 04:27:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 48d8f5ff-b8c5-3a2b-9cac-80924f66ff4e | -11.38841 | -57.82992 | 2025-05-15 04:27:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c7574ccb-5ec5-39e5-93cb-0b174e4e6a79 | -16.61407 | -53.41024 | 2025-05-15 04:27:00 | NOAA-21 | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4f370964-c8da-34dd-803f-d3f7b97ea697 | -12.18683 | -48.68126 | 2025-05-15 04:27:00 | NOAA-21 | SUCUPIRA | TOCANTINS | Brasil | 1720853 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7aea4b6e-ec8d-38e9-9370-c2ab27628254 | -11.84099 | -46.63652 | 2025-05-15 04:27:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 18ee3fd4-0cee-3f8e-b151-956e6bb7ac32 | -15.78279 | -47.15167 | 2025-05-15 04:27:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5d1676da-fb27-34d7-9117-cc22feb46e2b | -13.29705 | -47.79615 | 2025-05-15 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 58d02dc6-7536-3337-a210-1122af7b08d5 | -11.56376 | -47.43881 | 2025-05-15 04:27:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 3687ba0a-a9c7-3cac-8b22-0ccf3b167a91 | -12.99587 | -48.88229 | 2025-05-15 04:27:00 | NOAA-21 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 25900f45-b868-3047-97f3-b06cce2e3638 | -11.38347 | -57.82497 | 2025-05-15 04:27:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0461baa4-fb24-3225-8b31-35b6fc4dbfb5 | -17.11346 | -49.14399 | 2025-05-15 04:27:00 | NOAA-21 | HIDROLÂNDIA | GOIÁS | Brasil | 5209705 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 3a9360ed-4c8b-31d1-baaa-1c39289e905a | -13.27642 | -45.4174 | 2025-05-15 04:27:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 68bf7bd3-4152-3a6b-80aa-3b754fe01db7 | -15.23263 | -51.19205 | 2025-05-15 04:27:00 | NOAA-21 | BRITÂNIA | GOIÁS | Brasil | 5203807 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0a5327c7-9fc4-3ea6-b7be-36f1912a81f9 | -13.03771 | -53.52885 | 2025-05-15 04:27:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bda8644f-7faf-3a98-829d-d2e4b28cb3fa | -13.07581 | -52.016 | 2025-05-15 04:27:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 052dc5b1-1abc-3e21-baa3-3f36d3e00f92 | -13.16274 | -53.27547 | 2025-05-15 04:27:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5d8f735f-2e7d-3818-acb2-a36b7bdfbc91 | -12.12101 | -54.66228 | 2025-05-15 04:27:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4ee5f2d3-36b0-314f-91c4-77366bb75f03 | -10.35216 | -47.97906 | 2025-05-15 04:27:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dc19aa1f-3852-3475-aa1a-d89b65938576 | -13.67122 | -53.93088 | 2025-05-15 04:27:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 32c280d6-744f-3d87-b829-118da622b00e | -12.18401 | -48.68104 | 2025-05-15 04:27:00 | NOAA-21 | SUCUPIRA | TOCANTINS | Brasil | 1720853 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9dec9a93-fa40-3fe4-8f53-06a63d20dc3f | -16.61489 | -53.40704 | 2025-05-15 04:27:00 | NOAA-21 | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 006e10b5-4804-3255-babe-2f0abe3a5ee6 | -13.69027 | -47.76269 | 2025-05-15 04:27:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 410ab843-8ccf-35c0-873c-732e75f7ddec | -13.27585 | -45.42133 | 2025-05-15 04:27:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2b329b5c-b99f-3667-a733-76bdb2cb6303 | -14.06616 | -57.1082 | 2025-05-15 04:27:00 | NOAA-21 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d4dccbb1-3d4d-38d5-a4ea-66b0a73b2a18 | -11.55287 | -47.61634 | 2025-05-15 04:27:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e6c31477-69c2-3937-aded-2feebf83c95e | -15.38714 | -48.00468 | 2025-05-15 04:27:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| dde98e8e-f8d7-35ef-b7e8-f1c840d01089 | -12.87411 | -55.06773 | 2025-05-15 04:27:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 45ec4789-9f72-3059-ba7f-3f48238736d0 | -11.08279 | -47.29281 | 2025-05-15 04:27:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c0445ff2-4be7-3df8-954a-2d3cfe8a2c9a | -11.78693 | -47.36036 | 2025-05-15 04:27:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 9750cd13-14ed-391a-8411-6cf01bf62289 | -10.65943 | -44.49047 | 2025-05-15 04:27:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a1b3cd9f-39e7-3daa-b3a8-88bf96195623 | -11.69591 | -48.81534 | 2025-05-15 04:27:00 | NOAA-21 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d733adf5-2c31-3520-a4fc-97d0848ce985 | -11.87575 | -56.41599 | 2025-05-15 04:27:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 89987e03-e51c-31f7-b7f9-675c41e735f6 | -15.26274 | -51.46321 | 2025-05-15 04:27:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 83967bfd-2212-3c0a-9cf0-b451af683f96 | -13.28397 | -45.43862 | 2025-05-15 04:27:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 135ed3a9-79e6-34b5-bfae-242955d18378 | -11.24632 | -49.48779 | 2025-05-15 04:27:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8fe92f9c-3f88-3d48-83bb-1a352604dc21 | -12.8704 | -55.06192 | 2025-05-15 04:27:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0f0fede0-4a4a-3f5e-a183-e53ad9f3797c | -11.94709 | -46.58778 | 2025-05-15 04:27:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 40049927-ef59-3c93-b01a-ee90992ca6e8 | -10.63559 | -46.27275 | 2025-05-15 04:27:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b4b59a97-75c0-30ea-b6ac-e32e6231412e | -13.28687 | -45.44307 | 2025-05-15 04:27:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 01f77a69-cd1b-3842-80e3-f963e3a3f1a2 | -13.53313 | -44.04834 | 2025-05-15 04:27:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 93eeb235-65f7-30a2-9eac-fd2b436a16ea | -11.42377 | -54.3325 | 2025-05-15 04:27:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 16eafc35-a5d5-38b2-bb29-ab18e210931f | -13.27355 | -45.43702 | 2025-05-15 04:27:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 0d99ccc3-5edc-3b74-838c-0dd3b2ae2f6a | -11.91649 | -54.40889 | 2025-05-15 04:27:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6b3e22d6-533f-3fc0-a2f3-437d155f6e24 | -11.55342 | -47.61284 | 2025-05-15 04:27:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5e0882b2-8d72-3770-877a-833b2d07f748 | -13.28222 | -45.4263 | 2025-05-15 04:27:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 36bd54fe-3155-32dc-860e-24519f61a72c | -10.63688 | -48.09394 | 2025-05-15 04:27:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d8333f98-38d7-33ce-8bbc-92fa1c020131 | -13.69357 | -47.76322 | 2025-05-15 04:27:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8d41eef6-71b0-3243-8c3e-00594fc4cc64 | -11.15395 | -48.67025 | 2025-05-15 04:27:00 | NOAA-21 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| dcfc51b8-2ed4-33f0-af10-657e0fb12e9f | -13.26947 | -45.41633 | 2025-05-15 04:27:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 48ad545f-a1bb-3e42-95cf-793675f5a840 | -10.47611 | -49.14462 | 2025-05-15 04:27:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 88d2da4f-f1bd-3161-80a9-fba4b88babd8 | -17.78042 | -42.80873 | 2025-05-15 04:27:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1eab3265-1daa-325d-97c2-c77f6bff16db | -13.27527 | -45.42525 | 2025-05-15 04:27:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f60552ae-4128-3b93-b5c9-9edec9912efb | -11.15337 | -48.67387 | 2025-05-15 04:27:00 | NOAA-21 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 07596550-8581-307d-bedb-030322e71bd5 | -14.52632 | -51.06806 | 2025-05-15 04:27:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1178e0a0-3c7c-3ba4-8aa2-0f2dbf594439 | -11.65112 | -48.11541 | 2025-05-15 04:27:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 24.4 |
| fd70e783-42d2-3b16-8394-c32cf284d979 | -12.10849 | -44.74529 | 2025-05-15 04:27:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0f7966aa-da1b-3b51-9ff9-7193bc857895 | -11.60809 | -47.99951 | 2025-05-15 04:27:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 401f48fa-21eb-3fe4-b877-22263a1ed66f | -17.17943 | -50.92764 | 2025-05-15 04:27:00 | NOAA-21 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 48b50754-2327-38f1-9eb7-b6cb94ce0bea | -13.28802 | -45.4352 | 2025-05-15 04:27:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 715870a1-40cd-3811-aa60-e96dcfc2f5e6 | -11.68478 | -44.85151 | 2025-05-15 04:27:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f375cb59-77db-3b49-91da-4eaafa4b5eb3 | -14.44735 | -51.54737 | 2025-05-15 04:27:00 | NOAA-21 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 55fb6087-9ec8-3c08-8e0d-81dd6b39ca2a | -13.04282 | -53.7179 | 2025-05-15 04:27:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 2b91df70-fb92-3062-8ffd-11bc192c5b48 | -11.1573 | -48.6708 | 2025-05-15 04:27:00 | NOAA-21 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d54c60b8-238c-30ae-a5b3-aa550772905f | -10.33558 | -47.97591 | 2025-05-15 04:27:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| f5f8dbd4-7d7d-3297-a1b1-db17f41168fa | -11.65168 | -48.11187 | 2025-05-15 04:27:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 24.4 |


[Clique aqui para ver as próximas entradas](README6.md)
