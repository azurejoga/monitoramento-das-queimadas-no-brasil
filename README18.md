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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e1e0a1e0-c365-3d02-8757-c6583a61a8ad | -2.6208 | -48.06865 | 2024-11-21 04:08:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e4da2651-4122-377c-9eb8-0046cefc1f75 | -0.93697 | -51.71766 | 2024-11-21 04:08:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 51b2e811-a0dd-3a7e-b265-72b2317836a9 | -3.4602 | -52.72189 | 2024-11-21 04:08:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| aef2301d-ba0c-3480-9da7-7b74abecc4e5 | -3.54258 | -51.60764 | 2024-11-21 04:08:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7b2156b5-1e9f-38b6-a164-65a6b3853b74 | -3.81284 | -51.35436 | 2024-11-21 04:08:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e4777570-0bb6-33ae-8eba-1344a26c94b6 | -1.41713 | -45.8252 | 2024-11-21 04:08:00 | NOAA-21 | GODOFREDO VIANA | MARANHÃO | Brasil | 2104305 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7341e586-e9ab-3e7c-b3c6-9bbc7fe6d6bc | -4.18413 | -53.57952 | 2024-11-21 04:08:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0275a202-cb93-3f90-b28b-731fe2cb3553 | -4.35259 | -41.23504 | 2024-11-21 04:08:00 | NOAA-21 | DOMINGOS MOURÃO | PIAUÍ | Brasil | 2203420 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| e1b3cac5-e783-3cee-b794-469b4e8a63b1 | -4.34535 | -42.56181 | 2024-11-21 04:08:00 | NOAA-21 | MIGUEL ALVES | PIAUÍ | Brasil | 2206209 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| cb8c7988-54ef-35d8-adf7-e1a37bebea29 | -4.8188 | -45.75478 | 2024-11-21 04:08:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 415f1f4b-f38c-36a2-882c-87793dfd67dc | -4.90726 | -37.41179 | 2024-11-21 04:08:00 | NOAA-21 | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 74e3e673-5101-33b7-b4a5-ea9d416a810b | -4.08555 | -49.28967 | 2024-11-21 04:08:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 6a2b50c7-dbb0-32ab-8520-51f3d5ee68ff | -2.63984 | -46.21881 | 2024-11-21 04:08:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 89d1791a-b521-31c3-8419-4f87a96ea495 | -3.64069 | -51.45477 | 2024-11-21 04:08:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| bd4f9412-2549-3701-96e1-3319a6b046a2 | -3.27936 | -50.21561 | 2024-11-21 04:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 8066eb31-81aa-3fce-b91b-716953f1f4fe | -1.13976 | -53.67176 | 2024-11-21 04:08:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| c08ca53c-177a-39b0-a609-7ddf217b8ab2 | -3.50435 | -44.71749 | 2024-11-21 04:08:00 | NOAA-21 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6554e624-6bb7-366a-99b1-42129d48ded7 | -3.23715 | -51.30067 | 2024-11-21 04:08:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d206f338-ee90-3d8c-b154-6a3ba08ec3fa | -4.3954 | -45.60027 | 2024-11-21 04:08:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 865463d8-efde-3b13-a722-371fbb4396ad | -6.20148 | -37.43312 | 2024-11-21 04:08:00 | NOAA-21 | BELÉM DO BREJO DO CRUZ | PARAÍBA | Brasil | 2502003 | 25 | 33 | nan | nan | nan | Caatinga | 2.7 |
| dd82a947-22c8-3f7c-a81b-5030f5e697fb | -6.51523 | -40.59244 | 2024-11-21 04:08:00 | NOAA-21 | PARAMBU | CEARÁ | Brasil | 2310308 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 290addcd-9cf7-3377-b751-d150857b637a | -1.08797 | -48.21255 | 2024-11-21 04:08:00 | NOAA-21 | SANTO ANTÔNIO DO TAUÁ | PARÁ | Brasil | 1507003 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c5c46c13-e342-3b14-ad68-626371e73ad3 | -2.02331 | -47.00196 | 2024-11-21 04:08:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 4a821309-7c6a-397d-8743-c3033a130c6f | -2.51453 | -47.22985 | 2024-11-21 04:08:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| caa47dbb-5ac4-3981-8591-2eb44e05486e | -3.53679 | -50.44419 | 2024-11-21 04:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| fde82e1f-729e-32a3-9756-696a031487ea | -6.20311 | -46.222 | 2024-11-21 04:08:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| e72caf44-3713-3ebf-9ea4-72cae6b18274 | -4.95975 | -49.84534 | 2024-11-21 04:08:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 244b3e91-941d-321f-8380-65794de0b17f | -2.88177 | -52.44606 | 2024-11-21 04:08:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b0ddb885-8b7d-3625-812a-79151f74419c | -2.19994 | -53.66217 | 2024-11-21 04:08:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 15.8 |
| dec6731b-db3e-390b-82c3-9806cb38eb54 | -5.76228 | -45.78636 | 2024-11-21 04:08:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 31e23007-fda3-32f6-8e14-9cb600ccf756 | -3.55135 | -50.1706 | 2024-11-21 04:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 96272329-e166-3c5f-a838-af3e4fa1a13c | -5.01493 | -41.95701 | 2024-11-21 04:08:00 | NOAA-21 | JATOBÁ DO PIAUÍ | PIAUÍ | Brasil | 2205276 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 39054823-b5f3-3d56-b76a-de0132b296a2 | -0.9627 | -46.80018 | 2024-11-21 04:08:00 | NOAA-21 | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4512775d-7e5d-3fad-a3a2-d01de2406092 | -4.35042 | -45.88255 | 2024-11-21 04:08:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fa968d10-7b89-364b-8611-8490fe02f7ef | -5.62192 | -46.75245 | 2024-11-21 04:08:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 614bc268-2d58-3551-bc23-e13e090316d5 | -3.59026 | -43.63594 | 2024-11-21 04:08:00 | NOAA-21 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 335f221e-6906-3907-8b04-39c470f8a814 | -3.27205 | -53.83026 | 2024-11-21 04:08:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 01ecc552-864c-35d9-a4c3-7a4b400e0522 | -4.24752 | -46.11823 | 2024-11-21 04:08:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 52.7 |
| 90bca11d-a482-3ab9-8878-6bb53320eff8 | -2.55754 | -46.54569 | 2024-11-21 04:08:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4a8e39fa-0b89-3a56-b965-a2f029d7b6dc | -4.25243 | -49.08643 | 2024-11-21 04:08:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a4b77f4a-03df-37be-8f87-d742c0fb0573 | -3.00383 | -51.01738 | 2024-11-21 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b570e575-87a2-3cad-9b39-37b2ddddd11b | -3.51509 | -50.22543 | 2024-11-21 04:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 82b48f95-851c-3468-b46c-3fc90064aa08 | -4.22505 | -47.17912 | 2024-11-21 04:08:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0bf4d004-a392-3495-ae27-60111db61c0c | -2.45157 | -46.14394 | 2024-11-21 04:08:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3e1c9b32-e2d2-34df-ba7c-99575aab07d7 | -1.92828 | -46.60223 | 2024-11-21 04:08:00 | NOAA-21 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9a77f3bc-a502-30a7-b104-7e9bc10a6368 | -4.24411 | -46.11412 | 2024-11-21 04:08:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 3b78a2d3-e82d-38e3-99d5-d52f83d0139f | -2.45664 | -47.03119 | 2024-11-21 04:08:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1dc573bb-3fa0-3016-a561-b52c62129e1a | -0.96063 | -51.72616 | 2024-11-21 04:08:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 131daf2b-faf1-3d55-906b-7874391c8112 | -3.17964 | -54.31973 | 2024-11-21 04:08:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 35aa4a56-0a88-3dbb-9685-ef47f8353aae | -5.44569 | -45.58369 | 2024-11-21 04:08:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 646124d9-e63d-368e-b3a5-60ce9549f231 | -4.88821 | -45.83989 | 2024-11-21 04:08:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1ca50add-2ecf-308d-87ca-079a9fe23209 | -2.94578 | -48.3312 | 2024-11-21 04:08:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 898d29c6-1b38-3dbd-93b5-58e9142af6ff | -2.61683 | -51.80238 | 2024-11-21 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 058a655d-4528-3b31-921b-a744d866e06b | -2.43786 | -46.53541 | 2024-11-21 04:08:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1dca573a-ef00-358d-a224-1c1ee61dac7b | -3.19087 | -46.55032 | 2024-11-21 04:08:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4a37b136-e305-303f-a139-3fc5ba3abf61 | -0.80014 | -51.78284 | 2024-11-21 04:08:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6ca7c00b-133b-3eb8-acc1-436953370fb6 | -3.49183 | -50.44746 | 2024-11-21 04:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 9fde442d-b511-3d59-b389-eed1411e404d | -5.41387 | -46.443 | 2024-11-21 04:08:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 28677cfe-e10e-331f-afce-858a540bf4ab | -2.62439 | -47.96027 | 2024-11-21 04:08:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 94f509f3-b54d-308f-9fa1-8391a26a810c | -2.18576 | -52.12715 | 2024-11-21 04:08:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| b576a522-31aa-301f-a1db-b20549cc5454 | -1.22801 | -51.74427 | 2024-11-21 04:08:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 79916603-963a-3acb-9735-cfeb14860f11 | -6.12023 | -42.52069 | 2024-11-21 04:08:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 13.0 |
| bbbb8aba-89dc-3279-b858-9766bd890774 | -3.19321 | -45.03458 | 2024-11-21 04:08:00 | NOAA-21 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b02f1ce0-14d7-3c41-9e4a-9a6ac32c6d27 | -3.03199 | -49.46938 | 2024-11-21 04:08:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 31b20c5f-b902-32e4-81d4-78d308931c94 | -1.78229 | -53.59739 | 2024-11-21 04:08:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| f9249c94-51da-36cd-9598-a90998e560b0 | -2.93633 | -48.32971 | 2024-11-21 04:08:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4d575c02-dca7-3fe8-8ea0-718d56086e1a | -4.0321 | -43.23932 | 2024-11-21 04:08:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1d29c85b-9541-3913-afd5-e941af936059 | -2.8904 | -48.27403 | 2024-11-21 04:08:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e84d29dc-f5cb-3a34-ad1c-30c6c3cd926b | -3.51362 | -54.68982 | 2024-11-21 04:08:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| ef94bc53-8567-3782-b310-8e66a3fa23f2 | -2.40384 | -48.60794 | 2024-11-21 04:08:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c4c1832d-748c-3fda-883b-4c7ef263beb6 | -4.62993 | -49.54361 | 2024-11-21 04:08:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c633c25f-95b8-383b-8d74-01abd310dab0 | -4.95355 | -47.80638 | 2024-11-21 04:08:00 | NOAA-21 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6f2eb283-b3b0-3d2a-88bc-56b84cddbd11 | -2.0239 | -54.53443 | 2024-11-21 04:08:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 26.1 |
| 0fbc413c-0829-3033-b38f-d24f0f22adce | -2.6847 | -46.24846 | 2024-11-21 04:08:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ba8712b9-eea7-3464-bafc-074ea38501c0 | -4.66465 | -46.4003 | 2024-11-21 04:08:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 46d59e9c-7556-3e2c-bc0d-5a7a28412aa7 | -5.22119 | -44.90918 | 2024-11-21 04:08:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5baa3fd0-778b-3565-b02b-72d201939162 | -5.81388 | -43.80043 | 2024-11-21 04:08:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 070d7820-f447-3651-9062-6455e82bee88 | -5.9486 | -44.2474 | 2024-11-21 04:08:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 2c598c82-dbdc-34b0-897c-9d8652c359ea | -4.18593 | -46.83137 | 2024-11-21 04:08:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 920cce86-f881-3e07-87e2-71e591694215 | -3.64642 | -51.45588 | 2024-11-21 04:08:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 72bb24d8-0291-3adb-bff5-dfee3ec2febf | -5.52066 | -43.32666 | 2024-11-21 04:08:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 656f19f5-6dcc-3359-b9b2-7b69b9e1db29 | -3.42603 | -53.2892 | 2024-11-21 04:08:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 80d707c8-9259-32fe-bc8d-e3ce38f57267 | -0.94848 | -51.71951 | 2024-11-21 04:08:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 441980c3-b2a1-3e9f-9fd3-f022c697426a | -3.1714 | -49.15602 | 2024-11-21 04:08:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 02346f4a-9c36-381b-809f-693d0986892d | -1.73229 | -52.39623 | 2024-11-21 04:08:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 9fc1f299-652d-39a6-8d28-085c3c341423 | -3.33465 | -50.49814 | 2024-11-21 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 936a18f1-f516-35b9-a501-9128a188472d | -2.01801 | -54.52597 | 2024-11-21 04:08:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 30.3 |
| 76f56dad-094a-3268-8582-06b8d4e33a94 | -1.22996 | -47.3592 | 2024-11-21 04:08:00 | NOAA-21 | NOVA TIMBOTEUA | PARÁ | Brasil | 1505007 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9ff378a2-b726-33ba-aebe-a4329cbf161b | -3.80869 | -47.79799 | 2024-11-21 04:08:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 8216fdb7-ce1e-36ff-98cf-012a0d5d5883 | -3.14 | -49.12929 | 2024-11-21 04:08:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 404d4ca0-07ce-38c4-a30b-2dfb354eaa52 | -4.91427 | -46.83974 | 2024-11-21 04:08:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7a56e232-123d-3d64-803d-a0dc1a3a5a0e | -4.09823 | -46.10297 | 2024-11-21 04:08:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6e826102-7e30-35d2-9d3a-d97ec7f82694 | -1.29442 | -52.22343 | 2024-11-21 04:08:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 783cd516-7614-3509-9efd-1beda2b2a3f3 | -5.42935 | -45.34461 | 2024-11-21 04:08:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| fa735a9d-5aef-349e-af02-48435c4ab8d8 | -3.28131 | -48.80371 | 2024-11-21 04:08:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0a33e3eb-31bc-349d-87b8-d790e901f721 | -3.72993 | -52.31628 | 2024-11-21 04:08:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| dbf0f04a-6bf4-3e64-bc9d-04bb26035645 | -2.8318 | -46.67556 | 2024-11-21 04:08:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 68108c62-d108-3502-868b-0c20aad0d80f | -0.94841 | -51.72424 | 2024-11-21 04:08:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 28084193-3600-3ebd-b66c-4512117cef4d | -0.29366 | -51.60804 | 2024-11-21 04:08:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| be9fac1a-c515-354d-8e25-84c006480545 | -4.14953 | -43.88465 | 2024-11-21 04:08:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 10.4 |


[Clique aqui para ver as próximas entradas](README19.md)
