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

## Dados Diários - Página 56

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8b4cdc39-8d05-334c-a952-5b28082a9981 | -4.62993 | -48.54492 | 2024-09-27 03:47:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 70c17122-4c9d-3735-b38a-4a8da8d8f5ab | -4.56286 | -48.00611 | 2024-09-27 03:47:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| abdac5b2-d588-3044-ab8f-2d3a8c595f1a | -4.56198 | -48.01124 | 2024-09-27 03:47:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 4c27b7e7-4050-3419-8a8a-fef60a948d13 | -4.55884 | -48.00841 | 2024-09-27 03:47:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 838754b3-3c1c-3b6b-9765-268155318d00 | -4.55654 | -48.00497 | 2024-09-27 03:47:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 56ebfa00-a3d4-3485-868a-e55c2e2ae2d3 | -4.55566 | -48.0101 | 2024-09-27 03:47:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c90f740e-50f7-3fef-a194-bb83e50f7917 | -4.24569 | -48.14878 | 2024-09-27 03:47:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8c404dc9-3f15-38cb-82c6-94bfa93113e8 | -4.19527 | -48.62778 | 2024-09-27 03:47:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| be9b8e92-93b1-3691-b712-2b395bff4f97 | -22.2257 | -48.6155 | 2024-09-27 03:47:08 | GOES-16 | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 81.6 |
| 6ea1561f-8aa8-3b4b-920b-4dfdf6d921c3 | -22.7433 | -44.8035 | 2024-09-27 03:47:10 | GOES-16 | SILVEIRAS | SÃO PAULO | Brasil | 3552007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 108.7 |
| 58fc5923-de7a-3f94-9986-14abb097e834 | -22.7442 | -44.7785 | 2024-09-27 03:47:10 | GOES-16 | SILVEIRAS | SÃO PAULO | Brasil | 3552007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 70.7 |
| 69b4264a-f688-3253-a48d-814b2b43329a | -22.901 | -44.73777 | 2024-09-27 03:49:00 | NOAA-20 | CUNHA | SÃO PAULO | Brasil | 3513603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| dd0652f4-bb3f-3f72-8d89-599cc0bc0760 | -22.90011 | -44.74264 | 2024-09-27 03:49:00 | NOAA-20 | CUNHA | SÃO PAULO | Brasil | 3513603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| 39fb26b1-1482-333e-a215-f33252b9fc35 | -16.31904 | -45.6771 | 2024-09-27 03:49:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ea9acfd8-a759-3449-94d4-e92c67eda2df | -15.91434 | -44.99731 | 2024-09-27 03:49:00 | NOAA-20 | SÃO FRANCISCO | MINAS GERAIS | Brasil | 3161106 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a7b7690b-a219-364b-ba6c-348fb065d61f | -15.75145 | -44.6492 | 2024-09-27 03:49:00 | NOAA-20 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0315a107-70e6-3176-9ac4-58f9fb6523e3 | -16.89224 | -45.33017 | 2024-09-27 03:49:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 5.4 |
| ddf60199-70d7-3ed1-bd15-56e1e8629890 | -16.88795 | -45.32928 | 2024-09-27 03:49:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 0467724a-3e9f-31e4-83e4-38ddf725a448 | -16.88367 | -45.32841 | 2024-09-27 03:49:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| a50d5081-8585-327d-83b9-7bcb12aeefef | -16.88287 | -45.33265 | 2024-09-27 03:49:00 | NOAA-20 | SANTA FÉ DE MINAS | MINAS GERAIS | Brasil | 3157609 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5dde959d-0b34-3a39-b986-ca91c7c72091 | -16.85053 | -44.35989 | 2024-09-27 03:49:00 | NOAA-20 | SÃO JOÃO DA LAGOA | MINAS GERAIS | Brasil | 3162252 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 425f14bc-63ff-37de-8d02-8bc9ed0be284 | -18.9339 | -46.30987 | 2024-09-27 03:49:00 | NOAA-20 | CARMO DO PARANAÍBA | MINAS GERAIS | Brasil | 3114303 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4fa12592-94c0-35e5-ae4e-c5b3e9d1ba43 | -20.55009 | -46.36551 | 2024-09-27 03:49:00 | NOAA-20 | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6a59f494-0de7-3169-af27-bc4390744d36 | -20.53304 | -46.36134 | 2024-09-27 03:49:00 | NOAA-20 | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 87f9cda7-73ef-324d-999b-eb163efb0b54 | -20.5322 | -46.3657 | 2024-09-27 03:49:00 | NOAA-20 | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 61d6d614-79a3-30c9-99b4-6740f8a22d39 | -20.5288 | -46.36018 | 2024-09-27 03:49:00 | NOAA-20 | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d9319bbf-707d-37ef-a9d8-367bd6000c8a | -20.52797 | -46.36449 | 2024-09-27 03:49:00 | NOAA-20 | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7e2f1e54-c0f3-3356-ada5-cfde2766eab9 | -20.50581 | -45.88972 | 2024-09-27 03:49:00 | NOAA-20 | PIUMHI | MINAS GERAIS | Brasil | 3151503 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 52d9a614-e7cd-3911-9c19-7860b378f231 | -20.50496 | -45.89416 | 2024-09-27 03:49:00 | NOAA-20 | PIUMHI | MINAS GERAIS | Brasil | 3151503 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 749047c2-54a3-3508-9a34-7871fe6a1040 | -20.4659 | -45.89438 | 2024-09-27 03:49:00 | NOAA-20 | PIUMHI | MINAS GERAIS | Brasil | 3151503 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e3183387-4a10-30c9-b59e-538407236a43 | -20.33491 | -46.39703 | 2024-09-27 03:49:00 | NOAA-20 | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3b2a74d2-c3ee-39c3-b8b9-86d6fa913354 | -20.02103 | -45.21582 | 2024-09-27 03:49:00 | NOAA-20 | SANTO ANTÔNIO DO MONTE | MINAS GERAIS | Brasil | 3160405 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 60b547b5-0f5e-3681-ac78-bb67f7346e7a | -20.02073 | -45.21585 | 2024-09-27 03:49:00 | NOAA-20 | SANTO ANTÔNIO DO MONTE | MINAS GERAIS | Brasil | 3160405 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7c203dd5-7e14-3da5-9370-f8fe7c305b0a | -20.01741 | -45.21119 | 2024-09-27 03:49:00 | NOAA-20 | SANTO ANTÔNIO DO MONTE | MINAS GERAIS | Brasil | 3160405 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8de3e59a-8409-361a-9953-a2a85995d29f | -19.89188 | -46.48046 | 2024-09-27 03:49:00 | NOAA-20 | MEDEIROS | MINAS GERAIS | Brasil | 3141306 | 31 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 29af9b20-1d83-3ded-b3c8-64d17f22c350 | -19.89121 | -46.48273 | 2024-09-27 03:49:00 | NOAA-20 | MEDEIROS | MINAS GERAIS | Brasil | 3141306 | 31 | 33 | nan | nan | nan | Cerrado | 8.0 |
| b79eb723-4220-3620-9e69-5488b90c0b7e | -19.89102 | -46.48499 | 2024-09-27 03:49:00 | NOAA-20 | MEDEIROS | MINAS GERAIS | Brasil | 3141306 | 31 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 7d8cfdab-47cc-30f4-8701-070fd9f25f72 | -19.61799 | -45.87669 | 2024-09-27 03:49:00 | NOAA-20 | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 15.0 |
| cec84d79-161f-37c6-87c6-36c06f59934f | -19.61719 | -45.88084 | 2024-09-27 03:49:00 | NOAA-20 | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 15.0 |
| a6c546e2-91b0-36a1-8bf3-5cea07a003c9 | -19.61374 | -45.87592 | 2024-09-27 03:49:00 | NOAA-20 | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 3e3d234c-56f1-3c79-9361-8f5731b33731 | -19.61294 | -45.88005 | 2024-09-27 03:49:00 | NOAA-20 | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 6.8 |
| a033efe9-7f48-3c3a-93e1-a1a722ff0fe1 | -19.61209 | -45.88448 | 2024-09-27 03:49:00 | NOAA-20 | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7053a898-fe71-3587-9ae0-af9934ca3f8b | -19.6095 | -45.87512 | 2024-09-27 03:49:00 | NOAA-20 | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 79924e29-4430-3dc4-972a-48095782e278 | -19.60869 | -45.87928 | 2024-09-27 03:49:00 | NOAA-20 | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 6.8 |
| d8ed022f-17a8-3b62-92ea-2cd4534af24a | -19.60786 | -45.88359 | 2024-09-27 03:49:00 | NOAA-20 | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9aeec0a3-c8fa-31f4-8107-ed122c797c4d | -19.58214 | -46.10861 | 2024-09-27 03:49:00 | NOAA-20 | CAMPOS ALTOS | MINAS GERAIS | Brasil | 3111507 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c605092d-5c9e-3bd7-abec-42d565432b01 | -19.5813 | -46.11293 | 2024-09-27 03:49:00 | NOAA-20 | CAMPOS ALTOS | MINAS GERAIS | Brasil | 3111507 | 31 | 33 | nan | nan | nan | Cerrado | 7.2 |
| d3898d03-958b-3092-bd97-deb63b7927b7 | -19.58047 | -46.11721 | 2024-09-27 03:49:00 | NOAA-20 | CAMPOS ALTOS | MINAS GERAIS | Brasil | 3111507 | 31 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 466daa26-a6f8-3b52-afef-297162b4658c | -19.57784 | -46.10772 | 2024-09-27 03:49:00 | NOAA-20 | SANTA ROSA DA SERRA | MINAS GERAIS | Brasil | 3159704 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| a46b8a5e-e666-3b55-a92c-2568477c5399 | -22.15949 | -45.82679 | 2024-09-27 03:49:00 | NOAA-20 | SÃO SEBASTIÃO DA BELA VISTA | MINAS GERAIS | Brasil | 3164407 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 21fd1e81-1856-3db0-b352-92eab034ee7a | -21.96361 | -45.81919 | 2024-09-27 03:49:00 | NOAA-20 | TURVOLÂNDIA | MINAS GERAIS | Brasil | 3169802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |
| 7b66abb1-a4ce-3df7-852c-76434a2e1e0b | -21.96288 | -45.82305 | 2024-09-27 03:49:00 | NOAA-20 | TURVOLÂNDIA | MINAS GERAIS | Brasil | 3169802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |
| ce531b9e-819e-307d-a308-534ad36d1dbd | -21.95956 | -45.81835 | 2024-09-27 03:49:00 | NOAA-20 | TURVOLÂNDIA | MINAS GERAIS | Brasil | 3169802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 9047486e-3683-3e27-8b8f-7969965a3c92 | -21.95884 | -45.82217 | 2024-09-27 03:49:00 | NOAA-20 | TURVOLÂNDIA | MINAS GERAIS | Brasil | 3169802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| e7cb3bcd-0e73-31b9-accb-f268725278c6 | -21.95736 | -45.82996 | 2024-09-27 03:49:00 | NOAA-20 | TURVOLÂNDIA | MINAS GERAIS | Brasil | 3169802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 9266591e-9d8e-3734-b7d2-cc3f0a893e11 | -21.95406 | -45.82517 | 2024-09-27 03:49:00 | NOAA-20 | TURVOLÂNDIA | MINAS GERAIS | Brasil | 3169802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| a12f61bf-dc52-38cd-ab24-b0ef6aac1689 | -21.95333 | -45.82903 | 2024-09-27 03:49:00 | NOAA-20 | TURVOLÂNDIA | MINAS GERAIS | Brasil | 3169802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 381d19eb-6327-375a-a27f-d92a5b8f7095 | -21.95001 | -45.82434 | 2024-09-27 03:49:00 | NOAA-20 | TURVOLÂNDIA | MINAS GERAIS | Brasil | 3169802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| eedbf934-0b30-3e9d-8971-43fda6120835 | -21.91909 | -45.80996 | 2024-09-27 03:49:00 | NOAA-20 | TURVOLÂNDIA | MINAS GERAIS | Brasil | 3169802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 46432ca9-82a5-3e8b-a13a-11cd35b040b9 | -21.87027 | -45.77954 | 2024-09-27 03:49:00 | NOAA-20 | TURVOLÂNDIA | MINAS GERAIS | Brasil | 3169802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 8e5d6ac4-0e8c-3b12-9239-5c187661b3f7 | -21.64216 | -45.52237 | 2024-09-27 03:49:00 | NOAA-20 | ELÓI MENDES | MINAS GERAIS | Brasil | 3123601 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| d568177f-3443-3fe7-ae7a-46264ce2301a | -21.61889 | -46.92492 | 2024-09-27 03:49:00 | NOAA-20 | SÃO JOSÉ DO RIO PARDO | SÃO PAULO | Brasil | 3549706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 6a068b11-415e-32c7-b4c3-8df09e495550 | -21.28467 | -46.64003 | 2024-09-27 03:49:00 | NOAA-20 | GUAXUPÉ | MINAS GERAIS | Brasil | 3128709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 341dce1d-5446-39f6-94c7-bfec646de115 | -21.28279 | -46.64113 | 2024-09-27 03:49:00 | NOAA-20 | GUAXUPÉ | MINAS GERAIS | Brasil | 3128709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| b3619243-cbde-3f3d-81c9-443cc1a4faa8 | -21.21123 | -45.78048 | 2024-09-27 03:49:00 | NOAA-20 | CAMPOS GERAIS | MINAS GERAIS | Brasil | 3111606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| d50325a2-972f-3596-8c46-4c8ad9953f30 | -22.49031 | -46.11475 | 2024-09-27 03:49:00 | NOAA-20 | ESTIVA | MINAS GERAIS | Brasil | 3124500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 95f162ec-24b8-3486-a337-4d1508397880 | -22.44868 | -46.89892 | 2024-09-27 03:49:00 | NOAA-20 | MOGI MIRIM | SÃO PAULO | Brasil | 3530805 | 35 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e9a128b4-2bdf-3b91-a770-8d1f14df3fe6 | -16.54573 | -46.92868 | 2024-09-27 03:49:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b1c44e8f-6238-3e93-ba76-c0c8bcc13bb0 | -16.54462 | -46.92966 | 2024-09-27 03:49:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e5822c04-5e10-3e81-ab75-d5679f30fb11 | -16.53411 | -46.93732 | 2024-09-27 03:49:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4f66ba31-0083-3617-b868-f1e4286f5130 | -16.53289 | -46.93847 | 2024-09-27 03:49:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9b1aad3b-dceb-3257-9ad0-3e305dfb13f8 | -16.52926 | -46.93667 | 2024-09-27 03:49:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 32c56f8b-3c88-37a0-ad9a-a1e9a1e9db3e | -16.52823 | -46.94199 | 2024-09-27 03:49:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ac9b1c04-56db-3e42-a7f8-841c59a0d97f | -16.52804 | -46.93778 | 2024-09-27 03:49:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 89f6e952-f2ad-3464-93af-3fd8b48c7cd1 | -16.49906 | -46.96379 | 2024-09-27 03:49:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b991a5ec-db14-32a2-9f68-4ef18d36f8c1 | -16.49801 | -46.9692 | 2024-09-27 03:49:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e5082575-4055-3716-b94e-9fe949f44c1f | -16.49318 | -46.96835 | 2024-09-27 03:49:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9ce348f2-9a19-3af5-a07e-bf2aecfe199c | -16.48833 | -46.96761 | 2024-09-27 03:49:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 97321b28-0377-3270-b916-dafa691cd544 | -15.81041 | -46.94307 | 2024-09-27 03:49:00 | NOAA-20 | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6de4b327-3a03-3950-aa60-20df03596025 | -17.49774 | -47.01734 | 2024-09-27 03:49:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9676ec4a-8e11-3f09-827b-0b6c80f30aa5 | -17.49756 | -47.01514 | 2024-09-27 03:49:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2bc8bc46-9051-3955-bd3d-b7d7b05d099e | -17.49658 | -47.02016 | 2024-09-27 03:49:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 561bf702-e07d-36f0-9dbd-32213b1a1480 | -17.23992 | -46.28794 | 2024-09-27 03:49:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 49264ab9-79fc-310a-b212-15a0d470f649 | -17.2354 | -46.28696 | 2024-09-27 03:49:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 636f81bd-b698-32fb-9ddc-ae105ce3effd | -16.98466 | -45.91766 | 2024-09-27 03:49:00 | NOAA-20 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 93c6943e-37db-3768-be78-5aa961ea1b4b | -16.57617 | -46.94655 | 2024-09-27 03:49:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5e521ac8-3ed8-32a9-b074-68cf4c43091d | -16.57232 | -46.94081 | 2024-09-27 03:49:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c00df55f-ac8f-3b16-ad29-146c51a21e65 | -16.57132 | -46.94589 | 2024-09-27 03:49:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d451e488-508d-35cf-90b9-f55b7861fcc3 | -19.16693 | -46.51462 | 2024-09-27 03:49:00 | NOAA-20 | RIO PARANAÍBA | MINAS GERAIS | Brasil | 3155504 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f730cfa1-3923-3db8-8671-bda341c80b3f | -18.91206 | -47.20166 | 2024-09-27 03:49:00 | NOAA-20 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a914515e-959d-355b-8384-d4f3e583c344 | -18.89594 | -47.09988 | 2024-09-27 03:49:00 | NOAA-20 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fe6b3b68-0b0e-32d4-9bc7-7606e927139e | -18.89359 | -47.10107 | 2024-09-27 03:49:00 | NOAA-20 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 72d58cc5-cab5-3958-af80-babe71411ec0 | -18.89129 | -47.099 | 2024-09-27 03:49:00 | NOAA-20 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 136fd615-efd4-3ed6-8f75-f7cf05678d85 | -18.78036 | -46.62592 | 2024-09-27 03:49:00 | NOAA-20 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| eab78ffb-9893-3e63-a27f-26ca245c62b9 | -18.60169 | -46.41552 | 2024-09-27 03:49:00 | NOAA-20 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ded183da-9ac5-3180-b1d2-3f34062f8137 | -18.5071 | -47.09469 | 2024-09-27 03:49:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 09ba02f5-f0e4-32b3-9d70-325eb0bbb427 | -18.50608 | -47.09978 | 2024-09-27 03:49:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| aa9b3202-90c5-3df6-abe1-7250e57c810c | -18.50036 | -47.1041 | 2024-09-27 03:49:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 64c33e95-3977-3492-b1af-7dd05bb7fd1b | -19.9833 | -47.15876 | 2024-09-27 03:49:00 | NOAA-20 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 29.3 |
| c5ecaef6-6dad-36d1-9670-8110f7fa43a4 | -19.98272 | -47.16048 | 2024-09-27 03:49:00 | NOAA-20 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 36.3 |


[Clique aqui para ver as próximas entradas](README57.md)
