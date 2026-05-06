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
| a8520cc5-c48c-3ca3-8e05-693a93681fa4 | -21.70941 | -48.42452 | 2026-05-06 05:29:00 | NPP-375D | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 8d597e99-b017-3804-94c2-ff233707e047 | -12.5033 | -58.4781 | 2026-05-06 05:30:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 56.0 |
| c5918d6e-2ddc-326b-8298-e89d33a27777 | -12.5033 | -58.4781 | 2026-05-06 05:40:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 50.7 |
| 2f1f3ff7-b02e-375d-8e1b-deb0b593871c | -13.69806 | -55.68318 | 2026-05-06 05:46:00 | NOAA-20 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3fadd658-1d90-31ee-9fd6-67220cdfacd2 | -12.4953 | -58.47072 | 2026-05-06 05:46:00 | NOAA-20 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 6effc3db-b46a-3751-9e26-1535a9d046cd | -16.1556 | -58.49157 | 2026-05-06 05:46:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 5b5b5170-ec91-31a1-b2fe-240520391d99 | -16.42849 | -57.26993 | 2026-05-06 05:46:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| f2e93166-bc73-33bc-94c4-e4e585b524f0 | -12.50523 | -58.47197 | 2026-05-06 05:46:00 | NOAA-20 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 49eb109b-2b1d-3a69-9aea-41978e17b5d5 | -12.49307 | -58.48806 | 2026-05-06 05:46:00 | NOAA-20 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 38f51785-644e-3b8e-9e3f-f8189a847b7c | -11.63612 | -54.16309 | 2026-05-06 05:46:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f1727a85-f627-3ffc-80e4-829d3ec16655 | -11.85703 | -63.71823 | 2026-05-06 05:46:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b71ac6fd-38ff-3920-87d8-cf50a10c633f | -12.49951 | -58.47722 | 2026-05-06 05:46:00 | NOAA-20 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| ec379ddb-1d8c-31f0-808f-44f7c9a3010b | -12.50372 | -58.48365 | 2026-05-06 05:46:00 | NOAA-20 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| bc74fb9e-e59d-3215-a5ad-76dd0a0c223d | -11.4436 | -55.10473 | 2026-05-06 05:46:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ae735642-6db4-3763-b574-a23ec55406ef | -11.44895 | -55.10833 | 2026-05-06 05:46:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 058f2c1a-0a05-349a-941f-36c30434aa5a | -13.69753 | -55.68776 | 2026-05-06 05:46:00 | NOAA-20 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5bd7ec0c-94ba-3871-a9de-65f893b49e74 | -12.5102 | -58.47262 | 2026-05-06 05:46:00 | NOAA-20 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 8.4 |
| f8c86b35-5bd0-316a-9d15-fc8360269f51 | -11.43676 | -55.10669 | 2026-05-06 05:46:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| d5d9c6d4-f45d-3ebe-bd84-5f191bad03ad | -12.49802 | -58.48875 | 2026-05-06 05:46:00 | NOAA-20 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 27bbc2e1-29a1-3ab8-9d46-21a86d05092a | -13.69701 | -55.6923 | 2026-05-06 05:46:00 | NOAA-20 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8529878e-7dcc-3545-a3f3-97d0977de9fb | -11.43734 | -55.10199 | 2026-05-06 05:46:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 3b6974ad-fa77-396b-b4d5-14520aa3b64d | -16.4289 | -57.26602 | 2026-05-06 05:46:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 085d115c-d30c-376c-856e-c773e56567e1 | -12.29515 | -57.56622 | 2026-05-06 05:46:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 600edc13-03e2-32f6-bda3-f7d9607ad988 | -16.16013 | -58.49198 | 2026-05-06 05:46:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 9acb27b0-1bed-3010-add8-75dc34061910 | -11.44344 | -55.10279 | 2026-05-06 05:46:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 5a4971d9-8c30-3ef5-888d-91fef576b0c1 | -12.50868 | -58.4843 | 2026-05-06 05:46:00 | NOAA-20 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 1d43c2cd-bdb9-3055-be98-289977962581 | -12.50944 | -58.47847 | 2026-05-06 05:46:00 | NOAA-20 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 833444f8-e8b2-3a8d-8afe-7b5239409721 | -12.29555 | -57.56298 | 2026-05-06 05:46:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a310df87-01a0-3ce0-ab4f-f59d3237d8ab | -12.49381 | -58.48235 | 2026-05-06 05:46:00 | NOAA-20 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| e0b92a61-7931-363b-880a-f0aee5466ce8 | -12.50448 | -58.47781 | 2026-05-06 05:46:00 | NOAA-20 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 8.4 |
| c6658a22-d344-3812-bfef-0dcb653db8ef | -16.16081 | -58.49225 | 2026-05-06 05:46:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 0e8c6cc5-1d73-3f02-9c8b-f8f5c8eeb8e3 | -12.50027 | -58.47136 | 2026-05-06 05:46:00 | NOAA-20 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| ee968a46-16c7-3ca9-b84c-b6f96a51faaf | -9.42101 | -65.61295 | 2026-05-06 05:46:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 8a65d13d-f869-33a1-b2a8-96ddd9eb4b53 | -16.15973 | -58.49525 | 2026-05-06 05:46:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 211c9538-f2aa-34ec-b6d4-9f823903944a | -12.49876 | -58.48302 | 2026-05-06 05:46:00 | NOAA-20 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| bedafdd6-09fa-30ae-bd5a-9595da7c7780 | -18.50005 | -55.51038 | 2026-05-06 05:48:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 9180b37c-244e-3d30-9d0b-1b67fba49b18 | -21.98176 | -57.59412 | 2026-05-06 05:48:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 3.9 |
| c7c65222-4f2f-31cf-a81f-a9c437ff57f1 | -21.97387 | -57.59032 | 2026-05-06 05:48:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 81cf10e5-51dd-35da-b137-c432b138fd0c | -21.97344 | -57.59534 | 2026-05-06 05:48:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4bc67aaa-619d-34bc-a389-eca0e8233b07 | -18.49951 | -55.51593 | 2026-05-06 05:48:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 5a676ad4-9c6f-3dfc-963b-1c0fa3ffd065 | -21.97933 | -57.5963 | 2026-05-06 05:48:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3d0f9a74-612a-366e-b3c8-6e0b8846ac20 | -19.94817 | -54.37923 | 2026-05-06 05:48:00 | NOAA-20 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 804cee2c-c811-3b19-9add-42a2464ee5f0 | -21.97978 | -57.59108 | 2026-05-06 05:48:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d9a0352b-9460-31dc-83dd-fa138c3094e6 | -21.97585 | -57.59349 | 2026-05-06 05:48:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 4c94fb23-0ca6-3775-8ba0-afabc0f25e2b | -12.5033 | -58.4781 | 2026-05-06 06:00:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 49.8 |
| 85af97a2-1b19-3664-a992-e1ea5ac9797f | -20.787 | -51.6635 | 2026-05-06 06:10:00 | GOES-19 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Mata Atlântica | 64.1 |
| e64a4a7b-ec07-3e72-b9a2-6ef4ea85028f | -20.787 | -51.6635 | 2026-05-06 06:20:00 | GOES-19 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Mata Atlântica | 79.3 |
| 4cd37b84-edfa-3cc7-ab9c-caeb33c00770 | -12.38859 | -46.32109 | 2026-05-06 06:22:00 | AQUA_M-M | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| cc8ce32a-a959-324c-8d42-625a10daa6bb | -11.13079 | -45.14061 | 2026-05-06 06:22:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 14.4 |
| a990de85-8345-3e9b-8093-0f1ab7091d47 | -11.13219 | -45.13108 | 2026-05-06 06:22:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 6ae76172-0cef-3b70-8606-6e46f2967b1a | -13.43827 | -43.84401 | 2026-05-06 06:22:00 | AQUA_M-M | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 21.7 |
| 16d725fd-2dde-3bb1-90cf-9d18edbc9fb6 | -12.34696 | -50.02386 | 2026-05-06 06:22:00 | AQUA_M-M | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 11.4 |
| e3b0b0be-f107-3fc5-915d-e039cb282078 | -13.43834 | -43.84964 | 2026-05-06 06:22:00 | AQUA_M-M | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 5adbc8e2-5277-3b01-99bb-fac979ce7a29 | -13.43992 | -43.83787 | 2026-05-06 06:22:00 | AQUA_M-M | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 1b6fd08c-a106-3cd9-b7db-01ace6806155 | -12.33904 | -50.01102 | 2026-05-06 06:22:00 | AQUA_M-M | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 20.9 |
| d1bb899c-d082-3ec1-ae4a-f614856e96d9 | -12.34881 | -50.01261 | 2026-05-06 06:22:00 | AQUA_M-M | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 10d81b72-4850-32de-af1f-60b9c8877a86 | -14.07091 | -47.79493 | 2026-05-06 06:25:00 | AQUA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 7.6 |
| c3f3dc79-6ca9-3dab-ae1f-cd8257018526 | -20.20825 | -50.6578 | 2026-05-06 06:25:00 | AQUA_M-M | URÂNIA | SÃO PAULO | Brasil | 3555802 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| f86a137c-e108-3232-b079-bb46bbac6037 | -20.2099 | -50.64768 | 2026-05-06 06:25:00 | AQUA_M-M | URÂNIA | SÃO PAULO | Brasil | 3555802 | 35 | 33 | nan | nan | nan | Mata Atlântica | 64.7 |
| fec90aaf-cf57-3c7b-b2c5-4a58b3baa172 | -20.79222 | -51.66549 | 2026-05-06 06:25:00 | AQUA_M-M | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Mata Atlântica | 29.2 |
| e430ad9e-0b7a-3c7d-8cca-a194d944ebcd | -21.70948 | -48.4222 | 2026-05-06 06:25:00 | AQUA_M-M | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 4725e78f-1b9f-3897-b1d9-4ef0d48a9787 | -20.79408 | -51.65448 | 2026-05-06 06:25:00 | AQUA_M-M | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Mata Atlântica | 112.5 |
| e4c59798-0439-3f6e-bae1-fe791539fa0d | -20.787 | -51.6635 | 2026-05-06 06:30:00 | GOES-19 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Mata Atlântica | 71.0 |
| 05cd4465-8f87-3a59-b1da-002fa28fb9b5 | -20.8074 | -51.6595 | 2026-05-06 06:40:00 | GOES-19 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Mata Atlântica | 62.0 |
| fcbf4257-fb22-3fb0-b008-c7ef95c1a53e | -20.787 | -51.6635 | 2026-05-06 06:40:00 | GOES-19 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Mata Atlântica | 79.6 |
| eee1f4e8-2e68-32f8-be3b-fc66bfdd4d80 | -20.787 | -51.6635 | 2026-05-06 06:50:00 | GOES-19 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Mata Atlântica | 82.6 |
| e4d2493b-b52a-319a-a501-6905245c44ce | -12.5033 | -58.4781 | 2026-05-06 07:00:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 50.2 |
| 0b837f03-bf08-3b4d-b228-5614a667794f | -20.8074 | -51.6595 | 2026-05-06 07:00:00 | GOES-19 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Mata Atlântica | 63.3 |
| eeee2148-f785-3c17-a250-8e6e0af5b9bc | -20.2237 | -50.6371 | 2026-05-06 07:10:00 | GOES-19 | URÂNIA | SÃO PAULO | Brasil | 3555802 | 35 | 33 | nan | nan | nan | Mata Atlântica | 64.7 |
| 40b7f007-5f2e-343c-bdc8-1c362f86022f | -20.2237 | -50.6371 | 2026-05-06 07:20:00 | GOES-19 | URÂNIA | SÃO PAULO | Brasil | 3555802 | 35 | 33 | nan | nan | nan | Mata Atlântica | 61.6 |
| 841be4d8-adcc-3a53-8f22-778015fae62b | -8.78677 | -44.83886 | 2026-05-06 11:19:00 | TERRA_M-M | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 22.1 |
| 7777c96f-9c65-3717-8f05-91e65fec193c | -11.83779 | -39.174 | 2026-05-06 11:21:00 | TERRA_M-M | CANDEAL | BAHIA | Brasil | 2906402 | 29 | 33 | nan | nan | nan | Caatinga | 8.8 |
| 5200da46-d519-3d86-9f0e-c08f981a086b | -13.44049 | -43.84533 | 2026-05-06 11:21:00 | TERRA_M-M | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 21.5 |
| a6897fd2-665e-3d31-9b06-fe6793d3f750 | -12.7699 | -42.74888 | 2026-05-06 11:21:00 | TERRA_M-M | BOQUIRA | BAHIA | Brasil | 2904100 | 29 | 33 | nan | nan | nan | Caatinga | 7.2 |
| 5b08141d-35a0-3deb-b654-a15d1c9b257e | -11.9498 | -43.3781 | 2026-05-06 11:50:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 100.4 |
| aa72352e-8579-3bd5-a247-7a50ae1fa968 | -11.9498 | -43.3781 | 2026-05-06 12:00:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 112.6 |
| 4bf12ca0-0478-3035-9d71-b1e23fe5cf76 | -11.9498 | -43.3781 | 2026-05-06 12:10:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 121.4 |
| 558ec62a-97f0-38dc-b42f-33f8973dc67b | -18.7844 | -51.9467 | 2026-05-06 12:10:00 | GOES-19 | APORÉ | GOIÁS | Brasil | 5201504 | 52 | 33 | nan | nan | nan | Cerrado | 125.0 |
| 235379eb-03f4-3aef-9e48-ebda88eb5ab5 | -18.7849 | -51.9247 | 2026-05-06 12:10:00 | GOES-19 | APORÉ | GOIÁS | Brasil | 5201504 | 52 | 33 | nan | nan | nan | Cerrado | 84.2 |
| 4f4b2b42-d687-33d8-aa5a-8bc951a1e248 | -18.7849 | -51.9247 | 2026-05-06 12:20:00 | GOES-19 | APORÉ | GOIÁS | Brasil | 5201504 | 52 | 33 | nan | nan | nan | Cerrado | 114.3 |
| 81ca69cc-2d17-3220-83e9-0f1a885fb305 | -18.7844 | -51.9467 | 2026-05-06 12:20:00 | GOES-19 | APORÉ | GOIÁS | Brasil | 5201504 | 52 | 33 | nan | nan | nan | Cerrado | 154.9 |
| 4024e0f0-c74c-30c9-a493-0127a5cb5295 | -11.9498 | -43.3781 | 2026-05-06 12:20:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 89.7 |
| 567b672f-11d0-3e0d-9e49-fa46e131499d | -12.5033 | -58.4781 | 2026-05-06 12:20:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 74.8 |
| 86a8325e-5a63-3da8-b48f-baf2ad6f0201 | -18.7849 | -51.9247 | 2026-05-06 12:30:00 | GOES-19 | APORÉ | GOIÁS | Brasil | 5201504 | 52 | 33 | nan | nan | nan | Cerrado | 96.5 |
| d8de8399-3587-3987-a0d4-e940e27bea05 | -18.7844 | -51.9467 | 2026-05-06 12:30:00 | GOES-19 | APORÉ | GOIÁS | Brasil | 5201504 | 52 | 33 | nan | nan | nan | Cerrado | 133.5 |
| e33b5d00-bf9c-35b3-97e9-9ecff0991867 | -12.5033 | -58.4781 | 2026-05-06 12:30:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 115.9 |
| 4bd6f262-e4f6-33c8-b7b4-7d30a67b1c23 | -12.5031 | -58.4979 | 2026-05-06 12:30:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 67.3 |
| b860e76b-2518-3a22-b17d-50024dbc51da | -12.5033 | -58.4781 | 2026-05-06 12:40:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 161.6 |
| 500da154-57b5-3c2f-86c0-85ebb978e1db | -12.5031 | -58.4979 | 2026-05-06 12:40:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 68.3 |
| 03b76c63-ab1e-3925-9ab7-32510fb79939 | -18.7849 | -51.9247 | 2026-05-06 12:40:00 | GOES-19 | APORÉ | GOIÁS | Brasil | 5201504 | 52 | 33 | nan | nan | nan | Cerrado | 81.2 |
| bf426efe-e8a0-3ae1-b979-c24533e4daed | -11.9498 | -43.3781 | 2026-05-06 12:40:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 85.3 |
| 171d2e87-4dd3-3ecb-be49-adf3bb44c77a | -18.7844 | -51.9467 | 2026-05-06 12:40:00 | GOES-19 | APORÉ | GOIÁS | Brasil | 5201504 | 52 | 33 | nan | nan | nan | Cerrado | 142.5 |
| 125ab48e-cab4-3f68-ab44-4ab9cdff3cf6 | -9.4259 | -50.683 | 2026-05-06 12:40:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 72.1 |
| 2540f2db-0282-3bcc-afc0-a7bcb00605ad | -12.4843 | -58.4795 | 2026-05-06 12:40:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 83.9 |
| 91753bd9-5d18-37a1-8925-1470356eaff0 | -12.5033 | -58.4781 | 2026-05-06 12:50:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 243.0 |
| fe980a08-bc6f-3a97-9c5d-446acbcce251 | -12.4843 | -58.4795 | 2026-05-06 12:50:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 93.5 |
| ae76a7b3-ae79-3cf8-8e8f-c40051e40183 | -18.7849 | -51.9247 | 2026-05-06 12:50:00 | GOES-19 | APORÉ | GOIÁS | Brasil | 5201504 | 52 | 33 | nan | nan | nan | Cerrado | 91.2 |
| 61f8109b-a2f6-3051-b0c4-0b178f37e920 | -12.5031 | -58.4979 | 2026-05-06 12:50:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 121.5 |
| 89f2f0b3-3db5-3c1b-b857-c786248c37a0 | -9.4259 | -50.683 | 2026-05-06 12:50:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 81.0 |
| 25155e5b-155c-3118-9fff-95fdb8f1d59d | -18.7844 | -51.9467 | 2026-05-06 12:50:00 | GOES-19 | APORÉ | GOIÁS | Brasil | 5201504 | 52 | 33 | nan | nan | nan | Cerrado | 179.6 |


[Clique aqui para ver as próximas entradas](README12.md)
