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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1aac150b-b408-33b1-853b-192c74a0a46f | -12.8859 | -58.1891 | 2026-05-23 05:00:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 65.3 |
| a2d0dcc9-8bbd-348f-bd69-f96b266e18df | -12.9049 | -58.1875 | 2026-05-23 05:00:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 48.0 |
| 6109cc08-840c-3229-b407-5cb32d6eb3c0 | -5.35333 | -45.18859 | 2026-05-23 05:06:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b4d91c6f-7f5b-3467-ab4f-ab581a567a4d | -5.95622 | -43.49117 | 2026-05-23 05:06:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 43bf161f-4fc5-3e07-bb1d-4f5a256d8cb9 | -5.77784 | -45.12912 | 2026-05-23 05:06:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6e1df116-623d-3184-8493-a485dec39663 | -2.07713 | -52.41543 | 2026-05-23 05:06:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f55bfae2-6d4a-3c63-8193-42cbdaa33732 | -5.95394 | -43.48915 | 2026-05-23 05:06:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 5e1d9738-0eaf-3db9-a301-3dd8bb968e39 | -6.21773 | -46.88535 | 2026-05-23 05:06:00 | NPP-375D | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 770d74de-aec9-3716-a1ce-ddd378eabc61 | -6.39331 | -44.1682 | 2026-05-23 05:06:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| ad695a21-e6d4-3bdd-baec-68a9c132a67a | -5.77737 | -45.13235 | 2026-05-23 05:06:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5ce50da3-3626-3b15-a635-468ee266ac51 | -6.63968 | -43.9171 | 2026-05-23 05:06:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 550afae5-721a-35b3-a235-f7b4d60e2b83 | -5.77298 | -45.12481 | 2026-05-23 05:06:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cbc00b52-1ac1-3be0-afc9-cbf01375713e | -5.95022 | -43.49032 | 2026-05-23 05:06:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8fdd622d-43ec-3ffe-a85a-d69f4c9db6f6 | -6.39276 | -44.17223 | 2026-05-23 05:06:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 35cb3c1f-5505-3f23-aa06-a5c6faa21dab | -5.95082 | -43.486 | 2026-05-23 05:06:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c76eb8ff-80ab-35eb-be85-ea9d0c31e49a | -6.64558 | -43.91783 | 2026-05-23 05:06:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a4be3536-47a1-326e-b7ee-77b4b5335228 | -5.95681 | -43.48684 | 2026-05-23 05:06:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 14ca42ea-e679-38fb-8668-e0948a1fe036 | -0.08829 | -51.28005 | 2026-05-23 05:06:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2801975f-210d-3f5a-86dd-94cdbf89b5dd | -0.26049 | -53.07677 | 2026-05-23 05:06:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 8e59430d-748f-33dd-adb7-f35bcf6e6eee | -11.94554 | -57.04093 | 2026-05-23 05:08:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 776d4d9c-6c9b-3d07-ba00-1bc118061ffd | -12.44699 | -54.44824 | 2026-05-23 05:08:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 41f63f48-bf1c-33ac-b85d-cec120d1b040 | -11.45243 | -52.92677 | 2026-05-23 05:08:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 13.9 |
| 8685eb12-324b-327c-afec-e476237d722e | -11.45302 | -52.92274 | 2026-05-23 05:08:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c529d4fc-e52b-3cb3-a474-2a654afc8452 | -12.16985 | -56.45135 | 2026-05-23 05:08:00 | NPP-375D | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b779b1b3-5638-3fc8-8a21-67dcd118f4fb | -10.48568 | -42.40826 | 2026-05-23 05:08:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 3.6 |
| b64d0b1a-f78e-395f-adb8-33cf2f1184eb | -11.79276 | -57.35361 | 2026-05-23 05:08:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 00ab9621-1110-38eb-9439-c181ccb2dc10 | -10.4782 | -42.41345 | 2026-05-23 05:08:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 344da473-942d-35cd-aa72-bb411b73d110 | -7.01114 | -45.00951 | 2026-05-23 05:08:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 542d9fb9-61b4-3621-b271-0c4f74737df3 | -10.48342 | -42.41154 | 2026-05-23 05:08:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 2.8 |
| cac4a53c-e6dd-3cc1-9487-a3e50a6a06c1 | -11.79495 | -57.36165 | 2026-05-23 05:08:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 00b1f71e-de7f-33b2-afc2-3f5c52f3a0a4 | -10.48415 | -42.40545 | 2026-05-23 05:08:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 2.8 |
| e5b02cba-2e72-3a9e-a016-d738b7de0397 | -7.64321 | -45.3026 | 2026-05-23 05:08:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 33753f3e-010a-3dca-b5a2-c3e3d6c0a3ba | -11.63653 | -58.25246 | 2026-05-23 05:08:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| de901779-c300-3b25-93fb-78e2d8e78137 | -9.30131 | -45.49579 | 2026-05-23 05:08:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b8a9ee2c-aa06-3c14-8081-90953e37804d | -12.17319 | -56.4519 | 2026-05-23 05:08:00 | NPP-375D | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7aa61ccf-be04-3cd3-9ad2-5232d4e90173 | -11.79337 | -57.34989 | 2026-05-23 05:08:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1811d33b-f374-33f2-b329-04254ac855af | -10.48268 | -42.41765 | 2026-05-23 05:08:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 553da016-6b6d-3db3-a07b-117c3b8b8b52 | -7.0056 | -45.00897 | 2026-05-23 05:08:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| b8562803-1930-348f-bc35-f262c47c17c8 | -10.48499 | -42.41436 | 2026-05-23 05:08:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 3.8 |
| f350c4d3-7b8f-38d9-8e45-e6c4bd5e2d88 | -9.30084 | -45.4994 | 2026-05-23 05:08:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 211073ff-a6e0-3887-8087-b7b26c941473 | -12.44812 | -54.46349 | 2026-05-23 05:08:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c25eca1b-74f2-3fa9-a52a-b695676e2cee | -11.79215 | -57.35734 | 2026-05-23 05:08:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5024b043-f815-383a-a55e-cfc80bd6dfd6 | -11.79153 | -57.36108 | 2026-05-23 05:08:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fa6b6f33-3599-3862-85df-96b96169780d | -12.44925 | -54.45615 | 2026-05-23 05:08:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e5b6f978-c663-3707-9167-9d322de1fb49 | -12.44869 | -54.45982 | 2026-05-23 05:08:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5e9cb9a8-1f22-38f2-89ac-da4fb36b15c3 | -11.78995 | -57.34932 | 2026-05-23 05:08:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| cb75df58-0de3-340d-b659-723aa9d36961 | -11.4489 | -52.92621 | 2026-05-23 05:08:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 13.9 |
| 78826db8-0566-3283-8c63-8d4361aaf730 | -9.21864 | -48.5927 | 2026-05-23 05:08:00 | NPP-375D | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 79f1cd57-08f4-3163-b8d3-dcffc5dad84e | -11.79618 | -57.35417 | 2026-05-23 05:08:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 600a963a-29ce-3542-a63d-cdfb99198675 | -11.78934 | -57.35304 | 2026-05-23 05:08:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c1ebcb81-a563-38e6-b969-27bca4e8786a | -9.14324 | -51.28556 | 2026-05-23 05:08:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 2b1f4ecc-7edc-3b0f-ade9-1c559debc2c0 | -11.94892 | -57.0415 | 2026-05-23 05:08:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 22193aa6-3a88-3ba6-9cab-7b5cf19c6825 | -12.45037 | -54.44878 | 2026-05-23 05:08:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 89414def-f9b2-3683-bde1-d15d3a87b918 | -11.79679 | -57.35046 | 2026-05-23 05:08:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2299b9ab-4420-38cf-825b-64ff8ae32b36 | -15.2283 | -57.6517 | 2026-05-23 05:10:00 | GOES-19 | LAMBARI D'OESTE | MATO GROSSO | Brasil | 5105234 | 51 | 33 | nan | nan | nan | Amazônia | 54.1 |
| 93bc8dab-521e-3655-842e-6bedf1c35525 | -11.1903 | -55.9101 | 2026-05-23 05:10:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 46.1 |
| f074ed69-59bf-3660-bbd1-d7e7ca8c02a6 | -15.09482 | -57.63345 | 2026-05-23 05:10:00 | NPP-375D | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 4c7160ee-8ec9-3982-b699-07b02ee7df6e | -12.8907 | -58.18514 | 2026-05-23 05:10:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 22494562-ce2c-35a7-8c0a-8ed15c810fed | -15.09542 | -57.62978 | 2026-05-23 05:10:00 | NPP-375D | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b795dc2e-3ee9-30f5-b7fe-94080e73e710 | -14.05575 | -52.77982 | 2026-05-23 05:10:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c7070b02-7dd3-30c1-bf7f-3a73aa93bc53 | -16.85402 | -49.56318 | 2026-05-23 05:10:00 | NPP-375D | GUAPÓ | GOIÁS | Brasil | 5209200 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0118a97c-0c6c-3e43-af15-4144abeaca09 | -16.85207 | -49.56453 | 2026-05-23 05:10:00 | NPP-375D | GUAPÓ | GOIÁS | Brasil | 5209200 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c86227da-8364-3948-8198-afb33f4c0b20 | -12.89335 | -58.16946 | 2026-05-23 05:10:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 8e465b5b-3223-3972-bd8c-8bf4c115e4ea | -12.88766 | -58.17778 | 2026-05-23 05:10:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 6e0c0000-5839-300b-85fd-6921f7a897a5 | -12.89351 | -58.18965 | 2026-05-23 05:10:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 6.2 |
| beacd13c-6da5-3d7d-b17c-7e4c19608305 | -12.88637 | -58.18561 | 2026-05-23 05:10:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| c3bd861d-a53d-30a0-bd77-4ae5a4a349ae | -12.89484 | -58.18183 | 2026-05-23 05:10:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 83985064-c632-3b39-9201-db05ad7290a7 | -15.21965 | -57.65839 | 2026-05-23 05:10:00 | NPP-375D | LAMBARI D'OESTE | MATO GROSSO | Brasil | 5105234 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| a9830d59-becf-3c13-bf66-aca7769963e8 | -15.22699 | -57.65588 | 2026-05-23 05:10:00 | NPP-375D | LAMBARI D'OESTE | MATO GROSSO | Brasil | 5105234 | 51 | 33 | nan | nan | nan | Amazônia | 15.2 |
| c58d37ce-0b88-3d30-8114-a87168f42f95 | -15.22025 | -57.65471 | 2026-05-23 05:10:00 | NPP-375D | LAMBARI D'OESTE | MATO GROSSO | Brasil | 5105234 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| b44cd124-ce45-3e4a-93cf-3126b82b2476 | -21.52307 | -48.62502 | 2026-05-23 05:10:00 | NPP-375D | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 76060a32-0a56-313a-b182-22058655a1b2 | -21.5178 | -48.62446 | 2026-05-23 05:10:00 | NPP-375D | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| aa41082b-6c8c-325d-b30c-a25c49bdb597 | -14.17752 | -52.86319 | 2026-05-23 05:10:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 3e5fce66-b4eb-380d-a2b8-5dad429c7e28 | -15.09602 | -57.6261 | 2026-05-23 05:10:00 | NPP-375D | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 205843f3-0e23-3a75-b9f2-f8863534875c | -12.89418 | -58.18575 | 2026-05-23 05:10:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 12d4103e-8d84-3b13-8e1b-0f1ca68a3dd2 | -15.10277 | -57.62727 | 2026-05-23 05:10:00 | NPP-375D | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| fa1f020c-5729-30f3-9cb5-6a0bf5b25f0b | -14.16534 | -52.87008 | 2026-05-23 05:10:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1b720bd8-f4c6-36ca-bdf2-35723fb20d5e | -14.16169 | -52.86951 | 2026-05-23 05:10:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 979a2897-1436-3cb1-9694-40bc1d10b3cf | -12.88572 | -58.18952 | 2026-05-23 05:10:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 81904944-32cc-3c9f-a034-893f47e53308 | -21.51817 | -48.62095 | 2026-05-23 05:10:00 | NPP-375D | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 32df7b4b-161d-39c3-9120-5775d6d88f2b | -14.16473 | -52.87437 | 2026-05-23 05:10:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 76802f52-83ec-363b-8d99-eb2a896a6e4c | -12.88701 | -58.1817 | 2026-05-23 05:10:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 13f61093-6851-3948-9987-ab8d6b48c3db | -15.10337 | -57.6236 | 2026-05-23 05:10:00 | NPP-375D | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 03ea9020-7ca3-323e-9431-e2c303073541 | -12.89219 | -58.19748 | 2026-05-23 05:10:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 4d20f8fb-f171-39c4-b7ac-61cfb282f30c | -15.22362 | -57.65529 | 2026-05-23 05:10:00 | NPP-375D | LAMBARI D'OESTE | MATO GROSSO | Brasil | 5105234 | 51 | 33 | nan | nan | nan | Amazônia | 15.2 |
| 809cd44c-4d16-3861-bec4-429376bb0b7f | -12.89832 | -58.18245 | 2026-05-23 05:10:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 20441357-7e84-39d5-a4e1-610e46fc495b | -14.05608 | -52.78186 | 2026-05-23 05:10:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| eda1a08a-f473-3a0d-9095-3aa78c3137d4 | -15.22302 | -57.65897 | 2026-05-23 05:10:00 | NPP-375D | LAMBARI D'OESTE | MATO GROSSO | Brasil | 5105234 | 51 | 33 | nan | nan | nan | Amazônia | 15.2 |
| 7010bd75-b8d3-3318-a305-3881e5b06612 | -15.22085 | -57.65102 | 2026-05-23 05:10:00 | NPP-375D | LAMBARI D'OESTE | MATO GROSSO | Brasil | 5105234 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e089b537-b804-3a92-807c-f7eba20a59ea | -21.52344 | -48.62152 | 2026-05-23 05:10:00 | NPP-375D | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d7dcfd7d-482b-3fb5-a584-442e1751940b | -12.88223 | -58.18893 | 2026-05-23 05:10:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 5e05d460-f2bc-3bd5-9ef1-67a7c9d0cf1f | -12.89766 | -58.18636 | 2026-05-23 05:10:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f12f125f-69a4-3091-a4ca-f687d4a00ade | -12.89269 | -58.17338 | 2026-05-23 05:10:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 40435079-39c6-3a4f-ac84-eca54b1e1760 | -14.05242 | -52.7813 | 2026-05-23 05:10:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 49450568-a3c0-3718-b754-8e7252f0d098 | -15.22422 | -57.65161 | 2026-05-23 05:10:00 | NPP-375D | LAMBARI D'OESTE | MATO GROSSO | Brasil | 5105234 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fe037cd0-69ae-3c4e-b65c-0a2f27b81ad4 | -12.8781 | -58.19225 | 2026-05-23 05:10:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| db312809-7a36-35da-b11e-5c84e8df019a | -12.89202 | -58.1773 | 2026-05-23 05:10:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 395cd217-65fe-3663-9579-d5828d4b0e72 | -21.52236 | -48.62082 | 2026-05-23 05:10:00 | NPP-375D | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fc375b8e-9587-33e9-82aa-bceb78542464 | -12.89136 | -58.18122 | 2026-05-23 05:10:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 6e78b0cc-82bc-3efc-aff4-b6b8b30f2d56 | -21.52202 | -48.62434 | 2026-05-23 05:10:00 | NPP-375D | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |


[Clique aqui para ver as próximas entradas](README6.md)
