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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d8694ec5-d7a4-340b-97c5-f255154ddb04 | -8.35471 | -45.17682 | 2025-02-06 04:12:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1b428e0e-c469-3284-8c59-2b1b1c82627a | -8.86252 | -48.83055 | 2025-02-06 04:12:00 | NOAA-20 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4479c48e-5230-36a9-b427-1676057b02bb | -9.29564 | -43.27155 | 2025-02-06 04:12:00 | NOAA-20 | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 0b4f36c3-36aa-309e-b48f-c4d8ebed9e1d | -7.86154 | -43.12754 | 2025-02-06 04:12:00 | NOAA-20 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| f6971d2f-6e02-3e2e-8c15-1f5ec5c51191 | -8.1216 | -43.1363 | 2025-02-06 04:12:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 729cfdbd-c188-3c62-8e99-fba7cc73a730 | -4.32465 | -39.15775 | 2025-02-06 04:12:00 | NOAA-20 | CANINDÉ | CEARÁ | Brasil | 2302800 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| c4cc515e-11fe-3b15-8a99-7ee08ca74d8c | -7.86485 | -43.12807 | 2025-02-06 04:12:00 | NOAA-20 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 4be6a674-233e-31de-b1a7-f54385f732a3 | -6.23875 | -44.83318 | 2025-02-06 04:12:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 99dd187c-1111-3efe-bbc5-0bf0f4d33f78 | -8.35191 | -45.17265 | 2025-02-06 04:12:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7a433296-e5d4-3591-bb5f-f703a35c8279 | -6.21726 | -41.51972 | 2025-02-06 04:12:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| aebfe92f-ea80-342d-b813-74002274c85e | -8.34794 | -45.17574 | 2025-02-06 04:12:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 798e5ca1-8358-39fc-af25-124bb963ab69 | -8.12105 | -43.13977 | 2025-02-06 04:12:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 4805d729-da56-36c0-a8e3-fed7fe289a6c | -7.03285 | -44.36964 | 2025-02-06 04:12:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6499cc0b-3ff8-31d5-aa0c-eed5e55a1d6e | -13.90171 | -38.94803 | 2025-02-06 04:14:00 | NOAA-20 | MARAÚ | BAHIA | Brasil | 2920700 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 0d05fc2e-bdc9-3344-bf92-95c5ee185b97 | -9.98481 | -48.0817 | 2025-02-06 04:14:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6c138bfa-653d-364d-9168-d753995999c0 | -12.45712 | -43.56707 | 2025-02-06 04:14:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e9c0ecc0-39ee-3b80-b4df-449aabb63a58 | -13.61458 | -42.24287 | 2025-02-06 04:14:00 | NOAA-20 | PARAMIRIM | BAHIA | Brasil | 2923605 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| ceb17ff4-cfd7-32cc-b364-1bf917d38ebd | -12.84989 | -43.81961 | 2025-02-06 04:14:00 | NOAA-20 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c41e7d45-dc75-3199-a845-b0035ea1f6e7 | -12.87862 | -43.47844 | 2025-02-06 04:14:00 | NOAA-20 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 752d5102-daa7-3b4f-8c28-0a315961e58f | -11.25525 | -41.90547 | 2025-02-06 04:14:00 | NOAA-20 | IRECÊ | BAHIA | Brasil | 2914604 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 3ff1a877-b57d-3d39-a1ac-efaa2b11e183 | -16.08669 | -39.40798 | 2025-02-06 04:14:00 | NOAA-20 | BELMONTE | BAHIA | Brasil | 2903409 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 5be12a01-ff7f-3862-b4a5-f254d477a394 | -13.90596 | -38.94863 | 2025-02-06 04:14:00 | NOAA-20 | MARAÚ | BAHIA | Brasil | 2920700 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 3f1f8a03-7e42-3c6c-a55b-4d86e03dd032 | -15.64693 | -39.19028 | 2025-02-06 04:14:00 | NOAA-20 | CANAVIEIRAS | BAHIA | Brasil | 2906303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| dbdb3df7-dae5-3d33-8dfb-9918ba67520e | -12.41422 | -43.80531 | 2025-02-06 04:14:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 389c5779-6530-3dce-86f0-3ef4172b1812 | -11.58201 | -47.63398 | 2025-02-06 04:14:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 59fdb966-4b98-3038-a108-a0b5d5e87ba0 | -11.58184 | -47.63125 | 2025-02-06 04:14:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c9ae0815-7a39-37ff-a529-14666502ab84 | -11.58477 | -47.6361 | 2025-02-06 04:14:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d4e92c69-acf9-3ad2-bda6-773b8bd7fb10 | -11.14841 | -42.15282 | 2025-02-06 04:14:00 | NOAA-20 | CENTRAL | BAHIA | Brasil | 2907608 | 29 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 42920cbe-b895-342e-a0cb-a2df9974c852 | -12.49133 | -43.78831 | 2025-02-06 04:14:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| d91bbbeb-a981-39b4-b320-e6fdb2456e71 | -12.84601 | -43.82265 | 2025-02-06 04:14:00 | NOAA-20 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8fec39e7-7255-38c8-bb01-cc53940ed7e7 | -10.72821 | -47.2653 | 2025-02-06 04:14:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| edd691e3-47f2-3ad4-82e0-80b24721cb4d | -14.78101 | -42.66602 | 2025-02-06 04:14:00 | NOAA-20 | URANDI | BAHIA | Brasil | 2932606 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 59a1299a-ae05-3fc1-9cd0-8d934670a0f0 | -12.84934 | -43.82318 | 2025-02-06 04:14:00 | NOAA-20 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4797b72f-4147-32b0-ba3e-3842fdaba8d8 | -16.85264 | -40.82539 | 2025-02-06 04:14:00 | NOAA-20 | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| b3135b07-8e05-33c7-a7b0-8449b9f2a154 | -12.10722 | -44.74496 | 2025-02-06 04:14:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 824ede3a-ff00-3b9a-a21f-c33baca540ac | -16.86539 | -40.82038 | 2025-02-06 04:14:00 | NOAA-20 | FRONTEIRA DOS VALES | MINAS GERAIS | Brasil | 3127057 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 9ba20d04-ae5b-3135-8b62-15fa7bec7129 | -10.34646 | -47.90068 | 2025-02-06 04:14:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c12f863d-611d-3203-b30f-52f4c83d2c4a | -13.99805 | -44.03141 | 2025-02-06 04:14:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| db95de2e-a558-3869-b2c0-5d3d79f461e3 | -12.85598 | -43.82043 | 2025-02-06 04:14:00 | NOAA-20 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 98646a19-f72e-35f7-8615-de64468d32c9 | -16.86511 | -40.82174 | 2025-02-06 04:14:00 | NOAA-20 | FRONTEIRA DOS VALES | MINAS GERAIS | Brasil | 3127057 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 40c5b8a8-70a7-3d49-b982-478debe8b141 | -16.85287 | -40.8241 | 2025-02-06 04:14:00 | NOAA-20 | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 701fddca-f65b-3634-acef-f36f58342771 | -12.41478 | -43.80176 | 2025-02-06 04:14:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7ebfa089-c418-3df4-8828-224c90cae001 | -16.86441 | -40.82704 | 2025-02-06 04:14:00 | NOAA-20 | FRONTEIRA DOS VALES | MINAS GERAIS | Brasil | 3127057 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| ae2219e5-6598-356b-b298-9a054fcd8a24 | -12.48801 | -43.78779 | 2025-02-06 04:14:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 5b64bf41-662e-30e5-8272-49a4c55208f7 | -16.86465 | -40.82573 | 2025-02-06 04:14:00 | NOAA-20 | FRONTEIRA DOS VALES | MINAS GERAIS | Brasil | 3127057 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 4bd9a5d8-cc2f-3ef5-a0f9-9c0103dd3a33 | -12.47398 | -41.11388 | 2025-02-06 04:14:00 | NOAA-20 | LAJEDINHO | BAHIA | Brasil | 2919009 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| e0a87cc8-21ae-349c-9bda-e0b892f60bc9 | -9.984 | -48.08639 | 2025-02-06 04:14:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9161a157-1e04-3d3f-b3e9-3b9d72fb01dc | -12.74243 | -44.83092 | 2025-02-06 04:14:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 70c3df3d-f690-3217-8b03-932a5d95a15d | -10.78371 | -44.75682 | 2025-02-06 04:14:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 5773333e-cd64-3fcb-a7ad-9c44706bdfa0 | -14.9286 | -41.73734 | 2025-02-06 04:14:00 | NOAA-20 | PIRIPÁ | BAHIA | Brasil | 2924702 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| ec3f9013-448c-39f6-89d3-212b946401ec | -10.85223 | -44.77522 | 2025-02-06 04:14:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a8111db8-8654-3d74-98e3-293e4f8bb9e3 | -12.85265 | -43.8199 | 2025-02-06 04:14:00 | NOAA-20 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e7a13c1c-4977-378d-a6d1-bdb8a968e010 | -16.03571 | -42.13824 | 2025-02-06 04:14:00 | NOAA-20 | SALINAS | MINAS GERAIS | Brasil | 3157005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 7ae8835f-b984-3334-85c3-76ba3598dca2 | -16.68155 | -43.88617 | 2025-02-06 04:14:00 | NOAA-20 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 38e08b4b-dc65-33fb-8834-129c58ba2b8e | -12.07497 | -40.67315 | 2025-02-06 04:14:00 | NOAA-20 | MUNDO NOVO | BAHIA | Brasil | 2922102 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 5f52bfbf-2775-3e05-9dad-ee6355d8dcab | -12.30907 | -43.53998 | 2025-02-06 04:14:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d7ab5609-23b2-3fe2-8550-5bb4b1b38cf0 | -10.7859 | -44.76439 | 2025-02-06 04:14:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5aa66ff3-3503-3282-9ae2-f908003387f2 | -16.85656 | -40.826 | 2025-02-06 04:14:00 | NOAA-20 | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 1a942c36-59a7-30b9-b490-e6572377df91 | -16.86901 | -40.61697 | 2025-02-06 04:14:00 | NOAA-20 | SANTA HELENA DE MINAS | MINAS GERAIS | Brasil | 3157658 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 10cb68d4-1cbb-3f63-b1d1-56c12d35098e | -11.49619 | -43.22211 | 2025-02-06 04:14:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 090671e7-ece0-3f09-bc55-a55ff18168be | -16.86835 | -40.8275 | 2025-02-06 04:14:00 | NOAA-20 | FRONTEIRA DOS VALES | MINAS GERAIS | Brasil | 3127057 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| e681ae8a-00e3-33a1-8a82-2707ad44de37 | -13.99472 | -44.03087 | 2025-02-06 04:14:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f8b05c8f-736b-38f0-83d2-3a64b4f429c3 | -9.98574 | -48.07965 | 2025-02-06 04:14:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7ab05eef-55f8-395b-b0d6-2d1a47d9886d | -12.8521 | -43.82347 | 2025-02-06 04:14:00 | NOAA-20 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| aea19ec7-22f1-3cd8-bad1-223a8cac1ab6 | -10.78096 | -44.75277 | 2025-02-06 04:14:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 41b009b5-ca4e-3678-8b5f-70f272f042fc | -12.49188 | -43.78476 | 2025-02-06 04:14:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ed564812-d24c-3de5-a24b-6173d1a4b148 | -11.58114 | -47.63552 | 2025-02-06 04:14:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9ec20e4e-bcce-3e71-9737-b7686e181f18 | -9.98419 | -48.089 | 2025-02-06 04:14:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 87c6d5c5-a26b-3f23-b9b4-747492ec8ddf | -11.05043 | -46.12101 | 2025-02-06 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c3bcde02-2e93-3047-aaae-ea51a7dce6c8 | -10.78039 | -44.75629 | 2025-02-06 04:14:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 603d5e6b-238d-36a4-9f81-632b1618a29e | -10.78647 | -44.76088 | 2025-02-06 04:14:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7fcfdf97-5992-30f1-a147-c8114406be68 | -16.03933 | -42.13872 | 2025-02-06 04:14:00 | NOAA-20 | SALINAS | MINAS GERAIS | Brasil | 3157005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 15f492bc-0348-3f78-9360-a189034b87c5 | -12.74187 | -44.83445 | 2025-02-06 04:14:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a021167e-8a57-3197-bc3b-c3ad440bff15 | -12.46101 | -43.56402 | 2025-02-06 04:14:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f88274f2-41f9-389a-a08f-c69011d2c5ba | -16.85679 | -40.82471 | 2025-02-06 04:14:00 | NOAA-20 | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| da35fb1d-3580-3648-9bc1-c6ef513d3343 | -11.58564 | -47.63456 | 2025-02-06 04:14:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7d97a822-bba2-37db-ad21-d4b7e2862c13 | -20.76404 | -46.77103 | 2025-02-06 04:16:00 | NOAA-20 | ITAÚ DE MINAS | MINAS GERAIS | Brasil | 3133758 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| eb5ac76a-79b2-368b-b12a-1b331fb99935 | -19.49107 | -43.53159 | 2025-02-06 04:16:00 | NOAA-20 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 35e6a7b5-d035-393a-892e-8f56bdd48e43 | -20.31125 | -40.75215 | 2025-02-06 04:16:00 | NOAA-20 | DOMINGOS MARTINS | ESPÍRITO SANTO | Brasil | 3201902 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 28a82d07-e6da-32ae-b62e-eb866203e2b8 | -22.78618 | -43.75681 | 2025-02-06 04:16:00 | NOAA-20 | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| c13481f4-57bf-37c9-8fbd-ff9190638704 | -19.49164 | -43.5276 | 2025-02-06 04:16:00 | NOAA-20 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ca2faf39-d1f2-356d-bad5-7e30800123db | -23.33744 | -46.77435 | 2025-02-06 04:16:00 | NOAA-20 | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 610eb6fe-faee-3cf4-90e0-5d75e2d75f03 | -20.90013 | -43.8197 | 2025-02-06 04:16:00 | NOAA-20 | CARANDAÍ | MINAS GERAIS | Brasil | 3113206 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 7e83d495-1e8f-3a7a-bf2d-06fd2747da40 | -22.53784 | -48.81245 | 2025-02-06 04:16:00 | NOAA-20 | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ce5bb0ea-a28e-3019-a2f9-0f8ec4764122 | -23.69849 | -46.67917 | 2025-02-06 04:16:00 | NOAA-20 | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| d2291153-ceb4-3d4f-bc07-3ece6be7b593 | -18.6094 | -44.25528 | 2025-02-06 04:16:00 | NOAA-20 | INIMUTABA | MINAS GERAIS | Brasil | 3131109 | 31 | 33 | nan | nan | nan | Cerrado | 9.6 |
| e9faa16e-52a2-3fcd-af2b-25ef58380e08 | -19.49516 | -43.5281 | 2025-02-06 04:16:00 | NOAA-20 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 25e6a67a-cd06-3fc4-9bfb-be861d328e76 | -22.85649 | -42.97909 | 2025-02-06 04:16:00 | NOAA-20 | SÃO GONÇALO | RIO DE JANEIRO | Brasil | 3304904 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| b8555470-72c9-3d2f-9a07-a72d30902615 | -20.90642 | -42.57785 | 2025-02-06 04:16:00 | NOAA-20 | ERVÁLIA | MINAS GERAIS | Brasil | 3124005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 48e4175c-e2fd-300d-968d-a2cd9b16abbc | -19.48812 | -43.52711 | 2025-02-06 04:16:00 | NOAA-20 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| cc5f7b40-3818-35c6-8086-cd19cf2f249f | -20.41486 | -43.55375 | 2025-02-06 04:16:00 | NOAA-20 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| f5e597d5-1c2d-36be-a7e0-628b34d937d2 | -22.90182 | -43.75403 | 2025-02-06 04:16:00 | NOAA-20 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 745e6a7c-9dc7-39a6-be93-ac9b14b960d5 | -28.8633 | -53.3959 | 2025-02-06 04:18:00 | NOAA-20 | BOA VISTA DO INCRA | RIO GRANDE DO SUL | Brasil | 4302238 | 43 | 33 | nan | nan | nan | Pampa | 0.7 |
| ed503df6-1b29-3869-834a-5a80b684b690 | -29.93121 | -50.96929 | 2025-02-06 04:18:00 | NOAA-20 | GRAVATAÍ | RIO GRANDE DO SUL | Brasil | 4309209 | 43 | 33 | nan | nan | nan | Pampa | 1.5 |
| c6cb8c06-7cb5-362b-a5b2-39c043bbe05f | -29.87327 | -51.1594 | 2025-02-06 04:18:00 | NOAA-20 | CANOAS | RIO GRANDE DO SUL | Brasil | 4304606 | 43 | 33 | nan | nan | nan | Pampa | 1.8 |
| 048b825b-95c2-38ff-86af-28a403f565fd | -28.86595 | -53.39259 | 2025-02-06 04:18:00 | NOAA-20 | BOA VISTA DO INCRA | RIO GRANDE DO SUL | Brasil | 4302238 | 43 | 33 | nan | nan | nan | Pampa | 0.9 |
| a9d89f18-f60e-3db6-b57e-f9e4564508f0 | -29.91338 | -54.35626 | 2025-02-06 04:18:00 | NOAA-20 | CACEQUI | RIO GRANDE DO SUL | Brasil | 4302907 | 43 | 33 | nan | nan | nan | Pampa | 2.5 |
| 749eff3f-a644-38cf-a253-1d4a287add96 | -29.91222 | -54.36206 | 2025-02-06 04:18:00 | NOAA-20 | CACEQUI | RIO GRANDE DO SUL | Brasil | 4302907 | 43 | 33 | nan | nan | nan | Pampa | 3.0 |
| a1debd7b-bbeb-350b-8247-5d932533c45f | -29.63204 | -56.6426 | 2025-02-06 04:21:00 | NOAA-20 | URUGUAIANA | RIO GRANDE DO SUL | Brasil | 4322400 | 43 | 33 | nan | nan | nan | Pampa | 3.7 |
| cfd234f2-bcfd-3749-a399-dfa6076b96ec | -29.62197 | -56.6452 | 2025-02-06 04:21:00 | NOAA-20 | URUGUAIANA | RIO GRANDE DO SUL | Brasil | 4322400 | 43 | 33 | nan | nan | nan | Pampa | 1.7 |


[Clique aqui para ver as próximas entradas](README4.md)
