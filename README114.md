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

## Dados Diários - Página 114

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 42caab87-38f8-317e-94af-f4c494d1319b | -12.99746 | -51.25881 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 90e34f01-3d81-3384-82d8-b5e3cad9c246 | -12.99429 | -51.31661 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 51.2 |
| 54cd4189-eb63-3154-905c-b03899428033 | -12.99427 | -51.28339 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 75ae9374-76b5-3d66-a5a9-000909dd1c56 | -12.99383 | -51.26054 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 034e3fa6-4dfd-348e-8a22-449d1f58a315 | -12.99376 | -51.32067 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 2c95af0b-8720-3628-99df-f17e8818d917 | -12.99327 | -51.26463 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ad19558d-bda6-3e2c-828f-74bebf524662 | -12.99271 | -51.26873 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 9d28f591-20a0-3e05-87f6-4662446a5dc1 | -12.99265 | -51.2623 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 22.6 |
| 53541c7b-8144-3f07-84b9-adff2aaacce2 | -12.99159 | -51.2705 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 8.3 |
| ce1d1bf0-5423-368f-a38f-6776db50b549 | -12.99106 | -51.2746 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 8.3 |
| d84ebb4b-e2e5-3f35-ab70-12d3bfba14d6 | -12.99053 | -51.27869 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1085b95f-61e7-3c9d-9c5c-46cb5a976989 | -12.99003 | -51.316 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| b18efb3c-dc40-323f-a7be-091d6f5f5b60 | -12.9895 | -51.32006 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 59.9 |
| 387ec41e-37f9-3900-b22f-0c7d16efd03d | -12.989 | -51.35717 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d9cf459c-21f7-31a1-832f-0e54c307cd2a | -12.989 | -51.26402 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d016e740-9cb9-3d2b-b5f5-a621d4094fe3 | -12.98473 | -51.26342 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| dce176ff-20f1-3f9a-8814-8286bd617e26 | -12.98433 | -51.32975 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 81a8222f-6e26-30f7-acec-df2bc2006c32 | -12.9842 | -51.32758 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 24.0 |
| a56aec1f-b2cd-3e91-b749-c8dd1dddbd50 | -12.98411 | -51.26107 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 01168186-3ee6-3192-8af1-9353c2d96f91 | -12.98367 | -51.33164 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 24.0 |
| 12031b56-70d6-3b7a-930d-7fa262a253ad | -13.80063 | -52.43926 | 2024-10-01 05:06:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1cd8a66e-3bd0-31bd-9f39-c06d9e9b2541 | -13.79873 | -52.43956 | 2024-10-01 05:06:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 078c489f-09e4-3fd0-8487-dad5f4a595f1 | -13.78865 | -52.42401 | 2024-10-01 05:06:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 272f204f-5a56-3d6f-b947-96bae4a8bb55 | -13.78817 | -52.42744 | 2024-10-01 05:06:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7871632d-9e12-363d-9646-fb8ff6998960 | -13.78465 | -52.42344 | 2024-10-01 05:06:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4387ae45-899f-391a-aa37-bbf440693234 | -13.78065 | -52.42285 | 2024-10-01 05:06:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8f9120a9-f8f4-3983-8479-eaaf7195ed42 | -13.77665 | -52.42223 | 2024-10-01 05:06:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b9271891-64de-3f74-b147-d11e38c23517 | -13.77265 | -52.42161 | 2024-10-01 05:06:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7f671489-8155-3d22-9bf0-12113dc72348 | -13.77074 | -52.43552 | 2024-10-01 05:06:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a4586e3f-f792-3329-9b25-d958c42420f3 | -13.77026 | -52.43905 | 2024-10-01 05:06:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ef914b87-5bdb-38ad-8734-cebb2ccbaca5 | -13.76819 | -52.42444 | 2024-10-01 05:06:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 926f841b-691e-385b-a1ce-717eb93a9cbd | -8.9537 | -52.80608 | 2024-10-01 05:06:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b7e33f80-3fcd-32df-8b05-2c90784fdf60 | -9.67461 | -53.16663 | 2024-10-01 05:06:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e231016c-6b95-3a67-a730-2352fec8ed8b | -9.67397 | -53.17089 | 2024-10-01 05:06:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 24bf7dd7-c1e4-34ec-9d04-258848839b5b | -9.67034 | -53.17033 | 2024-10-01 05:06:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c52821f6-9832-3fe1-89f9-e7fd20756827 | -9.65582 | -53.16814 | 2024-10-01 05:06:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 84a6225a-1c02-33ce-b145-ce3dfca40625 | -9.62906 | -53.19881 | 2024-10-01 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cdd3defd-be56-370d-9293-4ac8777dcb99 | -9.62814 | -53.40463 | 2024-10-01 05:06:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 21dbe7aa-0731-3195-a550-a195a02b22a5 | -9.62481 | -53.20253 | 2024-10-01 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b6fa99c7-8882-3baf-a7fc-94aa50bee50f | -9.62056 | -53.20622 | 2024-10-01 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b30fe240-c51a-3b82-941b-5dd9d1f12009 | -9.61995 | -53.21045 | 2024-10-01 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8464f3fb-150b-3f9c-84b8-ae05262919c7 | -9.61509 | -53.21838 | 2024-10-01 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2f909edf-1d98-3948-8bae-58325cd119b5 | -9.61447 | -53.2226 | 2024-10-01 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2d1489ea-0163-35f0-b82b-ef9d0ed34fe0 | -9.61385 | -53.22683 | 2024-10-01 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6009e216-bac5-3c15-a975-e964036e6252 | -9.60469 | -53.26429 | 2024-10-01 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b44b31e7-6f0e-3c3c-9b04-041d5fc83718 | -9.60407 | -53.26849 | 2024-10-01 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 75b80fed-b076-342b-a7d5-573bd48f0907 | -9.60346 | -53.27269 | 2024-10-01 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 972226d3-40da-3aed-8c2e-57073a54914a | -9.59984 | -53.27218 | 2024-10-01 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 67e88c9a-4e64-316e-b1e2-c38743d6d4f0 | -9.59684 | -53.26747 | 2024-10-01 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6c3797c2-dae1-3f28-a841-e5a0adc3e782 | -9.59623 | -53.27167 | 2024-10-01 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| b5484a2a-d993-3778-99a7-5fdb6a58cdc2 | -9.59262 | -53.27113 | 2024-10-01 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f0f08a5d-a311-335a-ad72-0736ddfb8175 | -9.5884 | -53.27475 | 2024-10-01 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 94402fd7-db80-32ed-a1cb-4401b6e170e1 | -9.58479 | -53.27422 | 2024-10-01 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9c52ea6b-6e21-39fd-a8e6-2c34c414cffb | -9.58418 | -53.27841 | 2024-10-01 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7fbd7b87-7949-3d11-9f3e-b435a46e2ca1 | -12.90647 | -53.88085 | 2024-10-01 05:06:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b6656e70-6b9a-3ed8-b1fe-75e42ee392eb | -12.90585 | -53.88514 | 2024-10-01 05:06:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| ffceb6db-8f88-393c-b0aa-e919485d0af7 | -12.9016 | -53.88887 | 2024-10-01 05:06:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8d0baed6-06f0-37bd-a7a9-807ee50e3b86 | -12.87286 | -54.01161 | 2024-10-01 05:06:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4fd221b7-4599-39ea-b96e-df2f6c9a5356 | -12.77547 | -53.98565 | 2024-10-01 05:06:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 60908b97-8808-3ecd-ab54-d0ca55504a98 | -12.73506 | -54.11311 | 2024-10-01 05:06:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1c23d967-0d66-30d7-b793-abf2d80f7d13 | -12.73393 | -54.01846 | 2024-10-01 05:06:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 87b15303-e1f4-3668-a52a-5c1471f57327 | -12.73093 | -54.01365 | 2024-10-01 05:06:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4408d321-c6de-32d7-b96a-94cffb79404f | -12.72969 | -54.09949 | 2024-10-01 05:06:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cb6e087a-6375-365e-ac55-f6dc150692a0 | -12.72729 | -54.11621 | 2024-10-01 05:06:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| adff18b0-035e-34f0-b81a-704a6aad8264 | -12.7261 | -54.09896 | 2024-10-01 05:06:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f6881caf-6798-31b6-85d5-fdbcc05c1d7e | -12.72431 | -54.1115 | 2024-10-01 05:06:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a03b629d-28dd-3ab6-bb08-a6af422ae6cc | -12.72371 | -54.11567 | 2024-10-01 05:06:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 46465fb8-271f-3035-b896-eb40fea3e387 | -12.71713 | -54.11043 | 2024-10-01 05:06:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 99e16929-a1ee-3fd6-90d2-0144608e7f86 | -12.71056 | -54.10518 | 2024-10-01 05:06:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f27ebb9d-eb64-3b10-a0fd-65641e3c3e52 | -12.70457 | -54.09575 | 2024-10-01 05:06:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f83f664a-c0fd-31db-bab1-c1050969e3f2 | -12.70301 | -54.09224 | 2024-10-01 05:06:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b48451df-c11b-3c1e-aaaa-3deba4590008 | -12.7024 | -54.09641 | 2024-10-01 05:06:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 276cfff1-a7c7-34d0-9f41-2957a5d99084 | -12.70098 | -54.09519 | 2024-10-01 05:06:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e77b0bdc-77d2-3a77-99a7-c1d6919b31c0 | -12.69943 | -54.09169 | 2024-10-01 05:06:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 01450ec2-c7f1-378b-bbe3-d0d118f4fb62 | -12.69584 | -54.09114 | 2024-10-01 05:06:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3b2e2cde-2ec2-349e-b1b2-516cce518eb1 | -12.68773 | -54.02114 | 2024-10-01 05:06:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 464d483f-fa11-3bb8-a578-f348d32f5b3b | -12.68569 | -54.08532 | 2024-10-01 05:06:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 506c502b-ce89-3ce4-a1ad-ff12414d6006 | -12.68509 | -54.08949 | 2024-10-01 05:06:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8fade479-134c-3e33-983d-24b84c0d9879 | -12.68036 | -54.07167 | 2024-10-01 05:06:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 842a5c06-a17f-34f1-ab27-2234a3538ae0 | -12.67914 | -54.08002 | 2024-10-01 05:06:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 23d7ff9f-0c0e-3264-879c-86d4ad32fba7 | -12.67616 | -54.07531 | 2024-10-01 05:06:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c6a25b23-7982-3b0b-95a9-d8ad7b2fc7b3 | -12.67264 | -54.04906 | 2024-10-01 05:06:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 45584010-7cbc-3a83-acc2-00b980ed79e9 | -12.67142 | -54.05746 | 2024-10-01 05:06:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 034415c1-7cf8-3e56-8862-ce3c32980821 | -12.67081 | -54.06166 | 2024-10-01 05:06:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 81e0ba3d-9058-35c3-96ed-d1534e503f3a | -12.6702 | -54.06586 | 2024-10-01 05:06:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c0b858cc-1b09-3c5a-809c-bd3fb2216a86 | -12.66959 | -54.07006 | 2024-10-01 05:06:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 6142756e-2325-39fc-8c6e-8082f4a43bd0 | -12.6666 | -54.06532 | 2024-10-01 05:06:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8099e9a8-41df-3c13-ad25-aa704ef3f19a | -12.90949 | -53.88567 | 2024-10-01 05:06:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| eb78788d-6a52-3399-b44e-9228e7e396a7 | -12.90222 | -53.88459 | 2024-10-01 05:06:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c1436572-35de-369b-a72b-a13cb75fcdde | -12.87224 | -54.01588 | 2024-10-01 05:06:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c5b807cd-b685-33d5-a7a1-befa2a5e9b56 | -12.87163 | -54.02015 | 2024-10-01 05:06:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 14ab43f9-23ee-30f4-b9eb-b7644a8a4673 | -12.77186 | -53.9851 | 2024-10-01 05:06:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 74849bb7-7635-3ced-a81e-81fc4a6d4842 | -12.75797 | -54.0048 | 2024-10-01 05:06:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 3b2f1df0-bbb6-39e0-a31c-c8183fd8fc3f | -12.73692 | -54.02325 | 2024-10-01 05:06:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ace40ab7-7281-3ca8-9fbd-88dcae33644f | -12.72909 | -54.10367 | 2024-10-01 05:06:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1adc5a9b-8c3b-3bb1-8934-68e8d33fe7e4 | -12.72789 | -54.11203 | 2024-10-01 05:06:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d6999c6d-0081-3f3a-86de-4480f880c53a | -12.72311 | -54.11984 | 2024-10-01 05:06:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 51322d7f-7cbb-3c7a-b423-b72571adcac0 | -12.72012 | -54.11514 | 2024-10-01 05:06:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1dfb2a89-a350-3b54-8401-8612426e8c06 | -12.71953 | -54.1193 | 2024-10-01 05:06:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cd551b9f-f52d-3f65-8092-a9845b102351 | -12.71355 | -54.10989 | 2024-10-01 05:06:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |


[Clique aqui para ver as próximas entradas](README115.md)
