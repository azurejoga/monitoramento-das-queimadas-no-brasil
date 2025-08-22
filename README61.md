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

## Dados Diários - Página 61

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ae424868-1824-3389-a033-96d412321e38 | -4.10027 | -60.66293 | 2025-08-22 05:59:00 | NOAA-20 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ac17efa2-95e2-356e-91aa-900f086a3283 | -6.89749 | -59.89228 | 2025-08-22 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ca4d15f2-ec9d-3192-9aa2-28b2cafdd2d6 | -7.56041 | -63.85463 | 2025-08-22 05:59:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 99e70733-6c99-3dc4-b3f4-4354413ec5a7 | -7.50603 | -63.83133 | 2025-08-22 05:59:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 111f607d-806e-3624-961f-3f16265e6412 | -7.59009 | -63.44279 | 2025-08-22 05:59:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| b0eaf97a-e591-3786-b6a2-20e43a1bf7a6 | -7.54701 | -63.85271 | 2025-08-22 05:59:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 00d751d7-7188-38d9-b932-6bc1d3932776 | -6.62731 | -58.54633 | 2025-08-22 05:59:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e4196bca-f34b-3dc8-a704-197ef137b226 | -6.57302 | -59.87977 | 2025-08-22 05:59:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 40690646-50f2-352c-a51d-5d2a08bee66b | -6.90226 | -59.89867 | 2025-08-22 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| de175624-eb52-3738-9367-16f2bb13889d | -7.09015 | -63.08404 | 2025-08-22 05:59:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ca05e67d-28a6-3f8f-9e09-993b80bcb8ff | -7.29955 | -59.6304 | 2025-08-22 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 358c4551-8566-3c76-b31b-364dafe92e12 | -7.55594 | -63.85399 | 2025-08-22 05:59:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b9884b56-8eec-31be-b864-6b4ea145c2ad | -7.30012 | -59.62614 | 2025-08-22 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 1d5e8669-a882-3225-8ff1-7d24f7bfc34c | -5.43596 | -60.16438 | 2025-08-22 05:59:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 744a3fb3-5e7b-37ff-8e51-1bf4afe8e0e3 | -7.29422 | -59.62522 | 2025-08-22 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4ec09651-56cb-3b65-b517-ad6fdb4ff960 | -7.84354 | -61.72743 | 2025-08-22 05:59:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8954e455-3b01-32b0-ac3f-e9f31734c6dd | -7.06004 | -59.82831 | 2025-08-22 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 913fa584-790e-3da7-b60c-401c88fe59ac | -7.55916 | -63.86346 | 2025-08-22 05:59:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0cf03e81-839c-3039-b079-04765e482f62 | -7.58615 | -63.4374 | 2025-08-22 05:59:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 29aa656a-6ca7-3c95-9b49-f83f62ded1e5 | -7.30603 | -59.62708 | 2025-08-22 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 80324f23-c2ec-34f0-b1d1-849a4568e5fa | -7.93205 | -63.04463 | 2025-08-22 05:59:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dab76a57-d533-33a5-90b9-ef4f0a068d8a | -7.44047 | -60.6278 | 2025-08-22 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 150e40c5-45d1-32e3-82f8-d4a93bbacb95 | -6.57401 | -59.87952 | 2025-08-22 05:59:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 766751a5-e24c-33f0-8ffa-caf10756c2d5 | -5.80657 | -59.2267 | 2025-08-22 05:59:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 60fa307c-4832-30f8-a40a-6ffeb3990b16 | -7.84397 | -61.72426 | 2025-08-22 05:59:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 728971ea-7ab4-3c73-8558-8c140d4b36ce | -6.8965 | -59.89775 | 2025-08-22 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8d7fb5d2-2783-3f2d-984c-45b346a97882 | -7.83878 | -61.72354 | 2025-08-22 05:59:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 262cdc48-ae1d-3b43-8d14-3412d8e0080b | -7.84312 | -61.73057 | 2025-08-22 05:59:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3c1192fc-d906-3e13-a015-40c6dfbef424 | -5.80471 | -59.22121 | 2025-08-22 05:59:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ca63d110-25bf-31b1-88f1-714dfacb2b63 | -5.44153 | -60.16516 | 2025-08-22 05:59:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 880034cb-d69b-3cd7-b50a-d474361f4729 | -6.57456 | -59.87537 | 2025-08-22 05:59:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 316ae782-5183-37f2-9e64-23c64038b5ef | -15.8955 | -43.4523 | 2025-08-22 06:00:00 | GOES-19 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 91.6 |
| 5567a17e-33f6-38d4-a0bb-9a13e6b37cc7 | -8.86012 | -62.39725 | 2025-08-22 06:01:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ddf5d6b1-23f1-333f-ab30-0b3561a6e763 | -9.22495 | -59.76857 | 2025-08-22 06:01:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 89b45dc2-ebf9-3ecf-a5b3-838fd5e49835 | -8.62651 | -62.6126 | 2025-08-22 06:01:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7f7ac558-6d48-3ecb-8c1a-67ea638abf4a | -8.60521 | -62.62109 | 2025-08-22 06:01:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 94ed0cb1-b7f8-397c-bedb-6c1671bfe7c5 | -8.86701 | -62.42189 | 2025-08-22 06:01:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2ffc1a03-45cc-3867-acc9-6cfe1facaf3a | -8.86319 | -62.4124 | 2025-08-22 06:01:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 98623909-e6e6-3a64-8b24-8e2d65cdc9e0 | -8.04354 | -70.19068 | 2025-08-22 06:01:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6765853f-7a80-3649-b78d-a3ed5ad56cc0 | -9.50643 | -60.51689 | 2025-08-22 06:01:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 832839c7-5f56-3600-94a5-8b635fe82709 | -8.26388 | -70.19309 | 2025-08-22 06:01:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fd96c30d-6b84-367b-9fb5-04da531cabce | -8.14744 | -70.50208 | 2025-08-22 06:01:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 111547b5-2ca7-3c9f-a07b-459624bdf502 | -9.91028 | -62.14174 | 2025-08-22 06:01:00 | NOAA-20 | VALE DO ANARI | RONDÔNIA | Brasil | 1101757 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e4eae54b-35f5-3f24-8bfe-7d78cdcb942b | -9.09603 | -61.43403 | 2025-08-22 06:01:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d7a8b774-7732-3397-860a-85cc9a713755 | -9.20986 | -59.44852 | 2025-08-22 06:01:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c26bc21e-7563-37c2-803d-6961dfb8349d | -9.21004 | -60.78511 | 2025-08-22 06:01:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0d2c6ad1-edc6-320c-8778-1047c7d80fb2 | -9.2086 | -59.45808 | 2025-08-22 06:01:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| be2ae358-8aba-309d-9394-37351ab25bd0 | -8.88631 | -62.43047 | 2025-08-22 06:01:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b268ac47-4753-3d39-b150-e1c71430b7f8 | -9.21331 | -59.47124 | 2025-08-22 06:01:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2b15a205-4ed1-3a8c-8a4d-cee60289dc42 | -8.62574 | -62.6182 | 2025-08-22 06:01:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9c941c01-3267-3aa7-ac06-2dc3d19e9b94 | -8.87284 | -62.41671 | 2025-08-22 06:01:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 802340e4-bc01-32e8-bcb4-c08e6b241406 | -9.18616 | -59.6386 | 2025-08-22 06:01:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e547649c-6bad-3a55-9edb-340c3765bf99 | -8.60104 | -62.61481 | 2025-08-22 06:01:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7b836a38-79ca-3a11-8323-de58479c2d77 | -9.21417 | -60.79723 | 2025-08-22 06:01:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 44f9196d-a3c3-33a4-8d61-7e1bee2f17dd | -8.5488 | -66.95234 | 2025-08-22 06:01:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ed9838d3-faa5-3d95-a3f7-ba065287f0bc | -9.15302 | -59.5979 | 2025-08-22 06:01:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 910b5f29-4ca3-3fc8-b0b7-35adca862506 | -9.16536 | -59.60728 | 2025-08-22 06:01:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6d62aab3-9e38-3f7b-8d69-9716da134365 | -7.71694 | -66.92278 | 2025-08-22 06:01:00 | NOAA-20 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 55d023a4-fbd7-3ad9-8bb5-7f1bd9a246c9 | -8.46735 | -70.08621 | 2025-08-22 06:01:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 65e8cf28-ecd7-3d31-9ae5-3c05882edda0 | -9.20673 | -59.47224 | 2025-08-22 06:01:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6248446e-117e-3397-aa28-f4c7b64d3ab7 | -9.20954 | -60.78893 | 2025-08-22 06:01:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c3790846-fcec-38d6-8ecb-63c09b845e89 | -9.2139 | -59.46656 | 2025-08-22 06:01:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fd2a8b7d-9018-3054-88c6-10c9b69e57b4 | -7.62625 | -69.94976 | 2025-08-22 06:01:00 | NOAA-20 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b38135db-6759-3be5-9f4e-4d2e66f97c91 | -8.6649 | -70.03814 | 2025-08-22 06:01:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f979df64-d70b-33de-9e05-e7f1a3c40182 | -8.87404 | -62.40793 | 2025-08-22 06:01:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b41074f1-68ee-3e2a-81e0-c776795d0bfc | -9.51336 | -60.55443 | 2025-08-22 06:01:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0aa99bef-7230-360a-9fb4-a5417dfaf293 | -9.7531 | -62.77449 | 2025-08-22 06:01:00 | NOAA-20 | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 6c06ada0-f9e1-36ec-a3dd-172eddd731e1 | -8.71423 | -69.46025 | 2025-08-22 06:01:00 | NOAA-20 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 09d57761-9851-38d7-9939-c02cc494e66a | -9.52691 | -60.53997 | 2025-08-22 06:01:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2911aab3-c29d-3eee-9978-3153e54c358b | -9.52064 | -60.54319 | 2025-08-22 06:01:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d13c928d-141a-36b8-8870-4769be29de49 | -9.10143 | -61.4347 | 2025-08-22 06:01:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7b7daa04-26be-3fc4-b53c-5ed743547722 | -9.19218 | -59.63979 | 2025-08-22 06:01:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6835e247-55dc-3b71-a85a-5a7d1b152cd3 | -8.62157 | -62.61193 | 2025-08-22 06:01:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 9.1 |
| da700e51-b6e2-34e8-ad45-b74cb9008b07 | -8.60028 | -62.62038 | 2025-08-22 06:01:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a7924483-b8d7-3f30-a3e0-4961b2f8d2a0 | -9.91133 | -62.14314 | 2025-08-22 06:01:00 | NOAA-20 | VALE DO ANARI | RONDÔNIA | Brasil | 1101757 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7621b38f-e0a1-3a5c-ad3a-d7826691c1b6 | -9.18675 | -59.63389 | 2025-08-22 06:01:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c904cb95-7aea-3966-870b-0bb4f00b8d18 | -9.93251 | -65.00769 | 2025-08-22 06:01:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 76afd9ef-d1a4-30d3-a66a-fc69061561a2 | -7.63011 | -69.94681 | 2025-08-22 06:01:00 | NOAA-20 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7f02be3d-a60e-3db5-9ce9-6fa4320dc0cf | -9.16458 | -59.60412 | 2025-08-22 06:01:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 822acf53-963e-37c7-9819-ecf12a1d86bb | -9.52013 | -60.54721 | 2025-08-22 06:01:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 9d61bc1b-2f3d-36a6-be82-2a7c158fb261 | -9.17852 | -59.5921 | 2025-08-22 06:01:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 27f46100-8160-3adf-9927-0d0e1f7dbe05 | -9.05249 | -67.45978 | 2025-08-22 06:01:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a5ba72fe-fb2a-344d-a39e-29ea42184088 | -14.78748 | -59.67134 | 2025-08-22 06:01:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 3150c49e-be59-3985-ad10-b26a48f530bb | -9.09649 | -61.43056 | 2025-08-22 06:01:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 92de0782-94aa-3dc2-b28a-80cab7c30ddd | -9.15434 | -59.59638 | 2025-08-22 06:01:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c82fc00a-89dc-3ee0-9a00-aeaca01c3e24 | -8.54509 | -66.95178 | 2025-08-22 06:01:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 032e0d2a-bd7a-35ae-bd22-df248310beae | -9.81644 | -64.27258 | 2025-08-22 06:01:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c2d0c5fa-477e-3262-8653-10cd3474419b | -9.20735 | -59.46754 | 2025-08-22 06:01:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| eee44c10-c086-3de1-bf10-5037b7ed3ec4 | -9.52588 | -60.54801 | 2025-08-22 06:01:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 5197cb5f-0c16-3cbf-b7b9-c2b43fd18f3d | -9.22798 | -60.33535 | 2025-08-22 06:01:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 42befc9d-e5e4-37f2-acd0-d4a3c590a15d | -10.38049 | -69.51548 | 2025-08-22 06:01:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fafb981a-ee56-3017-a47b-ebb829e4491d | -8.86821 | -62.41309 | 2025-08-22 06:01:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fc602728-5b5c-3669-be2d-ffc0d00f7bde | -9.95157 | -60.18032 | 2025-08-22 06:01:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 8d76caef-1f70-37b3-b439-4e9f14c8c02a | -9.18952 | -60.7667 | 2025-08-22 06:01:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 63eb7f3e-35c8-3cec-ab16-3f60ea80d7b8 | -9.15242 | -59.60255 | 2025-08-22 06:01:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fb62eeb4-6a39-3d2a-a936-d682a4ea82c4 | -7.77517 | -66.95671 | 2025-08-22 06:01:00 | NOAA-20 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4ea555ca-862f-3f59-a787-5678a9fd06e2 | -9.16593 | -59.60268 | 2025-08-22 06:01:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 119d1220-fed6-39e5-9aa5-81fb29809b43 | -8.89174 | -62.42825 | 2025-08-22 06:01:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cfd25bc1-92bb-3fa6-991b-9a58f0bcfa94 | -8.66448 | -63.85158 | 2025-08-22 06:01:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ba0b891c-382e-30c2-ad73-07edcb6e51d9 | -8.86239 | -62.41827 | 2025-08-22 06:01:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README62.md)
