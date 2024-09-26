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

## Dados Diários - Página 131

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 05ebda5e-cb29-3ad5-95d0-816cbf657d60 | -9.69714 | -58.08508 | 2024-09-26 04:59:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6de50f69-81f5-3027-ae41-fb57773fb21b | -9.69701 | -57.21393 | 2024-09-26 04:59:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 2ab646b7-800f-3d72-9071-5c4e2eefb5c5 | -9.69661 | -57.20199 | 2024-09-26 04:59:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| f3d45153-1ee3-3598-9ece-7b196f5afc79 | -9.69644 | -58.08926 | 2024-09-26 04:59:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7d4e37e7-0a47-3dcd-bfed-aeb338dfc075 | -9.69637 | -57.21778 | 2024-09-26 04:59:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e223a706-c433-3589-8c08-02515de24b00 | -9.69608 | -57.19809 | 2024-09-26 04:59:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 64197c16-8efd-3d03-8f46-cd9429ed0a48 | -9.696 | -57.20581 | 2024-09-26 04:59:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| fa167cda-55f2-3088-9b56-7e619cf3687e | -9.69545 | -57.20189 | 2024-09-26 04:59:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| b737d4d3-4f52-3e90-9aa2-26107678826e | -9.69482 | -57.20571 | 2024-09-26 04:59:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 3b72d200-cf9c-350d-98c8-7ab98bf9d5ff | -9.69476 | -57.21347 | 2024-09-26 04:59:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 1718ba91-e592-391d-b7b4-cd3ebed1739e | -9.69424 | -58.08031 | 2024-09-26 04:59:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| cc3cb39d-94bb-34af-984f-544d6a4bcfe7 | -9.69414 | -57.21731 | 2024-09-26 04:59:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ea87f970-ec0d-38ca-97d8-cb89a91d7770 | -9.69355 | -57.21335 | 2024-09-26 04:59:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 61ed238b-c724-3924-b3c3-32e9100e01e4 | -9.69354 | -58.08449 | 2024-09-26 04:59:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| da7017eb-2fa6-30d3-8009-72f13ce0359c | -9.69292 | -57.21718 | 2024-09-26 04:59:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6ae6ad66-50fd-3a85-beed-81a6d04df97b | -9.69284 | -58.08867 | 2024-09-26 04:59:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9dafda3d-215d-3505-b8d7-38bcca86000e | -9.69214 | -58.09286 | 2024-09-26 04:59:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f3228397-82f9-3da9-8afe-32cf4e185b2d | -9.69068 | -57.21671 | 2024-09-26 04:59:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4896505b-a6e1-3b48-8b36-fcab4970f567 | -9.68924 | -58.0881 | 2024-09-26 04:59:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3a784272-38cc-38ad-a2f4-6ae5d5521ca3 | -9.68439 | -57.21172 | 2024-09-26 04:59:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 89919690-f132-3e8e-9e4c-31e7c96ba427 | -9.65704 | -57.27066 | 2024-09-26 04:59:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ffd10bbf-2f3e-31fe-8311-4f0036ea154f | -9.6542 | -57.26621 | 2024-09-26 04:59:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fe607bf7-a001-39ad-9034-ebdcd22cf906 | -9.64902 | -56.95176 | 2024-09-26 04:59:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| acea0bd4-d369-3be4-a8b1-861e46cc6a13 | -9.6484 | -56.95554 | 2024-09-26 04:59:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6796b9e1-0ad1-3524-b0f4-7a6378d122fa | -9.64497 | -56.95498 | 2024-09-26 04:59:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6b4d6860-aafb-3a63-84e5-c30b635767ec | -9.63993 | -56.74694 | 2024-09-26 04:59:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| dde4edfc-0be9-3ad3-8109-516c41f24e3c | -9.62898 | -57.77424 | 2024-09-26 04:59:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6f530fa4-7f71-3857-bd52-33a6ea8a42e3 | -9.62292 | -56.74416 | 2024-09-26 04:59:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5977a45d-6fde-3f1b-8773-40305d957cf5 | -9.62232 | -56.74783 | 2024-09-26 04:59:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2ce6f155-fbdb-3bc5-812f-cf6f5372d94b | -9.62188 | -57.77309 | 2024-09-26 04:59:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 24f045d0-abb4-3657-b851-9efaa2febe3e | -9.62053 | -57.78117 | 2024-09-26 04:59:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 403ba66c-c0da-3b1a-80a5-fa23bd000dab | -9.62035 | -57.76042 | 2024-09-26 04:59:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| fcbd94b3-877d-3238-a4de-792541d753cc | -9.61968 | -57.76445 | 2024-09-26 04:59:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 409657bc-bd44-3fc9-ae77-655ee751b289 | -9.61951 | -56.74359 | 2024-09-26 04:59:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c92141e2-fd92-394e-af98-40d2c5f033e8 | -9.61901 | -57.76847 | 2024-09-26 04:59:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4524b7d8-e761-34ef-a79f-d9d602180b49 | -9.61833 | -57.77251 | 2024-09-26 04:59:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 88169f6d-ad00-3314-8799-f43be648014a | -9.61749 | -57.7558 | 2024-09-26 04:59:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 59e498f9-d264-345b-b8da-0277c53263ad | -9.61681 | -57.75983 | 2024-09-26 04:59:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 832ebb0c-cef1-3753-aab3-5540c269acb0 | -9.61614 | -57.76386 | 2024-09-26 04:59:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 40f92c5f-e165-30a4-bd77-c4f61a318f4f | -9.61546 | -57.76788 | 2024-09-26 04:59:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 359f9c33-6f4b-38a7-8209-8bbe69111895 | -9.61479 | -57.77193 | 2024-09-26 04:59:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0e9a9fb2-0809-3149-af62-7d192410e25b | -9.61327 | -57.75924 | 2024-09-26 04:59:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 670b0d7e-6c9a-3943-8c78-d6f6cc7ef512 | -9.61259 | -57.76326 | 2024-09-26 04:59:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 7c02e329-c972-38c4-bc91-97ea6beefdc1 | -9.61192 | -57.7673 | 2024-09-26 04:59:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 051e93f0-4ba7-3084-aa96-ce5af237c6d3 | -9.60525 | -56.81002 | 2024-09-26 04:59:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| db749983-ef43-3261-a5cc-351c3d4e76c8 | -9.60465 | -56.81375 | 2024-09-26 04:59:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f0fb297c-35db-3a3a-ac87-687f675fc303 | -9.60359 | -56.97197 | 2024-09-26 04:59:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 090f6415-d5e7-3b9a-8e3e-a180848a1aa0 | -9.58618 | -56.99242 | 2024-09-26 04:59:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0392ffd9-9b38-3d8e-b7fb-35269f8f4ac6 | -9.58557 | -56.99622 | 2024-09-26 04:59:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1c29aabc-ece8-3529-9661-36070c8b06b1 | -10.74912 | -57.55053 | 2024-09-26 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b1a87400-38e3-3c8d-885f-a92022ccbbf2 | -10.74629 | -57.54606 | 2024-09-26 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 028ce2d3-b5bc-3de7-9bbb-0989a91f6832 | -10.74565 | -57.54992 | 2024-09-26 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7077c207-02a6-3b4a-9350-478515811e3c | -10.74283 | -57.54543 | 2024-09-26 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 36ae8a62-1c06-3ce0-a284-e1dc0d186f03 | -10.74219 | -57.5493 | 2024-09-26 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9b172a17-3de2-3943-a400-6b3fae810509 | -10.73296 | -57.5283 | 2024-09-26 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 281011ff-864f-3494-aac9-9022aa5a12e0 | -10.73222 | -57.52359 | 2024-09-26 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 55d71ac8-71ef-3f52-9f16-c583fbfd1a50 | -10.73157 | -57.52746 | 2024-09-26 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 5653275f-43b2-3a98-b64b-510c81a64745 | -10.73043 | -57.54392 | 2024-09-26 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7003eeb5-5f4f-3237-9455-e61bc75cb591 | -10.73012 | -57.52387 | 2024-09-26 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1424784b-2a0b-3698-b2ae-2aed65b71c8a | -10.7295 | -57.52773 | 2024-09-26 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 084d92e3-96f9-3be1-aa0b-c79d6ca9c426 | -10.72897 | -57.54306 | 2024-09-26 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| dc5c01aa-3e0f-3c65-95f7-9a7b4975aae6 | -10.72759 | -57.53943 | 2024-09-26 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 037986a2-f51a-3aa5-8e80-7d6770a1d841 | -10.72696 | -57.54335 | 2024-09-26 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9884683e-9a8d-39e9-98d6-ab652d61a09c | -10.72603 | -57.52714 | 2024-09-26 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f60f3abc-e9b2-39c4-8e2a-17b52ae6630e | -10.72319 | -57.52269 | 2024-09-26 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4ce61e21-1745-3cfd-9257-98b59abd0fcb | -10.72256 | -57.52654 | 2024-09-26 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b0406b80-9af7-334f-ab1c-58df30cb13f3 | -10.66432 | -57.57714 | 2024-09-26 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e8dad0f8-298d-3429-a8d7-c0280d3e7271 | -10.64827 | -57.4588 | 2024-09-26 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f4746c66-5c94-353a-bd37-708e08970c0c | -10.64493 | -57.39897 | 2024-09-26 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 269d3892-d460-3d5d-853f-1b801412b164 | -10.64481 | -57.45824 | 2024-09-26 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4432b578-d9ab-3040-a316-0d0b29d622b8 | -10.64406 | -57.39872 | 2024-09-26 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 953d87ae-9bce-3f47-9b8e-87886dc4f350 | -10.64368 | -57.40667 | 2024-09-26 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 031d2fee-eec8-32ac-a778-bad6c8bd90c8 | -10.64342 | -57.40256 | 2024-09-26 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b01d026f-1751-32d0-9fbb-e0edc91b8119 | -10.64278 | -57.40641 | 2024-09-26 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 864ab8fa-b25d-3533-b6c7-e4169b002668 | -10.64213 | -57.41027 | 2024-09-26 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ea77990f-79ce-3328-9f7e-587d8f40da4e | -10.64148 | -57.39838 | 2024-09-26 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ffc38d54-51db-3585-a0d0-ad9dff559a09 | -10.6396 | -57.40993 | 2024-09-26 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4f811ea0-9ed1-38b4-bec5-6944528e782d | -10.63898 | -57.41381 | 2024-09-26 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d521456b-f84f-3111-af97-8d1924b4bb43 | -10.63865 | -57.39396 | 2024-09-26 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5dc5e618-38f0-31d6-916b-7bdf5865872b | -10.63802 | -57.3978 | 2024-09-26 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| cef3871d-45b7-33a0-bfe5-31c35b494483 | -10.63519 | -57.3934 | 2024-09-26 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4993fa4d-cc95-30d9-825f-dff1b26b3299 | -10.63174 | -57.39282 | 2024-09-26 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d8c98d97-c2bf-3f01-a2e6-65f4c51e6830 | -10.63143 | -57.41653 | 2024-09-26 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 039b95bc-2341-3ce6-9751-6ffe4d125393 | -10.63111 | -57.39666 | 2024-09-26 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e0ca4b5a-6e0e-327b-b71a-b0eafc2c27c0 | -10.62893 | -57.43192 | 2024-09-26 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3d336b9f-873f-3769-bceb-bb208185489e | -10.62547 | -57.43135 | 2024-09-26 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 78652609-c738-3090-a526-c63d3fe78310 | -10.6176 | -57.62152 | 2024-09-26 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c4dcc662-a414-32fb-9511-461eac9ca7f9 | -10.6151 | -57.38612 | 2024-09-26 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 728d9796-4b65-37a0-af12-1131bc5e08d6 | -10.5978 | -57.42675 | 2024-09-26 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4bb93f79-5665-318b-b634-123b4f411d9e | -10.55422 | -57.36807 | 2024-09-26 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b0ccab11-665b-3f2e-8b17-84583b3f1250 | -10.55359 | -57.37189 | 2024-09-26 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c29bf844-0c26-3fb6-a655-27dd3d0c4ad2 | -10.55077 | -57.3675 | 2024-09-26 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bf93c775-bea3-3027-a358-5d570c41f10a | -10.55013 | -57.37133 | 2024-09-26 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6ec401af-f9ff-3555-9419-df7645d57dc9 | -10.53665 | -57.3736 | 2024-09-26 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fa05bf12-83cf-3b0e-a43b-e18245a83df0 | -10.52754 | -57.36417 | 2024-09-26 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d17b6bf4-ea4e-3396-8478-36b3e401c792 | -10.52691 | -57.36803 | 2024-09-26 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3645ea61-da05-3049-a8df-004eb40349f2 | -10.48986 | -57.37762 | 2024-09-26 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| be61a18f-0f83-366e-b45d-58cd8951adf0 | -10.48923 | -57.38147 | 2024-09-26 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4008e0ac-5e25-3f35-a421-ed4c80dadb6d | -10.4886 | -57.38533 | 2024-09-26 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 80469df0-c654-3193-b1ed-75f8dcc42512 | -10.48514 | -57.38476 | 2024-09-26 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |


[Clique aqui para ver as próximas entradas](README132.md)
