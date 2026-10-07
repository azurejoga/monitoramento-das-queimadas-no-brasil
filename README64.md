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

## Dados Diários - Página 64

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e86f90a5-c550-3480-9a4f-eedb179fcdfe | -2.7612 | -54.1142 | 2026-10-07 04:50:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 118.0 |
| 314026b2-778f-3b80-9164-511f4795fee6 | -2.7613 | -54.0941 | 2026-10-07 04:50:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 162.9 |
| 3397c6ac-3b09-3e21-bf36-55b46868853d | -2.7796 | -54.0937 | 2026-10-07 04:50:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 172.7 |
| ed694eed-e6e4-3ad1-b452-8318828bbb8c | -2.7796 | -54.1138 | 2026-10-07 04:50:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 153.5 |
| a8f26dbc-cfba-3def-821d-047daaba5dfd | -3.531 | -54.6557 | 2026-10-07 04:50:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 73.3 |
| c4d28cb3-2ea9-3029-b6cc-6f10de98d469 | 1.64134 | -55.8099 | 2026-10-07 05:01:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3e8e8cd8-f5d0-392d-822b-18d89313d219 | 3.52845 | -51.2767 | 2026-10-07 05:01:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f48c458a-ed52-3364-9e68-bb34c258c08c | 3.21713 | -51.32777 | 2026-10-07 05:01:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 53ddf308-717f-34a1-a08e-c7224e67c6fc | 0.0974 | -51.06844 | 2026-10-07 05:01:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 6401b63e-bbc9-3a9d-9028-8cb977d2e1e6 | 3.4066 | -51.30699 | 2026-10-07 05:01:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| cd5a9b14-7dd2-378f-b9e6-01c857cc40f8 | 4.27855 | -60.14635 | 2026-10-07 05:01:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 49087c65-bdcc-3fd9-9ca4-2294a95205f6 | 1.71128 | -55.62665 | 2026-10-07 05:01:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9bcdea23-eb72-3018-87a0-c27e98779c98 | 3.52026 | -51.27007 | 2026-10-07 05:01:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1490ebba-8954-3614-899d-396209becd7b | 2.43712 | -50.84672 | 2026-10-07 05:01:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8263b23d-8f70-33c3-a450-1f92c7037315 | 1.77947 | -55.56453 | 2026-10-07 05:01:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a3aa9261-1e87-316e-a2ce-8af9705f8454 | 1.73536 | -55.60471 | 2026-10-07 05:01:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8d32ffad-4720-3cd7-b83f-4742ed518db5 | 1.64246 | -55.79495 | 2026-10-07 05:01:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 20016a72-54c5-37d3-973d-2c8b096f78d7 | 3.15254 | -60.60322 | 2026-10-07 05:01:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9822dbd3-a95c-3b26-a1fc-ef5f671a8668 | 1.71968 | -55.61437 | 2026-10-07 05:01:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 184978ec-c12f-3840-9c54-8170184788a5 | 3.40311 | -51.30754 | 2026-10-07 05:01:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e544e97c-3057-37ff-aafa-36947fa88b05 | 2.56456 | -60.18601 | 2026-10-07 05:01:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a61135a1-a4d5-378f-9072-09be3e9ca72d | 3.15097 | -60.60276 | 2026-10-07 05:01:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 3.6 |
| a94ea743-bb09-3bc0-8335-cdf263153847 | 1.7711 | -55.55488 | 2026-10-07 05:01:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0339cb92-1bd7-3a3a-8f70-3bc6bba7aa0b | 2.44234 | -50.83316 | 2026-10-07 05:01:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 4.3 |
| f025cbc0-de92-3f5e-b55b-a1d6690d7e52 | 1.3406 | -50.84123 | 2026-10-07 05:01:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 54f4d73d-4fc3-3494-9dea-4cdd43e2d482 | 2.26932 | -50.81117 | 2026-10-07 05:01:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 766dd444-2d4a-3162-9735-3167b8fe86e0 | 3.15027 | -60.5982 | 2026-10-07 05:01:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 86e33274-4a78-36f5-9741-749a62f10f29 | 1.72304 | -55.61386 | 2026-10-07 05:01:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 24393cc9-24cd-363c-a054-6f76a96ac931 | 1.89123 | -55.71637 | 2026-10-07 05:01:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0012de1d-3364-3609-b1f9-1183c362cb80 | 2.13031 | -50.83132 | 2026-10-07 05:01:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5df42117-9413-31ba-a2e9-910a503e8aee | 2.43646 | -50.84259 | 2026-10-07 05:01:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 035d9a2e-e0a1-39f5-b91c-b372ee14a668 | 3.98275 | -59.73343 | 2026-10-07 05:01:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7aeb8184-e231-34cc-bff7-8ee9e714590e | 1.70623 | -55.63841 | 2026-10-07 05:01:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 3d275a0b-7d1e-3b7b-a0c2-86c7f55a47b1 | 3.36566 | -51.34117 | 2026-10-07 05:01:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 47e717de-40d1-3dc7-b96a-e2e5548f41b0 | 1.72248 | -55.6103 | 2026-10-07 05:01:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| e862574a-7394-36ac-91f0-f40edc2fa2f5 | 0.72519 | -51.3718 | 2026-10-07 05:01:00 | NOAA-21 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4b0d151b-387d-38ef-a165-13e2fa1de77c | 3.86321 | -51.77058 | 2026-10-07 05:01:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a1adb042-6dff-3bed-9533-bea044492268 | 3.52784 | -51.27283 | 2026-10-07 05:01:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8f05eb22-1f1c-3ff8-86ad-61935021b13e | 1.52721 | -56.02042 | 2026-10-07 05:01:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9c005f1e-aa9a-3389-a97a-11286cff6ff0 | 1.88786 | -55.71689 | 2026-10-07 05:01:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f758e95f-56ec-3caa-8dd7-1cc67fda7fcd | 0.72822 | -50.61429 | 2026-10-07 05:01:00 | NOAA-21 | ITAUBAL | AMAPÁ | Brasil | 1600253 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1881961f-adcd-3a80-bfcb-45c5a32afce8 | 1.86702 | -55.73854 | 2026-10-07 05:01:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 296f26a7-9876-365b-a594-6cfd70fc4a83 | 3.51616 | -51.26675 | 2026-10-07 05:01:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| eaf93e18-f2ad-38de-8f51-4ad11aaad3bb | 1.52324 | -56.01728 | 2026-10-07 05:01:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6d59bf9a-5321-3800-8c01-e592c90c9961 | 1.77276 | -55.56556 | 2026-10-07 05:01:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d3cf9afd-40e0-3814-878a-40559d480aca | 3.42777 | -51.50779 | 2026-10-07 05:01:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 64b92e49-4887-39db-b9b9-70f46030bc21 | 1.70287 | -55.63893 | 2026-10-07 05:01:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 56cba02a-3099-3009-a286-99beb6d7e57b | 2.45182 | -50.82316 | 2026-10-07 05:01:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 5.6 |
| ccec3ee6-0b57-37b5-93f5-339f942a0c91 | 1.72864 | -55.60573 | 2026-10-07 05:01:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| e33045fb-dead-327c-b3eb-2717e61d000f | 1.69952 | -50.90601 | 2026-10-07 05:01:00 | NOAA-21 | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 33cd5bd7-8443-362b-a60d-f1f8688b6b6a | 0.69838 | -51.43425 | 2026-10-07 05:01:00 | NOAA-21 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4da8f1d0-0984-3661-9eef-f6288bc14c3e | 1.7292 | -55.60929 | 2026-10-07 05:01:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e1717112-9669-3f0f-a368-b25ff3ba3be4 | 3.15187 | -60.59865 | 2026-10-07 05:01:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a80bc3aa-8a58-31dc-bebd-4d66948017ff | 1.70847 | -55.63074 | 2026-10-07 05:01:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 47cfaa44-6536-35a7-a9d5-b325400b3d82 | 2.59729 | -50.8694 | 2026-10-07 05:01:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 575207da-9f09-3fd8-81d1-91d0249a9229 | 3.51268 | -51.26731 | 2026-10-07 05:01:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a39107fd-146d-37de-b791-5fb039646b27 | 1.77611 | -55.56505 | 2026-10-07 05:01:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e862abfb-143d-3a58-8a45-2a56dd5c3845 | 3.14801 | -60.60389 | 2026-10-07 05:01:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 82e5cdef-7113-3b35-9479-c598107d0087 | 1.96896 | -55.88256 | 2026-10-07 05:01:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e1829b58-2a38-32fc-8a9c-ab286fc7c440 | 1.72584 | -55.6098 | 2026-10-07 05:01:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d92f510a-41ff-3da3-84e1-572fba7e23df | 1.81976 | -55.53651 | 2026-10-07 05:01:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3e87afbf-59de-3141-97b6-d5bb76448db9 | 1.7348 | -55.60115 | 2026-10-07 05:01:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 58cbaec2-89da-3634-ae49-027f9676fc8d | 3.23404 | -60.71408 | 2026-10-07 05:01:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c746ab43-f348-3375-a4e0-b4a4f1b1ee1a | 1.72809 | -55.60217 | 2026-10-07 05:01:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| ff7285dc-22e4-33a5-aa57-3dc3b257a882 | 2.75598 | -60.01863 | 2026-10-07 05:01:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 300e4d7a-1c21-3540-8cbe-09450af05449 | 1.77051 | -55.57321 | 2026-10-07 05:01:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 41909fa2-5edc-3f84-91f7-53eb769f6af5 | 2.75788 | -60.00167 | 2026-10-07 05:01:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 741e204b-4360-39d3-a837-88441fa9ee81 | 1.87039 | -55.73802 | 2026-10-07 05:01:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4f88c569-dbe7-37a3-a987-e5460cf32361 | 1.90079 | -55.71121 | 2026-10-07 05:01:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e5ce03ef-a375-32bb-901a-7955d5685617 | 0.72646 | -51.37994 | 2026-10-07 05:01:00 | NOAA-21 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f435ba2f-6dad-32ec-9c9c-3b44c6760bea | 1.09356 | -50.7271 | 2026-10-07 05:01:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c3302be9-cc5c-30ac-8d89-de437fde845d | 2.44168 | -50.82902 | 2026-10-07 05:01:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 4.3 |
| c50bbf31-d208-3378-ba3c-a09e63a4ee46 | 3.14434 | -60.58974 | 2026-10-07 05:01:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 4b2dd718-20c8-3d89-b05c-60cfe5314f1e | 1.7694 | -55.56608 | 2026-10-07 05:01:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ace1af18-15ac-374a-81fd-82d1185518cc | 2.44528 | -50.82845 | 2026-10-07 05:01:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 88278707-7134-3f39-b76d-400b3bfc440a | 1.732 | -55.60522 | 2026-10-07 05:01:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6864f18c-c7ae-38af-bb0d-30706965d537 | 3.74775 | -51.62069 | 2026-10-07 05:01:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5271a5b9-4aea-3b03-8c60-e0640f5a97eb | 3.14051 | -60.59497 | 2026-10-07 05:01:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7d777b7e-0051-3fa6-87fd-77f020c93fad | 4.14751 | -61.24833 | 2026-10-07 05:01:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 732a9323-1142-35a3-9cc9-7dd7809e634d | 3.14016 | -60.5817 | 2026-10-07 05:01:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 6217ea9c-64e3-39b2-9719-034fa800a01a | 3.13981 | -60.5904 | 2026-10-07 05:01:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5e6bd538-cff7-3fc4-89d6-acb7f6aa6eeb | 2.42585 | -51.41504 | 2026-10-07 05:01:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9cfa990a-3cb4-398b-bfde-b0fa3866bd88 | 2.43419 | -50.85144 | 2026-10-07 05:01:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2d311150-c97f-3b55-b914-77a60b495891 | 1.70567 | -55.63483 | 2026-10-07 05:01:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 950bd5f9-5a85-3a4c-adde-c8d901ae6bbd | 1.71352 | -55.61898 | 2026-10-07 05:01:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 518a5a16-d8ce-3683-aa7a-b8927cdfd3f2 | 3.20955 | -51.325 | 2026-10-07 05:01:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d23551b4-416e-3336-b9be-8aed86462bb7 | 1.79853 | -55.53247 | 2026-10-07 05:01:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ab5f0ffe-7073-3330-b773-1560362a4141 | 1.52268 | -56.01363 | 2026-10-07 05:01:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 41746426-a493-34aa-aa9a-d04b9d111d81 | 1.64189 | -55.79134 | 2026-10-07 05:01:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 24bac28b-21e1-365c-95aa-6db99a7b1f22 | 0.70194 | -51.43369 | 2026-10-07 05:01:00 | NOAA-21 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9b6078e1-6528-3789-9a88-598152241756 | 1.72528 | -55.60624 | 2026-10-07 05:01:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 8eebce45-4545-350b-923a-cab63f5c6179 | 2.44203 | -50.85442 | 2026-10-07 05:01:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b2b2bad4-67e6-3ccf-b814-b91169c23913 | 3.14294 | -60.58062 | 2026-10-07 05:01:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c6778309-d30b-35fc-9360-448283067cbb | 3.13842 | -60.58129 | 2026-10-07 05:01:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| eda05e4d-839b-34e8-8bd4-c5b6008d9fa5 | 2.56892 | -60.18534 | 2026-10-07 05:01:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| eb2eebf7-59ea-39da-8f4c-54ceb145ce63 | 1.73089 | -55.59811 | 2026-10-07 05:01:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| cbec5d45-7623-34ab-a3a8-c9fe4ae69190 | 3.14601 | -60.59016 | 2026-10-07 05:01:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d9adc144-6106-3dcc-ae7a-84d22c5c3aef | 3.14148 | -60.59083 | 2026-10-07 05:01:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| beb3adc1-67f5-32b0-8773-6b0ea25c5c04 | 0.93964 | -50.20063 | 2026-10-07 05:01:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 1cf5207e-aa3a-3d1f-baee-8b5602080266 | 1.52041 | -56.02146 | 2026-10-07 05:01:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README65.md)
