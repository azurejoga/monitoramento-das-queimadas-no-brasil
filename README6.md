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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4b135e1d-f09e-3b65-b7be-6990a046a266 | 2.7377 | -60.3895 | 2024-12-11 01:10:00 | METOP-B | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 621eeca5-e5aa-3c75-9594-6fd095cb19c3 | -2.9592 | -53.0952 | 2024-12-11 01:10:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 781f46a7-56e3-3bbb-a5b8-bbb5cfceda78 | -11.1057 | -54.611401 | 2024-12-11 01:10:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 11059d29-2f19-3280-b54a-250502ab8e2b | 2.742 | -60.646198 | 2024-12-11 01:10:00 | METOP-B | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| aaa183ea-11ef-37b3-9e80-637f405670f3 | -3.0971 | -53.246101 | 2024-12-11 01:10:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ca1e4785-fb0a-3f3a-940d-90311d308758 | -12.5516 | -58.363201 | 2024-12-11 01:10:00 | METOP-B | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 0c2fa561-b95f-35a0-bde1-ab6ea591e050 | 3.2296 | -61.181702 | 2024-12-11 01:10:00 | METOP-B | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 79a19b1c-0f3d-351e-9025-ef6403022848 | -11.1127 | -54.6404 | 2024-12-11 01:10:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6e3a1e72-41df-3be8-a001-221d365bfa93 | -11.1104 | -54.630699 | 2024-12-11 01:10:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ae19e629-48ef-3aaa-b455-2a6b0e88197e | -12.5551 | -58.332901 | 2024-12-11 01:10:00 | METOP-B | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 1f96e820-3d7e-3716-bfc3-d69cac86e3fa | -17.2477 | -54.441002 | 2024-12-11 01:10:00 | METOP-B | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| f5a44247-2eb6-30be-aa5a-04dc6f93f259 | 3.2265 | -61.195599 | 2024-12-11 01:10:00 | METOP-B | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 9ad0c487-cd5c-30b4-86db-25c5902f2d97 | -17.245701 | -54.432598 | 2024-12-11 01:10:00 | METOP-B | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| f40b8996-f720-35b2-83cb-8e082ce5a2b4 | -12.55 | -58.356201 | 2024-12-11 01:10:00 | METOP-B | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| edef1801-1585-3347-b0d7-3f26814f1190 | 2.7467 | -60.624802 | 2024-12-11 01:10:00 | METOP-B | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 4ce691c1-b3ae-3b2e-a0ea-bc2cca5d5863 | 2.7581 | -60.6199 | 2024-12-11 01:10:00 | METOP-B | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 80df45ba-824f-3f2c-b06a-d43c40cc6f65 | -11.096 | -54.6138 | 2024-12-11 01:10:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 370a9115-f4e9-316a-8c2c-19f6bdba31a2 | -12.5402 | -58.358501 | 2024-12-11 01:10:00 | METOP-B | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 005dac9c-2ec8-3d0e-a8c9-5d12ec84b110 | 2.7483 | -60.617699 | 2024-12-11 01:10:00 | METOP-B | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| cdf8fc67-e409-3260-90d9-f5eb75160109 | -3.8119 | -52.366699 | 2024-12-11 01:10:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c501b1fb-8ec5-3eed-af5e-9e910cd56283 | -12.5437 | -58.328201 | 2024-12-11 01:10:00 | METOP-B | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 44d6ed11-cdda-3e60-9c1e-72229cf3a450 | -2.9494 | -53.097401 | 2024-12-11 01:10:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 979382ce-d814-338d-8d37-1a3aa16cd0ba | 2.7393 | -60.382301 | 2024-12-11 01:10:00 | METOP-B | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 87c33af7-aa5c-345a-85a4-2e57d22356e9 | -12.5567 | -58.339901 | 2024-12-11 01:10:00 | METOP-B | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 7a72fc08-fe17-3dce-8d34-5ed801eae7d1 | -18.010099 | -52.956001 | 2024-12-11 01:10:00 | METOP-B | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| f0d29a29-2e8a-355c-ad11-6ea8f3a5627a | 2.7565 | -60.626999 | 2024-12-11 01:10:00 | METOP-B | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 2d5a6a75-9587-35d9-8611-0ba6863de632 | 2.7451 | -60.631901 | 2024-12-11 01:10:00 | METOP-B | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 149e277e-52b3-38d9-aa26-905ae18b6f1b | -12.5696 | -58.3517 | 2024-12-11 01:10:00 | METOP-B | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| f6917b57-2246-3abf-8f83-e68039c1b15a | -12.5453 | -58.335201 | 2024-12-11 01:10:00 | METOP-B | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 5c0ef58d-1bc9-334d-b982-31454154bbc2 | -12.5469 | -58.342201 | 2024-12-11 01:10:00 | METOP-B | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| dac679af-a3a7-3840-be5e-172b6a52d661 | -18.014799 | -52.9757 | 2024-12-11 01:10:00 | METOP-B | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 3b549c6f-058c-35d0-b41d-2401c44b6b4c | 2.7435 | -60.639 | 2024-12-11 01:10:00 | METOP-B | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 7e11ac81-bc82-3bc7-96e7-d18680b6af8a | -15.9722 | -57.1609 | 2024-12-11 01:10:00 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| dc9ebcb6-7824-3577-91f5-5a480128a994 | -3.8022 | -52.368999 | 2024-12-11 01:10:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 79ff7514-877b-3bc2-baa1-6d656a400f81 | -3.1032 | -53.228199 | 2024-12-11 01:10:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ef97854a-c2c3-3694-8abe-23ffa61bd7d8 | -12.5598 | -58.353901 | 2024-12-11 01:10:00 | METOP-B | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| ac5e139b-5b9a-3d57-af32-042c96f216d5 | -12.568 | -58.3447 | 2024-12-11 01:10:00 | METOP-B | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 42d82b3d-c053-39ac-bb4e-fd5d5f6bb456 | -11.1109 | -54.6204 | 2024-12-11 01:20:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 62.9 |
| e90f3ec7-9632-3477-b8c0-89bd16bb188a | -6.9594 | -42.9759 | 2024-12-11 01:20:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 113.9 |
| cd1553c6-230b-3981-8c23-63e6ee4dfa12 | -6.8972 | -43.4969 | 2024-12-11 01:20:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 375.7 |
| d52a2648-f1fa-30ec-b64b-573a4e0351b3 | 2.7444 | -60.657 | 2024-12-11 01:20:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 69.3 |
| 34aaf8d6-8752-33c0-995d-ba6632ac5594 | -11.1295 | -54.6391 | 2024-12-11 01:20:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 77.5 |
| fac064f3-4695-3da4-911d-31c665644869 | -6.9592 | -42.9994 | 2024-12-11 01:20:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 202.3 |
| 7a37e235-b8a3-348f-aa2c-e5f779bfc798 | -11.1106 | -54.6408 | 2024-12-11 01:20:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 95.0 |
| 044d91f6-7a4f-3599-b9fd-e9b8d6eabfe8 | -6.1366 | -42.5544 | 2024-12-11 01:20:00 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 82.0 |
| a8e455a7-1c37-3bba-850b-848ec085e05e | -6.1368 | -42.5307 | 2024-12-11 01:20:00 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 110.6 |
| 7c86b249-7d53-3d06-a052-935e3a80a9a1 | 2.7627 | -60.6378 | 2024-12-11 01:20:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 122.1 |
| bb4f2bdf-3b2e-3f29-a5b4-f823c52c2354 | -6.9783 | -42.9741 | 2024-12-11 01:20:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 100.8 |
| 46a08a81-e3a8-36e6-9d8f-3585d2ce7f75 | -6.897 | -43.5202 | 2024-12-11 01:20:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 392.6 |
| a7996b42-db07-382f-a058-e04f1f730900 | -3.8165 | -52.3813 | 2024-12-11 01:20:00 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 81.4 |
| 103109f8-8335-3735-a541-5e76f2263aca | -6.978 | -42.9977 | 2024-12-11 01:20:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 166.9 |
| db2856be-8e06-390c-931f-fc03530711dc | 3.2362 | -61.1982 | 2024-12-11 01:20:00 | GOES-16 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 62.7 |
| 55d08377-8c98-35b9-95c8-ad7fdcafec55 | 2.7444 | -60.6381 | 2024-12-11 01:20:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 143.4 |
| cba3de1d-6af4-3dd1-bd12-b5e756c7ad45 | -6.118 | -42.5323 | 2024-12-11 01:20:00 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 162.1 |
| 0809e97c-e320-3c2d-a2f8-ce4efa76cbec | -6.1178 | -42.5559 | 2024-12-11 01:20:00 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 111.1 |
| 6b170bc7-b7f3-3729-bd2c-d96adaf872cf | -6.9158 | -43.5185 | 2024-12-11 01:20:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 207.3 |
| 8e61a0b6-4c53-30b8-8444-462a9869ddc1 | -2.8196 | -53.0629 | 2024-12-11 01:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 76.3 |
| f8341c48-3740-3d15-b20e-5ffd7f19faaf | -18.0062 | -52.9861 | 2024-12-11 01:20:00 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 80.4 |
| c19ac44e-41c1-3f99-af92-48b0f3fd35ff | -2.9666 | -53.1201 | 2024-12-11 01:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 79.1 |
| 50f5fcef-ac53-3910-a38d-109808127546 | -6.9161 | -43.4952 | 2024-12-11 01:20:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 202.5 |
| 7487d40e-d689-3946-a8c8-ef9bf70dc5ec | -18.0261 | -52.9829 | 2024-12-11 01:20:00 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 73.2 |
| d75c4afd-62ab-334f-a804-d230443c12b0 | -3.2351 | -42.4353 | 2024-12-11 01:20:00 | GOES-16 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 47.2 |
| 2ac854ce-eccc-3bf6-80c3-2e72ad18daee | -6.1366 | -42.5544 | 2024-12-11 01:30:00 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 92.5 |
| 2adc5c2a-5bf4-34ac-a3e7-bc8cfa108d99 | -6.9158 | -43.5185 | 2024-12-11 01:30:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 243.8 |
| f0862daa-4b91-3764-b22d-99a640d614b5 | -18.0261 | -52.9829 | 2024-12-11 01:30:00 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 94.8 |
| 40f916a2-f8c1-30a1-bd55-1693cde4443d | -6.9592 | -42.9994 | 2024-12-11 01:30:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 216.1 |
| 77610edd-39b2-39e3-a2ba-c0bdaa1eebfe | 2.7444 | -60.6381 | 2024-12-11 01:30:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 141.5 |
| 0eac6f9d-d992-31a4-bf1d-6156d1169172 | -6.1368 | -42.5307 | 2024-12-11 01:30:00 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 122.2 |
| c408a389-b16d-3e6a-beea-a85b0edc8114 | -11.1106 | -54.6408 | 2024-12-11 01:30:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 103.2 |
| ea5b43f3-e559-3990-89c0-89e7bbc7c31f | -11.1295 | -54.6391 | 2024-12-11 01:30:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 72.1 |
| 950494a5-02ec-3976-a1ea-192e1ed7b2c0 | -6.9783 | -42.9741 | 2024-12-11 01:30:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 91.8 |
| ffe940fc-ab8d-3d9d-b527-7a16ffbf7b05 | -3.8165 | -52.3813 | 2024-12-11 01:30:00 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 89.0 |
| 4becedbc-c283-3cad-bbd0-d66241670099 | -3.2351 | -42.4353 | 2024-12-11 01:30:00 | GOES-16 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 76.1 |
| 55369183-d95b-30be-8643-3af180e520ee | -6.1178 | -42.5559 | 2024-12-11 01:30:00 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 99.5 |
| b0be82a2-d80b-390f-9496-6305aa5409ae | -6.118 | -42.5323 | 2024-12-11 01:30:00 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 133.5 |
| 8a51382a-1061-324d-b592-00e36fd22e9d | -6.8972 | -43.4969 | 2024-12-11 01:30:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 265.3 |
| c31b720e-db59-3fb9-b13e-242768dac5bf | -6.9594 | -42.9759 | 2024-12-11 01:30:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 99.3 |
| 5ba9aa7b-936e-30ca-bad5-9fcd83853f73 | 2.7627 | -60.6378 | 2024-12-11 01:30:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 101.8 |
| f807cabc-54ca-3fb0-88db-4dd4b1cc3a3d | -6.978 | -42.9977 | 2024-12-11 01:30:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 187.8 |
| 883978cf-d5ed-3a11-b2e9-9381edf8d7d3 | -2.9666 | -53.1201 | 2024-12-11 01:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 76.3 |
| 80e46772-80d1-382f-bfe9-ab563506ee37 | -18.0062 | -52.9861 | 2024-12-11 01:30:00 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 80.2 |
| 1c8d9a83-1273-303a-a82a-0f86c3301f01 | -6.9161 | -43.4952 | 2024-12-11 01:30:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 189.3 |
| 1f95d080-aee9-38e6-811f-0e10cf97cd94 | 2.7444 | -60.657 | 2024-12-11 01:30:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 80.5 |
| 82659c4c-f721-39f4-bdfc-968b369d297c | -6.897 | -43.5202 | 2024-12-11 01:30:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 344.3 |
| 898a2a74-8b24-3f17-9a6c-5dc89709b360 | -2.8196 | -53.0629 | 2024-12-11 01:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 71.1 |
| 1f557faf-382e-361b-bdef-2c8b2818bd71 | -6.9158 | -43.5185 | 2024-12-11 01:40:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 179.3 |
| 081ed47c-e2d0-3019-8830-4e83d0ad2ad0 | -6.897 | -43.5202 | 2024-12-11 01:40:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 350.7 |
| 5b219a38-c6c4-351f-a6c8-6773cb3f1261 | -6.118 | -42.5323 | 2024-12-11 01:40:00 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 148.6 |
| de1041f0-3445-3dce-b251-9acca00d8ad1 | 2.7444 | -60.6381 | 2024-12-11 01:40:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 126.0 |
| cf9aeee2-3808-3ddc-85c0-949a878af027 | -6.9594 | -42.9759 | 2024-12-11 01:40:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 101.7 |
| 2ad09a5d-2212-3568-9dbb-07b542201969 | -6.1178 | -42.5559 | 2024-12-11 01:40:00 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 116.2 |
| 8bd1f2f1-8fb6-35be-b022-2047b5ea760b | -6.8972 | -43.4969 | 2024-12-11 01:40:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 301.5 |
| e35e83b3-7335-36d6-8636-e25d91e5326f | -18.0261 | -52.9829 | 2024-12-11 01:40:00 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 81.9 |
| 2876d8b2-3811-31f0-81e5-2aaa959a43b3 | -2.8196 | -53.0629 | 2024-12-11 01:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 74.9 |
| bb21a9ee-ecd0-39dd-af93-fbc299f4bc9b | 2.7444 | -60.657 | 2024-12-11 01:40:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 76.2 |
| cac014eb-3744-37ed-9e17-aaf8c481cfbf | -3.8165 | -52.3813 | 2024-12-11 01:40:00 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 93.8 |
| 98c181f5-5978-3d3a-909b-1d2ef5129b4c | -6.1366 | -42.5544 | 2024-12-11 01:40:00 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 80.9 |
| 849c2593-f431-36d6-adaf-4ed8a4ac1c83 | -2.9666 | -53.1201 | 2024-12-11 01:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 73.2 |
| 1de43503-aeb6-3152-b9c5-ea62ccbdd226 | -6.9592 | -42.9994 | 2024-12-11 01:40:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 200.3 |
| a5183511-61e4-3909-bdca-da36d515f14b | -18.0062 | -52.9861 | 2024-12-11 01:40:00 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 80.7 |


[Clique aqui para ver as próximas entradas](README7.md)
