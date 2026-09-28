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

## Dados Diários - Página 69

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7d09715e-d55e-3359-a8e7-7c02354dc540 | -11.3958 | -45.4203 | 2026-09-28 10:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 99.1 |
| 33f55ba4-1309-3607-b36e-0c4d1cf83932 | -11.1962 | -44.8037 | 2026-09-28 10:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 148.7 |
| 2cb003ac-4a8e-3c15-b052-d3c6d8fbd8dd | -12.6643 | -47.3245 | 2026-09-28 10:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 98.8 |
| 02c790be-246a-39a0-a4b9-81bf7ec54dce | -12.6263 | -47.3075 | 2026-09-28 10:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 81.2 |
| 90e65ee5-ccf6-3720-8861-a3e5feeeeae9 | -13.468 | -48.5881 | 2026-09-28 10:40:00 | GOES-19 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 153.2 |
| 43d5c688-2dbb-3882-ae54-3fc9b56ec02a | -15.2038 | -46.1606 | 2026-09-28 10:40:00 | GOES-19 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 177.0 |
| 245b055b-f78a-3a15-8cc6-dc8b6b72146b | -11.1771 | -44.8064 | 2026-09-28 10:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 142.8 |
| 8f9e8d5e-7d0d-3ee0-9e83-90640339e052 | -7.3813 | -42.12442 | 2026-09-28 10:43:00 | TERRA_M-M | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 81.7 |
| f2b4cef9-0a6a-3a40-a235-7eeaa80b1e94 | -7.37523 | -42.11576 | 2026-09-28 10:43:00 | TERRA_M-M | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 51.1 |
| f22e6ae6-a987-38f6-a310-394192aba4c6 | -13.161 | -48.5437 | 2026-09-28 11:00:00 | GOES-19 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 143.1 |
| dd91f13a-8f22-30c0-b781-ddfe07339145 | -11.1966 | -44.7805 | 2026-09-28 11:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 89.2 |
| 051e3593-6b50-3b50-863e-553a879c334a | -11.8641 | -47.1004 | 2026-09-28 11:00:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 76.8 |
| 6f8763c4-ab04-3279-a37a-fb46f12c9bf4 | -11.1962 | -44.8037 | 2026-09-28 11:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 178.1 |
| bac7fd3b-3139-3187-9136-264c8aa6ebc2 | -11.1775 | -44.7832 | 2026-09-28 11:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 101.9 |
| 2c10faf4-13ae-305c-8b58-2813ce5a5fe2 | -12.6836 | -47.3217 | 2026-09-28 11:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 89.3 |
| 3a66e266-defa-3b44-a303-97deefcbd674 | -13.4676 | -48.6102 | 2026-09-28 11:00:00 | GOES-19 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 89.6 |
| 47ebac37-d579-32e9-9f1b-e17621ebfe78 | -13.468 | -48.5881 | 2026-09-28 11:00:00 | GOES-19 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 107.5 |
| 53ce928e-0c2a-33f9-9e28-32bc7a0a3424 | -12.6832 | -47.3442 | 2026-09-28 11:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 84.4 |
| 16d9dcbd-1728-3064-8ae7-6c883a5c486b | -12.6263 | -47.3075 | 2026-09-28 11:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 110.3 |
| 90fe0cf5-a272-3e35-bc1b-8b86692e903d | -11.1771 | -44.8064 | 2026-09-28 11:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 171.8 |
| e4876f18-9948-3b55-9cec-c284d0dc22e6 | -12.7024 | -47.3414 | 2026-09-28 11:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 84.9 |
| 0e545f1e-0225-397b-ac5b-8613d7986fab | -12.6836 | -47.3217 | 2026-09-28 11:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 104.5 |
| 6a7dff45-060a-3f5b-bb96-55eecbc873f1 | -15.1847 | -46.141 | 2026-09-28 11:10:00 | GOES-19 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 84.5 |
| c3acc663-8111-386e-93c4-9d1147e4917b | -8.2293 | -45.4375 | 2026-09-28 11:10:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 91.2 |
| e7bd9d73-36d8-35a3-aa97-00c09f5106b0 | -9.9784 | -50.1412 | 2026-09-28 11:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 79.6 |
| 1d7f2805-4ae1-304a-b4c5-f27fc69ab024 | -13.468 | -48.5881 | 2026-09-28 11:10:00 | GOES-19 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 73.9 |
| 15d5f46b-9abc-37a4-b1cc-e3bb17b34d62 | -12.6263 | -47.3075 | 2026-09-28 11:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 89.3 |
| f75cc5d4-2db5-3ca3-9b65-ab4063241803 | -12.7024 | -47.3414 | 2026-09-28 11:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 94.3 |
| b4ce7352-4f8a-3b44-ab25-300a5aa4cfea | -11.1775 | -44.7832 | 2026-09-28 11:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 87.6 |
| 35a993cf-ecec-35c7-8f59-eb26249b1e44 | -13.161 | -48.5437 | 2026-09-28 11:10:00 | GOES-19 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 85.0 |
| 260c473b-9055-37e5-824d-5f814d7f2a2f | -11.1966 | -44.7805 | 2026-09-28 11:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 86.7 |
| 517af41d-6164-3294-b2e8-ae1a4437e4f2 | -12.6832 | -47.3442 | 2026-09-28 11:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 101.1 |
| 14f3c772-8015-3b59-ba49-9327e7d58d0d | -11.1962 | -44.8037 | 2026-09-28 11:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 165.2 |
| b44d0969-1a94-3f21-ae83-9270b77af533 | -13.4676 | -48.6102 | 2026-09-28 11:10:00 | GOES-19 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 76.3 |
| 773fb88e-4083-3ed2-aac8-c9f418321776 | -10.1597 | -46.5781 | 2026-09-28 11:10:00 | GOES-19 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 104.1 |
| 455cd707-677f-359d-9711-55f1f8ccf196 | -11.1771 | -44.8064 | 2026-09-28 11:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 158.2 |
| fe660572-3772-3dca-98b3-f2d03f98412e | -7.39 | -42.13 | 2026-09-28 11:15:00 | MSG-03 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 33a87659-f3ac-31a3-80f2-034c475ae3ab | -11.1775 | -44.7832 | 2026-09-28 11:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 98.9 |
| 77e28743-b4e6-3a2f-8f38-7610283c6d94 | -12.6263 | -47.3075 | 2026-09-28 11:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 139.2 |
| 9fdcd3be-650e-3fd4-9fd0-bd31050db04b | -15.1847 | -46.141 | 2026-09-28 11:20:00 | GOES-19 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 96.8 |
| 0303dbf6-18df-31da-bd0b-f3454ab1d874 | -12.6836 | -47.3217 | 2026-09-28 11:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 87.5 |
| 62db26e8-44d5-36ae-9a6c-7ddc32d29d41 | -12.7024 | -47.3414 | 2026-09-28 11:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 108.9 |
| e5416a94-f9a5-34d6-81a4-e7551ccd3fd1 | -11.1771 | -44.8064 | 2026-09-28 11:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 182.6 |
| c1224152-9f1b-3f7c-9c3b-5d5d8aed3b4a | -11.1327 | -50.0624 | 2026-09-28 11:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 110.7 |
| 5a48ae09-ec78-3486-a6a0-ded1b1df22d6 | -11.1962 | -44.8037 | 2026-09-28 11:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 201.6 |
| 7a04ed77-554c-3c88-92cf-c721f7d4ad75 | -12.6455 | -47.3048 | 2026-09-28 11:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 89.8 |
| 0f6bde32-9782-38d6-bb40-13f9577f00f5 | -11.1966 | -44.7805 | 2026-09-28 11:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 95.2 |
| 3c3fbe46-6933-35aa-82f3-d77be66afb4c | -13.161 | -48.5437 | 2026-09-28 11:20:00 | GOES-19 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 96.9 |
| 11fbf5b7-4700-39fe-ad80-5a6ad8e45d4e | -12.6832 | -47.3442 | 2026-09-28 11:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 112.1 |
| 98933121-ea77-3b67-b35c-cc3615ab1369 | -8.2293 | -45.4375 | 2026-09-28 11:20:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 76.8 |
| 5945c0d7-bcd4-303c-8322-022454450c71 | -11.1775 | -44.7832 | 2026-09-28 11:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 112.3 |
| cead4396-dc4f-3a48-9642-b2aa47c17b06 | -11.1327 | -50.0624 | 2026-09-28 11:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 114.4 |
| 4e95ec0c-d20d-3ce2-b257-8ad75ed9f1d5 | -8.3666 | -46.5263 | 2026-09-28 11:30:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 103.5 |
| 77c8ac58-049b-3624-b707-421c11fbb78e | -12.7024 | -47.3414 | 2026-09-28 11:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 84.9 |
| 3b8ebc8e-f156-34a9-a8c6-27d0e9f9225f | -12.6263 | -47.3075 | 2026-09-28 11:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 125.9 |
| 0e667d67-c236-3b5a-b39a-4e234fc90f77 | -12.6836 | -47.3217 | 2026-09-28 11:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 108.0 |
| 60b805ea-8366-305d-8887-4461d114f48c | -11.1962 | -44.8037 | 2026-09-28 11:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 180.8 |
| 8e0187e4-7630-3e80-8247-be621712ff72 | -9.9784 | -50.1412 | 2026-09-28 11:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 85.5 |
| 72c9790c-7482-3280-be30-f3b8942b08fb | -11.1966 | -44.7805 | 2026-09-28 11:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 105.3 |
| 17075431-f255-32fb-b3e9-750daa6a3516 | -15.1847 | -46.141 | 2026-09-28 11:30:00 | GOES-19 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 76.0 |
| e8152d2e-a6ab-380c-8aa2-2a4fbad8f89c | -11.1771 | -44.8064 | 2026-09-28 11:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 178.9 |
| 215d9aba-bea7-3e28-8548-8863c27f8a43 | -13.161 | -48.5437 | 2026-09-28 11:30:00 | GOES-19 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 98.6 |
| f90ea6d4-23b8-3c8b-b8e1-efa2f1dfc420 | -8.4438 | -44.8683 | 2026-09-28 11:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 108.4 |
| af951a95-f29c-3c39-ad68-1c57f1b376ac | -11.2154 | -44.801 | 2026-09-28 11:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 72.4 |
| 2ad62274-98e4-30a8-8f24-9da941af7330 | -12.6263 | -47.3075 | 2026-09-28 11:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 112.9 |
| 56f9b362-910b-3eb6-804e-de5f029535fd | -12.6836 | -47.3217 | 2026-09-28 11:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 175.1 |
| 97d11a6f-a5ab-36bd-b968-6ed78fe50402 | -12.7024 | -47.3414 | 2026-09-28 11:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 141.5 |
| 2b99fdd9-daeb-314c-bf38-93a78a03048e | -15.1842 | -46.1642 | 2026-09-28 11:40:00 | GOES-19 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 85.4 |
| b7697b97-7fff-32c0-8a38-07248a2153fa | -12.6643 | -47.3245 | 2026-09-28 11:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 181.4 |
| 2963b84b-4232-3656-b6c6-44012057f89a | -12.7028 | -47.3189 | 2026-09-28 11:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 98.7 |
| cb071b66-dea7-38bf-b18f-47baa680ec2a | -11.1775 | -44.7832 | 2026-09-28 11:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 86.4 |
| 9f46cfe5-f3c0-33a2-9c11-4de74f6775e1 | -11.1966 | -44.7805 | 2026-09-28 11:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 143.1 |
| cadc28ff-45a3-3f11-9f7d-65164ba9c45d | -11.1771 | -44.8064 | 2026-09-28 11:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 187.8 |
| 9c7f9a91-53da-39eb-8852-a4579615ca08 | -12.6832 | -47.3442 | 2026-09-28 11:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 134.3 |
| 7aea052b-772d-37f9-ba0a-4830aa7a1c3e | -11.1962 | -44.8037 | 2026-09-28 11:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 280.5 |
| f1b9399a-bdd3-39ed-bf9d-e3abdd34a1b5 | -13.161 | -48.5437 | 2026-09-28 11:40:00 | GOES-19 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 105.2 |
| c96c5bf9-d4fa-35af-a48a-3cc955dcc93a | -15.1847 | -46.141 | 2026-09-28 11:40:00 | GOES-19 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 74.3 |
| a4fdbf32-9515-3acc-a186-8741920c5e1b | -14.7289 | -45.576 | 2026-09-28 11:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 94.6 |
| 511f6191-51af-3700-a840-0a109ff8677d | -11.1775 | -44.7832 | 2026-09-28 11:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 97.6 |
| ad2a2cfa-83f3-3ad1-b22e-9e0eb99ebbda | -8.2862 | -45.409 | 2026-09-28 11:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 101.8 |
| 632a41ac-9fb1-3917-8129-799cd879585a | -12.7028 | -47.3189 | 2026-09-28 11:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 114.4 |
| 2f701ed2-da4c-3986-bbc9-dbffd1475ca5 | -12.6832 | -47.3442 | 2026-09-28 11:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 201.5 |
| 0dd715a7-9ddc-32dc-8b99-bd9b6a2d9edc | -11.1771 | -44.8064 | 2026-09-28 11:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 150.7 |
| 7b7f8971-5a36-3602-9e3d-58507521fbcb | -14.7485 | -45.5725 | 2026-09-28 11:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 77.4 |
| 07edff83-947a-3e83-8729-16c42a5a64e4 | -12.6643 | -47.3245 | 2026-09-28 11:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 170.6 |
| 152af3d6-5ee4-3f03-817a-7fa8a2e84d3d | -11.1962 | -44.8037 | 2026-09-28 11:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 284.6 |
| f46ea9e5-9c7f-3dcf-9d65-8f2f5b5f6a75 | -13.161 | -48.5437 | 2026-09-28 11:50:00 | GOES-19 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 105.8 |
| 58d3dcc3-d35f-3ea5-95f5-31287f92237f | -12.6836 | -47.3217 | 2026-09-28 11:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 224.6 |
| 5dccd65f-f91f-344d-a0b9-78d756715773 | -11.2154 | -44.801 | 2026-09-28 11:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 91.8 |
| ceb37ae9-4bf0-39d1-970a-702ce065dd10 | -12.6263 | -47.3075 | 2026-09-28 11:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 92.9 |
| f36c74d7-de79-3515-bbd8-369b6a6d0664 | -12.7024 | -47.3414 | 2026-09-28 11:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 275.9 |
| 0feb8fc4-4e9c-38b6-85fd-13dcd34863fd | -15.1847 | -46.141 | 2026-09-28 11:50:00 | GOES-19 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 72.6 |
| d425e55b-bad0-37b5-a787-7d1d5e47a884 | -9.9784 | -50.1412 | 2026-09-28 11:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 73.0 |
| aa07792d-5207-3ad6-9fd4-d40db6d74d33 | -11.1966 | -44.7805 | 2026-09-28 11:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 184.8 |
| 7a17756e-1872-3008-8e36-52d46b45d69b | -9.9784 | -50.1412 | 2026-09-28 12:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 83.4 |
| 82cff6ac-cd03-336f-b89e-0841a7b0689a | -12.6836 | -47.3217 | 2026-09-28 12:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 289.5 |
| de99cad5-1ddd-39e3-889b-b93e5ed12186 | -12.6643 | -47.3245 | 2026-09-28 12:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 132.5 |
| b66f88ec-1d0a-3d0b-b265-90dfa47de8ce | -12.7028 | -47.3189 | 2026-09-28 12:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 118.3 |
| 90fc5f30-922e-31bc-b32f-1c245c713724 | -15.1842 | -46.1642 | 2026-09-28 12:00:00 | GOES-19 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 66.4 |
| 8c32dcca-95c5-3b42-aab4-eac4104feef5 | -8.3608 | -45.4695 | 2026-09-28 12:00:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 119.4 |


[Clique aqui para ver as próximas entradas](README70.md)
