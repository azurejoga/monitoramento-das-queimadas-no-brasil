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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 71e512e7-3f2a-3b6e-9a85-e22b8e234e16 | -5.24614 | -38.22135 | 2025-12-30 03:42:00 | NOAA-20 | SÃO JOÃO DO JAGUARIBE | CEARÁ | Brasil | 2312502 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 75e7781d-fac8-3d52-bd88-707fa83588fe | -5.94305 | -39.66642 | 2025-12-30 03:42:00 | NOAA-20 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 28be7167-5d5f-3171-a634-42ff658ce58d | -4.0753 | -38.25597 | 2025-12-30 03:42:00 | NOAA-20 | CASCAVEL | CEARÁ | Brasil | 2303501 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| a203f24f-281b-39ee-b99e-aa9566f12f76 | -5.46081 | -40.70185 | 2025-12-30 03:42:00 | NOAA-20 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| ea389466-e1c3-355b-8ea5-c3216a20a2ce | -3.9243 | -40.53302 | 2025-12-30 03:42:00 | NOAA-20 | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 673c7b55-4aa9-388e-b346-debf4fc67ec9 | -6.08494 | -37.32006 | 2025-12-30 03:42:00 | NOAA-20 | BELÉM DO BREJO DO CRUZ | PARAÍBA | Brasil | 2502003 | 25 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 1bf806f6-df3d-3ea1-845b-b4361bd38d9b | -5.14421 | -39.4683 | 2025-12-30 03:42:00 | NOAA-20 | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 4dae9863-8ea8-30c7-867e-9c6d1e91c853 | -6.09169 | -35.40761 | 2025-12-30 03:42:00 | NOAA-20 | MONTE ALEGRE | RIO GRANDE DO NORTE | Brasil | 2407807 | 24 | 33 | nan | nan | nan | Caatinga | 0.4 |
| dd92b98a-9b00-327d-a5d7-e46d744c1d03 | -5.48853 | -38.04717 | 2025-12-30 03:42:00 | NOAA-20 | ALTO SANTO | CEARÁ | Brasil | 2300705 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| f4d01013-cd00-372b-8b0a-9e9267b344be | -5.38501 | -43.18914 | 2025-12-30 03:42:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8c2be110-8b37-39da-a435-7fc23920e436 | -4.12816 | -38.66952 | 2025-12-30 03:42:00 | NOAA-20 | GUAIÚBA | CEARÁ | Brasil | 2304954 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 629b66f3-c93d-35e6-9739-d7724014c9ec | -5.1434 | -39.47318 | 2025-12-30 03:42:00 | NOAA-20 | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 85e8f36d-80cb-38f4-a053-866bb0bf0dd3 | -3.55814 | -43.20025 | 2025-12-30 03:42:00 | NOAA-20 | MATA ROMA | MARANHÃO | Brasil | 2106409 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 74fc5843-25c9-355e-b2ba-a1d5e1a52b92 | -5.13756 | -36.36404 | 2025-12-30 03:42:00 | NOAA-20 | GUAMARÉ | RIO GRANDE DO NORTE | Brasil | 2404507 | 24 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 84b8f505-dcb1-38f1-956b-b99086402fed | -3.61077 | -41.9218 | 2025-12-30 03:42:00 | NOAA-20 | CARAÚBAS DO PIAUÍ | PIAUÍ | Brasil | 2202539 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 804bd5d2-ebab-3858-a46d-1a3be227e6cb | -3.54229 | -43.61221 | 2025-12-30 03:42:00 | NOAA-20 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d6aeeefe-33fd-3e55-9d7b-91c3c91b7f0d | -4.90052 | -38.92796 | 2025-12-30 03:42:00 | NOAA-20 | QUIXADÁ | CEARÁ | Brasil | 2311306 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 423ff28e-a97f-300d-97e9-5593453140d1 | -2.82541 | -40.3625 | 2025-12-30 03:42:00 | NOAA-20 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| cb3123f6-69f2-348b-90de-af37f301d7e5 | -5.46144 | -40.69801 | 2025-12-30 03:42:00 | NOAA-20 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 476664c3-efa9-3c14-b336-ee8972d4351c | -6.24155 | -38.27468 | 2025-12-30 03:42:00 | NOAA-20 | RIACHO DE SANTANA | RIO GRANDE DO NORTE | Brasil | 2410801 | 24 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 0102df32-f6b2-3e0b-8dcc-ad2264218dce | -3.55018 | -43.59726 | 2025-12-30 03:42:00 | NOAA-20 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 3d4234ee-4428-3858-a06f-f19b626793fb | -3.55542 | -43.59825 | 2025-12-30 03:42:00 | NOAA-20 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 301ba8c2-dbcc-3801-a562-a9df3376d2b8 | -4.00301 | -44.21601 | 2025-12-30 03:42:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d74fc2b5-9158-353d-8311-85f1979caf7b | -5.96778 | -39.41901 | 2025-12-30 03:42:00 | NOAA-20 | PIQUET CARNEIRO | CEARÁ | Brasil | 2310902 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 1c57ccd6-a08f-39ef-9174-e5d6a6c17264 | -5.38421 | -43.18853 | 2025-12-30 03:42:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8d29b14b-11bd-353e-9251-996f5e5d6b83 | -5.13952 | -39.47254 | 2025-12-30 03:42:00 | NOAA-20 | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 0d3530e4-232e-330b-bbba-a31db53eed1f | -3.54334 | -43.60592 | 2025-12-30 03:42:00 | NOAA-20 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0e1771c4-41e8-3698-9595-3b360d18970e | -5.14092 | -36.36457 | 2025-12-30 03:42:00 | NOAA-20 | GUAMARÉ | RIO GRANDE DO NORTE | Brasil | 2404507 | 24 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 5c9a3b12-0a5d-3302-a08c-d359d7b122ff | -3.55763 | -43.20325 | 2025-12-30 03:42:00 | NOAA-20 | MATA ROMA | MARANHÃO | Brasil | 2106409 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9d8ebb82-ac56-3c7a-a4db-f7d51c2fdc86 | -4.51359 | -43.69642 | 2025-12-30 03:42:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 339b2272-2a50-39a3-bd0d-577ecdb433d7 | -5.9545 | -38.63077 | 2025-12-30 03:42:00 | NOAA-20 | JAGUARIBE | CEARÁ | Brasil | 2306900 | 23 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 82bddfe4-50b9-3039-b3c5-4e13903589f8 | -5.06755 | -40.48224 | 2025-12-30 03:42:00 | NOAA-20 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 9f0cac2c-0e4c-3590-b9b4-7ddb688d9697 | -4.42523 | -38.33888 | 2025-12-30 03:42:00 | NOAA-20 | CASCAVEL | CEARÁ | Brasil | 2303501 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| e18946f9-9b33-347c-937c-c0ef805cc23c | -4.7392 | -38.7294 | 2025-12-30 03:42:00 | NOAA-20 | IBARETAMA | CEARÁ | Brasil | 2305266 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 216acc19-08bd-3a6e-b1fe-5cc30aa34f54 | -3.54964 | -43.60052 | 2025-12-30 03:42:00 | NOAA-20 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 434cf000-c9d1-3137-a1a0-51dc9142d44a | -5.63466 | -39.75735 | 2025-12-30 03:42:00 | NOAA-20 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| ce3e4a62-4e06-3ad6-b61b-7e03a28f35a7 | -5.4872 | -38.05529 | 2025-12-30 03:42:00 | NOAA-20 | ALTO SANTO | CEARÁ | Brasil | 2300705 | 23 | 33 | nan | nan | nan | Caatinga | 3.1 |
| bc60cebd-68a1-315a-9fc5-c3a29bad9631 | -5.46253 | -40.69733 | 2025-12-30 03:42:00 | NOAA-20 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 94705ae9-8091-3e5f-918b-3f72304d7367 | -3.54858 | -43.6069 | 2025-12-30 03:42:00 | NOAA-20 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4aceb0ee-3a73-3ed6-88a6-eeb80ad433af | -4.60513 | -46.60157 | 2025-12-30 03:42:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 84ae9b9b-846d-32b0-814e-1505cdff16c3 | -3.54175 | -43.61548 | 2025-12-30 03:42:00 | NOAA-20 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fa130ce0-bf3d-392a-894d-cd5bd68b7888 | -4.51792 | -38.61442 | 2025-12-30 03:42:00 | NOAA-20 | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| da0ee336-9e14-31d0-bc60-76d707e24db7 | -3.54911 | -43.60375 | 2025-12-30 03:42:00 | NOAA-20 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 85ae5b14-b58f-3837-ae23-40bcd2fd4f6f | -3.41425 | -39.35806 | 2025-12-30 03:42:00 | NOAA-20 | TRAIRI | CEARÁ | Brasil | 2313500 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| c6dd6d23-a36f-3b50-9fb0-b36c294493d6 | -2.96272 | -39.99628 | 2025-12-30 03:42:00 | NOAA-20 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| b0d36cfb-1159-38c8-8f48-dab676481196 | -9.50852 | -35.98824 | 2025-12-30 03:44:00 | NOAA-20 | ATALAIA | ALAGOAS | Brasil | 2700409 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 8914c0c8-4dfc-395f-9e6b-36665e6710f8 | -11.75816 | -43.30688 | 2025-12-30 03:44:00 | NOAA-20 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 04718d4c-8cc2-30dc-9440-4fe07a346f41 | -6.08129 | -40.42521 | 2025-12-30 03:44:00 | NOAA-20 | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| a1eb764b-b1dd-3190-8d72-b87f897c60ff | -7.1478 | -38.66719 | 2025-12-30 03:44:00 | NOAA-20 | SÃO JOSÉ DE PIRANHAS | PARAÍBA | Brasil | 2514503 | 25 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 4a48040b-0045-3ea1-9bbf-2a5fd9fe2e96 | -7.14626 | -37.00014 | 2025-12-30 03:44:00 | NOAA-20 | AREIA DE BARAÚNAS | PARAÍBA | Brasil | 2501153 | 25 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 60e961e4-eba5-3309-ad96-fb2b59516904 | -11.75481 | -43.32507 | 2025-12-30 03:44:00 | NOAA-20 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3c87218e-4f97-3b85-a087-cd907ce9a526 | -7.54666 | -35.1837 | 2025-12-30 03:44:00 | NOAA-20 | ALIANÇA | PERNAMBUCO | Brasil | 2600708 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 18401b78-d2fa-3bcd-a173-7eb68d3273bc | -11.74669 | -43.31882 | 2025-12-30 03:44:00 | NOAA-20 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0eb5cab3-3b20-370e-9af9-0da380a70440 | -9.88673 | -36.02378 | 2025-12-30 03:44:00 | NOAA-20 | ROTEIRO | ALAGOAS | Brasil | 2707800 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 24238c69-3a57-3f6f-8151-b000ec693c21 | -5.39404 | -44.68666 | 2025-12-30 03:44:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| d83d70ff-6de1-3f6f-b9ca-148145d86ffb | -6.08822 | -41.81652 | 2025-12-30 03:44:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| d10038c6-9714-3cc8-bb57-283526e1d080 | -9.88342 | -36.02325 | 2025-12-30 03:44:00 | NOAA-20 | ROTEIRO | ALAGOAS | Brasil | 2707800 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 5a932f39-9ae8-3788-9914-ff2bad0f968f | -11.75369 | -43.30602 | 2025-12-30 03:44:00 | NOAA-20 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 69b9d5bf-c85f-32a1-ad52-1a975b13f25c | -8.46421 | -36.48915 | 2025-12-30 03:44:00 | NOAA-20 | SÃO BENTO DO UNA | PERNAMBUCO | Brasil | 2613008 | 26 | 33 | nan | nan | nan | Caatinga | 0.6 |
| e2486a16-541e-376b-ae7c-0a7a9933b097 | -5.3934 | -44.69035 | 2025-12-30 03:44:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 7bf2a88a-d2d0-3a7a-9c9f-d4ebea1c9617 | -6.93188 | -44.58173 | 2025-12-30 03:44:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0282124f-1eaa-3c01-8383-bd897baf4570 | -7.14711 | -38.67136 | 2025-12-30 03:44:00 | NOAA-20 | SÃO JOSÉ DE PIRANHAS | PARAÍBA | Brasil | 2514503 | 25 | 33 | nan | nan | nan | Caatinga | 2.4 |
| ed0f63a8-1fd2-3638-93a5-ad3f0ed9232b | -6.93246 | -44.57843 | 2025-12-30 03:44:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 26e867c7-a6d0-3e35-9b94-eb3b470b53c5 | -11.95792 | -41.28661 | 2025-12-30 03:44:00 | NOAA-20 | BONITO | BAHIA | Brasil | 2904050 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 4dfa8839-287e-3f62-b676-6b9374203d32 | -10.08039 | -38.4318 | 2025-12-30 03:44:00 | NOAA-20 | JEREMOABO | BAHIA | Brasil | 2918100 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 55737c69-e2c0-34d2-88e0-3fd960a45e96 | -7.04047 | -38.26448 | 2025-12-30 03:44:00 | NOAA-20 | AGUIAR | PARAÍBA | Brasil | 2500205 | 25 | 33 | nan | nan | nan | Caatinga | 4.3 |
| ee414aa5-1a6b-3dd5-bc8f-0874639fef17 | -7.06326 | -38.90771 | 2025-12-30 03:44:00 | NOAA-20 | AURORA | CEARÁ | Brasil | 2301703 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| a749c0dd-0f1d-3308-a703-09bc6e4ee787 | -11.75033 | -43.32423 | 2025-12-30 03:44:00 | NOAA-20 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a9e67d1f-f21a-3583-ad16-3cee5043c1c0 | -9.67185 | -36.94494 | 2025-12-30 03:44:00 | NOAA-20 | GIRAU DO PONCIANO | ALAGOAS | Brasil | 2702900 | 27 | 33 | nan | nan | nan | Caatinga | 0.9 |
| d7381f75-97c0-34b5-b1ad-d3b1c4adcce7 | -12.47928 | -38.10015 | 2025-12-30 03:44:00 | NOAA-20 | MATA DE SÃO JOÃO | BAHIA | Brasil | 2921005 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 4c4c0981-9c6a-3c50-afff-354b6aba7db9 | -10.04846 | -36.26838 | 2025-12-30 03:44:00 | NOAA-20 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 0a9baaae-2661-3cf3-82b0-6849f776bb46 | -9.81463 | -37.17972 | 2025-12-30 03:44:00 | NOAA-20 | BELO MONTE | ALAGOAS | Brasil | 2700904 | 27 | 33 | nan | nan | nan | Caatinga | 1.1 |
| f45c43c5-5a86-380c-97d5-8da14c752bc1 | -9.39387 | -36.89982 | 2025-12-30 03:44:00 | NOAA-20 | MINADOR DO NEGRÃO | ALAGOAS | Brasil | 2705309 | 27 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 1ab964fd-61a7-3907-8acd-e02a6f469fb9 | -12.09866 | -37.99963 | 2025-12-30 03:44:00 | NOAA-20 | ENTRE RIOS | BAHIA | Brasil | 2910503 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| c5dfc8df-4409-3c55-881d-32012f411c50 | -6.11432 | -39.79882 | 2025-12-30 03:44:00 | NOAA-20 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 4df8fce4-b15b-303e-a049-c95a5d062a9c | -6.23612 | -40.29787 | 2025-12-30 03:44:00 | NOAA-20 | ARNEIROZ | CEARÁ | Brasil | 2301505 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| e6bccc59-2ed5-3112-9c9d-75e2cd156361 | -8.78533 | -35.75108 | 2025-12-30 03:44:00 | NOAA-20 | MARAIAL | PERNAMBUCO | Brasil | 2609204 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 6fc4cc20-13b9-3381-a563-a3ce5bed0cf3 | -7.32013 | -35.06932 | 2025-12-30 03:44:00 | NOAA-20 | PEDRAS DE FOGO | PARAÍBA | Brasil | 2511202 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 839429a8-25a5-3082-92f8-abc8a2622b0e | -10.49337 | -40.53892 | 2025-12-30 03:44:00 | NOAA-20 | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| d34076d0-9ec3-37e9-9d70-080238d795cc | -12.32087 | -42.53751 | 2025-12-30 03:44:00 | NOAA-20 | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| b4836bdd-7198-3d2f-8d4e-82afdc75e5ad | -7.03694 | -38.26377 | 2025-12-30 03:44:00 | NOAA-20 | AGUIAR | PARAÍBA | Brasil | 2500205 | 25 | 33 | nan | nan | nan | Caatinga | 9.9 |
| 94b21959-34e2-3cf4-a893-fb8baf7c9886 | -7.06395 | -38.90343 | 2025-12-30 03:44:00 | NOAA-20 | AURORA | CEARÁ | Brasil | 2301703 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| bab24249-bf25-3b37-8320-873cc9f5f3c5 | -8.8138 | -38.93331 | 2025-12-30 03:44:00 | NOAA-20 | RODELAS | BAHIA | Brasil | 2927101 | 29 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 5fc41435-afab-3790-9757-a0c01267f1f2 | -8.90941 | -37.42072 | 2025-12-30 03:44:00 | NOAA-20 | ITAÍBA | PERNAMBUCO | Brasil | 2607505 | 26 | 33 | nan | nan | nan | Caatinga | 0.6 |
| efdfd6b7-2224-3109-9208-d25c2ea4b60f | -8.78588 | -35.7476 | 2025-12-30 03:44:00 | NOAA-20 | MARAIAL | PERNAMBUCO | Brasil | 2609204 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 4863b91a-76af-368f-b981-bfcbf207f5fc | -8.32617 | -37.70969 | 2025-12-30 03:44:00 | NOAA-20 | CUSTÓDIA | PERNAMBUCO | Brasil | 2605103 | 26 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 606e3a72-0c1f-3190-b654-94274df5041e | -7.06313 | -38.90596 | 2025-12-30 03:44:00 | NOAA-20 | AURORA | CEARÁ | Brasil | 2301703 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| e252fc5a-1ecd-33e9-98c8-07538fc595a7 | -6.11823 | -39.79945 | 2025-12-30 03:44:00 | NOAA-20 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| a6f464be-92d2-3593-ad7a-5fa495a36a37 | -5.39465 | -44.68314 | 2025-12-30 03:44:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| e6cbc52c-3f40-339b-8869-b0cac6c85681 | -9.50797 | -35.99173 | 2025-12-30 03:44:00 | NOAA-20 | ATALAIA | ALAGOAS | Brasil | 2700409 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| d34c2951-8f85-32dc-a305-8591acc7d30a | -13.25415 | -41.33705 | 2025-12-30 03:44:00 | NOAA-20 | MUCUGÊ | BAHIA | Brasil | 2921906 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| d5301f02-caa6-3ee9-90d5-f7efb75acf12 | -12.51358 | -43.68985 | 2025-12-30 03:44:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 6b4843c3-300f-3609-a52b-6e5f75b6c9d7 | -10.15431 | -36.39292 | 2025-12-30 03:44:00 | NOAA-20 | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| e1f3e99c-a923-375f-bae2-25d75de991e7 | -11.75453 | -43.30147 | 2025-12-30 03:44:00 | NOAA-20 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 36f2a87b-3018-33fe-9068-14922973ee36 | -5.26127 | -44.73277 | 2025-12-30 03:44:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 30235ab9-4885-32d1-8148-1241b1370254 | -6.92654 | -44.58099 | 2025-12-30 03:44:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| dbee884a-c1e0-3e47-973f-8fc6bc933936 | -8.42898 | -35.23031 | 2025-12-30 03:44:00 | NOAA-20 | IPOJUCA | PERNAMBUCO | Brasil | 2607208 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 4131c8f9-8000-319e-be07-1521d8f0081f | -12.10203 | -38.00021 | 2025-12-30 03:44:00 | NOAA-20 | ENTRE RIOS | BAHIA | Brasil | 2910503 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 95bca70f-4d47-3097-8967-99b6bcba1d5a | -7.54721 | -35.18023 | 2025-12-30 03:44:00 | NOAA-20 | ALIANÇA | PERNAMBUCO | Brasil | 2600708 | 26 | 33 | nan | nan | nan | Mata Atlântica | 9.5 |
| 074061c0-196d-33c4-a8a2-4b400dbbd63f | -10.49079 | -40.54129 | 2025-12-30 03:44:00 | NOAA-20 | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |


[Clique aqui para ver as próximas entradas](README4.md)
