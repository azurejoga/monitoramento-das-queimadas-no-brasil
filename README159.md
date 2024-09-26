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

## Dados Diários - Página 159

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 88034a12-d401-34c7-bf6b-ea26abaa6174 | -6.80102 | -59.30974 | 2024-09-26 05:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9cf991ca-8c32-37a9-b4fd-54ba7a9c7c9c | -6.79768 | -59.29881 | 2024-09-26 05:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0b8774e5-0215-38eb-a412-b15861de4564 | -6.79695 | -59.30397 | 2024-09-26 05:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 875796d7-21ee-3a83-9354-a0c04a731aff | -6.79623 | -59.30913 | 2024-09-26 05:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c94e09d6-6837-390b-8710-38c07066ff65 | -6.79146 | -59.3084 | 2024-09-26 05:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 90f5d705-2fb9-36f7-b0ee-8ae2301566f6 | -6.79074 | -59.31355 | 2024-09-26 05:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 60fb0259-6c72-3e36-a3c3-70136d10affb | -6.78669 | -59.30768 | 2024-09-26 05:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a921f64c-ae1b-3b4a-a160-2e5c7766307d | -6.78597 | -59.31285 | 2024-09-26 05:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3eb38cd2-e028-3591-ac71-fbd3ddaa8e25 | -6.78427 | -59.35997 | 2024-09-26 05:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d41dd13d-7823-3886-a6f2-9667906f4278 | -7.58409 | -60.59454 | 2024-09-26 05:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1d7800ff-36cd-3a90-828a-4dab6873c5c7 | -7.58348 | -60.59888 | 2024-09-26 05:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ceb3c686-9c36-3c0a-9691-d6a90a06f86d | -7.58027 | -60.58958 | 2024-09-26 05:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cfb7ce7f-9334-3cf7-9195-40828bc60e61 | -7.57967 | -60.59391 | 2024-09-26 05:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 044588b7-ae96-3e95-8dde-17ed7e24e950 | -7.4585 | -60.41024 | 2024-09-26 05:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 58b850ff-54d9-3841-8b5d-a5cb996c310b | -7.45403 | -60.40957 | 2024-09-26 05:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| efe03f58-db61-35ef-be45-623918e5612c | -7.4534 | -60.41394 | 2024-09-26 05:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 58041c97-6c65-35be-b2ab-6bdd3e3940f2 | -7.4496 | -60.40872 | 2024-09-26 05:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3eadd4b2-2d6a-3d8c-96e4-05d8980ce872 | -7.43573 | -60.62724 | 2024-09-26 05:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dd331c9b-dcb6-3d75-868f-76e4033ca591 | -7.43567 | -60.62905 | 2024-09-26 05:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 36225894-aad9-37ab-9683-76b2bca038ae | -7.43191 | -60.62236 | 2024-09-26 05:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| be54f045-2631-3aa6-ada8-16b60f6fc7ec | -7.43188 | -60.62418 | 2024-09-26 05:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 57a64222-0fab-3609-9057-8b3de181f38f | -7.42966 | -60.29212 | 2024-09-26 05:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2c9702da-3929-3b81-b7f2-49bdd93c5de5 | -7.42517 | -60.29134 | 2024-09-26 05:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 53113788-df0d-3a47-81e6-2d511ac987c0 | -7.42455 | -60.29575 | 2024-09-26 05:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 100d62a5-68fd-3033-a43c-56adbd04f746 | -7.42006 | -60.29499 | 2024-09-26 05:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6a418954-5ece-30e8-bbaa-356be6f35789 | -7.41914 | -60.52544 | 2024-09-26 05:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 65eed908-99e1-38b4-848b-24557909d3ca | -7.41043 | -60.29815 | 2024-09-26 05:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 38a4daf8-a40a-32eb-ae71-28f5ec8ea417 | -7.40216 | -59.79121 | 2024-09-26 05:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9527d6a2-5b50-392d-8a87-c2ac61c54336 | -7.40146 | -59.79613 | 2024-09-26 05:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| c457f37f-3c3c-3ad2-a943-93d4461217d3 | -7.31161 | -59.9049 | 2024-09-26 05:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e63625fb-c66d-3c13-be77-0389e350b123 | -7.30701 | -59.90416 | 2024-09-26 05:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c4181f12-4a30-38a9-9e39-cf491d369c64 | -7.22153 | -60.67952 | 2024-09-26 05:46:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d763a203-8f27-3148-b7ba-5fd2c45046a4 | -7.20856 | -60.68054 | 2024-09-26 05:46:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c2e1bc44-08a8-3ee8-9635-e3e47cb0e952 | -7.20778 | -60.68198 | 2024-09-26 05:46:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c20d28bf-a412-385d-9605-f5054fc1beab | -7.20527 | -60.66864 | 2024-09-26 05:46:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2ee8026b-36d5-3eb9-a4e3-9775a73f2727 | -7.20281 | -60.68547 | 2024-09-26 05:46:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0f73f284-990d-354d-a0e1-b9b9e58a9559 | -7.20151 | -60.66376 | 2024-09-26 05:46:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f1028c3e-a4cc-3947-b219-2937d24fad60 | -7.20091 | -60.66792 | 2024-09-26 05:46:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 34ab7e1a-ca07-3ac3-a2cc-ee839a8b8db2 | -7.19903 | -60.68075 | 2024-09-26 05:46:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ab03b6a9-90d1-303a-b597-847f2965ed76 | -7.19841 | -60.68498 | 2024-09-26 05:46:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 938171a8-a08d-31b4-8cea-3f6929531b46 | -7.1978 | -60.65861 | 2024-09-26 05:46:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 42e2fac6-c052-3b08-9d44-164260c3a997 | -7.19717 | -60.66292 | 2024-09-26 05:46:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| ac129f6f-df14-3ecf-ab84-7df7e4a23f9c | -7.19465 | -60.68018 | 2024-09-26 05:46:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6c2c9e11-ecd1-34e0-abfd-22da2565df3f | -7.19404 | -60.68443 | 2024-09-26 05:46:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b816441a-825b-3a87-b9c5-fd816a2d3a80 | -7.19341 | -60.6887 | 2024-09-26 05:46:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 329b5673-c9d6-3006-8930-82487460ca8d | -7.07981 | -59.82343 | 2024-09-26 05:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 55bdfe75-de7b-3042-95bf-3ba630af272b | -7.03689 | -60.12361 | 2024-09-26 05:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3ac69073-e591-35c2-811d-8f8162d989e1 | -7.00659 | -60.68022 | 2024-09-26 05:46:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 64a64006-b62d-35e4-9551-45ab00b9f616 | -6.99235 | -59.6143 | 2024-09-26 05:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5713db27-d98c-3d2b-8b4e-646b4ce98cef | -6.98904 | -59.60383 | 2024-09-26 05:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 35fd9321-972a-33ab-ba3f-252e7df6e5d5 | -6.98835 | -59.60875 | 2024-09-26 05:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| dca4633a-6721-3c1b-a450-78f7b158c790 | -6.98364 | -59.60822 | 2024-09-26 05:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f8d0e207-fd95-3cf2-a1c9-d4ccf6f6d823 | -6.95428 | -60.14095 | 2024-09-26 05:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e625e0d3-529e-3bf4-9343-73d2c4dd010a | -6.93332 | -59.93099 | 2024-09-26 05:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c45af76e-fd3a-3b08-ac24-7daa0c5f45f0 | -6.89834 | -59.65424 | 2024-09-26 05:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 26365f2b-d064-3a2d-9710-e3e31d31a3f7 | -6.89764 | -59.65911 | 2024-09-26 05:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5d07b522-facd-3b72-a85c-4ba1ebb1a0d4 | -6.89655 | -59.82462 | 2024-09-26 05:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fe0619f5-078a-3a05-b3b5-9d433dcb9b55 | -6.89297 | -59.65847 | 2024-09-26 05:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 68082231-6a57-3ec9-b226-ff8721accf14 | -6.81594 | -60.504 | 2024-09-26 05:46:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 84b7808b-064f-3888-b3ac-e033f38a63b8 | -6.81579 | -60.50572 | 2024-09-26 05:46:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e9144934-b69f-3d7d-b612-d68781a68bd8 | -6.81203 | -60.50079 | 2024-09-26 05:46:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9093a75f-4246-3fcd-898e-1ac0dedae9aa | -6.81153 | -60.50342 | 2024-09-26 05:46:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 22e112a4-73b6-34a5-8094-9262b7781f86 | -6.76612 | -59.69267 | 2024-09-26 05:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2bf684d4-63ae-3154-b147-fd7923ada792 | -6.73759 | -60.08606 | 2024-09-26 05:46:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5af670be-162c-38a4-9b8b-1828ba154b56 | -6.73693 | -60.09063 | 2024-09-26 05:46:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c8b99fc2-df04-3199-beef-cdc97ad56c23 | -6.73306 | -60.08547 | 2024-09-26 05:46:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 65bdc980-900f-3842-a87f-7ccac5b21180 | -6.63599 | -59.94899 | 2024-09-26 05:46:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d0a4de37-158c-3a52-8d25-9eba8261dd44 | -6.61442 | -60.00206 | 2024-09-26 05:46:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| c10aa919-09d5-3be3-959d-bc5e36d3ff7b | -6.61052 | -59.99692 | 2024-09-26 05:46:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b798977e-c06b-38bf-98af-206df26413a3 | -6.60599 | -59.99625 | 2024-09-26 05:46:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d7cf50c8-2e1b-3852-bf7e-80c9c7d9d59e | -6.5807 | -60.04396 | 2024-09-26 05:46:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 445ecc27-e9b9-3a76-b0f3-03ec7cb935e9 | -6.58006 | -60.04849 | 2024-09-26 05:46:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c2415158-4f9c-3a00-9d75-7c93616d8f5a | -6.57683 | -60.03868 | 2024-09-26 05:46:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2595ffcd-747b-3c41-8897-48aad0154fd2 | -6.57618 | -60.04326 | 2024-09-26 05:46:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 5b21e708-b380-31fa-b709-639cb87b40ab | -6.57554 | -60.04781 | 2024-09-26 05:46:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 980c5843-11b2-3f7e-a6b4-8ac07918017f | -6.5749 | -60.05231 | 2024-09-26 05:46:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 64c676a3-a5b2-396b-b79a-57ef63d6e9b5 | -6.5736 | -60.06154 | 2024-09-26 05:46:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b4972e78-e811-339e-89d1-645105d84b7a | -6.57297 | -60.06599 | 2024-09-26 05:46:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fb65be63-6803-3c7e-92ec-b36404b7f015 | -6.57231 | -60.03798 | 2024-09-26 05:46:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| be8e6e1f-07a0-3a41-ba56-c71ed676a475 | -6.57167 | -60.04254 | 2024-09-26 05:46:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 081670c5-6d4c-3aab-8222-b09fb98c2268 | -6.57102 | -60.0471 | 2024-09-26 05:46:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e3a9f6d5-8f3d-367c-8fbb-3aab82e9ca94 | -6.57038 | -60.05166 | 2024-09-26 05:46:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 800ac7e1-5af1-343e-8347-e336f28ab831 | -6.56715 | -60.04183 | 2024-09-26 05:46:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 86deab66-ea06-317f-a344-4beab23674bc | -6.55861 | -59.97052 | 2024-09-26 05:46:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ae604652-d388-305a-9e23-3e82490c488c | -6.55796 | -59.96767 | 2024-09-26 05:46:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 44491bb6-dc69-338c-ba7b-3e304b16049e | -6.55469 | -59.96538 | 2024-09-26 05:46:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 689cf725-7892-3fa7-856a-b7143aad0681 | -6.55341 | -59.96703 | 2024-09-26 05:46:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 672aa377-9c8b-34f4-b924-a38674c7ca53 | -9.05193 | -60.42923 | 2024-09-26 05:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c93c1561-17f5-3a68-b2ac-6bf9e0b571ba | -9.05128 | -60.43391 | 2024-09-26 05:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 0ecdc15f-e6fe-3ddc-844b-8f66631a7f99 | -9.04736 | -60.4286 | 2024-09-26 05:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 65d1e82f-0622-3c47-acca-5db3388caba6 | -9.04671 | -60.43328 | 2024-09-26 05:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| ba012f36-687b-32d8-b095-77022eb69c2b | -9.04605 | -60.43798 | 2024-09-26 05:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 420ec88e-4f14-3272-a26e-7c86d6fb5da5 | -9.04214 | -60.43261 | 2024-09-26 05:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3b3b208f-1087-3217-bc39-fb67156af665 | -9.1068 | -61.1273 | 2024-09-26 05:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 89c6cb2b-1d37-388d-936c-b15aba6a0cfd | -9.10243 | -61.12672 | 2024-09-26 05:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 799f8d5b-1200-3eb8-b96b-c6fba699e5f1 | -9.09865 | -61.12189 | 2024-09-26 05:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 65e9a66f-60f2-3d03-ae08-5e549f997052 | -9.09807 | -61.12613 | 2024-09-26 05:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 3ccc1ff5-911a-3b0f-8b69-a2237695a9a9 | -9.09762 | -61.12329 | 2024-09-26 05:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| bee5ed30-b42f-333c-a0ea-131ddb468cc6 | -9.09749 | -61.13034 | 2024-09-26 05:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 56221a8b-2faa-3725-b060-eba259e22821 | -9.09701 | -61.12751 | 2024-09-26 05:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |


[Clique aqui para ver as próximas entradas](README160.md)
