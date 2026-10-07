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

## Dados Diários - Página 79

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 26cdf01b-e23a-3e87-8955-b4c93632a4b5 | -3.50177 | -51.68648 | 2026-10-07 05:04:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5f871430-8169-3e29-ad9e-81e8a6e5020a | -3.10325 | -54.27904 | 2026-10-07 05:04:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 549c5e66-cd8b-32b6-bd0a-196c6ba85d9c | -3.96846 | -55.82259 | 2026-10-07 05:04:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c8c18a2b-bc6e-31fd-846c-e6482d3944a1 | -2.89614 | -54.07875 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3472dbb5-8c25-3c0c-8684-15bf15a8eb1b | -3.53427 | -54.63811 | 2026-10-07 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 658518c5-12df-36ae-95e9-9eed89535fb5 | -6.40238 | -55.24842 | 2026-10-07 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6e3c3b92-264a-3e18-b48e-c3b9cf3419de | -5.48048 | -44.25542 | 2026-10-07 05:04:00 | NOAA-21 | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e2377b0d-c008-3a40-bfe2-955edc33a702 | -0.04481 | -53.25248 | 2026-10-07 05:04:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7a0f27ff-3755-3881-8e7c-586d693bbee6 | -3.74243 | -51.22247 | 2026-10-07 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6c17b9da-1e05-3332-84fb-639a48355e70 | -2.83402 | -54.12978 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 219001e1-da04-3ed1-b0da-5dfcbadd77f3 | -5.88215 | -52.04117 | 2026-10-07 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a2d9814c-42e9-3e74-bd99-938822974070 | -3.6207 | -55.28218 | 2026-10-07 05:04:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 14.5 |
| d1531f12-829c-3c35-9076-bd5e42d63ab3 | -3.26615 | -50.4044 | 2026-10-07 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 14928bcd-3fdf-32eb-908c-6b201dfa4897 | -3.08779 | -54.29096 | 2026-10-07 05:04:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| efcc90f9-fc8f-3462-8f62-cb80f8dc369c | -3.08555 | -54.28347 | 2026-10-07 05:04:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| ee57e78c-6a53-3374-b1a4-686cf0c5101d | -3.5245 | -54.65447 | 2026-10-07 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 2922a3de-f681-3171-acd7-734faffa23e4 | -3.0816 | -54.26497 | 2026-10-07 05:04:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| f6146a9f-1b1f-3dc0-8925-19290d9410d0 | -3.34816 | -54.16974 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 2aa9008f-2799-3a01-bd7b-f67b4f661bbe | -3.2861 | -54.0232 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| a66a1f5e-acbb-3ae8-aeed-69ca8ffbe406 | 0.91087 | -59.62756 | 2026-10-07 05:04:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0bbd4457-9d95-31b9-b024-30c31be83245 | -3.47887 | -55.42874 | 2026-10-07 05:04:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dd5c671c-f6a0-3779-9745-f2f205eb6108 | -3.09978 | -57.66148 | 2026-10-07 05:04:00 | NOAA-21 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 041cbad8-b6ca-3205-96af-03f9e35444e1 | -3.85414 | -55.98766 | 2026-10-07 05:04:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 5c8c2989-50fc-31e0-8faa-809ae5dfc173 | -3.5349 | -54.65594 | 2026-10-07 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| af0586e1-30e2-34da-8409-4e91062a7175 | -1.99674 | -56.95299 | 2026-10-07 05:04:00 | NOAA-21 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| be7a051e-65bf-31e6-9d77-fba7402c6e7b | -2.78446 | -57.65718 | 2026-10-07 05:04:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7c752909-ea2c-34e6-a12a-0c9457549681 | -3.73773 | -59.45192 | 2026-10-07 05:04:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 83b2b3d6-29da-3dd5-8ec0-deadba0a1240 | -3.85522 | -55.98075 | 2026-10-07 05:04:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 15f7394f-6355-3b10-9351-1ba63c07f3c1 | -5.68436 | -53.48975 | 2026-10-07 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b73a797e-5ac6-3ccb-8903-ae223dd64a39 | -3.87339 | -55.82122 | 2026-10-07 05:04:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ad035d2d-ce65-3aff-800c-f1834999982d | -2.94305 | -54.17214 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| df9ea631-4c7e-38ab-8532-2bc2110be098 | -3.27606 | -54.02167 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 14e55f5b-2208-3d2b-a5e1-d15eb6570b61 | -4.8449 | -42.86362 | 2026-10-07 05:04:00 | NOAA-21 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| d47c498e-a49f-3be3-b55e-139086b3b613 | -3.1022 | -53.71743 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5937d54d-86d6-3561-8e8f-a8ed49df7e58 | -3.87393 | -55.81778 | 2026-10-07 05:04:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 01a55f70-a0a1-39ec-9c4c-0c4b08436d10 | -4.15236 | -55.14789 | 2026-10-07 05:04:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0da54a02-13e6-304a-ad57-e6ab448eff06 | -3.51019 | -54.65935 | 2026-10-07 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4e92b111-ee60-35d2-84dd-28a67ea0ade2 | -1.79525 | -57.11731 | 2026-10-07 05:04:00 | NOAA-21 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| be5fe9bc-ad10-3c96-b3cf-19018e75fa0f | -3.08011 | -54.16431 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4824b41b-5fa6-38fe-a7f1-febf1223f31f | -3.14162 | -53.71959 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| bf5ae771-dc6e-39dc-8855-e8b1fbf7d5d0 | -3.53821 | -54.65645 | 2026-10-07 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d66c53da-afd7-37aa-b329-7bd43269dace | -4.26667 | -54.87266 | 2026-10-07 05:04:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d2d1cc97-3635-31d8-8832-96b2326fc3a4 | -2.55649 | -53.96508 | 2026-10-07 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| de5ec6ad-c1e8-364b-9fd3-56034bd1337b | -3.51788 | -54.65345 | 2026-10-07 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| b95c1f02-2f42-3ec5-900b-56bc999f21d2 | -4.37373 | -54.75078 | 2026-10-07 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| a80be40d-a36d-358c-813e-a0660f13e262 | -3.04044 | -53.91625 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a4905850-c2ff-38b4-b263-0fa710ae5e07 | -3.48856 | -50.09062 | 2026-10-07 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2d711f8c-95df-3bd8-9682-1084fbc51b1f | -2.98237 | -54.04852 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6affedd0-7d7c-37a4-9180-5bb5b92c97af | -2.88521 | -54.12739 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 17ddc64a-531d-3c87-b89c-a19847b300a9 | -3.22825 | -53.88703 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 39c3e60a-bc10-3be7-b73d-9d4407ac66d9 | -3.04484 | -53.88783 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 74d086ec-9ddd-3fc7-bf8f-780af15edc0c | -4.51292 | -42.89078 | 2026-10-07 05:04:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 914793a3-5145-3ef9-8a5e-2a725a8243fe | -2.10652 | -52.06839 | 2026-10-07 05:04:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| fc7ddde4-a2f1-3c04-ac9d-9231c5a621bc | -4.16831 | -56.35051 | 2026-10-07 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bfca2939-0d50-36c1-ac51-a3b293174cf3 | -2.98657 | -54.13199 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2f26062f-cd94-32ee-a430-a77bc2668355 | -4.07347 | -51.03905 | 2026-10-07 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1d8a403f-fdbe-35a8-a0b7-622b6e2e7b18 | -2.89752 | -54.15799 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f6890d4f-99cd-3054-b84a-ed40add580d3 | -3.35207 | -59.50695 | 2026-10-07 05:04:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b27069e3-5eec-3a00-ac06-a805130e6aef | -3.53823 | -59.48375 | 2026-10-07 05:04:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c6e28dca-f385-346b-8ee2-ea8fcd142384 | -3.02978 | -53.89644 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bc70dca9-8911-386b-a5f7-ec8b21546319 | -3.08833 | -54.28747 | 2026-10-07 05:04:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| fccb0693-bebd-3379-8cce-e2cd84c86c96 | -3.51727 | -54.63563 | 2026-10-07 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4e054ad9-37dd-396d-bd2a-904ad99d6280 | -3.0983 | -53.74254 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 939066c6-038b-3e37-b2bc-7044621d1d33 | -1.28555 | -54.56905 | 2026-10-07 05:04:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9191d29f-3bd9-3fcc-b75d-82a7841b58c3 | -7.71495 | -45.44028 | 2026-10-07 05:04:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 047f6bf8-a8ba-30ef-bd64-c9bbd2120424 | -2.93917 | -54.17514 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ee151939-68e4-3ab2-9e6e-f2bead35230e | -3.23608 | -56.82355 | 2026-10-07 05:04:00 | NOAA-21 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ad60bafb-3b54-35f7-8b2d-a2ad9e2b050b | -2.59992 | -59.37889 | 2026-10-07 05:04:00 | NOAA-21 | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 677bbec7-5ac8-339f-b88e-c74b062aaefa | -3.22812 | -54.37355 | 2026-10-07 05:04:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 67f0ec4a-978c-3c7b-a4e0-283f1185f265 | -2.86197 | -54.14533 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 13312211-b77a-3e22-aca4-02ca0a11ffa0 | -3.27301 | -50.1395 | 2026-10-07 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| efca1afb-4e01-3a89-aab2-a1fc398ea1d6 | -3.18708 | -50.55708 | 2026-10-07 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 14.0 |
| a40784d8-d47a-3ba0-9797-ab9f7f7c9bca | -3.51457 | -54.65294 | 2026-10-07 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1f176cc4-9189-3661-a669-9188f438bb3f | -4.83948 | -45.79879 | 2026-10-07 05:04:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 18e0b9ec-aebe-3612-85ef-0360f9494d67 | -3.28665 | -54.01966 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| c8eb55bb-d30e-3d64-89b0-1415bfef0d90 | -2.87908 | -54.12286 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f8d81640-4937-383d-b526-2bc5488fd38b | -3.48775 | -59.58395 | 2026-10-07 05:04:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 7de12bd3-9d1f-3a1d-873a-6fe94970c5b8 | -2.87916 | -54.1444 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a1c3872d-b593-3c49-baef-4d8e5324433f | -3.1174 | -53.77482 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 8f1178be-6d34-39b4-b33a-0597fb7f05f7 | -5.73284 | -45.16368 | 2026-10-07 05:04:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| ee27b952-b7cc-3184-a655-4d3c9e5e41b8 | -5.9632 | -55.36076 | 2026-10-07 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0d740f3f-ff3a-3496-bc3c-61dd3dece6b7 | -3.08786 | -54.1583 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 49c79f0a-1959-35ee-9581-145e6bb0bb0d | -3.29334 | -54.02067 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 5aef6282-5d8c-312a-8893-9c178b212207 | -3.66859 | -60.6244 | 2026-10-07 05:04:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2722c31b-5436-39c7-ba1f-bf11467206a9 | -3.13729 | -54.36636 | 2026-10-07 05:04:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 11292540-498d-32bc-9ffa-20e8d3f642ea | -3.50911 | -54.66627 | 2026-10-07 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 70a94c14-fd8e-35d6-8473-e8c9371020b6 | -1.50955 | -54.8321 | 2026-10-07 05:04:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5d04ff4c-f5d5-3d83-8699-b9bbc5eb468d | -4.76363 | -55.65564 | 2026-10-07 05:04:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a6ba5f62-4ea6-3855-94a5-226b05c5366d | -3.54205 | -58.64862 | 2026-10-07 05:04:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7e688ef3-a5b2-3d71-9224-a6cb6ab7cb17 | -3.18315 | -50.55285 | 2026-10-07 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| b3d1a455-c1a8-3460-b48b-51dca8a5accc | -3.26668 | -50.40094 | 2026-10-07 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8ea38838-3577-3e5e-9ca3-bdbda5a15544 | -1.41535 | -53.23203 | 2026-10-07 05:04:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| bc92256d-f55f-3d42-887a-c951b79273cd | -3.0799 | -54.25398 | 2026-10-07 05:04:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b81210df-c14f-3b13-9faa-cc26c43226e7 | 0.44255 | -60.53702 | 2026-10-07 05:04:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2ebf9351-5622-37cc-a004-03dad8f10a64 | -3.58313 | -51.50359 | 2026-10-07 05:04:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8c0556b2-e107-3292-ae1c-1d9eb7806b20 | -1.14634 | -54.21647 | 2026-10-07 05:04:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bdce12cc-68c6-3a5f-bf7c-0772defa05b9 | -2.80337 | -54.08558 | 2026-10-07 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bb15ed90-ada3-3d02-bbaf-ed897590b081 | -3.27615 | -54.06511 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 6e8682b9-ec7b-365f-9c00-89ac2e6356aa | -3.53651 | -54.64555 | 2026-10-07 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 1274a36c-5764-33bf-b48d-c248af8e7243 | -3.05145 | -57.5254 | 2026-10-07 05:04:00 | NOAA-21 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |


[Clique aqui para ver as próximas entradas](README80.md)
