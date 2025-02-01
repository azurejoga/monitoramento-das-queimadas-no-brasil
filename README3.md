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
| 196194cb-635f-39df-87ad-d05a4e11c431 | 1.41908 | -59.95795 | 2025-02-01 04:55:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 06b3dc19-7eca-376c-badd-51e2736143d2 | 0.79158 | -60.0892 | 2025-02-01 04:55:00 | NOAA-21 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 39e2792b-4d6d-3223-8b6a-5c9e6855992f | 1.93848 | -60.3838 | 2025-02-01 04:55:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 2a047efe-34ad-356e-849c-6e172ec8efcd | 1.42306 | -59.95193 | 2025-02-01 04:55:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 8d0240e1-7098-32c9-8040-54f534136012 | 1.41441 | -59.96213 | 2025-02-01 04:55:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 2fda971d-57f4-317d-bc36-c54a611652e9 | 1.93931 | -60.38932 | 2025-02-01 04:55:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 738e976d-8231-3cc6-9a28-95daa11890eb | 1.41263 | -59.94813 | 2025-02-01 04:55:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 519a95c7-165d-3ec9-b939-be67d092e078 | 1.42222 | -59.94663 | 2025-02-01 04:55:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 4.8 |
| c0b2aca2-77f7-3bb5-bbc1-04b5745bbd6f | 1.42164 | -59.94473 | 2025-02-01 04:55:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 5.3 |
| c00c6999-44c7-3769-9b38-6e54daff61d1 | 1.41992 | -59.96323 | 2025-02-01 04:55:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 74857aca-407b-3f97-b63f-14b7432a3b68 | 1.41684 | -59.94549 | 2025-02-01 04:55:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 5.3 |
| d8f9b71e-f6cc-34a6-9b08-809a3b92d0b0 | 1.9389 | -60.38659 | 2025-02-01 04:55:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 4.7 |
| ff4fbed0-427b-3aef-8068-5830181c0874 | 1.41362 | -59.95682 | 2025-02-01 04:55:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 5.3 |
| f7a572e5-aee3-3df4-9d26-9ac8589c3140 | 1.94346 | -60.38295 | 2025-02-01 04:55:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5ba81746-28e8-38ae-804e-e4779816f4be | 0.79661 | -60.09165 | 2025-02-01 04:55:00 | NOAA-21 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c553541b-3b87-37c0-a316-209b260bf661 | 3.15548 | -61.01107 | 2025-02-01 04:55:00 | NOAA-21 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 61cd32d8-9d8e-3b9e-9bf1-fd5efff02449 | 1.42139 | -59.94132 | 2025-02-01 04:55:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 4.8 |
| c07b653b-c56d-355f-a927-718e5dc9b4bf | 0.79638 | -60.0885 | 2025-02-01 04:55:00 | NOAA-21 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a4cd51a5-45a0-3776-aba3-8e4f8ac712d1 | 1.41428 | -59.95868 | 2025-02-01 04:55:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 2d9c4c7c-f5b3-3562-bf21-0e6aa2ab9ba8 | 1.41345 | -59.95341 | 2025-02-01 04:55:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 26603e25-6e32-34e5-84a8-abe2b9c9ae29 | 1.41826 | -59.95267 | 2025-02-01 04:55:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 695ea3fb-7195-3424-863d-19e7931a2ee4 | 4.56524 | -60.77839 | 2025-02-01 04:55:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b0639157-e6b8-3ff5-b24c-3496b9454bbc | 1.41842 | -59.95609 | 2025-02-01 04:55:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 8.6 |
| cdb535be-3705-3a2e-888f-f2e2647853ad | 2.44016 | -60.65061 | 2025-02-01 04:55:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 4466a162-200c-3b40-be54-86ce7a33a9fa | 1.42244 | -59.95004 | 2025-02-01 04:55:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 18c69b70-9e49-339d-9d76-20a920e00801 | 1.94387 | -60.38571 | 2025-02-01 04:55:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| abec3ceb-a385-3928-bb85-e474c73cf11c | 3.15498 | -61.00771 | 2025-02-01 04:55:00 | NOAA-21 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 131a79f6-40a1-3a2d-bd80-5fa51cba1451 | -9.08901 | -66.86926 | 2025-02-01 04:57:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 370c3c65-9ec3-3142-838c-3ffa5715b12e | -15.39598 | -60.17641 | 2025-02-01 04:59:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c19534b5-eccd-324d-9c0e-08b09bb5bb33 | -16.09026 | -60.06167 | 2025-02-01 04:59:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 87aa4842-6d36-32a7-84b7-e949d4814381 | -15.39972 | -60.17711 | 2025-02-01 04:59:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 88ab5189-241b-3a71-acb1-d229aa6fdeb2 | -15.25332 | -60.23388 | 2025-02-01 04:59:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 93b389dd-dd63-310c-8e36-60fc8f15d204 | -15.25708 | -60.23458 | 2025-02-01 04:59:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ca7acb63-3c26-38c1-854a-4a34febdba45 | -12.77503 | -61.45449 | 2025-02-01 04:59:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b646d6e8-1fb9-3e6c-891a-bbce21b5b452 | -15.25624 | -60.23665 | 2025-02-01 04:59:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 5a3fe103-9df5-3c07-8d50-5205c3c14274 | 1.4134 | -59.9504 | 2025-02-01 05:00:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 60.1 |
| 688220e0-e198-3a40-b313-c814515d8d10 | -22.12194 | -56.68063 | 2025-02-01 05:01:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 273c79df-84cf-3a0d-9ce6-d4a3ffd6f535 | -22.15648 | -56.67881 | 2025-02-01 05:01:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fc3a2d17-52bd-3f46-bf5b-9674c68d5e8e | -21.25585 | -57.32552 | 2025-02-01 05:01:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 17d51d6b-e940-3b7c-9dd6-568b4d0f6a1a | -22.15314 | -56.67823 | 2025-02-01 05:01:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dac587ca-a740-3523-8ff1-ab9f91cc6d81 | -21.25254 | -57.32494 | 2025-02-01 05:01:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f95d6c00-3b08-3d39-9453-a0d306a05cb9 | -21.41743 | -55.77911 | 2025-02-01 05:01:00 | NOAA-21 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 09762d91-e171-38a1-ae1c-f7eb0c269f6e | -21.20293 | -56.91777 | 2025-02-01 05:01:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2e9aca62-bb54-34bf-8c69-bde8fbc76977 | -21.29816 | -55.90657 | 2025-02-01 05:01:00 | NOAA-21 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cc59cb9a-fe91-3e8c-8557-60f9f14d0451 | -22.12251 | -56.67684 | 2025-02-01 05:01:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| db6d6bbf-6a8b-3955-a125-51e9d9245ae2 | -17.74636 | -56.315 | 2025-02-01 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.5 |
| eceea0ab-fa3f-3fd8-a838-9f1b4114c955 | -30.98137 | -53.12236 | 2025-02-01 05:03:00 | NOAA-21 | SANTANA DA BOA VISTA | RIO GRANDE DO SUL | Brasil | 4317004 | 43 | 33 | nan | nan | nan | Pampa | 3.2 |
| 9a6d244f-a8c0-3473-ba05-15b315abaa33 | -29.78109 | -51.17598 | 2025-02-01 05:03:00 | NOAA-21 | SÃO LEOPOLDO | RIO GRANDE DO SUL | Brasil | 4318705 | 43 | 33 | nan | nan | nan | Pampa | 1.2 |
| cd473caf-34cf-35c3-ac4e-dd6a044177e6 | -30.66301 | -54.03139 | 2025-02-01 05:03:00 | NOAA-21 | SÃO GABRIEL | RIO GRANDE DO SUL | Brasil | 4318309 | 43 | 33 | nan | nan | nan | Pampa | 0.6 |
| 5155c476-adef-3e13-9b08-6abf7a510026 | 1.4134 | -59.9504 | 2025-02-01 05:10:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 54.9 |
| f730506e-12ff-3321-8192-c1df6768ff3b | 1.4134 | -59.9504 | 2025-02-01 05:20:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 65.7 |
| 176f1d9f-1f81-32aa-895d-9f0585f392ca | 2.14139 | -60.85092 | 2025-02-01 05:22:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e36a46b6-cd5a-3c38-832c-04e983e49f2d | 1.42275 | -59.94154 | 2025-02-01 05:22:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 696a8f51-a464-3ea2-be02-88b4e51faba4 | 1.1245 | -60.52672 | 2025-02-01 05:22:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f03c5c52-baae-3a0f-b6ae-70e025d3f653 | 1.42219 | -59.95967 | 2025-02-01 05:22:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e9e7c378-bec9-3a6b-a92a-c51869a8f076 | 3.15353 | -61.00924 | 2025-02-01 05:22:00 | NPP-375D | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c1c5d961-421d-3170-9926-e45c1c02186c | 1.41828 | -59.95667 | 2025-02-01 05:22:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 5c3dcb63-abb4-3f2d-9974-8c8512ed6c87 | 1.41382 | -59.95015 | 2025-02-01 05:22:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 136a52ab-61d9-32a7-8b9d-8961d2789432 | 1.94383 | -60.38652 | 2025-02-01 05:22:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a1fd1c49-53af-3a80-965b-6eee02bfe309 | 1.94328 | -60.38293 | 2025-02-01 05:22:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a5ed6e88-4d80-3694-9320-f369a59b7526 | 2.43856 | -60.65011 | 2025-02-01 05:22:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1dd29fdd-ad56-3ead-bac0-7d39784bf23d | 1.42387 | -59.94859 | 2025-02-01 05:22:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.7 |
| fa217c10-ec6b-3c6d-b707-5c3d952bad01 | 0.79271 | -60.08963 | 2025-02-01 05:22:00 | NPP-375D | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f71c53f6-788f-39ca-bcbb-1b31d1b43107 | 1.41772 | -59.95315 | 2025-02-01 05:22:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.8 |
| b236ce64-88e4-3c67-ad5c-79ac0f33f694 | 1.42052 | -59.9491 | 2025-02-01 05:22:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 2d4e7513-221c-3f1e-bc55-13285bfeee28 | 2.442 | -60.64958 | 2025-02-01 05:22:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 6.2 |
| b68afef6-72b7-3287-8fa6-96cc26a2d4e2 | 1.41437 | -59.95367 | 2025-02-01 05:22:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.8 |
| b986e96f-14cc-30c2-b52c-d3fc5e8653d1 | 1.41158 | -59.95771 | 2025-02-01 05:22:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 49a5910a-b241-3128-9b31-c597df461ed4 | 1.94044 | -60.38705 | 2025-02-01 05:22:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fe708803-3adc-37ab-8caa-daaebca30a8d | 1.41213 | -59.96123 | 2025-02-01 05:22:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| da7bee60-1a37-377e-b17e-81654347c9e4 | 1.41493 | -59.95719 | 2025-02-01 05:22:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.8 |
| a8e05924-fda4-39e2-be89-79196cfe12ca | 1.94099 | -60.39061 | 2025-02-01 05:22:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5af85455-8dbd-3c5d-b15e-0cd138450840 | 1.93705 | -60.38762 | 2025-02-01 05:22:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 385fff78-77d8-3d36-88d6-bb80946f5088 | 0.79607 | -60.08911 | 2025-02-01 05:22:00 | NPP-375D | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 31dba914-4b3f-32f8-a3a6-f356d37b5c76 | 1.41548 | -59.96071 | 2025-02-01 05:22:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 14.6 |
| fdb33fb9-dc6f-30bb-82f1-63031b87e031 | 1.41661 | -59.94611 | 2025-02-01 05:22:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 405d0df7-3029-32cd-bc2d-4d374a7eeb5f | 2.43914 | -60.65384 | 2025-02-01 05:22:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ae559fd7-c8ee-3bc7-866a-3eddf9a004d7 | 1.93988 | -60.38346 | 2025-02-01 05:22:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ce0cd626-1cc7-3e24-affe-f402d456c1ef | 1.42107 | -59.95263 | 2025-02-01 05:22:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 7adaa41c-9ac9-36c7-ab92-730060d0f8cf | 1.4127 | -59.94311 | 2025-02-01 05:22:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 188f5bc3-b035-3816-9b70-be4b380d05a6 | 1.42331 | -59.94506 | 2025-02-01 05:22:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 605b2cba-5fd4-319f-96e0-021c826bf76e | -8.33844 | -55.10293 | 2025-02-01 05:22:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c7f6f9fc-7729-3653-9c68-70362e0d25f8 | 1.41996 | -59.94559 | 2025-02-01 05:22:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.7 |
| c978333e-1412-33b5-a47a-817ddb4ff368 | -8.33904 | -55.09878 | 2025-02-01 05:22:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 52988569-63d8-3f15-9bac-a4d7b8fa7a54 | 1.42163 | -59.95615 | 2025-02-01 05:22:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 26c64220-7f3b-3d54-bdcd-1029440f7b14 | 1.41884 | -59.96019 | 2025-02-01 05:22:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 14.6 |
| 3fb12ecd-5231-3315-932c-d602aa523939 | 1.41717 | -59.94963 | 2025-02-01 05:22:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 4.1 |
| c997d2f0-6424-37ec-92d7-54f7d5e22dfa | 1.4194 | -59.94206 | 2025-02-01 05:22:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 62ae1ab2-15e4-323a-9f59-1eafb32bbfca | 1.93649 | -60.384 | 2025-02-01 05:22:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a950803f-7c78-3145-8b47-01e992efd9b9 | 1.41605 | -59.94258 | 2025-02-01 05:22:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 47d00a15-0524-33bd-b5de-b4260e38309e | 2.14484 | -60.85035 | 2025-02-01 05:22:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6ca58125-be51-3781-a9b3-34d603973afc | 1.12394 | -60.52311 | 2025-02-01 05:22:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c900f174-9747-3825-9f97-a47920b318ee | 1.41326 | -59.94663 | 2025-02-01 05:22:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 4.1 |
| f644bc79-4ea4-3669-a18d-d2f64cd5afbf | -12.41432 | -63.98117 | 2025-02-01 05:25:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 097eb462-5b95-3bd7-add0-34cce87589f0 | -14.52953 | -59.97096 | 2025-02-01 05:25:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3cad1a46-5298-3e6b-a13a-fc1c3a17bf46 | -15.25664 | -60.23564 | 2025-02-01 05:25:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8de78cd5-eb41-396b-9562-8b98927e0ce5 | -16.08652 | -60.0606 | 2025-02-01 05:25:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 392404b0-c7c7-3a55-8d80-2b6d0f807b51 | -12.77246 | -61.45467 | 2025-02-01 05:25:00 | NPP-375D | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 859f6331-ce4c-3e23-9fbb-77b9e47728cb | -11.86842 | -63.96532 | 2025-02-01 05:25:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 71bf5c17-c36d-3cce-9814-111877af5058 | -15.39793 | -60.17843 | 2025-02-01 05:25:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README4.md)
