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

## Dados Diários - Página 36

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 46fa5056-ab72-3d23-a1a4-b63aae417248 | -6.16584 | -42.61157 | 2024-11-28 03:59:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 68ec172e-333d-3e46-bbc2-54664c7d91c9 | -6.11799 | -46.5917 | 2024-11-28 03:59:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c2ab2794-4b2d-3469-b2da-280a53e43982 | -2.96948 | -51.0028 | 2024-11-28 03:59:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 36289082-ab75-3506-81cc-174d9c7f9ba4 | -3.30512 | -50.2771 | 2024-11-28 03:59:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| ae3208ef-c99d-3333-9eb1-21ed98a810b7 | -6.70525 | -47.27225 | 2024-11-28 03:59:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2456ba23-a33b-328e-8c28-6cbf5dcff181 | -3.13339 | -50.25536 | 2024-11-28 03:59:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5ff92747-d801-3994-a46f-3ded775afeb1 | -3.28064 | -50.56284 | 2024-11-28 03:59:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| aa3a03e5-5173-39a3-9b8b-df38da7464af | -4.18157 | -48.62457 | 2024-11-28 03:59:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 10fc6230-7a45-35d6-b708-11878b6d9abb | -3.48965 | -50.08253 | 2024-11-28 03:59:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4995e1d8-749b-3656-b789-e3520e39521a | -3.35176 | -50.52033 | 2024-11-28 03:59:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d2cc304d-85e7-382a-aa47-f791f985ae51 | -6.38286 | -45.68763 | 2024-11-28 03:59:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5da52a19-8f67-3e25-b901-25ec94562ad8 | -1.32401 | -51.92742 | 2024-11-28 03:59:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1ac57e7f-9be8-3dff-9d65-86a922ad23a0 | -3.93894 | -46.7231 | 2024-11-28 03:59:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 61dceed8-4401-3a8e-8197-8d35064a7eb5 | -3.25173 | -48.89219 | 2024-11-28 03:59:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f4fdb76f-e12e-31c9-989e-ec4d3c0359e9 | -4.47335 | -46.36764 | 2024-11-28 03:59:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 87f0763a-e223-396a-981a-2d73afaf6186 | -3.49313 | -44.70517 | 2024-11-28 03:59:00 | NPP-375D | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 24f8ae0d-d51d-3454-8a00-ee32c0452e7d | -3.11778 | -53.10833 | 2024-11-28 03:59:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 29524ea1-9735-3a8f-9d12-0d7ce449d155 | -1.74721 | -52.05459 | 2024-11-28 03:59:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| a5f01758-c47b-396e-bd74-cd42ef8dface | -5.97408 | -45.37474 | 2024-11-28 03:59:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 579d4bee-ea22-31d9-9d8f-ac62c199a33d | -3.53299 | -50.19118 | 2024-11-28 03:59:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bda79301-e05c-3519-a26b-f100ee65713b | -6.93601 | -39.25565 | 2024-11-28 03:59:00 | NPP-375D | CARIRIAÇU | CEARÁ | Brasil | 2303204 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 8a51ed6d-801f-395d-be22-fd2b42ed8e2f | -4.66197 | -49.52109 | 2024-11-28 03:59:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 704d75b9-1b58-3dbf-818f-373e290017ed | -3.23841 | -50.76709 | 2024-11-28 03:59:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| d434ba84-3ae7-397e-910d-3f8bf19ca9d3 | -4.14531 | -40.75687 | 2024-11-28 03:59:00 | NPP-375D | GUARACIABA DO NORTE | CEARÁ | Brasil | 2305001 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 2acfafe5-f49f-3015-8776-396d0c9222cd | -2.85519 | -46.87041 | 2024-11-28 03:59:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 26163165-5a31-3061-b94a-a596e028db96 | -3.97246 | -46.96405 | 2024-11-28 03:59:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a132eab9-aa79-315e-adf0-a01b20804dff | -2.84805 | -46.86508 | 2024-11-28 03:59:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6966c030-b18a-3138-9192-1c638a3630a5 | -2.31339 | -51.95861 | 2024-11-28 03:59:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 112f4144-3c39-306b-b9b8-963cdc798875 | -4.65728 | -49.5225 | 2024-11-28 03:59:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7547584d-4946-39e9-a50d-c247ac81b99b | -3.08018 | -48.66795 | 2024-11-28 03:59:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 42fed09f-d040-397d-b181-7a0ef1e5d8ae | -4.08105 | -48.81627 | 2024-11-28 03:59:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b95f1065-4a83-3e67-82e3-718f3161553d | -2.53171 | -47.3252 | 2024-11-28 03:59:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 69954a88-8f4a-306c-92c0-4ace0710f53e | -3.04397 | -48.51188 | 2024-11-28 03:59:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 684d3cd2-7efa-3aec-bd5d-d3866edecd74 | -4.64248 | -41.12493 | 2024-11-28 03:59:00 | NPP-375D | PORANGA | CEARÁ | Brasil | 2311009 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| d94e807c-1b31-3231-ac1c-605a2b02275f | -6.82825 | -44.39582 | 2024-11-28 03:59:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 6dbc582a-72a5-31ac-bff6-017224aa357d | -3.27222 | -50.61098 | 2024-11-28 03:59:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 282d8afb-4e41-34f7-b64a-1cc3ebfa1259 | -9.00367 | -35.99374 | 2024-11-28 03:59:00 | NPP-375D | SÃO JOSÉ DA LAJE | ALAGOAS | Brasil | 2708303 | 27 | 33 | nan | nan | nan | Mata Atlântica | 13.5 |
| 771fad7a-d4e3-3f1b-b9f2-98f911950eaa | -3.27137 | -50.61581 | 2024-11-28 03:59:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 2135ae51-4c08-34d3-b528-e65c21373f9b | -5.8054 | -43.01057 | 2024-11-28 03:59:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 8c562096-2f11-3d90-8ced-d1b49c9903de | -5.94817 | -39.66726 | 2024-11-28 03:59:00 | NPP-375D | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 9.1 |
| 3ce12060-4f7f-3a2b-b562-1c616d2895cd | -1.87427 | -50.59855 | 2024-11-28 03:59:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 73fd0d3e-ab11-3350-8a07-297b3a7c209b | -5.82558 | -44.11203 | 2024-11-28 03:59:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 75f0934d-c5d7-3824-a823-e1dcca525ae5 | -3.83291 | -46.53529 | 2024-11-28 03:59:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d466802f-ce16-31b4-9594-15b5e8cb81ee | -2.84223 | -46.86974 | 2024-11-28 03:59:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 89253c51-d7c0-34a0-9e55-e89545ccb030 | -8.99976 | -35.99324 | 2024-11-28 03:59:00 | NPP-375D | SÃO JOSÉ DA LAJE | ALAGOAS | Brasil | 2708303 | 27 | 33 | nan | nan | nan | Mata Atlântica | 13.5 |
| fe309f89-f706-37be-9229-14e60543c494 | -2.48091 | -45.86751 | 2024-11-28 03:59:00 | NPP-375D | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f02d5624-2cb4-3660-991a-19f18a37ba56 | -3.96327 | -48.08415 | 2024-11-28 03:59:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| c5d3aad2-ccbc-3284-8763-21a2ab482fcd | -1.64911 | -52.47189 | 2024-11-28 03:59:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| eea0c201-a349-32aa-94cb-3cb6f42e7ecb | -3.59189 | -50.3629 | 2024-11-28 03:59:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 6dc5aea1-21b6-3c1a-a073-4c940643d5f1 | -3.09565 | -50.36371 | 2024-11-28 03:59:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| db958521-6c4f-3d47-8ef5-e48f627160aa | -8.13458 | -44.47013 | 2024-11-28 03:59:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c7fc5386-ec8d-3427-a569-99bd4c62b061 | -5.98147 | -45.35618 | 2024-11-28 03:59:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 8e856ae9-ac60-3d77-b536-6f8c339c1a1d | -2.8881 | -51.58799 | 2024-11-28 03:59:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| bdb2fbd8-289f-38a1-9572-13c8c74cc073 | -2.68227 | -46.27256 | 2024-11-28 03:59:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2ca2e390-388e-36b7-aeff-8c8aad9d4e8d | -5.49471 | -47.6572 | 2024-11-28 03:59:00 | NPP-375D | SÃO MIGUEL DO TOCANTINS | TOCANTINS | Brasil | 1720200 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b6140ae8-b2fb-36ed-b698-e78951d96cac | -4.77952 | -44.43023 | 2024-11-28 03:59:00 | NPP-375D | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 9312f82f-5571-30a1-8f44-169101125570 | -7.47623 | -35.30378 | 2024-11-28 03:59:00 | NPP-375D | FERREIROS | PERNAMBUCO | Brasil | 2605509 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 26fc6452-f968-3c3e-9d8f-2f0f35f88f39 | -8.07216 | -34.977 | 2024-11-28 03:59:00 | NPP-375D | RECIFE | PERNAMBUCO | Brasil | 2611606 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 3e1aab6f-8432-3afb-8670-59f1de0389da | -3.81357 | -46.59375 | 2024-11-28 03:59:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8c32fcbb-dd9e-3d43-9515-99b3820afba1 | -3.43602 | -50.02618 | 2024-11-28 03:59:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6e4db9bb-4f88-3608-be6a-d622d0afe548 | -6.37084 | -45.69116 | 2024-11-28 03:59:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 47ae2bbe-e7e1-38b8-899e-0c2f097a85ac | -3.41329 | -50.15964 | 2024-11-28 03:59:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 2a860390-6e9c-38fb-89ca-2081439d4f8e | -5.90684 | -43.41067 | 2024-11-28 03:59:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| a1c0208b-c2ae-3efd-bbb6-f2af8d3a4d14 | -2.8624 | -46.83945 | 2024-11-28 03:59:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| faa8f306-d020-3019-beaa-ce02e1b4b7b3 | -2.01154 | -46.40073 | 2024-11-28 03:59:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 29bb3afd-f290-360f-8127-f0f58616804a | -2.31251 | -51.96378 | 2024-11-28 03:59:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 9df28afd-7b89-3aef-82f7-4839baa5f3c0 | -2.80833 | -51.59126 | 2024-11-28 03:59:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 86a58d7f-a450-30ad-ab30-72dcc4ae2ad6 | -8.99936 | -35.99573 | 2024-11-28 03:59:00 | NPP-375D | SÃO JOSÉ DA LAJE | ALAGOAS | Brasil | 2708303 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 9c1e05f7-eaf7-3b54-bcc3-bacbe98dc66d | -2.8566 | -46.84409 | 2024-11-28 03:59:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e073b85a-750c-343a-8263-b0d6affd685c | -4.52189 | -45.72969 | 2024-11-28 03:59:00 | NPP-375D | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e7f76c7f-f40f-3dc7-8f7c-7ec4bbbfe32b | -4.25144 | -43.72532 | 2024-11-28 03:59:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 709b765b-46be-3275-98e1-c9a0733094b0 | -3.38094 | -50.12203 | 2024-11-28 03:59:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| af25e5d0-d81d-3d3a-b5ae-9ddf58265215 | -5.21226 | -41.27377 | 2024-11-28 03:59:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| c3386b37-60ef-39d2-b151-f735bb067ae9 | -3.96798 | -48.08806 | 2024-11-28 03:59:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 489ef9e4-70e5-35df-b8cd-0400ea91ce4c | -2.27971 | -46.37509 | 2024-11-28 03:59:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3d65c171-c941-369f-8202-34e94044a89e | -6.17944 | -42.61786 | 2024-11-28 03:59:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 6fa95bb7-68a1-318c-bd81-1cf0e7e08aca | -3.78763 | -50.12947 | 2024-11-28 03:59:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a7e6d5c5-eca7-3cd3-a22d-55581584a3e9 | -3.67322 | -45.78926 | 2024-11-28 03:59:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d2a0a87f-507d-30cd-a181-d4ee2c4db382 | -2.30534 | -47.86261 | 2024-11-28 03:59:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7b9be9b2-b196-35fb-8bbb-d1eed3113af6 | -7.03439 | -35.00499 | 2024-11-28 03:59:00 | NPP-375D | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 37000d56-f9a9-361f-a49e-f0227a9162c1 | -3.26621 | -46.44186 | 2024-11-28 03:59:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8733ddaa-7db7-35cc-a1eb-e0feb9a9d114 | -3.26395 | -45.37208 | 2024-11-28 03:59:00 | NPP-375D | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5536e937-65c6-3e40-8d21-264c20dbcd14 | -3.08179 | -49.21156 | 2024-11-28 03:59:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2f330e72-bd71-3f63-9f94-1f7e1f7e22ec | -6.49041 | -47.88999 | 2024-11-28 03:59:00 | NPP-375D | ANGICO | TOCANTINS | Brasil | 1701051 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2ee653cb-1d74-33fa-8368-471933ce8c28 | -1.33364 | -51.95564 | 2024-11-28 03:59:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c460a92a-a72c-32b8-84e8-1fe33c04ec3b | -4.77668 | -44.42247 | 2024-11-28 03:59:00 | NPP-375D | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 3e18a402-8789-3f76-b098-10bd17cc4d15 | -2.73348 | -48.89567 | 2024-11-28 03:59:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 9ea9bc53-7e6f-35f1-99b2-283f3353b00c | -2.1777 | -52.13744 | 2024-11-28 03:59:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 29dab9a9-db16-3142-b48d-898a417ca69a | -5.97472 | -45.37088 | 2024-11-28 03:59:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9c7f8409-f6d4-35ff-82e5-8051c0ad55d5 | -8.40935 | -41.92281 | 2024-11-28 03:59:00 | NPP-375D | CAPITÃO GERVÁSIO OLIVEIRA | PIAUÍ | Brasil | 2202455 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| c870443f-e6a1-35a6-ad72-e85276ed4c25 | -5.42493 | -47.91775 | 2024-11-28 03:59:00 | NPP-375D | AUGUSTINÓPOLIS | TOCANTINS | Brasil | 1702554 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 939d1849-644f-346b-997e-b387aadf274f | -3.50458 | -50.32167 | 2024-11-28 03:59:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 91f6b8fd-7aea-35ba-9433-1cb6f26fe181 | -3.24674 | -50.62228 | 2024-11-28 03:59:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 9afd78ee-bfb5-3a2b-bc75-2a992023cfa3 | -2.84101 | -46.84717 | 2024-11-28 03:59:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 05bac3ba-424d-361d-906f-9a6026fa80fa | -5.75478 | -47.90636 | 2024-11-28 03:59:00 | NPP-375D | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a4e60eef-333e-3ee6-9ac7-209ce65afd39 | -4.08901 | -46.14497 | 2024-11-28 03:59:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 6b0afbcf-1b43-39fe-993f-3d1358f5ed31 | -5.97663 | -45.35933 | 2024-11-28 03:59:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 25.4 |
| b5768f64-7f1b-327f-8bc1-3e3830ab434a | -6.60322 | -39.19674 | 2024-11-28 03:59:00 | NPP-375D | CEDRO | CEARÁ | Brasil | 2303808 | 23 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 842a014b-0637-34e1-8e47-b1e20a3b71bc | -3.31123 | -50.27805 | 2024-11-28 03:59:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 757b4a4b-e083-3df6-8886-861f7fd2d243 | -1.66551 | -52.4817 | 2024-11-28 03:59:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |


[Clique aqui para ver as próximas entradas](README37.md)
