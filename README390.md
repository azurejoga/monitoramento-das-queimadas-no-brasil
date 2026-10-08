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

## Dados Diários - Página 390

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5744d04f-2579-3368-9fa8-826e11a0eaaa | 1.6938 | -55.6066 | 2026-10-08 18:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 65.6 |
| a7b8c4b4-8eb6-3e28-b1c6-afe9f8eb1045 | -9.3566 | -65.7436 | 2026-10-08 18:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 89.7 |
| c49a7e49-da07-35c0-8952-456870ddbdee | -3.1115 | -53.7637 | 2026-10-08 18:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 89.3 |
| 4a280dd7-1df9-3d3b-b68e-48e56627b647 | -1.5306 | -54.5558 | 2026-10-08 18:20:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 126.4 |
| d2b657ac-31c0-36eb-bc28-e7199ee41010 | -8.6136 | -44.873 | 2026-10-08 18:20:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 102.0 |
| 65c593c2-ccad-3882-a15b-03d8c7d0051a | -5.7729 | -45.3995 | 2026-10-08 18:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 87.5 |
| a47ca039-cbfb-34b7-a921-c68112ffb72c | -6.1298 | -51.9281 | 2026-10-08 18:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 58.5 |
| 396d7a36-97e0-3df2-b59f-6d4f2297b31e | -7.1894 | -44.2811 | 2026-10-08 18:20:00 | GOES-19 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 60.0 |
| c906d366-44b2-3f3a-8987-445305c6b6dc | -6.1977 | -52.7886 | 2026-10-08 18:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 84.4 |
| 41f94490-e71c-398a-b127-3d62aef17adf | -3.0374 | -53.9268 | 2026-10-08 18:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 78.4 |
| 1b0e0c1c-9e98-3b16-acf9-655526008df2 | -4.0838 | -44.1159 | 2026-10-08 18:20:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 294.7 |
| e6680b70-e772-3fc9-b971-dd59d918d6b1 | -3.4312 | -56.9307 | 2026-10-08 18:20:00 | GOES-19 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 94.6 |
| 3f257b2c-9341-3d81-942b-c53bc98602de | -3.2136 | -42.9764 | 2026-10-08 18:20:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 177.9 |
| 5c688e83-31fb-3994-a101-fb73c417fd30 | -2.5903 | -56.1642 | 2026-10-08 18:20:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 203.7 |
| 83c9df07-9207-3f01-9820-9665ee8959b4 | -5.4958 | -42.8413 | 2026-10-08 18:20:00 | GOES-19 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 149.4 |
| 6c0f2bba-b0bb-35f2-a044-5a5aa3e538d0 | -2.9005 | -56.6685 | 2026-10-08 18:20:00 | GOES-19 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 69.9 |
| c079dd8d-d93b-3936-9f47-731c39831b69 | -8.2176 | -46.4068 | 2026-10-08 18:20:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 90.7 |
| 685317ea-d272-3afa-b7e3-31baa772512f | -1.8232 | -54.9904 | 2026-10-08 18:20:00 | GOES-19 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 57.6 |
| 49db02e4-82d3-3828-8025-6c0d8940cb0b | -11.1666 | -47.7922 | 2026-10-08 18:20:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 114.5 |
| 2785b2a5-cdbe-3261-b960-354625f4635a | -4.7589 | -55.6516 | 2026-10-08 18:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 57.1 |
| 8e1d23f3-a065-3b6c-83a9-ff53699781b3 | -9.3565 | -65.7623 | 2026-10-08 18:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 92.4 |
| b1ab3229-3a1a-3a37-aa80-bc5d16f77340 | -6.1747 | -53.4224 | 2026-10-08 18:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 88.3 |
| 23309273-11aa-3985-9b33-4118fa8a5786 | -9.0362 | -44.3654 | 2026-10-08 18:20:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 137.0 |
| 75dd226c-768e-3fa6-9159-791424de4a0c | 3.5448 | -51.2772 | 2026-10-08 18:20:00 | GOES-19 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 55.3 |
| 24924faa-a790-38dc-9de9-212a49660613 | -5.699 | -45.2918 | 2026-10-08 18:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 97.5 |
| baa9a7c1-8fc7-31c9-bd95-6545a125ca1b | -11.2816 | -41.1194 | 2026-10-08 18:20:00 | GOES-19 | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 244.6 |
| 4b6652ac-4942-338e-9152-a6f89761d8ba | -2.7613 | -54.0941 | 2026-10-08 18:20:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 157.3 |
| cdb50fdf-7221-3cc6-a269-db9de79e9183 | -2.4806 | -56.0678 | 2026-10-08 18:20:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 80.1 |
| b50f72b0-77e1-304e-9024-860eb8ce5598 | -2.8433 | -57.4891 | 2026-10-08 18:20:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 97.6 |
| bfd1574d-0882-3768-8059-0b12d87df737 | -11.8696 | -43.5568 | 2026-10-08 18:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 131.3 |
| 1f7f0418-1480-3b64-99eb-f8d879ba73b7 | -3.1114 | -53.7839 | 2026-10-08 18:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 107.7 |
| b02174a1-a882-378a-911d-ef2b49fa90d6 | -2.9707 | -57.7779 | 2026-10-08 18:20:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 60.9 |
| d7b5fa1d-b19b-3284-b440-e361275eb2c2 | -5.9835 | -40.9367 | 2026-10-08 18:20:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 247.6 |
| 4fdb7a02-ec03-3eae-a43c-21ad4ecd38c2 | -2.4942 | -58.0575 | 2026-10-08 18:20:00 | GOES-19 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 65.2 |
| 11d9769a-4ebd-3f45-ac77-123cf76c7aec | -3.2215 | -53.8616 | 2026-10-08 18:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 68.9 |
| b4fbe5d5-4161-3535-a109-f57c0d209959 | -12.2316 | -44.7427 | 2026-10-08 18:20:00 | GOES-19 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 150.6 |
| 437eb88a-4906-3c83-836c-b8ce590feb81 | -9.1072 | -67.8141 | 2026-10-08 18:20:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 115.4 |
| 742dd34c-f639-32c6-b3e1-8455a165070e | -1.7681 | -55.0309 | 2026-10-08 18:20:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 45.5 |
| 3b08205b-ddaa-3617-bb35-0d7d9a985be8 | -9.1072 | -67.8326 | 2026-10-08 18:20:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 147.1 |
| 2777a06c-3551-3dee-b02f-7246336477e2 | -2.9264 | -54.1505 | 2026-10-08 18:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 60.2 |
| caedc4b2-b9be-3675-b38a-19ea98aad256 | -6.5399 | -45.3868 | 2026-10-08 18:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 108.8 |
| 3c1e9035-9763-3d2a-bf12-5dbeb3e53133 | 1.7672 | -55.5463 | 2026-10-08 18:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 68.7 |
| ce079723-448e-3605-b93f-f365c701e546 | 2.0047 | -55.8786 | 2026-10-08 18:20:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 92.7 |
| 945f6986-0c3e-35fb-8179-8dc098491fb2 | -4.0837 | -44.1389 | 2026-10-08 18:20:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 211.5 |
| 9cdd3b06-d4c3-3f64-a152-ad344f567c7b | -5.9936 | -55.6815 | 2026-10-08 18:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 82.6 |
| ea5e4aa8-4e54-3801-ab29-bf131af12962 | -5.3763 | -45.943 | 2026-10-08 18:20:00 | GOES-19 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 80.2 |
| 2909f8ed-38f7-3e1a-9326-b26d1dfad1e7 | -12.0256 | -43.4371 | 2026-10-08 18:20:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 479.4 |
| 683cd467-e979-3945-b711-10049f749636 | -7.2185 | -55.1016 | 2026-10-08 18:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 141.7 |
| ef82f661-94eb-32aa-b70d-a7e8a40f3188 | -13.3671 | -43.8742 | 2026-10-08 18:20:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 149.8 |
| 5afb870a-34cd-31b0-9ea0-1b7d738cc1ed | -3.86 | -44.1274 | 2026-10-08 18:20:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 222.2 |
| 2553cbed-b8e7-31b3-8332-8a0e1903d878 | -9.479 | -67.4897 | 2026-10-08 18:20:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 105.5 |
| 756b3c63-7b98-3132-bae7-8f4baceac5ca | -6.1615 | -52.6676 | 2026-10-08 18:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 91.8 |
| 98b4409f-10f2-3ef6-84ab-11424ea1bc9f | -3.3141 | -49.1409 | 2026-10-08 18:20:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 52.8 |
| f29370e2-1ea3-31a8-aaba-24c6f5ec648a | -14.0873 | -43.7671 | 2026-10-08 18:20:00 | GOES-19 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 484.0 |
| 9167e5cf-8c1e-3ec8-99ae-a757d8369a87 | -6.4567 | -55.4809 | 2026-10-08 18:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 107.6 |
| 3c8359e2-90bd-3ac9-88ed-dfa683b35ecd | -6.3134 | -54.7884 | 2026-10-08 18:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 100.3 |
| 8dcec695-2de3-30b4-89f3-bd67205eb432 | -3.5234 | -44.3267 | 2026-10-08 18:20:00 | GOES-19 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 107.4 |
| 36751df8-edb0-3c08-ac0c-e14a420c9093 | -2.5721 | -56.1449 | 2026-10-08 18:20:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 65.2 |
| 740c592b-3d33-3807-817d-ecbe1cd353ef | -3.2451 | -57.8693 | 2026-10-08 18:20:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 104.4 |
| 82a93494-ae22-304d-9142-dda3274d2549 | -9.0705 | -67.7225 | 2026-10-08 18:20:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 95.7 |
| cd32cc75-79da-3389-bc51-49c1b50a044a | -6.5212 | -45.3883 | 2026-10-08 18:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 238.9 |
| c45de814-5276-3b84-ab45-4c7faa9669ae | -6.1431 | -47.9214 | 2026-10-08 18:20:00 | GOES-19 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 81.5 |
| 6bac6581-5a37-3174-8961-411160448526 | -8.0578 | -45.6131 | 2026-10-08 18:20:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 104.1 |
| 89ff8ed2-2c66-3617-a1b8-c651f21b7bca | -3.1116 | -53.7436 | 2026-10-08 18:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 69.7 |
| 825e7109-dec3-306f-8b4c-a1f8d02fd4dc | -12.0444 | -43.4578 | 2026-10-08 18:20:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 124.2 |
| 8660849c-bcf9-3f44-acf2-6fbef8ea2eb5 | -3.7239 | -57.1384 | 2026-10-08 18:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 54.7 |
| ce5788f6-f23a-3b92-964d-bbf5f4055495 | 3.7462 | -51.6224 | 2026-10-08 18:20:00 | GOES-19 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 54.7 |
| 4ef84157-5019-3c72-841d-170b09eadbf8 | -1.8233 | -54.9307 | 2026-10-08 18:20:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 62.4 |
| 7021fba4-2bd3-3afb-b581-e6db1952effa | -2.7797 | -54.0736 | 2026-10-08 18:20:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 63.5 |
| 2caeb107-0bc3-38d8-9c40-7713cc742bea | -13.9668 | -44.8507 | 2026-10-08 18:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 98.2 |
| c699b8ae-0794-3c8c-9f65-1297b3734b1b | -6.1746 | -53.4427 | 2026-10-08 18:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 69.0 |
| ed9218ce-142a-3013-bf84-34d01e395fad | -3.8004 | -41.6708 | 2026-10-08 18:20:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 153.7 |
| 27fbcc77-e1a0-3a47-a6cf-f1ff62d6b5ef | -5.9647 | -40.9383 | 2026-10-08 18:20:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 123.8 |
| b631ecd1-413a-384c-aa89-439bed78026a | -2.9633 | -54.1095 | 2026-10-08 18:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 68.3 |
| 4c5490ef-6e5e-3343-9333-2dffbbb1e910 | -2.9451 | -54.0698 | 2026-10-08 18:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 61.4 |
| c291450d-618a-3542-bb34-9ee42a1986ce | -3.8036 | -47.5057 | 2026-10-08 18:20:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 48.8 |
| b25ce36e-84e0-3453-a314-163755423328 | -3.1299 | -53.7633 | 2026-10-08 18:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 55.6 |
| c6297284-8f2f-3c74-8034-4b044f4647f8 | -3.0558 | -53.9263 | 2026-10-08 18:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 212.9 |
| a31234b1-3fe7-3436-a2eb-0ab957e6e9ac | -3.2085 | -57.87 | 2026-10-08 18:20:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 101.3 |
| 84056444-49d3-35eb-b84c-75aa3cb358bf | -3.0447 | -57.4851 | 2026-10-08 18:20:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 75.4 |
| 8483943c-23c1-3973-94e0-a04ef8fe4866 | -3.1697 | -58.6244 | 2026-10-08 18:20:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 127.5 |
| 3c6cfcc1-91d7-323b-95a0-a79d74ac7df0 | -6.4905 | -55.9563 | 2026-10-08 18:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 100.1 |
| 952a9f1e-79cb-3cbc-8123-dd50340615bd | -3.6045 | -54.6736 | 2026-10-08 18:20:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 132.1 |
| f75befa2-77b8-3acf-a749-9b3f82795b53 | -2.2297 | -53.7026 | 2026-10-08 18:20:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 59.7 |
| 9b8500fe-9df8-3048-aab0-8cdb4fe17acc | -2.5492 | -58.0373 | 2026-10-08 18:20:00 | GOES-19 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 117.9 |
| 1b32511c-76a3-3cae-8561-a98cbc257365 | -8.3532 | -47.6568 | 2026-10-08 18:20:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 88.0 |
| bcf479b2-c3e2-34a8-9ec3-bc09c8ed5cad | -1.2911 | -55.4133 | 2026-10-08 18:20:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 66.3 |
| 542204ab-4d3b-3858-821e-62b69e74fc88 | -5.9772 | -55.344 | 2026-10-08 18:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 81.9 |
| d96d2eda-4d5f-3ea8-ba2b-f42d05ac98c7 | -7.5354 | -42.088 | 2026-10-08 18:20:00 | GOES-19 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 92.8 |
| 6397ec36-fb24-39e5-96b3-4e500dc524f2 | -2.77 | -57.5293 | 2026-10-08 18:20:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 180.3 |
| b5735fe8-7d34-3e9f-9cb4-2663e37fef3d | -5.3718 | -44.1981 | 2026-10-08 18:20:00 | GOES-19 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 140.5 |
| c6b32ff5-1522-37a2-9244-4da0976a5f3b | -10.9953 | -45.4068 | 2026-10-08 18:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 116.5 |
| 7ef2d571-30c4-3d85-94d6-27a3c87a01de | -9.1294 | -45.8405 | 2026-10-08 18:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 102.6 |
| da4a0cbe-3478-3f7e-920c-ef2ae097a1e0 | -5.6934 | -53.4667 | 2026-10-08 18:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 321.6 |
| 95278443-ec4b-3eaf-a1e6-d2cd9b25e1b3 | -11.4507 | -43.3854 | 2026-10-08 18:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 157.4 |
| bb3632ad-4cc1-3cb7-b3df-9be02f72c540 | -3.1879 | -58.6433 | 2026-10-08 18:20:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 212.1 |
| d230e3d1-0897-3185-affb-a7a10d2cd87a | -3.2267 | -57.889 | 2026-10-08 18:20:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 71.6 |
| b4e883f5-8d17-301d-bee4-2c0dede8e226 | -11.6382 | -43.6166 | 2026-10-08 18:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 129.6 |
| 1ea11905-3cb0-3b01-96c8-0eef8123b0ca | -15.3419 | -42.7704 | 2026-10-08 18:20:00 | GOES-19 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Cerrado | 150.0 |
| 36570167-ab0f-3367-bdb0-415852afb01b | -2.4623 | -56.0682 | 2026-10-08 18:20:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 76.9 |


[Clique aqui para ver as próximas entradas](README391.md)
