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

## Dados Diários - Página 76

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 949ef908-4639-3f2d-a696-76f1a08bd322 | -3.40875 | -42.26657 | 2024-10-03 04:25:00 | NOAA-21 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| abe4cab5-84a2-39b0-91c5-431d885dd3d9 | -3.4081 | -42.27077 | 2024-10-03 04:25:00 | NOAA-21 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 169.1 |
| a957c51b-8228-3285-b2c9-fb4f1447f34c | -3.40744 | -42.27504 | 2024-10-03 04:25:00 | NOAA-21 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 169.1 |
| a8c8f19e-e44d-3f2b-910b-179a5dff9c56 | -3.40678 | -42.27929 | 2024-10-03 04:25:00 | NOAA-21 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 85.7 |
| 32845f4c-b0b9-3317-bff3-b703270ea9c2 | -3.40613 | -42.2835 | 2024-10-03 04:25:00 | NOAA-21 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 85.7 |
| 8377fb52-1c59-39f8-aeb4-6f2d8560b966 | -3.40547 | -42.2877 | 2024-10-03 04:25:00 | NOAA-21 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1c31d192-65d5-3c11-a20b-ca0281d74bd2 | -3.40512 | -42.26602 | 2024-10-03 04:25:00 | NOAA-21 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6bee7bce-17ba-3a81-bd71-fa20c3659891 | -3.40482 | -42.29192 | 2024-10-03 04:25:00 | NOAA-21 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 482601f9-80ba-3b84-b4b7-6c5c15e79652 | -3.40447 | -42.27024 | 2024-10-03 04:25:00 | NOAA-21 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 169.1 |
| 77d3b474-dd4c-3510-bede-bdeeb3be5bea | -3.40381 | -42.2745 | 2024-10-03 04:25:00 | NOAA-21 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 169.1 |
| 039c7d31-9097-3509-85f5-b6f5e7528c0e | -3.40315 | -42.27875 | 2024-10-03 04:25:00 | NOAA-21 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 85.7 |
| 2ecbf1ce-c8d4-39ac-909b-f4fe746724b1 | -3.4025 | -42.28297 | 2024-10-03 04:25:00 | NOAA-21 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 85.7 |
| 81fc0f4a-0c14-3781-a8be-a7523f0a1e7c | -3.40185 | -42.28716 | 2024-10-03 04:25:00 | NOAA-21 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 55b32c2d-f847-3c61-be45-7e78f5f8932e | -3.40149 | -42.26547 | 2024-10-03 04:25:00 | NOAA-21 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 5d1b4a69-ea2f-3ea8-87a4-549015a2e5f7 | -3.40083 | -42.26971 | 2024-10-03 04:25:00 | NOAA-21 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| a7f202f8-e79d-3620-b723-be9003aefe15 | -3.40018 | -42.27396 | 2024-10-03 04:25:00 | NOAA-21 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| de5259a5-92d7-3e3b-bcd6-2d49eb01e22a | -3.39952 | -42.27821 | 2024-10-03 04:25:00 | NOAA-21 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 0124e797-3782-3ca8-96b8-0c054bd3aa7b | -3.39887 | -42.28242 | 2024-10-03 04:25:00 | NOAA-21 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 86eb5130-4dac-3c37-ad3d-dcc5ef0d24f0 | -3.39822 | -42.28662 | 2024-10-03 04:25:00 | NOAA-21 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 97c52465-55b4-3f3d-9e9b-4bf2fd414ddb | -3.39757 | -42.29082 | 2024-10-03 04:25:00 | NOAA-21 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6075304c-de19-3bef-b303-3e3106cb20c9 | -3.3972 | -42.26919 | 2024-10-03 04:25:00 | NOAA-21 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 62396ebd-e53e-3228-892d-3a7c17bcb46d | -3.39655 | -42.27343 | 2024-10-03 04:25:00 | NOAA-21 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| bf5ecba4-e897-308d-86f7-70a2d22d42a7 | -3.39589 | -42.27767 | 2024-10-03 04:25:00 | NOAA-21 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 28c14544-c285-32d0-8c45-337fce931ca5 | -3.39524 | -42.28189 | 2024-10-03 04:25:00 | NOAA-21 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 7676380d-c95f-3b26-b686-a685cd9551a5 | -3.39459 | -42.28607 | 2024-10-03 04:25:00 | NOAA-21 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fba166c2-d748-3233-a72f-ad310dc1d435 | -3.39357 | -42.26865 | 2024-10-03 04:25:00 | NOAA-21 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3f3d583b-4b98-303a-ade8-f1e3506ed253 | -3.39161 | -42.28135 | 2024-10-03 04:25:00 | NOAA-21 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e77aafb6-3341-3ab4-ae53-fcc2fcadd06b | -3.39032 | -42.28972 | 2024-10-03 04:25:00 | NOAA-21 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 185b153e-cf18-3be7-84b7-332574511f50 | -4.69746 | -42.66341 | 2024-10-03 04:25:00 | NOAA-21 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 1a9b8d2c-dbce-3ebb-8505-8579857eac8b | -4.81717 | -42.76139 | 2024-10-03 04:25:00 | NOAA-21 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 50c7dab7-1c7d-37a6-a778-4c31365b78e7 | -4.48917 | -42.87006 | 2024-10-03 04:25:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 38.3 |
| 130b345e-0fd4-3cd8-9e48-31a15ad03431 | -4.48855 | -42.87413 | 2024-10-03 04:25:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 38.3 |
| 3c7d113b-e2ed-34fa-91f1-ea91d9b53884 | -4.48793 | -42.87819 | 2024-10-03 04:25:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 38.9 |
| c03da8e7-86e1-3bb2-8139-5dc8d8a092e4 | -4.48499 | -42.87358 | 2024-10-03 04:25:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 38.3 |
| c5b73bc5-ead7-3233-9008-46bba4b19b16 | -4.48437 | -42.87763 | 2024-10-03 04:25:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 38.9 |
| e055a69a-310b-32ac-bab7-7052dcd8f154 | -4.48375 | -42.8817 | 2024-10-03 04:25:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 38.9 |
| c73b985e-d114-3e4c-9143-489f392c6f52 | -4.48081 | -42.87708 | 2024-10-03 04:25:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 3dacb703-f4f3-3078-8f69-14cd5c454b03 | -4.48019 | -42.88114 | 2024-10-03 04:25:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 11.3 |
| c838bc0c-d7e9-337a-8d54-9ead6891a512 | -4.46888 | -42.88356 | 2024-10-03 04:25:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9abb1815-2d9f-354f-a2cb-3e3a6d254125 | -4.46826 | -42.88763 | 2024-10-03 04:25:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 181bf95f-cdeb-3573-b2ec-459a78d6d253 | -3.94855 | -41.50909 | 2024-10-03 04:25:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 13f34e67-862d-3292-93a9-ed702049ae56 | -3.94783 | -41.51379 | 2024-10-03 04:25:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 917bf78a-adf8-3f66-9faa-989a08916405 | -3.94712 | -41.51846 | 2024-10-03 04:25:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 8.1 |
| 79550d1c-6ab8-38aa-b6f9-909848a0239c | -3.68059 | -42.96986 | 2024-10-03 04:25:00 | NOAA-21 | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| bc2f1c18-4360-3ef5-a0c3-f5e6802c5aa8 | -6.02532 | -43.19844 | 2024-10-03 04:25:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 7.4 |
| 32cb1ad1-88ce-33bc-9d9b-9aecb8f17ac0 | -5.91402 | -41.98884 | 2024-10-03 04:25:00 | NOAA-21 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 5bb49d39-fca8-3989-b214-825f8d2f3b02 | -5.90709 | -41.98307 | 2024-10-03 04:25:00 | NOAA-21 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 8.6 |
| a5e9fa6e-8e3c-3fc5-8c7f-7a74ea44df78 | -5.87758 | -43.05309 | 2024-10-03 04:25:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 676c7afb-bf1c-30c1-8880-1625dda7ca6f | -5.83079 | -42.5451 | 2024-10-03 04:25:00 | NOAA-21 | BARRO DURO | PIAUÍ | Brasil | 2201408 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 8dcd7189-8cea-319c-b803-e952cd64a669 | -5.8272 | -42.66845 | 2024-10-03 04:25:00 | NOAA-21 | AGRICOLÂNDIA | PIAUÍ | Brasil | 2200103 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| ab11b0fb-b184-382a-b1c2-2bee3e3ca03c | -5.82341 | -42.54406 | 2024-10-03 04:25:00 | NOAA-21 | BARRO DURO | PIAUÍ | Brasil | 2201408 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 44a79faf-4e9e-3f42-8ccb-5689c9390f02 | -5.82041 | -42.53899 | 2024-10-03 04:25:00 | NOAA-21 | BARRO DURO | PIAUÍ | Brasil | 2201408 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| ae7a77f4-0e4e-3b5b-8622-9e1bbfc80b48 | -5.76932 | -43.05004 | 2024-10-03 04:25:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 91ad885f-8251-3077-8bb3-94d01a25f89d | -5.74756 | -42.60156 | 2024-10-03 04:25:00 | NOAA-21 | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 4d38fd1f-8145-328d-9954-5f133984f5f4 | -5.73662 | -42.59951 | 2024-10-03 04:25:00 | NOAA-21 | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 1973fd86-146f-33a8-bef6-4007ceefdb09 | -5.73297 | -42.59884 | 2024-10-03 04:25:00 | NOAA-21 | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 6429e76d-edfb-3e91-b665-d327f065f139 | -5.6937 | -43.16397 | 2024-10-03 04:25:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 1.1 |
| b95b0d1b-dcc1-3b8a-abfa-8338c05c7d1c | -5.69014 | -43.16343 | 2024-10-03 04:25:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 97d454fb-aae2-38d1-a8a9-e79b8bdd89d1 | -5.57193 | -43.11086 | 2024-10-03 04:25:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Caatinga | 5.4 |
| ffc15568-0cbe-363b-ba33-c56159853960 | -5.56837 | -43.11033 | 2024-10-03 04:25:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 85e1e8b3-cbd3-3699-b886-63cc626a83a5 | -5.56774 | -43.11441 | 2024-10-03 04:25:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 78c9e4a1-0bd0-3553-a0fc-474310394410 | -5.5648 | -43.10981 | 2024-10-03 04:25:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 4e0e8380-0081-33eb-81df-bd2aa1bb88f4 | -5.53869 | -42.77189 | 2024-10-03 04:25:00 | NOAA-21 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| ccb4ab40-ac45-33fe-949b-a0bfbe645746 | -5.53806 | -42.7761 | 2024-10-03 04:25:00 | NOAA-21 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 9c148f2a-c93b-3b52-b44f-71236e5b1bb0 | -5.53444 | -42.77552 | 2024-10-03 04:25:00 | NOAA-21 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 058f5ad6-3e1d-3832-934c-41ef95fc0d22 | -5.53382 | -42.77973 | 2024-10-03 04:25:00 | NOAA-21 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 121efb69-5f07-3371-ab1e-c3efc773abf5 | -5.5302 | -42.77916 | 2024-10-03 04:25:00 | NOAA-21 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 31e43f9b-0af7-35b0-8817-6f283e6966d7 | -5.52658 | -42.77857 | 2024-10-03 04:25:00 | NOAA-21 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| b7be678e-fece-3416-987f-5b600c382209 | -5.52603 | -42.77516 | 2024-10-03 04:25:00 | NOAA-21 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 049fc369-5ab1-3b1d-b715-3eae04f61aca | -5.52538 | -42.77937 | 2024-10-03 04:25:00 | NOAA-21 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 76dbe6c8-2e4e-3fed-acd3-ba0e97769c7d | -6.19476 | -43.42107 | 2024-10-03 04:25:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4b8645ee-d1c2-3556-b4e8-b5f7f76f2886 | -5.41126 | -42.92336 | 2024-10-03 04:25:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 2.1 |
| b020a4df-918d-3095-a7ba-9427eb351495 | -5.40766 | -42.92281 | 2024-10-03 04:25:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 9e62a688-2757-38a6-ab8e-0b6dfb502b69 | -5.40407 | -42.92227 | 2024-10-03 04:25:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 2749b82c-b94c-3ef2-9d5e-0c0488bcfe51 | -5.32176 | -42.96655 | 2024-10-03 04:25:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 1.9 |
| cb9dcd9d-747e-3b11-89ca-260fe9b6b00e | -5.32114 | -42.97067 | 2024-10-03 04:25:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 004aaa92-bc01-3ba3-bf4f-34e9a820d664 | -5.31818 | -42.966 | 2024-10-03 04:25:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 826d5bd6-f7c6-388f-96d0-c7422a53e2dd | -5.31756 | -42.97012 | 2024-10-03 04:25:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 3ba48ff8-cd2a-3733-9f22-7abf98003fcc | -6.19416 | -43.4251 | 2024-10-03 04:25:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| a0473f3f-4a9c-3f92-9b72-04564a05f981 | -6.19123 | -43.42045 | 2024-10-03 04:25:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c6c7d4a6-5c5d-3cc6-9db2-3c32b9761a16 | -5.8821 | -43.42892 | 2024-10-03 04:25:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 27816b78-6dbc-3a43-8891-2de3a397c3d7 | -5.87917 | -43.42442 | 2024-10-03 04:25:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 60343530-6e7a-3710-849b-38cd0a929392 | -5.87857 | -43.42841 | 2024-10-03 04:25:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 3d624a18-ad1a-31fb-a764-98e1b9394d26 | -5.87798 | -43.43236 | 2024-10-03 04:25:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| c8ae11d1-c99d-3554-9d9d-5f211963f970 | -5.87445 | -43.43183 | 2024-10-03 04:25:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 25078850-26c6-3d9b-b51f-3823af2ab721 | -5.86507 | -43.42232 | 2024-10-03 04:25:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 841e9544-9327-37a5-83fd-d184ce25d009 | -5.86447 | -43.4263 | 2024-10-03 04:25:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 19a99969-ff27-3f6f-bb5d-ee20cb309a64 | -5.5823 | -43.25574 | 2024-10-03 04:25:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b3b38e3b-d72b-307e-a190-99c436800450 | -5.40914 | -43.10767 | 2024-10-03 04:25:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1deb27a3-dcf8-30a8-aa16-e5a5101718ec | -5.39847 | -43.10603 | 2024-10-03 04:25:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 030da87d-8a5b-3f1a-9e88-bfe0a897670a | -5.39785 | -43.1101 | 2024-10-03 04:25:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 44beaeaa-cfb3-3102-81fd-537e4cf978d5 | -5.39724 | -43.11416 | 2024-10-03 04:25:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 19ddc329-92b2-3346-91c2-ba3ee73f0635 | -5.39491 | -43.10548 | 2024-10-03 04:25:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 52a57501-6812-30f2-9c56-995f5220daaf | -6.27214 | -42.74681 | 2024-10-03 04:25:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| a1a1e19b-59f2-3d6e-af52-54539d4791cb | -6.26716 | -42.75491 | 2024-10-03 04:25:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 8109af24-e341-30dd-88d6-cff27f173e46 | -6.26651 | -42.7592 | 2024-10-03 04:25:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 36f49a77-b033-327b-b691-3d947913a524 | -6.26285 | -42.75866 | 2024-10-03 04:25:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| a662c9c2-1440-387a-8951-f4ae2f71b02e | -6.33536 | -43.42435 | 2024-10-03 04:25:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5b57ca0f-b03c-31bf-ad7c-6c05aa42994a | -6.30591 | -43.04505 | 2024-10-03 04:25:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 8f8086c0-8670-37f5-b451-1a57f52f967b | -6.30522 | -43.43221 | 2024-10-03 04:25:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README77.md)
