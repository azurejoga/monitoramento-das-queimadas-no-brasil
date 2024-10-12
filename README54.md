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

## Dados Diários - Página 54

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1864c635-6820-31d2-a40b-27a7ad4ed6bb | -17.17441 | -57.46367 | 2024-10-12 04:10:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 2fb56f05-b521-33ed-9366-b08ddde49314 | -17.17301 | -57.46984 | 2024-10-12 04:10:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| bf479068-b54e-3814-8c1c-0b18f23863e4 | -17.17161 | -57.47601 | 2024-10-12 04:10:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| a885966b-5beb-3885-be71-038d9e33c05f | -17.98463 | -57.38258 | 2024-10-12 04:10:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 298aceeb-9265-3ca1-ae84-a3e52f0ae1fc | -17.9808 | -57.36911 | 2024-10-12 04:10:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.8 |
| dd49a226-a3a4-3adf-a481-e80c0b53482e | -17.97947 | -57.37499 | 2024-10-12 04:10:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 6259cbb4-5f2d-3d74-a07d-3c68e170f90c | -17.97872 | -57.37101 | 2024-10-12 04:10:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.5 |
| 20aa0440-6d0f-3b2d-a527-1d643fbde9dd | -17.73008 | -56.26014 | 2024-10-12 04:10:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 0c3bccc7-7861-3516-97d6-c9f1447e2bb2 | -17.72282 | -56.26361 | 2024-10-12 04:10:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 83f170ea-bc20-3ebe-80e1-ff46972f64b2 | -17.17059 | -57.44967 | 2024-10-12 04:10:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| dd7c976f-39e3-38c7-ae08-0f5dc5c72135 | -18.1286 | -56.33922 | 2024-10-12 04:10:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 0e9f5ee5-c5fd-3664-8a49-11e3efdb5d01 | -18.1275 | -56.34424 | 2024-10-12 04:10:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 6d892f73-e9f8-3dde-9bf3-cd0afe524bf2 | -18.12693 | -56.34018 | 2024-10-12 04:10:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 1d27c540-52d2-3cde-ad07-cab9c5d072d4 | -18.12535 | -56.31862 | 2024-10-12 04:10:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 02dde23c-db00-30b7-bf94-fd1596fe09ee | -18.09139 | -56.41111 | 2024-10-12 04:10:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| c8077bea-ce0a-350f-ad3a-c2094a80cd6a | -18.09023 | -56.41619 | 2024-10-12 04:10:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| d25c0aba-db46-3c27-bb3d-aa96f9b0ef47 | -18.0902 | -56.42555 | 2024-10-12 04:10:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| f3f1e857-e303-3527-aacf-ed8260b0f02c | -18.08908 | -56.42128 | 2024-10-12 04:10:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 67f48192-6331-3ccd-8044-340f51d8e5cb | -18.08792 | -56.42636 | 2024-10-12 04:10:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| d1dd747c-e822-3706-adb4-d4181f450c65 | -18.08743 | -56.4087 | 2024-10-12 04:10:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 159086ee-6979-312f-840b-bf57ba691da4 | -18.0864 | -56.40451 | 2024-10-12 04:10:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 9086ea19-8c72-35ba-b5e3-779e8d4ed365 | -18.0863 | -56.41379 | 2024-10-12 04:10:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| c8386417-e7e9-38be-a2d8-7f5fc8dfe052 | -18.08524 | -56.40958 | 2024-10-12 04:10:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 3259e244-a500-3cd4-90fa-cdde6674bfb8 | -18.08408 | -56.41466 | 2024-10-12 04:10:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 752f4971-40a5-3348-8600-004f17c1e29b | -18.08405 | -56.42398 | 2024-10-12 04:10:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 242ae60f-13a4-375c-adca-ba27bed60b11 | -18.08292 | -56.42907 | 2024-10-12 04:10:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 17fcbff8-75cb-31c7-acca-9b74db65ba59 | -18.08061 | -56.42989 | 2024-10-12 04:10:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 09287971-b7b4-3452-899c-846e05caf2e6 | -18.07963 | -56.38532 | 2024-10-12 04:10:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 2fb461ce-1d76-333f-82dc-c16c2f11baf1 | -18.07349 | -56.38376 | 2024-10-12 04:10:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| b5682b1b-4182-3e4f-90ed-a9211c44183c | -17.70259 | -56.2959 | 2024-10-12 04:10:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 64bb76f5-f757-3e05-8d38-a9185b01a9b8 | -21.54506 | -52.58971 | 2024-10-12 04:10:00 | NOAA-20 | SANTA RITA DO PARDO | MATO GROSSO DO SUL | Brasil | 5007554 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fb245462-1eaa-3beb-b94b-46f1ce7d59cd | -17.6601 | -56.26251 | 2024-10-12 04:10:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 4cf05f4f-ed99-3e5b-b50b-7c29bec0816d | -17.7217 | -56.26863 | 2024-10-12 04:10:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 8538571c-d170-3825-9361-d9b494b4cb57 | -17.70593 | -56.2901 | 2024-10-12 04:10:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 5b1113a0-7432-3850-86d1-8063a5f3f975 | -17.70482 | -56.29518 | 2024-10-12 04:10:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 62b512dd-b55a-3086-8151-92dcde3c2b61 | -17.70373 | -56.29083 | 2024-10-12 04:10:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 879a1b92-6fa8-3157-b138-a64b13e7d56a | -17.69867 | -56.29364 | 2024-10-12 04:10:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| f1bb3417-fb61-34c9-949d-1ef41d3877ff | -17.69643 | -56.29439 | 2024-10-12 04:10:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| deb17085-665a-3db0-a284-0b6bf9672022 | -17.67608 | -56.32689 | 2024-10-12 04:10:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 1133d35b-44da-3285-bdd8-8e1a91d7ea14 | -17.67239 | -56.32464 | 2024-10-12 04:10:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| c82fe9eb-1c9c-37a8-9fca-1175557fc519 | -17.67127 | -56.32974 | 2024-10-12 04:10:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| fa962765-6cff-3835-ae60-f474d3959084 | -17.66233 | -56.25242 | 2024-10-12 04:10:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 53f4f870-c2c3-3b39-9d4b-5bc2d76e84fc | -17.65507 | -56.25592 | 2024-10-12 04:10:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 123414e0-c54c-3bc2-bbbc-aa222936c3d8 | -17.65171 | -56.27111 | 2024-10-12 04:10:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 4dad4664-7669-37c4-ad5a-72797c5f9b41 | -17.64556 | -56.26958 | 2024-10-12 04:10:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 9a6c37d2-ca52-3f28-836d-b9cd19707f1d | -17.64548 | -56.32861 | 2024-10-12 04:10:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.0 |
| b150ec13-2a54-3b8f-a5ac-81b7b754f459 | -17.64434 | -56.33372 | 2024-10-12 04:10:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.0 |
| b29e41c2-270f-3c97-a8b4-63a5204297c5 | -17.64157 | -56.31686 | 2024-10-12 04:10:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 7867bfd2-bf91-3914-a097-bed0132ff873 | -17.64044 | -56.32194 | 2024-10-12 04:10:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.0 |
| bebdcb78-a3d0-34d5-abda-6e0b712b3e8f | -17.63931 | -56.32701 | 2024-10-12 04:10:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.0 |
| 5b7b5bc3-8103-3a4b-b9e4-b027d000578e | -17.63818 | -56.33215 | 2024-10-12 04:10:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.0 |
| 6965b5f6-7b7b-3fa2-9c97-e8c22fd49f74 | -17.63704 | -56.3373 | 2024-10-12 04:10:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.0 |
| 60df1089-bd61-34d3-bc4b-da7f6c44596c | -17.63427 | -56.3204 | 2024-10-12 04:10:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 43731479-30d8-361b-a514-f4ebaa913dc0 | -17.63314 | -56.32549 | 2024-10-12 04:10:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 45dc9186-91c9-3c4e-91d0-9f972a4e0c4f | -17.63201 | -56.3306 | 2024-10-12 04:10:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| c02e152f-bfa0-3c19-9925-0d7503c0a4f6 | -17.63086 | -56.33575 | 2024-10-12 04:10:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| b0554814-dd3c-3695-a7cd-45d53940c144 | -18.21577 | -56.45667 | 2024-10-12 04:10:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 6314bcde-4a04-3b1f-92db-928e2ab2bebb | -18.21368 | -56.41549 | 2024-10-12 04:10:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 225df3d6-c222-36d2-be4c-dc7c32fbfc63 | -18.21346 | -56.46684 | 2024-10-12 04:10:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.0 |
| e60fdbb5-bc9d-3a51-8485-e84585f02c45 | -18.21266 | -56.4131 | 2024-10-12 04:10:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 4efa48a8-9c42-336d-864a-58ed36bc294c | -18.21257 | -56.42056 | 2024-10-12 04:10:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 2e9d5444-7175-305d-8b18-c5997436f9af | -18.21231 | -56.47192 | 2024-10-12 04:10:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 9ccbf9bd-05ed-34f3-afca-6d58d9fa7181 | -18.21152 | -56.41814 | 2024-10-12 04:10:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| c857d10e-69b0-3715-90e7-cc779f537f63 | -18.21116 | -56.47701 | 2024-10-12 04:10:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.1 |
| c9c36fab-b4f5-326c-b811-641ccb234772 | -18.21 | -56.48211 | 2024-10-12 04:10:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.1 |
| b6d729c5-95a0-3ee9-a2a7-862849ffc1e9 | -18.20866 | -56.40887 | 2024-10-12 04:10:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 33a20d9f-fb2e-3058-b699-77298280bbcc | -18.20692 | -56.43837 | 2024-10-12 04:10:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 438f19f9-6f54-3f10-bd6b-10ef379048cf | -18.20641 | -56.47807 | 2024-10-12 04:10:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.0 |
| e770b26a-0d62-3989-b4be-bb61ba463c92 | -18.20578 | -56.44342 | 2024-10-12 04:10:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 30dd6a79-c44a-3125-a28f-fa31a3c3e0d2 | -18.20528 | -56.48319 | 2024-10-12 04:10:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.0 |
| ba6bd19f-7031-304c-a56d-75b0cd80aa47 | -18.205 | -56.47546 | 2024-10-12 04:10:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.1 |
| ce4da9bd-c81f-36aa-afcc-bc6c4a3d387b | -18.20457 | -56.53485 | 2024-10-12 04:10:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.6 |
| 43c534ea-a046-3ac7-abc1-ed0aa495f74c | -18.20384 | -56.48055 | 2024-10-12 04:10:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.1 |
| 45a32cf1-1d2e-3fc3-a9c2-37777a0f54c7 | -18.20268 | -56.48566 | 2024-10-12 04:10:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.4 |
| f4d84676-92eb-32cb-b706-1e5e8017a822 | -18.20153 | -56.49076 | 2024-10-12 04:10:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 106c31c5-7bdd-3cc4-b782-10134db74a97 | -18.19913 | -56.48161 | 2024-10-12 04:10:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.0 |
| 2b75eeaf-a7eb-395c-b508-a251d363ea22 | -18.198 | -56.48672 | 2024-10-12 04:10:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.7 |
| 8ad3c0b2-dbb8-3876-ada1-58dc76486b2b | -18.19768 | -56.479 | 2024-10-12 04:10:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.9 |
| 7db75c98-9719-36ac-b2a4-911f1a858bdf | -18.19652 | -56.4841 | 2024-10-12 04:10:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| fe2f4d09-6ddc-3cdb-9838-2fa0907227d8 | -18.19536 | -56.4892 | 2024-10-12 04:10:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| eb66739e-8b0f-3486-81fb-701a53b321bb | -18.19297 | -56.48003 | 2024-10-12 04:10:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 7ea7ef6d-ebe3-31a6-a193-20ba459ed4ef | -18.19037 | -56.48255 | 2024-10-12 04:10:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 28c5dd90-1c78-3f64-9a64-fb14aa8d7be2 | -18.1387 | -56.46077 | 2024-10-12 04:10:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 6841ba5b-e97b-347a-97f3-65a659f7dd3d | -18.13369 | -56.45409 | 2024-10-12 04:10:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| fe39fe07-1896-3733-a03d-c6560c713367 | -18.13305 | -56.34174 | 2024-10-12 04:10:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 836a9844-fa1e-33be-82da-3dad20f86789 | -18.1319 | -56.32417 | 2024-10-12 04:10:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 17f87095-b63c-369d-a719-2a1fd393c8d1 | -18.13146 | -56.32016 | 2024-10-12 04:10:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| bc3aa89e-3042-3696-bb96-b1f84d8e293a | -18.13033 | -56.32515 | 2024-10-12 04:10:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 0b5e6146-29cb-31ab-99c4-955539d8d1d0 | -2.8255 | -51.3194 | 2024-10-12 04:15:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 45.9 |
| 5bbb80db-412e-3954-8a44-e17ba2cb0e4c | -2.8254 | -51.3401 | 2024-10-12 04:15:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 99.2 |
| 62d5df54-28dd-3504-828c-1e14e3d2d50b | -2.807 | -51.3406 | 2024-10-12 04:15:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 51.7 |
| 7e82f112-b8d8-3b10-afae-2a37ae6de96f | -2.7885 | -51.3618 | 2024-10-12 04:15:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 95.8 |
| bdd260f4-5ba7-3ec0-8b58-dc38fd96e7bb | -2.7884 | -51.3825 | 2024-10-12 04:15:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 50.2 |
| 604e21b7-9c5f-3039-a0d2-0bd29334c749 | -2.7701 | -51.3622 | 2024-10-12 04:15:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 53.9 |
| abc50260-522d-3dba-9748-bd29c8bb1c84 | -3.6979 | -50.1015 | 2024-10-12 04:15:27 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 46.1 |
| ae5a361d-7024-3877-9651-9027665bfe90 | -3.6978 | -50.1225 | 2024-10-12 04:15:27 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 71.9 |
| 81300127-2d3a-39be-9356-6dfbd16f6b09 | -3.7845 | -51.3104 | 2024-10-12 04:15:28 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 46.0 |
| 6fe8da48-c721-3e48-8f7e-798191668af9 | -3.7844 | -51.3312 | 2024-10-12 04:15:28 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 45.9 |
| e0a9a46c-6352-378c-ab15-117208e435f8 | -3.9267 | -42.401 | 2024-10-12 04:15:28 | GOES-16 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 53.2 |
| b5d737c2-968f-3b57-af29-bc541f3e369f | -3.9265 | -42.4246 | 2024-10-12 04:15:28 | GOES-16 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 31.2 |


[Clique aqui para ver as próximas entradas](README55.md)
