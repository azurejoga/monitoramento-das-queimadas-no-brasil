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
| c1d7511c-353b-3e2b-a677-21e37c802be7 | -4.03239 | -46.77972 | 2024-12-09 04:16:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1df1b171-3125-3d81-a95e-5e4d5ca1ed50 | -3.82754 | -52.42464 | 2024-12-09 04:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6046182d-08bf-3a63-a8f6-48bf438df264 | -5.18438 | -43.93018 | 2024-12-09 04:16:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5661c049-d81d-311e-8b1c-7518b35c64f0 | -4.08935 | -46.71865 | 2024-12-09 04:16:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 6172ff01-2b73-39f0-82fd-0d52a94e1268 | -7.80988 | -46.22608 | 2024-12-09 04:18:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4d4570a9-09fa-3976-beca-8cdab22eb304 | -5.58086 | -45.20578 | 2024-12-09 04:18:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| a13d08b9-42a1-33c5-986d-e44d7e1af05e | -7.78831 | -46.27433 | 2024-12-09 04:18:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 55f5ff68-1c6a-3031-b530-7932b82580bf | -5.37602 | -45.12651 | 2024-12-09 04:18:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 36affb96-1b3e-3c95-9fdd-b2a8ad22b727 | -6.38024 | -47.37955 | 2024-12-09 04:18:00 | NOAA-20 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0b7a5bd3-a297-323f-bda0-8eeced33cd83 | -6.45407 | -47.86053 | 2024-12-09 04:18:00 | NOAA-20 | ANGICO | TOCANTINS | Brasil | 1701051 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 467a25c9-1350-3301-bdd0-0d66cdd112bd | -10.47241 | -48.28021 | 2024-12-09 04:18:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a92a97ff-cca2-39fd-baaa-131aeb604846 | -7.79932 | -46.2059 | 2024-12-09 04:18:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 53b0dacb-0f30-3658-8399-f2185046c45a | -5.37214 | -45.12948 | 2024-12-09 04:18:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4f3adc36-456f-3744-9a8b-e924e85bbc3e | -7.78773 | -46.27794 | 2024-12-09 04:18:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9579d2ad-02e3-378d-9a5c-90fa04ee5cb7 | -7.88469 | -35.14902 | 2024-12-09 04:18:00 | NOAA-20 | PAUDALHO | PERNAMBUCO | Brasil | 2610608 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 210b1303-cd7a-3390-8afc-3b266c998ae0 | -7.79595 | -46.20536 | 2024-12-09 04:18:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1dac9d09-d33c-35e3-859d-385e860bded1 | -6.96524 | -34.92428 | 2024-12-09 04:18:00 | NOAA-20 | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| d5a2396d-db3c-31b8-80d3-7d9e1fad483c | -7.08479 | -45.21207 | 2024-12-09 04:18:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3f8f78af-d867-31c4-bcb3-bd944b45c503 | -9.06627 | -36.02607 | 2024-12-09 04:18:00 | NOAA-20 | UNIÃO DOS PALMARES | ALAGOAS | Brasil | 2709301 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| fbdef9e9-5030-3135-96d0-0cc67005dd13 | -6.9698 | -34.93242 | 2024-12-09 04:18:00 | NOAA-20 | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 7d855b47-fab1-3ec9-be66-943c81f73bf7 | -7.81267 | -46.23024 | 2024-12-09 04:18:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3e3fcb69-526b-3e6c-a5c8-eadd6a11b7ef | -6.87381 | -47.24301 | 2024-12-09 04:18:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 300b3d01-7fc6-36ce-bfbd-68ab367fa9f4 | -7.98247 | -50.69432 | 2024-12-09 04:18:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f33ff0c4-b0fb-3958-9d2f-1fe2d7d5dec2 | -7.74404 | -35.26998 | 2024-12-09 04:18:00 | NOAA-20 | NAZARÉ DA MATA | PERNAMBUCO | Brasil | 2609501 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| beef49e0-d450-3f93-83d8-0a4f5648c5cd | -6.30721 | -47.33932 | 2024-12-09 04:18:00 | NOAA-20 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6548b392-6c56-362a-93b8-921615474489 | -5.42162 | -44.70977 | 2024-12-09 04:18:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4e7e5ec1-ca10-3bea-b5b6-2d7ef5b5be92 | -6.06475 | -47.38058 | 2024-12-09 04:18:00 | NOAA-20 | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f338cdb7-4596-3b88-bf5d-27c7d1bd15cf | -5.57641 | -45.21227 | 2024-12-09 04:18:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b6ddf151-3bca-380e-b047-6ea33c07509f | -7.80431 | -46.21778 | 2024-12-09 04:18:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c486fdd3-6d42-39d6-92c0-064dee4fb947 | -5.37269 | -45.12598 | 2024-12-09 04:18:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8b8f296c-7bd0-3d08-aa4e-763c306d1d99 | -7.5181 | -39.26918 | 2024-12-09 04:18:00 | NOAA-20 | JARDIM | CEARÁ | Brasil | 2307106 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 85ef67af-3156-32a1-a8ee-b653b136c9c8 | -10.36254 | -40.55408 | 2024-12-09 04:18:00 | NOAA-20 | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 572da375-afe9-380e-94a9-bdb82b5d9f13 | -7.75565 | -35.14312 | 2024-12-09 04:18:00 | NOAA-20 | TRACUNHAÉM | PERNAMBUCO | Brasil | 2615508 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 0f9719fe-45f1-37b2-a9c9-14d74d8711d2 | -7.8093 | -46.22969 | 2024-12-09 04:18:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7035f070-f652-31d6-9582-ce6f037657c4 | -10.55805 | -36.96395 | 2024-12-09 04:18:00 | NOAA-20 | JAPARATUBA | SERGIPE | Brasil | 2803302 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| ee3b46b4-d6d4-3a78-8277-e354dc639048 | -7.75001 | -35.26727 | 2024-12-09 04:18:00 | NOAA-20 | NAZARÉ DA MATA | PERNAMBUCO | Brasil | 2609501 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 6d2c94d4-2349-3a44-8922-977dbebf9d6b | -8.71504 | -49.60597 | 2024-12-09 04:18:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 97495936-9b13-374b-8fdc-9034406a7ef9 | -9.83815 | -48.56726 | 2024-12-09 04:18:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4044e4b7-aeae-386a-9186-dda868ecc925 | -5.57976 | -45.10528 | 2024-12-09 04:18:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 27db059b-c229-3f6f-85cb-78977395bff9 | -7.97825 | -50.69355 | 2024-12-09 04:18:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 73cfd494-6ffa-3f20-b747-ae432476363b | -6.97174 | -34.91809 | 2024-12-09 04:18:00 | NOAA-20 | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 6.8 |
| 9b72b582-fb38-3b27-a24c-e153bf5cd1bc | -5.57919 | -45.21629 | 2024-12-09 04:18:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 805aee7d-3ae0-36e9-b2a5-f8f5577aa3f0 | -7.88328 | -35.154 | 2024-12-09 04:18:00 | NOAA-20 | PAUDALHO | PERNAMBUCO | Brasil | 2610608 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| f6c67a5f-0d77-3a4e-986e-4193c61520be | -6.97125 | -34.92168 | 2024-12-09 04:18:00 | NOAA-20 | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 6.8 |
| 6049d488-c75a-31e6-a4a8-c094b422cbf0 | -7.51863 | -39.26537 | 2024-12-09 04:18:00 | NOAA-20 | JARDIM | CEARÁ | Brasil | 2307106 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| cbe3b7fb-e9b0-369f-97cc-e9f7ae2adda5 | -7.88885 | -35.15456 | 2024-12-09 04:18:00 | NOAA-20 | PAUDALHO | PERNAMBUCO | Brasil | 2610608 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 56dedd4c-385a-374b-8624-1a294bccf435 | -8.75098 | -36.18944 | 2024-12-09 04:18:00 | NOAA-20 | JUREMA | PERNAMBUCO | Brasil | 2608404 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| c33c677e-fd39-3ef3-a3e3-bf7f1add82fa | -7.18087 | -45.44231 | 2024-12-09 04:18:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3e29cacf-5fb9-364c-87b8-2be47b604072 | -7.8071 | -46.22192 | 2024-12-09 04:18:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 73460438-8e03-3f2e-a7ee-67159dcf79d8 | -5.57974 | -45.21279 | 2024-12-09 04:18:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 798f0533-71d8-3f88-a4ab-5448d1519e76 | -6.0941 | -45.67777 | 2024-12-09 04:18:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| fcfabcbb-e8f0-3d0f-aed0-badb78050b24 | -10.50818 | -42.42807 | 2024-12-09 04:18:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 34018983-2697-3433-b61f-e731171afe02 | -7.59437 | -46.6293 | 2024-12-09 04:18:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ea249235-d131-334c-a0ee-e78878da0bdb | -7.75045 | -35.14215 | 2024-12-09 04:18:00 | NOAA-20 | TRACUNHAÉM | PERNAMBUCO | Brasil | 2615508 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 5ad43a34-7323-300a-8777-571b0983ebab | -6.9758 | -34.92992 | 2024-12-09 04:18:00 | NOAA-20 | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 6b06123b-cd9e-3128-886a-dc3d187f8046 | -7.59316 | -46.63671 | 2024-12-09 04:18:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 588a2c06-1261-30c5-9555-766236a3e8ff | -7.79654 | -46.20173 | 2024-12-09 04:18:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 398816ca-91d2-3906-9123-736cb8cc97da | -7.75611 | -35.13956 | 2024-12-09 04:18:00 | NOAA-20 | TRACUNHAÉM | PERNAMBUCO | Brasil | 2615508 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 0a373d60-54db-39cf-b967-ed52e80bf2d9 | -8.52799 | -39.44332 | 2024-12-09 04:18:00 | NOAA-20 | CABROBÓ | PERNAMBUCO | Brasil | 2603009 | 26 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 32ab8f66-839e-3ab8-814d-2588b095b094 | -10.00865 | -48.06177 | 2024-12-09 04:18:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e5907710-9c46-3233-a407-7af50b04d21b | -5.61373 | -43.46263 | 2024-12-09 04:18:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0b29a179-71d1-3a12-9fa2-0ab40c86162c | -5.61652 | -43.46664 | 2024-12-09 04:18:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b8bb0e54-8bb2-36c4-af67-90877f1b6a66 | -6.96573 | -34.92067 | 2024-12-09 04:18:00 | NOAA-20 | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 6.8 |
| afc3cea8-1758-329d-87bb-f0c201dc2bdf | -9.97953 | -36.47915 | 2024-12-09 04:18:00 | NOAA-20 | SÃO SEBASTIÃO | ALAGOAS | Brasil | 2708808 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 74c6a8e2-faad-3427-96ef-0df918bc724d | -5.8618 | -45.36168 | 2024-12-09 04:18:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 5a8c3dd9-1b89-3f12-92eb-5aeda3bb7b24 | -5.5803 | -45.20929 | 2024-12-09 04:18:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| f19a4273-c7e4-318f-85f2-51b17e8fcbd3 | -7.88418 | -35.15271 | 2024-12-09 04:18:00 | NOAA-20 | PAUDALHO | PERNAMBUCO | Brasil | 2610608 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 0be774a5-48e4-307f-943a-307a9332bc7b | -7.59377 | -46.633 | 2024-12-09 04:18:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 53691db9-9239-3fe6-a7fa-35dc21f71908 | -8.71586 | -49.60304 | 2024-12-09 04:18:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2333c70e-f7a0-37d4-93ae-1506282c2096 | -7.88933 | -35.15089 | 2024-12-09 04:18:00 | NOAA-20 | PAUDALHO | PERNAMBUCO | Brasil | 2610608 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| a3e845ca-c7f0-3c7c-866b-a54d9bbf83a6 | -6.09187 | -45.67015 | 2024-12-09 04:18:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b360f4be-df12-3aae-9e2d-69a07f0d79cc | -8.09157 | -46.03938 | 2024-12-09 04:18:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 39c8ec5b-77f3-3231-939b-bc1bf7dab35e | -9.64421 | -49.14934 | 2024-12-09 04:18:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c10f1bf2-2c7b-348e-a3de-4174834e7f13 | -7.75597 | -35.143 | 2024-12-09 04:18:00 | NOAA-20 | TRACUNHAÉM | PERNAMBUCO | Brasil | 2615508 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 314982c9-d49d-3050-8d92-f02127d6b8ab | -7.81931 | -47.0616 | 2024-12-09 04:18:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 980da352-99e4-3c03-97f9-6e13fb91db6d | -5.86457 | -45.36574 | 2024-12-09 04:18:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a66db690-bc5f-3e3b-a90b-5449ae26f81f | -5.33171 | -44.13716 | 2024-12-09 04:18:00 | NOAA-20 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b8148e3a-3387-3d1f-97a4-a4e67eff5813 | -6.98621 | -47.08801 | 2024-12-09 04:18:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 60e6aa05-28be-37d7-981d-f5a28b819fad | -7.80594 | -46.22914 | 2024-12-09 04:18:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 043014e1-da3b-312d-9a14-a9d66fdcf636 | -7.7451 | -35.26682 | 2024-12-09 04:18:00 | NOAA-20 | NAZARÉ DA MATA | PERNAMBUCO | Brasil | 2609501 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 296a4a9d-cd6e-373f-ad23-6d39a6323cc3 | -6.83477 | -44.38438 | 2024-12-09 04:18:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 59777846-06d1-3282-bf20-dceb363b3933 | -7.74952 | -35.27079 | 2024-12-09 04:18:00 | NOAA-20 | NAZARÉ DA MATA | PERNAMBUCO | Brasil | 2609501 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 07bf3073-59fd-309c-8736-07a0599fec55 | -5.58308 | -45.1058 | 2024-12-09 04:18:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 33781b5b-52f5-37ca-b50e-96dcdb6bcd73 | -9.98401 | -48.49995 | 2024-12-09 04:18:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ad2781eb-0e48-39e8-9b1f-1affbfedb894 | -8.78768 | -48.7506 | 2024-12-09 04:18:00 | NOAA-20 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 22ebaa16-8386-3c09-8ec3-92079e03663b | -5.86124 | -45.36521 | 2024-12-09 04:18:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 02b53a04-81ff-36fe-9b80-3db6e32194ef | -5.61319 | -43.46614 | 2024-12-09 04:18:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 90f7f5d8-b184-362e-9fd3-4a35cce140e1 | -6.30655 | -47.34334 | 2024-12-09 04:18:00 | NOAA-20 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1bb62dfd-fa5c-3361-bb46-69f89517bb87 | -7.82276 | -47.06218 | 2024-12-09 04:18:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5384e7e4-7825-38b1-a08c-98ac0b183321 | -6.83146 | -44.38387 | 2024-12-09 04:18:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 5a909db3-190f-3166-ad88-26544b559ead | -7.98313 | -50.69035 | 2024-12-09 04:18:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 49535fe2-7f0d-3042-93b8-69407adfd7a1 | -6.31905 | -47.37855 | 2024-12-09 04:18:00 | NOAA-20 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3a3dffac-f2b7-3717-8fc3-ceb03eeb62ab | -9.06673 | -36.02254 | 2024-12-09 04:18:00 | NOAA-20 | UNIÃO DOS PALMARES | ALAGOAS | Brasil | 2709301 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 17b24677-593c-30c2-812b-8cdf785c5aea | -5.42493 | -44.7103 | 2024-12-09 04:18:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e704f841-0423-38c3-bd3b-662b15be94be | -6.97532 | -34.93348 | 2024-12-09 04:18:00 | NOAA-20 | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| c1f3055f-6f0a-36dd-bb18-cc24db4bc328 | -7.88376 | -35.1503 | 2024-12-09 04:18:00 | NOAA-20 | PAUDALHO | PERNAMBUCO | Brasil | 2610608 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 4aca5fc4-ae3c-3380-aff9-5a1393057ff3 | -8.1513 | -49.14648 | 2024-12-09 04:18:00 | NOAA-20 | JUARINA | TOCANTINS | Brasil | 1711803 | 17 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 94158353-c2c8-35ad-9564-4d49a2d55102 | -7.81046 | -46.22248 | 2024-12-09 04:18:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 05a0d37d-e8ec-3393-ad17-78a1bd7cbddc | -8.01112 | -45.79782 | 2024-12-09 04:18:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 86568289-4f0d-3ce5-a969-0d6b93cc2b35 | -8.15415 | -49.14428 | 2024-12-09 04:18:00 | NOAA-20 | JUARINA | TOCANTINS | Brasil | 1711803 | 17 | 33 | nan | nan | nan | Amazônia | 1.8 |


[Clique aqui para ver as próximas entradas](README10.md)
