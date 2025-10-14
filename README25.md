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

## Dados Diários - Página 25

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f1c541c5-fc04-37ee-b7e9-6b0ba213e87b | -6.29141 | -42.98675 | 2025-10-14 04:23:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 49989abc-d532-3498-8854-3d7846274078 | -5.22589 | -50.82538 | 2025-10-14 04:23:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d9f28581-e163-3f93-8f27-9d1e0a47d0ed | -6.42351 | -42.43981 | 2025-10-14 04:23:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 9.2 |
| 7b3e7ccb-d152-30c1-b611-3172e7917c6d | -4.74453 | -45.65155 | 2025-10-14 04:23:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a7563ce8-91b4-34b4-b1fc-64c7a67e57c1 | -6.67584 | -43.56923 | 2025-10-14 04:23:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 2262c377-c0fb-3f31-ab9e-b8d796e2302d | -2.87611 | -50.74041 | 2025-10-14 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d89492ad-5527-32eb-b088-29b3fdf0eb20 | -1.89713 | -51.00887 | 2025-10-14 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6c81c84d-1cce-3ec3-a248-caf37c86bde2 | -2.5366 | -47.80289 | 2025-10-14 04:23:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a526c723-c2a2-3703-b008-6e6c0e514a57 | -4.67637 | -43.14009 | 2025-10-14 04:23:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 362a6250-e9d4-39e4-9354-ae19acc03945 | -2.79673 | -48.88649 | 2025-10-14 04:23:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7cecadc5-53a0-3641-9036-bdfcbeefa30b | -4.86223 | -49.473 | 2025-10-14 04:23:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1ec0ed03-111a-3561-bf67-93ead140331d | -6.15652 | -41.77426 | 2025-10-14 04:23:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| f19e8289-e9c9-30c8-9847-6ddc686d9b36 | -5.48216 | -50.8212 | 2025-10-14 04:23:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4c4a5de6-4c1a-30a7-9e47-9e46cc173832 | -5.61985 | -47.90821 | 2025-10-14 04:23:00 | NOAA-20 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d2487220-0092-3191-85a2-380b0cab5265 | -4.38097 | -50.86659 | 2025-10-14 04:23:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bca83d6f-1c15-343d-9663-138e941c21dc | -5.21551 | -41.64783 | 2025-10-14 04:23:00 | NOAA-20 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 2b98c79c-1862-3e37-ba0c-9644c4ec6207 | -3.35579 | -51.63082 | 2025-10-14 04:23:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7caa597f-99fa-3d36-9831-c12705c209de | -6.53523 | -43.56241 | 2025-10-14 04:23:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 518f8705-350b-3e96-b09b-667a2f29f5c4 | -5.31959 | -43.42462 | 2025-10-14 04:23:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 80899271-806c-39ca-ac81-0643477cbf30 | -0.89991 | -47.55099 | 2025-10-14 04:23:00 | NOAA-20 | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 5ccc51be-546c-3fff-a9bf-1499543f95dd | -3.38287 | -50.28166 | 2025-10-14 04:23:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f54823fa-95c0-3269-b881-2ec3c5961803 | -5.98966 | -42.86777 | 2025-10-14 04:23:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 7b248762-b3da-3f86-9138-6cdd5a487697 | -5.88349 | -42.87841 | 2025-10-14 04:23:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 5b90ed26-6a78-3fa7-8c36-f920795f15f3 | -6.86714 | -43.85524 | 2025-10-14 04:23:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0077959d-135d-3943-89e5-f84a6592488e | -2.07201 | -52.00915 | 2025-10-14 04:23:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d483c052-71f7-354a-8102-c5ab709a8cde | -4.82789 | -43.21061 | 2025-10-14 04:23:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cb5963ff-7769-39d4-b202-c8c4119da0aa | -3.15777 | -49.17342 | 2025-10-14 04:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d294af35-934b-3487-b7d6-12c77fbda5de | -4.95099 | -41.71053 | 2025-10-14 04:23:00 | NOAA-20 | SIGEFREDO PACHECO | PIAUÍ | Brasil | 2210656 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| adcf1add-e245-3a1a-854b-0c6a67f12337 | -6.33132 | -44.01669 | 2025-10-14 04:23:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c5f5c234-360a-35dc-a2e6-f18f28b70782 | -5.15183 | -46.25673 | 2025-10-14 04:23:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3ffbed27-f1d1-3a7a-9aa5-471518d81ee4 | -6.12509 | -44.94623 | 2025-10-14 04:23:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 061e9778-76e1-3680-b21c-1f7684d98876 | -5.71472 | -47.42968 | 2025-10-14 04:23:00 | NOAA-20 | GOVERNADOR EDISON LOBÃO | MARANHÃO | Brasil | 2104552 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1982003a-732f-3f88-bbfa-8427644aa7e7 | -4.95367 | -45.16479 | 2025-10-14 04:23:00 | NOAA-20 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 37438dde-1836-3508-87e1-e885865ca053 | -3.13599 | -50.21376 | 2025-10-14 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8781d7c1-a780-3e05-805c-2fc495b180bc | -5.96978 | -42.29793 | 2025-10-14 04:23:00 | NOAA-20 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 5f660399-72ac-3ebd-b363-6fb6b5490b21 | -6.29188 | -43.90674 | 2025-10-14 04:23:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 3865996a-fec5-33fd-af9b-6280f10b05e4 | -5.99325 | -42.86836 | 2025-10-14 04:23:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| f5b840a0-d8c2-336d-9400-9c99661f6dab | -4.1105 | -50.05493 | 2025-10-14 04:23:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| f77c560a-bb64-3f65-8a3f-f2dcb8b22aba | -4.61803 | -49.54273 | 2025-10-14 04:23:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b823583f-ee64-3209-b114-086b52eca420 | -5.84778 | -42.32335 | 2025-10-14 04:23:00 | NOAA-20 | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 040e457b-2afe-3a8e-bfa5-2efe2412fa25 | -6.33496 | -43.38428 | 2025-10-14 04:23:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2269f2a5-6976-335d-a5d7-4f4662220c70 | -4.30312 | -50.39964 | 2025-10-14 04:23:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8b7d2d4d-5352-323d-a628-f90e5e743895 | -6.51046 | -44.01185 | 2025-10-14 04:23:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e8559549-f234-3b7e-a608-4897089719c7 | -3.13943 | -50.2178 | 2025-10-14 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7a9049d2-d30f-385a-8166-f01851eb0158 | -2.88026 | -50.74109 | 2025-10-14 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ba819204-0fd9-3934-a706-706b23eec59d | -2.87941 | -49.09359 | 2025-10-14 04:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 04ab3b7b-ba8b-37f6-b46b-c7ae7ee3a23c | -4.5005 | -46.70055 | 2025-10-14 04:23:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 590baf83-03ee-307f-91d7-690468306f4b | -6.21806 | -41.55922 | 2025-10-14 04:23:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 30c9bf7e-17f4-38af-94b6-809d51f1401e | -3.29378 | -43.50043 | 2025-10-14 04:23:00 | NOAA-20 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b664841a-a877-3168-acdd-f0b803cc3274 | -6.30244 | -43.00013 | 2025-10-14 04:23:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 89ae9811-6ff8-3f95-a94f-640a0801edaa | -3.11853 | -49.09982 | 2025-10-14 04:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 266826d4-d5a6-3682-b3d1-1b68e3d530d7 | -4.68928 | -43.12608 | 2025-10-14 04:23:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 94432c52-91c9-3ed3-98e2-b3e249742c80 | -5.22103 | -50.95622 | 2025-10-14 04:23:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 981bdb8b-6335-3820-9dc8-1b2aca92e885 | -6.295 | -42.98725 | 2025-10-14 04:23:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c43497be-d2ff-3c0d-ac2e-de7c3c14f422 | -3.93281 | -46.61421 | 2025-10-14 04:23:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 75c59360-c0f5-3a14-b414-4cd7b1e07fc9 | -2.44264 | -47.16344 | 2025-10-14 04:23:00 | NOAA-20 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 47d8dd5a-79bb-3158-886d-f0348856ecdc | -2.94885 | -49.02903 | 2025-10-14 04:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 318d6b88-ff32-3d95-af6b-8cde70956229 | -5.05088 | -49.76396 | 2025-10-14 04:23:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1f2e60ff-f912-3d0f-bf5e-8140bf6be1a7 | -3.43486 | -50.25167 | 2025-10-14 04:23:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| e10be9fd-d0f5-3627-a885-57d1ce3720c4 | -5.108 | -43.20269 | 2025-10-14 04:23:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| d24aafa3-3c29-3db6-a01a-2bacfd777a52 | -5.39513 | -51.38283 | 2025-10-14 04:23:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 18aa1fe2-7964-3647-b85d-90ad5f9333c4 | -4.00184 | -44.67051 | 2025-10-14 04:23:00 | NOAA-20 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6ba50e12-b5f9-3703-9d31-9853677c4c50 | -3.09624 | -47.02313 | 2025-10-14 04:23:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| adc91c5f-a89f-3dd5-8cc5-210c00927519 | -6.29649 | -42.99078 | 2025-10-14 04:23:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c6412660-8deb-3694-9a37-a750411e0717 | -4.05227 | -47.25032 | 2025-10-14 04:23:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a25ddc33-be91-3fb3-96ae-2b3877c24a12 | -6.43787 | -41.82777 | 2025-10-14 04:23:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 91c52b58-8ca5-3392-bd9f-c3ee68441249 | -6.45805 | -44.5771 | 2025-10-14 04:23:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5b9f4e8e-0bbd-3721-ae3d-b9659f3f2fab | -3.13999 | -50.21436 | 2025-10-14 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e2e34828-f18b-30d4-9bef-6b5e8c2b2e12 | -5.88082 | -42.88317 | 2025-10-14 04:23:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 602a56a4-aa52-3421-9d1e-c78986b0e190 | -6.2361 | -44.90928 | 2025-10-14 04:23:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0a7c31c7-cf33-323e-8002-b01cf573645b | -4.66235 | -43.13797 | 2025-10-14 04:23:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 74adbd38-32c7-3bcf-8759-9b23328fb3e5 | -5.42447 | -41.34354 | 2025-10-14 04:23:00 | NOAA-20 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 0c528755-d842-34a6-8536-7cac76754f01 | -7.14385 | -41.72025 | 2025-10-14 04:23:00 | NOAA-20 | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 35e6ea46-b3ff-3fe3-b400-388d9c5fca2d | -7.09262 | -41.96515 | 2025-10-14 04:23:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 606b5159-f095-3f94-a51a-c8c69a97af68 | -6.54036 | -43.5576 | 2025-10-14 04:23:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 138e656b-5a29-38e4-bd0e-214c8f3c15d5 | -5.56414 | -41.32153 | 2025-10-14 04:23:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 1fae79d7-4f0b-3d94-9f3c-028ffbc2424b | -5.30808 | -45.52501 | 2025-10-14 04:23:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c5461258-0c5b-3265-bc7f-a2a713a35df2 | -4.63869 | -42.53096 | 2025-10-14 04:23:00 | NOAA-20 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 3f2fbd24-f39d-3cf2-aa9d-3e49a885545a | -4.8209 | -43.20953 | 2025-10-14 04:23:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5640ea73-f619-3780-9361-86907b748d2d | -3.46951 | -51.65282 | 2025-10-14 04:23:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 36d38a23-0fee-3d82-8769-c0551ec4256f | -5.33264 | -45.19544 | 2025-10-14 04:23:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a10b4824-bfac-3012-8ff5-48ea7f726303 | -6.09183 | -46.06995 | 2025-10-14 04:23:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 258f97bf-ff02-3c77-96c1-67395cf847cc | -5.88574 | -42.91246 | 2025-10-14 04:23:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 60c04153-e5fd-379c-9e68-8a7590aff05c | -4.58402 | -45.63688 | 2025-10-14 04:23:00 | NOAA-20 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| dfc9553b-bc6b-33b6-9bf9-434c7e2257f0 | -4.78923 | -46.61308 | 2025-10-14 04:23:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| acff895d-943c-3c52-a7aa-b26b9c38a0b4 | -4.91029 | -41.54227 | 2025-10-14 04:23:00 | NOAA-20 | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 7e178507-405f-36c8-835a-13eca759bfd6 | -6.17365 | -44.28875 | 2025-10-14 04:23:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0dd6d668-326c-3478-a19b-bdfc92189308 | -4.66645 | -43.13461 | 2025-10-14 04:23:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 331f20ab-a9b6-388a-88af-daa49151bdbd | -6.16168 | -43.75574 | 2025-10-14 04:23:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4ec7a10e-d968-3230-b038-e89565ddcfa4 | -3.93496 | -42.80871 | 2025-10-14 04:23:00 | NOAA-20 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 19b550d6-f4c0-33b4-bf51-0b19acf3aa11 | -6.99546 | -41.99672 | 2025-10-14 04:23:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 6c1e9fc5-699b-35b8-9a0e-940afbfc4fba | -5.48601 | -45.4077 | 2025-10-14 04:23:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| e678dcce-978a-37c3-8f2f-c9ec74f3f0d7 | -5.40712 | -46.01796 | 2025-10-14 04:23:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 93d15c06-05ff-3d2c-a580-b96c7c6e50bd | -4.22895 | -43.012 | 2025-10-14 04:23:00 | NOAA-20 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ca9aca44-9c33-31aa-8fb3-41106e59eafe | -5.32987 | -45.19144 | 2025-10-14 04:23:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fcc4af21-9691-3508-b8c9-02a29316bd06 | -3.38802 | -50.14799 | 2025-10-14 04:23:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 37aa5640-3a1e-3a11-b382-6cdae67323f6 | -5.48947 | -45.40864 | 2025-10-14 04:23:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 2c9d03fa-6a54-3e81-ba0c-d2ae7d9f6255 | -3.16422 | -48.60533 | 2025-10-14 04:23:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 77367f79-9ee5-3659-a70a-fa1e0a1c8e30 | -5.69558 | -49.30504 | 2025-10-14 04:23:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8dea26c8-f155-3082-ab37-6d67bb288231 | -4.87217 | -48.6603 | 2025-10-14 04:23:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |


[Clique aqui para ver as próximas entradas](README26.md)
