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

## Dados Diários - Página 105

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7a5f2689-7e0a-3b87-b2ae-c63a8d8b9c3d | -15.0369 | -59.70436 | 2024-10-25 05:06:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6b6eff1a-43d6-33a6-bb3c-c38ed97579c7 | -15.03628 | -59.70817 | 2024-10-25 05:06:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 392c0790-2306-346a-8fd5-f8d161112e1b | -15.03349 | -59.70375 | 2024-10-25 05:06:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bf3e263d-f46d-3548-8aea-82e0eb608cf0 | -15.03287 | -59.70757 | 2024-10-25 05:06:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 26be1f1d-3f85-3194-9242-35721ad2b33b | -15.02946 | -59.70697 | 2024-10-25 05:06:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7796af53-6d23-3be0-b0a0-f5ef5d5b39af | -15.93678 | -59.5674 | 2024-10-25 05:06:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f9dc0422-50de-3dc9-9a18-eeb217446471 | -15.93617 | -59.57114 | 2024-10-25 05:06:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ef4f3140-80d1-39c1-a533-e12110ee28ae | -15.93341 | -59.5668 | 2024-10-25 05:06:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8eee9412-dadb-323a-a969-f7c414b6315f | -15.93279 | -59.57054 | 2024-10-25 05:06:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a7704836-274d-37e4-a0a6-185b605089df | -15.92699 | -59.62738 | 2024-10-25 05:06:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 57f512e6-841e-3b9e-8a92-6fde7f2270d9 | -15.92638 | -59.63113 | 2024-10-25 05:06:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 178bf176-d2a0-3f10-8556-ae355153b317 | -15.92361 | -59.62678 | 2024-10-25 05:06:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3e39347e-ee37-3d66-882a-5edccdc761b8 | -15.923 | -59.63054 | 2024-10-25 05:06:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| be57b403-092f-36c1-99c4-d26978f79683 | -15.91961 | -59.62994 | 2024-10-25 05:06:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2eb0515e-b46d-374f-8c9e-8d1577ff8485 | -15.69405 | -59.74236 | 2024-10-25 05:06:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 451c95b7-39cc-3ea5-91a5-ab9e0d98a2b6 | -15.69065 | -59.74176 | 2024-10-25 05:06:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f28bb7a9-4dfe-3cac-9812-5d8519b4b536 | -15.68725 | -59.74116 | 2024-10-25 05:06:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e2818bf1-d560-3e72-b5fb-832e58b4056f | -15.68663 | -59.74495 | 2024-10-25 05:06:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a376cfe1-8f77-3b37-aef4-1b965f1b6f48 | -15.68385 | -59.74055 | 2024-10-25 05:06:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 53cca078-e63a-3811-a70a-ab580d40226e | -15.68323 | -59.74435 | 2024-10-25 05:06:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1ac2a35b-bf59-3044-9cd5-39df9b0c91f6 | -15.68045 | -59.73995 | 2024-10-25 05:06:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 54514061-414b-34f1-a059-5b00de996ef6 | -15.67983 | -59.74374 | 2024-10-25 05:06:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5646b027-42d6-3762-9ceb-b65c2603ded7 | -15.67921 | -59.74753 | 2024-10-25 05:06:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cfe87290-f427-3c9f-ba18-39e1872d6de0 | -15.67706 | -59.73935 | 2024-10-25 05:06:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 09bdf430-1c96-36a2-8aa3-ed6f752add69 | -15.67643 | -59.74314 | 2024-10-25 05:06:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| efee6ce3-c62f-3e1f-a543-56d0572f0aca | -15.67581 | -59.74693 | 2024-10-25 05:06:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6f95221d-84f7-3b9d-b8e1-4653f434244d | -15.67366 | -59.73874 | 2024-10-25 05:06:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 087a9647-203e-3bba-9df0-c06f70001139 | -15.67303 | -59.74254 | 2024-10-25 05:06:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 63f3ae2b-00d8-3176-b74f-d4bc32de426c | -15.67241 | -59.74633 | 2024-10-25 05:06:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0bf06b1c-5ad9-30fa-8810-ab4026e9c50a | -15.67179 | -59.75012 | 2024-10-25 05:06:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f02093b4-4895-3518-8a35-58b96d112b4a | -15.67116 | -59.75391 | 2024-10-25 05:06:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ea57b6df-5f9b-3ced-aaf5-c9b474a936d6 | -15.67054 | -59.75771 | 2024-10-25 05:06:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6da64318-2d45-35c8-8b71-62f6810bcd30 | -15.66991 | -59.76151 | 2024-10-25 05:06:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 07adea20-af95-31e3-9583-899d2d30d0c1 | -15.66963 | -59.74193 | 2024-10-25 05:06:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 99ad51d2-43e8-3285-bd5e-360ebb11134e | -15.66901 | -59.74572 | 2024-10-25 05:06:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 556bea0f-a56b-3f18-8e2f-3afcbb280f3c | -15.66839 | -59.74952 | 2024-10-25 05:06:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ccd6302c-460a-342c-9d85-c1cf6794dd70 | -15.66651 | -59.7609 | 2024-10-25 05:06:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 04096e06-2e68-30b7-9b9a-efd020bfe4df | -23.82267 | -55.28887 | 2024-10-25 05:08:00 | NOAA-20 | PARANHOS | MATO GROSSO DO SUL | Brasil | 5006358 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| c177e3cf-034a-30c4-a672-037cead12fea | -23.78535 | -55.30434 | 2024-10-25 05:08:00 | NOAA-20 | PARANHOS | MATO GROSSO DO SUL | Brasil | 5006358 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 26cc56fa-20ae-36ad-b20b-e2c27a31e43f | -1.1834 | -53.6569 | 2024-10-25 05:15:12 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 51.6 |
| b9404c34-9b88-3875-b89a-dbce9d3c724f | -1.6062 | -53.3087 | 2024-10-25 05:15:14 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 69.2 |
| 831b19aa-7e49-36a2-bb9b-e110c1c4c188 | -4.3165 | -48.63 | 2024-10-25 05:15:30 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 44.5 |
| 0c2635ff-e353-33e6-bf84-dcbda10276cf | -4.3349 | -48.6506 | 2024-10-25 05:15:30 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 54.8 |
| a8a1f646-6664-3673-9e1d-d36f7a00ab1c | -4.3351 | -48.6292 | 2024-10-25 05:15:30 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 89.3 |
| bee75723-ff8e-39ee-a8d9-dc785ad827af | -5.9788 | -45.3621 | 2024-10-25 05:15:39 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 102.7 |
| c38aa1ff-1f7a-3992-b4f3-d35cdc105010 | -10.58431 | -44.28286 | 2024-10-25 05:25:00 | AQUA_M-M | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 426dd964-8454-3282-a915-10a954ff79a9 | -3.80142 | -43.24897 | 2024-10-25 05:25:00 | AQUA_M-M | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 6bb94f61-b223-3871-a67e-a0ba075e332c | -3.79975 | -43.26037 | 2024-10-25 05:25:00 | AQUA_M-M | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| afe8b948-123d-385e-b296-c527bf84c90c | -6.45045 | -44.67405 | 2024-10-25 05:25:00 | AQUA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| a289ee5b-cfc4-3388-8487-acb167806a44 | -5.89282 | -44.64009 | 2024-10-25 05:25:00 | AQUA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 11e56b08-0c07-3934-a530-419865dddcec | -5.62639 | -44.82811 | 2024-10-25 05:25:00 | AQUA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 4b7b1752-f47c-3465-a28d-4bdc1f13ec7a | -5.61708 | -44.82673 | 2024-10-25 05:25:00 | AQUA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| e2f3425a-f3aa-3fb5-8111-4116b7eccd8e | -5.57123 | -44.88041 | 2024-10-25 05:25:00 | AQUA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 0c040237-5573-36bd-866c-5eacca538e04 | -5.50669 | -44.82443 | 2024-10-25 05:25:00 | AQUA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 8a04e5a9-e6c5-3708-9ae8-670b57654120 | -7.19821 | -44.73464 | 2024-10-25 05:25:00 | AQUA_M-M | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 99b7f1c4-f750-3a4e-9444-036bdc5061a9 | -7.18868 | -44.73327 | 2024-10-25 05:25:00 | AQUA_M-M | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 15.6 |
| de1ff007-0ac9-3e50-93de-5a1287ffe2b1 | -6.84146 | -44.7506 | 2024-10-25 05:25:00 | AQUA_M-M | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 57427941-604d-32c9-b71c-315112054bc2 | -6.83649 | -44.75348 | 2024-10-25 05:25:00 | AQUA_M-M | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 12.4 |
| e18741ae-6d73-3c0c-ab49-b967e547ee54 | -6.4614 | -44.6653 | 2024-10-25 05:25:00 | AQUA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 6288413e-6235-3fdc-bc55-7c30c9839eca | -6.4599 | -44.67556 | 2024-10-25 05:25:00 | AQUA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 4898e8e2-9c16-3d73-93c4-886f48d11964 | -10.86352 | -44.78763 | 2024-10-25 05:25:00 | AQUA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 3932280f-b07c-39bd-9233-ed46c2c1169d | -4.84726 | -45.04175 | 2024-10-25 05:25:00 | AQUA_M-M | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 75e2ead9-12ae-32b8-9037-cd10e938b83c | -6.00459 | -45.94728 | 2024-10-25 05:25:00 | AQUA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| b007cfe7-ba8e-393f-83e8-da731e2e4347 | -5.98101 | -45.36197 | 2024-10-25 05:25:00 | AQUA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 69.7 |
| 73425613-6164-3c7f-b30c-d8b21ebdea73 | -5.97962 | -45.3714 | 2024-10-25 05:25:00 | AQUA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 76.6 |
| b688f0b6-9734-3a5f-958b-958e212e1610 | -5.97189 | -45.3606 | 2024-10-25 05:25:00 | AQUA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| d8deafbe-e0fb-3e23-b3e2-99319ac9ee50 | -5.97051 | -45.37003 | 2024-10-25 05:25:00 | AQUA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 14.7 |
| b3a14f44-6e02-30bb-bd88-5a4fc25f0a4f | -5.70955 | -45.002 | 2024-10-25 05:25:00 | AQUA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| bb6b83aa-add6-3ac7-9fe3-8ebf982b88d3 | -5.70814 | -45.01173 | 2024-10-25 05:25:00 | AQUA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 0ce4ef71-5e57-3716-9b62-ff748fafe14b | -5.70029 | -45.00072 | 2024-10-25 05:25:00 | AQUA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 5942fb60-9f5e-3954-970e-36625444d5ae | -5.69889 | -45.01048 | 2024-10-25 05:25:00 | AQUA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 2c877973-5c33-3dc7-acc9-7897bcbdcaf4 | -5.09053 | -45.82673 | 2024-10-25 05:25:00 | AQUA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 97d9ba83-ab8f-355d-84a0-9d051c595188 | -7.53357 | -45.84087 | 2024-10-25 05:25:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 864877a0-0a27-320f-87a7-37d59728337c | -7.21242 | -45.57728 | 2024-10-25 05:25:00 | AQUA_M-M | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| cbcfbfc3-b4bc-38cc-aa53-cae1b222d760 | -7.21104 | -45.58677 | 2024-10-25 05:25:00 | AQUA_M-M | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| d38a99dd-8ff7-387b-bfdc-433463cfcd5d | -6.8528 | -45.89271 | 2024-10-25 05:25:00 | AQUA_M-M | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 9a2861fd-f217-3ef4-a2b0-6761a92f3032 | -9.26667 | -46.21948 | 2024-10-25 05:25:00 | AQUA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 7f6156f0-d9ec-3433-a3ff-0dd5ff8ffa14 | -9.14633 | -47.09842 | 2024-10-25 05:25:00 | AQUA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| f70a3c78-7992-33ad-b192-1d154deb5a82 | -9.145 | -47.10738 | 2024-10-25 05:25:00 | AQUA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 74efa38d-924e-3974-bad6-3c6a6895b20a | -8.50713 | -45.86973 | 2024-10-25 05:25:00 | AQUA_M-M | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 43e91dfa-f235-3fd9-a03d-e1a6cb13cb36 | -8.50574 | -45.87925 | 2024-10-25 05:25:00 | AQUA_M-M | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 10.6 |
| afcac208-cc8e-3497-8f7b-1abba4a1490d | -7.88933 | -46.68035 | 2024-10-25 05:25:00 | AQUA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 0b9dea5e-1826-3205-9c2c-3d50e98dfe21 | -3.20981 | -46.79982 | 2024-10-25 05:25:00 | AQUA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 57.1 |
| 3664954d-1768-30d4-ad48-9f1f03537e81 | -3.20094 | -46.79853 | 2024-10-25 05:25:00 | AQUA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 35.7 |
| 02a1cc0e-28cd-31b8-9a3e-2a04a83a73d1 | -2.60907 | -46.12959 | 2024-10-25 05:25:00 | AQUA_M-M | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 538cb4e1-7394-3494-be35-7632196730c7 | -4.77317 | -46.41383 | 2024-10-25 05:25:00 | AQUA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 21.8 |
| 77e84ec8-5023-3d99-8934-a5c13efb3d45 | -4.77185 | -46.42265 | 2024-10-25 05:25:00 | AQUA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 2e3d32fb-2231-31e4-baf5-772b597b20b2 | -4.76432 | -46.41253 | 2024-10-25 05:25:00 | AQUA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 4.6 |
| bf4cbc43-e113-399c-937d-b56929a9f591 | -4.43386 | -46.63648 | 2024-10-25 05:25:00 | AQUA_M-M | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 3bfb1710-7b79-3bf7-a019-e02617fa7cb7 | -4.37208 | -46.80751 | 2024-10-25 05:25:00 | AQUA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 7.2 |
| a02b4865-b2f0-35ee-9a77-019225fe0949 | -4.14858 | -46.82537 | 2024-10-25 05:25:00 | AQUA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 16.1 |
| 71850917-98ac-3e0a-a66d-ab913b9eba1b | -4.14725 | -46.83421 | 2024-10-25 05:25:00 | AQUA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 40.3 |
| 031b1337-fc15-3a27-9c50-5fa445c60f6c | -4.13839 | -46.83294 | 2024-10-25 05:25:00 | AQUA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 284cd85f-19e6-33f0-87fd-89b77122256f | -3.9501 | -46.42645 | 2024-10-25 05:25:00 | AQUA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 47.9 |
| 372c3f27-f526-3aed-a2dc-15e3bd9c4fa8 | -3.94879 | -46.43525 | 2024-10-25 05:25:00 | AQUA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 37.8 |
| 366a13ff-f617-35fc-b1ab-b57e8ce438fe | -3.94126 | -46.42516 | 2024-10-25 05:25:00 | AQUA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 18.7 |
| 4a1cc564-a020-351a-9526-84e4c947491c | -3.93995 | -46.43396 | 2024-10-25 05:25:00 | AQUA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 5bd199a8-480d-3d00-90e6-18aced36c37e | -3.93242 | -46.42387 | 2024-10-25 05:25:00 | AQUA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 9fc82dca-41e2-3883-9c45-46cd73b18ec6 | -3.87244 | -46.44524 | 2024-10-25 05:25:00 | AQUA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.3 |
| bf25cfd2-644d-3ea1-b7ad-93199869ab2e | -3.80992 | -46.92249 | 2024-10-25 05:25:00 | AQUA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 4.4 |


[Clique aqui para ver as próximas entradas](README106.md)
