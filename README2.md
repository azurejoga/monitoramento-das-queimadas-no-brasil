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
| 1a0c08e1-c3c2-378e-b74c-f3330f23d8b4 | -15.07839 | -48.94292 | 2025-05-01 04:17:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5eb5e3e5-f69b-32c3-a427-6b29e5a78eeb | -20.57916 | -44.57431 | 2025-05-01 04:17:00 | NPP-375D | PASSA TEMPO | MINAS GERAIS | Brasil | 3147709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 56bca180-501b-35a9-a19d-1d89827c59ed | -17.61939 | -50.91694 | 2025-05-01 04:17:00 | NPP-375D | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4f7efabf-e76c-388c-a694-281ad91d93c5 | -15.93072 | -49.60503 | 2025-05-01 04:19:00 | NPP-375D | ITAGUARI | GOIÁS | Brasil | 5210562 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 063df8a3-bcce-39c1-af8f-6280bfa84185 | -15.89904 | -48.55367 | 2025-05-01 04:19:00 | NPP-375D | CORUMBÁ DE GOIÁS | GOIÁS | Brasil | 5205802 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2f994ee8-7c93-345b-b9c4-b252a17a4a08 | -23.60144 | -49.00198 | 2025-05-01 04:19:00 | NPP-375D | ITAÍ | SÃO PAULO | Brasil | 3521804 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d8ad2448-3379-3ba3-81e6-3f4765f71b72 | -24.24212 | -50.74139 | 2025-05-01 04:19:00 | NPP-375D | ORTIGUEIRA | PARANÁ | Brasil | 4117305 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| dbac1075-d122-3ef7-a803-f552a151482a | -23.61032 | -49.012 | 2025-05-01 04:19:00 | NPP-375D | ITAÍ | SÃO PAULO | Brasil | 3521804 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7b165a8d-1fff-30ef-acae-1ec85343c82e | -23.59294 | -47.43982 | 2025-05-01 04:19:00 | NPP-375D | VOTORANTIM | SÃO PAULO | Brasil | 3557006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 80fb3a5c-980f-3058-881d-5325c517f46f | -23.98281 | -48.91863 | 2025-05-01 04:19:00 | NPP-375D | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e19197ce-960d-3a6b-914a-a83054377bda | -23.33694 | -46.77397 | 2025-05-01 04:19:00 | NPP-375D | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 2866cf59-7a21-36c1-b5ff-5f85f0dd678d | -21.47154 | -57.16014 | 2025-05-01 04:19:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4274eadb-e1c2-314b-9040-ddad1beaf4d5 | -15.56915 | -47.85449 | 2025-05-01 04:19:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cd7b79cd-3aee-35e0-af48-7faa097d46dd | -25.57095 | -49.35576 | 2025-05-01 04:19:00 | NPP-375D | ARAUCÁRIA | PARANÁ | Brasil | 4101804 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 084489c9-0ac0-3dac-b505-be38d4c3d87c | -15.89873 | -48.55485 | 2025-05-01 04:19:00 | NPP-375D | CORUMBÁ DE GOIÁS | GOIÁS | Brasil | 5205802 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f31fdd52-30de-3b49-85e4-82bb7c38d82a | -25.19097 | -49.32744 | 2025-05-01 04:19:00 | NPP-375D | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 92fce5b7-0ae3-3985-acff-04ff4df61aeb | -17.60862 | -49.59782 | 2025-05-01 04:19:00 | NPP-375D | PONTALINA | GOIÁS | Brasil | 5217708 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 40cf4cd4-ca1e-304d-8332-c96b125b153d | -23.42829 | -51.44857 | 2025-05-01 04:19:00 | NPP-375D | ARAPONGAS | PARANÁ | Brasil | 4101507 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 29e4ddd3-816c-3f03-aa0b-746d39c3c4f5 | -22.53811 | -48.81319 | 2025-05-01 04:19:00 | NPP-375D | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| aee5ad52-baf9-3b9e-9fe7-8ac6d39cd476 | -23.60076 | -49.00597 | 2025-05-01 04:19:00 | NPP-375D | ITAÍ | SÃO PAULO | Brasil | 3521804 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ea7392e4-5ad5-3f9f-87f9-c540ff37b70e | -20.6228 | -55.03406 | 2025-05-01 04:19:00 | NPP-375D | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ec6cbcc8-8377-38dd-aa81-9077a8a2af25 | -21.47068 | -57.16401 | 2025-05-01 04:19:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8a0a5b8e-0585-3636-a5b0-fc933b552efe | -20.62161 | -55.03981 | 2025-05-01 04:19:00 | NPP-375D | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 27dbdb51-b7c5-3505-9a9d-b47605f5fb88 | -22.04467 | -50.22989 | 2025-05-01 04:19:00 | NPP-375D | POMPÉIA | SÃO PAULO | Brasil | 3540002 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.2 |
| a4397e2a-ebb3-3fde-8f47-fdf0cc0c4c89 | -22.04911 | -50.2261 | 2025-05-01 04:19:00 | NPP-375D | POMPÉIA | SÃO PAULO | Brasil | 3540002 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.2 |
| 57b0e3e0-7b18-370e-9ed7-f50b8c2c96e9 | -28.58666 | -49.44345 | 2025-05-01 04:19:00 | NPP-375D | SIDERÓPOLIS | SANTA CATARINA | Brasil | 4217600 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| e7031e36-31e0-3450-91f3-2532b145b389 | -15.92826 | -49.60619 | 2025-05-01 04:19:00 | NPP-375D | ITAGUARI | GOIÁS | Brasil | 5210562 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 25c59b92-7b25-3386-a056-09c0dc891864 | -23.32737 | -52.04295 | 2025-05-01 04:19:00 | NPP-375D | MARINGÁ | PARANÁ | Brasil | 4115200 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 8c5f4ebe-3978-39ba-bf58-1806e14b7ede | -22.90031 | -43.75362 | 2025-05-01 04:19:00 | NPP-375D | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 59bbbd25-0cad-3806-9dcc-efabf0685318 | -23.60417 | -49.00665 | 2025-05-01 04:19:00 | NPP-375D | ITAÍ | SÃO PAULO | Brasil | 3521804 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 35275a15-5464-3d1d-9979-04d3d9601a12 | -23.27135 | -51.20747 | 2025-05-01 04:19:00 | NPP-375D | LONDRINA | PARANÁ | Brasil | 4113700 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 55d48885-79db-3f6a-ae3e-2cc5c76ff727 | -25.03475 | -53.17335 | 2025-05-01 04:19:00 | NPP-375D | CASCAVEL | PARANÁ | Brasil | 4104808 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 874f23fd-74df-3b5d-93f2-8d23c0013da1 | -22.78479 | -43.75571 | 2025-05-01 04:19:00 | NPP-375D | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| bdc8eb54-31eb-38b7-a4e1-f48b541a2a59 | -23.60691 | -49.01133 | 2025-05-01 04:19:00 | NPP-375D | ITAÍ | SÃO PAULO | Brasil | 3521804 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6c2ef3b5-adac-39f7-b55e-13e29d366abb | -26.33469 | -53.18655 | 2025-05-01 04:19:00 | NPP-375D | FLOR DA SERRA DO SUL | PARANÁ | Brasil | 4107850 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 92bacd11-08cf-3ee3-90f6-9e8d7fdeba51 | -32.33578 | -53.61192 | 2025-05-01 04:21:00 | NPP-375D | JAGUARÃO | RIO GRANDE DO SUL | Brasil | 4311007 | 43 | 33 | nan | nan | nan | Pampa | 1.1 |
| b8c7afab-ee24-325c-857b-6072df41f5d6 | -29.74026 | -51.26808 | 2025-05-01 04:21:00 | NPP-375D | PORTÃO | RIO GRANDE DO SUL | Brasil | 4314803 | 43 | 33 | nan | nan | nan | Pampa | 0.8 |
| aa6dc0be-c099-3545-826d-5e72be6f4775 | -30.00555 | -51.07537 | 2025-05-01 04:21:00 | NPP-375D | ALVORADA | RIO GRANDE DO SUL | Brasil | 4300604 | 43 | 33 | nan | nan | nan | Pampa | 0.4 |
| 4f321c91-9802-3b29-b3fa-023b818b79e1 | -29.70717 | -52.5752 | 2025-05-01 04:21:00 | NPP-375D | VERA CRUZ | RIO GRANDE DO SUL | Brasil | 4322707 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 66dc81f4-187c-3299-862e-30ff10fb7472 | -5.85288 | -46.18626 | 2025-05-01 04:36:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| da6bc480-51f0-34c2-92bd-0199bc9030fb | -6.19496 | -48.04292 | 2025-05-01 04:36:00 | NOAA-20 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9db25225-2269-3b89-9d34-4af9eefed51e | -4.86398 | -47.40847 | 2025-05-01 04:36:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 44fd73e4-2b3e-3122-9a71-ca41eb9efdbd | -6.19551 | -48.03936 | 2025-05-01 04:36:00 | NOAA-20 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 758bc369-9c25-386b-8175-0ebf2585d2c3 | -6.55029 | -44.47475 | 2025-05-01 04:36:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8aa5f9c7-ccab-3f26-a053-8e974dd6bdea | -6.48692 | -43.78715 | 2025-05-01 04:36:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ec1a4970-b5e9-3057-a312-c1fd544dddd2 | -6.88421 | -43.96243 | 2025-05-01 04:36:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1ca7e268-5b4a-36e8-8af0-1e3681fd6228 | -6.70052 | -42.12645 | 2025-05-01 04:36:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| b19632d1-c3d4-390e-a465-2c57dc23ac0d | -6.54977 | -44.47828 | 2025-05-01 04:36:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 598dc57c-155c-3df1-84f3-96c59ab8b694 | -6.69581 | -42.1258 | 2025-05-01 04:36:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 9.6 |
| 6c7ba63c-b3f5-37e5-b258-faa5e55dc7c1 | -6.19943 | -48.0363 | 2025-05-01 04:36:00 | NOAA-20 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1b1fe73b-e10a-32ef-b174-9271aecd0856 | -6.48791 | -43.7865 | 2025-05-01 04:36:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4d8cee3f-801f-3e88-afa7-85d7359d281d | -4.64976 | -47.5464 | 2025-05-01 04:36:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 45a44185-6725-3e24-8a85-5e3cf8aa3cae | -7.08336 | -44.3817 | 2025-05-01 04:38:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e823e949-63f9-3766-8002-134376b52747 | -11.88151 | -58.06774 | 2025-05-01 04:38:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ebe724d8-e831-3b6e-8c8d-29d45673512d | -13.25663 | -53.3666 | 2025-05-01 04:38:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5d6a6488-d268-3cc9-adef-2cfbcf87ece1 | -8.41116 | -49.85286 | 2025-05-01 04:38:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 23c626dd-dc1d-3342-84db-4d5b059c6aff | -11.40386 | -52.94832 | 2025-05-01 04:38:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7006a715-64b9-3d91-b6a6-0c46fff20716 | -8.41447 | -49.85339 | 2025-05-01 04:38:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| acae3eeb-2a3c-3973-83b8-e22b8b1c6b9a | -7.07063 | -44.38369 | 2025-05-01 04:38:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e1c0e6a5-d5c5-34bc-8875-3f4b0bdedcd5 | -7.0701 | -44.38732 | 2025-05-01 04:38:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 523d21a8-06de-3a39-9362-2df4a21fb57d | -12.03489 | -37.96734 | 2025-05-01 04:38:00 | NOAA-20 | CARDEAL DA SILVA | BAHIA | Brasil | 2907004 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| 5a63e991-34e2-354c-a2d3-18879de99dd3 | -7.2113 | -43.11996 | 2025-05-01 04:38:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 97a54d56-99b3-3839-8ef7-40d2c542892b | -8.08375 | -43.10994 | 2025-05-01 04:38:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 796c6693-2098-3457-9c94-85199f52ab4f | -11.8824 | -58.06282 | 2025-05-01 04:38:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 72e2a166-3c40-30d1-8df8-6fa679e54ab7 | -8.86108 | -49.88535 | 2025-05-01 04:38:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 02228973-5afb-3030-82f6-eb8b6813e91c | -10.66913 | -44.4043 | 2025-05-01 04:38:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 7eea9f64-c0aa-307d-b0c4-89a8f8bba12b | -11.40255 | -52.95618 | 2025-05-01 04:38:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| b4c3d2b7-43fa-3463-9f8c-1f7818486891 | -10.67343 | -44.40475 | 2025-05-01 04:38:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 129f0b0f-4742-3869-abd1-0ab588f9fee4 | -13.1854 | -53.25002 | 2025-05-01 04:38:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ea17e336-d3a0-3783-a174-67a52395c708 | -12.03304 | -37.9632 | 2025-05-01 04:38:00 | NOAA-20 | CARDEAL DA SILVA | BAHIA | Brasil | 2907004 | 29 | 33 | nan | nan | nan | Mata Atlântica | 6.2 |
| 64e5d114-87ba-3d86-aa82-c83f1cbce636 | -8.86053 | -49.88882 | 2025-05-01 04:38:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0dc535e7-9203-3852-89ce-049a5341b1de | -7.21573 | -43.1206 | 2025-05-01 04:38:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| c382474e-4531-3d62-befa-c23a8cc6644c | -12.03557 | -37.96148 | 2025-05-01 04:38:00 | NOAA-20 | CARDEAL DA SILVA | BAHIA | Brasil | 2907004 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| ac563d64-8839-3a15-a153-c10b082af4b2 | -7.08389 | -44.37803 | 2025-05-01 04:38:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d26548a3-4432-3221-8c3d-1b87c181475c | -6.63025 | -48.01405 | 2025-05-01 04:38:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5a1c131a-210f-3d09-bd5b-290f9ab18632 | -10.6697 | -44.40025 | 2025-05-01 04:38:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 7324e03d-aab7-3d73-9b57-98988cc8a61d | -11.83008 | -51.34042 | 2025-05-01 04:38:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e0df1da9-c99c-3c64-9b95-03d60bc0593e | -8.08115 | -43.11078 | 2025-05-01 04:38:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 523629d7-9c99-3a31-8380-0b4afd4144a6 | -8.85777 | -49.88482 | 2025-05-01 04:38:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4cc28a32-b53a-3113-8f25-b028bf554d30 | -11.87912 | -58.06474 | 2025-05-01 04:38:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 168a5a9c-ed17-35e9-94dd-0a07b816bd55 | -6.6297 | -48.01763 | 2025-05-01 04:38:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f290d962-a680-3e2c-a1fc-2945c61d5cbb | -9.61908 | -37.03281 | 2025-05-01 04:38:00 | NOAA-20 | MAJOR ISIDORO | ALAGOAS | Brasil | 2704401 | 27 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 1bd0df41-23c0-3e64-9075-67feeef7b33f | -8.86384 | -49.88935 | 2025-05-01 04:38:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d658f373-6495-36c4-ba97-891d90e123f8 | -9.61986 | -37.0265 | 2025-05-01 04:38:00 | NOAA-20 | MAJOR ISIDORO | ALAGOAS | Brasil | 2704401 | 27 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 6418431d-e86c-37dd-bff3-095fc97a02d3 | -18.95637 | -52.38207 | 2025-05-01 04:40:00 | NOAA-20 | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 6d4ac546-6b5a-3bfd-8223-2b773751e187 | -19.3572 | -53.2118 | 2025-05-01 04:40:00 | NOAA-20 | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1d0f17f7-46e9-31ee-af4b-19a5d11a2064 | -20.27334 | -54.63817 | 2025-05-01 04:40:00 | NOAA-20 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 11c091b4-19d3-368c-8a48-6343a839a99c | -17.6193 | -50.91714 | 2025-05-01 04:40:00 | NOAA-20 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f58a4189-9b93-328d-95e4-d0c42abb8c05 | -15.89947 | -48.5538 | 2025-05-01 04:40:00 | NOAA-20 | CORUMBÁ DE GOIÁS | GOIÁS | Brasil | 5205802 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0b37af41-2d38-38fc-9f9e-aaeb85989982 | -19.36053 | -53.21239 | 2025-05-01 04:40:00 | NOAA-20 | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0d43593b-35de-3abe-b6f8-7937cdc1ee30 | -18.95188 | -52.08589 | 2025-05-01 04:40:00 | NOAA-20 | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c3386f39-9218-39d8-adef-3c9807a3cd61 | -17.90748 | -54.65349 | 2025-05-01 04:40:00 | NOAA-20 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 82a823e9-09b0-3141-9f68-1d2be377628b | -20.14288 | -46.91156 | 2025-05-01 04:40:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| deb5944d-0c90-3c1a-a3a1-03ba0900e277 | -15.93139 | -49.60393 | 2025-05-01 04:40:00 | NOAA-20 | ITAGUARI | GOIÁS | Brasil | 5210562 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 72fe05b1-8886-333d-a4d7-ebabe517af9f | -20.99552 | -51.79293 | 2025-05-01 04:40:00 | NOAA-20 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| d4f3c3eb-f358-3eb3-b4e0-e37fe19bdfef | -15.78624 | -54.51313 | 2025-05-01 04:40:00 | NOAA-20 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 422f6ea0-3b03-3c91-b70c-04aae93d1307 | -15.57001 | -47.85495 | 2025-05-01 04:40:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2290733b-32a6-37b5-ae15-f90a16705785 | -21.19293 | -44.9362 | 2025-05-01 04:40:00 | NOAA-20 | IJACI | MINAS GERAIS | Brasil | 3130408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| eea6c3cc-82b7-384f-b198-9d1cba54ce3e | -15.86866 | -53.26267 | 2025-05-01 04:40:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d92f4de2-4309-3d8d-b774-c2055334a779 | -20.62335 | -55.0363 | 2025-05-01 04:40:00 | NOAA-20 | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 2.7 |


[Clique aqui para ver as próximas entradas](README3.md)
