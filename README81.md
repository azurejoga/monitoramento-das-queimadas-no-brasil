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

## Dados Diários - Página 81

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9d78c2d9-205b-321a-9ecd-16ae696aa181 | -22.32355 | -47.13304 | 2025-10-07 04:40:00 | NPP-375D | CONCHAL | SÃO PAULO | Brasil | 3512209 | 35 | 33 | nan | nan | nan | Cerrado | 4.2 |
| c3a7ede4-bb24-31cc-9a18-a00b0bbb7445 | -21.79928 | -46.15526 | 2025-10-07 04:40:00 | NPP-375D | CAMPESTRE | MINAS GERAIS | Brasil | 3111002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 4e943296-5c55-3c3e-961a-bbdadf863ac8 | -18.11508 | -53.36487 | 2025-10-07 04:40:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d6f96457-4bce-35e6-b156-d611a73f061f | -21.30189 | -45.94963 | 2025-10-07 04:40:00 | NPP-375D | ALFENAS | MINAS GERAIS | Brasil | 3101607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 321a75f3-b8ad-3460-ad7f-32e54a5fd6cd | -20.20842 | -43.91916 | 2025-10-07 04:40:00 | NPP-375D | NOVA LIMA | MINAS GERAIS | Brasil | 3144805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| f26b3f1a-74bc-3a2e-b8f3-75685cdf3b08 | -18.10513 | -53.35918 | 2025-10-07 04:40:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e76a8762-3080-3938-9826-d157e3cd46f3 | -20.03576 | -48.24013 | 2025-10-07 04:40:00 | NPP-375D | MIGUELÓPOLIS | SÃO PAULO | Brasil | 3529708 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6f7aa005-1531-3311-b0ac-d25300ebba32 | -20.21246 | -43.92441 | 2025-10-07 04:40:00 | NPP-375D | NOVA LIMA | MINAS GERAIS | Brasil | 3144805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 588d71de-d712-3a8c-a161-38f173f12670 | -18.15306 | -53.39832 | 2025-10-07 04:40:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9a02c512-44bc-388d-854d-3ceda0568558 | -22.15996 | -49.38862 | 2025-10-07 04:40:00 | NPP-375D | AVAÍ | SÃO PAULO | Brasil | 3504305 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0979fbc2-95bf-33f2-bf31-ff030dd8946f | -19.59713 | -44.85906 | 2025-10-07 04:40:00 | NPP-375D | PITANGUI | MINAS GERAIS | Brasil | 3151404 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 791d2713-1746-358d-bef0-6cb326a711eb | -19.01427 | -49.75303 | 2025-10-07 04:40:00 | NPP-375D | GURINHATÃ | MINAS GERAIS | Brasil | 3129103 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c1e14a88-cb73-3568-9b7a-b30f5e937b1d | -19.95296 | -44.63248 | 2025-10-07 04:40:00 | NPP-375D | IGARATINGA | MINAS GERAIS | Brasil | 3130200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 79428fe9-1bca-3709-8fb7-f57a1ddd93b5 | -21.62153 | -45.29314 | 2025-10-07 04:40:00 | NPP-375D | TRÊS CORAÇÕES | MINAS GERAIS | Brasil | 3169307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 81e32eeb-977c-3375-9186-4c5239910ee4 | -18.10833 | -53.34399 | 2025-10-07 04:40:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9f2ca87f-113b-3415-a328-5748e5b92bfe | -18.51124 | -47.51925 | 2025-10-07 04:40:00 | NPP-375D | DOURADOQUARA | MINAS GERAIS | Brasil | 3123502 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6d9a8bf7-b7ff-309c-86f6-ead553847528 | -22.54355 | -44.98441 | 2025-10-07 04:40:00 | NPP-375D | CRUZEIRO | SÃO PAULO | Brasil | 3513405 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| d1cc3bd7-e6b4-3a76-b059-6b911eea7692 | -23.31472 | -46.94223 | 2025-10-07 04:40:00 | NPP-375D | JUNDIAÍ | SÃO PAULO | Brasil | 3525904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 9fa6d9c5-d721-32dd-8774-49d146f24e45 | -18.23921 | -53.35817 | 2025-10-07 04:40:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2e86dbf0-3309-33f5-be10-c44c093c5e62 | -22.17792 | -49.38733 | 2025-10-07 04:40:00 | NPP-375D | AVAÍ | SÃO PAULO | Brasil | 3504305 | 35 | 33 | nan | nan | nan | Cerrado | 17.7 |
| f00fbb64-bea8-3bae-b597-b13456a6be46 | -20.10319 | -44.18617 | 2025-10-07 04:40:00 | NPP-375D | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 62cc90ce-26ea-3e24-8e05-051852f7a746 | -21.08153 | -46.90352 | 2025-10-07 04:40:00 | NPP-375D | MONTE SANTO DE MINAS | MINAS GERAIS | Brasil | 3143203 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7c2b25ad-201c-3219-9041-b5b4e0600f91 | -21.77115 | -47.78008 | 2025-10-07 04:40:00 | NPP-375D | SÃO CARLOS | SÃO PAULO | Brasil | 3548906 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3cc59d0a-6a66-385b-b00d-915e5df7f182 | -18.17001 | -53.38461 | 2025-10-07 04:40:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d0fdb343-87e4-3bc2-991b-f2761bf5f3fd | -17.68144 | -52.23957 | 2025-10-07 04:40:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1445027f-1fde-31f6-a7fe-8e88d49636d6 | -18.11581 | -53.3607 | 2025-10-07 04:40:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d70ebd7f-cd9a-3ee1-b79e-858bb69786e3 | -18.1596 | -53.36031 | 2025-10-07 04:40:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 3.9 |
| a45d57cb-585e-3f68-91a6-599d6f6f43ee | -21.76538 | -47.78204 | 2025-10-07 04:40:00 | NPP-375D | SÃO CARLOS | SÃO PAULO | Brasil | 3548906 | 35 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 23723c2c-e70e-3e8c-acb7-7ed1f09fb355 | -18.10646 | -53.37244 | 2025-10-07 04:40:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 26a8a869-3a90-348d-94a6-70d23a7be192 | -23.22661 | -46.56131 | 2025-10-07 04:40:00 | NPP-375D | ATIBAIA | SÃO PAULO | Brasil | 3504107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 5414438a-6b0f-3a34-8da2-aaf7803cc6e1 | -23.12979 | -47.00363 | 2025-10-07 04:40:00 | NPP-375D | JUNDIAÍ | SÃO PAULO | Brasil | 3525904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 265bf63f-0d88-330e-a364-ddf151646018 | -18.24205 | -53.34176 | 2025-10-07 04:40:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1e996da4-fa89-35a5-8866-295fd140b76c | 0.7555 | -51.58296 | 2025-10-07 04:53:00 | NOAA-20 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a919f14a-8ef5-3850-bbf6-39830b52303f | 0.56895 | -50.04041 | 2025-10-07 04:53:00 | NOAA-20 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f98771fa-e034-35a6-b005-27a756e98ebf | 4.41467 | -60.37654 | 2025-10-07 04:53:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1a8f9445-b2ad-3268-8071-a2f244c201f5 | 4.42009 | -60.3772 | 2025-10-07 04:53:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4fa40e81-44ab-3525-973b-a5daf21a7367 | 0.7483 | -51.58052 | 2025-10-07 04:53:00 | NOAA-20 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 335b4beb-f31d-338b-9f31-a815f1202687 | 0.56546 | -50.04095 | 2025-10-07 04:53:00 | NOAA-20 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d9e8b8c5-b794-3df2-bce8-9f3215755a2d | -1.70965 | -55.68447 | 2025-10-07 04:55:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 29e4c105-a032-30fc-8836-4ca4fcb28e8c | -5.63859 | -43.60603 | 2025-10-07 04:55:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9f2c0a1d-c92d-3168-a6c6-2aa7bbf610ff | -6.69573 | -42.86794 | 2025-10-07 04:55:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| c0d1a555-54b3-3f01-9cda-104b60a419b6 | -5.64615 | -45.95914 | 2025-10-07 04:55:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a7c5eff5-d4f0-3693-907f-7ecf9de6d4a3 | -7.80357 | -44.14415 | 2025-10-07 04:55:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d16971ee-1695-31a8-8a22-faf4570221a7 | -4.68778 | -49.50118 | 2025-10-07 04:55:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 356301e0-8828-3c5d-858c-13036c2e2c32 | -6.33838 | -44.0298 | 2025-10-07 04:55:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e82b5006-04a6-32eb-abc2-3a2568b69f31 | -3.14364 | -44.4207 | 2025-10-07 04:55:00 | NOAA-20 | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fee679b1-34ee-327d-80fa-5bb91964baf8 | -8.18508 | -44.11947 | 2025-10-07 04:55:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 92d6bee9-bef3-38c6-b9cf-b8e956386b56 | -8.20614 | -44.18804 | 2025-10-07 04:55:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| ed620b63-ec0e-3976-93bf-abee5440b45b | -3.09352 | -47.03065 | 2025-10-07 04:55:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4999aeef-1827-3b23-9f5b-71f575f53833 | -6.56423 | -44.14858 | 2025-10-07 04:55:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b2fb98b1-7267-33b6-98d5-9734eb4b5a16 | -1.56877 | -55.43432 | 2025-10-07 04:55:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 47479940-c4c7-3e56-a9ea-a8d6bbd024ae | -3.35464 | -54.72712 | 2025-10-07 04:55:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 26bcdf2a-9b79-3d09-9f06-0b940beba64c | -3.66618 | -51.95094 | 2025-10-07 04:55:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5b1d9b75-1e99-3919-b652-73f47426bc05 | -6.70336 | -42.85881 | 2025-10-07 04:55:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 777e03c8-996c-3580-9f9f-2a2782706626 | -8.20511 | -44.19611 | 2025-10-07 04:55:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a2a8d184-9094-3b0e-af59-266033d49821 | -1.09368 | -53.68716 | 2025-10-07 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| c47ba98b-1481-3d71-b11e-9b020a9a1f33 | -5.50261 | -43.06499 | 2025-10-07 04:55:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 26c7cd47-5ec9-3ed5-a60b-c1b21d69b5d9 | -5.39169 | -40.99949 | 2025-10-07 04:55:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 10.7 |
| f973e1f9-59de-386c-80e8-470d9e522707 | -5.49893 | -43.07233 | 2025-10-07 04:55:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 20.1 |
| e790c9c5-007b-31b1-8f1c-4e73592115ba | -7.69423 | -42.41267 | 2025-10-07 04:55:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| e1400f27-77eb-3c51-801b-c4eb3d0a3a65 | -5.14941 | -49.84993 | 2025-10-07 04:55:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 98a9efe6-048b-3d95-bbe0-bd213c21efd3 | -5.75736 | -43.39304 | 2025-10-07 04:55:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| cdf9b005-76fb-3bce-ae69-47b57a8a1b59 | -6.75183 | -49.04123 | 2025-10-07 04:55:00 | NOAA-20 | PIÇARRA | PARÁ | Brasil | 1505635 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 25bac0dc-dd66-36b2-a7a0-d2ee7e472c59 | -2.9354 | -54.17999 | 2025-10-07 04:55:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c9831c70-a218-313a-ae90-87becefdc7bf | -8.17022 | -43.33662 | 2025-10-07 04:55:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 7f31fc60-5c0a-3d7b-a41f-f5c316d4c1da | -1.3693 | -49.03804 | 2025-10-07 04:55:00 | NOAA-20 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| cdc78ac8-79ed-3884-a6cf-968d4b0cdea3 | -3.10016 | -47.01696 | 2025-10-07 04:55:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f79d5f89-5c14-3b70-9918-3c7eb0a3b128 | -1.36891 | -49.0351 | 2025-10-07 04:55:00 | NOAA-20 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4b3d3912-e192-351c-a60e-9bd95a447bcb | -5.50137 | -43.07355 | 2025-10-07 04:55:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 2c1a6742-1fe6-3027-93f1-ae32124f097b | -3.67524 | -55.57577 | 2025-10-07 04:55:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f05072cb-694c-3946-bb50-963a08986f17 | -2.53344 | -48.24321 | 2025-10-07 04:55:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c9cf7f5b-d9ce-302c-bf42-a8d78bb6b0f5 | -8.61931 | -44.94061 | 2025-10-07 04:55:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 84685e78-7dd0-3bd6-ada5-0da18a344d0b | -6.72591 | -42.82927 | 2025-10-07 04:55:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| ad9b0d25-f818-34af-ad60-85f8df4fea97 | -3.09284 | -50.58143 | 2025-10-07 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 7f9c454a-9329-362d-b779-19f9f7a7f483 | -3.09344 | -50.57751 | 2025-10-07 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| af89dc46-ef18-3564-ad3f-021d8cab46a1 | -1.61507 | -46.66657 | 2025-10-07 04:55:00 | NOAA-20 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c605cdc9-fd95-3940-92e7-c08793b5bdae | -8.48893 | -46.26871 | 2025-10-07 04:55:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4751cc15-2bdc-3d31-89fa-b460e94c79e2 | -3.09451 | -47.02481 | 2025-10-07 04:55:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 32163c20-0ba0-3fcf-94cc-884208f4cb08 | -5.99185 | -44.14969 | 2025-10-07 04:55:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 85e8ee49-52cd-3a19-aadc-d7c0c248ab08 | -5.49297 | -43.07153 | 2025-10-07 04:55:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 789a7619-198c-3a88-942c-c92be8de5190 | -8.20458 | -44.20018 | 2025-10-07 04:55:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f6a61d73-6f88-3c4c-aa26-b387849aa301 | -5.48582 | -43.07947 | 2025-10-07 04:55:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 081239d8-5618-3902-bd7b-382183eaaa2d | -2.89709 | -52.87278 | 2025-10-07 04:55:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.2 |
| 2cf6a029-5660-3329-9a1b-78ddc0b2d8f2 | -5.89344 | -49.37109 | 2025-10-07 04:55:00 | NOAA-20 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 74476aea-2a21-3a07-bc4c-49ad547b54ac | -3.0856 | -50.58094 | 2025-10-07 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 6029615c-8e87-35ec-83b2-35ec09a3fb65 | -5.39247 | -40.99382 | 2025-10-07 04:55:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 10.7 |
| 607671f9-b963-3441-92cd-093444d56fbc | -6.70348 | -42.85664 | 2025-10-07 04:55:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 2b41d211-8fe3-3773-adc7-43c10e59a0f8 | -5.4912 | -43.08445 | 2025-10-07 04:55:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 16411021-d78a-322e-a9ea-e6bdc353c6a8 | -6.70296 | -42.86059 | 2025-10-07 04:55:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 399dbf08-90c2-39b2-b5c6-de7151eb1af0 | -5.64536 | -45.9647 | 2025-10-07 04:55:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c9db9b34-cc52-397a-82d2-e2de102c0ab1 | -8.199 | -44.23342 | 2025-10-07 04:55:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| aacf5e40-06e9-35a1-be4f-195472f197ed | -1.09646 | -53.69112 | 2025-10-07 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8a6280eb-92c4-39e3-9db1-6bac089cc6d9 | -4.68848 | -49.4965 | 2025-10-07 04:55:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| dffb0384-5a5c-3d69-bf74-b2fb42f06f67 | -4.91219 | -48.01892 | 2025-10-07 04:55:00 | NOAA-20 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 78865c49-72f8-3149-81d2-bc099ebdb17d | -8.20063 | -44.22137 | 2025-10-07 04:55:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 43fb5e0a-9a68-3963-b45b-34c02ab13947 | -2.53499 | -54.73937 | 2025-10-07 04:55:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 5140f84a-bdb5-325b-9658-ecfa58e9ff59 | -3.19831 | -51.0181 | 2025-10-07 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fb4db9c4-e704-3f90-ade6-de62c70b37e7 | -2.90319 | -50.73084 | 2025-10-07 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d92760b2-f38c-3b47-aa35-f1432e05c1cf | -2.24977 | -47.87006 | 2025-10-07 04:55:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8903619e-9ea7-3f56-b3af-d855db57dee5 | -7.6815 | -42.41058 | 2025-10-07 04:55:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 6.6 |


[Clique aqui para ver as próximas entradas](README82.md)
