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

## Dados Diários - Página 391

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0f3324a1-f421-3148-a41e-9c66cfa03f0d | -11.1354 | -46.1623 | 2026-10-08 18:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 216.7 |
| 7e642dcf-3535-3892-9100-1fdd7ef7f9b2 | -7.0281 | -45.3008 | 2026-10-08 18:20:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 87.2 |
| 716e7d1a-1c0f-3c3d-aa54-a429d659d108 | -1.3264 | -56.4176 | 2026-10-08 18:20:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 74.4 |
| c0e8faef-fa69-3245-9ee4-bb8e983f6edc | -4.1023 | -44.1379 | 2026-10-08 18:20:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 113.9 |
| 9f89e137-80d2-3485-93dd-1ea49a1d85aa | -7.2187 | -55.0815 | 2026-10-08 18:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 99.3 |
| f13b0cd1-8586-3315-a913-533c4e1fbe73 | -3.0008 | -53.8874 | 2026-10-08 18:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 109.5 |
| 2e86042e-7ffa-3b9e-b848-56d86746a72a | -3.0375 | -53.9066 | 2026-10-08 18:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 74.7 |
| 8f5a2d5b-4e37-3a93-b1ff-f6293948dbec | 1.7121 | -55.6063 | 2026-10-08 18:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 69.7 |
| eff07696-e445-3517-b3fe-62d2c3d097e2 | -9.3395 | -65.4451 | 2026-10-08 18:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 111.8 |
| 3af73778-75a9-3362-ad6b-3e2dd67c941b | -10.7673 | -46.571 | 2026-10-08 18:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 150.8 |
| 23536f03-a2c7-3b0b-aef2-49ea30f107d5 | -6.4568 | -55.4609 | 2026-10-08 18:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 95.3 |
| e5d4784b-96df-3a76-8c23-9c0829141b28 | -3.7809 | -41.7913 | 2026-10-08 18:20:00 | GOES-19 | SÃO JOSÉ DO DIVINO | PIAUÍ | Brasil | 2210052 | 22 | 33 | nan | nan | nan | Caatinga | 346.8 |
| 39320893-d334-3749-b0cb-7e4a8cba499b | -2.4766 | -57.7867 | 2026-10-08 18:20:00 | GOES-19 | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 69.3 |
| 3874c8f4-9e81-38d8-a873-91cf17ab28a7 | -12.1549 | -44.7314 | 2026-10-08 18:20:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 178.3 |
| 9d8136f0-46ae-3486-967a-b97d69e0f149 | -6.3133 | -54.8084 | 2026-10-08 18:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 84.9 |
| 77f2fe0e-a825-3284-9c8d-cf196c068da5 | -8.948 | -65.9429 | 2026-10-08 18:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 476.1 |
| db3e1941-0c44-3a99-b579-3c4f3ac7de8f | -5.8801 | -45.9537 | 2026-10-08 18:20:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 72.8 |
| 8573db68-228e-3783-94f5-0c83c9d1514a | -5.9587 | -55.3448 | 2026-10-08 18:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 111.9 |
| 8f21cd82-ddf2-377d-999b-a296ef7c8b89 | -7.184 | -46.5225 | 2026-10-08 18:20:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 74.8 |
| 7abdb548-e846-340d-b1d4-43b9b4a4111a | -8.5313 | -46.911 | 2026-10-08 18:20:00 | GOES-19 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 104.3 |
| 9327a10d-02b8-32be-a4d7-b008be751bb3 | -3.1484 | -53.7225 | 2026-10-08 18:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 62.3 |
| 5026dd49-0844-320b-8480-e9c1ca3c6545 | -2.9451 | -54.0497 | 2026-10-08 18:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 70.6 |
| 0d0ce8d5-dad9-3ec0-8c11-6523298763ef | -5.4806 | -44.6029 | 2026-10-08 18:20:00 | GOES-19 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 84.7 |
| 0e2e1e29-36dd-3d52-a691-b4e03452cf62 | -12.7678 | -44.8671 | 2026-10-08 18:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 99.2 |
| 13ae30e6-71b0-389a-ba43-43bcb662056f | -6.1617 | -52.6471 | 2026-10-08 18:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 104.5 |
| c4b3d51f-ff45-3531-9fd9-f78e3287afb7 | -3.2031 | -53.8621 | 2026-10-08 18:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 68.9 |
| 67eec0d2-f719-3464-afc8-20b9f6f964f9 | -12.62 | -44.5414 | 2026-10-08 18:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 101.6 |
| 441fb58a-8748-318c-bb9f-7aeb73068f7e | -2.4623 | -56.0879 | 2026-10-08 18:20:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 116.2 |
| 41b90da0-fef0-35b3-bbc0-edfa1f64dfa6 | -1.5306 | -54.5359 | 2026-10-08 18:20:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 139.0 |
| 03d14cca-665b-3584-bd8b-a094af12ffd2 | -6.6899 | -45.3746 | 2026-10-08 18:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 134.3 |
| aa8b39a5-80c4-3366-897d-741782a5e371 | -7.4694 | -42.8551 | 2026-10-08 18:20:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 112.8 |
| e1aa7e94-3ae6-3230-aac0-3cf15d1c9a88 | -3.4277 | -58.0397 | 2026-10-08 18:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 67.2 |
| 6fb9a5e8-b672-393d-acb0-21d6ed065653 | -9.9801 | -45.9009 | 2026-10-08 18:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 93.1 |
| e4d164c6-387c-364a-bc89-02d789f25261 | -14.0868 | -43.791 | 2026-10-08 18:20:00 | GOES-19 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 240.8 |
| 0b5892ea-40c2-3a32-94aa-5fd29fb6cbc3 | -3.2268 | -57.8696 | 2026-10-08 18:20:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 73.5 |
| 1b451e90-1c2a-3fc7-9dd4-67e414dec7b4 | -9.8015 | -47.8186 | 2026-10-08 18:20:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 93.1 |
| 6a5b66ac-8676-3278-b8f6-7133c2e8028e | -2.8434 | -57.4696 | 2026-10-08 18:20:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 122.7 |
| d958c7f7-3e52-3089-87f3-341e0aa90b44 | -7.4697 | -42.8315 | 2026-10-08 18:20:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 129.5 |
| fbf6f8df-9d61-35ce-b8a6-d1335594293f | -2.9449 | -54.1099 | 2026-10-08 18:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 86.7 |
| 339fbbf6-3df8-3c6a-92ba-fe8f6caf0b72 | -2.9271 | -53.9295 | 2026-10-08 18:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 66.7 |
| aa03df10-763f-3b56-92af-901da31d9e82 | -3.7238 | -57.1579 | 2026-10-08 18:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 45.1 |
| dca6a185-562e-31bd-8800-33e7b6ed5339 | -7.2371 | -55.1005 | 2026-10-08 18:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 125.6 |
| 6e8d3195-2bed-3af6-9141-c67bfe7cfce0 | -2.572 | -56.1646 | 2026-10-08 18:20:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 249.0 |
| 119f8d99-efa9-3553-bfde-457eba828537 | -11.7738 | -43.5482 | 2026-10-08 18:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 177.6 |
| d7fd1c5c-c4cd-3f73-b36a-991a4e551efd | -5.5146 | -42.8399 | 2026-10-08 18:20:00 | GOES-19 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 188.4 |
| c18a74d1-975d-317b-816a-1f26b3f20928 | -2.0576 | -56.8786 | 2026-10-08 18:20:00 | GOES-19 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 77.3 |
| f4e4ae21-09ba-3ae0-8649-e5e801812cc4 | -6.1496 | -51.7614 | 2026-10-08 18:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 65.1 |
| c4b0612d-e5d8-36a8-9533-d42176b21a2c | -6.1484 | -51.927 | 2026-10-08 18:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 139.8 |
| f0a859ca-35af-385f-93c7-d2c04ee1603b | -5.5148 | -42.8164 | 2026-10-08 18:20:00 | GOES-19 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 83.7 |
| 5b8fac36-7a47-322a-a0fe-2b3318534796 | -2.9819 | -54.0488 | 2026-10-08 18:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 133.3 |
| 1042a8b7-6cf1-3191-b65c-b8a43efbd740 | -1.801 | -57.1161 | 2026-10-08 18:20:00 | GOES-19 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 69.7 |
| ccd7bc90-947a-3d11-9667-d1c8cc69ba83 | -12.1554 | -44.708 | 2026-10-08 18:20:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 132.9 |
| 05fbb4da-5c82-3e0b-b142-f54812917b5a | -3.3319 | -59.5043 | 2026-10-08 18:20:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 85.1 |
| 941e4d5c-aaea-3af8-85d3-7cb4bb752dea | -2.8228 | -58.361 | 2026-10-08 18:20:00 | GOES-19 | SILVES | AMAZONAS | Brasil | 1304005 | 13 | 33 | nan | nan | nan | Amazônia | 67.7 |
| 401b8787-5881-3a46-a9a5-2a28e12942c2 | -2.9632 | -54.1296 | 2026-10-08 18:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 56.0 |
| 6f0a3e61-677e-377b-8575-bcad3654cd24 | -4.576 | -40.657 | 2026-10-08 18:20:00 | GOES-19 | IPUEIRAS | CEARÁ | Brasil | 2305902 | 23 | 33 | nan | nan | nan | Caatinga | 125.1 |
| 7b0db9a1-20b5-3038-adf5-f5d8e252103f | -3.5182 | -41.9242 | 2026-10-08 18:20:00 | GOES-19 | CAXINGÓ | PIAUÍ | Brasil | 2202653 | 22 | 33 | nan | nan | nan | Caatinga | 87.4 |
| ed886897-83a4-3256-ba2a-e892a13b2c3b | -11.7674 | -44.9522 | 2026-10-08 18:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 77.7 |
| ba91bd99-0ba7-3e21-8f4c-230c0857be3a | -9.9398 | -43.5542 | 2026-10-08 18:20:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 99.3 |
| e4c44e6f-69cd-393a-844e-bcd03860ec2c | -3.2957 | -49.1202 | 2026-10-08 18:20:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 82.8 |
| a02f350a-b12e-3c44-aca8-4ec797ec2831 | -3.7817 | -41.6718 | 2026-10-08 18:20:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 111.1 |
| b4461204-1f3c-3340-9ad1-23f5bf2c5596 | -11.1358 | -46.1396 | 2026-10-08 18:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 105.1 |
| 3be569c8-4e4d-32c9-a6fb-f5bcd1a794a3 | -4.084 | -44.0929 | 2026-10-08 18:20:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 123.0 |
| d3391b2d-b006-3346-baa3-16c4ef2d8bb5 | -2.4942 | -58.0768 | 2026-10-08 18:20:00 | GOES-19 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 125.1 |
| a6af06f8-b559-3568-bfde-27187c78a1a7 | -3.1506 | -58.9134 | 2026-10-08 18:20:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 64.3 |
| d611fb1c-fe57-3d0e-97b6-d19a2d22c2a0 | -4.1025 | -44.1149 | 2026-10-08 18:20:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 143.0 |
| 0efc4f5b-cd2d-365d-b207-fac1abd47e9b | -11.6387 | -43.5929 | 2026-10-08 18:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 259.4 |
| eb05fd18-e697-3a64-9dce-0bad51b478cf | -14.0667 | -43.8185 | 2026-10-08 18:20:00 | GOES-19 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 151.4 |
| 8b57303b-5699-3255-b65d-0fe824600edf | -6.1501 | -51.6992 | 2026-10-08 18:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 77.6 |
| 83e58a04-8a51-3b80-afce-809e046acef1 | -8.0769 | -45.5886 | 2026-10-08 18:20:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 67.8 |
| d01c745f-f59d-396f-9252-7db9ec7ff6af | -3.2634 | -57.8689 | 2026-10-08 18:20:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 153.7 |
| 074f7426-f743-3b13-8bea-2ea48d20149b | -3.0925 | -53.9455 | 2026-10-08 18:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 455.5 |
| c2514709-fe08-3bef-bd25-e02b92bd290b | -6.6027 | -37.8944 | 2026-10-08 18:20:00 | GOES-19 | LAGOA | PARAÍBA | Brasil | 2508109 | 25 | 33 | nan | nan | nan | Caatinga | 137.4 |
| c3b9b849-e07c-399d-a42c-3db68f31dff3 | -11.755 | -43.5275 | 2026-10-08 18:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 129.5 |
| 11395ca2-2d22-390b-92ff-0eba6cfd5423 | -2.3115 | -57.9829 | 2026-10-08 18:20:00 | GOES-19 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 69.2 |
| f597b447-d42d-35f0-b381-acbeabfb05b3 | -11.7935 | -43.5215 | 2026-10-08 18:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 130.4 |
| b3cdbfd5-d3a4-3e1c-b81a-6a78a4bdb114 | -2.9819 | -54.0287 | 2026-10-08 18:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 71.4 |
| 8743b700-612f-3981-b9ef-c1ac51f452f0 | -6.1974 | -52.8295 | 2026-10-08 18:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 79.6 |
| 1dfe3ae9-25d6-352b-a188-ae2e3ee3560f | -6.4031 | -55.2042 | 2026-10-08 18:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 83.1 |
| 7f8968e9-815b-3a5e-a319-a46d04cbe839 | -6.0074 | -53.5325 | 2026-10-08 18:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 82.5 |
| a7b745ac-c26c-3f9c-b8f5-db44712ee845 | -9.0584 | -66.1073 | 2026-10-08 18:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 108.5 |
| bf78ccae-1e26-3f8a-b2ef-b90f963a49e2 | -6.6711 | -45.3761 | 2026-10-08 18:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 395.4 |
| 586a23c2-ad7f-3491-ad7e-7ea4f5cb8927 | -3.0559 | -53.9062 | 2026-10-08 18:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 95.3 |
| 7501fa5d-db03-30fd-a448-74a056146012 | -11.47 | -43.3824 | 2026-10-08 18:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 124.8 |
| c854341c-2f83-3fb2-9989-8dcc96e2fa2e | -3.7057 | -57.0998 | 2026-10-08 18:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 80.4 |
| eb2939bd-4471-37b1-83a9-ae44de3bf10c | -1.3264 | -56.398 | 2026-10-08 18:20:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 86.9 |
| ef17b2c7-d049-3d84-99de-de1a52487076 | -5.9649 | -40.914 | 2026-10-08 18:20:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 123.8 |
| 7ae46262-6971-31ea-ad2d-7aa3fcf0cc12 | -6.2159 | -52.8285 | 2026-10-08 18:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 76.7 |
| 155af556-57bb-3855-b127-a3e42cac6000 | -7.1813 | -55.1237 | 2026-10-08 18:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 105.3 |
| 2d97567a-e2f5-34b0-ae42-1bb8db378fc5 | -12.0448 | -43.434 | 2026-10-08 18:20:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 137.9 |
| 174046cd-31ff-3976-a863-c8f00c9bdfbe | -11.8503 | -43.5598 | 2026-10-08 18:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 182.3 |
| 355845a4-8be7-3c01-ba60-4bddb6794455 | -5.3034 | -45.7237 | 2026-10-08 18:20:00 | GOES-19 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 55.7 |
| 2cf0b2df-2e97-317d-99eb-3d3553de06ff | -7.1825 | -52.6283 | 2026-10-08 18:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 144.1 |
| 8ff3bfe0-e7a4-3787-a58f-dd1a841748fc | -5.6932 | -53.487 | 2026-10-08 18:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 232.1 |
| 21bab4d8-620f-3721-82dc-fd41f678f219 | -6.8907 | -45.8988 | 2026-10-08 18:20:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 102.3 |
| 6c1aae29-f304-3151-b934-1d12ab3bafaf | -3.724 | -57.1189 | 2026-10-08 18:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 65.7 |
| 287e83f3-2255-386b-9345-768e2522b4e5 | -5.3953 | -45.897 | 2026-10-08 18:20:00 | GOES-19 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 73.6 |
| b7129cdf-e81f-33f1-b8cf-96bd9cc41bfc | -3.1109 | -53.945 | 2026-10-08 18:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 218.9 |
| 4318be33-993d-394c-a582-f52ad0d6a456 | -6.5129 | -55.3784 | 2026-10-08 18:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 100.3 |
| ac4bbc40-014a-369b-8253-a1bed74b6f79 | -4.7404 | -55.6522 | 2026-10-08 18:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 159.5 |


[Clique aqui para ver as próximas entradas](README392.md)
