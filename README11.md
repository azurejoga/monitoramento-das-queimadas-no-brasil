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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 035da181-b809-344c-afba-69b84e685084 | -12.54351 | -46.9288 | 2026-08-08 04:25:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 29907565-0778-3d5d-b813-8f8edd78b705 | -7.1653 | -44.06811 | 2026-08-08 04:25:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e84467a5-e54e-3418-90a1-4839268c8ed7 | -11.1514 | -45.93701 | 2026-08-08 04:25:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c33bfa21-52aa-3382-a2ca-996a0b7e17ea | -11.15498 | -54.84794 | 2026-08-08 04:25:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8af8547a-5f2d-3f0e-97e2-ced2f955485c | -11.27193 | -55.86324 | 2026-08-08 04:25:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 7d4ff613-a4ee-3152-953a-17b768f21e91 | -7.16253 | -44.06408 | 2026-08-08 04:25:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c775803c-300d-3477-9d50-bb46763f3141 | -8.14873 | -55.4268 | 2026-08-08 04:25:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 804bc628-18e0-3a70-b7dd-4ef0532d051f | -12.54376 | -46.94861 | 2026-08-08 04:25:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 19.2 |
| ec97b672-4f98-366f-b11e-06d12de42115 | -6.72265 | -48.12162 | 2026-08-08 04:25:00 | NPP-375D | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d8f11106-5037-3f78-8343-545c535e0621 | -8.65446 | -45.86171 | 2026-08-08 04:25:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4bbee71f-c2fb-3fbb-a84f-65545d2b4b8b | -7.82927 | -47.54167 | 2026-08-08 04:25:00 | NPP-375D | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5438aced-cb03-3db1-88ae-a78fc01232ac | -6.92477 | -41.95869 | 2026-08-08 04:25:00 | NPP-375D | SÃO JOÃO DA VARJOTA | PIAUÍ | Brasil | 2209955 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 8a780654-f96b-349a-85de-5bee303bb73d | -6.91699 | -42.40703 | 2026-08-08 04:25:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| b68f3dab-d7b1-37b4-9dba-a149f907d8a9 | -13.95404 | -41.87109 | 2026-08-08 04:25:00 | NPP-375D | LIVRAMENTO DE NOSSA SENHORA | BAHIA | Brasil | 2919504 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 9774b281-0914-3f66-ab00-881b9b49d761 | -8.20771 | -42.21465 | 2026-08-08 04:25:00 | NPP-375D | PEDRO LAURENTINO | PIAUÍ | Brasil | 2207934 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| a5b24545-870c-3ab8-9749-34e67184d323 | -6.88754 | -48.00003 | 2026-08-08 04:25:00 | NPP-375D | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a094d752-3ffe-3dfe-bd50-cc38d6752f6c | -13.38892 | -41.32612 | 2026-08-08 04:25:00 | NPP-375D | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| c354417a-92d3-3332-9c82-90f7402b5dd6 | -7.83305 | -47.5423 | 2026-08-08 04:25:00 | NPP-375D | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b9604ae3-23a2-3e74-8a9c-87c686c5aca6 | -6.60277 | -56.35895 | 2026-08-08 04:25:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1695ddc2-d646-3cb2-ac85-b372d51b77b3 | -10.45788 | -37.14402 | 2026-08-08 04:25:00 | NPP-375D | NOSSA SENHORA DAS DORES | SERGIPE | Brasil | 2804607 | 28 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| 6cbabfa5-5c67-3758-8314-2a97be7d91b3 | -7.4472 | -55.29628 | 2026-08-08 04:25:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dd15d34e-c0dd-3ad3-869c-983fbd159dd4 | -10.78498 | -46.10637 | 2026-08-08 04:25:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ce1c0031-2ed5-304e-92d3-d5b0fb379ccc | -6.92092 | -42.42572 | 2026-08-08 04:25:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 17678a36-9cf5-3a83-bb11-d73fe2a2b975 | -6.60893 | -56.36658 | 2026-08-08 04:25:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| df8578e0-7006-3c97-95a5-2587bc481c10 | -6.97697 | -41.48769 | 2026-08-08 04:25:00 | NPP-375D | SANTANA DO PIAUÍ | PIAUÍ | Brasil | 2209351 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 9af9197d-2a8d-33fc-b7d0-ac176144b11e | -10.50713 | -46.37164 | 2026-08-08 04:25:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cd1fc219-5f65-3dac-90dd-8cc9d7fea2b5 | -11.24498 | -54.02326 | 2026-08-08 04:25:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 406e1386-b375-3d72-9ff6-285ffd85b317 | -6.97813 | -41.48024 | 2026-08-08 04:25:00 | NPP-375D | SANTANA DO PIAUÍ | PIAUÍ | Brasil | 2209351 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 8c2c4014-3e3c-30f0-b6e3-c601a7c0cf6a | -8.55822 | -45.39828 | 2026-08-08 04:25:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 19e7dfd1-7af2-323a-a0f6-ea64a1b007bd | -10.78559 | -46.10263 | 2026-08-08 04:25:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1bfe36ab-76da-3b5e-ad60-404b5a0c54c2 | -6.91978 | -42.41109 | 2026-08-08 04:25:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| b0e68fba-3528-36b3-8659-1efc6fd4a6f5 | -8.08069 | -45.58036 | 2026-08-08 04:25:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1d73774e-d7c5-3779-bc26-7b683e39d0d8 | -6.91241 | -41.97152 | 2026-08-08 04:25:00 | NPP-375D | SÃO JOÃO DA VARJOTA | PIAUÍ | Brasil | 2209955 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| d9cbc230-8070-3c74-ba65-7db78a686a26 | -10.23995 | -45.80324 | 2026-08-08 04:25:00 | NPP-375D | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 772df99d-eb07-3c49-8b2c-549e413aa146 | -7.26343 | -39.40271 | 2026-08-08 04:25:00 | NPP-375D | CRATO | CEARÁ | Brasil | 2304202 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 3e4f7646-e477-3532-ab5e-38f7967d07c0 | -6.88985 | -43.71312 | 2026-08-08 04:25:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 01c25a7c-35be-33c5-be52-28c50cae7a66 | -6.30624 | -52.81212 | 2026-08-08 04:25:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4a47e045-490a-330a-8c2b-f8819fa27dc2 | -11.1971 | -54.84536 | 2026-08-08 04:25:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a42893ee-760d-3571-8716-b9e22732ce1b | -14.10481 | -39.72716 | 2026-08-08 04:25:00 | NPP-375D | IPIAÚ | BAHIA | Brasil | 2913903 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 3a52ca72-6d35-3e55-b20e-2f9cac7bd3a8 | -7.16141 | -44.07109 | 2026-08-08 04:25:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9e3e15a3-04c7-3680-8958-49f073bb6d15 | -11.30485 | -44.8566 | 2026-08-08 04:25:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3a56559d-2642-3239-b5d4-3e3450aebb1b | -6.9128 | -41.96467 | 2026-08-08 04:25:00 | NPP-375D | SÃO JOÃO DA VARJOTA | PIAUÍ | Brasil | 2209955 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| a9663177-cc31-34c5-bf05-cdcc0f8acb44 | -10.26321 | -45.81046 | 2026-08-08 04:25:00 | NPP-375D | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a2f27952-1d04-3cdb-b177-02d08933ce2c | -6.90886 | -41.9677 | 2026-08-08 04:25:00 | NPP-375D | SÃO JOÃO DA VARJOTA | PIAUÍ | Brasil | 2209955 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| c8643dd1-a0c1-3302-8c09-b088dd4126d5 | -12.54763 | -46.92551 | 2026-08-08 04:25:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3366b4b7-5941-3bce-833f-4d828c5840ed | -11.79457 | -40.92221 | 2026-08-08 04:25:00 | NPP-375D | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 4bf69682-e1e6-37ab-82f3-d122ec611661 | -10.23714 | -45.79906 | 2026-08-08 04:25:00 | NPP-375D | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 637017fe-c9ff-332b-be67-fc052cace045 | -6.3058 | -52.81554 | 2026-08-08 04:25:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 164d9971-60a2-30de-a597-02a0404dd396 | -6.92147 | -42.42219 | 2026-08-08 04:25:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 5814124d-4710-3710-95c6-742505c7a1c2 | -8.33371 | -46.3886 | 2026-08-08 04:25:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| b5c42987-222e-3fbf-93ae-acc7d662aa31 | -12.52678 | -46.9859 | 2026-08-08 04:25:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c89e6b9d-b71d-3f27-9fe8-260e67ee3d71 | -12.57989 | -46.90313 | 2026-08-08 04:25:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b513372d-a964-3a41-9e29-2d1bcea47040 | -9.14473 | -49.66618 | 2026-08-08 04:25:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e25f15b8-484c-3c5f-8e50-cc2c8725b666 | -6.33754 | -46.05298 | 2026-08-08 04:25:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6f14dffc-d136-38dc-8f75-9182d1449345 | -12.3493 | -48.20336 | 2026-08-08 04:25:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| abc6a57d-1f8d-3efe-9b07-7e65efe16fe5 | -11.0356 | -44.27256 | 2026-08-08 04:25:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 13.7 |
| d91e6355-3dba-3e79-afde-455c763ed664 | -6.97015 | -41.48638 | 2026-08-08 04:25:00 | NPP-375D | SANTANA DO PIAUÍ | PIAUÍ | Brasil | 2209351 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| e4b11dce-7be5-3073-8132-44b3482331eb | -8.21165 | -42.21156 | 2026-08-08 04:25:00 | NPP-375D | PEDRO LAURENTINO | PIAUÍ | Brasil | 2207934 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| b011200d-2846-32c3-b036-b554fd0c23bf | -12.32435 | -53.16003 | 2026-08-08 04:25:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 60a4e504-9f4a-329f-855a-4f4908cca77c | -10.52761 | -46.62054 | 2026-08-08 04:25:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3f7b6a96-d060-35b2-bc77-788f0b55a624 | -6.91407 | -41.96075 | 2026-08-08 04:25:00 | NPP-375D | SÃO JOÃO DA VARJOTA | PIAUÍ | Brasil | 2209955 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| b0aa89e4-8add-32ae-a58f-2b4dda016df4 | -9.3801 | -47.08603 | 2026-08-08 04:25:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3ceb32c9-81c8-3a6a-904d-60cf2dd7462f | -8.15878 | -55.42538 | 2026-08-08 04:25:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ba0032e8-7a06-32f1-9aa3-2277e1b7daa4 | -7.21441 | -42.96718 | 2026-08-08 04:25:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| da866606-abf0-3e04-a4ed-c898d1a22efa | -10.25702 | -45.80564 | 2026-08-08 04:25:00 | NPP-375D | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3c64b660-637a-3311-8c17-50dbca6eb95d | -10.61554 | -46.54386 | 2026-08-08 04:25:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6626c2e4-cfa8-3b07-aa31-925c70986f6e | -6.92028 | -41.96537 | 2026-08-08 04:25:00 | NPP-375D | SÃO JOÃO DA VARJOTA | PIAUÍ | Brasil | 2209955 | 22 | 33 | nan | nan | nan | Caatinga | 5.7 |
| d7d37f8d-cc08-351a-a527-01aaa475a57b | -6.98686 | -42.90672 | 2026-08-08 04:25:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| a9458b34-d991-30ac-9240-1862266e081a | -11.03836 | -44.27661 | 2026-08-08 04:25:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 15.6 |
| dd7fa2ca-7f39-386d-8589-0aaaeae735a9 | -12.54135 | -46.92045 | 2026-08-08 04:25:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 30bfd528-a5ed-3df7-ba1b-a508b3038c61 | -8.11401 | -45.89663 | 2026-08-08 04:25:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 91a79fac-7639-37e4-a940-e9527aeff7b8 | -7.18713 | -42.34032 | 2026-08-08 04:25:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| fbd8d3f2-471b-3059-82da-9f71b551c868 | -12.54311 | -46.9525 | 2026-08-08 04:25:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1e77f116-3752-3e66-9260-9f5ae0f785f8 | -11.03172 | -44.27553 | 2026-08-08 04:25:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 13.7 |
| fb9ff0f4-e1d4-3840-b2d0-cdbb97351a80 | -10.26261 | -45.81416 | 2026-08-08 04:25:00 | NPP-375D | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| be56dd2b-a913-3746-bc12-9740643eb71f | -8.62179 | -50.02559 | 2026-08-08 04:25:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 3be30cb6-c5b1-3bfc-943a-26b909f7a37d | -11.15421 | -54.85194 | 2026-08-08 04:25:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3c94a491-deea-3944-b36b-2adf46190769 | -10.50527 | -46.62521 | 2026-08-08 04:25:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7252003b-0dad-3800-b91e-3a67017d3230 | -6.60833 | -56.36697 | 2026-08-08 04:25:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e8443796-7ac3-3cd3-9cc5-9e9dec1c2593 | -12.54634 | -46.93325 | 2026-08-08 04:25:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 89925758-396e-38e7-b9d8-ebfc9082c0ee | -11.15999 | -54.85292 | 2026-08-08 04:25:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d034541a-8911-345f-82ee-38e82dc342db | -6.90831 | -41.97128 | 2026-08-08 04:25:00 | NPP-375D | SÃO JOÃO DA VARJOTA | PIAUÍ | Brasil | 2209955 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 83013b1c-125b-3415-8dbe-30b7577e4417 | -6.92083 | -41.96177 | 2026-08-08 04:25:00 | NPP-375D | SÃO JOÃO DA VARJOTA | PIAUÍ | Brasil | 2209955 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 582f5418-1d2b-3a13-b791-f310e04774fa | -12.54004 | -46.9282 | 2026-08-08 04:25:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 811df493-d417-3d9c-b933-a3a8a3bf0238 | -6.92203 | -42.41866 | 2026-08-08 04:25:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| d063ebfb-71a4-3e41-b728-251bc71b29f6 | -11.72977 | -50.13282 | 2026-08-08 04:25:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| e016de1c-7322-3d74-924b-38a9157dc65b | -7.51221 | -47.00005 | 2026-08-08 04:25:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d3a9cfda-8f9b-381f-a425-fc2fcd0d6c22 | -12.55804 | -46.92727 | 2026-08-08 04:25:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 739c19f4-6742-3765-b5eb-f5f0818a8eed | -8.14339 | -55.42068 | 2026-08-08 04:25:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c8ad869a-4504-3a04-a324-1226b6b36fb7 | -8.2803 | -50.40665 | 2026-08-08 04:25:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| c7321968-c19e-33f5-993d-4deeed49b7ff | -11.19214 | -54.84027 | 2026-08-08 04:25:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 92b7435a-32f2-3371-ab2f-3e25752f87df | -10.26601 | -45.81472 | 2026-08-08 04:25:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f306ef88-d12a-3313-b344-ff3e89243aba | -12.53897 | -46.95588 | 2026-08-08 04:25:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c317c92b-0463-3c96-8f86-b09b6d647ad7 | -7.08194 | -42.26613 | 2026-08-08 04:25:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| e1fd38dc-640a-3a39-8d60-fb13c61da9f0 | -8.1181 | -45.89334 | 2026-08-08 04:25:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| f8b20c81-f908-3ac7-b663-ce18765e9066 | -8.21109 | -42.21518 | 2026-08-08 04:25:00 | NPP-375D | PEDRO LAURENTINO | PIAUÍ | Brasil | 2207934 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 21cc71ca-3e18-3f29-84f8-d090a1b42371 | -11.26483 | -55.867 | 2026-08-08 04:25:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 9e5c0483-f071-3403-9354-0d21ac42a836 | -11.30874 | -44.85362 | 2026-08-08 04:25:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 214c2009-1020-3c89-a6ce-82ffd592e14e | -12.32939 | -53.16106 | 2026-08-08 04:25:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 45cc001b-2fe8-35d0-9b8c-b69b275e006c | -11.23955 | -54.02209 | 2026-08-08 04:25:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README12.md)
