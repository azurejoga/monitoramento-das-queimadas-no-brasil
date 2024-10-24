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

## Dados Diários - Página 54

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 73a08ee2-0b20-3f80-86a1-993128b0760e | -17.26776 | -57.29485 | 2024-10-24 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.7 |
| 9d836fd1-2266-3c2e-80c4-54745cfc7bec | -17.26687 | -57.29949 | 2024-10-24 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| e70da511-635c-3eaa-b0ac-445a3319b6bf | -17.26599 | -57.23208 | 2024-10-24 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.7 |
| 466cacc4-a471-38dd-b230-023dbb1089b6 | -17.26422 | -57.24128 | 2024-10-24 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.9 |
| 6a59d245-ea42-32bd-80ca-719de3731fba | -17.26155 | -57.25509 | 2024-10-24 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.1 |
| db4d4cdc-b4a0-3928-81e8-4a027e8792db | -17.26155 | -57.23117 | 2024-10-24 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.7 |
| bbec5896-5e72-3122-94a6-c3383a8e6d8c | -17.26151 | -57.30322 | 2024-10-24 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 1ee54047-5023-3038-8a3d-23b7455f0aaa | -17.26066 | -57.23576 | 2024-10-24 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.7 |
| b8e8eee4-beb0-3a25-a4b8-21f6396d9496 | -17.25974 | -57.28838 | 2024-10-24 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 07b780e9-f1fd-36af-97a5-f0426c5b0047 | -17.25799 | -57.24957 | 2024-10-24 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.1 |
| f1fdbbd9-451a-3e76-9646-a83bf2585393 | -17.2571 | -57.25418 | 2024-10-24 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.1 |
| c8254ab9-98c3-3e30-b503-568fff45d5f7 | -17.25705 | -57.30229 | 2024-10-24 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 7417fabc-f4e1-30ac-8321-3669b663e46c | -17.25355 | -57.24865 | 2024-10-24 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.1 |
| 8f923369-6d92-32d0-94ab-68e74c93274e | -17.25265 | -57.25326 | 2024-10-24 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.1 |
| e5f33fef-b98f-3256-9c16-621643c311fb | -17.24821 | -57.25235 | 2024-10-24 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.1 |
| a05b7325-684f-38df-a308-748bf07a1ab0 | -17.24731 | -57.25696 | 2024-10-24 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 11.2 |
| d89002a9-83f3-31ae-8396-e3d6e1361bcf | -17.24555 | -57.24222 | 2024-10-24 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 22.3 |
| 91020e85-ce36-3c16-b215-9c6bfc2a1445 | -17.24196 | -57.26065 | 2024-10-24 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 24ff8da5-6536-32c0-8f28-2560f5ad7ab7 | -17.24111 | -57.24131 | 2024-10-24 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 22.3 |
| 2570b866-6bb3-3ea7-af03-4fef53e6327a | -17.24021 | -57.24591 | 2024-10-24 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 12.6 |
| 88e3518e-9366-3586-b8dc-f84aeed7b804 | -17.23927 | -57.27452 | 2024-10-24 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| 53a1e011-60d1-379d-b5bd-aa1e56ce31ba | -17.23577 | -57.24499 | 2024-10-24 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 29f5f91e-3fe3-3e41-be56-08fc78b4f4b2 | -17.23487 | -57.2496 | 2024-10-24 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 868be7f5-7550-3590-8e8f-a9360347ac43 | -14.8727 | -59.86526 | 2024-10-24 04:36:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 74ec8d89-191f-3acf-b057-1cbcafe09b15 | -14.87193 | -59.86898 | 2024-10-24 04:36:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 80ab7f5e-a4ae-39b3-9d47-6a8b550933f2 | -14.86645 | -59.8678 | 2024-10-24 04:36:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.3 |
| ab47f37d-515c-3f15-82f6-81b05e95979c | -14.54523 | -59.95689 | 2024-10-24 04:36:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 585b725d-f583-347a-b3a2-01f7a84f50e7 | -14.53963 | -59.95595 | 2024-10-24 04:36:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3969d5ec-d048-3852-8747-3ffc0108c7c8 | -15.92212 | -59.62976 | 2024-10-24 04:36:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ea6de6b6-be14-3bde-90dc-632ae38dcb8b | -15.91682 | -59.6286 | 2024-10-24 04:36:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 98fbc6bc-c79a-37ae-99a4-4f3541c6969c | -16.9792 | -57.5223 | 2024-10-24 04:36:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 87.4 |
| e884a4e9-06d0-3e4a-bae6-c7349ad38f70 | -16.9599 | -57.5041 | 2024-10-24 04:36:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 77.8 |
| 41e68386-6532-3073-909a-7a0e1aab76fe | -16.9596 | -57.5245 | 2024-10-24 04:36:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 127.3 |
| cbe9ed69-55b3-3c7a-90de-517314bf02e0 | -17.2579 | -57.2439 | 2024-10-24 04:36:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 80.4 |
| d9bd9a4a-1408-321b-94e5-95f70cd77058 | -17.2383 | -57.2462 | 2024-10-24 04:36:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 86.6 |
| dfc958ff-809e-398c-b0a7-d18b3f3b9041 | -17.234 | -57.5131 | 2024-10-24 04:36:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 73.3 |
| 95791d7b-53c3-3853-a62e-b9b65d9a1201 | -19.6442 | -56.8311 | 2024-10-24 04:36:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 55.5 |
| 1ba23ef7-a6a8-37fd-863d-9b8467ce0f41 | -19.6438 | -56.8521 | 2024-10-24 04:36:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 75.3 |
| ddd73e8c-09e0-330a-85b3-9cdfed395839 | -19.5681 | -56.6114 | 2024-10-24 04:36:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 74.7 |
| f00dd875-4558-3301-a7e7-3a5287689880 | -23.8366 | -55.2894 | 2024-10-24 04:37:17 | GOES-16 | PARANHOS | MATO GROSSO DO SUL | Brasil | 5006358 | 50 | 33 | nan | nan | nan | Mata Atlântica | 60.5 |
| 4b21074a-77a5-3517-a076-54d941edd3c8 | -23.8155 | -55.2933 | 2024-10-24 04:37:17 | GOES-16 | PARANHOS | MATO GROSSO DO SUL | Brasil | 5006358 | 50 | 33 | nan | nan | nan | Mata Atlântica | 57.2 |
| 9add4735-31ae-3c1f-a9c3-13a404cc4c5b | -21.28606 | -41.74808 | 2024-10-24 04:38:00 | NOAA-21 | ITAPERUNA | RIO DE JANEIRO | Brasil | 3302205 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| f8ae4065-6bae-3371-9fa2-f5fbb1e80b05 | -21.19526 | -44.93744 | 2024-10-24 04:38:00 | NOAA-21 | IJACI | MINAS GERAIS | Brasil | 3130408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 9bc17961-1a4c-395d-bc07-3d162e1d0954 | -18.29934 | -56.14954 | 2024-10-24 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| a95abd6f-ed9e-351b-820e-98cc3f0f6260 | -20.47682 | -53.67501 | 2024-10-24 04:38:00 | NOAA-21 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3a301d4d-3e97-3fcf-abba-0dbb6f23e0da | -21.14956 | -53.63164 | 2024-10-24 04:38:00 | NOAA-21 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 53f0a5e0-026f-3f94-9934-afcee5eaea40 | -22.30833 | -54.7795 | 2024-10-24 04:38:00 | NOAA-21 | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5f46815c-a595-34d6-bb10-3d03923cf844 | -20.5223 | -55.35367 | 2024-10-24 04:38:00 | NOAA-21 | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e5020ff0-5d54-3951-aafa-3152c3f9af1f | -20.52215 | -55.35688 | 2024-10-24 04:38:00 | NOAA-21 | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 38a81b02-40b6-30d6-8df9-d6361dbceaa8 | -20.42369 | -54.97271 | 2024-10-24 04:38:00 | NOAA-21 | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c334511d-01de-36a3-85e8-65d1ab7b6ece | -20.38731 | -54.86256 | 2024-10-24 04:38:00 | NOAA-21 | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 738d4cab-cd89-392c-a577-ad200a06c9ba | -20.26405 | -55.42317 | 2024-10-24 04:38:00 | NOAA-21 | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 66c6f519-917a-3a9f-b32d-2e9348f0f035 | -21.89945 | -56.10745 | 2024-10-24 04:38:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0027d790-c62b-31f6-b757-feeb866f1001 | -21.00793 | -55.41038 | 2024-10-24 04:38:00 | NOAA-21 | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 652b602b-bfcc-3f23-8c9e-b4487b70a7f5 | -23.83006 | -55.29422 | 2024-10-24 04:38:00 | NOAA-21 | PARANHOS | MATO GROSSO DO SUL | Brasil | 5006358 | 50 | 33 | nan | nan | nan | Mata Atlântica | 38.3 |
| 0885a974-b1bd-391a-a4e3-5179c91a5488 | -23.82729 | -55.28903 | 2024-10-24 04:38:00 | NOAA-21 | PARANHOS | MATO GROSSO DO SUL | Brasil | 5006358 | 50 | 33 | nan | nan | nan | Mata Atlântica | 54.4 |
| 0128e6f6-fd54-3e84-9b15-74d4cabe5bc4 | -23.82649 | -55.29345 | 2024-10-24 04:38:00 | NOAA-21 | PARANHOS | MATO GROSSO DO SUL | Brasil | 5006358 | 50 | 33 | nan | nan | nan | Mata Atlântica | 38.3 |
| b7902ab2-1f43-3e0a-80fa-2cf21ac13ca3 | -23.82452 | -55.28382 | 2024-10-24 04:38:00 | NOAA-21 | PARANHOS | MATO GROSSO DO SUL | Brasil | 5006358 | 50 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 90d05aae-894e-37fb-911d-0de267ea5faf | -23.82372 | -55.28824 | 2024-10-24 04:38:00 | NOAA-21 | PARANHOS | MATO GROSSO DO SUL | Brasil | 5006358 | 50 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 269626de-1b42-397c-b608-b39778dbb0c0 | -23.82096 | -55.28305 | 2024-10-24 04:38:00 | NOAA-21 | PARANHOS | MATO GROSSO DO SUL | Brasil | 5006358 | 50 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 9dd97100-0885-35b3-afb9-8eba9c78a620 | -23.79659 | -55.28453 | 2024-10-24 04:38:00 | NOAA-21 | PARANHOS | MATO GROSSO DO SUL | Brasil | 5006358 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 45effc60-0903-3bd9-bba8-dba9c35086a8 | -23.7958 | -55.28897 | 2024-10-24 04:38:00 | NOAA-21 | PARANHOS | MATO GROSSO DO SUL | Brasil | 5006358 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 96347610-1885-3ff0-a743-29d6af4c7e2f | -23.79459 | -55.2749 | 2024-10-24 04:38:00 | NOAA-21 | PARANHOS | MATO GROSSO DO SUL | Brasil | 5006358 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| bac2c901-7ec3-323d-90bd-8b32325091b7 | -23.79301 | -55.28379 | 2024-10-24 04:38:00 | NOAA-21 | PARANHOS | MATO GROSSO DO SUL | Brasil | 5006358 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 3fcc386e-74f9-3671-9d08-aad6c3e5263d | -23.7926 | -55.26519 | 2024-10-24 04:38:00 | NOAA-21 | PARANHOS | MATO GROSSO DO SUL | Brasil | 5006358 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 0481ef78-a28b-3968-912b-a751e8e5eb37 | -23.79222 | -55.28823 | 2024-10-24 04:38:00 | NOAA-21 | PARANHOS | MATO GROSSO DO SUL | Brasil | 5006358 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| c7fbcfb7-d416-3600-92fd-76181df5e504 | -23.79181 | -55.26965 | 2024-10-24 04:38:00 | NOAA-21 | PARANHOS | MATO GROSSO DO SUL | Brasil | 5006358 | 50 | 33 | nan | nan | nan | Mata Atlântica | 8.9 |
| 1a3bc861-6c00-3669-8796-bb5252c54ca3 | -23.79102 | -55.27411 | 2024-10-24 04:38:00 | NOAA-21 | PARANHOS | MATO GROSSO DO SUL | Brasil | 5006358 | 50 | 33 | nan | nan | nan | Mata Atlântica | 8.9 |
| 6586f9a1-3acb-3f69-8273-c5e9bbba3cb3 | -23.26466 | -55.20375 | 2024-10-24 04:38:00 | NOAA-21 | AMAMBAI | MATO GROSSO DO SUL | Brasil | 5000609 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| c993c153-ba86-3916-9000-7965fb773fb1 | -23.26387 | -55.20821 | 2024-10-24 04:38:00 | NOAA-21 | AMAMBAI | MATO GROSSO DO SUL | Brasil | 5000609 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 3eb20bf6-2b73-3964-8bff-ecb7c2c2d80d | -18.31437 | -56.20411 | 2024-10-24 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.3 |
| 81c5d0db-31fc-3100-a2f5-2943b326fea6 | -18.31417 | -56.16047 | 2024-10-24 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.7 |
| ca12b8ab-6b6d-38fc-93b4-346ea9a40ea9 | -18.31338 | -56.23181 | 2024-10-24 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 2f2b3b14-48cc-3af5-be25-8710e3c1eee9 | -18.31265 | -56.23566 | 2024-10-24 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 15.7 |
| c62f89cd-e1ed-379a-89e2-28a8c0ae3e78 | -18.30519 | -56.23016 | 2024-10-24 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.3 |
| 81a2da6c-d335-337b-862f-26c962404754 | -18.3034 | -56.15036 | 2024-10-24 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| b38a91d6-2ea0-3ec9-8f3e-68c4bb353766 | -18.30066 | -56.1462 | 2024-10-24 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| d5e3b4ae-1201-375c-bbb8-38ebe248e1d6 | -18.29289 | -56.07386 | 2024-10-24 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 6f25637c-b64a-33b4-a2b9-ad26c636bf0a | -18.29219 | -56.07764 | 2024-10-24 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.5 |
| ffb7bfa6-34f2-3c18-8bf3-dd1d17548cc5 | -18.27207 | -56.05009 | 2024-10-24 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 04dfbffc-5fe6-3f4f-b299-1bad3d6afdad | -18.26872 | -56.04552 | 2024-10-24 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 0e703e8a-3b05-3579-b017-fd744d5fc092 | -18.17189 | -56.35698 | 2024-10-24 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 10317e00-64dc-327c-95ea-56d709d23632 | -18.30929 | -56.23099 | 2024-10-24 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 26e550e1-c0c2-3caa-a9c0-1fe08b55f0eb | -18.29996 | -56.15001 | 2024-10-24 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 5e31392f-abb9-367e-a722-ed942889dfea | -18.27277 | -56.04633 | 2024-10-24 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 7570a660-936e-3718-9845-3d62c1a351a2 | -18.16773 | -56.31136 | 2024-10-24 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 127ae453-f541-30ab-9547-efdefa397f85 | -18.31701 | -56.21261 | 2024-10-24 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 9fcfb692-59a3-3bda-8c00-26245f890789 | -18.3151 | -56.20029 | 2024-10-24 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 2e76abfa-57f0-3428-a0f7-d5c7c901acb7 | -18.31489 | -56.15666 | 2024-10-24 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 5257b37f-8b99-3b76-bae2-a42f52b66c75 | -18.30856 | -56.23483 | 2024-10-24 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 15.7 |
| c0b83732-9928-38e2-985a-eee5deb92793 | -18.30447 | -56.234 | 2024-10-24 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.1 |
| 083cee84-a8ae-3277-9462-0bb0ba9b8dd4 | -18.30403 | -56.15084 | 2024-10-24 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 9c2a3337-c06b-30ce-ba49-583254a3cb92 | -18.26397 | -56.04847 | 2024-10-24 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.3 |
| 3bd02a57-cdcd-3c88-9f93-5dff68f627aa | -18.26328 | -56.05222 | 2024-10-24 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.7 |
| 9799049d-76b6-3dc0-8c2e-5b2e539bfb84 | -18.26257 | -56.05598 | 2024-10-24 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.7 |
| 9258e6e4-de9a-3e76-b86e-39ee8deea139 | -18.25782 | -56.05893 | 2024-10-24 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| f00766fc-769f-3631-b987-e4bcbb514a4f | -18.17185 | -56.3122 | 2024-10-24 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 0dc987c3-3dc6-31de-b947-8e7a1c99b39d | -18.1711 | -56.31611 | 2024-10-24 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 4420e738-8d8b-307e-89fe-b7a79401fb87 | -18.3211 | -56.21343 | 2024-10-24 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 10.3 |
| dc4be716-babb-359e-b1ee-99dd505cbd91 | -18.31918 | -56.20112 | 2024-10-24 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |


[Clique aqui para ver as próximas entradas](README55.md)
