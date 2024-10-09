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

## Dados Diários - Página 44

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4d29033e-111e-3dd2-a713-c69b7a5e8fa2 | -10.9272 | -63.851601 | 2024-10-09 01:26:57 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 5d00a1d3-d42d-3b49-9d13-289ef52edcc9 | -10.929 | -63.8601 | 2024-10-09 01:26:57 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 40b985f3-f9ae-31af-8d6f-18a35827c925 | -10.9156 | -63.8452 | 2024-10-09 01:26:57 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| b251c288-34e5-3729-ab2a-9a2440452a1a | -10.9174 | -63.853699 | 2024-10-09 01:26:57 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| d6ceb7b4-e5a0-32c6-a333-a45948cd3ab3 | -10.9192 | -63.862202 | 2024-10-09 01:26:57 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 6e083e02-7312-378e-870c-a49368ce4c10 | -10.913 | -63.881199 | 2024-10-09 01:26:57 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| efa9322c-d722-3e97-bf3a-afd99d959f9f | -10.9032 | -63.883301 | 2024-10-09 01:26:57 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 5e4cfc03-62e5-32e5-a16b-d6fa69d9da31 | -10.905 | -63.8918 | 2024-10-09 01:26:57 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 797820a6-3e97-3000-ac18-12ee222e6a67 | -20.2915 | -43.9444 | 2024-10-09 01:26:58 | GOES-16 | ITABIRITO | MINAS GERAIS | Brasil | 3131901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 126.6 |
| 71d706ef-fb61-3eec-afdd-eb68c99a9909 | -10.8641 | -63.8918 | 2024-10-09 01:26:58 | METOP-B | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 340d4973-6650-36f5-8ae4-d94f7295296e | -10.8659 | -63.9002 | 2024-10-09 01:26:58 | METOP-B | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 7c1fc5fe-5b0f-36d0-b3bc-dd4501747ba3 | -10.8677 | -63.908699 | 2024-10-09 01:26:58 | METOP-B | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 9ea53492-c9b3-3c93-8a51-ed836f8805f4 | -10.8695 | -63.917301 | 2024-10-09 01:26:58 | METOP-B | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 1fb67e3b-d52d-3b1c-b0be-37f79f87fcbc | -10.9134 | -64.1241 | 2024-10-09 01:26:58 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 8e36f09d-ea43-38b9-84ce-4f210a89fd42 | -10.9152 | -64.132797 | 2024-10-09 01:26:58 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 0926dd0b-0968-341c-9c7c-5ffa863a3d8b | -10.9171 | -64.141602 | 2024-10-09 01:26:58 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| dc0ef917-26a8-3f00-9549-e4da629fb7d2 | -10.9036 | -64.126198 | 2024-10-09 01:26:58 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 515f8870-889e-30ac-b334-3d37f21187ef | -10.9054 | -64.134903 | 2024-10-09 01:26:58 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 100a9edb-cc23-3f3a-8dae-4a9c4d79a4c6 | -10.9091 | -64.152397 | 2024-10-09 01:26:58 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 5ef6ce87-7ea4-3df5-958b-32ce5ef77769 | -10.8956 | -64.137001 | 2024-10-09 01:26:58 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| b5fc34e3-fed4-3f7d-acee-346c3136cb7a | -10.8975 | -64.145798 | 2024-10-09 01:26:58 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 1a607b06-e4a0-3866-9e14-8b00fb034abd | -10.8952 | -63.893902 | 2024-10-09 01:26:58 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 929a5895-42cc-3f6d-9f11-b9035ef496d5 | -10.897 | -63.902401 | 2024-10-09 01:26:58 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| de4ec59b-d4e4-3a03-aedf-91853a102ed2 | -10.8854 | -63.896 | 2024-10-09 01:26:58 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 557befa1-fc88-3948-957c-f732e82dbad6 | -10.8872 | -63.904499 | 2024-10-09 01:26:58 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 71d4a9c2-e4d4-3d7a-aa74-c7b3cca1af63 | -10.889 | -63.913101 | 2024-10-09 01:26:58 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| e44edef8-7e86-302e-9f08-37e12b919e63 | -10.8721 | -63.881199 | 2024-10-09 01:26:58 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| ad8069ea-f021-37aa-b5a0-928f06b585ac | -10.8739 | -63.889702 | 2024-10-09 01:26:58 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 5a1d8a10-6483-3dae-a3ed-fdf15d1c4ca4 | -10.8757 | -63.898102 | 2024-10-09 01:26:58 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 6ae827e1-8669-30d5-ad4c-7b12946555cf | -10.8775 | -63.906601 | 2024-10-09 01:26:58 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 0f042d0e-706c-399e-b311-4f3b68548413 | -10.8793 | -63.915199 | 2024-10-09 01:26:58 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| b386f6f1-e053-36c8-a45d-e2a6c5ae0a82 | -10.8586 | -63.866299 | 2024-10-09 01:26:58 | METOP-B | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| c4c17733-608e-3de3-9193-82200538bf94 | -10.8604 | -63.874802 | 2024-10-09 01:26:58 | METOP-B | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 9fc456ad-cedb-3c40-b67e-e95285e4a125 | -10.8623 | -63.883301 | 2024-10-09 01:26:58 | METOP-B | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| c255072c-11be-3be8-838a-3b17981a0a82 | -20.3346 | -48.7307 | 2024-10-09 01:26:59 | GOES-16 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 180.7 |
| 678df3e8-b1e3-35e6-9433-33d40996b401 | -20.3352 | -48.7076 | 2024-10-09 01:26:59 | GOES-16 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 198.8 |
| 3bacdfb5-fc7c-331d-9385-631e29ba3485 | -20.3551 | -48.7262 | 2024-10-09 01:26:59 | GOES-16 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 325.0 |
| 0c6ad5e4-c322-32e8-9ff0-22f6f6c72ed7 | -20.3557 | -48.7031 | 2024-10-09 01:26:59 | GOES-16 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 260.8 |
| da6dd8f1-cd50-35d7-87a8-bef900c460da | -20.3755 | -48.7217 | 2024-10-09 01:26:59 | GOES-16 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 147.1 |
| e7ecf344-838d-3c4e-ab3f-4861de9d071f | -20.3761 | -48.6986 | 2024-10-09 01:26:59 | GOES-16 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 111.9 |
| d3149e79-f030-3967-adaf-6640a29a3fca | -10.1779 | -60.8848 | 2024-10-09 01:26:59 | METOP-B | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ebc7098d-98e5-3775-923b-d1cb459e58c5 | -10.1795 | -60.891701 | 2024-10-09 01:26:59 | METOP-B | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5daf4ff4-0116-3cf9-9e50-23ed1cd559a9 | -10.8877 | -64.147903 | 2024-10-09 01:26:59 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 7d3ac723-aa0d-3b5a-a791-26df8fe2dbea | -10.8387 | -64.158302 | 2024-10-09 01:26:59 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| e0152db5-10a3-3eaa-9349-02cd8276894b | -10.8405 | -64.167099 | 2024-10-09 01:26:59 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 33127506-8735-32be-a112-5f782f2e7abd | -10.8363 | -64.195503 | 2024-10-09 01:27:00 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| e2ce455f-a057-3879-aa83-d25c6e4084e9 | -10.8382 | -64.2043 | 2024-10-09 01:27:00 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| ffae8eb2-fac2-3021-be90-e3d7ef58401d | -10.84 | -64.213097 | 2024-10-09 01:27:00 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 86567033-317c-353b-9eb9-ad902974ac0a | -10.694 | -63.623001 | 2024-10-09 01:27:00 | METOP-B | CAMPO NOVO DE RONDÔNIA | RONDÔNIA | Brasil | 1100700 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 45a211d5-dd37-3baa-9bb7-ef10922e92a0 | -10.6957 | -63.631199 | 2024-10-09 01:27:00 | METOP-B | CAMPO NOVO DE RONDÔNIA | RONDÔNIA | Brasil | 1100700 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| a956f7c2-b117-34e8-9333-89f85de76d95 | -20.7839 | -47.2559 | 2024-10-09 01:27:01 | GOES-16 | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | 313.0 |
| 89cefbca-877b-36f1-8e2b-6c8c2b260437 | -20.7846 | -47.2323 | 2024-10-09 01:27:01 | GOES-16 | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | 224.4 |
| bd015e6e-681a-37f4-b46b-a3349f6673d9 | -20.8045 | -47.251 | 2024-10-09 01:27:01 | GOES-16 | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | 102.9 |
| cf0de100-14ce-3db9-a60e-63c3d5052639 | -10.71 | -64.131302 | 2024-10-09 01:27:01 | METOP-B | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| c3dd0283-7319-3452-8776-bbc446389ecb | -10.7137 | -64.148697 | 2024-10-09 01:27:01 | METOP-B | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 141545d2-72b5-3a32-8102-1a0c9dabe8c5 | -9.8902 | -60.1992 | 2024-10-09 01:27:01 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a9e9e6cc-9b34-3db4-b072-38b58e452d64 | -9.8917 | -60.2061 | 2024-10-09 01:27:01 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6ed1035b-fbd0-3c2a-abec-dfb3fdabb170 | -9.9137 | -60.3036 | 2024-10-09 01:27:01 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| cfc650c0-35f7-3ab2-aa9c-c6d7ddc3c7e6 | -9.9153 | -60.3106 | 2024-10-09 01:27:01 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 083f2d24-2251-3434-babc-941fd8f15409 | -9.9023 | -60.299 | 2024-10-09 01:27:01 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| decd8ef7-27c6-348a-84cd-6a90d15b082e | -10.4739 | -62.886002 | 2024-10-09 01:27:01 | METOP-B | CACAULÂNDIA | RONDÔNIA | Brasil | 1100601 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 5fb9d8e1-59ee-38d9-85c6-84c12ef4cd57 | -9.8894 | -60.287201 | 2024-10-09 01:27:01 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 699a6aed-32da-3b53-aa97-251e35abb0c2 | -9.891 | -60.294201 | 2024-10-09 01:27:01 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a9b73989-c03b-3373-87a3-9d35699ca143 | -10.0711 | -61.098202 | 2024-10-09 01:27:01 | METOP-B | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 68ea3620-61da-3d82-a726-1a0c828ccc64 | -10.0726 | -61.105202 | 2024-10-09 01:27:01 | METOP-B | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d7714245-a4ef-3bda-ab28-42c95361dcde | -10.0742 | -61.112099 | 2024-10-09 01:27:01 | METOP-B | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f026aba8-d496-38e2-9239-8044205d964e | -10.0613 | -61.100399 | 2024-10-09 01:27:01 | METOP-B | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 21fde30e-9423-35a4-a0b7-403f41b6db47 | -10.0628 | -61.107399 | 2024-10-09 01:27:01 | METOP-B | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3ede7945-2170-353f-8f8d-b3b2d062f659 | -9.8698 | -60.291698 | 2024-10-09 01:27:01 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 374b9e3a-0f0d-34d2-9b78-97779fafee25 | -9.8714 | -60.298698 | 2024-10-09 01:27:01 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b645f1d9-f939-3cf7-8407-381ef8b1efd2 | -10.7063 | -64.113998 | 2024-10-09 01:27:01 | METOP-B | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 8503ca59-8e01-3b8f-8f2c-9902802874f7 | -10.7119 | -64.139999 | 2024-10-09 01:27:01 | METOP-B | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 3a636723-9149-3ca2-b673-6554d8cd0710 | -10.7021 | -64.142097 | 2024-10-09 01:27:02 | METOP-B | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 86c27b5e-0f4b-35fb-8abf-5368be4e9186 | -10.6521 | -63.9552 | 2024-10-09 01:27:02 | METOP-B | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 20be1e38-678c-304a-aa6c-162c10fd828b | -10.6539 | -63.963699 | 2024-10-09 01:27:02 | METOP-B | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| fce85c0b-cee2-31b9-8c0b-8b2e03fc6422 | -10.9001 | -65.229599 | 2024-10-09 01:27:02 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| fe9da11a-c4c1-3393-a53c-b183e375e901 | -9.8066 | -60.423 | 2024-10-09 01:27:03 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7196653d-f303-353a-bcd6-546cb6e9f51b | -9.8082 | -60.429901 | 2024-10-09 01:27:03 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 10796504-e904-3b74-8446-3e08f4f458cd | -9.8097 | -60.436901 | 2024-10-09 01:27:03 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 37ac139d-7bf8-3762-800d-a6a1d2c5d0f3 | -9.8129 | -60.450699 | 2024-10-09 01:27:03 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 74229a40-03bb-3d60-8202-0949209d18ed | -9.8144 | -60.457699 | 2024-10-09 01:27:03 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 631c302d-aaa8-3eac-881f-28e8f93d96a9 | -9.8657 | -60.686298 | 2024-10-09 01:27:03 | METOP-B | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e3845366-0adc-3088-b87a-076dace6d362 | -10.5907 | -64.003899 | 2024-10-09 01:27:03 | METOP-B | CAMPO NOVO DE RONDÔNIA | RONDÔNIA | Brasil | 1100700 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| d7692056-e32e-3d2b-a11f-514a1055056f | -10.5925 | -64.012497 | 2024-10-09 01:27:03 | METOP-B | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| ba82dd51-e68a-3720-b5bc-117c3db696bc | -10.5944 | -64.021004 | 2024-10-09 01:27:03 | METOP-B | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 0c26fb63-8eb9-3789-9f44-6101193a33ca | -9.8544 | -60.681599 | 2024-10-09 01:27:03 | METOP-B | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7e307a8c-cfcc-35b8-9af7-bda8554e08a7 | -9.8559 | -60.688499 | 2024-10-09 01:27:03 | METOP-B | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9839f584-a65a-3990-bfce-80c10dd5aa5f | -9.8575 | -60.6954 | 2024-10-09 01:27:03 | METOP-B | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4ae95013-cd8e-375e-b6f7-d8a7cbd70bbd | -10.5828 | -64.014603 | 2024-10-09 01:27:03 | METOP-B | CAMPO NOVO DE RONDÔNIA | RONDÔNIA | Brasil | 1100700 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 1ee12d19-d514-353a-9f31-79752aad0b89 | -10.5846 | -64.023102 | 2024-10-09 01:27:03 | METOP-B | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 4e65dec7-e79d-33b5-8391-0bc75d97bd5d | -10.6334 | -64.3498 | 2024-10-09 01:27:03 | METOP-B | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 86bdc48b-040f-3b92-b9e9-4df5d7f74ec6 | -10.8031 | -65.156303 | 2024-10-09 01:27:03 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 7524ee03-88dc-3e2c-8917-85323579572d | -10.1369 | -62.094501 | 2024-10-09 01:27:04 | METOP-B | THEOBROMA | RONDÔNIA | Brasil | 1101609 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 323ca44f-a19a-305f-8be5-188523dbfa8c | -10.1385 | -62.1017 | 2024-10-09 01:27:04 | METOP-B | THEOBROMA | RONDÔNIA | Brasil | 1101609 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 464026ae-f863-36bd-a692-f64de8cc6ee9 | -10.6271 | -64.416496 | 2024-10-09 01:27:04 | METOP-B | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| b16b9415-1200-3dac-bed6-8ccb1e24f05e | -10.648 | -64.5158 | 2024-10-09 01:27:04 | METOP-B | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 77611b1f-8691-33c7-a6f5-6d3817c3cf15 | -10.6499 | -64.524803 | 2024-10-09 01:27:04 | METOP-B | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| a7a88d17-a2f2-3595-b760-30fa2eaf31c4 | -10.6116 | -64.3918 | 2024-10-09 01:27:04 | METOP-B | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| d8b70239-a51a-3074-a544-c120b0bff9be | -10.6382 | -64.517799 | 2024-10-09 01:27:04 | METOP-B | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 4220fe0e-253b-3c5e-a42d-a229d55800b1 | -10.6401 | -64.526901 | 2024-10-09 01:27:04 | METOP-B | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README45.md)
