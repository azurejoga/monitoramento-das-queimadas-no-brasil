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
| 363d5017-28bf-394a-9878-e7e5640b4e82 | -14.80274 | -46.64598 | 2026-08-18 06:48:00 | AQUA_M-M | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 17.6 |
| 8cb15d6c-f077-3500-ac22-17f37250e9d4 | -14.18368 | -52.8952 | 2026-08-18 06:48:00 | AQUA_M-M | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 12.6 |
| e81b9252-e983-330c-ac5b-a59c7317f720 | -14.35772 | -51.8689 | 2026-08-18 06:48:00 | AQUA_M-M | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 6.9 |
| f6903425-fb61-32fb-ab13-854da49e5614 | -14.25706 | -51.92419 | 2026-08-18 06:48:00 | AQUA_M-M | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 89ac020e-a2f3-340a-b380-7af1a2429076 | -8.57891 | -54.73935 | 2026-08-18 06:48:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 153.6 |
| 43f3151c-66c5-3cad-bb14-f4a14de4fa85 | -12.26417 | -51.5325 | 2026-08-18 06:48:00 | AQUA_M-M | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 0319b259-ce51-350d-8c92-e1c8ee61cb67 | -14.18019 | -52.91661 | 2026-08-18 06:48:00 | AQUA_M-M | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 88.9 |
| 9ddbaa9d-65ec-387e-827b-4c367ce202ef | -8.58464 | -54.70557 | 2026-08-18 06:48:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 55.4 |
| 92304c94-1a48-30b8-b2e1-ab61b4709878 | -12.53983 | -47.8444 | 2026-08-18 06:48:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 58.9 |
| 9fe66204-81d3-3f7b-a2cf-7c3edd09f314 | -11.3635 | -46.37436 | 2026-08-18 06:48:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| edfaabf1-1e44-3e72-a0b8-6ef0bec62616 | -14.24802 | -51.92271 | 2026-08-18 06:48:00 | AQUA_M-M | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 50.7 |
| 8895e2f6-c6e5-36cb-a755-2e4a47355fff | -14.17675 | -52.93769 | 2026-08-18 06:48:00 | AQUA_M-M | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 098787c6-0dec-3e6f-9d5b-7b03703cd20c | -8.58693 | -54.71772 | 2026-08-18 06:48:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 78.8 |
| 6876b7b3-3f51-3fa4-a974-80c99378f946 | -14.17424 | -52.8935 | 2026-08-18 06:48:00 | AQUA_M-M | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 31.9 |
| 7599193e-54a1-3a64-8b77-4d28c724a431 | -15.39749 | -51.07492 | 2026-08-18 06:48:00 | AQUA_M-M | BRITÂNIA | GOIÁS | Brasil | 5203807 | 52 | 33 | nan | nan | nan | Cerrado | 18.7 |
| e38200b8-3242-335a-894f-5427e0791f39 | -14.18192 | -52.90598 | 2026-08-18 06:48:00 | AQUA_M-M | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 150.8 |
| f237a258-93e3-3100-9555-446c02ce03f2 | -10.27274 | -50.41333 | 2026-08-18 06:48:00 | AQUA_M-M | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 028bd84c-99a5-3cb3-8712-b6a0edaf31f5 | -14.80149 | -46.63886 | 2026-08-18 06:48:00 | AQUA_M-M | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 20.5 |
| 46883eec-c19e-3dbe-adb5-e30e03a02cc7 | -15.39888 | -51.06584 | 2026-08-18 06:48:00 | AQUA_M-M | BRITÂNIA | GOIÁS | Brasil | 5203807 | 52 | 33 | nan | nan | nan | Cerrado | 65.1 |
| da9f13fe-f652-31f9-a35d-fe36af363857 | -11.36189 | -46.38608 | 2026-08-18 06:48:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.8 |
| ebdc368e-ee7f-3f3f-9aaf-cf4c2794e486 | -14.18795 | -52.92874 | 2026-08-18 06:48:00 | AQUA_M-M | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 90.0 |
| f09d6b1b-b38c-3702-a124-bc824564cd6c | -12.46587 | -54.18803 | 2026-08-18 06:48:00 | AQUA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 43ebdefd-f086-315b-9909-02c9d20ced24 | -12.75413 | -48.41489 | 2026-08-18 06:48:00 | AQUA_M-M | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 8216aa5c-a474-370a-8f26-16f70e990c9c | -14.169 | -52.92554 | 2026-08-18 06:48:00 | AQUA_M-M | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 22.6 |
| 48a74c58-2b67-3a9d-bc58-5d1252c6932e | -8.5728 | -54.70348 | 2026-08-18 06:48:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 73.5 |
| 2391f3b2-f6c0-3c61-9a57-737beb71c96d | -11.11012 | -46.4968 | 2026-08-18 06:48:00 | AQUA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| e42883db-af11-34bc-9275-d4dc2ac96f00 | -14.2017 | -52.9065 | 2026-08-18 06:50:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 56.9 |
| e4a425a6-a929-3239-94c6-26ffd4064782 | -14.8228 | -46.6419 | 2026-08-18 06:50:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 59.4 |
| df249d34-bd46-309d-96fa-e8ec1ee3dda9 | -14.1821 | -52.93 | 2026-08-18 06:50:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 107.8 |
| d0e673fd-0dbf-3974-8e70-683605f8aeee | -14.2014 | -52.9276 | 2026-08-18 06:50:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 67.3 |
| a1066d5b-e569-392e-a09e-9e360db88279 | -14.8033 | -46.6453 | 2026-08-18 06:50:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 65.9 |
| 9362a838-496b-3c38-abc5-8893ca40f6ef | -14.2566 | -51.9259 | 2026-08-18 06:50:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 45.9 |
| 3bad1b5b-61aa-36c0-bbb0-7a428f51734c | -6.7478 | -59.1716 | 2026-08-18 06:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 53.4 |
| 1165b135-b5e1-3ae4-8195-e9643fe80bd4 | -14.1828 | -52.8878 | 2026-08-18 06:50:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 52.8 |
| 2a6d9f6f-61d0-387e-94db-b38abe65a102 | -14.1631 | -52.9113 | 2026-08-18 06:50:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 53.1 |
| 3e3b8c94-8874-3ed4-b979-dcb3849a5ab3 | -14.1824 | -52.9089 | 2026-08-18 06:50:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 164.8 |
| a91037e4-e949-392d-a56c-5218e3ed3490 | -19.68348 | -49.01965 | 2026-08-18 06:50:00 | AQUA_M-M | COMENDADOR GOMES | MINAS GERAIS | Brasil | 3116902 | 31 | 33 | nan | nan | nan | Cerrado | 14.6 |
| a647d9da-f983-3700-a08c-d7f1e89fcca4 | -17.47529 | -48.86806 | 2026-08-18 06:50:00 | AQUA_M-M | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 12.4 |
| c9e3584c-c2c8-3cc6-8bb6-e984b3b6bf9b | -19.68199 | -49.03053 | 2026-08-18 06:50:00 | AQUA_M-M | COMENDADOR GOMES | MINAS GERAIS | Brasil | 3116902 | 31 | 33 | nan | nan | nan | Cerrado | 36.0 |
| f40a7215-2e26-3434-ac0b-7ded289aed14 | -20.29777 | -46.4686 | 2026-08-18 06:50:00 | AQUA_M-M | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 15.7 |
| feffe472-d995-3da1-b422-f03e41412bb2 | -14.1824 | -52.9089 | 2026-08-18 07:00:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 194.8 |
| 62ef20fd-0fb6-369d-b0b7-cdde814a629f | -14.1631 | -52.9113 | 2026-08-18 07:00:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 66.4 |
| 613d1cd3-1df6-3110-8660-f854ee953203 | -6.7478 | -59.1716 | 2026-08-18 07:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 62.3 |
| 07638d02-7c6a-3199-a2af-4f539ab2733b | -14.8233 | -46.619 | 2026-08-18 07:00:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 59.6 |
| 1db35fa7-6a4d-3fdc-a56b-9af4f00b8af9 | -14.1821 | -52.93 | 2026-08-18 07:00:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 80.5 |
| d78fda74-24b8-3fad-b538-622cef882c4e | -14.2017 | -52.9065 | 2026-08-18 07:00:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 63.1 |
| 9156eb4f-5559-3869-8a1a-457e223812c9 | -14.2566 | -51.9259 | 2026-08-18 07:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 62.1 |
| 2b581204-6cce-3303-bee9-cb973c9b2a36 | -6.841 | -59.0132 | 2026-08-18 07:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 39.1 |
| 2b6e7b21-7d85-32a7-965e-85009f632809 | -14.1828 | -52.8878 | 2026-08-18 07:00:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 96.1 |
| 7f2a4391-aee1-396e-ad71-5e6f52c103a2 | -14.1631 | -52.9113 | 2026-08-18 07:10:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 53.4 |
| bc30f8f2-3e97-32fa-9976-670377e1d8ca | -14.1824 | -52.9089 | 2026-08-18 07:10:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 108.5 |
| f3cd4a0d-11e3-31a7-80c7-3f54c9aecf10 | -6.7478 | -59.1716 | 2026-08-18 07:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 62.9 |
| 4de8e7bc-ddb8-354c-a15d-484257c75060 | -14.2566 | -51.9259 | 2026-08-18 07:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 48.1 |
| bd1caae6-eaa5-36c4-b5dd-6640a4071fa9 | -14.1821 | -52.93 | 2026-08-18 07:10:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 53.4 |
| 90ed0b07-a3ee-3384-aeb8-750f5b32b52c | -14.1828 | -52.8878 | 2026-08-18 07:10:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 65.5 |
| 8f7ff499-448c-3fe4-a6d0-7133b7963a17 | -8.57 | -54.73 | 2026-08-18 07:15:00 | MSG-03 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e9a10a3d-d462-37ce-bd10-74bb3510cb85 | -6.7478 | -59.1716 | 2026-08-18 07:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 53.8 |
| 3b26dc67-f6cf-3a86-9661-76bea22a0e25 | -14.2566 | -51.9259 | 2026-08-18 07:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 50.9 |
| d6c69c10-6b5d-3a76-bb35-901e4ad6b63b | -14.8228 | -46.6419 | 2026-08-18 07:20:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 69.0 |
| 76ab897f-3538-3f15-88d0-8bc199b047fe | -14.8233 | -46.619 | 2026-08-18 07:20:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 61.0 |
| d677a0c0-5c08-335e-a5b7-cd7565e11706 | -14.1821 | -52.93 | 2026-08-18 07:20:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 53.5 |
| dca45831-597d-3ac1-b9e8-b2c6d6c8d73a | -14.1824 | -52.9089 | 2026-08-18 07:20:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 101.2 |
| ab1184a9-aa76-31e9-a175-a98d40c0b379 | -14.1828 | -52.8878 | 2026-08-18 07:20:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 64.5 |
| 53e0bd5d-25e9-309f-a7b0-ddb5ef2a2438 | -6.7478 | -59.1716 | 2026-08-18 07:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 61.9 |
| 500c413e-3435-38ab-8a64-155ec670c581 | -14.1824 | -52.9089 | 2026-08-18 07:30:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 64.4 |
| 8559885e-97e4-38a3-99dc-5a9c3eed111c | -6.7478 | -59.1716 | 2026-08-18 07:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 58.7 |
| 75410de6-5588-390a-8b68-11920a77e5a0 | -14.1824 | -52.9089 | 2026-08-18 07:40:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 84.6 |
| 38f769fe-0e47-3fa9-b2ca-d724d4d522f1 | -14.2566 | -51.9259 | 2026-08-18 07:50:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 426.8 |
| eec3489e-60ee-3b55-84d0-89ce606d94aa | -6.7478 | -59.1716 | 2026-08-18 07:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 59.7 |
| e1560e93-860b-3dd7-9c32-c29b2d069400 | -14.1828 | -52.8878 | 2026-08-18 07:50:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 60.0 |
| bf03b307-148b-334d-abf3-0ebb8b5fed2d | -14.257 | -51.9046 | 2026-08-18 07:50:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 55.4 |
| d9dd1829-018d-3d1e-a2d3-326792e151d1 | -14.1824 | -52.9089 | 2026-08-18 07:50:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 97.1 |
| 5f6ecdeb-8cdd-38f4-8d76-64dc8d202c2a | -14.2562 | -51.9472 | 2026-08-18 07:50:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 103.9 |
| 40caef87-90d4-3c2e-a2ce-11049c6cd114 | -14.2373 | -51.9284 | 2026-08-18 07:50:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 105.9 |
| b41adfae-1d34-3392-a3a8-e191cbec0bc1 | -6.7478 | -59.1716 | 2026-08-18 08:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 53.2 |
| 856eed0a-c7ad-37d0-8627-44f15ffa6312 | -14.1828 | -52.8878 | 2026-08-18 08:00:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 57.1 |
| 97453ff0-d5ae-35f7-98e5-5ee8387a3c49 | -14.1824 | -52.9089 | 2026-08-18 08:00:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 100.3 |
| 2e187386-f413-3f56-99be-676675fa6729 | -14.2566 | -51.9259 | 2026-08-18 08:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 83.1 |
| b832aa02-4136-32aa-952a-53bc7da98b40 | -14.1828 | -52.8878 | 2026-08-18 08:10:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 70.7 |
| aef1a717-851c-3bac-8ccc-8a3bc1654cf2 | -6.7478 | -59.1716 | 2026-08-18 08:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 46.3 |
| 238506f6-79d6-391e-9934-f24afa14a80c | -14.1824 | -52.9089 | 2026-08-18 08:10:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 100.3 |
| 42574779-5b71-3334-827c-2613c2def086 | -8.57 | -54.73 | 2026-08-18 08:15:00 | MSG-03 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7e06f5cf-e2a6-3569-afd3-f53b61ac7850 | -6.7478 | -59.1716 | 2026-08-18 08:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 45.7 |
| 77bcbb57-3b4f-3060-8a3d-ca639700c37e | -14.1824 | -52.9089 | 2026-08-18 08:20:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 170.2 |
| b5c79e46-1748-3d22-9d22-abdb2fda93cb | -14.1635 | -52.8902 | 2026-08-18 08:20:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 138.6 |
| c41a47ed-6ea5-3cef-814a-517e7d3ae302 | -14.1828 | -52.8878 | 2026-08-18 08:20:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 232.4 |
| bf018a3f-d76b-3758-9895-ff1f563df70a | -14.1631 | -52.9113 | 2026-08-18 08:20:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 81.4 |
| e7cc66f8-69ba-33f4-807d-d539f6d976cc | -14.1828 | -52.8878 | 2026-08-18 08:30:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 154.5 |
| 57aa7e14-864f-3a12-a884-dabc2752e953 | -14.1821 | -52.93 | 2026-08-18 08:30:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 49.1 |
| e5ac1d3e-790a-3cd0-a121-dcb51f8f4b63 | -14.1635 | -52.8902 | 2026-08-18 08:30:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 119.6 |
| 46599738-cac5-3660-809a-01838ac87312 | -14.1631 | -52.9113 | 2026-08-18 08:30:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 94.6 |
| 4d19edf2-0b02-3d8c-b912-252c1e7b6d46 | -14.1824 | -52.9089 | 2026-08-18 08:30:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 150.8 |
| 24f311af-c5a9-327f-a7cc-d7182ee8be9c | -6.7478 | -59.1716 | 2026-08-18 08:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 42.0 |
| 9f8a7b36-e768-36c1-a28e-691331a6b7d5 | -14.1828 | -52.8878 | 2026-08-18 08:40:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 121.7 |
| 243e3d07-b665-3300-9d60-49465614008f | -14.1824 | -52.9089 | 2026-08-18 08:40:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 146.0 |
| 28dd9e6a-5a73-3b6d-bf2a-acc71d88ccf2 | -14.1821 | -52.93 | 2026-08-18 08:40:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 53.5 |
| 4fd28580-5aab-3cea-a982-770ee06886ed | -6.7478 | -59.1716 | 2026-08-18 08:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 51.3 |
| 2e1e97f6-99b9-3478-b61a-70694be3c0b6 | -14.1631 | -52.9113 | 2026-08-18 08:40:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 52.3 |
| eb65f734-8a59-310e-a10d-e39dabc0cc5e | -6.7478 | -59.1716 | 2026-08-18 08:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 46.8 |
| d11969ae-ccd4-3572-a667-d3f6d7897dd5 | -14.1821 | -52.93 | 2026-08-18 08:50:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 51.4 |


[Clique aqui para ver as próximas entradas](README63.md)
