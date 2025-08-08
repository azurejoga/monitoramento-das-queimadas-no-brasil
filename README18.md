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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| adc3e201-9258-36dd-b514-39c18982f943 | -3.3612 | -43.16686 | 2025-08-08 04:57:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 29bc1908-0a6c-3b6d-bd0d-8a1df4a31ac3 | -8.21067 | -45.06403 | 2025-08-08 04:59:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ce81b43c-09b4-3528-8a14-84636417dd93 | -7.40785 | -47.13734 | 2025-08-08 04:59:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 42352b45-5d7b-3cc6-a9aa-a5ad68f74d97 | -6.15547 | -55.80699 | 2025-08-08 04:59:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d4310997-84aa-3520-a9b6-dc7e17c8b5e2 | -8.06541 | -49.71889 | 2025-08-08 04:59:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b26917b6-0b8c-3c48-85dc-018b45746445 | -8.21112 | -45.06057 | 2025-08-08 04:59:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f121aa48-e556-3af7-aad3-45a02ff064fe | -8.21111 | -45.05982 | 2025-08-08 04:59:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1122f0f9-9290-331a-8938-23107c4c4ba3 | -9.65357 | -43.85095 | 2025-08-08 04:59:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 7a87791f-cf4f-3b36-84ac-f20ed6669108 | -10.43117 | -44.35889 | 2025-08-08 04:59:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b5df069a-e149-39c2-853c-3a9af5107997 | -8.05228 | -46.34286 | 2025-08-08 04:59:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d6f11c46-ed53-39e7-8957-628fd0d06465 | -7.04682 | -59.19175 | 2025-08-08 04:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.5 |
| dea9f842-cad5-3864-9b91-a09fe6f1c6c1 | -6.09451 | -59.92674 | 2025-08-08 04:59:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7dfa5771-743a-3dd6-987e-8b7ece6b099f | -8.99182 | -45.68587 | 2025-08-08 04:59:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 29f4c88e-dbea-3cfe-b6ad-08067a904ea4 | -8.92179 | -60.73561 | 2025-08-08 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4aa7dce7-b97d-3df4-8ab8-71d5f969c19a | -7.11724 | -44.21296 | 2025-08-08 04:59:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b9e71f4d-8644-3871-ba3a-df74a76af36f | -6.91651 | -52.84882 | 2025-08-08 04:59:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a91ee7de-98d5-3962-8bff-35cbd712e6be | -8.11104 | -47.43169 | 2025-08-08 04:59:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 605d2de6-ba2d-3c6f-9423-86b5c4514ad4 | -8.91895 | -60.75216 | 2025-08-08 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4720f381-7ba2-39bc-8218-000b9b45c9bc | -6.91142 | -52.83697 | 2025-08-08 04:59:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5bffd03b-cf1c-369d-b0d6-9f852308b997 | -8.52152 | -43.31239 | 2025-08-08 04:59:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f1384546-46a0-3f4b-badd-9d95e87a6204 | -8.92108 | -60.73975 | 2025-08-08 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a2c0809b-e80e-31d8-84e2-c242905a2482 | -7.90874 | -45.54916 | 2025-08-08 04:59:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 2eca5bd7-d4cb-389b-9e31-afe9dada36e8 | -8.24938 | -45.06605 | 2025-08-08 04:59:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6cca4ec8-95d0-3169-91bc-333bf1495b88 | -8.9261 | -60.73636 | 2025-08-08 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 772ed581-2e8d-323b-bc96-c8c707d70b15 | -8.86397 | -47.27413 | 2025-08-08 04:59:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7bac7482-87c1-3f01-9909-af5264b493dd | -7.04768 | -59.18034 | 2025-08-08 04:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.1 |
| b565b666-17ed-3a63-8341-cdf2099464dd | -8.92184 | -60.76121 | 2025-08-08 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4c5b48b4-9a5b-310c-8cde-53d591562701 | -9.55636 | -47.88437 | 2025-08-08 04:59:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 37ba24cc-ac79-3c1a-acca-172e7c9409fa | -4.99972 | -56.03769 | 2025-08-08 04:59:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5b71b983-ec59-3c40-bfd5-816ec8f6b108 | -7.3999 | -60.00402 | 2025-08-08 04:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d5ebb21e-bc09-3f2c-be0b-9e65dca51994 | -5.88328 | -57.75102 | 2025-08-08 04:59:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 738af80c-7da9-3e93-abe0-76330df53150 | -7.91448 | -45.54651 | 2025-08-08 04:59:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4ae42a93-af12-339a-913e-09e4493f1679 | -8.5209 | -43.31713 | 2025-08-08 04:59:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 375b69da-0f7c-3499-a956-8fccdbb26ee1 | -11.18894 | -51.43369 | 2025-08-08 04:59:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 264509ab-1c7c-3d4f-9dea-2452b300ddec | -9.65462 | -43.84245 | 2025-08-08 04:59:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 547042fb-559f-304c-8384-928c5ddcbe13 | -6.91706 | -52.84523 | 2025-08-08 04:59:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0179460c-73e7-35c0-b0c7-d1ba65bad2dd | -11.74356 | -47.51078 | 2025-08-08 04:59:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 5c1d54cd-7180-3e2c-a226-56adc2ae9f2c | -7.06392 | -55.41619 | 2025-08-08 04:59:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ec1c1fd9-e281-3f55-b9fb-24a75af3bbf5 | -6.90534 | -51.06306 | 2025-08-08 04:59:00 | NPP-375D | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 5d96a3bf-e781-3529-ab91-ca28c49e8d21 | -10.63663 | -44.74732 | 2025-08-08 04:59:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e11d8d90-76db-3116-a6fd-c10c6d7f4d10 | -5.88338 | -57.74804 | 2025-08-08 04:59:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 551ca8ef-374f-38b2-a00f-7ba6fa28d229 | -8.98825 | -45.68585 | 2025-08-08 04:59:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 75eeb3b2-6d48-3a00-8989-c37ca167f79d | -5.81383 | -59.22797 | 2025-08-08 04:59:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| c087cc66-71c6-3c61-93a1-fdcb0b9b016b | -8.24845 | -45.07303 | 2025-08-08 04:59:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 76e31fe1-dbcd-3886-9015-27713da92bae | -10.4349 | -44.34952 | 2025-08-08 04:59:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2e7866b0-bdaa-3b08-8104-23d02befe853 | -8.98652 | -45.68508 | 2025-08-08 04:59:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 7ac0e173-d2a1-335e-a0f3-11ca6bb77100 | -7.9083 | -45.55235 | 2025-08-08 04:59:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d9a7ec8a-546e-3bc3-a942-265dcceca9a7 | -8.52215 | -43.30762 | 2025-08-08 04:59:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9a6781b2-8967-3f09-9ea4-769c2a1d88c2 | -7.04458 | -59.18077 | 2025-08-08 04:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 89ee7fde-152e-303d-90f5-c14a569e3f61 | -5.87502 | -57.7544 | 2025-08-08 04:59:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 83d90abf-16f4-32e8-a775-9da1ddd0dfb2 | -7.39633 | -59.99952 | 2025-08-08 04:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2aef86be-d823-3a60-a6d0-fdf8ecaf6d25 | -8.48557 | -46.00824 | 2025-08-08 04:59:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e39ab5c0-74eb-3986-9885-f5fc6e508a73 | -7.89417 | -45.33864 | 2025-08-08 04:59:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ec9ae3cc-a437-312f-ae52-21b64d19d34c | -9.82976 | -57.85204 | 2025-08-08 04:59:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0b0dbbc9-54d2-38d1-8c06-587d97fcee7c | -12.09262 | -44.72969 | 2025-08-08 04:59:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 64bb19de-87d6-33ad-a1e7-f26ff2787810 | -6.15488 | -55.81068 | 2025-08-08 04:59:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9719fb04-7b55-36b8-81ba-1af842bd54d8 | -6.12962 | -42.95505 | 2025-08-08 04:59:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| b4a7842d-df43-3c71-943e-10ea4568dc67 | -6.96243 | -42.87384 | 2025-08-08 04:59:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 11.3 |
| a4c2f7d3-4255-3e5b-92eb-94d93c2ff170 | -5.87952 | -57.75051 | 2025-08-08 04:59:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f43169b0-9c42-3e30-8058-052022df3731 | -6.96309 | -42.86892 | 2025-08-08 04:59:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 14.1 |
| 971aa53f-8eb9-370d-b248-e009c6336c13 | -9.47183 | -57.85036 | 2025-08-08 04:59:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 820715ba-24e2-3c0b-9900-e34269d16b23 | -7.40412 | -60.00463 | 2025-08-08 04:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 79c97fab-ac6a-3247-ba07-7748d8a30175 | -8.92326 | -60.75295 | 2025-08-08 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 56060466-2ade-30a8-835b-53b6415a7397 | -10.83273 | -49.37854 | 2025-08-08 04:59:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 170e6b20-dbb7-3bc3-9ba6-4e58e86efcd5 | -9.31463 | -62.64211 | 2025-08-08 04:59:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d63d2671-241c-3ac2-81a8-851a97d0f1d6 | -8.20338 | -46.9876 | 2025-08-08 04:59:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c8c979a7-17a8-3156-9f88-de48f9c95bd3 | -8.91824 | -60.75628 | 2025-08-08 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4142d222-e8a4-361a-8f41-f57e24f0bee2 | -8.52705 | -43.31799 | 2025-08-08 04:59:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b54c9fe4-728c-3c41-8cc3-50f02d4d6452 | -7.04919 | -59.17795 | 2025-08-08 04:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 2eaf902f-4210-311e-b41e-b247d00abe6d | -7.04399 | -59.1842 | 2025-08-08 04:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| e4f13d44-291a-3ec6-a714-29544d85ae69 | -10.63462 | -44.76349 | 2025-08-08 04:59:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 68c7110d-623f-327f-8c46-e1778439b9f4 | -10.63762 | -44.73933 | 2025-08-08 04:59:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ae1d2635-14a0-36fa-9698-b5074ac0ff8b | -6.96863 | -42.87467 | 2025-08-08 04:59:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 40d6e376-5de4-326b-911a-07aa8afabe86 | -7.24588 | -44.66126 | 2025-08-08 04:59:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 530cf3ce-105f-3ad5-8bae-6c972d0569fd | -9.65409 | -43.84674 | 2025-08-08 04:59:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 59a890c4-6889-39ff-9195-6b8a95e31042 | -7.91673 | -45.53021 | 2025-08-08 04:59:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6d70fb70-d110-3b45-9b73-722e63728fc0 | -9.31366 | -62.64753 | 2025-08-08 04:59:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d24ea630-d2e5-3358-830c-f71c73bb758c | -8.48599 | -46.00513 | 2025-08-08 04:59:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 34b89400-ed5f-3a32-9cd1-d8b1011de1ad | -9.47322 | -57.84204 | 2025-08-08 04:59:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| e2029a27-415f-326f-b368-16829578c37d | -9.46823 | -57.84974 | 2025-08-08 04:59:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 5ebd9de2-7bf7-332c-8f4a-b256546305c1 | -5.81854 | -59.22497 | 2025-08-08 04:59:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 09b3d828-6540-3568-96b8-2f8d4c5ff80b | -8.92468 | -60.74466 | 2025-08-08 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 201025ec-3e65-3cc4-aede-0f7c2fbd1835 | -8.93041 | -60.73712 | 2025-08-08 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e05a2c4d-e7cd-3e9a-883e-c483579f3bd6 | -7.11672 | -44.2168 | 2025-08-08 04:59:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a00bdcb9-ad2d-3290-962c-26bf3f794d4f | -7.15373 | -44.0745 | 2025-08-08 04:59:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fa6d4652-9364-3746-bf05-fff64758dd00 | -7.37727 | -44.64624 | 2025-08-08 04:59:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 9.3 |
| a307989b-a01d-3566-9de2-9a8980c1a8a4 | -8.9887 | -45.68257 | 2025-08-08 04:59:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6a243f7b-1825-33f9-bae5-3809beff9c3d | -11.80314 | -44.92786 | 2025-08-08 04:59:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c8808ad2-65dc-3e2a-b629-595929925177 | -11.65505 | -46.86974 | 2025-08-08 04:59:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5ecea983-115d-309a-9ead-fa91646cd925 | -8.11034 | -47.43653 | 2025-08-08 04:59:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b75e41cb-fd6d-3726-beb7-0d1910087285 | -10.6236 | -44.75784 | 2025-08-08 04:59:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 57706d77-e00c-3789-bb09-2c9806daac68 | -7.0728 | -59.16046 | 2025-08-08 04:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 56557bb5-72e7-3683-9419-df057099cc69 | -7.81997 | -46.87848 | 2025-08-08 04:59:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b9a52459-c6aa-34f4-8ef1-bd3e5438f154 | -7.81208 | -48.38125 | 2025-08-08 04:59:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 03448520-69c6-308c-89e0-b1bcacbba375 | -7.26081 | -44.3228 | 2025-08-08 04:59:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b6783f93-52f9-34a2-87e0-778746d241aa | -5.80912 | -59.23096 | 2025-08-08 04:59:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c7b1bb77-06f7-369e-8a66-4c7dcd702c5a | -11.80264 | -44.93195 | 2025-08-08 04:59:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 48f97502-6718-30cb-9b90-22271d23cc38 | -10.4344 | -44.35339 | 2025-08-08 04:59:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cccfb873-1441-3fff-b7c6-97860dc36831 | -8.11343 | -47.43355 | 2025-08-08 04:59:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f020aeb8-7c8c-3169-831d-1e5ae709cd71 | -7.25445 | -44.59803 | 2025-08-08 04:59:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |


[Clique aqui para ver as próximas entradas](README19.md)
