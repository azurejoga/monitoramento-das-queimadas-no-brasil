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

## Dados Diários - Página 124

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 378767a9-643c-362c-860a-0c5ad74681df | -4.06783 | -51.03531 | 2026-10-08 05:23:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4eaa79f0-ea74-3c34-becc-08dec21d4816 | -2.9822 | -54.11859 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 68c5558d-a64a-3db3-b8ae-3a790b86dd63 | -1.45839 | -54.78403 | 2026-10-08 05:23:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9b7a825c-4e77-3b2a-b1e6-8fcb57072a7a | -4.79486 | -55.72257 | 2026-10-08 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b8abdd1a-952a-3663-9bc2-ca65afaad766 | -2.49804 | -56.15958 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 422de63d-98dc-3cbe-886f-c66d5233c026 | -13.19323 | -47.88208 | 2026-10-08 05:23:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b4a595b1-447c-315d-8cdf-291d048c561b | -2.76935 | -54.09162 | 2026-10-08 05:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0053cf9f-9dc9-3429-b657-b5810c3a03cf | -5.91117 | -53.8853 | 2026-10-08 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b2802f70-f709-3389-973e-ff1d2d7409bb | -3.53503 | -55.52047 | 2026-10-08 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 537b076d-9c11-30e8-8c39-5d3866f03282 | -2.57405 | -56.14653 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2f65caeb-d451-3e42-8da7-291cc4fc8161 | -3.0486 | -53.94557 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1bba09c9-0c21-35df-be52-eeeb35992110 | -7.19744 | -45.35484 | 2026-10-08 05:23:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 37e9138b-e166-393a-90a6-5ab55c2c16e6 | -2.64947 | -56.54835 | 2026-10-08 05:23:00 | NPP-375D | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e4a172b1-3c1c-37a7-be15-4175de88bdf4 | -10.36502 | -56.44009 | 2026-10-08 05:23:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ce181f6f-c659-304c-9159-6d4d07405338 | -3.24743 | -56.80901 | 2026-10-08 05:23:00 | NPP-375D | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e8879942-adfc-35ab-9eb2-da305843fb48 | -6.46665 | -55.44516 | 2026-10-08 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2a3c3d9c-c323-3f4d-bc68-faa5a93d61ce | -3.48723 | -54.62101 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| db50318f-84ac-335e-bcbf-16282fa829ef | -6.25044 | -52.8717 | 2026-10-08 05:23:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 89e82fc0-f296-37c0-81cc-d6c3abaa73ca | -3.10188 | -53.7671 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| c7c15e04-fb69-3b01-9188-352fd45ab644 | -11.98262 | -57.57696 | 2026-10-08 05:23:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c58a02d0-bab5-3e6b-a702-cafbfcff9f1d | -3.18842 | -50.54343 | 2026-10-08 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 916628c8-2c68-3462-b74d-69ddf0f9ad4e | -8.61548 | -67.05434 | 2026-10-08 05:23:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b7267ae5-091c-3153-bae9-fb0e1f730274 | -4.09301 | -53.99122 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8867b406-a74c-3399-8e13-a489eebf5e3f | -6.7257 | -55.06363 | 2026-10-08 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 3152ba70-0914-3681-b9cf-c3f76bb0b775 | -6.93421 | -43.66468 | 2026-10-08 05:23:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 47cec102-046e-3ae1-8251-41332fea7b50 | -3.29564 | -54.02582 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 472eb01a-0785-3d9a-9eff-bcbbeca55af3 | -3.69335 | -55.95611 | 2026-10-08 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0bacf4ee-655b-39cf-ae14-1fd684067f78 | -7.20327 | -55.10141 | 2026-10-08 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5dd3c9ba-657f-3ced-aec9-a91d467b0cc9 | -1.83073 | -54.99131 | 2026-10-08 05:23:00 | NPP-375D | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 350df3df-1ef2-34da-9fed-80b9749483db | -3.01963 | -54.10862 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 15.7 |
| 558e0435-c9cb-3cde-ae8e-9a47070c6607 | -4.65781 | -56.21425 | 2026-10-08 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cfe4541e-6d87-350b-bacd-1ad7c48bf76e | -3.47916 | -54.62745 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a91e08fa-3d31-3357-bd75-c888544632ef | -3.16265 | -54.73566 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| da397267-695a-389a-a961-d0ed267aadc2 | -3.30428 | -54.70025 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c1ee4ff9-b735-34de-af33-52c4a6f725e8 | -3.85101 | -55.99138 | 2026-10-08 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6dbdc81c-89f7-3065-9f36-ef47b06d59cf | -7.64181 | -44.3729 | 2026-10-08 05:23:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| f4b7080a-c805-32e0-9ef5-69933969c0e6 | -2.84596 | -54.13417 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 84da46d5-aacf-3813-99c3-c43c36b81ba2 | -3.92427 | -56.05987 | 2026-10-08 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 97140a93-490c-3355-93e6-4cd2893ea488 | -9.08522 | -61.13757 | 2026-10-08 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1e0491a6-6d89-3e64-bcdc-18f5fab18f6c | -9.47506 | -64.35648 | 2026-10-08 05:23:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e4238281-1c7e-3b1b-ad2c-b5ff015c9c42 | -1.28277 | -55.4146 | 2026-10-08 05:23:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 05512ab3-2791-376a-997c-8049747a7fe5 | -4.57331 | -54.95275 | 2026-10-08 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| aa61e78a-40c9-3691-bb18-84cd48d805f1 | -2.91431 | -54.11224 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2b21eec5-b2cb-3647-b297-e9c0aafb1f0c | -3.47571 | -54.62693 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 94a75372-d35c-39fc-b5a2-746c0fca7624 | -3.08038 | -54.25089 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a23a9794-e1c3-3881-abad-f5f871335279 | -3.49253 | -59.60224 | 2026-10-08 05:23:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d13ed15f-b836-3397-9b13-9e6696a0dcfd | -3.67504 | -54.49923 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ba71388c-c8a2-38f8-b892-7ca791e7cdf9 | 0.78518 | -59.1937 | 2026-10-08 05:23:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 86928e29-bec8-3627-9770-935ea2e617d9 | -4.0577 | -55.32293 | 2026-10-08 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ed70212e-2388-3a31-8385-edd41721c78e | -4.34374 | -43.79314 | 2026-10-08 05:23:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 279b00e7-650c-380f-964f-5f976a0724a0 | -4.09646 | -52.06839 | 2026-10-08 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 18344dd1-a486-3758-a128-052eb97935b6 | -3.25852 | -54.67785 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| f34209f9-33c9-3acc-907d-3d02a8f5209b | -2.99765 | -54.04169 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 500b2ca7-87f6-3722-b83e-613f812f8bda | -3.10207 | -53.74256 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b0d3f742-ed35-300d-82cb-ef4a26c202cc | -2.76743 | -54.08652 | 2026-10-08 05:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 79428919-745f-3e80-be24-29c06bb620ea | -3.03824 | -54.52276 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b7e603ea-706b-3f9f-8eff-12a23082a7fa | -2.50082 | -56.16356 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3190d0ea-67b1-31ca-8dd9-c7f698ac541c | -3.27448 | -54.02259 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 59218cff-96e5-3abe-80ad-f9b335e52913 | -3.6502 | -54.06115 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9d1dae80-f8e1-3a3d-8123-c55c138bd0fd | -3.2972 | -61.01761 | 2026-10-08 05:23:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 91ec5c9a-baf2-3ab0-8ed2-62dfb78b66ce | -3.10375 | -53.75513 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| beb6fc2a-72ab-347c-8c30-14facf3c0396 | -5.33959 | -50.98483 | 2026-10-08 05:23:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 52309ab4-53e7-353e-aa1f-b90acc674ce5 | -2.97907 | -54.04296 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b4720c08-9d72-38ef-80e9-a7389c1f744c | -4.77363 | -55.74165 | 2026-10-08 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 71d7e900-96e1-394d-9389-6f579c2e82e9 | -2.50579 | -56.15371 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7e7bc5b3-e591-3c83-a4e2-d3b91cacf834 | -4.15627 | -55.14149 | 2026-10-08 05:23:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 5f135019-ea1e-3911-aef9-b106b0e75383 | -5.28979 | -60.0947 | 2026-10-08 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3438ff02-b8fb-3b19-8d4b-07dace80003c | -2.8162 | -59.24735 | 2026-10-08 05:23:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 10854d2c-9325-3c49-a8fb-a28e48a44a2e | -2.89313 | -54.15621 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 58823a9d-a5ab-3c96-aeb4-874cf272de7b | -2.93614 | -54.17862 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 72170508-9b45-3357-9b67-a7437b06a86e | -3.73538 | -51.2108 | 2026-10-08 05:23:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c1db3543-62d3-3ed0-953e-b1416b1232d9 | -11.35 | -51.87187 | 2026-10-08 05:23:00 | NPP-375D | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2aaefeb4-ba05-3864-a903-3f414940268b | -3.01522 | -54.04442 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cb12a80a-f38b-3def-8c40-588596fa2954 | -3.05566 | -54.24405 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 568a8586-1439-31fc-a7b5-5431b304c3d2 | -6.88413 | -43.69612 | 2026-10-08 05:23:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 11e53595-8dea-3f53-8c70-c120e5124b53 | -4.43069 | -55.65929 | 2026-10-08 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 249bea7a-b4a5-399d-bbac-48e16e8921cf | -3.3565 | -50.47287 | 2026-10-08 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e370cda9-033c-36cf-a66e-765a6e05a83e | -3.02494 | -54.09757 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 618ccdf2-c809-37ca-b955-15d519cd059b | -3.68285 | -57.05175 | 2026-10-08 05:23:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0415b3f8-30c8-38d2-98b4-2ddc12d126e6 | -3.03278 | -53.93102 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e43ff9b6-a041-3cbf-8630-ddf4e9f30355 | -1.11003 | -54.16486 | 2026-10-08 05:23:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ab70e487-d285-3423-acb7-2d8cc4290cf2 | -2.5041 | -56.14282 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 738a3100-ef82-3982-a121-1ebe76adeb89 | -2.87909 | -54.17759 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4a662904-c8c7-316b-874a-c525f1ad1184 | -3.84767 | -55.99086 | 2026-10-08 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f465308d-b323-3831-9808-9d7ed02c1dd0 | -2.56853 | -56.15983 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 79d70b53-a43d-32d2-a631-c304eb8f6c95 | -5.69617 | -53.48402 | 2026-10-08 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a685ff09-6ddc-3c8e-b6ed-58bdfef69f62 | -3.98607 | -59.22261 | 2026-10-08 05:23:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 980b4ee5-768c-30e5-8076-f4e75dec1325 | -3.08256 | -54.30591 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 70200817-a579-3ec0-a9b7-d21116d10ddb | -6.14172 | -47.93009 | 2026-10-08 05:23:00 | NPP-375D | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 45a68236-00f6-3aa2-afaa-243396e94829 | -2.85953 | -59.11557 | 2026-10-08 05:23:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 09de9ee1-a693-3cf1-9f4a-9f305d90bd46 | -3.08206 | -53.9628 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 59.0 |
| 0e597586-d7d4-31bd-83bc-7fbf78e088d5 | -1.2899 | -55.69317 | 2026-10-08 05:23:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 27a2b48c-0141-359f-9b79-e1995cf0b624 | -5.89765 | -53.50221 | 2026-10-08 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8fa7db01-7bbc-36d2-ae3b-f0da2b0fb971 | -7.22536 | -55.12075 | 2026-10-08 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2b0bd6ea-3b5b-3d63-ba0e-fbd3f408a3df | -3.08085 | -54.29393 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 70d0865a-0bf0-3379-b460-e80f1dd1a6ac | -3.10962 | -53.76423 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 594014f0-3839-3a78-afb4-9bcc3554c437 | -3.54114 | -54.66006 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 157a7d33-018d-3fd6-b3d4-4b1e21e759cd | -3.93997 | -59.79025 | 2026-10-08 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2713ee19-7822-30b9-a5ae-c91a47b325c2 | -2.9467 | -54.06577 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d07d04f4-8f53-3a25-a21b-3f7016492246 | -9.49417 | -64.35108 | 2026-10-08 05:23:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README125.md)
