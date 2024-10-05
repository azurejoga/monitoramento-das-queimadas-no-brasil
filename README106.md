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

## Dados Diários - Página 106

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3722dc60-ca70-30d6-a73d-bf7bd36e28f9 | -10.67014 | -50.69017 | 2024-10-05 04:38:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 32d0aaf3-d6ac-3a7a-b459-7ca3df466c6b | -10.66738 | -50.68613 | 2024-10-05 04:38:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 84ace972-efc6-3347-8474-44350351432b | -10.66731 | -51.53575 | 2024-10-05 04:38:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4cb1edb8-b914-3fa3-88f5-a4c8dc4d8ff2 | -10.66683 | -50.68963 | 2024-10-05 04:38:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 94c1ecad-4c42-324c-8bc9-c54f4fd8bb17 | -10.66627 | -50.69313 | 2024-10-05 04:38:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9f934df7-7cd0-3fe5-b187-372c793c3cd4 | -10.66572 | -50.69664 | 2024-10-05 04:38:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c9bf6c22-2447-36c7-ace6-2bb53c9210ad | -10.66396 | -50.68527 | 2024-10-05 04:38:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 21352825-b27a-3c9c-b35c-934ea50e7d16 | -10.56671 | -51.08418 | 2024-10-05 04:38:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 21608142-f82c-37ce-8cb4-d1f7ffb697e5 | -10.56339 | -51.08363 | 2024-10-05 04:38:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 806e0955-039f-3fc0-96f1-67bd4080fcb6 | -10.55398 | -51.07846 | 2024-10-05 04:38:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9c8f4648-fd35-3617-a611-4aa00591d4c1 | -10.55066 | -51.07792 | 2024-10-05 04:38:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2a6e359c-9359-34bc-a117-b042ea9d5999 | -10.55009 | -51.08145 | 2024-10-05 04:38:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 338a2183-5a86-3516-99d2-c59a9febce6b | -10.5479 | -51.07384 | 2024-10-05 04:38:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b67b1d4d-7cbe-348a-b00d-a08485143c06 | -10.54733 | -51.07737 | 2024-10-05 04:38:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b10be6ea-6f7d-3f71-a494-75eb6c780682 | -10.54457 | -51.07329 | 2024-10-05 04:38:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b4b5284a-086e-3cbf-8a8c-bacfe62429cb | -10.54401 | -51.07683 | 2024-10-05 04:38:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6fb3e963-e044-31c2-99b4-e7fcf190d079 | -10.53269 | -50.95559 | 2024-10-05 04:38:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c6f5ec03-dec6-3b2d-8c8b-21a668d8e199 | -10.53213 | -50.95912 | 2024-10-05 04:38:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 123c287f-9920-314c-8e26-84ccf4b246c8 | -10.52463 | -51.07003 | 2024-10-05 04:38:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 37d4e919-24a7-3b3a-a53b-b240db45149b | -10.52391 | -50.92527 | 2024-10-05 04:38:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 61ffe71c-615a-3692-9329-1e3316a78613 | -10.52048 | -50.96806 | 2024-10-05 04:38:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a7f56f4a-cc0c-3a59-b546-e1f7357ece47 | -10.51992 | -50.97158 | 2024-10-05 04:38:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a92946a4-dcb9-38e6-a07d-75368cc12deb | -10.51799 | -51.06894 | 2024-10-05 04:38:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 72cd286d-f74b-39f3-82f7-200c240d6889 | -10.51021 | -51.07491 | 2024-10-05 04:38:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 57fbd7cf-9611-3590-b8ec-b8643f9d59ea | -10.50689 | -51.07437 | 2024-10-05 04:38:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ffdda630-58b7-3eca-a0d6-c0773ef97247 | -10.50632 | -51.07789 | 2024-10-05 04:38:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2112d32e-ee9f-3217-9e2e-e08820cc05ef | -10.503 | -51.07735 | 2024-10-05 04:38:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 33742cd0-9120-308a-848e-f28263dc16bb | -10.50243 | -51.08088 | 2024-10-05 04:38:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b661f2da-99fd-3451-b69e-e1e91e6d23fe | -10.49903 | -51.1021 | 2024-10-05 04:38:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 52e67a46-6b83-3410-9016-f9aca1d96bba | -10.48666 | -51.11898 | 2024-10-05 04:38:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8fe1b2de-16a5-370b-a205-4f7bdfc61955 | -10.48609 | -51.12252 | 2024-10-05 04:38:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bed5c56f-1ca9-3c64-aa98-b9f05f49554d | -10.48221 | -51.12551 | 2024-10-05 04:38:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a01572e2-31cf-3df1-b87c-2b71bc94430e | -10.46023 | -50.72835 | 2024-10-05 04:38:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b9739734-7bed-3fe9-ace1-80d7fcd060d2 | -10.45967 | -50.73185 | 2024-10-05 04:38:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cf718777-9f3d-35aa-ac43-39ef1bbfe0bf | -10.45691 | -50.72781 | 2024-10-05 04:38:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2febe65b-1968-3c61-b76b-c6bcd4a97ede | -10.45304 | -50.73078 | 2024-10-05 04:38:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| adaa6e09-e6c3-3aea-aac5-d3ee6249a15f | -10.45084 | -50.72325 | 2024-10-05 04:38:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 329e00e8-c59d-3825-b10d-6eba8872f549 | -10.45029 | -50.72675 | 2024-10-05 04:38:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c97d66bc-9aa7-3610-8679-90d48afb97a3 | -10.44973 | -50.73025 | 2024-10-05 04:38:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1488db74-e9ae-38dc-81d3-3f121c1908fe | -10.44864 | -50.71571 | 2024-10-05 04:38:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7576167c-c1fc-3426-82fa-bd1678fcd766 | -10.44809 | -50.71922 | 2024-10-05 04:38:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 651fde6e-1bed-34bc-ac4e-a3b8e0bea835 | -10.44753 | -50.72272 | 2024-10-05 04:38:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a1104dcb-af6b-3d37-a118-e06128e25c8d | -10.44697 | -50.72622 | 2024-10-05 04:38:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f36b500d-693f-3ce9-a1d5-4988c787b17c | -10.44642 | -50.72972 | 2024-10-05 04:38:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b48cbe73-4582-3156-b3e9-4fa0a3224452 | -10.44533 | -50.71518 | 2024-10-05 04:38:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8923d7de-605d-3f41-b552-d4222386a2eb | -10.44477 | -50.71868 | 2024-10-05 04:38:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| fbd890ed-5d2d-3905-b06f-3b3f74f0b8ec | -10.44422 | -50.72218 | 2024-10-05 04:38:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6f7e5aa1-4bc4-3a0a-926b-99b74b31a1f1 | -10.44366 | -50.72568 | 2024-10-05 04:38:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 988f8aee-ecd7-3933-b32a-1392c3e090c9 | -10.44311 | -50.72918 | 2024-10-05 04:38:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f29036ce-5ecf-31d5-b192-0a316a016c58 | -10.44144 | -50.73969 | 2024-10-05 04:38:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 307d6949-4e00-3b5e-b506-772e4820e8d6 | -10.44088 | -50.7432 | 2024-10-05 04:38:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0b6c59ad-56f3-39fc-9a8e-0448546e8738 | -10.44084 | -50.72137 | 2024-10-05 04:38:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 1d5b0de6-9bad-3237-9e50-0dec9f9892a1 | -10.44029 | -50.72487 | 2024-10-05 04:38:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 7.0 |
| e78fe3fc-7880-3a4e-974d-32fd33124544 | -10.43973 | -50.72837 | 2024-10-05 04:38:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 7.0 |
| f4786c57-4817-33c7-9cd6-ae0db67f8bed | -10.43918 | -50.73187 | 2024-10-05 04:38:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 498406f7-7842-39ca-b90b-33e89f00633c | -10.43863 | -50.73537 | 2024-10-05 04:38:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f28f3d43-28ca-3649-adfb-a60cfe07d2cd | -10.43807 | -50.73888 | 2024-10-05 04:38:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b5c137be-eaa4-394b-a523-e40aeb221f60 | -10.43752 | -50.74238 | 2024-10-05 04:38:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a8bb294d-e763-3dd0-9358-ca87c00c3886 | -10.43698 | -50.72433 | 2024-10-05 04:38:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 79462f89-0e50-32de-9dec-5807374c65af | -10.43642 | -50.72784 | 2024-10-05 04:38:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 5b1c6957-e8ac-334e-b1db-61d64bb9ba4d | -10.43587 | -50.73134 | 2024-10-05 04:38:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 74ff026f-44ce-3603-a27b-9bc92d69145d | -10.43531 | -50.73484 | 2024-10-05 04:38:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 10ca1369-dade-37f1-b3b5-5ab4f3266c28 | -10.43476 | -50.73834 | 2024-10-05 04:38:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fe7c4545-7362-36d3-9553-b5b5bc245034 | -10.43311 | -50.7273 | 2024-10-05 04:38:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 8f791654-e077-3037-aca3-340866317e4a | -10.43256 | -50.7308 | 2024-10-05 04:38:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 720f3870-5246-3528-b304-58890c8da204 | -10.432 | -50.7343 | 2024-10-05 04:38:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9b691131-41bb-300a-baee-e2ec72240bb3 | -10.43145 | -50.73781 | 2024-10-05 04:38:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 20dd7cf5-6751-368a-93c7-bbbd7865c1e6 | -10.42924 | -50.73027 | 2024-10-05 04:38:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ece5e4fc-1b5d-37b4-a8f7-4c2284ed5536 | -10.42869 | -50.73377 | 2024-10-05 04:38:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6d72f305-fb7f-3866-b25a-100f0c7b1ae9 | -10.42814 | -50.73727 | 2024-10-05 04:38:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| bb6a7810-1390-3b6b-a428-053297934033 | -10.42758 | -50.74078 | 2024-10-05 04:38:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 3ade4b14-0960-3cc5-8978-1ea237486445 | -10.42703 | -50.74428 | 2024-10-05 04:38:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e3a89d2d-e131-3042-a64a-a41eeb4a37fe | -10.42538 | -50.73323 | 2024-10-05 04:38:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| aa8fffc1-8b5b-3c9a-ac3f-e395af0bfd9f | -10.43809 | -50.76072 | 2024-10-05 04:38:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f69d4992-7d81-300c-a5dd-95b6baf8706f | -10.43754 | -50.76423 | 2024-10-05 04:38:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 859de7c0-8191-3937-8064-fa96eb583074 | -10.43698 | -50.76773 | 2024-10-05 04:38:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 19639993-b84a-332d-9965-f3a48c8023fe | -10.43694 | -50.78933 | 2024-10-05 04:38:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b0692f22-e4e4-3801-b03b-0a880bb5ca2d | -10.43475 | -50.75991 | 2024-10-05 04:38:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3f5bca2e-44a5-3420-be60-38870a4c7d12 | -10.43419 | -50.76342 | 2024-10-05 04:38:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 22d4ba8f-5e49-366d-b720-26b567f664cc | -10.43364 | -50.76693 | 2024-10-05 04:38:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fe900038-6da7-3cec-b9ff-98056d7d84e5 | -10.43363 | -50.78879 | 2024-10-05 04:38:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b148118a-ef73-3af7-9064-9f7783da60d0 | -10.43231 | -51.28848 | 2024-10-05 04:38:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e6bc6dd9-6631-3a00-9237-10d800ec4d17 | -10.43143 | -50.75938 | 2024-10-05 04:38:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 49d0014b-11a1-3e79-a1d7-b0deae77b9b1 | -10.43088 | -50.76289 | 2024-10-05 04:38:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bb566bcb-c4ba-3827-9c1f-61089df60604 | -10.43032 | -50.7664 | 2024-10-05 04:38:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ec42e8ac-961f-3f4c-8090-ec44bba4656f | -10.43031 | -50.78799 | 2024-10-05 04:38:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d33b321a-90f4-38d8-9ceb-1eafe20680f5 | -10.42975 | -50.79149 | 2024-10-05 04:38:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6c83ca47-0bde-3b19-b439-5112dd37157d | -10.42897 | -51.28793 | 2024-10-05 04:38:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a720b47b-2e83-30aa-91e2-b476d0576bc2 | -10.427 | -50.78745 | 2024-10-05 04:38:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a67adb98-7af8-33bf-a0cd-da3cd91cdee3 | -10.42644 | -50.79096 | 2024-10-05 04:38:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5233b5c3-c619-389d-9aed-a1a9a95ae975 | -10.42589 | -50.79446 | 2024-10-05 04:38:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a32d80b0-8f7d-364a-948a-f77ce2d282b5 | -10.42257 | -50.79393 | 2024-10-05 04:38:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ef92a793-7cb3-33de-bd98-dc6b4bf140ba | -10.42202 | -50.79743 | 2024-10-05 04:38:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 42a0217a-b11e-3bbe-a8a8-5321981f5962 | -10.42146 | -50.80092 | 2024-10-05 04:38:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9aa2e010-1406-3383-9437-f8b9220e28c0 | -10.4187 | -50.79689 | 2024-10-05 04:38:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 497043d1-7a39-3feb-aefd-9f72c8490a45 | -10.41815 | -50.8004 | 2024-10-05 04:38:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 38f65fea-c095-3f69-8075-6d008a94c877 | -10.41759 | -50.8039 | 2024-10-05 04:38:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f04c66f8-beb9-39ed-be20-adee330bc833 | -10.41704 | -50.80742 | 2024-10-05 04:38:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 44f30637-67a8-376a-9ee2-d0cab8c1736c | -10.41648 | -50.81093 | 2024-10-05 04:38:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 082ae5ca-368b-31e3-930c-9cc4d899ea61 | -10.41428 | -50.80338 | 2024-10-05 04:38:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |


[Clique aqui para ver as próximas entradas](README107.md)
