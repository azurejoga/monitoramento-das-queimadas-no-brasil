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
| e084d328-9711-3df0-85f2-b38aa70ec14c | -7.91459 | -45.54426 | 2025-08-08 03:42:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 333b30ce-486d-3767-8259-12d5dcbf766d | -6.56552 | -42.80369 | 2025-08-08 03:42:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 6ced263a-0c06-3881-8293-af115b292615 | -9.06762 | -45.06471 | 2025-08-08 03:42:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 7b9255c5-1ed4-3240-bbc1-0a8b68b49d0d | -6.96725 | -42.87159 | 2025-08-08 03:42:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 11.9 |
| 3d40f7bf-8dc9-3df1-a0af-ea0b800d1ca4 | -8.52302 | -43.31455 | 2025-08-08 03:42:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 11.9 |
| eeeac7ec-aec1-36e9-b8fe-90e2bd608475 | -5.28428 | -41.7716 | 2025-08-08 03:42:00 | NOAA-20 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| f2df10fc-36a4-3f30-a0fb-08e7aeb5c918 | -9.33207 | -37.98219 | 2025-08-08 03:42:00 | NOAA-20 | ÁGUA BRANCA | ALAGOAS | Brasil | 2700102 | 27 | 33 | nan | nan | nan | Caatinga | 1.0 |
| ad7fb77f-bea5-37fb-a068-922286278df3 | -8.19807 | -46.98653 | 2025-08-08 03:42:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b8652461-5a78-37b0-82e6-df2f4d725a26 | -10.6261 | -44.75806 | 2025-08-08 03:42:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 45b348b5-59d2-37ed-9d93-1eef8544a84c | -8.93275 | -46.74902 | 2025-08-08 03:42:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| e492266d-09a1-397c-852c-250923b8a0b1 | -10.43222 | -44.35416 | 2025-08-08 03:42:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7bcadbed-5afe-3428-bd79-90065d681374 | -9.07225 | -45.06937 | 2025-08-08 03:42:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| f7232684-0084-3471-aa11-38f6fdf58b9d | -7.25453 | -44.33289 | 2025-08-08 03:42:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| da3377d0-7c97-313a-b3a8-85035b89de0f | -7.32888 | -44.70168 | 2025-08-08 03:42:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2e358633-5262-360d-9269-03128ce816c4 | -10.5783 | -45.25359 | 2025-08-08 03:42:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 067b1f9c-34f0-3103-b942-5564094e61a0 | -8.24984 | -45.07154 | 2025-08-08 03:42:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 503fbb65-e104-38dc-84e7-19df0a24377a | -8.21053 | -45.06085 | 2025-08-08 03:42:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fef4fe0f-dfe6-34ae-a445-975633a32daf | -8.52394 | -43.30943 | 2025-08-08 03:42:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 88e490a9-816a-3742-be00-a0c2694556b1 | -6.84373 | -44.30673 | 2025-08-08 03:42:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7c86639c-225d-3e15-846f-6fe111c482e2 | -10.62051 | -44.76006 | 2025-08-08 03:42:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3bed80d5-a9b3-308c-9cd9-4cf1e221ee87 | -8.33459 | -36.31588 | 2025-08-08 03:42:00 | NOAA-20 | TACAIMBÓ | PERNAMBUCO | Brasil | 2614709 | 26 | 33 | nan | nan | nan | Caatinga | 1.1 |
| bd47ce6f-7d20-3d88-b622-45fcd027b185 | -7.81982 | -46.88236 | 2025-08-08 03:42:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8444542d-2d7c-31e8-93df-2695b1c5cac0 | -7.37687 | -44.64814 | 2025-08-08 03:42:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 120e0922-b773-3b18-b1c0-f9ece316ac24 | -9.06639 | -45.07156 | 2025-08-08 03:42:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 72b15978-dcd5-33ca-a1f8-dba686bcf9e7 | -9.61854 | -40.59124 | 2025-08-08 03:42:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 10.5 |
| e18ac4a7-55fb-373a-a8df-4f8859a51f18 | -4.91829 | -46.73472 | 2025-08-08 03:42:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 93a638bd-05a0-3a21-b335-69179faf4c9f | -7.11451 | -44.2106 | 2025-08-08 03:42:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4a483d0c-78af-3fda-a4a7-110e16d0fcd2 | -6.5566 | -39.0146 | 2025-08-08 03:42:00 | NOAA-20 | CEDRO | CEARÁ | Brasil | 2303808 | 23 | 33 | nan | nan | nan | Caatinga | 5.4 |
| ae666196-f591-31be-9561-020cb3b88dc1 | -8.86479 | -47.27578 | 2025-08-08 03:42:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4bf3f481-0e5e-3551-b5e0-60a464c2fb89 | -7.37746 | -44.64482 | 2025-08-08 03:42:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9e5b9c01-7838-3a0d-b6e0-b2264f66f2d8 | -10.63564 | -44.76297 | 2025-08-08 03:42:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b5f3ce72-57f0-383f-a6e6-659b46dbafd7 | -8.20688 | -45.06376 | 2025-08-08 03:42:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 257df994-5661-3e76-a291-84262be71680 | -8.32532 | -46.57658 | 2025-08-08 03:42:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 687f3950-5747-3208-9722-729fd237f7b9 | -9.55717 | -47.88472 | 2025-08-08 03:42:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9341937b-8f12-3f55-8de6-880ea624e2cd | -7.11158 | -44.22712 | 2025-08-08 03:42:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7a5a6ddd-4121-3a17-bfe7-14b71f5ee6d4 | -7.38795 | -44.24707 | 2025-08-08 03:42:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 84fadf9e-0f61-3786-ad65-df6f26189603 | -9.07014 | -45.0727 | 2025-08-08 03:42:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 81cc1941-1ec4-3dd5-9016-60d3ccd86129 | -9.65322 | -43.84735 | 2025-08-08 03:42:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| b9a1e172-7039-3839-9640-33ec1735295f | -10.63061 | -44.76196 | 2025-08-08 03:42:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 15.4 |
| f3c0864c-6c90-38b3-b69e-5766751a5a4b | -6.46522 | -44.57974 | 2025-08-08 03:42:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 27e6230c-256a-30b5-9355-eb1b61cddcdf | -10.4818 | -44.33361 | 2025-08-08 03:42:00 | NOAA-20 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e383ed4d-f761-3eb6-9479-b407141d466f | -7.11278 | -44.22032 | 2025-08-08 03:42:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d547d9bc-4bc3-3e6d-a227-168e45097c8f | -6.96278 | -42.86305 | 2025-08-08 03:42:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 9.5 |
| 3e7fb745-87c0-3675-b0ba-46d5a81d9ccf | -7.11337 | -44.21701 | 2025-08-08 03:42:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c114fb8d-beb0-360c-a6fa-e6be07a08664 | -8.52203 | -43.318 | 2025-08-08 03:42:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 5c18266b-e5e3-32d5-84a5-a8c100a0f3dc | -9.61769 | -40.59624 | 2025-08-08 03:42:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 10.5 |
| a28974d0-3905-353d-a4e7-51fe56149864 | -8.20754 | -45.06023 | 2025-08-08 03:42:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2a7b0438-ef1a-3515-a49d-9f97ba8e5ebf | -7.91451 | -45.53565 | 2025-08-08 03:42:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 11b17443-f95a-304d-90de-4b37611cb77f | -9.0721 | -45.06222 | 2025-08-08 03:42:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 39f76c0b-75a5-34b7-96f5-eb6ccbe6a678 | -9.06556 | -45.06791 | 2025-08-08 03:42:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 9cdf46d0-ff35-3b8e-94cc-b9f83e721dac | -9.06428 | -45.07471 | 2025-08-08 03:42:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| fc27be25-4fbf-3c8b-bb78-aad878e618a2 | -9.06492 | -45.07129 | 2025-08-08 03:42:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| b0600617-dc4e-3e98-ac7e-dd7e3c7d0d76 | -8.9785 | -40.6174 | 2025-08-08 03:42:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 5e1b03cd-b669-38ee-a924-f01efbcd53dc | -7.02067 | -42.55159 | 2025-08-08 03:42:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 71868c85-82cd-326e-b909-36a848855adf | -10.60933 | -44.76406 | 2025-08-08 03:42:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 7a1880b6-df28-3f9b-abef-24ff4633e74f | -10.63332 | -44.74709 | 2025-08-08 03:42:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ee85f236-de5b-30b9-ad25-65dc7c96bb55 | -10.61438 | -44.76504 | 2025-08-08 03:42:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2d2382de-af09-33e7-96d2-72ff0594898a | -7.14747 | -44.48011 | 2025-08-08 03:42:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c5d1564d-2605-36a4-a2f1-305cc550f333 | -9.07288 | -45.06585 | 2025-08-08 03:42:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 84fdb514-9e2f-31a0-afe9-f75ee215aa1b | -9.0674 | -45.05811 | 2025-08-08 03:42:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 718a10ad-e496-3d21-8c65-87f0c643deea | -6.15126 | -44.54204 | 2025-08-08 03:42:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6e461672-1666-3155-a0d9-7ff7c45e4dfd | -6.96665 | -42.86894 | 2025-08-08 03:42:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 11.5 |
| d69c8072-96cf-3625-99aa-8eee1f13251d | -9.62243 | -40.59192 | 2025-08-08 03:42:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 96.7 |
| 9901cf9b-9ac7-3630-a20f-7def7e21bea9 | -4.91916 | -46.72988 | 2025-08-08 03:42:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cd7aee65-145c-31f9-81d4-23853e2b8c30 | -6.31756 | -42.36423 | 2025-08-08 03:42:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 66215230-6acc-3b62-9316-1dfa515c4151 | -7.38468 | -44.24496 | 2025-08-08 03:42:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fc3d617f-93ff-3715-b114-456953ad3906 | -7.90621 | -45.54933 | 2025-08-08 03:42:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 741c3cd3-cf88-3e6a-801c-9bf10aabcf27 | -8.85866 | -47.27472 | 2025-08-08 03:42:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2feac61e-6270-3c05-801d-7291bab8128d | -7.23394 | -44.48193 | 2025-08-08 03:42:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| daf3c34e-51ad-3467-ac3f-14b3c4a44ddb | -7.91799 | -45.54792 | 2025-08-08 03:42:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8e0c848d-e2d1-3b78-adcd-cb5c6b3a9318 | -7.25442 | -44.33666 | 2025-08-08 03:42:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 38819dca-ddca-3262-a945-cd403ddc7be1 | -9.47743 | -46.3008 | 2025-08-08 03:42:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d210c528-07a9-3cb4-9cd2-d0499c29c0ff | -6.52205 | -45.55164 | 2025-08-08 03:42:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 990567b1-32c4-32ac-a83c-31809e21a823 | -6.79684 | -43.24644 | 2025-08-08 03:42:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 7.2 |
| 2d7ef747-4ba5-36a5-b6ef-6d0dfd1fcdfe | -8.19726 | -46.99097 | 2025-08-08 03:42:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 46fc2d59-09ce-3fc9-9c99-69945c037c17 | -4.91571 | -46.733 | 2025-08-08 03:42:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3982a0fc-34f2-3201-9a9d-bc436f070f8d | -10.61493 | -44.76203 | 2025-08-08 03:42:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ea5ae45f-a962-358f-a9c7-e0553ec39388 | -7.22967 | -44.65261 | 2025-08-08 03:42:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 60668776-24f2-3591-95f2-598f69a0ee37 | -9.06822 | -45.06138 | 2025-08-08 03:42:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 152b0636-9521-38f4-83b7-862a44ba7735 | -7.9005 | -45.33635 | 2025-08-08 03:42:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8e5cfd11-ff2f-34a1-8a58-886d3b951406 | -10.63946 | -44.74201 | 2025-08-08 03:42:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a29f4e02-51a2-34eb-9137-884ae1bb477c | -6.57112 | -42.79963 | 2025-08-08 03:42:00 | NOAA-20 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| dd046759-f392-3055-847d-a25cf183a32e | -8.20991 | -45.06436 | 2025-08-08 03:42:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d71f556d-494f-3ea2-9fed-ebf9294ed20d | -7.91383 | -45.53933 | 2025-08-08 03:42:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c7475ddb-2d19-3af3-938b-dbba0c2facee | -9.64944 | -43.84069 | 2025-08-08 03:42:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| fa843428-8989-3e95-9e1a-7bdc7fa881be | -7.39671 | -39.67908 | 2025-08-08 03:42:00 | NOAA-20 | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 7d3202b6-465b-35fc-9365-9408abdd5398 | -7.37627 | -44.65148 | 2025-08-08 03:42:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 2616c681-ce94-36c7-b7c8-9acaf605f441 | -7.37945 | -44.24442 | 2025-08-08 03:42:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b5a11bcc-4479-39b3-80de-14ab896b7988 | -10.63619 | -44.76 | 2025-08-08 03:42:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 1dac1a1b-ecd5-3b1d-a4ee-e8046fb633fb | -7.23921 | -44.48276 | 2025-08-08 03:42:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 677e155f-9351-34fb-940c-ed0c831786bf | -7.03289 | -42.5565 | 2025-08-08 03:42:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 8ac14f82-4477-3d0d-9b26-ab8e5bd8179e | -9.06053 | -45.07367 | 2025-08-08 03:42:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2abaef2f-fd5f-3e4b-9b5b-3d3be9254116 | -6.57073 | -42.79709 | 2025-08-08 03:42:00 | NOAA-20 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 7bde1e98-b9bc-30bc-8406-094950f6e7c9 | -8.52292 | -43.31286 | 2025-08-08 03:42:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 93d5c298-8c58-38c9-babe-7cce9d459d3a | -10.63442 | -44.74107 | 2025-08-08 03:42:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c8d926bd-c6d2-3a8e-8530-c1a361034446 | -6.65256 | -42.0041 | 2025-08-08 03:42:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| f5cc0ec1-c379-3e0d-8116-212922785b76 | -7.11395 | -44.21375 | 2025-08-08 03:42:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9ff951ee-6d10-3fc6-8c83-0b1466b31b01 | -7.2243 | -44.65196 | 2025-08-08 03:42:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 54d7af90-faf0-3936-a57b-caf5b3bb1440 | -5.28351 | -41.77619 | 2025-08-08 03:42:00 | NOAA-20 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| cf178951-ac8d-3228-9512-ee7ffa43bcbe | -5.28053 | -41.76625 | 2025-08-08 03:42:00 | NOAA-20 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |


[Clique aqui para ver as próximas entradas](README9.md)
