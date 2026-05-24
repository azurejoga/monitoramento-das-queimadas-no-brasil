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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7762c7ba-b725-3198-a203-8bcb9655b0ad | -12.8861 | -58.1692 | 2026-05-24 00:00:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 102.4 |
| 7fd06841-6c69-3049-8f40-1090fb0db670 | -12.9052 | -58.1676 | 2026-05-24 00:00:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 80.2 |
| 37224ff1-5603-3147-a9cd-8b64b310f93d | -12.8859 | -58.1891 | 2026-05-24 00:00:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 59.9 |
| 384b7961-d7e2-38f8-a65d-86b02f2b2886 | -12.9049 | -58.1875 | 2026-05-24 00:00:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 48.6 |
| e108c963-6ed9-33fa-a61e-8f730c730ee8 | -12.8861 | -58.1692 | 2026-05-24 00:10:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 85.6 |
| 7b1f23f3-84e2-3626-be43-678557d6b29b | -12.9049 | -58.1875 | 2026-05-24 00:10:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 54.3 |
| 91de5485-80fe-3f15-b2e6-d602c708aea8 | -12.9052 | -58.1676 | 2026-05-24 00:10:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 72.7 |
| 2d8459d9-67fa-3c87-b830-2c98f2f0d0b5 | -12.8859 | -58.1891 | 2026-05-24 00:10:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 56.3 |
| a33af312-127d-3be9-8db7-ee21274f9228 | -12.8859 | -58.1891 | 2026-05-24 00:20:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 52.4 |
| f613b886-7161-35e2-8fb9-cbc6e94bce57 | -12.9049 | -58.1875 | 2026-05-24 00:20:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 46.7 |
| 5f7f30d3-17ff-38e8-9129-961cfe0a995b | -12.9052 | -58.1676 | 2026-05-24 00:20:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 67.8 |
| 4a41dd10-e7e9-3dbf-adb1-e80d92e621ff | -18.657 | -48.8785 | 2026-05-24 00:20:00 | GOES-19 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 59.2 |
| 9cf078b2-1f70-35dc-901d-12867bfbe936 | -12.8861 | -58.1692 | 2026-05-24 00:20:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 82.6 |
| 8551b9c9-41b7-3f8b-a8d9-912e24ab6262 | -12.8861 | -58.1692 | 2026-05-24 00:30:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 91.4 |
| db39eb5e-b466-39cc-9afe-ff9e0ad99339 | -12.8859 | -58.1891 | 2026-05-24 00:30:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 49.4 |
| 71ab649b-59b9-3840-9936-edc43980c35a | -12.9049 | -58.1875 | 2026-05-24 00:30:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 43.6 |
| 9f205a86-f439-307c-a164-7840dd891799 | -12.9052 | -58.1676 | 2026-05-24 00:30:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 78.3 |
| a2a61c34-9e21-3025-9175-284fe7007a6f | -12.9049 | -58.1875 | 2026-05-24 00:40:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 43.2 |
| 2107527e-6213-3e9c-b26a-b44665990e24 | -12.8861 | -58.1692 | 2026-05-24 00:40:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 90.3 |
| 716d558e-3b23-3c52-8d0d-1588cb7ef2d4 | -12.8859 | -58.1891 | 2026-05-24 00:40:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 58.2 |
| d9e75456-18b1-30ea-8f9b-9bcd3baef06e | -12.9052 | -58.1676 | 2026-05-24 00:40:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 65.5 |
| 8f187a3e-3f24-3b1c-8635-8f99d80d896c | -18.65558 | -48.8762 | 2026-05-24 00:48:00 | TERRA_M-M | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 43.2 |
| 5666d50c-39af-333e-8f0e-59f3743ceba9 | -18.64211 | -48.87914 | 2026-05-24 00:48:00 | TERRA_M-M | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 31.6 |
| 82fe1da2-f238-3a5b-96a3-dfed77c0a792 | -18.23847 | -54.592 | 2026-05-24 00:48:00 | TERRA_M-M | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 7535d6c4-c45c-3aa6-bfbf-84293b07f119 | -18.64898 | -48.87204 | 2026-05-24 00:48:00 | TERRA_M-M | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 68.7 |
| 2c94610f-6dea-3cfc-94cb-e58266d4d1cd | -18.65331 | -48.89547 | 2026-05-24 00:48:00 | TERRA_M-M | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 27.6 |
| d7a96c2f-5283-30a2-9726-b6b8652f8ab6 | -12.8861 | -58.1692 | 2026-05-24 00:50:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 86.9 |
| 36b0542e-35b3-3864-b9a7-22a0dce78fe6 | -12.8859 | -58.1891 | 2026-05-24 00:50:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 53.3 |
| fbaa4ab9-8291-32c3-b671-acd00d9db4a8 | -12.9052 | -58.1676 | 2026-05-24 00:50:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 63.1 |
| 58a31fdf-d830-3e40-9659-d6f775a09d20 | -11.27502 | -53.96805 | 2026-05-24 00:50:00 | TERRA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 57467ace-ae40-31b0-91b8-464d1510e27f | -11.913 | -57.03769 | 2026-05-24 00:50:00 | TERRA_M-M | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| b899c244-4180-371e-a05a-7fc22c30e1d7 | -14.01892 | -53.35447 | 2026-05-24 00:50:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 31.0 |
| 1021125c-542a-3fc2-b104-a0a2ab80eb67 | -12.89154 | -58.18081 | 2026-05-24 00:50:00 | TERRA_M-M | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 69.1 |
| c09adbd7-e4b0-3029-8c59-48212b79ba12 | -12.90038 | -58.17954 | 2026-05-24 00:50:00 | TERRA_M-M | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 25.2 |
| d118fd00-fa9e-3a07-aaf5-9642417d35e2 | -11.5502 | -56.94166 | 2026-05-24 00:50:00 | TERRA_M-M | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 0306bc1c-389a-3e59-8f99-b58b740baab4 | -12.88394 | -58.19113 | 2026-05-24 00:50:00 | TERRA_M-M | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 959fe90d-7d16-348e-966b-1af55d7f9e95 | -15.08379 | -57.63474 | 2026-05-24 00:50:00 | TERRA_M-M | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 16.1 |
| c9a7bc36-afd7-3f18-89d1-4bb3286d4678 | -15.10146 | -57.63213 | 2026-05-24 00:50:00 | TERRA_M-M | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| ba581594-aa01-3258-a401-e5ca4a459251 | -11.54128 | -56.943 | 2026-05-24 00:50:00 | TERRA_M-M | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| a6029d76-69bf-3988-9224-4e46216c07d8 | -11.54259 | -56.95218 | 2026-05-24 00:50:00 | TERRA_M-M | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 34.9 |
| d4c84d10-6014-31b1-ae8c-3a830b24d59b | -12.54962 | -57.16899 | 2026-05-24 00:50:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 23.4 |
| ee4bca4b-688c-3e12-b324-b5c97789f537 | -12.561 | -54.75818 | 2026-05-24 00:50:00 | TERRA_M-M | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 481d1ffa-44d9-33a1-8e4e-c61c780cb0f6 | -14.02096 | -53.36767 | 2026-05-24 00:50:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 23.7 |
| 1ac276ed-e658-3a5a-bf6e-16a688f2f1e0 | -15.10022 | -57.62302 | 2026-05-24 00:50:00 | TERRA_M-M | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 0b395553-aaaf-3bde-99e6-4b71e34a9e11 | -11.5439 | -56.96136 | 2026-05-24 00:50:00 | TERRA_M-M | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 26.6 |
| 873e31e3-e0c6-34da-9063-5d51290f9559 | -12.89031 | -58.17176 | 2026-05-24 00:50:00 | TERRA_M-M | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 144.6 |
| 6619675d-f01b-30a1-8314-527747157821 | -14.7787 | -52.66972 | 2026-05-24 00:50:00 | TERRA_M-M | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 63baaddc-9b91-388a-8d14-b70ff406172c | -12.89401 | -58.1989 | 2026-05-24 00:50:00 | TERRA_M-M | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 8519d23b-4ff2-3baf-86b2-861c4a04da43 | -12.88907 | -58.16272 | 2026-05-24 00:50:00 | TERRA_M-M | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| bdeff77d-8f57-38ee-995d-39640c6570ff | -11.95181 | -57.0443 | 2026-05-24 00:50:00 | TERRA_M-M | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| e5015615-ddb1-3c64-b83e-2a892fa1e940 | -15.09263 | -57.63343 | 2026-05-24 00:50:00 | TERRA_M-M | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 19.6 |
| 168a62ea-4b50-3552-aca1-68234928b6ce | -11.5515 | -56.95083 | 2026-05-24 00:50:00 | TERRA_M-M | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| d53c0651-80b8-31b3-9d28-741352244540 | -12.54205 | -57.17937 | 2026-05-24 00:50:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| be815099-277d-36b2-a0d6-05a00b82f928 | -10.72664 | -51.59269 | 2026-05-24 00:50:00 | TERRA_M-M | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 18.0 |
| c469ec32-a420-38ee-aead-312b406ad6d6 | -11.04965 | -49.60332 | 2026-05-24 00:50:00 | TERRA_M-M | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 30.3 |
| 7ff3edfa-96a3-3d39-b307-4c0dc9c3c3f6 | -12.55089 | -57.17804 | 2026-05-24 00:50:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 7ef2ac4f-a430-3fed-a725-1ca59317e1b1 | -15.08503 | -57.64386 | 2026-05-24 00:50:00 | TERRA_M-M | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 60379b1e-9e07-35a1-bdd1-78ce65e23f69 | -14.77692 | -52.67652 | 2026-05-24 00:50:00 | TERRA_M-M | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 13.0 |
| c2f5b122-2283-35de-87ff-d7adfa807c34 | -12.53901 | -54.61111 | 2026-05-24 00:50:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 9.6 |
| d93bc567-e72d-392c-b4d2-44af41127f06 | -15.0926 | -57.627701 | 2026-05-24 00:55:00 | METOP-B | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7e6cc6a7-5724-3146-a61f-dcb0755576ad | -18.6483 | -48.8592 | 2026-05-24 00:55:00 | METOP-B | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 532bb99c-1162-3811-a093-c0d2011f59ea | -11.1838 | -55.905899 | 2026-05-24 00:55:00 | METOP-B | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 40d5f77c-1ecc-3edd-ac8d-122a684e120c | -14.0202 | -53.350101 | 2026-05-24 00:55:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 60e5a19f-43af-39c6-a4e5-a25f5e0cf80f | -14.0105 | -53.3526 | 2026-05-24 00:55:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| a1cbc4bb-ed88-302b-bc1e-bebe373e4ac0 | -11.9108 | -57.026402 | 2026-05-24 00:55:00 | METOP-B | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b51da757-6b2a-3ed7-9ddb-7c8178740aef | -11.5504 | -56.941502 | 2026-05-24 00:55:00 | METOP-B | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4fb598ee-d686-359f-ba53-a0a9c9c80587 | -12.5494 | -57.154202 | 2026-05-24 00:55:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 20759697-76d4-35d8-8874-c75206b3e0f1 | -12.5529 | -57.169201 | 2026-05-24 00:55:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4b56b6ad-3a93-35dd-bb94-2adc3ac1dd30 | -12.8917 | -58.154999 | 2026-05-24 00:55:00 | METOP-B | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| e4312fe9-3f2a-3d37-8bfa-97e2c911403d | -15.0909 | -57.620499 | 2026-05-24 00:55:00 | METOP-B | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6e28d476-ac53-3bbe-b6d8-4c52daa25081 | -11.5486 | -56.9338 | 2026-05-24 00:55:00 | METOP-B | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 18314eae-4116-305f-92c8-87106a6c1eed | -11.5424 | -56.951599 | 2026-05-24 00:55:00 | METOP-B | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a0601016-330d-3f4d-81ff-f30f463d0c36 | -18.6387 | -48.862099 | 2026-05-24 00:55:00 | METOP-B | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| e4a7ddc4-8191-30f0-a25b-525b8b03eb56 | -12.5511 | -57.161701 | 2026-05-24 00:55:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| fb2675d4-8dc2-33ef-bddd-9acb53d726d0 | -11.174 | -55.908199 | 2026-05-24 00:55:00 | METOP-B | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| df500dad-df52-3b21-bd43-61d5f435269e | -15.1007 | -57.618198 | 2026-05-24 00:55:00 | METOP-B | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| cd547473-77d2-32d5-b2f6-d944630f15f5 | -12.8933 | -58.161999 | 2026-05-24 00:55:00 | METOP-B | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 64046278-fed3-3a4f-b3aa-60f95bb28496 | -14.0175 | -53.338902 | 2026-05-24 00:55:00 | METOP-B | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 36c991a6-39ee-3a63-be54-2c69d2011dc3 | -12.8899 | -58.192699 | 2026-05-24 00:55:00 | METOP-B | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| fd184920-02db-3fd4-ab4e-dcadb66c6719 | -11.5406 | -56.943802 | 2026-05-24 00:55:00 | METOP-B | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7da3ff04-e0d3-3a72-a200-f763152db6aa | -12.8965 | -58.176201 | 2026-05-24 00:55:00 | METOP-B | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 65e640bf-024f-3d2c-844e-95f46450807a | -12.8949 | -58.169102 | 2026-05-24 00:55:00 | METOP-B | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 600ae5e4-6f57-3133-81d7-2e1d655642d5 | -11.176 | -55.916901 | 2026-05-24 00:55:00 | METOP-B | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2cd0ebc2-7c91-37fa-8f6b-1d903a372704 | -12.8861 | -58.1692 | 2026-05-24 01:00:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 70.7 |
| c7c04d28-1a51-3153-8bbb-099c15287ed8 | -12.9052 | -58.1676 | 2026-05-24 01:00:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 62.9 |
| 29f40da0-a029-3057-b5a5-2538482ebae1 | -18.657 | -48.8785 | 2026-05-24 01:00:00 | GOES-19 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 65.0 |
| 48b43fab-8e97-395e-ae3b-c0bc2ba8d65d | -12.9049 | -58.1875 | 2026-05-24 01:00:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 45.0 |
| aa68b721-b1ce-376e-9ff0-64560f58147d | -12.8859 | -58.1891 | 2026-05-24 01:00:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 49.8 |
| cb1c363a-7efa-347a-9a13-4decf4a91343 | -12.8861 | -58.1692 | 2026-05-24 01:10:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 74.2 |
| d5d84fb0-bee0-3c38-8957-dc5e83fd8de4 | -12.9052 | -58.1676 | 2026-05-24 01:10:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 74.3 |
| db8e8df7-2704-3471-819b-16e187e0d8ce | -18.657 | -48.8785 | 2026-05-24 01:10:00 | GOES-19 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 64.3 |
| 98798a58-4e46-31ed-876c-40c257683472 | -18.6576 | -48.8558 | 2026-05-24 01:10:00 | GOES-19 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 50.2 |
| 443d1337-ae0a-35cc-bb23-da54600aa37f | -12.9052 | -58.1676 | 2026-05-24 01:20:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 60.7 |
| 4f0dc0ef-b73e-33a7-bab1-0a850ec03d5f | -12.8861 | -58.1692 | 2026-05-24 01:20:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 65.4 |
| 25be0355-adfe-35c0-8ecc-d7bdaf66bf62 | -12.902 | -58.182201 | 2026-05-24 01:21:00 | METOP-C | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 47b6ca3b-a91e-30a6-8922-a993b40f2498 | -15.0858 | -57.628601 | 2026-05-24 01:21:00 | METOP-C | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2771569c-a47e-3dbc-be8c-80922816bcd3 | -15.1038 | -57.617001 | 2026-05-24 01:21:00 | METOP-C | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4b5ccca1-68df-3fd8-ac0e-4db759cec977 | -15.0874 | -57.6357 | 2026-05-24 01:21:00 | METOP-C | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 931cfb52-f132-3619-b16a-18bc89e16925 | -12.8953 | -58.198502 | 2026-05-24 01:21:00 | METOP-C | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 9f8f3972-8e18-38b8-8eaa-7ebd6c28448d | -14.0199 | -53.363602 | 2026-05-24 01:21:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README2.md)
