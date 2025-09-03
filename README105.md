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

## Dados Diários - Página 105

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 55e166ff-6f6d-360c-b5d3-e55258fe804b | -11.5875 | -52.13119 | 2025-09-03 05:36:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 3b5e0426-f9c3-337c-bf25-df0577a8de7f | -12.94248 | -56.99154 | 2025-09-03 05:36:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 53573a6e-396b-39a2-bf95-b658f488416b | -7.54683 | -61.32565 | 2025-09-03 05:36:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d069b5bd-9124-3fb5-addf-0c9b8933619a | -11.62382 | -52.13884 | 2025-09-03 05:36:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f8e59c22-7763-387d-9612-eafe03690167 | -11.60981 | -52.0827 | 2025-09-03 05:36:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7a5b4db5-47cd-315c-a310-ced31f185e7f | -11.42119 | -55.18227 | 2025-09-03 05:36:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3ed8d425-941a-3621-8938-70760f0604e5 | -13.10224 | -57.14214 | 2025-09-03 05:36:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9fe554b0-562b-3d24-99dc-39318a911aa4 | -11.58609 | -52.14302 | 2025-09-03 05:36:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 8ba33f33-8509-3e31-bf72-dc47ac60b595 | -12.64093 | -57.0003 | 2025-09-03 05:36:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d699ede7-ca91-340e-b0ef-bd89befe0973 | -12.89115 | -56.95494 | 2025-09-03 05:36:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| af2cd3af-f050-3dec-bbf2-a1a0f6d234ab | -7.53793 | -61.33657 | 2025-09-03 05:36:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| c91c8e8c-0b19-3191-a17a-0aa799757059 | -11.5882 | -52.12528 | 2025-09-03 05:36:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 88de0920-eff8-3ccf-8cc2-d04646e4ced3 | -11.86022 | -52.42573 | 2025-09-03 05:36:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| da5f284a-f367-3b96-8e67-491761b22457 | -12.89685 | -56.94984 | 2025-09-03 05:36:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ec416d91-4e17-3b30-b385-b8c70391464c | -11.59632 | -52.11415 | 2025-09-03 05:36:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 38816a91-eea0-3037-9c0a-4a2d4f709e4b | -10.45201 | -53.61675 | 2025-09-03 05:36:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 2903ed4b-2824-3e82-b1fb-23fb0bbda040 | -11.6104 | -52.13744 | 2025-09-03 05:36:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9e20372d-2fac-310d-8f08-b2ebb7356a7e | -7.54914 | -61.33413 | 2025-09-03 05:36:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c0639c13-e04d-38e8-98c9-3f0d1526c2d1 | -11.42033 | -55.18936 | 2025-09-03 05:36:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e02dc969-6aa8-320e-a9c9-1f471b76e58b | -11.60141 | -52.07148 | 2025-09-03 05:36:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 427d1222-38aa-3a31-befd-7187fd2ef0a4 | -7.54459 | -61.34055 | 2025-09-03 05:36:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b663cde2-c0b4-3aea-9124-37b000049b03 | -8.1444 | -54.93517 | 2025-09-03 05:36:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 16c3f8d0-b7fa-3bab-9184-31d8703fdcf3 | -12.94747 | -56.99218 | 2025-09-03 05:36:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 2c2d3dc8-08ac-3c50-8a52-15b657682d09 | -11.65985 | -57.35897 | 2025-09-03 05:36:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| bd4ff667-6cc0-3551-a11e-b017d2771093 | -11.01969 | -51.47802 | 2025-09-03 05:36:00 | NOAA-20 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1c0008d9-02de-30a6-a683-89ee9bfd88ed | -7.54024 | -61.34504 | 2025-09-03 05:36:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 3f7ada85-cd0d-37bb-bdbc-0e25daa4dba6 | -7.53671 | -61.34451 | 2025-09-03 05:36:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 5.6 |
| fd38d57f-e01a-3f80-af91-d0d96d24d42d | -10.94567 | -50.78371 | 2025-09-03 05:36:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4cd812a0-07a9-3543-a892-b18c930ab7ac | -11.60641 | -52.11274 | 2025-09-03 05:36:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 10fb7884-3b4e-326c-9741-b6d299d3f497 | -12.91325 | -56.94041 | 2025-09-03 05:36:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| e35bf7be-eadd-3562-8592-541c9d8faa47 | -13.09411 | -57.11854 | 2025-09-03 05:36:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| df45f91e-f7fc-36e0-8637-f12e177766f2 | -11.66595 | -57.34922 | 2025-09-03 05:36:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 55b7a7fb-e065-3325-b1b7-4d508ffac52a | -7.54578 | -61.33257 | 2025-09-03 05:36:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fec37180-750a-35b8-8c0a-4076b4948cff | -12.90825 | -56.93974 | 2025-09-03 05:36:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| f71a18e2-1455-34d1-8b0f-396b781829c9 | -12.62603 | -56.99838 | 2025-09-03 05:36:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bd11f66a-62f3-34e1-a170-404584a7f650 | -7.5505 | -61.32512 | 2025-09-03 05:36:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0dc9753b-c0b2-3db2-9ceb-96ebddeae5fe | -11.64684 | -52.05684 | 2025-09-03 05:36:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c0caa64b-e700-31f5-beb1-ad8928f9e1c2 | -11.66463 | -57.35739 | 2025-09-03 05:36:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 2ff2dc6e-cb16-309b-b4d8-7ac66492eb6f | -13.01853 | -56.87431 | 2025-09-03 05:36:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c925023d-9e01-3a4e-ae1c-38108858c466 | -7.38128 | -57.14608 | 2025-09-03 05:36:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ca4b7993-dffd-3439-8548-ecd42ba49bf1 | -6.92845 | -62.94603 | 2025-09-03 05:36:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 0beb0f5c-263d-30b9-a264-06319362db49 | -11.67486 | -57.35569 | 2025-09-03 05:36:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| b1cae0c4-2161-353d-8f0e-393184c755c8 | -7.55284 | -61.33361 | 2025-09-03 05:36:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1c6e72c2-96b8-3f0c-b791-8fa5aaa64368 | -11.61107 | -52.13152 | 2025-09-03 05:36:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6f05e454-a43e-3d67-85c0-377f7edfd635 | -11.85393 | -51.53425 | 2025-09-03 05:36:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 95473b86-4ca2-3c63-9e09-acb28328a5da | -11.85304 | -51.41853 | 2025-09-03 05:36:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a76c464e-a343-3607-8700-c119ea7ecb54 | -11.60311 | -52.08168 | 2025-09-03 05:36:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 563fd64a-a0e9-305e-aa15-533f014aa87a | -10.94649 | -50.77651 | 2025-09-03 05:36:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 56b65788-4d9c-307f-8866-fcfee3724f7e | -6.83488 | -59.36597 | 2025-09-03 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7fe42c07-5dc6-37e1-98e9-6b90641cb5bc | -11.84618 | -51.41652 | 2025-09-03 05:36:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 278f9c75-a4b4-354c-acde-3061924c4de2 | -11.42131 | -55.18286 | 2025-09-03 05:36:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 36d3d12a-03c7-3cd6-903d-e38b9d1f07de | -7.54146 | -61.33709 | 2025-09-03 05:36:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| db817e16-c769-38ca-9e9e-dd647782a953 | -7.25956 | -57.55022 | 2025-09-03 05:36:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ccea0c46-3d6c-3e71-95a6-6f0b7afca111 | -12.93253 | -56.94912 | 2025-09-03 05:36:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6f0acbde-b30d-335c-956e-55042ca43e3c | -10.96506 | -50.93015 | 2025-09-03 05:36:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5b711ca4-5c5c-3cae-ae9e-348eec9e6239 | -11.66529 | -57.35447 | 2025-09-03 05:36:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0488c6aa-4470-3d6a-817a-d68d522c4fa5 | -12.6104 | -57.00221 | 2025-09-03 05:36:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f6c1dd48-8db3-36d1-93a6-da8bd628d5fd | -12.93607 | -56.96152 | 2025-09-03 05:36:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a723f001-d1b6-3362-aab9-005a86151933 | -10.9687 | -50.93176 | 2025-09-03 05:36:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| aab19a39-6b84-34a7-8b38-ce88647d0cba | -11.19597 | -55.01408 | 2025-09-03 05:36:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f96e808d-94a7-3ef9-a33f-8eaf914fe339 | -11.58362 | -52.13419 | 2025-09-03 05:36:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 13.3 |
| d37bd7cb-f4c6-3e1f-ac87-c32ed4373782 | -11.59031 | -52.13504 | 2025-09-03 05:36:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 0b15242e-0439-3c54-95d1-af9d11631519 | -11.62664 | -52.05453 | 2025-09-03 05:36:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8ee73bc7-60b5-3701-95d2-5ac43a0c5a4f | -11.60438 | -52.13066 | 2025-09-03 05:36:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ec9df20a-b0bb-3b98-8c87-caeb393e662d | -11.60449 | -52.06945 | 2025-09-03 05:36:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| de309fad-3c0d-3a61-be21-6c9a1765ac91 | -12.91345 | -56.93952 | 2025-09-03 05:36:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 1a8b3845-6dfd-3bea-817d-3334b5743c2c | -8.1502 | -54.93278 | 2025-09-03 05:36:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 075ccd09-2b3b-34d1-abde-df086ecff43d | -12.9077 | -56.9446 | 2025-09-03 05:36:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| bc36212a-1e7d-348f-a178-e7e74bd35af1 | -7.76064 | -61.20375 | 2025-09-03 05:36:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9d113701-87e8-3d80-a145-1e88423e8871 | -7.54931 | -61.33309 | 2025-09-03 05:36:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8b88619c-db96-3c6c-9e25-4292ce2208b2 | -13.1011 | -57.14228 | 2025-09-03 05:36:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9e8156b1-1f8f-31b9-84b1-0c5b75ea470a | -11.59279 | -52.14375 | 2025-09-03 05:36:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 34a59c3e-ad79-3b51-86d0-a01a9a07b3c1 | -11.60973 | -52.14331 | 2025-09-03 05:36:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| a2caa94e-240f-3a94-b942-e15cbcf05062 | -12.94536 | -56.96856 | 2025-09-03 05:36:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| be61a455-bf3d-349b-889b-2a38957b35bf | -11.59297 | -52.11137 | 2025-09-03 05:36:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 5982995e-7fd6-3e41-918e-e4df4037fc04 | -11.58428 | -52.12829 | 2025-09-03 05:36:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 432fc06f-22f5-3cf7-8ce5-733a6f24e31f | -11.61118 | -52.07055 | 2025-09-03 05:36:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b9958f35-22f9-3295-88c0-6bc12c2ef267 | -12.92538 | -57.00669 | 2025-09-03 05:36:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 96dc57e1-7c04-36eb-9487-e3670c6576c5 | -7.76837 | -61.20078 | 2025-09-03 05:36:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3b2d6011-b40e-3a9c-8533-52878b19d83c | -11.59421 | -52.1318 | 2025-09-03 05:36:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 12.2 |
| b71f515c-a212-367c-927b-d9d04cf31c44 | -12.97451 | -54.77246 | 2025-09-03 05:36:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 81b579f4-7d71-320c-a01a-9831e59a590b | -12.63595 | -56.99972 | 2025-09-03 05:36:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 591209b4-6967-304e-b293-7eba238557c7 | -7.54622 | -61.32964 | 2025-09-03 05:36:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 707e9663-9e62-3204-a3f9-7b58bdc06c57 | -11.66533 | -57.3522 | 2025-09-03 05:36:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6087222b-b687-35a4-8fa7-eb269b588b9b | -8.06238 | -52.37406 | 2025-09-03 05:36:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 99020f2e-0b94-3920-a9aa-2474e6de9023 | -7.54438 | -61.34158 | 2025-09-03 05:36:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| cf5ea884-eea3-37d7-98cf-658fc45fffc4 | -12.93893 | -56.97934 | 2025-09-03 05:36:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 5bbb4ae5-bbb5-3eb5-a28b-9a7fde82386c | -7.54377 | -61.34555 | 2025-09-03 05:36:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4b2eed9e-654d-37e4-8d80-ee92293f60f9 | -11.58963 | -52.14103 | 2025-09-03 05:36:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 16.7 |
| a9e6cba2-0249-335a-8894-a34bf0b94067 | -7.67274 | -61.09224 | 2025-09-03 05:36:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b50d3e9a-ae7c-3ba2-b64e-d447b8a90190 | -13.01789 | -56.87582 | 2025-09-03 05:36:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 63bb1979-a758-3c8e-983e-d84e8dd59f14 | -12.9197 | -57.01164 | 2025-09-03 05:36:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 8c394335-355b-3e3e-98f1-c379b867954a | -10.96948 | -50.92471 | 2025-09-03 05:36:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 02d4ef64-0d71-3a74-b1cf-25c01b350613 | -13.09686 | -57.13616 | 2025-09-03 05:36:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 356eb70a-b19e-385d-9216-449705082314 | -9.15266 | -58.88937 | 2025-09-03 05:36:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 498cae69-3e69-385b-9c3d-fd9ba1cdd84f | -11.6605 | -57.35386 | 2025-09-03 05:36:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 70ea5dbe-4565-3304-b67f-60413942e804 | -12.63099 | -56.99909 | 2025-09-03 05:36:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ed4bb6de-9b1d-331b-ba88-8efd0e23cd07 | -11.59995 | -52.08379 | 2025-09-03 05:36:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ddd7fb51-cd41-3769-a21d-66f33e85f8ce | -11.59492 | -52.1259 | 2025-09-03 05:36:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 12.2 |
| a986fd6c-43bc-34f5-9770-eccff35cfca6 | -12.94819 | -56.9865 | 2025-09-03 05:36:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |


[Clique aqui para ver as próximas entradas](README106.md)
