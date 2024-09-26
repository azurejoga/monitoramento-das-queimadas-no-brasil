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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1016e679-fe45-3bb2-80ae-a547cb6bc026 | -11.85655 | -49.62004 | 2024-09-26 00:43:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 50.1 |
| 7efa4b5f-07e8-3924-8494-5d27a0c665de | -11.85083 | -49.67371 | 2024-09-26 00:43:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 14.6 |
| d1a14357-7011-3c10-a7b9-ac61f18b90cb | -11.84872 | -49.65625 | 2024-09-26 00:43:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 58.9 |
| d45f5e38-64d9-3287-a731-8da4ad4b01b3 | -11.71818 | -47.861 | 2024-09-26 00:43:00 | TERRA_M-M | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 6195e5aa-8eaf-39fd-93c4-fe2fa251845e | -11.71656 | -47.84822 | 2024-09-26 00:43:00 | TERRA_M-M | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 9d96757e-e2de-38d2-8468-e418cc7379e0 | -11.70773 | -47.86234 | 2024-09-26 00:43:00 | TERRA_M-M | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 39.0 |
| 64ba6210-f247-3f4e-8be5-bcf842d958b4 | -11.70612 | -47.84956 | 2024-09-26 00:43:00 | TERRA_M-M | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 53.2 |
| 9ee614cb-76ed-3c8e-b323-5fcce137ecc9 | -11.67835 | -46.35321 | 2024-09-26 00:43:00 | TERRA_M-M | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 697ebbb0-54b2-3eb4-96e2-b5d7fa71e066 | -11.677 | -46.34283 | 2024-09-26 00:43:00 | TERRA_M-M | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 24.7 |
| 70ed2430-c8fb-36cb-bb0b-728873b3f7fe | -11.66752 | -46.34402 | 2024-09-26 00:43:00 | TERRA_M-M | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 9f4d8633-ed4e-39d3-a33f-9ecfbb0c5f09 | -11.52013 | -47.4237 | 2024-09-26 00:43:00 | TERRA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 718c3c40-af5e-3071-b376-8fef85ac0f6a | -11.50999 | -47.42479 | 2024-09-26 00:43:00 | TERRA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 365fe824-4c48-3400-b822-d5e8b2f6f6a3 | -11.47463 | -47.3102 | 2024-09-26 00:43:00 | TERRA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 37.6 |
| e43b0d7f-2811-317c-a41a-fa67f5c4ff2b | -11.47312 | -47.29855 | 2024-09-26 00:43:00 | TERRA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 34.5 |
| 028cb693-95ca-3f5d-b209-e382102de711 | -11.47162 | -47.2869 | 2024-09-26 00:43:00 | TERRA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 15.1 |
| a389d7ac-ddd6-3637-bb5b-a651d45fed2c | -11.46761 | -47.33476 | 2024-09-26 00:43:00 | TERRA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 9.7 |
| b01abf50-c366-3721-836e-a9a30f00c29d | -11.44458 | -47.31416 | 2024-09-26 00:43:00 | TERRA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 17.2 |
| b58375fd-a846-3e0a-85d7-1be3f35a484f | -11.42063 | -47.28828 | 2024-09-26 00:43:00 | TERRA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 165b35e6-de33-34a2-aef1-3cfa9d701689 | -11.19582 | -54.7711 | 2024-09-26 00:43:00 | TERRA_M-M | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 118.1 |
| 6fa8b9be-be13-3bd6-96cd-4e1afa443b47 | -11.19562 | -54.76454 | 2024-09-26 00:43:00 | TERRA_M-M | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 94.9 |
| cb25cbf0-e011-3f5f-aab5-00607365af42 | -11.07266 | -51.44823 | 2024-09-26 00:43:00 | TERRA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 19.3 |
| 3cd34b1e-a2f3-338e-9190-3bb61d486f7c | -11.0699 | -51.42492 | 2024-09-26 00:43:00 | TERRA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 50.2 |
| abd0413d-d27d-3c82-8ea2-d02c4d86f71e | -10.94556 | -50.15685 | 2024-09-26 00:43:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 18.0 |
| df2f4f64-e4a6-35a5-bda4-e000d8c0976b | -10.94298 | -50.1626 | 2024-09-26 00:43:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 86470c00-e386-3b34-9943-b1ea32420e5d | -10.94289 | -54.27405 | 2024-09-26 00:43:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 43.4 |
| daec3ad1-c348-3297-8260-6bcac1de161d | -10.85668 | -48.38213 | 2024-09-26 00:43:00 | TERRA_M-M | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 4b20d99e-d120-313d-aef5-063d17749b52 | -10.79544 | -50.1135 | 2024-09-26 00:43:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 21.2 |
| 9b5082df-f9a2-3276-bf23-de3cfc69c32e | -10.69038 | -47.95972 | 2024-09-26 00:43:00 | TERRA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 054a1f05-2e58-3cd8-be63-1065574d7184 | -10.64212 | -49.90402 | 2024-09-26 00:43:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 7598d8ea-2e54-3b56-b09b-fe5130847895 | -10.60538 | -51.12467 | 2024-09-26 00:43:00 | TERRA_M-M | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 16.3 |
| f18f9077-0e42-3fd8-9940-8f64aac216f5 | -10.45693 | -53.31723 | 2024-09-26 00:43:00 | TERRA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 32.4 |
| 5131161a-c9d0-33d2-804c-c160f2b95b5f | -10.15463 | -50.00178 | 2024-09-26 00:43:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 8b7c315c-deec-3cc3-9904-a44fa5631458 | -10.11352 | -50.01344 | 2024-09-26 00:43:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 30d11e04-4377-34d8-96ca-a619b0d515f0 | -10.04009 | -53.49194 | 2024-09-26 00:43:00 | TERRA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 173.2 |
| 1a30583b-a4ee-3ff9-89c4-ecc9d4a36d3f | -10.03634 | -53.4596 | 2024-09-26 00:43:00 | TERRA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 443.1 |
| 275fd3f8-422d-31c3-be7e-4812d763b0ac | -10.02418 | -53.49364 | 2024-09-26 00:43:00 | TERRA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 69.4 |
| 717c5ab0-d085-3293-bc03-0365ef77f531 | -10.02045 | -53.46113 | 2024-09-26 00:43:00 | TERRA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 39.6 |
| 17401fef-c0e1-3b53-b00b-54fc1394383d | -8.52104 | -55.20011 | 2024-09-26 00:43:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 90.3 |
| 14fa0503-3dad-39c3-8d20-cdc7b4148dc0 | -9.45188 | -40.36661 | 2024-09-26 00:43:00 | TERRA_M-M | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 40.6 |
| c1708c52-1eff-31ba-9af3-485b8de924bb | -9.25354 | -40.20411 | 2024-09-26 00:43:00 | TERRA_M-M | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 8f8b36c2-16f0-3430-80d8-c84bbb662fcb | -8.84091 | -44.95534 | 2024-09-26 00:43:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| f81d589b-ec5d-3a23-812f-dee6c884cd76 | -8.55136 | -44.07277 | 2024-09-26 00:43:00 | TERRA_M-M | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 77a7fcfd-e300-37e3-a53e-9bd21f06a046 | -8.55009 | -44.06374 | 2024-09-26 00:43:00 | TERRA_M-M | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 9b3456c0-b5ed-3567-8a17-3814266f1579 | -8.3865 | -45.40387 | 2024-09-26 00:43:00 | TERRA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 20.3 |
| ca90b0e3-663e-3898-ad0d-fd6ce62d8824 | -8.38525 | -45.39486 | 2024-09-26 00:43:00 | TERRA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 4b44e975-7ff1-39f5-909d-6bc359b82835 | -8.26428 | -44.8478 | 2024-09-26 00:43:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 97fe907c-f58d-3106-a744-04754e54e14a | -8.23673 | -44.85762 | 2024-09-26 00:43:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 993e94a2-523c-3aa4-8516-0018666bedd2 | -8.23549 | -44.84874 | 2024-09-26 00:43:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 19.9 |
| c10b1673-6ee0-3ed5-837e-74b9119ac2e0 | -8.06865 | -42.89025 | 2024-09-26 00:43:00 | TERRA_M-M | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 81ce01d9-7ab8-318f-bcb7-c9018941d635 | -7.97068 | -42.85124 | 2024-09-26 00:43:00 | TERRA_M-M | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 51da01f7-1c70-3070-83f3-66692fda7a64 | -7.58925 | -42.2987 | 2024-09-26 00:43:00 | TERRA_M-M | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 31.2 |
| 5fdc22a2-0a86-32af-b995-0c6c816e202c | -7.58774 | -42.2882 | 2024-09-26 00:43:00 | TERRA_M-M | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 11.0 |
| de696499-be6d-3363-98dd-3fb0fd8c6aae | -7.24376 | -39.85456 | 2024-09-26 00:43:00 | TERRA_M-M | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 9.1 |
| 22e7f74f-a93d-3f87-bae3-d6cfc2c5d2bc | -7.22341 | -42.45314 | 2024-09-26 00:43:00 | TERRA_M-M | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 12.4 |
| f03bd028-3ac2-3e15-bf69-056e291f9dc8 | -7.20235 | -42.50938 | 2024-09-26 00:43:00 | TERRA_M-M | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 12.4 |
| 856ab6c8-33ff-3d5c-befe-bd6e5dd94710 | -7.07174 | -44.16537 | 2024-09-26 00:43:00 | TERRA_M-M | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 4146f703-1a13-34df-b413-22a9d91ae2d9 | -6.9605 | -42.47862 | 2024-09-26 00:43:00 | TERRA_M-M | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 34.1 |
| 93b463fa-c199-38ad-bf26-a5bc3bd97e75 | -6.95898 | -42.46804 | 2024-09-26 00:43:00 | TERRA_M-M | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 25.0 |
| 3b4c2701-2059-37d5-b367-5efd56cca6c9 | -6.94761 | -39.42596 | 2024-09-26 00:43:00 | TERRA_M-M | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 9.6 |
| 0dd6fd33-608e-382c-9dd6-502990f4ec39 | -6.85644 | -43.1051 | 2024-09-26 00:43:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 0b3a8346-ec4f-36dd-9263-75a61c29045f | -6.71957 | -43.56817 | 2024-09-26 00:43:00 | TERRA_M-M | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 6948bf64-4d72-37b6-9cc0-0af52590094f | -6.71823 | -43.55878 | 2024-09-26 00:43:00 | TERRA_M-M | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 29.0 |
| cdd50278-bdbe-3090-9035-b8ae0eb5ba45 | -6.68958 | -43.55344 | 2024-09-26 00:43:00 | TERRA_M-M | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 12.3 |
| bdb227b3-87c0-3e6e-821e-f0e2cd80492e | -6.68823 | -43.54403 | 2024-09-26 00:43:00 | TERRA_M-M | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 17.3 |
| 3f3274b1-67a4-331b-a39b-a9125b304d89 | -6.68048 | -43.5548 | 2024-09-26 00:43:00 | TERRA_M-M | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 213765d7-8c80-3947-9ced-02ed1ff0e9a4 | -6.67912 | -43.5454 | 2024-09-26 00:43:00 | TERRA_M-M | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 2ac6b94a-ae3b-3f56-a989-15b34ca21278 | -6.61659 | -39.58842 | 2024-09-26 00:43:00 | TERRA_M-M | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 26.8 |
| 396ed6d5-eca1-35eb-8946-2392e993f205 | -6.54988 | -43.02827 | 2024-09-26 00:43:00 | TERRA_M-M | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 2fdfed30-ef23-3cfb-8cfa-4a2c1c619001 | -6.54198 | -43.03959 | 2024-09-26 00:43:00 | TERRA_M-M | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 21.5 |
| c775b98f-5c9f-3f68-a7ed-48e3cd7c3a9e | -6.54054 | -43.02964 | 2024-09-26 00:43:00 | TERRA_M-M | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 34.7 |
| 20f3401e-884b-3338-b5bf-464da6321e77 | -6.46947 | -43.30603 | 2024-09-26 00:43:00 | TERRA_M-M | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 4e9da7ca-75ca-33d1-ae0c-fbf45a2d96a8 | -6.46026 | -43.30739 | 2024-09-26 00:43:00 | TERRA_M-M | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 260a5897-1d35-37c3-9e2b-f3a35f695ae3 | -6.45885 | -43.29772 | 2024-09-26 00:43:00 | TERRA_M-M | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 8cda0813-56da-3918-93b4-ea7c4cc4063f | -6.34672 | -43.16119 | 2024-09-26 00:43:00 | TERRA_M-M | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 44087417-359b-36f4-b498-2f00c871f39f | -6.34096 | -43.16794 | 2024-09-26 00:43:00 | TERRA_M-M | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 85fc6602-d793-353d-97e4-1583fc4e880a | -6.32968 | -42.50862 | 2024-09-26 00:43:00 | TERRA_M-M | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| b28f3d5c-98db-3325-b874-73c85712cfe1 | -6.32004 | -42.50988 | 2024-09-26 00:43:00 | TERRA_M-M | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 10.9 |
| caceb7a2-2ec6-3218-ae7f-6aa7141e4530 | -6.31038 | -42.51112 | 2024-09-26 00:43:00 | TERRA_M-M | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 6907c87e-579b-3c14-8216-326816785963 | -6.24171 | -43.31826 | 2024-09-26 00:43:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| d2d6fd4a-7715-3941-96ec-c8eab5db5153 | -6.23248 | -43.31966 | 2024-09-26 00:43:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 22.4 |
| fd8e6d4f-dad2-383f-965e-ae71c6cfd9e8 | -6.23109 | -43.3099 | 2024-09-26 00:43:00 | TERRA_M-M | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 99e9690f-ba0a-3f6b-a761-87a1f599e732 | -6.207 | -43.2736 | 2024-09-26 00:43:00 | TERRA_M-M | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 8ba6babd-78ea-3c2c-8c9a-ac2418757406 | -6.12019 | -42.80701 | 2024-09-26 00:43:00 | TERRA_M-M | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 2da42a38-6b68-32c8-85fa-378ebd495d2c | -6.02002 | -42.55027 | 2024-09-26 00:43:00 | TERRA_M-M | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 8.3 |
| cd911776-a829-3982-aeb1-a88499af1f29 | -5.9499 | -42.56716 | 2024-09-26 00:43:00 | TERRA_M-M | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 9.3 |
| ada0f0cc-83a3-3d4b-85b5-6f03bd7bad7f | -5.89838 | -43.88655 | 2024-09-26 00:43:00 | TERRA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| e171105a-e9c1-33b1-b131-2516c2683428 | -12.24584 | -43.88139 | 2024-09-26 00:43:00 | TERRA_M-M | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 8.0 |
| eb8711e0-5e60-3b93-9b09-ab6211612fb4 | -12.22989 | -45.5119 | 2024-09-26 00:43:00 | TERRA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 30.4 |
| f88500af-9b13-343e-8185-9463f5c375fb | -12.2286 | -45.50226 | 2024-09-26 00:43:00 | TERRA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 146.0 |
| 71f467d6-5387-3c34-a2b8-4314ec74fa72 | -12.15245 | -40.87426 | 2024-09-26 00:43:00 | TERRA_M-M | RUY BARBOSA | BAHIA | Brasil | 2927200 | 29 | 33 | nan | nan | nan | Caatinga | 8.4 |
| 9eed2b04-cdf7-3f9b-803d-7be51244ce3b | -12.15073 | -40.86278 | 2024-09-26 00:43:00 | TERRA_M-M | RUY BARBOSA | BAHIA | Brasil | 2927200 | 29 | 33 | nan | nan | nan | Caatinga | 8.7 |
| 90cad361-2186-334d-bf23-2f7c7efdf572 | -11.86562 | -45.5386 | 2024-09-26 00:43:00 | TERRA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 3f32fb59-3125-307b-9054-9406d1e55186 | -11.85164 | -43.82625 | 2024-09-26 00:43:00 | TERRA_M-M | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 3af7bade-9fba-3367-95aa-477a21de72e4 | -11.85038 | -43.81726 | 2024-09-26 00:43:00 | TERRA_M-M | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 6101ce39-bc79-3008-8377-ce976b1b983e | -11.84279 | -43.82756 | 2024-09-26 00:43:00 | TERRA_M-M | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 23.5 |
| c5f617fc-4902-3b3e-90cf-78d909b912bd | -11.784 | -45.5462 | 2024-09-26 00:43:00 | TERRA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| afac0d7b-f201-3c03-a7e7-e91e0191a157 | -11.67979 | -44.51238 | 2024-09-26 00:43:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 840ec36b-0c77-38b7-9500-85758854e48c | -11.45857 | -45.72393 | 2024-09-26 00:43:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 5b85022c-6e0f-3c59-99d8-e3ac3d80c814 | -11.39776 | -46.38904 | 2024-09-26 00:43:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 17.6 |
| ec5e02fe-d1bf-367c-8082-7900e516c662 | -11.39643 | -46.37883 | 2024-09-26 00:43:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 20.7 |


[Clique aqui para ver as próximas entradas](README13.md)
