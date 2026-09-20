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

## Dados Diários - Página 124

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1ec6422e-ea85-3c40-a930-db16a93cc714 | -6.595 | -45.4953 | 2026-09-20 14:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 78.6 |
| 19491914-9075-3ea4-ac3c-cab4c39f0d40 | -7.3259 | -55.6153 | 2026-09-20 14:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 173.2 |
| 3079ddc3-a19c-3078-8473-1dd9347b239a | -15.4174 | -53.0236 | 2026-09-20 14:10:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 107.4 |
| 8549bc31-4380-353e-9795-d6f4bffa8784 | -10.67 | -50.6678 | 2026-09-20 14:10:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 117.0 |
| 93fa34e5-d9a7-3633-9153-ebf0aed45330 | -11.731 | -50.7014 | 2026-09-20 14:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 97.2 |
| 012c2e74-1758-3d31-b67e-ef34699d867f | -7.7446 | -46.6961 | 2026-09-20 14:10:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 56.5 |
| dac0be01-f606-3ba4-966d-70bc29aa768c | -9.2606 | -45.9164 | 2026-09-20 14:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 161.4 |
| 890fe2cb-2ddd-3ab7-814c-6ae511b91de5 | -11.0506 | -54.9309 | 2026-09-20 14:10:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 180.0 |
| 48b6d0cc-57f6-3e3f-bf14-3f2bac73afe9 | -8.1688 | -54.7432 | 2026-09-20 14:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 118.4 |
| 7806d4a7-a937-3c4f-89e7-fecf44f5e973 | -8.4549 | -47.0072 | 2026-09-20 14:10:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 63.4 |
| 87e0a3d1-ab31-3a4a-b290-0f0268739aed | -9.8502 | -48.4053 | 2026-09-20 14:10:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 140.4 |
| 240a12cd-6004-3d7c-bb38-c7c73b670906 | -7.5704 | -57.6766 | 2026-09-20 14:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 54.8 |
| ebaa611e-383e-30bb-992a-468dd7adef72 | -9.0353 | -48.7704 | 2026-09-20 14:10:00 | GOES-19 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Amazônia | 81.9 |
| 310437e0-4a62-3559-b846-253f9c5f7f99 | -6.7406 | -44.0909 | 2026-09-20 14:10:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 78.4 |
| 5a307a6e-5c17-3d14-92cc-ab083b9030d3 | -12.2341 | -50.1703 | 2026-09-20 14:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 192.0 |
| cdbe96a5-216c-383a-b4a9-0d540dd28d66 | -8.169 | -54.7231 | 2026-09-20 14:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 54.1 |
| e3567330-dadd-35d7-9079-a35e63cd4fce | -11.0407 | -54.1772 | 2026-09-20 14:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 72.2 |
| 98669182-3538-386c-956b-7941e303c929 | -7.0267 | -43.6945 | 2026-09-20 14:10:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 78.4 |
| 0a82b840-a169-3079-883a-e737ad591a73 | -10.9694 | -57.1881 | 2026-09-20 14:10:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 61.2 |
| 24cb4fc5-622e-3fe0-8bfe-c882b8761228 | -11.041 | -54.1567 | 2026-09-20 14:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 122.1 |
| d480f3ad-719f-3942-87eb-0e9b3571b426 | -4.9797 | -37.4562 | 2026-09-20 14:10:00 | GOES-19 | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 134.9 |
| 5c60d9ce-3122-30d7-8864-35154080d5af | -11.875 | -49.9767 | 2026-09-20 14:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 81.4 |
| dfb9faca-5ef3-3206-ad19-ccf5386dd8dd | -14.1258 | -45.5904 | 2026-09-20 14:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 49.7 |
| 070ba99a-3c29-330e-99d8-d22896891f9b | -7.9637 | -44.0667 | 2026-09-20 14:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 66.0 |
| 516641cd-5f64-3185-8483-8f17cb5ba2aa | -10.4914 | -51.3212 | 2026-09-20 14:10:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 91.3 |
| 32c86e77-ab8d-3c8f-9bf2-e98ca31d003a | -12.5224 | -50.0484 | 2026-09-20 14:10:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 141.8 |
| efb7255c-6ec7-384e-b18e-6cd4816d02c4 | -8.05 | -46.2663 | 2026-09-20 14:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 179.4 |
| 2cdaa047-7bd3-363b-8174-a401b235e46b | -11.0509 | -54.9106 | 2026-09-20 14:10:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 594.7 |
| caf8a195-1ece-3ec6-80ca-0981357a764e | -10.473 | -51.2808 | 2026-09-20 14:10:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 80.7 |
| 1c3ed8f9-cb78-36f9-82fb-4bc9fe7f0293 | -12.3404 | -50.6942 | 2026-09-20 14:10:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 78.1 |
| dc329557-6f20-35b8-92a2-1492401c623e | -12.1328 | -47.041 | 2026-09-20 14:10:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 105.6 |
| e8ab39d4-0615-362b-8f6b-1f1a32a46fe3 | -2.9143 | -58.3401 | 2026-09-20 14:10:00 | GOES-19 | SILVES | AMAZONAS | Brasil | 1304005 | 13 | 33 | nan | nan | nan | Amazônia | 77.7 |
| 743a13db-a83e-3cd3-b377-b6b479b7d759 | -2.9157 | -57.8177 | 2026-09-20 14:10:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 74.6 |
| bcd79b03-426d-3864-abfe-e891e1546374 | -8.0894 | -55.331 | 2026-09-20 14:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 62.5 |
| 994e616b-4d3a-3298-b312-f139bc52bda7 | -11.4714 | -47.776 | 2026-09-20 14:10:00 | GOES-19 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 61.7 |
| f9685b03-26d8-3780-8f7d-4b84b2ae970b | -10.8364 | -50.9479 | 2026-09-20 14:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 233.5 |
| 8e631a63-50e3-332a-abc4-e0120a61167d | -5.9152 | -59.933 | 2026-09-20 14:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 60.8 |
| b2ac0969-5b9a-35ad-a8db-867756ca351f | -12.7629 | -46.1343 | 2026-09-20 14:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 84.3 |
| 09d049bb-eb46-32e8-aede-2f874570288d | -7.7634 | -46.6944 | 2026-09-20 14:10:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 60.2 |
| f4cb658a-b6e4-3bb2-ba8e-b5b45e950e9c | -11.4541 | -45.3662 | 2026-09-20 14:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 77.1 |
| da30af7a-62b3-3a61-82bd-3e2e8d05128b | -8.2314 | -61.3732 | 2026-09-20 14:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 55.4 |
| 17695e5d-4a15-3314-b5b0-e00bff5cf144 | -10.6703 | -50.6465 | 2026-09-20 14:10:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 107.4 |
| 4172ad3d-53eb-396c-b2f2-6c65c10b6771 | -11.6238 | -47.7786 | 2026-09-20 14:10:00 | GOES-19 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 95.0 |
| 1f51377b-a606-3fc0-b979-53d03c4b494d | -6.7185 | -55.0684 | 2026-09-20 14:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 77.0 |
| 5cfdd9e8-1475-35b3-88e8-7810dcdbc25e | -11.9681 | -50.1164 | 2026-09-20 14:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 129.7 |
| d2db5773-d7cd-33b9-93d2-578c7a2a99b5 | -10.41 | -48.933 | 2026-09-20 14:10:00 | GOES-19 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 69.6 |
| 25abeb2a-0d1b-32e6-90c2-7bba56145c9d | -10.8553 | -50.9459 | 2026-09-20 14:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 198.8 |
| b7db0e0d-6a57-3f5d-8c14-4d8b681072c7 | -8.1874 | -54.742 | 2026-09-20 14:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 86.0 |
| c12c8cb6-0c74-3a01-bba0-c99833648c80 | -12.5415 | -50.046 | 2026-09-20 14:10:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 64.0 |
| 9b0846e5-6040-398d-a964-e207d5e749ac | -7.5944 | -46.7095 | 2026-09-20 14:10:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 70.0 |
| 061691f7-952a-335f-ba9f-7956789a04d9 | -10.7466 | -50.5959 | 2026-09-20 14:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 87.1 |
| cbcb45eb-ab31-3ee1-a1c5-eb75903ce1ab | -8.7729 | -44.2568 | 2026-09-20 14:10:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 222.9 |
| 6ac1f90f-8f15-3fff-aeb1-d82db50e445f | -9.3577 | -50.0943 | 2026-09-20 14:10:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 101.0 |
| 183128e5-8aaf-3719-bf44-f9303fc4b593 | -14.6661 | -46.6919 | 2026-09-20 14:10:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 54.1 |
| 8fe60736-2201-3a9b-9e44-9d9901f887d1 | -10.6889 | -50.6658 | 2026-09-20 14:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 90.0 |
| c57e8519-826d-38ef-bb93-c9a28e7ca214 | -7.1392 | -42.0811 | 2026-09-20 14:10:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 105.7 |
| 30782d15-e448-36b3-a5a7-7129ada0bb83 | -11.0256 | -48.3164 | 2026-09-20 14:10:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 85.6 |
| 3910d60c-8fc5-3991-893d-deeb317132bf | -7.0455 | -43.6928 | 2026-09-20 14:10:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 90.5 |
| f1a476d4-f34c-31ea-a5e7-fee95b34d941 | -15.866 | -49.9177 | 2026-09-20 14:10:00 | GOES-19 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 71.0 |
| e1a82598-6271-30ea-add9-0d4e06038bbe | -8.1378 | -46.7933 | 2026-09-20 14:10:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 93.3 |
| 363c84bd-9ca9-3b8d-adc6-ed8030d19b43 | -11.4545 | -45.3432 | 2026-09-20 14:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 104.9 |
| 00aa80be-f472-3b82-9c7e-85c92e4a07b5 | -11.4537 | -45.3892 | 2026-09-20 14:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 86.7 |
| cd92f41d-24de-39d4-9da7-ad882892859c | -12.5227 | -50.0267 | 2026-09-20 14:10:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 113.9 |
| 6309d1a1-0edf-371b-8afb-79654cbe6c48 | -11.4544 | -51.4542 | 2026-09-20 14:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 98.4 |
| bd5d32ca-85e1-3895-ad1d-cb5a34b3b63a | -10.7463 | -50.6172 | 2026-09-20 14:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 129.0 |
| a4ae3f0c-e7be-3beb-b0b0-7ba7564cde47 | -12.2344 | -50.1488 | 2026-09-20 14:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 180.1 |
| 13852ab9-1846-3519-aadc-d58c0a501bd6 | -3.478 | -59.5779 | 2026-09-20 14:10:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 61.8 |
| 9d6acf09-aced-348f-a36b-d56b859cb5e1 | -9.2603 | -45.939 | 2026-09-20 14:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 563.2 |
| 2e22ddab-989b-39c7-970f-93fcd40c00d6 | -11.1372 | -54.0045 | 2026-09-20 14:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 92.5 |
| 45ecb6bf-ee04-3b63-874e-d3fc113380e2 | -8.0706 | -55.3522 | 2026-09-20 14:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 56.3 |
| f42e4ff6-73c5-3040-8f13-36fdd6a60479 | -6.9414 | -42.907 | 2026-09-20 14:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 80.1 |
| 5d7b8a76-7d04-3db3-a45d-5796830d671e | -9.0544 | -48.7469 | 2026-09-20 14:10:00 | GOES-19 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 343.8 |
| 13ca0223-33fe-32ba-8097-c91b5a8fa092 | -10.9692 | -57.208 | 2026-09-20 14:10:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 60.3 |
| d8791323-f034-3af5-91d9-268f004e2672 | -8.1872 | -54.7622 | 2026-09-20 14:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 80.5 |
| 3d92ae82-f8ed-3ef6-9234-56e3ed63d7b5 | -8.754 | -44.2589 | 2026-09-20 14:10:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 99.8 |
| 4078d047-bae5-3e5f-922f-c39327b276e6 | -11.1183 | -54.0062 | 2026-09-20 14:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 111.6 |
| e955dfbf-a496-39ea-a70d-70a08a0369e7 | -12.027 | -50.0015 | 2026-09-20 14:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 91.9 |
| 687105e5-ba3e-38e6-a75d-b72fb39027ca | -10.2787 | -50.2605 | 2026-09-20 14:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 109.1 |
| c71fa0de-87e8-344f-b81b-c0cbf2d6b3eb | -9.8313 | -48.4073 | 2026-09-20 14:10:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 136.0 |
| 4c2efadd-947d-3f48-8aef-801a843daccd | -7.7631 | -46.7167 | 2026-09-20 14:10:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 92.1 |
| 2d3baf25-42f5-3de1-9940-ad6f41491e74 | -9.2865 | -48.2453 | 2026-09-20 14:10:00 | GOES-19 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 88.4 |
| d2be4504-02c9-3d8d-9866-cf508592ceb7 | -14.6856 | -46.6886 | 2026-09-20 14:10:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 156.9 |
| 91f24d65-4188-3031-b7ee-87f1db0e468b | -6.7184 | -55.0884 | 2026-09-20 14:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 94.2 |
| 749e7be1-cd9c-3e08-a62b-9d4e8f1c2dee | -12.1516 | -47.0608 | 2026-09-20 14:10:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 147.0 |
| b09d2e62-0f19-305a-97b6-25851731e0b3 | -6.3382 | -59.9566 | 2026-09-20 14:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 184.4 |
| e840ef8c-0fef-3562-a67d-591b9bfecfe5 | -8.7003 | -45.4567 | 2026-09-20 14:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 75.0 |
| 52aa433a-579b-3e56-96e0-0c2a15b0ce9e | -13.5907 | -51.4794 | 2026-09-20 14:10:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 171.4 |
| c47af720-1efc-31ae-abd5-23f53979f0ad | -6.1359 | -59.9446 | 2026-09-20 14:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 68.6 |
| bda90562-dd93-3ebe-b003-feef452fc50d | -9.8397 | -46.4361 | 2026-09-20 14:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 235.5 |
| c126ff26-69c9-35b3-92d6-758f5e088038 | -8.8639 | -45.937 | 2026-09-20 14:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 123.8 |
| c862bb60-aa81-34ed-9495-e6f0dac6b39a | -10.7652 | -50.6153 | 2026-09-20 14:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 104.7 |
| 708c2b86-f83d-32d4-86a9-7419335705b6 | -6.7369 | -55.0874 | 2026-09-20 14:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 65.4 |
| 1e1e7185-f6cd-3869-93f6-355641c62924 | -11.0065 | -48.3187 | 2026-09-20 14:10:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 73.4 |
| 11aa24ec-1df9-3b6a-908e-e184f1489c59 | -8.7733 | -44.2336 | 2026-09-20 14:10:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 76.0 |
| d6f6dccc-92d5-3777-987a-f7755afe02ff | -8.4314 | -45.8467 | 2026-09-20 14:10:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 68.3 |
| 08530f3c-ff79-3992-9eb8-8e637c25e5e6 | -2.8009 | -59.8957 | 2026-09-20 14:10:00 | GOES-19 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 95.2 |
| 81c393f8-ea6c-35cc-89e5-0c53c5e916e9 | -3.1261 | -61.4077 | 2026-09-20 14:10:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 73.7 |
| 7774b7c1-6d7e-399e-84ce-11a941125967 | -10.2793 | -50.2177 | 2026-09-20 14:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 91.1 |
| 76aaf667-8475-3476-b970-f91d5e60078c | -8.1376 | -46.8155 | 2026-09-20 14:10:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 157.7 |
| 86b872f9-758d-32db-84cb-758efffe584f | -11.1369 | -54.0251 | 2026-09-20 14:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 94.5 |


[Clique aqui para ver as próximas entradas](README125.md)
