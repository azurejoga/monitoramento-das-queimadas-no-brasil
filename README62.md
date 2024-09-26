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

## Dados Diários - Página 62

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7e907373-986f-3d8b-b960-3680dfc1141c | -7.27542 | -46.61504 | 2024-09-26 04:06:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 92fe2d6f-0402-3d43-bebc-ae88ddcfbfe9 | -7.15519 | -45.68162 | 2024-09-26 04:06:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5fa197fb-8fc3-3e47-bd3a-c057d46a0941 | -7.14371 | -45.44396 | 2024-09-26 04:06:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8c0e1b27-61be-3b6d-a9a9-af933a62a21e | -7.1409 | -45.44162 | 2024-09-26 04:06:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e3b70477-f353-38a6-88c1-85a010038b67 | -7.0997 | -46.44416 | 2024-09-26 04:06:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 31a84a0c-0bb6-3e5f-81cb-b1fb00f211ea | -7.09572 | -46.44341 | 2024-09-26 04:06:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 0fb47559-b768-34b2-9326-b91f5b159de8 | -7.09514 | -46.44687 | 2024-09-26 04:06:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| bd6a74d4-a44a-3802-b06d-d8b6e61001da | -7.09172 | -46.44283 | 2024-09-26 04:06:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1cd60620-70a6-30af-9df8-0d88ea93eeb3 | -7.09113 | -46.44624 | 2024-09-26 04:06:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5a926f01-fa25-3123-bfc4-25586989b313 | -7.01711 | -46.17188 | 2024-09-26 04:06:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 69f7fe59-5762-3054-85a4-95a0cab0d672 | -7.01709 | -46.17462 | 2024-09-26 04:06:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 10ebf168-03e1-38af-a93e-14b57fdb6aed | -6.873 | -45.41681 | 2024-09-26 04:06:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f3c44a17-d088-3af0-a7db-804152ac7275 | -6.81125 | -46.46798 | 2024-09-26 04:06:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d40f8d24-95a6-3ef9-bb8b-231b2bbc7090 | -6.52577 | -46.55328 | 2024-09-26 04:06:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2d1b756e-e0b7-3be7-8d75-a013355123cd | -9.4778 | -46.47326 | 2024-09-26 04:06:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1984d5a4-d8c6-3f96-b35b-271fb0b6c420 | -10.13893 | -47.28798 | 2024-09-26 04:06:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 64711106-92ce-385b-94b4-4fe1907f9c55 | -10.13552 | -47.28368 | 2024-09-26 04:06:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9904a833-5eba-334a-9224-b6b4783739f3 | -10.85313 | -46.62974 | 2024-09-26 04:06:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0fbe0392-f408-3179-8a59-6472b4fb853d | -10.85023 | -46.63143 | 2024-09-26 04:06:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 00cffd48-b6b1-3615-bde0-e159ddce4c9c | -10.84931 | -46.62907 | 2024-09-26 04:06:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1023c964-c4b3-34c3-b2fa-1139a076b053 | -10.73857 | -47.54227 | 2024-09-26 04:06:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 48e24ad7-1f42-3cfd-9ac7-195abd57ce08 | -10.72533 | -47.38123 | 2024-09-26 04:06:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e5de3d7a-edfd-37cc-9490-a3f741cef1c9 | -10.7247 | -47.38478 | 2024-09-26 04:06:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a8e8e62b-bd4c-3d6f-adfc-e457f7c1331f | -10.72344 | -47.38419 | 2024-09-26 04:06:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 64b654e6-2612-305f-b46e-39c94c9b17c7 | -10.7207 | -47.38405 | 2024-09-26 04:06:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 56f5f1ca-80b4-367f-b993-184cece23d94 | -10.71824 | -47.39051 | 2024-09-26 04:06:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d8b859b9-0ffa-3a12-88c1-a70273d1d569 | -10.71363 | -47.3933 | 2024-09-26 04:06:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3e74851f-d53c-3cea-8748-89a1a68def15 | -10.19247 | -46.13458 | 2024-09-26 04:06:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2bd4cdb8-7946-3ba6-a514-c2a8cca6007d | -11.90434 | -47.16124 | 2024-09-26 04:06:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| bf33d252-5dbc-3f9f-9ee0-1b640053f216 | -11.88794 | -47.16343 | 2024-09-26 04:06:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2804443d-ab19-39f4-8cb9-d68578216760 | -11.80567 | -47.63384 | 2024-09-26 04:06:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a45b5638-e714-3255-ad73-ed1693b2c75b | -11.80167 | -47.63309 | 2024-09-26 04:06:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 93700c88-0b39-378d-bb68-e89e771baef0 | -11.79768 | -47.63234 | 2024-09-26 04:06:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2fd26881-ce39-35ca-ac4e-73112f573c9a | -11.67654 | -46.3411 | 2024-09-26 04:06:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7b9ad885-e4e6-37d5-b494-6a9e1a7130f2 | -11.67285 | -46.34035 | 2024-09-26 04:06:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 96ef46b6-d18b-3e41-a374-56f485910b97 | -11.66996 | -46.33491 | 2024-09-26 04:06:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 29dc81ed-7af8-306f-b0c5-b7c6dda6a0c3 | -11.66915 | -46.33957 | 2024-09-26 04:06:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 99de1235-649f-3827-8c9e-113c6032baaa | -11.66786 | -46.33755 | 2024-09-26 04:06:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 38414bd4-b409-3e73-ba97-85d4f381f392 | -11.66547 | -46.33879 | 2024-09-26 04:06:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 43127f40-10ee-3339-8a62-0cb92fdd1c37 | -11.66417 | -46.33675 | 2024-09-26 04:06:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b617e9ec-c086-39ef-bcdc-0cf9d842907a | -11.62792 | -46.43871 | 2024-09-26 04:06:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 86bfd7af-2a79-3445-9832-b47769a1d641 | -11.62419 | -46.438 | 2024-09-26 04:06:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 62e6701f-e166-3bc4-b439-d27e666880fc | -11.51674 | -47.42033 | 2024-09-26 04:06:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 31d3660c-a6b6-3f8d-9e24-44b1f4af0656 | -11.51279 | -47.41953 | 2024-09-26 04:06:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 87b95ef6-610c-30e6-ae92-943942f6b271 | -11.51189 | -47.42463 | 2024-09-26 04:06:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b084dece-46bf-35a7-877e-d17ae1342e8c | -11.50797 | -47.42367 | 2024-09-26 04:06:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bd05f7ea-f97f-3963-971c-552d011aac85 | -11.32243 | -46.31521 | 2024-09-26 04:06:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1da7571e-2f38-3219-935a-5802d61c6856 | -11.31871 | -46.31456 | 2024-09-26 04:06:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d879006a-3882-3df5-9910-62361542b44c | -11.31123 | -46.33615 | 2024-09-26 04:06:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 696036e3-8931-3892-884e-c499f736ff45 | -11.31049 | -46.34056 | 2024-09-26 04:06:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4e517100-fa46-3e1f-af4e-d4631f184d70 | -11.28835 | -46.28997 | 2024-09-26 04:06:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 55390d7d-a746-3795-ad0d-c15fb4eeeeb4 | -11.28539 | -46.28484 | 2024-09-26 04:06:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8d3a55ed-6c20-37e4-a5ba-f116838aaf29 | -11.27873 | -46.27895 | 2024-09-26 04:06:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 94ab0523-54c5-3792-90de-7d0d6525848d | -11.27578 | -46.27382 | 2024-09-26 04:06:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cd455b38-d769-3a81-a82b-22a793cb1abf | -11.27359 | -46.26419 | 2024-09-26 04:06:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 5a0a5136-f167-3997-bb8e-875b22f719b4 | -11.27283 | -46.26863 | 2024-09-26 04:06:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 4d67c0cd-f161-376f-a579-d025f80e764f | -11.26989 | -46.26346 | 2024-09-26 04:06:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 15be9c24-5bb8-315c-8026-28598087430d | -11.14354 | -46.18799 | 2024-09-26 04:06:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 86bfc8a6-5f74-3d48-81c2-464a20a65351 | -11.47904 | -47.31662 | 2024-09-26 04:06:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| fcc757a9-5ab7-3613-bdcb-f643cb404c4f | -11.47598 | -47.31078 | 2024-09-26 04:06:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| bce94d65-b6bf-321e-a5db-6e53bc8b83a5 | -11.47556 | -47.28952 | 2024-09-26 04:06:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2487dfce-626d-349d-b028-bb21fdc67e87 | -11.4751 | -47.3159 | 2024-09-26 04:06:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 6aefbda1-b78a-3a6b-b8f7-11666042c159 | -11.47468 | -47.29465 | 2024-09-26 04:06:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b35e9bcf-322b-3124-9ec6-25fe392797b8 | -11.4738 | -47.29979 | 2024-09-26 04:06:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 099c4d1f-49b1-351c-b3a5-1f58dbc85b7c | -11.47292 | -47.30492 | 2024-09-26 04:06:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| cc3a4095-0fbd-37e6-b58d-5e45f8a66101 | -11.47162 | -47.28879 | 2024-09-26 04:06:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7543f0a2-8948-3cc9-811d-a9db3ffd1bcf | -11.47116 | -47.31518 | 2024-09-26 04:06:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5a7012af-edcd-3709-a235-52bb1912dcb2 | -11.47028 | -47.3203 | 2024-09-26 04:06:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| be12cc2f-8158-3fa4-b1f5-065dc9b491ad | -11.46986 | -47.29907 | 2024-09-26 04:06:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6082e44b-e1f3-3304-a407-67238961b37d | -11.46898 | -47.30421 | 2024-09-26 04:06:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 105e20f5-c350-3f03-bdfb-4967e755a5f5 | -11.46852 | -47.33052 | 2024-09-26 04:06:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1fb51fd6-949b-3a16-8acc-1c499cfd389b | -11.46546 | -47.3247 | 2024-09-26 04:06:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| cbf0c18a-afb7-3826-a08e-ddd83382af10 | -11.46458 | -47.32981 | 2024-09-26 04:06:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ed54c11a-766b-3a9c-b862-7be50853a64e | -11.46063 | -47.32909 | 2024-09-26 04:06:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 06178a20-3b92-37ed-8db1-14f3890a5ecb | -11.45056 | -47.31669 | 2024-09-26 04:06:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 47cfb5d2-734a-39fc-b65f-efc351aa1bf1 | -11.44051 | -47.30428 | 2024-09-26 04:06:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4bf84144-7ebf-3980-bf2f-4b7bf55f8492 | -11.43963 | -47.30939 | 2024-09-26 04:06:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5d84adc2-dd20-34f7-a69f-e81620441dbb | -11.43658 | -47.30354 | 2024-09-26 04:06:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d6a26090-d19f-3020-843b-79f1af067cf1 | -11.43569 | -47.30865 | 2024-09-26 04:06:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 86f56b4e-e601-3598-8cd2-20248d264982 | -11.43264 | -47.30279 | 2024-09-26 04:06:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6bd94df0-3008-3c66-83cd-f35ffab2e43e | -11.43175 | -47.3079 | 2024-09-26 04:06:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c6e056b8-b330-36ea-a63b-a82c75e241fc | -11.42351 | -47.28527 | 2024-09-26 04:06:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| abe04e47-8ba1-3381-ac49-c6a9f9200370 | -11.42261 | -47.2904 | 2024-09-26 04:06:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 26260e43-3b06-3d07-8493-35b1e57f830f | -11.28196 | -47.00983 | 2024-09-26 04:06:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ad9d531e-fd58-36d0-87c8-c03c90f73c80 | -11.28111 | -47.01476 | 2024-09-26 04:06:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8979be05-005c-3653-b9f8-c309e5c72879 | -11.27892 | -47.00424 | 2024-09-26 04:06:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a4a3dcbf-ed24-39af-b387-2bd50baa3595 | -11.27722 | -47.0141 | 2024-09-26 04:06:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 784adf25-8889-39d3-9bef-1209e064738e | -11.24975 | -47.4587 | 2024-09-26 04:06:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c508ba8d-f0cb-324b-baf5-d7b21cfcb4c4 | -6.08964 | -47.67346 | 2024-09-26 04:06:00 | NOAA-20 | MAURILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1712801 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 055a9951-3995-3597-ab9b-5ea942788bf3 | -6.0889 | -47.67787 | 2024-09-26 04:06:00 | NOAA-20 | MAURILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1712801 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| efcfed8c-ee37-3925-91fb-69613fa45779 | -6.08817 | -47.68225 | 2024-09-26 04:06:00 | NOAA-20 | MAURILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1712801 | 17 | 33 | nan | nan | nan | Cerrado | 0.1 |
| 20350e44-2c7e-3893-8f86-db12872ddffa | -5.81971 | -47.66655 | 2024-09-26 04:06:00 | NOAA-20 | ITAGUATINS | TOCANTINS | Brasil | 1710706 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9db8a8b9-cda6-3865-9bf7-55e249d81860 | -5.73736 | -47.46109 | 2024-09-26 04:06:00 | NOAA-20 | GOVERNADOR EDISON LOBÃO | MARANHÃO | Brasil | 2104552 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d72cba02-4982-35e8-84a7-fcc88f762cc7 | -6.05225 | -46.9352 | 2024-09-26 04:06:00 | NOAA-20 | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0f4fee9b-6470-35d4-a416-5c01f2c11acd | -6.04806 | -46.9345 | 2024-09-26 04:06:00 | NOAA-20 | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 5bc5bfbb-90dc-3a88-a59d-9d9286c093ba | -6.0474 | -46.93839 | 2024-09-26 04:06:00 | NOAA-20 | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ed4f4817-d468-3710-a86e-100dbc89f713 | -6.33836 | -46.90642 | 2024-09-26 04:06:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4fe2b6fa-f89f-329d-9c2e-93b4e21dbf52 | -6.33419 | -46.90574 | 2024-09-26 04:06:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 73125b8c-1a61-35e7-a637-c56ffab967bb | -7.42505 | -47.86682 | 2024-09-26 04:06:00 | NOAA-20 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a10f9d67-5c07-3f5a-9698-155e88a1d1e1 | -7.3161 | -47.41497 | 2024-09-26 04:06:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |


[Clique aqui para ver as próximas entradas](README63.md)
