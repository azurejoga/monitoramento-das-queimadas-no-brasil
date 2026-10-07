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

## Dados Diários - Página 207

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5cd1c8d7-beef-317c-a30d-109566494dda | -6.3807 | -42.53755 | 2026-10-07 16:37:00 | NPP-375 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 9.8 |
| 8a22a291-7295-32ea-87b1-55944ff60703 | -6.83221 | -44.86774 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ea941d09-d508-3f03-bb9f-7a595418dd29 | -8.96051 | -47.5594 | 2026-10-07 16:37:00 | NPP-375 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 453fa66b-b212-3470-8531-7038e9d15bae | -8.984 | -45.9274 | 2026-10-07 16:37:00 | NPP-375 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 62773972-6afe-3af5-bc2c-e45b2a7a9f8d | -6.93349 | -44.64985 | 2026-10-07 16:37:00 | NPP-375 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a4fe65cd-04f0-354a-a7ef-8c857a3bd015 | -11.32452 | -46.68417 | 2026-10-07 16:37:00 | NPP-375 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 1859f1ea-94f1-31c3-833d-7724cd71ff1c | -5.7974 | -52.36256 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| e158f4bb-9279-3758-a7dd-077c5baacdf8 | -6.43449 | -43.83576 | 2026-10-07 16:37:00 | NPP-375 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 026eda93-1fd1-3d00-8587-8dc536c22fa1 | -9.82149 | -46.24093 | 2026-10-07 16:37:00 | NPP-375 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 47fe0ddd-ab56-3657-a2ad-901025167a5b | -11.33845 | -46.66518 | 2026-10-07 16:37:00 | NPP-375 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 38f9599c-3e62-348d-b90f-fd5994c5ce9e | -2.97716 | -41.41419 | 2026-10-07 16:37:00 | NPP-375 | CAJUEIRO DA PRAIA | PIAUÍ | Brasil | 2202083 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| d56e256b-cf51-3b17-a643-229ed3c35dfb | -3.75135 | -41.71575 | 2026-10-07 16:37:00 | NPP-375 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 13.3 |
| edfc0bc2-65e1-3edd-ae1b-7482d52d88f2 | -8.30208 | -44.15814 | 2026-10-07 16:37:00 | NPP-375 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 42.2 |
| 120dcc76-487e-3602-93de-e0c4263ab198 | -14.97952 | -43.99404 | 2026-10-07 16:37:00 | NPP-375 | MATIAS CARDOSO | MINAS GERAIS | Brasil | 3140852 | 31 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 10b54c53-a27a-3e2e-8ae1-c58032fdf7a9 | -6.60051 | -37.89072 | 2026-10-07 16:37:00 | NPP-375 | LAGOA | PARAÍBA | Brasil | 2508109 | 25 | 33 | nan | nan | nan | Caatinga | 14.4 |
| b2c20610-9128-31ab-acdd-623ae556112f | -6.29298 | -44.90174 | 2026-10-07 16:37:00 | NPP-375 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| b3971b96-b7b2-3d8a-a3ea-a8b707eac2c8 | -5.73981 | -53.45432 | 2026-10-07 16:37:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 77.8 |
| f3fbf01f-eefa-37f4-bd58-890897ee0467 | -5.73213 | -45.15057 | 2026-10-07 16:37:00 | NPP-375 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 158.7 |
| 6db5e0d0-c343-3fe8-b34b-2ffc26164c88 | -6.04634 | -53.48996 | 2026-10-07 16:37:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 19.0 |
| cdad0fe1-57f8-375a-a8ed-fe81aead8433 | -9.56019 | -45.68819 | 2026-10-07 16:37:00 | NPP-375 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 1e253b95-8af5-3eea-9969-474472a33387 | -11.14606 | -46.1159 | 2026-10-07 16:37:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.3 |
| e3c2340d-8147-34b9-996e-6ed6be2e702a | -3.9441 | -38.49311 | 2026-10-07 16:37:00 | NPP-375 | AQUIRAZ | CEARÁ | Brasil | 2301000 | 23 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 34d5d4c2-f3c4-39ec-8587-928ab5b0100a | -16.14537 | -43.74974 | 2026-10-07 16:37:00 | NPP-375 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 819eef00-288a-3f4f-abe3-7e72dd436e82 | -7.52183 | -38.37792 | 2026-10-07 16:37:00 | NPP-375 | IBIARA | PARAÍBA | Brasil | 2506608 | 25 | 33 | nan | nan | nan | Caatinga | 7.4 |
| 4d34befb-2aad-3fbf-8981-c5356f56408f | -6.14814 | -52.89612 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 40573853-f6fd-3e58-9300-528e56fbb9c2 | -5.24423 | -50.91732 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 126c8bf3-1b46-31c8-a0b2-3b1e8c59cbee | -6.73041 | -55.1039 | 2026-10-07 16:37:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 22.8 |
| 8a5d5a1a-29d0-340e-8e3b-b6e6ddac3650 | -6.91706 | -41.23739 | 2026-10-07 16:37:00 | NPP-375 | BOCAINA | PIAUÍ | Brasil | 2201804 | 22 | 33 | nan | nan | nan | Caatinga | 7.7 |
| 932fe93b-c0e0-3aee-adbd-e3cc21076e58 | -7.20935 | -45.09217 | 2026-10-07 16:37:00 | NPP-375 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 6a315f15-9c32-3e8c-b96e-b8eda2a5f1c6 | -5.87287 | -45.97081 | 2026-10-07 16:37:00 | NPP-375 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 16.1 |
| b02a45f5-c16f-307b-8d4f-440a0b13590e | -3.77341 | -41.78734 | 2026-10-07 16:37:00 | NPP-375 | SÃO JOSÉ DO DIVINO | PIAUÍ | Brasil | 2210052 | 22 | 33 | nan | nan | nan | Caatinga | 44.6 |
| 18d8ad67-9306-35ab-8d37-f3809e2eb6a8 | -11.15513 | -46.10186 | 2026-10-07 16:37:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 42.4 |
| 6cd8b279-a06b-30bb-ade3-2e85271f4334 | -3.8976 | -44.11501 | 2026-10-07 16:37:00 | NPP-375 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 33.5 |
| fac5a728-32fa-3a5d-b5c3-dceb3b8739ae | -6.94211 | -45.29046 | 2026-10-07 16:37:00 | NPP-375 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 104.9 |
| 71d92a73-c7ad-3d74-b550-f1ebbda6cdb9 | -6.36361 | -55.15661 | 2026-10-07 16:37:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| fbcb4cdc-6557-3057-b5ea-a2585482916f | -7.00348 | -44.06475 | 2026-10-07 16:37:00 | NPP-375 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 402f315d-3a2f-34d1-a32f-26be22028ef7 | -14.79403 | -41.96077 | 2026-10-07 16:37:00 | NPP-375 | CONDEÚBA | BAHIA | Brasil | 2908705 | 29 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 2854d2f1-8e94-3b49-9976-9a4a27812f3d | -5.23753 | -48.39308 | 2026-10-07 16:37:00 | NPP-375 | SÃO SEBASTIÃO DO TOCANTINS | TOCANTINS | Brasil | 1720309 | 17 | 33 | nan | nan | nan | Amazônia | 44.2 |
| e06877bd-4829-3fd2-8b01-ca6ed4d4f93a | -11.19094 | -50.80243 | 2026-10-07 16:37:00 | NPP-375 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 10.9 |
| a1a006f7-1a15-38d2-9e8c-d3c3e3e051fc | -6.21986 | -52.83318 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 14.9 |
| 9cd685cd-a851-33e0-9800-ae7840f1a4c3 | -5.74525 | -41.67551 | 2026-10-07 16:37:00 | NPP-375 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 15.5 |
| ceaba6f7-66f5-3d75-99c3-d59c40f1e0ae | -6.98676 | -43.29436 | 2026-10-07 16:37:00 | NPP-375 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 12.8 |
| 54c0107a-0454-31e9-b3ff-13a2aecbd184 | -7.3002 | -48.62062 | 2026-10-07 16:37:00 | NPP-375 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 21.3 |
| 9db66c9d-adea-395a-972b-beaababc074c | -4.57426 | -43.87874 | 2026-10-07 16:37:00 | NPP-375 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| dc235086-6ff4-3e85-9f05-88705af6b021 | -3.94419 | -40.72255 | 2026-10-07 16:37:00 | NPP-375 | MUCAMBO | CEARÁ | Brasil | 2309003 | 23 | 33 | nan | nan | nan | Caatinga | 11.9 |
| 5898eca8-74bf-307a-b865-d6271a5d8c66 | -4.84456 | -40.39294 | 2026-10-07 16:37:00 | NPP-375 | TAMBORIL | CEARÁ | Brasil | 2313203 | 23 | 33 | nan | nan | nan | Caatinga | 8.6 |
| 239db1b8-cb23-308f-9217-269fdf3f203f | -5.9721 | -53.59464 | 2026-10-07 16:37:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| faea6de9-471e-3823-8bab-72d6aa71f420 | -3.48541 | -41.51429 | 2026-10-07 16:37:00 | NPP-375 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 44.9 |
| 7e9c6f7f-a20f-38f8-aaa6-7b4f7dcf0741 | -16.04547 | -40.64901 | 2026-10-07 16:37:00 | NPP-375 | ALMENARA | MINAS GERAIS | Brasil | 3101706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| 797bee1f-4de5-34b3-8ed6-0c3f16ff53f9 | -6.2098 | -52.83724 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 114ca69b-60b0-3ae4-b3f3-7023498e415d | -8.95823 | -45.11172 | 2026-10-07 16:37:00 | NPP-375 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 292b1f6e-6e9e-3372-906c-c8b200c41d38 | -5.97646 | -43.73784 | 2026-10-07 16:37:00 | NPP-375 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 0711ed44-d50f-3987-b4cd-0ef585d555cc | -16.6138 | -40.64655 | 2026-10-07 16:37:00 | NPP-375 | FELISBURGO | MINAS GERAIS | Brasil | 3125606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.9 |
| d02b9607-e11d-316c-a5f9-97870e7f05cd | -11.22696 | -46.24218 | 2026-10-07 16:37:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 99e5a050-a09d-3387-9a36-270f2b412ce6 | -5.50579 | -42.83967 | 2026-10-07 16:37:00 | NPP-375 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 6.4 |
| 79f9faea-4b90-394d-996f-29d913605dce | -7.06542 | -45.36774 | 2026-10-07 16:37:00 | NPP-375 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 39fa4683-af9d-3e7a-93ba-246ee052be2f | -9.82749 | -46.25698 | 2026-10-07 16:37:00 | NPP-375 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b4f57d97-cf61-35c7-917e-719347527c6c | -6.47761 | -46.62302 | 2026-10-07 16:37:00 | NPP-375 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 44.8 |
| 311ff0e5-c157-303a-b559-e5e1af33aff0 | -6.61647 | -37.87933 | 2026-10-07 16:37:00 | NPP-375 | LAGOA | PARAÍBA | Brasil | 2508109 | 25 | 33 | nan | nan | nan | Caatinga | 15.4 |
| 302bbc89-381a-3341-9860-f5020cdcb287 | -4.29429 | -50.7617 | 2026-10-07 16:37:00 | NPP-375 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| b707665b-0c34-3788-8b73-9fc68ce2df32 | -9.86461 | -46.07261 | 2026-10-07 16:37:00 | NPP-375 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 40ec2912-5cb0-38d4-8016-7ee99ea75f99 | -7.21105 | -55.11283 | 2026-10-07 16:37:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 73.9 |
| 7cc538f3-1875-3ed3-b278-40c446a94ad4 | -7.21161 | -55.11695 | 2026-10-07 16:37:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 41.3 |
| 81153f01-25e4-38cd-973d-f729787123d4 | -6.35367 | -38.85884 | 2026-10-07 16:37:00 | NPP-375 | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 6.2 |
| ee32d4c5-9523-3658-ac11-def046bcf84f | -15.47578 | -40.54239 | 2026-10-07 16:37:00 | NPP-375 | RIBEIRÃO DO LARGO | BAHIA | Brasil | 2926657 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| cdbae73c-247f-336d-a489-15d3c23f90ef | -3.70617 | -44.81003 | 2026-10-07 16:37:00 | NPP-375 | CONCEIÇÃO DO LAGO-AÇU | MARANHÃO | Brasil | 2103554 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d0130eef-7624-3042-8e95-48be82c0760a | -5.32735 | -40.89944 | 2026-10-07 16:37:00 | NPP-375 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 020ccca9-6858-3dc0-bb8b-ce7119084073 | -7.70957 | -45.45632 | 2026-10-07 16:37:00 | NPP-375 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 13.5 |
| f95a39dd-2d9c-3279-a092-847d6a592820 | -5.961 | -46.37026 | 2026-10-07 16:37:00 | NPP-375 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 72.0 |
| 20d5d99a-2af2-37cf-a97c-d74f6b88a98d | -4.57705 | -43.87475 | 2026-10-07 16:37:00 | NPP-375 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| ce60808a-37ce-3efe-ad59-42e63059aad9 | -6.82085 | -43.68857 | 2026-10-07 16:37:00 | NPP-375 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 619e9439-fe34-369c-831a-16bc9522a320 | -4.21613 | -44.60914 | 2026-10-07 16:37:00 | NPP-375 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Cerrado | 29.0 |
| bd2a19dd-5fa0-3eb6-a3f4-31c2dc818c45 | -6.23029 | -46.00741 | 2026-10-07 16:37:00 | NPP-375 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| d2c4f4d4-2fbe-379f-884f-c3a8eba4f2cf | -3.50713 | -41.93533 | 2026-10-07 16:37:00 | NPP-375 | CAXINGÓ | PIAUÍ | Brasil | 2202653 | 22 | 33 | nan | nan | nan | Caatinga | 23.7 |
| 18d9dd05-596d-386e-961f-cfc471e8b8a5 | -10.91458 | -49.62054 | 2026-10-07 16:37:00 | NPP-375 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 70b2d844-49d1-3c98-87da-cc4938fc05e6 | -3.53085 | -39.50711 | 2026-10-07 16:37:00 | NPP-375 | ITAPIPOCA | CEARÁ | Brasil | 2306405 | 23 | 33 | nan | nan | nan | Caatinga | 10.6 |
| 3ff3dcaf-24a5-38a6-8317-7b70720931f2 | -6.69068 | -44.96492 | 2026-10-07 16:37:00 | NPP-375 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 5338a6ef-f7e6-3660-a70a-82019c8bcc5a | -7.04989 | -44.32433 | 2026-10-07 16:37:00 | NPP-375 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 540228d3-3f6f-3daa-bea9-b691d0a08aeb | -9.95376 | -43.55128 | 2026-10-07 16:37:00 | NPP-375 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 78.3 |
| fc3e4918-d528-328d-8bd4-786301b5badf | -7.75382 | -54.79279 | 2026-10-07 16:37:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 4cf969e8-16c8-34d0-aab9-8739c4f82c4c | -3.79484 | -38.59323 | 2026-10-07 16:37:00 | NPP-375 | FORTALEZA | CEARÁ | Brasil | 2304400 | 23 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 1b833352-bd88-365f-aa37-4598c51d9450 | -3.81545 | -38.55602 | 2026-10-07 16:37:00 | NPP-375 | FORTALEZA | CEARÁ | Brasil | 2304400 | 23 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 1fffe062-83de-336a-b176-c2255779b9fe | -16.19385 | -44.57006 | 2026-10-07 16:37:00 | NPP-375 | LUISLÂNDIA | MINAS GERAIS | Brasil | 3138682 | 31 | 33 | nan | nan | nan | Cerrado | 17.7 |
| fce9cb26-2b5a-3ea5-8afb-c5fb5caef593 | -9.9671 | -45.95898 | 2026-10-07 16:37:00 | NPP-375 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 31.9 |
| 81d919d6-08b2-3b7c-a0aa-c4342380ca0c | -5.51407 | -45.62812 | 2026-10-07 16:37:00 | NPP-375 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 8d86c90e-842b-34ea-ad2c-e970bba9d18b | -3.3011 | -42.93527 | 2026-10-07 16:37:00 | NPP-375 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 834a945b-fe56-3012-81f9-cdeb6d572706 | -10.4917 | -47.29044 | 2026-10-07 16:37:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 25.5 |
| 08ae2986-24db-3eab-8d52-818efbbe83f6 | -10.34728 | -46.25126 | 2026-10-07 16:37:00 | NPP-375 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 31.1 |
| 85313af9-b357-3d3e-9ae0-4804871d0b01 | -9.8359 | -47.8384 | 2026-10-07 16:37:00 | NPP-375 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 2d30d612-d1ad-331d-850b-63f0188301a5 | -8.78765 | -47.58493 | 2026-10-07 16:37:00 | NPP-375 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| edef85fc-a358-30a1-a511-53ede6431afa | -5.36603 | -46.72453 | 2026-10-07 16:37:00 | NPP-375 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 792d9967-3c64-3e11-b8ce-29246cae7c53 | -7.21779 | -55.11645 | 2026-10-07 16:37:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 41.3 |
| f9ba8969-5dad-3c99-829d-fef6aa3dbfb6 | -6.12304 | -52.71862 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 38.3 |
| 5ad28252-c59c-3335-bcce-d5837c19b952 | -6.05082 | -53.48256 | 2026-10-07 16:37:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 93125e48-648e-3e84-8d82-2ac6e4205f5d | -6.12014 | -51.73624 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 117e82c4-1432-3bbd-b7f8-d23952e6cb42 | -5.96011 | -53.55239 | 2026-10-07 16:37:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| dbf3098b-cf19-3057-82fc-554d5b9d22f7 | -4.54024 | -39.48085 | 2026-10-07 16:37:00 | NPP-375 | ITATIRA | CEARÁ | Brasil | 2306603 | 23 | 33 | nan | nan | nan | Caatinga | 13.6 |
| c290875b-4aeb-3a9f-a39d-2cd6fa426d71 | -5.37996 | -45.91837 | 2026-10-07 16:37:00 | NPP-375 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 08b14268-e804-3487-9c63-604a25ea725e | -6.63207 | -43.77955 | 2026-10-07 16:37:00 | NPP-375 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 158.1 |
| 91dfbdf6-4501-3969-9861-4d539e1cef0e | -5.7966 | -52.35676 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |


[Clique aqui para ver as próximas entradas](README208.md)
