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

## Dados Diários - Página 34

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5647a4a5-ba60-3a1e-b7f0-d2210b76bd2b | -6.53598 | -43.11542 | 2026-08-18 04:55:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 17ced17a-7eca-3117-9ac4-e3045ea8bc02 | -4.48904 | -42.55693 | 2026-08-18 04:55:00 | NOAA-20 | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| b7574e08-0382-3b95-a899-3b1adc77fdb2 | 0.49144 | -60.59576 | 2026-08-18 04:55:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 21df1bd1-a886-3a6d-8943-996c89e755b0 | -6.26587 | -43.27972 | 2026-08-18 04:55:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 0cf38728-f182-37bb-9b01-10fb15423e0b | -2.83563 | -49.14 | 2026-08-18 04:55:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| be80ae40-d15d-363d-ad50-a3c2dd22f044 | -4.31003 | -49.08058 | 2026-08-18 04:55:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 02fc8fb4-ac1a-3c54-a6a9-14f5c913c85e | -4.97006 | -42.21676 | 2026-08-18 04:55:00 | NOAA-20 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 312622cb-5664-3dff-9cf3-df5a0aa6e31c | -2.57896 | -49.44555 | 2026-08-18 04:55:00 | NOAA-20 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 99c9ace7-0401-3577-9ae7-6c80a34c941a | -6.18374 | -47.81194 | 2026-08-18 04:55:00 | NOAA-20 | LUZINÓPOLIS | TOCANTINS | Brasil | 1712454 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ab9ee133-39a6-314e-a624-e41a1b330ab6 | -4.70465 | -55.99839 | 2026-08-18 04:55:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9e8b690b-5827-382e-becf-e256e0e329c6 | -3.54853 | -62.07923 | 2026-08-18 04:55:00 | NOAA-20 | CODAJÁS | AMAZONAS | Brasil | 1301308 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b159ce15-16a9-30cb-a417-02c5dbc69729 | -3.26083 | -49.52613 | 2026-08-18 04:55:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a5d3e27a-f4fd-3473-ab72-583421c397c7 | -6.5302 | -43.12254 | 2026-08-18 04:55:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 6964e9c3-d7ab-3ce8-b0d7-b87f9b7a548e | -6.18269 | -47.81886 | 2026-08-18 04:55:00 | NOAA-20 | LUZINÓPOLIS | TOCANTINS | Brasil | 1712454 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 4b0c734c-6bb3-35d4-9224-8bf859c7cc1f | -3.42814 | -51.51659 | 2026-08-18 04:55:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3d8c8dc6-d437-37e9-bb77-098961c589fa | -4.96973 | -42.21392 | 2026-08-18 04:55:00 | NOAA-20 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 5001abb4-2763-3cd2-b0fe-c924435dca12 | -4.01146 | -48.90568 | 2026-08-18 04:55:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 44.9 |
| f6127da0-780a-39a8-9f63-5021a96dca25 | -3.51105 | -48.03133 | 2026-08-18 04:55:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 53bd7bd5-1983-3439-bd3a-6a17095d0f73 | -6.16179 | -47.79448 | 2026-08-18 04:55:00 | NOAA-20 | LUZINÓPOLIS | TOCANTINS | Brasil | 1712454 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 379a28b6-0e32-3bda-b43e-6ec197c240ee | -6.53123 | -43.11537 | 2026-08-18 04:55:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 168cd6f6-2f52-31b3-9b1d-0c4a94bcf40e | -6.53402 | -43.12988 | 2026-08-18 04:55:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 32f4bcb7-993c-3be4-a8ca-dbdb08210f5b | -3.45684 | -56.80824 | 2026-08-18 04:55:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 47a9379d-140f-3cc4-aa81-795d235f0179 | -6.52917 | -43.12974 | 2026-08-18 04:55:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ca541ec3-2de4-3400-b051-7effcb1bcfe6 | -6.53472 | -43.13052 | 2026-08-18 04:55:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6b34926b-4afb-3c90-88b4-e3e11d3e6f6f | -2.49578 | -48.13879 | 2026-08-18 04:55:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| ab0bb3c6-414a-3b31-9a6d-8b2224611f0a | -3.4989 | -57.01896 | 2026-08-18 04:55:00 | NOAA-20 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 8166aac7-94e7-34f3-9c13-04dd154390f7 | -2.83624 | -49.14127 | 2026-08-18 04:55:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f01abdd5-6c3a-3414-875c-f54da036ef37 | -6.52994 | -43.11828 | 2026-08-18 04:55:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b3e5f644-6bdf-3d0a-80c3-f4918a39e004 | -6.16649 | -47.76324 | 2026-08-18 04:55:00 | NOAA-20 | LUZINÓPOLIS | TOCANTINS | Brasil | 1712454 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2663a3bd-be17-3d71-a2be-6c26526aa644 | -6.30581 | -47.89473 | 2026-08-18 04:55:00 | NOAA-20 | NAZARÉ | TOCANTINS | Brasil | 1714302 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7b1575ef-48f1-3087-b63e-b5987cda45b4 | -4.53719 | -42.93117 | 2026-08-18 04:55:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 63044a26-e08b-34ac-8afb-a6e77512c9d6 | -10.14511 | -54.27973 | 2026-08-18 04:57:00 | NOAA-20 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 638403ed-93fe-3630-bb2f-5f0e7321ef9b | -11.3034 | -46.33548 | 2026-08-18 04:57:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 889d2614-3bbc-364d-bbcb-b9960fb23f8b | -8.6348 | -54.70969 | 2026-08-18 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 78a6a940-ab21-329b-a88e-4200ec31e377 | -10.17674 | -54.23088 | 2026-08-18 04:57:00 | NOAA-20 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| deb0b22f-3684-31ad-9f41-b119c88a9861 | -9.77597 | -46.71598 | 2026-08-18 04:57:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 372a84e8-3b0a-3c98-85fa-b092bb3e49d7 | -8.90061 | -60.55679 | 2026-08-18 04:57:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 25a2225f-99ad-36e8-96b3-068e697bacfc | -6.69786 | -58.9589 | 2026-08-18 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 59b1a41f-73d1-3ca1-bd98-c55bc79d3b51 | -8.4906 | -54.90599 | 2026-08-18 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| a18485ab-ea87-34e7-aaf8-f498826f1332 | -8.9544 | -60.57658 | 2026-08-18 04:57:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 79d654fe-7674-34b0-a9a9-afd3943876ff | -12.34347 | -55.336 | 2026-08-18 04:57:00 | NOAA-20 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1653061b-8cd9-30a0-b70d-1da72ac69523 | -9.16693 | -59.70318 | 2026-08-18 04:57:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 27cfa5e9-a1c8-30d2-bcbf-30efcfff14dc | -7.55209 | -55.56503 | 2026-08-18 04:57:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2692c962-5555-31a1-8e48-1b391f6ab310 | -8.63597 | -54.70247 | 2026-08-18 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ed26b7b8-270e-3ad2-bc4b-15e2b18e59f2 | -11.36809 | -55.42041 | 2026-08-18 04:57:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d3ebf0a4-6b07-397d-b757-dab67c9bd99d | -10.118 | -54.27893 | 2026-08-18 04:57:00 | NOAA-20 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| cc121014-1fea-3bb8-a9a5-9b97c02cad91 | -8.56789 | -54.72831 | 2026-08-18 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 34.4 |
| e5b0ef4d-ec05-3994-860c-1bcc56bab2fc | -8.08327 | -44.35855 | 2026-08-18 04:57:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ce6ef41e-7d1e-3bd5-ac26-116d03d30401 | -9.07686 | -50.81816 | 2026-08-18 04:57:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a6a97ac2-ed3c-396f-a0e8-b045a7dabdba | -6.7496 | -59.18218 | 2026-08-18 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 31475a7d-5b7b-30c3-b07d-927e78297260 | -6.60798 | -58.39615 | 2026-08-18 04:57:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 30741ae0-0de4-391e-b54b-ebcaddfe2d44 | -9.42807 | -60.43108 | 2026-08-18 04:57:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 432bf079-577b-3b5b-993d-efddfda62e65 | -10.27328 | -50.42462 | 2026-08-18 04:57:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0c41841c-ddbb-35a0-8b0a-f02ded7445e6 | -8.57347 | -54.73667 | 2026-08-18 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 35.6 |
| 00a8aa7b-4752-3896-8c9b-a2e8adddcd98 | -8.95065 | -60.5708 | 2026-08-18 04:57:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 3fccc370-2a2b-38ae-8a5f-0593df1444bc | -12.76714 | -48.42461 | 2026-08-18 04:57:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 80aa64df-de62-3fd7-90ce-ab0682be60ef | -8.55022 | -55.3153 | 2026-08-18 04:57:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3afe7be5-b939-3fa8-ad82-2675d34a4e41 | -8.58427 | -54.71248 | 2026-08-18 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 92599ad6-f175-3828-aa2f-049402f8b7de | -11.20451 | -54.81281 | 2026-08-18 04:57:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7b70bd0c-6f2c-362f-94bd-629ccf480fa9 | -11.7399 | -54.59172 | 2026-08-18 04:57:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 05a67afb-3f2c-3ce3-a784-24fb328ce945 | -6.75625 | -59.16996 | 2026-08-18 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 1c0ad272-6b5b-386c-b8a5-752eb620f274 | -8.20187 | -55.04087 | 2026-08-18 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e44e8bea-7afa-3510-bd3b-b98fd4a110cc | -7.39551 | -46.47994 | 2026-08-18 04:57:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| bfb42b8b-9acf-3712-8479-f2c18ef10ae3 | -6.75255 | -59.16188 | 2026-08-18 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 6270db9f-c99b-3262-8e69-5e5245dc1c18 | -7.07206 | -56.65836 | 2026-08-18 04:57:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a5529d28-6b60-3196-8f8e-c09177b60e9a | -8.51031 | -45.32018 | 2026-08-18 04:57:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0137456b-79ae-3ccf-a09d-d46d664774e8 | -6.02241 | -57.81153 | 2026-08-18 04:57:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 198eaf36-a912-3f0d-9391-69a51d671aeb | -8.10418 | -51.65886 | 2026-08-18 04:57:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a559b352-0a7e-3ce0-8af7-412163ea2295 | -12.13317 | -57.21249 | 2026-08-18 04:57:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ab15af8b-caef-307d-86f4-0bbbb3f5bacf | -6.87296 | -56.41965 | 2026-08-18 04:57:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e976f7c3-bb57-3598-90fe-1acceb9dfcc5 | -9.21566 | -50.1026 | 2026-08-18 04:57:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c74d02ff-9c8a-3317-8937-a0c9f22e6ff7 | -7.38336 | -59.99893 | 2026-08-18 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6e76181c-1b66-3c12-9997-496cb9147f5b | -10.51508 | -50.79026 | 2026-08-18 04:57:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6d5b4690-aa60-35ec-af4b-a9a6d81fa549 | -8.58322 | -54.69752 | 2026-08-18 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| c3357a39-946c-3107-832e-4583901ca1f3 | -13.27617 | -51.65552 | 2026-08-18 04:57:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2c186cc6-5035-3e34-bca3-208aa604b515 | -10.14843 | -54.28028 | 2026-08-18 04:57:00 | NOAA-20 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 012d0df7-4673-3e0e-8467-654e88f10f93 | -12.46228 | -54.19373 | 2026-08-18 04:57:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 936f7a49-9bae-3ca4-9a9e-94d95fdeb001 | -8.57707 | -54.69278 | 2026-08-18 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 15.2 |
| 76d527dc-1155-3293-aa20-81ed91defec4 | -8.2266 | -55.04071 | 2026-08-18 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 4f25b81e-4506-314f-860c-b1b0be571ada | -6.71642 | -58.92852 | 2026-08-18 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 04bdb3f1-e817-32a1-821f-bd5b804e8a94 | -11.11978 | -46.49854 | 2026-08-18 04:57:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| ac32648d-5094-3c4d-9b5d-437afcd41c17 | -12.15826 | -57.21684 | 2026-08-18 04:57:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 041503c3-23ac-3c4c-a31f-c5ed4d6783c2 | -11.34079 | -55.26992 | 2026-08-18 04:57:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1f3a715a-7e1d-318d-bf79-84a480a2783b | -6.13973 | -57.73675 | 2026-08-18 04:57:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b38e8f7e-28b0-3fdd-8603-ccdf438a2a18 | -9.58582 | -60.49921 | 2026-08-18 04:57:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d2e83f7b-525d-34ce-ba8d-179120342a0e | -8.57301 | -54.71802 | 2026-08-18 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 23.2 |
| 77189b77-cc03-35d9-b50f-7d60f8a86918 | -6.70143 | -58.93829 | 2026-08-18 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| ea934ed6-0a34-3224-8ea6-26f8177f6ea9 | -14.22757 | -45.41382 | 2026-08-18 04:57:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 11f42427-da20-3fcc-b7b4-2351bb661096 | -8.58369 | -54.71608 | 2026-08-18 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| d155c805-1c6d-3805-997e-e5be98644083 | -13.43694 | -43.84058 | 2026-08-18 04:57:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 53019b36-1131-390b-98fb-b64abbb1e875 | -8.60625 | -50.34831 | 2026-08-18 04:57:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| d3a1cec4-59bd-3c8a-aa5d-f4d54cf1f8f8 | -6.62489 | -53.38573 | 2026-08-18 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 87ec1d02-1695-31f7-ae7b-2300e811133a | -8.89817 | -60.57874 | 2026-08-18 04:57:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e45f7d76-b950-38df-9ac2-2bf32f1410e8 | -7.56257 | -55.56681 | 2026-08-18 04:57:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| deb291ca-0329-3cc3-b31a-bf29c9d4367e | -8.31817 | -46.48005 | 2026-08-18 04:57:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| aaf53b55-9a53-3f4e-8ec6-68b707f07858 | -8.58358 | -54.73833 | 2026-08-18 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 54.0 |
| 99eea4ab-0df0-3db1-8b13-7bce690165c3 | -11.20785 | -54.81337 | 2026-08-18 04:57:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7f1263f3-57d5-3a42-a23d-a134a32663fc | -12.46284 | -54.1902 | 2026-08-18 04:57:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ba4a2d3a-f137-3d2b-9425-045ab0c17da2 | -6.75553 | -59.17091 | 2026-08-18 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 5c52b2c0-7c42-34ca-9242-27b3cca19ccf | -6.95418 | -59.03977 | 2026-08-18 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |


[Clique aqui para ver as próximas entradas](README35.md)
