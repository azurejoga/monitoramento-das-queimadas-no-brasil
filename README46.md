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

## Dados Diários - Página 46

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4a7fc13c-e9bc-34be-9596-405ef8dea236 | -17.61934 | -57.43297 | 2024-11-11 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 3adac278-70d3-374a-a2b7-57c0e6ed2f55 | -16.94481 | -57.65203 | 2024-11-11 05:40:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 62f88c58-4743-3488-b8c5-6b06b9383283 | -17.60324 | -57.53236 | 2024-11-11 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.2 |
| 7ebe5aa6-bc86-3f8e-97c1-4abd379837c5 | -17.60289 | -57.53557 | 2024-11-11 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.9 |
| 23e0f219-bd17-3217-891c-304fa2793b87 | -17.6349 | -57.5299 | 2024-11-11 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 42.2 |
| c71786a4-3d29-3de5-8023-4b0ca76fb760 | -17.71183 | -57.51299 | 2024-11-11 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| c5c91c22-2d9c-3455-8c81-8cdd2fe18fb1 | -17.61836 | -57.53755 | 2024-11-11 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.6 |
| 17f4a521-d497-3ead-8f59-b6d94fb1177e | -17.23502 | -57.49586 | 2024-11-11 05:40:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| a25f3d04-bd1b-30f3-a259-fb95cc987d7c | -17.6342 | -57.44145 | 2024-11-11 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 9d38ac05-9bb0-36a8-a5cc-e64731978d90 | -17.62903 | -57.53565 | 2024-11-11 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.2 |
| ca438deb-3e56-3ff9-90cf-eb76e35bd3b7 | -17.30921 | -57.48602 | 2024-11-11 05:40:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 922de2fb-d4d6-33a3-97bc-691915c923c5 | -17.24439 | -57.48635 | 2024-11-11 05:40:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 034d58e2-58f2-3f18-bc5e-843505ea7544 | -17.58783 | -57.43224 | 2024-11-11 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 5acf9437-f78f-3535-af4c-69913e6c72d5 | -15.96422 | -59.32813 | 2024-11-11 05:40:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6c4e7bd3-2434-3230-8f3a-09b310f9277e | -16.00478 | -59.35339 | 2024-11-11 05:40:00 | NOAA-21 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 03baeff8-94e5-3f8d-9071-6cb23b13f75f | -17.60219 | -57.54199 | 2024-11-11 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.8 |
| 5c4d18a7-426a-39f0-a8ff-a79df46a0b5d | -17.69727 | -54.09577 | 2024-11-11 05:40:00 | NOAA-21 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 534712de-4b6d-3664-8e02-03b22199021e | -17.6027 | -57.44073 | 2024-11-11 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 75f3e84d-1ffa-3d06-99ca-525890f9a7fa | -17.29819 | -57.49108 | 2024-11-11 05:40:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 095dac31-d9ac-348b-9a0b-fb28efc10a7e | -17.29375 | -57.48404 | 2024-11-11 05:40:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 3d6d7406-cbfd-33cf-a103-ac869fabebe8 | -17.59773 | -57.53492 | 2024-11-11 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 16.0 |
| 02ab55ce-fa3c-365e-8833-a0f3f704fea8 | -17.24668 | -57.48446 | 2024-11-11 05:40:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| a00dbdcb-2cf0-37a0-ad47-99a843745893 | -17.59267 | -57.43617 | 2024-11-11 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| bac50f11-4df5-3621-8acb-c047c6ef18b0 | -16.09053 | -60.10973 | 2024-11-11 05:40:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8afa1085-294c-3d28-bf7b-f5cc3c846937 | -17.62458 | -57.52859 | 2024-11-11 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 03774eb3-7e5d-34d1-b110-707f8c5cfbfd | -15.05473 | -58.23094 | 2024-11-11 05:40:00 | NOAA-21 | SALTO DO CÉU | MATO GROSSO | Brasil | 5107750 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 66560fdf-9f1f-3dec-90f7-7e830140f345 | -17.62936 | -57.43754 | 2024-11-11 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 5b875575-4132-3e14-8dc2-c9567f225697 | -17.66798 | -57.46874 | 2024-11-11 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 53c2b474-3558-33e7-9d68-c0f36a2ef9f8 | -17.23888 | -57.48888 | 2024-11-11 05:40:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| a88e34ed-acaa-3cb1-b887-a2df100f867e | -17.59786 | -57.43682 | 2024-11-11 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 3b4693eb-2b89-3e80-9362-355aa5049e9c | -15.98962 | -59.36597 | 2024-11-11 05:40:00 | NOAA-21 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| eb83e08a-3db8-395e-93d4-172791d8842e | -17.24954 | -57.48701 | 2024-11-11 05:40:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 8af05343-e535-354a-9f5b-61581860267b | -17.24917 | -57.49019 | 2024-11-11 05:40:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 1c50fbc9-14c5-36a4-b3e8-c3037e117cce | -17.30779 | -57.49877 | 2024-11-11 05:40:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 0ff95eaf-1abe-3bbc-a1a3-f2169c4a947c | -17.66761 | -57.47198 | 2024-11-11 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 6f88bf75-7aca-3a30-8dec-f774b9bd863b | -17.62423 | -57.53179 | 2024-11-11 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.2 |
| 57723e85-8505-3e8c-8460-c3b0c5f51842 | -12.92218 | -62.1764 | 2024-11-11 05:40:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 37588e28-e533-3b8a-9c76-d81733786640 | -17.59843 | -57.52851 | 2024-11-11 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.9 |
| 146c67a3-22fa-3eb9-ac71-437068f0cd6c | -17.63562 | -57.52348 | 2024-11-11 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 20.9 |
| 6df967c2-9d40-392d-99e0-408f5bfe118b | -17.63971 | -57.53376 | 2024-11-11 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 18.9 |
| 62b6ae82-7e45-372e-a6e4-4a2e98e3f2b0 | -17.24366 | -57.49271 | 2024-11-11 05:40:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| b004b3b0-1881-34b2-853e-a86eb81984a8 | -16.09104 | -60.10562 | 2024-11-11 05:40:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7b225489-36b0-356a-b022-e77c4d460714 | -17.59926 | -57.42381 | 2024-11-11 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 442fd909-0b40-3136-bc9a-e1e785aefe2d | -17.6145 | -57.42904 | 2024-11-11 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 4729f9ab-ad06-3dd7-ba96-7c3c5dca3d42 | -17.29445 | -57.47766 | 2024-11-11 05:40:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 12.0 |
| 0eeef5be-4690-3deb-a426-d151ede38c7b | -17.2499 | -57.48383 | 2024-11-11 05:40:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| b2cdbf80-ddf1-3487-87e0-cfac8cef1ebd | -17.59892 | -57.42706 | 2024-11-11 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| a24908c2-d0d8-38df-9563-b9bd8333e9a4 | -17.68529 | -57.51613 | 2024-11-11 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| dda995d2-3b5e-33f2-a857-9edcd95fb81a | -17.29926 | -57.48151 | 2024-11-11 05:40:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 145ded55-cc87-3b6a-b44c-5c0684c9cf24 | -17.2563 | -57.49216 | 2024-11-11 05:40:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| aa4deb76-edfc-3e85-9a24-62152cb8eae9 | -17.24634 | -57.48764 | 2024-11-11 05:40:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| d322f778-9d32-3596-aec1-4eeebe5b1ad8 | -17.77057 | -57.51957 | 2024-11-11 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| fd66aed5-7ffc-34b0-b58b-1fdaa478dbe5 | -17.61285 | -57.54008 | 2024-11-11 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.6 |
| 24d333b3-2269-3d84-a266-f8745da712da | -17.60088 | -57.50603 | 2024-11-11 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.3 |
| a0d3d9ea-6a51-302e-b064-2bdf0b56f090 | -17.59739 | -57.53812 | 2024-11-11 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 16.0 |
| b0c169ff-dd09-3950-aefc-34a20a1ad349 | -17.60966 | -57.42511 | 2024-11-11 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| d9dac06f-1cd7-32e1-8e8c-e4a23fe03fc6 | -17.62939 | -57.53244 | 2024-11-11 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.2 |
| 06022b33-a23c-3e60-8b3a-ccf136143318 | -17.59856 | -57.43031 | 2024-11-11 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 20a7c31e-3801-3d43-b108-f73fe1494902 | -17.61121 | -57.50734 | 2024-11-11 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 13.0 |
| a6e85547-aa05-317e-a605-b12dbe87aa43 | -16.00029 | -59.35301 | 2024-11-11 05:40:00 | NOAA-21 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 24908bbe-ca94-3d23-a463-88603a6d33b3 | -23.92677 | -54.04221 | 2024-11-11 05:42:00 | NOAA-21 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 8.7 |
| 7edf89cc-0646-341a-9b5c-dd43121ef7c1 | -23.91994 | -54.04159 | 2024-11-11 05:42:00 | NOAA-21 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 8.7 |
| 1e4786f4-ed57-3476-b2d8-23b6a04fb564 | -23.9336 | -54.04284 | 2024-11-11 05:42:00 | NOAA-21 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 14.1 |
| 7c838b2d-8e2b-3288-9cd5-cb4a9046a99e | -3.1094 | -45.2293 | 2024-11-11 05:50:00 | GOES-16 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 126.7 |
| 399779d3-de37-3eaa-a9c3-acc4909f7ad6 | -3.1458 | -54.4859 | 2024-11-11 05:50:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 50.2 |
| 19921f12-20cf-35c1-9cfd-0be5b5478563 | -3.1095 | -45.2067 | 2024-11-11 05:50:00 | GOES-16 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 73.8 |
| 383a5537-8582-3b54-a765-03c23729196f | -2.2114 | -53.6626 | 2024-11-11 05:50:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 44.2 |
| 5101274c-7076-3085-8030-ca5ab3e135b2 | -2.7402 | -49.3502 | 2024-11-11 05:50:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 59.0 |
| 95024a9f-cd7b-34e6-8fb2-a90e0d122627 | -2.7587 | -49.3497 | 2024-11-11 05:50:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 83.6 |
| 5f34c611-2ba1-37c1-909a-e5810c19027c | -1.4057 | -52.3758 | 2024-11-11 05:50:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 43.5 |
| 9a45eee3-bc90-347b-9c3d-d8b73e139287 | -3.128 | -45.2285 | 2024-11-11 05:50:00 | GOES-16 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 144.1 |
| ae4b1106-6538-3a48-aa6b-b29dfa3e1fb1 | -3.1281 | -45.206 | 2024-11-11 05:50:00 | GOES-16 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 80.4 |
| ea3333a5-4ade-317c-9dbb-3c5ecd4cb3bd | -2.2297 | -53.6824 | 2024-11-11 05:50:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 78.1 |
| 567cfa46-713a-349f-bd44-02749d73a29f | -2.2481 | -53.6821 | 2024-11-11 05:50:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 44.5 |
| a307e6aa-0cd4-3e2f-b7c0-9eae0046bcd1 | -2.248 | -53.7426 | 2024-11-11 05:50:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 64.8 |
| 6f45408f-8cfd-3d96-addb-24be7542425b | -2.2482 | -53.6619 | 2024-11-11 05:50:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 51.9 |
| d9cfbfaa-9969-3373-9e3a-e6f60cf0311e | -2.2298 | -53.6623 | 2024-11-11 05:50:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 96.0 |
| bda423da-fc44-3076-bcfb-cee0d6ccd45c | 4.65258 | -60.94006 | 2024-11-11 05:59:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3badcc6f-a465-3d18-8071-ef8c83e5d5d8 | 4.65703 | -60.93931 | 2024-11-11 05:59:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2a8b3b25-bfb6-31e9-9430-a7688bb88ea1 | -1.54262 | -55.87992 | 2024-11-11 05:59:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c53536a2-fedb-37a3-8bb9-2d273e33827e | 4.64806 | -60.94046 | 2024-11-11 05:59:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8bb3402b-6ac7-3254-b073-ba22d1f58c83 | -1.54253 | -55.87428 | 2024-11-11 05:59:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8a99dc59-d9ea-368b-b6a5-3d73c42a5371 | -1.54153 | -55.88064 | 2024-11-11 05:59:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 33b235a8-f108-39fe-98e3-96c3b5123c38 | -1.54358 | -55.87356 | 2024-11-11 05:59:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7045cc5e-ee5a-30e8-9b24-7c6e9beb09b6 | 2.67507 | -61.17795 | 2024-11-11 05:59:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ebdfe524-390c-3be4-a835-728c8f12501f | 4.64886 | -60.94516 | 2024-11-11 05:59:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b4ce9811-f385-3d95-b47c-2a0a1f2ab293 | 2.67128 | -61.18323 | 2024-11-11 05:59:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 60b6b398-d22a-3262-812a-9dceb8ecec3e | 4.64436 | -60.94565 | 2024-11-11 05:59:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 41b35a57-84ee-3b40-98e9-51d4ee891e44 | 2.85542 | -60.07766 | 2024-11-11 05:59:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 071e5ccd-672e-3275-a207-afc9f758a632 | 3.18633 | -64.19738 | 2024-11-11 05:59:00 | NPP-375D | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a5463ad5-12d4-3aaf-9d61-36b63d702c73 | 2.85864 | -60.07831 | 2024-11-11 05:59:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a73112ea-3f80-3851-bb0e-0501fcc9fb8f | 2.6758 | -61.18244 | 2024-11-11 05:59:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 3.4 |
| bd57995a-4a79-3d9b-ae25-03b87392d6a9 | 4.65335 | -60.94462 | 2024-11-11 05:59:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c26cdd5c-4f34-34c4-8665-5c889d705e04 | 2.85376 | -60.07913 | 2024-11-11 05:59:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7e55228e-c4bc-3080-9828-a2eb7e3918b5 | -2.2298 | -53.6623 | 2024-11-11 06:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 82.2 |
| ab4c800c-1723-32ce-b8af-acc83cc9457b | -3.1458 | -54.4859 | 2024-11-11 06:00:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 51.0 |
| 08b7ce58-a5e3-3015-875d-e9d03f592c15 | -2.248 | -53.7426 | 2024-11-11 06:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 60.8 |
| dc132d65-a509-38c2-a92e-b87e70aa72e6 | -2.2297 | -53.6824 | 2024-11-11 06:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 69.6 |
| dc402608-86a0-3735-835f-766f2277b7b6 | -2.7587 | -49.3497 | 2024-11-11 06:00:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 80.4 |
| b9792f58-b412-30f6-a382-d52f66bc26c1 | -2.2114 | -53.6626 | 2024-11-11 06:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 45.2 |


[Clique aqui para ver as próximas entradas](README47.md)
