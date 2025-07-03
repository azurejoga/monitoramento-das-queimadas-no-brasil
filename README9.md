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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 323b0a68-e6b3-326b-89de-6662a6e16af6 | -5.40346 | -43.24825 | 2025-07-03 04:08:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 283b634b-7929-326c-997c-3d2ce05f8d4c | -7.22786 | -43.06012 | 2025-07-03 04:08:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 56a42fb3-21fd-31a3-a2dd-9ba182ee8a16 | -6.2501 | -44.83336 | 2025-07-03 04:08:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9789b811-a5f2-379b-81f5-730316639be5 | -6.93047 | -43.88875 | 2025-07-03 04:08:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 15ac21a7-4c9e-32e4-b816-5fce1b1deef2 | -6.65136 | -43.37047 | 2025-07-03 04:08:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 7d65da5e-21cc-3145-a65b-aed1b9f37b01 | -6.33713 | -43.38058 | 2025-07-03 04:08:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dcc4cbae-19da-36fd-9bfe-7605ad0a8f44 | -6.01944 | -49.22996 | 2025-07-03 04:08:00 | NOAA-21 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 80ae21ee-6396-3691-8b10-129d85b31ba4 | -7.23286 | -43.07184 | 2025-07-03 04:08:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 14.7 |
| 1c983b80-e84b-3815-a1de-c5426fd446b0 | -6.69528 | -43.15855 | 2025-07-03 04:08:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 61bbc462-4514-3486-a5e8-2d4d24d6803e | -5.9245 | -43.48172 | 2025-07-03 04:08:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 5aae7a6a-2c7d-3318-8404-f643f7798434 | -6.2892 | -43.68358 | 2025-07-03 04:08:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 33.6 |
| da0e7bac-29ff-37ff-a700-372908ecbbca | -6.29314 | -43.67994 | 2025-07-03 04:08:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 33.0 |
| c9fdfee7-d994-3323-879f-bdc67cb9acc8 | -5.99111 | -43.74517 | 2025-07-03 04:08:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| cea05e7f-ea17-3d96-b522-b347776f2040 | -5.73572 | -43.49769 | 2025-07-03 04:08:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 86b54d82-8c93-3ae2-a2d9-785248579770 | -6.18226 | -42.61367 | 2025-07-03 04:08:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 01584608-e0ec-3cd9-b78b-8675073a8084 | -4.53852 | -48.0269 | 2025-07-03 04:08:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| b868cbc3-e420-3a1c-8497-3ebc9ca3e17c | -6.00266 | -43.73927 | 2025-07-03 04:08:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e5913066-f55f-320d-8a7d-9f8adf07e19b | -7.95478 | -37.18381 | 2025-07-03 04:08:00 | NOAA-21 | MONTEIRO | PARAÍBA | Brasil | 2509701 | 25 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 6b68f063-90bb-308e-860d-efd1ba057c81 | -9.83792 | -44.67947 | 2025-07-03 04:08:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 05c1f36c-d2a2-30db-b839-9b8425f696d8 | -6.85848 | -43.30673 | 2025-07-03 04:08:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 0f4eeadc-6b4a-3faf-92d5-a085430b52c8 | -11.14335 | -43.32697 | 2025-07-03 04:08:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 29.2 |
| 25bbff11-7afe-3fb1-95d9-4f739318411d | -6.70184 | -43.15197 | 2025-07-03 04:08:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e9fa0364-b8da-38a2-83b0-0eb1dc58e84a | -6.28637 | -43.67928 | 2025-07-03 04:08:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 33.6 |
| 7b93a2e5-9aec-370a-b25c-71ba492d128d | -10.99427 | -45.19584 | 2025-07-03 04:08:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 6a079f03-99a6-32c7-af5c-eb90be43a156 | -6.20478 | -51.4507 | 2025-07-03 04:08:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 08bb3276-6dfb-3505-9e29-acf759ded03e | -5.72548 | -49.107 | 2025-07-03 04:08:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| d6929f4b-5078-3978-b20d-9ba32adeded5 | -6.27607 | -43.67771 | 2025-07-03 04:08:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 07f2d2c6-33e6-3fe2-8416-795505d84dbe | -7.19428 | -43.09862 | 2025-07-03 04:08:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| f7455081-a479-3bf1-9758-c7804fdb7ce2 | -6.00326 | -43.73551 | 2025-07-03 04:08:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a90dba22-a036-3c91-92a6-57fb6ed600a9 | -7.85877 | -47.88267 | 2025-07-03 04:08:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ac6f4387-510d-3e7a-b06a-a0841cf1f28a | -5.40405 | -43.24459 | 2025-07-03 04:08:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f7167c3b-24d5-3820-8f05-80b3394e444e | -10.08869 | -47.99273 | 2025-07-03 04:08:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c26481a3-b982-3000-a2e6-edb40f4fa2e9 | -6.72596 | -43.15208 | 2025-07-03 04:08:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0a73a923-09c5-3b71-8272-a72c7f13d759 | -6.8324 | -42.02906 | 2025-07-03 04:08:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| f9df4237-a335-3b3f-affc-c626ebec67ff | -7.22409 | -35.90129 | 2025-07-03 04:08:00 | NOAA-21 | CAMPINA GRANDE | PARAÍBA | Brasil | 2504009 | 25 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 58d9f409-c344-3a71-9135-5596c1022ca1 | -7.19371 | -43.10218 | 2025-07-03 04:08:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 34ef2674-ca25-3d8c-8aff-432960b5eb44 | -5.99861 | -43.74249 | 2025-07-03 04:08:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 879d0f5c-01a1-3a35-904b-6f869215a472 | -7.10864 | -47.84957 | 2025-07-03 04:08:00 | NOAA-21 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2c57741b-1ff1-39ed-8d85-00b4598fc23b | -5.40064 | -43.24407 | 2025-07-03 04:08:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9a38e994-5e47-38b4-899c-71d5346d2bbe | -5.99922 | -43.73872 | 2025-07-03 04:08:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 45970fb3-4b43-38b3-bc7c-289b9e9744a0 | -7.21725 | -43.0621 | 2025-07-03 04:08:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 68e70dab-c716-361e-89af-02931ef5dceb | -8.81829 | -43.9265 | 2025-07-03 04:08:00 | NOAA-21 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5b4cae24-1416-351e-8b90-9dd01c6ccb28 | -6.175 | -48.05216 | 2025-07-03 04:08:00 | NOAA-21 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 17.0 |
| a80177bb-2108-3e04-83a5-34e801d9e702 | -5.60084 | -44.90119 | 2025-07-03 04:08:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5d644f0d-aeca-36c8-9574-6f3f42669b09 | -5.07865 | -42.51113 | 2025-07-03 04:08:00 | NOAA-21 | ALTOS | PIAUÍ | Brasil | 2200400 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| e4fc31c1-50f3-3cde-88d0-9de7d155edf0 | -7.22117 | -43.05906 | 2025-07-03 04:08:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 33.7 |
| 965c61c7-a160-356b-8659-824f6069192b | -7.22395 | -43.06314 | 2025-07-03 04:08:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 33.7 |
| 5c214ffd-2534-39e8-a43d-705bac2ee273 | -5.51485 | -45.265 | 2025-07-03 04:08:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1c3c8500-cf9e-374f-860e-880ed4444e8d | -6.19446 | -42.64447 | 2025-07-03 04:08:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| c0d249da-c97d-30e2-afff-3e9efa900608 | -6.72539 | -43.15567 | 2025-07-03 04:08:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0d95a0a1-718f-3965-a1d6-63f09a3812b9 | -9.24505 | -48.75071 | 2025-07-03 04:08:00 | NOAA-21 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cdf62130-05c2-3cfc-a4cf-ae988959542f | -6.16989 | -48.05552 | 2025-07-03 04:08:00 | NOAA-21 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 0efbf0ac-b5e8-3e87-b570-ef905bb60981 | -7.20212 | -43.09254 | 2025-07-03 04:08:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| d3af8898-1d10-33a7-90b1-86ec76c82fc9 | -8.86024 | -47.95195 | 2025-07-03 04:08:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ce53005d-99a0-3114-8742-e8365d2ce5b1 | -7.21782 | -43.05853 | 2025-07-03 04:08:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 3bbaeb69-8a6c-3996-9360-1c6c516103d3 | -5.87341 | -50.14785 | 2025-07-03 04:08:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 6ca2c9fd-910c-3803-b2aa-c53702567753 | -6.00145 | -43.74678 | 2025-07-03 04:08:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| eb2ea966-9136-3c6a-bdda-d35c739a1154 | -6.96112 | -42.87561 | 2025-07-03 04:08:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 8498e356-3177-3285-a06a-0be3a9762101 | -10.65049 | -44.48447 | 2025-07-03 04:08:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 312b723f-3dd5-3707-a821-7020b1823889 | -7.20024 | -43.16916 | 2025-07-03 04:08:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 897b46c0-daed-3a57-b71f-87cb63b37622 | -5.9974 | -43.75002 | 2025-07-03 04:08:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a549ffec-b1fd-392d-934a-be99632238bc | -7.22508 | -43.05604 | 2025-07-03 04:08:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 8.1 |
| aa09c157-9faa-3b4b-a540-5f5efad640fd | -6.33431 | -43.752 | 2025-07-03 04:08:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 11.9 |
| e9bac223-25a0-333d-83d1-1092d3b085f9 | -7.84037 | -46.87949 | 2025-07-03 04:08:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b4a2dd14-306a-3f57-beb3-8154dced36be | -6.02035 | -49.22475 | 2025-07-03 04:08:00 | NOAA-21 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 06b35418-2f50-3d99-bd7a-d1daa3b0c332 | -5.99982 | -43.73496 | 2025-07-03 04:08:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| f097ebb6-7547-3cf4-9526-651df6fd0b08 | -5.91708 | -43.48433 | 2025-07-03 04:08:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7db0f480-775c-39e4-9bf6-b0263c88f11d | -7.22173 | -43.05551 | 2025-07-03 04:08:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 8.1 |
| 6108e4e7-efab-301e-9659-bd4cc948b840 | -7.44642 | -44.46223 | 2025-07-03 04:08:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0066d6c6-1077-3c55-93f8-417ece1f596d | -5.99456 | -43.74572 | 2025-07-03 04:08:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 3d66a2b1-725d-313c-bede-83605dac966c | -7.2206 | -43.06261 | 2025-07-03 04:08:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 33.7 |
| ecb5cada-05d8-37a3-bb50-4d9819a59f08 | -6.69191 | -43.15802 | 2025-07-03 04:08:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 7.4 |
| 4b23758e-2d0c-3496-b5da-655ff8241e2f | -6.95723 | -42.87861 | 2025-07-03 04:08:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 33.9 |
| bf5f0c91-56e0-34ad-9919-f57fb78ea7da | -5.90881 | -43.44876 | 2025-07-03 04:08:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c2b4cce5-b10e-3002-bf33-38278815ca8d | -8.32099 | -42.2135 | 2025-07-03 04:08:00 | NOAA-21 | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 63b42a27-8e82-31fe-8b4c-0670b28dcaa6 | -6.94888 | -42.88816 | 2025-07-03 04:08:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 33.0 |
| f3dff3f7-55b7-3a23-ade8-3fcd5a5e1d40 | -5.65758 | -46.59539 | 2025-07-03 04:08:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 12afbd00-ae9a-3cd7-8710-4310e7cd80e9 | -7.61525 | -45.75236 | 2025-07-03 04:08:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 14.7 |
| a0026514-36cf-3b6d-b7e1-7d42561665a2 | -11.5139 | -43.24316 | 2025-07-03 04:08:00 | NOAA-21 | MORPARÁ | BAHIA | Brasil | 2921609 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 3fa7aba0-10de-32f9-8bf7-e7ea43188ef7 | -9.8442 | -44.68441 | 2025-07-03 04:08:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bdce3f79-7ccf-38c1-9a42-ac7b3bda1f6f | -10.69555 | -37.04929 | 2025-07-03 04:08:00 | NOAA-21 | ROSÁRIO DO CATETE | SERGIPE | Brasil | 2806107 | 28 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| ca86bdb4-41e1-3ec4-af55-732217c42aa1 | -6.00085 | -43.75055 | 2025-07-03 04:08:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| fb05edbe-b4db-3c20-8702-0b4a0700fd10 | -9.1778 | -48.77223 | 2025-07-03 04:08:00 | NOAA-21 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 2e348cbb-87ac-3a76-920f-271ed0806c09 | -6.96947 | -42.80093 | 2025-07-03 04:08:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| d9c29d67-c13e-30bd-ace6-967b0e48a15d | -8.43638 | -49.19994 | 2025-07-03 04:08:00 | NOAA-21 | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c006bd96-a466-39b8-8d25-a890846e8d32 | -9.60989 | -49.0214 | 2025-07-03 04:08:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 195e64b8-d5df-3fba-91c7-acdc64f45449 | -6.29375 | -43.67619 | 2025-07-03 04:08:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 73154c49-719d-33aa-9478-afd1fa9273d8 | -5.07014 | -43.73138 | 2025-07-03 04:08:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| efac114a-b102-3f72-8cca-0398950e1b22 | -6.3337 | -43.7558 | 2025-07-03 04:08:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a679c69c-8428-3734-9d7f-df3296034adc | -7.09313 | -49.17184 | 2025-07-03 04:08:00 | NOAA-21 | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2a412578-12c6-35bd-99d3-097b123f3020 | -6.97008 | -42.8806 | 2025-07-03 04:08:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 454381d1-60d2-3428-bbb9-c51a38f351e8 | -11.8821 | -40.95604 | 2025-07-03 04:08:00 | NOAA-21 | TAPIRAMUTÁ | BAHIA | Brasil | 2931301 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| f78ef80f-1060-33bc-86f9-5738bcbc19ab | -4.54005 | -48.01774 | 2025-07-03 04:08:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ec0c1868-a156-3b6b-9d99-f2290b8e6ee0 | -6.69135 | -43.1616 | 2025-07-03 04:08:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 7.4 |
| 44a8cccd-9d52-3487-93cf-0e38f81bc317 | -6.95611 | -42.88567 | 2025-07-03 04:08:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 43.7 |
| 2b336c5e-0617-3b07-b60a-36d47ef220a9 | -6.95333 | -42.88161 | 2025-07-03 04:08:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 16.2 |
| c119fb9d-1615-353b-bed0-c8ab8997f463 | -9.17339 | -48.77149 | 2025-07-03 04:08:00 | NOAA-21 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Amazônia | 8.5 |
| b45b327e-ab83-3759-b1a3-42a211a9260a | -6.92703 | -43.88821 | 2025-07-03 04:08:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 754afe3b-9089-3c45-95a2-e37d22853751 | -6.28577 | -43.68303 | 2025-07-03 04:08:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 33.6 |
| c26a3431-dc88-3190-947e-70a8684feb56 | -5.39724 | -43.24354 | 2025-07-03 04:08:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 11.8 |


[Clique aqui para ver as próximas entradas](README10.md)
