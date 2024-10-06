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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e8e00ffb-25e2-3dc6-b5b2-c1b35d50db96 | -16.636 | -55.492802 | 2024-10-06 00:46:47 | METOP-B | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 6a3f7c1b-2e34-3f45-a54c-c56151121318 | -16.6383 | -55.504799 | 2024-10-06 00:46:47 | METOP-B | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 17d233e0-e07e-3686-a5e7-09916ea86c9e | -16.6406 | -55.516899 | 2024-10-06 00:46:47 | METOP-B | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 91ef483b-97c2-3b3e-8176-87de18dd8b46 | -16.6429 | -55.5289 | 2024-10-06 00:46:47 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 7592f468-e904-3466-94aa-677383094e5d | -16.6453 | -55.541 | 2024-10-06 00:46:47 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| e44f8de5-b9ef-35c9-848a-1ed841d3b4c6 | -16.8624 | -56.6908 | 2024-10-06 00:46:47 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| c24b8877-e7dd-3714-9002-d99c83df7869 | -16.865101 | -56.705399 | 2024-10-06 00:46:47 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| e1c64841-dd3d-3908-9f59-5d20563b25f2 | -16.6262 | -55.494801 | 2024-10-06 00:46:48 | METOP-B | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 72e3c431-5722-3bd9-adf2-f8ef99f163a0 | -16.6285 | -55.506802 | 2024-10-06 00:46:48 | METOP-B | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 98cd461a-c7d7-30a0-9507-e86efb9e7043 | -16.6308 | -55.518902 | 2024-10-06 00:46:48 | METOP-B | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| fe845b04-aa47-32eb-8106-10deee0bef68 | -16.633101 | -55.530899 | 2024-10-06 00:46:48 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| d2cf1b47-2486-32a3-a1c4-e0c293d53e0e | -16.6355 | -55.542999 | 2024-10-06 00:46:48 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| e5a720d8-0cc7-3d27-bcde-eb28ea9a9fd1 | -16.7019 | -55.891102 | 2024-10-06 00:46:48 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 3ab967c5-e1e6-3f67-93d5-cf1db039c0e0 | -16.8526 | -56.692699 | 2024-10-06 00:46:48 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| ee913da5-ce98-3727-ba74-9977f54bc833 | -16.855301 | -56.707298 | 2024-10-06 00:46:48 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 54f91b4b-62ef-3f30-bac4-f148429d950a | -16.6826 | -55.842201 | 2024-10-06 00:46:48 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 70b6d4eb-168f-3ae5-a6aa-b2abc190c42c | -16.684999 | -55.8549 | 2024-10-06 00:46:48 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 3fd15a1f-6ac4-3ec6-82de-2a05e7645498 | -16.687401 | -55.867599 | 2024-10-06 00:46:48 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 56e0604a-e195-364e-b239-84533636ad52 | -16.6898 | -55.880299 | 2024-10-06 00:46:48 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| e0e8f09a-8f29-3f7a-a8a5-9d3036447d5b | -16.6922 | -55.893101 | 2024-10-06 00:46:48 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| c0752292-478b-3731-87fb-2e2b9b12ff1d | -16.6947 | -55.9058 | 2024-10-06 00:46:48 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| e847f02c-f851-3d77-9575-e8f98189ab5b | -16.6752 | -55.8568 | 2024-10-06 00:46:48 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 553b3998-565a-386d-941f-1ba69d567330 | -16.677601 | -55.869499 | 2024-10-06 00:46:48 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 35d673ed-c542-358f-b7eb-1675912bc145 | -16.68 | -55.882198 | 2024-10-06 00:46:48 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 3010c1bf-b83f-34c6-a2c8-09b82a52c2f2 | -16.6483 | -55.875401 | 2024-10-06 00:46:48 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 21f86a6a-cc1d-3e36-a686-6442edb5f76c | -16.6507 | -55.888199 | 2024-10-06 00:46:48 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 4b99678e-bfe6-36df-880b-1bfb8322adc7 | -16.6385 | -55.877399 | 2024-10-06 00:46:49 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| bb58a412-3d45-3d15-b6bf-b6c997c379f1 | -16.6409 | -55.890099 | 2024-10-06 00:46:49 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 4f0a7584-346e-3e73-a818-5506a7ed7fab | -16.628799 | -55.879299 | 2024-10-06 00:46:49 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| fc087f40-b266-3254-966d-5cc4cc47cfbf | -16.618999 | -55.881302 | 2024-10-06 00:46:49 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 47cc472e-8f88-33f9-b0ac-e78179e69f2e | -16.621401 | -55.894001 | 2024-10-06 00:46:49 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| ebf2c53b-92d8-3e07-a592-aa91e1034b72 | -16.6092 | -55.883202 | 2024-10-06 00:46:49 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 5ca153d8-f592-304d-96bb-9316e5b26d3e | -16.611601 | -55.896 | 2024-10-06 00:46:49 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 9e16cb73-38d0-3d40-a4c0-ed0b1df3a8a9 | -16.6141 | -55.908699 | 2024-10-06 00:46:49 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 7b76f410-68fd-3145-99b7-2c7c3366ac89 | -16.9203 | -57.6661 | 2024-10-06 00:46:49 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 93715e71-4da3-365a-88ed-f7479ccbd51c | -16.562799 | -55.9058 | 2024-10-06 00:46:50 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 331e6b6b-80c2-3e23-bd25-8b83593cc7e9 | -16.5653 | -55.918598 | 2024-10-06 00:46:50 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| cb274718-8d99-319f-8948-3e54c3aed7b4 | -16.5506 | -55.8951 | 2024-10-06 00:46:50 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 4f75e6ae-a333-3564-80a5-7a2783afc1f9 | -16.552999 | -55.907799 | 2024-10-06 00:46:50 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| ef4d7f36-2af4-3e1c-b031-68434cf8081d | -16.5555 | -55.920601 | 2024-10-06 00:46:50 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 1aeecab1-4b36-38fe-829a-8c672612a34f | -16.8332 | -57.409401 | 2024-10-06 00:46:50 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 719ce9e7-281f-3719-9fc5-39eacb4d6b53 | -16.836201 | -57.425598 | 2024-10-06 00:46:50 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 56d7dd5b-4eef-3e6d-bd1a-656d3d7e22a9 | -16.8235 | -57.411301 | 2024-10-06 00:46:50 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 65b4ae0a-82f0-33eb-990a-d9fe4b31e532 | -16.8265 | -57.427502 | 2024-10-06 00:46:50 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 4720d583-bf22-3744-9307-7a64b1a14dce | -16.8137 | -57.4132 | 2024-10-06 00:46:50 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 78a31c29-95e8-3ca3-8dd7-c810b5eff54f | -13.0234 | -40.497398 | 2024-10-06 00:46:50 | METOP-B | MARCIONÍLIO SOUZA | BAHIA | Brasil | 2920809 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 6500423d-ada3-3090-9b3b-6db695e36436 | -13.0293 | -40.519699 | 2024-10-06 00:46:50 | METOP-B | MARCIONÍLIO SOUZA | BAHIA | Brasil | 2920809 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| bda815b6-f94b-31ee-9796-72ecfd4e038a | -16.5604 | -55.893101 | 2024-10-06 00:46:50 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| f97f7488-344f-36d1-bf94-2da40edb9dee | -18.6586 | -57.2759 | 2024-10-06 00:46:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 82.8 |
| 9bc5eb17-f187-3b2f-874d-6edb13f4f547 | -16.7719 | -57.404499 | 2024-10-06 00:46:51 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 64a59e47-368e-38da-a14f-a336f98ddf62 | -16.774799 | -57.420601 | 2024-10-06 00:46:51 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 1c1b415c-e318-32a3-a571-0d39f04a8b68 | -16.7778 | -57.436798 | 2024-10-06 00:46:51 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 3096ff1d-8731-3a06-ae6f-1d5a587aa39f | -16.838301 | -57.7696 | 2024-10-06 00:46:51 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 0036b2e3-3670-3853-b14c-8091866d11a8 | -16.768 | -57.438702 | 2024-10-06 00:46:51 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 4fbd4078-9363-3391-8179-eb0ec442aba3 | -16.770901 | -57.454899 | 2024-10-06 00:46:51 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| b073cb70-0bf4-3905-be16-420410630097 | -16.773899 | -57.471199 | 2024-10-06 00:46:51 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 1bff2f9f-fc8f-3e21-ae8a-6b19730e8833 | -16.828501 | -57.7715 | 2024-10-06 00:46:51 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 6b4b12f7-cbe3-3008-9a8a-62161d0507ba | -16.8316 | -57.788601 | 2024-10-06 00:46:51 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 28ae6e17-f71c-377b-ba74-286371b656d0 | -16.758301 | -57.440601 | 2024-10-06 00:46:51 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| c5e9fa63-0b26-3851-931c-865c694c6eb6 | -16.7612 | -57.456799 | 2024-10-06 00:46:51 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| db0d16d2-378c-3279-a332-fcc293cf778b | -16.821899 | -57.790401 | 2024-10-06 00:46:51 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 1aa63f70-7536-315d-86e2-d5c39c7e55f5 | -16.812201 | -57.792301 | 2024-10-06 00:46:52 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 05532f8a-c46f-3088-9cad-e1320d64fdb9 | -16.802401 | -57.794102 | 2024-10-06 00:46:52 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 5fe284b2-421a-343f-ab09-a268d8fc085b | -16.8055 | -57.811298 | 2024-10-06 00:46:52 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| a8e636a2-75b9-31dd-92eb-2ec284b64f6b | -16.7066 | -57.433899 | 2024-10-06 00:46:52 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 30cac3f4-2f71-394a-88eb-aa8991f5985a | -16.693899 | -57.419601 | 2024-10-06 00:46:52 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 38ea7b13-cb41-3903-ab91-1940030bb123 | -16.696899 | -57.435699 | 2024-10-06 00:46:52 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| b5e5d71e-7676-3c60-8b08-3095214f3d83 | -16.6842 | -57.421501 | 2024-10-06 00:46:53 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 2500b7d3-84c0-3956-a8ac-37dfc69501bd | -16.619499 | -57.124699 | 2024-10-06 00:46:53 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 6446888b-f184-3918-9509-de5e244d28d4 | -16.622299 | -57.139999 | 2024-10-06 00:46:53 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 1d8d94c5-6b27-361a-8f60-8845456ba37c | -16.677401 | -57.439499 | 2024-10-06 00:46:53 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| d23ba5d6-42fc-3d02-9b7d-39719ea01d78 | -16.5805 | -57.132198 | 2024-10-06 00:46:53 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| f25a8d43-5c8a-314f-ad07-eb5d18642bf7 | -12.6952 | -40.194801 | 2024-10-06 00:46:54 | METOP-B | ITABERABA | BAHIA | Brasil | 2914703 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| f7716001-754d-3ad9-a9f5-c7ab53b1d239 | -14.075 | -45.572399 | 2024-10-06 00:46:54 | METOP-B | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 0fa6d9ed-5c22-32d1-8584-4e4fa2c5e90f | -16.5679 | -57.118801 | 2024-10-06 00:46:54 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| a36156ca-a00b-3bf8-b005-3e91c126af94 | -16.570801 | -57.134102 | 2024-10-06 00:46:54 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| c61e19a7-2e96-3e61-bc87-b53ea9df2250 | -16.566601 | -57.166801 | 2024-10-06 00:46:54 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| b6566a13-9a5f-3337-8aee-3a957ab77b39 | -16.5695 | -57.182201 | 2024-10-06 00:46:54 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| f6c16558-09ad-3f24-9dcb-96cebce89c34 | -16.5723 | -57.197701 | 2024-10-06 00:46:54 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| b42a7f39-493a-3da4-a539-10ecf9857f7f | -16.5569 | -57.168701 | 2024-10-06 00:46:54 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| ea97f4dc-4e06-3508-ac47-fd626ae4b1c4 | -16.559799 | -57.1842 | 2024-10-06 00:46:54 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| c9b9437d-8dc5-378b-9f6e-b1c7f88a73f7 | -16.562599 | -57.1996 | 2024-10-06 00:46:54 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| e93259d9-f237-33f8-90ec-279f38a24c42 | -16.547199 | -57.170601 | 2024-10-06 00:46:54 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 2acbbca1-9b3b-35c8-a838-6a6f79fee671 | -16.549999 | -57.1861 | 2024-10-06 00:46:54 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 182e095d-eb11-3703-afe8-e578fcd908b8 | -16.5529 | -57.2015 | 2024-10-06 00:46:54 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| b1043937-dbac-3bcf-b01e-96a5798f8b00 | -16.537399 | -57.172501 | 2024-10-06 00:46:54 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 3db87781-ae35-3aab-be97-5c4fc93ecb32 | -16.5403 | -57.187901 | 2024-10-06 00:46:54 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| e48828d6-c467-3e98-8cdf-9a459b1ff1d8 | -16.5431 | -57.2034 | 2024-10-06 00:46:54 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 96b2081c-1e9c-3a51-b267-1d6e52da4a23 | -16.546 | -57.218899 | 2024-10-06 00:46:54 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 2eb469dc-e71d-35a4-995c-31da12a5640b | -16.5305 | -57.1898 | 2024-10-06 00:46:54 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 8b4c1af6-eaf6-3065-b117-2d5bbf75bef4 | -16.5334 | -57.205299 | 2024-10-06 00:46:54 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| ad15fc89-e004-3f87-8e49-fab14bb67a65 | -16.536301 | -57.220798 | 2024-10-06 00:46:54 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 261dd4e3-d0e3-30a8-818a-3a1e1bf0dc97 | -14.1907 | -46.4412 | 2024-10-06 00:46:55 | METOP-B | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| cfa0d3cf-b869-3c0e-841f-4084f9f3dfcd | -14.1929 | -46.450199 | 2024-10-06 00:46:55 | METOP-B | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 93ba0c22-d92f-3ac1-a158-21589d533f0c | -16.511 | -57.1936 | 2024-10-06 00:46:55 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 5c70a60a-a493-3ec1-af78-70d6af52c5d7 | -16.513901 | -57.209099 | 2024-10-06 00:46:55 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 384a4523-875a-3a3e-bd45-1c9cc09199d8 | -16.5168 | -57.224602 | 2024-10-06 00:46:55 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 1c83aff0-28b4-31c9-b32b-cc21355aa973 | -16.501301 | -57.195499 | 2024-10-06 00:46:55 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 75300ee5-9e02-3c9a-afc3-d05ac80e4d04 | -16.5042 | -57.210999 | 2024-10-06 00:46:55 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| adc829ff-832f-3faa-84af-49e9b4c5e2df | -16.507099 | -57.226501 | 2024-10-06 00:46:55 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |


[Clique aqui para ver as próximas entradas](README10.md)
