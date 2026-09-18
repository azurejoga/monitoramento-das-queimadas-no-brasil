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

## Dados Diários - Página 40

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1ac194f2-31c5-310f-a6d1-6396695f1dba | -11.80868 | -46.79702 | 2026-09-18 04:21:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ebf6f3ca-a949-319f-80c2-fd98935b9b6a | -9.93963 | -46.54639 | 2026-09-18 04:21:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 1d9fa21c-502e-3e9e-8918-b5391d98ad61 | -9.75993 | -45.06408 | 2026-09-18 04:21:00 | NOAA-21 | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cc0e20cb-91cd-319b-a71a-901ccab23a4d | -11.69584 | -45.38486 | 2026-09-18 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7a09d6dc-6530-36ce-b717-4fef63c4d46b | -12.3916 | -48.46748 | 2026-09-18 04:21:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| a1b70ca6-5b3b-3b86-9263-be4c01688199 | -11.52317 | -46.88091 | 2026-09-18 04:21:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 40084432-e47c-3e4f-bdb4-4092c96eae27 | -9.60592 | -45.35458 | 2026-09-18 04:21:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 6c52df75-fa13-3d18-a5a6-5e49d7420cad | -11.24216 | -54.20918 | 2026-09-18 04:21:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 4e7ba834-77a8-3145-92e5-f249daeab209 | -10.11218 | -46.29335 | 2026-09-18 04:21:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1a983895-b533-3dd9-81d1-cc748fa658e4 | -11.5359 | -46.88663 | 2026-09-18 04:21:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 77c76549-9cbd-3d66-9265-2a801533473d | -11.28941 | -43.35034 | 2026-09-18 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| ca7e1cf4-26b7-3fe1-a471-9d003ff198d2 | -14.96566 | -46.24651 | 2026-09-18 04:21:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b00550a2-912a-3181-b32c-8591e9b1801a | -9.09362 | -45.71753 | 2026-09-18 04:21:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 66f1cae9-e6ef-3b0a-9807-025dabc2d896 | -10.55075 | -44.85228 | 2026-09-18 04:21:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0a8057c1-68ee-3fe6-a1ee-4b61323685c7 | -12.36824 | -50.70089 | 2026-09-18 04:21:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d1210390-b2e4-3a16-8526-008a1a25abc8 | -13.40592 | -42.27774 | 2026-09-18 04:21:00 | NOAA-21 | PARAMIRIM | BAHIA | Brasil | 2923605 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| bf9bef54-1843-382a-b205-6c90324f87e0 | -8.84844 | -45.91421 | 2026-09-18 04:21:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a989cc75-059a-3473-81ba-eec6a40159c2 | -12.71095 | -43.86879 | 2026-09-18 04:21:00 | NOAA-21 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d59c6a9b-00f6-307c-8453-8d4367cc99d3 | -9.48499 | -54.48535 | 2026-09-18 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| c4b7e2a1-f4aa-35d3-ba1a-66fd8c9656ec | -10.63204 | -46.06133 | 2026-09-18 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d54527e1-2f54-3abe-a079-cc25be59be38 | -10.29175 | -45.32048 | 2026-09-18 04:21:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fce90d0d-5e57-3f89-ac10-7c0528bfc84c | -11.82138 | -46.80273 | 2026-09-18 04:21:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ca52245a-9a63-3a28-bb7f-06d662efc5dd | -11.66939 | -54.44382 | 2026-09-18 04:21:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 25.1 |
| fb71fff8-6084-3c1e-a2ca-6bd2735eb5ef | -8.33765 | -47.58009 | 2026-09-18 04:21:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7a9e7e80-de18-3603-814e-05005212b475 | -10.60934 | -46.55023 | 2026-09-18 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| bcb6fdf3-c169-3e84-b210-e1a295eff8db | -13.74431 | -48.78986 | 2026-09-18 04:21:00 | NOAA-21 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d3f9d0d7-077f-3b25-a0ae-b18f02152889 | -10.50707 | -47.89601 | 2026-09-18 04:21:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 892dc43e-f92f-3023-ad90-56c37d69e599 | -13.36521 | -46.30667 | 2026-09-18 04:21:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8fc23ecd-c0db-39d1-9b32-149d20d27d26 | -9.95393 | -46.60695 | 2026-09-18 04:21:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 61b5529c-bb0a-3dab-8e09-b14c63adf2a4 | -9.7789 | -48.35957 | 2026-09-18 04:21:00 | NOAA-21 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1aeb560d-4bf5-309e-a120-21fb212ffa64 | -8.4451 | -45.70981 | 2026-09-18 04:21:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a3121580-3e85-3934-81b1-70748cfba9ce | -10.40443 | -46.61853 | 2026-09-18 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9e8fcef8-750b-388d-b658-e623e39605f1 | -8.51461 | -48.49964 | 2026-09-18 04:21:00 | NOAA-21 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a5c2773d-bc9c-3656-9eb9-2c13498c8ad4 | -10.02159 | -45.50268 | 2026-09-18 04:21:00 | NOAA-21 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 59bed279-e195-3d7d-a6f5-33973186c01a | -13.25141 | -46.90326 | 2026-09-18 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| faf7e263-a44a-3495-a528-0957c86bf64b | -10.63534 | -46.06186 | 2026-09-18 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 2b4c3962-37a1-3425-8d38-4d6e8c5374ec | -10.66268 | -50.26732 | 2026-09-18 04:21:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3d21ade7-26fb-38b3-a680-42bd103ba236 | -12.65232 | -54.7157 | 2026-09-18 04:21:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 3b760597-7679-3b9c-a23a-d0c68c65f22d | -9.18651 | -45.69008 | 2026-09-18 04:21:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 24afbb32-3aa7-34e8-8ae2-46d232489294 | -13.43124 | -51.89907 | 2026-09-18 04:21:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 47c4e96a-6a09-3df0-afbe-17d0b0869f36 | -9.72226 | -47.14053 | 2026-09-18 04:21:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 91c93727-3527-3974-be92-acfd06cf520f | -12.33324 | -50.83273 | 2026-09-18 04:21:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cd25aa61-26d4-3504-85ee-59b99203db7a | -8.46031 | -44.49758 | 2026-09-18 04:21:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4a4bae24-6f20-31ca-ac0a-4df17ee30b6f | -12.52406 | -45.96523 | 2026-09-18 04:21:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 26838d24-48a4-35fc-ae47-f36a3de56af1 | -14.26355 | -46.36961 | 2026-09-18 04:21:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 62ef1fd8-3be1-3432-9cee-dd5902bc0a93 | -10.08128 | -45.57978 | 2026-09-18 04:21:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 93fefb30-596d-35b7-a882-028f124fd70a | -11.58564 | -47.30242 | 2026-09-18 04:21:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f5d8e992-9476-36dc-802a-698e0f102b97 | -9.18981 | -45.69061 | 2026-09-18 04:21:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 734dadbe-6ce7-3340-a232-0f3d3cd65409 | -8.44564 | -45.70633 | 2026-09-18 04:21:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| fb8433db-d73f-3995-b808-f0b439819099 | -8.93523 | -51.46472 | 2026-09-18 04:21:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 345b6d60-d428-39af-8359-036d8c0e5840 | -9.94958 | -45.33419 | 2026-09-18 04:21:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| db4fe392-707a-39b8-a188-15f7298311f3 | -11.13132 | -47.70843 | 2026-09-18 04:21:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| e48302b0-f61b-3053-9534-872241fa857f | -15.06068 | -48.5896 | 2026-09-18 04:21:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d875735e-7398-3df4-a876-70eb1401155d | -10.9408 | -53.05703 | 2026-09-18 04:21:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e139beb1-40c9-3c37-9d34-13fc4320d852 | -11.37995 | -47.03309 | 2026-09-18 04:21:00 | NOAA-21 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 59692fd6-3786-3918-92fc-83ba3908d84d | -9.94773 | -45.45531 | 2026-09-18 04:21:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 6509eff1-f7e0-3e95-a38f-750b9f223afb | -8.87098 | -45.85698 | 2026-09-18 04:21:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cadbb611-3719-3e0d-9441-14f7454c6aed | -13.51367 | -48.94955 | 2026-09-18 04:21:00 | NOAA-21 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 4162a84d-13f1-32c5-ae36-2f6452d52e35 | -10.38476 | -46.63675 | 2026-09-18 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bb7925a0-56d2-30fc-8f81-aa83f0e0d3e3 | -10.02844 | -45.57141 | 2026-09-18 04:21:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 04f1bfb5-14ea-303e-b1fe-79223a79badf | -8.91235 | -45.00569 | 2026-09-18 04:21:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7281f7d5-457a-30e0-953e-d40f22a6e9c8 | -9.59433 | -45.34207 | 2026-09-18 04:21:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a59964a3-ddc4-3e16-9955-6672f873d852 | -15.86314 | -38.94157 | 2026-09-18 04:21:00 | NOAA-21 | BELMONTE | BAHIA | Brasil | 2903409 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| e2a2ff18-73ff-30b5-8bf8-c1e2ce1ed095 | -10.49773 | -46.28735 | 2026-09-18 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d867b538-75f5-3a44-8df1-e4ec9d0a4052 | -11.77602 | -47.43085 | 2026-09-18 04:21:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 79bcf4b4-8293-36aa-a7b6-4139ed7c89f9 | -8.67904 | -45.30293 | 2026-09-18 04:21:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5f524691-c6ad-3d74-8bcb-c8abd9e68aaa | -13.60345 | -46.93604 | 2026-09-18 04:21:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 124af1f6-1da1-3e75-8c9b-4f0b937c29db | -12.27048 | -50.75175 | 2026-09-18 04:21:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 0ae30dbc-897d-3bb9-9fb4-976a20c44c49 | -11.27651 | -43.50995 | 2026-09-18 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2ba5edfa-32bc-3ed4-93c2-4faccfb09757 | -10.66471 | -50.26509 | 2026-09-18 04:21:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 3ab2bfe6-bd9c-33f7-8fea-dd0c3637422a | -8.4739 | -44.8932 | 2026-09-18 04:21:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 194e3de6-a5d0-34fa-b762-f519b5f22deb | -8.46094 | -44.51564 | 2026-09-18 04:21:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9c6354e8-7633-3fd2-9e85-28e1d590c7d7 | -8.95527 | -51.46733 | 2026-09-18 04:21:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 592532a5-91f1-3a70-8e93-f47c7bc4b57b | -10.33031 | -45.3122 | 2026-09-18 04:21:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0f2d3d0d-a01f-33eb-a515-398ca7dbeb7d | -10.11605 | -46.29037 | 2026-09-18 04:21:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a7780718-9704-3f26-9b13-e061ff9bdd37 | -10.02051 | -45.50965 | 2026-09-18 04:21:00 | NOAA-21 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 43194583-4262-3e97-9cba-7a2608c73cc8 | -8.91888 | -44.98529 | 2026-09-18 04:21:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d86b23fe-03fe-3dca-88e7-9846be562311 | -10.48217 | -45.29654 | 2026-09-18 04:21:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f837b820-73e6-39a2-aa80-089a82297c91 | -11.52265 | -46.86267 | 2026-09-18 04:21:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f4e8cd91-2a89-36bc-92fc-c997a917f456 | -9.62195 | -46.61868 | 2026-09-18 04:21:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5c93b48e-7f2b-339f-b558-2f7c400e11f2 | -8.51101 | -48.49905 | 2026-09-18 04:21:00 | NOAA-21 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 39f9000d-ea04-3004-ae47-339eb4544fcd | -12.72011 | -48.26694 | 2026-09-18 04:21:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 239803aa-2f85-38e0-9878-7cb778adf7dd | -9.59769 | -45.86641 | 2026-09-18 04:21:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 57.9 |
| e3a7c5ca-d87c-3888-8403-371ce00a9cce | -9.94338 | -46.60893 | 2026-09-18 04:21:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 6bfe9a29-dfc8-390e-9449-c6dda6883818 | -9.6148 | -45.36658 | 2026-09-18 04:21:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4578b971-68f6-3a48-867e-c0d65e9e966c | -12.26062 | -47.14457 | 2026-09-18 04:21:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fdf294a6-3538-3041-a477-f21fb03129a8 | -12.56041 | -50.73456 | 2026-09-18 04:21:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 391e9361-d171-343e-81e0-21c48fc79ff4 | -14.15014 | -47.00837 | 2026-09-18 04:21:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7ccc9ade-e89b-382b-90b8-2e7c9e4ab4ba | -9.93841 | -46.5972 | 2026-09-18 04:21:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 3951904b-3de0-3b89-a158-0ed06c976270 | -10.31876 | -45.32114 | 2026-09-18 04:21:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4af82ebb-a7a0-3d07-a847-178b95d8e78a | -14.89703 | -48.14903 | 2026-09-18 04:21:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 41518663-2e4a-3613-b364-ceacd1f853ac | -9.5587 | -48.10825 | 2026-09-18 04:21:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4b35bc6a-8fe6-30ef-8edb-52a0b673e036 | -10.66281 | -50.4838 | 2026-09-18 04:21:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 954041ed-f9dc-3588-8d12-799f47f07b30 | -12.67974 | -43.91213 | 2026-09-18 04:21:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 91bd2345-7ba0-3acf-846e-67dc345ca5a6 | -12.65176 | -54.7187 | 2026-09-18 04:21:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 1119dc96-f37c-358f-be77-a165ace0d7dd | -14.67284 | -42.5007 | 2026-09-18 04:21:00 | NOAA-21 | LICÍNIO DE ALMEIDA | BAHIA | Brasil | 2919405 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| e6b926cc-bc5f-3dc7-bc19-1fda7d6090fb | -10.98324 | -49.72729 | 2026-09-18 04:21:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4eaa8e94-fe52-3f18-a170-675d2c626670 | -8.93095 | -51.464 | 2026-09-18 04:21:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 37ebaf0d-ae5d-3812-a78c-f95b6bf38727 | -9.70792 | -48.14784 | 2026-09-18 04:21:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f8b69bd3-dbe6-3cb0-8f21-a2bf43b60270 | -12.46159 | -50.69952 | 2026-09-18 04:21:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |


[Clique aqui para ver as próximas entradas](README41.md)
