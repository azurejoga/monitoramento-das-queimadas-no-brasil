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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ce575239-2448-393d-9b55-7abb15f8fba6 | 0.43046 | -50.923 | 2025-12-06 12:33:00 | TERRA_M-T | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 9.9 |
| e2425b67-0358-34a3-97d6-65f401e5bbd7 | 0.43805 | -50.91291 | 2025-12-06 12:33:00 | TERRA_M-T | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 5c44d960-d118-33d5-9b85-3b45aff93d48 | -1.11757 | -52.16774 | 2025-12-06 12:33:00 | TERRA_M-T | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 11.7 |
| d3a76e2d-46f5-33d6-ba18-30efd634486e | 2.0994 | -55.85401 | 2025-12-06 12:33:00 | TERRA_M-T | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| c366a29b-c408-35cd-9abb-23034cab6523 | -1.40507 | -52.79744 | 2025-12-06 12:33:00 | TERRA_M-T | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 9bbc5a53-88aa-3192-a0f0-507e85a15ee8 | -2.62786 | -43.92222 | 2025-12-06 12:33:00 | TERRA_M-T | ICATU | MARANHÃO | Brasil | 2105104 | 21 | 33 | nan | nan | nan | Amazônia | 56.2 |
| 59556fbd-ac2f-3cc3-ae0e-f1e958e27e9e | -1.10877 | -52.16652 | 2025-12-06 12:33:00 | TERRA_M-T | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 19.8 |
| 69e2e851-a1d7-379e-9d66-09e986961137 | 1.70195 | -50.83981 | 2025-12-06 12:33:00 | TERRA_M-T | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 743f246e-8f12-3479-8eb7-cf62124521f4 | 1.69439 | -50.84984 | 2025-12-06 12:33:00 | TERRA_M-T | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 44.8 |
| c1d34cce-68d3-3aa4-b8af-4a3e2c59753a | 0.43932 | -50.92178 | 2025-12-06 12:33:00 | TERRA_M-T | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 0e813389-b6ea-344f-acf6-b3b1350597a2 | -3.1337 | -42.13489 | 2025-12-06 12:36:00 | TERRA_M-T | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Cerrado | 60.8 |
| 94cf9af6-c7e1-3458-82fc-20f3b4147021 | -3.41566 | -42.06348 | 2025-12-06 12:36:00 | TERRA_M-T | MURICI DOS PORTELAS | PIAUÍ | Brasil | 2206696 | 22 | 33 | nan | nan | nan | Caatinga | 129.8 |
| 240998a5-1822-3444-8932-dfaf4ff3d045 | -3.13532 | -42.14058 | 2025-12-06 12:36:00 | TERRA_M-T | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Cerrado | 68.5 |
| 2a3645bc-d6f1-345d-b153-265ae7167f29 | -3.48023 | -42.41084 | 2025-12-06 12:36:00 | TERRA_M-T | JOCA MARQUES | PIAUÍ | Brasil | 2205458 | 22 | 33 | nan | nan | nan | Caatinga | 48.2 |
| 5643f084-61d8-3ed4-8686-407b79d9d70f | -3.41609 | -42.07063 | 2025-12-06 12:36:00 | TERRA_M-T | MURICI DOS PORTELAS | PIAUÍ | Brasil | 2206696 | 22 | 33 | nan | nan | nan | Caatinga | 96.6 |
| 6c7ec200-c144-3526-a0b0-a2109d05ba49 | -3.5341 | -42.42519 | 2025-12-06 12:36:00 | TERRA_M-T | JOCA MARQUES | PIAUÍ | Brasil | 2205458 | 22 | 33 | nan | nan | nan | Caatinga | 72.9 |
| 40659d0e-81c7-3c37-a6d8-41f244592d12 | -2.11314 | -53.45647 | 2025-12-06 12:36:00 | TERRA_M-T | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 9fe47420-c61a-37d8-93d2-6e0b3fcd1b38 | -3.62764 | -43.81948 | 2025-12-06 12:36:00 | TERRA_M-T | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 40.1 |
| aea2f044-27cb-3266-8166-23d884c214ea | -2.98126 | -45.274 | 2025-12-06 12:36:00 | TERRA_M-T | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 39.6 |
| e9a4d757-9855-35de-9ce6-529bf269393c | -1.94762 | -49.91411 | 2025-12-06 12:36:00 | TERRA_M-T | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 2831985f-c3eb-39c9-83e5-accee2318830 | -3.22227 | -42.15179 | 2025-12-06 12:36:00 | TERRA_M-T | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 94.8 |
| e9cf5b44-2641-39de-8cd9-9b0fc7e01f1f | -2.78136 | -45.5046 | 2025-12-06 12:36:00 | TERRA_M-T | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 24.8 |
| 8ffb5656-04aa-3129-8293-eccfbbb6089d | -2.76924 | -45.51814 | 2025-12-06 12:36:00 | TERRA_M-T | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 21.0 |
| 906fc786-2cca-3c4b-954f-5ea400b8c9f2 | -3.22353 | -42.1586 | 2025-12-06 12:36:00 | TERRA_M-T | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 92.1 |
| 219ec642-dffd-3498-aca9-0853811c03b0 | -21.62623 | -56.13054 | 2025-12-06 12:40:00 | TERRA_M-T | JARDIM | MATO GROSSO DO SUL | Brasil | 5005004 | 50 | 33 | nan | nan | nan | Cerrado | 8.8 |
| c3671257-0143-39c8-bb47-73679d40c3de | -21.92905 | -56.79119 | 2025-12-06 12:40:00 | TERRA_M-T | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 7cc5a966-30e0-3bea-a30c-a0989125cd52 | -23.2248 | -51.05086 | 2025-12-06 12:40:00 | TERRA_M-T | IBIPORÃ | PARANÁ | Brasil | 4109807 | 41 | 33 | nan | nan | nan | Mata Atlântica | 11.3 |
| 5422e661-994a-3909-b5b7-b26ac237cb40 | -19.65666 | -56.86713 | 2025-12-06 12:40:00 | TERRA_M-T | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 15.7 |
| 2b8d0f9e-9327-34a5-b622-73528958bb60 | -22.27592 | -48.54331 | 2025-12-06 12:40:00 | TERRA_M-T | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 22.5 |
| bf948e4a-5d00-3726-a0a6-28479d9e3fe8 | -24.17379 | -49.57946 | 2025-12-06 12:40:00 | TERRA_M-T | SENGÉS | PARANÁ | Brasil | 4126306 | 41 | 33 | nan | nan | nan | Cerrado | 40.9 |
| 368be2a2-0870-3203-b270-01e22b0dc9c9 | -24.16043 | -49.57797 | 2025-12-06 12:40:00 | TERRA_M-T | SENGÉS | PARANÁ | Brasil | 4126306 | 41 | 33 | nan | nan | nan | Cerrado | 77.1 |
| 30220a23-04d6-3956-bcb1-32d0e30bb212 | -20.02889 | -53.44951 | 2025-12-06 12:40:00 | TERRA_M-T | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 7.1 |
| cae6e8da-349e-31e7-be0c-69d18a72fe39 | -19.06209 | -57.50305 | 2025-12-06 12:40:00 | TERRA_M-T | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 10.5 |
| 6556fb73-3bf7-3110-8100-934b5fb20aaf | -22.13396 | -48.80307 | 2025-12-06 12:40:00 | TERRA_M-T | BORACÉIA | SÃO PAULO | Brasil | 3507308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 27.8 |
| a14f6b6f-660e-3925-b24e-44fd29d80c1d | -19.65807 | -56.85763 | 2025-12-06 12:40:00 | TERRA_M-T | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.5 |
| a17b36fd-972d-3046-be61-3801b4061eee | -23.88869 | -53.88664 | 2025-12-06 12:40:00 | TERRA_M-T | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 24.1 |
| 683488b2-ce5c-37dd-ad6c-ac3fd0488f25 | -21.2961 | -50.34089 | 2025-12-06 12:40:00 | TERRA_M-T | BIRIGUI | SÃO PAULO | Brasil | 3506508 | 35 | 33 | nan | nan | nan | Mata Atlântica | 18.4 |
| 563dee85-f9df-34dc-98bc-16b9986f7a12 | -22.14117 | -48.79839 | 2025-12-06 12:40:00 | TERRA_M-T | BORACÉIA | SÃO PAULO | Brasil | 3507308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 22.2 |
| 3429c9a3-7a56-3d97-9cf6-aa2412adb3fa | -20.75425 | -55.18645 | 2025-12-06 12:40:00 | TERRA_M-T | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 7.6 |
| c99afc87-5b59-3fee-8f11-e79a52552094 | -20.70476 | -49.14475 | 2025-12-06 12:40:00 | TERRA_M-T | GUAPIAÇU | SÃO PAULO | Brasil | 3517505 | 35 | 33 | nan | nan | nan | Cerrado | 27.5 |
| a69fab0e-5a2d-394f-a861-7d444c4c9179 | -22.26904 | -48.5619 | 2025-12-06 12:40:00 | TERRA_M-T | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 26.3 |
| 684f1fef-ca05-357a-80f6-5d628bf2f90f | -18.79668 | -52.62521 | 2025-12-06 12:40:00 | TERRA_M-T | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 9.0 |
| acfe230d-15cd-3d95-842c-cbdddbbf16b3 | -22.13874 | -48.82318 | 2025-12-06 12:40:00 | TERRA_M-T | BORACÉIA | SÃO PAULO | Brasil | 3507308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 107.1 |
| ad5e4b94-70ef-3262-b63b-02d6975b9df5 | -24.33107 | -50.62855 | 2025-12-06 12:40:00 | TERRA_M-T | TELÊMACO BORBA | PARANÁ | Brasil | 4127106 | 41 | 33 | nan | nan | nan | Mata Atlântica | 19.6 |
| 03c80afe-e844-321e-887e-81efa9cdd236 | -24.16488 | -49.57204 | 2025-12-06 12:40:00 | TERRA_M-T | SENGÉS | PARANÁ | Brasil | 4126306 | 41 | 33 | nan | nan | nan | Cerrado | 135.6 |
| ae626694-1b0b-3acb-800d-8ce5922abb00 | -20.00775 | -53.20218 | 2025-12-06 12:40:00 | TERRA_M-T | ÁGUA CLARA | MATO GROSSO DO SUL | Brasil | 5000203 | 50 | 33 | nan | nan | nan | Cerrado | 10.4 |
| fa371ec8-90cc-34dc-991d-4dde16067a7e | -28.83833 | -52.02764 | 2025-12-06 12:42:00 | TERRA_M-T | ARVOREZINHA | RIO GRANDE DO SUL | Brasil | 4301404 | 43 | 33 | nan | nan | nan | Mata Atlântica | 12.9 |
| 93ffcbc8-902e-3da9-b3c3-f0c85902f438 | -28.97108 | -51.06734 | 2025-12-06 12:42:00 | TERRA_M-T | SÃO MARCOS | RIO GRANDE DO SUL | Brasil | 4319000 | 43 | 33 | nan | nan | nan | Mata Atlântica | 16.3 |
| 1a166250-a9b8-326d-b1d7-c68d6546c395 | -27.02838 | -50.91538 | 2025-12-06 12:42:00 | TERRA_M-T | FRAIBURGO | SANTA CATARINA | Brasil | 4205506 | 42 | 33 | nan | nan | nan | Mata Atlântica | 17.6 |
| e3b8d3ea-7f26-34d4-9563-fd177fd9c0f5 | -26.95184 | -50.90007 | 2025-12-06 12:42:00 | TERRA_M-T | FRAIBURGO | SANTA CATARINA | Brasil | 4205506 | 42 | 33 | nan | nan | nan | Mata Atlântica | 21.1 |
| 81e592d4-bdcd-3dfc-8d8b-a9fc4897e7bf | -30.73181 | -52.36881 | 2025-12-06 12:42:00 | TERRA_M-T | AMARAL FERRADOR | RIO GRANDE DO SUL | Brasil | 4300638 | 43 | 33 | nan | nan | nan | Pampa | 39.3 |
| 1e45382d-495e-32ef-9e9e-e181cffec489 | -28.85023 | -50.97367 | 2025-12-06 12:42:00 | TERRA_M-T | CAXIAS DO SUL | RIO GRANDE DO SUL | Brasil | 4305108 | 43 | 33 | nan | nan | nan | Mata Atlântica | 19.5 |
| 3fd565fe-d952-36d7-852a-398f5d86984e | -26.85933 | -51.45501 | 2025-12-06 12:42:00 | TERRA_M-T | SALTO VELOSO | SANTA CATARINA | Brasil | 4215406 | 42 | 33 | nan | nan | nan | Mata Atlântica | 15.1 |
| 32a04625-77a0-3088-810c-1b7f258f840d | -28.84019 | -52.00921 | 2025-12-06 12:42:00 | TERRA_M-T | GUAPORÉ | RIO GRANDE DO SUL | Brasil | 4309407 | 43 | 33 | nan | nan | nan | Mata Atlântica | 10.8 |
| 857ae282-70c6-3606-8b08-498ece6ab239 | -24.80282 | -53.29654 | 2025-12-06 12:42:00 | TERRA_M-T | CORBÉLIA | PARANÁ | Brasil | 4106308 | 41 | 33 | nan | nan | nan | Mata Atlântica | 10.5 |
| 2df0c337-7c71-3396-98e6-9a22004f57ac | -26.95393 | -50.87889 | 2025-12-06 12:42:00 | TERRA_M-T | FRAIBURGO | SANTA CATARINA | Brasil | 4205506 | 42 | 33 | nan | nan | nan | Mata Atlântica | 39.1 |
| 948044f9-5afb-3ff9-bae2-0a9501c39872 | -24.5157 | -53.57785 | 2025-12-06 12:42:00 | TERRA_M-T | ASSIS CHATEAUBRIAND | PARANÁ | Brasil | 4102000 | 41 | 33 | nan | nan | nan | Mata Atlântica | 8.8 |
| a0dea3b7-db21-3b7d-9009-2dde077024c4 | -28.84606 | -52.01638 | 2025-12-06 12:42:00 | TERRA_M-T | GUAPORÉ | RIO GRANDE DO SUL | Brasil | 4309407 | 43 | 33 | nan | nan | nan | Mata Atlântica | 22.0 |
| eb57b6cc-ca8a-346d-bd96-12788da85247 | -26.96124 | -49.78361 | 2025-12-06 12:42:00 | TERRA_M-T | DONA EMMA | SANTA CATARINA | Brasil | 4205100 | 42 | 33 | nan | nan | nan | Mata Atlântica | 39.6 |
| 1d1bb60a-35af-325f-9e62-9f0efcb645e8 | -26.84729 | -51.45354 | 2025-12-06 12:42:00 | TERRA_M-T | ÁGUA DOCE | SANTA CATARINA | Brasil | 4200408 | 42 | 33 | nan | nan | nan | Mata Atlântica | 10.1 |
| 1e02452e-c27a-388f-9096-dbcae8fce5f5 | -26.95492 | -50.88578 | 2025-12-06 12:42:00 | TERRA_M-T | FRAIBURGO | SANTA CATARINA | Brasil | 4205506 | 42 | 33 | nan | nan | nan | Mata Atlântica | 56.2 |
| b07e4843-3259-3fa6-9479-4b650ecd3cda | -19.6442 | -56.8311 | 2025-12-06 13:50:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 107.6 |
| cc283e70-7d0c-3fad-80bc-578e999285b4 | -19.6438 | -56.8521 | 2025-12-06 13:50:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 110.0 |
| 7dc0d98d-b8dc-3f25-bf17-ecf4dca46a9e | -24.164 | -49.5806 | 2025-12-06 14:00:00 | GOES-19 | SENGÉS | PARANÁ | Brasil | 4126306 | 41 | 33 | nan | nan | nan | Cerrado | 112.0 |
| 3f6ed4ec-5756-3108-bd2c-580b0bbdf4ac | -19.6442 | -56.8311 | 2025-12-06 14:00:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 114.2 |
| 9ed0bd50-392b-3659-ad7c-dce439b3ed75 | -24.164 | -49.5806 | 2025-12-06 14:10:00 | GOES-19 | SENGÉS | PARANÁ | Brasil | 4126306 | 41 | 33 | nan | nan | nan | Cerrado | 143.9 |


