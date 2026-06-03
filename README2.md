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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d826634f-fe60-3a2e-b294-3de502041aca | -16.17812 | -58.48125 | 2026-06-03 00:48:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.2 |
| 8ec58159-709e-3c54-ac8b-b9d5385a33d9 | -11.79455 | -47.31833 | 2026-06-03 00:48:00 | TERRA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 37.5 |
| 7270d46e-af48-3660-bbb2-461405db7a16 | -11.5674 | -54.58041 | 2026-06-03 00:48:00 | TERRA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 8a328b42-1fcf-3e45-9dbc-63764884d572 | -11.79203 | -47.32377 | 2026-06-03 00:48:00 | TERRA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 46.1 |
| c740d1fb-be90-38bb-823d-0d1f866f3360 | -11.75024 | -47.07713 | 2026-06-03 00:48:00 | TERRA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 58.5 |
| 5f3ff886-c687-3fe6-a899-bd1df7b3001a | -11.8029 | -47.3323 | 2026-06-03 00:50:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 61.1 |
| 7e37e58a-944f-391e-a3be-c323e4cbb7e6 | -17.444 | -42.6337 | 2026-06-03 00:50:00 | GOES-19 | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 124.3 |
| b8882f4d-b21d-3877-ae27-3313620c3d37 | -17.4447 | -42.6088 | 2026-06-03 00:50:00 | GOES-19 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 67.4 |
| 8b340e83-3236-372f-b860-dcf87ed83a39 | -16.5851 | -45.8715 | 2026-06-03 00:50:00 | GOES-19 | SANTA FÉ DE MINAS | MINAS GERAIS | Brasil | 3157609 | 31 | 33 | nan | nan | nan | Cerrado | 62.2 |
| 37a89b88-65b0-3b94-9fc4-564ae4c94463 | -7.50203 | -55.00396 | 2026-06-03 00:50:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| c61ee8c8-f380-3fda-bf52-4df74f5b6629 | -9.18093 | -58.05801 | 2026-06-03 00:50:00 | TERRA_M-M | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 43.8 |
| 579f8dba-6425-3d94-ae03-2da3e8a3c818 | -9.1797 | -58.04913 | 2026-06-03 00:50:00 | TERRA_M-M | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 7.6 |
| c381a1ad-3a94-38a7-a3ea-27b098e53d35 | -16.5851 | -45.8715 | 2026-06-03 01:00:00 | GOES-19 | SANTA FÉ DE MINAS | MINAS GERAIS | Brasil | 3157609 | 31 | 33 | nan | nan | nan | Cerrado | 63.6 |
| 59053366-491f-329f-91b4-da6b5062cfae | -17.444 | -42.6337 | 2026-06-03 01:00:00 | GOES-19 | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 103.2 |
| 9710a7e7-0b55-3c87-917f-4870587f122f | -17.4447 | -42.6088 | 2026-06-03 01:00:00 | GOES-19 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 66.9 |
| 4dd802dc-713e-378a-b8b8-6e630cc063b4 | -17.4447 | -42.6088 | 2026-06-03 01:10:00 | GOES-19 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 78.4 |
| 92048c16-d51d-3bbb-a264-c68929be9cfc | -16.5851 | -45.8715 | 2026-06-03 01:10:00 | GOES-19 | SANTA FÉ DE MINAS | MINAS GERAIS | Brasil | 3157609 | 31 | 33 | nan | nan | nan | Cerrado | 68.6 |
| c6091f74-2ae7-3a3e-a616-fd5ff5073b48 | -17.444 | -42.6337 | 2026-06-03 01:10:00 | GOES-19 | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 102.0 |
| c58579a6-76c0-3568-b7fd-78d81c5aac08 | -11.8029 | -47.3323 | 2026-06-03 01:10:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 41.6 |
| 99b9befc-2641-3a20-84c6-0e93fec4f9b5 | -17.444 | -42.6337 | 2026-06-03 01:20:00 | GOES-19 | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 94.9 |
| 6396fdd6-8f4f-3e4f-b23d-17eeb58ab63c | -17.4447 | -42.6088 | 2026-06-03 01:20:00 | GOES-19 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 55.4 |
| de5d4b9d-b60c-3bd5-a213-e5590978899a | -16.5851 | -45.8715 | 2026-06-03 01:20:00 | GOES-19 | SANTA FÉ DE MINAS | MINAS GERAIS | Brasil | 3157609 | 31 | 33 | nan | nan | nan | Cerrado | 57.6 |
| 424019b2-9829-34ac-9020-37e31a3216cb | -17.444 | -42.6337 | 2026-06-03 01:30:00 | GOES-19 | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 80.2 |
| ee41a722-a839-30c0-b6a6-80b4071c89b0 | -16.5851 | -45.8715 | 2026-06-03 01:30:00 | GOES-19 | SANTA FÉ DE MINAS | MINAS GERAIS | Brasil | 3157609 | 31 | 33 | nan | nan | nan | Cerrado | 46.4 |
| c6beb3dc-8712-30ab-a2ad-7eebf398c6e0 | -17.444 | -42.6337 | 2026-06-03 01:40:00 | GOES-19 | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 61.1 |
| 6155eb12-167e-3d1e-99b6-28dca1f848ea | -17.444 | -42.6337 | 2026-06-03 01:50:00 | GOES-19 | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 60.6 |
| d0a9102f-c7ea-38ca-8ff1-4441b5250e07 | -17.444 | -42.6337 | 2026-06-03 02:00:00 | GOES-19 | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 61.2 |
| a4b1a8a5-26a2-3d98-a304-a94144986f1a | -17.444 | -42.6337 | 2026-06-03 02:10:00 | GOES-19 | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 52.9 |
| 079867fd-87cd-39c5-a931-e6e06a7132ae | -17.444 | -42.6337 | 2026-06-03 02:20:00 | GOES-19 | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 55.7 |
| 13df6d99-7f40-39d2-9672-a4c0ecf20e02 | -16.5851 | -45.8715 | 2026-06-03 02:30:00 | GOES-19 | SANTA FÉ DE MINAS | MINAS GERAIS | Brasil | 3157609 | 31 | 33 | nan | nan | nan | Cerrado | 50.0 |
| 99c3a116-a779-302d-80d2-462206458abd | -17.444 | -42.6337 | 2026-06-03 02:30:00 | GOES-19 | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 59.4 |
| 5771c317-a114-32ca-9cee-1e0afbf811fb | -17.444 | -42.6337 | 2026-06-03 02:40:00 | GOES-19 | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 55.0 |
| b6c43f18-d1c5-3241-8d3c-daa80fee5e15 | -11.7962 | -42.63784 | 2026-06-03 03:21:00 | NPP-375D | IPUPIARA | BAHIA | Brasil | 2914109 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 8397f3f1-4d06-3424-9cb2-8526c0420001 | -19.72119 | -40.15975 | 2026-06-03 03:23:00 | NPP-375D | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| cf9eee84-8c1d-3122-b460-037bffd54547 | -19.05515 | -42.0081 | 2026-06-03 03:23:00 | NPP-375D | ENGENHEIRO CALDAS | MINAS GERAIS | Brasil | 3123700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 51ed0bce-e6b5-3478-b1ef-49c0271d55f6 | -18.45326 | -40.34993 | 2026-06-03 03:23:00 | NPP-375D | BOA ESPERANÇA | ESPÍRITO SANTO | Brasil | 3201001 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 57258baa-a11a-3c4c-923b-25caa03f9149 | -18.00364 | -39.79373 | 2026-06-03 03:23:00 | NPP-375D | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| bddf6341-7216-3f5e-bcbe-f2234a607b4b | -17.44558 | -42.63561 | 2026-06-03 03:23:00 | NPP-375D | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 6.7 |
| d68bea82-34ed-3906-9cd0-7a8f419f82a8 | -19.72192 | -40.15635 | 2026-06-03 03:23:00 | NPP-375D | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 68ed1a91-5acc-3ea8-9b4b-7f40b528a5ce | -17.44044 | -42.62869 | 2026-06-03 03:23:00 | NPP-375D | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 7.6 |
| a6060f69-f725-3de5-b14c-2492137803e3 | -17.99833 | -39.7925 | 2026-06-03 03:23:00 | NPP-375D | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| aef861bf-5674-32db-a12c-fcee8e0f12df | -17.43921 | -42.63414 | 2026-06-03 03:23:00 | NPP-375D | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 8a11dd07-1db6-3467-8531-cb26e6618509 | -19.05618 | -42.00353 | 2026-06-03 03:23:00 | NPP-375D | ENGENHEIRO CALDAS | MINAS GERAIS | Brasil | 3123700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 3f3953be-e372-37df-b85e-25ca8ccd2fc4 | -17.44679 | -42.63021 | 2026-06-03 03:23:00 | NPP-375D | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 1b169c46-19f0-38e6-ba30-a2d0318dd9d8 | -17.44168 | -42.62324 | 2026-06-03 03:23:00 | NPP-375D | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 7.6 |
| b312d75f-0514-38fa-a745-c62cdd29d5d7 | -5.511 | -35.59864 | 2026-06-03 03:38:00 | NOAA-20 | TAIPU | RIO GRANDE DO NORTE | Brasil | 2413904 | 24 | 33 | nan | nan | nan | Caatinga | 1.0 |
| de3b5a48-b5c8-300d-af61-7e601ccfaa30 | -5.51445 | -35.59922 | 2026-06-03 03:38:00 | NOAA-20 | TAIPU | RIO GRANDE DO NORTE | Brasil | 2413904 | 24 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 470d6a24-5825-3d35-9933-8a3ff834e5b6 | -5.72394 | -45.02846 | 2026-06-03 03:38:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 80edb721-cc2e-3cd2-9654-7cf9cedf2584 | -5.72306 | -45.03339 | 2026-06-03 03:38:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3f188a9b-2e91-3924-8411-cba12c3b96e2 | -5.72064 | -45.03466 | 2026-06-03 03:38:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f667c2d2-1845-37ae-981d-804821bc3ceb | -5.72219 | -45.03835 | 2026-06-03 03:38:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 44c86998-c962-3426-ba3f-d605a52ca038 | -5.51162 | -35.59485 | 2026-06-03 03:38:00 | NOAA-20 | TAIPU | RIO GRANDE DO NORTE | Brasil | 2413904 | 24 | 33 | nan | nan | nan | Caatinga | 0.6 |
| ea335fd9-8463-326d-8679-12fb9eb4b86f | -5.92706 | -43.47968 | 2026-06-03 03:38:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 145134f1-030d-3a21-9495-d7a0df535d00 | -5.50754 | -35.59808 | 2026-06-03 03:38:00 | NOAA-20 | TAIPU | RIO GRANDE DO NORTE | Brasil | 2413904 | 24 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 8dccf072-7177-3223-b6ba-c83c515bcf8b | -5.51037 | -35.60244 | 2026-06-03 03:38:00 | NOAA-20 | TAIPU | RIO GRANDE DO NORTE | Brasil | 2413904 | 24 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 8edbab0e-7b22-39d2-a176-766cb2889734 | -5.83973 | -43.49551 | 2026-06-03 03:38:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 155ffcbb-b702-302b-ab50-444624487ba3 | -5.92636 | -43.48355 | 2026-06-03 03:38:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| dd40a761-1f8e-3039-a654-c4f737ad922b | -5.72155 | -45.02968 | 2026-06-03 03:38:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2d609057-76a8-3c4a-8701-de5d41103ae5 | -5.72686 | -45.03577 | 2026-06-03 03:38:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7d97fde3-b90a-3788-acd0-03b56d968f46 | -5.84042 | -43.49163 | 2026-06-03 03:38:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a2f1c2a6-4427-36fe-bb87-d97660effb3e | -6.29921 | -43.64318 | 2026-06-03 03:40:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 02bd44c4-0d31-30f8-9f2d-f1b24434e516 | -11.7969 | -47.33519 | 2026-06-03 03:40:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 12.0 |
| deb647f6-8328-3b16-ba28-040fb9942ef0 | -6.98948 | -42.87704 | 2026-06-03 03:40:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.1 |
| dc9a1870-56de-3335-91db-aed2f8f58498 | -11.79489 | -42.63914 | 2026-06-03 03:40:00 | NOAA-20 | IPUPIARA | BAHIA | Brasil | 2914109 | 29 | 33 | nan | nan | nan | Caatinga | 5.8 |
| a9cc00e4-2ae0-3de2-a0c9-15f5103cee5a | -10.54185 | -46.62519 | 2026-06-03 03:40:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 11.2 |
| c8d12931-87b2-39de-a8da-a77d7262f5b8 | -8.56939 | -46.00164 | 2026-06-03 03:40:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 9f49524b-1413-3467-bc77-21ce5595d14f | -8.57032 | -45.99682 | 2026-06-03 03:40:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1e55a0e0-66cc-3756-9a9a-a27d3f86d5eb | -11.26404 | -48.3582 | 2026-06-03 03:40:00 | NOAA-20 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b6ebcd1c-f448-3f8f-b2f9-90c4808731c3 | -6.28682 | -43.63128 | 2026-06-03 03:40:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4dcf0c14-551b-398f-93fb-f5859229da20 | -10.53451 | -46.62903 | 2026-06-03 03:40:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| a5214d14-3be3-3f70-95e1-9f15b06d116e | -12.73384 | -46.96794 | 2026-06-03 03:40:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8a36ee7e-1b4f-358a-88a3-1d3d9b20bd06 | -11.79576 | -47.34077 | 2026-06-03 03:40:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 4df4de4d-f27b-3724-800b-e9e764ab8a1c | -6.76024 | -45.01505 | 2026-06-03 03:40:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 21e38653-3eae-33b9-8ae6-f561dc63902c | -8.57283 | -46.00371 | 2026-06-03 03:40:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 442d4ae3-23c2-39e2-8fb8-f738d6b85da6 | -10.54812 | -46.62679 | 2026-06-03 03:40:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 6df49550-894e-325c-bedc-c48b228baf88 | -10.97902 | -45.09565 | 2026-06-03 03:40:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 667ac0ec-17f0-37a9-ae30-d7772496bc82 | -8.57657 | -45.99828 | 2026-06-03 03:40:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 85738bbb-4d2e-3d51-8ceb-a7c5fd9f2766 | -12.37435 | -38.79351 | 2026-06-03 03:40:00 | NOAA-20 | AMÉLIA RODRIGUES | BAHIA | Brasil | 2901106 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 3f186c40-4ee6-387d-85fe-e1b29ec6ac51 | -11.13672 | -45.15095 | 2026-06-03 03:40:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d0039414-d3d1-3a9c-860e-d58178806553 | -10.55862 | -46.64024 | 2026-06-03 03:40:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 89eaa301-bda9-3f8a-b006-f11c1bc0f70c | -6.75494 | -45.00951 | 2026-06-03 03:40:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 05f4cecd-988d-375c-8bbf-a031114f642f | -8.97153 | -42.68272 | 2026-06-03 03:40:00 | NOAA-20 | SÃO RAIMUNDO NONATO | PIAUÍ | Brasil | 2210607 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| b8bfb575-b66c-3e00-84c0-df7c99823d1e | -6.3018 | -43.64547 | 2026-06-03 03:40:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f9b93b31-4d95-3021-a748-ea04e93e6cc6 | -8.57563 | -46.00314 | 2026-06-03 03:40:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 7a9859f6-42e5-331b-aba0-2582b8020a96 | -11.94809 | -43.40474 | 2026-06-03 03:40:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 99d2ed49-6a96-308a-b6b4-351c58f6774d | -7.94987 | -46.83744 | 2026-06-03 03:40:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 772bb05a-285d-3e83-9704-6c8bc3ec6b3f | -11.75569 | -47.07543 | 2026-06-03 03:40:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f2564cc6-fda5-392f-b679-64b49990427a | -6.98565 | -42.87808 | 2026-06-03 03:40:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 1e9b8b3b-749a-3bdc-ad45-5b56f00e5cfc | -10.55334 | -46.63366 | 2026-06-03 03:40:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 44201eaa-4090-3b6e-a4dd-4f1a5df03998 | -6.30247 | -43.64162 | 2026-06-03 03:40:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2e27cb19-6c0e-3ffe-aa5c-3fc0ec88b702 | -11.99617 | -43.7829 | 2026-06-03 03:40:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3e2e104d-a5de-3495-bca0-6790cae83da1 | -6.76106 | -45.01056 | 2026-06-03 03:40:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 96f3291e-b787-338b-a6a8-b9fb4936be69 | -10.97822 | -45.09979 | 2026-06-03 03:40:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7292d167-d786-38e1-8113-5080fac1461d | -10.54075 | -46.63076 | 2026-06-03 03:40:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| adfd38ed-ffce-3bea-96b4-dc68b3674fdf | -11.13259 | -45.14166 | 2026-06-03 03:40:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a83505e0-e8c5-34a5-9d21-2565baee7989 | -12.73286 | -46.97272 | 2026-06-03 03:40:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d9e75615-d572-36cd-b379-e6b3897011b2 | -7.594 | -46.46554 | 2026-06-03 03:40:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 03b89a79-ce3e-3878-8459-5fab069f00f2 | -10.98023 | -45.09568 | 2026-06-03 03:40:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 59926e29-039e-3808-b69b-1bd128bf6d9a | -11.99043 | -45.14652 | 2026-06-03 03:40:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8c68b676-0607-3d37-b7cb-5fd8270a6769 | -11.80333 | -47.33666 | 2026-06-03 03:40:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |


[Clique aqui para ver as próximas entradas](README3.md)
