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

## Dados Diários - Página 130

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fd21d438-c68f-35bc-be07-7a7299eb38a4 | -18.1909 | -56.8186 | 2024-10-14 07:06:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 51.4 |
| bdbdfa64-897d-3ebb-90ff-02714da982f8 | -18.2754 | -56.517 | 2024-10-14 07:06:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 87.4 |
| f10983d4-918a-33b7-b3c5-6af61b769143 | -18.2144 | -56.6081 | 2024-10-14 07:26:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 56.7 |
| 39f1d3b5-476a-369b-9c54-246a2d74462b | -18.2342 | -56.6055 | 2024-10-14 07:26:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 67.9 |
| 57fc78c6-3461-3508-a22c-368fd4af1e99 | -18.2342 | -56.6055 | 2024-10-14 07:36:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 71.5 |
| d2f17e09-732e-3e09-abb0-6459fe8898f8 | -18.2342 | -56.6055 | 2024-10-14 07:46:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 73.2 |
| 1df7586b-81bf-3457-ac34-4bad6d1984e0 | -18.2144 | -56.6081 | 2024-10-14 07:46:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 79.1 |
| 1a797194-e66c-3919-ae50-a3b77fba6bad | -18.1909 | -56.8186 | 2024-10-14 07:46:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 51.0 |
| b9243ba8-9040-37fe-bf1b-1f3fac7baa3a | -18.2757 | -56.4962 | 2024-10-14 07:56:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 75.2 |
| edf9d67b-95d6-34f1-acfb-a8b08515be41 | -18.2754 | -56.517 | 2024-10-14 07:56:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 151.1 |
| 660e73c9-8f9b-3579-abb5-8a6a1119554a | -18.275 | -56.5378 | 2024-10-14 07:56:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 110.5 |
| 46e31c97-2073-3f79-8cc2-1219acd95408 | -18.2559 | -56.4988 | 2024-10-14 07:56:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 90.4 |
| e9609266-0292-3062-8328-6a2a6bbd3c7f | -18.2555 | -56.5196 | 2024-10-14 07:56:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 122.5 |
| 58f3f80b-a165-34e4-87f4-7f0899274b62 | -18.2551 | -56.5405 | 2024-10-14 07:56:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 78.5 |
| 61e930ff-ca1e-31d3-ad15-843317937066 | -18.2342 | -56.6055 | 2024-10-14 07:56:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 71.4 |
| 73387ffc-e023-38d3-955a-0610d9057a43 | -18.2144 | -56.6081 | 2024-10-14 07:56:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 72.5 |
| d66a755d-65b3-3eb4-b2dc-8347e705d415 | -3.29 | -42.83 | 2024-10-14 08:05:09 | MSG-03 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4f793fbe-f7d2-3378-9c00-4fc7fa9e84cb | -18.2342 | -56.6055 | 2024-10-14 08:06:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 63.5 |
| f61f65f3-4fae-3c1c-94d0-cfccf764999c | -18.2551 | -56.5405 | 2024-10-14 08:16:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 145.3 |
| 5c4159ad-85ce-31f8-b608-8a4be3eecb62 | -18.2555 | -56.5196 | 2024-10-14 08:16:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 216.1 |
| e8a0b2d0-4ea0-3565-afa3-684024273189 | -18.2559 | -56.4988 | 2024-10-14 08:16:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 136.5 |
| 54024300-3130-3496-94b9-77cae59d9b71 | -18.275 | -56.5378 | 2024-10-14 08:16:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 106.0 |
| e470f03e-b22d-3565-8248-a1f6ec585cca | -18.2754 | -56.517 | 2024-10-14 08:16:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 145.5 |
| 4d0dc327-fa0a-3a88-b5e7-c0f7a0c0757a | -18.2757 | -56.4962 | 2024-10-14 08:16:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 70.7 |
| 5e9f2518-d352-3d4e-82e4-716479dfdecf | -18.2342 | -56.6055 | 2024-10-14 08:26:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 61.8 |
| c715fb47-f5a4-3c8a-bd89-c3abce4b9cfd | -18.2551 | -56.5405 | 2024-10-14 08:26:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 204.6 |
| 730b0f2c-8a38-3e9c-a8db-f848d1028a5c | -18.2555 | -56.5196 | 2024-10-14 08:26:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 237.2 |
| 4aa2600d-3229-3e8e-925d-ccb111d9f2ef | -18.2559 | -56.4988 | 2024-10-14 08:26:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 103.3 |
| f2a059f5-75e8-33d3-810e-65e369d79b0e | -18.275 | -56.5378 | 2024-10-14 08:26:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 156.3 |
| 2940c0b8-ab19-37d1-938b-329e495a11f7 | -18.2754 | -56.517 | 2024-10-14 08:26:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 180.6 |
| 9a763ac0-3957-31aa-bed7-246fcbf62c9b | -18.2757 | -56.4962 | 2024-10-14 08:26:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 73.2 |
| 017fd03d-c93a-3bd2-9f51-f19be83dbd75 | -18.2338 | -56.6263 | 2024-10-14 08:36:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 51.5 |
| 89247807-042d-33ae-9ec4-3f8f7134d35e | -18.2144 | -56.6081 | 2024-10-14 08:36:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 78.8 |
| 382e41da-9f60-3c60-aa49-58ceeaf683fa | -18.2342 | -56.6055 | 2024-10-14 08:36:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 83.3 |
| f35a1987-7def-35fd-94e5-c8f303dd71ee | -17.196 | -57.4357 | 2024-10-14 08:46:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 85.1 |
| 15dd2393-b73a-322e-8e61-b106c5fb2cd5 | -17.1957 | -57.4562 | 2024-10-14 08:46:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 66.8 |
| 0afebf4c-2e27-3151-8e9d-c22f22cb3297 | -10.89 | -44.68 | 2024-10-14 11:04:21 | MSG-03 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| eb21023d-3ac9-356d-908d-d968ec31ad2a | -10.92 | -44.69 | 2024-10-14 11:04:21 | MSG-03 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 77abd25d-022b-3c5e-995d-0f94aa41e430 | -10.92 | -44.74 | 2024-10-14 11:04:21 | MSG-03 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e7433914-43be-3a11-b017-5616631e2ca8 | -10.9116 | -44.7048 | 2024-10-14 11:26:09 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 172.3 |
| af90b126-6de1-3a79-8f5f-bc63d7d7972b | -10.9116 | -44.7048 | 2024-10-14 11:36:09 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 265.6 |
| c632a03f-003c-3b8e-b4cd-6b1e7cfc17bb | -10.912 | -44.6816 | 2024-10-14 11:36:09 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 136.6 |
| bae9972e-d819-3e54-be4c-a6a3ce64268c | -10.8925 | -44.7074 | 2024-10-14 11:36:09 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 98.2 |
| 1c72fe1f-989e-3be8-a5ba-cbed874fccc2 | -11.2258 | -44.1952 | 2024-10-14 11:36:11 | GOES-16 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 84.4 |
| 53edad8a-2e3a-34ba-b73e-7193306c93a4 | -11.245 | -44.1924 | 2024-10-14 11:36:11 | GOES-16 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 177.2 |
| 9db1cb03-57de-32b6-87ce-a2950f985299 | -11.2454 | -44.169 | 2024-10-14 11:36:11 | GOES-16 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 80.5 |
| c121e247-1116-3810-ac1d-b39fa586fb0d | -10.3303 | -46.58 | 2024-10-14 11:46:06 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 79.2 |
| 4154adda-48ad-3fff-90b4-5b640f4697d2 | -10.9116 | -44.7048 | 2024-10-14 11:46:09 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 186.2 |
| 74012826-5294-3bdb-9031-b9561dbaab80 | -10.8925 | -44.7074 | 2024-10-14 11:46:09 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 76.4 |
| ab8913b6-9ed0-378c-9a0d-c4792a8a8fb7 | -10.912 | -44.6816 | 2024-10-14 11:46:09 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 99.7 |
| 88047fb8-4fe3-3664-b4ff-be319fa8a9b5 | -10.9307 | -44.7021 | 2024-10-14 11:46:09 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 78.7 |
| 46c7723e-bf28-3c3e-ab8c-f1566663c4be | -10.9116 | -44.7048 | 2024-10-14 11:56:09 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 202.3 |
| 09934c53-6b11-3b3a-952c-d8d223936502 | -10.912 | -44.6816 | 2024-10-14 11:56:09 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 101.7 |
| 3cc479bf-c30c-32bf-a76a-f457518982d0 | -10.90864 | -44.69201 | 2024-10-14 12:04:00 | TERRA_M-T | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 162.3 |
| d0698974-3944-3c25-a504-3ce1d706e199 | -10.90517 | -44.71272 | 2024-10-14 12:04:00 | TERRA_M-T | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 191.1 |
| 5ea7b3e7-c40b-346b-b9d4-d8b7bf5fa31d | -10.69002 | -41.41772 | 2024-10-14 12:04:00 | TERRA_M-T | UMBURANAS | BAHIA | Brasil | 2932457 | 29 | 33 | nan | nan | nan | Caatinga | 14.0 |
| 3f2838a7-97f8-31c6-b162-19436e4d5bde | -10.65438 | -40.52273 | 2024-10-14 12:04:00 | TERRA_M-T | ANTÔNIO GONÇALVES | BAHIA | Brasil | 2901809 | 29 | 33 | nan | nan | nan | Caatinga | 87.2 |
| 65e610e8-b73d-3be1-9339-ae2ca52a4c01 | -10.378 | -39.23906 | 2024-10-14 12:04:00 | TERRA_M-T | MONTE SANTO | BAHIA | Brasil | 2921500 | 29 | 33 | nan | nan | nan | Caatinga | 45.3 |
| 0e71026f-1d0c-32bf-b3ce-0a01cd20ff34 | -10.08269 | -44.20124 | 2024-10-14 12:04:00 | TERRA_M-T | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 114.2 |
| 6ff2c0e3-37ab-3910-a3c4-d786c9d76125 | -10.06019 | -44.25848 | 2024-10-14 12:04:00 | TERRA_M-T | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 359.8 |
| 50bfdf9c-5fd3-3647-8ee2-80cea86e2eff | -10.06347 | -44.23855 | 2024-10-14 12:04:00 | TERRA_M-T | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 106.8 |
| 15ce11a0-1c39-3330-8cee-ef69e8044ec4 | -8.53218 | -45.99124 | 2024-10-14 12:04:00 | TERRA_M-T | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 45.6 |
| 85711aae-39f6-310f-96d9-41785d84275d | -10.03438 | -47.35764 | 2024-10-14 12:04:00 | TERRA_M-T | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 110.9 |
| 9d9f335e-b2fc-3707-a4b9-da7ea40af51d | -10.33818 | -46.59379 | 2024-10-14 12:04:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 69.8 |
| 4a7480b3-c073-37c5-b83f-0d38ca9b504d | -10.34185 | -46.58732 | 2024-10-14 12:04:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 93.2 |
| a347d8c8-6ad9-38bd-9349-9b3dfc88373d | -10.34343 | -46.56433 | 2024-10-14 12:04:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 31.3 |
| ab910fa2-a805-3882-9def-5266082e3048 | -6.94796 | -45.20887 | 2024-10-14 12:04:00 | TERRA_M-T | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 39.5 |
| 888638f7-2527-3933-aa38-3dad8cabb6e6 | -6.94836 | -45.21584 | 2024-10-14 12:04:00 | TERRA_M-T | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 43.3 |
| 0e452c34-a1b6-3fe7-b316-e1fb5dbbb53f | -7.13602 | -44.80712 | 2024-10-14 12:04:00 | TERRA_M-T | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 30.6 |
| 5f276033-cba8-3f1d-bd48-5cedc9455824 | -7.1395 | -45.72593 | 2024-10-14 12:04:00 | TERRA_M-T | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 39.2 |
| cb558b81-ff8d-3cb1-a69d-26cefada8c5a | -8.52999 | -45.99694 | 2024-10-14 12:04:00 | TERRA_M-T | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 39.0 |
| c836c14a-7041-3f66-bb5c-c6d686c97f6e | -9.70546 | -46.46211 | 2024-10-14 12:04:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 34.7 |
| cb86a7c2-ac76-32b7-b5c2-bbb7de4a5b54 | -9.98869 | -47.33588 | 2024-10-14 12:04:00 | TERRA_M-T | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 95.0 |
| fdddaade-ca3b-31d2-9334-8d1c1385bd1f | -10.07945 | -44.22105 | 2024-10-14 12:04:00 | TERRA_M-T | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 65.4 |
| dab4a324-9606-3ada-8337-5de80f656f16 | -9.48873 | -45.84969 | 2024-10-14 12:04:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 165.1 |
| 47e61eb2-8618-391d-9d0d-cefd8126564c | -10.07293 | -44.26089 | 2024-10-14 12:04:00 | TERRA_M-T | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 41.0 |
| 389be26c-361b-3b83-8a5e-dcdbc538eb57 | -9.99581 | -47.34285 | 2024-10-14 12:04:00 | TERRA_M-T | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 112.9 |
| 930aee58-1e5b-3b59-b508-5c7a00082cf9 | -7.64489 | -44.67214 | 2024-10-14 12:04:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 48.0 |
| 6a9186f3-63f9-3a27-b2d4-05ee3055dc78 | -9.16887 | -40.58607 | 2024-10-14 12:04:00 | TERRA_M-T | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 19.0 |
| dccb4557-4226-3202-830c-5aacbd9db6f5 | -8.82209 | -45.36296 | 2024-10-14 12:04:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 30.9 |
| 4562f6c1-bcfe-3bcc-900f-050479647beb | -8.51451 | -40.23462 | 2024-10-14 12:04:00 | TERRA_M-T | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 10.5 |
| 67bc96a0-1560-379d-8942-d851a332ffff | -8.50146 | -44.87664 | 2024-10-14 12:04:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 28.1 |
| d2f9cc2c-b439-34ef-b799-287efaeba82b | -9.4934 | -45.82247 | 2024-10-14 12:04:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 77.8 |
| 014f0222-e052-39e7-9823-0085a71ffb15 | -8.49779 | -44.8991 | 2024-10-14 12:04:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 286.8 |
| 774b2092-e921-3b8c-8fb2-c50cb71c6461 | -8.38743 | -41.75365 | 2024-10-14 12:04:00 | TERRA_M-T | CAMPO ALEGRE DO FIDALGO | PIAUÍ | Brasil | 2202117 | 22 | 33 | nan | nan | nan | Caatinga | 20.8 |
| 309fb3ca-0521-34fc-8636-27a05236c47d | -8.3401 | -42.73999 | 2024-10-14 12:04:00 | TERRA_M-T | BREJO DO PIAUÍ | PIAUÍ | Brasil | 2201988 | 22 | 33 | nan | nan | nan | Caatinga | 57.9 |
| cece2122-af1b-3d9d-bd36-3fc006bc97c6 | -8.33812 | -42.72921 | 2024-10-14 12:04:00 | TERRA_M-T | BREJO DO PIAUÍ | PIAUÍ | Brasil | 2201988 | 22 | 33 | nan | nan | nan | Caatinga | 16.7 |
| 47fdb533-a800-3de1-b882-5b79ce878756 | -8.33761 | -42.75625 | 2024-10-14 12:04:00 | TERRA_M-T | BREJO DO PIAUÍ | PIAUÍ | Brasil | 2201988 | 22 | 33 | nan | nan | nan | Caatinga | 74.7 |
| 180d3685-e8f4-37c0-b2bf-d1a13d8ab16a | -8.33552 | -42.74532 | 2024-10-14 12:04:00 | TERRA_M-T | BREJO DO PIAUÍ | PIAUÍ | Brasil | 2201988 | 22 | 33 | nan | nan | nan | Caatinga | 80.5 |
| 1e82126e-21f8-310e-a275-bad0535bfc52 | -8.33288 | -42.76162 | 2024-10-14 12:04:00 | TERRA_M-T | BREJO DO PIAUÍ | PIAUÍ | Brasil | 2201988 | 22 | 33 | nan | nan | nan | Caatinga | 70.8 |
| 61cd090d-1ad4-38c9-921d-2bcc0754b8c3 | -8.25144 | -44.84772 | 2024-10-14 12:04:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 33.2 |
| 80397f6a-9437-332b-8337-b16b964b36d0 | -8.24753 | -44.87093 | 2024-10-14 12:04:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 34.6 |
| e2e34aac-16a9-3d3d-a0fb-e489e81cf618 | -8.24255 | -44.86322 | 2024-10-14 12:04:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 48.6 |
| 7545cd0d-f73e-3285-b389-ea1bdc7d7c63 | -7.95446 | -38.6657 | 2024-10-14 12:04:00 | TERRA_M-T | SÃO JOSÉ DO BELMONTE | PERNAMBUCO | Brasil | 2613503 | 26 | 33 | nan | nan | nan | Caatinga | 13.1 |
| 9eedbea6-ea2d-3275-98fe-9eeee0073461 | -7.84239 | -43.9929 | 2024-10-14 12:04:00 | TERRA_M-T | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 117.0 |
| f8c26c78-5327-39c7-85de-f4b4977ffdcc | -7.84219 | -44.00669 | 2024-10-14 12:04:00 | TERRA_M-T | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 300.4 |
| 3e29e9ec-8a3c-3ff2-8020-a457cc4b59e6 | -7.83906 | -44.01299 | 2024-10-14 12:04:00 | TERRA_M-T | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 383.4 |
| d31578da-d9a6-3d59-b3b0-ef0c530f18cd | -7.83225 | -43.98489 | 2024-10-14 12:04:00 | TERRA_M-T | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 38.7 |
| 2881eb7d-1956-3527-969b-e56bed1af364 | -10.05687 | -44.27863 | 2024-10-14 12:04:00 | TERRA_M-T | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 28.3 |
| afc5fca6-6ebd-33e7-a520-df198193a65e | -7.82913 | -44.00454 | 2024-10-14 12:04:00 | TERRA_M-T | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 295.5 |


[Clique aqui para ver as próximas entradas](README131.md)
