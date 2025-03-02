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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a3924588-0742-3df0-984b-3a5ba94f20bb | -9.4986 | -40.86503 | 2025-03-02 04:14:00 | NOAA-21 | SOBRADINHO | BAHIA | Brasil | 2930774 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 4dedc37e-4550-38fb-b2e0-9bf95512b1cf | -10.52533 | -42.4407 | 2025-03-02 04:14:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 10e63576-e43b-361d-b056-3c70f1e2605e | -10.52588 | -42.43699 | 2025-03-02 04:14:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 3cf617d8-28cf-3575-aa7a-56c313f6b5c7 | -14.00023 | -45.58662 | 2025-03-02 04:16:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| e1e9f5bf-98ea-3405-86c8-41d9ff41bac2 | -13.97976 | -45.58688 | 2025-03-02 04:16:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| ca357003-7f8d-3cf8-a56e-f95bb0e25a1c | -14.00136 | -45.57948 | 2025-03-02 04:16:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 2e2229ac-482d-3cc7-8374-04e9eee5ff4f | -14.00354 | -45.58717 | 2025-03-02 04:16:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| d8900601-9a9e-332c-bd41-a8da9fb5b228 | -13.26304 | -43.50383 | 2025-03-02 04:16:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 755f0cf1-aee0-3680-9df5-f8f0ba57ac83 | -13.78862 | -44.33175 | 2025-03-02 04:16:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3fe4549c-5d40-372d-a78e-f6cc5293509b | -14.00079 | -45.58305 | 2025-03-02 04:16:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 41165951-4bc4-3334-9a5e-3cf97b3c744d | -13.97701 | -45.58276 | 2025-03-02 04:16:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| c963a845-4068-3db7-ab9e-eb82979b20f5 | -14.8821 | -46.35026 | 2025-03-02 04:16:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 5e771613-570a-3e97-9382-19307919f5f3 | -13.98251 | -45.591 | 2025-03-02 04:16:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| bf1a292e-fc01-33db-a4ed-71389765e157 | -13.97919 | -45.59045 | 2025-03-02 04:16:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 3b13db3e-51ed-3e51-8152-45e925c3103f | -14.00297 | -45.59073 | 2025-03-02 04:16:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 11f9f548-5fcc-365f-8380-b5436f8e21e3 | -14.00193 | -45.57592 | 2025-03-02 04:16:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 9bf53c9c-3741-3b5c-85de-21a59aaf8627 | -13.97644 | -45.58633 | 2025-03-02 04:16:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 24307a75-e16a-378f-9557-3ea33954d585 | -13.98033 | -45.58331 | 2025-03-02 04:16:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 1e0a51da-f0a6-304a-8a40-bcd72a3e16be | -12.8427 | -43.83063 | 2025-03-02 04:16:00 | NOAA-21 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| af994b59-4f56-3813-a29c-e538f923efe2 | -12.84657 | -43.82759 | 2025-03-02 04:16:00 | NOAA-21 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 8f5e62e6-a809-3591-ba78-76ff3f85ad9d | -14.00241 | -45.5943 | 2025-03-02 04:16:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 25635aa4-88ec-32a5-8e58-00b765bf5250 | -13.98194 | -45.59457 | 2025-03-02 04:16:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 986009c0-2643-38c5-9d75-ed5c82391e3d | -14.00572 | -45.59486 | 2025-03-02 04:16:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 0fdc292d-7fc1-3a7d-8913-0caf176b3371 | -12.84989 | -43.82812 | 2025-03-02 04:16:00 | NOAA-21 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 076ae9ee-060a-397a-a9f6-b9d5c4069887 | -12.85321 | -43.82866 | 2025-03-02 04:16:00 | NOAA-21 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 17.1 |
| fc69e670-5f9a-3078-96bc-5baf03c1378b | -18.04151 | -39.92593 | 2025-03-02 04:16:00 | NOAA-21 | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 53282051-6b03-34c1-bd5c-1ff82b0d8399 | -14.00411 | -45.5836 | 2025-03-02 04:16:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 28163959-ec9c-30e8-8b42-e34add378ad7 | -13.79472 | -44.35815 | 2025-03-02 04:16:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 08639236-a264-3f5b-943d-650a698d061b | -13.97758 | -45.57919 | 2025-03-02 04:16:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| b2fcc908-1bc5-31fb-8029-21f2e79bacad | -13.9737 | -45.58221 | 2025-03-02 04:16:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 58d5cfa9-3692-3f92-a7c9-8c03c719159b | -14.85602 | -46.79593 | 2025-03-02 04:16:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fbad249d-20a7-3230-99ef-275966752273 | -13.9809 | -45.57974 | 2025-03-02 04:16:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| de2e8c5d-acd3-3831-974d-3dc9b1cc9abd | -13.79139 | -44.33582 | 2025-03-02 04:16:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b4266c1d-5e66-366b-b4b2-cbcf6c815999 | -12.84602 | -43.83115 | 2025-03-02 04:16:00 | NOAA-21 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 08e57abe-57b0-32a7-b384-d18a7260e39c | -13.79193 | -44.33228 | 2025-03-02 04:16:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c03d7dfc-62e6-3574-97af-70578049d80e | -20.39086 | -49.11361 | 2025-03-02 04:18:00 | NOAA-21 | ICÉM | SÃO PAULO | Brasil | 3519808 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 7fad253c-82c1-3d6e-9166-6f92d6f5ed46 | -22.78769 | -43.75771 | 2025-03-02 04:18:00 | NOAA-21 | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| ab7689a0-dd93-331a-8582-617be5fa7d18 | -22.90129 | -43.75747 | 2025-03-02 04:18:00 | NOAA-21 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 3a6ffa18-b87d-3314-aada-9dcd62ccb36d | -20.98191 | -40.84985 | 2025-03-02 04:18:00 | NOAA-21 | ITAPEMIRIM | ESPÍRITO SANTO | Brasil | 3202801 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| dba40a1b-d1ad-34cc-a563-475c9a525ac9 | -22.3278 | -42.73731 | 2025-03-02 04:18:00 | NOAA-21 | TERESÓPOLIS | RIO DE JANEIRO | Brasil | 3305802 | 33 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 3cfdd220-36a6-3e01-a90a-414db1842112 | -22.66109 | -44.77701 | 2025-03-02 04:18:00 | NOAA-21 | SILVEIRAS | SÃO PAULO | Brasil | 3552007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 0c2b3d4b-e977-3b4e-951c-b8b0c998cbbe | -21.12476 | -41.67844 | 2025-03-02 04:18:00 | NOAA-21 | BOM JESUS DO ITABAPOANA | RIO DE JANEIRO | Brasil | 3300605 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| f099251c-5db9-388a-aa77-9d9c6b08fcc6 | -22.89743 | -43.47476 | 2025-03-02 04:18:00 | NOAA-21 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 24404794-14f3-3c35-8e9a-2edddf5b3704 | -22.9036 | -43.75557 | 2025-03-02 04:18:00 | NOAA-21 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 96e476fb-6fc4-335f-b151-8be877b2d459 | -20.98453 | -43.03522 | 2025-03-02 04:18:00 | NOAA-21 | DIVINÉSIA | MINAS GERAIS | Brasil | 3121902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| e49ab57b-8404-3237-9ce7-b2379da34c72 | -22.9969 | -43.51096 | 2025-03-02 04:18:00 | NOAA-21 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| f34728ea-997c-3156-ba70-c693eec8360e | -22.90188 | -43.75303 | 2025-03-02 04:18:00 | NOAA-21 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| df1b09e6-7b23-39df-91b6-c2022779db44 | -21.6263 | -43.46786 | 2025-03-02 04:18:00 | NOAA-21 | JUIZ DE FORA | MINAS GERAIS | Brasil | 3136702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 01e1482f-16cd-3be0-bd58-1ffa2b65efb5 | -20.85676 | -44.57922 | 2025-03-02 04:18:00 | NOAA-21 | SÃO TIAGO | MINAS GERAIS | Brasil | 3165008 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 911a284d-de61-3ced-a42c-52acb98352c5 | -22.66166 | -44.77291 | 2025-03-02 04:18:00 | NOAA-21 | SILVEIRAS | SÃO PAULO | Brasil | 3552007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| b6ebbcba-a167-3df8-8260-b51f510b979d | -23.27943 | -45.87437 | 2025-03-02 04:18:00 | NOAA-21 | SÃO JOSÉ DOS CAMPOS | SÃO PAULO | Brasil | 3549904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 828ef4b1-9169-3dc5-be99-69d693071870 | -17.6755 | -54.15965 | 2025-03-02 04:18:00 | NOAA-21 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 454eca47-7282-32b8-8e9f-4170e5f3220b | -23.98322 | -48.91802 | 2025-03-02 04:18:00 | NOAA-21 | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ed1c1d9a-f053-39b9-8d68-d7bba67e55ca | -22.75388 | -43.26817 | 2025-03-02 04:18:00 | NOAA-21 | DUQUE DE CAXIAS | RIO DE JANEIRO | Brasil | 3301702 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 039636b6-8728-34a0-a11f-bc72232682e6 | -22.37158 | -49.03893 | 2025-03-02 04:18:00 | NOAA-21 | BAURU | SÃO PAULO | Brasil | 3506003 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1ea86529-a66a-312c-9d4b-aa2d738f409f | -22.88402 | -43.6294 | 2025-03-02 04:18:00 | NOAA-21 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 56ad8af3-94dd-3c1f-ac1c-f18f9161260b | -20.88292 | -54.79246 | 2025-03-02 04:18:00 | NOAA-21 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 271a50ad-ed22-3699-954d-65f5202aae2a | -20.98142 | -40.85379 | 2025-03-02 04:18:00 | NOAA-21 | ITAPEMIRIM | ESPÍRITO SANTO | Brasil | 3202801 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| b86790d5-d240-3e3c-a1c9-c0ea83284e98 | -22.65823 | -44.77229 | 2025-03-02 04:18:00 | NOAA-21 | SILVEIRAS | SÃO PAULO | Brasil | 3552007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| e19536f6-e240-3f28-a235-9d615fcb14ef | -21.1483 | -49.2785 | 2025-03-02 04:18:00 | NOAA-21 | URUPÊS | SÃO PAULO | Brasil | 3556008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 15492f02-6854-3f63-8076-b76db2618fc6 | -23.9866 | -48.91868 | 2025-03-02 04:18:00 | NOAA-21 | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d5f0c207-71fd-389a-b903-389c327eb2ad | -17.67434 | -54.16537 | 2025-03-02 04:18:00 | NOAA-21 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d42eed9d-6aa1-3e9e-93e6-ab4cb6eecad1 | -23.68998 | -51.84591 | 2025-03-02 04:18:00 | NOAA-21 | BOM SUCESSO | PARANÁ | Brasil | 4103206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 33b300ef-75e3-3458-9faf-4cf7920018d0 | -21.19606 | -44.93953 | 2025-03-02 04:18:00 | NOAA-21 | IJACI | MINAS GERAIS | Brasil | 3130408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 0cf949b3-9baf-31c1-b67d-7b79a87f45c1 | -23.33792 | -46.77093 | 2025-03-02 04:18:00 | NOAA-21 | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 4774baa1-d067-395b-9159-d75e1e3de3df | -22.32405 | -42.73674 | 2025-03-02 04:18:00 | NOAA-21 | TERESÓPOLIS | RIO DE JANEIRO | Brasil | 3305802 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| ede0d8e6-5c28-3321-9967-9fe91e87d575 | -22.54011 | -48.81182 | 2025-03-02 04:18:00 | NOAA-21 | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 820f059c-bec0-3a27-8abb-07eb26d37ad7 | -18.90177 | -54.97609 | 2025-03-02 04:18:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0af79584-6f5a-311d-bc66-3ce0fed5c6f2 | -20.91867 | -56.54511 | 2025-03-02 04:18:00 | NOAA-21 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 23cdb5dd-02c9-3590-8b6e-a84d08a60a4a | -23.40495 | -46.55514 | 2025-03-02 04:18:00 | NOAA-21 | GUARULHOS | SÃO PAULO | Brasil | 3518800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| b0ebe797-93c3-30a1-a110-dab23ecc97fe | -21.71813 | -45.27869 | 2025-03-02 04:18:00 | NOAA-21 | TRÊS CORAÇÕES | MINAS GERAIS | Brasil | 3169307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 3797d381-eb9a-3bf3-ae19-9469a577f77f | -24.24488 | -50.73944 | 2025-03-02 04:18:00 | NOAA-21 | ORTIGUEIRA | PARANÁ | Brasil | 4117305 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| a7ab1346-1f4b-3ea5-9f55-9aa73f63971a | -21.20751 | -48.55568 | 2025-03-02 04:18:00 | NOAA-21 | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| e55a8657-dc73-3da1-836d-65c104a4591e | -27.72439 | -50.07222 | 2025-03-02 04:21:00 | NOAA-21 | LAGES | SANTA CATARINA | Brasil | 4209300 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 351e325b-d7bb-3c04-ad0d-a35a4042d3d8 | -25.19149 | -49.3266 | 2025-03-02 04:21:00 | NOAA-21 | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 519ce237-6469-3aa9-a8a9-b310388aa1d5 | -24.7539 | -48.87582 | 2025-03-02 04:21:00 | NOAA-21 | ADRIANÓPOLIS | PARANÁ | Brasil | 4100202 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 1cd4678f-7bba-32a8-ac8f-a4b0650c650b | -26.78405 | -48.65065 | 2025-03-02 04:21:00 | NOAA-21 | PENHA | SANTA CATARINA | Brasil | 4212502 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 448bcb61-3a27-3f72-84aa-342e2b3604a3 | -24.75454 | -48.87194 | 2025-03-02 04:21:00 | NOAA-21 | ADRIANÓPOLIS | PARANÁ | Brasil | 4100202 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| a0906dcc-49f9-393e-a954-fd254f1ae4d7 | -25.13882 | -49.47342 | 2025-03-02 04:21:00 | NOAA-21 | ITAPERUÇU | PARANÁ | Brasil | 4111258 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 86a437a6-430f-32fa-bc54-c3b740bbcec5 | -24.75056 | -48.87508 | 2025-03-02 04:21:00 | NOAA-21 | ADRIANÓPOLIS | PARANÁ | Brasil | 4100202 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 6c428a50-862a-362e-b530-cf45544037f8 | 2.5802 | -60.6215 | 2025-03-02 04:30:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 57.1 |
| a9def79c-fb84-3c99-bdd4-33d91ce01c92 | 1.93702 | -60.39367 | 2025-03-02 04:38:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 3debeef8-3539-3b70-9d29-bd2f86af922a | 2.58495 | -60.62539 | 2025-03-02 04:38:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 6.3 |
| cbdc8161-026e-3afe-813d-b8d18cd787ac | 1.32342 | -60.4278 | 2025-03-02 04:38:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.8 |
| e9ab37f5-69c0-33ad-8b82-2928ba5d961b | 2.00509 | -60.55969 | 2025-03-02 04:38:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f718eae7-7bcf-3559-9550-63467b8e5edd | 1.99731 | -60.5545 | 2025-03-02 04:38:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8a105c3f-e377-30a8-a2da-796ec0a060d8 | 0.95804 | -60.53266 | 2025-03-02 04:38:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1da1950f-3abd-343c-9529-dd82d1289833 | 1.9384 | -60.39365 | 2025-03-02 04:38:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 1ade6237-8188-3175-b9db-c0d5c3ae518e | 2.57706 | -60.62778 | 2025-03-02 04:38:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1c691309-4f23-3e77-b777-15e9f0c7afe1 | 1.94357 | -60.39119 | 2025-03-02 04:38:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 8245e41d-c450-37cb-92be-d7b500c899b1 | 1.3176 | -60.43484 | 2025-03-02 04:38:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 654f05f2-10b9-3692-953c-3363fc770e6c | 1.31668 | -60.42883 | 2025-03-02 04:38:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 8ed67a1f-f88d-311c-bd20-c9e087330c7d | 1.31546 | -60.43405 | 2025-03-02 04:38:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 91a9520f-2abb-3a39-929f-5c8d096039ba | 2.57804 | -60.62654 | 2025-03-02 04:38:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 4ea97492-6e2e-3640-8b90-efe34a0116ea | 1.93758 | -60.38811 | 2025-03-02 04:38:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 0f6c8471-b91a-32ac-9c3e-ae26f2205167 | 1.78944 | -60.66944 | 2025-03-02 04:38:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a9f251ed-e842-351b-9c32-8c87120dd210 | 1.32219 | -60.43299 | 2025-03-02 04:38:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 4.3 |
| d3ffdfe7-51c0-3e5c-96e3-610d851ba5ad | 1.32432 | -60.43377 | 2025-03-02 04:38:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 8.2 |
| ae3b06f2-0c13-35eb-bd67-dd726c849a21 | 2.5859 | -60.63167 | 2025-03-02 04:38:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 3d5e4293-c288-3602-9e4c-ede143e4fa6c | 2.58489 | -60.63294 | 2025-03-02 04:38:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 9.8 |


[Clique aqui para ver as próximas entradas](README4.md)
