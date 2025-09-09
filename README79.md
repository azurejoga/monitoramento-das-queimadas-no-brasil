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

## Dados Diários - Página 79

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 063f15de-dab0-3213-9e54-781dc6933985 | -12.2181 | -53.8798 | 2025-09-09 13:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 89.3 |
| 1bf666dc-805d-3018-b2c7-893bc005444f | -5.6738 | -43.9 | 2025-09-09 13:30:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 67.3 |
| d047c133-2dc2-3d60-b92f-c0e60da81bea | -17.5799 | -49.8019 | 2025-09-09 13:30:00 | GOES-19 | EDEALINA | GOIÁS | Brasil | 5207352 | 52 | 33 | nan | nan | nan | Cerrado | 73.6 |
| f21dcd35-b5ec-3dd8-a339-ba21d6e37d79 | -13.1367 | -54.9171 | 2025-09-09 13:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 85.8 |
| 290c25b5-475a-33c8-992c-6813b1048d62 | -11.446 | -43.6461 | 2025-09-09 13:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 74.3 |
| 7c85b537-eeb6-37e7-9eaa-19491d3c0ed1 | -18.6904 | -52.594 | 2025-09-09 13:30:00 | GOES-19 | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 101.5 |
| eaf8c721-bf4a-363b-8786-8eb08e24f633 | -17.2973 | -46.6799 | 2025-09-09 13:30:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 89.7 |
| 2110c407-26c5-32d6-a065-4b2a4cffef2b | -12.5286 | -45.2987 | 2025-09-09 13:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 61.8 |
| 43634164-0305-38aa-850b-e4a275ec17c8 | -5.7483 | -43.9406 | 2025-09-09 13:30:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 101.0 |
| 30c247e7-7ca5-336e-af25-0c2540410c36 | -17.2557 | -46.7578 | 2025-09-09 13:30:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 296.9 |
| 07d5a971-cdda-358c-a820-b1c440809eca | -14.432 | -52.9619 | 2025-09-09 13:30:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 73.0 |
| 23f946fd-81bc-3f13-b07a-cd09c97e8b97 | -5.8406 | -44.0951 | 2025-09-09 13:30:00 | GOES-19 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 123.2 |
| 8bc5b2c9-2efa-3028-8b65-25f6094a5b38 | -5.9563 | -45.7915 | 2025-09-09 13:30:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 87.5 |
| 1aea874f-0d4d-3ea8-a6dd-633b0ea4c567 | -12.1991 | -53.8817 | 2025-09-09 13:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 313.0 |
| b91d9133-5c7a-3670-a7b4-148ce5874c00 | -12.2178 | -53.9005 | 2025-09-09 13:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 93.0 |
| 67a6b4a2-79eb-3347-93d0-4d81884d0741 | -6.2407 | -43.4144 | 2025-09-09 13:30:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 110.6 |
| 7a376a13-4a97-3124-bec2-c843e94af9fb | -11.9926 | -51.0126 | 2025-09-09 13:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 87.3 |
| 05fe3358-7de1-340f-a8b2-7215889beec5 | -12.6343 | -56.9725 | 2025-09-09 13:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 72.3 |
| 53dbb1bc-6710-378e-aeab-f81f7a195b35 | -13.2215 | -51.7808 | 2025-09-09 13:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 87.0 |
| 5b90038b-0807-3aef-a482-a17e4f6869cb | -6.2226 | -43.3459 | 2025-09-09 13:40:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 112.0 |
| 1b0e1050-783b-3fa0-bbcd-e9ede5ed5c11 | -13.1367 | -54.9171 | 2025-09-09 13:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 98.5 |
| 369c534d-b2f1-38cd-8ce7-d1fec5ffd39e | -15.758 | -53.548 | 2025-09-09 13:40:00 | GOES-19 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 70.7 |
| 8f55cc1c-d508-348e-9f01-360acb577b02 | -17.2757 | -46.7538 | 2025-09-09 13:40:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 73.0 |
| 50c37307-0338-3075-b609-a16ca465c70f | -15.2683 | -53.8012 | 2025-09-09 13:40:00 | GOES-19 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 142.4 |
| 1a3c8008-85aa-31b2-a611-68c74ec7f242 | -9.1914 | -59.3843 | 2025-09-09 13:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 66.1 |
| 0f7a56e4-4bb3-3223-a7ea-f2064e0144a3 | -15.8201 | -52.2659 | 2025-09-09 13:40:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 88.5 |
| a3d996ae-4e26-391f-afe3-13e6a4c9a43a | -14.1901 | -41.8111 | 2025-09-09 13:40:00 | GOES-19 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 108.1 |
| 5fad3924-424e-3e54-8b08-3ca7d134cfb1 | -4.7346 | -44.4457 | 2025-09-09 13:40:00 | GOES-19 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 98.7 |
| e899bde2-a94d-33af-a98c-9cccff3447e1 | -15.7778 | -53.5242 | 2025-09-09 13:40:00 | GOES-19 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 218.5 |
| b1b351e9-8816-3822-940f-bd1f293e5fe4 | -5.453 | -43.4525 | 2025-09-09 13:40:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 129.9 |
| 01cde3a7-f720-3cff-8602-071c3b586934 | -5.5504 | -45.1891 | 2025-09-09 13:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 93.7 |
| 7d19eed4-d722-3d47-bc32-bfda4485c6d8 | -8.0606 | -48.6423 | 2025-09-09 13:40:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 140.3 |
| 0a969309-fd24-3a9b-b01f-76da0d8627f2 | -5.8397 | -44.1872 | 2025-09-09 13:40:00 | GOES-19 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 100.6 |
| 437320fb-bc9c-3009-99cf-cdd89d7b70db | -17.2762 | -46.7305 | 2025-09-09 13:40:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 95.9 |
| 0fdb0731-77b0-3d9a-a649-db8e98b3dcf0 | -15.8205 | -52.2444 | 2025-09-09 13:40:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 158.1 |
| 3c8bf632-8c0a-33ea-8370-3e8affa3b6af | -10.0993 | -48.1595 | 2025-09-09 13:40:00 | GOES-19 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 71.1 |
| 6a1155c8-e22d-30b9-9d79-368928abb8ff | -5.0438 | -43.1314 | 2025-09-09 13:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 81.9 |
| 825d29f9-e4f1-3e7a-83cc-0ca0cbab033c | -7.5611 | -44.6597 | 2025-09-09 13:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 96.3 |
| 606e35c1-4341-3db9-8ea4-ed186a19d15e | -5.8585 | -44.1858 | 2025-09-09 13:40:00 | GOES-19 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 75.2 |
| 939617da-56b2-36bb-a3dd-cb0166344312 | -5.8582 | -44.2088 | 2025-09-09 13:40:00 | GOES-19 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 286.1 |
| 5b4ddc29-eaed-3e34-8aad-aa240f68f5b4 | -18.6904 | -52.594 | 2025-09-09 13:40:00 | GOES-19 | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 146.0 |
| 1322b18f-98bd-3105-9cc3-1c9820175069 | -11.4272 | -43.6254 | 2025-09-09 13:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 112.7 |
| e7e735d2-6e20-346a-85a6-1880874b279d | -6.199 | -45.8186 | 2025-09-09 13:40:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 114.6 |
| b043fb73-f1ba-3415-a129-3347bef9fd4a | -16.3602 | -43.0349 | 2025-09-09 13:40:00 | GOES-19 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 75.7 |
| e92861d5-9f47-33a7-b769-3d93363282d6 | -9.4623 | -60.5104 | 2025-09-09 13:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 55.0 |
| bbdd6cc8-6da9-3884-87be-cc41b63a3310 | -10.2982 | -48.8148 | 2025-09-09 13:40:00 | GOES-19 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 47.9 |
| 0f365278-b35b-351d-a2d4-70df4b2f1e1a | -5.5702 | -42.9062 | 2025-09-09 13:40:00 | GOES-19 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 351.4 |
| 75578468-5d04-3c68-8734-63ecda5866c9 | -12.5286 | -45.2987 | 2025-09-09 13:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 117.3 |
| bcfb091a-d7b9-3c4e-a393-998a18c0a4d9 | -8.0794 | -48.6407 | 2025-09-09 13:40:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 163.9 |
| 7eccb186-99fa-3f31-9b64-66566c5c1b81 | -17.5799 | -49.8019 | 2025-09-09 13:40:00 | GOES-19 | EDEALINA | GOIÁS | Brasil | 5207352 | 52 | 33 | nan | nan | nan | Cerrado | 108.9 |
| 6dca9a0d-3974-31f0-b24f-3345ff7deff5 | -11.4469 | -43.5988 | 2025-09-09 13:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 104.2 |
| bff7ce3b-6110-3ad7-8cf7-4d49503978e1 | -5.3482 | -44.7943 | 2025-09-09 13:40:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 68.4 |
| a4907b80-630e-3997-9efc-d37f1dd84c6f | -8.4612 | -51.4595 | 2025-09-09 13:40:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 70.3 |
| 519a627a-b7f9-3880-b327-305702971440 | -6.7851 | -43.4371 | 2025-09-09 13:40:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 83.4 |
| a1037fbd-3892-361b-ada3-51cccfac9a59 | -13.2023 | -51.7831 | 2025-09-09 13:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 84.2 |
| c565710d-1fd0-33dd-9a1c-d9a713c36b34 | -11.4465 | -43.6224 | 2025-09-09 13:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 90.6 |
| e9e93ea1-c656-36cd-8b8e-bd6d78b660c7 | -12.529 | -45.2756 | 2025-09-09 13:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 152.4 |
| d3e537e2-6d43-3833-a2d9-65b6bcd51fe4 | -5.589 | -42.9048 | 2025-09-09 13:40:00 | GOES-19 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 285.6 |
| 18ce147b-d5fe-305e-a4cf-6b92c47d1ab7 | -11.3552 | -50.4233 | 2025-09-09 13:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 104.7 |
| eb6ace58-b968-30a3-900e-0d4046cb57d6 | -11.3389 | -46.5419 | 2025-09-09 13:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 114.9 |
| c5e64b12-b92a-3e42-9348-bfeabb95b732 | -15.2686 | -53.7801 | 2025-09-09 13:40:00 | GOES-19 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 274.3 |
| 6034a419-17aa-357e-9c24-0968b350dd4f | -5.8406 | -44.0951 | 2025-09-09 13:40:00 | GOES-19 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 108.3 |
| a77fa1a9-e867-3f76-b910-f3fb116d5b6b | -11.2196 | -54.9975 | 2025-09-09 13:40:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 79.9 |
| 8aa76997-635e-3a0e-9fe1-9ccacb353e2f | -5.8218 | -44.0965 | 2025-09-09 13:40:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 86.9 |
| 017a881d-885a-320a-a751-4ab4144a4d39 | -6.2038 | -43.3475 | 2025-09-09 13:40:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 88.8 |
| 08b10a4c-5249-3e65-9d80-d29b2bd4d58d | -9.8266 | -46.0322 | 2025-09-09 13:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 168.5 |
| d473c746-d924-355e-8571-09fbec30d96b | -5.4343 | -43.4538 | 2025-09-09 13:40:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 112.1 |
| d5e3f85f-41e8-3bbf-b58d-ca25d723fe0b | -5.6925 | -43.8986 | 2025-09-09 13:40:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 83.0 |
| f8089bdd-4523-3c34-9f95-456c61b01151 | -11.9926 | -51.0126 | 2025-09-09 13:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 91.6 |
| f96b2654-bb7a-3097-9bd6-c7344194a4aa | -5.4587 | -42.797 | 2025-09-09 13:40:00 | GOES-19 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 72.9 |
| 593aa55b-fef2-36eb-9c0c-90151083fca8 | -12.6153 | -56.9742 | 2025-09-09 13:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 65.8 |
| 67a183b6-98c8-380d-b7a2-b6fd83867fa7 | -11.9735 | -51.0148 | 2025-09-09 13:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 97.5 |
| 58857226-1600-3363-91d4-6eb01ac2f766 | -17.7328 | -44.4637 | 2025-09-09 13:40:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 105.2 |
| 839bd639-c414-387a-bd92-a24ca401263e | -11.4277 | -43.6017 | 2025-09-09 13:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 128.8 |
| 0d241168-e353-3609-93de-7b1e6026659f | -12.0295 | -51.0935 | 2025-09-09 13:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 171.3 |
| 84aabddd-075a-30cc-a8ef-1e886ee2387e | -9.0931 | -45.7314 | 2025-09-09 13:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 65.6 |
| e29f0cd9-9d5f-3076-a1a5-eb857b1590e4 | -5.8395 | -44.2103 | 2025-09-09 13:40:00 | GOES-19 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 459.5 |
| b5a47bd0-81a8-37aa-ac0e-3e2f1209b488 | -6.527 | -44.7974 | 2025-09-09 13:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 109.5 |
| cfdcb3d7-c42d-3eae-9512-c27a26c85940 | -5.975 | -45.7901 | 2025-09-09 13:40:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 94.3 |
| e8627238-c50e-304c-9fa5-410aeb6ae349 | -8.4119 | -49.0869 | 2025-09-09 13:40:00 | GOES-19 | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 119.4 |
| eead783c-7ae4-3be1-ab85-daa21918ced7 | -8.4116 | -49.1085 | 2025-09-09 13:40:00 | GOES-19 | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 108.4 |
| 57177062-fe35-36b5-95d0-239107cb56bb | -15.2489 | -53.8036 | 2025-09-09 13:40:00 | GOES-19 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 65.0 |
| b23f21db-8fd3-333e-94fb-1df611985948 | -17.2967 | -46.7032 | 2025-09-09 13:40:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 134.9 |
| 4287cd16-65c7-33eb-b7d6-5ef6c3405843 | -12.0291 | -51.1149 | 2025-09-09 13:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 352.0 |
| 1ef22c92-55d5-3e8b-b995-6acd75ffd91c | -7.5799 | -44.6579 | 2025-09-09 13:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 97.3 |
| 4a02a57e-c7af-3202-9fd5-e5da0fe9a2c5 | -5.8208 | -44.2117 | 2025-09-09 13:40:00 | GOES-19 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 99.9 |
| de2d34dc-4531-31a5-87e4-0aee1967c507 | -17.2563 | -46.7346 | 2025-09-09 13:40:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 73.7 |
| c4f297a5-333c-3d7c-af64-58bd4ac18f5d | -11.9739 | -50.9935 | 2025-09-09 13:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 168.6 |
| 05e73cf9-ceb8-32af-979f-a9a0d7cf6321 | -9.6289 | -48.0129 | 2025-09-09 13:40:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 197.7 |
| 30a087fc-5f74-31ea-b6bb-dfea2c4a9b93 | -7.789 | -46.0891 | 2025-09-09 13:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 88.3 |
| 1ad39457-da65-36c6-bfed-9a48bd2741fe | -11.2007 | -54.9992 | 2025-09-09 13:40:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 63.9 |
| 9f9031b7-ddc8-3be0-9f10-012a5c762841 | -11.3172 | -50.4275 | 2025-09-09 13:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 91.1 |
| 874606ac-96f8-3dbb-8eba-aa48a571a69f | -21.127 | -48.8519 | 2025-09-09 13:40:00 | GOES-19 | PALMARES PAULISTA | SÃO PAULO | Brasil | 3535101 | 35 | 33 | nan | nan | nan | Mata Atlântica | 111.8 |
| 7a0fa076-9872-370c-a567-ec9cbed8ee6d | -17.2973 | -46.6799 | 2025-09-09 13:40:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 116.6 |
| 27d0f04e-e29d-3d93-b182-18a09deed9e0 | -13.299 | -51.7288 | 2025-09-09 13:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 85.5 |
| a0a1d502-e96f-3c11-b869-6d6d965e3e1e | -9.0934 | -45.7088 | 2025-09-09 13:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 93.7 |
| b5147445-9ea7-3d65-8a22-8262aeff1ecd | -6.2407 | -43.4144 | 2025-09-09 13:40:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 114.7 |
| a451cdb2-4961-3902-992f-d60dbb96fe34 | -9.4436 | -60.5114 | 2025-09-09 13:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 56.0 |
| 6a911599-1ece-38fa-9790-060dad78b3dc | -11.446 | -43.6461 | 2025-09-09 13:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 84.4 |
| ef8808c6-03cf-3f51-8d71-d81472e43a1d | -5.9563 | -45.7915 | 2025-09-09 13:40:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 78.0 |


[Clique aqui para ver as próximas entradas](README80.md)
