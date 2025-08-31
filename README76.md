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
| 2f0ff75f-83ec-3fb6-a333-a022ce366d31 | -9.06244 | -65.42383 | 2025-08-31 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6c73221d-0c0a-350d-a794-06ffafb1409c | -10.72845 | -65.04594 | 2025-08-31 05:44:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6c349aa6-190a-3558-aeea-3686cbcf5faf | -7.9505 | -63.3288 | 2025-08-31 05:44:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 850bee03-0b3a-33a2-b7a8-63e695889cac | -10.2451 | -54.97798 | 2025-08-31 05:44:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 25219ab3-00bb-3813-8f9e-6b055bbe7870 | -9.4721 | -60.32022 | 2025-08-31 05:44:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8c7defcf-7ca9-37b6-8d29-6f839cdd92ea | -9.46453 | -62.34252 | 2025-08-31 05:44:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 5cbf7987-1a65-346c-89fa-88c559daece1 | -9.45816 | -62.36006 | 2025-08-31 05:44:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 42114101-4ee6-3366-9789-be44d84a7b41 | -8.74356 | -64.08337 | 2025-08-31 05:44:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 01756e98-0ec2-36f2-b592-251eb5017f23 | -8.10003 | -71.24742 | 2025-08-31 05:44:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f9f788b9-8826-3479-93f8-abd571eea70c | -9.44959 | -62.34034 | 2025-08-31 05:44:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 37783637-4207-32fc-a996-c5b64c2f1c1a | -9.89851 | -67.0136 | 2025-08-31 05:44:00 | NOAA-21 | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3edcb001-de02-32a9-8443-4918c93b1558 | -8.74895 | -62.37516 | 2025-08-31 05:44:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 869fbefa-5cd2-3ad7-8e45-f57a81d92d3c | -9.4426 | -62.36227 | 2025-08-31 05:44:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 193f25e7-db2a-33e0-8a52-390d50e5da14 | -9.44763 | -62.35384 | 2025-08-31 05:44:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b5bce658-b675-3720-aa4c-52603a4af324 | -15.21451 | -56.0584 | 2025-08-31 05:44:00 | NOAA-21 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fd6976c6-eef3-3395-87b6-45cb559a1e82 | -8.74641 | -62.39283 | 2025-08-31 05:44:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2f619fa1-51e2-3093-803b-9d31d9325c6e | -9.46839 | -60.31568 | 2025-08-31 05:44:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5065a724-01ae-3796-bf31-03d498d070d2 | -7.6805 | -61.09491 | 2025-08-31 05:44:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b93407bf-27e8-30f9-ab08-9fa0736669a7 | -11.3197 | -63.2615 | 2025-08-31 05:44:00 | NOAA-21 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 966f2dcb-249b-316b-b58f-6a94750f6f61 | -8.56999 | -63.0129 | 2025-08-31 05:44:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c4ec1d4a-dd23-3cf9-80c9-72f25df9f084 | -8.73903 | -62.3917 | 2025-08-31 05:44:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1f94d8b4-8257-3172-bff2-36b6fd56d5bf | -8.68309 | -66.93269 | 2025-08-31 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a0a73c54-5c68-3ba2-8e03-729504c0de07 | -10.31882 | -59.19759 | 2025-08-31 05:44:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| f5cbe951-00a7-3804-b9f9-f13bf0f0267d | -8.56462 | -63.02462 | 2025-08-31 05:44:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9a457752-375e-3870-a641-a9f36eb6b83a | -8.66444 | -70.03845 | 2025-08-31 05:44:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 80f7fee2-7bb2-3864-86c0-e204a0c2523f | -12.2257 | -64.22426 | 2025-08-31 05:44:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9d66e35d-0dde-392e-91fd-af2e01e83177 | -9.38984 | -68.22637 | 2025-08-31 05:44:00 | NOAA-21 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 88497076-b49b-3e00-a9b9-8796543152ca | -9.71311 | -62.39604 | 2025-08-31 05:44:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| dd1f3e94-147c-32c8-b43a-05be138971ca | -9.11623 | -61.20278 | 2025-08-31 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 77b9bb9e-a036-3994-894e-d9919155f34e | -9.4411 | -60.53745 | 2025-08-31 05:44:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4d6c95cc-aa1b-36ce-94e2-0b86717e8dfa | -7.90067 | -63.01364 | 2025-08-31 05:44:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2cd9fb45-6918-31aa-b44c-6ce3dd5549df | -9.66132 | -66.25105 | 2025-08-31 05:44:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dfda30a1-e1eb-3ddd-a168-fd5aa1e0cb7c | -9.44639 | -60.57199 | 2025-08-31 05:44:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 11880a69-f995-3063-a420-fcb5c36df157 | -9.45527 | -60.56934 | 2025-08-31 05:44:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| eff3e33a-8d5e-3b24-9442-218f330be823 | -14.80419 | -59.72388 | 2025-08-31 05:44:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 9af0e633-8f5e-3e03-9dad-cf9bbc256a0d | -8.38561 | -70.83525 | 2025-08-31 05:44:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 45cbd1a0-ea23-3dc8-bddd-85b4db56c267 | -8.85145 | -70.62393 | 2025-08-31 05:44:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6d1ea743-bb50-3fe6-a912-7ad203330317 | -9.45706 | -62.34144 | 2025-08-31 05:44:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 10.1 |
| ad1e295e-87f5-3ec2-9f1d-ef9fdaa4a14c | -10.32411 | -59.19338 | 2025-08-31 05:44:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| acf400f0-ff52-355e-8f3f-e1e34d06699b | -6.91829 | -71.74703 | 2025-08-31 05:44:00 | NOAA-21 | IPIXUNA | AMAZONAS | Brasil | 1301803 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b803e39c-4c84-385a-bb6b-9563f3bc6071 | -9.20422 | -62.38083 | 2025-08-31 05:44:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9400eead-e320-300a-9b70-710a8f9f3aa0 | -7.50189 | -63.50672 | 2025-08-31 05:44:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cdf31ed1-ac02-3aa0-a2be-78437996b697 | -8.72783 | -64.16465 | 2025-08-31 05:44:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 90937ae9-4196-3f70-bf36-d5634a0796c6 | -9.4358 | -62.35663 | 2025-08-31 05:44:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6288d963-22d6-3c03-b9e8-5a7181625959 | -9.45736 | -60.5541 | 2025-08-31 05:44:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fff74acb-7f77-3158-8325-2cecb365ad91 | -10.3129 | -59.20658 | 2025-08-31 05:44:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fff8261c-395a-3fde-bf25-bd3f5dedb1a7 | -12.92284 | -56.98415 | 2025-08-31 05:44:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 377083be-3e3e-3a36-8c5b-c5e3f5df4bb4 | -12.05659 | -64.79687 | 2025-08-31 05:44:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 08322a5e-fbe0-3231-831e-4965ac7c321f | -8.97655 | -70.7431 | 2025-08-31 05:44:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 646a3e64-7bc2-3ced-a939-0fd24c03bc8b | -8.69099 | -62.87795 | 2025-08-31 05:44:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 22a34b31-7ce9-3b00-8717-04aeebc9259b | -7.91248 | -63.00723 | 2025-08-31 05:44:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 338b04a7-6488-3fd0-a682-962b7bdbe8d4 | -9.06684 | -65.41734 | 2025-08-31 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 508a1757-4565-3faa-bc07-6ad2d9a504bf | -8.74272 | -62.39227 | 2025-08-31 05:44:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 65a21190-fc4a-316d-8a3b-4b550e494355 | -15.23095 | -56.07881 | 2025-08-31 05:44:00 | NOAA-21 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 16b698d0-f024-3aa7-a0c2-a8a2d89b621c | -9.44535 | -60.57961 | 2025-08-31 05:44:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fd1e5265-27b1-3dfb-810b-5bc95f80fa64 | -15.21418 | -56.05479 | 2025-08-31 05:44:00 | NOAA-21 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 469b6d96-220a-3c28-b181-03d2444452ed | -11.38745 | -63.28053 | 2025-08-31 05:44:00 | NOAA-21 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 46d14ebc-9cc2-3a92-a230-381b99ef330f | -9.06738 | -65.41384 | 2025-08-31 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d205fd0f-2f70-3fbd-8624-4248b1edd13e | -9.07524 | -65.45094 | 2025-08-31 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 73cb48db-7636-358f-aaa2-a3deff736231 | -8.23369 | -72.81434 | 2025-08-31 05:44:00 | NOAA-21 | PORTO WALTER | ACRE | Brasil | 1200393 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 571ad01d-de18-3117-9900-b08e059f8a95 | -9.44148 | -62.34367 | 2025-08-31 05:44:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f67eea5b-f2ff-315a-bded-a2fd8209ee98 | -7.91483 | -63.01582 | 2025-08-31 05:44:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ac4e3648-6a98-3ad0-b0e3-4b5fdd0de485 | -8.74258 | -62.39909 | 2025-08-31 05:44:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 81028225-80a4-3532-ae91-a0995e374097 | -11.32474 | -63.27286 | 2025-08-31 05:44:00 | NOAA-21 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d2013568-9fd2-366b-abb2-796aa0be8aa4 | -9.00411 | -63.62715 | 2025-08-31 05:44:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d05fd5cc-0972-3bff-8303-3fa927163d86 | -13.01723 | -56.90717 | 2025-08-31 05:44:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3c336fd2-16b4-3a9b-8bad-79ba1efd02c2 | -8.34317 | -62.93069 | 2025-08-31 05:44:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8a47dcb4-6fc1-3c44-aa74-b42393fca346 | -8.01829 | -69.88061 | 2025-08-31 05:44:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6d19c128-4900-350d-a50b-8177b7608c3f | -9.07069 | -65.41436 | 2025-08-31 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ef611b07-a86b-3e2c-962d-3cb1d8984729 | -13.01959 | -56.88765 | 2025-08-31 05:44:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7c1cccd2-9dca-3408-9fb1-b7e6e8a79b07 | -10.31419 | -59.19691 | 2025-08-31 05:44:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 8c53bdab-7635-3cf4-af31-4edf1c779e31 | -9.4509 | -62.3313 | 2025-08-31 05:44:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f3b67197-b348-37d6-a4f2-ba6c915cb0c3 | -7.9231 | -63.00885 | 2025-08-31 05:44:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 19.1 |
| 3d6d2560-1773-3f09-8d92-376c14eb6390 | -9.56204 | -66.68886 | 2025-08-31 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 71686c2c-3b95-3734-a2d9-e4334d135e88 | -9.06799 | -65.43188 | 2025-08-31 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 84925aa0-5c61-38a8-a4d6-957400e59ed1 | -8.34674 | -62.93122 | 2025-08-31 05:44:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9aabf533-e783-30d1-8813-94e97f8ff598 | -9.4494 | -62.3679 | 2025-08-31 05:44:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 50f39360-0cf0-3dd4-abaf-4241e08aa029 | -8.85271 | -64.14919 | 2025-08-31 05:44:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1b03e74f-16e3-3928-ba89-886e2e067526 | -8.92209 | -62.42237 | 2025-08-31 05:44:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 94ecfdf5-efe1-3d0c-8bef-f4396ad133b8 | -8.64468 | -62.83014 | 2025-08-31 05:44:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ac9017cf-05d7-363e-84ea-d5c8c915be57 | -8.51396 | -70.00815 | 2025-08-31 05:44:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 481662e8-7a4b-3ad9-af59-7afe0994c838 | -11.28482 | -63.26686 | 2025-08-31 05:44:00 | NOAA-21 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 33276dc8-fa5e-331b-b14f-961d9b313da8 | -9.00469 | -63.62325 | 2025-08-31 05:44:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c8f3691a-2eff-3ab1-a215-5169174ad045 | -10.7555 | -59.81816 | 2025-08-31 05:44:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8652d88a-479f-3436-9c1a-02d906def44a | -11.31909 | -63.26578 | 2025-08-31 05:44:00 | NOAA-21 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| f8ed924d-c592-358e-87ef-f6432951a362 | -13.02674 | -56.90606 | 2025-08-31 05:44:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4b4fb81f-6eaa-375d-86e1-0f177f06f1fd | -11.32663 | -63.26005 | 2025-08-31 05:44:00 | NOAA-21 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d5101170-7184-3336-9d4c-a26424c5aa01 | -9.44225 | -60.54003 | 2025-08-31 05:44:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6dc2c479-dfbf-3e93-a709-5a914d505dbc | -8.65548 | -62.83178 | 2025-08-31 05:44:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 9dcffc2b-60f6-3cac-bd55-3fbdbb27a7fb | -9.44642 | -60.54068 | 2025-08-31 05:44:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3e9cabad-5d12-3448-8733-151d0e59ba06 | -9.44014 | -60.55548 | 2025-08-31 05:44:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3c81fa1a-f265-3e2e-a06e-79c0ffd4808f | -9.44055 | -60.5413 | 2025-08-31 05:44:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8513913b-2627-3ba3-9462-a3fc906118a4 | -14.31361 | -60.3496 | 2025-08-31 05:44:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 1f46ffc2-25c2-36a2-90ec-7e47a867abfc | -9.07185 | -65.42889 | 2025-08-31 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0cbc6f11-1d22-3a31-8815-9c90aa591159 | -13.02286 | -56.90778 | 2025-08-31 05:44:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 49827adf-11c7-396e-be64-7a9ab6d1a491 | -9.11326 | -61.19524 | 2025-08-31 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d29fa2ea-79d3-34d5-b01e-afc0f00ba4c2 | -9.44274 | -60.5676 | 2025-08-31 05:44:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bd659f26-f914-3f82-a67c-c417055b16e9 | -9.44743 | -60.56441 | 2025-08-31 05:44:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 05c730ba-a01a-34d0-8592-6d836d50e5cb | -8.7501 | -62.39338 | 2025-08-31 05:44:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 20908b39-0a7e-3df4-ab75-8d032249a64c | -10.31947 | -59.19277 | 2025-08-31 05:44:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |


[Clique aqui para ver as próximas entradas](README77.md)
