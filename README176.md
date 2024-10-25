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

## Dados Diários - Página 176

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3eda13a9-4654-3550-a2f3-3ab81da1277e | -9.12114 | -46.12685 | 2024-10-25 16:52:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 34.0 |
| 77401d58-020e-3322-9c79-353b3760d16f | -9.11812 | -46.13173 | 2024-10-25 16:52:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 34.0 |
| 13d640c1-9f2d-3620-bb00-676ce4b06341 | -9.07379 | -46.50761 | 2024-10-25 16:52:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 3231d1bf-d52e-3b8f-b121-c8d7e075194e | -9.07016 | -46.50832 | 2024-10-25 16:52:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| b38d25a4-9f40-37df-a204-a6ee65d7283a | -8.9601 | -46.77641 | 2024-10-25 16:52:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 8e2f5385-8825-36e8-b5c4-98200e89fb70 | -8.92111 | -46.82053 | 2024-10-25 16:52:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 49ecdbd6-0337-3c8b-ad76-96f3f800a96f | -8.91952 | -46.82148 | 2024-10-25 16:52:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 3ea194c6-0b3f-3ae3-aae7-a39ba5e037f3 | -8.90268 | -46.65206 | 2024-10-25 16:52:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| d9c58cc7-b051-3dec-8a30-fd7968c6d6b5 | -8.8254 | -47.15462 | 2024-10-25 16:52:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| bfc5aca4-f3cb-314a-91a2-db9136574075 | -8.77599 | -46.58924 | 2024-10-25 16:52:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 59.5 |
| bc9232b9-4d9b-3cfa-af5e-53f6f3f62710 | -8.77528 | -46.58496 | 2024-10-25 16:52:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 59.5 |
| f13bea4c-a2bb-3739-81b6-646f81193f7a | -8.77464 | -46.58434 | 2024-10-25 16:52:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 0fe77704-b2c3-3b05-95fe-ab8667e3972f | -8.77164 | -46.58558 | 2024-10-25 16:52:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| d7d8474b-cf41-3f63-acdc-af8762619793 | -8.771 | -46.58496 | 2024-10-25 16:52:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| eda73771-d0c1-3e45-b1a4-e149ad15ad2f | -8.77013 | -46.59899 | 2024-10-25 16:52:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 17.3 |
| 573b27c2-b362-3a76-87c2-35e6cbeaaf93 | -8.76942 | -46.59842 | 2024-10-25 16:52:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 3b7a72b8-9d9e-30ff-8050-41cbc14df145 | -8.768 | -46.58617 | 2024-10-25 16:52:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 32b5e1e3-9851-3ba3-9e00-490198c45c05 | -8.76736 | -46.58555 | 2024-10-25 16:52:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| d90cae7f-89f8-3238-9d50-db1a87d65c9f | -8.76441 | -46.59046 | 2024-10-25 16:52:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 357984d4-ed26-30fa-9b68-cd0cf474107c | -8.68903 | -47.05088 | 2024-10-25 16:52:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 4a5b87d7-604c-33a1-a2bc-eb3e680dea14 | -8.68613 | -47.05554 | 2024-10-25 16:52:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 10.1 |
| e018ce0c-9705-3c8a-8f7a-9ce313cc62c8 | -8.68547 | -47.05146 | 2024-10-25 16:52:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 8e9abc74-93aa-33e2-9c8e-f517c24bc112 | -8.68191 | -47.05202 | 2024-10-25 16:52:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c9508996-6c0b-34c1-854f-a7564849dd34 | -8.67875 | -47.07766 | 2024-10-25 16:52:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| d8de2802-ad46-3383-8941-7ecf8f240a5b | -8.64741 | -47.08693 | 2024-10-25 16:52:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 53.3 |
| 37e5ea78-2899-3951-bc6f-acda63ed6338 | -8.52835 | -46.98009 | 2024-10-25 16:52:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 1775f418-edf7-39e5-811c-bf5bd8bfacf4 | -8.52544 | -46.98478 | 2024-10-25 16:52:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f4c1b8a2-2720-3df4-a4ac-9f98ab077332 | -8.52477 | -46.98065 | 2024-10-25 16:52:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 3a350790-db8f-3d83-ba9a-ecbd8c42b575 | -8.41654 | -47.00629 | 2024-10-25 16:52:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 63f3ca39-44de-3cb2-93d8-937c117635b3 | -8.4085 | -46.61505 | 2024-10-25 16:52:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 0d1343e0-28b8-3381-9dd7-4aa46fe3cca4 | -8.40414 | -46.61131 | 2024-10-25 16:52:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| aa82895d-7448-3474-bb88-991c75400f60 | -8.40049 | -46.61189 | 2024-10-25 16:52:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| f917a83a-b69d-3d85-b521-da29d2431f59 | -8.38447 | -46.60561 | 2024-10-25 16:52:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 265d2606-4258-34c3-885e-2fa45b3ed7fa | -8.38082 | -46.60621 | 2024-10-25 16:52:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 8604774b-7ff2-34ef-8048-321fcf698d6d | -8.36399 | -46.61791 | 2024-10-25 16:52:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| e91ba8cb-5d07-3db7-8a91-a8a7a65b3441 | -8.35974 | -46.82628 | 2024-10-25 16:52:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 28dea3e7-32ca-3497-8424-39cbe934d9f1 | -8.35962 | -46.61416 | 2024-10-25 16:52:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| eee2f8e1-a1f5-3e11-bb04-c34a26f0799d | -8.35596 | -46.61473 | 2024-10-25 16:52:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 384b7571-9755-3b50-bb8d-859a35297354 | -8.35525 | -46.61041 | 2024-10-25 16:52:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 63a2c8fd-d858-33e6-b704-89615c8f157c | -8.29159 | -46.47187 | 2024-10-25 16:52:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 5f9a14ba-b790-39fd-8fee-7e9b18451f03 | -8.26521 | -46.96106 | 2024-10-25 16:52:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 65.6 |
| 0fe16d90-eea1-3c81-a633-e3162487990d | -8.26445 | -46.9101 | 2024-10-25 16:52:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| ce218059-12ed-3c80-aa40-296b9fbb429a | -8.26163 | -46.96173 | 2024-10-25 16:52:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 100.1 |
| 75c30b48-2fa9-3ef9-ab8d-1dee3908bfbd | -8.10454 | -46.75401 | 2024-10-25 16:52:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 68806dd9-a325-3819-ab46-9f015958f3a9 | -8.0448 | -46.47831 | 2024-10-25 16:52:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 50da76ed-5b60-38f1-b241-8feeabd5c80a | -8.04111 | -46.47892 | 2024-10-25 16:52:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 12.2 |
| cf69b8ee-e15e-3882-a18b-529ee784c9e5 | -7.89446 | -46.68371 | 2024-10-25 16:52:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 26.9 |
| a4fe82a0-0ee5-3a8d-8f21-990fbb2f595e | -9.22509 | -47.0455 | 2024-10-25 16:52:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 349add36-84b1-335f-8fb8-b1642bdfa1f4 | -1.89304 | -47.08187 | 2024-10-25 16:52:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 3aca4799-ccf8-37cc-9f83-90aaf1684a7c | -1.9055 | -47.07696 | 2024-10-25 16:52:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 898eefaa-7f89-350a-a8cd-d9a666975fd9 | -1.90317 | -47.08729 | 2024-10-25 16:52:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 69.9 |
| 79a7b8d9-54aa-3162-9f42-538fb59d820e | -1.90239 | -47.08242 | 2024-10-25 16:52:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 4d2ec074-da90-36d9-b944-287426963196 | -1.90162 | -47.07756 | 2024-10-25 16:52:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 1338bd91-feee-394f-ab86-dafb087e86d9 | -1.90155 | -47.08554 | 2024-10-25 16:52:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 217.1 |
| cc7c9ff0-5585-3c17-a6e2-ff346aa34c3c | -1.90084 | -47.0727 | 2024-10-25 16:52:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 6e6d9e2a-e943-3c23-afe9-ab3d71c16b1d | -1.9008 | -47.08066 | 2024-10-25 16:52:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 8665abf2-623d-3bd7-9154-c7cdefece9fa | -1.90006 | -47.07579 | 2024-10-25 16:52:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| a87a9140-69c5-3370-a349-d95add87c902 | -1.89929 | -47.08789 | 2024-10-25 16:52:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 267.9 |
| e055c8ed-fc57-3853-b47c-7847f9998963 | -1.89852 | -47.08303 | 2024-10-25 16:52:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 49.3 |
| 0ab6479a-f2a5-321f-b90c-4ab6730f103a | -1.89774 | -47.07816 | 2024-10-25 16:52:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 49.3 |
| f21892f3-d445-35b6-bfa2-b6bc9c65534b | -1.89767 | -47.08615 | 2024-10-25 16:52:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 217.1 |
| c4e9d4e9-a733-397f-b41c-204505d07a7a | -1.89692 | -47.08126 | 2024-10-25 16:52:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| fc636c00-59a6-3f5c-827d-f6a998db413b | -1.89464 | -47.08363 | 2024-10-25 16:52:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 49.3 |
| c3f30dc2-f4be-3656-a2b7-80272ec56f71 | -1.8923 | -47.06902 | 2024-10-25 16:52:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| eb693de2-fa75-3d0b-845f-bd49ca768147 | -1.74925 | -47.18653 | 2024-10-25 16:52:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| ce431f3f-e55d-337d-973a-5a6d9eb83918 | -1.7457 | -46.62822 | 2024-10-25 16:52:00 | NOAA-21 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| cc3eb904-8774-3ad0-9ead-fe003c1f3e6d | -1.67699 | -47.03529 | 2024-10-25 16:52:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 35.8 |
| 8e288d83-30b7-3d14-be9b-e71f93627468 | -1.66946 | -47.00911 | 2024-10-25 16:52:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 18.8 |
| fc54d4a9-526f-387b-b746-61916fd90dd5 | -1.66856 | -47.00623 | 2024-10-25 16:52:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 17.5 |
| 8309caa6-b274-310b-bd63-2e7da73549d1 | -1.62078 | -47.03386 | 2024-10-25 16:52:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 54179f66-cf69-36c4-9a6b-bfd35397b7fd | -1.61451 | -47.04491 | 2024-10-25 16:52:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 887dbfa9-5382-3113-b677-5c9e55d3ba49 | -1.6106 | -47.04551 | 2024-10-25 16:52:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| d2b239e9-5557-3a3d-ab44-9e3fb583153a | -1.94835 | -46.22033 | 2024-10-25 16:52:00 | NOAA-21 | JUNCO DO MARANHÃO | MARANHÃO | Brasil | 2105658 | 21 | 33 | nan | nan | nan | Amazônia | 14.6 |
| 559a935d-d829-3545-b829-72afb591bbcb | -1.65104 | -46.19145 | 2024-10-25 16:52:00 | NOAA-21 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 2d42ff86-cc23-380e-b914-c690416f7176 | -1.64843 | -46.19196 | 2024-10-25 16:52:00 | NOAA-21 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 5f8d6704-c839-3010-bbda-5bd35572f95f | -1.64786 | -46.18825 | 2024-10-25 16:52:00 | NOAA-21 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 20f06569-ec81-3795-925e-63e5b48d4ae0 | -1.64752 | -46.19581 | 2024-10-25 16:52:00 | NOAA-21 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| dae209e3-68d4-305b-8c04-55a4f81a7249 | -1.64692 | -46.1921 | 2024-10-25 16:52:00 | NOAA-21 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 01021771-9cae-32fb-b6b5-5766c319d291 | -1.64633 | -46.18841 | 2024-10-25 16:52:00 | NOAA-21 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| b48b4b34-7434-3a6f-96c3-cde5e404f308 | -1.64601 | -46.20377 | 2024-10-25 16:52:00 | NOAA-21 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 41.9 |
| fb5843c0-d95d-31eb-a9c6-026077fc104b | -1.64544 | -46.20005 | 2024-10-25 16:52:00 | NOAA-21 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| dab214cf-245b-3379-bcde-4d7439d81c12 | -1.64487 | -46.19633 | 2024-10-25 16:52:00 | NOAA-21 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| fdd0f822-1cbf-3b12-93d7-214d48d3bc8a | -1.64459 | -46.20387 | 2024-10-25 16:52:00 | NOAA-21 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 33.9 |
| d92beffd-b6c5-3641-950c-f3134c3b7582 | -1.6443 | -46.19262 | 2024-10-25 16:52:00 | NOAA-21 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 9f787064-837d-37ac-a258-8237ec8044dc | -1.64399 | -46.20016 | 2024-10-25 16:52:00 | NOAA-21 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 85a0c362-0cc3-363b-bb15-028ee01a6713 | -1.6434 | -46.19646 | 2024-10-25 16:52:00 | NOAA-21 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 9b18132b-9754-3609-beb3-44c6f56d50ff | -1.6428 | -46.19276 | 2024-10-25 16:52:00 | NOAA-21 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| e83276ac-6eb1-35d8-b6c5-15f3dee133d0 | -1.64189 | -46.20442 | 2024-10-25 16:52:00 | NOAA-21 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 5b6b7149-9275-3bf2-b2ee-831d0bd7925b | -1.64132 | -46.2007 | 2024-10-25 16:52:00 | NOAA-21 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| bd422e38-86a1-3844-8267-3840b67f5695 | -1.64075 | -46.19699 | 2024-10-25 16:52:00 | NOAA-21 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 9bf78920-d5e6-3e0b-b326-de2964638ff5 | -1.63663 | -46.19766 | 2024-10-25 16:52:00 | NOAA-21 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 848f7b00-81fc-302c-89d1-fd3521472d9e | -1.61139 | -46.35942 | 2024-10-25 16:52:00 | NOAA-21 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| de5b60c1-be4b-32d7-83c3-2fedf7c9aa16 | -1.60674 | -46.35643 | 2024-10-25 16:52:00 | NOAA-21 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 4e755850-a7c2-3b57-a1ab-a0ad23d37dd3 | -1.598 | -46.35408 | 2024-10-25 16:52:00 | NOAA-21 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 25e41cf7-aefe-360e-acb6-a9f24bd4dbbe | -3.58967 | -46.1282 | 2024-10-25 16:52:00 | NOAA-21 | SÃO JOÃO DO CARÚ | MARANHÃO | Brasil | 2111029 | 21 | 33 | nan | nan | nan | Amazônia | 4.9 |
| b87492d9-f626-39ac-b796-078300c3226e | -3.58808 | -46.08532 | 2024-10-25 16:52:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 669d099c-59e7-3926-8180-264abbd737b4 | -3.58693 | -46.12881 | 2024-10-25 16:52:00 | NOAA-21 | SÃO JOÃO DO CARÚ | MARANHÃO | Brasil | 2111029 | 21 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 46abbd95-4636-38f4-b09c-c04109441712 | -3.58565 | -46.12885 | 2024-10-25 16:52:00 | NOAA-21 | SÃO JOÃO DO CARÚ | MARANHÃO | Brasil | 2111029 | 21 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 53ed93ac-d1b0-3b41-87ec-b11b22de3cfa | -3.58404 | -46.06057 | 2024-10-25 16:52:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 2a0f44ac-6c7c-33f6-970d-dce38f8b7898 | -3.58001 | -46.06123 | 2024-10-25 16:52:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 8.8 |


[Clique aqui para ver as próximas entradas](README177.md)
