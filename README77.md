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

## Dados Diários - Página 77

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| acde59d7-33df-30a8-9e6c-294353131709 | -18.05881 | -42.63128 | 2024-10-04 04:10:00 | NOAA-21 | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 1ae1309a-dbd1-35d0-8305-1d59e0a402c7 | -18.04274 | -42.61388 | 2024-10-04 04:10:00 | NOAA-21 | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| cd077079-0e4b-396a-9686-54ee1f61d64f | -18.03936 | -42.61335 | 2024-10-04 04:10:00 | NOAA-21 | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 9bcc608e-8986-376c-8b7c-998b48a2ed61 | -18.29342 | -42.55912 | 2024-10-04 04:10:00 | NOAA-21 | SÃO PEDRO DO SUAÇUÍ | MINAS GERAIS | Brasil | 3164100 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 6815873b-ce0d-3b09-86f9-8bd7c63dffee | -11.56307 | -42.18333 | 2024-10-04 04:10:00 | NOAA-21 | IBIPEBA | BAHIA | Brasil | 2912400 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| cba36438-ebba-34a2-8bc9-2d706a58d1bb | -11.52512 | -41.79088 | 2024-10-04 04:10:00 | NOAA-21 | LAPÃO | BAHIA | Brasil | 2919157 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 26c6a712-5ab2-3f49-8d59-286e9644e52f | -11.24238 | -41.64064 | 2024-10-04 04:10:00 | NOAA-21 | JOÃO DOURADO | BAHIA | Brasil | 2918357 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| cb362cdf-e14f-37f1-9155-f8a9852fbad7 | -12.68614 | -43.11751 | 2024-10-04 04:10:00 | NOAA-21 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| bc452c1b-53cb-3631-8610-70c61a0287e4 | -12.68284 | -43.11698 | 2024-10-04 04:10:00 | NOAA-21 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 14d342ab-c0a6-3eca-bbee-985a1b04db50 | -13.30111 | -42.31297 | 2024-10-04 04:10:00 | NOAA-21 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 190f8ffa-40a1-35ed-91d3-adb9b160108f | -13.29834 | -42.30889 | 2024-10-04 04:10:00 | NOAA-21 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| a64a81e1-56e8-30d9-bc1e-2d0e0fa82dd6 | -13.29779 | -42.31244 | 2024-10-04 04:10:00 | NOAA-21 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 930d334d-4f48-3348-9c48-52a195e33d1d | -14.56356 | -43.57635 | 2024-10-04 04:10:00 | NOAA-21 | IUIU | BAHIA | Brasil | 2917334 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a5af44cb-6752-3648-9cad-7c22753cffcc | -14.32999 | -42.34143 | 2024-10-04 04:10:00 | NOAA-21 | IBIASSUCÊ | BAHIA | Brasil | 2912004 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 5cc264e7-b336-392f-8ac7-3521957defd8 | -14.32944 | -42.34505 | 2024-10-04 04:10:00 | NOAA-21 | IBIASSUCÊ | BAHIA | Brasil | 2912004 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 5db481df-c0b6-39ac-aa43-56557f0212a6 | -14.32611 | -42.34449 | 2024-10-04 04:10:00 | NOAA-21 | IBIASSUCÊ | BAHIA | Brasil | 2912004 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| e293e8f9-624e-3989-8aee-654cb3a5a662 | -14.19498 | -42.379 | 2024-10-04 04:10:00 | NOAA-21 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 5f86d500-b9ab-38be-b7fd-dd4c2b9c7995 | -13.87599 | -42.33221 | 2024-10-04 04:10:00 | NOAA-21 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| bd618ee3-2860-3fc6-81a4-fab3fc4457e3 | -16.0174 | -43.19643 | 2024-10-04 04:10:00 | NOAA-21 | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a7ccdd8b-1dd6-3f2a-b1fb-a1efc5aa4892 | -15.95694 | -43.36648 | 2024-10-04 04:10:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| dec194b9-1e77-3879-aa06-1a93161cd45e | -15.77061 | -43.58029 | 2024-10-04 04:10:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0aa77a95-737e-3028-aa2b-d90b0567c7d6 | -16.4754 | -43.81585 | 2024-10-04 04:10:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4aafb412-30a5-33ca-85dc-8ad86efe0dbc | -16.47484 | -43.81942 | 2024-10-04 04:10:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2a4098c7-2e32-368c-9b4f-b16fc22755b6 | -16.4721 | -43.81529 | 2024-10-04 04:10:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b641e735-667a-3a27-bb37-d709f7e4fd08 | -16.47154 | -43.81887 | 2024-10-04 04:10:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 94ac101a-564e-36cd-b608-61e979fdd629 | -15.30309 | -42.53419 | 2024-10-04 04:10:00 | NOAA-21 | MONTEZUMA | MINAS GERAIS | Brasil | 3143450 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 133c3221-e631-3081-8938-a1a2dc5646a3 | -15.96025 | -43.36703 | 2024-10-04 04:10:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 51a6ca23-ba05-309e-a8d0-7035ffa9be81 | -15.76731 | -43.57974 | 2024-10-04 04:10:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c6ad6707-6315-3e4a-b638-4b41719b2955 | -15.59284 | -43.64972 | 2024-10-04 04:10:00 | NOAA-21 | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b0075cdf-3875-3797-927a-ff4a57926393 | -15.59228 | -43.65328 | 2024-10-04 04:10:00 | NOAA-21 | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b2cd9d09-76f3-3433-85be-b63a5f2da45f | -15.95639 | -43.37006 | 2024-10-04 04:10:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| cd78496f-47fa-37d0-9470-d1e2a0b54cc0 | -17.74667 | -43.81921 | 2024-10-04 04:10:00 | NOAA-21 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 56aa0747-273a-322a-b4d3-3e91aef69ba8 | -17.73732 | -43.81393 | 2024-10-04 04:10:00 | NOAA-21 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 12a47ed4-b158-380a-8c0d-0f082ba098bb | -17.73513 | -43.80618 | 2024-10-04 04:10:00 | NOAA-21 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4f0716c5-115e-3cc0-ba24-a86f147336dd | -17.74393 | -43.81506 | 2024-10-04 04:10:00 | NOAA-21 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 27.0 |
| 78eb8145-65cd-3301-b764-b58dc7aa133b | -17.74337 | -43.81865 | 2024-10-04 04:10:00 | NOAA-21 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 27.0 |
| 5780b15a-e702-3688-8212-249fcc860036 | -17.74281 | -43.82224 | 2024-10-04 04:10:00 | NOAA-21 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d87bb0bb-044a-3218-a6e0-067feb22bab4 | -17.7395 | -43.82168 | 2024-10-04 04:10:00 | NOAA-21 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6e9421e6-3f90-3e11-98bc-c276c2d2582e | -17.73844 | -43.80674 | 2024-10-04 04:10:00 | NOAA-21 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 20732d96-87c2-33ad-8133-f1472533d9fa | -17.73788 | -43.81034 | 2024-10-04 04:10:00 | NOAA-21 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8cf9cdcc-80e6-3681-9394-ea7aa88c6051 | -17.73676 | -43.81753 | 2024-10-04 04:10:00 | NOAA-21 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 5.6 |
| cf240cc3-6e45-3aee-bd86-3a1756c0dceb | -17.73458 | -43.80979 | 2024-10-04 04:10:00 | NOAA-21 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a60c40ce-cdb5-31d6-81d1-6fcdd2ed56e3 | -17.73402 | -43.81338 | 2024-10-04 04:10:00 | NOAA-21 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 5.6 |
| b3beb3b6-e9a2-3eff-a461-83ff772c760a | -17.69555 | -43.77732 | 2024-10-04 04:10:00 | NOAA-21 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9699605b-c0e5-392b-9bf0-e753bb23d747 | -17.74118 | -43.8109 | 2024-10-04 04:10:00 | NOAA-21 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| f15b410f-401d-3996-8bcd-6a628a4251d8 | -17.74062 | -43.8145 | 2024-10-04 04:10:00 | NOAA-21 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 27.0 |
| e90144ec-8f33-3e5d-bbe5-e7acdaa92ee5 | -17.74006 | -43.81808 | 2024-10-04 04:10:00 | NOAA-21 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 27.0 |
| 84781be7-3c72-391b-9091-889eb3a902bf | -17.7362 | -43.82112 | 2024-10-04 04:10:00 | NOAA-21 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| d60b06b0-8dfc-3efb-a3c6-b409f5ae8da4 | -17.695 | -43.78093 | 2024-10-04 04:10:00 | NOAA-21 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ab7678ce-cb82-3a1d-ae6a-c5cd7d7c2391 | -18.04708 | -43.32602 | 2024-10-04 04:10:00 | NOAA-21 | SÃO GONÇALO DO RIO PRETO | MINAS GERAIS | Brasil | 3125507 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c23ed7f1-7643-313c-b725-84f17f6e48c4 | -17.81006 | -44.21842 | 2024-10-04 04:10:00 | NOAA-21 | JOAQUIM FELÍCIO | MINAS GERAIS | Brasil | 3136405 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0a20ee55-08a0-3b61-9956-10ba91983204 | -17.78337 | -44.28035 | 2024-10-04 04:10:00 | NOAA-21 | JOAQUIM FELÍCIO | MINAS GERAIS | Brasil | 3136405 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4ef7f8bf-0fd2-3cdb-aa07-ba84e1e8cba9 | -17.74448 | -43.81146 | 2024-10-04 04:10:00 | NOAA-21 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| a9e187a1-c441-3e62-aef1-f67a71b7ed6f | -17.73681 | -43.79537 | 2024-10-04 04:10:00 | NOAA-21 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 51637356-1064-36f3-ad30-b501676d2fc9 | -17.24474 | -43.21674 | 2024-10-04 04:10:00 | NOAA-21 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 34071a62-42eb-34e8-acfb-a23819747609 | -17.24198 | -43.19017 | 2024-10-04 04:10:00 | NOAA-21 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e5790a7e-575c-3e76-9324-536c4639fb02 | -17.24141 | -43.21621 | 2024-10-04 04:10:00 | NOAA-21 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6a03800a-2e4a-3b82-a2c6-6c048add1ba4 | -17.23809 | -43.21567 | 2024-10-04 04:10:00 | NOAA-21 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bcd6d273-a489-34ed-9a76-7098337d8a24 | -17.23532 | -43.21151 | 2024-10-04 04:10:00 | NOAA-21 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c0f50d5a-bd39-3273-a186-1714e7e6fa3c | -16.6826 | -43.88329 | 2024-10-04 04:10:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 14f48107-3bec-3b56-af4c-16b895680d6b | -18.08774 | -43.50434 | 2024-10-04 04:10:00 | NOAA-21 | COUTO DE MAGALHÃES DE MINAS | MINAS GERAIS | Brasil | 3120102 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 85275cb1-6b16-381d-902f-05e5a4f57e81 | -17.91259 | -43.44987 | 2024-10-04 04:10:00 | NOAA-21 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 28dda9ea-6c29-31a8-b150-411af6babb8b | -17.24086 | -43.21982 | 2024-10-04 04:10:00 | NOAA-21 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9b7b34b6-5eeb-3862-a383-8f03f5f12a30 | -17.739 | -43.80314 | 2024-10-04 04:10:00 | NOAA-21 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 60e2aa10-f54f-3203-9f2f-97c8872cd02c | -17.92092 | -43.43996 | 2024-10-04 04:10:00 | NOAA-21 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 42d66233-4f5b-3da2-89d8-9a399fc36018 | -17.9176 | -43.43941 | 2024-10-04 04:10:00 | NOAA-21 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 53bc539e-b97e-3c5c-8072-a7ef98d3fb72 | -17.91704 | -43.44308 | 2024-10-04 04:10:00 | NOAA-21 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 76da3e35-c288-3e29-a836-0553092a302e | -17.91647 | -43.44675 | 2024-10-04 04:10:00 | NOAA-21 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 08177dce-9fd8-3a16-aed4-eb889389272d | -17.91315 | -43.4462 | 2024-10-04 04:10:00 | NOAA-21 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 9.7 |
| bf8061dc-9c86-3adf-9f73-a8e31baa8b0b | -17.73625 | -43.79898 | 2024-10-04 04:10:00 | NOAA-21 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 681474c7-5c50-3f95-a34a-54248d6d28f1 | -17.73569 | -43.80258 | 2024-10-04 04:10:00 | NOAA-21 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0988b294-4bfe-37b4-9071-8aecec4985da | -17.28129 | -43.20033 | 2024-10-04 04:10:00 | NOAA-21 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fa2a4e84-2fb4-32d1-ac3d-89a0b5dc3868 | -17.24806 | -43.21729 | 2024-10-04 04:10:00 | NOAA-21 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b42aa309-75a0-3b44-94b3-09e3215ae866 | -17.24253 | -43.18653 | 2024-10-04 04:10:00 | NOAA-21 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 594fce6f-430a-3191-8902-8f479b3d8c08 | -17.09578 | -43.80575 | 2024-10-04 04:10:00 | NOAA-21 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 43c0fd29-e67c-3fab-9bc4-6dc7bfd5ac7a | -16.75279 | -43.78123 | 2024-10-04 04:10:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 667a7189-bb7b-3c38-bfd5-9e9cd2601e00 | -18.04651 | -43.3297 | 2024-10-04 04:10:00 | NOAA-21 | SÃO GONÇALO DO RIO PRETO | MINAS GERAIS | Brasil | 3125507 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0bc23942-eda9-3d05-8462-c7b3d13f9ae7 | -17.91372 | -43.44253 | 2024-10-04 04:10:00 | NOAA-21 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 174e868a-a230-36e0-8918-cb45dc01e5fb | -17.23755 | -43.1969 | 2024-10-04 04:10:00 | NOAA-21 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1b39da14-eba8-397f-af58-5bd806820f98 | -18.49027 | -43.87043 | 2024-10-04 04:10:00 | NOAA-21 | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7131e212-959d-3e2f-98e2-0d5adab605e6 | -18.47593 | -43.87543 | 2024-10-04 04:10:00 | NOAA-21 | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cf901a33-7058-3654-bc4f-0dee9032f9c7 | -13.89318 | -44.27633 | 2024-10-04 04:10:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 55d5c41e-f0cc-327e-8fee-e448f13e21c4 | -18.36939 | -44.03521 | 2024-10-04 04:10:00 | NOAA-21 | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 93823100-6a60-3c15-b071-41fd6ed1b732 | -18.33522 | -44.0368 | 2024-10-04 04:10:00 | NOAA-21 | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9af1cf98-b9e2-3c29-b5f6-0de7f02a23b4 | -18.33248 | -44.03263 | 2024-10-04 04:10:00 | NOAA-21 | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ddc72641-07eb-398b-ba2a-ac68c8e12813 | -18.57514 | -43.95886 | 2024-10-04 04:10:00 | NOAA-21 | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 14e75121-4e5e-3bbd-9fa1-9383126b2204 | -18.56995 | -43.83881 | 2024-10-04 04:10:00 | NOAA-21 | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 04e2e323-2ddc-3a74-98b2-835080d8f37d | -18.56333 | -43.8377 | 2024-10-04 04:10:00 | NOAA-21 | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ece4ff19-b5cc-3872-899c-85c909f3d732 | -18.40091 | -44.464 | 2024-10-04 04:10:00 | NOAA-21 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a23ad432-2167-3cf3-92cc-088a48a001df | -18.38316 | -44.03387 | 2024-10-04 04:10:00 | NOAA-21 | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0aa5ae28-c77f-31bd-a0c4-1b85534fb4b0 | -18.34907 | -44.01323 | 2024-10-04 04:10:00 | NOAA-21 | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 66654615-87dd-394a-8f8a-165d7014270c | -18.34851 | -44.01683 | 2024-10-04 04:10:00 | NOAA-21 | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 8.5 |
| ae55bf5c-4d22-36d1-91bc-7a5fd4bb2f90 | -18.32812 | -44.0171 | 2024-10-04 04:10:00 | NOAA-21 | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d8eed565-0955-3f90-b46b-d670a764271b | -14.31092 | -44.7054 | 2024-10-04 04:10:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6088ce9e-1864-302e-9e37-f67082628da5 | -18.26786 | -43.43701 | 2024-10-04 04:10:00 | NOAA-21 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e93dd781-7769-3133-a629-b034f91489bf | -18.30894 | -43.23308 | 2024-10-04 04:10:00 | NOAA-21 | RIO VERMELHO | MINAS GERAIS | Brasil | 3156007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| a336a2be-d68a-328e-b180-dc052fc76636 | -18.56664 | -43.83826 | 2024-10-04 04:10:00 | NOAA-21 | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 72b675d0-c2ce-3ccc-b303-cc21973944a6 | -18.37269 | -44.03578 | 2024-10-04 04:10:00 | NOAA-21 | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 23ddc16d-8327-3764-afd9-d4bee124dbe7 | -18.35237 | -44.0138 | 2024-10-04 04:10:00 | NOAA-21 | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 0ab0bb6f-2658-3f1c-bf2f-73c748952633 | -18.33199 | -44.01406 | 2024-10-04 04:10:00 | NOAA-21 | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |


[Clique aqui para ver as próximas entradas](README78.md)
