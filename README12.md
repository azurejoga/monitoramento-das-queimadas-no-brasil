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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fa5d48d2-b357-3b38-b438-18d5b820d94a | -6.1106 | -57.7425 | 2026-08-17 04:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 69.3 |
| 6f20c0d6-1e7c-3cb7-92fc-efe5129de486 | -6.7123 | -58.9412 | 2026-08-17 04:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 61.5 |
| 78f5126d-fbfa-3553-9e53-d0aa39979951 | -6.6385 | -58.9442 | 2026-08-17 04:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 53.4 |
| 3a007bd4-985a-3865-8093-187463b0bfc9 | -7.3824 | -55.4924 | 2026-08-17 04:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 50.9 |
| 17af335f-69a8-34e7-94d8-3e005def94ea | -10.5085 | -50.0228 | 2026-08-17 04:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 48.0 |
| 5ecb1c20-ac1c-3672-addc-762642d98eb7 | -6.6199 | -58.9643 | 2026-08-17 04:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 75.7 |
| 396a38d1-cd0b-32c2-a58f-0ea304980c69 | -6.6568 | -58.9628 | 2026-08-17 04:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 101.4 |
| de18fad8-da4c-3797-98b3-a1423116ccad | -6.6015 | -58.9651 | 2026-08-17 04:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 56.1 |
| dd3f835a-a21a-353e-b860-5f54538fa2af | -6.6384 | -58.9636 | 2026-08-17 04:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 124.7 |
| 386271e1-f251-34e7-9951-85cfca280f0d | -6.6568 | -58.9628 | 2026-08-17 04:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 79.5 |
| 6e77bef7-37ef-304f-bfa0-0d505de8cb83 | -6.7123 | -58.9412 | 2026-08-17 04:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 58.9 |
| 74f06fe7-2c82-3adf-beaa-d5eb74a5480d | -6.6199 | -58.9643 | 2026-08-17 04:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 68.5 |
| 26c9ba0a-af69-3a3c-9c91-6367d14aa80c | -6.6384 | -58.9636 | 2026-08-17 04:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 99.4 |
| c0d8e222-92e3-3f10-9325-7014cc3d3f26 | -6.1106 | -57.7425 | 2026-08-17 04:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 65.9 |
| 9be95056-6f27-3658-96f1-cbc441e9528c | 1.59336 | -55.7733 | 2026-08-17 04:17:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| bdcda642-04aa-31f2-b4b8-181f7bbc274c | 1.58571 | -55.76836 | 2026-08-17 04:17:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ba6c08dc-fe91-3fe3-9375-3a733453a623 | -3.96666 | -43.1061 | 2026-08-17 04:19:00 | NOAA-21 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8398b5a0-43eb-3104-969d-92c7b3e072c7 | -7.1757 | -43.72158 | 2026-08-17 04:19:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 92bfd443-6615-3d36-b134-061a8deb114d | -7.12447 | -41.45018 | 2026-08-17 04:19:00 | NOAA-21 | GEMINIANO | PIAUÍ | Brasil | 2204352 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| ce872705-f8df-315d-8080-ba71fb410c4d | -7.24329 | -49.88594 | 2026-08-17 04:19:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b39fca93-fa1c-3c57-81c3-b1ba61e8dd05 | -2.596 | -45.15837 | 2026-08-17 04:19:00 | NOAA-21 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 68158bc1-bc85-3239-bb62-2632f9eed557 | -7.81427 | -44.09673 | 2026-08-17 04:19:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 295504ca-cd93-35c3-95b4-f3e3ac598816 | -6.52932 | -43.11816 | 2026-08-17 04:19:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| e7794eb0-9b71-3543-ba84-71c3136892e9 | -2.59265 | -45.15786 | 2026-08-17 04:19:00 | NOAA-21 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| b82b3335-1e35-3e43-bad5-ac5cc0df7c2e | -7.17905 | -43.7221 | 2026-08-17 04:19:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| eda5ae04-48ee-3a23-9844-ce47d4046afa | -5.40897 | -46.62479 | 2026-08-17 04:19:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 00059014-7999-3b8d-8793-2c32caf6f901 | -4.10308 | -49.06103 | 2026-08-17 04:19:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0d38c925-874b-3a77-98d7-98e53d846801 | -6.77802 | -46.33449 | 2026-08-17 04:19:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 75e6f79c-47d2-313b-b3f7-2ab82e39629c | -6.70933 | -45.36499 | 2026-08-17 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 94feac80-6e3c-3531-8673-ce9f9f0001f0 | -7.22586 | -43.25975 | 2026-08-17 04:19:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| a3c91c06-19d5-3471-a31d-5fbd82cf2147 | -6.24526 | -47.76739 | 2026-08-17 04:19:00 | NOAA-21 | LUZINÓPOLIS | TOCANTINS | Brasil | 1712454 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 782255a4-2465-3a9d-b443-103ac68c692d | -4.7199 | -42.76712 | 2026-08-17 04:19:00 | NOAA-21 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9208a8ef-4416-3ca3-b4d2-f8973b11b88d | -6.10719 | -57.73465 | 2026-08-17 04:19:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 3f4fd0a8-bff1-3df4-b5e1-998497277dd3 | -6.10017 | -44.323 | 2026-08-17 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8ffc579a-d80c-3ea3-b357-cc73afa0bc10 | -4.52839 | -38.55085 | 2026-08-17 04:19:00 | NOAA-21 | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 766895d3-2b04-3971-86ce-456d9a9a8256 | -7.00389 | -44.82962 | 2026-08-17 04:19:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d6f5b76c-9f8b-3ee1-b371-1b24a41d4dcb | -6.11961 | -57.74318 | 2026-08-17 04:19:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f0d4897c-26fb-3deb-9e9f-a6b9b873a4df | -2.76637 | -48.57049 | 2026-08-17 04:19:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 8eba0224-779c-333b-b048-d38a80329d91 | -4.31839 | -50.28889 | 2026-08-17 04:19:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 438c93ed-371b-3426-a1bc-a83ac47d2d60 | -2.49813 | -48.13774 | 2026-08-17 04:19:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 937a3238-7431-38fd-aec6-a7affbb0c23c | -7.1447 | -47.52729 | 2026-08-17 04:19:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c4661131-8032-3373-9d5d-45b1347260a3 | -6.95774 | -42.0667 | 2026-08-17 04:19:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| d52bc8b6-12b0-38cd-982f-80f236afd291 | -7.21922 | -41.54292 | 2026-08-17 04:19:00 | NOAA-21 | AROEIRAS DO ITAIM | PIAUÍ | Brasil | 2200954 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| a990ec88-2271-32b8-b802-97603115808f | -7.6113 | -46.54895 | 2026-08-17 04:19:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4db95eda-4231-3cbc-bf0d-33a60fbc2e36 | -6.37965 | -51.73827 | 2026-08-17 04:19:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 60597781-e859-3143-88fb-599b95740bb4 | -6.7801 | -51.05939 | 2026-08-17 04:19:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8ebabd05-ddd1-3566-b4cc-c328f81b76d2 | -7.59396 | -45.0153 | 2026-08-17 04:19:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 90ee91e9-d173-3df1-b35e-7dd52196f1ea | -4.35913 | -46.16076 | 2026-08-17 04:19:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 09975fc9-88e1-3958-a82d-166dceeedc1c | -6.10606 | -57.74084 | 2026-08-17 04:19:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 04a348a0-be7c-33dc-8dba-4e4a72acc363 | -6.87104 | -42.91978 | 2026-08-17 04:19:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| c29cbcfe-6f5a-32df-8ba1-459c50b461b1 | -8.94545 | -38.00322 | 2026-08-17 04:19:00 | NOAA-21 | INAJÁ | PERNAMBUCO | Brasil | 2607000 | 26 | 33 | nan | nan | nan | Caatinga | 1.3 |
| cfac4e0f-7752-3fa0-8a78-8d0d07c807f2 | -7.57569 | -48.44172 | 2026-08-17 04:19:00 | NOAA-21 | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1d463863-142c-389a-96e0-cba18612394c | -6.11501 | -57.73004 | 2026-08-17 04:19:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 99982da2-e548-3701-8932-940d344c40dd | -6.3146 | -43.61928 | 2026-08-17 04:19:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8a8b58df-06c6-36d8-85e3-76606bd41d14 | -7.67634 | -45.40152 | 2026-08-17 04:19:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4217839a-5e6d-36a1-9d84-7ab1df6a58f1 | -6.52987 | -43.11452 | 2026-08-17 04:19:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 674e7931-b83a-31af-8f59-0628ef2b0848 | -7.59949 | -45.02327 | 2026-08-17 04:19:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 66621148-57c6-3570-a8c8-1821499756dc | -3.47353 | -41.59671 | 2026-08-17 04:19:00 | NOAA-21 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| ffa244b3-a6b9-3ade-9872-7e16f7d33f56 | -6.10141 | -44.86086 | 2026-08-17 04:19:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 812f8b07-cb75-31ab-ae6d-1498ffa7afcb | -7.81039 | -44.09971 | 2026-08-17 04:19:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1a9ffec9-21e5-3202-8ff6-32cd19014009 | -6.11831 | -57.71185 | 2026-08-17 04:19:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 81c549df-fa15-3ad8-a8e3-94861d4ab9e6 | -0.83651 | -47.3598 | 2026-08-17 04:19:00 | NOAA-21 | SÃO JOÃO DE PIRABAS | PARÁ | Brasil | 1507474 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9575b77d-e26a-3396-abe6-b3944dfa3956 | -7.02164 | -45.90923 | 2026-08-17 04:19:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1c33dacb-92a0-3436-ba38-01393d8b6647 | -1.83763 | -54.48481 | 2026-08-17 04:19:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 18b7d17b-9658-33fe-b44c-a3b2fd6ff665 | -6.6933 | -43.9839 | 2026-08-17 04:19:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0959ca41-704a-32e8-95f6-b3ae34928594 | -7.23984 | -49.88203 | 2026-08-17 04:19:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 10cffbaa-7881-378e-a064-990eaac6a111 | -6.87161 | -42.91606 | 2026-08-17 04:19:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 93d5f35b-c819-37e0-a5fd-05a9308ac7ba | -7.82428 | -44.0983 | 2026-08-17 04:19:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 26c20dea-7af9-3bf6-a1d3-b80556322ba6 | -7.20763 | -41.54551 | 2026-08-17 04:19:00 | NOAA-21 | AROEIRAS DO ITAIM | PIAUÍ | Brasil | 2200954 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 39ce0884-5759-328b-9a89-186aaed6be19 | -5.8419 | -44.91171 | 2026-08-17 04:19:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8dd9bf7c-f901-3c34-aa76-774a40ba8637 | -5.76245 | -47.34663 | 2026-08-17 04:19:00 | NOAA-21 | GOVERNADOR EDISON LOBÃO | MARANHÃO | Brasil | 2104552 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4c573187-12d8-364a-8466-c9ff4bd2a26d | -6.30736 | -43.6218 | 2026-08-17 04:19:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 1ceb1f75-a34d-344c-9633-02de00d659fe | -2.95947 | -49.26184 | 2026-08-17 04:19:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0737c157-86ee-301c-b9fb-7e650ceea69b | -7.45376 | -44.86919 | 2026-08-17 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| ed0259aa-91ae-3e08-ab39-e0eaf7302d40 | -7.6758 | -45.40499 | 2026-08-17 04:19:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e5fbdc48-004c-3fac-9956-8df35aebcb07 | -6.10826 | -57.72874 | 2026-08-17 04:19:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 278c8258-9211-3e80-a315-221515cc0495 | -6.52877 | -43.1218 | 2026-08-17 04:19:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 7a2cbaea-957c-3d70-9593-e7712a944f60 | -7.14534 | -47.52337 | 2026-08-17 04:19:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a82ff06d-85ce-3bc2-902e-8d598fda193b | -6.24233 | -47.7628 | 2026-08-17 04:19:00 | NOAA-21 | LUZINÓPOLIS | TOCANTINS | Brasil | 1712454 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7c743598-91bc-3327-8553-7abc67e40a5a | -7.78662 | -43.94691 | 2026-08-17 04:19:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2bed4823-9b7b-3dbc-91e9-b740e955b13f | -7.47496 | -45.12431 | 2026-08-17 04:19:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b4c17500-7cea-3a31-9693-d8d3ef2bf083 | -7.40198 | -46.83087 | 2026-08-17 04:19:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 20a1ad7c-5253-3151-87ae-29a7efe8c124 | -7.23472 | -43.13312 | 2026-08-17 04:19:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| cbc7a2ae-d6b3-39ab-8914-e07cf4ee0651 | -6.73868 | -44.6786 | 2026-08-17 04:19:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f0f0a1a9-084e-3e4b-bd72-b95523c3931b | -7.55405 | -45.11905 | 2026-08-17 04:19:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9d743587-2cfc-33af-9c3a-2176a9f5ff2b | -4.12375 | -56.33393 | 2026-08-17 04:19:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e28bc56a-301d-36c5-8cfd-9d38115829a6 | -6.7293 | -44.6736 | 2026-08-17 04:19:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b68e4aaa-0a59-394a-a707-300466a83eb1 | -7.81221 | -47.83898 | 2026-08-17 04:19:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5366c6e9-f437-376d-9727-5845de95a2e9 | -6.53042 | -43.11087 | 2026-08-17 04:19:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 5ed94c34-57b2-3cc4-906f-1508823335a9 | -2.80717 | -48.59219 | 2026-08-17 04:19:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 8ee3c2f7-3ad6-3132-9a30-231dea466789 | -7.81286 | -47.83498 | 2026-08-17 04:19:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 153a97f0-7cf2-3553-8573-671fe200e1ac | -7.45288 | -46.1522 | 2026-08-17 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 08c19dc0-019e-31e2-bc82-40e75199b75c | -6.03025 | -57.81027 | 2026-08-17 04:19:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| a416d1dd-5c60-3efa-afc6-08fda19454e1 | -7.23813 | -43.13364 | 2026-08-17 04:19:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 37bbb6d7-1007-3676-aa80-850a29dbab45 | -6.53326 | -43.11503 | 2026-08-17 04:19:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 3211fe5f-bd2a-3d55-863a-8951c4077525 | -4.09826 | -49.06559 | 2026-08-17 04:19:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f60c869b-2725-31a7-8c18-dee5ff0b1cd0 | -6.02113 | -57.81386 | 2026-08-17 04:19:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| de842854-6459-3362-a105-e2f71ad7a4cf | -6.9352 | -45.44396 | 2026-08-17 04:19:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fdc4e68b-edd5-3f36-b2b0-cd3619935359 | -7.80868 | -47.83842 | 2026-08-17 04:19:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b9cba284-761e-37e9-ac48-fc64dcf614f2 | -4.12551 | -56.33125 | 2026-08-17 04:19:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |


[Clique aqui para ver as próximas entradas](README13.md)
