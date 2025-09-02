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

## Dados Diários - Página 31

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e9de8e28-7077-3941-a77a-ef6cca3f31ec | -6.27425 | -43.51966 | 2025-09-02 04:12:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 339f34f0-2671-3451-b64a-d58cb22291dd | -6.12371 | -43.28982 | 2025-09-02 04:12:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.8 |
| af97849d-7499-3a0e-a6f3-aa693ed9d98e | -6.41897 | -43.95649 | 2025-09-02 04:12:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 15d61f36-91a3-3875-a108-c19ab4f21f28 | -5.96481 | -42.96391 | 2025-09-02 04:12:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 0eea7b8e-e6bd-3231-a425-7dec597592a9 | -4.47727 | -48.11853 | 2025-09-02 04:12:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 020080a6-c25e-3686-aac6-3731e305a8b6 | -6.01658 | -46.01497 | 2025-09-02 04:12:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f28f057d-1e26-3014-b397-11d68e387927 | -6.51775 | -43.50476 | 2025-09-02 04:12:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f776fcd7-efe6-3032-a28e-3ac6397a295b | -6.24168 | -41.80413 | 2025-09-02 04:12:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| e11ccbdd-75dd-3081-8eaf-cc430d7cb8d0 | -6.72433 | -42.25626 | 2025-09-02 04:12:00 | NOAA-20 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 53b2371a-e43d-3cb1-be9a-c4945790ac58 | -6.19623 | -43.34767 | 2025-09-02 04:12:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3985d40d-a5a1-3179-b8d1-f750bad996b6 | -6.71602 | -42.2657 | 2025-09-02 04:12:00 | NOAA-20 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| be5af792-43bc-3363-a44b-2141bfa52547 | -6.59303 | -43.63079 | 2025-09-02 04:12:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7e7c9bf3-fd22-3098-84c8-f0061328d4fc | -6.25807 | -42.60967 | 2025-09-02 04:12:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| cbcc5956-6ffe-3fe2-9449-cdd87933e860 | -6.18773 | -44.19419 | 2025-09-02 04:12:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8323295b-64da-314b-89dd-d0d949c5f0c7 | -2.19799 | -47.99395 | 2025-09-02 04:12:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| df9059b8-9a27-3543-a319-757b3e9e66cb | -5.95986 | -44.28183 | 2025-09-02 04:12:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b512a7c2-a2d1-3c26-9fc4-5e9767ccee0f | -2.65414 | -48.79967 | 2025-09-02 04:12:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9d468761-3253-34cd-b183-9d7dae12a4cb | -2.4411 | -47.33214 | 2025-09-02 04:12:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9b613b87-7701-3a41-8cbf-aea42d3bb7f5 | -6.2859 | -43.57478 | 2025-09-02 04:12:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 81971ebd-6411-3804-be6b-bb0875ac5336 | -6.23281 | -42.42371 | 2025-09-02 04:12:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| b5775131-aa67-3107-9e38-65b9d44f8dfc | -2.74698 | -48.67634 | 2025-09-02 04:12:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 47d1afe7-9fe0-36ce-b180-0fe30fda8cb9 | -3.23079 | -47.12423 | 2025-09-02 04:12:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 27.3 |
| 147d7097-7fb3-31db-bd34-53c3eb3cd0fc | -6.70435 | -42.25299 | 2025-09-02 04:12:00 | NOAA-20 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 8ef1758a-de54-30a0-b99e-fa4be2c6bbf0 | -6.22657 | -41.81277 | 2025-09-02 04:12:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 262275ba-0712-3e12-9e62-ce16beace511 | -4.54504 | -46.68366 | 2025-09-02 04:12:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f44e8dd8-30d8-3b1a-90e9-f521250c8fe6 | -6.33735 | -43.52947 | 2025-09-02 04:12:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b17ba6ec-cdd8-374e-bf96-aeadbdabbbea | -6.26307 | -42.62112 | 2025-09-02 04:12:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 649297cc-f58f-391e-b33f-8a4b3bf807f3 | -5.20805 | -46.80265 | 2025-09-02 04:12:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f3c33974-2016-39cc-b09b-f6bd38fcc371 | -6.3313 | -43.56759 | 2025-09-02 04:12:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 01bad560-4df8-3ca6-b25d-df981b9a11b0 | -6.49941 | -44.07029 | 2025-09-02 04:12:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a452e13f-3282-3150-8941-52b983554ecf | -6.13379 | -44.12407 | 2025-09-02 04:12:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 7ca8177c-8061-3c74-8a65-e11092dfacb1 | -5.78781 | -43.84531 | 2025-09-02 04:12:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4342888d-5deb-38b1-8180-fae480e10c53 | -6.53388 | -42.95091 | 2025-09-02 04:12:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f6aeb15d-9a23-3351-a6a6-979a0b64f8b9 | -5.45407 | -42.58237 | 2025-09-02 04:12:00 | NOAA-20 | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| e14fab2d-6143-3224-8b16-99977c8307ee | -2.44107 | -47.32912 | 2025-09-02 04:12:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| dbe32b66-4b53-3fe3-81cd-fcf6aaf3438c | -4.47847 | -48.11106 | 2025-09-02 04:12:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b5c66fff-6527-3139-99b7-b4ec5d8a7fa9 | -6.19937 | -45.39494 | 2025-09-02 04:12:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 4af998c3-1fb5-342b-a0f2-f0d130d196ea | -5.78195 | -42.59163 | 2025-09-02 04:12:00 | NOAA-20 | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 8.8 |
| f1defa10-f8e3-3b4b-8957-eea756f0178e | -3.22334 | -47.12642 | 2025-09-02 04:12:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 19198994-ae35-37e1-9812-9778ed0303db | -4.47565 | -48.11729 | 2025-09-02 04:12:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 034096f2-a730-3c2e-8f3e-b3808d053fbb | -6.47698 | -43.56937 | 2025-09-02 04:12:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 153a6538-04cc-3af5-9597-d4b8ef5a2876 | -6.56601 | -43.71553 | 2025-09-02 04:12:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2c71d506-56a2-3189-9b4d-d95537ec7056 | -6.72155 | -42.25221 | 2025-09-02 04:12:00 | NOAA-20 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| f9659d33-af44-39fd-9669-a824805f1a57 | -5.51049 | -42.63374 | 2025-09-02 04:12:00 | NOAA-20 | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 6d4686e3-ba78-3d3e-943b-03b750e5f889 | -6.28088 | -43.52069 | 2025-09-02 04:12:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0cb4f872-e8cc-3198-afb2-19605e2e7a4b | -5.66348 | -43.66515 | 2025-09-02 04:12:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 95ae3648-3b81-3eae-861d-36ee89c7cd91 | -5.7825 | -42.58817 | 2025-09-02 04:12:00 | NOAA-20 | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 8.8 |
| 4c76cd8d-ed5d-3bc8-bb41-b754b085ba57 | -6.27983 | -43.57024 | 2025-09-02 04:12:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0bac8f9c-c1c0-32cd-aedb-3670f53be713 | -5.76529 | -45.21424 | 2025-09-02 04:12:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6e9f1517-5bee-3417-8029-448663c24049 | -6.53941 | -42.95887 | 2025-09-02 04:12:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5e16b036-1678-3123-9937-2d0303455e18 | -6.25476 | -42.60915 | 2025-09-02 04:12:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 97c0a0dd-8a7d-3b12-a31c-dd7913382c00 | -6.25922 | -42.62407 | 2025-09-02 04:12:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 37eda2d5-83a0-30f9-816b-8c7759e5c288 | -4.47628 | -48.11355 | 2025-09-02 04:12:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 86cfd3f0-db8f-3619-a381-8de396c5cd7c | -5.81278 | -43.8385 | 2025-09-02 04:12:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8fe52e8c-229c-3ea0-a8c3-2228c95c50ff | -3.23044 | -47.13275 | 2025-09-02 04:12:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 17.8 |
| b30eef95-1907-34d8-b3b3-85820bc1bd9c | -2.44168 | -47.32858 | 2025-09-02 04:12:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8ae4620f-d046-3ba0-9a3b-31eaa78f93ff | -6.24927 | -42.62251 | 2025-09-02 04:12:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 4094c84f-791d-3075-bf60-235d96c81faf | -5.36648 | -42.62177 | 2025-09-02 04:12:00 | NOAA-20 | DEMERVAL LOBÃO | PIAUÍ | Brasil | 2203305 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 9cf93e76-931d-3b1e-a6c3-fcbdb379a076 | -2.44233 | -49.36821 | 2025-09-02 04:12:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 2d7d2b7e-d761-3262-89ae-cad57712c4d9 | -3.23124 | -47.12767 | 2025-09-02 04:12:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 17.8 |
| b46d616e-69f2-3852-a194-10f59bf17b02 | -5.5138 | -42.63425 | 2025-09-02 04:12:00 | NOAA-20 | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| bb8b2322-20e2-38cf-84e5-4b2cbcf99bf3 | -6.25861 | -42.6062 | 2025-09-02 04:12:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 6c52e8d6-e261-3e0b-925b-2ab204aac0dc | -3.22684 | -47.12362 | 2025-09-02 04:12:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 43e65fff-63ae-3d76-9952-435036fb4226 | -4.48103 | -48.11052 | 2025-09-02 04:12:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 86bc44fd-f2fa-3414-806d-1977b967c36c | -6.24981 | -42.61904 | 2025-09-02 04:12:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| b4c3e3c6-4ea2-3373-95e0-a2504cf1fadf | -5.87208 | -43.01265 | 2025-09-02 04:12:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 7029d9ec-464c-3c22-9057-520626482508 | -5.49948 | -42.63909 | 2025-09-02 04:12:00 | NOAA-20 | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| bc9c3348-a9b6-3b21-b6d6-5b7fdb30bfdd | -10.58617 | -44.85831 | 2025-09-02 04:14:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 765f4154-0362-3df8-b58e-375f64fc528f | -11.85858 | -52.4178 | 2025-09-02 04:14:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 33b961f4-6e3e-3918-b413-d0a3e138178b | -13.33167 | -46.8464 | 2025-09-02 04:14:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 93729b49-8116-36fc-aa79-f168b7c4c610 | -7.78295 | -45.4462 | 2025-09-02 04:14:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| dc5fdd23-0480-307b-aedb-75c9de1fe9cc | -7.46733 | -44.81603 | 2025-09-02 04:14:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ab9616c0-d068-33bf-8152-409f95962cf3 | -7.70495 | -45.02055 | 2025-09-02 04:14:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5ad855e6-7bfe-34cd-912e-27ac3a092692 | -11.35604 | -43.66138 | 2025-09-02 04:14:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ab64f263-f5d2-32fe-8482-2605f6e1e031 | -13.33726 | -46.85537 | 2025-09-02 04:14:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cae927e8-1c60-3c55-b8a0-7f58907f59cb | -8.46296 | -43.61906 | 2025-09-02 04:14:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c3d353f5-c7f7-31d1-acc3-8aa5230ebe2e | -7.98285 | -44.05605 | 2025-09-02 04:14:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d60931d7-7ebc-3d6e-9a16-a6ebf622a42d | -13.69569 | -46.94032 | 2025-09-02 04:14:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 17.3 |
| 94271fe1-2831-3751-9ece-aa4619710dd2 | -9.12582 | -46.05331 | 2025-09-02 04:14:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 67e2e1a2-a10a-3738-94ea-3ee5d6e193ea | -6.82849 | -52.81416 | 2025-09-02 04:14:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a04e9a70-d02f-3ca3-842c-2c0582902773 | -11.42062 | -55.18627 | 2025-09-02 04:14:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0b0356ac-c2a7-3bde-a444-e31284e4be1e | -11.09709 | -44.63775 | 2025-09-02 04:14:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 31.0 |
| 5187ef66-f8b5-3c14-9473-99ddaa79b645 | -11.64368 | -52.04232 | 2025-09-02 04:14:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 5f8ae0fc-15d5-3ad8-b050-6c9a20bb89e0 | -6.80475 | -52.8207 | 2025-09-02 04:14:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| c64365c0-42f3-3394-abd5-44c88c8584bb | -6.79964 | -52.81458 | 2025-09-02 04:14:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 8e8d4e3c-eb91-3dae-932b-ea084ecb7d9c | -11.09821 | -44.63071 | 2025-09-02 04:14:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 27.2 |
| 7edc01df-4916-3bb8-bb78-855f0acc710c | -11.65643 | -52.18819 | 2025-09-02 04:14:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 42.0 |
| bdc74399-e43d-39d5-9667-603ab4002e9c | -6.83878 | -52.81958 | 2025-09-02 04:14:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 170a895d-e2a9-322c-9778-466511c6d6be | -13.3109 | -43.79251 | 2025-09-02 04:14:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 676b23cb-40eb-3bf6-9b1c-09000a636b88 | -13.32611 | -46.83729 | 2025-09-02 04:14:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 54a8c254-e175-3280-9dac-337b89dee8ec | -7.21903 | -44.05149 | 2025-09-02 04:14:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 207c39ef-d58d-3bec-8bc4-31554b1ec5d0 | -8.45986 | -47.36412 | 2025-09-02 04:14:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 227cd447-7868-30e0-96dc-23961965729d | -7.57913 | -45.21137 | 2025-09-02 04:14:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9855927c-70ef-3561-9272-87c29d564990 | -9.26155 | -47.12043 | 2025-09-02 04:14:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fb39c90f-7004-3c34-b2b1-bd2373612af7 | -10.26693 | -47.51991 | 2025-09-02 04:14:00 | NOAA-20 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1dd37a0a-bbc7-35a6-a2d3-d88c96d34393 | -7.38792 | -47.43948 | 2025-09-02 04:14:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c20a710d-1172-38c4-8fb1-971c85ea5105 | -7.5615 | -45.71098 | 2025-09-02 04:14:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4570299d-5d36-36a6-9506-01492fb117e9 | -7.48469 | -47.87796 | 2025-09-02 04:14:00 | NOAA-20 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| cbdbd136-0ace-379d-a1b4-d4584312a9c0 | -12.33708 | -45.67771 | 2025-09-02 04:14:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d296e7e2-104f-3ca8-b551-96dc1f4aa943 | -7.47998 | -45.36762 | 2025-09-02 04:14:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |


[Clique aqui para ver as próximas entradas](README32.md)
