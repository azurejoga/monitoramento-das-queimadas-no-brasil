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

## Dados Diários - Página 31

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 42aab78c-740f-3f82-84c3-caab78991bc9 | -2.5597 | -54.00134 | 2024-11-08 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 55cb51b3-9958-348c-862a-adfd292c8257 | -4.48695 | -48.11081 | 2024-11-08 04:53:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 643c1506-6355-3d85-90b2-5e8e3a131a2d | -1.18945 | -53.89752 | 2024-11-08 04:53:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8b4d8751-cd6e-353d-9d16-010088691cb9 | -3.3809 | -50.22501 | 2024-11-08 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 3cb5c779-4d62-3a38-9008-f68b579c9907 | -2.16802 | -48.73061 | 2024-11-08 04:53:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8172e378-807b-3916-8912-9344e2e37736 | -2.77565 | -54.03456 | 2024-11-08 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| af037f4e-c2ea-341c-9125-b0cfbd37b352 | -2.07552 | -52.04183 | 2024-11-08 04:53:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e5f0ad4a-396b-3c1b-9efd-a6ce46d92d01 | -2.61647 | -51.30035 | 2024-11-08 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| be32d26e-77bc-3759-8d30-14edfb92505c | -2.65126 | -49.23718 | 2024-11-08 04:53:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e8076c19-e84d-3a18-a56c-08bd2307a57e | -2.55041 | -54.01533 | 2024-11-08 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 33570a6b-9966-329e-bc3d-b3294cda6f2d | -2.27862 | -53.82489 | 2024-11-08 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4a653c97-4098-3075-b0df-9d979a894b79 | 0.04473 | -49.54304 | 2024-11-08 04:53:00 | NOAA-21 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5d478a33-dc88-38d7-86e7-2e6b0821001c | -4.21227 | -45.73978 | 2024-11-08 04:53:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 70eae2fe-1ed8-310f-881f-4d7a464f202d | -3.04118 | -48.04014 | 2024-11-08 04:53:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b1de27a0-e9fa-360c-a0dd-6340d88803b0 | -2.17509 | -53.7029 | 2024-11-08 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1f371e84-0ae3-326a-8cb8-acf7aef0a904 | -1.1639 | -53.72738 | 2024-11-08 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4dc1e3e0-55d3-317a-9ef0-eb21c2a52c31 | -1.32637 | -54.18221 | 2024-11-08 04:53:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 328f7c13-f806-3c14-9476-e9d95e64dc79 | -2.2548 | -53.73022 | 2024-11-08 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 66658fb6-bd21-38dd-b2d1-0de7910d29ba | -4.40014 | -49.40639 | 2024-11-08 04:53:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| b704a1b6-69db-3a96-97fd-62c44f895cb0 | -1.22134 | -51.76094 | 2024-11-08 04:53:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3e96c3f3-ae95-39e9-99ff-86b8f0f9cb75 | -1.16972 | -54.16008 | 2024-11-08 04:53:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 9a399666-d555-3f9a-979e-41c1295b4731 | -2.88913 | -53.31926 | 2024-11-08 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 96872ce6-f66d-3794-9c5a-18b9c4a9664a | -1.23231 | -51.75561 | 2024-11-08 04:53:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3cf5abbb-3c8b-39e3-b4c8-394f553b8f17 | -1.33738 | -54.59595 | 2024-11-08 04:53:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 91d31ba8-d9af-397b-9490-bba8235f07c3 | -2.81629 | -52.94196 | 2024-11-08 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 971511f5-f98c-3ae9-a90f-74fde11d930f | -2.20679 | -48.82694 | 2024-11-08 04:53:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c77d5fd1-e8ac-3a3a-9ceb-60fb79ff5870 | -3.32834 | -53.18784 | 2024-11-08 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 08058a9f-951f-306b-ac81-8f80bc085f79 | -3.97088 | -48.16793 | 2024-11-08 04:53:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 19.2 |
| 99c7db7d-cabc-3b28-a41a-aae02d90c454 | -2.20096 | -48.37697 | 2024-11-08 04:53:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9e5ce60a-a22e-3b79-af13-54075d5e09ed | -1.11323 | -53.17315 | 2024-11-08 04:53:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d0787556-3b11-3cad-8a2e-bd9a67f31d82 | -0.6437 | -52.3881 | 2024-11-08 04:53:00 | NOAA-21 | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4faf4d82-fc7c-3109-b516-7a11c99a938f | -1.75725 | -52.68726 | 2024-11-08 04:53:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 393f9136-7194-3397-9e36-6fb82486a0ec | -3.20477 | -51.03913 | 2024-11-08 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 50bda345-43dd-31f4-b8e7-6f5c2ef6d9ba | -2.14965 | -54.52435 | 2024-11-08 04:53:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 75b71e71-a8a7-3999-aa07-f0866e542b32 | -3.2476 | -53.40069 | 2024-11-08 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2fc7a95f-e4bf-3161-84c9-628d19cda378 | -2.21378 | -53.72389 | 2024-11-08 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e8ecd88c-755c-3622-af76-b11872efac62 | -0.90765 | -51.65568 | 2024-11-08 04:53:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 694943b3-bdb8-3f9b-9315-36f6cd6c12b7 | -6.96915 | -45.46748 | 2024-11-08 04:53:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 36c67496-3a21-3828-bb80-582751ca4848 | -4.34868 | -48.62807 | 2024-11-08 04:53:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e99c0e64-679a-35fc-92d3-40bfe03395ab | -3.75546 | -47.1506 | 2024-11-08 04:53:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fe815c6b-7089-3db0-a8eb-28bf46ab22b7 | -1.97587 | -46.81763 | 2024-11-08 04:53:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b8de213e-b068-3b8d-b339-5795e87fd308 | -1.62596 | -52.24328 | 2024-11-08 04:53:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f9e327ef-a35c-34a2-b5e3-114c151c83d0 | 0.30378 | -51.13279 | 2024-11-08 04:53:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| eaec95d2-3a8e-350c-8b00-c8076c618614 | -2.64886 | -46.75039 | 2024-11-08 04:53:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4390b593-05f3-3b39-854e-19ca0eac19f3 | -3.07919 | -50.57162 | 2024-11-08 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5984567e-6e71-30f6-9fb5-11b92ed008b8 | -3.11161 | -51.2886 | 2024-11-08 04:53:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4d14cb9e-acc4-3047-a227-41122525434f | -1.62103 | -52.25312 | 2024-11-08 04:53:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d3ee2648-3370-31fd-a3a6-8c55eaed92bc | -5.72652 | -43.8156 | 2024-11-08 04:53:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| aeaf7d9a-e9e9-3afb-8124-2949b520c8de | -2.88525 | -48.28986 | 2024-11-08 04:53:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5f13c919-caa5-3474-aabd-904e54ff3c62 | -1.38827 | -52.19516 | 2024-11-08 04:53:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8184b247-a5cf-309a-9388-e2ffde9db1b1 | -2.8137 | -53.99443 | 2024-11-08 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 92cd77db-3077-3ad7-8c50-1096a152e1e3 | -2.82763 | -48.4674 | 2024-11-08 04:53:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a8b051d8-a0b3-3c0a-8708-86f0b53d6729 | -2.95574 | -53.71737 | 2024-11-08 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1af2dff1-1a8a-377e-be2a-a8c3e6a1604d | -4.67655 | -46.45118 | 2024-11-08 04:53:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 22c6c55c-ca23-356f-986a-a84c3ccf2151 | -3.07086 | -50.56706 | 2024-11-08 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a52060ac-b2c4-3acb-9f93-4729558f90ca | -2.87047 | -50.32299 | 2024-11-08 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 96d393fb-f75d-3e29-b561-08e0f91f03c4 | -5.98866 | -45.36549 | 2024-11-08 04:53:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 14.1 |
| d1488733-6415-359e-8eaa-dd9997d077bf | -2.81246 | -52.96654 | 2024-11-08 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 372e24ce-6317-3716-b077-ec67f91eb12c | -2.13618 | -48.74666 | 2024-11-08 04:53:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e05e8b81-b76f-3868-ad51-c9ca586313ff | -5.00065 | -46.89752 | 2024-11-08 04:53:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5345c2d2-457d-3ffc-878d-6a1bf68046b9 | -3.03675 | -53.26921 | 2024-11-08 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b5eff2b6-fcb6-393e-ac16-86ac2df67219 | -1.52508 | -52.17104 | 2024-11-08 04:53:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8f8e10c3-2b5e-3972-837e-803ca433b49e | -3.04626 | -53.27431 | 2024-11-08 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 587279bf-eb4b-3cce-8267-bf888229bc52 | -2.68067 | -52.52557 | 2024-11-08 04:53:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ff79da55-711e-34cf-a91f-a3de99b55efd | -2.05229 | -53.29952 | 2024-11-08 04:53:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 10d8cba0-c7b1-36db-be98-61d8947a781f | -5.64153 | -44.24345 | 2024-11-08 04:53:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 86fd2ade-dc8a-3e38-a6a8-d23e607b97fa | -4.51833 | -45.67625 | 2024-11-08 04:53:00 | NOAA-21 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 27.1 |
| 45794f09-1684-3297-a582-aee6cf8f86e7 | -2.18618 | -53.6329 | 2024-11-08 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7bad7448-1619-3c9b-ad10-82782859a265 | -4.51318 | -45.68009 | 2024-11-08 04:53:00 | NOAA-21 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 23.4 |
| 9630aee3-b1d7-314b-ac8a-afca0fe60c14 | 0.0315 | -49.43663 | 2024-11-08 04:53:00 | NOAA-21 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 118dbccf-e3a7-32d1-8f24-39c150c0fb8a | 0.03491 | -49.4361 | 2024-11-08 04:53:00 | NOAA-21 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| c3059de5-3789-3210-a010-04c9da8f27c0 | -2.76069 | -54.03995 | 2024-11-08 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| fb034b35-481e-3269-b11d-aefb6f5cec6d | -3.80652 | -47.79768 | 2024-11-08 04:53:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d5571a78-fda3-3f8d-9e4f-10c33b2f82bd | -2.81356 | -52.95949 | 2024-11-08 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d213c72c-b1a8-3d9a-9fce-f6ac30c60860 | -2.96037 | -52.91105 | 2024-11-08 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d7798973-fbea-32ee-8ff7-7fd97fdd2d1e | -2.4981 | -47.23693 | 2024-11-08 04:53:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 94fc5129-75ec-3934-8848-23a2dd400d28 | -1.38442 | -52.1981 | 2024-11-08 04:53:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d4f5c8ad-8b5e-3df4-a8ef-46e7153d1940 | -3.4411 | -51.11522 | 2024-11-08 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7ecbe342-3a8d-39dd-ae61-d971da02092b | -3.24702 | -51.55409 | 2024-11-08 04:53:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| f03e4704-d0c0-32a6-9981-913ad81ef153 | -5.43928 | -46.36005 | 2024-11-08 04:53:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| b4f420e9-f1e8-3deb-bf53-caa7d8dae37b | -2.05481 | -52.08788 | 2024-11-08 04:53:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| f856e6b9-cd34-3bd2-b101-ce917ca3e137 | -1.50856 | -54.51862 | 2024-11-08 04:53:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7d31c6c5-139c-342f-931e-bf527b0128ad | -2.1856 | -53.63656 | 2024-11-08 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 997c0041-1a0b-329c-ae70-74f7f991528d | 0.04187 | -49.52484 | 2024-11-08 04:53:00 | NOAA-21 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5922638f-d411-354f-8e72-dbfecb5d630d | -3.62473 | -50.18973 | 2024-11-08 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ea846c39-d4aa-3cea-b344-dcbc1babe852 | -2.58154 | -53.99702 | 2024-11-08 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 5dcca395-a5d9-36c2-ba53-d9e37085b9c8 | -2.86766 | -50.31884 | 2024-11-08 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| e486b452-1c37-340f-86c2-d5f06332e61f | -1.33969 | -52.18063 | 2024-11-08 04:53:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 73003e92-d254-3ea9-8a00-0a0108b14db7 | -5.54785 | -44.33026 | 2024-11-08 04:53:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3ca52083-c124-3ad6-8604-079b3bb120c3 | -3.02576 | -51.53347 | 2024-11-08 04:53:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 53bd654c-fcf1-3696-98bd-469df3f075f6 | -3.2504 | -53.4048 | 2024-11-08 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4775ab64-c585-3b48-b3ba-bd6652ff5fc5 | -3.55264 | -47.38118 | 2024-11-08 04:53:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 71.5 |
| 3509997c-8acb-3674-85a5-ccd9da28dd87 | -3.87279 | -52.38413 | 2024-11-08 04:53:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f578cba7-6631-36f0-8288-c5e1b4390a39 | -6.74542 | -46.9141 | 2024-11-08 04:53:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 128eb102-12d8-340f-8f98-905259698dce | -2.7471 | -49.13037 | 2024-11-08 04:53:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 235bcd37-5d48-326e-9332-72d486742d27 | -4.67799 | -46.41054 | 2024-11-08 04:53:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 9ef2df4a-0d39-3e8a-9ad4-22c7821af16b | -2.8566 | -48.44986 | 2024-11-08 04:53:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8d169e8f-158b-396c-8e0a-84a7028350b1 | -3.02556 | -48.09343 | 2024-11-08 04:53:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 19eb1216-fc69-3bf2-8b33-573fbafc7ae4 | -4.68284 | -46.40719 | 2024-11-08 04:53:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 15.3 |
| d1d1b006-b8d3-3b8d-bf69-d8e8d98c7185 | -4.48482 | -48.4921 | 2024-11-08 04:53:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |


[Clique aqui para ver as próximas entradas](README32.md)
