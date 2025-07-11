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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8d210551-40cc-31e3-8714-4bfcf74be2fe | -6.30028 | -58.14233 | 2025-07-11 04:57:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6d38e7b7-c3f1-311f-baf8-7dff5582e869 | -4.5517 | -48.00813 | 2025-07-11 04:57:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 9b1cdfe9-4e5f-3272-a894-2dfec402ef73 | -10.63229 | -45.23424 | 2025-07-11 04:57:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| cb6c6259-6be1-3fb8-9669-7c2e119a49f3 | -8.28418 | -46.33294 | 2025-07-11 04:57:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 17bfae78-5374-396b-9035-0b66a7a82aa7 | -9.91173 | -47.82724 | 2025-07-11 04:57:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 22.7 |
| ac6c03e7-038d-3d3d-87f1-9489218ce0f2 | -6.72941 | -51.07483 | 2025-07-11 04:57:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b98f4a79-5927-3efd-8ba2-8d5c52b88333 | -8.57522 | -47.18797 | 2025-07-11 04:57:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 92eba280-06db-3d4b-961b-21930ffafff7 | -9.85989 | -47.87432 | 2025-07-11 04:57:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1fe7013b-8729-376f-bc72-3d9740546862 | -7.95146 | -44.85176 | 2025-07-11 04:57:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 625295b9-1416-3369-838b-6ee3e928130a | -4.13091 | -54.90017 | 2025-07-11 04:57:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ea102c9c-e68a-323e-8245-3a731658fc0e | -8.58481 | -47.18946 | 2025-07-11 04:57:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4226383a-4f3c-3b78-b01d-e2b2636a3671 | -7.30933 | -55.30775 | 2025-07-11 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f2c84466-c90b-3498-915d-9c7e6569b9e8 | -8.22912 | -44.92651 | 2025-07-11 04:57:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6dedb77a-7ed5-3d77-818a-f4b09a4db86f | -7.20331 | -43.11911 | 2025-07-11 04:57:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 1dc7ef56-6bbf-3698-afdb-9c17307d734c | -5.58742 | -45.75346 | 2025-07-11 04:57:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e4c07912-affd-3478-b27f-d55573916a82 | -4.02812 | -48.06548 | 2025-07-11 04:57:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6242c539-145a-3c8f-aae0-21da46df9982 | -8.25563 | -46.98711 | 2025-07-11 04:57:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a94a4f09-f55d-3323-b3c0-cede3bdec1d4 | -9.53895 | -46.29946 | 2025-07-11 04:57:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a3504a7d-094a-3835-8e99-05df6b2f1a4b | -7.19776 | -43.11326 | 2025-07-11 04:57:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 1249ed9a-42b6-3aff-9487-280d526ae7e4 | -7.19772 | -43.12054 | 2025-07-11 04:57:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| aa4fd951-fd1c-3235-adf7-470191f12824 | -9.90945 | -47.82605 | 2025-07-11 04:57:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 6a83970e-1de6-39a9-8f2e-bd563bd1596a | -6.29315 | -44.23312 | 2025-07-11 04:57:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b1ab0df4-ee92-3125-8441-86900f0db5cf | -7.79034 | -48.46044 | 2025-07-11 04:57:00 | NOAA-21 | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6bcd4bd7-12d8-3faf-aecb-ff08a730554a | -6.72365 | -44.3368 | 2025-07-11 04:57:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 82d33a9a-9bc6-3307-8ba2-20820ffcdf79 | -3.07559 | -52.4224 | 2025-07-11 04:57:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0d6324f5-24b2-316d-b8c0-3d5b059335b4 | -10.62664 | -45.23355 | 2025-07-11 04:57:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| bf92785e-9a18-3d5f-8943-f643aa85aec7 | -7.9565 | -49.6469 | 2025-07-11 04:57:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b5c0428d-f4d1-3fa6-a41e-697585a52cfd | -4.54743 | -48.00743 | 2025-07-11 04:57:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| acb8ef41-01b3-3cb3-9b0e-211396067865 | -4.45545 | -48.99561 | 2025-07-11 04:57:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9ac1fcb1-705b-392e-9697-0905935c1369 | -9.53376 | -46.29878 | 2025-07-11 04:57:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8505a32c-ca69-3c8b-922a-933ef58c71ca | -8.70549 | -50.0455 | 2025-07-11 04:57:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3952fe7e-d33c-35ba-a5f2-63f571918d8a | -9.19653 | -45.26384 | 2025-07-11 04:57:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1f0b7369-0883-3da3-bb09-5d8c478d7ca5 | -7.20394 | -43.1142 | 2025-07-11 04:57:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 35acc810-c1de-3e06-8f78-e9234d123442 | -8.39489 | -46.93737 | 2025-07-11 04:57:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| c25c3715-6e40-3f01-8b77-ca7045656bce | -8.22407 | -44.92181 | 2025-07-11 04:57:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0eeebdf4-211b-3f92-bf2d-985f104e0cd9 | -3.75157 | -47.11005 | 2025-07-11 04:57:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 53d3b2c7-d47b-3e4b-bc07-1f7e8c782bef | -9.34887 | -50.2195 | 2025-07-11 04:57:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6266c367-65f8-3f76-b0d3-91fda2debd7c | -8.67871 | -49.94867 | 2025-07-11 04:57:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1a5af118-2381-3950-8b49-091e8283e36a | -5.55133 | -43.89577 | 2025-07-11 04:57:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 250eddb3-56b6-3ba2-8d94-feb55a1740db | -2.92233 | -48.24236 | 2025-07-11 04:57:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7562cff5-4a1a-37ec-a81b-637f48f22162 | -8.28459 | -46.32998 | 2025-07-11 04:57:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 85464249-6405-3836-bbb5-bbb1b247576c | -8.28308 | -46.32962 | 2025-07-11 04:57:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9391d95d-39fe-3916-a528-537771e893ab | -6.99433 | -44.44851 | 2025-07-11 04:57:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 64e51479-a2ba-335a-8826-ded5bd358c15 | -7.94136 | -44.85079 | 2025-07-11 04:57:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d786910c-d39b-3284-bf0c-ee54e620feb3 | -7.19714 | -43.11818 | 2025-07-11 04:57:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 51c204bd-7ca8-3bfe-b3a0-4d4bc6fa87e1 | -6.98198 | -44.45454 | 2025-07-11 04:57:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| af964a84-139b-3517-8db7-015e8a56472f | -6.67737 | -46.30531 | 2025-07-11 04:57:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 394af5b3-debe-32aa-a250-16c233d685a9 | -9.91643 | -47.82785 | 2025-07-11 04:57:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 22.7 |
| 9c139a0d-2e80-3654-9164-ca1156c7a756 | -3.75092 | -47.11457 | 2025-07-11 04:57:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 3f57aef9-f27d-35bc-b86b-dd2d05d9a39c | -7.48972 | -43.9381 | 2025-07-11 04:57:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 5b8a70c9-8a07-3748-bc7a-5b2ee97cc993 | -7.19838 | -43.11564 | 2025-07-11 04:57:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.4 |
| a87171f8-0d99-3500-a838-d81bd2b57bbc | -7.65365 | -45.34852 | 2025-07-11 04:57:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 53bceed1-df4b-3943-b9fb-2ef3a94b3e82 | -6.87083 | -45.23201 | 2025-07-11 04:57:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 900968f3-11fd-30fb-a46a-fd45ca384ac7 | -9.90876 | -47.83102 | 2025-07-11 04:57:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 32.9 |
| 4409bd96-b809-301b-8e7b-39e1cb6919b3 | -8.59707 | -47.20427 | 2025-07-11 04:57:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c9d91831-47e5-3ce8-b241-e44ea8f853bb | -6.16104 | -47.27327 | 2025-07-11 04:57:00 | NOAA-21 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 1093c5c0-d9bd-325e-80bd-1ceb164780ac | -8.89578 | -47.34623 | 2025-07-11 04:57:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fff49440-0ac0-3639-90f8-dab4c86e5ba4 | -6.63076 | -56.27568 | 2025-07-11 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1a75fd43-189f-3510-8a1e-b0fe38cb6eea | -3.70861 | -53.70972 | 2025-07-11 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a0f911b0-7d1f-381f-bb0b-550529dc829c | -6.85097 | -42.80363 | 2025-07-11 04:57:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| cf328d58-d504-307c-b644-9fa299a7e1e8 | -9.53419 | -46.29552 | 2025-07-11 04:57:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e2c0f4a0-1d48-36e6-a7b4-2b034b2795d4 | -8.28377 | -46.33591 | 2025-07-11 04:57:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9516d1f4-0128-39be-b38a-ab48ea82f100 | -6.87659 | -45.22993 | 2025-07-11 04:57:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 8126ca4e-0e41-383f-a2f0-01b28a92f8ca | -9.91578 | -47.83276 | 2025-07-11 04:57:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 22.7 |
| f960a38e-1339-3c78-8eaa-3c88cfc84767 | -8.28268 | -46.3326 | 2025-07-11 04:57:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6c50cdaf-b3d8-3c9b-8ca2-352090015047 | -7.43141 | -43.83165 | 2025-07-11 04:57:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7b6f5866-c769-3c99-9834-8f8f657ec038 | -5.78328 | -45.11322 | 2025-07-11 04:57:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f82ea016-7553-3434-a438-6bc30a64372b | -9.66393 | -49.89036 | 2025-07-11 04:57:00 | NOAA-21 | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b09c2773-8fa2-3d83-82a3-378e7350cf1f | -7.65712 | -45.34447 | 2025-07-11 04:57:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d6f12f13-9aba-33b9-b9dd-68d98c972b52 | -9.91413 | -47.82678 | 2025-07-11 04:57:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 08ecd6a1-2969-3578-bb86-5902cc2f6dc6 | -8.22357 | -44.92559 | 2025-07-11 04:57:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 60acdaf0-1106-3338-842d-c7223a035730 | -6.85995 | -42.78382 | 2025-07-11 04:57:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| b3cf923a-13c2-3f04-98c1-815431dc587b | -3.74963 | -47.12354 | 2025-07-11 04:57:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cf500071-5f92-3313-9cb6-e917614b7651 | -4.13815 | -54.89765 | 2025-07-11 04:57:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 977aa4bd-e924-395a-b821-7b7350045cab | -7.94693 | -44.85169 | 2025-07-11 04:57:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4cef79e0-6b42-3020-9b42-31656f256ba1 | -4.5511 | -48.01215 | 2025-07-11 04:57:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| bd05f19d-01af-3e9c-911c-ba1e324e493e | -4.3149 | -47.75832 | 2025-07-11 04:57:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| aa3cfffc-da97-33af-af97-e3e3945c14a8 | -5.78372 | -45.10999 | 2025-07-11 04:57:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a15d78fe-572d-3c3f-809b-37379a4bd11c | -8.31727 | -55.10865 | 2025-07-11 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7142fbbb-72ab-3234-84b2-5954cf2524f1 | -4.2392 | -47.26148 | 2025-07-11 04:57:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 62208e3d-6349-31c2-ac44-5cb5d497aac6 | -10.51193 | -46.52393 | 2025-07-11 04:57:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e4fa5f79-260d-333a-92f8-8a163c439746 | -9.91108 | -47.83215 | 2025-07-11 04:57:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 22.7 |
| a6827482-e298-3aa7-9c9d-d90891de8f1d | -10.51149 | -46.52747 | 2025-07-11 04:57:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d2d8581f-bfc9-3e18-adb1-2708c5f31e6a | -6.62676 | -56.27884 | 2025-07-11 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1f4feee9-6cc8-3683-9385-f693f5a5597e | -6.8606 | -42.77883 | 2025-07-11 04:57:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| b58cd21c-55f7-3224-96c0-6584c26ef977 | -3.58329 | -49.43362 | 2025-07-11 04:57:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f3e61b3f-8769-3617-be31-379ce953438d | -9.6563 | -49.88558 | 2025-07-11 04:57:00 | NOAA-21 | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8d228e4a-01cd-30ec-85bf-631d34a225e7 | -6.13981 | -44.107 | 2025-07-11 04:57:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5e727bf3-a719-3ce2-8e49-3ed6875d73cd | -7.19139 | -43.3581 | 2025-07-11 04:57:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 8c1a70c9-21aa-311e-8646-c63820db86d5 | -7.49566 | -43.93856 | 2025-07-11 04:57:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 2f0f6c10-492d-3bf7-9ead-77d94c5382fa | -8.67471 | -49.94809 | 2025-07-11 04:57:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5f2e9bfb-87ec-35c8-9db7-20b8f803fd9a | -3.7488 | -47.11245 | 2025-07-11 04:57:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 10592c65-da23-3aa5-a7d3-d89679659ac8 | -3.07504 | -52.42591 | 2025-07-11 04:57:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c10c1dbe-aec4-35b8-b101-0a75d218f23e | -8.22458 | -44.91797 | 2025-07-11 04:57:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b879c8b7-0791-380d-9105-a4d357a73940 | -6.72932 | -44.33767 | 2025-07-11 04:57:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 88056b1c-ba30-3f32-b311-b91aeaa67455 | -3.12579 | -52.4518 | 2025-07-11 04:57:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c8cd1dc9-b2d7-3210-ae54-433eb22e31ad | -7.94538 | -44.8548 | 2025-07-11 04:57:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b3394fc9-d4b5-3913-a958-27b7953a8801 | -6.98706 | -44.45961 | 2025-07-11 04:57:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cbca785e-e293-3b1d-9f2f-8e9d84463dc0 | -7.19707 | -43.12536 | 2025-07-11 04:57:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 6049180a-16d9-31d2-a9f1-31710d88ea0f | -6.62335 | -56.27831 | 2025-07-11 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README18.md)
