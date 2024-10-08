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

## Dados Diários - Página 101

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 14746edf-f838-36f1-b49c-05d71c14a267 | -16.49195 | -57.7374 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| e0057803-97b3-3c00-999d-116e3c6da19f | -16.49133 | -57.69891 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| d7779d36-0b6b-3de9-be65-2b1509f5c3e6 | -16.49103 | -57.72187 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.3 |
| 7e911459-d067-37e5-a92a-d4e6513154c0 | -16.49072 | -57.70264 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.5 |
| 0b02159f-079e-33c4-b282-596de4f11c30 | -16.4898 | -57.72936 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 9a882a22-ff54-3506-b142-7d2855b2f403 | -16.48919 | -57.73309 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 205a9613-e5b0-30c9-956b-c9c5ff5fbc4c | -16.38647 | -57.70045 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.4 |
| 09a00cfc-cbc6-3eb1-bf2d-c6b895e4cf5c | -16.38371 | -57.6961 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.6 |
| 0587ea90-9281-33f2-b065-1ba3597dce9e | -16.14805 | -57.59465 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 2d98a086-f6ae-3164-b5a9-d57edfd73d50 | -16.14745 | -57.59837 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 5e94e6eb-a387-32e3-b969-79613f790bba | -16.1419 | -57.58979 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 22a88e26-eb3d-3231-8d96-9b81f6a603e0 | -16.13853 | -57.58916 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| b4f3e1b9-bf33-3afa-aaa7-97c7c3661fa8 | -16.13793 | -57.59288 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 3453442a-71fe-37f4-9e13-56e7e6f9916c | -16.13516 | -57.58855 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 69363b7d-ebab-38c4-b502-67b5ea62b635 | -16.13395 | -57.59604 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| d3be1398-00c4-3fb6-bceb-fc735379e41e | -16.12317 | -57.55567 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 6a3b5fe5-80f6-370f-b65d-010f81b0ea23 | -16.11981 | -57.55503 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 9707c424-b849-3b9e-9b59-30cf4fbbba2f | -16.11644 | -57.55443 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| b2af2be9-bc51-3889-a424-5f77f9230cec | -16.11583 | -57.55819 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 6935b41a-bd1d-322f-b53d-fe3df30ea635 | -16.11493 | -57.58505 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 33188aa9-d3c8-321b-ac21-09505d3a9117 | -16.11029 | -57.54969 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 02af9ead-fb48-3924-bf4a-5cf08980152b | -16.10847 | -57.56089 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 2f099245-f5ac-315c-8629-1348dfd6db13 | -16.10509 | -57.56033 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 54aa7c81-22d3-3555-b2f8-e377262d1e34 | -16.10354 | -57.54859 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 2e6ad04f-f89e-3214-bcf3-1f0df1968252 | -16.09957 | -57.55168 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 36145c0a-852e-340f-a21e-9a693473d946 | -16.09678 | -57.54753 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e85cb520-af83-3a54-a525-bf16b3977426 | -16.09158 | -57.55814 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| caee9fa1-dc4e-35bc-ab47-d746e3ff361d | -16.09097 | -57.56189 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 261949a3-cdbb-317a-952a-28ef2ee59be3 | -16.04511 | -57.52013 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| eee822d8-b764-3e00-9bcb-5d7d2294ff7f | -16.04451 | -57.52387 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 714cc9a9-5e9c-3fe8-bf96-6167b294553b | -16.04174 | -57.51957 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 965353b1-18f2-3852-8575-7debc2c6d6aa | -16.03838 | -57.51899 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 1e23d285-24ee-3c01-a51e-f530c95d361d | -16.03622 | -57.51089 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2ae7c933-5a8b-38be-af73-c91ca15c1807 | -15.96634 | -57.47232 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ea1f8670-f7ce-390f-98a4-bda3a0edabd2 | -15.96236 | -57.47543 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d033f5ab-e609-3aac-ac42-1ea1aed9370d | -15.95961 | -57.47112 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 37638e46-36f8-35f3-9459-5b8de10a8f21 | -15.89758 | -57.48337 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a08797e1-7830-328c-a76f-3c8ed31c6c8e | -15.89264 | -57.47119 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fa72867f-d4ae-3a0a-b2e9-9e460db9b409 | -15.89204 | -57.47483 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1bf6c1aa-2fbf-31cf-84e4-5e0b67e333a0 | -15.88986 | -57.46701 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d95e5aa2-b766-39e0-b0d0-bb26bb2e3ac4 | -15.87976 | -57.46524 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 26380bd1-ca26-32e9-b053-d5438365a4cc | -15.87639 | -57.46466 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d08195f8-e13e-3b07-92a9-49730c94b0af | -15.87519 | -57.47199 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9c4f74a8-d1cb-36ea-99b0-12614fedd5d0 | -15.87395 | -57.47956 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 4c777ab8-b0dc-354d-afdf-5dc909bbfe8c | -15.87362 | -57.46044 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3fa5b909-5897-3685-a5ce-d89630aa151a | -15.87181 | -57.47146 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 85c134d3-cdfc-30ca-9573-f2182522e555 | -16.55975 | -57.72629 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 4ca28050-1697-3d7d-8e95-fbb6349688a1 | -16.55422 | -57.71761 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.3 |
| 90331f01-ff1d-3328-86ae-1e27db71cd68 | -16.55361 | -57.72134 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 71d60386-e020-39d6-ac41-a7096a773e69 | -16.5524 | -57.7288 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 5aaf89da-f5e9-3296-965d-94e1210961ab | -16.54903 | -57.72819 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.4 |
| fc776dae-4f62-3b42-9973-db2b5a2e2625 | -16.54686 | -57.72016 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 7d68aa20-ab89-3995-81a3-b231a1470123 | -16.54505 | -57.73131 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.4 |
| d583fb1e-ba5c-39aa-b6e9-9523670d4897 | -16.54444 | -57.73504 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.4 |
| 60b7639f-73ca-3235-8efe-e3bc19bfe5bb | -16.54322 | -57.74254 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.3 |
| 7ca36428-ed13-33ea-8081-e5a20f02c449 | -16.5337 | -57.73706 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| ecdb4fe2-6ee6-3a02-84b0-187ee1e847ba | -16.53309 | -57.7408 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.4 |
| ccccf6d4-1b4e-3d0b-959f-b994aa07787a | -16.53248 | -57.74451 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.4 |
| fcc8c0e5-7696-3e9b-8958-1bdcc1934934 | -16.52507 | -57.70478 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.3 |
| 55377c0c-4dc0-34dd-a3ab-b5b1693607f3 | -16.51036 | -57.70988 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| dee2c795-a2fe-3bb1-b5b6-4b39c5dc2349 | -16.49531 | -57.69579 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 2c75d4ce-165b-3f56-9722-acac4cf6d247 | -16.49501 | -57.71876 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.3 |
| b3d1b26a-d67d-3fdb-ae69-26eb703db7bc | -16.49287 | -57.71069 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.4 |
| 8932d594-fc48-3619-b8a1-cb1d4926374e | -16.49225 | -57.71442 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.4 |
| 8d6de8cc-b732-32b2-b03b-2fa2bba2bc1f | -16.49164 | -57.71814 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.3 |
| 97542fa0-efcb-3682-bc80-2ca179d66063 | -16.49134 | -57.74112 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 81b7e816-b2bf-3c5a-be95-a028d0c41ac5 | -16.49041 | -57.72562 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 913a6b53-7480-3e4b-8a4e-556ad8bee1f1 | -16.38309 | -57.69985 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 268b2631-2a49-3808-a252-28401966bd8f | -16.37972 | -57.69925 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 8e36f931-e573-3421-b90a-44f922624107 | -16.24452 | -56.63063 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| f67cccd3-f16c-3d0c-88ea-c7b39d7d7362 | -15.55067 | -56.65103 | 2024-10-08 04:59:00 | NPP-375D | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2bc3676c-4155-3505-ac40-7b92304be2cd | -15.54197 | -56.65009 | 2024-10-08 04:59:00 | NPP-375D | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d3f5f3b3-0e13-322d-b84b-6a3244fae72b | -16.16548 | -57.4229 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8acc10d8-6285-36eb-847a-7c1bc3ca4983 | -16.14527 | -57.59039 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| d68249b9-bc4e-3458-a0a2-43acca39e3be | -16.14468 | -57.59403 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| da3da6a0-4ec4-3647-98b1-8c44efa823ee | -16.14407 | -57.59776 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 3c80bd75-9f4e-3f01-a122-247e6f0986e9 | -16.1413 | -57.59347 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| d3bbd117-1aa7-3741-9c5e-773c85f6707b | -16.13526 | -57.41753 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6f4fb267-27e7-39da-9af6-85bf7132e81d | -16.1318 | -57.58793 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| c4090a3b-55af-313a-8233-89c7a49519f8 | -16.12257 | -57.55937 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 4ab92870-169a-3b0e-9a52-22680e7e0941 | -16.1204 | -57.55145 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 4b49bd56-c0b6-33e2-9382-26d9ad0872ce | -16.1192 | -57.55878 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 7245ee7d-ce62-3085-aa0e-910b773c8bc3 | -16.11703 | -57.55085 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 47832b62-7dda-3aa8-bbf8-5721eabf33c6 | -16.11553 | -57.58133 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| ab014609-b352-3cc0-a94a-5a29dfa1a0b5 | -16.11366 | -57.55026 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| c837b55e-6496-342b-ad27-92fa372db137 | -16.11184 | -57.56145 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 802ef98f-11e4-3cac-a487-0cdb8a8dc81e | -16.10016 | -57.54807 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 51544ee7-ae02-3357-bdd0-50925538a558 | -16.09988 | -57.57101 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 12b8fe16-76bf-3871-b851-52e267e52bda | -16.0965 | -57.57045 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9c4a3c56-2190-3c98-bd0e-6290632f6d29 | -16.0934 | -57.54701 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| db11b6a8-b94c-3f4f-a9d9-5893fd56eb3f | -16.0928 | -57.55068 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 5edeb908-6432-3690-9d05-b8f977cc3798 | -16.0922 | -57.55438 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 11dd0b56-bf08-3a9c-bbb3-869887fd0fcd | -16.04788 | -57.52445 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 72e40787-2139-3eb0-8b7c-4fc3eafb01dd | -16.04114 | -57.52329 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 02b8c04d-b5a3-3a51-aeae-47040e36915c | -16.03562 | -57.51462 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 618b8247-2b47-3c88-8a86-39323346a2b5 | -16.03501 | -57.51839 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ca998071-5ede-3b3c-9f2a-2b36fdd583e4 | -16.03285 | -57.51032 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 73f82229-cd35-384f-a3f8-36ea0bb765db | -15.96573 | -57.47601 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 980260ef-c94b-309b-b412-b9a5468ce083 | -15.959 | -57.47485 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d0c6aa88-e730-3f35-8499-fca2aab0f9a3 | -15.90432 | -57.48449 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |


[Clique aqui para ver as próximas entradas](README102.md)
