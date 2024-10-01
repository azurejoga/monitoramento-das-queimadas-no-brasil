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

## Dados Diários - Página 136

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 57859aec-a924-3f65-82c0-0fc3bae8c3c1 | -9.74775 | -66.58984 | 2024-10-01 05:29:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6003e00f-c722-35a5-a5c3-3fd36422f2f3 | -9.74762 | -65.95808 | 2024-10-01 05:29:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fb3e42c6-8e53-3191-b660-2ec5212f0764 | -9.74701 | -66.59435 | 2024-10-01 05:29:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0867ecfa-0508-3c05-b027-d46d4b6e0db4 | -9.70442 | -66.85095 | 2024-10-01 05:29:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dab1e6e3-dd7e-3572-9cb4-d494a0a59d3e | -9.70062 | -66.85031 | 2024-10-01 05:29:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a800745d-cad4-3376-a7d3-7cba8139c470 | -9.69985 | -66.85496 | 2024-10-01 05:29:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 29529b3d-8c10-3b34-ad70-8ef28d3ad906 | -9.64878 | -65.74217 | 2024-10-01 05:29:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e3ea55e5-be15-33d2-ad78-5a8df483343c | -9.62906 | -67.44276 | 2024-10-01 05:29:00 | NPP-375D | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 64807810-eb7c-32e7-a5b7-5e8574de9910 | -9.61268 | -67.16275 | 2024-10-01 05:29:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2e49ed07-ec22-3f97-bcd2-5a52855dc9a2 | -9.61186 | -67.16759 | 2024-10-01 05:29:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 17449f9b-2e1e-32d7-803e-67f5bfaa8999 | -9.59722 | -53.2717 | 2024-10-01 05:29:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6adce07f-d878-3ba2-96be-3cd1ca818905 | -9.59661 | -53.27256 | 2024-10-01 05:29:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 96622ee1-69d8-3928-8ad7-330df1b6247b | -9.59173 | -53.271 | 2024-10-01 05:29:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7d98343d-02e9-373c-b01a-87ae136dcac0 | -9.59112 | -66.18205 | 2024-10-01 05:29:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9e2f553d-e777-355e-89cf-8d6c83d916b7 | -9.59111 | -53.27186 | 2024-10-01 05:29:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 132f2ff2-3a51-3277-9279-0f5c09a9b67b | -9.57628 | -66.64658 | 2024-10-01 05:29:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 57bef9c8-4413-3d9d-9940-c474d9ae110f | -9.51766 | -68.57843 | 2024-10-01 05:29:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6b72c753-d155-3899-b222-07a090186cba | -9.51698 | -68.58241 | 2024-10-01 05:29:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a670fa5f-a85d-35a7-926d-100e8c79d6f5 | -9.50782 | -68.58492 | 2024-10-01 05:29:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f321224b-a7cc-3ebf-9556-8f6aeacfa4e0 | -9.42592 | -68.75305 | 2024-10-01 05:29:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4af741e6-1b10-3a58-9b48-7671ca9127ed | -9.37084 | -68.77798 | 2024-10-01 05:29:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ffab70de-9b9a-3d21-bfba-820e4b9ad837 | -9.34724 | -68.8377 | 2024-10-01 05:29:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f17c8156-1871-3371-9d8c-3e9513bad97b | -9.32242 | -66.54411 | 2024-10-01 05:29:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b880b953-738f-3a21-9620-b37804fdc8c5 | -9.32065 | -68.76057 | 2024-10-01 05:29:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c6f1932c-0f82-3460-9117-c5db3e4cb644 | -9.31868 | -66.54346 | 2024-10-01 05:29:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 71330a4a-53b2-3ec4-a73e-d62dd2667458 | -9.3006 | -68.74853 | 2024-10-01 05:29:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c3665d0e-1d51-302a-a38c-7615018a0860 | -9.29987 | -68.75263 | 2024-10-01 05:29:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b7e50345-8276-335c-b450-feab9f3a2414 | -9.27138 | -67.60712 | 2024-10-01 05:29:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7ac0f526-cabd-3d42-93ab-56f24d740ecb | -9.27053 | -67.60569 | 2024-10-01 05:29:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 40ad6bee-482e-3623-9008-532e59b961c8 | -9.27047 | -67.61234 | 2024-10-01 05:29:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9b68e561-5af9-37ee-8a84-2a2c4ce53e39 | -9.26966 | -67.61092 | 2024-10-01 05:29:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d54c8cce-a4ea-353e-97d7-a352f3a57065 | -9.26738 | -67.60643 | 2024-10-01 05:29:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 548479f6-c2c8-3a84-a1b4-3c6407348e87 | -9.26654 | -67.605 | 2024-10-01 05:29:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3f2cc8b6-5ce5-377c-b96e-314acc719b5e | -9.2047 | -68.30889 | 2024-10-01 05:29:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b816b40f-2319-3f4c-8bd6-0fbbd4d1f555 | -9.20051 | -68.30816 | 2024-10-01 05:29:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3b9d131f-7b7a-3dfc-9051-5b78b5419810 | -9.1956 | -68.78231 | 2024-10-01 05:29:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9f4f1025-ca04-3a39-a56f-2b4b76c73513 | -9.0792 | -67.38284 | 2024-10-01 05:29:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f4cf8a67-d65a-3efd-9a9b-891972657692 | -9.04136 | -68.50358 | 2024-10-01 05:29:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| cc48202b-8ee5-3692-a3ed-ea3332a4631f | -9.03711 | -68.50282 | 2024-10-01 05:29:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3c22c28e-27e0-3363-9dde-60eba6dcdde0 | -9.03642 | -68.5068 | 2024-10-01 05:29:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 14001245-98a1-3151-90c0-4c99c5fa81d7 | -8.79305 | -69.02682 | 2024-10-01 05:29:00 | NPP-375D | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 39665e47-6c28-3659-8f1a-10119da0b6ce | -8.79197 | -69.02433 | 2024-10-01 05:29:00 | NPP-375D | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8588a5c5-1103-314b-ada9-09e1f9df432a | -8.7912 | -69.02866 | 2024-10-01 05:29:00 | NPP-375D | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4b629855-5e99-3cf3-bf58-fa2526707db6 | -7.92935 | -61.55527 | 2024-10-01 05:29:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a464362f-d86c-35ab-b3ca-5368df7684eb | -7.926 | -61.55474 | 2024-10-01 05:29:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5ae1b296-9909-3fc2-8e3f-d88a6bcd5f62 | -7.90026 | -61.52176 | 2024-10-01 05:29:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 0698706e-8958-38d1-9574-b0015a5255e2 | -13.63327 | -51.17461 | 2024-10-01 05:29:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 7.1 |
| fedc49b9-750b-39af-84f1-6b0ac9b137b6 | -13.64241 | -51.15244 | 2024-10-01 05:29:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 8.8 |
| bf711817-da4b-36c7-b424-fba130007a63 | -13.64177 | -51.15816 | 2024-10-01 05:29:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 8.8 |
| a1d1640c-b8bd-39c6-8d33-f4e6c168b11b | -13.64034 | -51.15381 | 2024-10-01 05:29:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 14.9 |
| bfaa1802-3a33-3e2b-8877-1208b60191a4 | -13.63974 | -51.15954 | 2024-10-01 05:29:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 19.5 |
| 8d570e34-5732-33b7-9d16-42e5c318ea39 | -13.6358 | -51.15168 | 2024-10-01 05:29:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |
| e480e1ac-2d92-362a-877c-fe58aacdf76e | -13.63517 | -51.15741 | 2024-10-01 05:29:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 08173727-fbe2-3d14-ba69-f0d564f0c97f | -13.63454 | -51.16313 | 2024-10-01 05:29:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 0bd4665b-f1a2-34db-82aa-82761cbcc701 | -13.6339 | -51.16888 | 2024-10-01 05:29:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 7.5 |
| dae1822c-4923-3d04-b1bc-e7dfe80ed78c | -13.63313 | -51.15876 | 2024-10-01 05:29:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| de8800bc-0a07-33a6-b883-45916bd12c93 | -13.63254 | -51.16449 | 2024-10-01 05:29:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 7188a5ed-15a9-379c-b076-d900b8334083 | -13.63194 | -51.17024 | 2024-10-01 05:29:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 048af105-c2e5-388e-8c82-1386796d3091 | -13.63135 | -51.17596 | 2024-10-01 05:29:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 6.3 |
| edce1128-16c8-3ec9-a9d7-be5f22c6944c | -13.63046 | -51.13945 | 2024-10-01 05:29:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 04cebf22-b208-3be0-ae09-e3c91ab26900 | -13.62983 | -51.14518 | 2024-10-01 05:29:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6eec32bc-0f4c-35d7-9906-cf999ec4740f | -13.6289 | -51.09269 | 2024-10-01 05:29:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5b0971d6-a677-3f65-abaf-9fda962cbd5c | -13.62831 | -51.14074 | 2024-10-01 05:29:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 9.3 |
| d8607c03-9c9c-3a9f-b176-7fba6d205741 | -13.62827 | -51.09845 | 2024-10-01 05:29:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9c0d8542-d603-3016-8c65-fbcb8da44896 | -13.62772 | -51.14648 | 2024-10-01 05:29:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 59f01fe0-9b1e-3ce3-9aab-64220f81f9c6 | -13.62385 | -51.13869 | 2024-10-01 05:29:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| e5a03471-5284-3411-b26d-791032427c16 | -13.62322 | -51.14442 | 2024-10-01 05:29:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| b81723ea-170e-35a0-821f-1a4ff1a7abfb | -13.6217 | -51.13995 | 2024-10-01 05:29:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| dd5984ca-ec03-36f4-8fe8-6ba017073f7f | -13.62111 | -51.1457 | 2024-10-01 05:29:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9a3731f5-e874-30e1-a108-350f43d9a71a | -13.60489 | -51.06641 | 2024-10-01 05:29:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 806a1eae-6e8d-337c-a6a7-26c4e388614e | -13.59825 | -51.06565 | 2024-10-01 05:29:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| cc3c6529-4e4b-3f7d-a4a0-94e38eac8781 | -13.59492 | -51.15862 | 2024-10-01 05:29:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c5acd231-a6a3-32c1-963e-afb60af39aa6 | -13.58894 | -51.1521 | 2024-10-01 05:29:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| cd6592f1-150f-3742-b750-e3fb1d878956 | -13.58833 | -51.15782 | 2024-10-01 05:29:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c3163d35-1d50-3e76-8912-3eecc52bf422 | -13.58173 | -51.15702 | 2024-10-01 05:29:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 7.0 |
| a05a760f-9ec5-3f27-b20c-7fc80bf43d1e | -13.41685 | -61.92833 | 2024-10-01 05:29:00 | NPP-375D | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ca6633ab-399a-36a8-8e46-d640d29d3c90 | -13.23369 | -51.23009 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2e4f6e02-fd07-36f9-9200-b958530ec48b | -13.23305 | -51.23565 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4bd7c5b0-e348-3df2-825c-0087a2cbcf97 | -13.22817 | -51.21321 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1314aa1b-0a7a-3c51-ad21-cb5612561fbb | -13.22714 | -51.22935 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3939e803-2a29-3e60-a864-cb2e45a2d71c | -13.2225 | -51.21183 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 16.3 |
| ef370650-b0ac-35ca-b862-cef652cc7a0c | -13.22223 | -51.20674 | 2024-10-01 05:29:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 30fb376c-6da4-38bb-83f2-2411d02b1ced | -13.22187 | -51.21741 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 18.5 |
| 77b89a89-c189-3852-a701-c78591adb6cf | -13.22162 | -51.21245 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 15.5 |
| a35d4c50-1572-3e15-861a-109a0294eebc | -13.22102 | -51.21803 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 76a978ff-40ed-3249-aba3-d43e9ff1a646 | -13.21659 | -51.20538 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 52c435af-812c-327c-8603-ec1e97c25b71 | -13.21595 | -51.21106 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 771a41aa-9ae9-3b55-b999-80aed05167d4 | -13.21567 | -51.20595 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 1bd48319-11e8-39db-9df1-b338351400a7 | -13.21532 | -51.21666 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 18.5 |
| 55945455-a81b-3d5b-bbbb-749f94e1b0f2 | -13.21507 | -51.21164 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 9850e27a-4a11-3881-b98c-e82f3c2791d7 | -13.21447 | -51.21725 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 8b2a153b-2a1c-3a8d-b5b1-2a501f44031a | -13.2094 | -51.21027 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 41f374b8-a97b-3530-80f1-a613c92d133d | -13.20877 | -51.21586 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7a778f5c-4c56-30e0-847d-dd4194fde378 | -13.20852 | -51.21084 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 06ade31d-2934-36d6-9ed0-79eaefea47b4 | -13.20223 | -51.21507 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 576a507b-a55a-3833-83cd-d47d31b74fb2 | -13.20138 | -51.21561 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 612f70a6-8bdb-3c2e-969c-2364fb4eb4b0 | -13.06878 | -51.17647 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a4c9289a-1a1c-3c7c-90cf-58c08cd62992 | -13.06816 | -51.18207 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 69.9 |
| 124952f4-d9d9-3e7d-8233-609031c832df | -13.06754 | -51.18766 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 69.9 |
| 377c79a1-871b-3703-8de9-2e24f937afd2 | -13.06692 | -51.19326 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 75.2 |


[Clique aqui para ver as próximas entradas](README137.md)
