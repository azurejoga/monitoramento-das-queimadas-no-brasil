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

## Dados Diários - Página 86

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6d5f3947-9e08-340d-8760-b7373c76fef3 | -9.122 | -65.77489 | 2025-08-28 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 14aafc48-fd5b-3ed5-a66a-b4e3dbffa735 | -9.14992 | -59.56982 | 2025-08-28 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 64b3f8ae-3ea2-3943-ad61-20df371f7c4b | -8.88024 | -62.48146 | 2025-08-28 05:48:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 97b05f3b-1cc7-3db5-80e2-6400ee88a29f | -10.03534 | -59.36024 | 2025-08-28 05:48:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b4a4e1a3-0380-31d8-b241-43314b9ee028 | -8.89504 | -62.47217 | 2025-08-28 05:48:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f3c06765-9a33-3d2e-bab8-5fa1155127da | -8.90043 | -60.59557 | 2025-08-28 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a5f57f65-0dae-3742-a2dc-9bc5cb975b31 | -8.96226 | -65.97231 | 2025-08-28 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f4d1ea67-2331-34f3-a587-4c1e5c0bd3b9 | -9.3105 | -57.703 | 2025-08-28 05:48:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 339aae2d-b378-39c8-9ba3-f32e9f593505 | -8.94363 | -65.95821 | 2025-08-28 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9609d01d-4e24-31e2-9066-07268fee3f71 | -9.1237 | -65.78654 | 2025-08-28 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 16.9 |
| 01bd9cbe-785c-31c6-bf8d-5212065e387c | -7.50086 | -60.30701 | 2025-08-28 05:48:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b18ddbb3-8839-317c-94c7-c7bee37f1965 | -9.07409 | -66.06425 | 2025-08-28 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a6ec58e0-44be-3a81-9049-920f5dde63fa | -7.41291 | -60.62049 | 2025-08-28 05:48:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 002891ef-b74d-32a6-b869-6b9c1b2f6646 | -9.3959 | -60.52532 | 2025-08-28 05:48:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5ba8efaf-3c47-3d0e-9eb1-2cbf8d3764f6 | -7.37253 | -64.37177 | 2025-08-28 05:48:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 3c753fc4-8727-3c05-b851-49972fc00536 | -9.10553 | -60.32424 | 2025-08-28 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ed20af6e-4897-3656-ad51-4b4378ec9350 | -9.16097 | -65.79565 | 2025-08-28 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 05949997-8cfe-384a-a92a-b0a08b37a1be | -8.94136 | -65.95039 | 2025-08-28 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 09429c4e-9fc8-3a17-a853-1fb583c41d6b | -10.07871 | -62.90079 | 2025-08-28 05:48:00 | NOAA-20 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| daaf4677-c5f9-3c83-bd4a-fc141d8293de | -10.46111 | -57.95699 | 2025-08-28 05:48:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 061d4232-88e7-3faa-ace2-276f872f82b1 | -9.48419 | -62.38344 | 2025-08-28 05:48:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 84cdd090-5723-3bab-8759-a75c2e380e26 | -7.44639 | -63.15871 | 2025-08-28 05:48:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4b98470b-ae29-3129-b5da-a1ba7e1759de | -7.46655 | -61.40333 | 2025-08-28 05:48:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a017d42a-5f46-37cf-bb22-18e645b999c2 | -8.2893 | -45.1586 | 2025-08-28 05:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 89.3 |
| eead79f9-e0ae-38b2-a975-4f1cdc8a9602 | -9.1153 | -65.8073 | 2025-08-28 05:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 59.0 |
| c096f6ed-78fe-3f30-aaa3-2ef7ec991a88 | -10.4738 | -57.9366 | 2025-08-28 05:50:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 57.0 |
| 12c8cd92-a4ae-3b7d-88f1-6d68634ebc78 | -10.8049 | -60.7644 | 2025-08-28 05:50:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 58.0 |
| 2f4751d5-4164-3955-8375-0a5506996f03 | -9.1155 | -65.7699 | 2025-08-28 05:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 90.4 |
| b03b9eb1-ecbb-34d2-be6e-93f374165113 | -14.3485 | -53.3504 | 2025-08-28 05:50:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 56.2 |
| b2b2a879-0a77-32de-ad5a-dbdf57ef753f | -9.1338 | -65.8067 | 2025-08-28 05:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 43.7 |
| 50e1608e-79df-3726-b765-ec5e2d889446 | -6.4355 | -44.5764 | 2025-08-28 05:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 60.2 |
| 65433a59-5e54-3b54-b14f-a89ee0aeba6d | -9.1154 | -65.7886 | 2025-08-28 05:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 310.3 |
| 1b33f512-efcf-3757-b446-c17c0ebb0c51 | -8.289 | -45.1814 | 2025-08-28 05:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 78.0 |
| 9078baae-a93c-3170-8c56-21aa97a4a9f2 | -9.1339 | -65.788 | 2025-08-28 05:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 208.7 |
| 620c1474-dd9f-3c38-b309-aaeaa0b75fcb | -9.134 | -65.7694 | 2025-08-28 05:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 68.4 |
| 914febbb-55a3-38a8-89f6-decbaa4eefad | -12.9662 | -44.5781 | 2025-08-28 05:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 53.3 |
| 4be55d4e-dcb5-3c27-8fd7-93746ac284a8 | -8.3082 | -45.1566 | 2025-08-28 05:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 70.0 |
| 062e7d40-e8e5-36e6-929c-2ee27d5e6da1 | -10.3273 | -46.7821 | 2025-08-28 05:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 62.8 |
| cb871778-80d3-3368-99cd-3889be851618 | -6.8772 | -43.6152 | 2025-08-28 05:50:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 85.2 |
| 486e01aa-ea81-352e-910c-620ed9cf2612 | -10.25656 | -64.499 | 2025-08-28 05:50:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 80b53206-aa98-3f6b-9085-22a1df120354 | -10.80235 | -60.76166 | 2025-08-28 05:50:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 359678ae-4158-38a2-a913-f686ffef24d7 | -10.72748 | -69.10692 | 2025-08-28 05:50:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 65511472-5e6f-3ba2-96cc-456f0a299a40 | -10.2602 | -64.49956 | 2025-08-28 05:50:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b8db19c0-9c2e-3477-954b-d864ea89f5fd | -11.36171 | -63.2645 | 2025-08-28 05:50:00 | NOAA-20 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a91c8316-2d78-3126-a068-30fd847bf3a4 | -9.74646 | -67.69723 | 2025-08-28 05:50:00 | NOAA-20 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 4.2 |
| e3bc2774-11ae-3e6d-bc1e-d9449093dabb | -10.42821 | -64.37361 | 2025-08-28 05:50:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9925474b-bf01-3c5f-8984-693fc2b02997 | -10.78784 | -60.79926 | 2025-08-28 05:50:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 63a6dbf5-47b1-356d-8c76-fd14f133f71b | -14.76634 | -59.74302 | 2025-08-28 05:50:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 76ea0ad1-3946-391d-a984-ebe7f764c2e3 | -11.36568 | -63.26508 | 2025-08-28 05:50:00 | NOAA-20 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e24b67e1-9d0e-3da6-b738-3f9baca991c8 | -10.17533 | -69.00928 | 2025-08-28 05:50:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 71ed1474-cf7f-3148-949e-3556fa78c158 | -11.35774 | -63.26394 | 2025-08-28 05:50:00 | NOAA-20 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e7b6e971-4a6b-3e56-b64a-e9f73a65c25e | -9.94464 | -67.81872 | 2025-08-28 05:50:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2634e730-0394-36b0-8518-fd25b4bae0da | -10.93828 | -63.63174 | 2025-08-28 05:50:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| cabfce8b-b473-3950-958c-bb8d42dcba09 | -9.36955 | -71.03416 | 2025-08-28 05:50:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f9d0e61b-6142-385d-a906-5384022cfa83 | -10.56355 | -69.81004 | 2025-08-28 05:50:00 | NOAA-20 | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 9215f374-b2b4-3df0-9b1a-cac7cdb0169d | -10.79109 | -60.77504 | 2025-08-28 05:50:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 17.9 |
| c329fcaa-db96-3a0f-be7b-8e0a5ef6997b | -10.73083 | -69.10748 | 2025-08-28 05:50:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d4ede8f1-e6b4-3a72-8504-aa5fe46b7694 | -12.22324 | -64.22575 | 2025-08-28 05:50:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 949982ce-86c7-3331-bf65-e8a784d000a9 | -11.36175 | -63.27285 | 2025-08-28 05:50:00 | NOAA-20 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ce4af827-c1ee-3e9e-a176-985c0c1097f4 | -10.81964 | -60.77398 | 2025-08-28 05:50:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1d3605b2-c835-301f-bb8b-be38d8f9e051 | -10.81565 | -60.76843 | 2025-08-28 05:50:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 154fcfbe-cf5f-322b-a47b-a279c0b15b47 | -9.54489 | -68.58174 | 2025-08-28 05:50:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 18605d89-a6a9-3189-bf55-c1ad77eef74f | -10.7977 | -60.76104 | 2025-08-28 05:50:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 1ff767f3-2f3a-3077-9e69-71d74de780af | -10.17591 | -69.00569 | 2025-08-28 05:50:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7f019c3a-9087-3614-b8d1-8c8f5d0c0c5f | -11.35853 | -63.26712 | 2025-08-28 05:50:00 | NOAA-20 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8650e083-5caa-3806-afae-7449678d9532 | -10.15116 | -68.57079 | 2025-08-28 05:50:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 68f4c0b2-dce4-38ef-a26c-bad90a17fba6 | -10.27601 | -64.49322 | 2025-08-28 05:50:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0354b38a-b608-3e9d-91fc-87eb2cf9bd5b | -10.15059 | -68.57433 | 2025-08-28 05:50:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| fb4afee3-ccfe-39ce-89f1-af1c100fbec4 | -10.80701 | -60.76228 | 2025-08-28 05:50:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 12.1 |
| dd54134a-db24-3d29-bd28-df8cab42b8e0 | -14.32064 | -60.37142 | 2025-08-28 05:50:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4c6a9e45-36db-3a96-9965-08b796e90c6e | -10.82099 | -60.76406 | 2025-08-28 05:50:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 8db0382b-fd31-3fd7-a3e5-6cd4ec7fa2c8 | -10.47186 | -67.8141 | 2025-08-28 05:50:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7373011c-382b-3e21-9f1d-40d87bd1481d | -14.31523 | -60.37387 | 2025-08-28 05:50:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2f624ea5-ee0d-3fd4-9eff-97df4dac2a06 | -10.58538 | -68.25557 | 2025-08-28 05:50:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 4e5399b8-e0cd-3870-8b96-a16fc1b2e1e6 | -14.766 | -59.74596 | 2025-08-28 05:50:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 19979825-b542-3526-97fc-2aa15ab237fb | -10.0088 | -68.84293 | 2025-08-28 05:50:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fd5faeda-1412-3c3f-9e21-563040e9e77a | -13.00762 | -56.90864 | 2025-08-28 05:50:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6c0a8a13-c5c4-3e49-a545-064bc926e5d8 | -9.58382 | -68.57358 | 2025-08-28 05:50:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6eab948a-edee-39e8-a9a5-e702d92da9ef | -11.36029 | -63.27485 | 2025-08-28 05:50:00 | NOAA-20 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 4.1 |
| cd6d041d-7690-32f6-8aee-104376cacc69 | -13.00145 | -56.90773 | 2025-08-28 05:50:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| ba33a540-8582-3c48-b982-bfb1d84ffac8 | -11.36645 | -63.26827 | 2025-08-28 05:50:00 | NOAA-20 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d1b33e15-458d-3eb7-934b-2d728dac20ad | -10.79573 | -60.77568 | 2025-08-28 05:50:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 380b97ed-810c-3d30-bc91-f4ee26f08ccb | -11.36249 | -63.26769 | 2025-08-28 05:50:00 | NOAA-20 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 16d28c66-18d5-3f96-b36a-c01ce031762f | -13.00705 | -56.91357 | 2025-08-28 05:50:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5f130b2a-ed97-3620-a44a-271a48c7670d | -10.58594 | -68.25208 | 2025-08-28 05:50:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 6b005c90-84db-3465-990f-4f716e9e802e | -9.75093 | -67.86242 | 2025-08-28 05:50:00 | NOAA-20 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 51c9794c-95f5-3843-bc06-e47560b87143 | -10.83288 | -60.81549 | 2025-08-28 05:50:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 5d1f11da-30cc-324b-ba02-2b1d591f7861 | -12.99529 | -56.90677 | 2025-08-28 05:50:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 8349df62-73e7-310d-a17c-5baa5ef6eaaf | -10.79704 | -60.76593 | 2025-08-28 05:50:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 9.2 |
| df1d0462-da28-3c82-ae94-4a1145ed4735 | -10.08689 | -68.46297 | 2025-08-28 05:50:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d2f0cbc1-4600-3326-9c50-62e878114712 | -10.25594 | -64.50324 | 2025-08-28 05:50:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b1d2f134-bd9c-38da-a53a-7302a9d464e7 | -10.80634 | -60.7672 | 2025-08-28 05:50:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 37333faf-faf1-37ef-b5e6-c09acb345dbb | -10.19147 | -68.42551 | 2025-08-28 05:50:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 61c6a920-5ab1-3db3-b002-89bd42a17dff | -10.17926 | -69.00624 | 2025-08-28 05:50:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 55c86df4-ba76-3967-b09f-d55cc4a574c9 | -10.31008 | -68.44832 | 2025-08-28 05:50:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f86f17a2-f1d1-3ca4-8968-6586b6373a90 | -14.32064 | -60.37008 | 2025-08-28 05:50:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f2464dee-f1d4-3abf-8c83-a333eee09b75 | -10.56416 | -69.80627 | 2025-08-28 05:50:00 | NOAA-20 | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e3e3b3a0-d825-37d5-bce6-293bb18a4d06 | -12.22703 | -64.22632 | 2025-08-28 05:50:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5ab1f322-2dee-3fc8-b611-34b7efa86796 | -10.09625 | -68.48979 | 2025-08-28 05:50:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b07807bb-51ad-36de-98d7-118a6c9c98f9 | -10.20194 | -68.44526 | 2025-08-28 05:50:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |


[Clique aqui para ver as próximas entradas](README87.md)
