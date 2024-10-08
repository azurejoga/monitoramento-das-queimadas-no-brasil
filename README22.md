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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3c009fc1-bd9b-3a0c-a3ad-e13510b854da | -21.381001 | -55.675701 | 2024-10-08 01:43:36 | METOP-B | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 5241f1e6-2836-317d-9b9e-40cb3c7cbb0b | -20.7773 | -54.824799 | 2024-10-08 01:43:42 | METOP-B | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| a0e8a121-1954-3707-8663-40d8dcb90d7f | -20.7677 | -54.827702 | 2024-10-08 01:43:42 | METOP-B | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| da19f588-d937-3a26-9092-8873ffeb3438 | -21.4158 | -57.206299 | 2024-10-08 01:43:42 | METOP-B | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| cd805490-40c9-3c54-9eb0-992f72dcd5da | -21.419001 | -57.218601 | 2024-10-08 01:43:42 | METOP-B | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 52fdc5ae-8cf1-3cd3-a59e-5fc58e71fd3d | -21.4221 | -57.230999 | 2024-10-08 01:43:42 | METOP-B | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| b52eddcd-e365-3218-ab5d-96824f2b9377 | -21.425301 | -57.243301 | 2024-10-08 01:43:42 | METOP-B | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 73d14546-6b42-3ae5-9138-1602d7b12b17 | -21.4156 | -57.246101 | 2024-10-08 01:43:42 | METOP-B | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 89de09dd-743b-345d-b2b0-e46d995e1175 | -21.4028 | -57.236599 | 2024-10-08 01:43:42 | METOP-B | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 80321237-61f2-3d34-860b-7747babacf15 | -21.405899 | -57.248901 | 2024-10-08 01:43:42 | METOP-B | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 2b1241f4-1437-3b64-a3e3-f8f38b222add | -21.3899 | -57.2271 | 2024-10-08 01:43:42 | METOP-B | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| ef452927-d602-3836-b8ee-40fa896670c9 | -21.393101 | -57.239399 | 2024-10-08 01:43:42 | METOP-B | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 076cb4a8-48d4-36ab-b47a-5d975b322b2d | -21.3962 | -57.251701 | 2024-10-08 01:43:42 | METOP-B | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| bc335517-3304-36d1-b014-f5acaf04bf05 | -19.367701 | -51.678398 | 2024-10-08 01:43:50 | METOP-B | PARANAÍBA | MATO GROSSO DO SUL | Brasil | 5006309 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 377105b2-c236-3195-a6ae-b301a5bb746c | -20.061199 | -55.957199 | 2024-10-08 01:43:58 | METOP-B | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 5a28cff3-f560-34ee-a989-ff2c9d4fd7c7 | -19.575399 | -56.521301 | 2024-10-08 01:44:08 | METOP-B | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| e869858b-dd68-3362-99d1-f5e29551ce2d | -18.8913 | -54.548302 | 2024-10-08 01:44:11 | METOP-B | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 59561c61-05fd-3f6d-8ff6-4fc75cc3740f | -18.633801 | -57.216099 | 2024-10-08 01:44:26 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| af38ed45-f8a0-370a-85d6-232d229a82e3 | -18.6241 | -57.2188 | 2024-10-08 01:44:26 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 263db2cd-9bd9-3c6c-a1e3-082f9c734623 | -18.608299 | -57.237999 | 2024-10-08 01:44:27 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 93be8f79-8177-38ea-8740-94f05889f8d4 | -18.5986 | -57.2407 | 2024-10-08 01:44:27 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 9510d6b6-c037-3e5c-8f09-5cf9cbbb69b4 | -18.6021 | -57.2542 | 2024-10-08 01:44:27 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 8dcd5534-01bb-3bfa-9aaf-772e3604bf2d | -16.9963 | -56.6646 | 2024-10-08 01:44:50 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| a1ebec27-a02c-3346-ab62-3457d556c428 | -16.9226 | -57.461498 | 2024-10-08 01:44:55 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 347ecced-abfe-349d-8cb1-dbe713d2f3be | -16.926201 | -57.475498 | 2024-10-08 01:44:55 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 11684661-bec2-3931-88aa-d1b2a57cfbd6 | -16.912901 | -57.464199 | 2024-10-08 01:44:55 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| c319c822-ef3f-37f1-b9ec-c3285b1b6b7d | -16.9165 | -57.478199 | 2024-10-08 01:44:55 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| fab28510-93fb-31e2-8259-f8075b738e94 | -16.7946 | -57.406898 | 2024-10-08 01:44:57 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| c8ec1b23-f9d7-34cb-be52-2ffaadc490d4 | -16.6506 | -57.089699 | 2024-10-08 01:44:58 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 689b20e7-d734-3850-ba07-1ba733b2a5ae | -16.6544 | -57.1045 | 2024-10-08 01:44:58 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 03050144-9758-3523-90d9-99b86078cc87 | -16.6583 | -57.1194 | 2024-10-08 01:44:58 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 1dc65053-4d8d-35be-ab02-2a0776df3ae1 | -16.541599 | -57.714699 | 2024-10-08 01:45:02 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| d7be1fc2-e143-3938-a745-86379d33f077 | -16.4828 | -57.687 | 2024-10-08 01:45:03 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| d8799951-d5d8-3a48-9a21-11a32cc22b16 | -16.480101 | -57.717098 | 2024-10-08 01:45:03 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 7dfe5a36-781b-304a-a61e-61c69b283564 | -16.483601 | -57.730701 | 2024-10-08 01:45:03 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| c4b6c331-dd6a-309c-8cd0-27cc67f834a6 | -16.0299 | -57.496799 | 2024-10-08 01:45:09 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 8ecd8970-cb01-34af-9928-48a3e96a081b | -16.033501 | -57.5112 | 2024-10-08 01:45:09 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| b88048e9-839e-31d6-9b96-81e508f64e86 | -2.9797 | -49.5342 | 2024-10-08 01:45:23 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 51.3 |
| c80fecb4-9e40-3bb5-9f0f-a5b5c0e2891c | -5.5718 | -44.87 | 2024-10-08 01:45:38 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 83.9 |
| 13829b60-bd4c-3fa5-9e22-ada5308099ea | -5.5716 | -44.8927 | 2024-10-08 01:45:38 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 63.7 |
| f6c27d06-d302-3d40-bb7e-5ca3614b12c7 | -9.4086 | -66.5624 | 2024-10-08 01:46:00 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 62.9 |
| a5bfa8d1-1fe2-326f-ba3e-a44ca20f716f | -9.4087 | -66.5438 | 2024-10-08 01:46:00 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 94.0 |
| e004695d-f912-3080-b517-0670982aa94e | -9.445 | -66.7289 | 2024-10-08 01:46:00 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 65.7 |
| 5075176b-e056-3f31-990d-2b63fc7a1585 | -9.4635 | -66.7283 | 2024-10-08 01:46:01 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 55.8 |
| 8bc5d7ad-200b-39b5-9366-0d158f15b8b9 | -10.1261 | -55.2093 | 2024-10-08 01:46:04 | GOES-16 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 65.5 |
| f87472cf-a528-3b8e-8593-9adba6b01e93 | -10.1263 | -55.1891 | 2024-10-08 01:46:04 | GOES-16 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 69.4 |
| 2232a4fc-8d78-3d00-8e4b-a6f2bd15466b | -10.1448 | -55.2078 | 2024-10-08 01:46:04 | GOES-16 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 112.6 |
| 2a76bfe0-a6a6-3302-8767-cdfc2bc9b9f8 | -10.1451 | -55.1876 | 2024-10-08 01:46:04 | GOES-16 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 143.2 |
| 8fe1f36e-0119-304a-a442-03eddeb9440a | -10.6256 | -55.9154 | 2024-10-08 01:46:07 | GOES-16 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 93.9 |
| 0e5c2b8a-f286-319c-9953-7678071a3a98 | -10.8754 | -63.9169 | 2024-10-08 01:46:08 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 89.6 |
| e9e61f0f-eb27-3430-b994-874dcfe600f3 | -10.8755 | -63.8979 | 2024-10-08 01:46:08 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 84.8 |
| 163f3ec2-0504-308c-9c53-8b234054e5d5 | -11.2479 | -51.3071 | 2024-10-08 01:46:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 85.2 |
| 727ac0ef-5b9d-3624-873d-53b4e2fc72e7 | -11.2482 | -51.2859 | 2024-10-08 01:46:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 105.2 |
| b8e3a865-c140-3652-9ce3-7855ea94fb8b | -13.3824 | -61.9683 | 2024-10-08 01:46:10 | METOP-B | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 212c5708-5f00-3037-9a88-35302fe08b28 | -11.5233 | -65.137 | 2024-10-08 01:46:12 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 72.1 |
| 602a0409-8255-3e9c-852b-f6ceeb84fae1 | -11.6806 | -64.0312 | 2024-10-08 01:46:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 70.5 |
| 024c0ba5-9de2-3170-8912-e2f37af1cdd5 | -11.6808 | -64.0121 | 2024-10-08 01:46:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 68.3 |
| 1db488e4-e1cd-3d25-b3e0-607d1e206191 | -12.3616 | -47.0986 | 2024-10-08 01:46:16 | GOES-16 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 53.7 |
| 3db20b0b-022e-3b99-9262-8216a43c8a15 | -12.1913 | -63.6628 | 2024-10-08 01:46:16 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 44.6 |
| 7d6ffa5a-4043-39d4-9822-316bf3fb977f | -12.9844 | -62.649601 | 2024-10-08 01:46:19 | METOP-B | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 157eebd0-ec2e-36f9-8a9c-b3f33874bf7f | -12.9784 | -62.667999 | 2024-10-08 01:46:19 | METOP-B | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| ab1891c9-3356-3f6b-a003-2408e73f1e2a | -12.9877 | -62.707901 | 2024-10-08 01:46:19 | METOP-B | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 8475d906-c368-34c1-9a92-cac6566adb5f | -12.9895 | -62.7159 | 2024-10-08 01:46:19 | METOP-B | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 54d0c2e0-1bde-35a1-963e-7b23e1c433f7 | -12.9951 | -62.739799 | 2024-10-08 01:46:19 | METOP-B | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| f197bfb4-fa21-3244-907f-c905c7588405 | -12.7453 | -62.070301 | 2024-10-08 01:46:20 | METOP-B | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| e3c50fa1-c5f2-342e-b3b1-397ca09f3481 | -12.822 | -62.440701 | 2024-10-08 01:46:20 | METOP-B | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| de34feac-8f63-333f-bc2f-454535b340ab | -12.8239 | -62.448898 | 2024-10-08 01:46:20 | METOP-B | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 075727d0-ad47-3606-95bf-8bdc4fe45028 | -12.8258 | -62.4571 | 2024-10-08 01:46:20 | METOP-B | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| be31a794-8925-39cc-a824-f5d85782b08a | -12.8141 | -62.451302 | 2024-10-08 01:46:21 | METOP-B | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| d8cb81bc-9f93-3d05-9a91-4a81890f41f0 | -12.7461 | -62.2491 | 2024-10-08 01:46:21 | METOP-B | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 1a0327cc-1960-378e-896c-769b1feda3ea | -12.748 | -62.257401 | 2024-10-08 01:46:21 | METOP-B | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 1a3cdc73-7ba4-3ecc-a3f1-9baeed06a52f | -12.8717 | -62.786301 | 2024-10-08 01:46:21 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 7040afae-f543-3dd4-ad8c-88bf920d4db5 | -12.8424 | -62.793301 | 2024-10-08 01:46:21 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 247cbf74-a313-3d7b-aa14-7f8debfd1c74 | -12.6982 | -62.928001 | 2024-10-08 01:46:24 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 835ae3df-13c6-3838-872d-fc5084763012 | -12.7018 | -62.943699 | 2024-10-08 01:46:24 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 01dca06e-ce0a-3412-b9f9-a898d72cf493 | -12.7036 | -62.9515 | 2024-10-08 01:46:24 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 7ea5655e-fbc7-3422-a1cd-50f95b7f7c3d | -12.6884 | -62.930401 | 2024-10-08 01:46:24 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| d1a52c95-3959-3ff6-b2f0-e5b3735780f5 | -12.6902 | -62.938202 | 2024-10-08 01:46:24 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| f0100a62-8766-3dea-bf17-e3d8883e6585 | -12.692 | -62.946098 | 2024-10-08 01:46:24 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 36a55d8f-0c72-311e-ab72-a423840892c4 | -12.6938 | -62.953899 | 2024-10-08 01:46:24 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 3c1a00db-8585-365b-b481-47f013509cd5 | -12.6702 | -63.074699 | 2024-10-08 01:46:25 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 3e801af5-eea1-3edf-ae10-fbee37310d76 | -12.672 | -63.082401 | 2024-10-08 01:46:25 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| f407ac62-2fae-31a2-b805-03048c73632d | -12.6409 | -63.081699 | 2024-10-08 01:46:26 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 3e364d97-c8cd-39d3-83e1-75ba8d05445a | -12.6311 | -63.084099 | 2024-10-08 01:46:26 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| e85388ae-fa57-3080-b79d-0a42c5366a6d | -12.4439 | -62.988998 | 2024-10-08 01:46:29 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 47860849-ee9c-3be6-88b1-a540c575112b | -12.4457 | -62.996899 | 2024-10-08 01:46:29 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| aa85bb6c-afea-345f-8289-706b10069d57 | -12.4475 | -63.0047 | 2024-10-08 01:46:29 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 406146c2-6a51-3170-bef8-c187c344b96a | -12.4493 | -63.012501 | 2024-10-08 01:46:29 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 54a9cd65-fb7c-352e-9129-2c0ee449c246 | -12.4396 | -63.0149 | 2024-10-08 01:46:29 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| e2eb8755-234c-3fb0-953d-25de0689d26a | -11.4857 | -59.0849 | 2024-10-08 01:46:29 | METOP-B | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| c0661c81-c666-37c9-945d-fa23cdf82922 | -11.476 | -59.087299 | 2024-10-08 01:46:29 | METOP-B | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 5b35df5f-b1d4-370f-a04d-3e356c4a6315 | -10.6125 | -55.890701 | 2024-10-08 01:46:30 | METOP-B | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b6e51122-909c-3984-ac9f-ba53804a065b | -10.6183 | -55.9132 | 2024-10-08 01:46:30 | METOP-B | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f356b45e-db96-3340-93c9-c3f97936afe7 | -10.6029 | -55.893299 | 2024-10-08 01:46:30 | METOP-B | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5e63ef56-f3cf-37fe-8e02-96fff832f0f8 | -10.127 | -55.173199 | 2024-10-08 01:46:35 | METOP-B | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| cf73bfa8-e772-30c0-a85b-c601eec06bc9 | -10.1107 | -55.150101 | 2024-10-08 01:46:35 | METOP-B | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0ccbf7e0-9ae7-327b-9e0e-bcb93da262d0 | -10.1174 | -55.1758 | 2024-10-08 01:46:35 | METOP-B | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7b77ffdb-a9c3-395b-9090-784d7fe2485b | -10.1241 | -55.201401 | 2024-10-08 01:46:35 | METOP-B | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 09b59a95-0679-3090-abe5-db61c9ea620b | -12.1948 | -63.653099 | 2024-10-08 01:46:35 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| f6c94519-bef9-33ed-a8bf-04520a9eb2ff | -12.1965 | -63.660599 | 2024-10-08 01:46:35 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README23.md)
