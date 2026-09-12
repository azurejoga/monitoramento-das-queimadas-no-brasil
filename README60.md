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

## Dados Diários - Página 60

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4d5b9877-e81e-3d6a-9c4c-6feada6b2f6a | -2.7331 | -57.6271 | 2026-09-12 13:50:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 62.7 |
| db74582e-b4e0-397b-9b1a-21d0cff33378 | -12.1388 | -48.9672 | 2026-09-12 13:50:00 | GOES-19 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 114.0 |
| 687a3234-629e-3e09-ab22-fff5dc96ab64 | -6.2429 | -51.6939 | 2026-09-12 13:50:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 59.8 |
| edf0b814-1ca5-31c4-ba56-228fcefb31d8 | -7.0166 | -44.6184 | 2026-09-12 13:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 426.1 |
| 2a6de628-8f72-3e04-8951-293c950b1272 | -11.3727 | -46.8074 | 2026-09-12 13:50:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 167.4 |
| c87d7a71-d7fd-36eb-8a24-4ee75ca96e51 | -8.951 | -49.533 | 2026-09-12 13:50:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 106.3 |
| ae025144-cbf7-3f83-822e-9cd57fea6171 | -10.2206 | -50.373 | 2026-09-12 13:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 129.3 |
| 5e4822bd-5bc8-34b5-834e-5da588117de8 | -11.383 | -43.9614 | 2026-09-12 13:50:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 169.8 |
| 6b919292-a1a6-346b-9f9f-1efea2856d5a | -10.6829 | -54.1475 | 2026-09-12 13:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 63.1 |
| 6627ea0d-aa87-3b2c-a503-34a1e5f2e1b8 | -7.6008 | -46.1288 | 2026-09-12 13:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 233.6 |
| 45f0142a-1c39-355e-a1e2-d69a65836082 | -11.4026 | -43.935 | 2026-09-12 13:50:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 347.5 |
| 4cd9cc50-84e4-34cb-b0f2-733781179e09 | -11.3723 | -46.8299 | 2026-09-12 13:50:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 122.9 |
| 79e4c9d1-d502-3a5b-8812-37698643a2bf | -9.7223 | -48.0907 | 2026-09-12 13:50:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 75.6 |
| 3bff9ff6-b397-37e9-af62-00d425444104 | -8.8249 | -46.0313 | 2026-09-12 13:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 63.3 |
| 3481ad81-731d-3f03-92ef-64a2806fc0af | -8.5415 | -54.7187 | 2026-09-12 13:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 209.0 |
| 9f09199c-b97e-3e51-ad14-d4b6bfcd15e8 | -7.9645 | -43.9971 | 2026-09-12 13:50:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 107.7 |
| f3d6abec-50ac-3fcc-b1fc-84ebd85037df | -11.3723 | -46.8299 | 2026-09-12 14:00:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 194.7 |
| 38e12d8f-74c0-3fc4-9b0d-cb7b31aef3b1 | -12.1388 | -48.9672 | 2026-09-12 14:00:00 | GOES-19 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 121.4 |
| 8ed488bc-dee5-3743-b3c3-075d3765eb39 | -7.6008 | -46.1288 | 2026-09-12 14:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 393.4 |
| b0dbf2ec-6a88-3eb0-b991-722868868a98 | -11.3731 | -46.7849 | 2026-09-12 14:00:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 134.4 |
| 053c19e2-5d12-3be3-aa6a-f6035eef8fae | -11.4021 | -43.9585 | 2026-09-12 14:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 278.3 |
| f157f58d-2f73-380b-86a1-f872b0694b44 | -10.6827 | -54.1679 | 2026-09-12 14:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 102.5 |
| a5343132-5a0f-3185-935c-b4ca2e13e1f1 | -2.7148 | -57.6274 | 2026-09-12 14:00:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 67.2 |
| 935c4530-7667-30ea-a3ef-d17f0509cabf | -6.2243 | -51.6949 | 2026-09-12 14:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 70.0 |
| fcfbdfa4-5c9e-3d62-9713-9f2e76dba606 | -10.2206 | -50.373 | 2026-09-12 14:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 101.9 |
| 23947565-c45c-37c5-aacf-be9bd0c58d33 | -11.3727 | -46.8074 | 2026-09-12 14:00:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 355.6 |
| 9c72f44e-638a-3129-b549-05d2012bac2d | -2.7331 | -57.6271 | 2026-09-12 14:00:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 61.1 |
| 3b0bd1ec-f1d0-3c29-9c65-32601b547660 | -10.2171 | -45.2799 | 2026-09-12 14:00:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 127.4 |
| 34b20236-6f95-3880-bfc7-52a92ad1a649 | -10.7015 | -54.1663 | 2026-09-12 14:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 130.8 |
| 7ee512b1-384e-33b0-b09f-9632565509de | -8.2203 | -55.2427 | 2026-09-12 14:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 71.5 |
| 836ade94-ac0a-3f8b-9461-dfd62d5672e1 | -8.2201 | -55.2627 | 2026-09-12 14:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 92.0 |
| d8197efd-4397-3cb5-8c6f-8a139b957a6e | -8.7943 | -46.9514 | 2026-09-12 14:00:00 | GOES-19 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 59.5 |
| c883e420-8aec-3fde-b483-7803eb0bdda0 | -10.7018 | -54.1458 | 2026-09-12 14:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 71.1 |
| a7514d5c-e2f1-3c34-9a8d-6fad601755cb | -7.9645 | -43.9971 | 2026-09-12 14:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 124.3 |
| 20c81a03-03ce-3c78-a04f-4ea2e4af0971 | -7.0166 | -44.6184 | 2026-09-12 14:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 331.3 |
| ab76b990-0d2b-3764-9f67-5fb7c1d158f4 | -11.3825 | -43.9849 | 2026-09-12 14:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 102.0 |
| 6051d956-d5c4-3047-b29e-3034888e23fa | -11.4218 | -43.9321 | 2026-09-12 14:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 442.1 |
| 92cdbddc-3fc9-3158-8c05-acbae4679766 | -10.7359 | -46.1465 | 2026-09-12 14:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 142.5 |
| 0ca3b509-7d8b-3d58-9e97-c9f456382aef | -11.4026 | -43.935 | 2026-09-12 14:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 664.7 |
| bb2b8bd9-849b-33e3-b059-50ca75d9e6b8 | -7.2147 | -43.7001 | 2026-09-12 14:00:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 135.4 |
| 05239042-e44c-3b6e-ab77-4888c7680901 | -11.4213 | -43.9556 | 2026-09-12 14:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 171.3 |
| ec0ee775-b621-3f25-9022-40eefc578b4f | -8.5229 | -54.72 | 2026-09-12 14:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 62.0 |
| c04edb8d-fb7c-3f77-837f-62d5772b60d6 | -6.2429 | -51.6939 | 2026-09-12 14:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 64.3 |
| 5104809c-bd2e-374a-85f8-55fb85ea6472 | -12.1391 | -48.9453 | 2026-09-12 14:00:00 | GOES-19 | SUCUPIRA | TOCANTINS | Brasil | 1720853 | 17 | 33 | nan | nan | nan | Cerrado | 77.8 |
| 5db3b4b1-6bba-3f91-bb4d-68de7e8d2dac | -6.5004 | -47.5909 | 2026-09-12 14:00:00 | GOES-19 | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 111.2 |
| 3cffa8fc-47d3-3bb9-b1f3-a9b102206350 | -5.1254 | -55.9748 | 2026-09-12 14:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 61.6 |
| ef9c80a5-f23a-3b88-9978-99f7495d5e1a | -14.5912 | -52.6673 | 2026-09-12 14:00:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 139.8 |
| 40c2acfa-63f7-34a0-9c29-07cf004e7d6d | -9.6951 | -43.3981 | 2026-09-12 14:00:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 88.5 |
| 2e72b958-3a37-3a24-ba47-09247426dcb4 | -10.7539 | -46.212 | 2026-09-12 14:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 84.9 |
| bcdff71d-b5a2-3d07-a524-c23400907358 | -10.2926 | -45.3161 | 2026-09-12 14:00:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 52.6 |
| cec2f27f-8d18-3818-a048-3dde83673690 | -4.9335 | -42.8813 | 2026-09-12 14:00:00 | GOES-19 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 87.4 |
| 775f606d-e392-37a4-b5da-f3df7434ea7d | -8.5417 | -54.6985 | 2026-09-12 14:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 185.4 |
| baa8722d-f578-3514-aeb7-1df35256431c | -6.5002 | -47.6128 | 2026-09-12 14:00:00 | GOES-19 | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 62.5 |
| e3e123b3-b242-3c42-a278-448964a4d602 | -12.1579 | -48.9647 | 2026-09-12 14:00:00 | GOES-19 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 87.4 |
| ff783030-b7ce-3d49-9362-9c1514ff1846 | -10.5664 | -51.356 | 2026-09-12 14:00:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 119.4 |
| dde5d4ce-ba0d-3567-a1dc-d051468d8327 | -8.5415 | -54.7187 | 2026-09-12 14:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 210.2 |
| d5621498-58ec-3fbd-a37d-e74cb2ae39fa | -11.372 | -46.8524 | 2026-09-12 14:00:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 81.3 |
| 15ffacd4-5df8-383c-8f75-dbf64b37d6f1 | -6.9036 | -44.6512 | 2026-09-12 14:00:00 | GOES-19 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 80.8 |
| 65a24b35-68c2-3dc7-8d60-7a639363d86a | -10.7168 | -46.1489 | 2026-09-12 14:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 180.9 |
| 2d313b34-3359-3d11-b8df-fba6e7b8ca59 | -10.9491 | -48.3474 | 2026-09-12 14:00:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 81.9 |
| 6db87945-2d69-3477-b8b2-ca694ee91d7f | -8.043 | -43.7565 | 2026-09-12 14:00:00 | GOES-19 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Caatinga | 104.1 |
| 6b7b5af2-2fa4-382a-aeca-0d104dc1ca14 | -11.4026 | -43.935 | 2026-09-12 14:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 516.5 |
| b11cab83-7627-3c0b-8c6a-415772122d6d | -11.4836 | -50.7293 | 2026-09-12 14:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 169.5 |
| 84820a2a-2acd-3693-8be9-e0b45d978ced | -8.8132 | -46.9495 | 2026-09-12 14:10:00 | GOES-19 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 73.5 |
| 1505f39c-3403-3a01-ab35-ab4664c55b5f | -8.002 | -44.0163 | 2026-09-12 14:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 77.5 |
| a8801597-778e-3160-9b62-e692bdcf2bab | -12.1388 | -48.9672 | 2026-09-12 14:10:00 | GOES-19 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 147.1 |
| 7fdafc26-0684-32f0-9354-d424ffd80519 | -2.9395 | -50.3994 | 2026-09-12 14:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 131.7 |
| 8323b52b-ddbe-38b8-b944-f25cb74c22d1 | -6.6206 | -58.8483 | 2026-09-12 14:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 76.0 |
| 832e6c94-ca94-306d-b610-7756e72cdc25 | -11.4021 | -43.9585 | 2026-09-12 14:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 268.4 |
| bab66a7d-90d4-3218-a39c-3bde6bf9d9be | -11.4213 | -43.9556 | 2026-09-12 14:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 178.6 |
| 87dc3ead-5791-3f0d-95e2-97b971050056 | -12.1579 | -48.9647 | 2026-09-12 14:10:00 | GOES-19 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 91.2 |
| ce9a69b5-411d-3364-86fe-a6931f489e39 | -11.403 | -43.9114 | 2026-09-12 14:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 148.8 |
| 9150e23b-49f8-3351-871a-999035e19386 | -11.1032 | -50.8135 | 2026-09-12 14:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 75.5 |
| bfd62379-1afa-32d1-818b-167027b13f81 | -10.9491 | -48.3474 | 2026-09-12 14:10:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 76.9 |
| 8c9e638f-1dfb-38e3-84ea-f8b1fee8eb39 | -6.2429 | -51.6939 | 2026-09-12 14:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 66.0 |
| 619cd94c-a1e8-3d67-b437-fd6fad74ae79 | -7.0166 | -44.6184 | 2026-09-12 14:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 342.6 |
| e5a3d6ec-2427-3322-9f00-0fde960f97bb | -10.7018 | -54.1458 | 2026-09-12 14:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 98.2 |
| 6985f331-4a31-305b-ad53-b2b50a8b0c76 | -2.7148 | -57.6274 | 2026-09-12 14:10:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 60.7 |
| fef00345-6cb8-34af-a1b8-12b46a0683ef | -6.2243 | -51.6949 | 2026-09-12 14:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 65.3 |
| 0929a4ab-d1bd-3460-b06a-3dbec8f7db5d | -6.5004 | -47.5909 | 2026-09-12 14:10:00 | GOES-19 | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 74.9 |
| dee97058-a17f-3d00-8357-bf44549a1da8 | -7.6008 | -46.1288 | 2026-09-12 14:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 257.4 |
| f3a124e6-4c94-39d0-8f8d-db26dc0e25be | -13.3825 | -48.0015 | 2026-09-12 14:10:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 59.0 |
| 112e7535-5994-3721-ba64-cdaab8f368a2 | -11.3723 | -46.8299 | 2026-09-12 14:10:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 114.9 |
| ae73c5f9-29a4-36c4-ab68-6d731e4fb39b | -8.043 | -43.7565 | 2026-09-12 14:10:00 | GOES-19 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Caatinga | 82.3 |
| 936b0d78-e127-362d-b376-173042aa8515 | -11.383 | -43.9614 | 2026-09-12 14:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 106.8 |
| 5e6bd384-d9ff-3200-bb9b-1d7aab1df695 | -8.2203 | -55.2427 | 2026-09-12 14:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 80.4 |
| 99b749ed-8fa4-3fb1-a229-02397eef6510 | -6.8977 | -38.5802 | 2026-09-12 14:10:00 | GOES-19 | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 83.7 |
| 76654ea6-0eaa-3754-91f8-728de9402b17 | -8.2201 | -55.2627 | 2026-09-12 14:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 86.8 |
| 1197df5e-63bc-39ea-95bc-9d840d9693d8 | -10.2735 | -45.3185 | 2026-09-12 14:10:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 99.4 |
| a3362c18-54c0-384e-b457-f15badb2b7c1 | -10.6829 | -54.1475 | 2026-09-12 14:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 96.5 |
| f3fa661b-909f-33c1-9ced-0e4acedfd74d | -11.8193 | -46.3633 | 2026-09-12 14:10:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 46.8 |
| 8cd5f339-5839-3706-b71c-7977f3cf1795 | -10.6827 | -54.1679 | 2026-09-12 14:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 180.7 |
| 6a1a619c-5d1a-3195-bf06-defaa1309dd6 | -7.9645 | -43.9971 | 2026-09-12 14:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 112.7 |
| ef542afe-4138-3003-bccc-f73c846b9d28 | -10.7015 | -54.1663 | 2026-09-12 14:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 188.2 |
| 7aec143e-3ec9-33fd-869f-9b9778ee2093 | -10.5664 | -51.356 | 2026-09-12 14:10:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 195.4 |
| 83385712-57f0-3e7a-9c50-f65c1baeef3a | -14.5912 | -52.6673 | 2026-09-12 14:10:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 167.3 |
| 16bcc96e-6ae0-3b43-8287-f9d3b1b353c6 | -9.6951 | -43.3981 | 2026-09-12 14:10:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 92.0 |
| 11dd13c0-2402-3cbd-b5f6-46ca5bc4165f | -8.5229 | -54.72 | 2026-09-12 14:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 64.3 |
| 131c0ea4-d6e3-3dd8-b666-e5c410e09a3d | -4.8676 | -56.0039 | 2026-09-12 14:10:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 60.7 |
| 765bb2f9-9690-308c-8b63-4e9af1f29c84 | -11.3825 | -43.9849 | 2026-09-12 14:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 106.2 |


[Clique aqui para ver as próximas entradas](README61.md)
