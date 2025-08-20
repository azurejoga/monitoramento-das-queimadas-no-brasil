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

## Dados Diários - Página 52

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e56b26e8-afd3-3946-a541-f5b0d097eed8 | -15.54552 | -48.56505 | 2025-08-20 04:59:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c02c2aec-9a6a-3c1a-8d66-460de1475d85 | -14.9933 | -54.82643 | 2025-08-20 04:59:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 66d70343-c954-32cd-8bae-685514234f39 | -19.7285 | -48.97573 | 2025-08-20 04:59:00 | NOAA-20 | COMENDADOR GOMES | MINAS GERAIS | Brasil | 3116902 | 31 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 293151f3-5f01-3432-a304-c6ba199f6df3 | -12.97563 | -56.85137 | 2025-08-20 04:59:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dca43536-a8f5-350f-88a0-63a6befe80f1 | -12.97999 | -56.86693 | 2025-08-20 04:59:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 505da7cc-7e87-30d0-b647-748ede4715bf | -13.15616 | -54.93308 | 2025-08-20 04:59:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 84069e7f-d145-3908-b370-58129a713425 | -13.14839 | -54.93917 | 2025-08-20 04:59:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c96d298f-b7ae-3cfa-8636-00f9fc3d16d5 | -12.97882 | -56.87416 | 2025-08-20 04:59:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f054a1b2-ae77-3615-84d2-b5459c3fdc06 | -14.61724 | -54.8886 | 2025-08-20 04:59:00 | NOAA-20 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 85efb850-a759-3c07-883f-afecb0d00e85 | -14.62059 | -54.88917 | 2025-08-20 04:59:00 | NOAA-20 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5b179302-9673-369b-8572-be936e08e5cf | -13.15506 | -54.94024 | 2025-08-20 04:59:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1a587f1d-8063-33cf-b89e-4fd05729a79c | -18.67338 | -46.9832 | 2025-08-20 04:59:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c202a9df-33a9-37a9-b182-30faf492755e | -15.63534 | -56.29728 | 2025-08-20 04:59:00 | NOAA-20 | VÁRZEA GRANDE | MATO GROSSO | Brasil | 5108402 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 917f3a60-4a68-33fb-9ffc-de1f5985d6fd | -13.74017 | -52.01205 | 2025-08-20 04:59:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 9956ed57-e877-3af3-94c7-4b801fcfa639 | -15.57429 | -50.30888 | 2025-08-20 04:59:00 | NOAA-20 | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 353f5cb3-7701-37cb-882c-c5068bebdd2f | -15.06498 | -54.84204 | 2025-08-20 04:59:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9956ca43-7c9f-3dcb-821f-93ff0340d3d6 | -14.50701 | -45.95949 | 2025-08-20 04:59:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1b584cd7-024d-3925-9118-7d527b930b42 | -13.3529 | -54.40202 | 2025-08-20 04:59:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b2d29700-f0fd-377d-ac69-3976e5d84c68 | -14.36308 | -52.00276 | 2025-08-20 04:59:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9f9c25d1-d00d-39e5-89e9-ede51924b1c7 | -13.19007 | -54.95688 | 2025-08-20 04:59:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2f10cfbf-ff9a-3327-bf2c-f785a9bf2f94 | -15.74674 | -46.62412 | 2025-08-20 04:59:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 289cf07d-d213-3337-9818-c982b4a8a478 | -14.89681 | -48.07692 | 2025-08-20 04:59:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| db7233ac-2b81-3269-8cab-568f729f0cf8 | -13.16173 | -54.94131 | 2025-08-20 04:59:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4e921a36-98f4-3da6-b89d-a23b4e62cf13 | -14.32268 | -51.98737 | 2025-08-20 04:59:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3749bccb-a528-3a86-af94-79f4f0609033 | -13.32703 | -54.41299 | 2025-08-20 04:59:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 1c804f01-70eb-3409-b296-63fb033fae8f | -14.98656 | -54.82535 | 2025-08-20 04:59:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 972bd2c6-ac77-399d-8a2e-6a231cfcfdea | -17.66936 | -54.06098 | 2025-08-20 04:59:00 | NOAA-20 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 470bd222-daeb-3e6c-8bdb-6f006de5dc70 | -13.1545 | -54.94382 | 2025-08-20 04:59:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3849063f-923e-39ef-a1d0-5f65521c92d4 | -13.15005 | -54.92842 | 2025-08-20 04:59:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 5ea9a45e-a724-3800-9d07-21caa96906c9 | -15.54484 | -42.28561 | 2025-08-20 04:59:00 | NOAA-20 | INDAIABIRA | MINAS GERAIS | Brasil | 3130655 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 2a51f29d-add2-3ba5-8df2-4b9166a1664c | -14.74497 | -56.02219 | 2025-08-20 04:59:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| aea5a8ff-daaa-3005-a547-3e263ca36fee | -12.97548 | -56.87358 | 2025-08-20 04:59:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5b487c33-0ffc-3291-9413-9e7f62a6a974 | -13.1367 | -54.9171 | 2025-08-20 05:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 33.7 |
| e07a1cff-e97a-3266-892f-9ecdcd7cf954 | -13.1364 | -54.9376 | 2025-08-20 05:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 39.1 |
| aed9386f-c425-322c-b1e7-f862add0f754 | -13.1558 | -54.9151 | 2025-08-20 05:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 44.9 |
| 56a84b7f-acb9-322d-bb2d-31d122af0f96 | -13.1555 | -54.9357 | 2025-08-20 05:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 40.4 |
| fefc0ae4-68e4-35a1-9aa1-b4c670ae5be5 | -4.8786 | -42.7204 | 2025-08-20 05:00:00 | GOES-19 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 58.8 |
| c6422e77-b2bd-336a-b738-c1ee4ae92a85 | -20.339 | -51.7062 | 2025-08-20 05:00:00 | GOES-19 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 83.9 |
| 6810a5c4-b6be-3454-a84e-8e974b030ba8 | -4.8788 | -42.6969 | 2025-08-20 05:00:00 | GOES-19 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 69.2 |
| 938e09f1-6362-3a35-891d-e2249659140c | -20.52336 | -57.40488 | 2025-08-20 05:01:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d09e70ba-df1c-35d7-91b1-9ebef74d904e | -21.0035 | -47.65672 | 2025-08-20 05:01:00 | NOAA-20 | BRODOWSKI | SÃO PAULO | Brasil | 3507803 | 35 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 4369c8cb-7971-3cad-b349-8033eef11f6b | -20.34543 | -51.71206 | 2025-08-20 05:01:00 | NOAA-20 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| cbb971bb-b644-3be8-a8e5-5f814258b1fd | -22.26966 | -48.50414 | 2025-08-20 05:01:00 | NOAA-20 | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 96c4026e-79b3-3fd8-bb51-891b163ba3af | -23.99032 | -48.56209 | 2025-08-20 05:01:00 | NOAA-20 | CAPÃO BONITO | SÃO PAULO | Brasil | 3510203 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 4ea1a42c-be3b-30b5-8577-064850b9772c | -20.34286 | -51.70646 | 2025-08-20 05:01:00 | NOAA-20 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 586f2e9f-de68-31ef-aa12-b3df87a054a5 | -21.62941 | -57.23389 | 2025-08-20 05:01:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5e90a4b4-37db-321a-b7f4-e744f14c50fa | -22.37008 | -50.4044 | 2025-08-20 05:01:00 | NOAA-20 | LUTÉCIA | SÃO PAULO | Brasil | 3527900 | 35 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 725a7aeb-961c-3d68-8e81-ce5e9e001fd2 | -21.87523 | -48.20376 | 2025-08-20 05:01:00 | NOAA-20 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 4e2c508c-b1d2-322d-9f7a-9300b318b8b7 | -20.33339 | -51.7064 | 2025-08-20 05:01:00 | NOAA-20 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a1a7c993-bad9-32cc-870c-d17535bf9f33 | -21.8934 | -48.18453 | 2025-08-20 05:01:00 | NOAA-20 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 603d3b57-aaf5-3eb7-b7a4-5f7d05ce4ee9 | -21.13037 | -47.03683 | 2025-08-20 05:01:00 | NOAA-20 | ITAMOGI | MINAS GERAIS | Brasil | 3132909 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ccfd7746-28e1-39c5-a825-1e74b855e569 | -20.33288 | -51.71043 | 2025-08-20 05:01:00 | NOAA-20 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 55224e81-ae18-3baf-8305-52b9c3c2df18 | -22.45563 | -47.55984 | 2025-08-20 05:01:00 | NOAA-20 | RIO CLARO | SÃO PAULO | Brasil | 3543907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 9b2662ee-e0f7-3347-ae5c-dcdb2acf0f9c | -21.89871 | -48.18567 | 2025-08-20 05:01:00 | NOAA-20 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a6123670-3195-3f33-94e0-6df40dcbb828 | -22.456 | -47.55581 | 2025-08-20 05:01:00 | NOAA-20 | SANTA GERTRUDES | SÃO PAULO | Brasil | 3546702 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 30841e17-392d-3323-a6c8-eb0b889b6d59 | -21.00389 | -47.65284 | 2025-08-20 05:01:00 | NOAA-20 | BRODOWSKI | SÃO PAULO | Brasil | 3507803 | 35 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 4957c1e6-aad6-304c-9f1d-73a849d71372 | -20.52034 | -57.40443 | 2025-08-20 05:01:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 8.1 |
| 370b1837-9b46-321c-8641-0bf7c65645a2 | -22.36952 | -50.4095 | 2025-08-20 05:01:00 | NOAA-20 | LUTÉCIA | SÃO PAULO | Brasil | 3527900 | 35 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 15a4fe35-4a21-362c-b6e5-5d997d5059e7 | -20.33705 | -51.71103 | 2025-08-20 05:01:00 | NOAA-20 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 274d6808-ebb1-37f0-b054-d79e640a10bd | -20.52495 | -57.37499 | 2025-08-20 05:01:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| dcdd3778-16a6-326c-8c51-3da4716acc36 | -22.69206 | -47.34853 | 2025-08-20 05:01:00 | NOAA-20 | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 73d3a9cf-bbeb-3a07-be57-2f1ff5b792f2 | -23.99272 | -48.56207 | 2025-08-20 05:01:00 | NOAA-20 | CAPÃO BONITO | SÃO PAULO | Brasil | 3510203 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 57fd002c-30b4-3485-85fd-39b510f38d88 | -23.97549 | -49.65183 | 2025-08-20 05:01:00 | NOAA-20 | SÃO JOSÉ DA BOA VISTA | PARANÁ | Brasil | 4125407 | 41 | 33 | nan | nan | nan | Cerrado | 3.0 |
| dd4ef596-3c82-3561-900d-93fcb89bdc69 | -20.34175 | -51.70755 | 2025-08-20 05:01:00 | NOAA-20 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 5b4673d8-47be-35e2-811a-cb80d4895202 | -21.00311 | -47.66051 | 2025-08-20 05:01:00 | NOAA-20 | BRODOWSKI | SÃO PAULO | Brasil | 3507803 | 35 | 33 | nan | nan | nan | Cerrado | 19.8 |
| 7d2a3d54-69d6-3f06-95ef-b140751f8473 | -21.87558 | -48.20019 | 2025-08-20 05:01:00 | NOAA-20 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 4a44b7c9-be86-333c-92b5-914407cd1678 | -23.98735 | -48.5615 | 2025-08-20 05:01:00 | NOAA-20 | CAPÃO BONITO | SÃO PAULO | Brasil | 3510203 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 0a1aaa1d-418d-3a1f-a5d1-6fd8f605da7e | -22.27 | -48.50067 | 2025-08-20 05:01:00 | NOAA-20 | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 39fe1ac6-fe37-3919-a4ef-b69de40c23a3 | -20.34191 | -51.71447 | 2025-08-20 05:01:00 | NOAA-20 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 489f5f7e-2d35-3d39-97dc-15a9aa3808a0 | -21.89301 | -48.18848 | 2025-08-20 05:01:00 | NOAA-20 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| fd335a20-f7f3-3d50-ac1f-0eb1e4edbb12 | -22.45038 | -47.55517 | 2025-08-20 05:01:00 | NOAA-20 | RIO CLARO | SÃO PAULO | Brasil | 3543907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| f13003f8-160e-3672-b75b-fb66eb7e0777 | -20.52451 | -57.39754 | 2025-08-20 05:01:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 053a3de6-7562-3f7d-84f6-0d5bd9cd956a | -21.00377 | -47.65768 | 2025-08-20 05:01:00 | NOAA-20 | BRODOWSKI | SÃO PAULO | Brasil | 3507803 | 35 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 43f29686-d3d6-3e8a-9791-d9ef8074c7c2 | -22.55879 | -49.77683 | 2025-08-20 05:01:00 | NOAA-20 | SÃO PEDRO DO TURVO | SÃO PAULO | Brasil | 3550506 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| acfe3fc2-4a5d-3c4f-bbce-060260caed56 | -20.33756 | -51.70701 | 2025-08-20 05:01:00 | NOAA-20 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 0f1c07be-3b9c-398a-a3a2-f3a2f891b23a | -21.00413 | -47.65385 | 2025-08-20 05:01:00 | NOAA-20 | BRODOWSKI | SÃO PAULO | Brasil | 3507803 | 35 | 33 | nan | nan | nan | Cerrado | 7.6 |
| aa90227c-dbe5-3d7c-b25f-4b238d739268 | -22.55391 | -49.7763 | 2025-08-20 05:01:00 | NOAA-20 | SÃO PEDRO DO TURVO | SÃO PAULO | Brasil | 3550506 | 35 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 318dc084-540e-38df-9dea-b519995e1f0f | -22.36485 | -50.40889 | 2025-08-20 05:01:00 | NOAA-20 | LUTÉCIA | SÃO PAULO | Brasil | 3527900 | 35 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 47042d0d-e97a-3ba0-b89a-f978f91f0a87 | -20.34124 | -51.71155 | 2025-08-20 05:01:00 | NOAA-20 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 15.5 |
| cb139632-43dd-3704-b264-0159efad1745 | -20.52783 | -57.39812 | 2025-08-20 05:01:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 951bc1d3-3e81-3d13-9c51-968939a3c475 | -20.34644 | -51.70411 | 2025-08-20 05:01:00 | NOAA-20 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9258d767-ba83-362e-83e0-405a48bd3dcf | -21.90713 | -47.25599 | 2025-08-20 05:01:00 | NOAA-20 | SANTA CRUZ DAS PALMEIRAS | SÃO PAULO | Brasil | 3546306 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 3677e6ca-c78c-3e1c-8530-bb6bb50a01b6 | -22.36464 | -51.51449 | 2025-08-20 05:01:00 | NOAA-20 | NARANDIBA | SÃO PAULO | Brasil | 3532207 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| cb508e2e-71fd-3dac-b2c4-d6b1af94148b | -20.34225 | -51.70356 | 2025-08-20 05:01:00 | NOAA-20 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 6275c361-e677-3232-8907-e17b7917e837 | -22.69242 | -47.34457 | 2025-08-20 05:01:00 | NOAA-20 | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 99330f99-3806-355f-bd62-bd8f3a3e801e | -21.00341 | -47.66147 | 2025-08-20 05:01:00 | NOAA-20 | BRODOWSKI | SÃO PAULO | Brasil | 3507803 | 35 | 33 | nan | nan | nan | Cerrado | 15.0 |
| c5bb9212-b5e4-30c1-9530-5119afeef60d | -20.34492 | -51.71606 | 2025-08-20 05:01:00 | NOAA-20 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 0feff3ff-c97d-3005-a29d-1a37ed900cb5 | -22.36541 | -50.40379 | 2025-08-20 05:01:00 | NOAA-20 | LUTÉCIA | SÃO PAULO | Brasil | 3527900 | 35 | 33 | nan | nan | nan | Cerrado | 6.3 |
| ec4ef637-4993-3083-b56d-adae4232d505 | -20.34593 | -51.70808 | 2025-08-20 05:01:00 | NOAA-20 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 01c1bb59-bee4-30d9-8ba8-4d3da460421d | -22.55452 | -49.7705 | 2025-08-20 05:01:00 | NOAA-20 | SÃO PEDRO DO TURVO | SÃO PAULO | Brasil | 3550506 | 35 | 33 | nan | nan | nan | Cerrado | 5.6 |
| c3499a6a-d17b-3a81-89cb-80705b7e6a0b | -20.34238 | -51.71045 | 2025-08-20 05:01:00 | NOAA-20 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 510e55c5-b508-3c89-9e1f-ad7a3fa5cfa3 | -20.339 | -51.7062 | 2025-08-20 05:10:00 | GOES-19 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 81.2 |
| a9e0b6f7-a9ca-33ac-8f31-846ae5499a0b | -13.1364 | -54.9376 | 2025-08-20 05:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 38.5 |
| 7a9d038e-a365-3c5c-99a1-72292c3a3dbf | -8.034 | -47.6639 | 2025-08-20 05:10:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 47.8 |
| 43ac62ae-8887-3fcb-9fac-1f459e3a19d8 | -13.1558 | -54.9151 | 2025-08-20 05:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 33.5 |
| 2be06c4b-ae33-391f-aede-840eb7c6144f | -13.1555 | -54.9357 | 2025-08-20 05:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 46.6 |
| 5f623736-a773-3dff-8ea2-f68cd9650e93 | -20.339 | -51.7062 | 2025-08-20 05:20:00 | GOES-19 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 73.5 |
| f46f375e-011c-372e-9b9e-77fc5cf3d609 | -13.1555 | -54.9357 | 2025-08-20 05:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 42.3 |
| a875b0d6-2530-3528-b8b5-fb74a608bb5e | -13.1364 | -54.9376 | 2025-08-20 05:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 34.1 |
| 9c67d8e4-2b6d-3b5d-8195-4b51af158efe | -13.1558 | -54.9151 | 2025-08-20 05:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 35.0 |


[Clique aqui para ver as próximas entradas](README53.md)
