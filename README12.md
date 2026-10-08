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
| ab49ecbe-110d-3f29-911e-a954362a57ed | -3.7367 | -54.646301 | 2026-10-08 00:26:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2d267eb5-6286-36d5-8dbd-a176508e2932 | -2.7824 | -54.074501 | 2026-10-08 00:26:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b2361b9e-014a-3bfa-8665-75f14e40cad4 | -3.8656 | -55.9967 | 2026-10-08 00:26:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0287c855-60ed-33f0-8fce-0fbfe4ce830d | -3.5942 | -54.563499 | 2026-10-08 00:26:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d811f1da-02dc-3cbd-a9ae-b9fdf2163208 | -3.6681 | -57.092701 | 2026-10-08 00:26:00 | METOP-B | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 81ecb3b7-bc2b-346c-8763-95fa84f20b68 | -7.2225 | -55.166 | 2026-10-08 00:26:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ad36e5bd-8dc5-3a3a-9b01-628e8df9de02 | -3.0532 | -53.904701 | 2026-10-08 00:26:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| be134b19-ae03-3076-a0c8-680fdbe2af45 | -9.8745 | -50.500801 | 2026-10-08 00:26:00 | METOP-B | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1bb21d70-ad4d-3599-9e3f-b28cbd00219f | -3.5082 | -59.935001 | 2026-10-08 00:26:00 | METOP-B | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e1791842-8df7-361e-9814-d0c2850c357b | -3.2193 | -53.955002 | 2026-10-08 00:26:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1b093091-7dde-3af5-950e-f008188bdbf2 | -7.4586 | -42.865799 | 2026-10-08 00:26:00 | METOP-B | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| cad19413-ac28-3a94-9c2a-abad843674d0 | -3.2126 | -57.8638 | 2026-10-08 00:26:00 | METOP-B | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| bb90b9ad-9735-3f4c-887b-15ed9fd87280 | -3.5538 | -54.658298 | 2026-10-08 00:26:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b2b81f8e-5ea2-3cd5-81b1-3cb1afa04b62 | -3.2707 | -54.0453 | 2026-10-08 00:26:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 24ebaced-9b69-3b9e-8fdd-7802ec7a8d98 | -5.7354 | -53.456299 | 2026-10-08 00:26:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9d6bdc7e-7e8a-36ba-9dba-dbf3f4a9f762 | -2.5872 | -56.176201 | 2026-10-08 00:26:00 | METOP-B | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a3cb387a-085e-3074-a9a7-e91f0686d8b9 | -3.542 | -50.104198 | 2026-10-08 00:26:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 382a7a45-3ebc-3e8a-82bb-4a3fe4785c18 | -3.0804 | -54.297501 | 2026-10-08 00:26:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2ee2c753-de68-3c43-9472-10aede8ca8e6 | -8.9031 | -49.967602 | 2026-10-08 00:26:00 | METOP-B | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 46a5059f-d34c-308b-a02d-250a79124a22 | -1.5162 | -54.811001 | 2026-10-08 00:26:00 | METOP-B | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bac2d3ac-245b-3380-8d37-bcdacaba9d7e | -2.469 | -56.063301 | 2026-10-08 00:26:00 | METOP-B | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a753ab00-bd37-3b48-92c7-330b5d4df681 | -3.6056 | -54.5681 | 2026-10-08 00:26:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b9d55dc0-34ff-3cb5-a9d9-0eaabe7bd0a2 | -4.8965 | -54.990299 | 2026-10-08 00:26:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 85e2a15b-b883-342d-83a8-9bcb7f93dc22 | -2.8715 | -54.148998 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| af14ab6a-c95d-3085-972a-bd9629aadb18 | -2.8456 | -54.125801 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9da2f92e-4e62-3341-baac-8d9c1b61b3a5 | -3.0847 | -58.028301 | 2026-10-08 00:26:00 | METOP-B | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a83f472b-3e51-3578-a1b8-6c569ad69536 | -16.861401 | -40.586498 | 2026-10-08 00:26:00 | METOP-B | SANTA HELENA DE MINAS | MINAS GERAIS | Brasil | 3157658 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| ec94544b-f709-3920-8c56-b48382133d9f | -2.5711 | -56.150299 | 2026-10-08 00:26:00 | METOP-B | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| eab442bf-4738-3f85-a93a-5f82609fbafd | -2.5075 | -56.142399 | 2026-10-08 00:26:00 | METOP-B | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ff42a9cc-77c6-3b72-8177-a2225e0f1d09 | -3.4935 | -59.590199 | 2026-10-08 00:26:00 | METOP-B | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 73f34b8b-cc01-3531-be07-dd14b9a5e779 | -2.9708 | -54.177502 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 453c846e-9479-3941-a7dd-d384d628e16a | -6.0313 | -51.728901 | 2026-10-08 00:26:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 91b4a87f-6b08-3a33-9d0c-c536a79be463 | -3.0198 | -54.1665 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 11856707-b500-3053-a3a1-2b21fc8adc45 | -2.9268 | -54.1656 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7c23b25e-5472-3477-985a-bf0f7ae4db39 | -10.6258 | -53.848202 | 2026-10-08 00:26:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d26aae41-645a-3db7-9d21-82a453874547 | -3.09 | -54.1581 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6791ae2f-5fdb-3b17-befb-fdefa06b66ec | -3.0211 | -54.035702 | 2026-10-08 00:26:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a8907c68-c996-36ec-9ee6-44b91677c07c | -3.604 | -54.561298 | 2026-10-08 00:26:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 018a6555-bafa-3b64-a7eb-4a80bd3b6cf5 | -4.0707 | -59.835701 | 2026-10-08 00:26:00 | METOP-B | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 37fab44e-3357-33c7-b56c-c3366b646491 | -5.8382 | -52.055 | 2026-10-08 00:26:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 63f3d731-9751-3f6f-acb9-c15ed88ff9dc | -1.3267 | -55.431801 | 2026-10-08 00:26:00 | METOP-B | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5264fad2-d54e-31f4-ac07-de7849770cc5 | -2.4959 | -58.063301 | 2026-10-08 00:26:00 | METOP-B | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b318ee82-22f5-3d2d-bbc3-04f5c7e7da60 | -1.1098 | -54.1549 | 2026-10-08 00:26:00 | METOP-B | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c72909ff-3b84-35ab-bab3-00101f978e86 | -1.5244 | -54.528702 | 2026-10-08 00:26:00 | METOP-B | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7cd7eee4-16e5-372c-b04c-21241609160e | -3.7096 | -59.6395 | 2026-10-08 00:26:00 | METOP-B | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 4b8e7ad4-f358-36b2-bbbc-18ead231be18 | -3.2738 | -54.059101 | 2026-10-08 00:26:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 59172001-365e-325c-a8ba-39e9d148b075 | -2.5774 | -56.178299 | 2026-10-08 00:26:00 | METOP-B | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 87285db1-2ab6-3ea2-ae89-75bd9a91ffa5 | -6.1148 | -55.6936 | 2026-10-08 00:26:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a343add8-8855-376a-8d9f-9155839df36e | -3.0809 | -54.254101 | 2026-10-08 00:26:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 402a251c-c3be-39cd-beb9-3dfff98657c1 | -3.5802 | -59.518501 | 2026-10-08 00:26:00 | METOP-B | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f0cb81a1-0863-3ece-827e-516dd264133f | -1.4562 | -54.774101 | 2026-10-08 00:26:00 | METOP-B | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a704c0f0-5985-3f32-ae7f-edd5dfe6c424 | -5.3429 | -50.9818 | 2026-10-08 00:26:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 41ef9501-aa72-33a8-8265-6df7c619fc0d | -8.202 | -46.3232 | 2026-10-08 00:26:00 | METOP-B | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ff36b7a3-1b11-38c7-a90e-a34a7d165b90 | -4.9851 | -56.213799 | 2026-10-08 00:26:00 | METOP-B | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4eb4521b-cf01-3fef-98b7-8473fa3ea1ea | -3.544 | -54.6605 | 2026-10-08 00:26:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f93f8008-a9e7-3db0-b97e-a77342927920 | -1.5208 | -54.831501 | 2026-10-08 00:26:00 | METOP-B | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ee92f388-4fa0-3eb2-8f2d-6c759f9dfc0f | -3.0566 | -54.2379 | 2026-10-08 00:26:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0ebe7f98-85e1-353d-a27f-adba59129cd8 | -2.9935 | -54.186901 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 82b911a6-bc9f-3bab-b7e8-c7810bd47e7f | -3.1052 | -54.270302 | 2026-10-08 00:26:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 636af5ea-fb12-3ab9-8669-8a669314927e | -6.1896 | -53.141201 | 2026-10-08 00:26:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4f7865c7-5684-3ac1-9a9c-e5dba6c598a8 | -6.1516 | -52.657398 | 2026-10-08 00:26:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1542a454-8780-364a-bf99-a7b347020e4e | -3.4387 | -59.528198 | 2026-10-08 00:26:00 | METOP-B | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 84c01b1b-b723-3bf0-a6d9-1837098a3b60 | -2.4592 | -56.065498 | 2026-10-08 00:26:00 | METOP-B | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| abb01ac1-8be5-3f16-8f58-c10799900faf | -3.5518 | -59.4827 | 2026-10-08 00:26:00 | METOP-B | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 1ccd9228-d729-39c2-86a5-301b4a6d3652 | -5.8982 | -53.492401 | 2026-10-08 00:26:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| de4f05a7-cb62-395a-b211-9c90e452479e | -3.1193 | -53.7873 | 2026-10-08 00:26:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e6bdb6eb-b794-33c2-917e-ad3cb893cc90 | -6.0982 | -49.403599 | 2026-10-08 00:26:00 | METOP-B | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 26d05270-1e3a-31cb-8da1-619c6a4d2515 | -2.5742 | -56.164299 | 2026-10-08 00:26:00 | METOP-B | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c509a4d5-5772-3868-b232-ef55e3633811 | -5.2927 | -60.085201 | 2026-10-08 00:26:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 39a3d937-8b3c-3771-8c0d-dbb32d9d48de | -2.8931 | -54.107899 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f7bc991e-f1e3-3d87-8910-02d68b6fae28 | -2.8548 | -49.537399 | 2026-10-08 00:26:00 | METOP-B | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1c1b30d7-0588-3008-8eeb-d9754a3285e4 | -6.8084 | -55.294701 | 2026-10-08 00:26:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ce6b3161-52fa-3b3b-9ec6-0ddcfc5f084f | -3.1177 | -53.7803 | 2026-10-08 00:26:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4e6d508e-72c4-3467-a1a4-ed995a14ab53 | -3.5456 | -54.6674 | 2026-10-08 00:26:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| da29f72c-7fa2-3a27-ae5e-bb37fad6f1ff | -3.284 | -54.013302 | 2026-10-08 00:26:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f0497700-5da4-3d2c-94b8-f5626706c3c2 | -3.5638 | -59.490601 | 2026-10-08 00:26:00 | METOP-B | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2d014a7c-18a5-3d5e-8f1b-a84184c1014e | -3.2789 | -54.036201 | 2026-10-08 00:26:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 623c6685-05b1-340e-b761-b73a078bfe87 | -3.3889 | -59.5811 | 2026-10-08 00:26:00 | METOP-B | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c38865a9-33b7-36cb-922e-b3932a7a3d68 | -2.9996 | -54.7603 | 2026-10-08 00:26:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3aae85fd-8f73-3b48-ace5-c018fe4f564a | -3.2597 | -53.996899 | 2026-10-08 00:26:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9c8be9eb-9ef9-3898-8a91-d3dc8a1915fb | -6.469 | -55.480999 | 2026-10-08 00:26:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cb9d10c3-a0c8-35c1-9f18-54702bd62c5a | -3.0477 | -54.153099 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e6500c5e-9bd5-353f-92e7-ef422b15f370 | -2.5695 | -56.143398 | 2026-10-08 00:26:00 | METOP-B | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 10eaa29f-cfc3-3740-9b98-ddedf82793ed | -2.4831 | -56.1259 | 2026-10-08 00:26:00 | METOP-B | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 92baccb7-2c78-32da-ba19-d16d5d08520d | -2.4929 | -56.123699 | 2026-10-08 00:26:00 | METOP-B | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 06d48c09-40f7-347b-9dd0-f982dbf37948 | -3.0593 | -59.252399 | 2026-10-08 00:26:00 | METOP-B | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| acdba50d-a2e1-3a73-9e70-3a2f286601d8 | -3.0414 | -53.943802 | 2026-10-08 00:26:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4a271869-b010-39fb-b74a-1e30e8bebd4e | -3.0269 | -53.925098 | 2026-10-08 00:26:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 113ea994-9cfa-349d-a9ad-55ab93ce3fe4 | -4.0673 | -51.038101 | 2026-10-08 00:26:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 958a60d0-3ff2-39bf-90a7-39b815eb212b | -11.5262 | -47.590199 | 2026-10-08 00:26:00 | METOP-B | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1713e560-fa00-3f39-b121-25ce8569589a | -13.6907 | -49.110699 | 2026-10-08 00:26:00 | METOP-B | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 884563e2-f061-3daf-9918-5b24071e4fd2 | -2.9963 | -54.063 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f9dbab68-3227-3fdf-be13-1864f918f161 | -3.001 | -54.083801 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 665a1d85-f054-3d2d-b440-2e54ebe276aa | -2.9841 | -54.145599 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4a6ff3d3-f22f-3dfd-929b-f5160b504c21 | -2.8632 | -54.1581 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4a1db843-2b88-3237-ac80-68863b6d52a9 | -3.2769 | -54.072899 | 2026-10-08 00:26:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ea2414f7-584b-3fd0-bb5e-8bf0f28ea4d4 | -3.224 | -54.294201 | 2026-10-08 00:26:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d5e22baf-e7cd-3d98-84a7-068cec07c6a9 | -3.5125 | -59.305199 | 2026-10-08 00:26:00 | METOP-B | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 0c594325-a4a6-3d1f-ab4f-5a585612eb77 | -3.1695 | -54.736801 | 2026-10-08 00:26:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6305de98-c1f8-334e-9568-8b910820cf37 | -3.003 | -54.047001 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README13.md)
