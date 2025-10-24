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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6f212291-1d8a-3dfd-a320-2d77be7a6287 | -2.482 | -49.2297 | 2025-10-24 00:50:00 | GOES-19 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 47.5 |
| 2856d690-bb3c-35f8-b718-2400dc344f82 | -3.2433 | -52.9095 | 2025-10-24 00:50:00 | GOES-19 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 56.7 |
| 957cb233-1f14-33be-b6ad-abb5e38bd9ef | -6.7842 | -38.5673 | 2025-10-24 00:50:00 | GOES-19 | SANTA HELENA | PARAÍBA | Brasil | 2513307 | 25 | 33 | nan | nan | nan | Caatinga | 82.9 |
| c466fe81-c780-33db-9d61-3b30e5cdd01f | -4.2942 | -40.7 | 2025-10-24 00:50:00 | GOES-19 | IPU | CEARÁ | Brasil | 2305803 | 23 | 33 | nan | nan | nan | Caatinga | 72.3 |
| 4c94b43a-80f1-343b-9a4c-24319093c863 | -3.2617 | -52.909 | 2025-10-24 00:50:00 | GOES-19 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 55.3 |
| ba50033a-c60d-34d6-b88d-95e033a90cef | -7.5497 | -47.3766 | 2025-10-24 00:50:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 84.0 |
| e3cd07a8-b8f5-3029-8c6c-ca59726f6416 | -2.4265 | -49.2736 | 2025-10-24 00:50:00 | GOES-19 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 83.1 |
| 15fe6da8-7ff0-33a7-a42c-2c17ca6dd218 | -7.5499 | -47.3546 | 2025-10-24 00:50:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 82.8 |
| 941b159b-4ac1-34c5-8851-7467f347b1eb | -14.3083 | -49.0599 | 2025-10-24 00:50:00 | GOES-19 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 187.6 |
| d75d810f-0d4f-36fd-9b38-57b441d929ff | -6.3127 | -41.8727 | 2025-10-24 00:50:00 | GOES-19 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 68.0 |
| efa0620e-d38c-3df5-b60e-55ecea9db83b | -15.1939 | -49.4083 | 2025-10-24 00:50:00 | GOES-19 | SANTA ISABEL | GOIÁS | Brasil | 5219357 | 52 | 33 | nan | nan | nan | Cerrado | 79.9 |
| 6c5d728a-e39f-3f24-93db-8d819dbe42de | -4.2754 | -40.7012 | 2025-10-24 00:50:00 | GOES-19 | IPU | CEARÁ | Brasil | 2305803 | 23 | 33 | nan | nan | nan | Caatinga | 103.7 |
| 2b4abc73-ebb5-32f6-b0d5-c7cc10a64203 | -14.3079 | -49.082 | 2025-10-24 00:50:00 | GOES-19 | CAMPINORTE | GOIÁS | Brasil | 5204706 | 52 | 33 | nan | nan | nan | Cerrado | 155.1 |
| d56164a0-7d63-3f7f-928e-a63ae1335e3a | -16.9563 | -53.2104 | 2025-10-24 00:50:00 | GOES-19 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 60.7 |
| 3f8d4ede-61dc-3daf-a5a5-b5f759b36d65 | -16.9559 | -53.2318 | 2025-10-24 00:50:00 | GOES-19 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 56.9 |
| 0e023cde-d084-3633-a5ef-820d510ee585 | -2.4264 | -49.2948 | 2025-10-24 00:50:00 | GOES-19 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 26.2 |
| 3a516a15-fa23-3c2e-85d7-1326ec59a74c | -14.3277 | -49.0569 | 2025-10-24 00:50:00 | GOES-19 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 70.6 |
| 4c46f303-d0b0-3ca7-8558-104d69adfa7c | -4.2942 | -40.7 | 2025-10-24 01:00:00 | GOES-19 | IPU | CEARÁ | Brasil | 2305803 | 23 | 33 | nan | nan | nan | Caatinga | 62.4 |
| 6bedf1d5-3c44-354c-8ffe-9827701d0f96 | -3.2617 | -52.909 | 2025-10-24 01:00:00 | GOES-19 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 73.2 |
| 0f8a0d18-6548-3595-b990-a7eb774163a4 | -17.5967 | -46.6182 | 2025-10-24 01:00:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 59.7 |
| 465af66d-856a-318e-9b09-005493a16569 | -2.482 | -49.2297 | 2025-10-24 01:00:00 | GOES-19 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 41.5 |
| 174f7cf2-c707-3b5d-b546-60258d037755 | -15.1939 | -49.4083 | 2025-10-24 01:00:00 | GOES-19 | SANTA ISABEL | GOIÁS | Brasil | 5219357 | 52 | 33 | nan | nan | nan | Cerrado | 90.0 |
| a060fbcf-d71a-3e6d-96cd-603a61c994dc | -2.4265 | -49.2736 | 2025-10-24 01:00:00 | GOES-19 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 104.9 |
| f31c852d-ba43-3b06-9c7b-358ad5849241 | -7.5499 | -47.3546 | 2025-10-24 01:00:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 77.5 |
| 9513c1bd-2e06-3434-bb46-1c50eb6927a5 | -15.1744 | -49.4114 | 2025-10-24 01:00:00 | GOES-19 | SANTA ISABEL | GOIÁS | Brasil | 5219357 | 52 | 33 | nan | nan | nan | Cerrado | 55.2 |
| f9f4d7f4-bb12-3ef2-9cf9-5df04ece73fd | -7.5497 | -47.3766 | 2025-10-24 01:00:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 93.5 |
| 95cb2cd5-a6a7-3323-8418-62aa77fb577c | -7.5499 | -47.3546 | 2025-10-24 01:10:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 84.6 |
| 317d4cfb-af30-3c48-bb7a-a0c7ce46a4ba | -3.2617 | -52.909 | 2025-10-24 01:10:00 | GOES-19 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 63.1 |
| 8cf3898a-c46a-34f7-bb2c-3ab25db186a9 | -2.482 | -49.2297 | 2025-10-24 01:10:00 | GOES-19 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 46.9 |
| e18ea196-0e93-380e-b032-150516081cd8 | -2.4265 | -49.2736 | 2025-10-24 01:10:00 | GOES-19 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 67.7 |
| d0cc32ec-c2fd-38dd-930a-b74d3b42e58c | -7.5497 | -47.3766 | 2025-10-24 01:10:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 82.8 |
| 3b93cdb4-e9f3-3ea1-bc89-8500f5d7c834 | -15.1939 | -49.4083 | 2025-10-24 01:10:00 | GOES-19 | SANTA ISABEL | GOIÁS | Brasil | 5219357 | 52 | 33 | nan | nan | nan | Cerrado | 67.4 |
| 1df785d8-78a3-3e3d-9ca3-42a3e9aa32ad | -15.1939 | -49.4083 | 2025-10-24 01:20:00 | GOES-19 | SANTA ISABEL | GOIÁS | Brasil | 5219357 | 52 | 33 | nan | nan | nan | Cerrado | 56.2 |
| bfac3d2c-05a7-3747-9480-c3141722314a | -7.5499 | -47.3546 | 2025-10-24 01:20:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 78.3 |
| 407cc079-3124-3dd1-8306-66fe1a5cdea8 | -3.2617 | -52.909 | 2025-10-24 01:20:00 | GOES-19 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 51.1 |
| c2530c2d-de95-3606-b5d1-40ccea524352 | -7.5497 | -47.3766 | 2025-10-24 01:20:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 70.0 |
| 6bc4b6c9-2552-34d5-86a3-e77e942b552a | -11.0526 | -45.399 | 2025-10-24 01:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 63.8 |
| 3965aea7-e70b-32af-b86f-b21f132b20fe | -2.4265 | -49.2736 | 2025-10-24 01:20:00 | GOES-19 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 53.8 |
| 4893dc53-598c-305c-9032-af4c6899effa | -8.6526 | -44.7771 | 2025-10-24 01:20:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 76.6 |
| 4b240097-385b-37d4-8d64-e5438fcc1c76 | -20.64808 | -55.08727 | 2025-10-24 01:28:00 | TERRA_M-M | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 22.8 |
| 191216c1-b45c-3bd1-b5c9-dfefc640d428 | -2.482 | -49.2297 | 2025-10-24 01:30:00 | GOES-19 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 47.4 |
| 042c9b8e-b961-3c94-9e67-8aa2b6f7d13c | -12.8136 | -50.9576 | 2025-10-24 01:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 40.2 |
| 9ff01ca8-533c-3c59-81ae-510f83f1fa67 | -7.5497 | -47.3766 | 2025-10-24 01:30:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 74.7 |
| 35c2b81f-497e-3ae5-b518-bc81f9f478a9 | -15.1939 | -49.4083 | 2025-10-24 01:30:00 | GOES-19 | SANTA ISABEL | GOIÁS | Brasil | 5219357 | 52 | 33 | nan | nan | nan | Cerrado | 65.8 |
| f7a08dec-3692-3a44-b986-e660f25d1a4c | -2.4265 | -49.2736 | 2025-10-24 01:30:00 | GOES-19 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 36.9 |
| a27d226d-5f42-3846-8523-1fb642f693f2 | -7.5499 | -47.3546 | 2025-10-24 01:30:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 64.2 |
| e66734f0-02f7-37f1-bc16-73f310005d8c | -16.94939 | -53.22265 | 2025-10-24 01:30:00 | TERRA_M-M | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 68.1 |
| 2d812765-d7c1-39c1-8646-9aaae8bca9b8 | -17.32387 | -55.02655 | 2025-10-24 01:30:00 | TERRA_M-M | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 38.9 |
| 449e0c48-f1d2-3e03-ae46-e98150d65e64 | -16.94514 | -53.21672 | 2025-10-24 01:30:00 | TERRA_M-M | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 33.5 |
| 86d75e47-51ef-3dd7-bbf3-152d1e7fda48 | -17.32786 | -55.04898 | 2025-10-24 01:30:00 | TERRA_M-M | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 18.8 |
| 732dd403-993f-3fbc-9229-aab7a5217890 | -12.2326 | -60.32847 | 2025-10-24 01:32:00 | TERRA_M-M | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 2a9d7dfc-d498-34e5-a0c7-e6d47bd4ab43 | -10.91151 | -62.02275 | 2025-10-24 01:32:00 | TERRA_M-M | JI-PARANÁ | RONDÔNIA | Brasil | 1100122 | 11 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 48d9414c-9fe9-3484-8763-3674174de738 | -10.06481 | -63.53007 | 2025-10-24 01:32:00 | TERRA_M-M | MONTE NEGRO | RONDÔNIA | Brasil | 1101401 | 11 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 2b2fd269-f38a-3ca1-8ad1-db9c199ddcab | -11.78491 | -63.18039 | 2025-10-24 01:32:00 | TERRA_M-M | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 99b06e83-5875-3c3a-b590-efdc0c59d37f | -9.11824 | -65.36117 | 2025-10-24 01:32:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| b5998c6e-c6fc-3b18-9bae-2be91fe5560e | -9.10921 | -65.36243 | 2025-10-24 01:32:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 6.2 |
| fb23bd09-e2fe-3aee-a297-46e7c1612aaf | -10.96801 | -62.42056 | 2025-10-24 01:32:00 | TERRA_M-M | TEIXEIRÓPOLIS | RONDÔNIA | Brasil | 1101559 | 11 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 402dc057-6318-3570-839d-826f9e5f7510 | -2.482 | -49.2297 | 2025-10-24 01:40:00 | GOES-19 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 41.4 |
| 5ee98e1c-4572-30f7-8b73-bb2b586a89b1 | -9.6061 | -46.9099 | 2025-10-24 01:40:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 119.7 |
| f6edf3a1-1efb-3aaa-b44d-516ff74ce6d5 | -2.2647 | -47.84 | 2025-10-24 01:40:00 | GOES-19 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 29.3 |
| e222a961-6978-37b9-b7f9-10698d850c34 | -3.2617 | -52.909 | 2025-10-24 01:40:00 | GOES-19 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 55.9 |
| 68163f0f-f362-3724-90e0-e292de7195d5 | -7.5499 | -47.3546 | 2025-10-24 01:40:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 76.1 |
| a3ffe1ff-0405-32e2-ad5a-8e7b99d3d526 | -11.3682 | -45.9265 | 2025-10-24 01:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 58.9 |
| 030c46db-6e45-3a12-9e74-eff18d22139d | -12.2597 | -47.4487 | 2025-10-24 01:40:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 58.4 |
| d6631a29-0fd7-399e-9373-641f890433c9 | -9.6064 | -46.8876 | 2025-10-24 01:40:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 100.2 |
| 460c6d78-a12f-3e80-8e66-7a56ee74b0a7 | -7.5497 | -47.3766 | 2025-10-24 01:40:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 76.2 |
| 8d94e773-7f82-3ca2-98c4-7daa9f2ad8b3 | -9.6061 | -46.9099 | 2025-10-24 01:50:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 224.7 |
| 76d66b69-8d60-3a21-bfff-1904fe823b4c | -9.625 | -46.9078 | 2025-10-24 01:50:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 69.4 |
| 0ba174fb-3ef3-3cde-9051-879dddc494ab | -7.5499 | -47.3546 | 2025-10-24 01:50:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 74.8 |
| ce40bd81-7d9c-39b8-b17d-678caf7fee33 | -7.5497 | -47.3766 | 2025-10-24 01:50:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 66.3 |
| fd458e5e-78da-356c-9c25-73fbd57bb853 | -9.6064 | -46.8876 | 2025-10-24 01:50:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 116.5 |
| 060bf2fa-1e6e-3c7e-983c-8516d2e2453c | -11.3682 | -45.9265 | 2025-10-24 02:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 77.8 |
| 0d63342c-86b6-3a60-930e-910fc390110f | -9.625 | -46.9078 | 2025-10-24 02:00:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 71.8 |
| 0625274a-655d-3111-878d-c9be7e493e2d | -9.6061 | -46.9099 | 2025-10-24 02:00:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 184.2 |
| 69856a72-9123-3b86-a71e-8eacf059b112 | -11.3678 | -45.9493 | 2025-10-24 02:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 61.9 |
| f13463cc-5a97-3d2d-8d44-3e35e1a30f86 | -7.5499 | -47.3546 | 2025-10-24 02:00:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 73.1 |
| d1e65ddb-7f26-3716-ac46-0e75f9d35c0a | -7.5497 | -47.3766 | 2025-10-24 02:00:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 65.9 |
| 787f6133-f0de-3192-8c58-03ff716e0973 | -11.3678 | -45.9493 | 2025-10-24 02:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 75.1 |
| 8f865f98-2372-3c2e-a5b9-ff305c4ea621 | -2.8149 | -49.1354 | 2025-10-24 02:10:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 51.1 |
| 0b1cabb1-a3d2-3e9f-8f08-7934f3e66036 | -11.3682 | -45.9265 | 2025-10-24 02:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 138.7 |
| f5c61709-f22b-3dfe-9614-b0377a0ff754 | -5.4551 | -45.4214 | 2025-10-24 02:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 63.3 |
| 518412c7-313c-3d3c-b967-447db3d11ee2 | -11.0526 | -45.399 | 2025-10-24 02:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 60.7 |
| 7a87b4cf-9fb8-3bcb-b4a8-f0e43c2a478a | -7.5499 | -47.3546 | 2025-10-24 02:10:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 65.3 |
| 1bc4f274-5b8d-33f6-b1c5-9070799a0f51 | -9.6061 | -46.9099 | 2025-10-24 02:10:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 141.7 |
| bbe73ec8-e220-3a68-913f-ceb571faae31 | -9.625 | -46.9078 | 2025-10-24 02:10:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 69.0 |
| 35433de7-f3b7-3b0c-ad16-5df9aeb9253e | -9.6061 | -46.9099 | 2025-10-24 02:20:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 110.3 |
| 8611dc09-d4a6-3d73-b3ab-edfc509f0776 | -11.3682 | -45.9265 | 2025-10-24 02:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 87.5 |
| aec27154-155e-3440-88c7-637893fadcfe | -3.2617 | -52.909 | 2025-10-24 02:20:00 | GOES-19 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 47.5 |
| d3953e50-ccbd-3db4-8b56-81e7869963f2 | -2.8149 | -49.1354 | 2025-10-24 02:20:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 47.6 |
| fc66eb79-c099-3113-a19f-883af9f8e6e8 | -11.3678 | -45.9493 | 2025-10-24 02:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 67.8 |
| 422d2f47-3161-3cd1-bb8f-29452bd566a1 | -7.5497 | -47.3766 | 2025-10-24 02:20:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 77.3 |
| 60b44bb8-4fb6-3c24-a73b-c2b14083447b | -9.6061 | -46.9099 | 2025-10-24 02:30:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 75.6 |
| 1415c634-2158-3b0a-985c-7869b880b230 | -7.5497 | -47.3766 | 2025-10-24 02:30:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 79.8 |
| 8657da02-3298-377c-8c6f-99d495223269 | -11.3682 | -45.9265 | 2025-10-24 02:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 77.6 |
| d281b43b-1f75-389a-8295-60f52448eee1 | -5.4551 | -45.4214 | 2025-10-24 02:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 63.8 |
| 6cca1703-94e4-3ec7-9350-86681a90306d | -11.3678 | -45.9493 | 2025-10-24 02:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 120.1 |
| b84139aa-772f-3c05-9488-80253abeb8bb | -2.8149 | -49.1354 | 2025-10-24 02:40:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 47.7 |
| d3c89706-bdff-3396-a337-bbc1abbf6bfc | -9.6061 | -46.9099 | 2025-10-24 02:50:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 83.3 |
| f59e1a2f-1b30-3e4d-9fdc-a744af19bfcb | -2.8149 | -49.1354 | 2025-10-24 02:50:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 46.0 |
| b1c59908-3948-346e-886a-798d30d64329 | -6.9293 | -44.0048 | 2025-10-24 02:50:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 38.5 |


[Clique aqui para ver as próximas entradas](README3.md)
