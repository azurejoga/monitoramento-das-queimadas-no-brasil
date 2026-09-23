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
| 1c3673ff-a958-3eaf-ae17-e4df166f217b | -5.28827 | -47.26283 | 2026-09-23 00:03:00 | TERRA_M-M | SÃO FRANCISCO DO BREJÃO | MARANHÃO | Brasil | 2110856 | 21 | 33 | nan | nan | nan | Amazônia | 30.9 |
| 98689c78-ce43-32cf-a0ed-3f7466813af4 | -2.6283 | -48.48349 | 2026-09-23 00:03:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| a1e67ca0-19d6-304b-8728-f034a0184927 | -3.15286 | -57.70354 | 2026-09-23 00:03:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 31.4 |
| 48f82aa9-0e38-3e80-984a-de24cd455fca | -5.56691 | -52.02522 | 2026-09-23 00:03:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| beccb5cf-0742-354a-9f9d-fcd3c383bbe5 | -5.19321 | -50.08922 | 2026-09-23 00:03:00 | TERRA_M-M | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 286e1ec7-2168-3cf0-97de-78fdf9d62e04 | -6.64424 | -50.93548 | 2026-09-23 00:03:00 | TERRA_M-M | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 94278911-36e8-3159-8e3e-27c40b800a64 | -5.89711 | -52.09988 | 2026-09-23 00:03:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 20.4 |
| ec73bce5-dc08-372d-a7d8-16751b752ae1 | -6.66447 | -50.87978 | 2026-09-23 00:03:00 | TERRA_M-M | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| b0ccfa72-29a1-3bbd-8172-16186bab36aa | -4.74305 | -48.04208 | 2026-09-23 00:03:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 32.5 |
| b0cf8af5-f530-3f60-93f4-4b1ca9d2f68e | -6.11397 | -57.69119 | 2026-09-23 00:03:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 26.2 |
| 8cf08e01-bd2c-35d4-9d25-5a762b9d66d1 | -5.2772 | -47.25364 | 2026-09-23 00:03:00 | TERRA_M-M | SÃO FRANCISCO DO BREJÃO | MARANHÃO | Brasil | 2110856 | 21 | 33 | nan | nan | nan | Amazônia | 14.6 |
| c7dbdce1-06a1-31f5-ba7e-755b30644bbb | -3.57597 | -51.94838 | 2026-09-23 00:03:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| a378dfde-c24b-390f-8e09-71bdf6d722d1 | -4.57924 | -45.66292 | 2026-09-23 00:03:00 | TERRA_M-M | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 34.5 |
| 517a38a6-284d-3ea3-b43e-cb2333b3bf7f | -2.96749 | -50.40099 | 2026-09-23 00:03:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 8fae32da-4dcd-3cac-ad66-9a7b3fb33838 | -3.98259 | -52.09367 | 2026-09-23 00:03:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 41740a42-0f08-3e16-a8c7-6fe27dd9cd98 | -3.80049 | -52.36811 | 2026-09-23 00:03:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 1abb63e6-9150-391a-832c-4eae98160a24 | -5.87615 | -52.05661 | 2026-09-23 00:03:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| b9f9f2cd-eceb-309c-aad4-9abb48e7e534 | -2.63078 | -51.70209 | 2026-09-23 00:03:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| acbc8636-0a79-305c-afb8-d4879654f78f | -5.80481 | -52.09741 | 2026-09-23 00:03:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| c62f79cb-a9a3-31cd-b804-7fc4b59ceaf4 | -6.67875 | -58.5698 | 2026-09-23 00:03:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 61.2 |
| 5be82bf4-a66c-3960-8f7a-4988d861ae92 | -4.22418 | -48.61782 | 2026-09-23 00:03:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 23.8 |
| e4998c1a-13ba-3e11-93f4-28bfe3f0aaf5 | -3.82056 | -52.40002 | 2026-09-23 00:03:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 9a62a007-0bae-34aa-a8e4-af1aa5b69119 | -2.45603 | -49.2246 | 2026-09-23 00:03:00 | TERRA_M-M | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 15.3 |
| ab0a8fdf-317e-3c93-93ff-8c7fc8e899f0 | -3.62302 | -51.47918 | 2026-09-23 00:03:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 6bb5a77d-0620-3eec-b5eb-0f803a746612 | -6.67443 | -50.95399 | 2026-09-23 00:03:00 | TERRA_M-M | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 3d69a68a-b35f-3a0f-96a9-468994262a34 | -6.37921 | -55.28254 | 2026-09-23 00:03:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 30.6 |
| affe248a-7cd0-3ce0-91f3-1bcbae6e31e1 | -6.43288 | -48.45701 | 2026-09-23 00:03:00 | TERRA_M-M | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 23.7 |
| ad7c301f-2bec-3645-8267-fcf664dc6a8b | -5.6216 | -45.23416 | 2026-09-23 00:03:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 35.3 |
| 0a571124-2395-3596-8970-6d01e8ab26d3 | -2.24291 | -48.75422 | 2026-09-23 00:03:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 22.3 |
| ac751f55-dada-327c-8891-f1e4e3232e1f | -5.28678 | -47.2523 | 2026-09-23 00:03:00 | TERRA_M-M | SÃO FRANCISCO DO BREJÃO | MARANHÃO | Brasil | 2110856 | 21 | 33 | nan | nan | nan | Amazônia | 33.2 |
| f55c24ee-aba8-3160-be6e-9345690fe3b3 | -3.24001 | -47.25126 | 2026-09-23 00:03:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| b7178106-6085-3961-bb6e-3bb9badf9435 | -6.59556 | -51.32271 | 2026-09-23 00:03:00 | TERRA_M-M | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | 30.7 |
| 6b93917d-12fe-3420-8bb1-ec3954ba8397 | -4.42669 | -55.08332 | 2026-09-23 00:03:00 | TERRA_M-M | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 15.4 |
| f1785d7a-3790-3ecf-b4a3-b331424749bc | -4.2216 | -50.66046 | 2026-09-23 00:03:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 3f780b06-11ff-329c-ad2c-8627edd0d11f | -2.66471 | -48.33886 | 2026-09-23 00:03:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 127069e0-2e30-3187-ab54-598e9c41de9f | -5.87334 | -52.03606 | 2026-09-23 00:03:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 15629233-1979-3a91-a3b3-13834f79bfca | -4.27849 | -48.61023 | 2026-09-23 00:03:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 26.0 |
| 7bbac4c8-17d4-3ec6-9be5-fbee30e642a4 | -5.87754 | -52.06682 | 2026-09-23 00:03:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| e4108cc4-f4e9-387c-852c-a19480319648 | -7.57112 | -57.69376 | 2026-09-23 00:03:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 22.3 |
| b8861e3e-82bb-34ed-b2c7-fbf7680cf3f6 | -6.52957 | -51.5145 | 2026-09-23 00:03:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 0bdec836-5b3f-345a-b163-af91ddd1a661 | -5.14033 | -50.04913 | 2026-09-23 00:03:00 | TERRA_M-M | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 54a11978-985b-3c57-a94f-018490c422a8 | -5.56821 | -42.74358 | 2026-09-23 00:03:00 | TERRA_M-M | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 26.3 |
| 6f231d39-8597-3e79-9115-be7cd419efa8 | -5.77707 | -47.15433 | 2026-09-23 00:03:00 | TERRA_M-M | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 74.7 |
| f9b1f6be-a823-3ada-b7a2-be1d57e7fcef | -6.59686 | -51.33229 | 2026-09-23 00:03:00 | TERRA_M-M | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 3d12aa5e-a978-3f36-aebf-2fefa6a69ffb | -2.94435 | -50.49347 | 2026-09-23 00:03:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| d388e50a-37c1-36b2-91ba-71954a03367d | -2.1636 | -48.18555 | 2026-09-23 00:03:00 | TERRA_M-M | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 6ad77c86-3666-32c7-8d75-1efb2176f15a | -4.87159 | -55.85133 | 2026-09-23 00:03:00 | TERRA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 23.5 |
| 6fda25d5-31c9-3e3d-9075-5cd7f987a74e | -5.60208 | -45.95293 | 2026-09-23 00:03:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 18.0 |
| 6cfadd10-0431-3828-8844-a01dca29046e | -2.9625 | -54.08918 | 2026-09-23 00:03:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 23.5 |
| 9cf70b60-e878-3e06-b6d2-02a0b50d7add | -2.24158 | -48.74469 | 2026-09-23 00:03:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 26.3 |
| a5f34a54-8937-3f52-aa20-ab0829ef51bf | -6.2153 | -47.50478 | 2026-09-23 00:03:00 | TERRA_M-M | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 95bed400-c7a6-3a09-804e-2d34afa50f02 | -6.73464 | -59.44481 | 2026-09-23 00:03:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 47.7 |
| d44129c5-65a1-347a-99f2-8154bea3ab62 | -5.28726 | -60.20573 | 2026-09-23 00:03:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 35.6 |
| 44bc60ad-a096-33a7-9ca5-cddc6075d80b | -5.87474 | -52.0463 | 2026-09-23 00:03:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 870c45a2-2c8a-3cf8-ac2f-54b484a599bf | -6.30217 | -57.7385 | 2026-09-23 00:03:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 34.6 |
| b4f912f5-84fb-3785-8af5-ce19f1a089f3 | 0.34007 | -51.08715 | 2026-09-23 00:03:00 | TERRA_M-M | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 9376ebb0-9292-3ff5-a733-d81bf4212804 | -6.98685 | -52.85802 | 2026-09-23 00:03:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 8a6ad1aa-0a90-39f8-9757-c46a199eac01 | -5.82788 | -52.19902 | 2026-09-23 00:03:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 4e2d9cea-5a25-329a-9317-faf1b442a889 | -4.45264 | -55.02704 | 2026-09-23 00:03:00 | TERRA_M-M | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 149f252f-3dac-3ac3-a4c6-a815a7dd1d81 | -6.44313 | -48.46494 | 2026-09-23 00:03:00 | TERRA_M-M | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 1a42efcc-8ac7-3860-b16b-0a460187db65 | -3.86443 | -58.83434 | 2026-09-23 00:03:00 | TERRA_M-M | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 43.9 |
| 413ed553-c1d9-34b3-8359-fd343a1553ca | -3.70038 | -60.56102 | 2026-09-23 00:03:00 | TERRA_M-M | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 38.4 |
| b92741f8-8c6f-3f9f-9ded-18d9f60b473f | -4.7417 | -48.03239 | 2026-09-23 00:03:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 36.6 |
| 674d0486-5943-347d-b440-12d3895719f2 | -2.73881 | -51.55091 | 2026-09-23 00:03:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 37c1c414-503c-3962-9402-04f96a95986d | -2.40816 | -48.16367 | 2026-09-23 00:03:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 68bd43a5-dade-307c-bb84-9ffa8549bdc6 | -3.46009 | -59.5705 | 2026-09-23 00:03:00 | TERRA_M-M | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 63.7 |
| 2e5eed75-1c0c-3ff9-ae20-1505a73e4d23 | -7.56768 | -57.66559 | 2026-09-23 00:03:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 19.0 |
| 5604d1a2-966f-3652-8bd0-9ba1765dc43d | -3.84511 | -51.75806 | 2026-09-23 00:03:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 4e4d0942-0ffb-3b51-b8ea-67aea8170a7d | -2.87994 | -54.0816 | 2026-09-23 00:03:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 01060aef-4855-3489-98ee-b4467b12ff19 | -1.05524 | -47.35888 | 2026-09-23 00:03:00 | TERRA_M-M | NOVA TIMBOTEUA | PARÁ | Brasil | 1505007 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 1f9042de-c651-3123-a656-45bcaa0ad3ca | -6.20597 | -47.5062 | 2026-09-23 00:03:00 | TERRA_M-M | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 4c3e1a23-0de4-312c-b993-006b31499c7a | -4.32175 | -55.42993 | 2026-09-23 00:03:00 | TERRA_M-M | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 0e691707-7543-3b3a-be45-6d90b40d1b8c | -3.86029 | -58.80402 | 2026-09-23 00:03:00 | TERRA_M-M | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 23.5 |
| f4a1e659-9dd6-3555-a4f5-83b5080e2b3d | -6.06048 | -46.35492 | 2026-09-23 00:03:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 1ef21d99-95a1-3c85-96ce-ad1f274f5dd6 | -2.64094 | -54.78807 | 2026-09-23 00:03:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| d77dce37-48f0-3c86-9877-47456ec232e3 | -6.12412 | -57.7716 | 2026-09-23 00:03:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 45.5 |
| 598839ae-5609-30df-b1d9-fcab1e5bf2ba | -5.52511 | -47.70438 | 2026-09-23 00:03:00 | TERRA_M-M | SÃO MIGUEL DO TOCANTINS | TOCANTINS | Brasil | 1720200 | 17 | 33 | nan | nan | nan | Cerrado | 11.1 |
| b4195320-00e4-3b3d-b909-91b30d73680e | -3.93361 | -42.98139 | 2026-09-23 00:03:00 | TERRA_M-M | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 33.0 |
| 1d262359-7eaa-300d-bf1f-aa91ebd64f26 | -5.76314 | -45.0986 | 2026-09-23 00:03:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 33.7 |
| b337864f-b022-3b12-b5f3-b96c12a9ff95 | -3.51551 | -51.6377 | 2026-09-23 00:03:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 310f6059-a15b-3c9c-a947-ae142f2c79df | -5.77158 | -43.75859 | 2026-09-23 00:03:00 | TERRA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 32.5 |
| ea6dfff2-100c-3493-b239-2308340afde9 | -6.88457 | -55.32368 | 2026-09-23 00:03:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| e768d457-a05b-399f-974f-65735989366e | -6.62461 | -59.91536 | 2026-09-23 00:03:00 | TERRA_M-M | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 66.3 |
| e8676515-ee85-36c0-9ce1-77869d76811d | -2.74777 | -51.54968 | 2026-09-23 00:03:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 86b6df04-ebe0-3195-9e6d-47d3ee7453af | -5.75418 | -45.1145 | 2026-09-23 00:03:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 29.7 |
| 98b924c1-dc8e-367e-a8d8-c8b306c118c3 | -6.12729 | -52.77086 | 2026-09-23 00:03:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 2b23d149-611f-3c2a-b4cf-f92c951d8811 | -2.45953 | -57.92266 | 2026-09-23 00:03:00 | TERRA_M-M | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 69.2 |
| dfed6f4a-f9ed-35a5-be56-ec03d8aeb17c | -3.00721 | -54.18493 | 2026-09-23 00:03:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| d6f9c378-8131-3c99-9f5a-225288a02bf8 | -2.45475 | -49.21547 | 2026-09-23 00:03:00 | TERRA_M-M | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 21.6 |
| 2b42d35d-371f-3ddf-b042-18b40dc3466e | -6.04094 | -53.26814 | 2026-09-23 00:03:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| e4500863-2881-3ac0-90d5-9d354346443e | -6.04013 | -53.27478 | 2026-09-23 00:03:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 18.4 |
| a4db5f95-6ba9-3ed8-9d16-c95d7c809b5b | -3.04148 | -50.26832 | 2026-09-23 00:03:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 208fa082-acb9-3b30-a9b4-330f7887196e | -3.66476 | -53.45988 | 2026-09-23 00:03:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 7f2b138a-6081-3dcb-ac0e-57d2dfdee718 | -6.45392 | -59.98305 | 2026-09-23 00:03:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 44.8 |
| c0ba5002-5cc0-32d2-9c2a-7fc6aad4adc9 | -6.18318 | -52.80317 | 2026-09-23 00:03:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 18.8 |
| 217fe270-fe1c-3836-94d6-26ed1e5e8811 | -5.35733 | -45.16055 | 2026-09-23 00:03:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 26.0 |
| 6169ae7a-eb95-3efe-84a1-7b97db4fbe3f | -6.1767 | -52.05431 | 2026-09-23 00:03:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| f511b3ed-386d-3da8-bc2e-15135455c774 | -5.81029 | -47.76539 | 2026-09-23 00:03:00 | TERRA_M-M | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 207a2434-d321-3165-a64f-bb3398999a23 | -4.44721 | -55.07494 | 2026-09-23 00:03:00 | TERRA_M-M | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 70.3 |
| 90ff085e-b938-3d93-bccb-67bdb67af7ff | -2.10523 | -49.69068 | 2026-09-23 00:03:00 | TERRA_M-M | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 28.4 |


[Clique aqui para ver as próximas entradas](README6.md)
