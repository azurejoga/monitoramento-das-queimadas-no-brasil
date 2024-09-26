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

## Dados Diários - Página 111

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ac2e7d64-77f8-3b3a-8266-46e0dc50ac31 | -8.15883 | -61.52474 | 2024-09-26 04:57:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a921b85b-175d-37e1-b44f-aa9067769806 | -8.14962 | -61.28492 | 2024-09-26 04:57:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 99c955ae-44ab-38d7-b592-738c3c8a2cef | -8.14803 | -61.29393 | 2024-09-26 04:57:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 33969756-ead9-32cc-99e3-95e927a1ae5f | -8.14723 | -61.29845 | 2024-09-26 04:57:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cbbc9a70-4d82-30eb-aeeb-e4b31df0a6a7 | -8.14434 | -61.28865 | 2024-09-26 04:57:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 9b929cc1-62f1-33f3-ba46-b871ab2bfa50 | -8.13294 | -61.28848 | 2024-09-26 04:57:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e6e58b38-eb82-3b89-82a0-5e0debdf8b27 | -8.0835 | -61.28007 | 2024-09-26 04:57:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 49142dbd-cc65-3a0d-85d6-3ca029803b28 | -3.02785 | -61.67613 | 2024-09-26 04:57:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6fc5e392-aeb9-3573-97e7-4555fc1af074 | -3.02282 | -61.67537 | 2024-09-26 04:57:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4f5b788b-c2ae-3f78-bfa5-773bbd2f3dd3 | -3.02234 | -61.67825 | 2024-09-26 04:57:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8322d610-d29a-3180-9324-1b6bfad48afa | -3.02185 | -61.68116 | 2024-09-26 04:57:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9df01ff4-7758-3f9b-8747-0d76a326ab8b | -3.02137 | -61.68407 | 2024-09-26 04:57:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4d2dfa0f-2e50-322c-afca-1150abaafb61 | -3.02089 | -61.68699 | 2024-09-26 04:57:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| df0617ef-58e7-3b3b-b198-464c865ab64b | -3.01683 | -61.68032 | 2024-09-26 04:57:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8d53b5fb-7499-3dc6-b686-089d109eeaba | -3.01635 | -61.68324 | 2024-09-26 04:57:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cbb9e734-f273-3eda-a9d6-be65b3d51515 | -3.01586 | -61.68614 | 2024-09-26 04:57:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b4c35d52-2430-330b-ab5a-724133654e27 | -7.95622 | -62.94484 | 2024-09-26 04:57:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6258792c-bba5-3681-955a-57722629c92b | -7.95576 | -62.94286 | 2024-09-26 04:57:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 90482190-0dc1-3ec3-b597-87af2f1a3b59 | -7.52538 | -63.4623 | 2024-09-26 04:57:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 868198e7-006f-3d84-b7bc-25e50f6c7408 | -7.52496 | -63.46284 | 2024-09-26 04:57:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e3f21772-7871-333c-95ac-bff63c0e0960 | -7.5248 | -63.46555 | 2024-09-26 04:57:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 584f616d-f94e-3711-89de-c2e6b060f657 | -7.52436 | -63.4661 | 2024-09-26 04:57:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 65172c91-32d0-38c6-bf3f-a4ef533a1464 | -7.50812 | -63.6442 | 2024-09-26 04:57:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ad1ab72d-5171-37cb-b1be-9450bd298b0a | -7.05881 | -62.94745 | 2024-09-26 04:57:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9fa20499-9001-3284-94ba-98b1af8cd4b5 | -7.05369 | -62.94655 | 2024-09-26 04:57:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c337c93c-d350-393c-982b-969e7e3812bb | -7.03158 | -62.95217 | 2024-09-26 04:57:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e404d721-2cb0-3b8c-bf49-d33b015e8f53 | -7.03104 | -62.95524 | 2024-09-26 04:57:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 11b6227b-504e-3e16-88d8-670d14142cc5 | -7.0305 | -62.95833 | 2024-09-26 04:57:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7ab52eb7-d0bf-37c1-9fe4-9db07b699d26 | -7.02591 | -62.95436 | 2024-09-26 04:57:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8b966b4b-f6b5-3b55-867a-72ed5a63b978 | -6.99954 | -62.92454 | 2024-09-26 04:57:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 70f11d7f-1746-3f40-97eb-3d4390e3404a | -6.96617 | -62.91927 | 2024-09-26 04:57:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ca288958-2f96-3b1b-a681-7802a8cf882c | -6.96564 | -62.92231 | 2024-09-26 04:57:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0ef57d44-30a1-37a8-8246-dd9842311f77 | -6.96511 | -62.92536 | 2024-09-26 04:57:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 60a59968-e797-324a-9181-548ad10e2d9d | -6.96458 | -62.92842 | 2024-09-26 04:57:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ea20578a-781c-31b8-805e-45e54c8bfbc7 | -6.96106 | -62.91833 | 2024-09-26 04:57:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a947634e-11fd-3f31-8378-ca3cabe4cf63 | -6.96053 | -62.92139 | 2024-09-26 04:57:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dac73556-e046-3eb4-93dd-4d510a8c4732 | -6.95999 | -62.92444 | 2024-09-26 04:57:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fb3692de-1e58-3257-9702-dea3ac6ac65e | -6.95946 | -62.92751 | 2024-09-26 04:57:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b4d540d5-b952-3516-9035-826f2d04adc7 | -6.9403 | -63.10603 | 2024-09-26 04:57:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b963f031-0462-3820-ba7f-a051bba82372 | -6.93973 | -63.10917 | 2024-09-26 04:57:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6f982da1-cd63-3240-985b-1668f10af454 | -6.93916 | -63.11231 | 2024-09-26 04:57:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f5cc495e-8c17-367b-874d-d70d49c0b3bd | -6.93845 | -63.10967 | 2024-09-26 04:57:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 207cbf65-128a-39fc-a7fe-168054c02402 | -6.9379 | -63.11282 | 2024-09-26 04:57:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 9766c53d-f41b-347e-a9a9-a6b3510e1710 | -6.60172 | -62.96571 | 2024-09-26 04:57:00 | NOAA-21 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8e8e1154-3d17-39e9-9a0c-4bfcc6eba178 | -6.60117 | -62.96884 | 2024-09-26 04:57:00 | NOAA-21 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b070b59a-ff24-38ff-bf2b-53ce0af32366 | -14.56497 | -45.67923 | 2024-09-26 04:59:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 31c67d2b-3272-33aa-8391-70f383e0a0eb | -14.56359 | -45.67142 | 2024-09-26 04:59:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 51954c61-47f8-3402-8136-86532f710699 | -14.56313 | -45.67538 | 2024-09-26 04:59:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0746d2cc-ab77-33e9-9dbf-fba283c57548 | -14.56267 | -45.67933 | 2024-09-26 04:59:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 23327c1b-5c87-3cd0-9d50-2e33cbd8ffa6 | -14.55972 | -45.6744 | 2024-09-26 04:59:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 82cb8cf7-9f43-3efa-901a-c452ccff360d | -14.5103 | -45.63124 | 2024-09-26 04:59:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 71f9779d-476f-3316-8732-3d66eab11b14 | -9.56282 | -66.01542 | 2024-09-26 04:59:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 20c004cc-9c07-3b2d-ace2-28e829f16987 | -9.55768 | -66.00977 | 2024-09-26 04:59:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 79a886e1-d39e-3c09-b537-5c8195693a4a | -10.39644 | -67.86954 | 2024-09-26 04:59:00 | NOAA-21 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0e0deb7c-81de-3cbd-86fd-2c8686809f79 | -10.39526 | -67.87538 | 2024-09-26 04:59:00 | NOAA-21 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 02fe2610-998e-3cd2-8e36-30ed86be9c65 | -10.39171 | -67.87012 | 2024-09-26 04:59:00 | NOAA-21 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 9dc58a8b-063a-3f12-9a98-38694198dfff | -10.39057 | -67.87595 | 2024-09-26 04:59:00 | NOAA-21 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 6ce8723f-2da1-3bc4-955c-d3059acb2ec4 | -10.38983 | -67.86836 | 2024-09-26 04:59:00 | NOAA-21 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 75fce0af-efd1-3ab3-90f1-ded9e399a8bd | -10.38865 | -67.8742 | 2024-09-26 04:59:00 | NOAA-21 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bae57bfe-b455-3c7a-bfb5-e552c196954d | -16.75552 | -42.4724 | 2024-09-26 04:59:00 | NOAA-21 | BERILO | MINAS GERAIS | Brasil | 3106507 | 31 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 36832b17-a957-397f-8aa4-fd50d8fe8b26 | -16.75278 | -42.4695 | 2024-09-26 04:59:00 | NOAA-21 | VIRGEM DA LAPA | MINAS GERAIS | Brasil | 3171600 | 31 | 33 | nan | nan | nan | Cerrado | 5.2 |
| f33032d0-bde7-329a-b86b-db49fabd4fd6 | -13.53713 | -42.55901 | 2024-09-26 04:59:00 | NOAA-21 | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 71790efc-3226-3d8e-a6da-eb53d4af7473 | -13.53642 | -42.56553 | 2024-09-26 04:59:00 | NOAA-21 | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 9bc10a9b-f2a7-30a8-8662-0594052ecc03 | -13.53173 | -42.56242 | 2024-09-26 04:59:00 | NOAA-21 | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | 3.2 |
| ec54269e-1ae9-3631-b191-08cda1d78195 | -11.85073 | -43.826 | 2024-09-26 04:59:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f3f52135-f378-3a0b-ba87-bb02e58e8416 | -11.84511 | -43.82029 | 2024-09-26 04:59:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 1ce58caf-1b3e-3c0b-99fe-5ad3332cb0fc | -11.84454 | -43.82514 | 2024-09-26 04:59:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 849f8d93-fbe3-39a2-a785-6342c5e7909b | -11.6768 | -44.50682 | 2024-09-26 04:59:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e4b01548-ca40-3658-b7be-65d95a48e2e2 | -11.67628 | -44.5112 | 2024-09-26 04:59:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 596821bb-3968-373b-96a8-35c32235c847 | -14.44563 | -45.25822 | 2024-09-26 04:59:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c54ac6e0-57ae-30ac-afb8-dafec73b1f8a | -14.43976 | -45.25774 | 2024-09-26 04:59:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 882061bd-abbd-35d7-ab5b-0ee0074858bc | -14.41163 | -45.29839 | 2024-09-26 04:59:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9a71b399-d5a5-35f8-b6b9-3ed5352550ee | -16.32832 | -45.67162 | 2024-09-26 04:59:00 | NOAA-21 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 70b039d1-b92a-381d-a7f7-aacd7d95985e | -16.32787 | -45.67586 | 2024-09-26 04:59:00 | NOAA-21 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 36013bdd-6560-38ae-8f94-950c7a9f8c03 | -16.32205 | -45.67514 | 2024-09-26 04:59:00 | NOAA-21 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 95ff3ccf-be99-3089-867b-c4a417b5498d | -12.23508 | -45.50433 | 2024-09-26 04:59:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 4894aaae-efcd-3ea9-b046-a740484e5b65 | -12.2342 | -45.49839 | 2024-09-26 04:59:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 120d4132-059b-320d-8eea-c3ecb3a77f33 | -12.23375 | -45.50224 | 2024-09-26 04:59:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| aefe465d-11dc-3b28-bd9b-b10fe6708fea | -12.2333 | -45.50609 | 2024-09-26 04:59:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 21cef6ec-db41-38ac-8a77-930988d00013 | -12.23044 | -45.49586 | 2024-09-26 04:59:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 1e44a9ef-7bbc-3ecb-a456-d21031207418 | -12.22996 | -45.49973 | 2024-09-26 04:59:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 07bf240c-a87a-3f92-af7a-8ff3133886c6 | -12.22949 | -45.50359 | 2024-09-26 04:59:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 9e09c5e1-5ec3-3e49-ab2a-a6ee355eec57 | -12.22861 | -45.49759 | 2024-09-26 04:59:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 6.5 |
| a55859e7-cfa3-39e6-a7d1-0dc8e36a17c2 | -12.22816 | -45.50147 | 2024-09-26 04:59:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 8fa7aa2d-d02f-3885-b16d-3af0bb112a7e | -12.22771 | -45.50533 | 2024-09-26 04:59:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| b67e9a94-6cbc-3a50-9cbb-49803aadd626 | -12.2276 | -45.51892 | 2024-09-26 04:59:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 4b3ef963-1149-3261-a713-76a2faa0bf5c | -12.22713 | -45.52272 | 2024-09-26 04:59:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| bc755066-feee-35cf-a20c-5fd5b0ff46c7 | -12.22666 | -45.52654 | 2024-09-26 04:59:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 32.9 |
| ddbb7f0e-d481-337c-8cdf-3859836eb02b | -12.22638 | -45.51685 | 2024-09-26 04:59:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 4465d82c-c220-3cdf-99d1-9b4409faebd8 | -12.22618 | -45.53035 | 2024-09-26 04:59:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 32.9 |
| f22a8fc6-0901-3529-907a-0dc146e9947c | -12.22594 | -45.52066 | 2024-09-26 04:59:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 11.6 |
| a19c3e99-f3d0-345b-95bb-b94c923d6e3c | -12.22505 | -45.52832 | 2024-09-26 04:59:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 82.6 |
| f152bf2d-779e-31f1-8276-fab13074b48d | -12.22461 | -45.53214 | 2024-09-26 04:59:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 21.7 |
| cdabc58b-9c0e-3daf-a1f6-a02c27dd7f2e | -12.22437 | -45.49899 | 2024-09-26 04:59:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 60ff41c5-85af-31f3-a1c4-d98a7ab7ccb5 | -12.2239 | -45.50285 | 2024-09-26 04:59:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 13.0 |
| dc7e5895-f0fa-3247-959a-f9c92fd92474 | -12.22257 | -45.50072 | 2024-09-26 04:59:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| a6e4cd57-8ebe-38ad-9f6d-4a76e5014402 | -12.22212 | -45.50457 | 2024-09-26 04:59:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 11b10301-a4fe-3a46-8084-4761765fb320 | -12.22202 | -45.51811 | 2024-09-26 04:59:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 31.5 |
| f77bf05c-5e2b-3aed-9ba4-dfb4a9e62c3a | -12.22155 | -45.52193 | 2024-09-26 04:59:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 31.5 |
| 11d37e83-7f82-3811-8dc0-35ff3cc621b5 | -12.22108 | -45.52578 | 2024-09-26 04:59:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 72.1 |


[Clique aqui para ver as próximas entradas](README112.md)
