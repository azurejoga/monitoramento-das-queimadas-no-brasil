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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8f44a98e-f24b-315f-a31d-5b5bb9356d9e | -9.7359 | -64.2295 | 2024-10-13 00:56:02 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 82.0 |
| 7fbfc37e-5360-3841-866e-bd2ebf1326b6 | -10.8796 | -44.3379 | 2024-10-13 00:56:07 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 82.1 |
| d539e2e8-8b43-375d-a88c-7231007a60a8 | -10.8987 | -44.3352 | 2024-10-13 00:56:07 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 60.8 |
| 9aecaa4d-76ae-3808-a412-7ba968da83e5 | -10.9311 | -44.6789 | 2024-10-13 00:56:08 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 144.6 |
| dadff20b-73d9-3755-9301-168d59760ae5 | -10.9315 | -44.6557 | 2024-10-13 00:56:08 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 80.5 |
| d2297eb3-0523-323b-81a3-238998eabc09 | -10.9502 | -44.6762 | 2024-10-13 00:56:08 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 144.4 |
| 4b4ce20d-8419-3248-8ea6-7ba133532eed | -10.9506 | -44.653 | 2024-10-13 00:56:08 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 99.5 |
| 7e14d0c5-6157-333c-aec7-4c20d848d87e | -11.2532 | -50.9249 | 2024-10-13 00:56:10 | GOES-16 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 84.1 |
| 8932082d-8b6f-30b6-86bd-5503f0863353 | -11.2535 | -50.9036 | 2024-10-13 00:56:10 | GOES-16 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 84.5 |
| 7eefc6fe-911a-3244-b609-bd17d1b7b907 | -11.2722 | -50.9228 | 2024-10-13 00:56:10 | GOES-16 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 83.6 |
| b778ce65-7e8a-3382-8938-765e4c8b2946 | -11.2725 | -50.9016 | 2024-10-13 00:56:10 | GOES-16 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 95.1 |
| 105d2672-bdd9-3217-ac77-dcd8489a4c0d | -11.6143 | -48.376 | 2024-10-13 00:56:12 | GOES-16 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 83.6 |
| 4a816efc-66d2-392a-83b0-21160dc7c93b | -11.6334 | -48.3736 | 2024-10-13 00:56:12 | GOES-16 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 127.8 |
| a8de323a-0528-3d5c-9264-803077a77cf1 | -11.7479 | -48.3591 | 2024-10-13 00:56:13 | GOES-16 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 78.6 |
| 506aee97-2997-3cef-bdbe-f84d2c5af28e | -11.712 | -64.9777 | 2024-10-13 00:56:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 88.7 |
| c353002e-c436-3b8c-bf56-b9ea828af8e0 | -11.7308 | -64.9769 | 2024-10-13 00:56:14 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 102.2 |
| d9fa1ec8-7c72-3f4f-a481-40a57e487065 | -12.2754 | -47.6473 | 2024-10-13 00:56:15 | GOES-16 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 108.7 |
| 4d81bd0b-aee6-3880-87fd-1d8955a19d51 | -12.3793 | -63.7294 | 2024-10-13 00:56:17 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 96.3 |
| 4d8c1555-e8b0-36fa-b2c8-935625ff0652 | -12.398 | -63.7475 | 2024-10-13 00:56:17 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 76.7 |
| 47087712-9836-307b-a64c-791b60a122fb | -12.3982 | -63.7284 | 2024-10-13 00:56:17 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 118.3 |
| 6b0d675b-ab96-3fec-95ce-cfc9586722ba | -18.2089 | -56.577702 | 2024-10-13 00:56:18 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 59bde1f2-563c-3b6f-a52b-f82c5300818e | -18.210501 | -56.419399 | 2024-10-13 00:56:18 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 87a4e7a4-d172-3513-b1be-4bc4100aaaab | -18.213499 | -56.436199 | 2024-10-13 00:56:18 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 2b2c2426-3893-3251-87ab-391afc405e63 | -18.2166 | -56.452999 | 2024-10-13 00:56:18 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| fc67bf55-d12a-37eb-970d-85dd1c7b4b91 | -18.219601 | -56.469898 | 2024-10-13 00:56:18 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 86388855-020d-3a67-aca6-1318d37942d7 | -18.2227 | -56.486801 | 2024-10-13 00:56:18 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| ac06d26b-7a18-3f7d-843f-637da4df6de4 | -18.219101 | -56.522701 | 2024-10-13 00:56:18 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| e6517075-4027-361c-b108-8e0170d2f256 | -18.2094 | -56.524601 | 2024-10-13 00:56:18 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 379ea4d9-baed-3907-8aa8-fe0fd3df711f | -18.2125 | -56.541599 | 2024-10-13 00:56:18 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| cfef1e29-e8a9-3f7f-a6ab-744c141de201 | -18.215599 | -56.558701 | 2024-10-13 00:56:18 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 6e28791f-52fd-3af8-99c2-ad0d472e5758 | -18.2187 | -56.575901 | 2024-10-13 00:56:18 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| d7acb649-ec27-3670-8f53-fac24d2d10f1 | -18.2027 | -56.543499 | 2024-10-13 00:56:18 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 3894dd70-5c15-3bec-92c3-662c2e6b911a | -18.205799 | -56.5606 | 2024-10-13 00:56:18 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 4a932c0f-2401-31f2-91e0-8db7d1d536f3 | -18.193001 | -56.5453 | 2024-10-13 00:56:19 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 4233585d-839f-3df8-ab0e-4467a6025f84 | -18.1961 | -56.562401 | 2024-10-13 00:56:19 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 78a5cb5e-83c0-3b03-a2ca-88ecc892bcee | -18.1992 | -56.579498 | 2024-10-13 00:56:19 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 873654c3-1e5b-3ef4-be18-a446c75deb28 | -12.9372 | -62.5275 | 2024-10-13 00:56:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 94.9 |
| 621d9df9-a3cd-3662-bd6a-3424224385d2 | -13.1475 | -62.3215 | 2024-10-13 00:56:21 | GOES-16 | ALTO ALEGRE DOS PARECIS | RONDÔNIA | Brasil | 1100379 | 11 | 33 | nan | nan | nan | Amazônia | 107.4 |
| 55b22aa6-545e-35cd-9e55-1dd4283ced17 | -13.7346 | -60.6079 | 2024-10-13 00:56:24 | GOES-16 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 120.8 |
| e9820b54-a8dd-3bc6-a17c-edca4df0010a | -13.7348 | -60.5883 | 2024-10-13 00:56:24 | GOES-16 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 102.0 |
| 6e8ce951-b01e-3236-9919-5cc25ec86aec | -17.9856 | -57.3517 | 2024-10-13 00:56:24 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 90cad0e8-1b43-30fa-9c81-68bd8fb7cf81 | -17.975901 | -57.3536 | 2024-10-13 00:56:25 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| bfa4909b-68e6-3412-a7a2-e3f09a3d67fb | -17.9793 | -57.372799 | 2024-10-13 00:56:25 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| d8dc5f0f-52e6-3cb0-9ca8-5e9ec6463f45 | -17.9627 | -57.336201 | 2024-10-13 00:56:25 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| cb31a386-004a-3841-b2df-47bd11f04db0 | -17.966101 | -57.355301 | 2024-10-13 00:56:25 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 957ee50d-7ede-375a-abdb-d151313bfa45 | -17.9725 | -57.3344 | 2024-10-13 00:56:25 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 9ace3a24-9faa-3e63-8a4b-d65afa0cede3 | -17.9695 | -57.374599 | 2024-10-13 00:56:25 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 385e9aad-33f6-3794-9542-038d5749d220 | -17.952999 | -57.338001 | 2024-10-13 00:56:25 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| c46c8600-0b1e-35b1-94da-9cfc066ea0eb | -17.9564 | -57.357101 | 2024-10-13 00:56:25 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| f5d8c627-c54a-3860-b8bf-925d367f4b58 | -17.959801 | -57.3764 | 2024-10-13 00:56:25 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 3f15a318-5cbd-3784-bfe4-cdb5653bb64c | -17.946699 | -57.359001 | 2024-10-13 00:56:25 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 528d4881-0c52-3c4b-99c1-1e1743ff5895 | -17.9501 | -57.378201 | 2024-10-13 00:56:25 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| b95b82d5-2663-362b-bd45-dd32ffa031cd | -17.907301 | -57.307201 | 2024-10-13 00:56:26 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 81d0d2f1-e695-3adb-9756-ca426e604a38 | -17.9107 | -57.326199 | 2024-10-13 00:56:26 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 23ecd368-7336-36dc-a172-d9265be33497 | -17.894199 | -57.289902 | 2024-10-13 00:56:26 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 411f7063-d98f-375e-9e80-2430878ad3d1 | -17.8976 | -57.308899 | 2024-10-13 00:56:26 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| cfeb4bcc-6cb7-31d3-ab4b-d604da6961bf | -17.900999 | -57.327999 | 2024-10-13 00:56:26 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| efb59bef-f595-35a5-8830-12a593999c25 | -17.9044 | -57.347099 | 2024-10-13 00:56:26 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| bf3be0da-bfb2-389a-97cc-a1ff2665c7d8 | -17.884501 | -57.291698 | 2024-10-13 00:56:26 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 7f9c8b46-458b-3bbc-b1ba-c2df76ffc4f1 | -17.887899 | -57.310699 | 2024-10-13 00:56:26 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| cec77bad-3688-32ce-9f57-3f7bdd80a69b | -17.8913 | -57.3298 | 2024-10-13 00:56:26 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| b1da89f4-ee45-3c85-a93e-65187000cba2 | -17.894699 | -57.3489 | 2024-10-13 00:56:26 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 637f236d-633c-3ea5-9e2d-efe2dfae27d7 | -17.871401 | -57.2747 | 2024-10-13 00:56:26 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 0727c57b-fdb6-34b8-805a-3188035da910 | -17.8748 | -57.293598 | 2024-10-13 00:56:26 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| b3f92148-ff7e-3efc-9f69-e15774c46cb1 | -17.878099 | -57.312599 | 2024-10-13 00:56:26 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 4ea433cb-069c-3d57-add8-11eca87072e4 | -17.8815 | -57.331699 | 2024-10-13 00:56:26 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 4df7e6a4-ac64-3d36-9699-f50bda110a35 | -17.884899 | -57.3508 | 2024-10-13 00:56:26 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| f171bfba-675e-31a5-8aae-38be22571145 | -17.865101 | -57.295399 | 2024-10-13 00:56:26 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 50d06570-6a0d-3a71-90d9-18ffbdd03d10 | -17.868401 | -57.3144 | 2024-10-13 00:56:26 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 3e284fbf-5e0e-3c06-91a5-52a74c7ba11a | -17.871799 | -57.3335 | 2024-10-13 00:56:26 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 529f88ca-4fa1-3397-9d41-0737a197d9e4 | -17.8752 | -57.3526 | 2024-10-13 00:56:26 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 9bd8201d-d5c5-30ea-bf40-7ca8309b074b | -17.8554 | -57.297199 | 2024-10-13 00:56:26 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 7e8bbde6-cd15-3f95-b106-d2c96e7fea2c | -17.862101 | -57.3353 | 2024-10-13 00:56:26 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 0569e6f3-681e-3633-b7ab-89209933bd59 | -17.865499 | -57.354401 | 2024-10-13 00:56:26 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| c1f97c77-0c47-38e0-b167-f05fdc8d8bff | -17.836399 | -57.359798 | 2024-10-13 00:56:27 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 2990575d-4c97-3f9b-868e-68db40db54cd | -17.8398 | -57.378899 | 2024-10-13 00:56:27 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| e30b60ad-87ab-31ca-aba6-417a230b4802 | -17.8267 | -57.361698 | 2024-10-13 00:56:27 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 4ff8605d-b894-349f-a464-2b580eacd3d1 | -17.653299 | -56.238998 | 2024-10-13 00:56:27 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 11cb568b-bbb6-337b-bd84-470817a91c5b | -17.6563 | -56.255001 | 2024-10-13 00:56:27 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 225a6a37-68cd-3216-822c-e7b306eeceb1 | -17.845699 | -57.299099 | 2024-10-13 00:56:27 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 9c470132-59c4-3446-9aed-4e2f310c9ddd | -17.849001 | -57.3181 | 2024-10-13 00:56:27 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 9f2e2755-9290-328f-8fa4-c80dd29ad15b | -17.8524 | -57.337101 | 2024-10-13 00:56:27 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 23a27662-109f-358f-9270-69a5eb6a7f25 | -17.855801 | -57.356201 | 2024-10-13 00:56:27 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 2a1693fb-e4b1-3352-9b68-cff2f024d4b2 | -17.8592 | -57.375401 | 2024-10-13 00:56:27 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 12172cf6-0c0a-3b76-928e-c77db190ec08 | -17.6436 | -56.240898 | 2024-10-13 00:56:27 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 7126dfcd-a97a-3463-aeeb-966efa4946c6 | -17.6465 | -56.256901 | 2024-10-13 00:56:27 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 0376f7d2-5c24-3ea5-ad87-b1f35f6c648f | -17.6495 | -56.272999 | 2024-10-13 00:56:27 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 40803aef-7c46-35e7-a697-2e91c00001bf | -17.836 | -57.3009 | 2024-10-13 00:56:27 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 30a73eda-2472-316e-8a9a-fcd4610734ab | -17.8393 | -57.319901 | 2024-10-13 00:56:27 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| b0705c8f-6b68-33d5-a313-753288ef96b1 | -17.842699 | -57.338902 | 2024-10-13 00:56:27 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| bf4cf6b1-6570-397b-95f7-2f5f96bda423 | -17.8461 | -57.358002 | 2024-10-13 00:56:27 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 4eba40eb-945b-3154-9798-819537e6c4e0 | -17.849501 | -57.377201 | 2024-10-13 00:56:27 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 4a62d471-44a4-3b0a-b319-a6b6b84a7b5f | -17.636801 | -56.258801 | 2024-10-13 00:56:27 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| b6cf1e0a-d1f6-3139-805a-436635cceaea | -17.6397 | -56.274899 | 2024-10-13 00:56:27 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| af9be658-085e-3a76-982e-763660b9bd0b | -17.8262 | -57.3027 | 2024-10-13 00:56:27 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| cda5410f-3197-3663-99a3-f75250148a4d | -17.829599 | -57.321701 | 2024-10-13 00:56:27 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| e3076eb0-d20b-3e47-aefd-cac9012c0f25 | -17.833 | -57.340698 | 2024-10-13 00:56:27 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| e7b74c14-e4f4-3a6d-94a5-565e36bb0b38 | -15.6419 | -59.9767 | 2024-10-13 00:56:35 | GOES-16 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 105.9 |
| bd95895a-2150-363d-9698-3eb9698dbf01 | -15.6612 | -59.975 | 2024-10-13 00:56:35 | GOES-16 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 80.8 |
| 8897c74c-d0c4-34f6-977f-7a599caeba93 | -15.9437 | -59.0897 | 2024-10-13 00:56:36 | GOES-16 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 54.9 |


[Clique aqui para ver as próximas entradas](README13.md)
