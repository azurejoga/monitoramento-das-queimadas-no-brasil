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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c7c1656a-53f2-3425-9cdb-6b12e1b34160 | -4.10902 | -48.02953 | 2025-10-22 00:16:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| e160db8a-1cd6-3f75-9d02-0d529640e20c | -4.70482 | -48.13157 | 2025-10-22 00:16:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 17ba6ef5-0b4d-38f9-b0d9-99f03222ef5c | -4.21273 | -48.79413 | 2025-10-22 00:16:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 24.1 |
| 01cfb133-dda9-34dc-a24b-c8b282f96394 | -3.82093 | -47.40574 | 2025-10-22 00:16:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 28e27dc9-f98e-3209-b58f-29cc9ee58e34 | -4.4711 | -49.10915 | 2025-10-22 00:16:00 | TERRA_M-M | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 17.2 |
| bfe56eb8-1da6-309d-8a32-d801971b0947 | -3.36351 | -45.41349 | 2025-10-22 00:16:00 | TERRA_M-M | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 55f8485a-61ee-36ae-9775-99e8f42d40a9 | -2.44329 | -47.16216 | 2025-10-22 00:16:00 | TERRA_M-M | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 0c5c916a-1ee7-38ac-a774-539ca324f85c | -2.95045 | -49.34328 | 2025-10-22 00:16:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 31.2 |
| 46fbd886-837c-3c04-9d26-5e96d929a402 | -4.22764 | -47.21933 | 2025-10-22 00:16:00 | TERRA_M-M | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 8.0 |
| d262ea2e-a7b4-36f1-8129-a9d36ce4be62 | -3.32037 | -45.70327 | 2025-10-22 00:16:00 | TERRA_M-M | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 109eeb20-e55f-356e-84bd-3eb54f378370 | -4.4752 | -49.0899 | 2025-10-22 00:16:00 | TERRA_M-M | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 27.6 |
| db7c4478-e5fc-3d22-9780-14519ec99659 | -3.70625 | -47.63565 | 2025-10-22 00:16:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| ad34ad91-5b67-3e99-8892-4a3c6790bea6 | -2.94643 | -49.33756 | 2025-10-22 00:16:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 16.9 |
| ddf2384a-877f-3fe5-b590-7b7e29f9ccf9 | -2.95873 | -48.58846 | 2025-10-22 00:16:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 23691453-3fd3-3aa9-a57e-6639bbe66ab2 | -3.94253 | -48.08617 | 2025-10-22 00:16:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| f97771ff-18af-3d04-886b-f3350b8f28b4 | -4.22633 | -47.20962 | 2025-10-22 00:16:00 | TERRA_M-M | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 46550c33-f676-3a07-b6a5-720ccd80e899 | -4.46937 | -49.09655 | 2025-10-22 00:16:00 | TERRA_M-M | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 68.3 |
| a6af7654-8b2a-3942-89a9-98b251de9c16 | -2.93021 | -48.3039 | 2025-10-22 00:16:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 39.7 |
| 3fe69999-560f-3ece-b0a0-f831223f83fc | -2.2538 | -51.94377 | 2025-10-22 00:16:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 15.5 |
| 8fcda8f3-9d58-3d61-a42e-dc7f508dccdf | -4.47685 | -49.10252 | 2025-10-22 00:16:00 | TERRA_M-M | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 51.1 |
| f30a3df3-f751-3688-9429-26429b3e0e18 | -3.44265 | -41.83754 | 2025-10-22 00:16:00 | TERRA_M-M | CAXINGÓ | PIAUÍ | Brasil | 2202653 | 22 | 33 | nan | nan | nan | Caatinga | 7.2 |
| f4e42b01-7798-3f04-929c-5b4ed3ae24e0 | -2.94807 | -49.34989 | 2025-10-22 00:16:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 18.2 |
| e3341dce-ed57-3f85-b824-b7abf8e2e7d7 | -3.45463 | -41.84811 | 2025-10-22 00:16:00 | TERRA_M-M | CAXINGÓ | PIAUÍ | Brasil | 2202653 | 22 | 33 | nan | nan | nan | Caatinga | 39.3 |
| 0aa95c12-b878-3e2b-823a-ee72639f3e16 | -3.82227 | -47.41559 | 2025-10-22 00:16:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 755dc5ca-7eb6-3ad7-96e5-b8864b521280 | -2.60899 | -45.02971 | 2025-10-22 00:16:00 | TERRA_M-M | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 8.5 |
| b57b7fe4-b920-3fc7-a263-d7e8ad05ba3d | -3.44438 | -41.84969 | 2025-10-22 00:16:00 | TERRA_M-M | CAXINGÓ | PIAUÍ | Brasil | 2202653 | 22 | 33 | nan | nan | nan | Caatinga | 72.2 |
| 9549922c-bd00-3609-82f6-a4f03411f5d6 | -3.40283 | -46.90491 | 2025-10-22 00:16:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 12556d03-f5a2-3610-b686-11b546f29294 | -3.96555 | -49.00596 | 2025-10-22 00:16:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| de85475a-538d-39af-aad1-a6c98185004f | -3.52207 | -49.44183 | 2025-10-22 00:16:00 | TERRA_M-M | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 70.4 |
| 76d29060-53fc-30dd-8147-89e05a77697e | -3.52377 | -49.45471 | 2025-10-22 00:16:00 | TERRA_M-M | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 45.8 |
| 606cfe04-59dc-3a09-a5d3-3f3ada7ab556 | -3.40138 | -44.55648 | 2025-10-22 00:16:00 | TERRA_M-M | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 62a10bc6-ea34-3065-ba30-43e7f9068c6c | -3.81212 | -50.76954 | 2025-10-22 00:16:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 43.4 |
| 94ae45e2-aad1-39ba-aafd-d0e1e21887f9 | -4.60398 | -46.59578 | 2025-10-22 00:16:00 | TERRA_M-M | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 47adfcf0-12db-3603-a1ac-43bc42d3bd24 | -3.82394 | -50.76805 | 2025-10-22 00:16:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 6c76266d-1948-3b9d-a7e2-c93993607927 | -3.2492 | -48.77194 | 2025-10-22 00:16:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 5b8838e3-7a67-35f8-a238-55ce8bf1fc25 | -2.9899 | -48.74456 | 2025-10-22 00:16:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 2fc6a4a4-60fc-37ca-954e-fb93f04e25f5 | -3.3623 | -45.40471 | 2025-10-22 00:16:00 | TERRA_M-M | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 18.9 |
| fc563278-3e1e-3b2c-a2f8-6bfee89d8a44 | -3.66762 | -50.28413 | 2025-10-22 00:16:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 17.3 |
| fdc4c4c7-b777-3795-bef9-807c9d4caa87 | -3.31915 | -45.69448 | 2025-10-22 00:16:00 | TERRA_M-M | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 9.3 |
| fc0eff9f-f496-3355-962b-992bf6af78cb | -4.61303 | -46.59459 | 2025-10-22 00:16:00 | TERRA_M-M | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 5.0 |
| e3ec6c9b-b69a-3945-aab7-5dfab1bf616c | -2.60776 | -45.02085 | 2025-10-22 00:16:00 | TERRA_M-M | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 9ea9c004-0a3c-358f-9606-95881b062e1d | -4.4066 | -43.3118 | 2025-10-22 00:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 57.7 |
| 29ebdd1d-a647-38d0-abd2-72271a828c9d | -9.0221 | -65.9407 | 2025-10-22 00:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 95.5 |
| 53aaab7a-eb64-38c8-ab04-ea0190850822 | -16.1782 | -49.9549 | 2025-10-22 00:20:00 | GOES-19 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 91.2 |
| 4cca7286-6e95-304a-b247-1d3f78f29d4e | -9.0036 | -65.9412 | 2025-10-22 00:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 119.8 |
| 94620d1a-8f69-3a34-8ac5-c3310752e13f | -9.0222 | -65.922 | 2025-10-22 00:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 111.9 |
| 6c5a08bf-775e-3e88-89ea-c16599ffcb6f | -9.0036 | -65.9226 | 2025-10-22 00:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 196.8 |
| 5fbdfb31-8e19-3102-b07b-e5c55df7f409 | -2.2527 | -51.9108 | 2025-10-22 00:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 47.8 |
| ef27e6ff-77ce-31a2-a3a6-042f1159c97e | -4.4806 | -49.0936 | 2025-10-22 00:20:00 | GOES-19 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 77.3 |
| c9c8f49f-ce68-3864-8f31-3f73ad26c1cb | -3.824 | -50.7678 | 2025-10-22 00:20:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 67.5 |
| 5316793c-b1de-368a-a60b-5a187cc3b1ac | -16.1778 | -49.977 | 2025-10-22 00:20:00 | GOES-19 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 131.5 |
| 9097aaba-c326-30b3-8ba5-352a9debe357 | -4.388 | -43.2896 | 2025-10-22 00:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 56.0 |
| 54c02cb6-0d53-3940-9865-b5ae047e0537 | -16.1974 | -49.9737 | 2025-10-22 00:20:00 | GOES-19 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 89.4 |
| 0b714c38-3460-3e52-a822-ae2c10741d90 | -2.2527 | -51.9313 | 2025-10-22 00:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 55.3 |
| 3521066e-fa33-384e-a1de-01a75ee36546 | -9.0037 | -65.904 | 2025-10-22 00:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 68.8 |
| aff33ebf-dbf1-3104-bd16-b7e325cd70ac | -4.4067 | -43.2885 | 2025-10-22 00:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 49.3 |
| 505c437d-14b1-3207-867d-f5a6067fdc06 | -8.9851 | -65.9232 | 2025-10-22 00:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 64.3 |
| a4193263-4993-34b3-8139-2184280c8ce8 | -4.3879 | -43.3129 | 2025-10-22 00:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 64.4 |
| 1a96fa49-63bd-3000-9c46-0bea14fce20f | -9.0037 | -65.904 | 2025-10-22 00:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 65.9 |
| dab680f0-416e-39d7-906a-570792161a63 | -16.1778 | -49.977 | 2025-10-22 00:30:00 | GOES-19 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 169.8 |
| 17e909eb-e224-3a1b-b08a-9f7797dd5c9d | -16.1782 | -49.9549 | 2025-10-22 00:30:00 | GOES-19 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 66.0 |
| 28e60206-e139-32fd-b100-9fb7664bd7d9 | -9.0036 | -65.9412 | 2025-10-22 00:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 151.4 |
| 5c6d0efa-6f29-3495-a5e6-f47dd22ed099 | -9.0221 | -65.9407 | 2025-10-22 00:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 72.3 |
| 4027ab9d-965f-3f56-ad4f-c131a57e7760 | -9.0222 | -65.922 | 2025-10-22 00:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 84.3 |
| 370bc0ef-31b1-355d-b233-ddf6e03aa997 | -9.0036 | -65.9226 | 2025-10-22 00:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 208.9 |
| 08827e4f-17e6-30a9-addd-6c51c9e9f7f3 | -12.8139 | -48.6362 | 2025-10-22 00:30:00 | GOES-19 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 76.9 |
| f0f7d42e-c068-30c6-a007-7ec0065560e7 | -8.9851 | -65.9232 | 2025-10-22 00:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 60.2 |
| ee96894d-d9e9-3920-8cdf-2bbbc8d3129d | -13.4636 | -48.8314 | 2025-10-22 00:40:00 | GOES-19 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 64.0 |
| f358868a-5a6a-3893-a460-973b4cf11cf1 | -12.5404 | -51.3317 | 2025-10-22 00:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 68.7 |
| 1381728c-d7eb-35b7-a56f-35efd8c9600b | -9.0036 | -65.9412 | 2025-10-22 00:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 151.2 |
| 5e675033-aded-31a9-ab91-bacd885990f9 | -9.0221 | -65.9407 | 2025-10-22 00:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 68.2 |
| 4cf2c951-34e0-3aa9-a47a-cc89c87edb03 | -4.4806 | -49.0936 | 2025-10-22 00:40:00 | GOES-19 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 61.4 |
| 91779eec-b6cb-3b71-84f1-7a7bc937b7db | -12.5216 | -51.3127 | 2025-10-22 00:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 56.1 |
| 4b316ebb-b517-3732-aa74-aa48a82517b6 | -9.0036 | -65.9226 | 2025-10-22 00:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 217.4 |
| f64f9694-b8e7-3f58-bb66-58af30c3edeb | -9.0222 | -65.922 | 2025-10-22 00:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 79.6 |
| 7306d1c3-8e11-32f5-a667-4ddbcde87514 | -12.5213 | -51.334 | 2025-10-22 00:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 153.4 |
| a74199ab-d88b-3036-ad11-21456902d03f | -16.8845 | -49.9908 | 2025-10-22 00:40:00 | GOES-19 | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 86.2 |
| f06dc0fc-ed23-3f3c-8a45-30b0ee5eaf08 | -9.0037 | -65.904 | 2025-10-22 00:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 64.6 |
| 788d91e3-ce49-37f5-b789-ccac1b0b3599 | -9.0037 | -65.904 | 2025-10-22 00:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 63.6 |
| 10a4c5a2-b105-3eaa-8ad0-994940728c10 | -9.0221 | -65.9407 | 2025-10-22 00:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 68.6 |
| d0cb12ff-9f96-3c0a-8798-015dba77c0bc | -2.9291 | -48.2966 | 2025-10-22 00:50:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 50.5 |
| ab441010-e17f-355f-b56c-ea2e752ec005 | -16.8845 | -49.9908 | 2025-10-22 00:50:00 | GOES-19 | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 68.0 |
| 9fe5fc97-60ed-303b-94bb-82ccd360cb2d | -3.8056 | -50.7685 | 2025-10-22 00:50:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 52.9 |
| 3ca05a55-bde2-3664-95b0-39cc3150a11e | -9.0222 | -65.922 | 2025-10-22 00:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 80.6 |
| 266d231d-ab72-308c-9ff0-85917d64e583 | -9.0036 | -65.9412 | 2025-10-22 00:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 146.4 |
| bf0dd49d-1900-3a2a-9d01-764a4c90d300 | -9.0036 | -65.9226 | 2025-10-22 00:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 208.1 |
| 0a57d41b-6f2c-334e-8deb-892880ff2fd3 | -8.9851 | -65.9232 | 2025-10-22 01:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 70.4 |
| e7cebbb1-4b6b-31ff-8025-7babfc7995d1 | -3.824 | -50.7678 | 2025-10-22 01:00:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 53.2 |
| 3f4665fc-e93d-3f0c-bb5e-5a7d15389990 | -9.0221 | -65.9407 | 2025-10-22 01:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 68.5 |
| fe66ef15-11c9-3c1e-b314-a86aa33d245d | -3.8056 | -50.7685 | 2025-10-22 01:00:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 57.1 |
| 858e34e7-5064-3467-91f7-c62d0a1b08da | -5.066 | -40.475 | 2025-10-22 01:00:00 | GOES-19 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 63.4 |
| 00e805a3-ed16-3d85-975b-4db3a826cfba | -9.0036 | -65.9226 | 2025-10-22 01:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 187.1 |
| 1ffc97db-2e14-380b-835c-77e393f6e945 | -9.0222 | -65.922 | 2025-10-22 01:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 79.4 |
| 1856c3e6-071e-3878-9bfd-f34cfb0f690d | -9.0036 | -65.9412 | 2025-10-22 01:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 134.2 |
| 58a85835-ce0d-3eb5-98a4-b8ca52c2d4de | -9.0036 | -65.9226 | 2025-10-22 01:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 175.3 |
| b57728cc-b548-32e1-82c3-0fc4c6649e37 | -9.0221 | -65.9407 | 2025-10-22 01:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 85.0 |
| 86d076a4-f259-3087-b449-5281389b4ddb | -8.9851 | -65.9232 | 2025-10-22 01:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 69.4 |
| 3bb8a2ff-3b0a-3ac1-bf3f-c9e60243d24d | -3.383 | -50.2807 | 2025-10-22 01:10:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 56.7 |
| ed25ec8c-d7bc-31bb-809f-a458913299aa | -3.3831 | -50.2597 | 2025-10-22 01:10:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 57.7 |
| 1a4f93ce-feb0-3cb2-90f2-67120dcd32dd | -9.0222 | -65.922 | 2025-10-22 01:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 90.0 |


[Clique aqui para ver as próximas entradas](README3.md)
