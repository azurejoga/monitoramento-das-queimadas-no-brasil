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
| 961ba07c-378d-3dcd-9def-3a9657e7fe52 | -9.2033 | -59.641998 | 2025-08-19 01:27:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6367d580-b634-3c99-89b5-bb4ced5b14bb | -9.1156 | -60.335899 | 2025-08-19 01:27:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a2a737b5-a407-3fa5-9ff8-49eaf58ea1c0 | -10.0387 | -59.352299 | 2025-08-19 01:27:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9a322fcb-25a5-37b0-9a1b-26971148b573 | -13.1628 | -54.9314 | 2025-08-19 01:27:00 | METOP-B | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5665d258-d2a4-37cd-8ebd-a260d9ce5230 | -13.1532 | -54.9342 | 2025-08-19 01:27:00 | METOP-B | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 466bb564-2c0e-3264-ad1f-d2471a0ca801 | -13.02 | -56.838299 | 2025-08-19 01:27:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c0639099-6245-3e50-9ea9-2696e0d9b1df | -14.9811 | -54.822399 | 2025-08-19 01:27:00 | METOP-B | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| b7102782-25ed-329e-b771-60828dcf645b | -7.7947 | -66.956398 | 2025-08-19 01:27:00 | METOP-B | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 475fd0b4-2ce6-38ce-b50b-202a2c146e8d | -9.1936 | -59.644402 | 2025-08-19 01:27:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5718ec2d-085f-3f09-8416-c4f3409df77c | -10.0424 | -59.367298 | 2025-08-19 01:27:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7618847f-c940-3891-abf7-2fbd6a5c5d3c | -8.9727 | -60.511398 | 2025-08-19 01:27:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 92ac281f-f23f-3152-905e-7ccc5eeac12a | -9.1742 | -59.6493 | 2025-08-19 01:27:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 33b7939d-4f4b-38bf-877f-863472d150bf | -15.0194 | -54.811199 | 2025-08-19 01:27:00 | METOP-B | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 31b8ffc0-9901-3f9d-ac63-527e81fe791d | -9.19 | -59.629601 | 2025-08-19 01:27:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 75efb35d-c2d0-35ea-8876-d56c837fc32c | -7.4513 | -63.034801 | 2025-08-19 01:27:00 | METOP-B | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| efb6f8cc-3f00-3aa9-a70b-eb2700438e8a | -7.9328 | -63.285702 | 2025-08-19 01:27:00 | METOP-B | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 594d8a9b-6b6f-36c3-8e70-58f423dfe9b9 | -23.7661 | -51.999001 | 2025-08-19 01:27:00 | METOP-B | ITAMBÉ | PARANÁ | Brasil | 4111100 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |
| e0929e36-eaaa-3684-9e7d-807ebea09463 | -9.0734 | -60.416801 | 2025-08-19 01:27:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9385410d-2e84-34f9-8e04-af0316262eda | -8.9695 | -60.498299 | 2025-08-19 01:27:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 846cdc1a-09fb-3688-b843-d7e2e2110962 | -23.758301 | -51.972698 | 2025-08-19 01:27:00 | METOP-B | ITAMBÉ | PARANÁ | Brasil | 4111100 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 40dc9b48-b3f2-38e7-a1aa-9c7e45aa43be | -13.0104 | -56.841 | 2025-08-19 01:27:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e12d8f74-84d7-3d51-b670-ae3aceaa1e39 | -15.029 | -54.808399 | 2025-08-19 01:27:00 | METOP-B | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 668a053d-2513-315d-aed9-1c2e77cf04de | -8.4378 | -63.859001 | 2025-08-19 01:27:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 5c25b459-3507-3a6b-b560-98d77c41cd8a | -9.0766 | -60.430099 | 2025-08-19 01:27:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0ea2371e-ea41-32a9-86e8-879158ab4928 | -8.7642 | -64.198799 | 2025-08-19 01:27:00 | METOP-B | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3e20e3d1-c3d5-3bca-b844-1c9135ba76d2 | -14.9742 | -54.797401 | 2025-08-19 01:27:00 | METOP-B | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| e276096c-8601-36cd-86dd-8baa042ee758 | -14.9907 | -54.819599 | 2025-08-19 01:27:00 | METOP-B | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| b4a3eb7d-0747-306d-ba27-97a3cfd553eb | -12.2271 | -64.229797 | 2025-08-19 01:27:00 | METOP-B | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 562d4de2-8a02-3d07-b7d5-7d66b5633a72 | -19.9433 | -48.1957 | 2025-08-19 01:30:00 | GOES-19 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 145.3 |
| b1a08f3f-5342-33fc-b680-22789fa4f35a | -6.9715 | -43.5833 | 2025-08-19 01:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 108.6 |
| 9af101d9-99d3-3a00-9395-a3aae64df80a | -6.9712 | -43.6066 | 2025-08-19 01:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 97.6 |
| 28b13b06-72be-3370-aa3d-777eb873438e | -19.9426 | -48.2189 | 2025-08-19 01:30:00 | GOES-19 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 118.1 |
| af64d711-43df-3738-9e9f-90d2f350d449 | -4.0007 | -42.5149 | 2025-08-19 01:30:00 | GOES-19 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 76.4 |
| fa7e9dc9-6931-34de-b81d-35c81432f9fc | -14.9812 | -54.7951 | 2025-08-19 01:30:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 72.9 |
| 3da747f6-5599-32e4-8939-91a66c7a67e1 | -6.9336 | -43.6101 | 2025-08-19 01:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 90.4 |
| cbdd6595-d1a5-3774-bb2d-65e184e778a6 | -17.5729 | -44.4764 | 2025-08-19 01:30:00 | GOES-19 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 64.1 |
| c88206e3-e2b3-3d45-8107-64ad66a66b81 | -16.4863 | -45.0702 | 2025-08-19 01:30:00 | GOES-19 | PONTO CHIQUE | MINAS GERAIS | Brasil | 3152131 | 31 | 33 | nan | nan | nan | Cerrado | 95.4 |
| 553752f4-ba3b-38ad-b1c5-698e03748faf | -14.9809 | -54.8158 | 2025-08-19 01:30:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 55.5 |
| 06a350ee-86b2-3109-8ec3-0cb7fd759683 | -13.2563 | -50.8162 | 2025-08-19 01:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 95.9 |
| 2d07e3f1-ab0e-388f-b60e-dc5f74faa1d8 | -3.9819 | -42.5396 | 2025-08-19 01:30:00 | GOES-19 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 50.9 |
| 00f6cbe6-5c65-32a2-8154-0b3b8cceae8c | -9.1895 | -59.6364 | 2025-08-19 01:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 57.8 |
| 298525bf-4e40-36d8-8309-0b7a625ed49f | -15.0389 | -54.8089 | 2025-08-19 01:30:00 | GOES-19 | CAMPO VERDE | MATO GROSSO | Brasil | 5102678 | 51 | 33 | nan | nan | nan | Cerrado | 50.8 |
| 31173a67-f760-302b-993f-7517d7b708ae | -16.4659 | -45.098 | 2025-08-19 01:30:00 | GOES-19 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 83.2 |
| 08d2371f-1760-3db4-92fd-67b365f40f06 | -3.982 | -42.516 | 2025-08-19 01:30:00 | GOES-19 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 128.5 |
| 8e527efd-1e5d-3510-9875-a33a2ab42c42 | -16.4857 | -45.0939 | 2025-08-19 01:30:00 | GOES-19 | PONTO CHIQUE | MINAS GERAIS | Brasil | 3152131 | 31 | 33 | nan | nan | nan | Cerrado | 250.7 |
| d96543d9-68e4-3574-a84b-5889fc4bbfc6 | -19.9636 | -48.1912 | 2025-08-19 01:30:00 | GOES-19 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 50.7 |
| 5e60ef2f-f894-3fbe-94db-2a3e083e443f | -6.9524 | -43.6083 | 2025-08-19 01:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 145.3 |
| 62aea347-178f-3466-befc-746e250706ee | -6.9339 | -43.5868 | 2025-08-19 01:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 93.4 |
| 9004e27f-c87f-34f3-a274-490d9f635dd5 | -13.1555 | -54.9357 | 2025-08-19 01:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 41.2 |
| 0a981a8f-7d1c-379b-99d6-b6a2d25f60a8 | -16.4851 | -45.1176 | 2025-08-19 01:30:00 | GOES-19 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 89.0 |
| 880d952f-6067-3a51-bcff-c20f43ee3a04 | -6.9527 | -43.585 | 2025-08-19 01:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 124.6 |
| 724ad5a7-e961-3190-ac7c-1729b6a06e71 | -6.9339 | -43.5868 | 2025-08-19 01:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 110.1 |
| 859e9e38-7d48-34c5-9f48-3f8d9e3da4a3 | -3.982 | -42.516 | 2025-08-19 01:40:00 | GOES-19 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 119.4 |
| d4c4ee35-40b4-3ffd-a56c-980a82159235 | -16.4857 | -45.0939 | 2025-08-19 01:40:00 | GOES-19 | PONTO CHIQUE | MINAS GERAIS | Brasil | 3152131 | 31 | 33 | nan | nan | nan | Cerrado | 159.2 |
| 7fac9d6c-7f0e-3647-92dc-c3092270f0d3 | -14.9812 | -54.7951 | 2025-08-19 01:40:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 70.7 |
| ebcbdf61-5815-36c7-bb6e-c70958749e42 | -9.1895 | -59.6364 | 2025-08-19 01:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 56.2 |
| 2e48f031-5be9-3982-af68-1571487195f7 | -6.9527 | -43.585 | 2025-08-19 01:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 100.2 |
| 739502db-308d-3aba-a2d6-e6dc6bde69bf | -6.9336 | -43.6101 | 2025-08-19 01:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 94.2 |
| e49b0209-3aba-39ff-808c-a6e6bf671ddc | -6.9524 | -43.6083 | 2025-08-19 01:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 118.7 |
| 8bad13ee-a98b-3634-ba07-64ea8b5b790d | -5.7887 | -43.6134 | 2025-08-19 01:40:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 51.7 |
| 51d85d4b-082f-34cf-aab6-b82605f36953 | -16.4659 | -45.098 | 2025-08-19 01:40:00 | GOES-19 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 93.1 |
| 6e63f7fc-1ca1-3d31-835d-3a3e93ab5089 | -14.9809 | -54.8158 | 2025-08-19 01:40:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 57.8 |
| 577fd07d-8909-3332-9366-51f18ac36195 | -17.5736 | -44.4523 | 2025-08-19 01:40:00 | GOES-19 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 66.0 |
| 7ae1f2b2-910d-300d-9ae6-e09c8a94a8e4 | -6.9715 | -43.5833 | 2025-08-19 01:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 128.9 |
| 9880cde0-6e6f-31cb-a92e-e91d235fb516 | -4.0007 | -42.5149 | 2025-08-19 01:40:00 | GOES-19 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 53.8 |
| 5db701e3-3fb7-35bd-bad4-d159311278b4 | -15.0389 | -54.8089 | 2025-08-19 01:40:00 | GOES-19 | CAMPO VERDE | MATO GROSSO | Brasil | 5102678 | 51 | 33 | nan | nan | nan | Cerrado | 82.1 |
| e2d703a2-ab72-320d-920c-93a35fe8f096 | -17.5729 | -44.4764 | 2025-08-19 01:40:00 | GOES-19 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 94.3 |
| e4d15495-8c94-3fc0-95ad-f3d8db516e99 | -6.9712 | -43.6066 | 2025-08-19 01:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 115.9 |
| 28396998-bf2d-37de-8cfa-93b45bee28a9 | -16.4857 | -45.0939 | 2025-08-19 01:50:00 | GOES-19 | PONTO CHIQUE | MINAS GERAIS | Brasil | 3152131 | 31 | 33 | nan | nan | nan | Cerrado | 165.5 |
| 35b4d909-f1b3-365a-90d2-98479277509a | -16.4659 | -45.098 | 2025-08-19 01:50:00 | GOES-19 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 74.4 |
| 45ba4f49-f594-3843-b05f-feabff9aad32 | -6.9712 | -43.6066 | 2025-08-19 01:50:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 89.5 |
| 34409b7b-70a8-3548-95f1-a1b81d214790 | -5.7887 | -43.6134 | 2025-08-19 01:50:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 55.6 |
| d5e91b1b-455e-3b8b-93dc-8fc849052ac8 | -6.9524 | -43.6083 | 2025-08-19 01:50:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 116.2 |
| f7d1894a-17d8-319b-a7f2-b935378cf3b9 | -3.982 | -42.516 | 2025-08-19 01:50:00 | GOES-19 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 83.7 |
| b439d854-6494-3da9-b406-96e282c585f9 | -6.9339 | -43.5868 | 2025-08-19 01:50:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 111.2 |
| b077dcc3-4037-3e92-8773-3a9a0384fd0d | -15.0389 | -54.8089 | 2025-08-19 01:50:00 | GOES-19 | CAMPO VERDE | MATO GROSSO | Brasil | 5102678 | 51 | 33 | nan | nan | nan | Cerrado | 76.3 |
| 9ec98247-adbd-3574-afc0-9e48974f4e68 | -9.1895 | -59.6364 | 2025-08-19 01:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 51.9 |
| 9bb441a0-f29c-35be-a97b-7a54705d3bc5 | -14.9809 | -54.8158 | 2025-08-19 01:50:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 59.7 |
| cb7617b5-3d32-3fb9-a83a-cd8efb27825a | -16.4863 | -45.0702 | 2025-08-19 01:50:00 | GOES-19 | PONTO CHIQUE | MINAS GERAIS | Brasil | 3152131 | 31 | 33 | nan | nan | nan | Cerrado | 86.8 |
| 37d91328-df1f-3bc3-a382-c663edf23450 | -6.9715 | -43.5833 | 2025-08-19 01:50:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 128.6 |
| bfbaee08-010b-353d-b094-3a32287514f5 | -6.9336 | -43.6101 | 2025-08-19 01:50:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 77.7 |
| 3dcd8835-949c-39e6-bcdf-e8d22b00d4e3 | -6.9527 | -43.585 | 2025-08-19 01:50:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 115.0 |
| 6c413596-b6f9-3de7-92f9-43740fac5f7b | -15.0196 | -54.8112 | 2025-08-19 01:50:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 48.3 |
| 5fe12d75-0eb8-3eff-8d6e-e1e327fa3d08 | -14.9812 | -54.7951 | 2025-08-19 01:50:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 69.9 |
| 965d8d5f-4bf8-3e79-9261-b35f73467b56 | -3.982 | -42.516 | 2025-08-19 02:00:00 | GOES-19 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 86.9 |
| ae9de249-bfa9-3a52-95a6-c318431babfe | -14.9809 | -54.8158 | 2025-08-19 02:00:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 74.0 |
| 0b7457d8-2122-3e7c-a697-c789e57a002d | -6.9524 | -43.6083 | 2025-08-19 02:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 116.4 |
| 9befdc68-7e72-3d21-b2b7-7ee7801df21a | -14.9812 | -54.7951 | 2025-08-19 02:00:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 90.3 |
| c951da33-d275-332a-8198-53dc5ebcacc5 | -6.9527 | -43.585 | 2025-08-19 02:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 113.6 |
| abd814e8-5fb8-3a60-ae3e-73a6bdcd074b | -6.9715 | -43.5833 | 2025-08-19 02:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 99.9 |
| 79b233af-8450-3176-a0bb-7642dac80ec3 | -6.9712 | -43.6066 | 2025-08-19 02:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 76.8 |
| 9b03d692-35c2-3dbd-9971-7dd64385ddff | -16.4857 | -45.0939 | 2025-08-19 02:00:00 | GOES-19 | PONTO CHIQUE | MINAS GERAIS | Brasil | 3152131 | 31 | 33 | nan | nan | nan | Cerrado | 116.9 |
| 1dd4f099-362a-39dd-9750-5efe824206b4 | -16.4863 | -45.0702 | 2025-08-19 02:00:00 | GOES-19 | PONTO CHIQUE | MINAS GERAIS | Brasil | 3152131 | 31 | 33 | nan | nan | nan | Cerrado | 64.2 |
| 2bc447d3-303a-37fd-815e-43655c6b8b0d | -6.9339 | -43.5868 | 2025-08-19 02:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 95.3 |
| 852d8b66-620a-35cb-a74d-baa953c3b0f9 | -6.9336 | -43.6101 | 2025-08-19 02:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 81.1 |
| 18fb2df6-65e2-369d-a14c-507104c9fa5e | -14.9812 | -54.7951 | 2025-08-19 02:10:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 41.5 |
| 4ba6d209-e17b-3fcc-a259-83e5b4c78392 | -6.9524 | -43.6083 | 2025-08-19 02:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 118.3 |
| 770d4a34-f52d-3cb5-903b-25e232b8b138 | -16.4857 | -45.0939 | 2025-08-19 02:10:00 | GOES-19 | PONTO CHIQUE | MINAS GERAIS | Brasil | 3152131 | 31 | 33 | nan | nan | nan | Cerrado | 114.9 |
| eefa8c5c-0ca0-3d30-878f-3a190f52ae5a | -16.4863 | -45.0702 | 2025-08-19 02:10:00 | GOES-19 | PONTO CHIQUE | MINAS GERAIS | Brasil | 3152131 | 31 | 33 | nan | nan | nan | Cerrado | 72.7 |
| 95775c43-d70c-3f85-8f6a-22f6d4855246 | -15.0196 | -54.8112 | 2025-08-19 02:10:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 54.2 |


[Clique aqui para ver as próximas entradas](README11.md)
