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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b7fcbf22-2daf-3a39-958a-75a4f3c63ed4 | -17.6457 | -57.5668 | 2024-11-29 02:10:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 49.3 |
| 27fa9d19-4c2b-3b93-a5b5-a4b6f9f8ddd5 | -2.966 | -53.2824 | 2024-11-29 02:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 153.8 |
| bf412afc-36e7-3581-a74c-2439e546b1d9 | -2.1351 | -54.906 | 2024-11-29 02:10:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 65.2 |
| 1c9572dc-2c45-3fb4-a07e-82de538c0421 | -2.9844 | -53.3022 | 2024-11-29 02:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 213.0 |
| c46edd92-c4c8-32c0-bb16-9a512f513276 | -3.259 | -53.6388 | 2024-11-29 02:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 52.7 |
| a7c0f04d-83e1-326d-9aff-3bfc406a76ba | -1.6074 | -52.6181 | 2024-11-29 02:10:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 92.4 |
| fa6981ef-72f6-30ee-b147-5cf209f6e7c5 | -4.4405 | -46.5754 | 2024-11-29 02:10:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 133.3 |
| 119a28e4-11fd-3a84-a75d-fe7cef85122c | -2.966 | -53.3027 | 2024-11-29 02:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 114.7 |
| 678eb3e8-4555-3ab0-b9d8-e5d13375a2de | -5.0399 | -43.6205 | 2024-11-29 02:10:00 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 70.4 |
| 104d6cb7-3d28-3766-a1d5-b265fff647db | 1.2171 | -55.9471 | 2024-11-29 02:20:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 178.8 |
| a47f201a-2b78-3b70-9d59-c5851150aa02 | -2.8611 | -46.8186 | 2024-11-29 02:20:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 63.3 |
| 39ba5e8a-8240-37aa-9939-ea618a2a3066 | -3.3439 | -46.6912 | 2024-11-29 02:20:00 | GOES-16 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 90.5 |
| c49d5c8a-b669-351c-9031-f1df58b6d343 | -2.8665 | -45.5304 | 2024-11-29 02:20:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 71.0 |
| 523e7ad1-c111-3947-8895-aaa07db3fdcb | -1.9541 | -46.4471 | 2024-11-29 02:20:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 92.4 |
| e4bf4e55-c4e6-39ef-bc84-04d4c96f5d56 | -4.4405 | -46.5754 | 2024-11-29 02:20:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 146.9 |
| 6578c7ff-4926-3185-85a2-0972ef365e07 | -4.4404 | -46.5975 | 2024-11-29 02:20:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 94.9 |
| 4ef1847e-ca87-329e-9a74-8606026a2d83 | -3.0028 | -53.2815 | 2024-11-29 02:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 65.8 |
| 13502874-a8a7-3faa-b71e-941d97f334e4 | -17.5805 | -42.7483 | 2024-11-29 02:20:00 | GOES-16 | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 99.2 |
| 6a970bf5-563c-3c8e-a5ac-8376d55be6a9 | -2.9844 | -53.3022 | 2024-11-29 02:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 174.4 |
| 9e87c9e2-6dda-3223-b529-3120aebbfd51 | 1.2172 | -55.9274 | 2024-11-29 02:20:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 48.8 |
| cd5f44af-ed10-3b17-b69b-45db01438404 | -2.3419 | -46.8781 | 2024-11-29 02:20:00 | GOES-16 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 72.6 |
| 44537be3-e175-36b5-87e2-a690f0c65980 | -2.6684 | -48.7767 | 2024-11-29 02:20:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 300.5 |
| 100e9ca0-4b38-3036-9425-fe74f0ee54f1 | 1.1988 | -55.9669 | 2024-11-29 02:20:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 82.6 |
| 12373af3-2ebc-303e-961d-83eac3b61fa3 | 1.2354 | -55.9469 | 2024-11-29 02:20:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 84.4 |
| 1c7318af-5f24-3eb7-9ade-344ef8fe8166 | -1.092 | -53.3954 | 2024-11-29 02:20:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 58.8 |
| a42c75c8-d13a-3ba0-9873-5225c1c2595c | -17.6007 | -42.7434 | 2024-11-29 02:20:00 | GOES-16 | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 77.8 |
| 6028e675-7858-3b41-8919-e2c53265647a | -2.6498 | -48.7986 | 2024-11-29 02:20:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 131.3 |
| 5b528bbd-7674-340a-adfc-af234818a766 | -2.6499 | -48.7772 | 2024-11-29 02:20:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 142.3 |
| 160460de-527f-3056-b82d-e1aae82d58a3 | -2.966 | -53.3027 | 2024-11-29 02:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 94.7 |
| 64127f90-0665-360c-99c9-314434f7cc3b | 1.1988 | -55.9472 | 2024-11-29 02:20:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 58.7 |
| a2b9e500-ea41-3010-9b48-31bcf0ec986a | -1.6074 | -52.6181 | 2024-11-29 02:20:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 49.5 |
| ced45a9c-bab0-30e8-91d8-e3406ddd5532 | 1.2171 | -55.9667 | 2024-11-29 02:20:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 156.8 |
| c8c6eb7b-9ef1-3aad-8bd5-30d83eb15b5e | -2.8425 | -46.8193 | 2024-11-29 02:20:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 68.9 |
| 479e198f-1c3e-3d2f-b5d7-bb1b1537f73e | -1.6997 | -52.4535 | 2024-11-29 02:20:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 44.4 |
| 85ea8235-3141-3932-b941-59ee79132013 | -2.9844 | -53.2819 | 2024-11-29 02:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 318.4 |
| 2a3d9a7f-6078-3565-95e0-3b99541b6309 | -2.6683 | -48.7981 | 2024-11-29 02:20:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 271.8 |
| 30e15474-8f0f-3f0d-9976-8db251a81301 | -2.966 | -53.2824 | 2024-11-29 02:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 158.2 |
| 399893c8-31ff-39f4-9b7c-d12762bc3097 | -3.196 | -46.5644 | 2024-11-29 02:30:00 | GOES-16 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 62.3 |
| b6e53b9b-fcf3-3ae0-bd19-1afe43cb57ba | 1.2354 | -55.9469 | 2024-11-29 02:30:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 82.6 |
| b7c8f11b-6876-3f54-a83a-5c74bee13976 | 1.8583 | -55.8018 | 2024-11-29 02:30:00 | GOES-16 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 56.7 |
| 2bb7dd78-b41e-33bc-8ca0-a949e934d00e | -1.9726 | -46.4467 | 2024-11-29 02:30:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 83.3 |
| 301ae769-0b80-37c9-9304-913ab960f34a | -3.3253 | -46.692 | 2024-11-29 02:30:00 | GOES-16 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 73.9 |
| dbff3204-86ae-3d7e-933c-9fb2344b6402 | -2.9844 | -53.2819 | 2024-11-29 02:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 272.0 |
| 7ef70a59-3972-3487-ac2e-df09b208f540 | 1.2172 | -55.9274 | 2024-11-29 02:30:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 56.7 |
| ac32a3fd-be33-3f81-bf50-fc3038fe9c26 | 1.1988 | -55.9669 | 2024-11-29 02:30:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 55.6 |
| fb491afc-4c94-36db-834d-a5b6a391d6c9 | -2.6684 | -48.7767 | 2024-11-29 02:30:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 298.3 |
| f210cfba-a055-3e32-8d06-1c1624a41190 | -2.966 | -53.3027 | 2024-11-29 02:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 92.8 |
| fd2d52db-0931-39c1-9091-776fadb4d3d9 | -2.966 | -53.2824 | 2024-11-29 02:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 128.0 |
| 1ed65abc-145a-39a2-a6af-f615c2a2c0fc | 1.2171 | -55.9667 | 2024-11-29 02:30:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 86.1 |
| dfdf64ab-8b1c-33ae-836c-e24cca58c48a | -17.5805 | -42.7483 | 2024-11-29 02:30:00 | GOES-16 | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 90.6 |
| bce2ab61-1f6b-3bcf-b4cc-3334b8e9cf83 | -1.092 | -53.3954 | 2024-11-29 02:30:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 52.7 |
| d764b620-272f-3253-aed1-61320eb70078 | -3.3439 | -46.6912 | 2024-11-29 02:30:00 | GOES-16 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 87.3 |
| 2398f957-033d-397b-9cee-a16821c93652 | -5.0399 | -43.6205 | 2024-11-29 02:30:00 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 73.8 |
| debe58f8-298c-30e6-b2c7-b746e700a8b8 | -1.9541 | -46.4471 | 2024-11-29 02:30:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 140.8 |
| 038ee574-f681-33fa-a962-96fd3ee126a5 | -2.6499 | -48.7772 | 2024-11-29 02:30:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 131.0 |
| b40e56d1-5595-3fa1-8ae0-7fd32113bc61 | -2.9844 | -53.3022 | 2024-11-29 02:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 191.8 |
| dffe9494-543b-3779-aa02-ebf3b52f5364 | -1.6997 | -52.4535 | 2024-11-29 02:30:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 47.5 |
| 5d7cdde4-2f22-3bd4-af2d-7a6dc6f0d5a0 | -4.4404 | -46.5975 | 2024-11-29 02:30:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 85.1 |
| c4d8130e-33a2-3ada-a0e7-ad2dba1ba5e7 | -2.8611 | -46.8186 | 2024-11-29 02:30:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 63.8 |
| 0e521800-0864-3262-bb2c-5d85e250abac | -4.4405 | -46.5754 | 2024-11-29 02:30:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 168.3 |
| 4b344da9-a6c2-374f-807a-61d37f177f07 | -2.8425 | -46.8193 | 2024-11-29 02:30:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 67.0 |
| 7ec26ee0-f9bd-32fc-99ff-ed0bb613ec82 | 1.2171 | -55.9471 | 2024-11-29 02:30:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 165.1 |
| 55da7ae0-84f8-3bca-8776-7fa299984aec | -2.6498 | -48.7986 | 2024-11-29 02:30:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 139.3 |
| d6c8264b-74c7-3590-bcb2-b499a152e13f | -17.6007 | -42.7434 | 2024-11-29 02:30:00 | GOES-16 | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 75.2 |
| 3922d2e9-d7ba-332d-abc8-01d8275b39d6 | -2.6683 | -48.7981 | 2024-11-29 02:30:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 320.0 |
| 736befde-cf75-3e43-9d24-80bd2cbad7e5 | -2.3419 | -46.8781 | 2024-11-29 02:30:00 | GOES-16 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 72.2 |
| 0411640a-a092-3972-bf47-24c13f41f013 | -5.0399 | -43.6205 | 2024-11-29 02:40:00 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 72.1 |
| 7fcab9a8-97d1-3592-b729-538683a4d0ae | -2.6683 | -48.7981 | 2024-11-29 02:40:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 309.9 |
| 16c48189-2fc6-3f6a-9e47-2bc16f6f613c | -3.0028 | -53.2815 | 2024-11-29 02:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 51.9 |
| 818a9ac1-b7d3-338e-ba8a-d2faa84f7289 | 1.2354 | -55.9469 | 2024-11-29 02:40:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 51.9 |
| b6187349-e674-35ff-a8a2-f05dd20fcdbf | -2.6499 | -48.7772 | 2024-11-29 02:40:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 143.7 |
| c049f09c-e397-35f0-af33-07b798070a42 | -3.3439 | -46.6912 | 2024-11-29 02:40:00 | GOES-16 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 70.7 |
| 87f98ab0-9b83-3dde-9142-f65d0d7578d2 | -2.9844 | -53.3022 | 2024-11-29 02:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 180.4 |
| 9f7b0b33-6480-34bf-bf9f-16ea546054a1 | -2.9844 | -53.2819 | 2024-11-29 02:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 243.8 |
| db0e5f5c-306e-3c24-a8e2-d9978e1dfcbe | 1.2171 | -55.9471 | 2024-11-29 02:40:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 97.4 |
| 98def190-4387-3b61-a346-593fc2780d13 | -18.7777 | -54.1284 | 2024-11-29 02:40:00 | GOES-16 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 77.8 |
| 83c457f5-e501-3fab-bac1-2e3fec036b62 | -4.4405 | -46.5754 | 2024-11-29 02:40:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 162.9 |
| 1da7df45-316a-3835-8025-315d39ff3b15 | 1.8399 | -55.8218 | 2024-11-29 02:40:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 54.5 |
| 496ba128-9f96-318b-8388-81b8627871fa | -2.8611 | -46.8186 | 2024-11-29 02:40:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 63.2 |
| c832887a-cf3d-3e35-be01-0d01ec652816 | -1.9541 | -46.4471 | 2024-11-29 02:40:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 117.1 |
| 988d00be-622f-3b99-a254-d162450befdd | -1.6997 | -52.4535 | 2024-11-29 02:40:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 51.4 |
| 905afc94-91e6-3cdf-8e75-8139ce093dea | -2.8665 | -45.5304 | 2024-11-29 02:40:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 68.5 |
| ad1f4549-b556-30aa-958f-de10a24ccc5b | -17.6007 | -42.7434 | 2024-11-29 02:40:00 | GOES-16 | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 75.8 |
| bd565098-2e8a-3717-9906-8e70bfcff835 | 1.84 | -55.8021 | 2024-11-29 02:40:00 | GOES-16 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 68.0 |
| 6c6d2af2-c09f-35de-b23d-45e69a28b3ca | -2.966 | -53.2824 | 2024-11-29 02:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 127.6 |
| 0a237824-c1b4-39bd-ba3e-0e990be73c70 | -17.5805 | -42.7483 | 2024-11-29 02:40:00 | GOES-16 | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 91.5 |
| e4dd65d3-80aa-3806-a910-48d1d2403de5 | -2.6684 | -48.7767 | 2024-11-29 02:40:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 286.4 |
| 70918dfa-db91-3606-8148-667fed063121 | 1.8583 | -55.8018 | 2024-11-29 02:40:00 | GOES-16 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 74.4 |
| 75cda62f-b054-383c-a218-cf6650592cde | -4.4404 | -46.5975 | 2024-11-29 02:40:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 82.9 |
| 6d1a4935-9dfc-3f95-9b62-2e0d65dd085c | -2.6498 | -48.7986 | 2024-11-29 02:40:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 155.9 |
| 2dfa817d-a05e-3c52-bd5a-3a7b4a77c7cd | -2.966 | -53.3027 | 2024-11-29 02:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 97.5 |
| f04547d0-292f-357e-a165-1f43fe4e5eab | -2.3419 | -46.8781 | 2024-11-29 02:40:00 | GOES-16 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 68.3 |
| 238dfdf5-8b49-3d11-a7ff-39f920ec5100 | 1.2171 | -55.9667 | 2024-11-29 02:40:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 64.1 |
| 5739fd10-c134-33d5-a85f-99623242408c | 1.8767 | -55.7424 | 2024-11-29 02:40:00 | GOES-16 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 50.5 |
| cae3f306-9539-31c1-ac17-67b87339c611 | -1.9726 | -46.4467 | 2024-11-29 02:40:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 79.8 |
| a2972faf-491c-3cf9-b1d9-0fd744074c8f | -1.092 | -53.3954 | 2024-11-29 02:40:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 53.3 |
| f1d52e09-7ddc-334f-9e56-a49ca3fd9ae6 | 1.84 | -55.8021 | 2024-11-29 02:50:00 | GOES-16 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 67.0 |
| 92585113-f43e-3f2a-b514-454b6c30036f | -1.9541 | -46.4471 | 2024-11-29 02:50:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 82.5 |
| d22b970b-adcf-3b80-acd1-1948c789b06e | -4.4405 | -46.5754 | 2024-11-29 02:50:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 144.9 |
| 9d9e7770-0246-3357-a702-5098d8559b40 | -2.966 | -53.2824 | 2024-11-29 02:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 141.7 |


[Clique aqui para ver as próximas entradas](README15.md)
