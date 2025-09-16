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

## Dados Diários - Página 79

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 95d0be5c-8959-3119-abe0-94767bd85457 | -16.69792 | -54.96091 | 2025-09-16 04:53:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4c7e5713-b968-342f-958a-9cbe5b37576a | -16.6911 | -46.94398 | 2025-09-16 04:53:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| afa02ac4-792b-39c1-9e2c-67ff5608c759 | -16.69383 | -49.78165 | 2025-09-16 04:53:00 | NOAA-20 | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2315bf32-f66a-3ff4-9790-168b476c2676 | -16.01257 | -59.27069 | 2025-09-16 04:53:00 | NOAA-20 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d9999ee8-9205-33ca-b1a1-919ef64f6bb6 | -15.83916 | -53.47298 | 2025-09-16 04:53:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 31cca94e-cc55-3be3-abbb-4a5aa86de63b | -15.7719 | -53.4621 | 2025-09-16 04:53:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 004ac9ce-a4e0-38b4-8cc1-97266d46ca6d | -15.86242 | -59.38338 | 2025-09-16 04:53:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6ad23624-d981-3e44-924c-2f376a840473 | -16.4847 | -55.10527 | 2025-09-16 04:53:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 15.8 |
| 8801f2e7-933e-3af6-8718-e96d366a6a5b | -16.48081 | -55.1083 | 2025-09-16 04:53:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 775057a6-7922-3f1b-ac30-5ecfe96aa5f3 | -15.81617 | -53.46552 | 2025-09-16 04:53:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bc471bf5-baba-3ef9-9e88-20d4a65b8091 | -17.30468 | -40.68705 | 2025-09-16 04:53:00 | NOAA-20 | UMBURATIBA | MINAS GERAIS | Brasil | 3170305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| ab099c52-2c9e-32f3-972f-1a9f679fd3cd | -15.79109 | -52.17751 | 2025-09-16 04:53:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f399b96d-474b-3514-b72c-d888fa532b55 | -16.48744 | -55.10943 | 2025-09-16 04:53:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| c271ac1b-bcae-3ee3-bdcb-a4fe8340539f | -15.8027 | -53.48618 | 2025-09-16 04:53:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 921e9e1c-8a71-30ee-b34a-ef240aae6594 | -16.06778 | -59.43038 | 2025-09-16 04:53:00 | NOAA-20 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 977f78b8-5136-39e7-b6e0-ddca682c809d | -15.83243 | -53.47191 | 2025-09-16 04:53:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 39844613-c469-34c6-8f79-07c99244d50b | -15.97627 | -47.69693 | 2025-09-16 04:53:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 32a61024-a80e-3940-a671-820ce518474d | -16.47636 | -55.11491 | 2025-09-16 04:53:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 101871cd-c954-35c4-8cfc-5d9128555e7c | -16.70947 | -54.97394 | 2025-09-16 04:53:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| dc8d8f76-436b-31da-8cfe-a244a9ba978f | -15.99506 | -59.41173 | 2025-09-16 04:53:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 3642f83e-cdcd-3545-b661-307d4d406ce0 | -18.01167 | -43.93757 | 2025-09-16 04:53:00 | NOAA-20 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8dfd209a-e9db-3a08-ad23-f6af6ca9b1b1 | -16.69337 | -49.78511 | 2025-09-16 04:53:00 | NOAA-20 | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 09e872b0-9411-3bea-910f-044910c0e89d | -16.00105 | -59.42292 | 2025-09-16 04:53:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ecb378a0-fddf-348c-b603-18ffbcd80c5f | -17.86519 | -44.44809 | 2025-09-16 04:53:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| e56cfe79-b0f6-369f-8166-533276f07e5d | -18.01219 | -43.93247 | 2025-09-16 04:53:00 | NOAA-20 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 67c37412-62ff-37b2-829f-bf31f98653f5 | -16.01694 | -59.24647 | 2025-09-16 04:53:00 | NOAA-20 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 92504118-c09c-3bf5-849b-f7d6a8b6aaf4 | -15.80607 | -53.48671 | 2025-09-16 04:53:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8602a1b5-efab-3392-936f-03bbf75907d5 | -15.787 | -53.45335 | 2025-09-16 04:53:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d1025c42-938f-3b0c-bebc-1137bce04e52 | -15.26681 | -56.03881 | 2025-09-16 04:53:00 | NOAA-20 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 186ad753-fddc-381a-a394-f57bc3588c4f | -15.78196 | -53.44106 | 2025-09-16 04:53:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3ed1e00e-2c53-33cd-9370-c0b82f86ebe2 | -15.80887 | -53.49091 | 2025-09-16 04:53:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d53db4e2-6d5e-34b4-8b8c-755cbc1794cb | -17.08032 | -45.83016 | 2025-09-16 04:53:00 | NOAA-20 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 1d3db0da-9c0c-3d2d-9c13-976bd044df71 | -15.80046 | -53.47823 | 2025-09-16 04:53:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4de33248-1ff8-33a2-a35e-a89a2d865bc9 | -15.79634 | -52.19069 | 2025-09-16 04:53:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c6916ac1-5253-3780-8f20-60ee508b27dc | -16.52922 | -43.73758 | 2025-09-16 04:53:00 | NOAA-20 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0be053a5-2d55-37e8-aca7-e2f8ac53a9b4 | -15.77412 | -53.44734 | 2025-09-16 04:53:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 149c4396-5511-3059-89f4-ccccd441e44d | -15.91926 | -56.27285 | 2025-09-16 04:53:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| c343fa11-3171-33d2-8757-ea353b71e1fe | -15.81281 | -53.46499 | 2025-09-16 04:53:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f5c21f54-4931-3afd-b8e1-221f39ace1a5 | -15.78297 | -52.2086 | 2025-09-16 04:53:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2c7cb781-8c70-3f21-b7c0-d7559be3a4b2 | -16.02077 | -59.2472 | 2025-09-16 04:53:00 | NOAA-20 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| a65e1c08-fee4-3509-bad5-64ec66f43734 | -16.47523 | -55.12208 | 2025-09-16 04:53:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 0224c930-2a28-399f-8b6b-27690b3ad52c | -15.81674 | -53.4618 | 2025-09-16 04:53:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3904655c-c347-3574-81a4-e32e6468366b | -16.52415 | -43.72811 | 2025-09-16 04:53:00 | NOAA-20 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f119a157-7512-302a-ae86-c074cfac4320 | -15.9717 | -47.69619 | 2025-09-16 04:53:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 03c75a03-f5f5-347c-9f41-a011eecb19c3 | -16.01652 | -59.42599 | 2025-09-16 04:53:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3f5004e0-0b98-3b7a-b185-6cfd7b18f2d6 | -16.0619 | -59.41832 | 2025-09-16 04:53:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2754ddf5-0c78-340c-ba86-ab4a86c42795 | -15.01451 | -55.33682 | 2025-09-16 04:53:00 | NOAA-20 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 84305981-0db3-31b8-b711-e89faa9df150 | -16.06534 | -59.42691 | 2025-09-16 04:53:00 | NOAA-20 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 94d85c04-d992-3788-b94d-f7959d2cf51b | -16.6943 | -49.77817 | 2025-09-16 04:53:00 | NOAA-20 | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ec4e351b-85af-3ec8-a1da-0c11e556f47a | -16.02456 | -59.2482 | 2025-09-16 04:53:00 | NOAA-20 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| ac3a6ec6-0cee-32b4-941d-b5753fdb6519 | -16.70341 | -54.96923 | 2025-09-16 04:53:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 13cca12d-3c12-3729-9de3-108996277213 | -16.06442 | -59.43196 | 2025-09-16 04:53:00 | NOAA-20 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| cc68cc7b-358f-31f1-8306-fe49e8b9a7f5 | -17.08104 | -45.83034 | 2025-09-16 04:53:00 | NOAA-20 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 1565d62c-39d8-3eea-8cb8-61e08a295647 | -16.7035 | -54.9471 | 2025-09-16 04:53:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fcd3bbec-f91f-3535-976d-9b9130a8f9e0 | -16.02757 | -59.45383 | 2025-09-16 04:53:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| cc9121b3-f1bb-3b05-8f70-5861c7c26289 | -16.71989 | -54.94897 | 2025-09-16 04:53:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 66b2adfa-fc3c-357b-b775-0fa5d2f1cc81 | -15.99805 | -59.41735 | 2025-09-16 04:53:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 145cf166-f144-3e03-a975-62358c9b0a19 | -16.51206 | -43.54993 | 2025-09-16 04:53:00 | NOAA-20 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 1b7deaf1-ba8c-3c5e-a208-1c321c17a9f3 | -15.01119 | -55.33626 | 2025-09-16 04:53:00 | NOAA-20 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b7e3c55d-6a12-39d4-95aa-84130bd1da48 | -14.8704 | -55.82384 | 2025-09-16 04:53:00 | NOAA-20 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 89913d0a-cad9-3603-a79e-e0fc06a3627e | -15.8697 | -59.39215 | 2025-09-16 04:53:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 3a9e169d-4cd6-31c7-a75e-ed794179a98c | -16.01203 | -59.45103 | 2025-09-16 04:53:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 382b73a7-32d0-3473-aca3-005e087f0295 | -15.82907 | -53.47137 | 2025-09-16 04:53:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 10.5 |
| fd7f7f61-7445-3485-8d63-d6c13094c4a9 | -17.07613 | -45.82651 | 2025-09-16 04:53:00 | NOAA-20 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 698df32a-bc6a-3cbd-9111-7d7f012cc69d | -15.77356 | -53.45105 | 2025-09-16 04:53:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 7.1 |
| bd6c9aa4-e704-34ee-94d2-4d062d8814d9 | -16.4775 | -55.10773 | 2025-09-16 04:53:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 905db962-6732-33c6-935d-4027a8f3a32d | -16.00517 | -59.44456 | 2025-09-16 04:53:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f917b955-4dd1-3535-8562-2a0c81753d0c | -15.99192 | -59.26593 | 2025-09-16 04:53:00 | NOAA-20 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| dca0a338-a857-31ea-bfe8-6dc3bc1220b2 | -15.62735 | -52.79028 | 2025-09-16 04:53:00 | NOAA-20 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 15141033-243b-347c-b32e-bfbfc9589267 | -16.52369 | -43.73244 | 2025-09-16 04:53:00 | NOAA-20 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2b2a8548-d16b-3fe0-9c6e-c6cd2c1550af | -17.07651 | -45.82318 | 2025-09-16 04:53:00 | NOAA-20 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| fe29db9e-3ee4-33d3-be20-5aafe5e9b356 | -15.99036 | -59.26182 | 2025-09-16 04:53:00 | NOAA-20 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 754deab4-afaf-3cb7-a094-5601eb1e54a3 | -16.48413 | -55.10886 | 2025-09-16 04:53:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| 3ce799f1-b18f-3665-8e79-8e5f303848e3 | -16.42824 | -45.67345 | 2025-09-16 04:53:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4946bfaa-83a7-34fd-a4f2-7438a1b00630 | -15.31259 | -59.41747 | 2025-09-16 04:53:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 81073cba-0dd9-3b64-80a2-23b70be3d659 | -15.78588 | -52.21323 | 2025-09-16 04:53:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d06d53ed-f08d-348d-8017-432b9d201d48 | -17.29748 | -40.68602 | 2025-09-16 04:53:00 | NOAA-20 | UMBURATIBA | MINAS GERAIS | Brasil | 3170305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 79273516-9b28-3630-8eec-14ea6da1cd4c | -16.71788 | -54.94216 | 2025-09-16 04:53:00 | NOAA-20 | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2f315b56-c440-3a6e-a79b-a243b865a374 | -16.01134 | -59.2555 | 2025-09-16 04:53:00 | NOAA-20 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 82b4980c-abb6-342c-9fd9-5a04e14a5f67 | -15.78532 | -53.44164 | 2025-09-16 04:53:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 4d8fd1af-ccee-317c-8457-e886b04b43d2 | -16.05231 | -59.42731 | 2025-09-16 04:53:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4ef07807-8888-3d63-8ea8-bbdb97383af9 | -16.00224 | -59.43854 | 2025-09-16 04:53:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0912e6a0-ae27-351a-87b5-cee305564c14 | -18.16413 | -49.20279 | 2025-09-16 04:53:00 | NOAA-20 | BURITI ALEGRE | GOIÁS | Brasil | 5203906 | 52 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| e9bbb0e7-c382-30a7-9017-8ccf74536b7e | -17.16481 | -49.3827 | 2025-09-16 04:53:00 | NOAA-20 | CROMÍNIA | GOIÁS | Brasil | 5206503 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 54a4f6d5-d28a-33f1-a06d-6527be0b5e5e | -18.15987 | -49.2021 | 2025-09-16 04:53:00 | NOAA-20 | BURITI ALEGRE | GOIÁS | Brasil | 5203906 | 52 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| a197824e-79a6-3b7d-a6b3-092e95bd0797 | -16.69735 | -54.96451 | 2025-09-16 04:53:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a73c1a4c-4720-3291-b897-960454d2885c | -15.9966 | -59.26186 | 2025-09-16 04:53:00 | NOAA-20 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 99ee2d6a-c207-3117-9bcc-1341d5e65327 | -16.71457 | -54.9416 | 2025-09-16 04:53:00 | NOAA-20 | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 93f9ac81-a952-34e6-8733-14140f430980 | -17.07085 | -45.82589 | 2025-09-16 04:53:00 | NOAA-20 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f24682f8-e4cd-3fa4-ae64-158d69963672 | -15.84191 | -59.43156 | 2025-09-16 04:53:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e263003e-932b-3940-b768-d9492ed9e267 | -15.80551 | -53.4904 | 2025-09-16 04:53:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5959151c-22e9-3224-a8ce-f1029caed10b | -15.78529 | -52.21726 | 2025-09-16 04:53:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 99048472-776d-3db8-9642-a01525173db5 | -15.79343 | -52.18608 | 2025-09-16 04:53:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4971b6e0-9c91-332e-95d6-48309b72f15b | -15.79577 | -52.19461 | 2025-09-16 04:53:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 7947637d-bbe6-3e41-a1fe-d8c8c0f640ce | -15.81897 | -53.46975 | 2025-09-16 04:53:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6596fd25-c726-31f9-aacb-93e77c2518a4 | -16.03235 | -59.44951 | 2025-09-16 04:53:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 11bb0ce8-d5f4-3174-b03e-fe04b6e2fb91 | -15.99594 | -59.25295 | 2025-09-16 04:53:00 | NOAA-20 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 7b5a2380-f8e9-3ecb-8ae7-981144f41d0f | -15.90637 | -56.26676 | 2025-09-16 04:53:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 9eacdb31-6347-33d7-87f6-9dfff0bfe175 | -16.66439 | -49.75548 | 2025-09-16 04:53:00 | NOAA-20 | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 404f58ac-2d62-35b0-a11c-bb53aff8415a | -16.71344 | -54.94879 | 2025-09-16 04:53:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |


[Clique aqui para ver as próximas entradas](README80.md)
