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
| 047fb554-f2fb-35ba-bfd9-5b31ba54328e | -13.3243 | -61.6709 | 2026-09-11 01:30:00 | GOES-19 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 171.1 |
| af026814-bf2a-3229-9406-41274aced7c3 | -10.7772 | -45.9372 | 2026-09-11 01:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 194.6 |
| 6eb96b49-4717-385f-9f46-3b5c79047200 | -2.7331 | -57.6271 | 2026-09-11 01:30:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 57.2 |
| 175e10b7-ddc4-3fd5-87ee-b3e4a430d345 | -2.7332 | -57.6077 | 2026-09-11 01:30:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 42.9 |
| e37f9b81-6d70-318d-b79e-d1f46f8bb5d0 | -13.3245 | -61.6514 | 2026-09-11 01:30:00 | GOES-19 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 97.1 |
| 9f5ed382-4f46-3857-94f8-aa7de2d0ab29 | -9.068 | -61.0296 | 2026-09-11 01:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 55.3 |
| 74a82667-d165-3108-bb83-d5bc27dbcfc7 | -2.7148 | -57.6274 | 2026-09-11 01:30:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 46.8 |
| 327390bc-c038-3a28-9326-29fd9dc0fe13 | -4.2953 | -49.1021 | 2026-09-11 01:30:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 69.5 |
| 0cb310df-503a-3b1b-92e8-d1ca2d5c713d | -19.8023 | -58.0593 | 2026-09-11 01:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 44.5 |
| c6a70f93-3966-33b1-aef3-30d2c2266147 | -10.7963 | -45.9348 | 2026-09-11 01:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 96.6 |
| eedaddf4-9245-30ac-a882-120ea73e6e4b | -9.1984 | -68.2189 | 2026-09-11 01:30:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 82.2 |
| e1ef7c8b-8f5d-3b53-a6de-46e8e88e63e1 | -4.3587 | -47.7853 | 2026-09-11 01:30:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 74.2 |
| 4ac8f223-378c-3284-9397-ca9b2e5224c3 | -9.18 | -68.2009 | 2026-09-11 01:30:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 86.5 |
| b62c0391-131d-38e4-81fb-6f8f54053c92 | -10.7769 | -45.96 | 2026-09-11 01:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 117.4 |
| 42eb6d88-78a0-37a2-8462-4e06bb933059 | -9.1985 | -68.2004 | 2026-09-11 01:30:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 74.8 |
| d5044af6-59a1-3500-89e8-e09a38bd5e82 | -13.3435 | -61.6501 | 2026-09-11 01:30:00 | GOES-19 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 138.2 |
| 24088004-92ff-31af-9cbc-3f13c4d28480 | -9.5908 | -40.3696 | 2026-09-11 01:30:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 118.1 |
| d5381156-620c-3172-8955-2c8d63ab441f | -13.249 | -61.5983 | 2026-09-11 01:30:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 80.1 |
| bf0a661f-ac2b-3683-85ab-8c261e1ff8a8 | -9.1799 | -68.2194 | 2026-09-11 01:30:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 96.9 |
| 89b8bc29-0134-384e-965f-a73d10de3a1e | -4.3587 | -47.7853 | 2026-09-11 01:40:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 52.9 |
| ca7cde24-d20e-35a8-8b8d-e72cf9846471 | -9.043 | -65.4175 | 2026-09-11 01:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 62.4 |
| d98de89f-4230-3649-981a-d28be944a994 | -13.3245 | -61.6514 | 2026-09-11 01:40:00 | GOES-19 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 101.6 |
| 4873f0ae-fb77-300d-ba6b-4a676b5a8230 | -13.3433 | -61.6696 | 2026-09-11 01:40:00 | GOES-19 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 207.3 |
| 04f548ea-c201-3681-87c9-4c37eda3fd38 | -9.1985 | -68.2004 | 2026-09-11 01:40:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 92.2 |
| 8ae9b736-a18c-3242-a09a-93e74f8c9277 | -9.1799 | -68.2194 | 2026-09-11 01:40:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 82.2 |
| 4d78231f-41b4-3453-af8c-592d60e4f9de | -10.7772 | -45.9372 | 2026-09-11 01:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 91.8 |
| 283cc764-1fca-35c1-b1b0-3636f9df4e06 | -2.7331 | -57.6271 | 2026-09-11 01:40:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 63.0 |
| 1edd4206-c580-3495-9c4d-a3bc1957f759 | -9.0866 | -61.0287 | 2026-09-11 01:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 52.2 |
| 76114c03-26b5-3999-82ee-262026c5419a | -10.7963 | -45.9348 | 2026-09-11 01:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 64.4 |
| d3e5b666-d038-373c-a94d-3171d662efc8 | -13.3435 | -61.6501 | 2026-09-11 01:40:00 | GOES-19 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 157.2 |
| a6edc3eb-2c10-3345-8e52-a13bd42c7e73 | -8.6311 | -66.5101 | 2026-09-11 01:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 59.1 |
| 11c74a99-468f-3ff5-b30d-4aaf707c80e5 | -13.3243 | -61.6709 | 2026-09-11 01:40:00 | GOES-19 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 210.8 |
| cd5d47e6-8db9-3ed3-b038-8aab4ef2d242 | -9.0244 | -65.4181 | 2026-09-11 01:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 58.8 |
| 770a95a5-839d-324f-8f2a-6de5b76b8f9a | -9.1984 | -68.2189 | 2026-09-11 01:40:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 84.8 |
| da5db03b-df73-39a1-9938-a1dd16418ccf | -10.7769 | -45.96 | 2026-09-11 01:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 80.3 |
| d326efc1-e916-3a73-aeb4-45e6f4767084 | -9.068 | -61.0296 | 2026-09-11 01:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 64.6 |
| faaffcf6-5d42-30de-a105-2c4a4a3d096a | -10.7959 | -45.9575 | 2026-09-11 01:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 57.6 |
| 99cd0d44-a9f8-393d-b7b4-542512ba105e | -14.6026 | -48.8601 | 2026-09-11 01:40:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 85.2 |
| 24ca485d-7f6c-3469-b093-f411699703f2 | -2.7148 | -57.6274 | 2026-09-11 01:40:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 51.1 |
| d7e2b137-b262-3491-953b-94f9f763db53 | -2.7332 | -57.6077 | 2026-09-11 01:40:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 40.1 |
| ff8bd651-36f0-3ec6-ab50-f27174bef6f4 | -9.18 | -68.2009 | 2026-09-11 01:40:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 88.4 |
| ad071ba5-23c4-3ca6-8417-6dc0ed8ef580 | -9.1784 | -68.206802 | 2026-09-11 01:47:00 | METOP-C | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a5b750b8-e572-33cc-8133-3c4925ce5ce2 | -9.0869 | -61.026299 | 2026-09-11 01:47:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ce35d5e6-e259-3057-bfbe-789bd555ec91 | -9.0771 | -61.028702 | 2026-09-11 01:47:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ba3eaab7-8a4b-3e13-a666-263c30fc7fa4 | -8.9815 | -65.3899 | 2026-09-11 01:47:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 053ef1b8-9b12-3bad-a981-66549e3cac85 | -8.6055 | -67.196701 | 2026-09-11 01:47:00 | METOP-C | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b2bf3091-df88-3544-8098-7da0b31669cf | -9.0352 | -65.399498 | 2026-09-11 01:47:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 9c431c13-1319-3880-931e-affa90fe423e | -8.6508 | -69.787102 | 2026-09-11 01:47:00 | METOP-C | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 8b910331-21d3-3bcf-b80f-1415611beb94 | -9.1766 | -68.1987 | 2026-09-11 01:47:00 | METOP-C | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d646e482-b433-3776-b2d7-0c7d334a8eb9 | -13.2456 | -61.604301 | 2026-09-11 01:47:00 | METOP-C | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 916aa13d-b897-35c8-9672-f59ea1194663 | -9.7154 | -64.539001 | 2026-09-11 01:47:00 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| bbb269f1-eaa7-38af-a024-f2555fe0c026 | -13.2182 | -61.837898 | 2026-09-11 01:47:00 | METOP-C | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 83a21f76-5623-3c06-8f7b-b3494d5de164 | -9.1064 | -67.692703 | 2026-09-11 01:47:00 | METOP-C | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| fa6649b9-d3ca-3e79-83b6-ec4aadd67a72 | -9.19 | -68.212799 | 2026-09-11 01:47:00 | METOP-C | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 0ee8307a-ba33-35c0-893a-1d2986489cfb | -12.1493 | -64.131302 | 2026-09-11 01:47:00 | METOP-C | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 4b5cc2da-36e4-3172-ad96-e0596bfece0f | -9.0768 | -65.4916 | 2026-09-11 01:47:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 89ebfca6-3079-3b6b-9d47-90ee5ef25bb3 | -9.1418 | -67.806702 | 2026-09-11 01:47:00 | METOP-C | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8afe2731-2643-34cf-adc0-39a7c2ee14bb | -13.3311 | -61.659599 | 2026-09-11 01:47:00 | METOP-C | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 05137d3f-a51a-3443-a998-180c06397ded | -13.339 | -61.6492 | 2026-09-11 01:47:00 | METOP-C | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| dc7c6d87-4080-3027-9101-6ab18c16aa41 | -13.3195 | -61.653999 | 2026-09-11 01:47:00 | METOP-C | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 9e6b58bb-7d90-3faf-bd99-e09873d14cc9 | -13.2163 | -61.830002 | 2026-09-11 01:47:00 | METOP-C | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 91e14027-1bc6-34c4-8d00-2700c964ef18 | -13.333 | -61.6675 | 2026-09-11 01:47:00 | METOP-C | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 6002791d-cf62-374f-b0b5-6619d9e3dee6 | -8.6357 | -66.504097 | 2026-09-11 01:47:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 384c29b8-4579-3e56-a793-0ee616940a5c | -9.0269 | -65.4086 | 2026-09-11 01:47:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 046b0e0d-a6db-3fa5-887d-a475482e3b1d | -13.3214 | -61.661999 | 2026-09-11 01:47:00 | METOP-C | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 128dc57f-f054-37ae-b8ac-8ebff71c72e8 | -9.0794 | -61.0382 | 2026-09-11 01:47:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7ac07438-01ef-339b-bc8e-42d125278ccb | -7.4025 | -64.575897 | 2026-09-11 01:47:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e834d339-e3ce-3115-aa8c-2020e284f8e4 | -8.5387 | -66.989998 | 2026-09-11 01:47:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 4bca6877-f48a-3e57-91e2-3bd5115e3c3a | -9.3993 | -65.869698 | 2026-09-11 01:47:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 57a20489-8fae-3fbb-bf46-3cec742a03b1 | -9.7551 | -64.938301 | 2026-09-11 01:47:00 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 0c44869b-e1e5-3e36-bbbf-91e58307f62b | -13.3232 | -61.669899 | 2026-09-11 01:47:00 | METOP-C | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 2fee7186-ad99-3d95-8087-4e0b4d2ffb2c | -9.7566 | -64.945198 | 2026-09-11 01:47:00 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 7e6abf16-71f0-38f0-9b61-da51278ab222 | -8.8258 | -63.813702 | 2026-09-11 01:47:00 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 93c374b1-36a2-33bd-b5c8-8fc2f18a1986 | -13.2945 | -61.811001 | 2026-09-11 01:47:00 | METOP-C | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| f7c0c01a-cf2a-3ffb-a497-46180a8d4a75 | -9.0383 | -65.4133 | 2026-09-11 01:47:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 979c4637-b4ca-342b-85f7-31295f65fa5c | -9.182 | -68.223 | 2026-09-11 01:47:00 | METOP-C | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 35d91f12-2755-3ed2-9ab9-ed26a6d8ca13 | -13.2475 | -61.612301 | 2026-09-11 01:47:00 | METOP-C | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| f99f9cca-7c84-3fbd-a4d7-01be190f0b4b | -13.222 | -61.635502 | 2026-09-11 01:47:00 | METOP-C | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 0a5754b3-0209-3e9a-8bdc-044e20a1c900 | -13.2963 | -61.818901 | 2026-09-11 01:47:00 | METOP-C | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 78b2143d-3629-37ad-8bf0-8bda0783b354 | -10.2881 | -67.272003 | 2026-09-11 01:47:00 | METOP-C | PLÁCIDO DE CASTRO | ACRE | Brasil | 1200385 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 072f9fed-0be5-3dbd-b7ca-0c8b1fad347a | -9.4174 | -65.858299 | 2026-09-11 01:47:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 7ad71c11-2c5b-3475-ad0b-ddad57d51676 | -13.3292 | -61.6516 | 2026-09-11 01:47:00 | METOP-C | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 51d1dafd-edd4-3275-aaf3-a9be0d11f33b | -9.0748 | -61.019199 | 2026-09-11 01:47:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 28d33f38-851d-3d21-ba9d-040360dd3658 | -9.3962 | -65.855797 | 2026-09-11 01:47:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e3b87bc4-8a8c-3723-b07d-2d5390bcd082 | -8.5371 | -66.982803 | 2026-09-11 01:47:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 84daec46-902f-3459-8d0f-62bc54560e58 | -9.0156 | -65.4039 | 2026-09-11 01:47:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2d6c78f9-2f6f-3da1-940c-0f3855d663a4 | -9.5028 | -66.7911 | 2026-09-11 01:47:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d89f3a72-84f5-3ff9-b220-4ccc1aa74657 | -8.6389 | -66.518204 | 2026-09-11 01:47:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a5d0a06e-a960-3756-92ee-4680aa7e3374 | -12.1525 | -64.145302 | 2026-09-11 01:47:00 | METOP-C | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| a5d04f51-d852-3d6b-a2fb-f277d58a4c0e | -9.0964 | -65.487099 | 2026-09-11 01:47:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8fd6680d-cbd0-3329-867f-dba9404ff752 | -20.4918 | -57.455299 | 2026-09-11 01:47:00 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| b7c8fcf2-0db7-38d9-9fc9-f70592c97057 | -8.8241 | -63.806499 | 2026-09-11 01:47:00 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| a17f44af-eaa2-387d-a5d4-b95dbc345b50 | -8.983 | -65.396797 | 2026-09-11 01:47:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 5758a999-203c-305c-ab86-34f9bc2feb15 | -13.3507 | -61.6548 | 2026-09-11 01:47:00 | METOP-C | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 955d8440-04f2-39a0-890a-84bcc17a9d05 | -13.2201 | -61.627499 | 2026-09-11 01:47:00 | METOP-C | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| ca3d0515-c199-3e57-9117-4642a1e41a8e | -22.273899 | -55.8437 | 2026-09-11 01:47:00 | METOP-C | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 0839ec88-9801-383f-99d9-61c392ec8518 | -11.415 | -62.1231 | 2026-09-11 01:47:00 | METOP-C | NOVA BRASILÂNDIA D'OESTE | RONDÔNIA | Brasil | 1100148 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 93fa99ae-6482-3d06-88aa-4463ca1af50b | -8.9877 | -65.417503 | 2026-09-11 01:47:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 26e94301-157c-3f5f-b83b-208992df3ca8 | -13.3116 | -61.664398 | 2026-09-11 01:47:00 | METOP-C | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 53b85505-f302-35c8-906d-fa6f9cb80e56 | -9.1918 | -68.220901 | 2026-09-11 01:47:00 | METOP-C | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README6.md)
