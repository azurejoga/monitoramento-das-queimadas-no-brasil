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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 57c616d0-9859-39b0-a2c9-b1ac8675ae80 | -6.5075 | -56.1932 | 2025-07-31 00:50:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 102.6 |
| 01c5eba3-5fd0-30c1-b1be-eb19cd6d086f | -13.5044 | -45.6726 | 2025-07-31 00:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 75.3 |
| af4d67fa-fcd9-36bb-a7ea-57f02d7ab5cc | -6.5074 | -56.213 | 2025-07-31 00:50:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 85.1 |
| 45f4990a-c5f8-3edb-bcf9-da39bf1d0219 | -6.6726 | -56.3831 | 2025-07-31 00:50:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 61.4 |
| ba9fea3d-488c-319b-801c-dd166e0cab0c | -6.5074 | -56.213 | 2025-07-31 01:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 67.8 |
| a9ca2a8c-4c2b-33d6-b9e0-e4ef0ace0a72 | -6.654 | -56.4038 | 2025-07-31 01:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 57.0 |
| add022c4-c807-32a4-9b77-3cdd6d0e61af | -6.6328 | -59.9841 | 2025-07-31 01:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 41.2 |
| 7fab530d-14ce-3417-874e-4b343fcbae53 | -6.6726 | -56.3831 | 2025-07-31 01:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 55.1 |
| 39f72ce2-b279-3952-824b-6a4c49758573 | -13.5243 | -45.6462 | 2025-07-31 01:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 57.3 |
| 3093ce66-3d9f-3bb5-a24f-0774e20bbb4d | -6.526 | -56.1923 | 2025-07-31 01:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 110.8 |
| 46b58b6b-6b80-34b3-aa40-83bccb6fe9ac | -10.0843 | -53.8712 | 2025-07-31 01:00:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 128.7 |
| b33db976-02c2-348b-af32-bea4eb318afd | -6.5258 | -56.2121 | 2025-07-31 01:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 91.5 |
| a9726558-a415-3e6b-9229-83138278745b | -6.6725 | -56.4029 | 2025-07-31 01:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 117.8 |
| 92451843-8a57-31c5-86d3-4d16f07ec071 | -11.7508 | -48.1825 | 2025-07-31 01:00:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 132.6 |
| f8cc7028-213d-3c7e-b84b-d24fd5f56d65 | -13.5238 | -45.6693 | 2025-07-31 01:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 74.1 |
| 4e2f89b2-2ab5-3ba6-9a5d-c15f2e79f573 | -6.5075 | -56.1932 | 2025-07-31 01:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 82.1 |
| 92e7cf1f-26cc-3f0f-80e3-5b9ed529a0d7 | -10.0655 | -53.8727 | 2025-07-31 01:00:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 77.6 |
| c051576a-1b96-3241-a041-1869efd26213 | -6.526 | -56.1923 | 2025-07-31 01:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 88.3 |
| 775fedaa-ac81-3a1e-a4ea-773909e2dce4 | -6.5629 | -56.1906 | 2025-07-31 01:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 50.4 |
| 671ab34a-b411-35da-baae-af0ea0a12da9 | -6.5258 | -56.2121 | 2025-07-31 01:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 77.9 |
| 08e96b5d-258c-3bb7-8fab-c87b0489eff0 | -18.553 | -46.6929 | 2025-07-31 01:10:00 | GOES-19 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 42.6 |
| 830cd06b-627e-3119-822f-e25b39eaa61a | -6.6725 | -56.4029 | 2025-07-31 01:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 141.1 |
| 6c6eeb1c-1756-38e5-9822-b2c81c5a08c2 | -11.7508 | -48.1825 | 2025-07-31 01:10:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 75.0 |
| e325d2a7-e2b4-31ca-9f5b-2906d5dd143f | -10.0843 | -53.8712 | 2025-07-31 01:10:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 154.3 |
| ef43d722-b0c9-37b9-b755-b2e78043c515 | -10.0655 | -53.8727 | 2025-07-31 01:10:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 87.2 |
| cbbbbd35-da3b-398a-9f3f-82d0171d3ecc | -6.6726 | -56.3831 | 2025-07-31 01:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 52.7 |
| 95325afb-38d2-34b1-9f12-32cc8b5a1572 | -10.084 | -53.8916 | 2025-07-31 01:10:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 57.5 |
| 92c4d672-a61a-3781-8965-f68284ee977d | -6.654 | -56.4038 | 2025-07-31 01:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 52.0 |
| c6d81df4-746a-390a-8ef7-ed338c4a18d4 | -6.5075 | -56.1932 | 2025-07-31 01:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 89.6 |
| ff9a19fa-0830-36bc-a0ac-df7b45d902c6 | -6.5074 | -56.213 | 2025-07-31 01:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 80.5 |
| febf82b4-3b3a-3b35-8e23-83ce5c9c33ca | -10.069 | -53.875099 | 2025-07-31 01:19:00 | METOP-B | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e1a7806a-d352-34be-a0fd-85dbe3bab6a9 | -10.072 | -53.847099 | 2025-07-31 01:19:00 | METOP-B | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8012bd0d-ae26-3274-aa5a-971488002a62 | -11.9807 | -61.986698 | 2025-07-31 01:19:00 | METOP-B | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| e4f32c43-a420-3543-8336-8b8e70ba076f | -10.0624 | -53.849701 | 2025-07-31 01:19:00 | METOP-B | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 22076c3f-de79-370b-b65f-2076e33244a0 | -10.0852 | -53.8978 | 2025-07-31 01:19:00 | METOP-B | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d8be5eb4-5241-3ad8-aa9b-8d5dd607685d | -10.0786 | -53.872501 | 2025-07-31 01:19:00 | METOP-B | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 30e80321-5662-3184-8d53-eace5a9ff17e | -6.5258 | -56.2121 | 2025-07-31 01:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 85.2 |
| 92462fad-88b1-3703-ad42-3634c87d12ba | -6.526 | -56.1923 | 2025-07-31 01:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 92.3 |
| 3a1cd7af-562b-3d95-b4e3-d448ef5243e4 | -18.553 | -46.6929 | 2025-07-31 01:20:00 | GOES-19 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 47.7 |
| efb32f84-7995-367e-991e-9cf3e8c39321 | -6.6725 | -56.4029 | 2025-07-31 01:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 121.9 |
| 5ac13902-68cb-346f-8b94-ccbd16c8728d | -6.654 | -56.4038 | 2025-07-31 01:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 54.3 |
| 2c2570b1-35ac-3eea-903a-ba0358cdfe4a | -13.5243 | -45.6462 | 2025-07-31 01:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 87.2 |
| 3023ae13-291f-3ff2-a42d-3842c0fa6370 | -11.7508 | -48.1825 | 2025-07-31 01:20:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 122.6 |
| ba5269d9-817e-3587-bba0-ad666c7fd70f | -10.0843 | -53.8712 | 2025-07-31 01:20:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 148.8 |
| 7215336f-8bb3-3c1a-9f21-518180990aa5 | -6.5075 | -56.1932 | 2025-07-31 01:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 70.0 |
| 8b300aa9-b56c-3a19-b154-c33890f406e6 | -10.0655 | -53.8727 | 2025-07-31 01:20:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 49.8 |
| aa67f19a-e55a-3d70-a612-454939ea1f86 | -10.084 | -53.8916 | 2025-07-31 01:20:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 52.9 |
| 03de7b25-2d2b-3cc2-b107-84f5b87bc714 | -6.5074 | -56.213 | 2025-07-31 01:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 65.1 |
| 5cf63d4f-034a-31c2-821c-6cfc322e345c | -13.5247 | -45.6231 | 2025-07-31 01:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 63.3 |
| c2e1711b-46da-35b2-b17d-0ff52aa8a019 | -6.5231 | -56.203499 | 2025-07-31 01:20:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 517a0b8a-ef9a-3ee2-9af9-09c634581894 | -6.8125 | -59.264599 | 2025-07-31 01:20:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 50c7d1b8-ef0d-330a-894f-46707b488139 | -6.5084 | -56.185699 | 2025-07-31 01:20:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1b89d8b6-baeb-3081-ae09-a16bcdb4df44 | -6.5037 | -56.208199 | 2025-07-31 01:20:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| abd595be-3596-3cab-a842-73acf5a6ea26 | -6.8154 | -59.276901 | 2025-07-31 01:20:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d16dd6fb-d4d2-3cb7-96ad-0c853dbd2b6a | -6.5424 | -56.1987 | 2025-07-31 01:20:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 25209e32-f338-3d34-9f03-46be05108e66 | -6.6683 | -56.418701 | 2025-07-31 01:20:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e5f9c436-1242-31e3-ae87-83253eb7356a | -6.6636 | -56.3993 | 2025-07-31 01:20:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1d3619da-3952-3126-a2cf-c7a1650a955b | -6.5617 | -56.193901 | 2025-07-31 01:20:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 45a53bf0-195a-3411-bfb3-c3241843db34 | -6.6779 | -56.416302 | 2025-07-31 01:20:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 13eaf051-105c-3930-b791-4d2c5086dce4 | -6.6732 | -56.3969 | 2025-07-31 01:20:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bb0a0d86-d08b-3b58-84ef-20bd363dfeff | -6.6491 | -56.382301 | 2025-07-31 01:20:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0fd039c3-a1ca-3992-8a87-862787ac68c9 | -7.6241 | -67.321602 | 2025-07-31 01:20:00 | METOP-B | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 788cde25-030e-3845-92ec-9a434f2351aa | -6.6588 | -56.379902 | 2025-07-31 01:20:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1d7544ee-0c14-3821-8004-a28c1de20020 | -6.5134 | -56.205898 | 2025-07-31 01:20:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 597fdfd2-af64-32d0-a98e-b4381bae2a44 | -6.5181 | -56.1833 | 2025-07-31 01:20:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6d081f96-5508-3ed8-9350-599a69bf92bd | -6.5521 | -56.196301 | 2025-07-31 01:20:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e37f1966-c11f-3b81-9d84-06a21b32e26c | -6.6539 | -56.401699 | 2025-07-31 01:20:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5b7973e1-4d6c-3f10-b564-d98b780fc0e1 | -6.4987 | -56.188 | 2025-07-31 01:20:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7adf5d37-4652-30af-a665-5b2bfa036e9b | -6.6684 | -56.377499 | 2025-07-31 01:20:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 98a5105b-b6b9-358b-b6ac-b4ded615801c | -21.97771 | -57.58644 | 2025-07-31 01:22:00 | TERRA_M-M | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 5c57af18-d2e4-3564-b7f6-be053eb2c7f7 | -22.22396 | -56.04319 | 2025-07-31 01:22:00 | TERRA_M-M | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 52558ac5-060d-3d19-aea3-430df736170c | -21.33333 | -55.63955 | 2025-07-31 01:22:00 | TERRA_M-M | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | 7.9 |
| ddbdeed4-1d3f-33dc-be28-d36ce9f23706 | -21.97905 | -57.59602 | 2025-07-31 01:22:00 | TERRA_M-M | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 7.3 |
| a5b7d83e-2368-3640-889c-286b201dcbfb | -11.97013 | -55.52137 | 2025-07-31 01:24:00 | TERRA_M-M | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 13.5 |
| c72e59fb-6958-33e9-96f6-fb910564ca7f | -10.07616 | -53.85658 | 2025-07-31 01:24:00 | TERRA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 32.7 |
| 0a86d499-908c-30af-87c9-c3a6c370e8eb | -10.08041 | -53.89145 | 2025-07-31 01:24:00 | TERRA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 59.9 |
| 157c101c-2f71-38c7-9e6a-3e58b626d87b | -10.32019 | -54.1485 | 2025-07-31 01:24:00 | TERRA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 11.5 |
| dbdcf3f7-c103-336d-990a-40dc3e7543d4 | -10.07701 | -53.87097 | 2025-07-31 01:24:00 | TERRA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 269.2 |
| a2e3b2ee-de12-3f4d-81aa-31c154307ae4 | -10.31992 | -54.15501 | 2025-07-31 01:24:00 | TERRA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 23.8 |
| dcadb007-0436-3092-8fa0-83e325c5b9b4 | -11.9798 | -61.99193 | 2025-07-31 01:24:00 | TERRA_M-M | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 5.0 |
| b0a0b6e1-9a0d-3f4a-869e-30093ee04e8c | -10.0794 | -53.87706 | 2025-07-31 01:24:00 | TERRA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 252.8 |
| f2eab364-ebae-38ac-9f88-9a6d7a9c08a7 | -10.30727 | -54.15705 | 2025-07-31 01:24:00 | TERRA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 15.4 |
| cc60f43b-ef96-3440-9ba5-2f2e0c1dc329 | -6.5049 | -56.21046 | 2025-07-31 01:26:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 38.9 |
| 510818ac-dba1-3105-a9b2-b88d0627bc35 | -6.5164 | -56.20866 | 2025-07-31 01:26:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 85.3 |
| a4906e89-7083-3814-aaf2-ac91aa5dc5ee | -6.66299 | -56.41415 | 2025-07-31 01:26:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 31.0 |
| fe180def-c629-3e34-b810-32293cc06e50 | -6.81589 | -59.27457 | 2025-07-31 01:26:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 16.5 |
| 38da078b-805c-3fd3-a42f-2805230778af | -6.67206 | -56.39764 | 2025-07-31 01:26:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 115.5 |
| 96ded56a-e5c5-3269-8355-4887bd5b33cd | -6.56238 | -56.20139 | 2025-07-31 01:26:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 23.6 |
| a1eaaa12-3d13-340a-8fbe-63074f94ef29 | -6.95706 | -56.38152 | 2025-07-31 01:26:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 681d5d45-d313-3f4f-8b61-a2fda86f86e7 | -6.65854 | -56.38458 | 2025-07-31 01:26:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 15.9 |
| 3138e132-e076-3108-8bff-03ff732ddf8e | -10.05451 | -59.11087 | 2025-07-31 01:26:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 141535ed-39c0-315f-aec2-f4eb3c1660e4 | -10.23671 | -56.76619 | 2025-07-31 01:26:00 | TERRA_M-M | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 9.3 |
| a3b38d80-ab47-3f68-b3db-43fa37c7dc2c | -6.5279 | -56.2069 | 2025-07-31 01:26:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 40.3 |
| 5c3376b9-f868-33f9-ba61-385b727f4e49 | -6.51401 | -56.19299 | 2025-07-31 01:26:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 81.1 |
| fc920f51-8c25-3c6d-8824-ab4cc98f7ce3 | -6.56007 | -56.18584 | 2025-07-31 01:26:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 36.5 |
| d7feb8c2-7ca8-323e-8539-05aa680abf82 | -6.52553 | -56.19127 | 2025-07-31 01:26:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 25.7 |
| 949f8dc9-3ee1-36f9-b12b-b60ac0311e3c | -6.67433 | -56.41284 | 2025-07-31 01:26:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 55.8 |
| 0c5ddeb5-4a59-3d56-b781-9f23f8a6d16e | -6.55089 | -56.20325 | 2025-07-31 01:26:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 20.1 |
| 9a3b9f68-1a33-3899-8419-afbb146fdc33 | -6.50251 | -56.19486 | 2025-07-31 01:26:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 25.0 |
| babbe947-aef5-3e05-87be-d63418c91b79 | -6.50562 | -56.20004 | 2025-07-31 01:26:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 52.0 |


[Clique aqui para ver as próximas entradas](README5.md)
