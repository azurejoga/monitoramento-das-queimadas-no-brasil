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
| 6870fda7-d8cc-3ef2-86f4-ea517f725eee | -7.9256 | -44.0937 | 2025-09-21 01:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 156.1 |
| 618835ec-89d0-3ff3-be67-6c7f33cccbf0 | -9.4289 | -44.7113 | 2025-09-21 01:00:00 | GOES-19 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 131.3 |
| d71b500d-39fb-3024-bab6-943ac51d30ea | -9.4292 | -44.6883 | 2025-09-21 01:00:00 | GOES-19 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 77.2 |
| 824732f5-8347-396a-98ca-acc2f29ee24c | -4.4568 | -44.1413 | 2025-09-21 01:00:00 | GOES-19 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 69.1 |
| b1c2466b-d4a4-33c4-8b6f-6022d5528edc | -7.9442 | -44.115 | 2025-09-21 01:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 73.3 |
| 3922b536-efb2-3231-b0d5-f2ba0d6ea0a3 | -24.69599 | -49.13934 | 2025-09-21 01:07:00 | TERRA_M-M | CERRO AZUL | PARANÁ | Brasil | 4105201 | 41 | 33 | nan | nan | nan | Mata Atlântica | 17.9 |
| ba6d51c8-9a6d-3804-80b5-bd700756da2f | -24.7563 | -48.81982 | 2025-09-21 01:07:00 | TERRA_M-M | ADRIANÓPOLIS | PARANÁ | Brasil | 4100202 | 41 | 33 | nan | nan | nan | Mata Atlântica | 11.6 |
| 32b30c64-df30-3a6a-86b5-efff4a327903 | -22.70745 | -51.56236 | 2025-09-21 01:07:00 | TERRA_M-M | CENTENÁRIO DO SUL | PARANÁ | Brasil | 4105102 | 41 | 33 | nan | nan | nan | Mata Atlântica | 13.2 |
| c3d937d4-1115-37d9-99d0-3ca39fa8fbba | -22.6354 | -48.2619 | 2025-09-21 01:07:00 | TERRA_M-M | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 21.0 |
| 057aad03-849d-3db2-b9d6-f35dc85ecc4b | -22.71546 | -51.42533 | 2025-09-21 01:07:00 | TERRA_M-M | PORECATU | PARANÁ | Brasil | 4120002 | 41 | 33 | nan | nan | nan | Mata Atlântica | 8.2 |
| ae123757-eda1-34a4-8075-0d8759633262 | -23.23979 | -50.14656 | 2025-09-21 01:07:00 | TERRA_M-M | SANTO ANTÔNIO DA PLATINA | PARANÁ | Brasil | 4124103 | 41 | 33 | nan | nan | nan | Mata Atlântica | 9.7 |
| c3dbd7bb-b848-3cdc-b6d4-6eba0a582a02 | -22.78331 | -55.3694 | 2025-09-21 01:07:00 | TERRA_M-M | ARAL MOREIRA | MATO GROSSO DO SUL | Brasil | 5001243 | 50 | 33 | nan | nan | nan | Mata Atlântica | 12.4 |
| 44aa0220-23bb-34fb-90fd-33d72df21bd4 | -24.75155 | -48.81453 | 2025-09-21 01:07:00 | TERRA_M-M | ADRIANÓPOLIS | PARANÁ | Brasil | 4100202 | 41 | 33 | nan | nan | nan | Mata Atlântica | 9.8 |
| 3c1dc66f-195b-363f-a310-d9901077249b | -23.15083 | -47.62721 | 2025-09-21 01:07:00 | TERRA_M-M | TIETÊ | SÃO PAULO | Brasil | 3554508 | 35 | 33 | nan | nan | nan | Mata Atlântica | 25.7 |
| b1b92f41-3bfa-38e6-9ac5-b681a73761b5 | -23.24235 | -50.16133 | 2025-09-21 01:07:00 | TERRA_M-M | SANTO ANTÔNIO DA PLATINA | PARANÁ | Brasil | 4124103 | 41 | 33 | nan | nan | nan | Mata Atlântica | 14.1 |
| d6c4df58-e526-33fb-a593-5eeb2836bdca | -18.73929 | -53.29636 | 2025-09-21 01:09:00 | TERRA_M-M | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 6.8 |
| bdbe2359-cce6-3eb5-a67b-ee80806c45f3 | -20.99446 | -54.76313 | 2025-09-21 01:09:00 | TERRA_M-M | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 15.4 |
| f88c041d-cf9a-37f2-acee-fd281f345991 | -17.376 | -52.70385 | 2025-09-21 01:09:00 | TERRA_M-M | PORTELÂNDIA | GOIÁS | Brasil | 5218102 | 52 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 37870d45-d297-350d-a5a3-06cc1cea057b | -20.99583 | -54.77268 | 2025-09-21 01:09:00 | TERRA_M-M | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 26.2 |
| 4602b444-8420-37c9-a065-2e6d6fa1712f | -15.27141 | -51.47861 | 2025-09-21 01:09:00 | TERRA_M-M | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 7f9dbc2c-0a8d-387d-b4c2-5fdf1947b5f1 | -20.53244 | -56.14922 | 2025-09-21 01:09:00 | TERRA_M-M | MIRANDA | MATO GROSSO DO SUL | Brasil | 5005608 | 50 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 974d3b0e-0d70-357f-b541-e76f4251c1dd | -18.73762 | -53.28527 | 2025-09-21 01:09:00 | TERRA_M-M | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 8.4 |
| ea7ee28b-f0be-347d-8195-1ed6243d7608 | -20.60195 | -56.73253 | 2025-09-21 01:09:00 | TERRA_M-M | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 9d3c9a1c-eefb-32a7-ab41-6dffe68452b1 | -14.4598 | -46.5288 | 2025-09-21 01:09:00 | TERRA_M-M | SIMOLÂNDIA | GOIÁS | Brasil | 5220686 | 52 | 33 | nan | nan | nan | Cerrado | 30.6 |
| a5f15717-a7f1-3047-b818-413ad926b36b | -18.74431 | -53.32957 | 2025-09-21 01:09:00 | TERRA_M-M | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 30385468-4678-364c-8c5d-2db39e830b0d | -20.60962 | -56.72147 | 2025-09-21 01:09:00 | TERRA_M-M | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 2f194b08-99a9-3ad7-82b6-3b6b0c94ad9d | -20.54332 | -56.15083 | 2025-09-21 01:09:00 | TERRA_M-M | MIRANDA | MATO GROSSO DO SUL | Brasil | 5005608 | 50 | 33 | nan | nan | nan | Cerrado | 7.3 |
| a77e4bb1-3b72-3b38-b5bf-2de7c910f0b8 | -16.32747 | -56.70702 | 2025-09-21 01:09:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.9 |
| 6e88048e-d46f-3481-a10d-4ac072bb85f8 | -19.84038 | -57.30113 | 2025-09-21 01:09:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 15.1 |
| 3ea69696-9ac2-3377-8ea3-13ab56580810 | -18.74206 | -53.29002 | 2025-09-21 01:09:00 | TERRA_M-M | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 8.1 |
| c855ca76-890f-39fd-8771-3000e3005c3d | -14.61188 | -49.74531 | 2025-09-21 01:09:00 | TERRA_M-M | GUARINOS | GOIÁS | Brasil | 5209457 | 52 | 33 | nan | nan | nan | Cerrado | 13.3 |
| a0f9c2c1-1722-3b14-adc0-1a468925ec6b | -14.60228 | -49.76959 | 2025-09-21 01:09:00 | TERRA_M-M | GUARINOS | GOIÁS | Brasil | 5209457 | 52 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 8524104a-7061-3169-bfc2-edc96fd7d197 | -15.27845 | -56.85488 | 2025-09-21 01:09:00 | TERRA_M-M | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 24.8 |
| 14979326-ab6f-39b4-8979-6e746216d1d3 | -14.36794 | -60.30384 | 2025-09-21 01:09:00 | TERRA_M-M | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 1a1e1bc0-b718-3620-9a27-0831237e492f | -15.89502 | -59.40369 | 2025-09-21 01:09:00 | TERRA_M-M | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 11.1 |
| f294e126-ebd9-35b7-a012-2e6feed170c7 | -14.79282 | -51.37437 | 2025-09-21 01:09:00 | TERRA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 15.3 |
| b2a87a9f-7e41-3881-b73f-c6312a5dad3b | -14.6157 | -49.76759 | 2025-09-21 01:09:00 | TERRA_M-M | GUARINOS | GOIÁS | Brasil | 5209457 | 52 | 33 | nan | nan | nan | Cerrado | 42.0 |
| 304369c9-8486-327f-941e-16235d9e1fe0 | -15.89641 | -59.41449 | 2025-09-21 01:09:00 | TERRA_M-M | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 15072b7f-2fa3-355b-b089-e6d71ae098fd | -15.28223 | -56.8172 | 2025-09-21 01:09:00 | TERRA_M-M | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 8.7 |
| e49f1f0e-1664-3619-9559-df72001dc51b | -15.82665 | -59.5103 | 2025-09-21 01:09:00 | TERRA_M-M | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 384b4397-24e0-3a81-95e5-f015ef812954 | -14.36689 | -60.29835 | 2025-09-21 01:09:00 | TERRA_M-M | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 16.9 |
| e747295e-d914-3ec9-bbe7-9a91b9ac6e56 | -11.1188 | -49.68539 | 2025-09-21 01:09:00 | TERRA_M-M | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 23.2 |
| 5a6f6bf0-0b5d-32d1-9080-ebba74da8e96 | -15.91167 | -59.45684 | 2025-09-21 01:09:00 | TERRA_M-M | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| cab96118-c84c-3555-ba5e-7c3ac97f538a | -11.62485 | -50.60563 | 2025-09-21 01:09:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 894f1e1f-1cff-360b-9210-a65d2f0bb298 | -15.26712 | -56.83803 | 2025-09-21 01:09:00 | TERRA_M-M | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| be1215f5-a8f4-3856-967e-366138463a67 | -15.41802 | -58.78022 | 2025-09-21 01:09:00 | TERRA_M-M | JAURU | MATO GROSSO | Brasil | 5105002 | 51 | 33 | nan | nan | nan | Amazônia | 9.9 |
| e0d8c101-a4d1-3764-9ece-0950d9424d75 | -15.95153 | -59.43489 | 2025-09-21 01:09:00 | TERRA_M-M | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 30.2 |
| fa9f6b54-e347-313f-b096-47bc80da4318 | -13.97239 | -56.34173 | 2025-09-21 01:09:00 | TERRA_M-M | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 5ec50aa3-0c82-308c-b1ff-377d51b56513 | -11.12076 | -49.67951 | 2025-09-21 01:09:00 | TERRA_M-M | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 26.7 |
| d2b10346-adc9-3ea8-b8c8-ac762dd49680 | -15.27971 | -56.86396 | 2025-09-21 01:09:00 | TERRA_M-M | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 4147923f-5f51-3884-8921-12288f074f4b | -14.81626 | -51.37017 | 2025-09-21 01:09:00 | TERRA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 26.5 |
| 7ca9b4ca-c212-3cb5-86ac-58863d6d0f98 | -14.36658 | -60.29276 | 2025-09-21 01:09:00 | TERRA_M-M | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 4fd8e72a-8871-3286-976a-95070a9dfaf8 | -15.26964 | -56.8562 | 2025-09-21 01:09:00 | TERRA_M-M | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 915531b5-da17-355a-8f05-4929d662f95b | -11.6186 | -50.5861 | 2025-09-21 01:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 52.6 |
| 697fa167-6bac-30f4-ae07-0145d936360b | -7.9445 | -44.0918 | 2025-09-21 01:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 108.2 |
| bb7a16fe-0287-3bee-b719-b713241fb4c9 | -7.9256 | -44.0937 | 2025-09-21 01:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 152.7 |
| f16bf45f-1518-31b0-ba12-1bf779a89c75 | -11.6183 | -50.6075 | 2025-09-21 01:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 83.1 |
| 09853b2b-5d95-3cdb-a83a-56f6864ce3b6 | -11.6374 | -50.6053 | 2025-09-21 01:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 60.8 |
| d070f01b-db3c-39ac-aaeb-e87b6e14e72b | -5.5243 | -43.8647 | 2025-09-21 01:10:00 | GOES-19 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 100.1 |
| 389fb3bf-a4d1-3ed5-ab9e-c849aa11f095 | -9.4289 | -44.7113 | 2025-09-21 01:10:00 | GOES-19 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 139.7 |
| d5243152-abd8-3116-93db-f4d281349369 | -9.4292 | -44.6883 | 2025-09-21 01:10:00 | GOES-19 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 75.6 |
| 6d17574a-5080-3c83-9eec-70a636b72186 | -15.9586 | -59.4288 | 2025-09-21 01:10:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 62.4 |
| ab4f4974-779a-36b5-aef7-993d57e17af3 | -7.9253 | -44.1169 | 2025-09-21 01:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 103.8 |
| 5b509278-4378-39aa-89d6-24139f6a4b0e | -3.75808 | -54.82664 | 2025-09-21 01:11:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 8f09f10e-b9f8-3c24-8a1b-683784f0795b | -3.92375 | -53.82311 | 2025-09-21 01:11:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| c68443f4-5c48-3394-adb5-45b0042b71d9 | -3.75615 | -54.8129 | 2025-09-21 01:11:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 47.5 |
| 1fa79770-e2ff-387c-bbaa-2969f27d9c21 | -3.7601 | -54.82 | 2025-09-21 01:11:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 49.9 |
| a1d36446-2cdd-398d-974a-44442be37e73 | -4.36829 | -56.03857 | 2025-09-21 01:11:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 16be03cc-a0f3-3639-b3e5-0aef88f40a4e | -4.36669 | -56.02727 | 2025-09-21 01:11:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 27.8 |
| 06373283-8437-3434-8f40-16286a1de4c8 | -3.75808 | -54.80635 | 2025-09-21 01:11:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 25.9 |
| d8418308-8508-375c-a149-2ab93bc04325 | -3.65283 | -58.16733 | 2025-09-21 01:13:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 581cbb11-da05-3e6e-8b90-0c9369c5c8e7 | -2.80318 | -58.35203 | 2025-09-21 01:13:00 | TERRA_M-M | SILVES | AMAZONAS | Brasil | 1304005 | 13 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 98fb03b1-5b66-399f-af96-24237f16fd80 | -1.97901 | -56.43891 | 2025-09-21 01:13:00 | TERRA_M-M | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 41d9d6a8-2569-39a5-99af-53b84602212a | -1.12151 | -54.14736 | 2025-09-21 01:13:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 17.0 |
| 284517a1-4b8b-30d4-81a7-85d461de1529 | -2.69393 | -59.42478 | 2025-09-21 01:13:00 | TERRA_M-M | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| d40a4a00-0383-305f-9ed0-8d1eabe06a22 | -1.60314 | -54.30378 | 2025-09-21 01:13:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 0b487a7e-063f-3fa0-8d5d-68a08ecec897 | -3.65157 | -58.15825 | 2025-09-21 01:13:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 9.7 |
| c06eaf06-fb88-3665-b455-76712a74d776 | 3.88067 | -59.62724 | 2025-09-21 01:15:00 | TERRA_M-M | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 449e6a93-8b42-3560-a25a-d72ebf245ac5 | 4.32699 | -60.73411 | 2025-09-21 01:15:00 | TERRA_M-M | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 9c3dc4cb-971f-31f8-ae9f-91cb1152fbba | 3.8717 | -59.62598 | 2025-09-21 01:15:00 | TERRA_M-M | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 9.7 |
| ba5bcc0e-b42d-3c70-b547-8c186308a7f0 | -7.9256 | -44.0937 | 2025-09-21 01:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 129.2 |
| c11b49d7-b1b8-3cd8-825e-8d6d38c8362a | -5.5243 | -43.8647 | 2025-09-21 01:20:00 | GOES-19 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 83.2 |
| ef7fc813-0932-3c04-95ce-9ecde62224cc | -19.743 | -49.6543 | 2025-09-21 01:20:00 | GOES-19 | ITAPAGIPE | MINAS GERAIS | Brasil | 3133402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 125.7 |
| 8fbc3fb1-9abd-37c9-a4fd-497c1ea78ee9 | -15.9586 | -59.4288 | 2025-09-21 01:20:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 57.4 |
| 30e3a0ee-4aed-36c4-9c5e-05be1e14779c | -7.9442 | -44.115 | 2025-09-21 01:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 77.9 |
| c9dca050-00b4-3fa4-a239-f099880c8e5c | -22.5079 | -47.5325 | 2025-09-21 01:20:00 | GOES-19 | SANTA GERTRUDES | SÃO PAULO | Brasil | 3546702 | 35 | 33 | nan | nan | nan | Mata Atlântica | 67.4 |
| c6492d89-49b5-32c6-b307-b63f9ac70283 | -15.2783 | -56.8555 | 2025-09-21 01:20:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 64.9 |
| 645c2ad5-7b7c-3e61-8abe-a426cd58fcfd | -11.6183 | -50.6075 | 2025-09-21 01:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 63.8 |
| 0dcf9afb-b06c-37c9-aef0-7376d099c544 | -7.9445 | -44.0918 | 2025-09-21 01:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 107.1 |
| faaafae2-5af6-3934-9b58-854613937446 | -7.9253 | -44.1169 | 2025-09-21 01:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 104.1 |
| 9a9b1831-d763-3171-a41c-ae5164ab8579 | -11.6374 | -50.6053 | 2025-09-21 01:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 58.2 |
| e4a623e0-c7b5-3bd9-86bf-a702ea932a3e | -9.4289 | -44.7113 | 2025-09-21 01:20:00 | GOES-19 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 105.2 |
| 58dc48b5-a54a-3c38-b86e-62bac2640d8e | -5.5243 | -43.8647 | 2025-09-21 01:30:00 | GOES-19 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 85.4 |
| 71439baf-7105-3f05-8899-058975f16d2a | -15.9586 | -59.4288 | 2025-09-21 01:30:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 65.7 |
| 09aef52a-8d5a-323c-9827-3e311fa71c91 | -9.4289 | -44.7113 | 2025-09-21 01:30:00 | GOES-19 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 98.7 |
| b715e4d6-8a6b-3f6a-b4e4-ad97205ab77b | -7.9253 | -44.1169 | 2025-09-21 01:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 102.5 |
| 89129b26-538b-3932-a682-116eae518bad | -7.9442 | -44.115 | 2025-09-21 01:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 74.3 |
| 3e1ee34f-c6e1-36af-a2cb-1fdb73c2968b | -19.743 | -49.6543 | 2025-09-21 01:30:00 | GOES-19 | ITAPAGIPE | MINAS GERAIS | Brasil | 3133402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 99.6 |
| 72f0ef1c-a922-3321-8c4f-33d53ca00182 | -7.9445 | -44.0918 | 2025-09-21 01:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 109.0 |
| c1a3a99f-3b50-3d05-997e-f68aafe0c022 | -11.6183 | -50.6075 | 2025-09-21 01:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 54.6 |


[Clique aqui para ver as próximas entradas](README3.md)
