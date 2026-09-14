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

## Dados Diários - Página 49

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bd36f343-f97f-32d7-a07c-71ff9194e938 | -9.43943 | -47.86019 | 2026-09-14 04:53:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ce265874-0a56-32db-8380-2fc15e8321ce | -8.44295 | -46.0317 | 2026-09-14 04:53:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 09065b3a-bede-3990-ba67-8f8ce812cb21 | -9.4005 | -50.19201 | 2026-09-14 04:53:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a5e78b06-ca5f-38fa-917a-5111df34e326 | -9.13912 | -51.58545 | 2026-09-14 04:53:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e27d0987-09af-3be1-a8a4-58e2556aec4f | -6.28661 | -59.94279 | 2026-09-14 04:53:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 27309c36-06be-3a4f-a1d8-487055711e6a | -7.86767 | -54.72591 | 2026-09-14 04:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4e8d36ea-5bec-3f2b-962d-dbb281ed5841 | -10.56966 | -51.33817 | 2026-09-14 04:53:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| bea5942e-d492-36f4-a3cd-2fb1840bb803 | -6.68522 | -59.13005 | 2026-09-14 04:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2f0a79d4-73e1-3b52-acc7-6f1ada078b95 | -6.29531 | -59.95419 | 2026-09-14 04:53:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 98a9ab75-bdc9-3f3b-a419-a46924238353 | -7.95931 | -43.98751 | 2026-09-14 04:53:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 576f8442-735e-31e2-869d-9e8b3b9228ed | -7.47741 | -42.11938 | 2026-09-14 04:53:00 | NOAA-20 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 9b358b75-3f4c-37fc-a0c1-d2044092030d | -6.11258 | -57.67901 | 2026-09-14 04:53:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 48d54fd1-0158-353e-81f6-2b5fe754d6d9 | -10.68833 | -54.15976 | 2026-09-14 04:53:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a88e6c0b-0600-31db-895c-68b37a41619d | -10.66904 | -54.1488 | 2026-09-14 04:53:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 30.7 |
| cdf279bc-0ba9-3fb2-a09e-0538a39d45af | -15.52998 | -47.89415 | 2026-09-14 04:53:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ea4f1ed0-19be-3900-8aa6-d6c4f69c680d | -9.3778 | -50.11269 | 2026-09-14 04:53:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 15c922f8-aad1-354c-a7d2-c54011f6d27c | -5.73057 | -60.2234 | 2026-09-14 04:53:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7ba5362e-1a90-3eaf-8193-41b43a20706a | -5.13231 | -55.96089 | 2026-09-14 04:53:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5ec9264a-9c45-325e-aa7d-1a822a5cbc92 | -5.84424 | -52.097 | 2026-09-14 04:53:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| bba598f8-4fbb-3eb0-8a35-f68a676ac01c | -11.77852 | -46.40268 | 2026-09-14 04:53:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3c20ad75-7b33-3309-9702-026642af5122 | -6.5875 | -58.84661 | 2026-09-14 04:53:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| aa888ad2-3110-3bb2-a80e-420453b5ca3c | -10.54244 | -51.29739 | 2026-09-14 04:53:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c036ea36-3099-3b19-a539-0ed9bf408677 | -6.30155 | -59.94889 | 2026-09-14 04:53:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5effd2fd-c0b3-304c-b5e0-05f29f56b89f | -5.07903 | -56.25729 | 2026-09-14 04:53:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4638ff40-80b0-34e7-a7d1-a7498a06de81 | -10.52251 | -51.3595 | 2026-09-14 04:53:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 76249fff-f91c-30ad-adea-66e51f865615 | -9.00146 | -50.81958 | 2026-09-14 04:53:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| d649bfd3-9239-3deb-8d95-fd3e64ad38ec | -10.20059 | -45.29484 | 2026-09-14 04:53:00 | NOAA-20 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4b12edfd-4541-3826-8334-3dba1f312948 | -6.7927 | -58.79662 | 2026-09-14 04:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 65f14070-c6c4-3521-8633-b0c1f1a0cebc | -9.3362 | -44.37076 | 2026-09-14 04:53:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| a52ad221-8901-3f03-9161-3eba10d984b0 | -4.77502 | -56.15314 | 2026-09-14 04:53:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 84da6e1b-73f5-3172-9acc-c7f9de4dc061 | -9.33211 | -44.36506 | 2026-09-14 04:53:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 2c0fb6cb-747d-327d-bf38-2a418280f6e6 | -8.12108 | -44.05274 | 2026-09-14 04:53:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a4c5e0e7-da12-3174-b725-5e913e021f17 | -11.51491 | -50.25505 | 2026-09-14 04:53:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7715596e-108f-3b86-b418-e59e87984cbe | -9.41471 | -50.16772 | 2026-09-14 04:53:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 17.3 |
| 1b6cbcab-edde-3ccc-88ec-5ed5eab97540 | -7.82777 | -49.46742 | 2026-09-14 04:53:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5b6876c8-dc83-34c3-90c9-d401e7d5428c | -6.32777 | -60.01991 | 2026-09-14 04:53:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0cdef4d5-2189-3482-9436-4aa3d415e00f | -6.01686 | -59.94628 | 2026-09-14 04:53:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 6c7dd17b-545a-32db-989c-b85b1fc7cba8 | -6.30726 | -59.95485 | 2026-09-14 04:53:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c54a6551-c30e-3f91-a7e9-030f478e150f | -8.38994 | -46.29924 | 2026-09-14 04:53:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 62198637-04a6-3a4b-a15c-33312aaa3517 | -6.10433 | -55.66091 | 2026-09-14 04:53:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 00e9b1d5-e7ea-3238-ae40-6fcb23b6cf02 | -7.09268 | -55.62007 | 2026-09-14 04:53:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5c96e0d7-8a35-3ed2-bcfa-72e864e89a01 | -6.31895 | -59.97911 | 2026-09-14 04:53:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 331d84a7-c4b0-33a8-82c4-4bb8de4f18ae | -10.548 | -51.30556 | 2026-09-14 04:53:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 67f476b9-bdbb-3454-8edf-3faea7bacc14 | -10.6678 | -54.15631 | 2026-09-14 04:53:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 26.7 |
| c8172846-3886-3953-bdbd-45f7fe1b0d35 | -6.29 | -55.29196 | 2026-09-14 04:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b52d08cc-c8b8-3f8e-9f81-5aba5c267bb5 | -7.33902 | -55.21645 | 2026-09-14 04:53:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f8c1cad3-5559-3ffe-8aa5-281b018c4ecd | -10.543 | -51.31567 | 2026-09-14 04:53:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 79804531-2e7f-3c9d-94fa-6280a8b8b879 | -9.44933 | -47.86887 | 2026-09-14 04:53:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| dfecca3f-ab0e-30da-a0f3-563c86b0c1eb | -10.67495 | -54.13437 | 2026-09-14 04:53:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5c6202a4-aa76-3be6-84c4-dd0a59003ce1 | -7.01829 | -44.6347 | 2026-09-14 04:53:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| bbd97e3d-e515-386b-a454-a7b90f1fb3d2 | -6.58336 | -58.86913 | 2026-09-14 04:53:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 59182590-b4c8-3d4a-a9cd-ae48c6e227b8 | -9.41813 | -50.14552 | 2026-09-14 04:53:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 82c0ac86-dad2-3eeb-b6f2-9bdd74cd92aa | -4.38256 | -55.20224 | 2026-09-14 04:53:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| ecb7b7b3-154e-3620-9094-eb007852d22a | -9.37442 | -50.1804 | 2026-09-14 04:53:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7ae1dcad-eb58-34bc-a9ae-d451c6e6eba5 | -10.66842 | -54.15255 | 2026-09-14 04:53:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 26.7 |
| f803b987-aeb9-341f-9384-f3cd909dc947 | -6.59138 | -58.85273 | 2026-09-14 04:53:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2f6c74d9-bf0f-3ef7-b418-5ae3e50c02c8 | -10.64764 | -50.57423 | 2026-09-14 04:53:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| eb25c796-b30e-3827-97b3-e9558c21fadc | -12.10346 | -47.31672 | 2026-09-14 04:53:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 89c844fb-7b7b-359c-b24e-23d5a4eea71c | -6.37733 | -55.25558 | 2026-09-14 04:53:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| be80cc65-d371-33dd-84c6-740073461bb7 | -6.01852 | -59.93682 | 2026-09-14 04:53:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 616595e9-6578-3ed6-87f7-21df5862096a | -12.17518 | -48.96497 | 2026-09-14 04:53:00 | NOAA-20 | SUCUPIRA | TOCANTINS | Brasil | 1720853 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 142d9fc5-9939-3328-b29c-a967193502f4 | -6.58571 | -58.85711 | 2026-09-14 04:53:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 97860144-a777-3827-aa5a-25a63da3053f | -9.43348 | -50.13653 | 2026-09-14 04:53:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0065fcc3-fa3b-3a67-af48-da27f3101cef | -10.23652 | -50.9053 | 2026-09-14 04:53:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 20247457-35ec-3bc2-8295-45b498f3ab32 | -6.29378 | -55.29269 | 2026-09-14 04:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 98284bf7-1500-38e3-af31-0863cb4895b5 | -4.12504 | -60.68085 | 2026-09-14 04:53:00 | NOAA-20 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 19.2 |
| 67086a1e-f28a-3e87-ba44-86f40c2b6b79 | -6.64593 | -59.96175 | 2026-09-14 04:53:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| b80889b7-15c9-3182-8192-a967d61a7b59 | -9.44144 | -50.13018 | 2026-09-14 04:53:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 24ba0226-4a91-370a-a41f-73d25c2eb708 | -11.17684 | -46.38768 | 2026-09-14 04:53:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 927b0a0a-801f-309a-bf59-54f6af432b89 | -3.73275 | -61.76345 | 2026-09-14 04:53:00 | NOAA-20 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f7bb939f-75b4-3834-9a4f-3db29671eb8e | -4.39479 | -55.20613 | 2026-09-14 04:53:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 61e3398f-b983-33c7-8213-db20d9a72186 | -6.02317 | -59.9408 | 2026-09-14 04:53:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 681c3771-f5ad-394d-9b79-a77bc5bfcba6 | -7.08318 | -43.551 | 2026-09-14 04:53:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bd8c72a8-6eb3-3fa0-9736-cabb7e9aeadc | -7.09293 | -41.80154 | 2026-09-14 04:53:00 | NOAA-20 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 5dfd57b2-e6f9-3983-b476-cfd5ec5dccc8 | -10.42999 | -48.64899 | 2026-09-14 04:53:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 24.7 |
| aac75886-ae1e-3a08-94f6-722d3814f40f | -10.57354 | -51.33514 | 2026-09-14 04:53:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2cfc1d45-165b-3a56-a817-8c459f8e579e | -6.13331 | -57.69171 | 2026-09-14 04:53:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f41ca6bd-50a5-3bde-8046-edd87aee048e | -6.29477 | -59.95734 | 2026-09-14 04:53:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cee013ec-e73a-3560-937d-ed882bcfe567 | -9.12257 | -51.58283 | 2026-09-14 04:53:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1b8a7824-b33b-3046-aa0c-f7ee8f2af0d6 | -10.64311 | -50.58107 | 2026-09-14 04:53:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ff176d63-6175-39f8-ae70-51e70a4097a1 | -3.35365 | -59.83173 | 2026-09-14 04:53:00 | NOAA-20 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cc372ce9-4204-39cd-b05b-361e5757ce38 | -8.17132 | -43.10878 | 2026-09-14 04:53:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 1dbda6f7-0551-3e03-a8b6-c7c9b5353af2 | -5.71002 | -51.74585 | 2026-09-14 04:53:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d00dd1dd-34f0-33e3-b108-830857d0e881 | -4.12687 | -60.68609 | 2026-09-14 04:53:00 | NOAA-20 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| d3740ae6-5ecb-3709-ac0a-b2d650af4390 | -4.09504 | -54.44198 | 2026-09-14 04:53:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d3fa36e2-0ed1-3410-8dab-4275890ea903 | -10.74909 | -54.08919 | 2026-09-14 04:53:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c64a8ebb-85c6-331f-aa96-3a1fc4c10080 | -9.98692 | -50.27312 | 2026-09-14 04:53:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 70015941-6b9b-3e3a-8476-f315fd2187b7 | -4.39033 | -55.20345 | 2026-09-14 04:53:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f87a775a-fba8-33ce-aae1-5fd71a279269 | -3.3551 | -59.628 | 2026-09-14 04:53:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5cdd9c87-77eb-324e-84ec-ab3ad9560f0f | -10.23932 | -50.90944 | 2026-09-14 04:53:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ecd135a3-bbcc-379b-9879-4245ffece1d3 | -9.42213 | -50.11957 | 2026-09-14 04:53:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 2a66e409-83f1-326e-8854-6baeb08af792 | -6.59186 | -58.8491 | 2026-09-14 04:53:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6b0e2ca6-3cf9-3d6d-a61e-c99c80692afa | -10.56354 | -51.33353 | 2026-09-14 04:53:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 29d20c6c-5810-31b6-bd4e-8f2bf37aa9bb | -6.19734 | -53.08928 | 2026-09-14 04:53:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f7fda889-3607-329c-a0e3-83f70340a3b3 | -13.63117 | -47.9005 | 2026-09-14 04:55:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| df8e210b-ca08-3e89-a0be-09fc41ba48f4 | -15.08192 | -48.32679 | 2026-09-14 04:55:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b5cf1128-cc15-31e6-983e-66e435d42a93 | -13.31114 | -51.31149 | 2026-09-14 04:55:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6c41faea-3dc7-335e-95d0-1ddd2d2aeaff | -13.06522 | -48.6022 | 2026-09-14 04:55:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| db54893c-a750-3281-92a8-67c070db6cd0 | -14.189 | -47.3928 | 2026-09-14 04:55:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 7ce278aa-f027-326e-868f-24134a39a22d | -12.74235 | -48.45668 | 2026-09-14 04:55:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |


[Clique aqui para ver as próximas entradas](README50.md)
