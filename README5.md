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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 32d0741b-96f1-316c-bb58-e809f820bd10 | -4.26364 | -43.76217 | 2026-01-08 04:14:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| dfc1293f-8756-3b22-9793-7530b0c38f2b | -3.48304 | -42.42854 | 2026-01-08 04:14:00 | NOAA-20 | JOCA MARQUES | PIAUÍ | Brasil | 2205458 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 18b3cba9-eca0-329d-b195-f61ed9659f63 | -2.63974 | -44.67258 | 2026-01-08 04:14:00 | NOAA-20 | BACURITUBA | MARANHÃO | Brasil | 2101350 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6372b5be-ecab-3df0-a74f-fcf383c7becf | -2.66754 | -42.7303 | 2026-01-08 04:14:00 | NOAA-20 | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| a3864577-9af4-3e63-bd19-8355724e86b8 | -4.27142 | -43.77784 | 2026-01-08 04:14:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6a357a9b-d2dd-3aad-9d4f-0e89231597b0 | -4.27977 | -43.76835 | 2026-01-08 04:14:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| c56c8974-5cc6-3afd-ae84-a0d28787994c | -5.0398 | -43.26091 | 2026-01-08 04:14:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 552d92da-1c8d-3783-b4bb-6bff009a0ad7 | -5.04087 | -42.5009 | 2026-01-08 04:14:00 | NOAA-20 | ALTOS | PIAUÍ | Brasil | 2200400 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| cb381991-d217-3bea-80ea-f068a1693e35 | -3.70362 | -46.98042 | 2026-01-08 04:14:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 3fcad5e8-60fa-32e8-bac5-86a2b661496a | -3.66115 | -44.81349 | 2026-01-08 04:14:00 | NOAA-20 | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 0c2edf41-0ea4-36ef-86ad-df893b130841 | -3.43703 | -44.83373 | 2026-01-08 04:14:00 | NOAA-20 | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| abffde37-195d-30c6-9bcf-519968140eba | -4.9663 | -40.58261 | 2026-01-08 04:14:00 | NOAA-20 | TAMBORIL | CEARÁ | Brasil | 2313203 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 0daf1089-8f8c-359d-bb17-ff8cc79760d5 | -3.20232 | -46.82417 | 2026-01-08 04:14:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| de9a1370-5095-376a-b77f-99374e91e804 | -4.27309 | -43.7673 | 2026-01-08 04:14:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 944ab584-127c-360f-8a2b-26fc1d9870c2 | -3.70441 | -46.9756 | 2026-01-08 04:14:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 870a8912-3eff-358d-88f3-e1e241d24eb1 | -5.17382 | -37.76181 | 2026-01-08 04:14:00 | NOAA-20 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 0.5 |
| cb84f413-cda3-3580-b393-a3a59a05fea8 | -4.03727 | -38.20655 | 2026-01-08 04:14:00 | NOAA-20 | CASCAVEL | CEARÁ | Brasil | 2303501 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| e5b2e3a8-4255-32e5-88b5-a562b400197e | -3.73438 | -44.55269 | 2026-01-08 04:14:00 | NOAA-20 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bf63c655-64ca-3bd3-8511-ee46b6de311d | -7.75372 | -41.39471 | 2026-01-08 04:14:00 | NOAA-20 | PATOS DO PIAUÍ | PIAUÍ | Brasil | 2207777 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 40fd698a-41b0-35bf-b839-47f95941ce8b | -3.70748 | -46.98103 | 2026-01-08 04:14:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 88b3302b-c514-3ae3-975a-760c88462266 | -6.9702 | -40.95829 | 2026-01-08 04:14:00 | NOAA-20 | ALAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2200251 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 4b9293eb-f920-3632-8d6c-b03bd3090635 | -6.3424 | -43.3794 | 2026-01-08 04:14:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7baa5cbe-fa38-374e-b3a6-3cfb49156bdd | -2.93811 | -41.79154 | 2026-01-08 04:14:00 | NOAA-20 | PARNAÍBA | PIAUÍ | Brasil | 2207702 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b3eeb582-22a9-311b-9159-39cdffe074a7 | -6.61136 | -39.38771 | 2026-01-08 04:14:00 | NOAA-20 | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 3f2065c2-fe8e-3ae2-8a07-2db65c948974 | -4.27588 | -43.77134 | 2026-01-08 04:14:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 16.6 |
| dc8e0cad-d4bb-3563-a64f-8d6c8c9b007e | -5.09516 | -37.95776 | 2026-01-08 04:14:00 | NOAA-20 | QUIXERÉ | CEARÁ | Brasil | 2311504 | 23 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 08a85481-a05e-3609-bed3-76aba24c031c | -4.27198 | -43.77432 | 2026-01-08 04:14:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 16.6 |
| a6a28639-dcbc-360d-a9f8-03c1ef43f885 | -4.28534 | -43.77645 | 2026-01-08 04:14:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b4d12f7a-40af-327b-84b9-f522f48328a3 | -1.69676 | -45.22959 | 2026-01-08 04:14:00 | NOAA-20 | BACURI | MARANHÃO | Brasil | 2101301 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8905a251-ac7b-373f-9111-b080a1af9409 | -5.09821 | -37.95831 | 2026-01-08 04:14:00 | NOAA-20 | QUIXERÉ | CEARÁ | Brasil | 2311504 | 23 | 33 | nan | nan | nan | Caatinga | 2.9 |
| f818f6e2-6c19-32b6-9691-3066c86d26c5 | -2.66423 | -42.72977 | 2026-01-08 04:14:00 | NOAA-20 | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| a41467c4-262f-3a65-a8ec-debea1a3edf4 | -5.03925 | -43.26437 | 2026-01-08 04:14:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5619b5ca-e391-3fce-8980-229efd2ab684 | -4.28144 | -43.77943 | 2026-01-08 04:14:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f7990d54-b219-3a24-a89c-172a0427489c | -3.23185 | -41.80147 | 2026-01-08 04:14:00 | NOAA-20 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| d5ce7e72-a9db-33c2-b1fa-3861f7b7a83c | -3.06924 | -41.88596 | 2026-01-08 04:14:00 | NOAA-20 | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 1ea002ff-d668-3c3d-8cd8-c217605ae61c | -4.2653 | -43.77326 | 2026-01-08 04:14:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 39cbbb06-11d6-3841-b6a4-9425e57b60be | -3.2324 | -41.79799 | 2026-01-08 04:14:00 | NOAA-20 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| c14f65eb-bd8f-3dd8-87c2-c2c878c3e616 | -3.65769 | -44.81294 | 2026-01-08 04:14:00 | NOAA-20 | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 8e592e44-d458-362a-9e29-16efb0eb6efe | -5.38374 | -45.39219 | 2026-01-08 04:14:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| fdb223f1-e3aa-35aa-a3fd-a72e9c13c932 | -1.6722 | -45.78049 | 2026-01-08 04:14:00 | NOAA-20 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| efe86eba-d239-3b11-9002-757bae26f969 | -5.09419 | -37.95763 | 2026-01-08 04:14:00 | NOAA-20 | QUIXERÉ | CEARÁ | Brasil | 2311504 | 23 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 7e144133-677c-34bf-b305-447efa8cef10 | -6.45881 | -46.42269 | 2026-01-08 04:14:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 9155850a-9c46-3c5d-9651-f8c8b2c17ce1 | -5.32379 | -37.59473 | 2026-01-08 04:14:00 | NOAA-20 | GOVERNADOR DIX-SEPT ROSADO | RIO GRANDE DO NORTE | Brasil | 2404309 | 24 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 89fd8458-7a72-310a-b871-18f1b0c9cfe6 | -2.8983 | -52.63355 | 2026-01-08 04:14:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 10573bca-92ab-342e-843b-77b9821e2a92 | -4.11847 | -43.88386 | 2026-01-08 04:14:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e4870e35-9849-36ca-a611-ccb87e947e37 | -6.06575 | -39.18567 | 2026-01-08 04:14:00 | NOAA-20 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 6517bbe8-f748-3929-92a0-f3db7478e887 | -5.67018 | -45.20695 | 2026-01-08 04:14:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6ae0c7b7-cbc4-3b85-aa66-1fc37dbe9761 | -3.19768 | -46.82832 | 2026-01-08 04:14:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1fce5773-c507-32fc-bf82-5187cf455c97 | -4.27031 | -43.76325 | 2026-01-08 04:14:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4e8fac95-74a3-311b-9f0e-ea5491b0c453 | -5.94358 | -44.44926 | 2026-01-08 04:14:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9ba564a5-5799-3de6-85a0-32c9ea66b6f3 | -4.27365 | -43.76378 | 2026-01-08 04:14:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 32f5e310-cb09-3609-8707-3237cd7d6283 | -3.56215 | -47.18077 | 2026-01-08 04:14:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b595b701-c7e7-3003-93db-8b6cf1b4e79d | -4.28311 | -43.76888 | 2026-01-08 04:14:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| f7699810-38cf-322d-b096-5309a9d5d667 | -1.92807 | -45.18813 | 2026-01-08 04:14:00 | NOAA-20 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 035c1fcb-68d0-31a8-bb51-62fa1eb9a660 | -5.10584 | -43.14397 | 2026-01-08 04:14:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f41d33c9-5510-3533-8eb7-2a75c0ad694a | -4.25918 | -43.76867 | 2026-01-08 04:14:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| e18a4802-a536-3828-8186-5ff96d5c1fcc | -4.28478 | -43.77997 | 2026-01-08 04:14:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fde2067d-7b68-362e-badd-45e53a429f71 | -3.19691 | -46.8331 | 2026-01-08 04:14:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0ad2dc8a-2628-3ff9-925a-7dc7723a2c43 | -5.24623 | -37.50386 | 2026-01-08 04:14:00 | NOAA-20 | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 0.7 |
| cd4705cf-833c-3c3a-9c62-af212598243b | -3.23572 | -41.79851 | 2026-01-08 04:14:00 | NOAA-20 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| eafb8aee-d24d-320c-833b-34b7b431e3da | -4.26252 | -43.7692 | 2026-01-08 04:14:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 93ce226f-1e45-3903-b38b-337a5d6dd812 | -6.58558 | -44.62103 | 2026-01-08 04:14:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c7bd8675-3a1a-3692-bf5c-72c23564bfcb | -4.37224 | -46.37865 | 2026-01-08 04:14:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f4a71913-9b7a-3e35-88c5-9a725359379a | -4.26642 | -43.76622 | 2026-01-08 04:14:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6ae5edc2-09a9-3db9-a1c8-0c1c6843d0d9 | -6.41364 | -43.4651 | 2026-01-08 04:14:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 624612da-72d1-37ae-818a-62be1690d1e5 | -4.60046 | -45.99233 | 2026-01-08 04:14:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 6.2 |
| cdc2e6fb-7ffe-3c82-b813-2e64718c549b | -5.49089 | -45.10174 | 2026-01-08 04:14:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ac8bb852-7939-3362-a7dc-52e08c28a42b | -1.9245 | -45.18756 | 2026-01-08 04:14:00 | NOAA-20 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2ef08139-edbd-3a42-8644-7d065ae2d230 | -6.61155 | -39.38942 | 2026-01-08 04:14:00 | NOAA-20 | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| a2bf486e-c310-3465-a2c2-e6ef4724b25c | -5.58334 | -43.7523 | 2026-01-08 04:14:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0c18f95a-ffc1-3045-8a84-9c13ae102a1e | -5.38721 | -45.39277 | 2026-01-08 04:14:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a74806da-7f2e-30b6-8045-2c51789d3e98 | -4.51026 | -43.49278 | 2026-01-08 04:14:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 08456907-bc7e-383b-aee1-26fcfcaf1cc7 | -5.04239 | -40.8618 | 2026-01-08 04:14:00 | NOAA-20 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 8.0 |
| 77590724-516e-3f82-b8b2-8f5eb2a8e3ea | -4.27699 | -43.7643 | 2026-01-08 04:14:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| d6eb49ea-498d-35d5-8542-2a518fdb101d | -2.64874 | -44.67369 | 2026-01-08 04:14:00 | NOAA-20 | BACURITUBA | MARANHÃO | Brasil | 2101350 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 24a7c170-73b2-3c21-8e96-521a8d2ba55c | -3.69451 | -44.53875 | 2026-01-08 04:14:00 | NOAA-20 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2298551a-2114-3b8c-a443-b3dd5895f9e8 | -4.599 | -45.99311 | 2026-01-08 04:14:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 257df82a-b991-389a-8d62-49ea3606bd39 | -5.38437 | -45.38831 | 2026-01-08 04:14:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b3297bf0-b729-320b-b209-1afbbcd6b408 | -5.17791 | -37.76241 | 2026-01-08 04:14:00 | NOAA-20 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 041577eb-977b-34a1-bf49-c09e5508d345 | -4.27922 | -43.77187 | 2026-01-08 04:14:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| b11ac0d8-f263-34ee-893c-45bf19b52ec7 | -3.83531 | -45.9234 | 2026-01-08 04:14:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ba1c5c9f-ab5f-353d-89e8-2f8ec3ac348c | -4.27643 | -43.76782 | 2026-01-08 04:14:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 5a3bfc63-9fd4-3f32-93ab-83e9effb1ad5 | -6.61532 | -39.38998 | 2026-01-08 04:14:00 | NOAA-20 | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 4a858e64-aea7-3ae1-a7b4-66075aa78053 | -1.59322 | -46.68635 | 2026-01-08 04:14:00 | NOAA-20 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 28696217-148f-340e-ae90-dab3753641cd | -4.74871 | -44.44088 | 2026-01-08 04:14:00 | NOAA-20 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a00f539d-6645-3bd8-afda-212311954e64 | -2.89761 | -52.63766 | 2026-01-08 04:14:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1ae03fae-82be-3cc7-a302-9989bce16ae9 | -6.33909 | -43.37887 | 2026-01-08 04:14:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9f3b524c-ead2-30f7-a0c5-e28cf38c4f19 | -4.26196 | -43.77272 | 2026-01-08 04:14:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| b0c3c21e-ac86-3405-b559-5c242841e869 | -3.20076 | -46.83371 | 2026-01-08 04:14:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 48cc95a5-f87b-3f8c-baed-1a0c73cc24f9 | -4.26864 | -43.77379 | 2026-01-08 04:14:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b02156e2-a564-376a-8cc1-90dd343b9ffe | -3.19846 | -46.82355 | 2026-01-08 04:14:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3483051a-add1-3cad-8e67-fd53d2905ddd | -4.96968 | -42.75868 | 2026-01-08 04:14:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 41a3d847-8363-375d-81ba-7fd0f11c7d55 | -2.99543 | -40.10799 | 2026-01-08 04:14:00 | NOAA-20 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 695ba98f-39aa-3cf4-ac12-41536940fda1 | -5.53354 | -43.6801 | 2026-01-08 04:14:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 54415d45-8f67-3bc6-b2d1-35278c352ea8 | -7.2244 | -39.94479 | 2026-01-08 04:14:00 | NOAA-20 | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 1f9c6a7b-d7d5-3047-a790-6a38d18453e9 | -4.26418 | -43.78032 | 2026-01-08 04:14:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c0f3dcad-cca5-3caf-ac55-c5d70ba6c7b8 | -3.93749 | -41.89381 | 2026-01-08 04:14:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 0e18938c-431f-3075-abe8-a2a2b79d2d77 | -2.64181 | -44.6726 | 2026-01-08 04:14:00 | NOAA-20 | BACURITUBA | MARANHÃO | Brasil | 2101350 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 3462fafa-71e0-3a5b-8f14-2b0ddba462f3 | -7.56682 | -46.48564 | 2026-01-08 04:16:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7c039d9c-7052-346b-bf84-9b9c9d1ef650 | -15.14461 | -45.27237 | 2026-01-08 04:16:00 | NOAA-20 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README6.md)
