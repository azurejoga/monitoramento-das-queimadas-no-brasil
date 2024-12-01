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

## Dados Diários - Página 48

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 92fcbe95-f671-33e7-a309-0d1d5d31dc80 | -1.56605 | -53.83476 | 2024-12-01 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f1a653c5-c26f-34e3-93fa-c00cbb11229d | -1.71826 | -52.62041 | 2024-12-01 04:44:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 6890f934-7567-3124-9dd3-577a5ed362c0 | -2.88539 | -53.33267 | 2024-12-01 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 32b1d3bf-e5d1-372d-860c-f7fa17806124 | -2.98347 | -53.27858 | 2024-12-01 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 83cc5ad9-92d9-3407-b355-9148a7dffbba | -3.25174 | -53.92322 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| ed2c9e5b-e41f-3c41-aabf-eff9cd9aa8af | -2.37578 | -50.39301 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 5faa217f-5e1b-3536-a29f-89324b76a817 | -1.26659 | -51.8241 | 2024-12-01 04:44:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| d2f16556-14fb-32e1-bef7-de2a8bff3c20 | -3.49364 | -53.83712 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| b2332638-d3c5-3cd3-a5ea-95f34b67e0a4 | -2.14952 | -50.62737 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| abcf636e-3a87-3836-85ab-bf0eaa7e1092 | -4.11567 | -50.8612 | 2024-12-01 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| de0ce275-e819-3bd7-ab22-63432cd9e68a | -2.93508 | -49.41776 | 2024-12-01 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2aaab450-25b9-3aa3-87cc-f4dd8db01595 | -2.11614 | -50.34202 | 2024-12-01 04:44:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e1ffae67-b3d6-3ddd-aa41-3a1a27ffbfef | -1.66897 | -52.51948 | 2024-12-01 04:44:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1371c878-c3ca-354a-bd1a-6177a56357e8 | -1.85319 | -55.61689 | 2024-12-01 04:44:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 87fbeefd-042e-39e9-b27e-646f3faa98a3 | -3.7129 | -53.40754 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 09d161c1-9136-3149-8c16-a71de5681198 | -2.92903 | -51.45082 | 2024-12-01 04:44:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 5dc0bc18-9c53-3419-a6aa-48af5d3033c3 | -1.48061 | -55.3826 | 2024-12-01 04:44:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ed86df91-f90e-3bff-9fe5-469395cd1ad8 | -7.38276 | -45.83171 | 2024-12-01 04:44:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2b3a11c2-1b1f-336f-b66a-44af1a9f0cf7 | -3.95218 | -48.16982 | 2024-12-01 04:44:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| a57664e4-f601-31bd-bd2d-ed7f3173dd2c | -3.07615 | -51.09738 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b400d41c-a103-3d8a-95f9-3b640038210f | -1.59397 | -52.53688 | 2024-12-01 04:44:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 834d35b3-f3d3-3840-aaa3-f59d31a0e95a | -2.26616 | -50.72015 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5ff5251a-d43f-3ffc-835c-6a57891cf659 | -3.61918 | -50.19245 | 2024-12-01 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b36f8db3-1919-3538-ae85-b0fb1589c504 | -5.112 | -50.61388 | 2024-12-01 04:44:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b21af7bd-909f-3004-b353-0ba98244dc08 | -3.54462 | -51.28589 | 2024-12-01 04:44:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f212856d-93a0-3266-a903-d095755714e8 | -3.37318 | -50.42224 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9b3b7b25-aa11-30de-8ae5-419cd5e4dcaf | -3.30051 | -50.797 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9721788c-71c8-339c-86b2-69876b4a37b9 | -2.67512 | -46.60998 | 2024-12-01 04:44:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a32cde90-899b-3bd4-9ca4-bfe61aee9b7a | -2.75086 | -51.75757 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 3d893b6f-b5b4-34b6-a176-94d6bd0d1b0b | -4.03567 | -46.9313 | 2024-12-01 04:44:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 35.8 |
| 78bc292f-3e19-3350-beb8-abed516dbad6 | -3.96876 | -47.24853 | 2024-12-01 04:44:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d776d3fa-f766-3f4c-981e-ac490c98bb47 | -2.89595 | -55.22205 | 2024-12-01 04:44:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5232e56b-dd18-3e4b-a99e-4e67f09fc90c | -2.37802 | -50.40043 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 48f92a03-53e8-3887-aa63-d618d6fb351e | -2.8245 | -51.95314 | 2024-12-01 04:44:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ee88d691-6363-31b2-b980-1c4b287a1995 | -3.32551 | -50.18512 | 2024-12-01 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| e80734b0-3fa5-3db2-b855-f45edb9a721c | -4.18778 | -50.68471 | 2024-12-01 04:44:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 34d2b505-f30c-353c-be96-e397692e4422 | -1.23452 | -51.80378 | 2024-12-01 04:44:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 62e075c7-8ed5-3270-ac9a-49173d582900 | -2.03143 | -52.08212 | 2024-12-01 04:44:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ffd1ac1a-e112-3817-8578-c74fead53e2d | -2.63628 | -46.87989 | 2024-12-01 04:44:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 73067329-eea5-30cb-9766-e53fd28cb7eb | -1.15407 | -51.69667 | 2024-12-01 04:44:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ba726d94-7d67-38d8-840e-e94f03de8c78 | -3.4965 | -53.81963 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ae5a318b-7056-3067-ada5-04e2297eed30 | -3.86547 | -50.53825 | 2024-12-01 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 30c14e22-d013-37e4-b12e-844ab197e7f9 | -1.14566 | -53.66351 | 2024-12-01 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e1564994-8064-3403-aadf-7f89eab4c776 | -0.58067 | -51.12719 | 2024-12-01 04:44:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7e86e093-d056-37f8-bb1d-7342ca156de9 | -2.33159 | -50.67339 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4f6414b2-b2da-350d-9940-890824d77659 | -4.07878 | -54.5611 | 2024-12-01 04:44:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f330c90a-67ef-3c85-a245-f7c6a6fb9ce7 | -3.22187 | -54.17569 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 92512895-02a2-333c-9328-d15011ecfb9b | -1.14495 | -53.66792 | 2024-12-01 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0ec59be1-32c4-3f4c-8d61-568df80b2acc | -2.46401 | -46.57716 | 2024-12-01 04:44:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| abc1499b-e0e3-3c51-b640-4d08d79b6c41 | -3.29031 | -53.67245 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e42c3453-0b83-3001-9e26-b4081b41ee84 | -4.25103 | -50.83969 | 2024-12-01 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 64df735b-655a-308c-90c1-0f35697e9714 | -3.60624 | -50.37764 | 2024-12-01 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4cf03219-72b4-3ed9-b1b0-01fa4882edf3 | -2.32771 | -50.67635 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 18772794-195d-3465-8925-a132191c146a | -3.96094 | -51.2613 | 2024-12-01 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 30dbb290-7ab2-30fe-9913-b3fccca20e6f | -3.28297 | -50.6275 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 472bba6c-b8c1-3303-baac-010cd128a01a | 0.07962 | -60.46927 | 2024-12-01 04:44:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a104218d-fd31-323e-9c6d-9b72bd2c1ab3 | -3.59424 | -50.37238 | 2024-12-01 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d1d08cad-3071-36c4-9ee4-645a9f761bdd | -3.42663 | -50.20779 | 2024-12-01 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 602390d4-f6fd-32f1-adf3-57d87bc8cdfe | -2.321 | -50.65395 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 577b1569-821e-3bf9-bd08-c9f27db90ca1 | -3.10117 | -53.17451 | 2024-12-01 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b01176ba-ff5f-3f99-a7dd-7d2b4823f0a6 | -2.80312 | -54.04499 | 2024-12-01 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fe650372-17c2-3599-a576-682a23206d58 | -1.58445 | -52.27963 | 2024-12-01 04:44:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 14009c6f-bfd8-35c3-9945-152a2b2a2261 | -1.66027 | -53.75469 | 2024-12-01 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 1ccf2189-0ab1-3541-9a56-4183e26f8d5e | -2.4209 | -54.01874 | 2024-12-01 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 9e11b34b-b539-30ca-9af6-46e4ba3af5ae | -2.27473 | -53.46386 | 2024-12-01 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5b3ab390-987e-33c3-a892-302f9e784837 | -3.03452 | -50.98007 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ed787960-5116-30d0-9a1b-acd674f69b8c | -3.21843 | -49.89975 | 2024-12-01 04:44:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| aadf5eca-b795-301a-a0f3-b64640da122a | -1.06034 | -53.22478 | 2024-12-01 04:44:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1b2ebd86-875b-3c52-8d4c-6728a29a81ef | -2.62593 | -51.77573 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3cbdada4-5c2a-3422-9839-d8c6c6966bc9 | -3.41402 | -50.24471 | 2024-12-01 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 01c66bf0-1d3c-354f-b781-f1671fc48a20 | -2.99036 | -53.35159 | 2024-12-01 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1c68c5a2-5909-3b38-be7b-adc2b0b3c2b4 | -3.48391 | -50.31921 | 2024-12-01 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 809a94da-6419-3cc4-a413-ca57aa082958 | -3.09138 | -54.29657 | 2024-12-01 04:44:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8cd370aa-63a0-3648-b7e5-c17c4d1049b1 | -1.00586 | -51.73178 | 2024-12-01 04:44:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.7 |
| cde2a1ea-5d0f-3f8e-a00f-1708b1dd247f | -3.97371 | -48.93881 | 2024-12-01 04:44:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 23c16b9b-b2ae-3bc1-9392-cadff3787f55 | -3.40625 | -50.6608 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 4354c1f6-578c-3593-bead-0b4d480304e5 | -2.41905 | -50.35384 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 62958e0e-8364-3f35-985a-b7402b998203 | -3.33559 | -54.0687 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d492197e-9f8d-3c53-8a9c-3f61dcb48828 | -1.24802 | -51.7411 | 2024-12-01 04:44:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9211a80b-78fc-3228-875c-7bf8c1e65bd3 | -2.32155 | -50.65048 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cf0881e4-acb0-3b89-b10a-53d1e2206d2a | -4.05951 | -46.82316 | 2024-12-01 04:44:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2a6d2684-14d9-3c74-b818-93741c3c799e | -1.25146 | -51.74163 | 2024-12-01 04:44:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7a312c67-a5cc-316b-a579-a89f8dcca597 | -3.09786 | -53.28743 | 2024-12-01 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 629ce030-c921-3ab8-a2f7-8ab6bc67bb6b | -3.79494 | -58.97922 | 2024-12-01 04:44:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a0059434-2fd8-3eb4-9ea0-2bfe0c69857b | -2.60972 | -54.2868 | 2024-12-01 04:44:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| f1a04180-b621-32b5-80ef-24a74b5a9624 | -3.69141 | -51.08642 | 2024-12-01 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a0ac597b-dced-3245-99e4-c2d2b01e643c | -3.03963 | -51.47868 | 2024-12-01 04:44:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 32e78efb-1206-38a8-811a-a92817038b5c | -1.52635 | -52.66475 | 2024-12-01 04:44:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 09882f99-27e0-3084-81d8-ab2860cfc889 | -0.76229 | -52.41346 | 2024-12-01 04:44:00 | NPP-375D | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 51cc1850-cc04-34c6-963a-5a7ccf934030 | -2.87242 | -53.92449 | 2024-12-01 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| c2cf49c5-4fe9-3e23-b95c-d820084377f7 | -1.95865 | -46.43986 | 2024-12-01 04:44:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 48492c40-bb08-3750-9738-3ed99a22e6e1 | -0.10157 | -51.32876 | 2024-12-01 04:44:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 88ae7964-7fb0-3968-ba4a-3498cf0f11c6 | -3.48399 | -53.8145 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 39d3b35e-cba2-3b18-8d1b-bd2d74734a06 | -3.38115 | -50.11248 | 2024-12-01 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d197fc3b-8a63-3390-a560-d4ac30c1ce39 | -3.37704 | -50.41931 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 738ab640-543f-3589-9147-30c60f33ebd0 | -1.74826 | -52.65301 | 2024-12-01 04:44:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cb3bd726-c91b-39cc-a137-9c3d8c8cf884 | -1.14671 | -51.67656 | 2024-12-01 04:44:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bc3652ca-b0f4-36fc-9e7e-fce0dea959c0 | -3.2474 | -53.92012 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 583fe67e-3ce5-364c-b235-b08fb2f47288 | -4.09657 | -50.35905 | 2024-12-01 04:44:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3b24227d-07ee-351d-9cc1-7f8191df7434 | -4.17751 | -48.61434 | 2024-12-01 04:44:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |


[Clique aqui para ver as próximas entradas](README49.md)
