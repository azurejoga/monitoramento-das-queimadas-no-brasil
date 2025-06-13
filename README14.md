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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4aa1d9f7-3566-3c9b-8383-01def53fba58 | -9.39806 | -48.42137 | 2025-06-13 04:32:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ed0776b1-2a73-37a5-ad98-952be1228ac6 | -8.65481 | -47.13505 | 2025-06-13 04:32:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| df0aa1c2-8340-3722-9057-fe7319cba687 | -9.84696 | -44.69491 | 2025-06-13 04:32:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bd2a68cb-5682-365e-8f02-b5e0c3fa9cac | -9.0422 | -47.02543 | 2025-06-13 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 83b4c355-f410-3351-bca9-3698a0405364 | -6.73592 | -47.42256 | 2025-06-13 04:32:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3d8fa9d2-e49b-3440-a281-27cd734d968d | -10.36449 | -57.23267 | 2025-06-13 04:32:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 83502361-a8f1-399f-ae41-c09a57321590 | -10.87608 | -54.74745 | 2025-06-13 04:32:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0ff366b9-c36b-3f64-8da6-9a7fa2dd92e4 | -11.16869 | -46.88108 | 2025-06-13 04:32:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 47f997ba-3569-399c-a3a4-23c1e420c62a | -11.36912 | -56.56001 | 2025-06-13 04:32:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a2f1fd26-556e-34d0-bc61-cda57b8ce95e | -10.64806 | -49.42954 | 2025-06-13 04:32:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 188ea820-854b-3bea-afde-9961f24b6254 | -10.83763 | -53.77218 | 2025-06-13 04:32:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5b6d6961-adf6-3072-b40e-5e1df1e74cce | -9.87259 | -61.39987 | 2025-06-13 04:32:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fdb07930-851b-39bc-9298-6b8855b81b8e | -7.45895 | -45.51926 | 2025-06-13 04:32:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c6e4eb26-2468-3e9d-868f-b6c84ce155d4 | -6.94508 | -44.5575 | 2025-06-13 04:32:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a27f08fe-e6b4-371f-9c80-e57e4f13fa6e | -9.4146 | -48.42401 | 2025-06-13 04:32:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 89a34509-b628-3b76-b954-edb663834005 | -13.11662 | -44.07783 | 2025-06-13 04:32:00 | NOAA-20 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f66f9025-0638-36b5-9faa-07843d6c26e2 | -11.13395 | -53.91995 | 2025-06-13 04:32:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 5e6dd45f-9791-3de7-b744-adc8818bb83e | -10.80811 | -54.03889 | 2025-06-13 04:32:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 89d562b1-364b-3490-9076-30d2f2211d52 | -9.01395 | -48.164 | 2025-06-13 04:32:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 77bb2ca5-357f-3286-9f7c-543b8bf28b38 | -9.40559 | -57.54995 | 2025-06-13 04:32:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 5ae14e38-3d36-33b9-bb24-3b6fd4a4e1ef | -10.29984 | -57.13788 | 2025-06-13 04:32:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2b58b44d-ffea-3e5b-a454-a84f6cd8d925 | -11.80024 | -43.78983 | 2025-06-13 04:32:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b369ce89-54aa-36ae-8107-cbb0558842dd | -10.64142 | -49.42847 | 2025-06-13 04:32:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 9259ba70-1708-3421-9e94-ed72bd089604 | -11.07635 | -55.06908 | 2025-06-13 04:32:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3d4f70b7-7878-32c6-bdfb-5ae01d518cf2 | -10.23698 | -52.23604 | 2025-06-13 04:32:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| c5424752-9846-32a5-a83b-c6b8271a1c0f | -11.80638 | -56.96959 | 2025-06-13 04:32:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 587ded21-d9e3-3244-a13f-b8ef537b33e5 | -12.13706 | -54.66589 | 2025-06-13 04:32:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 23f4710a-dfb9-3593-9ee5-57aee3796ae1 | -8.95584 | -47.27253 | 2025-06-13 04:32:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 683fff35-76c3-3a94-9c67-0f64a0ccdf04 | -10.85096 | -53.79003 | 2025-06-13 04:32:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| cc78a972-8ef7-351a-a9c0-c3b122eb7514 | -9.39035 | -48.42727 | 2025-06-13 04:32:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ed3df6ba-7381-31c8-9722-99369035a7bd | -12.17481 | -54.23325 | 2025-06-13 04:32:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| cd1e1285-405c-3fe3-9286-64003e985794 | -11.12902 | -53.94828 | 2025-06-13 04:32:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 7c34e246-e4b6-3446-b7d3-cb3dd8dbe92b | -11.56704 | -54.57546 | 2025-06-13 04:32:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| a37a6a59-31c5-321a-8bef-89ae69ac733a | -11.13263 | -54.21667 | 2025-06-13 04:32:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c4e06f30-c025-35bb-a63d-de1e36f4e989 | -11.79712 | -43.78616 | 2025-06-13 04:32:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9248dee9-43f5-3cde-abdb-497f935880a2 | -12.12815 | -54.66814 | 2025-06-13 04:32:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8eb62d0b-6927-312c-a1b8-2009550f19a9 | -11.36407 | -56.55646 | 2025-06-13 04:32:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0f4c1cbe-a6d9-3f74-94e3-f0be52fff64b | -11.21185 | -49.00286 | 2025-06-13 04:32:00 | NOAA-20 | CRIXÁS DO TOCANTINS | TOCANTINS | Brasil | 1706258 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| cb492a5e-2835-30f6-84d8-477af93c58ee | -12.76712 | -44.41168 | 2025-06-13 04:32:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 6e854ad0-879f-30f0-a18a-7692c130367a | -11.92032 | -54.81692 | 2025-06-13 04:32:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bcbd7dda-461d-3961-ac6c-0a74ffc22abc | -11.20799 | -49.00583 | 2025-06-13 04:32:00 | NOAA-20 | CRIXÁS DO TOCANTINS | TOCANTINS | Brasil | 1706258 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ff7b6ade-cc66-301b-8535-02420e2a98d2 | -10.69938 | -49.49219 | 2025-06-13 04:32:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 697267c1-455a-3737-a2c3-afe903be4d7d | -12.00768 | -45.13483 | 2025-06-13 04:32:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fef985b1-b920-39ec-8d59-439218ffcc24 | -11.12841 | -53.95178 | 2025-06-13 04:32:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 551b12af-d579-311d-9f03-2fb2cdebaa36 | -9.87771 | -46.28029 | 2025-06-13 04:32:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 958e6969-70f3-32b9-aeae-6dda5f23ce19 | -10.35342 | -51.98915 | 2025-06-13 04:32:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 721e4e32-ae8a-3ef1-8762-c32e43c8e400 | -11.37677 | -55.11135 | 2025-06-13 04:32:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 890c9ae0-881b-3f44-a604-2b7306111777 | -10.59938 | -52.82845 | 2025-06-13 04:32:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 297403dd-3e12-3537-b0da-1163d469f308 | -9.8766 | -61.40133 | 2025-06-13 04:32:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ef6f07be-d21a-3052-9040-a20dc066a121 | -11.13764 | -53.9462 | 2025-06-13 04:32:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5d091d53-2e41-3831-8e59-fa3e039b5c52 | -10.86335 | -54.29804 | 2025-06-13 04:32:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 623eb117-95d4-36f5-9a8c-c5e6fd12c08b | -11.57117 | -54.57626 | 2025-06-13 04:32:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 5b88420f-862a-34ba-b4fd-737d9eb41ee7 | -12.2593 | -51.44331 | 2025-06-13 04:32:00 | NOAA-20 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9a7b7c9d-694f-3114-8b54-b2ba347cb412 | -11.80155 | -56.96867 | 2025-06-13 04:32:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 8e747160-1aa2-3ae1-8334-76b6cf3c543e | -9.3997 | -48.41092 | 2025-06-13 04:32:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 068e4e42-88ae-30a8-b5cf-41764420acfc | -10.6955 | -49.49517 | 2025-06-13 04:32:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| be216d07-f20d-3fc2-af87-a05a6704858b | -10.29929 | -57.1408 | 2025-06-13 04:32:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 86af6aa2-6cc8-37fa-ae67-d8e374c6f743 | -10.92273 | -56.84022 | 2025-06-13 04:32:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 750a3989-d0e4-3800-a38e-c7957ed1f3df | -9.40082 | -48.42538 | 2025-06-13 04:32:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 19159a95-d26a-3cb2-bcc9-e34146d3dd3f | -9.21743 | -62.47588 | 2025-06-13 04:32:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f7c7bce5-1083-3d53-9cad-a9aee3dc0acf | -13.04097 | -50.40086 | 2025-06-13 04:32:00 | NOAA-20 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c51e925b-6298-35a6-b016-56a395b262b0 | -9.10832 | -46.92056 | 2025-06-13 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 469e4bb2-3e08-3323-a1df-7bd52e7ef467 | -11.36538 | -56.55381 | 2025-06-13 04:32:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3e2cb9a4-c4f2-3087-bd82-c03e9eccbb16 | -9.40744 | -48.42643 | 2025-06-13 04:32:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2886bfce-62cb-3452-8b65-c0483996fa8b | -10.91404 | -56.83281 | 2025-06-13 04:32:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 8e1e840d-2d39-3628-bb06-43391c9a483b | -10.63866 | -49.42441 | 2025-06-13 04:32:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| dcdc43e5-aa3d-3dbd-a9f0-98c724fa86be | -10.36141 | -57.50139 | 2025-06-13 04:32:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dbb36e76-6ffb-35e4-b1b1-5928f813d587 | -9.38978 | -48.40934 | 2025-06-13 04:32:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9ea8c401-a3be-3952-9024-dcf6564ca44f | -10.88032 | -54.7482 | 2025-06-13 04:32:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 69e75a63-8c1d-3965-bb7f-e972906cebc5 | -7.45371 | -45.50639 | 2025-06-13 04:32:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 30df9e1c-321b-34e8-9a75-ddad2785739b | -11.81407 | -54.50326 | 2025-06-13 04:32:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a9ad9dc2-df47-30eb-9375-2d1b8b514156 | -6.94618 | -42.89547 | 2025-06-13 04:32:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 5c22ce1e-3621-3929-b9c6-f36f1d2286fc | -10.64474 | -49.42901 | 2025-06-13 04:32:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| eb98f63d-8763-366b-87e2-e67474af001d | -10.18431 | -49.50262 | 2025-06-13 04:32:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 955dba16-3c31-36c0-8e34-089073769f4a | -10.69606 | -49.49164 | 2025-06-13 04:32:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 89303425-ba42-3233-a835-2925e49ab83e | -12.26847 | -54.53547 | 2025-06-13 04:32:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5baadfc5-1676-30b7-a40d-333dde754b87 | -10.69826 | -49.49924 | 2025-06-13 04:32:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 0c35596c-ceef-3473-9a25-cb843382c063 | -10.29427 | -57.13989 | 2025-06-13 04:32:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a5d98225-75b6-390f-93ab-821d23030181 | -10.51114 | -48.68561 | 2025-06-13 04:32:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| af254ad2-b08a-315a-9a93-1b3ba5f51e70 | -11.3644 | -56.55905 | 2025-06-13 04:32:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 28a85978-680d-3b72-8687-ea6463596de1 | -10.65363 | -49.41602 | 2025-06-13 04:32:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| c49196d7-8572-3195-b2bb-d1257a0a52a5 | -11.81817 | -54.50401 | 2025-06-13 04:32:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 98a0ab8b-9974-39a4-9901-8a9f276ee11b | -12.28617 | -50.10608 | 2025-06-13 04:32:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 40a1bef2-005c-3272-9186-44f7e47ea9b8 | -10.64364 | -47.48196 | 2025-06-13 04:32:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 5b945de6-8476-337f-a991-38361192dda9 | -7.45194 | -45.51816 | 2025-06-13 04:32:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 844e0482-865c-3818-bb5b-c0c6d9f091ac | -6.9438 | -44.56616 | 2025-06-13 04:32:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4c5d2864-140a-3b91-9592-22e061a8d472 | -10.69493 | -49.4987 | 2025-06-13 04:32:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| aa303fe7-cfb7-3664-a649-4938d1cdbc19 | -8.58949 | -45.86226 | 2025-06-13 04:32:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2025f1ba-de07-3295-bb7a-49df15d6b955 | -9.25114 | -57.53715 | 2025-06-13 04:32:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 492f5a28-5f10-31f6-9ee9-923c479a8f53 | -9.4102 | -48.43044 | 2025-06-13 04:32:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| eded94e1-d315-31f1-ad7b-52e67d5016ec | -7.44843 | -45.51762 | 2025-06-13 04:32:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 32cadffa-3557-3eb8-a078-058faae97acb | -9.84386 | -44.68976 | 2025-06-13 04:32:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 51dd08cc-ec36-325b-8d19-7be75c1737dd | -9.66893 | -48.77177 | 2025-06-13 04:32:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0434326a-010f-3e3e-bb87-4eb5e43ba601 | -10.36615 | -57.22388 | 2025-06-13 04:32:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 22957f08-dba4-311b-9fc6-86cc75a36405 | -10.1387 | -47.43734 | 2025-06-13 04:32:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8247281a-a15f-3dae-b6f1-85e35f4246ea | -6.15851 | -47.27127 | 2025-06-13 04:32:00 | NOAA-20 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a5926e4d-5444-3e3d-9550-273ff81474ac | -9.39309 | -48.40986 | 2025-06-13 04:32:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 59b2c525-d0a7-3651-9f96-85b007a73859 | -8.95249 | -47.272 | 2025-06-13 04:32:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d76958c8-d272-337f-a7de-11757707c4c4 | -11.17555 | -46.88217 | 2025-06-13 04:32:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 7d26117c-18f9-3ef4-a301-9c69cb656a44 | -11.2113 | -49.00637 | 2025-06-13 04:32:00 | NOAA-20 | CRIXÁS DO TOCANTINS | TOCANTINS | Brasil | 1706258 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |


[Clique aqui para ver as próximas entradas](README15.md)
