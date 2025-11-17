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
| e8a9cb93-3622-3a09-b49c-21ff7c7857c9 | -7.70495 | -42.95031 | 2025-11-17 05:08:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 358b36fa-45b5-3916-a5c7-da5e9ece46c3 | -3.78292 | -49.25429 | 2025-11-17 05:08:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| eb6c93fd-ede4-3689-94ee-04f43096b2a5 | -2.96449 | -53.21988 | 2025-11-17 05:08:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| df482012-73f2-34c8-8d68-d3fa5deaa868 | -3.81954 | -47.4952 | 2025-11-17 05:08:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f1af795e-cb23-30f0-a5e0-e46b3bc28557 | -5.12459 | -55.96456 | 2025-11-17 05:08:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c6811cdc-289d-35b1-ba66-6191d8720b7e | -6.32009 | -55.16563 | 2025-11-17 05:08:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 112a5a86-8015-355c-97a7-062d44b417d3 | -4.70373 | -46.31031 | 2025-11-17 05:08:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 25ffb258-7937-3403-8e0c-66ad9cdecdd7 | -4.68007 | -46.94186 | 2025-11-17 05:08:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a8a3128b-105c-374c-8fa2-2e9bdf4fc60d | -5.83925 | -48.83209 | 2025-11-17 05:08:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6d35b3ae-5ae2-390e-8cb6-319f4b5c6791 | -5.88773 | -43.97178 | 2025-11-17 05:08:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 67f50672-c4e6-341e-96ea-a5ab287173f5 | -11.13591 | -44.93368 | 2025-11-17 05:08:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 73a7fc14-7a53-38b3-840a-b682b89f3208 | -11.20484 | -46.61727 | 2025-11-17 05:08:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4ef1a15a-a93e-3ba4-a97b-bf75caa8b51e | -3.5942 | -50.71767 | 2025-11-17 05:08:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a00afc3e-c42e-3236-b306-f18e376c24d0 | -4.71872 | -46.37724 | 2025-11-17 05:08:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8227880b-fde7-358c-9b07-0cb6554a90a9 | -3.77304 | -47.74522 | 2025-11-17 05:08:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| fd5fa7f8-c527-32bc-85d3-3432063a1c5f | -3.90147 | -54.15043 | 2025-11-17 05:08:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5891b990-c2bb-3ea8-aa09-cd671cdbc1b3 | -10.65223 | -48.16449 | 2025-11-17 05:08:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 210aba05-ae03-316c-ab3a-0eb51d0bb59b | -6.1323 | -41.82174 | 2025-11-17 05:08:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 2c4857b1-c8bc-35c6-9e78-e73ef7afeafc | -5.64353 | -51.32333 | 2025-11-17 05:08:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1bd5ed96-18e3-3a6b-a956-3c97db85e170 | -8.12065 | -43.52702 | 2025-11-17 05:08:00 | NPP-375D | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bb530d41-2734-390d-8da9-dd24246e2989 | -4.95269 | -49.83469 | 2025-11-17 05:08:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 499a7a2d-89f5-3703-82b0-df89f092d6ca | -3.7449 | -51.81435 | 2025-11-17 05:08:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 46958114-4a73-301d-bd7c-5bf08f826f3b | -8.87097 | -50.18824 | 2025-11-17 05:08:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 32431c67-d3bc-347e-81aa-cbac9c40cbb0 | -3.46196 | -50.12096 | 2025-11-17 05:08:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cecee6ca-0aa2-3dc7-a3ed-b7fa4c69ded3 | -4.3904 | -49.65498 | 2025-11-17 05:08:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9c3808e2-1848-3662-92a8-c0a1842d99d0 | -3.30368 | -50.07101 | 2025-11-17 05:08:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 23eb7dcc-58c4-3b27-aff5-60d8fa7f4ac3 | -4.57392 | -50.94549 | 2025-11-17 05:08:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b7222b71-0553-3d9b-b616-f437d848e0c2 | -3.30721 | -50.07511 | 2025-11-17 05:08:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4c44959f-5eb4-3699-8908-0b887de552ce | -10.95075 | -48.70288 | 2025-11-17 05:08:00 | NPP-375D | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| f0a33490-9086-361c-a924-5a59d94fe35b | -2.8838 | -51.42649 | 2025-11-17 05:08:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f5c527c5-dc39-3e7f-a989-6405cdcc0b8e | -3.93722 | -52.18349 | 2025-11-17 05:08:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7932fbea-da9f-3079-9d82-4264df342638 | -3.24452 | -50.49982 | 2025-11-17 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2c1009f7-0180-3db6-a38d-5baa5f53885a | -10.96775 | -44.52786 | 2025-11-17 05:08:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4fac73f1-dcf9-3cef-b5a4-f5252cf688ce | -3.88988 | -46.46288 | 2025-11-17 05:08:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c7ea040f-3212-390d-aba2-053fa0f872dd | -3.83262 | -49.80841 | 2025-11-17 05:08:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 5b1f3855-4423-3f1d-a86c-d2ed49f40154 | -5.49071 | -46.91346 | 2025-11-17 05:08:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5626a286-3d10-3527-825f-8564bfdd0b40 | -8.87087 | -50.19044 | 2025-11-17 05:08:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f9ef7ace-29d7-34fe-a095-4ffd70660c40 | -3.32448 | -50.20633 | 2025-11-17 05:08:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| abeb9f21-3e73-3350-b069-218d8fe8d545 | -4.71826 | -46.38048 | 2025-11-17 05:08:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| da6108e0-f414-39c8-b17f-1b983e2dbab6 | -3.52715 | -49.10208 | 2025-11-17 05:08:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fea34c1c-29ec-33c6-a9ea-79f7a8777949 | -4.07399 | -46.19844 | 2025-11-17 05:08:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 82f36830-c587-3a72-bef8-cdbad40e3e00 | -3.40841 | -50.11986 | 2025-11-17 05:08:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cd3616c2-e4d6-32a1-94d2-63cffcfdaa93 | -3.50752 | -54.37283 | 2025-11-17 05:08:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2f9acf66-63fd-3870-98fb-54e6cba2567c | -3.48227 | -50.25601 | 2025-11-17 05:08:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9e3478ac-b261-310c-865b-fc07ee29651d | -3.24012 | -50.4958 | 2025-11-17 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| ff8726a6-f69e-3532-af72-3065cc7db652 | -8.86601 | -50.19176 | 2025-11-17 05:08:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bcf95982-f1d8-3701-b4d1-0530985b45d6 | -3.23508 | -50.50867 | 2025-11-17 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| e946c720-9368-38a0-b643-c9ab41eba001 | -7.22399 | -47.98556 | 2025-11-17 05:08:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 2690c08e-8f3f-3794-bf73-12ec5fd96a35 | -7.26035 | -48.01364 | 2025-11-17 05:08:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3aff31e9-9e82-30a0-a935-5d2775cb5902 | -5.49107 | -46.91346 | 2025-11-17 05:08:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 146e7330-9536-31ca-a402-26fd3778496f | -3.82834 | -51.19762 | 2025-11-17 05:08:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cb15153a-1ae5-3078-a398-21642723b2a7 | -6.22488 | -47.23729 | 2025-11-17 05:08:00 | NPP-375D | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f1a81362-3a42-3e66-9c94-b2c4255346ed | -9.33586 | -46.57507 | 2025-11-17 05:08:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 13edd467-dacd-33ad-80c1-d76cf1840d49 | -4.244 | -49.6813 | 2025-11-17 05:08:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| f22b6a45-b9b9-30a2-9dc6-b8b712fc89e4 | -6.35896 | -46.1553 | 2025-11-17 05:08:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ccdb70cb-3b74-3d50-9d42-ef2f4e17a2c0 | -7.83642 | -47.1919 | 2025-11-17 05:08:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 22979498-0481-35d3-8592-1dd0ab8ce8c5 | -5.83857 | -48.83667 | 2025-11-17 05:08:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 0005f54d-7c3e-3012-9ef0-8eeda619f80f | -6.91872 | -59.72412 | 2025-11-17 05:08:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0d9fe081-e6b8-368a-884b-ed7f2292fdbb | -3.8842 | -46.46516 | 2025-11-17 05:08:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 60f49ba2-781f-34d2-8d49-e468e29c6244 | -4.69352 | -46.30547 | 2025-11-17 05:08:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7ef7138c-f35d-336c-8c47-effcb9d7f4ba | -3.39846 | -50.18642 | 2025-11-17 05:08:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 503a4b7f-362d-334f-b437-b674bdf9939e | -10.55817 | -44.82483 | 2025-11-17 05:08:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d07f888a-daa7-3066-a7ab-64f91454bea3 | -3.08355 | -52.92152 | 2025-11-17 05:08:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1d865312-b01e-3730-b3ea-0e8e6f6ccbc7 | -3.88511 | -46.459 | 2025-11-17 05:08:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6af80d07-13b3-39ea-a925-9733154bb556 | -4.73919 | -46.38614 | 2025-11-17 05:08:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e443fa4e-9820-36a6-acb3-62c2cdbbdb7a | -3.85379 | -51.30867 | 2025-11-17 05:08:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 41541f62-48ff-370a-b792-9e1dd347db24 | -10.65776 | -49.37434 | 2025-11-17 05:08:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 375f68a8-768b-35b3-a6ec-e265555e38f8 | -3.18863 | -50.65228 | 2025-11-17 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 6a384836-7f82-3bba-acf1-e51ca04affd6 | -4.12415 | -47.29202 | 2025-11-17 05:08:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e4345914-a0b8-3900-b1f9-776e922d0684 | -10.84641 | -46.75543 | 2025-11-17 05:08:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 949a7e35-fa72-37ea-a6e2-dd73d14f715e | -3.24405 | -50.4964 | 2025-11-17 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b4a4d5ef-fa4d-3545-b783-632282c620cf | -3.23901 | -50.50926 | 2025-11-17 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 938090cb-e9ed-32c1-9f8e-3f60c340e5d3 | -4.40338 | -45.83165 | 2025-11-17 05:08:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| adfcd347-0ec6-32d8-b87e-e8197ca2ba67 | -3.78231 | -49.25837 | 2025-11-17 05:08:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8f414f72-2f16-34e9-a7d3-a01b2db38f88 | -6.68483 | -42.04352 | 2025-11-17 05:08:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 9.8 |
| a0653219-789c-3a5e-9dbd-390c1e6bd671 | -3.85708 | -49.1441 | 2025-11-17 05:08:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 108328bd-bb5c-30f6-9b03-dd8b7ad98629 | -3.30316 | -50.07453 | 2025-11-17 05:08:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 338cb65e-1229-3108-b473-afca8aa6905c | -7.97209 | -50.00207 | 2025-11-17 05:08:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 368d508c-1156-353a-8d26-6bcc84c67570 | -10.84689 | -46.75153 | 2025-11-17 05:08:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1540dd00-b4d5-3291-9069-db3efb5f3ea9 | -2.98777 | -54.92266 | 2025-11-17 05:08:00 | NPP-375D | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c1a4c650-0400-3fe3-924d-347c6b56760b | -9.71084 | -43.96434 | 2025-11-17 05:08:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 2d97df3c-0c9e-3837-96b4-9fce9a2d5eb9 | -4.7236 | -46.38115 | 2025-11-17 05:08:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 26e06788-3f93-3983-af0a-cdec999a9d3a | -4.99475 | -44.3643 | 2025-11-17 05:08:00 | NPP-375D | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| e247b48a-4ffc-3122-b33b-1c2ce16b578f | -10.55687 | -44.81875 | 2025-11-17 05:08:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9b214efd-2b0a-39d7-b068-07c3e8562663 | -2.93727 | -51.07404 | 2025-11-17 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 01dae693-a350-3d0e-90d4-8955aeee53cd | -10.96842 | -44.52223 | 2025-11-17 05:08:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0bc2feee-9fbc-380a-87e3-4973eda2087f | -3.22399 | -50.96656 | 2025-11-17 05:08:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bb31e23b-f6dd-3587-8187-8f3b0065c279 | -3.4744 | -54.15645 | 2025-11-17 05:08:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 69f60980-5b3f-372e-8023-e913394199f6 | -11.4098 | -43.32458 | 2025-11-17 05:08:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b61c9552-af0a-3011-9fd3-a2dafc39ae7b | -4.72313 | -46.38446 | 2025-11-17 05:08:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| bc37e9ab-97d0-3a78-b9bd-bd566506980f | -11.05839 | -45.15122 | 2025-11-17 05:08:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9b559992-3097-3c5b-ba4f-486e68fd249d | -3.85309 | -51.31321 | 2025-11-17 05:08:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2bb28491-8c58-374c-8712-bd403f96b44a | -6.00343 | -51.51304 | 2025-11-17 05:08:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9ce5e38f-33f5-3bb7-93d3-65569761030b | -3.80032 | -51.96413 | 2025-11-17 05:08:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 61da29ab-5cff-32e9-bb3a-054f6374d70e | -3.83733 | -49.80532 | 2025-11-17 05:08:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 7252a0fc-4878-3f22-9540-45fa570b1deb | -3.43803 | -52.8894 | 2025-11-17 05:08:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6654cd51-797f-3e4f-98e9-be46460949b8 | -3.233 | -50.48962 | 2025-11-17 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| abe2a798-c781-3f4a-8fe9-c78585f6507d | -4.10827 | -49.08402 | 2025-11-17 05:08:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 40413bfc-ac0b-3c95-bb58-0b2feb49a5f8 | -9.76363 | -55.62231 | 2025-11-17 05:08:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| abba315b-119e-3fe1-b3fe-339c2c8d7d3b | -4.72407 | -46.37781 | 2025-11-17 05:08:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |


[Clique aqui para ver as próximas entradas](README45.md)
