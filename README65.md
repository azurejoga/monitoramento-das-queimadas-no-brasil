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

## Dados Diários - Página 65

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8339ff77-a01b-3342-ac74-5d2669256e60 | -3.28 | -42.05 | 2024-11-16 13:00:00 | MSG-03 | MURICI DOS PORTELAS | PIAUÍ | Brasil | 2206696 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| fe17fa06-191b-3f04-bc19-0aadcb5036d6 | -3.31 | -42.05 | 2024-11-16 13:00:00 | MSG-03 | MURICI DOS PORTELAS | PIAUÍ | Brasil | 2206696 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 7d96ad36-2ffa-3e1a-891e-07be4525d215 | -16.0466 | -60.119 | 2024-11-16 13:10:00 | GOES-16 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 131.4 |
| d12a3f37-854b-3598-bf38-ce6567bcb0d9 | -19.5422 | -56.9289 | 2024-11-16 13:10:00 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 63.6 |
| 3221eae1-fae6-3b48-924a-be6d65c0c680 | -19.5225 | -56.9108 | 2024-11-16 13:10:00 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 77.9 |
| cb9950df-00ec-315b-9f23-60715be17620 | -17.2543 | -57.4698 | 2024-11-16 13:10:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 86.8 |
| 8139894d-9241-3825-b35a-66b88ab4b818 | -3.8348 | -42.1455 | 2024-11-16 13:10:00 | GOES-16 | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 110.5 |
| ab3959c4-988c-3721-a0eb-61eadc72d907 | -3.4787 | -42.3058 | 2024-11-16 13:10:00 | GOES-16 | LUZILÂNDIA | PIAUÍ | Brasil | 2205805 | 22 | 33 | nan | nan | nan | Cerrado | 83.3 |
| 94276454-1453-3615-8c06-500410722513 | -3.6489 | -41.9652 | 2024-11-16 13:10:00 | GOES-16 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 332.2 |
| d6a458ea-fe8c-3cab-94e8-0721bb7df507 | -3.6836 | -42.4138 | 2024-11-16 13:10:00 | GOES-16 | LUZILÂNDIA | PIAUÍ | Brasil | 2205805 | 22 | 33 | nan | nan | nan | Caatinga | 82.7 |
| eaadf9e7-17be-3886-9e97-6ca8f459d25a | -3.2932 | -42.0539 | 2024-11-16 13:10:00 | GOES-16 | MURICI DOS PORTELAS | PIAUÍ | Brasil | 2206696 | 22 | 33 | nan | nan | nan | Cerrado | 149.8 |
| f9a4ae6e-0a9a-31a3-ac34-549ce99f8ef5 | -16.9577 | -57.6473 | 2024-11-16 13:10:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 104.9 |
| a764c5bc-9a10-34e4-8f69-7a2f498cc7d6 | -2.2482 | -47.2093 | 2024-11-16 13:10:00 | GOES-16 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 77.3 |
| 193cacc6-0b31-3a69-a2a6-b0b79b3fb066 | -19.5426 | -56.908 | 2024-11-16 13:10:00 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 124.5 |
| 66983687-ace4-3a07-852d-349e84ef6c8b | -19.5426 | -56.908 | 2024-11-16 13:20:00 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 108.8 |
| 053eb3b6-dce7-3c41-bd3f-4bc6b8f09d01 | -3.6836 | -42.4138 | 2024-11-16 13:20:00 | GOES-16 | LUZILÂNDIA | PIAUÍ | Brasil | 2205805 | 22 | 33 | nan | nan | nan | Caatinga | 80.9 |
| 07e5f8db-4ca0-3dc0-bbdb-7a600538b1c7 | -16.9384 | -57.6291 | 2024-11-16 13:20:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 141.5 |
| 545e5296-23df-3c87-a5a5-590404192e8f | -0.7837 | -49.4916 | 2024-11-16 13:20:00 | GOES-16 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 94.9 |
| 4101dfc4-3097-3336-a1cc-b5f9998f5fd1 | -3.8348 | -42.1455 | 2024-11-16 13:20:00 | GOES-16 | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 96.1 |
| 56acf54e-32be-32a1-9de6-9c368f85e8ae | -16.9577 | -57.6473 | 2024-11-16 13:20:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 121.1 |
| d5f4e3bb-7221-3dbc-9be3-86c5c37f0fc4 | -19.5225 | -56.9108 | 2024-11-16 13:20:00 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 73.0 |
| ec9ccfea-3cb7-348d-9cb2-d59182aba353 | -16.0466 | -60.119 | 2024-11-16 13:20:00 | GOES-16 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 116.3 |
| 47cabb03-f030-3736-b5e8-70fda6bdf070 | -6.9424 | -42.8126 | 2024-11-16 13:20:00 | GOES-16 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 74.4 |
| aa8e00dd-304c-30cc-8f47-f960115b37a3 | -17.2933 | -57.4857 | 2024-11-16 13:20:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 83.0 |
| 29fc7504-63e2-3a82-bfbc-ad2443fefdc8 | -3.6489 | -41.9652 | 2024-11-16 13:20:00 | GOES-16 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 183.4 |
| 8af530cb-55a3-38bb-928d-3f01d24f7f24 | -19.5422 | -56.9289 | 2024-11-16 13:20:00 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 63.3 |
| 88d347c2-f7de-3661-a6e9-083d0cce865d | -3.4787 | -42.3058 | 2024-11-16 13:20:00 | GOES-16 | LUZILÂNDIA | PIAUÍ | Brasil | 2205805 | 22 | 33 | nan | nan | nan | Cerrado | 90.2 |
| 44b12aaa-331b-3c45-9ff0-64e8db14c169 | -4.8041 | -40.3228 | 2024-11-16 13:20:00 | GOES-16 | TAMBORIL | CEARÁ | Brasil | 2313203 | 23 | 33 | nan | nan | nan | Caatinga | 117.9 |
| 60a2182e-3d59-35f7-ba79-5cafe7b25357 | -23.9517 | -54.0521 | 2024-11-16 13:30:00 | GOES-16 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 68.3 |
| 4cd5842b-90ec-3d8a-98ab-fb6efda25045 | -17.2963 | -57.3008 | 2024-11-16 13:30:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 84.9 |
| 0109cf1c-fcc8-3545-b9f1-9c006a77df6d | -4.8209 | -42.9122 | 2024-11-16 13:30:00 | GOES-16 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 75.5 |
| 037d4289-dff5-3751-94d4-8db5611956ce | -17.5885 | -57.4506 | 2024-11-16 13:30:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 95.8 |
| 4f816b5f-1d7e-38ba-935e-d91cc78944e3 | -16.9384 | -57.6291 | 2024-11-16 13:30:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 153.1 |
| d07f29b2-745e-3471-97fe-a244417e8b7e | -17.5688 | -57.4529 | 2024-11-16 13:30:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 91.7 |
| 5502c080-5354-33a4-b53c-899d0b4a28fb | -16.0466 | -60.119 | 2024-11-16 13:30:00 | GOES-16 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 116.5 |
| 2babd7e6-0721-37ad-8015-359f5a85729b | -17.5692 | -57.4324 | 2024-11-16 13:30:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 96.9 |
| 73ec1c9a-df74-3823-b9b3-22a0110ea446 | -17.2186 | -57.2485 | 2024-11-16 13:30:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 86.1 |
| 1543bfb6-122f-3957-a637-2ee6e7d1219a | -17.5882 | -57.4711 | 2024-11-16 13:30:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 103.2 |
| a226e417-105c-354d-8a34-403d7f482de8 | -17.2933 | -57.4857 | 2024-11-16 13:30:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 83.9 |
| efd7ae9d-96a3-3982-bf96-c6b09bdd0bf9 | -19.5426 | -56.908 | 2024-11-16 13:30:00 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 109.4 |
| 8a4acc26-1647-32af-90d7-582eaed3f27b | -17.5879 | -57.4917 | 2024-11-16 13:30:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 96.6 |
| 4d6bd253-a179-32a4-8d92-92c671fd4a09 | -0.7837 | -49.4916 | 2024-11-16 13:30:00 | GOES-16 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 77.5 |
| abe274ed-d136-3046-96b5-3c89c015a828 | -19.5225 | -56.9108 | 2024-11-16 13:30:00 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 66.1 |
| cf6b0967-1e54-3508-8646-c9c782885a75 | -2.2482 | -47.2093 | 2024-11-16 13:30:00 | GOES-16 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 109.7 |
| afdb9a2c-7793-33e9-ba4a-f5227a207072 | -19.5422 | -56.9289 | 2024-11-16 13:30:00 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 66.2 |
| 71e1721e-36ef-37d6-8bde-73af70caf939 | -23.9306 | -54.0564 | 2024-11-16 13:30:00 | GOES-16 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 67.7 |
| a98d0e6a-bb4a-3614-878d-223c3f4f1aee | -3.6489 | -41.9652 | 2024-11-16 13:30:00 | GOES-16 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 130.4 |
| 7ebe376c-0cc7-36c0-8411-686d8dd156da | -16.9577 | -57.6473 | 2024-11-16 13:30:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 118.5 |
| 42caa5ea-6123-3db7-800d-8cc1a51b3424 | -3.2932 | -42.0539 | 2024-11-16 13:30:00 | GOES-16 | MURICI DOS PORTELAS | PIAUÍ | Brasil | 2206696 | 22 | 33 | nan | nan | nan | Cerrado | 81.8 |
| 452d1d08-2afc-30e4-8419-8cba4444a08b | -17.235 | -57.4516 | 2024-11-16 13:30:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 115.5 |
| d093b2e8-a0a7-339a-a3b2-0b02ec8d4351 | -8.2532 | -36.8489 | 2024-11-16 13:30:00 | GOES-16 | PESQUEIRA | PERNAMBUCO | Brasil | 2610905 | 26 | 33 | nan | nan | nan | Caatinga | 108.3 |
| 60fa2454-ed26-34e8-b651-d3e3841075c7 | -4.2362 | -46.5415 | 2024-11-16 13:30:00 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 80.6 |
| 50738469-662d-3265-9988-345f8b38143b | -17.5889 | -57.43 | 2024-11-16 13:30:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 88.7 |
| 36b0a8e5-27bc-37e3-b1a8-c7775bf91d83 | -6.1621 | -38.3264 | 2024-11-16 13:30:00 | GOES-16 | ENCANTO | RIO GRANDE DO NORTE | Brasil | 2403301 | 24 | 33 | nan | nan | nan | Caatinga | 126.2 |
| e2cc62d1-228c-3910-88b4-d9a48d7eff87 | -19.5426 | -56.908 | 2024-11-16 13:40:00 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 105.4 |
| ed2a99e2-ea4b-34d9-9c06-6bcf46f81f83 | -16.9413 | -57.4449 | 2024-11-16 13:40:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 85.1 |
| 130bd111-2a5c-3db8-a9e7-08361dec495c | -0.6547 | -49.3866 | 2024-11-16 13:40:00 | GOES-16 | SANTA CRUZ DO ARARI | PARÁ | Brasil | 1506401 | 15 | 33 | nan | nan | nan | Amazônia | 75.0 |
| fe8ea830-cc9f-334b-b2f9-750810428c4b | -17.6865 | -57.4798 | 2024-11-16 13:40:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 84.3 |
| 22c8faae-a93c-32c4-8b00-39c6dad4e0b1 | -16.9577 | -57.6473 | 2024-11-16 13:40:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 111.9 |
| 98a1119d-c16d-3459-8962-069c1ced954c | -4.0244 | -44.6677 | 2024-11-16 13:40:00 | GOES-16 | SÃO MATEUS DO MARANHÃO | MARANHÃO | Brasil | 2111508 | 21 | 33 | nan | nan | nan | Amazônia | 76.1 |
| 1bfebd6a-509b-3ed4-9603-de66d12c3818 | -16.9388 | -57.6086 | 2024-11-16 13:40:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 94.8 |
| 235878a6-18da-3c7f-83e6-caa3dcac3ff8 | -19.5225 | -56.9108 | 2024-11-16 13:40:00 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 68.7 |
| daba7e0c-12e2-3276-b0e7-a26265848d06 | -16.9384 | -57.6291 | 2024-11-16 13:40:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 190.7 |
| d9dd3e5b-bd11-33e1-b5cc-b0f303d546a7 | -19.5422 | -56.9289 | 2024-11-16 13:40:00 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 61.4 |
| dcda7afa-d24f-359b-ae58-419a814a5141 | -0.7837 | -49.4916 | 2024-11-16 13:40:00 | GOES-16 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 90.1 |
| 183f96b1-9ac8-3392-9804-a309111a770e | -4.8209 | -42.9122 | 2024-11-16 13:40:00 | GOES-16 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 127.8 |
| 3cb7cdd4-cd04-3b54-aa79-bfe865e59bc3 | -3.9021 | -40.4309 | 2024-11-16 13:40:00 | GOES-16 | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 100.4 |
| 606a5c73-f252-3a2f-b33e-846385a8ccba | -4.2362 | -46.5415 | 2024-11-16 13:40:00 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 76.3 |
| 31f5ec4e-3cff-3773-96f9-b62b3abfb222 | -18.7574 | -57.3046 | 2024-11-16 13:40:00 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 65.1 |
| 25363c9b-d4f0-38a7-9f43-59d5dad1aec1 | -16.9773 | -57.6451 | 2024-11-16 13:40:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 81.8 |
| 2717417e-e4d9-338d-b1c9-91436302a234 | -16.0466 | -60.119 | 2024-11-16 13:40:00 | GOES-16 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 95.5 |
| dec4300f-1d17-3c4b-8642-f568e2668028 | -3.6233 | -43.1443 | 2024-11-16 13:50:00 | GOES-16 | MATA ROMA | MARANHÃO | Brasil | 2106409 | 21 | 33 | nan | nan | nan | Cerrado | 97.0 |
| cd56733d-30c5-3d22-bbf4-71367cc8b05c | -16.9384 | -57.6291 | 2024-11-16 13:50:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 229.4 |
| f872995b-b79c-30d6-ad14-b4ec9a7b99db | -19.5426 | -56.908 | 2024-11-16 13:50:00 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 111.8 |
| 9b0bfcc3-3cc0-3a44-a50b-7e3d72fd9c87 | -4.8209 | -42.9122 | 2024-11-16 13:50:00 | GOES-16 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 125.5 |
| 24cd4ef0-71ed-3baa-aa22-ca042278c4ea | -16.0466 | -60.119 | 2024-11-16 13:50:00 | GOES-16 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 88.0 |
| 6bf43133-8902-392a-b524-dbaedbadf27a | -19.5422 | -56.9289 | 2024-11-16 13:50:00 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 67.6 |
| 9df29e5d-369a-3043-be37-bd47f1f07508 | -17.2737 | -57.488 | 2024-11-16 13:50:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 81.2 |
| 34d8da3f-9cf9-3a2d-b5fe-cf899e49d91d | -23.9517 | -54.0521 | 2024-11-16 13:50:00 | GOES-16 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 68.5 |
| 26551e1f-4877-3dd4-a5db-ce9536874c55 | -16.9388 | -57.6086 | 2024-11-16 13:50:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 114.9 |
| b0e7623f-ee92-3050-b998-931269b78fbc | -23.9306 | -54.0564 | 2024-11-16 13:50:00 | GOES-16 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 71.0 |
| 57ded747-b69d-3612-8531-e18bb94c090f | -0.7837 | -49.4916 | 2024-11-16 13:50:00 | GOES-16 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 87.6 |
| 8383123e-5f67-36d0-91fa-f8e5eb0484b1 | -16.9773 | -57.6451 | 2024-11-16 13:50:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 83.3 |
| 02ef934a-0e73-3988-8b61-d75f19e35719 | -3.7867 | -43.9011 | 2024-11-16 13:50:00 | GOES-16 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 75.2 |
| 9499a8f8-c2da-3f69-be31-1eb25070600d | -6.2022 | -41.6427 | 2024-11-16 13:50:00 | GOES-16 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 74.9 |
| 55d3af83-a3c8-3d99-b760-6f516ead32aa | -16.9381 | -57.6495 | 2024-11-16 13:50:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 82.9 |
| 67b5e72e-5306-33a9-8998-721ec1c8ae3f | -0.6547 | -49.3866 | 2024-11-16 13:50:00 | GOES-16 | SANTA CRUZ DO ARARI | PARÁ | Brasil | 1506401 | 15 | 33 | nan | nan | nan | Amazônia | 98.7 |
| 4d77ff12-0604-3b76-9218-010e47fd9a20 | -18.7574 | -57.3046 | 2024-11-16 13:50:00 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 66.7 |
| 6f7fc366-c804-3554-ab23-4a3a2b489cb7 | -16.9577 | -57.6473 | 2024-11-16 13:50:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 105.5 |
| b18b8952-1a15-3206-b170-630184715bbd | -19.5225 | -56.9108 | 2024-11-16 13:50:00 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 62.2 |
| ca432d69-0128-3fef-9def-cfb3f4815dee | -23.9512 | -54.0744 | 2024-11-16 13:50:00 | GOES-16 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 66.1 |
| 70a28805-348e-384b-be54-c182979cafef | -23.9306 | -54.0564 | 2024-11-16 14:00:00 | GOES-16 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 94.6 |
| 72cf59ce-9202-308f-9a90-1698aa95b55c | -17.2353 | -57.4311 | 2024-11-16 14:00:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 93.2 |
| 2e4f6279-5bfe-3afc-b8ea-9ec4baa54b3e | -16.9577 | -57.6473 | 2024-11-16 14:00:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 106.3 |
| ca5a1b9e-63e4-399c-b496-4691473382b4 | -1.0258 | -47.7541 | 2024-11-16 14:00:00 | GOES-16 | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 70.6 |
| ccba55e0-da03-39c9-b609-0b07b394baf7 | -0.6547 | -49.3866 | 2024-11-16 14:00:00 | GOES-16 | SANTA CRUZ DO ARARI | PARÁ | Brasil | 1506401 | 15 | 33 | nan | nan | nan | Amazônia | 84.1 |
| 880e87dc-e785-3c6a-902c-6d66d481a76e | -3.6472 | -42.2501 | 2024-11-16 14:00:00 | GOES-16 | MORRO DO CHAPÉU DO PIAUÍ | PIAUÍ | Brasil | 2206670 | 22 | 33 | nan | nan | nan | Caatinga | 138.5 |
| 9f8405b1-2fb6-32d5-8b82-1ca6f735238b | -3.7597 | -42.1969 | 2024-11-16 14:00:00 | GOES-16 | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 273.4 |
| 15d73212-284b-3837-9359-9d5f8332ddb9 | -17.6283 | -57.4252 | 2024-11-16 14:00:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 91.5 |
| 4a8c8026-63cd-3bea-b5f4-4a9056e6ac86 | -23.9517 | -54.0521 | 2024-11-16 14:00:00 | GOES-16 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 78.0 |


[Clique aqui para ver as próximas entradas](README66.md)
