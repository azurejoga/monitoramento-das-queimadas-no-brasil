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

## Dados Diários - Página 95

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 46e06c48-f75c-35ae-ade2-1a22b75b758d | -19.47835 | -56.67667 | 2024-10-30 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 9bfccce7-1ae5-3ec5-9d89-f381c0600a3e | -19.62453 | -56.70025 | 2024-10-30 05:12:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 8.2 |
| 95b66251-cd57-315b-ae1c-05152a5fd3f9 | -19.62083 | -56.69969 | 2024-10-30 05:12:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.0 |
| ff9aedb1-cdad-33da-b407-fc5442d62a7a | -19.6202 | -56.70431 | 2024-10-30 05:12:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 7.6 |
| 7b1ed4d8-7885-3643-bd2d-955dc5f22c4d | -19.61957 | -56.70892 | 2024-10-30 05:12:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 7.6 |
| 69b87cf1-541a-351b-8706-76091efe1b02 | -19.61894 | -56.71354 | 2024-10-30 05:12:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 6.8 |
| 3ca3b698-923e-3a49-ab4e-989db5a0d599 | -19.61713 | -56.69913 | 2024-10-30 05:12:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.0 |
| dbec750e-35ad-3a97-b6c9-018d50b8d949 | -19.6165 | -56.70375 | 2024-10-30 05:12:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 7.6 |
| 0b5bb280-b057-3913-95c3-dae2295c0979 | -19.61587 | -56.70837 | 2024-10-30 05:12:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 7.6 |
| 94114c0d-095e-3229-8e24-738ce5a84ee9 | -19.61524 | -56.71298 | 2024-10-30 05:12:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 6.8 |
| cd0d0fd4-9418-3c84-9541-dfa07f79e81b | -19.61461 | -56.7176 | 2024-10-30 05:12:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 6.8 |
| e6117751-3821-38bc-968b-8568cbaae987 | -19.6128 | -56.70319 | 2024-10-30 05:12:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 4af80f3c-caa6-34e9-b259-a1fc1a9bfa9f | -19.61217 | -56.70781 | 2024-10-30 05:12:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 883322ad-4295-3e6d-a558-ad100d2a094d | -19.61154 | -56.71243 | 2024-10-30 05:12:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 8.2 |
| bd84e1d5-e5a2-3019-b1d3-89cc5c624a23 | -19.61091 | -56.71704 | 2024-10-30 05:12:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 8.2 |
| 082e8a53-11f9-3b28-afcf-1f45cffbba05 | -19.6091 | -56.70263 | 2024-10-30 05:12:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 1bb89ab1-b2ee-3ddc-b6e7-21a58071f5c7 | -19.60847 | -56.70725 | 2024-10-30 05:12:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| ccd885cf-71d1-3b0c-aa10-feebec19d174 | -19.60784 | -56.71187 | 2024-10-30 05:12:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 8.2 |
| 988edf9f-8bac-3efc-8439-5f82f681ed1f | -19.60722 | -56.71648 | 2024-10-30 05:12:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 8.2 |
| 1a9ea2c3-8c92-3928-b54d-323e55eb3ae9 | -19.6054 | -56.70208 | 2024-10-30 05:12:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 8.1 |
| 9d6bed99-3d9c-30a1-900b-7f03b0e21774 | -19.60477 | -56.7067 | 2024-10-30 05:12:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 8.1 |
| ba3b7910-9728-3cae-9e60-0b8854e0b8ae | -19.60415 | -56.71132 | 2024-10-30 05:12:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 13.8 |
| f91f1e3b-fd27-3b45-bcb9-ae8dbc5c655f | -19.60352 | -56.71592 | 2024-10-30 05:12:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 13.8 |
| 0c82de83-477d-3f93-9449-c710058d5aa4 | -19.60289 | -56.72054 | 2024-10-30 05:12:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.8 |
| dc1bca6c-e22d-3ad9-970e-5ded9ef40895 | -19.6017 | -56.70152 | 2024-10-30 05:12:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 8.1 |
| f846531b-8dfc-337b-867b-e32b86851bc6 | -19.60108 | -56.70613 | 2024-10-30 05:12:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 8.1 |
| c29a6845-e6a1-35f4-93d3-221490245acb | -19.60045 | -56.71075 | 2024-10-30 05:12:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 13.8 |
| 944c8f3e-c68d-3e4a-bdaf-bb7908386df8 | -19.59982 | -56.71536 | 2024-10-30 05:12:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 13.8 |
| a60dcc68-06c6-379a-bdf2-b442a0eb2bb9 | -19.5992 | -56.71997 | 2024-10-30 05:12:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.8 |
| e01f0de9-d598-33b7-9006-7b7e93418534 | -19.598 | -56.70095 | 2024-10-30 05:12:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.9 |
| c3c07710-4428-3f8d-8704-ccc227b58bc7 | -19.59738 | -56.70558 | 2024-10-30 05:12:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 1a597d92-662b-3912-a23e-3721ee6a528c | -19.59675 | -56.71019 | 2024-10-30 05:12:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 6.2 |
| 1d500ccf-e255-37b5-a973-9f5413202410 | -19.59368 | -56.70502 | 2024-10-30 05:12:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 6ebf1c3f-ab7d-383a-8118-aafb909f2817 | -19.58874 | -56.71369 | 2024-10-30 05:12:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 5a0bb51b-f6ad-3179-a7cf-9a647ae813ce | -19.58812 | -56.71829 | 2024-10-30 05:12:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 6.1 |
| 780e61c7-6cfb-36ec-8cf6-c27d03019045 | -19.58628 | -56.7039 | 2024-10-30 05:12:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| df01a4ba-e69e-3d43-a834-2e4c1e3de3b8 | -19.58566 | -56.70852 | 2024-10-30 05:12:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 06baf98b-b088-35e0-984c-0da11db319f2 | -19.58504 | -56.71313 | 2024-10-30 05:12:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.5 |
| d000b665-5fa9-336c-8034-094dc67a1a41 | -19.58442 | -56.71774 | 2024-10-30 05:12:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 6.1 |
| 729313fc-8b8b-37a0-b236-d45e46161a71 | -19.5838 | -56.72234 | 2024-10-30 05:12:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 6.1 |
| 3bba852e-1d0d-3c53-b3cb-10eebaa2d1ce | -19.58196 | -56.70796 | 2024-10-30 05:12:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 6.2 |
| 1141059b-ef02-3d4d-aeaa-de05d4a26141 | -19.58134 | -56.71257 | 2024-10-30 05:12:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 6.2 |
| 1fa7f238-79c8-3dde-a05f-ef89c38fcf1a | -19.58072 | -56.71718 | 2024-10-30 05:12:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 10.9 |
| 0166242e-f66d-3ee6-986f-581e199fb4ff | -19.5801 | -56.72178 | 2024-10-30 05:12:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 10.9 |
| 45b89f44-230d-33fa-99ad-6abdbc246e56 | -19.57827 | -56.7074 | 2024-10-30 05:12:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 6.2 |
| ddd86e01-202d-3bc4-bcec-5f1a8f59e15b | -19.57765 | -56.71201 | 2024-10-30 05:12:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 6.2 |
| 2e0cd840-1ec0-3020-ba8f-2b35d3b3f235 | -19.57703 | -56.71662 | 2024-10-30 05:12:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 10.9 |
| 8c6dabad-23d6-3488-9ea3-05e9af362305 | -19.57641 | -56.72123 | 2024-10-30 05:12:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 10.9 |
| 62f0ab8f-3a41-355d-85de-001ba00a183f | -19.57579 | -56.72583 | 2024-10-30 05:12:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.5 |
| a9339722-bd87-3dc7-bbd6-a750d457db3e | -19.57457 | -56.70684 | 2024-10-30 05:12:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 7.7 |
| 453d3168-33c1-383e-9084-e55d7f30d096 | -19.57395 | -56.71145 | 2024-10-30 05:12:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 7.7 |
| dccd770f-6218-3c99-a474-4d5e5b63599d | -19.57333 | -56.71606 | 2024-10-30 05:12:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 8.1 |
| c0f6eff8-92ff-35bc-90fe-e0a0f5c07cd4 | -19.57271 | -56.72067 | 2024-10-30 05:12:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 8.1 |
| 3ff64ce5-3584-3399-ba28-d111c740d0eb | -19.57026 | -56.71089 | 2024-10-30 05:12:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 7.7 |
| 93c143ab-f1a1-3215-ade5-1b9ddcf7950a | -19.56964 | -56.7155 | 2024-10-30 05:12:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 8.1 |
| 1049ea02-e8be-3091-bf3e-ad56356cfae4 | -19.56902 | -56.72011 | 2024-10-30 05:12:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 8.1 |
| 7f0fc539-a091-36d5-a34d-f77112c3930e | -19.54543 | -56.71031 | 2024-10-30 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| a481f163-f665-322d-b9dd-a7712d71a1e0 | -19.54174 | -56.70975 | 2024-10-30 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.2 |
| 99798191-16c6-35b0-8597-e9ac17d03aa2 | -19.5411 | -56.71435 | 2024-10-30 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.2 |
| 80603707-5ee9-3041-95ef-2b4893ed64e2 | -19.53804 | -56.70919 | 2024-10-30 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.2 |
| 7f92608f-639f-363a-a391-55b02591bf69 | -19.53741 | -56.71379 | 2024-10-30 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.2 |
| d2092b89-8926-32d6-8506-074eb2000253 | -19.53677 | -56.71839 | 2024-10-30 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.2 |
| 9d540a11-7762-3bff-893f-367314e5fd20 | -19.53435 | -56.70864 | 2024-10-30 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.5 |
| 35ddd3f6-47a2-37e4-8177-fc34fee83b3f | -19.53372 | -56.71324 | 2024-10-30 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 09c73a52-f5d4-3f18-99cb-6a48af1f3bc1 | -19.53066 | -56.70808 | 2024-10-30 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.5 |
| b967eb91-344b-3308-a167-db3e59da4fc1 | -19.53002 | -56.71268 | 2024-10-30 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 7b50785d-fc40-3da2-9a6b-6cf73bb96eba | -19.52759 | -56.70292 | 2024-10-30 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| bee29cce-ff8e-343f-9e27-e8957e35689a | -19.52696 | -56.70752 | 2024-10-30 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| ed9de300-2881-36a6-afd1-6d8ee0ff647b | -19.52633 | -56.71212 | 2024-10-30 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.9 |
| 3c2cbd99-40d0-3067-b583-b7199d750f25 | -19.5239 | -56.70236 | 2024-10-30 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 8c5b4572-2977-3a40-88b7-45299b712b22 | -19.52327 | -56.70696 | 2024-10-30 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| de9a2580-357d-3016-bb94-55570cd6ae2b | -19.49371 | -56.70251 | 2024-10-30 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 667e9eb9-1570-35f4-b871-e3659c70bff2 | -19.49002 | -56.70195 | 2024-10-30 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| a82c67c0-6525-3858-aa97-0745df0b6733 | -21.55985 | -54.20883 | 2024-10-30 05:14:00 | NOAA-20 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 916abd4a-8b30-3ee8-9a12-a010e814f408 | -21.20175 | -54.44112 | 2024-10-30 05:14:00 | NOAA-20 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b77b87cc-956b-36bd-ba35-5a63181da097 | -24.00905 | -54.1441 | 2024-10-30 05:14:00 | NOAA-20 | GUAÍRA | PARANÁ | Brasil | 4108809 | 41 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| 9ce2a6c9-fd30-3d81-9b31-8e1052a81f98 | -20.88493 | -57.26032 | 2024-10-30 05:14:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 68a08cb9-a1bc-3168-8991-6af4fee6e365 | -23.14886 | -52.66826 | 2024-10-30 05:14:00 | NOAA-20 | MIRADOR | PARANÁ | Brasil | 4115903 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 4b803851-3335-3610-943f-6727b2bf4b32 | -23.14452 | -52.6678 | 2024-10-30 05:14:00 | NOAA-20 | MIRADOR | PARANÁ | Brasil | 4115903 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 661af05e-c19f-3f3d-a3e8-de04e1dda91b | -23.75107 | -54.50469 | 2024-10-30 05:14:00 | NOAA-20 | JAPORÃ | MATO GROSSO DO SUL | Brasil | 5004809 | 50 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| fbe239ab-458d-3c20-9ccc-4387d97ee2bb | -24.0085 | -54.14915 | 2024-10-30 05:14:00 | NOAA-20 | GUAÍRA | PARANÁ | Brasil | 4108809 | 41 | 33 | nan | nan | nan | Mata Atlântica | 12.0 |
| f1b74847-4f4f-3e83-95c4-2abd213bf4d4 | -24.00795 | -54.15421 | 2024-10-30 05:14:00 | NOAA-20 | GUAÍRA | PARANÁ | Brasil | 4108809 | 41 | 33 | nan | nan | nan | Mata Atlântica | 12.0 |
| a3f58674-1ba2-362e-ab28-d7567bdd0ad2 | -24.00393 | -54.14857 | 2024-10-30 05:14:00 | NOAA-20 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 12.0 |
| 31295ce8-72ea-34f8-a12b-c8e04ed52faa | -24.00338 | -54.15363 | 2024-10-30 05:14:00 | NOAA-20 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 12.0 |
| 18353e8a-f357-3c45-8378-de02701c18b2 | -24.00283 | -54.15867 | 2024-10-30 05:14:00 | NOAA-20 | GUAÍRA | PARANÁ | Brasil | 4108809 | 41 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| 9b0fc414-9c89-33d4-9cd3-6c9e1d14b71d | -23.98941 | -54.11076 | 2024-10-30 05:14:00 | NOAA-20 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |
| 17116aac-7b55-3956-8c2e-4fe78e13bf0e | -23.98483 | -54.11018 | 2024-10-30 05:14:00 | NOAA-20 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 007aad9f-a3c4-3f2d-bb4e-ef3f8856e276 | -23.98429 | -54.11525 | 2024-10-30 05:14:00 | NOAA-20 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 8.0 |
| 42a64559-dc8b-36c7-9c4e-c0c9b22c57e8 | -2.833 | -49.2413 | 2024-10-30 05:15:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 46.8 |
| d1b4fef8-ef25-3357-856f-0702ff76cb2b | -3.0734 | -54.167 | 2024-10-30 05:15:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 46.1 |
| 63bfc5ca-cad9-3a26-9986-190b61d59a3f | -3.1097 | -54.2865 | 2024-10-30 05:15:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 48.9 |
| a297c921-9eed-3844-a85e-8a16721d06d6 | -3.1098 | -54.2665 | 2024-10-30 05:15:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 54.1 |
| 9ee61b96-009e-3894-9ec9-14b0d3784369 | -3.1602 | -50.5812 | 2024-10-30 05:15:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 29.0 |
| 9ff1d34b-1fd2-37aa-838a-f9149a28bc5f | -3.1786 | -50.6016 | 2024-10-30 05:15:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 29.4 |
| 32ca2895-55d2-343c-bdf3-4d6b67654cae | -3.1787 | -50.5807 | 2024-10-30 05:15:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 30.0 |
| f8a8ffdd-63c3-3635-a620-afdfe0116fda | -3.1281 | -54.266 | 2024-10-30 05:15:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 40.6 |
| ba8946b5-694a-30dd-9641-3850e8e86c00 | -3.1601 | -50.6021 | 2024-10-30 05:15:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 29.2 |
| 31426f5a-73e6-3a03-b862-c08f4afb7495 | -3.2535 | -50.3479 | 2024-10-30 05:15:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 104.7 |
| f5ad5d2b-5c85-3ef5-8227-3ae47e4af583 | -3.2718 | -50.3683 | 2024-10-30 05:15:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 26.9 |
| 6c3a6a38-f5c6-3f6a-9cec-ddbd89c05ec1 | -3.2719 | -50.3473 | 2024-10-30 05:15:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 134.9 |


[Clique aqui para ver as próximas entradas](README96.md)
