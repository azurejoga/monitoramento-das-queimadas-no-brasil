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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a3d52417-bb66-3e90-8b5f-3aaf801a76ec | -21.88977 | -53.72099 | 2025-02-11 04:23:00 | NOAA-20 | NOVA ANDRADINA | MATO GROSSO DO SUL | Brasil | 5006200 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 217cb842-b265-3da3-9e17-ef67b36d5dbd | -20.48379 | -47.53356 | 2025-02-11 04:23:00 | NOAA-20 | RIBEIRÃO CORRENTE | SÃO PAULO | Brasil | 3543105 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9562964a-c5ab-3f10-a727-de127b640417 | -20.8131 | -48.71741 | 2025-02-11 04:23:00 | NOAA-20 | COLINA | SÃO PAULO | Brasil | 3512001 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 78a141b1-8205-33e6-bfa2-e524c589911c | -20.7622 | -46.76781 | 2025-02-11 04:23:00 | NOAA-20 | ITAÚ DE MINAS | MINAS GERAIS | Brasil | 3133758 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 197fb843-6d31-3476-adbc-b1df4f3a6eda | -20.90655 | -56.53489 | 2025-02-11 04:23:00 | NOAA-20 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 036592a3-984a-3f0c-b035-c6eee9770ab0 | -22.33148 | -55.03969 | 2025-02-11 04:23:00 | NOAA-20 | PONTA PORÃ | MATO GROSSO DO SUL | Brasil | 5006606 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 768c539d-dd88-3d5d-bff1-4e67f0260c20 | -20.29307 | -54.99837 | 2025-02-11 04:23:00 | NOAA-20 | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 57f91416-65bf-3a38-8b03-280f07edf122 | -21.35283 | -48.61562 | 2025-02-11 04:23:00 | NOAA-20 | CÂNDIDO RODRIGUES | SÃO PAULO | Brasil | 3510104 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| faa29880-33f0-3a90-838a-e67d07639910 | -16.08145 | -60.06438 | 2025-02-11 04:23:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 644fbc0c-5c53-3567-ab07-452e384e14de | -22.5965 | -54.91606 | 2025-02-11 04:23:00 | NOAA-20 | CAARAPÓ | MATO GROSSO DO SUL | Brasil | 5002407 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| d85ed820-4bc7-32c2-a26c-6cb72f77f78f | -16.08008 | -60.07045 | 2025-02-11 04:23:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 8cac3e5d-ee50-3cad-b5b8-b6ae17480119 | -21.35673 | -48.61252 | 2025-02-11 04:23:00 | NOAA-20 | CÂNDIDO RODRIGUES | SÃO PAULO | Brasil | 3510104 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 282402a3-da05-33e6-8f75-44ee2dc3cac2 | -23.33725 | -46.77296 | 2025-02-11 04:23:00 | NOAA-20 | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 843e5fa9-a04d-3694-a1bd-28bf32e11805 | -21.89121 | -53.71352 | 2025-02-11 04:23:00 | NOAA-20 | NOVA ANDRADINA | MATO GROSSO DO SUL | Brasil | 5006200 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ec40a882-54f1-3fc1-91dc-4e4625850090 | -20.27979 | -54.99521 | 2025-02-11 04:23:00 | NOAA-20 | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0d88745c-be7f-3f2e-a7f9-9876a0c6d48d | -30.19258 | -56.68782 | 2025-02-11 04:25:00 | NOAA-20 | URUGUAIANA | RIO GRANDE DO SUL | Brasil | 4322400 | 43 | 33 | nan | nan | nan | Pampa | 3.9 |
| dbb8c31e-03a0-379e-bd96-297dfc905155 | -30.67987 | -53.53647 | 2025-02-11 04:25:00 | NOAA-20 | CAÇAPAVA DO SUL | RIO GRANDE DO SUL | Brasil | 4302808 | 43 | 33 | nan | nan | nan | Pampa | 0.8 |
| ee82d2db-182e-39e9-89ec-732cd1c5b8c5 | -30.31009 | -51.89776 | 2025-02-11 04:25:00 | NOAA-20 | SÃO JERÔNIMO | RIO GRANDE DO SUL | Brasil | 4318408 | 43 | 33 | nan | nan | nan | Pampa | 2.4 |
| 594cb256-3a5f-3c72-931c-c6755ff86dd9 | -32.15651 | -52.22958 | 2025-02-11 04:25:00 | NOAA-20 | RIO GRANDE | RIO GRANDE DO SUL | Brasil | 4315602 | 43 | 33 | nan | nan | nan | Pampa | 1.1 |
| 6b56162a-a6eb-3703-a6d9-27319e3994b9 | -32.2001 | -52.2682 | 2025-02-11 04:25:00 | NOAA-20 | RIO GRANDE | RIO GRANDE DO SUL | Brasil | 4315602 | 43 | 33 | nan | nan | nan | Pampa | 7.4 |
| 46411c56-d0c8-3e9e-a181-547e63c9c0b5 | -24.24317 | -50.74059 | 2025-02-11 04:25:00 | NOAA-20 | ORTIGUEIRA | PARANÁ | Brasil | 4117305 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| dff02d40-c753-32fb-9c04-a56f04878b08 | -31.67238 | -52.08162 | 2025-02-11 04:25:00 | NOAA-20 | PELOTAS | RIO GRANDE DO SUL | Brasil | 4314407 | 43 | 33 | nan | nan | nan | Pampa | 1.0 |
| 6acb6939-a42d-3de9-8f5b-7b3a50f82773 | -25.19849 | -49.32365 | 2025-02-11 04:25:00 | NOAA-20 | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| d1c014ef-4e64-3355-b26e-34d52e88e0b2 | -30.19662 | -56.68897 | 2025-02-11 04:25:00 | NOAA-20 | URUGUAIANA | RIO GRANDE DO SUL | Brasil | 4322400 | 43 | 33 | nan | nan | nan | Pampa | 3.9 |
| ca62015d-f18e-3d1e-afdd-2e9bdc44190b | -25.30041 | -50.70327 | 2025-02-11 04:25:00 | NOAA-20 | IMBITUVA | PARANÁ | Brasil | 4110102 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 11187110-8c24-3baf-a1ec-15f893c932e9 | -31.39067 | -52.66275 | 2025-02-11 04:25:00 | NOAA-20 | CANGUÇU | RIO GRANDE DO SUL | Brasil | 4304507 | 43 | 33 | nan | nan | nan | Pampa | 0.9 |
| 710bc1da-40fd-330f-821c-02be9604a777 | -30.30743 | -51.89291 | 2025-02-11 04:25:00 | NOAA-20 | SÃO JERÔNIMO | RIO GRANDE DO SUL | Brasil | 4318408 | 43 | 33 | nan | nan | nan | Pampa | 2.4 |
| d73909d8-5568-3bd6-89b8-ac8f8f2cf307 | -30.19172 | -56.69199 | 2025-02-11 04:25:00 | NOAA-20 | URUGUAIANA | RIO GRANDE DO SUL | Brasil | 4322400 | 43 | 33 | nan | nan | nan | Pampa | 3.9 |
| 38fcf1af-0e49-3dda-9d44-ef8601898bea | -30.41329 | -50.6589 | 2025-02-11 04:25:00 | NOAA-20 | PALMARES DO SUL | RIO GRANDE DO SUL | Brasil | 4313656 | 43 | 33 | nan | nan | nan | Pampa | 0.4 |
| 000f936d-f725-367c-a605-686e6815f4df | -25.28768 | -49.99598 | 2025-02-11 04:25:00 | NOAA-20 | PONTA GROSSA | PARANÁ | Brasil | 4119905 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 930b9cb2-bb79-3d6e-97c0-2036704e246f | -31.14378 | -50.80938 | 2025-02-11 04:25:00 | NOAA-20 | MOSTARDAS | RIO GRANDE DO SUL | Brasil | 4312500 | 43 | 33 | nan | nan | nan | Pampa | 2.3 |
| 17672532-4681-38c6-94d1-fd432e48a47e | -32.15248 | -52.23295 | 2025-02-11 04:25:00 | NOAA-20 | RIO GRANDE | RIO GRANDE DO SUL | Brasil | 4315602 | 43 | 33 | nan | nan | nan | Pampa | 1.1 |
| ddc553d1-f88d-39e9-a494-555a11797353 | -32.19411 | -52.26252 | 2025-02-11 04:25:00 | NOAA-20 | RIO GRANDE | RIO GRANDE DO SUL | Brasil | 4315602 | 43 | 33 | nan | nan | nan | Pampa | 8.2 |
| 90819110-6003-3353-9c6e-e2f758808dd9 | -30.18854 | -56.68667 | 2025-02-11 04:25:00 | NOAA-20 | URUGUAIANA | RIO GRANDE DO SUL | Brasil | 4322400 | 43 | 33 | nan | nan | nan | Pampa | 9.0 |
| 44b8d1df-e81b-3528-bee9-8b7de85ee099 | -30.78729 | -52.75016 | 2025-02-11 04:25:00 | NOAA-20 | ENCRUZILHADA DO SUL | RIO GRANDE DO SUL | Brasil | 4306908 | 43 | 33 | nan | nan | nan | Pampa | 1.1 |
| dd2b2a73-323a-3617-888e-90ad01eeb24e | -30.26182 | -52.01901 | 2025-02-11 04:25:00 | NOAA-20 | BUTIÁ | RIO GRANDE DO SUL | Brasil | 4302709 | 43 | 33 | nan | nan | nan | Pampa | 0.7 |
| 958507e0-d8e7-37d9-92c9-8f531f529a45 | -30.40998 | -50.6582 | 2025-02-11 04:25:00 | NOAA-20 | PALMARES DO SUL | RIO GRANDE DO SUL | Brasil | 4313656 | 43 | 33 | nan | nan | nan | Pampa | 0.4 |
| 15ee0f57-b2c2-3fdf-8f30-1372711f5ae5 | -25.19127 | -49.32619 | 2025-02-11 04:25:00 | NOAA-20 | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| d46ce70f-eba9-3e91-8ada-1fac65f77605 | -25.47871 | -49.84681 | 2025-02-11 04:25:00 | NOAA-20 | PORTO AMAZONAS | PARANÁ | Brasil | 4120101 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 08cc5ff9-cfa9-3f41-9a14-111123ddd377 | -32.20343 | -52.26897 | 2025-02-11 04:25:00 | NOAA-20 | RIO GRANDE | RIO GRANDE DO SUL | Brasil | 4315602 | 43 | 33 | nan | nan | nan | Pampa | 7.4 |
| 98dbabbc-e64a-3de7-9c63-9662ee02c886 | 1.33101 | -60.72387 | 2025-02-11 05:08:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 7b17e44e-6863-34d2-a321-b7507fb7a747 | -7.24665 | -44.71834 | 2025-02-11 05:10:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a78f4edf-831c-3288-ba8e-394fd72dc301 | -7.23995 | -44.71728 | 2025-02-11 05:10:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 697b0109-da20-38f2-97d2-3c082b565c29 | -4.04689 | -54.78944 | 2025-02-11 05:10:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b69306e9-5640-3d35-b9b4-d148a362caae | -19.57165 | -55.23801 | 2025-02-11 05:14:00 | NOAA-21 | CORGUINHO | MATO GROSSO DO SUL | Brasil | 5003108 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8f8ee4ca-e9f1-31fd-abb3-991c20519873 | -20.28125 | -54.99548 | 2025-02-11 05:14:00 | NOAA-21 | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 79b8efe5-1dbd-3de0-b3cd-7e15e5b58372 | -20.91217 | -56.53338 | 2025-02-11 05:14:00 | NOAA-21 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 64339788-2b7f-37a5-975c-80b70c84bcd3 | -20.29356 | -54.99714 | 2025-02-11 05:14:00 | NOAA-21 | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a1eb2f8e-d458-36aa-beeb-57aa1affe97a | -16.08291 | -60.06414 | 2025-02-11 05:14:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3aabe3ac-94b2-3c7f-afbf-11e16b5b9533 | -22.17682 | -56.55637 | 2025-02-11 05:14:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b1606b26-47f0-32a1-8beb-ac0f62b9158e | -16.08452 | -60.07547 | 2025-02-11 05:14:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d2da0c4b-0c94-3342-ad53-2bf59233f6cc | -20.28849 | -55.00437 | 2025-02-11 05:14:00 | NOAA-21 | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 4.9 |
| c9e65dd3-4408-3140-908e-8ec76d6bcc26 | -14.62674 | -59.99511 | 2025-02-11 05:14:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1542ae6c-bfdd-3f30-bb3c-e8a784c31ecf | -20.28487 | -54.99993 | 2025-02-11 05:14:00 | NOAA-21 | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8f8d0b1a-3985-3d9e-b1e9-abe44fc9abcc | -22.33624 | -55.0429 | 2025-02-11 05:14:00 | NOAA-21 | PONTA PORÃ | MATO GROSSO DO SUL | Brasil | 5006606 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 99425def-a83d-3181-8a84-eab155ab63e9 | -20.28946 | -54.99658 | 2025-02-11 05:14:00 | NOAA-21 | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f7d94d24-9be9-3660-806d-497d88f01b35 | -20.28898 | -55.00048 | 2025-02-11 05:14:00 | NOAA-21 | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9b5533d6-6b12-3186-b446-c0b4c6caf48b | -20.28536 | -54.99602 | 2025-02-11 05:14:00 | NOAA-21 | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e80b71f9-e9f2-367c-8aa8-ee1fdadf5450 | -20.72906 | -54.60857 | 2025-02-11 05:14:00 | NOAA-21 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 84a80dd0-d082-3d7e-8999-b04f0dcb67e0 | -16.08679 | -60.06111 | 2025-02-11 05:14:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 630a3512-1c30-3d46-93ad-8a8db2e1b083 | -21.20704 | -55.7514 | 2025-02-11 05:14:00 | NOAA-21 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b66d878d-e0ee-3b02-baab-a938a4a43e88 | -16.08508 | -60.07187 | 2025-02-11 05:14:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ae24355c-0e4c-32be-9b8e-8f72b7479a71 | -19.76333 | -54.7979 | 2025-02-11 05:14:00 | NOAA-21 | CORGUINHO | MATO GROSSO DO SUL | Brasil | 5003108 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 85751298-af83-353c-a2bd-ee37bae2a966 | -21.077 | -56.39309 | 2025-02-11 05:14:00 | NOAA-21 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b8c92710-b36e-3f1e-b2f2-9d825d627cbb | -16.08565 | -60.06828 | 2025-02-11 05:14:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4cafb2fc-e4b1-3b8d-bab0-bb51099c90b0 | -16.08622 | -60.0647 | 2025-02-11 05:14:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 54187a1f-f4b8-3422-b3b0-90f6e9e9ce06 | -21.89486 | -53.71599 | 2025-02-11 05:14:00 | NOAA-21 | NOVA ANDRADINA | MATO GROSSO DO SUL | Brasil | 5006200 | 50 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7444bb2e-f825-3554-a520-f02ee5eafc77 | -21.8954 | -53.71108 | 2025-02-11 05:14:00 | NOAA-21 | NOVA ANDRADINA | MATO GROSSO DO SUL | Brasil | 5006200 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c8c26922-67e0-345c-8727-c99d5e79f5e4 | -16.08953 | -60.06526 | 2025-02-11 05:14:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b706e389-659c-34b1-a0d3-6c3fe44199d1 | -16.10059 | -60.05976 | 2025-02-11 05:14:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a75f8c33-1019-3b44-beae-bf0ac72ed17b | -20.25056 | -54.1506 | 2025-02-11 05:14:00 | NOAA-21 | JARAGUARI | MATO GROSSO DO SUL | Brasil | 5004908 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 556b435b-e958-30bc-9fcf-7f612fcaf2da | -19.0535 | -52.86026 | 2025-02-11 05:14:00 | NOAA-21 | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 44893495-561f-3274-b464-d3c1b4d98708 | -16.08896 | -60.06884 | 2025-02-11 05:14:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 74d1e6c8-337a-34a3-916e-392b5592ee9e | -20.56767 | -55.08789 | 2025-02-11 05:14:00 | NOAA-21 | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8846d89f-98ab-3ea2-9054-f7eba9d469ff | -21.96521 | -57.5881 | 2025-02-11 05:14:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 13db5e66-14cb-39d4-9ca1-1c1022fe49e5 | -24.24254 | -50.7387 | 2025-02-11 05:16:00 | NOAA-21 | ORTIGUEIRA | PARANÁ | Brasil | 4117305 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| bedae85b-5b9d-3e61-9da9-0e14863a7169 | -30.31298 | -51.89547 | 2025-02-11 05:16:00 | NOAA-21 | SÃO JERÔNIMO | RIO GRANDE DO SUL | Brasil | 4318408 | 43 | 33 | nan | nan | nan | Pampa | 2.2 |
| 4152d205-9145-3353-96a5-61e5ab02b9fd | -30.30922 | -51.89854 | 2025-02-11 05:16:00 | NOAA-21 | SÃO JERÔNIMO | RIO GRANDE DO SUL | Brasil | 4318408 | 43 | 33 | nan | nan | nan | Pampa | 3.9 |
| 83802f8c-7506-3f5b-a713-0b3b88c0b92b | -30.3127 | -51.8996 | 2025-02-11 05:16:00 | NOAA-21 | SÃO JERÔNIMO | RIO GRANDE DO SUL | Brasil | 4318408 | 43 | 33 | nan | nan | nan | Pampa | 2.2 |
| 9545ac05-5a28-3bbd-94c3-acef315294e1 | -28.86563 | -50.87522 | 2025-02-11 05:16:00 | NOAA-21 | CAXIAS DO SUL | RIO GRANDE DO SUL | Brasil | 4305108 | 43 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 11fb70d4-a777-38f6-b079-182a207b694d | -30.19352 | -56.69081 | 2025-02-11 05:16:00 | NOAA-21 | URUGUAIANA | RIO GRANDE DO SUL | Brasil | 4322400 | 43 | 33 | nan | nan | nan | Pampa | 5.1 |
| 3f67866e-0eb5-35a6-a754-15700349c5c7 | -30.19773 | -56.6914 | 2025-02-11 05:16:00 | NOAA-21 | URUGUAIANA | RIO GRANDE DO SUL | Brasil | 4322400 | 43 | 33 | nan | nan | nan | Pampa | 3.1 |
| 3bb0d4b9-d788-3d00-ae96-890de5c2a425 | -30.18931 | -56.69024 | 2025-02-11 05:16:00 | NOAA-21 | URUGUAIANA | RIO GRANDE DO SUL | Brasil | 4322400 | 43 | 33 | nan | nan | nan | Pampa | 5.1 |
| 463f7fed-066a-3ad2-926a-c61f5eb18608 | -30.18979 | -56.6858 | 2025-02-11 05:16:00 | NOAA-21 | URUGUAIANA | RIO GRANDE DO SUL | Brasil | 4322400 | 43 | 33 | nan | nan | nan | Pampa | 5.1 |
| 441002ac-f215-35cc-acda-bf1eed186271 | -30.30951 | -51.89451 | 2025-02-11 05:16:00 | NOAA-21 | SÃO JERÔNIMO | RIO GRANDE DO SUL | Brasil | 4318408 | 43 | 33 | nan | nan | nan | Pampa | 2.8 |
| f6b74936-886b-38cf-81ea-ab39f61e7815 | -32.19593 | -52.264 | 2025-02-11 05:18:00 | NOAA-21 | RIO GRANDE | RIO GRANDE DO SUL | Brasil | 4315602 | 43 | 33 | nan | nan | nan | Pampa | 4.0 |
| e7df4f0c-2eaa-3e09-a99b-cd5dbaf37222 | -32.15497 | -52.22894 | 2025-02-11 05:18:00 | NOAA-21 | RIO GRANDE | RIO GRANDE DO SUL | Brasil | 4315602 | 43 | 33 | nan | nan | nan | Pampa | 1.1 |
| 1301199a-a005-3b5c-acd9-7c0863733995 | -32.19781 | -52.26402 | 2025-02-11 05:18:00 | NOAA-21 | RIO GRANDE | RIO GRANDE DO SUL | Brasil | 4315602 | 43 | 33 | nan | nan | nan | Pampa | 8.2 |
| 5bd7cd0e-1c7c-3237-938a-e352458ab841 | -32.20154 | -52.26457 | 2025-02-11 05:18:00 | NOAA-21 | RIO GRANDE | RIO GRANDE DO SUL | Brasil | 4315602 | 43 | 33 | nan | nan | nan | Pampa | 4.0 |
| ac926609-8fa6-30e5-b5b1-fc05139401d7 | -32.20688 | -52.26952 | 2025-02-11 05:18:00 | NOAA-21 | RIO GRANDE | RIO GRANDE DO SUL | Brasil | 4315602 | 43 | 33 | nan | nan | nan | Pampa | 3.0 |
| 77ab1ea9-c155-3fbe-bdf7-80b3be2c86bd | -32.20661 | -52.27389 | 2025-02-11 05:18:00 | NOAA-21 | RIO GRANDE | RIO GRANDE DO SUL | Brasil | 4315602 | 43 | 33 | nan | nan | nan | Pampa | 3.3 |
| 82c77244-8907-3fc8-a74c-05a1254ed18d | -12.85405 | -43.81876 | 2025-02-11 05:25:00 | AQUA_M-M | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| d30685eb-f4f7-30ca-902e-ca019abb8259 | -32.20025 | -52.25844 | 2025-02-11 05:29:00 | AQUA_M-M | RIO GRANDE | RIO GRANDE DO SUL | Brasil | 4315602 | 43 | 33 | nan | nan | nan | Pampa | 5.9 |
| f122661c-be19-3b99-a3c3-674cd6c78e66 | -30.30886 | -51.89325 | 2025-02-11 05:29:00 | AQUA_M-M | SÃO JERÔNIMO | RIO GRANDE DO SUL | Brasil | 4318408 | 43 | 33 | nan | nan | nan | Pampa | 6.3 |
| c0b01b15-ed71-38d2-96e8-ce7f54d9d9e1 | -32.20756 | -52.27205 | 2025-02-11 05:29:00 | AQUA_M-M | RIO GRANDE | RIO GRANDE DO SUL | Brasil | 4315602 | 43 | 33 | nan | nan | nan | Pampa | 6.8 |
| 0a2f05e4-615b-3376-afaa-7827d6f5a671 | 3.19901 | -60.58454 | 2025-02-11 05:33:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 919b9265-5ea5-377c-ae9a-3c9faa0c8655 | 1.33154 | -60.72462 | 2025-02-11 05:33:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5f245d95-6533-3356-86bc-cf2e74af8515 | -16.08796 | -60.07112 | 2025-02-11 05:40:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| dd64062d-1abe-32c8-b758-a8dfba102418 | -20.29117 | -54.99453 | 2025-02-11 05:40:00 | NPP-375D | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f6827d70-140d-387a-b116-fc11ddf384de | -16.08315 | -60.07462 | 2025-02-11 05:40:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |


[Clique aqui para ver as próximas entradas](README5.md)
