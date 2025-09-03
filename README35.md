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

## Dados Diários - Página 35

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 83662bb7-22ba-3c1a-b132-111605d0917f | -5.80876 | -43.23462 | 2025-09-03 03:53:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 201c61a0-70e4-3128-992b-2a53c5fc36f5 | -6.94775 | -43.28309 | 2025-09-03 03:53:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 0eb08b3f-b426-39b8-9853-ae0627215537 | -7.13426 | -44.57133 | 2025-09-03 03:53:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 71530d32-ed93-3753-941f-d88c69695a80 | -6.22994 | -43.3853 | 2025-09-03 03:53:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f93d28e2-e805-3595-85a5-1290c6ebeb98 | -7.63162 | -42.64581 | 2025-09-03 03:53:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 029ac5a7-e170-3bc3-a944-612b9ee34e3c | -6.98733 | -44.34087 | 2025-09-03 03:53:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3cc0cead-d3da-3058-b81d-8ba94e811f04 | -7.69158 | -48.74407 | 2025-09-03 03:53:00 | NOAA-20 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 2e10f7d2-6118-37a1-8be6-d0119c12f59e | -7.70018 | -48.72883 | 2025-09-03 03:53:00 | NOAA-20 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 6dda391b-affc-3acd-ba0e-47d6ce23a77c | -6.89644 | -45.56901 | 2025-09-03 03:53:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 12920d36-b221-3fae-87fc-20c82e6ee893 | -5.68638 | -45.94627 | 2025-09-03 03:53:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| f74b8986-1661-31aa-b8a1-78e7d79f7064 | -8.3599 | -48.31647 | 2025-09-03 03:53:00 | NOAA-20 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| af5ba9a3-22ae-3393-ac21-713344645739 | -7.91702 | -46.43701 | 2025-09-03 03:53:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 543aea86-6506-32e3-99e6-53a4021351e6 | -6.28375 | -43.51099 | 2025-09-03 03:53:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 21f697b8-f0c3-362e-b3dc-0a15b50b5c0b | -6.08923 | -43.17548 | 2025-09-03 03:53:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 36093437-db40-325d-b30e-d66187676337 | -7.71768 | -48.72845 | 2025-09-03 03:53:00 | NOAA-20 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 4.8 |
| ac063f53-1181-3aa2-b44e-334031143843 | -6.92945 | -44.3476 | 2025-09-03 03:53:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8d04fe9a-42a4-352e-828b-ac0578c97ac8 | -6.49471 | -44.09867 | 2025-09-03 03:53:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 61eb5474-2717-3d8e-8763-573c981c5d88 | -7.01465 | -43.87749 | 2025-09-03 03:53:00 | NOAA-20 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6fb24e9d-9960-31b0-919d-254757e857f2 | -7.85942 | -46.73524 | 2025-09-03 03:53:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 98132d6b-036f-3dfc-9ffd-6fa46272c96f | -7.7126 | -48.75637 | 2025-09-03 03:53:00 | NOAA-20 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 3.0 |
| efac38d7-0e0e-360e-a285-f270ac749d18 | -8.36915 | -48.29615 | 2025-09-03 03:53:00 | NOAA-20 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7eadab40-a465-3801-9c96-1b8a48dbd8c2 | -7.00581 | -43.22203 | 2025-09-03 03:53:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 1329e553-0ff2-33b8-bc12-c3e7fc47f851 | -6.53718 | -42.9477 | 2025-09-03 03:53:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 46af95ae-ac06-3b6e-8f0c-1af5eee06157 | -7.4861 | -44.81408 | 2025-09-03 03:53:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 15af8b70-e117-3e83-acd6-687a1ff5ae0e | -6.95495 | -42.97582 | 2025-09-03 03:53:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 21b4495c-f8de-3046-a84c-56619952cc43 | -6.70205 | -44.18129 | 2025-09-03 03:53:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| d16bcbcc-6668-3685-ad5c-f16010e3ce3d | -6.7298 | -42.25338 | 2025-09-03 03:53:00 | NOAA-20 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 48e63d0a-31b4-38a4-981b-78f364dcdc11 | -6.19869 | -43.34424 | 2025-09-03 03:53:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 642b9273-d0fe-37be-a092-fa1f145b4f13 | -6.35111 | -45.65092 | 2025-09-03 03:53:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 51c9c753-ebed-3e0d-8469-fc3a57f4f3c0 | -7.24421 | -44.05336 | 2025-09-03 03:53:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 564184eb-54c7-3bb2-860e-9871877050f1 | -6.97555 | -44.35893 | 2025-09-03 03:53:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 023165ce-b618-3555-9d2a-66f4b02b7806 | -8.06757 | -45.36423 | 2025-09-03 03:53:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 8f79b342-9a80-3546-bd22-d2d7c11a2a2a | -6.26071 | -43.30085 | 2025-09-03 03:53:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 484fb1e6-e81b-35d3-8874-a427d49fd25c | -7.12244 | -43.76044 | 2025-09-03 03:53:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1fa84efe-71e7-34e6-b73c-6146ee2a8ee5 | -6.2839 | -43.58424 | 2025-09-03 03:53:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f57bb7c9-c8f8-3547-9cca-7fbc177b9f42 | -6.27742 | -44.4831 | 2025-09-03 03:53:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c21c5a06-f9ea-373d-af9b-651b02015e6a | -7.61917 | -42.65067 | 2025-09-03 03:53:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 790b00ca-131c-38d2-b6dc-dfd4769e35e1 | -8.02074 | -44.05376 | 2025-09-03 03:53:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9752bdec-55b4-36ee-be4a-5e90fe69e25a | -8.07569 | -47.61251 | 2025-09-03 03:53:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d2763ec8-c659-309b-b9f0-5001ba4573c7 | -5.61089 | -45.02278 | 2025-09-03 03:53:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| af7b7dd2-ed85-33d5-addc-4bb5d91178c5 | -5.94242 | -43.03913 | 2025-09-03 03:53:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 09b2a8fa-bac2-38a8-af50-9d9315e519d1 | -8.91408 | -45.12421 | 2025-09-03 03:53:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| aee746be-56ee-3410-bc6b-b1d8ae675bd2 | -8.02134 | -44.05023 | 2025-09-03 03:53:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 99753066-270a-301a-b348-ed83d5caa35a | -6.503 | -43.07912 | 2025-09-03 03:53:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 85436e97-e58e-351d-88d0-9c2886fc1d00 | -6.51267 | -42.19134 | 2025-09-03 03:53:00 | NOAA-20 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 51701006-75e5-3f4e-ad24-44570d1c16be | -7.62746 | -42.6474 | 2025-09-03 03:53:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 75bf2195-602b-3aab-9e95-af2284fe4fc1 | -7.50504 | -45.33735 | 2025-09-03 03:53:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a95f89b0-657d-372e-8dd6-96830df3a861 | -8.06233 | -45.36786 | 2025-09-03 03:53:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 3b8b2d51-c844-3bb3-9ad9-d45a8c9d168b | -6.51387 | -43.08662 | 2025-09-03 03:53:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f1300942-bacf-3dac-b029-437a3f4a320c | -7.88533 | -40.47285 | 2025-09-03 03:53:00 | NOAA-20 | ARARIPINA | PERNAMBUCO | Brasil | 2601102 | 26 | 33 | nan | nan | nan | Caatinga | 0.7 |
| d5d88e88-be2b-382f-9bef-108c4cf06244 | -8.45429 | -47.35146 | 2025-09-03 03:53:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 920c9324-5f90-3956-b236-6ae4d5db1424 | -7.59954 | -46.22854 | 2025-09-03 03:53:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ad785a5b-5165-38f5-a474-c418669d6cf9 | -8.08327 | -47.60434 | 2025-09-03 03:53:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 750d7af6-18a1-3cc8-b3fc-4904bf71de1d | -8.86725 | -45.82743 | 2025-09-03 03:53:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 1a70d6b9-8a65-3772-9a73-01db04a5b500 | -7.70697 | -48.7553 | 2025-09-03 03:53:00 | NOAA-20 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 6e18dd12-2842-3181-8fd7-b3e8be8cae95 | -6.77942 | -44.47128 | 2025-09-03 03:53:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 94b625ad-85e7-3315-ba7c-1dcd8b1aa54d | -6.03242 | -46.02188 | 2025-09-03 03:53:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 1c5433a7-339b-33b8-8116-f25c899b6f7a | -6.72592 | -45.1625 | 2025-09-03 03:53:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0a2b66ba-3823-3351-aa2d-a9446909a37e | -8.45115 | -47.34922 | 2025-09-03 03:53:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bb0521cf-1399-3d6b-a5fc-7c0b356bc1a1 | -6.27558 | -43.51001 | 2025-09-03 03:53:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 42c01bde-f993-30ab-8d85-cb2af752753d | -6.31341 | -44.48091 | 2025-09-03 03:53:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 31747ef7-f47e-306d-844a-8d6492326f34 | -6.7305 | -42.24913 | 2025-09-03 03:53:00 | NOAA-20 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 134b93ef-f2b9-3c9d-9bb8-dfde4d5e98c7 | -5.89236 | -43.35789 | 2025-09-03 03:53:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 1dd1ed1e-771a-3b68-92c3-7003cb3d195e | -7.79366 | -45.44206 | 2025-09-03 03:53:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ac1a4a19-9e75-338e-a611-4fd401e36bdf | -6.94379 | -43.28239 | 2025-09-03 03:53:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 71c34b52-91fc-3a51-9975-f80f5891f6fc | -6.46051 | -49.52342 | 2025-09-03 03:53:00 | NOAA-20 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 13667e27-e7d1-3096-ba11-1424c30c9efc | -7.48259 | -44.82835 | 2025-09-03 03:53:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c69c2bd5-40a3-3a51-8b1e-a44cb81c027e | -6.99628 | -43.25996 | 2025-09-03 03:53:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 11.0 |
| a8d24469-6e93-3a8e-b2f7-cb40eeb81431 | -6.73371 | -43.38832 | 2025-09-03 03:53:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 7e6abd69-a97b-37a1-85e2-f7d33540f579 | -6.35578 | -43.1159 | 2025-09-03 03:53:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ec41514f-fdb2-3ff8-adba-c020e2f4cba8 | -8.87629 | -45.82925 | 2025-09-03 03:53:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 41ea0a4a-9808-3bbe-b1ab-01d9dbdf3d39 | -9.18719 | -45.19415 | 2025-09-03 03:53:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a3e7b65b-8548-3573-a0d0-7e2e39e25535 | -6.23619 | -43.39736 | 2025-09-03 03:53:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 00576551-ab6b-3679-8bbb-52522f26561f | -8.88576 | -45.80209 | 2025-09-03 03:53:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d8987949-37da-3ec1-94e1-01daef848e00 | -6.23606 | -42.42924 | 2025-09-03 03:53:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| d8d2db30-bb97-36df-b1f2-36e339bde8b7 | -6.17669 | -43.08258 | 2025-09-03 03:53:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d25fe60b-f984-3c4e-aa01-fed627a2d600 | -6.45266 | -42.38508 | 2025-09-03 03:53:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 9580c8f0-2a12-310d-b947-8e3ae2e8529a | -6.79039 | -44.30064 | 2025-09-03 03:53:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2f5c6b9e-f76e-3edf-ab64-508b51dc82de | -6.26131 | -43.29733 | 2025-09-03 03:53:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ba423678-04e4-3bae-b208-668b59b36e58 | -6.15852 | -46.60226 | 2025-09-03 03:53:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b7b26f51-b708-30a8-b46c-8f7785709e1a | -6.25972 | -42.63519 | 2025-09-03 03:53:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 8fafdedf-c404-3fa9-8f4b-79a0f10a9ec5 | -5.76636 | -45.2983 | 2025-09-03 03:53:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 66278a26-7a91-3414-9d6e-f92c81ee8574 | -7.50196 | -45.33984 | 2025-09-03 03:53:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7424f50c-5e41-3a6c-957e-d587c7ed2428 | -9.19 | -45.20356 | 2025-09-03 03:53:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b3fa0d9d-e2ad-3920-950f-81c706563a4e | -6.28413 | -43.58504 | 2025-09-03 03:53:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8b8d6467-2d4a-34cc-a468-b805216ad228 | -7.93217 | -46.54083 | 2025-09-03 03:53:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 5a8e1c6b-56de-352e-ad45-cbf4aeb099dd | -6.34465 | -45.66066 | 2025-09-03 03:53:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 58840844-59fb-30ec-a2b3-4a96577ff1e9 | -6.93109 | -45.56064 | 2025-09-03 03:53:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b7a7f216-a273-39e4-8c33-5c544f8c4258 | -6.09322 | -43.17607 | 2025-09-03 03:53:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.6 |
| acab156d-27fa-3cc7-8b10-edaa82bfc32f | -7.92771 | -46.461 | 2025-09-03 03:53:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| bfb6da88-ccba-3cbd-9a22-064f6239cd70 | -7.9329 | -46.54556 | 2025-09-03 03:53:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 10.6 |
| bef00211-071a-3df5-a667-8db1743631f0 | -4.89947 | -43.20497 | 2025-09-03 03:53:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 280effac-c618-3b5a-96e7-bcf5d0a2ea90 | -5.44188 | -42.83952 | 2025-09-03 03:53:00 | NOAA-20 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 12566351-3335-3f40-9d5f-f43c9b8a8dfa | -5.55858 | -43.07938 | 2025-09-03 03:53:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Caatinga | 1.0 |
| cc71af58-419a-3371-8e60-a86f4c372a01 | -2.90605 | -48.29547 | 2025-09-03 03:53:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 173314a7-e76a-39a9-9bc6-026ff912797b | -5.84981 | -42.99937 | 2025-09-03 03:53:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 33b7ba16-b112-34f1-86f8-b89b32786073 | -5.79831 | -43.24117 | 2025-09-03 03:53:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 870dd58f-b0fb-305c-bc23-1810238e367f | -5.50074 | -42.62706 | 2025-09-03 03:53:00 | NOAA-20 | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| c1f31c96-f9c8-3049-a552-405593037acf | -3.79207 | -49.43764 | 2025-09-03 03:53:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| df908137-752f-3a2f-938a-d9c441776ba8 | -2.93676 | -49.45941 | 2025-09-03 03:53:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |


[Clique aqui para ver as próximas entradas](README36.md)
