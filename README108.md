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

## Dados Diários - Página 108

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 31d59a7c-0adf-364c-82f0-3248494d3abe | -9.50339 | -50.88935 | 2025-09-13 05:25:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e1f47605-66a2-3873-b478-e2616bcfc4e0 | -8.09459 | -50.17873 | 2025-09-13 05:25:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0e2d0b16-8e62-3b62-a243-9e350e913967 | -9.24288 | -51.26479 | 2025-09-13 05:25:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d7d8c451-7a07-38fb-ab79-55da0dfb2bbe | -7.66953 | -61.17031 | 2025-09-13 05:25:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 50bd5c33-e887-3665-8803-9184d1185ad6 | -10.32647 | -48.81911 | 2025-09-13 05:25:00 | NPP-375D | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 3573e16e-c21e-37f9-9011-490ef85de4a3 | -10.50892 | -51.54142 | 2025-09-13 05:25:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 52cc3731-d6af-37bc-acd2-a0c14f9786fb | -9.50081 | -66.80003 | 2025-09-13 05:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ae254a09-ea67-370d-830f-000758a666be | -11.87247 | -50.58358 | 2025-09-13 05:25:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 38.0 |
| 6e361319-8445-3ab2-bfec-c6ddebb605dc | -9.23183 | -51.21695 | 2025-09-13 05:25:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8b3d5c62-c02d-3837-8a97-e20b6b7b6697 | -9.71781 | -64.93379 | 2025-09-13 05:25:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4ecbecdf-9f64-3ab2-a425-6a69480adfbf | -10.45426 | -50.60524 | 2025-09-13 05:25:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 26d54b1e-9aae-3ca1-a955-84e752d0e596 | -9.26301 | -59.40495 | 2025-09-13 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 21.2 |
| 5db49e63-48ac-39ee-9476-5eb8ca3a6200 | -11.83786 | -50.55665 | 2025-09-13 05:25:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 9f031f10-7620-3bce-813e-7b0059d3cef0 | -9.56002 | -66.7348 | 2025-09-13 05:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| eba3110c-0bb8-3664-9967-5b58e995433a | -9.72301 | -64.92554 | 2025-09-13 05:25:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8c3a6d6b-65aa-39f4-9d88-7cdbfbf77140 | -9.24019 | -51.24125 | 2025-09-13 05:25:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1190bb3e-5cd5-35d3-b3a6-10d3be1b06d3 | -7.75885 | -61.12373 | 2025-09-13 05:25:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 41620f9c-2b90-3025-9eb9-2303f6297740 | -9.49762 | -50.88842 | 2025-09-13 05:25:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 25eca94f-8351-308c-a7d7-1552094f0eda | -9.80985 | -61.52042 | 2025-09-13 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7ec2a91b-7174-3bb7-9ac8-aa839a7b750b | -11.11888 | -50.70228 | 2025-09-13 05:25:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4c716a90-28d0-3b9f-99d6-3066eea6c81d | -11.14338 | -50.70093 | 2025-09-13 05:25:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 8bba60af-cb8f-3a75-a15c-f88e04b62773 | -11.83357 | -50.5457 | 2025-09-13 05:25:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 13.0 |
| edacd85f-40b3-313c-b83c-4dfa6e1fe874 | -10.33784 | -48.81277 | 2025-09-13 05:25:00 | NPP-375D | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| ac8559d7-9de8-37e0-837d-ec7a5fb28d23 | -16.36906 | -51.53492 | 2025-09-13 05:27:00 | NPP-375D | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 527fb032-3c67-38ed-8be2-3162f571f96e | -15.67358 | -49.90601 | 2025-09-13 05:27:00 | NPP-375D | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 58ebdce7-9473-3798-83ed-39768dfbfee4 | -16.35746 | -51.54271 | 2025-09-13 05:27:00 | NPP-375D | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4eb0aa5b-f469-3f2e-921f-520564f70d53 | -16.33316 | -51.52647 | 2025-09-13 05:27:00 | NPP-375D | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f49c7e5a-25a3-3a69-a470-b263a8381824 | -15.77981 | -52.25215 | 2025-09-13 05:27:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 39480d8f-b35e-3fa6-ae54-630ba79f6327 | -17.41601 | -49.23948 | 2025-09-13 05:27:00 | NPP-375D | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 882d6c47-8802-35c0-bbb7-f3a63aa636e5 | -10.58107 | -61.26268 | 2025-09-13 05:27:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0d9c3f5b-fbb0-3820-95f7-73bafbd159aa | -12.88242 | -62.11215 | 2025-09-13 05:27:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e48d6040-ed53-3eea-aa23-ceff19fd845c | -10.5844 | -61.26323 | 2025-09-13 05:27:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 84cc740b-6de2-3686-b9ac-14219de78559 | -15.55685 | -54.80389 | 2025-09-13 05:27:00 | NPP-375D | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8629b9db-8733-3ccf-aedb-9dbe5ae5369f | -11.37906 | -63.35888 | 2025-09-13 05:27:00 | NPP-375D | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 90b90640-04af-3701-9bc2-716dadad91af | -15.10069 | -47.99895 | 2025-09-13 05:27:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3734fe04-b252-3f9e-a873-30ab4f88a844 | -10.15522 | -64.72726 | 2025-09-13 05:27:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 160bfe24-ba07-367a-8a00-c130635ebdb5 | -13.27142 | -51.70462 | 2025-09-13 05:27:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bbea695e-ff73-30cc-918d-36490ec04e78 | -12.35264 | -63.64236 | 2025-09-13 05:27:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a3c418ff-ecde-35d5-ba0c-22106a09d1f6 | -14.38827 | -60.30884 | 2025-09-13 05:27:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| adb9d943-f437-31e5-b35c-e8b598d823ee | -11.37845 | -63.36261 | 2025-09-13 05:27:00 | NPP-375D | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7f8d76ab-fb47-35e3-9fbf-266a17b59af0 | -14.61848 | -52.08363 | 2025-09-13 05:27:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 720faf9a-1923-3e98-9da4-10e078879c04 | -16.49507 | -55.13187 | 2025-09-13 05:27:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 8931db9c-560a-3d9d-90e9-317ea1abe1bf | -16.49667 | -55.15018 | 2025-09-13 05:27:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 8e910841-da9b-31f5-9672-5a5deb91031a | -16.33973 | -51.53616 | 2025-09-13 05:27:00 | NPP-375D | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 675fe5c3-51f3-3d59-93eb-a5399f48436f | -15.86052 | -49.94991 | 2025-09-13 05:27:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 30f56e02-58b8-3006-a976-511004342cad | -12.94706 | -47.98192 | 2025-09-13 05:27:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a406c1d7-ff71-3de5-98ba-c7f939d9785a | -15.77486 | -52.24396 | 2025-09-13 05:27:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 5211a5d3-9d89-3617-901c-733588964df0 | -15.21016 | -56.68777 | 2025-09-13 05:27:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e5160cae-4652-30ae-b764-3009319f5b80 | -15.2144 | -56.68845 | 2025-09-13 05:27:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1df0110e-628f-3b9c-9b33-7bce65670231 | -16.36247 | -51.53912 | 2025-09-13 05:27:00 | NPP-375D | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 16217db2-1a0b-3175-b2de-d6986107e1c7 | -16.41434 | -49.04673 | 2025-09-13 05:27:00 | NPP-375D | TEREZÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5221197 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7c1fb503-52d9-3b8d-9e15-acc808ed0480 | -12.89633 | -62.08899 | 2025-09-13 05:27:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d26223b2-fdcf-3b5f-b532-f6d974171ec9 | -16.56434 | -49.22369 | 2025-09-13 05:27:00 | NPP-375D | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 90bcfed2-eb59-3460-b834-4fec08314f16 | -16.49434 | -55.13765 | 2025-09-13 05:27:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 81279164-8f92-3273-b859-0f24bdaef1b4 | -16.64697 | -49.76294 | 2025-09-13 05:27:00 | NPP-375D | NAZÁRIO | GOIÁS | Brasil | 5214408 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c167f8bb-788e-3e44-a08e-257f22a265a7 | -15.15816 | -50.15873 | 2025-09-13 05:27:00 | NPP-375D | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| d6a2a4f4-8019-3c73-a812-0a6ac10670b0 | -16.55732 | -49.22356 | 2025-09-13 05:27:00 | NPP-375D | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 2f4ad730-5975-319c-bbd8-e1163906a797 | -15.54713 | -54.80285 | 2025-09-13 05:27:00 | NPP-375D | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 662bc0b4-12d4-382d-9d64-b952acbddf8c | -16.50958 | -55.1234 | 2025-09-13 05:27:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| f427da79-590f-3b4f-8c15-081a68b323d2 | -17.44571 | -49.24395 | 2025-09-13 05:27:00 | NPP-375D | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 218eefc4-7be6-3f58-ac09-7debda2c3d0d | -17.37238 | -52.91501 | 2025-09-13 05:27:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 99f3f20f-292f-3b9c-bb6f-eff574a68a5f | -12.8967 | -62.19447 | 2025-09-13 05:27:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 799c2955-1881-36e4-843e-5ff0f5c94360 | -10.15011 | -64.73528 | 2025-09-13 05:27:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 67b3c3fc-893c-3204-9972-8a21d3089132 | -11.77252 | -64.92805 | 2025-09-13 05:27:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 68cf6cbd-b2ee-3fb0-9f74-151dd0f626a5 | -15.7741 | -52.25106 | 2025-09-13 05:27:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 39ddb6f6-add0-362a-8469-19f6ac8348e2 | -15.207 | -56.6791 | 2025-09-13 05:27:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8125bee0-a150-3eb5-b8d5-630b14564f4c | -12.95288 | -47.99553 | 2025-09-13 05:27:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| d25101cd-2ffe-371b-80d6-00bafb93a147 | -16.87264 | -49.34095 | 2025-09-13 05:27:00 | NPP-375D | HIDROLÂNDIA | GOIÁS | Brasil | 5209705 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 25c6219c-3752-3ab0-af02-da7fddca0b69 | -15.58606 | -54.7532 | 2025-09-13 05:27:00 | NPP-375D | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 387cb0b8-b7e1-3c8e-81d2-8e9ca6db3ddd | -15.16175 | -52.47442 | 2025-09-13 05:27:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f0811cdc-6491-3ebc-9a93-5d7027169c69 | -15.7705 | -52.2303 | 2025-09-13 05:27:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| de4beecc-743d-311f-8187-29d2283de2b3 | -17.43312 | -49.22702 | 2025-09-13 05:27:00 | NPP-375D | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 157a8e15-b9c9-3ae7-a053-55a7d2b93aaf | -12.80913 | -47.96196 | 2025-09-13 05:27:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 9e5686b7-66d8-3b69-b662-5f3b59bb8742 | -15.06168 | -48.01317 | 2025-09-13 05:27:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| efdcafc1-fd18-337b-b3a6-fc12372aee00 | -16.40957 | -49.04133 | 2025-09-13 05:27:00 | NPP-375D | TEREZÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5221197 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1ac0df91-0e90-3c43-a712-eb2f44b6f4b2 | -12.8602 | -62.12304 | 2025-09-13 05:27:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f72bd359-fb0c-33c4-9133-78d9fa501b21 | -15.81902 | -52.21369 | 2025-09-13 05:27:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c4dce3f2-f4bb-3f5f-b616-db93173a969d | -12.79943 | -47.98471 | 2025-09-13 05:27:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d9c252e5-dde1-3f7c-a743-477e931e2c4c | -16.36018 | -51.51577 | 2025-09-13 05:27:00 | NPP-375D | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 44bf34a8-8885-3a65-8d52-ad1edc0e3519 | -15.78523 | -52.25583 | 2025-09-13 05:27:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| defb578c-606f-3acb-8144-1efb7f4bc8b1 | -14.74023 | -60.22484 | 2025-09-13 05:27:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e4cf5886-ed3b-36c9-884d-364572b554bd | -13.11432 | -56.8017 | 2025-09-13 05:27:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5cebe155-d75c-3528-b983-34ec966a3d8b | -15.21386 | -56.69243 | 2025-09-13 05:27:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e452060e-2e9c-3659-9774-4049b4d867ba | -12.86241 | -62.13068 | 2025-09-13 05:27:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4464ee1c-2e74-3d06-80a4-ba9d8a12a208 | -14.38784 | -60.28835 | 2025-09-13 05:27:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2faf0bb5-db37-3e0b-93b7-a90e513b86d4 | -17.30176 | -48.7408 | 2025-09-13 05:27:00 | NPP-375D | SANTA CRUZ DE GOIÁS | GOIÁS | Brasil | 5219209 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3f4583cf-f8f8-3e9d-a7e6-880ba92704c9 | -15.84743 | -49.94671 | 2025-09-13 05:27:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| fb3ecbf4-3732-30c3-968a-62b1c199b040 | -10.57565 | -63.48247 | 2025-09-13 05:27:00 | NPP-375D | GOVERNADOR JORGE TEIXEIRA | RONDÔNIA | Brasil | 1101005 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b197da4a-f576-3521-a5e0-b4b14e928f3d | -16.49452 | -55.12699 | 2025-09-13 05:27:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 98ab6433-0f24-3444-b9a6-7a8fb691d11c | -14.3866 | -60.2965 | 2025-09-13 05:27:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2312e7f6-886e-3b12-b2af-cd10129e1bdc | -17.30959 | -48.73446 | 2025-09-13 05:27:00 | NPP-375D | SANTA CRUZ DE GOIÁS | GOIÁS | Brasil | 5219209 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| af25e315-5ddc-3d65-9ec9-b5f40f0092a6 | -17.42272 | -49.26258 | 2025-09-13 05:27:00 | NPP-375D | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 07360825-e2ad-336c-91f4-74f6e9330e25 | -12.17116 | -60.74944 | 2025-09-13 05:27:00 | NPP-375D | CHUPINGUAIA | RONDÔNIA | Brasil | 1100924 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 32706d43-a0e8-3d53-8b8c-6f6a263738a6 | -15.87437 | -49.94564 | 2025-09-13 05:27:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3242dcb9-3b22-30f0-9996-d3d25dd7b845 | -17.41418 | -49.26072 | 2025-09-13 05:27:00 | NPP-375D | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 427a2e54-d320-31e6-b6fb-d9ce338c553c | -15.17101 | -52.49317 | 2025-09-13 05:27:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 99f9ff72-1915-349e-a105-90ab3d1584b9 | -16.55791 | -49.2169 | 2025-09-13 05:27:00 | NPP-375D | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 3b1e128c-3321-3939-9abf-4222e545e562 | -15.16579 | -50.14837 | 2025-09-13 05:27:00 | NPP-375D | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| c5da9260-b90b-3fef-83ba-f9c2f4eb6730 | -13.456 | -51.78482 | 2025-09-13 05:27:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e03dbe5b-b903-3815-998a-5a5965037dc3 | -15.782 | -52.23181 | 2025-09-13 05:27:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |


[Clique aqui para ver as próximas entradas](README109.md)
