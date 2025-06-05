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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| deefe730-e75d-3131-9dca-6bd7c3c6680f | -10.69597 | -57.6481 | 2025-06-05 04:34:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 221617c5-00c1-3031-bff0-4a58461357e1 | -11.54233 | -56.44143 | 2025-06-05 04:34:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| f6f3df38-4444-3535-9d0d-9854105a2197 | -11.90329 | -47.45217 | 2025-06-05 04:34:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7b561767-8309-367d-9f83-8d980aa9ba01 | -10.69655 | -57.64497 | 2025-06-05 04:34:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6e32352c-e236-3f49-a7a7-f5e2e4b0629d | -13.53556 | -56.56356 | 2025-06-05 04:34:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d556a610-d93e-3395-b22a-99e2cdea8e7d | -13.53105 | -56.56267 | 2025-06-05 04:34:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a9e25aed-f235-3ac2-b4fa-8cd8c444c353 | -10.65089 | -49.42625 | 2025-06-05 04:34:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 05d6a926-bb60-30f0-b6aa-d7b4140bc94f | -13.53202 | -56.54961 | 2025-06-05 04:34:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8e5c6c0b-39cd-39ff-9664-679db9a30b66 | -10.65639 | -49.43431 | 2025-06-05 04:34:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 262da903-631b-38b7-809d-dc90c48e5229 | -12.66312 | -58.22222 | 2025-06-05 04:34:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| e0228e55-0254-359c-8a2c-76ce539494b1 | -12.67393 | -58.2213 | 2025-06-05 04:34:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 695356eb-d62c-3e1f-9e52-35509f68fd21 | -10.88058 | -46.85943 | 2025-06-05 04:34:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a9b715fe-1e3e-3f2a-8f8d-b3a762ed1c72 | -13.51665 | -56.58931 | 2025-06-05 04:34:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2c463477-d4d6-3042-b3d4-9132122fe01b | -11.54786 | -56.43737 | 2025-06-05 04:34:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| ca64e65d-49f0-3696-949e-0f766e521169 | -10.69031 | -57.65016 | 2025-06-05 04:34:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 43117ab8-e717-31f8-a3e1-10f791f6ad5d | -11.48565 | -51.69772 | 2025-06-05 04:34:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3a3892f0-d4b4-3967-b3d3-89c7193ced3e | -12.1234 | -54.66349 | 2025-06-05 04:34:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bb207b8c-7404-319a-8414-c8d6c09f1961 | -10.68877 | -48.97055 | 2025-06-05 04:34:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8c5d066e-f23a-3f4d-a358-b1ae6e4822d2 | -14.73504 | -45.10057 | 2025-06-05 04:34:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bdd056ab-6ac4-37e0-83db-23f099435558 | -8.21282 | -49.47235 | 2025-06-05 04:34:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ee48f78d-f5bc-371d-95a0-d11fb8b4a7ba | -13.52609 | -56.58243 | 2025-06-05 04:34:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b51c2271-9da0-393b-b330-4c56e84bd19e | -11.55143 | -56.41766 | 2025-06-05 04:34:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0d82703e-8adb-3093-86fa-2722c493c67d | -13.5207 | -56.58635 | 2025-06-05 04:34:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e841ac04-06a6-3369-9251-fa48cd1bbe15 | -14.73828 | -45.10622 | 2025-06-05 04:34:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 55ddc7f7-4001-33de-979e-c8ccc3a649cc | -13.07014 | -46.74634 | 2025-06-05 04:34:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6dbbb1df-9262-35f3-826d-4238c92ffdc9 | -11.62384 | -55.38364 | 2025-06-05 04:34:00 | NOAA-21 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f023a857-d09f-38e5-9390-0ffdf029489d | -11.90274 | -47.45588 | 2025-06-05 04:34:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 932c2874-6945-33be-9f2e-2f12df978a56 | -8.94366 | -47.30083 | 2025-06-05 04:34:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 54fdb35e-91ee-30d0-997d-c2dd9bf30f95 | -13.70317 | -47.74495 | 2025-06-05 04:34:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 46560785-5891-358c-82b3-b4cc8a87cd0d | -11.90668 | -47.45271 | 2025-06-05 04:34:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 107f887e-2b29-31af-a78a-5a8e25fcb579 | -14.22984 | -45.47405 | 2025-06-05 04:34:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e9018a80-6cee-341a-b38f-34ff52cf1d6e | -13.51226 | -56.55553 | 2025-06-05 04:34:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1494922d-9bba-3562-b9a6-69465d40705d | -10.81634 | -56.95866 | 2025-06-05 04:34:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 16.3 |
| c3bc941d-b784-3d21-96d9-cec570928b99 | -10.30256 | -57.14361 | 2025-06-05 04:34:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 644ff2b9-665f-3ad3-bc47-74ea0f882b53 | -11.62816 | -55.38446 | 2025-06-05 04:34:00 | NOAA-21 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| db41bda1-aeeb-32bb-9805-44a5d3c22fb3 | -11.44203 | -45.11591 | 2025-06-05 04:34:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| fdd1c622-8377-3399-a371-70a2f1b48afc | -14.72718 | -45.09949 | 2025-06-05 04:34:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 73df2921-8aa6-33ea-81cb-2802be1a622a | -10.66563 | -44.37887 | 2025-06-05 04:34:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f05d6316-cba4-30d9-b1c9-c8e6d138947d | -13.52478 | -56.5711 | 2025-06-05 04:34:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 29.7 |
| 8b722559-24c5-38b1-ab45-ddd6c43366ac | -12.71238 | -48.57562 | 2025-06-05 04:34:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5e9dc1ab-1660-3643-9bcd-525a2bd4bd5e | -13.50857 | -56.5501 | 2025-06-05 04:34:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c50678c7-fa0b-3a7c-bfbf-ab1122d4af52 | -13.51423 | -56.57038 | 2025-06-05 04:34:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 18.0 |
| 5f4fc878-4cc2-3b41-b84e-006e8fe6684e | -11.84001 | -51.29651 | 2025-06-05 04:34:00 | NOAA-21 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2c850b39-73f3-305f-989c-7db40e2b9b9b | -8.96214 | -47.97409 | 2025-06-05 04:34:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c3c4406d-952e-3d08-94a6-aa2b086e36b9 | -10.7083 | -48.78077 | 2025-06-05 04:34:00 | NOAA-21 | FÁTIMA | TOCANTINS | Brasil | 1707553 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 342b5b19-ba9e-3d9f-a6f6-49077da87e32 | -12.64749 | -54.12757 | 2025-06-05 04:34:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e940479b-3fd0-3033-b1ce-1b4621c8a043 | -13.5201 | -56.54632 | 2025-06-05 04:34:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 289828cb-7653-39a4-bc19-d021a5ff45a7 | -10.12712 | -48.68727 | 2025-06-05 04:34:00 | NOAA-21 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c550653d-fefd-3ba8-8f74-8ea1b5c9cf38 | -12.36939 | -54.17124 | 2025-06-05 04:34:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0608cae5-14da-36a1-944b-fea17cfe1aa5 | -13.51835 | -56.55555 | 2025-06-05 04:34:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a92284a0-46b6-35eb-ba6b-c9a0eee607cf | -12.0826 | -54.58767 | 2025-06-05 04:34:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 58fa272a-fe6a-36c1-a156-32829b81ef8c | -13.51573 | -56.59412 | 2025-06-05 04:34:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8305b27b-aff8-3aa8-93fb-010b2402ffe9 | -10.16594 | -53.92596 | 2025-06-05 04:34:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f027a802-7bd0-3bd6-9584-efe3eff7de05 | -9.40345 | -48.41857 | 2025-06-05 04:34:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7db48ac8-57dd-3870-8c42-5c8f81925a6d | -9.45886 | -55.94255 | 2025-06-05 04:34:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ad3e48ca-2bfa-35e2-b005-b45d0ecb65c8 | -10.65584 | -49.43781 | 2025-06-05 04:34:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d9215303-69ed-38a6-a196-261bf7534357 | -10.30308 | -57.14075 | 2025-06-05 04:34:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2c824d4e-a682-37f1-be45-96b43dd6efa3 | -11.38075 | -55.11114 | 2025-06-05 04:34:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c2cbe3ab-a51a-3087-9fa0-edd6eb06009c | -11.55545 | -47.6214 | 2025-06-05 04:34:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| b20353aa-f4e5-3ae8-9844-ab2a13a42952 | -13.51935 | -56.575 | 2025-06-05 04:34:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 29.7 |
| 105cdd4c-2129-3c2a-a864-dde6d457b2f5 | -8.04409 | -46.89496 | 2025-06-05 04:34:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cca06648-7b7a-3945-aa8f-828e41709baf | -14.23284 | -45.47611 | 2025-06-05 04:34:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b3fb5622-2f82-3ba2-8268-cc91e1eefc20 | -12.29044 | -43.54691 | 2025-06-05 04:34:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3eec920a-8503-3030-9278-03a6eccf0ed4 | -9.39134 | -48.40954 | 2025-06-05 04:34:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 690b3fa2-bba1-33a7-9b84-0a5156b8ccd9 | -11.81675 | -46.14207 | 2025-06-05 04:34:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ceaea359-5df8-3f4d-96e1-67a96bb13967 | -13.52463 | -56.54712 | 2025-06-05 04:34:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 742a65d8-b45c-340c-80be-e920df7f9dd1 | -13.5114 | -56.56021 | 2025-06-05 04:34:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 9719a176-b37e-3a57-ac13-9909864e0428 | -12.66119 | -58.22056 | 2025-06-05 04:34:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9567353d-c9f1-39fc-b7ad-e7ec764b66b8 | -10.81147 | -56.95778 | 2025-06-05 04:34:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1d5bcee0-db3a-37dc-836f-1a09fe7153de | -13.51791 | -56.5759 | 2025-06-05 04:34:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 18.0 |
| c269115a-4da6-3ed1-ac86-151c71ac2744 | -9.21897 | -48.85871 | 2025-06-05 04:34:00 | NOAA-21 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 87264780-02d0-3d85-8dd7-5d9cc3829575 | -10.94497 | -55.32734 | 2025-06-05 04:34:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 02ada7fd-0ef9-3584-90c9-d29b02bc650b | -9.39188 | -48.40607 | 2025-06-05 04:34:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b614d147-f67b-3695-b227-b1ecf472d3ca | -13.5076 | -56.58753 | 2025-06-05 04:34:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b144d9f8-d8ba-3901-b95e-4981101c2d0c | -13.5293 | -56.57195 | 2025-06-05 04:34:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a993c633-72ff-380d-a5dd-41aac46b82b7 | -9.35282 | -47.69126 | 2025-06-05 04:34:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 18978ff3-5b93-3185-a642-03a50d5f9984 | -18.71339 | -54.18481 | 2025-06-05 04:36:00 | NOAA-21 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ad789bb1-439f-3c93-9911-5efd89ca4d21 | -18.71623 | -54.18993 | 2025-06-05 04:36:00 | NOAA-21 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d79cf715-b06a-3a72-9dd8-c4643e192385 | -18.84703 | -53.61999 | 2025-06-05 04:36:00 | NOAA-21 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 15d582b2-007e-30a9-9e49-10056f2b56d6 | -18.84632 | -53.62419 | 2025-06-05 04:36:00 | NOAA-21 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d6a8ffb5-928a-332d-95d3-7de3968c3cae | -19.97102 | -44.21589 | 2025-06-05 04:36:00 | NOAA-21 | BETIM | MINAS GERAIS | Brasil | 3106705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 554b0e99-b151-39f2-af2e-0f3513a718f3 | -19.94787 | -47.55959 | 2025-06-05 04:36:00 | NOAA-21 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| fbee644f-c29f-3664-bad6-af80c1cf2e5e | -18.84561 | -53.62839 | 2025-06-05 04:36:00 | NOAA-21 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 34f011ad-f00f-3d71-84a6-352fd4d625e1 | -20.31216 | -45.58492 | 2025-06-05 04:36:00 | NOAA-21 | ARCOS | MINAS GERAIS | Brasil | 3104205 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 37a49072-e844-3bfa-9d72-4575d51e2c5c | -19.4415 | -54.77517 | 2025-06-05 04:36:00 | NOAA-21 | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8bfedd2c-fa61-3560-abb8-7dfec126f4bf | -18.84067 | -53.63617 | 2025-06-05 04:36:00 | NOAA-21 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 74c2d02d-0d6d-3c49-a7a9-d0bcedcc1851 | -18.84708 | -53.62297 | 2025-06-05 04:36:00 | NOAA-21 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 03fb8c39-0367-3be2-aea8-af89ac08e11b | -18.83929 | -53.62291 | 2025-06-05 04:36:00 | NOAA-21 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 063bb4fd-3737-34b9-ab47-b2ebc2ef1f42 | -19.4941 | -45.33871 | 2025-06-05 04:36:00 | NOAA-21 | MARTINHO CAMPOS | MINAS GERAIS | Brasil | 3140506 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 23e512c8-6f6d-3525-a0be-64c3eef3c206 | -16.56377 | -43.92405 | 2025-06-05 04:36:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dc3f89a2-dec0-3764-8e19-56f89553a9af | -18.84 | -53.61872 | 2025-06-05 04:36:00 | NOAA-21 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 53401c80-c4d4-3918-9a8f-9806e34e1b2e | -20.7659 | -46.77062 | 2025-06-05 04:36:00 | NOAA-21 | ITAÚ DE MINAS | MINAS GERAIS | Brasil | 3133758 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 9ca3883e-8e4e-3c38-aa4f-d2264353115e | -18.84352 | -53.61935 | 2025-06-05 04:36:00 | NOAA-21 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 4.6 |
| da5dc70e-88d0-3cb8-af4d-59b75472a669 | -18.83578 | -53.62228 | 2025-06-05 04:36:00 | NOAA-21 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 01e91088-d6f1-38c6-80ff-22148f339f9e | -18.84489 | -53.63261 | 2025-06-05 04:36:00 | NOAA-21 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e9e19ce0-8b0c-3bc0-8943-653180f68f7c | -18.83715 | -53.63551 | 2025-06-05 04:36:00 | NOAA-21 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 6.0 |
| d7010b60-11c4-377e-be48-d39761423fcb | -18.83787 | -53.63131 | 2025-06-05 04:36:00 | NOAA-21 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 1f6223b2-a5f8-3882-940a-33b5f4ae3dce | -18.83435 | -53.63066 | 2025-06-05 04:36:00 | NOAA-21 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cce86f8b-4093-3a24-8234-65f33c668984 | -18.85059 | -53.62362 | 2025-06-05 04:36:00 | NOAA-21 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 816d3b2e-2176-3aec-be11-6896ae58d297 | -19.06644 | -53.44287 | 2025-06-05 04:36:00 | NOAA-21 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |


[Clique aqui para ver as próximas entradas](README12.md)
