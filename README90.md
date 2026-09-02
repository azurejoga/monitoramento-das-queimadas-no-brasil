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

## Dados Diários - Página 90

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 57bcd9c0-47f4-336b-82b1-038dcde28446 | -15.3647 | -53.8307 | 2026-09-02 17:00:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 84.9 |
| 0c675db6-0d77-3ddf-a02a-8a0b03733499 | -3.2361 | -61.2359 | 2026-09-02 17:00:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 73.5 |
| 5ba1f6fd-d2e3-3a68-b6f0-7662933b55e5 | -3.1267 | -61.1811 | 2026-09-02 17:00:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 68.7 |
| b6b61fb6-8fc0-3c36-af93-447c07e5ecb0 | -3.1998 | -61.161 | 2026-09-02 17:00:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 59.1 |
| 4c5c62fe-a257-34f7-bc34-0dd92226dd9d | -7.9794 | -44.3193 | 2026-09-02 17:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 55.5 |
| 411e00a8-6160-3996-9f31-cacb04937272 | -3.4185 | -61.3461 | 2026-09-02 17:00:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 55.6 |
| 7c1ffdec-59d9-364e-9614-fdb63b79a684 | -15.2672 | -53.8642 | 2026-09-02 17:00:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 110.6 |
| 7a59ecf2-dd4e-31b8-9640-d56e6401e849 | -14.2989 | -51.7072 | 2026-09-02 17:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 84.8 |
| 1f9d7256-30c7-3424-b170-bc2d81d4f700 | -15.2863 | -53.8827 | 2026-09-02 17:00:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 102.9 |
| 95c6321f-f2a5-3114-a1cb-7e52c41f6762 | -15.2866 | -53.8617 | 2026-09-02 17:00:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 173.5 |
| f05613d1-e7ae-36fd-99de-b6a353a00ca4 | -15.2669 | -53.8851 | 2026-09-02 17:00:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 74.3 |
| 3f35da61-596e-301b-adee-a2659af86289 | -10.1081 | -50.3203 | 2026-09-02 17:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 105.3 |
| 6057b111-dd4e-3ad9-9498-7eb538a5716a | -7.0242 | -59.2374 | 2026-09-02 17:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 133.5 |
| 5636a0dc-cfd4-3f54-942a-4c43a493c96e | -3.4185 | -61.3273 | 2026-09-02 17:00:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 64.4 |
| ea9970c8-e6c8-311b-bdbf-2a1436ce3caf | -3.0347 | -61.4846 | 2026-09-02 17:00:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 141.5 |
| 8a8fe3aa-e63f-3485-ae73-8f0bdd74143e | -7.2933 | -60.5905 | 2026-09-02 17:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 67.6 |
| f6337f3b-64cb-3d20-beab-787d1b85fd3b | -7.2934 | -60.5713 | 2026-09-02 17:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 61.9 |
| 21a5df9b-8e91-3e47-9406-8a14dc80f348 | -1.4761 | -54.2365 | 2026-09-02 17:00:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 61.3 |
| c2c30592-f196-37b0-bd19-84c9d97536d9 | -10.1084 | -50.299 | 2026-09-02 17:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 112.5 |
| efe8f4d1-042c-32f6-a2df-819d0db42ab3 | -3.4002 | -61.3276 | 2026-09-02 17:10:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 72.1 |
| 999cc8f3-311a-3d6f-a4da-3029fde344bd | -14.2989 | -51.7072 | 2026-09-02 17:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 83.0 |
| c7e3e0f2-041f-31dc-9d98-bdd98357de04 | -15.3651 | -53.8097 | 2026-09-02 17:10:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 75.6 |
| 946b19c7-875f-36db-a7d2-6cb772707580 | -3.1266 | -61.2 | 2026-09-02 17:10:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 48.5 |
| 477774c2-a899-3a32-bfde-6060b4c29ef9 | -3.2361 | -61.217 | 2026-09-02 17:10:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 184.7 |
| 43e29bba-efa5-3f5e-afa6-cee18a15419a | -3.4185 | -61.3273 | 2026-09-02 17:10:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 65.4 |
| 797a01fa-c389-3a65-b2dc-a5984030baf8 | -4.2383 | -62.2349 | 2026-09-02 17:10:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 107.4 |
| b9211ab7-6f0d-38b2-af15-1a1ff12f448d | -7.1822 | -60.6713 | 2026-09-02 17:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 61.7 |
| f70b4d7e-b20b-3b27-a12f-9512253419b0 | -15.3647 | -53.8307 | 2026-09-02 17:10:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 85.0 |
| 42850298-e304-3f1b-976a-f1d8ad21498e | -15.3654 | -53.7887 | 2026-09-02 17:10:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 80.4 |
| 542b3647-a962-3ec6-aef5-51d2f2b28c6f | -3.0347 | -61.4657 | 2026-09-02 17:10:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 73.4 |
| 116fd668-51c7-3fbe-8620-dfb3c014ce64 | -3.1083 | -61.238 | 2026-09-02 17:10:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 47.7 |
| ff507648-410c-356e-ac08-a0c09c7797da | -13.4516 | -57.0592 | 2026-09-02 17:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 47.0 |
| 644ec5ac-98b5-34b7-98bc-54518a8ac0ad | -3.0347 | -61.4846 | 2026-09-02 17:10:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 129.5 |
| 1f00ea62-81d7-35fc-b022-48f2bcf3814f | -7.2193 | -60.6316 | 2026-09-02 17:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 57.0 |
| 9a8eb72f-3a37-35f6-9b9f-5c36853d4ab5 | -1.4761 | -54.2365 | 2026-09-02 17:10:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 70.5 |
| ea6e3b45-ee5d-358a-891f-e9ae259c24ce | -6.9872 | -59.2582 | 2026-09-02 17:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 87.9 |
| 6949e0e7-4745-34f1-84a9-f4a4b372f746 | -3.1267 | -61.1811 | 2026-09-02 17:10:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 64.5 |
| 964cda4e-ab14-3779-9665-0746b8226d08 | -15.346 | -53.7912 | 2026-09-02 17:10:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 78.1 |
| 40f9ea1b-8cda-331c-9c73-7cdf10c38c0d | -15.2672 | -53.8642 | 2026-09-02 17:10:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 89.5 |
| 5fbfc289-f7a1-3d3f-9622-acc544d238ac | -5.9635 | -57.6899 | 2026-09-02 17:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 95.7 |
| 5e09964c-290f-3b2c-b4ed-edb95a3aead1 | -10.15 | -45.69 | 2026-09-02 17:15:00 | MSG-03 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 01465e2e-d194-3b2d-acb3-194e4ce6bd71 | -10.15 | -45.74 | 2026-09-02 17:15:00 | MSG-03 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| dd1ca469-3d99-3bdc-ab0a-f49d73ae6827 | -3.1267 | -61.1811 | 2026-09-02 17:20:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 62.8 |
| 09b51d81-d94f-33b4-8dc1-6026b76a4a50 | -3.1083 | -61.238 | 2026-09-02 17:20:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 53.7 |
| 07f1cd01-907c-39ed-a33a-6d1378b694ab | -3.1265 | -61.2377 | 2026-09-02 17:20:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 50.8 |
| 57bf180d-0a90-3577-9869-9a7f7cc40608 | -3.7533 | -59.3231 | 2026-09-02 17:20:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 113.8 |
| 48394347-71ba-3bbb-b62a-02841c5b00ea | -13.471 | -57.0373 | 2026-09-02 17:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 43.2 |
| 6d9f1fd9-5b47-3604-a3d5-d5a52638d397 | -3.3688 | -59.4079 | 2026-09-02 17:20:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 115.3 |
| f0bfc2d1-eb04-3ba2-be37-b79e21100453 | -3.1084 | -61.1814 | 2026-09-02 17:20:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 44.0 |
| f0b84ec6-aec8-34df-9f91-369f58f61550 | -4.2383 | -62.2349 | 2026-09-02 17:20:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 114.6 |
| 173c7c3f-4c9b-3474-81a1-41483c0621b5 | -3.0347 | -61.4846 | 2026-09-02 17:20:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 110.0 |
| 0ebc7c04-fc35-3adc-b591-5e602846bf46 | -3.1084 | -61.2003 | 2026-09-02 17:20:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 51.9 |
| 0c25c26d-3ae6-36d0-8fbd-85736d300149 | -3.4185 | -61.3273 | 2026-09-02 17:20:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 67.1 |
| 153486be-b127-3f2f-b18f-f36455d36340 | -15.3654 | -53.7887 | 2026-09-02 17:20:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 76.8 |
| 116b2283-5317-38fa-a9bd-c98bf21eacb1 | -3.4002 | -61.3276 | 2026-09-02 17:20:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 73.8 |
| 1ad22ebf-7c4c-342b-9148-44ccb1d62d17 | -5.9635 | -57.6899 | 2026-09-02 17:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 93.9 |
| 7603c16c-2746-3bb6-b6f8-e8d73c2941d6 | -14.5627 | -52.077 | 2026-09-02 17:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 67.4 |
| a27fb566-4d79-3173-bb3f-7dccf956e68f | -13.4519 | -57.039 | 2026-09-02 17:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 56.0 |
| 2e03c116-a208-3b19-b031-23fbf4bdb722 | -12.5012 | -62.6305 | 2026-09-02 17:20:00 | GOES-19 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 35.7 |
| dc0c4638-6f4c-3d1d-9b45-f3cea887dbf5 | -15.3841 | -53.8282 | 2026-09-02 17:20:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 84.7 |
| 974e2516-dbd5-39c7-bbf2-d1a4742dfac8 | -5.5648 | -60.2121 | 2026-09-02 17:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 86.5 |
| 31407db0-359a-3b32-8e15-fef1b3b01870 | -3.0347 | -61.4657 | 2026-09-02 17:20:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 57.8 |
| f64127f8-420a-3eba-8bb5-4fb1649e1653 | -7.0057 | -59.2575 | 2026-09-02 17:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 101.3 |
| 317c7257-cba9-3d9a-af7f-b0d4558c9556 | -1.4761 | -54.2365 | 2026-09-02 17:20:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 62.5 |
| 869d4fb8-80f7-3d8b-a440-bad412410068 | -6.6745 | -59.0973 | 2026-09-02 17:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 89.7 |
| 40aa8aff-cf8d-3b52-8dc5-9ba92a101990 | -6.7692 | -58.6679 | 2026-09-02 17:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 113.9 |
| 3ad2a9da-1211-3808-ad64-3d9a00ab01c0 | -3.4185 | -61.3461 | 2026-09-02 17:20:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 57.4 |
| a2401560-4dfb-3ae6-a984-f648ef3ad271 | -7.0242 | -59.2374 | 2026-09-02 17:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 116.6 |
| ac63dbad-0106-35c0-9ed1-97ad94cd1ab8 | -5.9635 | -57.6899 | 2026-09-02 17:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 104.9 |
| f673bfc3-08de-30ec-bd2f-310c77097885 | -3.2361 | -61.217 | 2026-09-02 17:30:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 151.9 |
| ab20084b-7ab1-34ef-b6ea-053f039f332d | -5.5648 | -60.2121 | 2026-09-02 17:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 88.7 |
| 3cbd7a74-2394-3154-a4f2-57e377bcea94 | -8.2414 | -54.9601 | 2026-09-02 17:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 68.3 |
| 077757f2-0bf9-3354-b3e9-02ac4a938af3 | -15.3852 | -53.7652 | 2026-09-02 17:30:00 | GOES-19 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 75.3 |
| e0d1fe13-bad6-3228-8d3b-a687904d2c9d | -7.1822 | -60.6713 | 2026-09-02 17:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 81.2 |
| da59bfa5-1677-3712-8f0b-f1bf7e46204e | -10.4334 | -49.9878 | 2026-09-02 17:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 91.6 |
| c02345bd-25e1-3dd6-98b1-cbaa58dff9ef | -3.1267 | -61.1811 | 2026-09-02 17:30:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 56.9 |
| 4d38fd28-7fb9-34bf-9275-9126031731ca | -3.7533 | -59.3231 | 2026-09-02 17:30:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 112.6 |
| 6c15e97c-f533-3dfd-8e33-e36389a85a92 | -7.2932 | -60.6096 | 2026-09-02 17:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 94.7 |
| dc82a3c1-e21d-3ef4-9807-765f1bab9d48 | -7.0242 | -59.2374 | 2026-09-02 17:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 112.2 |
| 01973e6e-b2ed-3cbc-9be6-7c50846c4d8a | -3.4185 | -61.3461 | 2026-09-02 17:30:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 58.5 |
| ef5ffff6-e1cb-34f8-a403-f580f51d8d9a | -3.4002 | -61.3276 | 2026-09-02 17:30:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 79.5 |
| 1b42a59d-0d33-32db-bc5c-43ddfd254e11 | -3.0347 | -61.4657 | 2026-09-02 17:30:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 57.5 |
| 461f73e2-945c-3778-a5e8-f01530e37c02 | -15.346 | -53.7912 | 2026-09-02 17:30:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 79.4 |
| fe6fad28-db55-313f-b767-0d109bcda9d2 | -6.8019 | -59.4008 | 2026-09-02 17:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 98.2 |
| 1a8b00e5-5295-3e61-8f9c-1f4117ab6a26 | -3.1083 | -61.2191 | 2026-09-02 17:30:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 52.5 |
| 8c362f3d-7bb9-3190-ac7c-b926efdd38c6 | -14.312 | -52.0676 | 2026-09-02 17:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 77.7 |
| f3aa7637-9a56-3daa-bd0b-dfb7d524ac47 | -3.4185 | -61.3273 | 2026-09-02 17:30:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 68.7 |
| bd546dcd-cc3f-3408-abda-3d853211e094 | -3.9707 | -60.0258 | 2026-09-02 17:30:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 47.3 |
| 548352d1-9aca-3e29-99d2-3f8f7b1da027 | -7.2192 | -60.6507 | 2026-09-02 17:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 71.6 |
| 6b974bd2-8397-3ec4-b5d3-edca524e128f | -3.3688 | -59.4079 | 2026-09-02 17:30:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 96.4 |
| 5489948b-6ed2-32f3-a8df-17348ae6b622 | -10.4142 | -50.0112 | 2026-09-02 17:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 150.0 |
| ee7af5b7-fc24-3972-a5b5-d7797121f240 | -5.5833 | -60.1924 | 2026-09-02 17:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 106.2 |
| 75d8c8d3-5a48-3324-a3fe-9a67f385b82d | -6.6409 | -58.5181 | 2026-09-02 17:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 99.7 |
| 33259775-147a-3b6a-b0c1-42af2b744c64 | -3.1998 | -61.161 | 2026-09-02 17:30:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 56.7 |
| 78447c08-e39b-3a69-8682-241ab1053565 | -3.4185 | -61.3273 | 2026-09-02 17:40:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 72.4 |
| f88ebfbf-0518-36b7-9e55-057f2f8336c7 | -6.6726 | -59.4445 | 2026-09-02 17:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 93.2 |
| ca0b0d06-5288-3ecc-ba1c-8a93ce8096b6 | -7.2932 | -60.6096 | 2026-09-02 17:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 100.6 |
| e66f5b0a-c1dd-3b78-a988-30a4da41e67c | -3.6399 | -60.5466 | 2026-09-02 17:40:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 37.5 |
| 38f289b5-b2f4-3b47-87d1-153b7b58c15b | -3.1083 | -61.2191 | 2026-09-02 17:40:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 54.5 |
| a1d8fb54-739b-3bbe-8419-2cb4898aa341 | -6.8422 | -41.6791 | 2026-09-02 17:40:00 | GOES-19 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 192.5 |


[Clique aqui para ver as próximas entradas](README91.md)
