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
| 7f6f7e43-34f5-3832-aefd-03390c69aa60 | -5.8788 | -38.9029 | 2025-12-11 04:18:00 | NPP-375D | SOLONÓPOLE | CEARÁ | Brasil | 2313005 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| b4abf4fd-03ea-301c-a468-065c33599ba2 | -3.95406 | -41.52286 | 2025-12-11 04:18:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 3b938b76-1eb5-33c7-9c75-e5f83aba8164 | -5.35809 | -38.06612 | 2025-12-11 04:18:00 | NPP-375D | TABULEIRO DO NORTE | CEARÁ | Brasil | 2313104 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 17b2c559-e574-3908-80ed-0b5690712810 | -2.77316 | -45.52158 | 2025-12-11 04:18:00 | NPP-375D | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 417790f1-c488-31ad-9145-cdac65e1d816 | -3.66731 | -48.93482 | 2025-12-11 04:18:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 675d5ed0-ced6-3170-9ee8-d331a4f6d63e | -3.42311 | -41.65345 | 2025-12-11 04:18:00 | NPP-375D | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 1f60d194-8752-380c-ae0b-476441051537 | -1.3102 | -53.48989 | 2025-12-11 04:18:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ddb57d1a-7ce3-312e-b943-c8a246c0bd7d | -6.94057 | -38.61696 | 2025-12-11 04:18:00 | NPP-375D | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 02cff705-c911-3047-9071-1790129efe0f | -2.65644 | -51.64811 | 2025-12-11 04:18:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b414ad46-54d1-3a02-ac8f-13ac345d2666 | -6.02928 | -43.70533 | 2025-12-11 04:18:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 17.3 |
| fd9c5c35-e63e-396a-8980-a75c757906a5 | -4.20171 | -44.47753 | 2025-12-11 04:18:00 | NPP-375D | ALTO ALEGRE DO MARANHÃO | MARANHÃO | Brasil | 2100436 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f121a806-8eec-361e-a6c4-1be31f919211 | -3.17553 | -48.02554 | 2025-12-11 04:18:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 51210397-b415-3357-b552-f261b4c74a83 | -4.95571 | -45.08485 | 2025-12-11 04:18:00 | NPP-375D | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b598b987-70bd-3677-8b1a-dad89685b203 | -3.18394 | -48.03004 | 2025-12-11 04:18:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| df7ef49c-70aa-3f1d-aa2f-054cb9f0bc88 | -3.39144 | -45.41866 | 2025-12-11 04:18:00 | NPP-375D | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c906d5c3-2442-3564-b017-ac044486907d | -4.50812 | -44.63479 | 2025-12-11 04:18:00 | NPP-375D | TRIZIDELA DO VALE | MARANHÃO | Brasil | 2112233 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 31a37925-5a5b-3c82-8dd4-e26b07ce1b39 | -6.94134 | -38.61188 | 2025-12-11 04:18:00 | NPP-375D | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 3.9 |
| d63f2bad-6e73-3260-af3d-95c328d377b5 | -3.52198 | -47.20897 | 2025-12-11 04:18:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 591f0163-dc84-3d46-82da-8d25d42efef3 | -4.0707 | -47.94827 | 2025-12-11 04:18:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e32c5bef-6596-382a-a08d-b8644277b724 | -6.11626 | -41.15839 | 2025-12-11 04:18:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 0.4 |
| f5af498c-5ae2-36ca-9be0-384a3fa64674 | -9.86409 | -36.01609 | 2025-12-11 04:18:00 | NPP-375D | ROTEIRO | ALAGOAS | Brasil | 2707800 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| d1fa0ae9-7cde-34c5-ab43-ec5d2be74c83 | -3.2302 | -47.47569 | 2025-12-11 04:18:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 0f8faf5f-0834-337c-8ef1-1f6c1159c990 | -6.18416 | -42.46685 | 2025-12-11 04:18:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| f08e11cc-b605-3e18-a74d-2e67b454e95a | -1.58147 | -53.76002 | 2025-12-11 04:18:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| e1871ef5-3b68-3cef-b69d-8cc6adddc512 | -3.36525 | -45.34086 | 2025-12-11 04:18:00 | NPP-375D | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 485d8dc1-e2c5-3df5-9df2-d81b5fbc57a4 | -2.88241 | -52.72205 | 2025-12-11 04:18:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 659e6f04-4b06-3bf4-885c-8baf74576b38 | -7.11911 | -40.22393 | 2025-12-11 04:18:00 | NPP-375D | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 6aeabc03-e2bb-33ff-83f1-efa750b3bdce | -3.228 | -52.64339 | 2025-12-11 04:18:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 87e62ebf-cca1-310f-8981-fe40b9a9c5bb | -5.35861 | -38.06266 | 2025-12-11 04:18:00 | NPP-375D | TABULEIRO DO NORTE | CEARÁ | Brasil | 2313104 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 1483acda-522c-32c8-8f43-08708f166bef | -3.66844 | -43.92507 | 2025-12-11 04:18:00 | NPP-375D | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 244c7dcc-a96d-3df6-a77f-3866091b5fcc | -3.37683 | -44.72598 | 2025-12-11 04:18:00 | NPP-375D | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 73945448-ed53-35c2-ab66-7ee78973837a | -3.49235 | -44.88792 | 2025-12-11 04:18:00 | NPP-375D | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6c044ce8-db20-3d17-9014-eabd6257ef27 | -2.20929 | -51.89325 | 2025-12-11 04:18:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4cc4fc7c-e9c5-3a8c-ab49-55a371c56bb0 | -9.16846 | -40.11053 | 2025-12-11 04:18:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| b910fc72-c5ea-397f-abd8-acb12f87872f | -2.56541 | -51.8237 | 2025-12-11 04:18:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 92c65985-1d4c-3ccb-8e64-6970ef807976 | -2.3131 | -46.48584 | 2025-12-11 04:18:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a6e593c1-fd1f-35dc-a236-2e2c15f3c03f | -5.9787 | -44.59535 | 2025-12-11 04:18:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f64249d2-8705-3618-981d-16ace2c85272 | -4.20513 | -44.47807 | 2025-12-11 04:18:00 | NPP-375D | ALTO ALEGRE DO MARANHÃO | MARANHÃO | Brasil | 2100436 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 57013cd2-9c25-3f89-948a-955a105bf8f2 | -3.35306 | -46.86365 | 2025-12-11 04:18:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 23a684f8-e619-33af-9081-076521c18148 | -2.10204 | -48.05175 | 2025-12-11 04:18:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0f68d11e-d95d-36fc-9f7c-b6b5f0534476 | -8.65544 | -35.99285 | 2025-12-11 04:18:00 | NPP-375D | PANELAS | PERNAMBUCO | Brasil | 2610202 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 63dd3e6d-b3e9-34d0-98c9-033523d7f268 | -2.09064 | -52.11669 | 2025-12-11 04:18:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e2ccf7f2-7561-35b4-8542-8a9c9ba953f2 | -4.68212 | -43.25986 | 2025-12-11 04:18:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cd9945c1-76b5-358c-b1a7-ba07fb226e0d | -2.88545 | -42.95487 | 2025-12-11 04:18:00 | NPP-375D | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| d0612bde-8a92-38a9-af96-2f864720fb61 | -5.98209 | -44.5959 | 2025-12-11 04:18:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fa551929-9df4-3a6e-a86d-0d9c564da06d | -3.23535 | -47.46945 | 2025-12-11 04:18:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 0e39ab34-932f-3136-8395-a65507f56df0 | -3.48793 | -51.54182 | 2025-12-11 04:18:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f128259c-c5f2-3e6b-8e49-4aa648c34a6d | -6.0608 | -43.73896 | 2025-12-11 04:18:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bd99612c-8e4c-3177-a049-e225456369ab | -6.0315 | -43.7105 | 2025-12-11 04:20:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 73.3 |
| 45f59564-b70b-3f85-8bf3-9f463562860c | -3.7589 | -45.4944 | 2025-12-11 04:20:00 | GOES-19 | PINDARÉ-MIRIM | MARANHÃO | Brasil | 2108504 | 21 | 33 | nan | nan | nan | Amazônia | 97.0 |
| 20950902-97e8-394d-8413-c504f1109a4e | -11.66829 | -47.12503 | 2025-12-11 04:21:00 | NPP-375D | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 168bfb48-1eb9-34e8-9884-236755d44bf4 | -10.02521 | -48.12618 | 2025-12-11 04:21:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0cbfc508-bcac-3721-8bf2-ca2a46411281 | -10.236 | -52.21754 | 2025-12-11 04:21:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c4a0a5cf-e70a-3979-82eb-e0621461986f | -10.23637 | -52.21882 | 2025-12-11 04:21:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 9d52b4a7-3e03-3b23-8c54-7c6f0433253c | -11.48588 | -41.47016 | 2025-12-11 04:21:00 | NPP-375D | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 321bfe06-b61f-330d-a556-a12a48454bc5 | -12.28627 | -43.54358 | 2025-12-11 04:21:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 270e0f66-8dde-31f9-b7ec-511e5f14c6ea | -10.47998 | -50.65821 | 2025-12-11 04:21:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2a9a480c-f920-364c-a5c4-993e04e3c96b | -11.58277 | -42.92575 | 2025-12-11 04:21:00 | NPP-375D | MORPARÁ | BAHIA | Brasil | 2921609 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 3fc84134-458e-322e-b59f-b23c52f056f2 | -12.67529 | -46.78475 | 2025-12-11 04:21:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d1dfe39e-e56f-3ce1-92d6-58276475afaa | -12.67592 | -46.78088 | 2025-12-11 04:21:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f219ef4b-4ccd-34a5-875f-1bc74437838b | -10.026 | -48.12156 | 2025-12-11 04:21:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4f42b343-091c-3cbf-9280-05965efe07c2 | -10.88536 | -44.32706 | 2025-12-11 04:21:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7952a697-fce4-356a-9ebd-0d2c5d033e84 | -12.21276 | -38.98345 | 2025-12-11 04:21:00 | NPP-375D | FEIRA DE SANTANA | BAHIA | Brasil | 2910800 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 30df173f-d79b-3f7c-b99b-9c14b93cd79c | -12.27511 | -43.54918 | 2025-12-11 04:21:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f3316cc3-b4c0-38a3-a9a6-8dc0d656e990 | -10.47632 | -50.653 | 2025-12-11 04:21:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1c448d39-e03a-3ea2-aad5-eb8a0d1e9478 | -12.27566 | -43.54558 | 2025-12-11 04:21:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9fd0c047-f605-35d0-83d6-b7c637dd5348 | -9.34146 | -43.08779 | 2025-12-11 04:21:00 | NPP-375D | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 12407cb6-9b2e-3128-8adc-e58000a4eb15 | -10.24095 | -52.21851 | 2025-12-11 04:21:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8558bdef-288c-3a78-99b1-2ee0667477e7 | -9.30529 | -48.55783 | 2025-12-11 04:21:00 | NPP-375D | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e6b82b8f-3258-3d47-929e-8e0bc906dff3 | -12.33095 | -43.65372 | 2025-12-11 04:21:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f93e8775-2239-399c-9723-673d8b616e48 | -11.48231 | -41.46963 | 2025-12-11 04:21:00 | NPP-375D | AMÉRICA DOURADA | BAHIA | Brasil | 2901155 | 29 | 33 | nan | nan | nan | Caatinga | 5.6 |
| fe94299c-1150-3968-827e-6516b340d0b7 | -10.235 | -52.22315 | 2025-12-11 04:21:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 09ae75be-fd21-3bed-9d6b-ff2fab9da33e | -11.66561 | -47.12592 | 2025-12-11 04:21:00 | NPP-375D | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4808b94b-84e6-3d92-bc5f-ec800cfed757 | -12.33306 | -43.65376 | 2025-12-11 04:21:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 02fd463e-a532-3348-ba8f-a2ef4b79950d | -10.47554 | -50.65741 | 2025-12-11 04:21:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 65c1f6c9-adeb-3c1e-9ae9-76190ea8fd4e | -23.21353 | -45.43463 | 2025-12-11 04:23:00 | NPP-375D | REDENÇÃO DA SERRA | SÃO PAULO | Brasil | 3542305 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| b4bb5d72-2a1f-3fd7-b606-a5a6a476f5da | -23.38481 | -46.41558 | 2025-12-11 04:23:00 | NPP-375D | GUARULHOS | SÃO PAULO | Brasil | 3518800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| c3c08c61-d71d-3d50-a2cf-d357a855cc83 | -23.22014 | -49.01609 | 2025-12-11 04:23:00 | NPP-375D | ARANDU | SÃO PAULO | Brasil | 3503109 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| cfceebb6-87ee-3f4c-b654-6def4b168c95 | -16.69738 | -44.965 | 2025-12-11 04:23:00 | NPP-375D | PONTO CHIQUE | MINAS GERAIS | Brasil | 3152131 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c31f9cb9-53c3-30dc-ad51-7c98d85c23cc | -22.04398 | -56.3098 | 2025-12-11 04:23:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d1756f92-2152-31f1-acf9-70b57c97c7b0 | -16.70072 | -44.96556 | 2025-12-11 04:23:00 | NPP-375D | PONTO CHIQUE | MINAS GERAIS | Brasil | 3152131 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0a9dbd9f-25df-3f19-b3e4-90f6ec2779fa | -22.02586 | -56.34328 | 2025-12-11 04:23:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5886ba49-b9d8-364f-94f6-8e234ecc3c06 | -16.3083 | -53.82576 | 2025-12-11 04:23:00 | NPP-375D | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 70af7ce8-aeef-3300-bbcf-bfa95df53a1d | -16.69795 | -44.96138 | 2025-12-11 04:23:00 | NPP-375D | PONTO CHIQUE | MINAS GERAIS | Brasil | 3152131 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9c9b2e5d-7493-38d2-a755-7d889707a3a6 | -16.70405 | -44.96612 | 2025-12-11 04:23:00 | NPP-375D | PONTO CHIQUE | MINAS GERAIS | Brasil | 3152131 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 84e4f10b-a5df-3d61-8cf9-7668bd5f9d34 | -22.10019 | -46.74832 | 2025-12-11 04:23:00 | NPP-375D | SANTO ANTÔNIO DO JARDIM | SÃO PAULO | Brasil | 3548104 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 79607bc5-a2a8-379c-bf45-7970459ef375 | -22.02659 | -56.33992 | 2025-12-11 04:23:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| eba05b47-96e1-3c1a-b20a-d407b3fb323d | -22.04469 | -56.30654 | 2025-12-11 04:23:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 33b1d068-6bf2-32d1-bb52-9c01df12a3ec | -26.2551 | -48.55679 | 2025-12-11 04:25:00 | NPP-375D | SÃO FRANCISCO DO SUL | SANTA CATARINA | Brasil | 4216206 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 4823bdfd-83d9-3395-a8c9-09b67a056005 | -25.28465 | -49.30514 | 2025-12-11 04:25:00 | NPP-375D | ALMIRANTE TAMANDARÉ | PARANÁ | Brasil | 4100400 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| daf3a2a4-e054-3524-b86f-04f1909db568 | -3.7589 | -45.4944 | 2025-12-11 04:30:00 | GOES-19 | PINDARÉ-MIRIM | MARANHÃO | Brasil | 2108504 | 21 | 33 | nan | nan | nan | Amazônia | 86.8 |
| 2bf035a5-88a7-3336-abd9-676be6fc2391 | -2.77171 | -45.51978 | 2025-12-11 04:38:00 | NOAA-20 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bd83e402-f8ce-3369-9f63-ff95b4d5af3e | -1.14692 | -51.69367 | 2025-12-11 04:38:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f8bd469b-4065-3b59-9bb6-7baceb3bd823 | 0.22723 | -50.07874 | 2025-12-11 04:38:00 | NOAA-20 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e1f23dcd-c535-369d-a6e4-6983d70a2379 | -1.90202 | -48.29073 | 2025-12-11 04:38:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d8ba93e4-098c-38d0-bf5c-e1aa75d98d77 | -2.89795 | -49.53455 | 2025-12-11 04:38:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4a28448a-f456-3b54-ade2-de43daa83794 | -2.28743 | -45.60306 | 2025-12-11 04:38:00 | NOAA-20 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 29480d5e-769c-317a-99ea-875d2db03ea3 | -2.89057 | -53.00291 | 2025-12-11 04:38:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c252d074-ff64-3cd9-b0ff-a8dba4b03ec6 | -2.1505 | -53.76018 | 2025-12-11 04:38:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1e6d4f13-53d2-33fb-9643-d3cc46059049 | -3.46133 | -48.97949 | 2025-12-11 04:38:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README12.md)
