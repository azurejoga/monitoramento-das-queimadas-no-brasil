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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e95e65cf-8be3-31c4-9ac2-195b39394ed0 | -18.7364 | -54.1988 | 2026-07-18 03:50:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 73.5 |
| c9724418-f14e-3d4c-985f-ee1f63b15532 | -21.8702 | -48.7478 | 2026-07-18 04:00:00 | GOES-19 | IBITINGA | SÃO PAULO | Brasil | 3519600 | 35 | 33 | nan | nan | nan | Cerrado | 107.7 |
| 6f47732e-34fa-31e1-8a30-c210db9e2cb3 | -18.7364 | -54.1988 | 2026-07-18 04:00:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 85.9 |
| e0d9cfcd-4c80-3383-a131-27421f7f5f15 | -13.3217 | -45.1479 | 2026-07-18 04:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 62.7 |
| b9b0be9f-2299-3fc9-95f2-1da9779532b8 | -21.8696 | -48.7712 | 2026-07-18 04:00:00 | GOES-19 | IBITINGA | SÃO PAULO | Brasil | 3519600 | 35 | 33 | nan | nan | nan | Cerrado | 49.5 |
| 25d1b511-2de8-3623-96a7-4b4e05e7b12b | -21.8488 | -48.7761 | 2026-07-18 04:00:00 | GOES-19 | IBITINGA | SÃO PAULO | Brasil | 3519600 | 35 | 33 | nan | nan | nan | Cerrado | 49.2 |
| eb820c6b-9867-3da0-a5de-88b3767b56f5 | -21.8495 | -48.7527 | 2026-07-18 04:00:00 | GOES-19 | IBITINGA | SÃO PAULO | Brasil | 3519600 | 35 | 33 | nan | nan | nan | Cerrado | 98.9 |
| b019109e-2dc0-3755-8ed6-7184ac77aab8 | -20.0252 | -57.9468 | 2026-07-18 04:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 65.8 |
| 7a76bc1d-d0c3-3df9-9739-d1a098a2f3fd | -18.7364 | -54.1988 | 2026-07-18 04:10:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 68.4 |
| cba55094-03b5-3454-b6a5-9b7415d58b04 | -13.3217 | -45.1479 | 2026-07-18 04:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 73.5 |
| 31ca8b3c-bb24-3d2f-941a-8274f8cf68c1 | -7.85109 | -48.3973 | 2026-07-18 04:17:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e74f12fe-93ff-32e6-aae4-e5eb75aab0a9 | -7.91009 | -48.26125 | 2026-07-18 04:17:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 50a93455-8b1d-33b4-a50e-9e35460047ca | -7.85181 | -48.39301 | 2026-07-18 04:17:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3a0b77af-4064-3a4e-ad23-886f48a351bb | -5.93514 | -43.64012 | 2026-07-18 04:17:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 834a54c0-21cf-39c4-8aac-ebf4a3bb0723 | -5.60043 | -45.34027 | 2026-07-18 04:17:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 45fed062-4425-37aa-9782-1e41fb661ecf | -5.92825 | -43.63899 | 2026-07-18 04:17:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| eab8cf07-ad91-36ea-beb5-0cc7f5b9f8fb | -8.87015 | -41.24364 | 2026-07-18 04:17:00 | NPP-375D | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 882d964f-01b4-3091-90f4-dded9bfee16e | -8.36576 | -46.80441 | 2026-07-18 04:17:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4a1f11e3-d408-32c4-aa8d-f456ae0444b4 | -5.35823 | -49.17009 | 2026-07-18 04:17:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 404c9856-77da-39a0-9e0a-97d2f96b5548 | -5.71289 | -45.66094 | 2026-07-18 04:17:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 24347370-b0f8-36b5-8419-e406cbc4af5d | -7.73169 | -47.24682 | 2026-07-18 04:17:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f351cfc9-16a0-3ac4-8ddf-5c1be0b9c1f5 | -5.74248 | -43.27122 | 2026-07-18 04:17:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 17951d04-3046-31ca-ae4c-866b8fc55bff | -7.84668 | -48.39657 | 2026-07-18 04:17:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 33002b53-cc03-3194-8dc2-430f8633aea6 | -8.12485 | -47.87493 | 2026-07-18 04:17:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| f2e79f62-f524-3d31-a9f0-0a8193fd4de6 | -7.47939 | -46.67107 | 2026-07-18 04:17:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| eaf63d6f-cfc5-3965-982f-e3664da7e7cc | -6.60397 | -41.62588 | 2026-07-18 04:17:00 | NPP-375D | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 9c143868-bb5c-387e-a02b-08e06e8845d0 | -5.92704 | -43.64655 | 2026-07-18 04:17:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| f1f824d3-bfa9-3c29-8cc7-fd0ebcc48140 | -5.74647 | -43.26811 | 2026-07-18 04:17:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a3fdbb0c-be3f-3451-872e-f6bdaccae3f1 | -5.93106 | -43.65816 | 2026-07-18 04:17:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 189e44ae-4be8-3375-a4a7-63dd0df39dff | -6.60342 | -41.62935 | 2026-07-18 04:17:00 | NPP-375D | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 071ba9b4-6b4e-3e78-ae83-e2a46a04acbc | -6.10944 | -46.18487 | 2026-07-18 04:17:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dca5b6d6-3a9f-3231-acf7-d82a8fbab4b1 | -5.35337 | -49.16938 | 2026-07-18 04:17:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 3692c7a0-994a-3c83-a3c3-27044e3b4012 | -7.91372 | -48.26617 | 2026-07-18 04:17:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a0825453-2b18-381c-8151-6ccb4f22f6f9 | -5.80633 | -45.11726 | 2026-07-18 04:17:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 17846d61-7b62-3611-a2b0-37aa5a9bfe99 | -5.5268 | -45.27074 | 2026-07-18 04:17:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a8b76ba5-3a9d-3493-ba08-d429ac1ce32f | -6.94451 | -44.14946 | 2026-07-18 04:17:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 0.4 |
| c479123d-7252-3bf5-891c-42a3e75f1e24 | -6.67185 | -47.52131 | 2026-07-18 04:17:00 | NPP-375D | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 773eb7a7-afba-3c36-9a99-df44bb65bd13 | -5.71047 | -45.66253 | 2026-07-18 04:17:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1ef00a56-41e4-3d69-825e-3e0093e89ac6 | -7.85048 | -48.39507 | 2026-07-18 04:17:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ae068cd8-6cd1-33a2-b80a-b3307f938e2d | -5.93353 | -43.64314 | 2026-07-18 04:17:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a9391491-5b32-3538-b3da-af0b83325fc1 | -6.74128 | -47.13258 | 2026-07-18 04:17:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7f1ac2a9-0029-359e-90e3-3d3d33f557a0 | -7.85489 | -48.39579 | 2026-07-18 04:17:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a698937e-86d0-3df8-ac06-bc154f026696 | -7.84973 | -48.39931 | 2026-07-18 04:17:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b9ec2bc0-67c9-3f4b-861d-4a4873de131a | -8.12554 | -47.87093 | 2026-07-18 04:17:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f20117d9-4960-3046-a26e-f3f85d30e6c7 | -7.48024 | -46.66596 | 2026-07-18 04:17:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| cbe44a39-13c4-39bb-a143-59ee6100f4fa | -5.93213 | -43.65894 | 2026-07-18 04:17:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7d3a97bc-86dc-3803-a248-a28f1287a7c3 | -5.93152 | -43.66272 | 2026-07-18 04:17:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 89f81eba-7d4a-3bc2-b09e-ccf2f9b2d6d8 | -7.85037 | -48.40155 | 2026-07-18 04:17:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7298d92a-4ea5-32b3-9126-38d8a9ecb1b6 | -5.93389 | -43.66251 | 2026-07-18 04:17:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e3cbbad6-2f22-3c4a-8f33-20121fef18ea | -5.92764 | -43.64278 | 2026-07-18 04:17:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 3ccdcec9-79fe-3cdd-a29a-55df121731e8 | -7.72761 | -47.24607 | 2026-07-18 04:17:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cb88d416-2a1a-37b1-a7f3-5fc29922c38d | -6.67606 | -47.52215 | 2026-07-18 04:17:00 | NPP-375D | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3b97acc9-a0ca-3103-b577-f4360c063c1c | -7.28785 | -46.25754 | 2026-07-18 04:17:00 | NPP-375D | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 43572ff6-35ef-3e3f-ab32-9f88d1d48681 | -7.29171 | -46.25824 | 2026-07-18 04:17:00 | NPP-375D | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3fef69ee-d2c3-3a91-aebc-337cab188edb | -5.80264 | -45.11661 | 2026-07-18 04:17:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 3796c912-dfdb-347a-99dc-5ac319e61e6e | -5.80462 | -45.11561 | 2026-07-18 04:17:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fcaa7a29-3ab0-34b2-ad29-7b11e3c098b6 | -7.91519 | -48.25772 | 2026-07-18 04:17:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| d1a456a4-cedb-3951-962f-6dadc2754bae | -5.93454 | -43.6439 | 2026-07-18 04:17:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 44f027d8-d0bf-3785-b359-cf28e8504e9b | -5.7121 | -45.66563 | 2026-07-18 04:17:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4e579496-e1f6-3f4f-a175-cb1a3e0f6387 | -5.89662 | -46.21197 | 2026-07-18 04:17:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1366712f-f481-3d8c-9edf-baab901fc393 | -5.9242 | -43.64222 | 2026-07-18 04:17:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 6cbb5eee-4357-338a-984b-3db7d078fec0 | -5.93415 | -43.63937 | 2026-07-18 04:17:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c507c903-7740-329b-bf8c-b8cc628c7330 | -5.89744 | -46.20709 | 2026-07-18 04:17:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3f6a5b5c-a87f-3786-8cfe-1085efd3288c | -7.48207 | -46.66868 | 2026-07-18 04:17:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d46ec0e8-93cb-38a3-bf31-f24a1565eac3 | -5.59668 | -45.33965 | 2026-07-18 04:17:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a338fd0e-a2e9-3a8f-bcfb-132fd39ee4d2 | -7.28399 | -46.25687 | 2026-07-18 04:17:00 | NPP-375D | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 56ab735f-60f1-36af-97e9-91aed959c8c0 | -15.70635 | -43.37999 | 2026-07-18 04:19:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 1a336f48-d3ab-3902-a4de-88022fa645f0 | -9.51204 | -47.13688 | 2026-07-18 04:19:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f58d6249-9a19-3ac6-bcad-2c5b08b4d47f | -5.11925 | -43.23709 | 2026-07-18 04:19:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| cdbf3af6-d72b-305b-8922-6c77ecef6775 | -16.12214 | -43.63714 | 2026-07-18 04:19:00 | NPP-375D | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0e5fd604-e876-3975-9516-41b9dc4bdea2 | -15.70911 | -43.38415 | 2026-07-18 04:19:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| bb1e7643-bf3e-37d0-9487-61be543899d0 | -9.61204 | -47.75987 | 2026-07-18 04:19:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1c3fb755-7428-3552-9658-9783c2dab1bf | -8.93944 | -47.60934 | 2026-07-18 04:19:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cfd9e07d-928b-30c4-95b8-a7f924d95544 | -5.11985 | -43.23339 | 2026-07-18 04:19:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a1dde264-1ff9-3054-9cb1-3adb500796e6 | -9.51686 | -47.13247 | 2026-07-18 04:19:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| af79cbf3-7287-3168-9099-95116a6a38d1 | -8.47201 | -50.22265 | 2026-07-18 04:19:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fc6f2c99-d5d0-3e79-ab60-17e09dee6859 | -9.51115 | -47.14203 | 2026-07-18 04:19:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d243f758-4f51-3969-b4ea-1f0c7088f007 | -13.55708 | -47.78412 | 2026-07-18 04:19:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 887944ac-0b4a-3088-8ec9-3772099a9403 | -8.47595 | -50.22911 | 2026-07-18 04:19:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c53414dd-1331-30cf-8d4b-2f07b9274fe4 | -8.71295 | -49.60743 | 2026-07-18 04:19:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 647a0b6c-4c15-34ad-8abe-3f8c465170ec | -4.10148 | -49.35472 | 2026-07-18 04:19:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 32e8d0ee-df6c-3540-9bc7-a45610c9a521 | -11.79368 | -45.94421 | 2026-07-18 04:19:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 43c9c8b7-e5cb-3c6e-8d5b-d6c44cf51619 | -13.31449 | -45.15125 | 2026-07-18 04:19:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 4e8f3db0-8a20-331b-bd82-c2af61922897 | -12.23598 | -44.63003 | 2026-07-18 04:19:00 | NPP-375D | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 2a4a0988-2c24-3e71-97ff-7ff61e4bd0cf | -12.76365 | -52.16033 | 2026-07-18 04:19:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 394517c8-0197-3f7c-b329-cb70f90999fd | -13.99768 | -54.00199 | 2026-07-18 04:19:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cdf8fbe7-1c8a-37d4-8607-e8ec0937b073 | -9.99811 | -43.43371 | 2026-07-18 04:19:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8a4fd3d4-b3f3-3628-9a05-be501166dce9 | -2.78986 | -49.52729 | 2026-07-18 04:19:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 569a0dfb-ea47-3416-9b32-1211b89d0f32 | -12.68645 | -48.21149 | 2026-07-18 04:19:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 0a6e8e57-7b5f-3db1-a6c9-d0f3c9e5f3f5 | -11.54958 | -48.26011 | 2026-07-18 04:19:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 63ecd91c-640d-3b80-b8f3-b0bcf1a9b7d6 | -9.70111 | -47.70002 | 2026-07-18 04:19:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b512d555-60e5-340c-8dd1-533c03aee7f8 | -12.45598 | -49.58825 | 2026-07-18 04:19:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 5bc8c35b-ddff-32f8-b8a0-2e8e0ab7a37d | -8.47102 | -50.22824 | 2026-07-18 04:19:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cec603cd-f764-3c98-9724-75f03b829772 | -13.31853 | -45.14809 | 2026-07-18 04:19:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 31dc6fc6-60e5-3c64-887f-6de11d305ffc | -12.79856 | -46.56636 | 2026-07-18 04:19:00 | NPP-375D | COMBINADO | TOCANTINS | Brasil | 1705557 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 4d899410-012f-30bf-b911-5f8f9a298b36 | -15.24418 | -48.57634 | 2026-07-18 04:19:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5744878d-7fe5-3754-9170-d868f99b9a07 | -10.65101 | -47.23424 | 2026-07-18 04:19:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a2cca7f0-b6f2-3125-aa15-c10ccb981eae | -9.64929 | -44.83273 | 2026-07-18 04:19:00 | NPP-375D | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 3729504c-29b5-3966-83c5-979495e3cf07 | -13.3117 | -45.14689 | 2026-07-18 04:19:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 26.9 |
| 9ccc2553-2016-39ae-bb62-0519a68b46b7 | -13.99688 | -54.00594 | 2026-07-18 04:19:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |


[Clique aqui para ver as próximas entradas](README7.md)
