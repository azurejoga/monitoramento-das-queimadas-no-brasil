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

## Dados Diários - Página 387

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2d50bc7a-0f1f-39f8-9ce7-a2a62e5ceb1c | -11.2849 | -45.2063 | 2026-10-08 18:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 237.1 |
| 872b70d1-8f38-395f-97e6-aab42519a253 | -9.1294 | -45.8405 | 2026-10-08 18:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 127.8 |
| 3bfe9e40-d841-3a94-9439-ae22479d61f5 | 1.6937 | -55.6263 | 2026-10-08 18:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 79.7 |
| e3c9b78b-bbd7-32be-8a30-c4e248c111bf | -9.0585 | -66.0887 | 2026-10-08 18:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 85.1 |
| 319eef8e-0e9a-3ba7-a548-fb6139938855 | -11.4503 | -43.4091 | 2026-10-08 18:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 137.4 |
| f58888fb-bfc1-3b54-abcc-5ba22cec016a | -11.8503 | -43.5598 | 2026-10-08 18:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 382.9 |
| d79c9360-879d-3e40-898a-00b8c1e7087d | -3.0447 | -57.4851 | 2026-10-08 18:00:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 84.3 |
| 92998249-0e04-39b4-8247-996ead698f26 | -2.3115 | -57.9829 | 2026-10-08 18:00:00 | GOES-19 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 79.4 |
| cdc6d177-60ad-35c4-b3c5-08a5d9090227 | -5.9586 | -55.3648 | 2026-10-08 18:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 126.5 |
| 164ae84e-88a4-3d76-88cd-617fa53c4df9 | -11.6374 | -43.664 | 2026-10-08 18:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 99.5 |
| 19500365-ad67-3733-9d93-ca236966734c | 1.7672 | -55.5463 | 2026-10-08 18:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 65.3 |
| 120a913e-b506-3f20-8287-e1aaaff61039 | -7.3054 | -43.9931 | 2026-10-08 18:00:00 | GOES-19 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 88.3 |
| 0f2df9fd-0adb-3182-a83d-f41553d1e69a | -3.2817 | -57.8685 | 2026-10-08 18:00:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 66.2 |
| 03a3f0c8-8c82-3bbc-88a9-3dfa69a30dbb | -12.2123 | -44.7457 | 2026-10-08 18:00:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 105.8 |
| 0c3d753d-55bb-31fd-9795-1cedea8e5d39 | -9.9011 | -44.8378 | 2026-10-08 18:00:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 599.5 |
| 3375d65d-a127-3a99-a2b2-8ab831691b88 | -11.6391 | -43.5692 | 2026-10-08 18:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 125.0 |
| 51d1d7d4-884d-3bfb-943a-1ac0a2d485ad | -3.4095 | -58.0013 | 2026-10-08 18:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 89.2 |
| 694e3c3b-153d-33df-b48d-792ffa80acd5 | -12.0256 | -43.4371 | 2026-10-08 18:00:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 745.9 |
| 253bfafd-f8a9-3195-8790-a23a4eba063f | -9.9007 | -44.8608 | 2026-10-08 18:00:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 819.8 |
| e4d525fe-9869-3cd4-8632-89dc598d4a85 | -2.8228 | -58.361 | 2026-10-08 18:00:00 | GOES-19 | SILVES | AMAZONAS | Brasil | 1304005 | 13 | 33 | nan | nan | nan | Amazônia | 85.8 |
| a897c3c9-b85d-3371-8079-ff7ef3c2e65f | -11.1358 | -46.1396 | 2026-10-08 18:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 127.7 |
| ca32964b-34c2-320f-938f-83b9b12c8cf4 | -2.9634 | -54.0693 | 2026-10-08 18:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 62.8 |
| 8efbfa83-1de1-38d9-9863-0de3bde42053 | -3.8383 | -55.9774 | 2026-10-08 18:10:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 71.9 |
| 2c75b894-2da1-3aef-a7eb-8460f435b446 | 1.7488 | -55.5861 | 2026-10-08 18:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 60.8 |
| 171fd9bd-b484-353c-a7f9-bac7b44564b4 | -5.2853 | -48.1053 | 2026-10-08 18:10:00 | GOES-19 | BURITI DO TOCANTINS | TOCANTINS | Brasil | 1703800 | 17 | 33 | nan | nan | nan | Cerrado | 72.1 |
| 0c711bfa-6d20-3f50-8a97-9ff6684ee56b | -11.4507 | -43.3854 | 2026-10-08 18:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 244.1 |
| d222a08a-26cd-3bd7-8b2c-61dc78870857 | -8.948 | -65.9429 | 2026-10-08 18:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 450.9 |
| eeeff372-e5da-35f5-8d7f-8fd1bb98ab8e | -2.853 | -54.1322 | 2026-10-08 18:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 102.4 |
| 261c1d49-539a-39ca-87d9-5f99ff28e835 | -14.4345 | -43.9157 | 2026-10-08 18:10:00 | GOES-19 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 139.5 |
| 184e371d-8746-3816-b7b9-edca8a421c6e | -6.6039 | -53.0116 | 2026-10-08 18:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 54.2 |
| 06719feb-5b0f-328e-83a3-af1717642d53 | -13.395 | -43.4652 | 2026-10-08 18:10:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 120.9 |
| cf275553-da36-3a6a-a987-57e8e1e28b06 | -9.9398 | -43.5542 | 2026-10-08 18:10:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 168.9 |
| 06123781-abbe-36cc-bb72-a74e9d3cbc9c | -9.9014 | -44.8147 | 2026-10-08 18:10:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 150.0 |
| b7042b94-d1d1-3f68-bb5d-47d337dd7e44 | 1.6938 | -55.6066 | 2026-10-08 18:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 74.4 |
| 990518a1-2015-3bbd-b85b-efd63dc9c128 | -2.8228 | -58.361 | 2026-10-08 18:10:00 | GOES-19 | SILVES | AMAZONAS | Brasil | 1304005 | 13 | 33 | nan | nan | nan | Amazônia | 76.5 |
| a4bfe893-8c33-3fca-9748-66788fb4262a | -4.0838 | -44.1159 | 2026-10-08 18:10:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 508.1 |
| 707835ca-6a5d-3ed6-a32d-b097aaa4ed71 | -3.1697 | -58.6244 | 2026-10-08 18:10:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 145.1 |
| c2cfbecd-e049-32a0-95d7-b04a26bcf0f9 | -3.7057 | -57.0998 | 2026-10-08 18:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 74.5 |
| 8da84907-92e5-3e78-897b-9d1750aeaff8 | -2.9449 | -54.1099 | 2026-10-08 18:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 86.7 |
| 5dc077e7-6b56-34e1-956a-e55b4a6b575e | -4.7404 | -55.6522 | 2026-10-08 18:10:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 111.6 |
| f23e9e3a-8fcf-3c05-a920-0b01539368f3 | 3.7462 | -51.6224 | 2026-10-08 18:10:00 | GOES-19 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 73.1 |
| 6a991c80-dac7-3e19-a9ee-ec1e2327a7b0 | -3.2585 | -59.6013 | 2026-10-08 18:10:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 55.8 |
| c50c75c0-4976-33b9-8a6a-1fe07f4c0043 | -6.895 | -43.7066 | 2026-10-08 18:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 163.6 |
| 47b82566-0cc5-38e3-ad21-d603f391bd4c | -2.9271 | -53.9295 | 2026-10-08 18:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 67.5 |
| 000ccfdb-96ef-3e37-aa1c-e0db7043a478 | -9.9011 | -44.8378 | 2026-10-08 18:10:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 344.4 |
| 3d65c571-3fd8-3c01-be52-846b507d7ded | -3.13 | -53.7229 | 2026-10-08 18:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 71.5 |
| 6287398e-8797-39d1-a837-121fd3113b0a | -9.0585 | -66.0887 | 2026-10-08 18:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 87.2 |
| f99bb4ea-4212-3574-aec9-284e460319ca | -3.1116 | -53.7436 | 2026-10-08 18:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 76.9 |
| f8a5449e-eb72-3f6a-a42b-1b5deee85fa9 | -3.1879 | -58.6433 | 2026-10-08 18:10:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 285.4 |
| c9239cca-f112-316b-abc9-3b3f14ac02bd | -13.1833 | -54.3158 | 2026-10-08 18:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 404.2 |
| 47f337ac-ed6f-3da0-a5f1-56640474f3f0 | -7.0706 | -52.6764 | 2026-10-08 18:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 107.4 |
| 8409886a-ea65-3601-bc10-d49613bb362c | -7.6071 | -42.3905 | 2026-10-08 18:10:00 | GOES-19 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 97.2 |
| 167ca5c8-9320-3b24-a602-4124eafcc0ea | -2.4806 | -56.0678 | 2026-10-08 18:10:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 81.0 |
| f6571602-7448-3ec3-9e6a-becf91885f4d | -5.5146 | -42.8399 | 2026-10-08 18:10:00 | GOES-19 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 207.6 |
| 43474a93-874d-381e-aa59-400ab0f2b67e | 2.023 | -55.8784 | 2026-10-08 18:10:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 102.8 |
| 75f213f6-9b39-3a53-99fb-b0fb640e2a50 | -11.6562 | -43.6846 | 2026-10-08 18:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 145.3 |
| 482a847e-e9ca-3cf4-9d64-91168b9ba748 | -12.834 | -44.4362 | 2026-10-08 18:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 119.1 |
| 78cb62d8-a012-3ffa-b860-351b7448bc08 | -2.9795 | -54.7696 | 2026-10-08 18:10:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 52.4 |
| 704dc8e9-6e70-330c-900f-897a147910b8 | -9.3395 | -65.4451 | 2026-10-08 18:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 87.3 |
| 7dd870a5-13d3-3d33-90e9-b51997434421 | -5.9838 | -40.9123 | 2026-10-08 18:10:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 81.9 |
| 46310a1f-2738-3d5c-b997-2771bff545a5 | -2.5491 | -58.0566 | 2026-10-08 18:10:00 | GOES-19 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 65.3 |
| 655e3355-39e1-32b2-ba63-9f1844aa47da | -15.3419 | -42.7704 | 2026-10-08 18:10:00 | GOES-19 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Cerrado | 163.0 |
| de095890-b706-3837-adc6-5a5579a89075 | -3.0559 | -53.9062 | 2026-10-08 18:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 122.5 |
| 00ad2f79-7f56-396e-bd18-c45244108698 | -3.2945 | -54.0006 | 2026-10-08 18:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 138.9 |
| f045e287-1994-3b40-b149-e26c798d3fdd | -12.8303 | -44.6239 | 2026-10-08 18:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 142.6 |
| cdbb5b64-6a10-3ed1-a305-1dc62766388e | -5.6934 | -53.4667 | 2026-10-08 18:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 365.3 |
| 369ef9af-5d37-32ee-83af-ee4957c5e4a2 | -5.9586 | -55.3648 | 2026-10-08 18:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 125.9 |
| 978a607b-b564-3e7e-9467-ba10258060fb | -2.2803 | -48.744 | 2026-10-08 18:10:00 | GOES-19 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 52.7 |
| 4c702795-be91-3e25-a796-5dbb06ac2c9c | -2.4942 | -58.0575 | 2026-10-08 18:10:00 | GOES-19 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 58.2 |
| 86156166-3639-3131-b446-68e47215a855 | -2.2198 | -58.1196 | 2026-10-08 18:10:00 | GOES-19 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 57.8 |
| 9b69c789-6998-3e95-89d5-f6c838d761d8 | -4.934 | -42.8108 | 2026-10-08 18:10:00 | GOES-19 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 91.6 |
| da950a09-c8b7-392d-89c0-a43a81f381c9 | -3.0375 | -53.9066 | 2026-10-08 18:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 73.1 |
| ceeaf5dd-ecd5-3a46-b12f-3e35759a3230 | -6.1974 | -52.8295 | 2026-10-08 18:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 79.1 |
| a166b222-715e-3ee3-9c49-934778b4608e | -2.9819 | -54.0287 | 2026-10-08 18:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 84.4 |
| 683aca82-8302-31f5-93b7-3d5146bc444d | -5.9772 | -55.344 | 2026-10-08 18:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 67.6 |
| 68e73176-ffb6-3dc6-a3fd-1ecafe427da4 | -11.2849 | -45.2063 | 2026-10-08 18:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 191.8 |
| df195ec7-5c8b-386a-b44b-b6bdb1360867 | -2.8713 | -54.1518 | 2026-10-08 18:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 72.7 |
| bac750e2-edf5-30d7-89a7-fa9538873832 | -5.7469 | -42.0643 | 2026-10-08 18:10:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 113.7 |
| 7b407a73-da0b-3150-90ab-0eb1ebc195a3 | -12.1554 | -44.708 | 2026-10-08 18:10:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 130.5 |
| b3c0261b-855f-34d7-9e80-559e3e7ce032 | -4.7589 | -55.6516 | 2026-10-08 18:10:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 56.7 |
| 8c9095cf-327d-3816-8e10-9335d66da33f | -3.1874 | -58.8358 | 2026-10-08 18:10:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 101.7 |
| dfea3547-8f0e-37bb-b03a-4006049b3e9f | -3.245 | -57.8886 | 2026-10-08 18:10:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 101.8 |
| 143a53ac-dcd0-3fa2-b0a3-e981cffca418 | -6.6711 | -45.3761 | 2026-10-08 18:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 307.8 |
| 72e4d579-6bf4-3953-bbe3-e1798ca393bf | -7.5847 | -55.7205 | 2026-10-08 18:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 71.9 |
| 3f8c66d9-625a-3f0b-9dad-2852fb21747e | -9.1294 | -45.8405 | 2026-10-08 18:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 119.1 |
| 2ce1f542-b2e8-3996-8564-ead1dc8e2c18 | -11.2816 | -41.1194 | 2026-10-08 18:10:00 | GOES-19 | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 220.9 |
| b9b72585-54e6-3250-8ce1-69b55bf46a69 | -9.479 | -67.4897 | 2026-10-08 18:10:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 118.3 |
| 01f716f2-88e1-35ae-a476-b57a930e9469 | -6.4568 | -55.4609 | 2026-10-08 18:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 98.0 |
| ff6ea34f-161c-3a39-93d4-367ece2d34e4 | -9.1257 | -67.8137 | 2026-10-08 18:10:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 103.9 |
| e54223c0-5c23-308f-8902-f43a07f234c5 | -6.1402 | -53.0574 | 2026-10-08 18:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 84.3 |
| 254061e7-b5f9-32b6-8e9c-9a7da3895f77 | -5.4958 | -42.8413 | 2026-10-08 18:10:00 | GOES-19 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 166.9 |
| ae5375f8-dae0-3c37-8434-8c34fc17e43b | -2.4623 | -56.0879 | 2026-10-08 18:10:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 131.7 |
| f413dc1e-13fa-3567-af0b-8613335bec65 | -11.7335 | -43.649 | 2026-10-08 18:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 105.7 |
| 077cf419-5b61-3e11-8e33-e8c4c9d75f0a | -9.9205 | -44.8124 | 2026-10-08 18:10:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 108.5 |
| 4f9357f3-3b82-339f-a965-16d6ed9a54bf | -6.3283 | -55.3276 | 2026-10-08 18:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 78.2 |
| 1faaeba6-b1d6-33f0-9c23-43d1246b0a89 | -3.724 | -57.1189 | 2026-10-08 18:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 90.4 |
| c2cad1a3-9b2b-3791-b4e2-45f482757c7d | -6.7485 | -45.1431 | 2026-10-08 18:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 221.0 |
| 128bee0d-b199-308c-8ae5-bae26c4b0d79 | -11.5989 | -43.6699 | 2026-10-08 18:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 94.2 |
| 3ecfd7b2-ef2d-3b78-b304-da930878f798 | -9.9801 | -45.9009 | 2026-10-08 18:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 304.9 |
| 2957c9cb-0e65-338d-9be0-0fa87fd5e0f0 | -6.1431 | -52.6481 | 2026-10-08 18:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 68.4 |


[Clique aqui para ver as próximas entradas](README388.md)
