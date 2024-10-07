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

## Dados Diários - Página 114

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fe6c9b67-5143-3c8e-b77b-989680977646 | -17.18303 | -53.92803 | 2024-10-07 05:18:00 | NPP-375D | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a1cb624c-041e-380f-82db-61e72e24838f | -17.16902 | -53.9258 | 2024-10-07 05:18:00 | NPP-375D | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2883a02a-0579-37eb-9bd0-a2f74333ef58 | -17.02723 | -55.0775 | 2024-10-07 05:18:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 81cf8303-241e-39f3-b5ee-027f5953f9d9 | -17.0175 | -55.0848 | 2024-10-07 05:18:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| eadb71b3-e713-3d9c-809f-36ab8db8d155 | -17.01697 | -55.08905 | 2024-10-07 05:18:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5f5d86d0-f4ee-30e0-ac47-ed5c1deb9999 | -17.01637 | -55.0587 | 2024-10-07 05:18:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cc8c8ddb-c382-3459-b830-8a79180abcba | -16.88728 | -54.52423 | 2024-10-07 05:18:00 | NPP-375D | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5ab330bd-3932-3085-bd40-48489dedd491 | -17.21737 | -55.12532 | 2024-10-07 05:18:00 | NPP-375D | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| defaef46-4e9a-3cc6-b59f-d0eaf78dace9 | -17.17429 | -53.92154 | 2024-10-07 05:18:00 | NPP-375D | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2dd8142d-d67e-36cd-b376-62378694f77f | -17.16254 | -53.94014 | 2024-10-07 05:18:00 | NPP-375D | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2434e90f-d313-32d7-82c0-6b53044531bf | -17.02884 | -55.06475 | 2024-10-07 05:18:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 3fa87668-3181-323c-bc00-804de6d01030 | -17.0283 | -55.06899 | 2024-10-07 05:18:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 10.0 |
| f0f80fa3-5c59-39a1-b19d-4edbfa46c38e | -17.0245 | -55.06415 | 2024-10-07 05:18:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 485968d4-fcf5-3bec-853a-4623532cf2bb | -17.01309 | -55.04958 | 2024-10-07 05:18:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 78a03380-bc20-36a9-86b2-f1babb394729 | -17.00706 | -55.02705 | 2024-10-07 05:18:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 423dfc59-4db6-3c34-a355-e06b9ca7133a | -16.90173 | -54.55442 | 2024-10-07 05:18:00 | NPP-375D | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2515f3d7-feb2-31b4-b58b-b4fe80d31dc7 | -16.89962 | -54.53492 | 2024-10-07 05:18:00 | NPP-375D | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 36c09640-1c6b-35af-8ccd-fa06d8846bf6 | -16.63957 | -55.56306 | 2024-10-07 05:18:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| e08b3c81-7299-3000-8407-06abfad70626 | -16.63489 | -55.56639 | 2024-10-07 05:18:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 1c93e5da-817f-35b2-821f-987360800e1b | -16.6312 | -55.56204 | 2024-10-07 05:18:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 3c592346-12e6-37d8-ae78-d7688a9c8380 | -16.62972 | -55.57357 | 2024-10-07 05:18:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| aab233c0-fcba-367e-9ae6-38eab7d03a69 | -16.62653 | -55.56538 | 2024-10-07 05:18:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 485ea9d7-fea1-31bc-a3b3-2f35eefbcd61 | -16.62603 | -55.56928 | 2024-10-07 05:18:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 8b3dc944-5e73-3f6a-87bb-6fd87241f003 | -16.62554 | -55.57309 | 2024-10-07 05:18:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 247f1bc0-661b-3453-b3f4-471618e4e1d3 | -16.62506 | -55.57683 | 2024-10-07 05:18:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 8e29bd2e-286a-368a-8186-32dd3effb509 | -16.62325 | -55.52455 | 2024-10-07 05:18:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 54a5ca5b-aec7-3a6b-9825-4da7ad326a18 | -16.62235 | -55.56483 | 2024-10-07 05:18:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 0abde2dd-c936-391b-bfc3-9c051d965e90 | -16.62185 | -55.56878 | 2024-10-07 05:18:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 62e52c1b-6370-3cc2-8471-2ee662a721aa | -16.62135 | -55.57261 | 2024-10-07 05:18:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 59c0a1cd-c159-32ce-bf8b-ddecf0995596 | -16.62039 | -55.58007 | 2024-10-07 05:18:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 0702d2b1-2000-336f-9df2-6df0ce8ca6cf | -16.61769 | -55.56807 | 2024-10-07 05:18:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| a67beeeb-2232-3b86-aceb-62dc6a4e33b0 | -16.61719 | -55.57195 | 2024-10-07 05:18:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 4b2adabd-6ad7-3ca2-baa0-7240108b1ae3 | -16.61622 | -55.5795 | 2024-10-07 05:18:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| d4e248a1-0b70-30f2-afc3-86f809949035 | -16.61255 | -55.57506 | 2024-10-07 05:18:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 77e37e3f-216f-33af-b091-766ddb08f478 | -16.61206 | -55.57891 | 2024-10-07 05:18:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| c8bb0aef-7ae3-3b9f-b935-0ef83d90c6df | -16.60789 | -55.57828 | 2024-10-07 05:18:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 7384754e-f7bb-3fa7-b1d5-8017d31556e2 | -16.6076 | -55.21744 | 2024-10-07 05:18:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 55d547e3-9744-31fd-a371-2f5ec62dcb61 | -15.89756 | -55.40683 | 2024-10-07 05:18:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1a6e6f45-3593-383f-88b2-c22d51c6d549 | -16.58267 | -56.06192 | 2024-10-07 05:18:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 8aee8801-0334-37fc-a419-e1017488674f | -16.57911 | -56.05769 | 2024-10-07 05:18:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| ae2d0e9c-96f9-35d2-ae84-195dfe39b508 | -16.57863 | -56.06134 | 2024-10-07 05:18:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| e665951d-0ea0-33fe-87e9-99fa09e348f2 | -16.56491 | -55.91321 | 2024-10-07 05:18:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 7.3 |
| 76895a19-4ed0-31ce-a1d7-4e2586543dfb | -16.56443 | -55.91692 | 2024-10-07 05:18:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 7.3 |
| 1d492409-2331-3879-a67d-14e5c3262d02 | -16.55676 | -55.91204 | 2024-10-07 05:18:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| b076962b-a9d4-37d2-9e35-e817709f1c79 | -16.55628 | -55.91576 | 2024-10-07 05:18:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| e241b222-ec0a-354a-8eb2-a533481f1060 | -16.41603 | -55.9502 | 2024-10-07 05:18:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 77f198cb-f644-3bbb-8204-5cd3cfb31ee0 | -16.35846 | -55.97934 | 2024-10-07 05:18:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| e1c1a508-a4df-3be2-b806-2eb778614515 | -16.20314 | -55.99844 | 2024-10-07 05:18:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 8c0f637a-d15b-3de9-92c4-a23749714c32 | -16.15477 | -55.92889 | 2024-10-07 05:18:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 0df8d440-664d-35f8-bcb8-21dc306fc606 | -16.15073 | -55.92822 | 2024-10-07 05:18:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| ad33396f-d9dd-3a28-8397-e6dcd853bbac | -16.14219 | -55.86704 | 2024-10-07 05:18:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 5eb498e7-ce5f-3e00-af78-2294b498c3a2 | -16.13812 | -55.86653 | 2024-10-07 05:18:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 7f528ac0-903f-30df-aff0-9bad98891379 | -16.64376 | -55.56353 | 2024-10-07 05:18:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 838c463e-7e22-31ac-bb1a-bfefa588ab34 | -16.63708 | -55.58233 | 2024-10-07 05:18:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| f9217821-a0d8-3fc3-b9d3-04f83c4a867e | -16.63539 | -55.56256 | 2024-10-07 05:18:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 26fc0847-637f-343b-af07-32a780818334 | -16.6344 | -55.57022 | 2024-10-07 05:18:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 4a81ab92-292f-3219-9ca2-cb9aa882c8b0 | -16.63391 | -55.57405 | 2024-10-07 05:18:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 916ed399-a3ab-3fd1-980c-53cd40d9c0c2 | -16.63071 | -55.5659 | 2024-10-07 05:18:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 2cbcd395-ba7b-325e-b2eb-fba1dca6b198 | -16.63021 | -55.56975 | 2024-10-07 05:18:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 76f8b147-b7c9-30bc-b138-6e7d63c4ed75 | -16.62703 | -55.56145 | 2024-10-07 05:18:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 1218ecd5-6857-307a-9ea3-1fa0b3b25c46 | -16.62441 | -55.54875 | 2024-10-07 05:18:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 9cbcfc56-7cfb-3881-919d-b32e4219ad15 | -16.62286 | -55.56083 | 2024-10-07 05:18:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 164709be-fedf-3f54-bdd9-506f92410ea4 | -16.62088 | -55.57633 | 2024-10-07 05:18:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 887b4081-bc78-31d7-a69b-01a5039010eb | -16.62024 | -55.54811 | 2024-10-07 05:18:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 576b5ef9-8bb6-384d-ae89-b36054bb2096 | -16.61907 | -55.52395 | 2024-10-07 05:18:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 247ffde7-5eab-34e6-98e2-a97e240999d0 | -16.61856 | -55.52789 | 2024-10-07 05:18:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 0abfd64b-78cf-33bb-b77b-97e0282ae7c0 | -16.61819 | -55.56413 | 2024-10-07 05:18:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 3a7583c6-4ca6-3afb-b62e-44dc7b13f575 | -16.61671 | -55.57571 | 2024-10-07 05:18:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 66e77303-8591-30d7-ad47-1cb97de5b670 | -16.61573 | -55.58335 | 2024-10-07 05:18:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 2ce742cd-2caf-3c53-bce3-d0606797a654 | -16.61556 | -55.55144 | 2024-10-07 05:18:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 8ad66796-7ac7-3b3e-af5c-b6c328cd7b90 | -16.61354 | -55.5673 | 2024-10-07 05:18:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| c9de2e7f-ec56-31ac-8783-0c9610ea1287 | -16.61304 | -55.57121 | 2024-10-07 05:18:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 915af343-1216-3157-95ff-5e929419ac7f | -16.61186 | -55.21803 | 2024-10-07 05:18:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 5bdbcece-564a-3ba3-86c7-06626d4ef704 | -16.61156 | -55.58276 | 2024-10-07 05:18:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 08b951b5-bd34-3dbd-9409-b77ec89fe067 | -16.6074 | -55.58215 | 2024-10-07 05:18:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 78069f23-507f-30ba-b28b-190890a06b7a | -16.60386 | -55.21275 | 2024-10-07 05:18:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 9bb52225-6dc8-3928-91fc-b1f94cfed9b3 | -16.58316 | -55.90065 | 2024-10-07 05:18:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| f1addb47-7cc5-34bb-871a-55e2604d1a3b | -16.58267 | -55.90438 | 2024-10-07 05:18:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| cf5acc02-9d6f-3027-8933-48c594f76e76 | -16.57814 | -56.06498 | 2024-10-07 05:18:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 40162e5f-f62b-31c0-b687-1038287c169f | -16.57766 | -56.06862 | 2024-10-07 05:18:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 7b1f1cad-838c-30d6-9f3e-3f4ffea2562f | -16.55173 | -55.91888 | 2024-10-07 05:18:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| b977c035-8aaa-3338-b082-9a36ac440795 | -16.15526 | -55.92514 | 2024-10-07 05:18:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 51794c09-1812-3635-93eb-3f50e71b2d8a | -17.15352 | -56.14438 | 2024-10-07 05:18:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| f9970185-eaa4-3d9a-b421-e82477d4c521 | -17.14898 | -56.14747 | 2024-10-07 05:18:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 4b37938b-8a67-366b-a85a-6620ae1f7645 | -17.14396 | -56.1542 | 2024-10-07 05:18:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 1e2e0717-c453-3373-9dbe-659c882215ae | -17.06514 | -56.67816 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| d05e6def-5285-3f5d-906f-2dc336e21388 | -17.05017 | -56.05152 | 2024-10-07 05:18:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| e49bb5e6-8270-3695-9eb7-ccedda15f8a7 | -17.02922 | -56.67816 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 28.6 |
| f7730c0b-5957-387d-ab95-fc729a7efb31 | -17.02072 | -56.68213 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 14.8 |
| 8a957cfd-3e5b-39f6-8713-db2b4c2b6271 | -17.01289 | -56.681 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 40.9 |
| 18d4d9bf-d63e-3354-8d63-43066f321283 | -17.00898 | -56.68042 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 19.1 |
| 5e127901-9c0c-3a70-b26a-9303feab26a6 | -16.9959 | -56.68892 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 4f09833d-9b36-3006-b965-cddab7b2a217 | -16.9326 | -56.62602 | 2024-10-07 05:18:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.6 |
| 84d45479-3152-3d93-8b30-a1d0c9b7aa36 | -16.92628 | -55.83255 | 2024-10-07 05:18:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 6be045cb-5594-3c1f-9fb9-28b4333a9e48 | -17.15303 | -56.14804 | 2024-10-07 05:18:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 62d14cba-ee1e-38c7-a57f-ea1d8c072049 | -17.15058 | -56.16633 | 2024-10-07 05:18:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 121b31e1-ab8e-3c6e-9440-423a4753181b | -17.14948 | -56.1438 | 2024-10-07 05:18:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 1f70e391-4fb6-30bc-886c-8386bcde08f9 | -17.148 | -56.15479 | 2024-10-07 05:18:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 4c4435b0-0986-30e6-95ba-c80a40399481 | -17.14751 | -56.15844 | 2024-10-07 05:18:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| cb517c1c-8b56-341d-9f3f-3b882dcb4562 | -17.14702 | -56.16209 | 2024-10-07 05:18:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |


[Clique aqui para ver as próximas entradas](README115.md)
