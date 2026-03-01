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
| db9db25d-9ef5-35be-aefb-a301faaa8485 | 1.4682 | -59.9119 | 2026-03-01 01:40:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 55.1 |
| cc455847-f0df-3bbf-a760-0d337aebc15d | 3.4564 | -60.8158 | 2026-03-01 01:40:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 109.1 |
| 6777a223-cce6-398d-89c1-910c812d2aa9 | 3.4381 | -60.8161 | 2026-03-01 01:40:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 70.6 |
| cdc70502-657c-3afa-b146-fb01a0779fe3 | 1.4864 | -59.9308 | 2026-03-01 01:40:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 145.2 |
| 19d69270-6d56-3e7c-aa7c-42bdb0324706 | 3.4564 | -60.7968 | 2026-03-01 01:40:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 76.3 |
| d24b2a9e-10f8-35c1-ae11-74be2d5c7191 | 1.5046 | -59.9306 | 2026-03-01 01:40:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 122.8 |
| ba73ddb4-b0d5-343b-b9c0-7ef1380998ff | 1.4864 | -59.9117 | 2026-03-01 01:40:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 233.2 |
| c7acac59-96c0-35f1-a320-05d3714ca263 | 1.5047 | -59.9116 | 2026-03-01 01:40:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 167.5 |
| 353416a7-068c-3ac1-aed7-419a38a6d68d | -12.29434 | -61.96585 | 2026-03-01 01:43:00 | TERRA_M-M | ALTO ALEGRE DOS PARECIS | RONDÔNIA | Brasil | 1100379 | 11 | 33 | nan | nan | nan | Amazônia | 23.1 |
| cdcc135a-2558-39bc-8095-6067b82ecaab | 1.4864 | -59.9117 | 2026-03-01 01:50:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 186.6 |
| d4db6c90-189b-39f6-9d38-b2ced4a62b20 | 1.4864 | -59.9308 | 2026-03-01 01:50:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 148.0 |
| d5fbcea5-3fd6-356b-b225-a95998919b62 | 1.4682 | -59.9119 | 2026-03-01 01:50:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 63.1 |
| 68264f13-46c8-3344-8bec-bb92acd8235b | 3.4381 | -60.8161 | 2026-03-01 01:50:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 89.0 |
| 717e7ed9-9cfe-341e-b7e0-51d93380054e | 3.4381 | -60.7972 | 2026-03-01 01:50:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 58.0 |
| fd8d9a12-8f6b-317d-b5c2-37a914b072f7 | 1.4681 | -59.9309 | 2026-03-01 01:50:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 77.9 |
| 883c1b5f-3a2a-3352-847c-4f4fb6e75175 | 1.5047 | -59.9116 | 2026-03-01 01:50:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 165.2 |
| 3a5b261f-060a-31ac-a469-c1de31bdebcc | 3.4564 | -60.8158 | 2026-03-01 01:50:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 59.8 |
| 7648ce01-f2ad-36cb-8a2e-ae392e48df79 | 1.5046 | -59.9306 | 2026-03-01 01:50:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 121.7 |
| 9b3e04b6-68c3-3859-9d21-ea3014de18fb | 1.4681 | -59.9309 | 2026-03-01 02:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 85.3 |
| 7423666c-60c4-3954-976d-1a97ae77ff57 | 1.4864 | -59.9117 | 2026-03-01 02:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 180.5 |
| 2218c017-59c4-33d7-b372-ad64ae88df3e | 1.5046 | -59.9306 | 2026-03-01 02:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 123.5 |
| d82ac725-50c2-32a8-839d-1b37ff2fc850 | 3.4381 | -60.8161 | 2026-03-01 02:00:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 64.8 |
| d6106da7-7e31-309c-b758-734a2cc39a50 | 1.5047 | -59.9116 | 2026-03-01 02:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 164.2 |
| 9ec97db5-f253-3d34-826f-d62548dcb8d1 | 1.4864 | -59.9308 | 2026-03-01 02:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 150.8 |
| 3fb873a7-788f-38ee-bd1c-02e71e4b56ca | 3.493 | -60.7772 | 2026-03-01 02:00:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 54.2 |
| f8145d50-94a2-3300-a7cd-cc9c1b142cf9 | 1.4682 | -59.9119 | 2026-03-01 02:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 63.4 |
| 3493add7-9575-377f-ad54-e0b5926a0ee4 | 1.4681 | -59.9309 | 2026-03-01 02:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 93.5 |
| f2146e45-6295-394b-b722-d9d961ec2010 | 3.4564 | -60.8158 | 2026-03-01 02:10:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 61.4 |
| bcb3b688-5821-3cb0-ac49-47b78f366e11 | 3.4381 | -60.8161 | 2026-03-01 02:10:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 60.3 |
| 0a9c6b45-0da9-3d4e-9e53-90f8cf466161 | 1.5047 | -59.9116 | 2026-03-01 02:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 150.1 |
| 7d56dbc8-f1cb-3a8b-94ac-1344064bf20c | 1.5046 | -59.9306 | 2026-03-01 02:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 110.6 |
| 92098a38-ac08-3b50-b412-c33820922626 | 0.1914 | -60.4499 | 2026-03-01 02:10:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 45.4 |
| 13adf2c9-4fa4-322e-a1b7-bec53778c5ed | 1.4864 | -59.9308 | 2026-03-01 02:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 137.7 |
| 0e02b288-1cfd-3094-9753-db28f97556a9 | 1.4682 | -59.9119 | 2026-03-01 02:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 72.3 |
| 70f85a94-b3e9-387f-a580-cc06596d4abd | 1.4864 | -59.9117 | 2026-03-01 02:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 202.6 |
| 00e01d81-a768-36bd-9728-431274078285 | 3.4564 | -60.8158 | 2026-03-01 02:20:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 57.3 |
| 73945fd9-22d1-3764-a33f-c09efda07e57 | 1.5047 | -59.9116 | 2026-03-01 02:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 150.7 |
| b704b074-848b-3864-aee8-6cdfd4c90403 | 1.5046 | -59.9306 | 2026-03-01 02:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 123.3 |
| 4f1b0fd3-fbdb-3e26-b7c5-1432680c8259 | 0.1914 | -60.4499 | 2026-03-01 02:20:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 46.5 |
| 79e59712-e5e1-3413-804d-4bdb6a0d4e22 | 1.4864 | -59.9117 | 2026-03-01 02:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 195.1 |
| 90651561-c59a-3989-868c-1d005145e203 | 1.4682 | -59.9119 | 2026-03-01 02:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 55.8 |
| 048ca896-3f84-3942-92ac-33934da3e271 | 1.4681 | -59.9309 | 2026-03-01 02:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 100.4 |
| e8556bc7-80b8-39a5-b1ff-7acb013e8057 | 1.4864 | -59.9308 | 2026-03-01 02:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 150.0 |
| f376c949-f73e-36f4-ae5c-b9efed4c8a5e | 1.4864 | -59.9308 | 2026-03-01 02:30:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 121.8 |
| 044bafb2-ba3a-3ef3-ab57-216ef0d155c6 | 1.5047 | -59.9116 | 2026-03-01 02:30:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 177.8 |
| 3fb4e743-32da-3ad1-9121-9aaf8fc8d37b | 1.4864 | -59.9117 | 2026-03-01 02:30:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 182.0 |
| 74f5c43d-417f-32a0-bee2-6af42c212977 | 1.4681 | -59.9309 | 2026-03-01 02:30:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 97.5 |
| d5589857-c849-3c6b-8026-01c44eee63da | 1.4682 | -59.9119 | 2026-03-01 02:30:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 62.3 |
| 76338a9c-757d-35d2-a2d4-e2b5108b7725 | 1.5046 | -59.9306 | 2026-03-01 02:30:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 108.4 |
| b81cded0-3e70-3815-b375-25609c1ef0b5 | 3.4564 | -60.8158 | 2026-03-01 02:40:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 53.0 |
| 5a08f82b-cf9c-30d9-aa61-809a607c67c1 | 1.5047 | -59.9116 | 2026-03-01 02:40:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 156.0 |
| 0cda99b6-17d9-3b65-8995-bff6f65dc5fd | 1.5046 | -59.9306 | 2026-03-01 02:40:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 127.3 |
| ff6a6c57-8b33-3954-8e9f-4afe20f5f81f | 1.4681 | -59.9309 | 2026-03-01 02:40:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 85.5 |
| a9d6387e-182b-344f-84e2-dc05298746a5 | 1.4864 | -59.9117 | 2026-03-01 02:40:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 190.7 |
| c856447f-5703-35e2-aabb-4d314b2b14e3 | 1.4864 | -59.9308 | 2026-03-01 02:40:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 136.7 |
| 521bb448-1638-3863-9dbb-83eb660e8098 | 1.4864 | -59.9308 | 2026-03-01 02:50:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 115.8 |
| e64d2f5d-111d-392b-bf55-eb1bb7cb21ff | 1.4864 | -59.9117 | 2026-03-01 02:50:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 161.4 |
| 80133fd5-c390-326a-a63c-c4bfc40c57f6 | 1.5047 | -59.9116 | 2026-03-01 02:50:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 171.7 |
| df62ce9e-af99-3e41-aedc-8938c7cfa4d3 | 1.4682 | -59.9119 | 2026-03-01 02:50:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 57.6 |
| e8e8c936-e22a-3e05-9c98-ceddfafb5595 | 1.5046 | -59.9306 | 2026-03-01 02:50:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 115.6 |
| dab0152e-2992-388a-98e9-d816fb5f1af0 | 1.4681 | -59.9309 | 2026-03-01 02:50:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 85.3 |
| 16dd1a31-55dc-3493-b413-fd163117fe2a | 1.5046 | -59.9306 | 2026-03-01 03:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 136.0 |
| ce3780b3-1fc8-38ae-a3bb-7745e06ffa93 | 1.4864 | -59.9308 | 2026-03-01 03:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 136.4 |
| 1fca1b0b-bca4-32c0-ae56-b16e2a20be29 | 1.5047 | -59.9116 | 2026-03-01 03:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 138.2 |
| 25ad6ce2-8592-37ba-90ba-08b6b5c91dec | 1.4681 | -59.9309 | 2026-03-01 03:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 86.1 |
| d5272d82-5333-3714-abbc-f0e83f937043 | 1.4864 | -59.9117 | 2026-03-01 03:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 141.2 |
| e26139fb-ccda-3372-84a5-68e753621f0b | 1.4864 | -59.9308 | 2026-03-01 03:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 130.3 |
| 7ba59517-2866-32dc-9e64-780599f3a467 | 1.4864 | -59.9117 | 2026-03-01 03:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 159.0 |
| d17a62e1-5e80-3cd3-8eca-78f98ca979a1 | 1.4681 | -59.9309 | 2026-03-01 03:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 82.5 |
| 073b3cb8-2dbc-3b7f-98ce-dfa71f12e059 | 1.5047 | -59.9116 | 2026-03-01 03:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 146.8 |
| 6ab99031-1660-30f5-836d-99a7d5bf94ea | 1.5046 | -59.9306 | 2026-03-01 03:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 132.5 |
| a6efd724-8dad-38ba-a678-e86b022ee9c5 | 1.4864 | -59.9117 | 2026-03-01 03:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 134.4 |
| 212d454b-55ba-3e20-9fbc-8fa910777bcf | 1.5047 | -59.9116 | 2026-03-01 03:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 150.0 |
| bb0950a7-6321-3402-9dc4-876408eca647 | 4.2427 | -60.8186 | 2026-03-01 03:20:00 | GOES-19 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 54.7 |
| f13d2417-2a81-3675-9096-21b168bfce8f | 1.5046 | -59.9306 | 2026-03-01 03:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 142.0 |
| e435780a-87bd-343a-82a3-43ed4095b197 | 1.4864 | -59.9308 | 2026-03-01 03:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 133.4 |
| 2dcccdc7-c275-3f7a-929f-30c63907b3f7 | 1.4681 | -59.9309 | 2026-03-01 03:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 74.6 |
| f5084b1b-6d0a-3fdb-aaee-0fefbc68af99 | 1.4682 | -59.9119 | 2026-03-01 03:30:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 49.7 |
| 74687f64-aa8d-3232-a41b-09746f42d6dd | 4.2427 | -60.8186 | 2026-03-01 03:30:00 | GOES-19 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 105.1 |
| 4fcc2656-e4f3-376c-8783-885fbf3c179f | 1.4681 | -59.9309 | 2026-03-01 03:30:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 78.5 |
| 0ee4cdda-4d31-39e9-b392-7f3e73abbb33 | 1.5046 | -59.9306 | 2026-03-01 03:30:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 116.9 |
| 68702e52-3d67-3021-897f-f098f24f9d97 | 1.4864 | -59.9308 | 2026-03-01 03:30:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 117.9 |
| 1c3ce084-833a-32b8-a837-55b0c9c3b685 | 1.5047 | -59.9116 | 2026-03-01 03:30:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 177.1 |
| 677cbb36-3ede-32fc-87da-3bf179aed987 | 1.4864 | -59.9117 | 2026-03-01 03:30:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 155.8 |
| 4ffa7d92-c3ee-39a0-8bbe-63a641880f40 | 1.5047 | -59.9116 | 2026-03-01 03:40:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 164.2 |
| 9de2c2c7-df29-3bec-87b0-d51c7ec7161f | 4.2427 | -60.8186 | 2026-03-01 03:40:00 | GOES-19 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 65.6 |
| fe209a13-753f-3edc-aa68-f52cfde95b99 | 1.4864 | -59.9117 | 2026-03-01 03:40:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 161.1 |
| 4d01851e-2dbf-3ff1-81ab-7103d28677d4 | 1.5046 | -59.9306 | 2026-03-01 03:40:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 125.5 |
| 6da435db-f6b3-3043-92eb-686beec2fcaf | 1.4681 | -59.9309 | 2026-03-01 03:40:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 68.4 |
| 08ca1e6b-1101-3d6d-9fed-186f9a77f8e0 | 1.4864 | -59.9308 | 2026-03-01 03:40:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 133.4 |
| fc0a7bd6-f96c-308b-9e9d-12c608de6753 | -5.84975 | -35.68622 | 2026-03-01 03:49:00 | NOAA-21 | SANTA MARIA | RIO GRANDE DO NORTE | Brasil | 2409332 | 24 | 33 | nan | nan | nan | Caatinga | 0.5 |
| a84b18b7-8bce-3429-960f-bb86dbb82a33 | -5.80024 | -35.32578 | 2026-03-01 03:49:00 | NOAA-21 | SÃO GONÇALO DO AMARANTE | RIO GRANDE DO NORTE | Brasil | 2412005 | 24 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 13c11739-2e4f-3bfd-b000-6b2a8cc80ef5 | 1.4681 | -59.9309 | 2026-03-01 03:50:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 72.1 |
| 8d36e01d-8099-3846-bc6c-f70c1dd50db4 | 1.5047 | -59.9116 | 2026-03-01 03:50:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 164.2 |
| c71cb87c-c5d0-3e00-8c54-9d7f04be9f1a | 1.4864 | -59.9117 | 2026-03-01 03:50:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 138.8 |
| 06f29a87-a3c8-37a6-8cbe-3ed3dd25030f | 1.5046 | -59.9306 | 2026-03-01 03:50:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 127.7 |
| 7d2a0ee8-69ea-3528-bddb-8fe31f3c4249 | 1.4864 | -59.9308 | 2026-03-01 03:50:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 130.1 |
| 32953314-3a65-370d-8f27-97fb8ef33c89 | -18.98071 | -52.93262 | 2026-03-01 03:53:00 | NOAA-21 | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7eabe8ae-221a-3fed-bb98-2149417c294e | -21.41456 | -48.73533 | 2026-03-01 03:53:00 | NOAA-21 | FERNANDO PRESTES | SÃO PAULO | Brasil | 3515608 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6b9c7480-5adb-3a6c-bd3c-8ed83d0be504 | -29.60638 | -51.39684 | 2026-03-01 03:55:00 | NOAA-21 | PARECI NOVO | RIO GRANDE DO SUL | Brasil | 4314035 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |


[Clique aqui para ver as próximas entradas](README3.md)
