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
| fbbc03ee-fae9-3099-a05e-e72004b8a578 | -11.08504 | -41.6604 | 2025-01-05 04:12:00 | NOAA-20 | SÃO GABRIEL | BAHIA | Brasil | 2929255 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 36b0124d-f13a-3fda-be96-bd5c830f419f | -10.03718 | -42.47525 | 2025-01-05 04:12:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 4.1 |
| c23b7274-071b-3a2a-99e7-7588fa493cf7 | -11.08608 | -41.65963 | 2025-01-05 04:12:00 | NOAA-20 | SÃO GABRIEL | BAHIA | Brasil | 2929255 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 227c323e-9479-314a-8526-ef25a59f07f3 | -10.64617 | -44.49263 | 2025-01-05 04:12:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| dc4e452b-f63f-3421-a225-7367fe035aec | -10.65979 | -44.4912 | 2025-01-05 04:12:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f8ace3e7-aa36-3d04-8b57-cf414a6521f3 | -10.67249 | -44.49686 | 2025-01-05 04:12:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a9a0e7c0-4bb4-39e6-ba29-96331b24b58e | -10.3224 | -42.42101 | 2025-01-05 04:12:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 2.5 |
| ecfa1796-c2f4-307b-8509-62531792ff0e | -6.07704 | -37.31289 | 2025-01-05 04:12:00 | NOAA-20 | BELÉM DO BREJO DO CRUZ | PARAÍBA | Brasil | 2502003 | 25 | 33 | nan | nan | nan | Caatinga | 7.4 |
| 08fbf9b8-d87d-32b8-8a9f-9ff869f7b8b3 | -9.74232 | -37.53595 | 2025-01-05 04:12:00 | NOAA-20 | PÃO DE AÇÚCAR | ALAGOAS | Brasil | 2706406 | 27 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 1551d583-8d35-349f-a08b-025f90ca3be2 | -6.14498 | -42.45334 | 2025-01-05 04:12:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 4a07fbaa-ad44-325d-85b8-5f8060f17a9e | -9.55106 | -40.30997 | 2025-01-05 04:12:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 1c8ab254-7641-3784-9aad-96d7847e0a63 | -10.6631 | -44.49174 | 2025-01-05 04:12:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 60a1ed74-edec-3db2-9f71-d1321917e149 | -10.64873 | -44.4966 | 2025-01-05 04:12:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 6f38faf5-16e2-3f19-96c1-fb30455a63f9 | -6.0734 | -37.30842 | 2025-01-05 04:12:00 | NOAA-20 | BELÉM DO BREJO DO CRUZ | PARAÍBA | Brasil | 2502003 | 25 | 33 | nan | nan | nan | Caatinga | 7.4 |
| a377e18d-1db8-3277-a900-e9638499230d | -10.66642 | -44.49228 | 2025-01-05 04:12:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a876a8c9-f5b6-368d-8c31-4e35908aef67 | -10.32295 | -42.41736 | 2025-01-05 04:12:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 7f44c165-67cb-3205-8644-a27fb5ae6f35 | -10.66918 | -44.49632 | 2025-01-05 04:12:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 75ff6dc0-07e3-3ecf-bbce-d322a0493691 | -6.92337 | -35.02789 | 2025-01-05 04:12:00 | NOAA-20 | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 9dd9ce5c-e6b3-3289-9a40-0dda5b514655 | -6.92297 | -35.03072 | 2025-01-05 04:12:00 | NOAA-20 | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 17e9c2d6-1a8a-393b-b91e-f015d449d1b5 | -6.26013 | -37.2414 | 2025-01-05 04:12:00 | NOAA-20 | JARDIM DE PIRANHAS | RIO GRANDE DO NORTE | Brasil | 2405603 | 24 | 33 | nan | nan | nan | Caatinga | 2.2 |
| c1a21fef-77f3-37b2-b648-6c3a6fbb7f6c | -10.43733 | -44.88622 | 2025-01-05 04:12:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6a10fd0e-b923-32c3-a388-e5262ed75fb9 | -7.68328 | -34.92408 | 2025-01-05 04:12:00 | NOAA-20 | GOIANA | PERNAMBUCO | Brasil | 2606200 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 003d2572-d891-3a4a-b639-f126982547ba | -9.3177 | -43.15865 | 2025-01-05 04:12:00 | NOAA-20 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 96d5d072-eb8d-3997-965f-1e15e82c6587 | -10.6548 | -44.50119 | 2025-01-05 04:12:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| ac64556c-9e06-30ae-bd58-1c0bf2000cf2 | -6.07282 | -37.31229 | 2025-01-05 04:12:00 | NOAA-20 | BELÉM DO BREJO DO CRUZ | PARAÍBA | Brasil | 2502003 | 25 | 33 | nan | nan | nan | Caatinga | 7.4 |
| cb591156-cb7b-39f1-8551-4a7b7d657199 | -10.43676 | -44.88977 | 2025-01-05 04:12:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 53920cae-8644-3026-96b8-e057e6dbfa0b | -6.07224 | -37.31618 | 2025-01-05 04:12:00 | NOAA-20 | BELÉM DO BREJO DO CRUZ | PARAÍBA | Brasil | 2502003 | 25 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 03e15516-c241-392e-8c4c-d82a667edd39 | -10.64929 | -44.4931 | 2025-01-05 04:12:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9ca8d6a8-dd10-39f9-8efb-b8c6a36e171c | -13.32964 | -41.36581 | 2025-01-05 04:14:00 | NOAA-20 | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 48d2a4a3-3754-3a39-819b-dc2de83ef974 | -11.50526 | -48.21239 | 2025-01-05 04:14:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c8bd6dfd-fb7c-3f45-a252-35405023aad1 | -11.9678 | -41.33604 | 2025-01-05 04:14:00 | NOAA-20 | BONITO | BAHIA | Brasil | 2904050 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 8a135d49-fce4-392f-a62e-02112690ffce | -11.11202 | -45.29631 | 2025-01-05 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 867e7ef7-48c9-3e47-8d67-cea5bf1e09c0 | -12.43986 | -41.75609 | 2025-01-05 04:14:00 | NOAA-20 | SEABRA | BAHIA | Brasil | 2929909 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 0fd800ef-a8c5-3c10-b67b-c648be292878 | -12.05599 | -40.01102 | 2025-01-05 04:14:00 | NOAA-20 | IPIRÁ | BAHIA | Brasil | 2914000 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 2525b035-cd57-3611-b622-76c360d35fc9 | -13.32902 | -41.37014 | 2025-01-05 04:14:00 | NOAA-20 | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 7f279037-a0af-3392-ba01-305f67119ae4 | -14.81152 | -42.84519 | 2025-01-05 04:14:00 | NOAA-20 | ESPINOSA | MINAS GERAIS | Brasil | 3124302 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 30d723e8-5294-31aa-85e2-7f963ec4e837 | -12.05529 | -40.01588 | 2025-01-05 04:14:00 | NOAA-20 | IPIRÁ | BAHIA | Brasil | 2914000 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| f89b4b04-21b2-32d4-aad1-bad53e85dd84 | -12.40397 | -41.48865 | 2025-01-05 04:14:00 | NOAA-20 | PALMEIRAS | BAHIA | Brasil | 2923506 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 802d6214-f3ab-34eb-bc74-4b98e6a1f8e2 | -11.89382 | -46.94137 | 2025-01-05 04:14:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 19083b7a-4462-3aef-9dc8-234c703f9d38 | -11.80128 | -49.32652 | 2025-01-05 04:14:00 | NOAA-20 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f0e55b33-1685-3f1f-9ffa-83848b9fe45e | -13.33264 | -41.37073 | 2025-01-05 04:14:00 | NOAA-20 | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| fd50ea0c-117f-31a0-b600-e07914cd5954 | -12.41051 | -41.48417 | 2025-01-05 04:14:00 | NOAA-20 | PALMEIRAS | BAHIA | Brasil | 2923506 | 29 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 11f26c47-0181-3dc6-985c-04d4e0ca2d24 | -12.41408 | -41.48471 | 2025-01-05 04:14:00 | NOAA-20 | PALMEIRAS | BAHIA | Brasil | 2923506 | 29 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 8b9b6a61-f0bf-3639-a81a-dc42176d8548 | -12.41111 | -41.48975 | 2025-01-05 04:14:00 | NOAA-20 | PALMEIRAS | BAHIA | Brasil | 2923506 | 29 | 33 | nan | nan | nan | Caatinga | 4.9 |
| cf720cce-ad3b-32be-b6a4-1e83ad690373 | -12.66091 | -46.57602 | 2025-01-05 04:14:00 | NOAA-20 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 706444aa-3a9a-393b-8920-e4ef81703022 | -12.4004 | -41.4881 | 2025-01-05 04:14:00 | NOAA-20 | PALMEIRAS | BAHIA | Brasil | 2923506 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| ee513ad8-6a29-32c3-808c-da1d26d1b2a5 | -12.40993 | -41.48824 | 2025-01-05 04:14:00 | NOAA-20 | PALMEIRAS | BAHIA | Brasil | 2923506 | 29 | 33 | nan | nan | nan | Caatinga | 2.5 |
| d1f40405-2645-3225-9d58-91009081e59b | -12.40814 | -41.48512 | 2025-01-05 04:14:00 | NOAA-20 | PALMEIRAS | BAHIA | Brasil | 2923506 | 29 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 95eb6767-e6af-3543-ab80-965f200050c2 | -14.80979 | -42.84175 | 2025-01-05 04:14:00 | NOAA-20 | ESPINOSA | MINAS GERAIS | Brasil | 3124302 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b7e7f060-f52c-355d-8899-907e3c6d78bd | -15.56974 | -47.85777 | 2025-01-05 04:14:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0cef66f1-8f17-3665-8217-b91e25131eb9 | -12.4135 | -41.48878 | 2025-01-05 04:14:00 | NOAA-20 | PALMEIRAS | BAHIA | Brasil | 2923506 | 29 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 225309dc-e37b-3719-8a2a-a4072ff81c91 | -12.41171 | -41.48568 | 2025-01-05 04:14:00 | NOAA-20 | PALMEIRAS | BAHIA | Brasil | 2923506 | 29 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 7043f9ea-2499-3a87-bae9-449c2be592ce | -14.80921 | -42.84563 | 2025-01-05 04:14:00 | NOAA-20 | ESPINOSA | MINAS GERAIS | Brasil | 3124302 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a8c0dc0e-fd14-3b5c-b603-328c686d8b55 | -14.80807 | -42.84462 | 2025-01-05 04:14:00 | NOAA-20 | ESPINOSA | MINAS GERAIS | Brasil | 3124302 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 62ddc2bb-a4a3-33ef-9fea-f28a5f6fcdd0 | -11.80726 | -48.0851 | 2025-01-05 04:14:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 90c71bd8-332e-3227-bc66-e097688185b6 | -11.87968 | -52.51261 | 2025-01-05 04:14:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ac6ed4ad-afbc-3c4c-9a35-edf8b816a678 | -11.89315 | -46.94537 | 2025-01-05 04:14:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 362a8664-76da-3982-8f87-1256ec2a7a31 | -11.58579 | -44.86241 | 2025-01-05 04:14:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| b34d3e80-1a32-378f-a47c-67989d3afa87 | -12.34909 | -47.99412 | 2025-01-05 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b10187a4-1a68-3c0a-9e07-aae5693ca9c7 | -22.26028 | -56.82822 | 2025-01-05 04:16:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| dea9d5e5-6071-3036-9e86-b99abc9520f6 | -23.69842 | -46.67743 | 2025-01-05 04:16:00 | NOAA-20 | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| af18a8ca-def7-305d-b6f0-b06474670cd2 | -23.9857 | -48.91963 | 2025-01-05 04:16:00 | NOAA-20 | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 0.3 |
| e787c972-1bb4-3071-ad1f-7d0afdc57069 | -22.26108 | -56.82463 | 2025-01-05 04:16:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a0ee8d5e-8ab6-316f-a149-ca8a2ce008c2 | -23.98232 | -48.91896 | 2025-01-05 04:16:00 | NOAA-20 | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| aad9b639-35d0-302e-a442-d98ebd1ee6a1 | -23.33748 | -46.77266 | 2025-01-05 04:16:00 | NOAA-20 | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| be0ea620-0211-3f0b-9510-d1024d0416f6 | -20.22581 | -50.91829 | 2025-01-05 04:16:00 | NOAA-20 | SANTA FÉ DO SUL | SÃO PAULO | Brasil | 3546603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 39bfd7a7-9936-3ce1-b5b9-145b6728d3f9 | -20.22475 | -50.9171 | 2025-01-05 04:16:00 | NOAA-20 | SANTA FÉ DO SUL | SÃO PAULO | Brasil | 3546603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 4be27305-b896-3962-9b86-a9cb9623decd | -21.83512 | -56.40221 | 2025-01-05 04:16:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 72c87369-2336-34f0-80c3-5ffae60432bf | -23.59994 | -46.92026 | 2025-01-05 04:16:00 | NOAA-20 | COTIA | SÃO PAULO | Brasil | 3513009 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| ced2bc13-b275-31c0-8c65-cbb228ffc67e | -20.99529 | -51.7953 | 2025-01-05 04:16:00 | NOAA-20 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 084b87c6-6453-3333-a0ce-a80fcf1830e8 | -22.53847 | -48.81403 | 2025-01-05 04:16:00 | NOAA-20 | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c484b448-90e9-33de-91f5-39aaa078d6c2 | -21.83436 | -56.40574 | 2025-01-05 04:16:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b9087c73-70f5-331a-a493-eac9594f52f2 | -21.83957 | -56.40704 | 2025-01-05 04:16:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ac32c751-b955-349e-a9b4-76cdba9c07e9 | -21.83881 | -56.41053 | 2025-01-05 04:16:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 470c5bee-6a65-3e16-8e6f-a8d24162f354 | -21.84032 | -56.40354 | 2025-01-05 04:16:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| eb3a6acc-c2da-3379-98eb-5b3a3d20723b | -19.50724 | -50.14538 | 2025-01-05 04:16:00 | NOAA-20 | CAMPINA VERDE | MINAS GERAIS | Brasil | 3111101 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6da2ed13-facb-3f4c-a8ab-702c27b50a43 | -24.24179 | -50.74028 | 2025-01-05 04:16:00 | NOAA-20 | ORTIGUEIRA | PARANÁ | Brasil | 4117305 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 7858deaa-e30b-3ba1-b9dc-70a2de89a915 | -30.77261 | -52.53032 | 2025-01-05 04:18:00 | NOAA-20 | ENCRUZILHADA DO SUL | RIO GRANDE DO SUL | Brasil | 4306908 | 43 | 33 | nan | nan | nan | Pampa | 0.8 |
| 2eb6ce35-cac2-3082-b3c1-876e7b80f3b0 | -29.872 | -51.15786 | 2025-01-05 04:18:00 | NOAA-20 | CANOAS | RIO GRANDE DO SUL | Brasil | 4304606 | 43 | 33 | nan | nan | nan | Pampa | 1.1 |
| f9359e18-e1c0-3dcd-a209-f84942f15c38 | -28.02456 | -48.64437 | 2025-01-05 04:18:00 | NOAA-20 | GAROPABA | SANTA CATARINA | Brasil | 4205704 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| d54365c5-061b-35a0-a567-7283aa5a4ac3 | -27.69698 | -50.03968 | 2025-01-05 04:18:00 | NOAA-20 | LAGES | SANTA CATARINA | Brasil | 4209300 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| a7676416-321f-38ef-a9c6-98294fbe461f | -11.80789 | -48.08504 | 2025-01-05 05:05:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 25b4a82a-146f-3618-bfb1-cee42bdcceb7 | -11.50913 | -48.21162 | 2025-01-05 05:05:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 21ead4fb-4050-36dd-a760-8690d47c8f18 | -12.1922 | -64.05966 | 2025-01-05 05:08:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d8095057-7673-31a1-b911-d313a8debf4b | -17.26557 | -51.05813 | 2025-01-05 05:08:00 | NOAA-21 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 372b1471-7a61-365f-a5f1-b96675fd2123 | -16.61584 | -49.23812 | 2025-01-05 05:08:00 | NOAA-21 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b98ccd5d-7e5a-3131-8ee1-a9e10a51b213 | -19.50875 | -50.14381 | 2025-01-05 05:08:00 | NOAA-21 | CAMPINA VERDE | MINAS GERAIS | Brasil | 3111101 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e19a97ea-f932-32a1-9866-b93e5cc503d3 | -18.51946 | -53.40161 | 2025-01-05 05:08:00 | NOAA-21 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d42ae16d-8b1b-3b9a-abc0-ba2b0f2daba9 | -12.17391 | -64.03256 | 2025-01-05 05:08:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5b25896a-0279-3e69-8b03-b683f1ad0b7e | -16.61065 | -49.23744 | 2025-01-05 05:08:00 | NOAA-21 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a96a76ff-fdcc-371d-812d-04eb665f4365 | -25.19742 | -49.32304 | 2025-01-05 05:10:00 | NOAA-21 | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 9103c9d5-b4f0-378a-9b7a-024d863d545c | -21.84116 | -56.40445 | 2025-01-05 05:10:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6e2d6c46-e2eb-3e6a-bf48-25c3d1ad00e8 | -21.84259 | -56.40253 | 2025-01-05 05:10:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e354209a-adfb-37aa-88a3-b864615b2153 | -21.84175 | -56.40012 | 2025-01-05 05:10:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 593bfd05-02b7-3161-951b-9a6c03198d02 | -21.83842 | -56.4063 | 2025-01-05 05:10:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f4f72d85-ef64-39ab-9d1e-42bf73bf0ab1 | -22.26046 | -56.82382 | 2025-01-05 05:10:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 34490968-7fa2-3792-ace5-e6c42d5c7112 | -21.84199 | -56.40686 | 2025-01-05 05:10:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e3dd1a95-dc63-32bf-8ba3-f7775c80427b | -22.54155 | -48.81431 | 2025-01-05 05:10:00 | NOAA-21 | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ae4a0fe0-43eb-39b6-84e1-7de305b8b7a2 | -21.83902 | -56.40197 | 2025-01-05 05:10:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2552083e-b142-365a-af9d-aed700c95b4c | -30.47037 | -53.4967 | 2025-01-05 05:12:00 | NOAA-21 | CAÇAPAVA DO SUL | RIO GRANDE DO SUL | Brasil | 4302808 | 43 | 33 | nan | nan | nan | Pampa | 2.2 |


[Clique aqui para ver as próximas entradas](README4.md)
