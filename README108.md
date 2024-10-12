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

## Dados Diários - Página 108

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e91dd412-bf60-3336-9536-c03ad66a2d80 | -6.67262 | -59.80795 | 2024-10-12 05:23:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2d3a48bf-9ab1-3f21-9b0d-8228e985427d | -6.67207 | -59.81145 | 2024-10-12 05:23:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 69e9fbaa-65dc-3eb2-b01b-89d811f2b1c3 | -6.66309 | -59.78136 | 2024-10-12 05:23:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fab78a8c-72b9-3629-aba9-7b214308b273 | -6.65975 | -59.78083 | 2024-10-12 05:23:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 99767b84-39f1-3ef8-b8c8-201de6c00310 | -6.65921 | -59.78433 | 2024-10-12 05:23:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 994cc72e-c60c-37c8-aa2c-0f693c649aa1 | -6.65587 | -59.78381 | 2024-10-12 05:23:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 529db369-780f-3f97-8f42-1f96d294f6b7 | -6.65308 | -59.7798 | 2024-10-12 05:23:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| eed92ebf-0008-3f04-9792-c7ceec411abd | -6.65253 | -59.78329 | 2024-10-12 05:23:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5d293aee-8f17-3a4d-ae5f-123bda195d63 | -6.64974 | -59.77928 | 2024-10-12 05:23:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 50b931f5-642d-3d5b-b971-d792a542cd4d | -6.6492 | -59.78278 | 2024-10-12 05:23:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 840dc90a-ab02-3de7-8b2b-f9e95ac07e75 | -6.64834 | -60.05077 | 2024-10-12 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ec5d85de-dad8-3181-b9b6-aa8c1887282d | -6.64502 | -60.05025 | 2024-10-12 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b327c4e6-502d-3df7-8014-cf66750db258 | -6.64423 | -59.96808 | 2024-10-12 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 97468334-6d4c-30a7-8b35-90c295ccfa81 | -6.6409 | -59.96755 | 2024-10-12 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4b0e9fa0-f260-3f5f-be0f-d55af1ced4a4 | -6.62934 | -59.99787 | 2024-10-12 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| aa35c78b-b0ef-3804-912b-8018f0f30ed8 | -6.61161 | -60.00223 | 2024-10-12 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 04b42300-6c3a-339e-bc47-213856dcf857 | -6.61107 | -60.0057 | 2024-10-12 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1da4efb3-8863-3675-bc65-6d9cdc948238 | -6.60829 | -60.0017 | 2024-10-12 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8b2444d1-1401-3720-a883-a466f0302a5b | -6.60774 | -60.00518 | 2024-10-12 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 65abe14a-670e-3bc3-b1a5-b10069af3a0d | -6.60653 | -59.93005 | 2024-10-12 05:23:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 65fb427d-54c2-3b81-a20a-31be4a1e8985 | -6.6032 | -59.92953 | 2024-10-12 05:23:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 33cd1760-19b2-37a6-a371-3dc34855b45e | -6.60057 | -59.9898 | 2024-10-12 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| da97845b-6aee-32e1-bec9-72aae771d937 | -6.5625 | -60.0587 | 2024-10-12 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2f8bd224-2318-3d41-a7f0-c76da21706db | -6.553 | -60.0323 | 2024-10-12 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5b1bb1e4-08e3-384d-934e-a662c2ba681f | -6.55246 | -60.03578 | 2024-10-12 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 69455efc-ee7b-3518-b05d-af54e653edbe | -6.54968 | -60.03178 | 2024-10-12 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bceadb82-4599-3c9e-b451-a328098d2a13 | -6.54667 | -59.76677 | 2024-10-12 05:23:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3371ec75-ee75-31a2-bcf2-888edf196e52 | -6.54636 | -60.03122 | 2024-10-12 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 83d73ff3-394b-3e34-b613-b0c547e42508 | -6.54411 | -60.02378 | 2024-10-12 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e2a106e7-f2f4-3598-9697-656a9e898154 | -6.54357 | -60.02727 | 2024-10-12 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 983c425b-d1fe-3f20-9a35-aee43f7ef987 | -6.54334 | -59.76625 | 2024-10-12 05:23:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 772a22da-5d77-38cb-bd32-96ea38f0f05b | -6.54303 | -60.03069 | 2024-10-12 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 115275f4-9c64-3a44-808a-3c39d5c13353 | -6.54279 | -59.76975 | 2024-10-12 05:23:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 39f54e3a-9ce7-341b-a04a-3c3640ac4455 | -6.54181 | -59.99488 | 2024-10-12 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d700384c-73ce-3cdd-b23b-db88d3fa2353 | -6.54078 | -60.02326 | 2024-10-12 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 499c60de-2e88-3a57-9eb6-79563669f7b1 | -6.54054 | -59.76223 | 2024-10-12 05:23:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0ca1940f-1558-362e-891d-6146ee483cc0 | -6.54024 | -60.02673 | 2024-10-12 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c3784bf3-66a3-341c-9ab7-db493a78cddb | -6.54 | -59.76573 | 2024-10-12 05:23:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 701cbfd3-3b60-3893-b372-24a664b444cb | -6.53946 | -59.76922 | 2024-10-12 05:23:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6059874f-4a55-3be6-93b8-59aa8b250744 | -6.53721 | -59.7617 | 2024-10-12 05:23:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e04355b7-1f7a-3d11-94e7-d0a228ee077b | -6.53666 | -59.7652 | 2024-10-12 05:23:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f088ae94-510f-30ed-82d9-4818b76a1035 | -6.52482 | -60.05992 | 2024-10-12 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f0216684-43fe-3b3e-ac2a-cdd85b60449e | -6.52204 | -60.05593 | 2024-10-12 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2b64f661-bed3-3052-a768-f235ae49f653 | -6.52149 | -60.0594 | 2024-10-12 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 60e69c07-1e04-32ed-9dd5-4616ef39e6ae | -6.51871 | -60.05541 | 2024-10-12 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2bdd6c5b-f15b-3605-866f-106885805dbc | -6.51817 | -60.05888 | 2024-10-12 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 16d9a597-6289-32ba-b4df-301baaa72fae | -6.51551 | -60.09766 | 2024-10-12 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 39d75a25-b852-3385-9826-552fc14fd2fa | -6.51484 | -60.05836 | 2024-10-12 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f943ef2b-c505-3e09-99f3-c3bbcaa3ba60 | -6.51218 | -60.09713 | 2024-10-12 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0e63ea6c-ce5d-3705-be90-498ef74bf0b6 | -6.51164 | -60.10061 | 2024-10-12 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1085b8dc-e158-3516-9e97-d06485c81b6b | -6.50323 | -60.06724 | 2024-10-12 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2c88b592-1e39-36a1-88ec-e3325da29aa0 | -6.50269 | -60.07071 | 2024-10-12 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7acd26c0-3ad4-3bc6-93c0-f10a1b27b440 | -6.49789 | -59.97757 | 2024-10-12 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fdc73c87-d994-30f7-b679-a3f973d2d522 | -6.49734 | -59.98106 | 2024-10-12 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 14fba0d4-83bb-39b6-ac67-75adb6c45978 | -6.48315 | -60.07147 | 2024-10-12 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8c6fdfec-fa27-3837-ad62-4592624a2cba | -6.68847 | -59.42823 | 2024-10-12 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 44531774-88e4-335c-b7ff-c41e1f79bfe8 | -6.68632 | -59.48596 | 2024-10-12 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4f85292e-62ce-37d8-8191-44ff7ae5468d | -6.68511 | -59.42771 | 2024-10-12 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9d1b2973-7a6e-31e3-bad1-1bd980b789e4 | -6.68296 | -59.48545 | 2024-10-12 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ab6c9409-e79c-3091-b207-4b99a668f6d5 | -6.68069 | -59.45602 | 2024-10-12 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1c28135f-5fa4-3fb9-9c12-da80ce8d8910 | -6.67734 | -59.4555 | 2024-10-12 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d66ee687-e16d-3c82-8ea6-233c510dc1c6 | -6.67678 | -59.45906 | 2024-10-12 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4073ea4e-1e2c-3299-b8da-da910a847cb0 | -6.67346 | -59.48034 | 2024-10-12 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8532ba64-1f32-3341-a6a7-fee700a7c780 | -6.67343 | -59.45854 | 2024-10-12 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d11f1255-0379-3566-890a-f898de461c9d | -6.67291 | -59.48388 | 2024-10-12 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 095ab87a-9c61-3a3d-9b8d-c54c6091e254 | -6.67236 | -59.48741 | 2024-10-12 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 277de1eb-00ce-3daf-a1d3-c7bf8e979a64 | -7.60526 | -60.58979 | 2024-10-12 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d884cd0e-1eb5-3e78-a40a-57a9203166a1 | -7.52062 | -60.65483 | 2024-10-12 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 68aa928c-4988-352a-a6ae-95b051aca563 | -7.25826 | -60.62736 | 2024-10-12 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6734d0a0-9476-392b-8712-60cca65be577 | -6.82455 | -59.36889 | 2024-10-12 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| af581c28-02cb-36bb-9eba-b48d01cac0df | -6.81074 | -59.13969 | 2024-10-12 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9c1c2902-db3e-38ea-9ef6-6b8d760415ef | -6.81018 | -59.1433 | 2024-10-12 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ccbe1df4-e587-3cf8-a2e7-97360eb0fd60 | -6.8068 | -59.14278 | 2024-10-12 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4b7bc364-fbb3-3df1-ba51-270fc4fd25f5 | -6.80677 | -59.12064 | 2024-10-12 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9d64b583-ff14-3dac-9996-bef5feda419b | -6.80621 | -59.12425 | 2024-10-12 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 98bbb2b3-3c0f-3b24-95d1-9e957e49cabe | -6.80283 | -59.12372 | 2024-10-12 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 40f5a467-600e-357a-9bf9-20320deb1f95 | -6.80146 | -59.33278 | 2024-10-12 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e8403655-8048-3d8d-af51-6416aba1508a | -6.7981 | -59.33227 | 2024-10-12 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b8a2bdcf-b06f-36c9-9cb8-c3144e07fa9f | -6.79754 | -59.33584 | 2024-10-12 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f9f523f7-4ef9-3f8b-abc6-59023fa082d3 | -6.79477 | -59.35364 | 2024-10-12 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 95ae4147-b298-3bd4-a35d-49ec77943a03 | -6.79473 | -59.33175 | 2024-10-12 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3598063e-9cc6-3523-b03a-2cc294f336c3 | -6.79417 | -59.33533 | 2024-10-12 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 17e30398-a320-386a-bfbf-5b7fa48a099f | -6.79362 | -59.33889 | 2024-10-12 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9244b545-372d-35d6-afb4-b8d1a03e97e3 | -6.7914 | -59.35313 | 2024-10-12 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| fe13432f-7641-3f28-9c71-4dbd91e153b3 | -6.79085 | -59.35669 | 2024-10-12 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 3263c2af-e664-3ddd-9049-ad68bb5d4972 | -6.78797 | -59.30877 | 2024-10-12 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 52dafd5a-f9b8-3edc-a466-7e3bbba79f55 | -6.78741 | -59.31234 | 2024-10-12 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ad6d7e04-7917-3746-937f-e8bb5efc2d12 | -6.78686 | -59.31591 | 2024-10-12 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5dd1ca59-0f4f-3cd0-b31a-1cc0ec27bc7e | -6.7846 | -59.30825 | 2024-10-12 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ac71615f-f6a5-3b57-8bda-a530f2a580c9 | -6.78405 | -59.31182 | 2024-10-12 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3501908f-a8e6-338a-8140-20c3e67b31a9 | -6.78349 | -59.3154 | 2024-10-12 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e47e05e8-afb8-355f-8beb-9f88f66d63f5 | -6.78012 | -59.31488 | 2024-10-12 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e5f5a7ce-5d8b-331d-a4ed-cfe72e2991c0 | -6.77709 | -59.2008 | 2024-10-12 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 084525d1-e58a-3723-9ca9-1dbfe7e4f058 | -6.77676 | -59.31436 | 2024-10-12 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b3b25669-2c10-37c1-8102-bb880107745f | -6.7762 | -59.31794 | 2024-10-12 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5d471315-0314-3685-b8f1-1bd4ea8ce010 | -6.77426 | -59.1967 | 2024-10-12 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 571cd8fd-0376-31c1-b323-2552cfd42f30 | -6.77339 | -59.31384 | 2024-10-12 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1bbad3f9-177c-3bbf-8225-3994962a78f4 | -6.77284 | -59.31742 | 2024-10-12 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3f709c73-b882-3c73-ad9b-e82e3139e8ae | -6.77229 | -59.32099 | 2024-10-12 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b3c94871-b04e-301f-a672-c36f1f7fa260 | -6.76947 | -59.3169 | 2024-10-12 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |


[Clique aqui para ver as próximas entradas](README109.md)
