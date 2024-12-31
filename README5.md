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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7003731a-7e14-3055-b899-914609c53923 | -8.08726 | -35.23432 | 2024-12-31 04:06:00 | NOAA-20 | VITÓRIA DE SANTO ANTÃO | PERNAMBUCO | Brasil | 2616407 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 48d0f89d-81cf-3744-8926-a266ed9400cd | -6.95296 | -43.00782 | 2024-12-31 04:06:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| cd33e5b9-f799-37f9-a400-d5def51c66eb | -5.95671 | -42.69886 | 2024-12-31 04:06:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 53351aa9-d7b8-362b-96e3-f4b5eea98f5b | -9.13894 | -38.436 | 2024-12-31 04:06:00 | NOAA-20 | GLÓRIA | BAHIA | Brasil | 2911402 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| cb0b1a88-83e5-3cbe-9388-252b115b13d2 | -9.86643 | -37.19836 | 2024-12-31 04:06:00 | NOAA-20 | BELO MONTE | ALAGOAS | Brasil | 2700904 | 27 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 1fa94c55-41c6-37b4-a2f7-35f96607152a | -7.91218 | -35.20966 | 2024-12-31 04:06:00 | NOAA-20 | PAUDALHO | PERNAMBUCO | Brasil | 2610608 | 26 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| adb7852d-e11d-3411-ad4e-a70b09cb4718 | -7.88611 | -45.95888 | 2024-12-31 04:06:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 85219cce-c3ca-3e80-bea6-813a1efb512d | -6.09213 | -42.67288 | 2024-12-31 04:06:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| c5bd08a2-bc5a-3193-a417-2908677bf2b6 | -6.09029 | -42.6728 | 2024-12-31 04:06:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| e8036771-9794-3d09-a39a-b4146f5823c1 | -8.1249 | -40.79166 | 2024-12-31 04:06:00 | NOAA-20 | BETÂNIA DO PIAUÍ | PIAUÍ | Brasil | 2201739 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 792a521c-2bb6-32f7-843f-a26b2ba07e43 | -7.90833 | -35.20442 | 2024-12-31 04:06:00 | NOAA-20 | PAUDALHO | PERNAMBUCO | Brasil | 2610608 | 26 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 2f7c05e2-4540-3807-b732-95e838019b2e | -6.27787 | -43.82317 | 2024-12-31 04:06:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6b7d7a6c-509b-3de8-9009-b0a0afa61483 | -6.59688 | -39.42197 | 2024-12-31 04:06:00 | NOAA-20 | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 57834bb1-9508-39ce-9cf5-987324b5a744 | -17.77972 | -42.81017 | 2024-12-31 04:08:00 | NOAA-20 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 69963882-5862-3fda-a497-2c27765bc159 | -13.61027 | -40.97442 | 2024-12-31 04:08:00 | NOAA-20 | BARRA DA ESTIVA | BAHIA | Brasil | 2902807 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| bcf53913-b9d0-3da7-8c90-483e4d73fd7e | -22.11698 | -51.46699 | 2024-12-31 04:10:00 | NOAA-20 | PRESIDENTE PRUDENTE | SÃO PAULO | Brasil | 3541406 | 35 | 33 | nan | nan | nan | Mata Atlântica | 34.1 |
| 91cfb49d-a380-31fa-8f2b-0439ff5e39c7 | -22.1212 | -51.46796 | 2024-12-31 04:10:00 | NOAA-20 | PRESIDENTE PRUDENTE | SÃO PAULO | Brasil | 3541406 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.5 |
| f0cffd22-a50a-3a82-8d63-0e4c19981dd3 | -20.41838 | -43.55424 | 2024-12-31 04:10:00 | NOAA-20 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| f5e7cf8f-7974-3a9c-b994-34a67b35562e | -17.73909 | -56.32293 | 2024-12-31 04:10:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| cf40e07a-8a2c-3557-ad7d-156062e8e63f | -20.49929 | -55.8094 | 2024-12-31 04:10:00 | NOAA-20 | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 545c30ad-dd4a-3fd7-bd27-1d69200cd0db | -23.9834 | -48.91893 | 2024-12-31 04:10:00 | NOAA-20 | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b5abd4fd-d067-38df-a2af-284bd82b2269 | -23.04726 | -49.89627 | 2024-12-31 04:10:00 | NOAA-20 | OURINHOS | SÃO PAULO | Brasil | 3534708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 7e6318b3-92a9-3048-a8a4-090b19b3d519 | -22.54694 | -48.37834 | 2024-12-31 04:10:00 | NOAA-20 | MINEIROS DO TIETÊ | SÃO PAULO | Brasil | 3529807 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| becb6955-cb84-3ccc-8d6c-b5aefe1effbe | -18.78528 | -52.7206 | 2024-12-31 04:10:00 | NOAA-20 | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4ab58211-404c-3cff-9876-c897757bdbff | -22.54871 | -48.37678 | 2024-12-31 04:10:00 | NOAA-20 | MINEIROS DO TIETÊ | SÃO PAULO | Brasil | 3529807 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 0355bcbe-4eba-3b21-843c-836c02f61ee2 | -23.04518 | -49.89334 | 2024-12-31 04:10:00 | NOAA-20 | OURINHOS | SÃO PAULO | Brasil | 3534708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 6c09273d-cc19-3aa2-b32b-1118904d2912 | -25.56731 | -49.3674 | 2024-12-31 04:10:00 | NOAA-20 | ARAUCÁRIA | PARANÁ | Brasil | 4101804 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 17227be7-b210-329e-8227-b4c8fd51b328 | -25.33027 | -52.74821 | 2024-12-31 04:10:00 | NOAA-20 | ESPIGÃO ALTO DO IGUAÇU | PARANÁ | Brasil | 4107546 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 28ec8d39-1227-3c81-8a07-de9b2ec7e4ae | -22.54516 | -48.37601 | 2024-12-31 04:10:00 | NOAA-20 | MINEIROS DO TIETÊ | SÃO PAULO | Brasil | 3529807 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a08ba968-d6a0-358c-80ac-cc73504964ef | -22.67418 | -42.85643 | 2024-12-31 04:10:00 | NOAA-20 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 44aed599-be94-3db7-abf4-f1bb14c8a409 | -22.53973 | -48.81305 | 2024-12-31 04:10:00 | NOAA-20 | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6c94fa2b-910f-3997-b68c-1b44bb47723a | -23.9816 | -48.91652 | 2024-12-31 04:10:00 | NOAA-20 | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9bf2cae9-c5d0-3c37-a167-2cef9fbc3fc8 | -23.33723 | -46.77253 | 2024-12-31 04:10:00 | NOAA-20 | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 82d70edc-26a8-3348-9d02-b05960c1aefa | -20.49856 | -55.80749 | 2024-12-31 04:10:00 | NOAA-20 | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 3.5 |
| bc20ab24-21cd-3dae-9293-b04d52c3cbac | -19.12287 | -54.4395 | 2024-12-31 04:10:00 | NOAA-20 | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a9807fb7-9139-3f55-bdcd-f9fa8b00ee7f | -21.31301 | -49.02834 | 2024-12-31 04:10:00 | NOAA-20 | ITAJOBI | SÃO PAULO | Brasil | 3521903 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| a5874bc3-e1dd-3557-8258-8e3c15dbf294 | -20.41502 | -43.5537 | 2024-12-31 04:10:00 | NOAA-20 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 44df0dc9-842e-329d-9020-c73c384e89c1 | -23.7052 | -46.4778 | 2024-12-31 04:10:00 | NOAA-20 | MAUÁ | SÃO PAULO | Brasil | 3529401 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| e4500c81-fe18-3561-9166-e88e341134c1 | -19.82952 | -57.47703 | 2024-12-31 04:10:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| e4c81790-9403-3894-acc8-0b1db85601f5 | -22.11783 | -51.46272 | 2024-12-31 04:10:00 | NOAA-20 | PRESIDENTE PRUDENTE | SÃO PAULO | Brasil | 3541406 | 35 | 33 | nan | nan | nan | Mata Atlântica | 34.1 |
| fd7c1cea-2b8d-3521-8ce8-10b7c972080f | -17.74526 | -56.32446 | 2024-12-31 04:10:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 5d6fa5bb-5519-3fc1-9251-2fdeda920d09 | -25.33202 | -52.74699 | 2024-12-31 04:10:00 | NOAA-20 | ESPIGÃO ALTO DO IGUAÇU | PARANÁ | Brasil | 4107546 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| a532796e-0308-3114-b186-ea4ef0a9061d | -22.5444 | -48.38039 | 2024-12-31 04:10:00 | NOAA-20 | MINEIROS DO TIETÊ | SÃO PAULO | Brasil | 3529807 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ade25b50-0156-312a-9558-da0e6417d227 | -23.59465 | -47.43882 | 2024-12-31 04:10:00 | NOAA-20 | VOTORANTIM | SÃO PAULO | Brasil | 3557006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 9b39f475-f3e2-370a-9594-4aee34af2310 | -23.98517 | -48.91726 | 2024-12-31 04:10:00 | NOAA-20 | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c5823aab-64ee-3780-854e-b9c4ade2c52a | -19.83582 | -57.47873 | 2024-12-31 04:10:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 7b6a0f42-3050-312f-8a36-c5b7a39932bb | -22.47879 | -46.01373 | 2024-12-31 04:10:00 | NOAA-20 | ESTIVA | MINAS GERAIS | Brasil | 3124500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| ee794ca5-906a-39b7-937b-2c5bc131d665 | -30.50336 | -54.00718 | 2024-12-31 04:12:00 | NOAA-20 | SANTA MARGARIDA DO SUL | RIO GRANDE DO SUL | Brasil | 4316972 | 43 | 33 | nan | nan | nan | Pampa | 1.0 |
| f478c223-cd02-34c3-85b2-cc8ce936a349 | -30.53914 | -53.50399 | 2024-12-31 04:12:00 | NOAA-20 | CAÇAPAVA DO SUL | RIO GRANDE DO SUL | Brasil | 4302808 | 43 | 33 | nan | nan | nan | Pampa | 0.4 |
| 8f6dd763-2052-3fc3-a475-01d8c55decd0 | 3.47381 | -60.4649 | 2024-12-31 04:55:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 325c088a-03f0-3106-99d0-af7dc45b3e12 | 3.18249 | -60.36895 | 2024-12-31 04:55:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b08bacce-78fe-326a-81ae-4e7d422fd293 | 3.47229 | -60.46068 | 2024-12-31 04:55:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ada91d56-269d-3cf7-8341-572e5e185987 | 3.18749 | -60.36822 | 2024-12-31 04:55:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 26b4eb55-4391-3b09-8dcd-b3b291926437 | 3.57093 | -60.18625 | 2024-12-31 04:55:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b35d4631-8f64-355b-81d3-0c82402fe7ed | 3.47187 | -60.45774 | 2024-12-31 04:55:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 43058e4f-106a-3576-9236-389a955d4279 | 3.62398 | -60.40915 | 2024-12-31 04:55:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9bddc73e-009a-372e-acae-11cd3a884c27 | 3.47293 | -60.45904 | 2024-12-31 04:55:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ac4bbf77-43bd-3317-a465-c3675b8f36cd | 3.5711 | -60.22235 | 2024-12-31 04:55:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9ab72189-6195-3144-9a4c-3d7ada692207 | 3.18707 | -60.36536 | 2024-12-31 04:55:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2cc7af21-1fd6-3fc2-8ac4-20376a833ea2 | 3.47337 | -60.46197 | 2024-12-31 04:55:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a9ec9449-a328-3284-b1c3-6e0c0c9995ef | 3.47819 | -60.46581 | 2024-12-31 04:55:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7382fc3a-c657-3a4f-8006-7981f869093f | 3.47271 | -60.46362 | 2024-12-31 04:55:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6be5c0fa-bcbc-367b-bc36-9ba26ccbacac | -0.87243 | -51.47372 | 2024-12-31 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8f33f85f-f05b-30c9-ae5e-1a9007cbfe3f | -1.5715 | -46.04535 | 2024-12-31 04:57:00 | NOAA-21 | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| bbe328c7-e027-314a-adec-e02b5901e3d1 | -2.80564 | -41.77526 | 2024-12-31 04:57:00 | NOAA-21 | ILHA GRANDE | PIAUÍ | Brasil | 2204659 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8699eb06-82fe-37be-810f-fc905c32c9c9 | -2.43341 | -53.63818 | 2024-12-31 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 06f9e7ff-9f93-33ad-ad2a-e86959644de9 | -2.79932 | -41.77427 | 2024-12-31 04:57:00 | NOAA-21 | ILHA GRANDE | PIAUÍ | Brasil | 2204659 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a9dc0116-fbd2-3fa5-b724-f5e541ea9af7 | -3.18109 | -53.75239 | 2024-12-31 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 2ac57637-e185-3239-b043-496c225ce630 | -1.85957 | -45.58536 | 2024-12-31 04:57:00 | NOAA-21 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 469206f0-b02d-370a-9c75-6ec7dd73a3b3 | -0.79372 | -48.10003 | 2024-12-31 04:57:00 | NOAA-21 | VIGIA | PARÁ | Brasil | 1508209 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 42d18456-ee3d-329a-b6e2-58f4ac76a2fa | -2.49265 | -45.4489 | 2024-12-31 04:57:00 | NOAA-21 | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 87a2c574-9019-37b0-8ee8-65ad2f31d8ee | -3.55297 | -43.56213 | 2024-12-31 04:57:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a41ad1eb-0598-3650-b2a9-f99bbe4ac76a | -3.16976 | -53.28323 | 2024-12-31 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 483f55df-fa95-363c-8846-fdff2cf23a90 | -1.65032 | -45.85947 | 2024-12-31 04:57:00 | NOAA-21 | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b8057216-8052-3ce7-9d56-81e54941b521 | -5.72545 | -43.24084 | 2024-12-31 04:57:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7303921d-c39e-33cd-b2b4-bc1d742e3932 | -1.64559 | -45.85871 | 2024-12-31 04:57:00 | NOAA-21 | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 55c7759a-79b3-316a-9e2c-c3c8ef537511 | -3.11106 | -53.32992 | 2024-12-31 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 917130db-f5eb-3c57-8da5-a266f68c5d8a | -3.53242 | -51.03005 | 2024-12-31 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c79f35cf-ae9f-32c4-abcb-ea6e103014cc | -1.65429 | -45.86531 | 2024-12-31 04:57:00 | NOAA-21 | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 982f90d6-51c6-3409-958d-dafb59a9a0d8 | -3.76249 | -43.95552 | 2024-12-31 04:57:00 | NOAA-21 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0575fdd2-3b2b-3bff-9978-495c515b9c00 | -3.55619 | -43.56547 | 2024-12-31 04:57:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2819a916-82a5-38bc-9546-d5cf4888b0b9 | -3.14019 | -53.05589 | 2024-12-31 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 30c549c6-9fe6-3a27-a1e3-1248f3f5a33d | -5.72607 | -43.23625 | 2024-12-31 04:57:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d8046e41-3e15-3b03-870a-8753007a84d2 | -3.1703 | -53.27979 | 2024-12-31 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ee930a27-c95f-3f95-9a4a-cbeff0c5ce13 | -2.71666 | -45.57179 | 2024-12-31 04:57:00 | NOAA-21 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ea5a4ed0-6e19-3bb4-969f-9e48193474f7 | -3.50789 | -50.05207 | 2024-12-31 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5edbedc7-4b4f-3d2a-921e-c1352c2ebc00 | -1.65506 | -45.86023 | 2024-12-31 04:57:00 | NOAA-21 | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 8.5 |
| b53f6c48-fda3-3574-ad17-56e54318ded1 | -3.22082 | -48.76234 | 2024-12-31 04:57:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 462cac7e-d906-3202-a8d4-6b42eb10ca00 | -3.55679 | -43.5615 | 2024-12-31 04:57:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0e699340-a6b2-3975-9479-75a12002e100 | -1.25119 | -46.60686 | 2024-12-31 04:57:00 | NOAA-21 | AUGUSTO CORRÊA | PARÁ | Brasil | 1500909 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| ea9b32ba-3cf5-342a-be24-ffe1a22e1c46 | -3.09069 | -53.72028 | 2024-12-31 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 92f9b164-6635-3ba2-b66d-3b7de0e14330 | -3.76806 | -43.95643 | 2024-12-31 04:57:00 | NOAA-21 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 52010d21-9416-3aa1-adff-ac3ed1c466e3 | -2.78871 | -54.04299 | 2024-12-31 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 3c53df62-4b9c-3af3-b45d-1ac4e49fbfbf | -1.25339 | -46.60532 | 2024-12-31 04:57:00 | NOAA-21 | AUGUSTO CORRÊA | PARÁ | Brasil | 1500909 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 8463eb55-36b8-3998-8478-e2d9022704ec | -3.76195 | -43.95921 | 2024-12-31 04:57:00 | NOAA-21 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6adcf4ab-c617-30ce-bd1c-29537953a556 | -1.57456 | -46.04227 | 2024-12-31 04:57:00 | NOAA-21 | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 55574217-0fb9-3525-81e4-3f1af7a56ed0 | -1.57227 | -46.04044 | 2024-12-31 04:57:00 | NOAA-21 | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fdfda2f9-8aa6-3fb4-8b90-4dbde5edf70a | -1.64955 | -45.86454 | 2024-12-31 04:57:00 | NOAA-21 | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6d9da5ad-323b-3a13-9f74-8b8baa6816b8 | -10.70676 | -59.23302 | 2024-12-31 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e614cdc6-57a7-3f88-957f-3cecd622d8d2 | -10.70388 | -59.23512 | 2024-12-31 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README6.md)
