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

## Dados Diários - Página 60

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d12b1497-f26c-35e5-87da-c4ccaf3e52a6 | -23.39904 | -45.39301 | 2025-10-06 04:29:00 | NOAA-21 | NATIVIDADE DA SERRA | SÃO PAULO | Brasil | 3532306 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 79ca82e0-d8f1-34b7-96d7-58a272b3c0cf | -20.69916 | -51.15533 | 2025-10-06 04:29:00 | NOAA-21 | PEREIRA BARRETO | SÃO PAULO | Brasil | 3537404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| fbccad55-763f-3fee-9c81-6a76c30d5eb8 | -17.29071 | -49.27394 | 2025-10-06 04:29:00 | NOAA-21 | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4ac8e13a-0170-3e35-b2f1-ccc2c1027eb1 | -18.86554 | -48.21941 | 2025-10-06 04:29:00 | NOAA-21 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ebcf719d-f441-3934-96f2-d00389e3fc97 | -18.2472 | -53.34755 | 2025-10-06 04:29:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 66a0abc1-b103-3f02-b8fe-be13f3a1b5ca | -20.39633 | -46.89278 | 2025-10-06 04:29:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a2f6d749-6d82-3073-8e5f-a004510fabc1 | -21.30651 | -43.83995 | 2025-10-06 04:29:00 | NOAA-21 | ANTÔNIO CARLOS | MINAS GERAIS | Brasil | 3102902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| a9e0a0ea-55bb-3391-b633-2874daf3cba9 | -16.96344 | -52.6775 | 2025-10-06 04:29:00 | NOAA-21 | DOVERLÂNDIA | GOIÁS | Brasil | 5207253 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 85f1b0f7-2363-3723-8e18-f8b9821a8829 | -16.34114 | -51.45572 | 2025-10-06 04:29:00 | NOAA-21 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7cd2b834-d6a5-3be3-b6bc-10656cb09f0a | -18.01031 | -57.59024 | 2025-10-06 04:29:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.3 |
| a5cb5507-02fd-3eaf-9195-163ee96869aa | -22.36424 | -44.2088 | 2025-10-06 04:29:00 | NOAA-21 | QUATIS | RIO DE JANEIRO | Brasil | 3304128 | 33 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| 9e941ea5-5d91-3e8f-b608-cb789c71a25b | -18.15619 | -53.31151 | 2025-10-06 04:29:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c017e978-0cc4-3237-bedb-2578efff7d10 | -18.45325 | -49.43305 | 2025-10-06 04:29:00 | NOAA-21 | CACHOEIRA DOURADA | GOIÁS | Brasil | 5204250 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 221e1b63-916a-35fd-8b7c-ac1bb1829f2d | -19.945 | -44.63662 | 2025-10-06 04:29:00 | NOAA-21 | IGARATINGA | MINAS GERAIS | Brasil | 3130200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 340c1e04-ac40-3eff-b941-e4c39ec13e18 | -18.1956 | -53.37357 | 2025-10-06 04:29:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 44e455fa-3f87-380f-8cbf-19b1afe36447 | -17.84056 | -57.63506 | 2025-10-06 04:29:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.7 |
| de963128-b554-3f0c-b693-a7047ba4bf93 | -17.97858 | -51.16292 | 2025-10-06 04:29:00 | NOAA-21 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 506593fb-9aa3-3981-b608-ab2a96a6f45c | -22.95231 | -46.13284 | 2025-10-06 04:29:00 | NOAA-21 | JOANÓPOLIS | SÃO PAULO | Brasil | 3525508 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 32483eb4-724c-3c54-a21e-c91bdeb666e9 | -18.1311 | -53.38702 | 2025-10-06 04:29:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 1a4e5731-6077-3f72-8eaf-169659542b31 | -21.70716 | -50.07688 | 2025-10-06 04:29:00 | NOAA-21 | GETULINA | SÃO PAULO | Brasil | 3517000 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| e1656452-167e-3b88-a001-5288f5e77c83 | -22.52479 | -43.57193 | 2025-10-06 04:29:00 | NOAA-21 | MIGUEL PEREIRA | RIO DE JANEIRO | Brasil | 3302908 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| df6b44d3-996e-3fbb-922c-4bc7ca31b714 | -17.86973 | -57.59299 | 2025-10-06 04:29:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.7 |
| e5e9a336-33f4-3011-929a-b09c11ef621e | -19.94052 | -44.64019 | 2025-10-06 04:29:00 | NOAA-21 | IGARATINGA | MINAS GERAIS | Brasil | 3130200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| ac3fb731-a7a6-3e50-8c31-cd983cd53c20 | -21.73688 | -50.08222 | 2025-10-06 04:29:00 | NOAA-21 | GETULINA | SÃO PAULO | Brasil | 3517000 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 2658ce8f-03bf-3e9d-9b0b-8b4fe7a11035 | -16.34043 | -51.45984 | 2025-10-06 04:29:00 | NOAA-21 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0cde2d44-3d23-3c89-9965-a4a69709c081 | -22.28927 | -49.92164 | 2025-10-06 04:29:00 | NOAA-21 | MARÍLIA | SÃO PAULO | Brasil | 3529005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 7d4883d5-2ed5-32dd-8edb-6e1f3b99eb1c | -21.38618 | -45.05206 | 2025-10-06 04:29:00 | NOAA-21 | INGAÍ | MINAS GERAIS | Brasil | 3130804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| a761d1f2-c970-30e8-9bca-bb05153cc745 | -17.98736 | -57.60533 | 2025-10-06 04:29:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 088228cf-dd6d-370e-9c6e-44c8682794e0 | -21.86983 | -48.28882 | 2025-10-06 04:29:00 | NOAA-21 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c2eaf9fc-c856-3c88-a70f-926fa62641e8 | -17.98331 | -51.1557 | 2025-10-06 04:29:00 | NOAA-21 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a804c17d-1f44-39df-b564-2bec9399e72b | -20.09445 | -44.19287 | 2025-10-06 04:29:00 | NOAA-21 | MÁRIO CAMPOS | MINAS GERAIS | Brasil | 3140159 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 9c093065-ee61-351f-8c65-b0b5e216b687 | -18.87765 | -48.60876 | 2025-10-06 04:29:00 | NOAA-21 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 7a6a4eee-065c-364a-ae0c-ea121a04fbb8 | -18.23406 | -50.9369 | 2025-10-06 04:29:00 | NOAA-21 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6e32aafc-e0d9-306a-bcd1-42f2c26b4293 | -22.29488 | -46.73027 | 2025-10-06 04:29:00 | NOAA-21 | ESPÍRITO SANTO DO PINHAL | SÃO PAULO | Brasil | 3515186 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| ede1d0a4-2609-3e61-8819-0529361c98da | -21.70189 | -52.00142 | 2025-10-06 04:29:00 | NOAA-21 | PRESIDENTE EPITÁCIO | SÃO PAULO | Brasil | 3541307 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| b9e6e53d-8ef1-308c-bdad-a821416aacdd | -17.97388 | -57.54071 | 2025-10-06 04:29:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 13.9 |
| e3af2e26-2289-3822-a1a9-8a8c389e6243 | -21.39556 | -45.03628 | 2025-10-06 04:29:00 | NOAA-21 | INGAÍ | MINAS GERAIS | Brasil | 3130804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 45af4f66-305a-3757-813a-4b9f75c2dc1c | -18.19359 | -53.36297 | 2025-10-06 04:29:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| eaffca27-b18c-30ab-968b-f0d8567fc299 | -16.95724 | -52.69067 | 2025-10-06 04:29:00 | NOAA-21 | DOVERLÂNDIA | GOIÁS | Brasil | 5207253 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| b10769a3-627a-3f1c-a1f7-ded051c83609 | -18.11422 | -53.41572 | 2025-10-06 04:29:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 8.6 |
| c012f21e-2121-3223-9ba2-0009296a389e | -20.66477 | -42.2828 | 2025-10-06 04:29:00 | NOAA-21 | FERVEDOURO | MINAS GERAIS | Brasil | 3125952 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| f5256379-d9bf-3fa3-81d2-2a698dce1b67 | -18.53074 | -47.50734 | 2025-10-06 04:29:00 | NOAA-21 | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 76d774b6-c462-3576-9b22-82ae3e9be020 | -22.37656 | -50.01674 | 2025-10-06 04:29:00 | NOAA-21 | MARÍLIA | SÃO PAULO | Brasil | 3529005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 4b4c09b2-c331-3650-8403-e12c1d768ef3 | -19.02037 | -45.02784 | 2025-10-06 04:29:00 | NOAA-21 | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| ed7d0d61-1893-3e62-af63-954048f6e2fc | -19.71311 | -44.00107 | 2025-10-06 04:29:00 | NOAA-21 | SÃO JOSÉ DA LAPA | MINAS GERAIS | Brasil | 3162955 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 611c84ff-c05a-3f1d-a589-2b2888dcac3f | -16.45168 | -52.16604 | 2025-10-06 04:29:00 | NOAA-21 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ec2ceea0-a825-3beb-b324-faa2989156be | -18.39932 | -45.22501 | 2025-10-06 04:29:00 | NOAA-21 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| fb15564d-1d62-3b4d-94cf-65baccf27fec | -17.60734 | -44.44999 | 2025-10-06 04:29:00 | NOAA-21 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 4.9 |
| ec20a9ae-30e1-3e64-8648-8d80e810201c | -18.12271 | -53.41216 | 2025-10-06 04:29:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 7.2 |
| b1092440-37d3-3039-ba90-e14b396b5ca6 | -19.70721 | -49.29073 | 2025-10-06 04:29:00 | NOAA-21 | ITAPAGIPE | MINAS GERAIS | Brasil | 3133402 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a22b3f0d-82aa-3047-9242-60c8df0ff188 | -18.2722 | -53.31641 | 2025-10-06 04:29:00 | NOAA-21 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 6.3 |
| abfb91e6-7994-303a-b2f1-62aa1e200320 | -16.95974 | -52.67676 | 2025-10-06 04:29:00 | NOAA-21 | DOVERLÂNDIA | GOIÁS | Brasil | 5207253 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4519dedc-2728-3a36-8319-3ff26bd7897f | -18.50292 | -48.34766 | 2025-10-06 04:29:00 | NOAA-21 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1288e6af-9fc5-3690-aab2-3b9cf48e84c8 | -18.19471 | -53.37848 | 2025-10-06 04:29:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 9bd2ea24-c9c4-3754-9cff-6e37c32ef08c | -23.19219 | -47.24165 | 2025-10-06 04:29:00 | NOAA-21 | SALTO | SÃO PAULO | Brasil | 3545209 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 047c64b6-0fb5-3f86-b6b1-ab6f317a378c | -22.29158 | -49.90681 | 2025-10-06 04:29:00 | NOAA-21 | MARÍLIA | SÃO PAULO | Brasil | 3529005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 9dd6053c-cb4b-3cd2-b50f-2d6de7a98618 | -18.51583 | -43.92522 | 2025-10-06 04:29:00 | NOAA-21 | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| bf1f1ba8-c538-3127-8c5b-b31252f272ba | -17.93441 | -57.60839 | 2025-10-06 04:29:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| eecae9f9-83d1-3bc4-a513-b55a003a0682 | -21.73416 | -50.07793 | 2025-10-06 04:29:00 | NOAA-21 | GETULINA | SÃO PAULO | Brasil | 3517000 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 8a8a12d2-fbde-3463-9713-69daf92a4223 | -21.56559 | -48.33125 | 2025-10-06 04:29:00 | NOAA-21 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 196b5e51-0ae0-3876-b65c-9150b2132351 | -22.38531 | -50.02596 | 2025-10-06 04:29:00 | NOAA-21 | MARÍLIA | SÃO PAULO | Brasil | 3529005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 59dec52f-f963-385f-8d02-f4af5754bf1d | -17.96792 | -57.54475 | 2025-10-06 04:29:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 175790ce-4cf4-38ab-a4a9-3aed1b928137 | -18.82313 | -44.47497 | 2025-10-06 04:29:00 | NOAA-21 | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ebcf4cbf-bd75-3961-9461-62a85bd011a9 | -21.32248 | -48.66571 | 2025-10-06 04:29:00 | NOAA-21 | FERNANDO PRESTES | SÃO PAULO | Brasil | 3515608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| e887f109-9ced-391b-82b7-1e482156a70b | -22.29877 | -49.90427 | 2025-10-06 04:29:00 | NOAA-21 | MARÍLIA | SÃO PAULO | Brasil | 3529005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| fb87e8e9-8b51-3550-b6d0-d7f5bd5f00bc | -17.98571 | -57.53299 | 2025-10-06 04:29:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 23.5 |
| cb66046e-596d-3dd8-8479-3d1c7e7d8882 | -21.70094 | -50.09476 | 2025-10-06 04:29:00 | NOAA-21 | GETULINA | SÃO PAULO | Brasil | 3517000 | 35 | 33 | nan | nan | nan | Mata Atlântica | 15.6 |
| ffa5da5e-e3d9-3db5-a49c-143ecdb48cd9 | -17.87617 | -57.63844 | 2025-10-06 04:29:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| b17c21b3-ebab-38c1-bf55-5daf71e20136 | -17.99327 | -57.55208 | 2025-10-06 04:29:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.9 |
| 3435d611-6676-3266-aa40-7f2c20d470c6 | -18.25142 | -53.36786 | 2025-10-06 04:29:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 26cba2b9-83ba-3e01-9e99-e8ac7d59bf9c | -17.25283 | -46.91066 | 2025-10-06 04:29:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 91898fbf-f837-38a2-9dcd-b1165a71dc03 | -21.44768 | -44.03046 | 2025-10-06 04:29:00 | NOAA-21 | IBERTIOGA | MINAS GERAIS | Brasil | 3129400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| fa05fdeb-fae0-3684-aa25-e3b0ec7d07ad | -20.36354 | -46.47511 | 2025-10-06 04:29:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f4f73d92-1070-31ca-a0d4-467489f82f91 | -22.70621 | -47.4452 | 2025-10-06 04:29:00 | NOAA-21 | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| dcf2221b-510c-30e7-89b9-5e9788b01873 | -17.9789 | -57.54131 | 2025-10-06 04:29:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 20.0 |
| 1e1e9477-aa2a-3d8b-9cf5-156788ea022a | -17.87667 | -57.5841 | 2025-10-06 04:29:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 0afab5c3-72b5-3b62-a393-c65b9d72bef3 | -17.87043 | -57.58946 | 2025-10-06 04:29:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.7 |
| fde57b4b-11b1-30df-a66b-2d85c9eb28f8 | -20.52343 | -54.63113 | 2025-10-06 04:29:00 | NOAA-21 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0e29bb57-826a-3bd5-a836-1e6673869f12 | -17.97983 | -57.53667 | 2025-10-06 04:29:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 20.0 |
| 7d89acfe-f154-392b-b25b-1a8099452a25 | -17.98591 | -51.14008 | 2025-10-06 04:29:00 | NOAA-21 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f344c29f-8792-366b-9dd0-5839bb6b4664 | -16.37016 | -51.49878 | 2025-10-06 04:29:00 | NOAA-21 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2a3073b6-76bd-390c-8765-137732f716e4 | -18.14222 | -53.40818 | 2025-10-06 04:29:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 3e92028c-f7e1-342c-8a95-b591d778285d | -19.65673 | -46.44664 | 2025-10-06 04:29:00 | NOAA-21 | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 37fe6bb2-4b44-3d70-87e1-b25745323a3d | -18.27134 | -53.32134 | 2025-10-06 04:29:00 | NOAA-21 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 9aaca4c8-8f6b-349a-9330-f3e39b6f35ed | -21.39656 | -45.0893 | 2025-10-06 04:29:00 | NOAA-21 | LAVRAS | MINAS GERAIS | Brasil | 3138203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 18fceb3c-d87a-3352-9f37-1713917a8c2e | -17.3483 | -46.83101 | 2025-10-06 04:29:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 153af964-caeb-3b13-b66f-ff825f317999 | -22.38647 | -50.01853 | 2025-10-06 04:29:00 | NOAA-21 | MARÍLIA | SÃO PAULO | Brasil | 3529005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 6d24b4c4-fb61-35c9-ad4c-8ce95f8a491c | -17.96848 | -57.56752 | 2025-10-06 04:29:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 4217f1ce-7066-3504-b94d-d4aaef80891b | -17.98385 | -57.54226 | 2025-10-06 04:29:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 20.0 |
| 30ee11ab-98cb-38f9-bf78-6f429175548b | -17.95148 | -48.55103 | 2025-10-06 04:29:00 | NOAA-21 | CALDAS NOVAS | GOIÁS | Brasil | 5204508 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ae08e3e7-95af-3876-bc89-d50d6ea891c2 | -17.93932 | -57.60965 | 2025-10-06 04:29:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 43a4a58a-1b03-35b5-a5fe-bb870b2551fe | -18.59009 | -49.98388 | 2025-10-06 04:29:00 | NOAA-21 | INACIOLÂNDIA | GOIÁS | Brasil | 5209937 | 52 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| d8e079f4-a77f-3deb-9cd6-9c9859d4deb8 | -18.25906 | -53.32462 | 2025-10-06 04:29:00 | NOAA-21 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1644f9cd-2099-3136-a857-5f31339a3aec | -18.26287 | -53.32515 | 2025-10-06 04:29:00 | NOAA-21 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 3.9 |
| bc75d1c0-d41b-3691-8500-5b30af946715 | -17.26591 | -46.91659 | 2025-10-06 04:29:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| bae8a1c1-6a19-3c09-88a0-1510285bb5d3 | -18.00213 | -57.60547 | 2025-10-06 04:29:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 4b64ab64-ec59-3f91-aade-d0229260bdeb | -17.99962 | -57.54046 | 2025-10-06 04:29:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.8 |
| 104fa9f9-ca89-31da-92d7-0286ffab3474 | -16.36313 | -51.4973 | 2025-10-06 04:29:00 | NOAA-21 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 17d575a0-7c6b-3845-b84d-7aea479edec1 | -17.87532 | -57.59084 | 2025-10-06 04:29:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.7 |
| b96e80e6-3a50-367f-b6cb-a017da20084b | -21.10836 | -44.20237 | 2025-10-06 04:29:00 | NOAA-21 | TIRADENTES | MINAS GERAIS | Brasil | 3168804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |


[Clique aqui para ver as próximas entradas](README61.md)
