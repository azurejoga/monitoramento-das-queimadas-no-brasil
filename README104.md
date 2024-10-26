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

## Dados Diários - Página 104

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 33271e51-1b71-3bb8-af96-003b7bceaf14 | -11.82351 | -42.65988 | 2024-10-26 11:53:00 | TERRA_M-M | IPUPIARA | BAHIA | Brasil | 2914109 | 29 | 33 | nan | nan | nan | Caatinga | 26.4 |
| d728709d-1f6b-36b3-ad7e-846f4cea75d3 | -10.61437 | -44.25987 | 2024-10-26 11:53:00 | TERRA_M-M | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 138.5 |
| a20ea3ab-163f-3b2e-970c-b7b81e4b2ec0 | -10.6091 | -44.29013 | 2024-10-26 11:53:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 114.0 |
| 3941bafc-c2b4-34f0-a774-3dcfc84e5bdf | -10.60283 | -44.25252 | 2024-10-26 11:53:00 | TERRA_M-M | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 105.7 |
| 5442f3a3-b556-34de-8fd3-15d43b2be168 | -10.5989 | -44.25775 | 2024-10-26 11:53:00 | TERRA_M-M | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 38.1 |
| f9151599-9e86-39cc-9a26-988b96ebe1a0 | -10.59783 | -44.28231 | 2024-10-26 11:53:00 | TERRA_M-M | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 189.1 |
| 24c9ad8b-d2e4-377a-a498-403325b1e02c | -10.59373 | -44.28726 | 2024-10-26 11:53:00 | TERRA_M-M | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 45.6 |
| d1fcce11-15a6-315e-8408-027a21e79b3e | -10.48724 | -42.47526 | 2024-10-26 11:53:00 | TERRA_M-M | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 41.9 |
| 42756d64-6d2f-37dd-92d0-eeda3d7246d1 | -7.3057 | -44.96803 | 2024-10-26 11:53:00 | TERRA_M-M | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 77.8 |
| 05dd46f6-cab1-35fc-b9f2-17600ee7a364 | -15.353 | -41.40244 | 2024-10-26 11:55:00 | TERRA_M-M | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 11.5 |
| c76925e0-9f50-3db6-b76b-41e251bebb78 | -15.33894 | -42.03558 | 2024-10-26 11:55:00 | TERRA_M-M | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 17.5 |
| 3ed41153-7355-3ee1-867d-7466a5d930ed | -15.33603 | -42.05276 | 2024-10-26 11:55:00 | TERRA_M-M | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 17.6 |
| 107d22fb-3c29-3fe5-b899-0fe8cfad7275 | -15.12585 | -40.9648 | 2024-10-26 11:55:00 | TERRA_M-M | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 13.7 |
| 2f0e51e1-c849-377e-8118-87db4f1159c3 | -14.84415 | -41.20045 | 2024-10-26 11:55:00 | TERRA_M-M | BELO CAMPO | BAHIA | Brasil | 2903508 | 29 | 33 | nan | nan | nan | Caatinga | 16.1 |
| 7297b249-ed72-3f23-b3fe-4d5bd49df0cd | -14.66893 | -42.64347 | 2024-10-26 11:55:00 | TERRA_M-M | URANDI | BAHIA | Brasil | 2932606 | 29 | 33 | nan | nan | nan | Cerrado | 24.0 |
| d1462f2f-09d2-38c5-af83-1696ab35ca67 | -14.58646 | -42.19384 | 2024-10-26 11:55:00 | TERRA_M-M | CACULÉ | BAHIA | Brasil | 2905008 | 29 | 33 | nan | nan | nan | Caatinga | 23.4 |
| 7ccaeb10-60c1-35c0-8657-99a6a43ce41c | -14.30637 | -42.91024 | 2024-10-26 11:55:00 | TERRA_M-M | GUANAMBI | BAHIA | Brasil | 2911709 | 29 | 33 | nan | nan | nan | Caatinga | 21.5 |
| 46827581-0474-3ee7-8732-70167cfa9e2f | -14.19146 | -43.71219 | 2024-10-26 11:55:00 | TERRA_M-M | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 21.8 |
| 42e35e58-c072-319c-bbdc-8f574430f58d | -14.07669 | -42.71608 | 2024-10-26 11:55:00 | TERRA_M-M | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 58.7 |
| 4a3d4877-631c-30f9-8c01-fe98dcd17670 | -14.07538 | -42.72337 | 2024-10-26 11:55:00 | TERRA_M-M | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 83.1 |
| 2d7409cb-7d67-313b-b71b-23371c19218c | -14.07314 | -42.73736 | 2024-10-26 11:55:00 | TERRA_M-M | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 27.9 |
| c7129f96-352e-3a45-aa47-689b087d0187 | -13.75426 | -43.05515 | 2024-10-26 11:55:00 | TERRA_M-M | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 44.7 |
| 7e3e5e48-9f1d-3cf9-8d12-e23258a6fb0e | -13.75046 | -43.07688 | 2024-10-26 11:55:00 | TERRA_M-M | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 100.8 |
| 44d9f9e8-2a76-3a68-b8c3-94bd45a1108b | -13.74105 | -43.06926 | 2024-10-26 11:55:00 | TERRA_M-M | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 27.6 |
| 1f5edea6-fde9-35c7-9ab7-8ea151fb91a0 | -13.69605 | -42.47728 | 2024-10-26 11:55:00 | TERRA_M-M | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 22.5 |
| 7b4cc4aa-3cde-362f-8d11-664008220062 | -13.69272 | -42.49685 | 2024-10-26 11:55:00 | TERRA_M-M | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 69.1 |
| 01ed8f7e-b06b-354a-9fcd-60f2b6b3b577 | -13.2996 | -40.34895 | 2024-10-26 11:55:00 | TERRA_M-M | PLANALTINO | BAHIA | Brasil | 2924900 | 29 | 33 | nan | nan | nan | Caatinga | 11.7 |
| 218dd5ef-4e2d-31ad-9b37-2393b30f876c | -13.27724 | -41.82818 | 2024-10-26 11:55:00 | TERRA_M-M | ABAÍRA | BAHIA | Brasil | 2900108 | 29 | 33 | nan | nan | nan | Caatinga | 29.7 |
| 64b75da0-7f1b-3883-bf43-23a66db50a72 | -13.19979 | -42.98444 | 2024-10-26 11:55:00 | TERRA_M-M | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 27.1 |
| 975a4740-df4f-3ef4-a5c0-6dfbbf271ec9 | -12.97596 | -42.22308 | 2024-10-26 11:55:00 | TERRA_M-M | IBIPITANGA | BAHIA | Brasil | 2912509 | 29 | 33 | nan | nan | nan | Caatinga | 55.8 |
| d8ff9cdb-f1bb-3661-bc5e-851ccb230f0c | -12.97265 | -42.24249 | 2024-10-26 11:55:00 | TERRA_M-M | IBIPITANGA | BAHIA | Brasil | 2912509 | 29 | 33 | nan | nan | nan | Caatinga | 114.3 |
| ee444ddb-8343-3d03-851d-ff664759d7c1 | -12.96345 | -42.2207 | 2024-10-26 11:55:00 | TERRA_M-M | IBIPITANGA | BAHIA | Brasil | 2912509 | 29 | 33 | nan | nan | nan | Caatinga | 167.5 |
| 5cb32908-5b61-31c0-a8bd-dd3d350ba19c | -12.92823 | -42.27467 | 2024-10-26 11:55:00 | TERRA_M-M | IBIPITANGA | BAHIA | Brasil | 2912509 | 29 | 33 | nan | nan | nan | Caatinga | 116.2 |
| a36b692b-337d-3ecc-a5e7-38ff5a2a8b91 | -12.92772 | -42.26847 | 2024-10-26 11:55:00 | TERRA_M-M | IBIPITANGA | BAHIA | Brasil | 2912509 | 29 | 33 | nan | nan | nan | Caatinga | 68.2 |
| fea47f5d-c9b7-352d-b655-3ae166f50615 | -12.92484 | -42.29415 | 2024-10-26 11:55:00 | TERRA_M-M | IBIPITANGA | BAHIA | Brasil | 2912509 | 29 | 33 | nan | nan | nan | Caatinga | 117.0 |
| 98398a3d-fa61-3303-8ffa-0893e50ff4c7 | -12.92447 | -42.28799 | 2024-10-26 11:55:00 | TERRA_M-M | IBIPITANGA | BAHIA | Brasil | 2912509 | 29 | 33 | nan | nan | nan | Caatinga | 195.2 |
| c7a688a8-6b9d-33a1-aade-c4e53106663f | -12.88151 | -42.23512 | 2024-10-26 11:55:00 | TERRA_M-M | IBIPITANGA | BAHIA | Brasil | 2912509 | 29 | 33 | nan | nan | nan | Caatinga | 32.8 |
| cc0f9186-295e-3540-90d8-d44145fc6e51 | -12.75988 | -42.32725 | 2024-10-26 11:55:00 | TERRA_M-M | IBIPITANGA | BAHIA | Brasil | 2912509 | 29 | 33 | nan | nan | nan | Caatinga | 32.5 |
| 75ff8f15-cb09-3cf3-84b8-82129c3f75ba | -12.75959 | -42.33342 | 2024-10-26 11:55:00 | TERRA_M-M | IBIPITANGA | BAHIA | Brasil | 2912509 | 29 | 33 | nan | nan | nan | Caatinga | 24.6 |
| c8161dce-5fe6-3363-a883-f4bd2c6ee61c | -12.6997 | -42.29653 | 2024-10-26 11:55:00 | TERRA_M-M | IBITIARA | BAHIA | Brasil | 2913002 | 29 | 33 | nan | nan | nan | Caatinga | 53.2 |
| e9a3ec55-04ae-3603-a061-b51db9b75c95 | -12.5514 | -42.47129 | 2024-10-26 11:55:00 | TERRA_M-M | IBITIARA | BAHIA | Brasil | 2913002 | 29 | 33 | nan | nan | nan | Caatinga | 29.4 |
| ca460359-68f1-39a8-bbc5-6e86c1cd3bf6 | -12.40917 | -42.91952 | 2024-10-26 11:55:00 | TERRA_M-M | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 72.8 |
| ae52fa8f-abef-3a01-bc59-e1632b95ebcd | -12.10246 | -45.68988 | 2024-10-26 11:55:00 | TERRA_M-M | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 38.8 |
| 967bc4a8-0813-3bc8-8d25-2bcc765fee81 | -12.09576 | -45.72661 | 2024-10-26 11:55:00 | TERRA_M-M | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 46.6 |
| 7a68fc57-64ed-3ff8-a2e9-89849101cfee | -12.07975 | -42.77132 | 2024-10-26 11:55:00 | TERRA_M-M | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 26.5 |
| 13ca4b31-baf0-3ff5-a9f7-32db22b7094d | -12.06653 | -42.76839 | 2024-10-26 11:55:00 | TERRA_M-M | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 20.4 |
| ed0a3cf4-e139-37be-9374-54d718f9de57 | -12.06511 | -42.6967 | 2024-10-26 11:55:00 | TERRA_M-M | BROTAS DE MACAÚBAS | BAHIA | Brasil | 2904506 | 29 | 33 | nan | nan | nan | Caatinga | 69.6 |
| ba1577d7-bf91-3a27-aaed-1397a98014fd | -19.18394 | -40.32449 | 2024-10-26 11:57:00 | TERRA_M-M | RIO BANANAL | ESPÍRITO SANTO | Brasil | 3204351 | 32 | 33 | nan | nan | nan | Mata Atlântica | 13.9 |
| 07e0e172-9f0d-3d62-9a55-c98fac3e0b24 | -18.19939 | -40.68983 | 2024-10-26 11:57:00 | TERRA_M-M | ECOPORANGA | ESPÍRITO SANTO | Brasil | 3202108 | 32 | 33 | nan | nan | nan | Mata Atlântica | 12.7 |
| c7ddb8b8-d859-3862-8a63-c579db531766 | -16.8851 | -41.83438 | 2024-10-26 11:57:00 | TERRA_M-M | ARAÇUAÍ | MINAS GERAIS | Brasil | 3103405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 27.1 |
| 5b469747-5ff2-3561-b4f2-86e902310948 | -16.88346 | -41.84056 | 2024-10-26 11:57:00 | TERRA_M-M | ARAÇUAÍ | MINAS GERAIS | Brasil | 3103405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 31.3 |
| 80559d4b-e8fe-3f7e-9788-9db38d99bfa5 | -16.88238 | -41.85079 | 2024-10-26 11:57:00 | TERRA_M-M | ARAÇUAÍ | MINAS GERAIS | Brasil | 3103405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 16.1 |
| b23083ec-eb97-3029-91bf-12130b712cff | -15.96254 | -43.75919 | 2024-10-26 11:57:00 | TERRA_M-M | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 32.9 |
| 0fddb650-278c-3825-96ce-22132d5f7adf | -13.7745 | -42.9639 | 2024-10-26 12:26:22 | GOES-16 | MATINA | BAHIA | Brasil | 2921054 | 29 | 33 | nan | nan | nan | Caatinga | 74.2 |
| d6dd1c3b-5b29-38a6-8318-75703e16a961 | -12.9161 | -42.301 | 2024-10-26 12:46:17 | GOES-16 | IBIPITANGA | BAHIA | Brasil | 2912509 | 29 | 33 | nan | nan | nan | Caatinga | 123.4 |
| d2c152f4-46ca-3d9e-baaf-e7b0de3c4ed2 | -12.9366 | -42.2488 | 2024-10-26 12:46:18 | GOES-16 | IBIPITANGA | BAHIA | Brasil | 2912509 | 29 | 33 | nan | nan | nan | Caatinga | 82.7 |
| 5029761b-17b7-33c4-877e-ab78b25bec1f | -14.0529 | -42.6931 | 2024-10-26 12:46:24 | GOES-16 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 74.3 |
| 9b054223-5c3d-39d5-a28d-c54e66761313 | 3.6185 | -51.2955 | 2024-10-26 12:54:45 | GOES-16 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 75.9 |
| 71e88a05-3820-3b95-9a91-97325b0a0920 | -3.4729 | -43.3377 | 2024-10-26 12:55:25 | GOES-16 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 243.9 |
| 96445ae4-9e70-3592-8148-11b22cd4f958 | -3.4915 | -43.3368 | 2024-10-26 12:55:25 | GOES-16 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 154.0 |
| 9ac2d7c3-fbd1-3479-88f6-15f3251669db | -3.473 | -43.3144 | 2024-10-26 12:55:25 | GOES-16 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 231.0 |
| 1c5acfd5-3b7b-398b-9da0-57fbe50aa2cc | -3.4917 | -43.3136 | 2024-10-26 12:55:25 | GOES-16 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 148.5 |
| a06fa4b8-649b-30d2-b2b5-a6aeb5178ed6 | -12.9161 | -42.301 | 2024-10-26 12:56:17 | GOES-16 | IBIPITANGA | BAHIA | Brasil | 2912509 | 29 | 33 | nan | nan | nan | Caatinga | 100.0 |
| 5736aaab-609e-3331-9f91-a2cb11c3ad5c | -14.0529 | -42.6931 | 2024-10-26 12:56:24 | GOES-16 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 100.8 |
| 4dec94ab-ea7a-3522-bf56-1c442e977b09 | 3.6185 | -51.2955 | 2024-10-26 13:04:45 | GOES-16 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 68.6 |
| e825f039-2c9b-39d4-b1cc-6a825a2a8cc7 | -3.4729 | -43.3377 | 2024-10-26 13:05:25 | GOES-16 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 232.8 |
| 76a05b3f-f4f4-3f6a-80a7-d29c484a9468 | -3.4917 | -43.3136 | 2024-10-26 13:05:25 | GOES-16 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 208.5 |
| 644951f6-5184-3c04-8df0-2d4bdfb0c59e | -3.473 | -43.3144 | 2024-10-26 13:05:25 | GOES-16 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 302.0 |
| 13fe203a-7b03-35a0-9dd8-546c56346ef6 | -12.6444 | -42.3498 | 2024-10-26 13:06:16 | GOES-16 | IBITIARA | BAHIA | Brasil | 2913002 | 29 | 33 | nan | nan | nan | Caatinga | 91.2 |
| 2edb00d1-1adf-3f2f-8189-293fce8d514a | -12.9161 | -42.301 | 2024-10-26 13:06:17 | GOES-16 | IBIPITANGA | BAHIA | Brasil | 2912509 | 29 | 33 | nan | nan | nan | Caatinga | 81.6 |
| d0035cab-fa71-306f-a33c-c69f3fb88ee1 | -13.0364 | -43.0272 | 2024-10-26 13:06:18 | GOES-16 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 69.9 |
| a8d4d443-e76c-3c2a-95c5-2ef15ecac3b1 | -14.0477 | -43.7983 | 2024-10-26 13:06:24 | GOES-16 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 70.5 |
| f7ac5bd0-be64-37ad-b78b-ab686285703a | -14.0529 | -42.6931 | 2024-10-26 13:06:24 | GOES-16 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 134.0 |
| 3ab8d39d-7fbe-3768-a0d9-68fb67e1a847 | -14.8574 | -43.3546 | 2024-10-26 13:06:28 | GOES-16 | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | 82.8 |
| 3a16ea8e-e4d1-3658-8840-34cfad7be20d | -14.7804 | -42.4739 | 2024-10-26 13:06:28 | GOES-16 | JACARACI | BAHIA | Brasil | 2917409 | 29 | 33 | nan | nan | nan | Caatinga | 87.1 |
| 277fb351-e759-35e3-80f5-5d6413933f52 | 3.6185 | -51.2955 | 2024-10-26 13:14:45 | GOES-16 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 79.3 |
| c4adb18f-90d6-3575-a78a-58947696cf27 | -3.473 | -43.3144 | 2024-10-26 13:15:25 | GOES-16 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 319.9 |
| 261cb8d9-689d-3252-a370-9ffb25a8466b | -3.4917 | -43.3136 | 2024-10-26 13:15:25 | GOES-16 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 208.7 |
| c4b1b8ff-4cce-35fb-a6d4-2a4b18a9dc61 | -3.4729 | -43.3377 | 2024-10-26 13:15:25 | GOES-16 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 315.9 |
| 67cc77aa-a006-3aa0-a2b7-22de80a249ab | -12.6444 | -42.3498 | 2024-10-26 13:16:16 | GOES-16 | IBITIARA | BAHIA | Brasil | 2913002 | 29 | 33 | nan | nan | nan | Caatinga | 85.7 |
| d9b87ca3-97ed-3f52-affb-cf1e5d6d9466 | -12.9161 | -42.301 | 2024-10-26 13:16:17 | GOES-16 | IBIPITANGA | BAHIA | Brasil | 2912509 | 29 | 33 | nan | nan | nan | Caatinga | 80.5 |
| d32d191b-98c4-31d6-b454-5976a5a33abd | -13.0558 | -43.0237 | 2024-10-26 13:16:18 | GOES-16 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 88.4 |
| 83301bd4-7895-38ae-907c-662a749c1deb | -13.0364 | -43.0272 | 2024-10-26 13:16:18 | GOES-16 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 75.7 |
| bd2e6105-1538-36d2-8ceb-406154abf187 | -14.0529 | -42.6931 | 2024-10-26 13:16:24 | GOES-16 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 105.6 |
| ff6242f8-b364-33ee-8ecf-af2d3241850d | -14.7804 | -42.4739 | 2024-10-26 13:16:28 | GOES-16 | JACARACI | BAHIA | Brasil | 2917409 | 29 | 33 | nan | nan | nan | Caatinga | 184.0 |
| 1bbcd2de-5baa-30ef-a55f-9ca4b17a23e5 | -15.9519 | -43.5609 | 2024-10-26 13:16:34 | GOES-16 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 100.2 |
| 949802f3-78d4-38e3-a970-0f7677727224 | 3.6185 | -51.2955 | 2024-10-26 13:24:45 | GOES-16 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 70.4 |
| 7e9929a2-a78d-3216-ab68-4df1b65f98c8 | -2.2114 | -53.6828 | 2024-10-26 13:25:18 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 62.3 |
| 25901947-0085-318f-b564-4fe0f8ba44fe | -2.135 | -54.9259 | 2024-10-26 13:25:18 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 69.7 |
| 639c1d0c-ffa5-3bc5-9ce4-01538045112c | -3.4917 | -43.3136 | 2024-10-26 13:25:25 | GOES-16 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 284.1 |
| b120f07f-7abb-3829-885a-572ae11f82e2 | -3.4729 | -43.3377 | 2024-10-26 13:25:25 | GOES-16 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 289.4 |
| 99652564-bf92-3d05-9f6e-47ff3aac91e0 | -3.473 | -43.3144 | 2024-10-26 13:25:25 | GOES-16 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 317.3 |
| 8fdde5a3-4cd2-37c4-9b74-da22ba5d1d4b | -13.9042 | -41.5239 | 2024-10-26 13:26:23 | GOES-16 | RIO DE CONTAS | BAHIA | Brasil | 2926707 | 29 | 33 | nan | nan | nan | Caatinga | 75.8 |
| 4ac07aa6-d9ed-3ec1-ab7a-37e88c9d7b77 | -14.7059 | -43.1441 | 2024-10-26 13:26:27 | GOES-16 | ESPINOSA | MINAS GERAIS | Brasil | 3124302 | 31 | 33 | nan | nan | nan | Caatinga | 82.9 |
| 0e517e89-a725-3e0d-9b26-a83890065be5 | -14.7804 | -42.4739 | 2024-10-26 13:26:28 | GOES-16 | JACARACI | BAHIA | Brasil | 2917409 | 29 | 33 | nan | nan | nan | Caatinga | 102.1 |
| f11c8b66-63ff-3e46-b181-02b4320fd9db | -15.9519 | -43.5609 | 2024-10-26 13:26:34 | GOES-16 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 89.6 |
| 833cbd91-a9a0-3bf7-928a-3c433d3afeb5 | -2.2114 | -53.6828 | 2024-10-26 13:35:18 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 65.9 |
| 0f538045-45a1-359d-8807-7daf996b57ed | -2.135 | -54.9259 | 2024-10-26 13:35:18 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 86.0 |
| 3ac59210-7bc5-3b2d-9631-3c0fb12a19f4 | -3.4917 | -43.3136 | 2024-10-26 13:35:25 | GOES-16 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 217.9 |
| b3a10597-e902-3902-bea6-93f1f8f00191 | -3.473 | -43.3144 | 2024-10-26 13:35:25 | GOES-16 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 374.0 |


[Clique aqui para ver as próximas entradas](README105.md)
