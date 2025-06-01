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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 337fe355-9408-304c-b51b-12072f463541 | -14.80872 | -48.37366 | 2025-06-01 04:36:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b78ee9ff-c579-3414-af41-20ab6af0f2f4 | -10.68146 | -57.60784 | 2025-06-01 04:36:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8b0064d5-3b81-389e-b4df-ef42899a19a7 | -11.07809 | -54.7821 | 2025-06-01 04:36:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 93c2620b-eadf-3468-80aa-2b70377dd3f4 | -11.91809 | -54.41726 | 2025-06-01 04:36:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ef619abf-23e3-3d0b-a304-f09369ca2c3d | -13.10483 | -45.27029 | 2025-06-01 04:36:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 55d6a3a2-5a6c-39f4-a3c2-f10e7775335e | -11.44145 | -55.00265 | 2025-06-01 04:36:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7037d252-2256-3869-a2ac-a4f4a1a643d0 | -11.07933 | -54.76855 | 2025-06-01 04:36:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 76019ebc-8a96-3447-9250-d867ed6bf1bd | -11.0744 | -54.77174 | 2025-06-01 04:36:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e64edd74-e6b7-3fc1-84c2-b112c1766825 | -13.10867 | -45.27081 | 2025-06-01 04:36:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 168edea4-2e8e-392b-a3d9-518a7ff9f111 | -14.6836 | -52.68715 | 2025-06-01 04:36:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7d014a36-a0d9-3c7e-91bc-46785dea52b0 | -11.08144 | -54.78106 | 2025-06-01 04:36:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8181e460-38aa-3752-bba7-1f15e588340c | -13.09649 | -45.27396 | 2025-06-01 04:36:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7011569f-5bac-3d55-bf88-dd73834127d2 | -13.10935 | -45.26603 | 2025-06-01 04:36:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 21e60dd5-d2ad-397a-8bde-f87a8c882e9b | -11.8315 | -51.27253 | 2025-06-01 04:36:00 | NPP-375D | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cac8a08b-2e9e-38f2-b1da-43f60d92fe7b | -10.71986 | -48.68176 | 2025-06-01 04:36:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 9c3c3f6c-a289-3dc5-ab4b-033053632c0d | -13.90808 | -54.66323 | 2025-06-01 04:36:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ab9b5023-3af6-3b3c-a005-d0b30a065ac6 | -14.0334 | -55.13014 | 2025-06-01 04:36:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3a43d870-ba3e-3291-9e4a-1e5f6cc67e9a | -14.6703 | -45.12791 | 2025-06-01 04:36:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5ffa6402-dbdb-360e-b071-18d2a8fb1866 | -10.82657 | -56.94512 | 2025-06-01 04:36:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a5d5e79a-3aaa-3987-98a6-0016b84e2895 | -12.02423 | -49.52088 | 2025-06-01 04:36:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ad35454f-8798-39ab-a42b-2d4a458c3192 | -14.68716 | -52.68779 | 2025-06-01 04:36:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d0bf3dee-cbe9-3e13-9fb6-c4a8c403eab7 | -14.01838 | -55.14281 | 2025-06-01 04:36:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 74912ebe-3ed0-37d2-9cd4-169f58dff81a | -13.64117 | -52.18068 | 2025-06-01 04:36:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6246afff-c825-3718-b574-297a3789e0b8 | -11.07369 | -54.77566 | 2025-06-01 04:36:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4ab89ad4-c34a-3903-86d0-b1285770b695 | -12.0859 | -54.58092 | 2025-06-01 04:36:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4fd30342-a4ef-3cfb-8090-44e363db931b | -12.52456 | -57.18824 | 2025-06-01 04:36:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a04d9eab-4acf-39bc-b8a0-dd14ec48699a | -11.08073 | -54.78499 | 2025-06-01 04:36:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 70a9ed81-0f12-387b-acf5-a8d3a9918dd0 | -12.08737 | -49.48395 | 2025-06-01 04:36:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fab769e5-da18-3524-92ce-a3507a54d933 | -11.57496 | -47.45523 | 2025-06-01 04:36:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 1cbdea76-4230-31d7-bf58-21c0a20f1771 | -11.44857 | -55.01223 | 2025-06-01 04:36:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 33562f0b-72ba-36cb-bbd0-b26ef75685e8 | -14.68914 | -45.10078 | 2025-06-01 04:36:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e68f358c-a98d-334b-b9ef-a30447c6c4a0 | -14.03552 | -55.14221 | 2025-06-01 04:36:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 59c433bc-ee94-3a46-83c5-b17b5274a282 | -13.90684 | -54.66725 | 2025-06-01 04:36:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 01a48d2f-f02d-3e4b-8f8c-6c31e2b31218 | -17.96773 | -45.38309 | 2025-06-01 04:38:00 | NPP-375D | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| f6333e1d-c826-3fce-8682-32e8dcb34676 | -21.1619 | -47.13947 | 2025-06-01 04:38:00 | NPP-375D | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4cf3c8db-50c4-3e5a-90e3-d0c25a7a4e11 | -20.59826 | -51.61075 | 2025-06-01 04:38:00 | NPP-375D | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| bc17ad19-9c79-396b-8c32-95591e47c3f1 | -20.99471 | -51.79222 | 2025-06-01 04:38:00 | NPP-375D | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 43093779-993e-3b8e-8499-91d9c4074f7e | -19.54983 | -44.1032 | 2025-06-01 04:38:00 | NPP-375D | MATOZINHOS | MINAS GERAIS | Brasil | 3141108 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f145ae89-8f33-376d-8907-05927be8ce83 | -17.02784 | -52.54012 | 2025-06-01 04:38:00 | NPP-375D | DOVERLÂNDIA | GOIÁS | Brasil | 5207253 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d7162fc3-0a34-3709-b636-695d4c8b1886 | -17.04606 | -49.06303 | 2025-06-01 04:38:00 | NPP-375D | BELA VISTA DE GOIÁS | GOIÁS | Brasil | 5203302 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c22eda3a-4a81-3e5a-a573-da823261b8a3 | -18.8989 | -48.39984 | 2025-06-01 04:38:00 | NPP-375D | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 621be4f5-6027-332a-91e0-feeed56241cc | -22.65298 | -50.67106 | 2025-06-01 04:38:00 | NPP-375D | MARACAÍ | SÃO PAULO | Brasil | 3528809 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| c7be84c4-cadd-3334-a311-e9cc90d42794 | -22.87874 | -53.14619 | 2025-06-01 04:38:00 | NPP-375D | LOANDA | PARANÁ | Brasil | 4113502 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| abfcfcda-121e-3ee4-9473-840fede4c8e1 | -17.96368 | -45.38248 | 2025-06-01 04:38:00 | NPP-375D | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b5971ab0-32d8-3a4a-96f7-48c38b5a7fad | -20.15088 | -49.61377 | 2025-06-01 04:38:00 | NPP-375D | PAULO DE FARIA | SÃO PAULO | Brasil | 3536604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 4dd08e1d-0f30-3fbe-8a5e-837744d52a99 | -21.15987 | -47.14156 | 2025-06-01 04:38:00 | NPP-375D | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 29d23ff6-3b5c-3a1f-abf6-3018b32b30c4 | -20.01985 | -44.59542 | 2025-06-01 04:38:00 | NPP-375D | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| ea1c1b67-55c1-39c9-95a9-d4e13e19e9b5 | -22.54154 | -48.81168 | 2025-06-01 04:38:00 | NPP-375D | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ae0dbc6f-3bff-390c-9146-3627c453140c | -22.5393 | -48.81281 | 2025-06-01 04:38:00 | NPP-375D | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2f836550-b3ba-374b-810f-8eb5fbaf6677 | -20.76253 | -46.77073 | 2025-06-01 04:38:00 | NPP-375D | ITAÚ DE MINAS | MINAS GERAIS | Brasil | 3133758 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 5abb2949-99b8-354d-92a1-55261ede85d6 | -23.33961 | -46.77017 | 2025-06-01 04:38:00 | NPP-375D | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| a6402972-8f90-3908-a87b-520f06fe0851 | -23.34055 | -46.77085 | 2025-06-01 04:38:00 | NPP-375D | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| f82644e0-d0a2-39c0-8da6-5ca40a3d2206 | -17.7555 | -52.43859 | 2025-06-01 04:38:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 201f3009-b032-3c50-a224-da1d851ad079 | -18.95239 | -50.02832 | 2025-06-01 04:38:00 | NPP-375D | SANTA VITÓRIA | MINAS GERAIS | Brasil | 3159803 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 29f96d4e-2595-38b3-a1f2-fee164612053 | -20.43184 | -50.13383 | 2025-06-01 04:38:00 | NPP-375D | VALENTIM GENTIL | SÃO PAULO | Brasil | 3556107 | 35 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 04fe1c0e-7bf8-3c71-8b2a-aa5d5e8d0b88 | -20.15427 | -49.61433 | 2025-06-01 04:38:00 | NPP-375D | PAULO DE FARIA | SÃO PAULO | Brasil | 3536604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 7b8b0a01-a670-3f4f-b3bc-a6b0544cd897 | -18.20557 | -48.15283 | 2025-06-01 04:38:00 | NPP-375D | GOIANDIRA | GOIÁS | Brasil | 5208509 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5bc1ed2a-0ddc-3e26-95eb-7b4c5c1a08ed | -27.45589 | -48.45129 | 2025-06-01 04:40:00 | NPP-375D | FLORIANÓPOLIS | SANTA CATARINA | Brasil | 4205407 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 47adf77c-0ee9-3950-9403-741269664baa | -27.03733 | -48.79963 | 2025-06-01 04:40:00 | NPP-375D | ITAJAÍ | SANTA CATARINA | Brasil | 4208203 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 2cce4b1a-934e-3e24-8d30-1c5c151f2cfe | -30.15181 | -52.02424 | 2025-06-01 04:40:00 | NPP-375D | MINAS DO LEÃO | RIO GRANDE DO SUL | Brasil | 4312252 | 43 | 33 | nan | nan | nan | Pampa | 0.8 |
| efe64f51-f800-34e5-ada5-9e2575b72c9e | -6.45239 | -54.84248 | 2025-06-01 04:55:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 4153d448-f00c-3659-aa36-6f013435d33a | -6.6366 | -47.34616 | 2025-06-01 04:55:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4a2cc4af-852f-314a-9074-893625faef7d | -8.13141 | -49.58752 | 2025-06-01 04:55:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| e0f68d7c-a6f4-313a-92bd-7cd8e1193868 | -8.67466 | -46.64047 | 2025-06-01 04:55:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 8085a4b4-ebcd-36e4-a39e-c4c28e130bdf | -6.63679 | -47.34392 | 2025-06-01 04:55:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ea127313-7798-3b71-aaf3-7ead6239c699 | -7.58745 | -45.86615 | 2025-06-01 04:55:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 44f631d4-f720-383f-b39b-2960cb785a24 | -2.37538 | -51.87681 | 2025-06-01 04:55:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a32e26c3-836d-3e74-88f2-1fd424944284 | -8.66895 | -46.64549 | 2025-06-01 04:55:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7ebb98f8-0bfe-306b-9477-2bc3ed60999e | -9.04755 | -47.02281 | 2025-06-01 04:55:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ad883e3d-8324-3109-ae99-400058c06297 | -2.58532 | -51.92385 | 2025-06-01 04:55:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b016ca55-98a0-35f2-a5b3-2f2afa204436 | -3.76091 | -49.92545 | 2025-06-01 04:55:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 38f71b97-0d39-3f5b-8e49-a0846bcf32cd | -8.67864 | -46.63971 | 2025-06-01 04:55:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 43629375-4f17-3d4f-99ac-dc766281984f | -7.00871 | -44.61908 | 2025-06-01 04:55:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 48a22e50-f541-3018-aa72-83462ca5f9b2 | -7.2282 | -43.12754 | 2025-06-01 04:55:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| b4fa9733-81af-3f95-82ba-b0c3cc9f31b3 | -7.08273 | -46.5582 | 2025-06-01 04:55:00 | NOAA-20 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1f127e32-7414-3578-907a-b1b6c2198446 | -4.48573 | -48.86345 | 2025-06-01 04:55:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4bd6733b-0100-3219-8a77-e3ca8b5be9e3 | -9.13321 | -47.57861 | 2025-06-01 04:55:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e9001791-0122-3965-ad93-2049e7978ed8 | -8.6739 | -46.64624 | 2025-06-01 04:55:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5eb6312d-1130-3a23-988c-131eabc2da2b | -8.66972 | -46.63974 | 2025-06-01 04:55:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| bf8245e9-3612-3272-8f65-03c1f82968f0 | -4.48123 | -48.86628 | 2025-06-01 04:55:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bdfb84b4-5015-3ec5-b684-b9a7c05830fd | -7.58275 | -45.86238 | 2025-06-01 04:55:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 253632c8-d5ea-3dc3-a84c-df71d8d453a6 | -7.30483 | -47.02758 | 2025-06-01 04:55:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 11f9479a-7421-3374-b9c7-bcdc55f22d0b | -7.22759 | -43.13224 | 2025-06-01 04:55:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 2987eba5-2a70-3166-b81d-66e4666bf5e7 | -7.00819 | -44.62276 | 2025-06-01 04:55:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b70b1316-1541-3036-ad3e-5d6ece9805fc | -9.39743 | -48.41824 | 2025-06-01 04:55:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bf322807-c0a6-370d-8708-f42ab5ce1ab0 | -7.22208 | -43.12666 | 2025-06-01 04:55:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 18cb470c-9bb3-31b5-a094-60501f5f7b30 | -9.34282 | -48.94545 | 2025-06-01 04:55:00 | NOAA-20 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 274215fb-4976-3d04-aa69-64e963fd26f4 | -6.17894 | -48.06913 | 2025-06-01 04:55:00 | NOAA-20 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 27fe023a-6829-3632-9988-9cf136e29a1a | -9.39778 | -48.41959 | 2025-06-01 04:55:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cd904c34-cdfe-3f3a-bd6f-46336f451825 | -9.40185 | -48.41888 | 2025-06-01 04:55:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 928d0997-ba76-3f49-8332-1317c2b85393 | -7.22911 | -43.12084 | 2025-06-01 04:55:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 903fc8b2-cd80-3af0-be05-c585cc28dddd | -4.36917 | -55.7733 | 2025-06-01 04:55:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 10413a82-74ad-3a71-b7e3-a162603ce4b0 | -7.2217 | -43.12934 | 2025-06-01 04:55:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 58c24890-62bc-368d-a4b7-b1d81ea7ee62 | -7.51902 | -46.86232 | 2025-06-01 04:55:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 05c16665-9849-3ec6-aa0e-2b643013d3ba | -6.63671 | -55.00816 | 2025-06-01 04:55:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 26bc7fb0-0172-38dd-a5d1-d20b608fc9f3 | -4.27534 | -48.09429 | 2025-06-01 04:55:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| df8ae2ed-deec-394f-84f8-3fdd222eae29 | -9.12853 | -47.57803 | 2025-06-01 04:55:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| beac548c-7f21-3a35-9588-104c9aab3d9f | -7.01308 | -44.62331 | 2025-06-01 04:55:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7d7af19e-8e2d-36d3-9578-3e3a35303b48 | -5.85078 | -47.89 | 2025-06-01 04:55:00 | NOAA-20 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| eda847bc-5787-3e1b-8d6b-efd16fbee55d | -8.1274 | -49.58695 | 2025-06-01 04:55:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |


[Clique aqui para ver as próximas entradas](README11.md)
