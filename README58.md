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

## Dados Diários - Página 58

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| eb09b9e7-0681-3f96-b05a-5053d4b71923 | -11.15729 | -45.10407 | 2024-11-17 04:31:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| eea77c15-b88c-3145-b09f-2d4830cece91 | -10.38292 | -44.87913 | 2024-11-17 04:31:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 74ce2c4e-19f1-3741-87f3-2c755bc48020 | -12.55362 | -57.82543 | 2024-11-17 04:31:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f1ff281b-4836-344f-9b55-064d4ada1db5 | -11.09919 | -45.34619 | 2024-11-17 04:31:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bd76b906-1b3f-3e14-b2d2-997d4c7822e0 | -9.20373 | -47.68788 | 2024-11-17 04:31:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 87f1beb2-769d-3b55-8108-56d684677c83 | -10.13263 | -49.14956 | 2024-11-17 04:31:00 | NOAA-20 | CHAPADA DE AREIA | TOCANTINS | Brasil | 1704600 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c2e35701-83e9-3dca-a6ce-ed9afcc53477 | -10.72672 | -40.52353 | 2024-11-17 04:31:00 | NOAA-20 | MIRANGABA | BAHIA | Brasil | 2921401 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| f3edf0d0-36af-3ed7-b36f-a2530f76b2fe | -9.93393 | -49.09561 | 2024-11-17 04:31:00 | NOAA-20 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5c488365-1dd3-3cc1-aa0b-315d88e3dc84 | -12.26739 | -44.98813 | 2024-11-17 04:31:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2d7c8ad0-39da-37bb-b61e-094574168a20 | -7.35619 | -46.37482 | 2024-11-17 04:31:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 732ec05d-1e3c-3008-ace6-4a4363ae5e44 | -12.54998 | -57.76852 | 2024-11-17 04:31:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fa4c47ac-6669-3a38-8b50-6f54871741e1 | -12.26745 | -44.98062 | 2024-11-17 04:31:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9a9fade1-ab22-30db-b87a-0d7ac4f8d4f3 | -12.5539 | -57.77547 | 2024-11-17 04:31:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5587f64e-8b54-37de-852b-38f9940ee0b3 | -8.44052 | -44.20877 | 2024-11-17 04:31:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 56d8e36d-c2b2-3079-9ff2-3d9dbb747c96 | -10.07953 | -48.29987 | 2024-11-17 04:31:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0fb29e56-8cac-3afd-a575-1c031cb7bf61 | -8.44432 | -44.20931 | 2024-11-17 04:31:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f521ab11-58ef-3788-bdca-08894d76c1dd | -10.68102 | -44.01932 | 2024-11-17 04:31:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7380f91e-9500-36f2-bf5b-e7a69ea01d19 | -11.7204 | -44.08479 | 2024-11-17 04:31:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cc568703-b98e-37b1-95b4-3b71ef76e352 | -11.12276 | -44.5707 | 2024-11-17 04:31:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f56587dc-185b-30b2-8986-29db06bd3056 | -7.42392 | -47.86503 | 2024-11-17 04:31:00 | NOAA-20 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9e26a31b-d260-32b4-9724-4cb45b58f0a5 | -12.39438 | -57.52448 | 2024-11-17 04:31:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| b079fd9e-beb0-3450-9aae-be7f65ebb6a8 | -12.54884 | -57.76916 | 2024-11-17 04:31:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bea73c98-d41c-3616-aae8-d34ee1be85a8 | -7.49978 | -47.35684 | 2024-11-17 04:31:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 48c6f2ac-978a-318d-af34-da687fecd667 | -10.4219 | -44.71551 | 2024-11-17 04:31:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a7bd2355-61b4-343a-afd9-7715ada5b1bf | -12.55865 | -57.82649 | 2024-11-17 04:31:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| aa92ff44-d811-37f9-94e4-4809d9bef4a8 | -11.84932 | -46.93773 | 2024-11-17 04:31:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 7bf7c229-5d98-3b20-89cf-7ea4b2788024 | -10.12931 | -49.14903 | 2024-11-17 04:31:00 | NOAA-20 | CHAPADA DE AREIA | TOCANTINS | Brasil | 1704600 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0069c2a1-b6aa-3ca0-814d-afab6cc2769c | -12.44104 | -43.79976 | 2024-11-17 04:31:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| affce88f-c831-3dfc-910f-69e1a3a79175 | -8.43808 | -44.19891 | 2024-11-17 04:31:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 74b2d8f6-9637-3003-bc66-055de59df604 | -7.35675 | -46.37117 | 2024-11-17 04:31:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1e1ce0bb-92f3-360c-b059-e503b08e470c | -10.08529 | -49.04144 | 2024-11-17 04:31:00 | NOAA-20 | MONTE SANTO DO TOCANTINS | TOCANTINS | Brasil | 1713700 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a9e896b1-252c-33a9-a30c-0f14a0457c1c | -12.54833 | -57.77743 | 2024-11-17 04:31:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 561c97c7-ef5d-3bb2-8b75-d2e39e077f79 | -12.55329 | -57.7731 | 2024-11-17 04:31:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e64484d9-2cf6-3f71-a83a-92c8e2969633 | -10.7272 | -40.52267 | 2024-11-17 04:31:00 | NOAA-20 | MIRANGABA | BAHIA | Brasil | 2921401 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 08040bc8-307a-3bcc-b20b-1acd94654161 | -7.48011 | -47.1781 | 2024-11-17 04:31:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0e56f694-4e55-352b-8785-c535c17d599a | -8.44189 | -44.19944 | 2024-11-17 04:31:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| b926427e-367b-367c-bc20-e8e9243e9475 | -11.16035 | -45.10918 | 2024-11-17 04:31:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4ffed20a-667d-3f74-ba75-999be4eb1943 | -9.43041 | -43.59916 | 2024-11-17 04:31:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| acf636c3-0c34-3adb-9514-178f7d5bbe4f | -8.44638 | -44.19529 | 2024-11-17 04:31:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 10.2 |
| cb2948f8-8e28-3125-9879-b9614255b1ee | -12.39302 | -57.5294 | 2024-11-17 04:31:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| d0902a7a-be98-3113-ac51-cca40544c85b | -12.26426 | -44.98289 | 2024-11-17 04:31:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 36cb9b84-e075-3e95-aac9-5e0809cae7ca | -12.55421 | -57.82236 | 2024-11-17 04:31:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e36e82a8-dfd1-3ff9-b9f2-ce410b73a059 | -12.26615 | -44.99003 | 2024-11-17 04:31:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c8e7b364-9f5d-3873-9f51-644668753708 | -12.56426 | -57.8245 | 2024-11-17 04:31:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a09c6c0d-2706-39d8-b50a-cb85d8161922 | -10.66196 | -44.49527 | 2024-11-17 04:31:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 265000c3-c06f-3b57-8f75-ee253b486c74 | -7.71515 | -46.6632 | 2024-11-17 04:31:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7733475f-490c-3147-ad05-b9ed676e2ce4 | -8.44394 | -44.18541 | 2024-11-17 04:31:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| ce083872-105b-3bd2-ac02-103eae9c7839 | -8.43984 | -44.2134 | 2024-11-17 04:31:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5e36f3d7-a8f8-3785-873b-19a6256755eb | -11.85276 | -46.93827 | 2024-11-17 04:31:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 7217b4d2-6e45-3f4f-88f0-e29f9bdfc4e9 | -10.72681 | -40.52554 | 2024-11-17 04:31:00 | NOAA-20 | MIRANGABA | BAHIA | Brasil | 2921401 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 0a4ad255-a63b-37dd-b55a-cabba1d2bd6f | -12.26807 | -44.98342 | 2024-11-17 04:31:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 4a98e138-4bd6-3503-9cf1-20ac1f16d71c | -10.68162 | -44.02371 | 2024-11-17 04:31:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b9007aa2-ab3d-31c0-ab1e-80fb71345f26 | -12.27055 | -44.9932 | 2024-11-17 04:31:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c46ad02e-51c0-3e63-9d2f-0fca6f69e35c | -8.4374 | -44.20359 | 2024-11-17 04:31:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 1ea1e8ba-ae94-3cb0-8a98-87d1cac290d9 | -10.08284 | -48.3004 | 2024-11-17 04:31:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e5821054-03cc-30bb-b45d-095ae82238cd | -11.12347 | -44.56582 | 2024-11-17 04:31:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7e6f8fa9-7151-3fec-8196-7afe3566e682 | -17.58306 | -57.59549 | 2024-11-17 04:33:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |
| 70455e34-1e93-3f45-bf4e-641903ac71cc | -17.5979 | -57.59451 | 2024-11-17 04:33:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.4 |
| c5a1e6b5-d328-39fc-bfb5-c2434b1efcce | -17.60618 | -57.57632 | 2024-11-17 04:33:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| 65a5b5b7-deea-3b60-ac52-73d151be19fe | -17.57788 | -57.47533 | 2024-11-17 04:33:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 5c31c027-73a3-3813-b02c-5a5dd8466fd5 | -17.6043 | -57.58589 | 2024-11-17 04:33:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.5 |
| 6c4c8b1a-e260-39d8-a694-9bb1b05ee4e4 | -17.60147 | -57.60027 | 2024-11-17 04:33:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 11.6 |
| 0ebb7df1-87a7-37ea-aece-620d43a06855 | -17.60336 | -57.59068 | 2024-11-17 04:33:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.5 |
| 89f57cf4-d555-3f09-b4df-089a573970d8 | -17.59119 | -57.60226 | 2024-11-17 04:33:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.4 |
| 21db9640-3f55-3588-a7ba-2e28a9315b67 | -17.59978 | -57.58492 | 2024-11-17 04:33:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 52d386e5-f2fb-3ab4-b1a2-1fce39b63ed5 | -17.55551 | -57.446 | 2024-11-17 04:33:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| d2d9e22c-54f8-36ac-8b50-4f92af42a8ac | -17.62065 | -57.57447 | 2024-11-17 04:33:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| c3b5bf53-8285-3448-be3d-e65ea42366c0 | -20.20782 | -56.62724 | 2024-11-17 04:33:00 | NOAA-20 | MIRANDA | MATO GROSSO DO SUL | Brasil | 5005608 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 83176141-acdf-37e7-a59b-29da7bd4b019 | -17.59338 | -57.59354 | 2024-11-17 04:33:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.4 |
| 25f64192-771c-3d57-97e3-54169267e0df | -17.58339 | -57.59638 | 2024-11-17 04:33:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 1f4ac6a1-2086-3c01-a56b-a93303fdd2f3 | -17.82548 | -54.54622 | 2024-11-17 04:33:00 | NOAA-20 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 78002f2b-56a7-3988-9932-037e17654ee0 | -16.09768 | -60.09644 | 2024-11-17 04:33:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f6cd38ad-b8e3-3a64-9408-a4d2ba1e5176 | -15.91671 | -59.8069 | 2024-11-17 04:33:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 449456e0-3b0a-3501-8fec-1d2a86af98e0 | -17.59665 | -57.57349 | 2024-11-17 04:33:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 59e033ef-0642-39f0-a0b2-d949e14e7a02 | -15.91382 | -59.82119 | 2024-11-17 04:33:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 750c83db-fb56-3428-a45b-80498fb8b117 | -17.82649 | -54.54424 | 2024-11-17 04:33:00 | NOAA-20 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 3.2 |
| af87f06c-d6b3-3002-92c5-2e7d5d592337 | -17.60881 | -57.58687 | 2024-11-17 04:33:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.5 |
| 2e50141c-6486-37f0-a533-917fd6467f69 | -17.60524 | -57.5811 | 2024-11-17 04:33:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| 24d2a8a3-dd5d-34ed-9f6b-f2a24b01bbc4 | -17.61069 | -57.5773 | 2024-11-17 04:33:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| 3d405072-55a0-3158-b1c3-edd5b6c96847 | -16.09712 | -60.10057 | 2024-11-17 04:33:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 631654af-4f7c-3472-a079-ae199f412cfc | -20.99539 | -51.79227 | 2024-11-17 04:33:00 | NOAA-20 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| a9c4dbfe-2189-39a7-927c-3f8b95c0dd18 | -17.59149 | -57.60312 | 2024-11-17 04:33:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.7 |
| 44a26165-c8f9-3f1e-a063-0d2bfec82602 | -17.5921 | -57.59746 | 2024-11-17 04:33:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.4 |
| 7ffe4bfd-a227-38d6-80b2-5a2cc14868fa | -19.48817 | -56.61977 | 2024-11-17 04:33:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 59cef14a-77ab-3898-9186-e7b4e18e5c36 | -17.60693 | -57.59645 | 2024-11-17 04:33:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 11.6 |
| aec18767-a30c-35c1-8ac9-15528a6246db | -17.59483 | -57.58307 | 2024-11-17 04:33:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| ed0149e8-2e68-3dfe-8987-c808e4981957 | -17.83023 | -54.54498 | 2024-11-17 04:33:00 | NOAA-20 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f767945e-3238-3f41-a378-93b2444fea64 | -17.58758 | -57.59649 | 2024-11-17 04:33:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.4 |
| b2fb5b8f-6aab-31a0-a704-1e75f7ec0243 | -17.60242 | -57.59547 | 2024-11-17 04:33:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 11.6 |
| 584c2173-3719-3141-9616-43556b1d396e | -17.59809 | -57.56963 | 2024-11-17 04:33:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.8 |
| aaf0cc98-5842-3fd8-963c-93687188b753 | -17.59695 | -57.59929 | 2024-11-17 04:33:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.4 |
| 0c1c8348-82fb-3870-879b-9ef2c54e899c | -17.59884 | -57.58971 | 2024-11-17 04:33:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 52f283d1-f46d-3dca-8853-a7c4ec45445e | -17.59122 | -57.57729 | 2024-11-17 04:33:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 0a9244d7-0acb-3a2a-a901-c6a9848d10c6 | -17.59601 | -57.60409 | 2024-11-17 04:33:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.7 |
| f14bffb8-5029-3639-bf25-4dad519d4d33 | -15.92675 | -59.81279 | 2024-11-17 04:33:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1f0b0a23-adee-3f79-9f0d-6bce77af047b | -15.66978 | -59.73289 | 2024-11-17 04:33:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c19cbba0-cfdc-35e9-947d-edf70bec856e | -17.57969 | -57.46587 | 2024-11-17 04:33:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| ad62e843-37ad-3710-9465-31892cc7b5e6 | -16.0979 | -60.09687 | 2024-11-17 04:33:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dab91979-ee97-329f-85c1-8d58fbdf2a1d | -17.59574 | -57.57827 | 2024-11-17 04:33:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 05f0aa38-4cd2-3574-88bd-d597ea97acff | -17.59527 | -57.58396 | 2024-11-17 04:33:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |


[Clique aqui para ver as próximas entradas](README59.md)
