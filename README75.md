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

## Dados Diários - Página 75

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ca83d13a-1d2b-35ae-ac26-c8df6e293e35 | -13.00081 | -51.12076 | 2024-10-04 04:10:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2431a6a5-6b6d-35be-ae52-2ee7cc547164 | -12.98029 | -51.1225 | 2024-10-04 04:10:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 757b567d-9a74-342c-9c7c-b4571badb5f9 | -12.97925 | -51.12803 | 2024-10-04 04:10:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| f6c5cf81-0462-30e6-93ea-8a24c827e8a6 | -13.704 | -49.85634 | 2024-10-04 04:10:00 | NOAA-21 | AMARALINA | GOIÁS | Brasil | 5200829 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c3187d5d-c2b8-3c93-aece-d3124afb1879 | -12.78574 | -50.58004 | 2024-10-04 04:10:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3b2e2803-81f1-3800-aade-92837857f90f | -16.67177 | -50.60048 | 2024-10-04 04:10:00 | NOAA-21 | AURILÂNDIA | GOIÁS | Brasil | 5202601 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 60d2fe30-194f-3a58-a4b8-139a92ec03a3 | -16.12324 | -50.44805 | 2024-10-04 04:10:00 | NOAA-21 | BURITI DE GOIÁS | GOIÁS | Brasil | 5203939 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ee65e878-7246-310e-a63b-094b9eec800e | -16.11802 | -50.45148 | 2024-10-04 04:10:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fa636484-e84c-3bc4-b7d6-3fc97340a79b | -16.11375 | -50.44992 | 2024-10-04 04:10:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0a7ed789-3cd4-31e1-a527-b1b4334d1609 | -16.11278 | -50.45502 | 2024-10-04 04:10:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 65d177d0-f53b-3c81-b642-ee0d3debb3ed | -16.11184 | -50.45996 | 2024-10-04 04:10:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c0b46df5-217e-3de3-aa1b-85f34e9913d2 | -16.10845 | -50.45375 | 2024-10-04 04:10:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 499fa962-1257-3322-9ed8-32221615fa59 | -16.10748 | -50.45885 | 2024-10-04 04:10:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ba3b2a86-b9e8-315e-b0e0-24188524997c | -16.1031 | -50.45782 | 2024-10-04 04:10:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 62b39371-5c87-3770-bc12-131267d997f8 | -16.09969 | -50.4518 | 2024-10-04 04:10:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 48b6270e-b1a3-3f98-bd3d-65d9e887c8f7 | -16.09868 | -50.45703 | 2024-10-04 04:10:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| dc38a765-adaa-31fc-a880-e01fb9c27c17 | -16.09772 | -50.46204 | 2024-10-04 04:10:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| c17573df-0175-306c-b235-bee6ef13c651 | -16.09623 | -50.44599 | 2024-10-04 04:10:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| edceab52-7d93-3575-87e2-1530861c8012 | -16.09522 | -50.45127 | 2024-10-04 04:10:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cb386c62-b07a-3e03-b0a3-6ab1a80ec58d | -16.09424 | -50.45637 | 2024-10-04 04:10:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1eb4a15b-6f2d-3892-8dd8-418d3bca628e | -16.09276 | -50.4403 | 2024-10-04 04:10:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 13.3 |
| b663f6c3-a077-32ec-a032-e05ea819683c | -16.09169 | -50.44581 | 2024-10-04 04:10:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 3133caac-f7a3-3b2f-bf41-547cec5dd145 | -16.0907 | -50.45094 | 2024-10-04 04:10:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 65f36286-5f56-3742-82f1-2620ed6f6740 | -16.08481 | -50.43726 | 2024-10-04 04:10:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f889e8a1-3539-3b13-b9a2-3285abed242c | -16.08456 | -50.43535 | 2024-10-04 04:10:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 852fb09e-b033-3e6b-b857-1619e16e10ce | -16.0803 | -50.43697 | 2024-10-04 04:10:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6d11e79c-9da8-3676-8b89-e9db5abe448f | -16.08003 | -50.43516 | 2024-10-04 04:10:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a8582273-d5f8-3112-8bba-61e29cd37854 | -9.8244 | -51.92081 | 2024-10-04 04:10:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 6586ac7c-0c54-3aea-844f-847e7a593724 | -9.8237 | -51.92447 | 2024-10-04 04:10:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| a7ca4236-162d-3e8b-a22c-e2971bba6414 | -9.82296 | -51.92039 | 2024-10-04 04:10:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 8a94a48f-4f89-3e0d-ae65-11a872c79235 | -9.8223 | -51.92405 | 2024-10-04 04:10:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 71df9cd9-a01d-3338-9292-7b7407ec8972 | -9.819 | -51.91964 | 2024-10-04 04:10:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| bc98a34c-0210-3b88-979d-dd148d866260 | -9.81831 | -51.92326 | 2024-10-04 04:10:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| af7879b1-b248-3694-a2b3-1b4dc7d40434 | -9.81755 | -51.91927 | 2024-10-04 04:10:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| b0d50719-8460-373d-a046-6a454b70581b | -9.81688 | -51.92288 | 2024-10-04 04:10:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| fadaa9e2-ed11-3055-a6d7-74ba157cffd1 | -9.77699 | -51.92569 | 2024-10-04 04:10:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 968dc47a-1690-3bda-aee3-9b59ee9ac391 | -9.77355 | -51.91396 | 2024-10-04 04:10:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 4fe2e39f-8f0a-3e40-83ea-bc079bd2152d | -9.77215 | -51.92144 | 2024-10-04 04:10:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e26d0614-0be5-35f3-8c6c-d3cd4d7ce143 | -9.77148 | -51.92505 | 2024-10-04 04:10:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4aa3a173-cba8-3eba-989f-a242c060d791 | -9.76408 | -51.93452 | 2024-10-04 04:10:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 96c3f52a-182c-3232-aef4-78e2cbe29e29 | -9.76346 | -51.93781 | 2024-10-04 04:10:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b9bf518c-22d0-3de8-9d0d-fc7a401836b6 | -9.68388 | -51.37672 | 2024-10-04 04:10:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 69bd199b-630d-3fb0-8a63-46e37e7d3eac | -9.68327 | -51.38008 | 2024-10-04 04:10:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b911b64e-2829-333e-965a-13950c296285 | -11.2197 | -43.32777 | 2024-10-04 04:10:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 608b09c8-8eee-394f-8300-947124adff24 | -11.21639 | -43.32722 | 2024-10-04 04:10:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 6a5c7c96-9e5e-3027-97c8-cfb3d6c554ac | -11.11299 | -43.33532 | 2024-10-04 04:10:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 8af0232b-7423-335c-9597-81de5a621216 | -11.10968 | -43.33478 | 2024-10-04 04:10:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| cd2b2b28-e0ed-3757-b763-679490c34d19 | -11.10911 | -43.33831 | 2024-10-04 04:10:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 3.6 |
| e7826230-15fe-3459-a490-4dbc928d87d9 | -11.28417 | -43.39276 | 2024-10-04 04:10:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ccbf9e09-3998-3530-a7ba-8ba3ca544c89 | -15.54196 | -39.07106 | 2024-10-04 04:10:00 | NOAA-21 | CANAVIEIRAS | BAHIA | Brasil | 2906303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| bfba9377-5194-3504-a4b5-5055d85b21b2 | -15.45709 | -39.16275 | 2024-10-04 04:10:00 | NOAA-21 | SANTA LUZIA | BAHIA | Brasil | 2928059 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| adfddc8e-9b9a-378d-ad83-0e06a1749aae | -16.36117 | -40.26317 | 2024-10-04 04:10:00 | NOAA-21 | JACINTO | MINAS GERAIS | Brasil | 3134707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 5fced256-f8b2-35ff-94ea-410c31fce565 | -15.25371 | -40.28167 | 2024-10-04 04:10:00 | NOAA-21 | ITAPETINGA | BAHIA | Brasil | 2916401 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 90761888-d3e5-3f2f-bcbe-4b2fb41490a5 | -17.85951 | -41.4239 | 2024-10-04 04:10:00 | NOAA-21 | TEÓFILO OTONI | MINAS GERAIS | Brasil | 3168606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| e1d9e323-d0cf-3a54-8096-a41f4e0674a7 | -17.85598 | -41.42347 | 2024-10-04 04:10:00 | NOAA-21 | TEÓFILO OTONI | MINAS GERAIS | Brasil | 3168606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 0b047cc3-9300-3255-bc02-2b182e6e101b | -17.85538 | -41.42762 | 2024-10-04 04:10:00 | NOAA-21 | TEÓFILO OTONI | MINAS GERAIS | Brasil | 3168606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 0fa4bf40-b7a1-38bc-927a-65d0bd408aae | -17.85481 | -41.43165 | 2024-10-04 04:10:00 | NOAA-21 | TEÓFILO OTONI | MINAS GERAIS | Brasil | 3168606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| b14dce71-8e16-3e5c-9221-45e25d801b65 | -17.85245 | -41.42297 | 2024-10-04 04:10:00 | NOAA-21 | TEÓFILO OTONI | MINAS GERAIS | Brasil | 3168606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| f5952a65-8e80-31ee-9e3d-458e41ea09d7 | -17.85187 | -41.42706 | 2024-10-04 04:10:00 | NOAA-21 | TEÓFILO OTONI | MINAS GERAIS | Brasil | 3168606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| a0328ab9-09d5-3220-bbf2-7265b168f9bf | -17.85129 | -41.4311 | 2024-10-04 04:10:00 | NOAA-21 | TEÓFILO OTONI | MINAS GERAIS | Brasil | 3168606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 4196b949-8ff9-36f2-9326-1e5a88f22740 | -17.60252 | -40.35631 | 2024-10-04 04:10:00 | NOAA-21 | LAJEDÃO | BAHIA | Brasil | 2918902 | 29 | 33 | nan | nan | nan | Mata Atlântica | 8.2 |
| e657425f-0cb7-3fe7-a808-cfa8570bcdc4 | -17.60188 | -40.36086 | 2024-10-04 04:10:00 | NOAA-21 | LAJEDÃO | BAHIA | Brasil | 2918902 | 29 | 33 | nan | nan | nan | Mata Atlântica | 40.4 |
| bd9e8089-3803-3d84-9038-e98cd4424aed | -17.10073 | -41.19678 | 2024-10-04 04:10:00 | NOAA-21 | NOVO ORIENTE DE MINAS | MINAS GERAIS | Brasil | 3145356 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 842678c9-092a-3aa0-b59c-df88f7149dcb | -16.89535 | -40.60711 | 2024-10-04 04:10:00 | NOAA-21 | SANTA HELENA DE MINAS | MINAS GERAIS | Brasil | 3157658 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 73562ec0-037b-3305-82a6-22e57006ed7a | -16.89475 | -40.61142 | 2024-10-04 04:10:00 | NOAA-21 | SANTA HELENA DE MINAS | MINAS GERAIS | Brasil | 3157658 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 76f5c523-bd92-3419-86af-ee2ed950b136 | -16.89413 | -40.61576 | 2024-10-04 04:10:00 | NOAA-21 | SANTA HELENA DE MINAS | MINAS GERAIS | Brasil | 3157658 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 07a675f9-315a-3981-a61a-576e93ae0eef | -18.5734 | -41.28299 | 2024-10-04 04:10:00 | NOAA-21 | ITABIRINHA | MINAS GERAIS | Brasil | 3131802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| a2d96fb7-bc97-39ef-b5ae-cb99376003b2 | -18.57277 | -41.28738 | 2024-10-04 04:10:00 | NOAA-21 | ITABIRINHA | MINAS GERAIS | Brasil | 3131802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| e84ef876-905f-3a09-896a-227188d4b3a2 | -18.57221 | -41.28523 | 2024-10-04 04:10:00 | NOAA-21 | ITABIRINHA | MINAS GERAIS | Brasil | 3131802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 6c09f8c5-d2e4-375a-853c-1fd1bf3992fe | -18.56983 | -41.28246 | 2024-10-04 04:10:00 | NOAA-21 | ITABIRINHA | MINAS GERAIS | Brasil | 3131802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 1d6c2cd0-005d-334a-9fcb-bb06bdd5a4ea | -18.50916 | -41.29952 | 2024-10-04 04:10:00 | NOAA-21 | ITABIRINHA | MINAS GERAIS | Brasil | 3131802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.8 |
| f89fde36-ba75-3668-a218-40cacb08f3fa | -18.50857 | -41.30376 | 2024-10-04 04:10:00 | NOAA-21 | ITABIRINHA | MINAS GERAIS | Brasil | 3131802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.8 |
| f20dea26-efa1-38a1-9335-ac02c5225a35 | -18.50561 | -41.29892 | 2024-10-04 04:10:00 | NOAA-21 | ITABIRINHA | MINAS GERAIS | Brasil | 3131802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.8 |
| eb819b7b-2fc5-3c14-840f-b39460b040e5 | -12.13891 | -40.89739 | 2024-10-04 04:10:00 | NOAA-21 | UTINGA | BAHIA | Brasil | 2932804 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| bce5924b-508f-38f6-85c6-881caa0b4ab6 | -13.04945 | -41.41781 | 2024-10-04 04:10:00 | NOAA-21 | MUCUGÊ | BAHIA | Brasil | 2921906 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 28703219-a513-36ce-88c9-9f86e78b7b29 | -14.77197 | -41.61561 | 2024-10-04 04:10:00 | NOAA-21 | PRESIDENTE JÂNIO QUADROS | BAHIA | Brasil | 2925709 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 56755489-745a-3b83-9ad3-7e09f9dd5a95 | -14.13666 | -41.69047 | 2024-10-04 04:10:00 | NOAA-21 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| a4c8c88b-2a3b-3c67-9b14-0e0a480ccbc4 | -13.92097 | -41.7479 | 2024-10-04 04:10:00 | NOAA-21 | DOM BASÍLIO | BAHIA | Brasil | 2910107 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 6416e010-e299-3132-8498-a83406154afe | -13.92041 | -41.75157 | 2024-10-04 04:10:00 | NOAA-21 | DOM BASÍLIO | BAHIA | Brasil | 2910107 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 7d643f9e-ce68-3e3b-9472-0b15be1cbe0b | -13.87985 | -42.01858 | 2024-10-04 04:10:00 | NOAA-21 | LIVRAMENTO DE NOSSA SENHORA | BAHIA | Brasil | 2919504 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| eef73153-e00e-315c-b924-4a906736980b | -13.87929 | -42.02222 | 2024-10-04 04:10:00 | NOAA-21 | LIVRAMENTO DE NOSSA SENHORA | BAHIA | Brasil | 2919504 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| d54ba50a-1799-3b42-878e-080e3d8aa9b5 | -13.77851 | -41.83477 | 2024-10-04 04:10:00 | NOAA-21 | DOM BASÍLIO | BAHIA | Brasil | 2910107 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 2127b7e2-0a74-3810-8cb8-64855fb23794 | -15.83341 | -41.89911 | 2024-10-04 04:10:00 | NOAA-21 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 9cdeae8e-f943-35cb-a113-a16dabb985c2 | -15.521 | -42.23621 | 2024-10-04 04:10:00 | NOAA-21 | INDAIABIRA | MINAS GERAIS | Brasil | 3130655 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3ac3ebef-915a-374c-92b4-62f9f703fb36 | -15.51764 | -42.23567 | 2024-10-04 04:10:00 | NOAA-21 | INDAIABIRA | MINAS GERAIS | Brasil | 3130655 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 94244421-8296-3580-8d4b-c68c78fcb634 | -15.43802 | -41.13953 | 2024-10-04 04:10:00 | NOAA-21 | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| d0c04f22-2b94-3298-b89e-9fe2efbbe6a2 | -15.43744 | -41.1435 | 2024-10-04 04:10:00 | NOAA-21 | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 8efbe77a-4824-3bb8-be75-3d3d96ee46c6 | -15.43396 | -41.14295 | 2024-10-04 04:10:00 | NOAA-21 | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| d0d64973-3fdc-310f-968b-95ee071e4b49 | -15.22993 | -42.16397 | 2024-10-04 04:10:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| b29d34eb-da8e-31a6-8be6-87013c3a2366 | -15.22658 | -42.16339 | 2024-10-04 04:10:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| c3048ea1-6993-3335-bc89-4a53eb1b7b5e | -17.31827 | -42.3727 | 2024-10-04 04:10:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d3056f7c-64d2-34db-adea-05860e986d73 | -17.31771 | -42.37648 | 2024-10-04 04:10:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f8994922-8f8b-3d9d-b258-69c9b32af226 | -17.38171 | -42.62868 | 2024-10-04 04:10:00 | NOAA-21 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 42500a3c-0251-30ff-8c16-aa6e3125de6b | -17.37947 | -42.62068 | 2024-10-04 04:10:00 | NOAA-21 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f425e080-38a9-303b-ad70-46e9ea04bc1d | -17.37891 | -42.62441 | 2024-10-04 04:10:00 | NOAA-21 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 6.7 |
| f37a8bfa-ec4c-376d-91b3-f792025361b4 | -17.37835 | -42.62814 | 2024-10-04 04:10:00 | NOAA-21 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 31169f29-18c7-3389-b65d-796f2682187d | -17.37611 | -42.62013 | 2024-10-04 04:10:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9a5efc23-dae5-3512-ac28-a8e84392e412 | -17.37499 | -42.62759 | 2024-10-04 04:10:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 049843c3-6b9b-3138-a9bb-7e102154f289 | -17.37219 | -42.62331 | 2024-10-04 04:10:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 9d1ef0d1-4b2d-30b7-a439-bbedb0b106dd | -17.37163 | -42.62704 | 2024-10-04 04:10:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 12.6 |


[Clique aqui para ver as próximas entradas](README76.md)
