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

## Dados Diários - Página 72

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5c582f17-e063-3479-b792-481d088caba0 | -3.04826 | -54.15228 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 5be6f458-5f70-3067-9329-5409b85e5e78 | -2.54031 | -56.42269 | 2026-10-07 05:04:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 78cc6c19-4698-3fba-8ef2-3d249adf851e | -2.99972 | -51.00726 | 2026-10-07 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5e386bcd-5e69-34c4-91e3-6db48037aaa8 | -3.28357 | -53.86267 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4b4413cd-bf86-3853-a6b3-102b5021e4e4 | -4.15843 | -55.15236 | 2026-10-07 05:04:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 44a14892-bffe-39b3-9931-e7e953ac5715 | -6.02382 | -51.72019 | 2026-10-07 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fb4e276b-f7a9-3b8a-8a31-4b2da88ef707 | -4.55522 | -49.35214 | 2026-10-07 05:04:00 | NOAA-21 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2fecc66e-486e-3d65-89ed-12bee14d8608 | -3.09268 | -53.73434 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| be8bb5cf-55af-3028-95f4-e22efb09e0e5 | -2.46616 | -56.07194 | 2026-10-07 05:04:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7d9f8e68-0cdf-37ad-a22d-43c260e8dde6 | -7.27813 | -46.15305 | 2026-10-07 05:04:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 43.5 |
| 6eafde0b-e7fa-3e68-b4be-d6f20f4f3643 | -3.52997 | -54.64114 | 2026-10-07 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 49572193-5fed-3a17-84b3-a712ed8e527b | -2.55381 | -57.38711 | 2026-10-07 05:04:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a8d707e7-9113-3833-8085-c83ae89140c8 | -6.21702 | -52.83032 | 2026-10-07 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| bd44adc6-4393-3c7a-960b-2c0193382f79 | -3.47278 | -50.08436 | 2026-10-07 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| e3878e71-92b3-3dc7-bfb0-c005a1d4b9c2 | -3.27166 | -54.04995 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 39a12091-1cf2-39f2-bc52-c2dc1ea54a0b | -2.58795 | -54.24584 | 2026-10-07 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b6172d00-3d46-3763-a6e7-300e22fe652b | -3.2761 | -54.04341 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 26.4 |
| 38e45871-97dd-310a-9c0a-499b43e6cfa7 | -3.27705 | -50.41314 | 2026-10-07 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| d3440f66-f1ff-3ed1-b162-cdca963b36a7 | -3.08019 | -54.18593 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cc827a13-8fcc-312a-a582-2f0e77dd7301 | -4.45538 | -47.92734 | 2026-10-07 05:04:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 22.7 |
| aa24048c-6bbe-3665-b591-14f1461fbe52 | -3.00855 | -54.23223 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| de82c0f7-11ea-32a4-a0ca-525e6f0a3b90 | -2.78835 | -51.67291 | 2026-10-07 05:04:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| b441c3ae-aba9-3db5-93f9-ebf037c61131 | -3.50403 | -54.63357 | 2026-10-07 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 52dfffed-a653-36b8-ae88-97c8db3d6455 | -3.54127 | -59.46516 | 2026-10-07 05:04:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| f3008c34-d9e6-3d82-b346-f2b718d836e8 | -2.88451 | -54.08775 | 2026-10-07 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 75361d12-5e93-3789-8f20-f5fb86e969e5 | -2.98378 | -54.12796 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 099c83b3-3bc0-3694-b8fc-22fd809da251 | -3.01466 | -54.23675 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 87d2ec8c-2c0a-300b-8a0b-6b1711c480e1 | -3.10173 | -54.15683 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a186d665-773b-3a8f-a511-1e12a446d49d | -2.95568 | -54.11305 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 36cece5c-26ec-3a19-92b6-7bc8cea98d8c | -3.27725 | -54.05806 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d3d2ef07-dcbe-316b-bdc2-b3f2c1cd274c | -3.6782 | -59.62962 | 2026-10-07 05:04:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 60e97cc9-68c0-35e9-94b5-cdb59722d401 | -4.28952 | -50.78054 | 2026-10-07 05:04:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2473db58-73f0-399f-a9d5-e0fe6792b2dd | -4.11512 | -54.42162 | 2026-10-07 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8adbc401-e850-3945-bb38-6833b58bc647 | -2.82627 | -54.13575 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e2dd4905-1a6a-3020-969a-a4a184c8d951 | -6.2164 | -52.83452 | 2026-10-07 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e240f41b-f771-3c57-9117-c724c60a8345 | -3.13084 | -53.7108 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9038e726-da94-363a-96f5-0f2f6b97ce44 | -3.23161 | -53.88755 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d26e8089-59aa-353a-8866-cc30fac3cf9e | -3.1129 | -53.75947 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 41732205-d7e9-3ed1-9c6e-b7473630a895 | -1.12898 | -53.10691 | 2026-10-07 05:04:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 06657e19-9017-3cab-914e-dde0c30652ad | -2.93131 | -54.13807 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fdc97ca1-3fa0-30e4-9567-febf8304714c | -3.86244 | -55.99955 | 2026-10-07 05:04:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 472cf6c4-59bf-3340-822e-95282708a4e1 | -3.82899 | -55.86723 | 2026-10-07 05:04:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 503eeb3c-a379-3a6c-be41-16fe27052007 | -3.34792 | -45.10458 | 2026-10-07 05:04:00 | NOAA-21 | CAJARI | MARANHÃO | Brasil | 2102507 | 21 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 45a58770-38a7-3685-ad40-bd8957f32265 | -2.85109 | -51.2962 | 2026-10-07 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d5a0fc1c-b945-3810-bc13-4bcf874c2083 | -3.27775 | -54.03279 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| e7d5f97e-916b-309a-86d2-6d09bc7cbfa4 | -6.38571 | -55.22438 | 2026-10-07 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| caa2a854-af99-3665-a782-81b9cd85ef80 | -4.15206 | -54.35902 | 2026-10-07 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cdc65a94-2f20-387e-a912-88455c250ed9 | -3.46844 | -50.08731 | 2026-10-07 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6d3f67da-00cb-3b25-852e-3dfbdab898bd | -3.09602 | -53.71281 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8078a9c9-1456-3c61-a229-da364d8d9734 | -2.95463 | -54.14162 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| a8047ff0-d052-33e2-aaae-9976754eb839 | -4.2568 | -50.72861 | 2026-10-07 05:04:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7ac3ea9a-17df-3476-89b7-ee920d7c0a37 | -3.85799 | -55.98471 | 2026-10-07 05:04:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 8bee5359-cc69-3f3c-b85b-61aa6da6fe61 | -3.53797 | -59.41438 | 2026-10-07 05:04:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c990b7f6-09bb-32fd-b3fc-8ac23d766ac1 | -3.80907 | -51.03883 | 2026-10-07 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 55c53bd4-e76f-33e3-94aa-f1653dc7f917 | -3.1847 | -50.54639 | 2026-10-07 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 4a06ba0a-2158-3bf6-8a87-736810f4ecdc | -3.28563 | -54.07016 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 570dd27b-789f-30db-a609-655252052758 | -3.23476 | -54.37456 | 2026-10-07 05:04:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e689754f-0409-3ce3-9b89-b418fe918afd | -2.79561 | -54.09157 | 2026-10-07 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 513056aa-f6ef-3255-9807-dd39e7127457 | -3.53319 | -54.64505 | 2026-10-07 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 48c2f294-e1e3-302c-ac90-4bf490d7e822 | -2.94026 | -54.16814 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 9718082c-0286-3103-a214-ae58a8889c23 | -1.50902 | -54.83552 | 2026-10-07 05:04:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ce3b2868-2fce-3325-9310-2aa6d3babbf1 | -3.65806 | -55.50285 | 2026-10-07 05:04:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f7cc212c-4a14-373e-aade-b777a6b2c624 | -2.8653 | -54.14583 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 30a7cf27-bc30-303e-b92f-4b5f03c252a0 | -4.08522 | -48.90543 | 2026-10-07 05:04:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 06f281fe-e1eb-3cfd-b73f-85eeb421afd1 | -3.60972 | -50.20054 | 2026-10-07 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 532645d4-b362-3f3e-9636-d95f3c03ada5 | -3.79431 | -58.28943 | 2026-10-07 05:04:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 45998fd1-0795-3fc2-8d91-9fe0aefa2d29 | -6.92013 | -47.65689 | 2026-10-07 05:04:00 | NOAA-21 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1d7d16c8-d7d4-3e8f-bf7c-90f59b4173c5 | -3.30862 | -42.27559 | 2026-10-07 05:04:00 | NOAA-21 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 2cf672a7-046c-392d-80a4-98c2179a0017 | -2.98462 | -54.05608 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3457b94f-2662-3c33-bb85-a0daa4cecd7f | -3.51734 | -54.65691 | 2026-10-07 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 65233149-1d7f-3af2-9d0a-873de421c380 | -3.06273 | -54.25487 | 2026-10-07 05:04:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ea8fe6f8-b0aa-3be1-aa7a-61e7722da407 | -3.16382 | -50.44512 | 2026-10-07 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7a919c88-6398-34ee-812e-a8ecb94fb5d2 | -3.68269 | -55.9541 | 2026-10-07 05:04:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 80dfbed4-601d-3f6f-9ca9-166e54894143 | -2.57186 | -56.1569 | 2026-10-07 05:04:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8e0ea212-359e-317e-ae0a-6098310cbecc | -3.11011 | -53.77736 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| f98a5ed4-f1b6-3076-a6c5-5e1953df3cd1 | -3.04874 | -53.88477 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 45d1625d-a415-36e4-923d-a762b1330195 | -3.50572 | -54.64448 | 2026-10-07 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d1c6cc9e-ba59-3ef9-a2ae-a7c690b9f79b | -3.28338 | -54.06261 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 3de28424-6b67-3f71-bff5-de9b91710cfb | -3.38008 | -59.42977 | 2026-10-07 05:04:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 36a3b4b7-a773-354b-a71b-177b00703d86 | -3.08044 | -54.25048 | 2026-10-07 05:04:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 923a2309-1792-3d4a-9d76-d26ae0802b5a | -5.74453 | -43.27881 | 2026-10-07 05:04:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| f921815c-5bb3-38e5-a754-da6dba28278e | -3.08114 | -54.28993 | 2026-10-07 05:04:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1848c1e2-8715-3b29-8a7e-131c9faebbe8 | -3.07881 | -54.26097 | 2026-10-07 05:04:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4b230cf2-0934-39c1-a730-896eddb028d9 | -3.52281 | -54.64359 | 2026-10-07 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 508e7aa5-cde6-3d43-8659-3c1f2cb47fb9 | -5.89303 | -53.64149 | 2026-10-07 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a1011c1c-9664-318d-8633-439a438e9eee | -2.58867 | -55.94187 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b5ad0fdf-904d-365f-b526-fc58078b6e19 | -1.12446 | -54.11774 | 2026-10-07 05:04:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 2b55ec34-bbcc-3b20-8e4d-48c8315205ad | -3.43411 | -59.62418 | 2026-10-07 05:04:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c1dc5acf-0be9-321e-abfb-793a5f4e0e00 | -3.624 | -55.28269 | 2026-10-07 05:04:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c97fcd20-038f-323e-91b8-bd0c22ff2174 | -4.11656 | -50.80932 | 2026-10-07 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 73b452df-9d75-3c51-ae69-ce3afea3f03b | -3.23834 | -50.17793 | 2026-10-07 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7e2be4b7-8189-38dd-8952-20ac5ed778d3 | -3.11348 | -53.77789 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 9078fbf2-3150-3f17-b47f-3d106386cacb | -4.24321 | -49.98138 | 2026-10-07 05:04:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 578d59e8-73c8-330d-8841-5183952c3132 | -3.08098 | -54.24699 | 2026-10-07 05:04:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3aa4fa5a-4a0a-3c8e-b096-7e4b6989eb10 | -2.76616 | -54.08345 | 2026-10-07 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 24.9 |
| 0a6e799b-d6aa-33e7-99ed-0487e99c94cb | -2.50963 | -56.33465 | 2026-10-07 05:04:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2ecb04ee-3a8f-3e2d-a46b-1e19ed654e28 | -2.57333 | -54.01093 | 2026-10-07 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0c0057c1-6c52-3833-b33b-eaaf0740793c | -3.04704 | -53.87357 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 4cb7acfe-2d03-3795-a8b8-e179ad8d9789 | -2.95956 | -54.11006 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 968b2e0c-8c1e-3779-ae1d-a0b8be72c857 | -3.52389 | -54.63666 | 2026-10-07 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README73.md)
