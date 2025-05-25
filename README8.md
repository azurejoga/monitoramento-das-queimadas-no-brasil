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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 87629fbc-1dc2-3c20-87a2-711cff9b742c | -19.1023 | -54.45102 | 2025-05-25 04:42:00 | NOAA-21 | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| aab572c1-89c3-3435-823a-a8225109f31c | -14.02001 | -55.12714 | 2025-05-25 04:42:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d265c066-b0fc-380d-8966-5dfa6dee0b2a | -14.20475 | -60.04871 | 2025-05-25 04:42:00 | NOAA-21 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fc86218f-cbda-3830-b549-6a6c7a00c3bb | -19.61635 | -54.42672 | 2025-05-25 04:42:00 | NOAA-21 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 157e43a2-57d8-36c3-b8ce-789e1e404a44 | -14.0349 | -55.12978 | 2025-05-25 04:42:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 2139fdbc-869c-35df-b8ae-8b6bc8016ab0 | -14.02962 | -55.13822 | 2025-05-25 04:42:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ae372a54-5a98-389c-ad84-956bf2173dad | -14.01629 | -55.12648 | 2025-05-25 04:42:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 072d72a4-96a5-33e3-a2bc-7bf676ba5fd1 | -19.95311 | -49.11015 | 2025-05-25 04:42:00 | NOAA-21 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e2b78a35-49af-3ecf-a6ae-6f1f0c5e7b96 | -20.51849 | -51.42178 | 2025-05-25 04:42:00 | NOAA-21 | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| a0687ebc-04bd-38a9-bd18-b49ce764822a | -14.68114 | -52.68579 | 2025-05-25 04:42:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 92b00775-ef41-3f0e-87cd-309a99f3a665 | -19.87609 | -54.3702 | 2025-05-25 04:42:00 | NOAA-21 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 930bb5c0-8d3e-3964-802c-dacdccfe6666 | -17.04629 | -49.0635 | 2025-05-25 04:42:00 | NOAA-21 | BELA VISTA DE GOIÁS | GOIÁS | Brasil | 5203302 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ef94661d-109f-3fbd-afb1-963a545fa882 | -14.0259 | -55.13757 | 2025-05-25 04:42:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 77169a91-729f-3841-a047-7cb03e4a5894 | -16.57798 | -51.54499 | 2025-05-25 04:42:00 | NOAA-21 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| e5d43109-ecb5-30ed-9ada-21e844766dd8 | -14.03784 | -55.13501 | 2025-05-25 04:42:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7bb1fce7-327a-31c7-bfbb-a73d65cf9f0f | -19.37814 | -53.2104 | 2025-05-25 04:42:00 | NOAA-21 | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 50d1ebaa-24c9-3d31-84b2-96cb58269156 | -19.37151 | -53.20921 | 2025-05-25 04:42:00 | NOAA-21 | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 82408181-e713-3a50-a7bd-e9919cf49075 | -14.02139 | -55.14148 | 2025-05-25 04:42:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| be86f21d-1329-3551-b860-80f92157fd99 | -19.02474 | -57.62241 | 2025-05-25 04:42:00 | NOAA-21 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| af16e0e7-9043-3cf7-b258-350ab7d7d4b7 | -20.51569 | -51.41745 | 2025-05-25 04:42:00 | NOAA-21 | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| eb6f04b0-3c0a-38e1-bd8b-4126be31ed3c | -14.04078 | -55.1403 | 2025-05-25 04:42:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 7f6ef8fc-c9c6-3df4-8d99-9244000c4b4c | -14.68174 | -52.68214 | 2025-05-25 04:42:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f64950c4-3ff5-33ec-b29d-05804c4de4d3 | -19.37482 | -53.2098 | 2025-05-25 04:42:00 | NOAA-21 | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d0df8cab-eac5-32a6-b5ab-a7857bc54e19 | -16.68069 | -43.88622 | 2025-05-25 04:42:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 20d3c63c-72b8-3727-8cbc-95d66e78cbfd | -19.36761 | -53.21228 | 2025-05-25 04:42:00 | NOAA-21 | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0f2a4b32-d303-30eb-abda-a99141f372e8 | -14.67779 | -52.68522 | 2025-05-25 04:42:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 5a83cff9-f78f-3e14-a7ac-bab547088f55 | -14.04257 | -55.13866 | 2025-05-25 04:42:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 2d8017cc-8e00-35f3-8c83-0af2bae29884 | -14.01923 | -55.13169 | 2025-05-25 04:42:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 72b47275-8706-3ee4-a8dc-fc51dd7f3897 | -17.15679 | -54.00709 | 2025-05-25 04:42:00 | NOAA-21 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3bdec1b6-c92b-37ce-8cf2-6f18880e9007 | -15.0792 | -48.9435 | 2025-05-25 04:42:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 689adb3a-a4ce-3767-840d-700da598f257 | -15.63081 | -57.30564 | 2025-05-25 04:42:00 | NOAA-21 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| df5a85f4-4584-369c-8f57-f3fe6e256e6c | -19.10295 | -54.44718 | 2025-05-25 04:42:00 | NOAA-21 | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1133debf-4aba-3f21-adc3-172457292ac1 | -14.68844 | -52.68327 | 2025-05-25 04:42:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e2200495-b394-3797-8da8-47653efa5ce9 | -20.51513 | -51.42122 | 2025-05-25 04:42:00 | NOAA-21 | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| 79a6db5f-19d7-39d4-8c0f-e3ef5aa9e357 | -14.03862 | -55.13047 | 2025-05-25 04:42:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| df1bf88b-e5e6-3295-9cc4-d18851e84d23 | -16.67981 | -43.88637 | 2025-05-25 04:42:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1a6f0a40-ed4c-3ff2-b5de-897fcb5758d1 | -14.03707 | -55.13958 | 2025-05-25 04:42:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| da953c09-f9ca-3f9c-a718-fbf1f6bec712 | -19.87947 | -54.37081 | 2025-05-25 04:42:00 | NOAA-21 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c2307199-e85e-3302-95dc-d191735fc0be | -19.61975 | -54.42735 | 2025-05-25 04:42:00 | NOAA-21 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0085d640-36ff-3969-9149-97b546ed400b | -14.01551 | -55.13102 | 2025-05-25 04:42:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c71d8fd7-7b00-30a9-9b3e-00fc69b31209 | -15.62803 | -57.30984 | 2025-05-25 04:42:00 | NOAA-21 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1e9e193e-4148-3bbe-9bae-8d6f41a44e17 | -20.47805 | -53.67548 | 2025-05-25 04:42:00 | NOAA-21 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a8d6b234-cfb8-3b86-b5df-2222b10e0bc8 | -14.20415 | -60.0518 | 2025-05-25 04:42:00 | NOAA-21 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 632dc75d-43c9-30df-ab34-fc548d443757 | -15.89762 | -48.07288 | 2025-05-25 04:42:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ddffeeb5-c284-38a6-ada1-7cf216621ce2 | -14.20534 | -60.04564 | 2025-05-25 04:42:00 | NOAA-21 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0693bcae-a94f-3a32-89ad-751fd00ddd32 | -18.39101 | -44.19023 | 2025-05-25 04:42:00 | NOAA-21 | SANTO HIPÓLITO | MINAS GERAIS | Brasil | 3160603 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f914bb5d-eb0a-3d22-8d4f-ddad0f142509 | -18.85262 | -46.73834 | 2025-05-25 04:42:00 | NOAA-21 | GUIMARÂNIA | MINAS GERAIS | Brasil | 3128907 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 98f28e42-7c57-3985-9dcb-305bd69dea91 | -15.63004 | -57.30973 | 2025-05-25 04:42:00 | NOAA-21 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f50829d6-7677-365e-8318-8d0a62c1b398 | -17.77948 | -42.80946 | 2025-05-25 04:42:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b28c8c61-1edd-389f-8d88-1b8c25b8bf17 | -14.03334 | -55.1389 | 2025-05-25 04:42:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3f66a656-0db1-3c22-a8ca-0f9887eef481 | -14.03412 | -55.13433 | 2025-05-25 04:42:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3607d522-d5bf-3e05-accf-34e2fd4c1ed4 | -20.70833 | -50.06751 | 2025-05-25 04:42:00 | NOAA-21 | NHANDEARA | SÃO PAULO | Brasil | 3532603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 14.7 |
| faa3db99-c04c-3cc8-9f13-4061456ccf46 | -14.47084 | -56.32004 | 2025-05-25 04:42:00 | NOAA-21 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 63dab4b5-9119-3351-b2bc-cffaf4caf30d | -18.63912 | -47.15406 | 2025-05-25 04:42:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b05d8254-4f78-351f-9a3f-5d059f7be582 | -16.37532 | -46.87553 | 2025-05-25 04:42:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 77fa5408-c87b-3144-816e-f06fc4ba5bdb | -16.57468 | -51.54444 | 2025-05-25 04:42:00 | NOAA-21 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 39cfcfac-edf4-33e5-aade-b468b6667d2d | -15.62876 | -57.30576 | 2025-05-25 04:42:00 | NOAA-21 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 588c28aa-5254-3034-88cd-9428f34d2ddf | -19.9525 | -49.11462 | 2025-05-25 04:42:00 | NOAA-21 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fff0f027-6460-3b5c-b910-a876a063ad03 | -14.68509 | -52.6827 | 2025-05-25 04:42:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3be1a9c5-6ce2-3e36-94c1-52c9876d8923 | -17.61781 | -54.17496 | 2025-05-25 04:42:00 | NOAA-21 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c9a5ff6e-1fc8-35e9-9c76-a7b97d782ab7 | -23.33951 | -46.77161 | 2025-05-25 04:44:00 | NOAA-21 | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 6dc3360e-bfd6-34d7-add8-287dd4d25314 | -20.93993 | -56.5935 | 2025-05-25 04:44:00 | NOAA-21 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 23.7 |
| e7672e5d-3341-35de-91e5-5feebebd7c2d | -21.63114 | -49.78145 | 2025-05-25 04:44:00 | NOAA-21 | GUAIÇARA | SÃO PAULO | Brasil | 3517208 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| fc484116-b88d-38cb-a940-80f0f0f466b1 | -21.18658 | -53.18221 | 2025-05-25 04:44:00 | NOAA-21 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 607f51e5-bc6f-3cee-8213-10a4ff26b293 | -20.94358 | -56.59422 | 2025-05-25 04:44:00 | NOAA-21 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 1ba02b46-47e8-3da0-a2d9-c4e6c0953a83 | -22.08044 | -51.40538 | 2025-05-25 04:44:00 | NOAA-21 | PRESIDENTE PRUDENTE | SÃO PAULO | Brasil | 3541406 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 669701f3-f2d5-344a-896a-4b67dbe30b85 | -21.62931 | -49.78264 | 2025-05-25 04:44:00 | NOAA-21 | GUAIÇARA | SÃO PAULO | Brasil | 3517208 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 67e05ccc-389c-38a6-bbf2-b448479790d1 | -22.31179 | -48.54779 | 2025-05-25 04:44:00 | NOAA-21 | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 8a21c772-e9cf-339c-9fc8-10e858ee7cfd | -20.94276 | -56.59882 | 2025-05-25 04:44:00 | NOAA-21 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 871fee27-b3a3-3ed4-8f4e-e0dd74d95d92 | -20.9391 | -56.59812 | 2025-05-25 04:44:00 | NOAA-21 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 053141d9-e8d8-348a-a6cd-19a6a21fc0a1 | -21.6329 | -49.78323 | 2025-05-25 04:44:00 | NOAA-21 | GUAIÇARA | SÃO PAULO | Brasil | 3517208 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 7da8313d-2922-3221-a72c-0f5a98636053 | -23.35372 | -52.30335 | 2025-05-25 04:44:00 | NOAA-21 | SÃO JORGE DO IVAÍ | PARANÁ | Brasil | 4125308 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 27c9fc33-7bd1-3257-a4df-0c66d0c4d725 | -21.6335 | -49.77884 | 2025-05-25 04:44:00 | NOAA-21 | GUAIÇARA | SÃO PAULO | Brasil | 3517208 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| b4264deb-6d6a-3b9c-96c5-5992e0f60a38 | -22.53923 | -48.81166 | 2025-05-25 04:44:00 | NOAA-21 | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a87994d1-ac60-396c-8322-3d3fb8ba8a38 | -23.76633 | -54.52753 | 2025-05-25 04:44:00 | NOAA-21 | JAPORÃ | MATO GROSSO DO SUL | Brasil | 5004809 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| b1e70d3e-a699-3ba3-a764-45b6116db430 | -20.95372 | -56.60099 | 2025-05-25 04:44:00 | NOAA-21 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9861906a-e93a-3125-84ff-0f94deb95745 | -24.24334 | -50.73928 | 2025-05-25 04:44:00 | NOAA-21 | ORTIGUEIRA | PARANÁ | Brasil | 4117305 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 2d13b8a9-f34b-31cd-87bf-4f6cf2ccb239 | -23.61253 | -49.00663 | 2025-05-25 04:44:00 | NOAA-21 | ITAÍ | SÃO PAULO | Brasil | 3521804 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e27855a8-55c6-34af-a464-b86a1b3c4f33 | -21.90892 | -55.84892 | 2025-05-25 04:44:00 | NOAA-21 | PONTA PORÃ | MATO GROSSO DO SUL | Brasil | 5006606 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0bb5939d-fe39-3e6f-abb1-5b94766e177b | -23.98606 | -48.9197 | 2025-05-25 04:44:00 | NOAA-21 | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9f2dee98-2297-31bc-b911-974cce5ffe4c | -23.59162 | -47.3891 | 2025-05-25 04:44:00 | NOAA-21 | VOTORANTIM | SÃO PAULO | Brasil | 3557006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 8a15c47e-0f8b-3755-bab8-5fa81d08b3ed | -7.6574 | -46.1013 | 2025-05-25 04:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 37.3 |
| 7ce66024-79e5-3a80-b618-14725f426758 | -7.6574 | -46.1013 | 2025-05-25 05:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 85.6 |
| e32884c5-bb4f-3ba3-955a-c2b697c1c8f4 | -5.58509 | -45.19539 | 2025-05-25 05:04:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a71d59a0-2315-307c-92c0-47c7c792801a | -6.23042 | -43.35592 | 2025-05-25 05:04:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e1483513-5665-3336-bbd5-c7ec80a21860 | -4.28813 | -48.26897 | 2025-05-25 05:04:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 04463dd8-dbbb-39cf-a8d1-008843bf9b1a | -4.30677 | -47.55802 | 2025-05-25 05:04:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8e47eaf5-03ac-3586-bb1a-4aaf90099e9a | -5.6808 | -44.12502 | 2025-05-25 05:04:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 46a3d13b-278d-351d-a7a2-ba07f50afb25 | -5.60605 | -45.33408 | 2025-05-25 05:04:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3352c166-fbfe-316a-b562-de836878b7f3 | -5.61187 | -45.33488 | 2025-05-25 05:04:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4734e97e-0db6-30fd-954a-400ef6e59b51 | -4.2928 | -48.26965 | 2025-05-25 05:04:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 1ff16930-297a-33c5-81c6-111bfdfc3568 | -4.28742 | -48.27375 | 2025-05-25 05:04:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 650d021b-54a9-32c1-b257-da68f5ae1570 | -5.60709 | -45.33284 | 2025-05-25 05:04:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 88d3d75c-df9e-3c72-8df4-2824d87ab4ef | -4.29208 | -48.27444 | 2025-05-25 05:04:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 270f38cf-a54b-3dfc-9b23-cf6bf7b62938 | -6.22381 | -43.35478 | 2025-05-25 05:04:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 35b0eac5-bd8d-3811-9e9d-d4aeb0c15ef3 | -2.65496 | -48.79647 | 2025-05-25 05:04:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c4f1d407-1331-3f93-b8b6-3a2523a0bd98 | -3.70922 | -53.7515 | 2025-05-25 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6e2fbc37-0e45-3881-9366-fa9bb6bd4c4a | -5.68708 | -44.12587 | 2025-05-25 05:04:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8990c17f-09b8-39dd-853d-b9a7edecb21a | -5.5845 | -45.19957 | 2025-05-25 05:04:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b7b1551f-2017-3af4-9f76-7eec5ad94659 | -4.30877 | -47.559 | 2025-05-25 05:04:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README9.md)
