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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 98220868-a384-34f6-95eb-fcec53643b83 | -6.92261 | -41.83036 | 2025-11-17 03:46:00 | NOAA-20 | SÃO JOÃO DA VARJOTA | PIAUÍ | Brasil | 2209955 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 07579647-3078-3175-927b-3046b83d92c4 | -6.70761 | -40.79757 | 2025-11-17 03:46:00 | NOAA-20 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 1ceb5f8f-facb-3f00-bd42-3145f4dd544c | -4.69437 | -46.31376 | 2025-11-17 03:46:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 180df071-37e0-3303-8584-f2265b2e9cca | -7.71547 | -42.18091 | 2025-11-17 03:46:00 | NOAA-20 | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 60fc7323-d321-3444-9213-3ef7eb7cdc6b | -7.36795 | -45.8356 | 2025-11-17 03:46:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 379554d4-6e22-335b-8345-de4433bcf26b | -4.7254 | -46.38791 | 2025-11-17 03:46:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 4.3 |
| c86b8920-fc6e-3f51-8896-6c5abaceb21d | -3.47313 | -49.68841 | 2025-11-17 03:46:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d0551b61-f831-3976-8683-b35b9360c023 | -5.47832 | -40.96194 | 2025-11-17 03:46:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 4ea38566-c24e-333a-a2af-212b254e5d37 | -5.76074 | -42.51528 | 2025-11-17 03:46:00 | NOAA-20 | BARRO DURO | PIAUÍ | Brasil | 2201408 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| d4e479d6-08f0-31a2-861c-45db2e0523d1 | -8.11974 | -43.5258 | 2025-11-17 03:46:00 | NOAA-20 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7a0d9196-89d3-3d82-9696-28d09da97c01 | -4.73721 | -46.38666 | 2025-11-17 03:46:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| afc4cf05-79a3-3a77-b603-ac034d60d67f | -7.8474 | -40.58508 | 2025-11-17 03:46:00 | NOAA-20 | SIMÕES | PIAUÍ | Brasil | 2210706 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 3a1cff41-7c68-3703-a57e-456f415c57e7 | -4.69872 | -46.30959 | 2025-11-17 03:46:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0125c553-ec32-3384-9edf-415e6edc49ee | -5.0967 | -46.08036 | 2025-11-17 03:46:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 917e64fe-6f51-32d6-afd9-97fead3065b9 | -5.48952 | -41.38316 | 2025-11-17 03:46:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 63e9896f-72cc-3caf-9349-d904c5aef79c | -7.61956 | -42.57746 | 2025-11-17 03:46:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| dcad1caa-efbe-32a3-9a95-1eb93baa55aa | -6.08677 | -41.61 | 2025-11-17 03:46:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 8a3bb8fa-2590-37bd-a34c-dddba6294ff4 | -4.99823 | -44.36643 | 2025-11-17 03:46:00 | NOAA-20 | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| e3f4ecae-fa94-37e1-8731-cfb3277f26d2 | -5.52242 | -40.99246 | 2025-11-17 03:46:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 99e181c1-e94c-31ed-99e1-154b4148b06f | -5.1094 | -46.23522 | 2025-11-17 03:46:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fe34d1b3-5ac9-3f9c-a93b-aa98559beb9e | -5.34243 | -43.04793 | 2025-11-17 03:46:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| cff7566d-548c-39f4-8cdc-47d1cfc2c752 | -4.89337 | -44.86092 | 2025-11-17 03:46:00 | NOAA-20 | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 50f001fb-d6c2-3167-bbfe-437e10b99357 | -5.92258 | -44.0172 | 2025-11-17 03:46:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5d7929e8-f85a-3974-8b99-fd2b6ff4c3c8 | -6.12615 | -41.82051 | 2025-11-17 03:46:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| a2990cfc-d7ec-3517-ab66-f370817b5b8e | -7.70932 | -42.9456 | 2025-11-17 03:46:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| aa6fa47b-f376-3cc6-a46b-ca6bdb55a812 | -3.29805 | -50.07399 | 2025-11-17 03:46:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 41a05f81-1554-3fc4-a0e6-845625788c90 | -4.91598 | -47.41747 | 2025-11-17 03:46:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 0215e76b-a1c2-318b-b3e4-7956ef1710b0 | -4.68948 | -46.30857 | 2025-11-17 03:46:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 76a4c657-5168-3adb-8f54-0069b208566b | -6.80525 | -39.13399 | 2025-11-17 03:46:00 | NOAA-20 | LAVRAS DA MANGABEIRA | CEARÁ | Brasil | 2307502 | 23 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 638e1fb7-1390-38e7-bb9b-56c9c11b501d | -7.61892 | -42.58133 | 2025-11-17 03:46:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 4a4215ed-0cd6-3395-a24e-6c48062c7d9c | -5.46897 | -40.97062 | 2025-11-17 03:46:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| af7f955f-1f5f-306b-be64-0336290fec16 | -6.36006 | -46.15704 | 2025-11-17 03:46:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8d4d0d6f-b0be-315e-977f-0bac4d046bbc | -4.40182 | -45.83776 | 2025-11-17 03:46:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b8aa804e-a277-3fec-b5c4-e895fce4c855 | -6.94507 | -41.53023 | 2025-11-17 03:46:00 | NOAA-20 | SANTANA DO PIAUÍ | PIAUÍ | Brasil | 2209351 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 1d5307c8-b0f0-3c3c-9e74-46705ee922fc | -5.49437 | -41.37848 | 2025-11-17 03:46:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 8d175f2c-45a4-331d-aca5-5d57a8c71da1 | -7.25321 | -48.01731 | 2025-11-17 03:46:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f88f8039-ca16-36a3-b7a3-249ac7ccbd71 | -5.76632 | -42.50805 | 2025-11-17 03:46:00 | NOAA-20 | BARRO DURO | PIAUÍ | Brasil | 2201408 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 6d93bcbd-0f80-387f-b279-ba54da30ef4c | -5.32914 | -43.04543 | 2025-11-17 03:46:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 790eec81-3ce7-397d-9650-4ad40e980b9c | -4.85668 | -44.16103 | 2025-11-17 03:46:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ac812aee-b1c3-3f49-9da4-0caf98103fd9 | -8.24517 | -41.42624 | 2025-11-17 03:46:00 | NOAA-20 | SÃO FRANCISCO DE ASSIS DO PIAUÍ | PIAUÍ | Brasil | 2209658 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| d1e4fcb7-a6a6-39d6-a398-b67d3b9d9195 | -7.89922 | -35.14356 | 2025-11-17 03:46:00 | NOAA-20 | PAUDALHO | PERNAMBUCO | Brasil | 2610608 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 527d1e3b-02c1-3691-933b-9c67ff562947 | -5.14146 | -43.84359 | 2025-11-17 03:46:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 933a627b-a7ca-3d31-9370-e557615d716c | -6.30484 | -38.9117 | 2025-11-17 03:46:00 | NOAA-20 | ORÓS | CEARÁ | Brasil | 2309508 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 75fbe16e-21a2-3d3f-813e-a29759c14fce | -4.09728 | -47.11988 | 2025-11-17 03:46:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5cc666c6-34df-312d-b653-47f3b83e4ab4 | -4.71981 | -46.38673 | 2025-11-17 03:46:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 0323ca6b-67ae-390b-8124-0919ea57ddb9 | -7.03288 | -47.62488 | 2025-11-17 03:46:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 407168ae-3e22-39dc-b09d-df09b0707ad6 | -7.70442 | -42.94869 | 2025-11-17 03:46:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 995ce3c1-8861-317f-8f3b-5a9a1f07576e | -6.61732 | -41.4685 | 2025-11-17 03:46:00 | NOAA-20 | SÃO JOÃO DA CANABRAVA | PIAUÍ | Brasil | 2209856 | 22 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 40bab5dd-d8a4-3494-a322-84f702ba5f82 | -7.49087 | -45.87182 | 2025-11-17 03:46:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f014dfa3-24de-31a7-b42a-96de2cec818e | -8.68895 | -39.69626 | 2025-11-17 03:46:00 | NOAA-20 | SANTA MARIA DA BOA VISTA | PERNAMBUCO | Brasil | 2612604 | 26 | 33 | nan | nan | nan | Caatinga | 1.2 |
| c4fefcf2-2687-385b-9d7b-dcb0d7bfcd77 | -5.79892 | -43.99369 | 2025-11-17 03:46:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a37cfb5d-fa70-3792-b8d2-995ea4591ff6 | -6.48716 | -39.76689 | 2025-11-17 03:46:00 | NOAA-20 | SABOEIRO | CEARÁ | Brasil | 2311900 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 7ff05390-8191-3c6d-b656-1c2d9a32354b | -6.37472 | -42.2994 | 2025-11-17 03:46:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 4a894be2-4f60-39aa-a898-74cd48500910 | -8.28177 | -41.43509 | 2025-11-17 03:46:00 | NOAA-20 | SÃO FRANCISCO DE ASSIS DO PIAUÍ | PIAUÍ | Brasil | 2209658 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| d7fd1daf-f897-38e9-bea5-737bf8da9750 | -4.69503 | -46.3099 | 2025-11-17 03:46:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9eb29e68-955d-3938-9300-dc29352ca233 | -7.86722 | -37.56973 | 2025-11-17 03:46:00 | NOAA-20 | IGUARACY | PERNAMBUCO | Brasil | 2606903 | 26 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 797e4b1f-d7a0-3014-b5df-53e3b5947c66 | -6.91701 | -39.1597 | 2025-11-17 03:46:00 | NOAA-20 | LAVRAS DA MANGABEIRA | CEARÁ | Brasil | 2307502 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| ec991296-20b8-3073-b5be-658e75ca18b2 | -7.08444 | -42.74164 | 2025-11-17 03:46:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 8c51a010-0966-3b24-b966-efa9c0247103 | -7.2897 | -45.45571 | 2025-11-17 03:46:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b35c8976-e81e-3fd2-b5ba-d9034bede553 | -5.03724 | -43.60776 | 2025-11-17 03:46:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 19.4 |
| 459a9a15-dee3-37e3-8782-decacfb92ece | -7.90265 | -35.14408 | 2025-11-17 03:46:00 | NOAA-20 | PAUDALHO | PERNAMBUCO | Brasil | 2610608 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 9aecbb39-36a9-385c-8b43-d2fde45eba7e | -4.70575 | -45.10758 | 2025-11-17 03:46:00 | NOAA-20 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5879f176-e8d7-3fdb-919a-3d76b8d15984 | -7.7002 | -42.94783 | 2025-11-17 03:46:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 12769258-1513-3702-9114-ea31ced1c86d | -6.68573 | -47.39364 | 2025-11-17 03:46:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 119452c1-6684-3862-bdcf-f593acd1ab47 | -6.68702 | -42.03789 | 2025-11-17 03:46:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 11.8 |
| 58f5cc1b-3922-3f05-80cb-442598e38c86 | -4.70629 | -45.10448 | 2025-11-17 03:46:00 | NOAA-20 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 366decf3-1ad0-3f3d-9e45-d522db7ea65b | -8.49669 | -41.26598 | 2025-11-17 03:46:00 | NOAA-20 | QUEIMADA NOVA | PIAUÍ | Brasil | 2208650 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 0167bb29-d2ae-3114-8958-740a4656fc4d | -5.32542 | -43.04036 | 2025-11-17 03:46:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 0b8ee34d-778d-3544-bd80-b60cf41c16f2 | -8.11461 | -43.52927 | 2025-11-17 03:46:00 | NOAA-20 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| cecc3122-d161-3b90-b41c-970ddf410a55 | -4.72671 | -46.38041 | 2025-11-17 03:46:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 11e1eb78-0f4e-36ac-b66c-e35e4ec4d8ea | -8.21224 | -43.5654 | 2025-11-17 03:46:00 | NOAA-20 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 893186b0-c5f0-36f2-82fb-f422c3aa1e84 | -6.67991 | -42.05531 | 2025-11-17 03:46:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 33832cbc-927e-371b-9d2b-1e109e8d3ad3 | -7.71144 | -42.18017 | 2025-11-17 03:46:00 | NOAA-20 | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 48032ccd-d451-391f-bdd7-55afd351bdb7 | -6.49006 | -39.77149 | 2025-11-17 03:46:00 | NOAA-20 | SABOEIRO | CEARÁ | Brasil | 2311900 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 7066fe67-63eb-34a9-8421-6adbd5025394 | -8.24196 | -40.86955 | 2025-11-17 03:46:00 | NOAA-20 | ACAUÃ | PIAUÍ | Brasil | 2200053 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| f2007f9c-7998-3a2a-84d1-ae363bc0ab29 | -4.05623 | -47.50439 | 2025-11-17 03:46:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 491749d1-ef06-3700-b0dd-1b884539a621 | -3.52608 | -49.10837 | 2025-11-17 03:46:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 46c48200-67e1-36ca-85a6-669c89405e7d | -7.03869 | -42.25261 | 2025-11-17 03:46:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| af3ed0e3-ac4e-3181-bce6-af07501b7156 | -4.74077 | -46.39948 | 2025-11-17 03:46:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d713e35a-d393-3bb7-8b21-bfab17aea1c4 | -6.68581 | -42.0451 | 2025-11-17 03:46:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 13.4 |
| e8c71ce5-c40c-32b2-a755-b8bc046380f8 | -4.1171 | -47.30243 | 2025-11-17 03:46:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8ae86e5c-6ec2-32dd-bc1c-e2161844ede9 | -7.21922 | -47.98832 | 2025-11-17 03:46:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 9d0cbd50-4d55-36c9-aa6f-a8809b4cfdd7 | -6.84644 | -42.83791 | 2025-11-17 03:46:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| f9c7ca6d-2c95-3de3-8507-df9910434e56 | -5.75735 | -43.02192 | 2025-11-17 03:46:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 9.6 |
| 8d1f4834-155e-3a13-9a7e-e7b70286f2c0 | -6.35862 | -46.15247 | 2025-11-17 03:46:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 56bdc61e-9887-34f2-a2e8-3188e3f203b1 | -3.76655 | -47.64899 | 2025-11-17 03:46:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 72a1c4ac-a15a-3d68-98cf-a793b6061d67 | -4.09849 | -48.03338 | 2025-11-17 03:46:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9683074e-64b6-388a-a745-657d5a0d353d | -6.49293 | -39.77631 | 2025-11-17 03:46:00 | NOAA-20 | SABOEIRO | CEARÁ | Brasil | 2311900 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| e95c01ff-22d0-3583-9ffd-562e7392c8d3 | -3.4598 | -49.99318 | 2025-11-17 03:46:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1add55f9-cdeb-37aa-9b01-2043a3b71fa9 | -6.6852 | -42.04873 | 2025-11-17 03:46:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 13.4 |
| 934a3028-c9f3-3a05-9b5d-2d6c2665d5c9 | -6.06651 | -41.65715 | 2025-11-17 03:46:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| c4547ae7-e0e1-37a5-b77a-87119ad21a76 | -6.87406 | -39.84404 | 2025-11-17 03:46:00 | NOAA-20 | ASSARÉ | CEARÁ | Brasil | 2301604 | 23 | 33 | nan | nan | nan | Caatinga | 4.1 |
| deb7ede8-d33e-31a9-b782-30cd712613a0 | -6.84148 | -42.84114 | 2025-11-17 03:46:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| c38bcd8e-d4c6-3693-abd4-0a7973cb50f3 | -7.97396 | -42.28038 | 2025-11-17 03:46:00 | NOAA-20 | PEDRO LAURENTINO | PIAUÍ | Brasil | 2207934 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 20bf766a-41cd-364c-a4e4-9f64eef1d47d | -7.87271 | -42.87978 | 2025-11-17 03:46:00 | NOAA-20 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 1d985c9e-ddaa-3179-84ca-08285d274bfd | -6.34104 | -41.75739 | 2025-11-17 03:46:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 0d36d98e-8472-3db5-8ad1-be854e6ae2c9 | -5.32986 | -43.04112 | 2025-11-17 03:46:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| b5729080-9117-32a1-87bc-f673bb9ca22c | -6.21735 | -47.24199 | 2025-11-17 03:46:00 | NOAA-20 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d466340a-3b38-3359-a229-d255c9d020c9 | -6.36598 | -42.21233 | 2025-11-17 03:46:00 | NOAA-20 | FRANCINÓPOLIS | PIAUÍ | Brasil | 2204006 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 31dd061a-a375-3fad-80ea-eaecfeff640e | -7.02419 | -39.36547 | 2025-11-17 03:46:00 | NOAA-20 | CARIRIAÇU | CEARÁ | Brasil | 2303204 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |


[Clique aqui para ver as próximas entradas](README17.md)
