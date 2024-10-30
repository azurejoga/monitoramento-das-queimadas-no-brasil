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

## Dados Diários - Página 33

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 47eb8927-84ba-3610-942d-6e704d318280 | -6.15453 | -41.8727 | 2024-10-30 04:19:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| b0d96301-a146-35fe-ac4c-5046df3c3fde | -6.1516 | -41.86827 | 2024-10-30 04:19:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| e14777b6-6255-3268-80fb-a024e58daee5 | -6.14929 | -41.85979 | 2024-10-30 04:19:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 8699f55c-7ff0-30e7-86ee-eae7b1f1248a | -6.14868 | -41.86379 | 2024-10-30 04:19:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 3d7dc158-32fb-3c3f-af90-c4d35c7a24b5 | -6.14576 | -41.85923 | 2024-10-30 04:19:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 9828ec9d-8141-3c8a-905a-50719c20215d | -7.36159 | -41.93787 | 2024-10-30 04:19:00 | NOAA-21 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 45f53379-9370-31a1-89d2-90ebddddffd2 | -7.36097 | -41.94196 | 2024-10-30 04:19:00 | NOAA-21 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 1f1a98dd-df24-3866-9b03-bd1f39836883 | -7.33345 | -41.85867 | 2024-10-30 04:19:00 | NOAA-21 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 721f640a-f9e0-3256-a84a-41c34aafc1ee | -7.33283 | -41.86275 | 2024-10-30 04:19:00 | NOAA-21 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| fed4859b-8b12-3f9c-befa-2879583b4b3e | -7.33222 | -41.86681 | 2024-10-30 04:19:00 | NOAA-21 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| b4502288-54c6-3159-9130-e580b5019c20 | -7.32926 | -41.86222 | 2024-10-30 04:19:00 | NOAA-21 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 8614396e-8bdf-3776-9489-fff84e69859d | -7.32865 | -41.86627 | 2024-10-30 04:19:00 | NOAA-21 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| a1daef3e-0928-3ad4-a8c8-f8ee685edfe8 | -7.32805 | -41.87032 | 2024-10-30 04:19:00 | NOAA-21 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 02cab94d-5103-3e78-bb5e-4b6a6c52b601 | -7.91371 | -43.18816 | 2024-10-30 04:19:00 | NOAA-21 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| f149fbc0-d5f2-322f-9d56-fcd6630cbfcf | -7.32683 | -41.8784 | 2024-10-30 04:19:00 | NOAA-21 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| dd0f85fa-9662-3f8c-8bb0-9e766da6a5b8 | -7.32387 | -41.87386 | 2024-10-30 04:19:00 | NOAA-21 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| e813c4f7-2f3a-3cc8-9ebb-9c6cddd91784 | -7.32252 | -42.19404 | 2024-10-30 04:19:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 6daee991-c9b8-31b8-8b13-c7a15cd50b19 | -7.32022 | -42.18555 | 2024-10-30 04:19:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| a28d5010-cfd7-3d2b-bec5-7139c37b27fc | -7.31969 | -41.87741 | 2024-10-30 04:19:00 | NOAA-21 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| da6a4518-1d9f-3d73-a0df-aefccb2fab4b | -7.31901 | -42.19351 | 2024-10-30 04:19:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 7d4c6aff-0f97-30b3-99e8-4322ad70164f | -7.31671 | -42.18502 | 2024-10-30 04:19:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| b4ef9824-99cf-34ff-bfa5-d437bf9653ea | -7.3161 | -42.18901 | 2024-10-30 04:19:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 548ff536-74da-305c-8fad-ee533905973f | -7.04961 | -41.37947 | 2024-10-30 04:19:00 | NOAA-21 | SUSSUAPARA | PIAUÍ | Brasil | 2210938 | 22 | 33 | nan | nan | nan | Caatinga | 6.1 |
| e9eab80e-4553-3bf5-b156-4221f371a7c5 | -7.04596 | -41.37891 | 2024-10-30 04:19:00 | NOAA-21 | SUSSUAPARA | PIAUÍ | Brasil | 2210938 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 880dc282-e8d7-30ed-bdec-ac1388866ace | -7.0066 | -41.29177 | 2024-10-30 04:19:00 | NOAA-21 | SANTO ANTÔNIO DE LISBOA | PIAUÍ | Brasil | 2209401 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 7674ee2f-6618-3d76-a3ac-9fd76c67baee | -6.99029 | -41.35043 | 2024-10-30 04:19:00 | NOAA-21 | SUSSUAPARA | PIAUÍ | Brasil | 2210938 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| bb3fd510-c5e9-3cff-8cdc-827a98a5ea71 | -6.98728 | -41.34559 | 2024-10-30 04:19:00 | NOAA-21 | BOCAINA | PIAUÍ | Brasil | 2201804 | 22 | 33 | nan | nan | nan | Caatinga | 6.4 |
| 38fa3768-7a20-367c-a378-475b4836e20a | -6.98681 | -41.32381 | 2024-10-30 04:19:00 | NOAA-21 | BOCAINA | PIAUÍ | Brasil | 2201804 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 8b60bac9-fbca-3231-b13d-6fbdb3364b20 | -6.98253 | -41.32747 | 2024-10-30 04:19:00 | NOAA-21 | BOCAINA | PIAUÍ | Brasil | 2201804 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| addf950e-2676-308c-964e-8e074af6c1a8 | -6.98189 | -41.3317 | 2024-10-30 04:19:00 | NOAA-21 | BOCAINA | PIAUÍ | Brasil | 2201804 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 06c69916-e1c5-349c-abef-b3dc34fd879b | -6.92581 | -41.33201 | 2024-10-30 04:19:00 | NOAA-21 | BOCAINA | PIAUÍ | Brasil | 2201804 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 79141763-4856-3ad4-890b-56e031bb18ee | -6.92534 | -41.33336 | 2024-10-30 04:19:00 | NOAA-21 | BOCAINA | PIAUÍ | Brasil | 2201804 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 7ee57804-6845-31f7-adfa-b89276297c98 | -6.60073 | -41.38019 | 2024-10-30 04:19:00 | NOAA-21 | SÃO JOÃO DA CANABRAVA | PIAUÍ | Brasil | 2209856 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 32422fad-d358-39ff-9096-0785c3f21ca7 | -6.59477 | -42.00167 | 2024-10-30 04:19:00 | NOAA-21 | NOVO ORIENTE DO PIAUÍ | PIAUÍ | Brasil | 2206902 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 477a651f-914b-36c9-a510-5476adc2b471 | -6.53852 | -41.56395 | 2024-10-30 04:19:00 | NOAA-21 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 48b8d57f-0e0f-336f-aea4-e1a1a5472cb7 | -6.5379 | -41.56805 | 2024-10-30 04:19:00 | NOAA-21 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| bd314606-0438-31c1-8094-2509951cfdbf | -6.53493 | -41.5634 | 2024-10-30 04:19:00 | NOAA-21 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 4f0b214a-fb2b-3d58-81a1-9cddfc32f88c | -6.53431 | -41.5675 | 2024-10-30 04:19:00 | NOAA-21 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| c69a4334-d892-3f53-8b36-a7778832e461 | -6.53368 | -41.57161 | 2024-10-30 04:19:00 | NOAA-21 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| a4560fa9-1360-3576-bf04-1f80dabc8ca7 | -6.53197 | -41.55872 | 2024-10-30 04:19:00 | NOAA-21 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| d3a8d0c5-10ad-3fe6-afce-3c258e6017a9 | -6.53134 | -41.56285 | 2024-10-30 04:19:00 | NOAA-21 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| d98a1fc3-f817-34e2-975e-e2e1640d2ef2 | -6.50569 | -41.87434 | 2024-10-30 04:19:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 242cb0af-0b72-36f1-8028-e580656ae3ed | -6.50106 | -41.85727 | 2024-10-30 04:19:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 5e8e2dee-a594-3b22-b4a7-83caa6ce647c | -8.14654 | -41.98448 | 2024-10-30 04:19:00 | NOAA-21 | NOVA SANTA RITA | PIAUÍ | Brasil | 2207959 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| dbf08c35-3f37-3bc3-b151-652896c7a0b9 | -3.55293 | -41.42809 | 2024-10-30 04:19:00 | NOAA-21 | COCAL DOS ALVES | PIAUÍ | Brasil | 2202729 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 168f0a48-1505-3111-8984-b80ce330a9b6 | -3.46598 | -41.99772 | 2024-10-30 04:19:00 | NOAA-21 | MURICI DOS PORTELAS | PIAUÍ | Brasil | 2206696 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 0f75e67b-9d7d-3fb1-974a-7cfdb2bb76c5 | -3.46256 | -41.99719 | 2024-10-30 04:19:00 | NOAA-21 | MURICI DOS PORTELAS | PIAUÍ | Brasil | 2206696 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| e46fd13c-0ec7-3a3b-b81b-143e2ec374b2 | -3.4506 | -42.00671 | 2024-10-30 04:19:00 | NOAA-21 | MURICI DOS PORTELAS | PIAUÍ | Brasil | 2206696 | 22 | 33 | nan | nan | nan | Caatinga | 14.1 |
| a4486a07-3ec8-386a-aaf0-0cc58417924d | -3.45044 | -42.00653 | 2024-10-30 04:19:00 | NOAA-21 | MURICI DOS PORTELAS | PIAUÍ | Brasil | 2206696 | 22 | 33 | nan | nan | nan | Caatinga | 8.1 |
| f0a515f7-2215-3b29-8513-da5b86d6a6f8 | -3.44702 | -42.006 | 2024-10-30 04:19:00 | NOAA-21 | MURICI DOS PORTELAS | PIAUÍ | Brasil | 2206696 | 22 | 33 | nan | nan | nan | Caatinga | 8.1 |
| e606831b-3896-3a4b-abed-02431a1f1fbe | -3.44129 | -42.02024 | 2024-10-30 04:19:00 | NOAA-21 | MURICI DOS PORTELAS | PIAUÍ | Brasil | 2206696 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| f66a7dd7-7227-365b-aada-d45dd3f36993 | -3.40638 | -41.63059 | 2024-10-30 04:19:00 | NOAA-21 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| b89054ae-96da-30f3-af18-c364e8807a35 | -3.39945 | -41.62948 | 2024-10-30 04:19:00 | NOAA-21 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| b7ecba94-d371-3921-8f5f-e00a6e0d77b6 | -3.39701 | -41.63001 | 2024-10-30 04:19:00 | NOAA-21 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 2c7dd578-6bc6-34a5-83e7-668cd2e449d7 | -3.32931 | -42.13479 | 2024-10-30 04:19:00 | NOAA-21 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 0a886487-f051-3d48-ad09-03c989920620 | -3.2196 | -42.69621 | 2024-10-30 04:19:00 | NOAA-21 | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b2429223-6e50-30c5-8d08-4ce965d796ce | -4.8589 | -42.47549 | 2024-10-30 04:19:00 | NOAA-21 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| d0cbe984-66a2-3bec-9d58-2170bb0e891c | -4.8555 | -42.47496 | 2024-10-30 04:19:00 | NOAA-21 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| b7dcc9a0-6da7-38d8-99cf-68b0d60fd651 | -4.85493 | -42.47864 | 2024-10-30 04:19:00 | NOAA-21 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 2df7daaf-a427-38b9-81e5-9c6b1db55072 | -4.8521 | -42.47443 | 2024-10-30 04:19:00 | NOAA-21 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 4a9a6707-28b8-32b6-9446-ed2ddadfe674 | -4.85153 | -42.47812 | 2024-10-30 04:19:00 | NOAA-21 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 48a825ff-528e-3108-853d-e59b7dcc5daf | -4.93945 | -43.18305 | 2024-10-30 04:19:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 74dff249-d536-3527-ba0f-70a1a11f5781 | -4.93891 | -43.18658 | 2024-10-30 04:19:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 30cf137f-f7c8-36d7-84d3-57afd05fbabc | -4.93557 | -43.18606 | 2024-10-30 04:19:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 825c0f07-8e89-31f5-944f-02c1a7c457bb | -4.93223 | -43.18554 | 2024-10-30 04:19:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 27855d7b-f7f1-3de4-a80d-35c29dd46408 | -4.93168 | -43.18908 | 2024-10-30 04:19:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c703f05d-2099-34a8-869e-846cbf8022fe | -4.93114 | -43.1926 | 2024-10-30 04:19:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ebb43e79-dcc1-3450-85ba-b11836c23902 | -4.87018 | -42.62665 | 2024-10-30 04:19:00 | NOAA-21 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 679f5e50-6705-3184-a54f-c3f0c258fb91 | -4.86962 | -42.63026 | 2024-10-30 04:19:00 | NOAA-21 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e7393189-e1af-38e7-b7d4-ba1a21fabbaf | -4.86623 | -42.62975 | 2024-10-30 04:19:00 | NOAA-21 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 84a7377f-0525-3e3c-9597-6e4c071a2773 | -4.86567 | -42.63335 | 2024-10-30 04:19:00 | NOAA-21 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b13c008d-f4c3-3b0d-86c1-8966b7ea86ba | -4.85212 | -42.63134 | 2024-10-30 04:19:00 | NOAA-21 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| fb9c4285-bed1-3d46-a794-9279648145a4 | -4.8493 | -42.62717 | 2024-10-30 04:19:00 | NOAA-21 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9921080d-f3b3-3097-9b73-61c2f2eddfae | -4.79492 | -42.8219 | 2024-10-30 04:19:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 53e3b74f-9d0d-370a-b92e-34c616c9bb95 | -4.79156 | -42.82137 | 2024-10-30 04:19:00 | NOAA-21 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 71551ae7-aa46-3598-b9d8-77035633583b | -3.96322 | -42.32463 | 2024-10-30 04:19:00 | NOAA-21 | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 03357570-9c42-340b-a959-551ff5502cb1 | -3.94389 | -41.49709 | 2024-10-30 04:19:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 71c76b7a-b48f-37f5-ad88-c1223c472791 | -3.94328 | -41.501 | 2024-10-30 04:19:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 2cb82f04-9afb-3c64-853a-592d780d9d96 | -3.94039 | -41.49656 | 2024-10-30 04:19:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 63939deb-c378-3a44-8663-d8ef9a3e42db | -3.93978 | -41.50047 | 2024-10-30 04:19:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| e3dc2ea4-a7a7-3563-ba55-66b22bd3eb5c | -3.93917 | -41.50437 | 2024-10-30 04:19:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 9e1c7ad6-56fa-30e3-937d-7a480db38b3a | -3.93869 | -41.48431 | 2024-10-30 04:19:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 6eb55a73-da34-3096-878e-58ef7283c6f0 | -3.93809 | -41.48822 | 2024-10-30 04:19:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 7.0 |
| 10ce3d8f-c572-3aff-be52-3a8cbd053408 | -3.93749 | -41.49212 | 2024-10-30 04:19:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 7.0 |
| 937c273b-016f-3596-81fc-4b1ec86d5156 | -3.93688 | -41.49603 | 2024-10-30 04:19:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| d66b2cea-6b90-3f34-b06b-206abb7fec9d | -3.93628 | -41.49993 | 2024-10-30 04:19:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| ddbb7a8a-75ab-3fbf-97d4-2f3c78b9035f | -3.93519 | -41.48378 | 2024-10-30 04:19:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 04225d6c-46c8-3989-b13f-f84789106fec | -3.93458 | -41.48767 | 2024-10-30 04:19:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 7.0 |
| 704b7086-a6ae-3c0c-bfd0-0d361e4a1353 | -3.93398 | -41.49158 | 2024-10-30 04:19:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 7.0 |
| ca83c4f1-41a4-346b-83d6-7510985dc77b | -3.7967 | -41.60617 | 2024-10-30 04:19:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| c9a67687-8644-3204-b479-274d1125a5c1 | -3.79321 | -41.60565 | 2024-10-30 04:19:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| a408bf7e-05a8-3ece-84ad-50ea2f5c63b2 | -3.78914 | -41.60898 | 2024-10-30 04:19:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 1cd51163-e321-3a16-b238-b80259960b4c | -3.78565 | -41.60846 | 2024-10-30 04:19:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 1cf02f19-4b1b-389e-8aeb-b18c461e2e50 | -3.78217 | -41.60793 | 2024-10-30 04:19:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| c267609b-76ed-381a-9127-f0c43b0be5d9 | -4.52719 | -42.05736 | 2024-10-30 04:19:00 | NOAA-21 | BOQUEIRÃO DO PIAUÍ | PIAUÍ | Brasil | 2201945 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| d770ef24-61ef-3b6d-bb33-68556250b605 | -5.95559 | -42.98793 | 2024-10-30 04:19:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 8e6928bc-4265-3c9a-b9bc-94f9ea979353 | -5.92868 | -42.86176 | 2024-10-30 04:19:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 0b046582-db13-3163-9e0b-dd0a28f40632 | -5.91048 | -42.41225 | 2024-10-30 04:19:00 | NOAA-21 | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| b6f7e206-04c3-393c-8212-7d646a26d143 | -5.88916 | -42.84829 | 2024-10-30 04:19:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 87a2649c-85ea-3089-94f0-18930504e69a | -5.84636 | -42.51042 | 2024-10-30 04:19:00 | NOAA-21 | BARRO DURO | PIAUÍ | Brasil | 2201408 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |


[Clique aqui para ver as próximas entradas](README34.md)
