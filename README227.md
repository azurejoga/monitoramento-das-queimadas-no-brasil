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

## Dados Diários - Página 227

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9611387f-72d6-331f-9892-b4ac206848df | -2.93343 | -53.92789 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| ba61e1e4-0b09-39e8-9cdf-f331ba7d494e | -2.48822 | -56.11328 | 2026-10-07 16:39:00 | NPP-375 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 63432a85-dc94-313d-971c-d95e12316705 | -0.79394 | -49.50999 | 2026-10-07 16:39:00 | NPP-375 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| f7d5c53f-9b3c-30a7-8c83-e2903d542a73 | -2.95114 | -57.20075 | 2026-10-07 16:39:00 | NPP-375 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 13.0 |
| b4e45fc0-a789-38d2-8a5b-11decc01e8d5 | -0.62062 | -56.81094 | 2026-10-07 16:39:00 | NPP-375 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 3af6c807-fd72-306d-823d-cafe9cd9c324 | -2.76268 | -54.10744 | 2026-10-07 16:39:00 | NPP-375 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 103.6 |
| 11d251ea-fba8-3b08-b3c3-ba3a74738107 | -2.41449 | -55.8683 | 2026-10-07 16:39:00 | NPP-375 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 4eccf2da-0b17-358f-92dd-c84308352b9f | -3.02751 | -57.48285 | 2026-10-07 16:39:00 | NPP-375 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 9.1 |
| b21e6603-281f-3c59-9903-907706133fac | -3.29292 | -54.04927 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 21.1 |
| 7a1367f5-9e1e-3464-8257-1caeb575c7c9 | -1.26684 | -55.71342 | 2026-10-07 16:39:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 402c6aa9-9db7-365c-8f23-35b43328f383 | -4.7725 | -55.72237 | 2026-10-07 16:39:00 | NPP-375 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 3a267733-9d99-3222-8650-47d192e258ed | -2.78019 | -54.07704 | 2026-10-07 16:39:00 | NPP-375 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 182.5 |
| d66308ea-e744-3579-b4fc-b17c7956137f | -1.3815 | -55.18932 | 2026-10-07 16:39:00 | NPP-375 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| bf6d0b49-8448-3f43-8724-2973965c1047 | -1.46793 | -54.77185 | 2026-10-07 16:39:00 | NPP-375 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| e524fadb-3b22-3117-be51-f741d2085905 | -3.29392 | -54.05614 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 1ee5c5e8-c9db-37d8-8b73-1bbc05a8e44e | -3.40263 | -58.00964 | 2026-10-07 16:39:00 | NPP-375 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 18.4 |
| 6006b843-813c-3c5a-b429-de01b5bff7b1 | 2.00653 | -55.85276 | 2026-10-07 16:39:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 13.8 |
| bc35dfd4-400d-3e3f-b562-7a4858a194d6 | -3.28799 | -54.05338 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| f555850e-1c66-3b40-a5f9-592c37a54448 | -4.54442 | -55.61327 | 2026-10-07 16:39:00 | NPP-375 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 103.5 |
| 27676710-f173-39fb-8482-32d06809ac9d | -3.18952 | -50.55722 | 2026-10-07 16:39:00 | NPP-375 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 16.8 |
| f1ffabf5-0a05-38be-9eb7-4fc1499e3f01 | -2.96699 | -56.62849 | 2026-10-07 16:39:00 | NPP-375 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 47772ef0-f436-3e02-be39-7530f2b9c9b1 | -2.69329 | -49.04529 | 2026-10-07 16:39:00 | NPP-375 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 33.3 |
| d888499a-418f-3698-a445-51d15b5a3e81 | -2.99229 | -42.83791 | 2026-10-07 16:39:00 | NPP-375 | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 13b6c1fd-f9c0-383e-91e4-24ae3b729eec | -3.43994 | -56.93705 | 2026-10-07 16:39:00 | NPP-375 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 34.2 |
| a46b6e60-a6f5-3c70-8604-a5ad2be4057e | -2.92857 | -53.93193 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 196449be-5635-3a64-bfd7-8b48b8d45909 | -3.04704 | -53.94019 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c6b77985-f975-33d7-a1f5-9bd71496f4c4 | 1.91238 | -55.69951 | 2026-10-07 16:39:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| bfef2695-1e1d-32e0-a0b7-b3f18e2a2c89 | -3.53416 | -54.63787 | 2026-10-07 16:39:00 | NPP-375 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| d7d4bb78-1a25-3689-b702-1c6fe6285222 | -2.49361 | -56.14468 | 2026-10-07 16:39:00 | NPP-375 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 18.1 |
| 79db57a0-76e1-36a5-b153-b281c176f6ff | -3.29927 | -53.86881 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 155.3 |
| 8502e99a-1dae-34ec-8aae-b972380814c2 | -2.52984 | -58.09763 | 2026-10-07 16:39:00 | NPP-375 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 8.1 |
| e67b4c6d-a1c6-3252-949c-4a3ac8d8d56b | -3.22861 | -53.889 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| e2f03a4f-904f-377c-852a-18a1cd0db3c5 | -3.54359 | -50.09621 | 2026-10-07 16:39:00 | NPP-375 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 16.0 |
| c4944aba-5c05-3bf0-ae06-c5954c6a08b3 | -1.29499 | -54.56228 | 2026-10-07 16:39:00 | NPP-375 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 6c90f1aa-8f0a-359c-9e6a-6826b14ec64a | -1.28382 | -55.85315 | 2026-10-07 16:39:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 29.3 |
| e7370d0a-ac3c-3ee9-a7a4-1847bd3ae2b9 | -3.04656 | -53.93685 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 2e51d801-9bf7-38e1-9651-e0543efbdab1 | 0.38225 | -51.14584 | 2026-10-07 16:39:00 | NPP-375 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b3753f8b-fd45-39fb-adab-926c83dca572 | -3.01868 | -54.1328 | 2026-10-07 16:39:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| a87282dc-dfc9-345b-b990-b394f56252ae | -3.8401 | -55.97041 | 2026-10-07 16:39:00 | NPP-375 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 54.3 |
| 7aaa2478-98b7-3548-b4db-872d52e4ace1 | -1.71706 | -55.44029 | 2026-10-07 16:39:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 410a1295-949f-30bd-8830-fab861af6848 | 2.19146 | -50.97981 | 2026-10-07 16:39:00 | NPP-375 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 455bf87b-5f7c-3772-8ac9-dd42fd7ec0e0 | -1.59407 | -45.43672 | 2026-10-07 16:39:00 | NPP-375 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 4c814b1e-ac64-3eb1-aea1-18181d563d44 | -3.66839 | -54.50761 | 2026-10-07 16:39:00 | NPP-375 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 626cbd4b-65f4-37c4-929d-3909fe576c4e | -3.78736 | -50.75414 | 2026-10-07 16:39:00 | NPP-375 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 24.2 |
| 9aaecafc-b6d9-3e50-b1cc-dd5cb6e8613e | 2.28642 | -55.85413 | 2026-10-07 16:39:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 2bb232c4-23fa-382c-82ab-c826600556c9 | -2.99899 | -54.038 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 75526b23-de56-3ecf-9071-80b65b64fcd3 | -2.99056 | -54.1299 | 2026-10-07 16:39:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 19.3 |
| e9b02d73-ac86-3cc2-8da8-b28e1c387d9d | -4.10714 | -52.0649 | 2026-10-07 16:39:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 08db01d0-22ea-39ec-a412-c6d64db223b2 | -2.11956 | -54.69627 | 2026-10-07 16:39:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 309a3a9f-64ab-3302-a582-6c32099e0150 | -2.9471 | -54.05938 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 18.4 |
| 75b97dfb-7703-3047-b12a-60ac3bc41009 | -3.70393 | -50.65173 | 2026-10-07 16:39:00 | NPP-375 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| da061307-25fd-3cdc-b3a9-616562e91d65 | -3.10117 | -54.15903 | 2026-10-07 16:39:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 4d99767a-3527-395c-8dde-e629270e1820 | -2.93784 | -54.14806 | 2026-10-07 16:39:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 20.7 |
| c0278d63-7cd8-38f4-91dd-1adb53be8be6 | -3.29334 | -54.01442 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| dff0bb2a-f949-34ea-a2b8-6cf2a7f43e76 | -3.94891 | -57.07481 | 2026-10-07 16:39:00 | NPP-375 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 17b33b43-8217-3fdd-adcf-75ab93bce635 | -3.45563 | -53.03944 | 2026-10-07 16:39:00 | NPP-375 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 96d9c896-a08e-3253-a454-b32793f71b7a | -3.04351 | -54.2615 | 2026-10-07 16:39:00 | NPP-375 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 49.7 |
| 4123a7fc-b083-3226-85a0-f8b401a10191 | -1.41045 | -55.41323 | 2026-10-07 16:39:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 31faeec2-c142-3c63-aad5-28b96876c4a2 | -3.0484 | -54.1461 | 2026-10-07 16:39:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| a808ad7c-602d-3a6e-9aa8-470216149980 | -3.04906 | -53.87941 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 74630d95-b423-3142-9ff6-2b6fc1367aeb | -2.78557 | -54.07629 | 2026-10-07 16:39:00 | NPP-375 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 234.7 |
| 99897b49-6867-355a-98b4-a20a2a0e50b5 | 3.22243 | -51.31138 | 2026-10-07 16:39:00 | NPP-375 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 15.8 |
| 65be3a14-6f63-3fe5-ab78-4968741ad9b7 | -1.13025 | -53.1116 | 2026-10-07 16:39:00 | NPP-375 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 05222a0b-f91e-34de-81cf-f214304b32e7 | -1.88244 | -53.97295 | 2026-10-07 16:39:00 | NPP-375 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 16.5 |
| 451b453a-fdec-3ca5-a5f5-ebdeaded37ba | -3.27867 | -54.06538 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| f11c38bf-0715-3cb6-9582-2f3a4090749b | -3.70898 | -51.13733 | 2026-10-07 16:39:00 | NPP-375 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 9158dad4-00c7-3b9a-98c7-7e4280887f04 | -3.03721 | -51.55341 | 2026-10-07 16:39:00 | NPP-375 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| ebc4a8d3-d934-3b06-820b-a2fe177f4983 | -2.93735 | -54.12087 | 2026-10-07 16:39:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 579841a1-8dea-3773-bdc1-0c614b1e627b | 2.06222 | -50.87304 | 2026-10-07 16:39:00 | NPP-375 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 6.2 |
| d3708d71-c89a-3fc7-86a0-e90137c889d9 | -3.93162 | -54.57597 | 2026-10-07 16:39:00 | NPP-375 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 6c929f58-f57c-3ec6-bc9e-e80cc78fd5f7 | -4.10236 | -52.06561 | 2026-10-07 16:39:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| c57d643e-8db6-32c6-ada3-92c950ae6d93 | 3.21029 | -51.30947 | 2026-10-07 16:39:00 | NPP-375 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 5a2df0c4-a70c-353d-a13c-9d7842b6c4d8 | -3.47252 | -50.0843 | 2026-10-07 16:39:00 | NPP-375 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| f6096808-fe04-39f2-aed1-6923191ce9fb | -1.71066 | -55.43726 | 2026-10-07 16:39:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 300e53a9-f9c3-3fcf-9e07-04d1873d754e | -2.10478 | -52.05684 | 2026-10-07 16:39:00 | NPP-375 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 20b14aee-670a-3a83-a96f-bbf8ac88f3ca | -3.47057 | -50.0996 | 2026-10-07 16:39:00 | NPP-375 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 45042aec-bd24-3a39-b865-7da24e16bdf5 | -3.683 | -55.95676 | 2026-10-07 16:39:00 | NPP-375 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| b91b62b8-0abf-30f8-a00a-77ec45e723dc | -2.06172 | -45.97795 | 2026-10-07 16:39:00 | NPP-375 | MARACAÇUMÉ | MARANHÃO | Brasil | 2106326 | 21 | 33 | nan | nan | nan | Amazônia | 7.1 |
| a69a5f7f-cab2-3ad5-ab1a-f70fdd2bcc13 | -2.49625 | -56.12087 | 2026-10-07 16:39:00 | NPP-375 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 1974d684-d849-330a-b0f6-c2c87f5ffeb2 | -3.28301 | -54.01928 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| b2937e2e-1fa4-3ce0-b6c5-d616fcc1a620 | -3.18354 | -50.54605 | 2026-10-07 16:39:00 | NPP-375 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 16.1 |
| dcee94c1-e4c8-3368-b49b-1115c3918380 | -4.14511 | -54.90575 | 2026-10-07 16:39:00 | NPP-375 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 79f69584-b152-30b7-afce-9c9ea7bde937 | -2.50448 | -56.13373 | 2026-10-07 16:39:00 | NPP-375 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 18.6 |
| 7b704b6d-083b-32f9-ac06-e0c987b1b035 | 0.94357 | -50.19727 | 2026-10-07 16:39:00 | NPP-375 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 15.7 |
| dd6ad126-1aa5-3030-9a94-2ccdc55f41dc | -2.89324 | -54.15882 | 2026-10-07 16:39:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| ecc70c49-07fe-32fd-b9d0-72f71c0e51a3 | -3.50637 | -58.5495 | 2026-10-07 16:39:00 | NPP-375 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 61cdfa5b-afcc-3039-8b6e-87cdcd4c8690 | -3.10044 | -53.75099 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 42106d6d-b36e-39b8-9cf3-798f5e6e489b | -4.12602 | -50.83509 | 2026-10-07 16:39:00 | NPP-375 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8ea6271c-34e8-3a60-b5df-d6556df71b3e | -3.47796 | -54.62365 | 2026-10-07 16:39:00 | NPP-375 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 624f0feb-5911-3b4f-9fac-da538c8b7ae5 | -1.29685 | -55.71359 | 2026-10-07 16:39:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 75bb4956-8400-3f4d-b4e4-08d8cf61ca7b | -1.80606 | -57.10996 | 2026-10-07 16:39:00 | NPP-375 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 69.8 |
| a7051805-fe12-365d-9f34-54981433d2e8 | -3.72758 | -55.49161 | 2026-10-07 16:39:00 | NPP-375 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 129.3 |
| 7b4473f5-883b-3817-850d-5abb444d5d07 | 2.17966 | -55.92558 | 2026-10-07 16:39:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 1e379f55-1fe1-3add-a95a-891272c601b1 | -3.10808 | -54.16822 | 2026-10-07 16:39:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 77.3 |
| f23fc045-79ee-3c1a-a6f5-115105c5bf9c | -3.10288 | -54.97221 | 2026-10-07 16:39:00 | NPP-375 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 411fe6b4-99bd-327e-a9e5-a40e652510e9 | -3.5347 | -54.64169 | 2026-10-07 16:39:00 | NPP-375 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 00d448ee-775e-3d13-b7de-0f3cdcc7616c | -0.59934 | -52.06102 | 2026-10-07 16:39:00 | NPP-375 | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0084f94e-4343-3c07-915d-674575a9b703 | -3.5179 | -54.66002 | 2026-10-07 16:39:00 | NPP-375 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| eb6fa6e8-e91d-3ce5-bf83-54cb79034854 | -3.22328 | -53.88985 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 5948d9d2-cc0b-389e-a01b-fbecbea9c707 | 1.73883 | -56.07924 | 2026-10-07 16:39:00 | NPP-375 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 15.1 |


[Clique aqui para ver as próximas entradas](README228.md)
