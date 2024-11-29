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
| 3429a3ab-9070-3fd3-8ded-6abf2f2aa932 | -2.57722 | -49.99371 | 2024-11-29 00:52:00 | TERRA_M-M | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 24.3 |
| 95ac98ce-6edc-3930-b5d3-2dc63d90155c | -4.43089 | -46.57546 | 2024-11-29 00:52:00 | TERRA_M-M | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 39.8 |
| 1e31f891-759d-377b-a909-6027b2246be4 | -3.19009 | -50.30003 | 2024-11-29 00:52:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 442254f2-d0bd-3406-8811-35e15fd38e2d | -2.87762 | -46.86356 | 2024-11-29 00:52:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 18.1 |
| 4837d4dc-fa49-3de0-a54c-fd6ec9d6688c | -4.04085 | -48.32718 | 2024-11-29 00:52:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 94eaefe4-b575-3f74-86ba-bacdb3b4eb21 | 0.8738 | -50.80171 | 2024-11-29 00:52:00 | TERRA_M-M | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 44f8c805-8c26-31cc-9f13-ab01df4474a4 | -1.14331 | -48.34971 | 2024-11-29 00:52:00 | TERRA_M-M | BELÉM | PARÁ | Brasil | 1501402 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 606795fd-ba5d-38eb-9c33-53fd1f75d3fa | -4.69912 | -46.51863 | 2024-11-29 00:52:00 | TERRA_M-M | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 69b9e63d-63db-34f1-ac10-f37ab3dc39f3 | -1.89545 | -54.55504 | 2024-11-29 00:52:00 | TERRA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 778a0fdd-4905-3b71-b1cf-cc0b69ff3b5c | -1.71268 | -52.62691 | 2024-11-29 00:52:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 16.3 |
| 6572cf7d-7310-3ca7-8a4f-118c57355982 | -3.28176 | -50.54929 | 2024-11-29 00:52:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 4adcdf1d-e36d-3467-aa55-252c9b5cfc48 | -3.70914 | -47.14083 | 2024-11-29 00:52:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| b7d2533f-a5c2-3f23-ac0c-08ace9244b57 | -2.80133 | -48.6865 | 2024-11-29 00:52:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| aac465b0-8b2c-3686-9de4-531280309edf | -2.15887 | -46.52276 | 2024-11-29 00:52:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| a3585d7a-10b3-3e1d-a5e5-63cd787e2672 | -4.51264 | -48.07079 | 2024-11-29 00:52:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 25.9 |
| 597c0f48-4d1f-36c3-bb01-dcf6047bda2c | -4.11826 | -48.48112 | 2024-11-29 00:52:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 63e2c4bc-8a52-3e08-bdb3-7dbe752de8ac | -3.43827 | -45.63419 | 2024-11-29 00:52:00 | TERRA_M-M | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 140.6 |
| 3d0f8ab4-bd23-3e20-a2d8-c61669983a16 | -0.28811 | -51.79939 | 2024-11-29 00:52:00 | TERRA_M-M | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 11.0 |
| db8a0344-45eb-393a-931e-639ed2307296 | -2.61452 | -46.55713 | 2024-11-29 00:52:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| ec8f5964-1fe7-39f9-a155-a3bb54746978 | -3.23726 | -50.1784 | 2024-11-29 00:52:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| b16bc9e5-0e4d-3611-a6d4-c035ff7a23f5 | -2.60635 | -46.83346 | 2024-11-29 00:52:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 640ef7f8-2d6b-3e21-bc27-400e1d7e5489 | -1.68962 | -52.46275 | 2024-11-29 00:52:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 19.8 |
| b7842da2-b0dd-3c33-a0e2-a309e20639bd | -1.30013 | -55.74674 | 2024-11-29 00:52:00 | TERRA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 28.5 |
| 2b327d11-4f0c-33c0-af80-48803707b029 | -1.66353 | -52.5046 | 2024-11-29 00:52:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 4d92cf27-a1a7-32f4-ab48-d46d2aa7e1c5 | -3.3185 | -54.17778 | 2024-11-29 00:52:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 18.3 |
| 435a5c2a-7ce6-3df8-b53a-a63dca94c084 | -4.14712 | -48.23391 | 2024-11-29 00:52:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 870227f8-8f6c-33f6-ad5c-39ca1bdd0e45 | -1.33962 | -51.9354 | 2024-11-29 00:52:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| fe46e35c-83fc-3779-8ec2-d7a65ddd3002 | -2.80763 | -46.82145 | 2024-11-29 00:52:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| ed26ac22-f509-3e14-855a-2a16fa841542 | -3.36117 | -52.66663 | 2024-11-29 00:52:00 | TERRA_M-M | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 26.0 |
| 3b79365b-105c-35c6-8a03-5b26cf08d8b7 | -4.6407 | -47.1507 | 2024-11-29 00:52:00 | TERRA_M-M | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 5.1 |
| be941bb8-2baa-32bf-a337-7792af6c641d | -2.3062 | -51.98241 | 2024-11-29 00:52:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| e5be0e87-8414-3a1d-bb7a-14cdfc9195d5 | 0.99576 | -50.26107 | 2024-11-29 00:52:00 | TERRA_M-M | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 4.7 |
| a824cd82-5224-3f29-b03c-2293967ce45e | -1.36534 | -51.97267 | 2024-11-29 00:52:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 14.8 |
| f1fe8bb3-3a21-3702-acd1-9c3b81debfa6 | 0.93606 | -50.74965 | 2024-11-29 00:52:00 | TERRA_M-M | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 8.7 |
| bd74fd50-6281-3fd4-88b2-d1dae7d134cf | -4.49008 | -48.11588 | 2024-11-29 00:52:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 92bd57bf-6579-3d93-b800-9b49174da738 | -0.57134 | -51.7081 | 2024-11-29 00:52:00 | TERRA_M-M | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 19.1 |
| d191d5a4-35fe-33ee-bc76-a84584986525 | -2.64341 | -46.24366 | 2024-11-29 00:52:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 4.9 |
| fee4a576-9252-36e3-a088-747a3b7989a1 | -3.35724 | -46.66754 | 2024-11-29 00:52:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 5851356d-33b0-3415-a15e-6d9e02abb015 | -3.12273 | -53.27145 | 2024-11-29 00:52:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 20.0 |
| d4440c4b-0190-3f4c-8164-46fc87994d6b | -3.82929 | -46.55014 | 2024-11-29 00:52:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 8.2 |
| dda537b9-24a0-392e-9845-90aff5d123c5 | -2.85027 | -45.54113 | 2024-11-29 00:52:00 | TERRA_M-M | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 9.9 |
| b6b8023b-a17a-3513-8406-331685b8074a | -2.2686 | -53.48083 | 2024-11-29 00:52:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 17.2 |
| 0dd934cc-e11c-3cc6-9f11-467bfd676a82 | -1.23795 | -51.79554 | 2024-11-29 00:52:00 | TERRA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| d057985a-d8f8-33e1-a808-6bb0871eb442 | -2.4928 | -49.05196 | 2024-11-29 00:52:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| c5da1adc-e6a0-3acd-86ab-eec08d352b6e | -4.34049 | -45.87232 | 2024-11-29 00:52:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 0caeee63-3c54-36ea-b84d-240ed4564925 | -1.59018 | -52.27659 | 2024-11-29 00:52:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 54.4 |
| c3d4ad48-f311-3304-a3c0-cae653545e80 | -3.9662 | -48.91982 | 2024-11-29 00:52:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 31.7 |
| f4334398-c69a-3570-b059-2a472ebe88ba | -5.51008 | -46.25904 | 2024-11-29 00:52:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 17.7 |
| e284e808-3109-3201-8e3c-39984757389e | -0.61507 | -51.71828 | 2024-11-29 00:52:00 | TERRA_M-M | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 8.6 |
| f8bc04eb-4b06-34f8-98f6-18185e0d7e32 | -2.86161 | -45.5507 | 2024-11-29 00:52:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 22.0 |
| 62429879-d6f6-3efa-ba20-e7c213190eb0 | -2.62824 | -46.20462 | 2024-11-29 00:52:00 | TERRA_M-M | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 946ece88-7e41-38e6-b0c0-f409ecc39b74 | -4.30445 | -48.23537 | 2024-11-29 00:52:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 7d0a512b-0f7c-3079-a11b-70964b2844b7 | -2.19956 | -49.59241 | 2024-11-29 00:52:00 | TERRA_M-M | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| fd0ef1fb-20b6-3fde-9875-46ddde3d8bbb | -5.02458 | -45.07227 | 2024-11-29 00:52:00 | TERRA_M-M | SÃO ROBERTO | MARANHÃO | Brasil | 2111672 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 18516dda-9363-30a5-bc8b-67683dec5c45 | -1.08649 | -53.64462 | 2024-11-29 00:52:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 659c633f-eda4-3ee7-a6ef-0b605697b8d3 | -2.96154 | -45.60822 | 2024-11-29 00:52:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 17.7 |
| 152a63e1-94d7-361e-9a01-8eca507cc534 | -3.66782 | -49.89318 | 2024-11-29 00:52:00 | TERRA_M-M | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 4181904b-ff98-32ff-b1d7-d004853324a5 | -4.84712 | -41.26284 | 2024-11-29 00:52:00 | TERRA_M-M | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 64.5 |
| d356c8ff-b2e3-395c-87b4-56d1d90a6383 | -2.04593 | -47.30023 | 2024-11-29 00:52:00 | TERRA_M-M | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| cbe4de30-3b0b-3e22-a070-5f2da855028f | -3.04597 | -49.52065 | 2024-11-29 00:52:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 506e7188-6356-3855-84c3-f9b91bfe0996 | -5.03698 | -43.60764 | 2024-11-29 00:52:00 | TERRA_M-M | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 5ee3ef73-7fde-3b6d-b4e7-a45ef67e294a | -4.02062 | -46.99728 | 2024-11-29 00:52:00 | TERRA_M-M | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 8a0d76e7-e631-39e0-970d-a9b75af59a26 | -2.87494 | -46.8447 | 2024-11-29 00:52:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| e65ec72f-323a-3b76-b0c5-7d545be2671a | 0.98692 | -50.25355 | 2024-11-29 00:52:00 | TERRA_M-M | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 8.0 |
| bc196aa1-c13d-3c2b-ab05-86d10bdc6752 | -1.19796 | -53.87102 | 2024-11-29 00:52:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| b0242c81-2dba-3b04-bd11-24029ab2649a | -4.31479 | -48.17992 | 2024-11-29 00:52:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 05b7a412-5faf-33ab-a5d7-7e22a805b0f8 | -2.6972 | -52.00134 | 2024-11-29 00:52:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| a056ea48-a86b-3f6e-a7ab-c17cf3f6f6a0 | -3.32239 | -52.15296 | 2024-11-29 00:52:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 16.1 |
| 8d5b845a-a159-3cea-8542-2acfcd5fab9d | -2.30781 | -51.99426 | 2024-11-29 00:52:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 5140325c-cf52-306f-9c28-e891c6a270eb | -5.6616 | -46.81014 | 2024-11-29 00:52:00 | TERRA_M-M | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| b063defb-40b2-34f6-8839-ac04f29578bf | -3.82798 | -46.54076 | 2024-11-29 00:52:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 9.8 |
| c1acb890-6ff2-38c4-b173-e49554516826 | -4.35506 | -48.13229 | 2024-11-29 00:52:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 5538584f-2d52-38bb-a6c5-fd1b7dfada51 | -2.65996 | -48.79959 | 2024-11-29 00:52:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 5d28b058-2cd8-3405-babc-55f0e89b952d | -2.73765 | -48.89051 | 2024-11-29 00:52:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| ea9f0fc1-9e6f-3ae3-ae11-4f3ea78db8de | -2.65627 | -48.7731 | 2024-11-29 00:52:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 80b8e7ca-9d8d-3387-90ef-e71180af40ee | -3.35374 | -45.40908 | 2024-11-29 00:52:00 | TERRA_M-M | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 12.9 |
| d2960fce-142a-3f86-9345-8269ea2c61e0 | -2.58881 | -53.9849 | 2024-11-29 00:52:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 49590068-4e83-3a43-b15b-aa4627490433 | -2.8329 | -49.84434 | 2024-11-29 00:52:00 | TERRA_M-M | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 9c1edf02-aec8-3f60-af2a-8c237ade8015 | -3.50664 | -53.81598 | 2024-11-29 00:52:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 49726afb-3575-3afc-982f-df1618535e12 | -1.94513 | -52.97353 | 2024-11-29 00:52:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 49.7 |
| fbb7324a-419b-38f3-8c1e-dca0c010917c | -4.71859 | -49.50077 | 2024-11-29 00:52:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 7c0d167a-0bd5-31a0-95ea-7ddc553af4ef | -3.0207 | -45.15429 | 2024-11-29 00:52:00 | TERRA_M-M | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 0fa342e5-b8fb-37f1-8fa7-3167dc53be24 | -1.33891 | -51.41558 | 2024-11-29 00:52:00 | TERRA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 2460a4d8-81ad-3a87-8ee7-cc7fe482b536 | -4.09738 | -51.02935 | 2024-11-29 00:52:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 69b630b2-b254-347c-9f4e-7a36f31cfdce | -1.59148 | -52.26977 | 2024-11-29 00:52:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 18.5 |
| b70eb724-7d41-31cd-8599-967da1d9bc68 | -3.97895 | -46.96226 | 2024-11-29 00:52:00 | TERRA_M-M | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 16.5 |
| a166b9f7-2ee4-30ad-9416-484443afcae5 | -2.66513 | -48.77185 | 2024-11-29 00:52:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| b0872758-d45e-3a94-a461-5fdcd86a3f9a | -4.97832 | -43.91086 | 2024-11-29 00:52:00 | TERRA_M-M | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 11.9 |
| abb55c97-f3f2-33c4-8bdf-51c3f576bc59 | -2.03083 | -53.5018 | 2024-11-29 00:52:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 16.2 |
| d99e7f50-1ce2-3b65-bae1-f08d6d36bdde | -3.87194 | -48.37224 | 2024-11-29 00:52:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| b415a4c5-1254-3ad0-a207-ed740770901a | -1.71985 | -52.47763 | 2024-11-29 00:52:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 18.7 |
| 61d61c18-7c98-37fa-afe2-487e945a5ac7 | -1.555 | -52.01629 | 2024-11-29 00:52:00 | TERRA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 33683d23-6eac-36f0-b606-3a14cccd5b8c | -1.1706 | -53.67224 | 2024-11-29 00:52:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 14.6 |
| 659ad846-b648-36c9-814c-9d50b39a7d85 | -2.05671 | -46.38032 | 2024-11-29 00:52:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 5f1d13a7-2306-3849-8eda-657f5efea6f7 | -2.57178 | -51.8315 | 2024-11-29 00:52:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 15.1 |
| 2961a918-1427-35d1-9cdd-b7cb8bac27d8 | -3.09128 | -54.13004 | 2024-11-29 00:52:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 16.6 |
| a78e2d0c-53c4-33ec-9ab9-a679a818ed45 | -3.71942 | -47.14876 | 2024-11-29 00:52:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 24.8 |
| b0d33eb3-29f9-30c1-ba26-cde3d3a9540b | -2.54564 | -47.97879 | 2024-11-29 00:52:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 933bf0e9-f1ed-3ee1-8881-0c48df15f35b | -2.97133 | -45.23744 | 2024-11-29 00:52:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 23946c0d-6046-3eed-afa4-25cd08848887 | -3.79304 | -46.69112 | 2024-11-29 00:52:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 10.4 |


[Clique aqui para ver as próximas entradas](README6.md)
