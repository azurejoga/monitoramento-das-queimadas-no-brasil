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

## Dados Diários - Página 31

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7a13f19c-ea58-3707-9e62-35533ccf3272 | -12.7557 | -44.4959 | 2026-07-01 07:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 73.8 |
| aa834cc9-c696-3f2e-9b13-ba8df38ddcb0 | -12.8359 | -44.3422 | 2026-07-01 07:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 226.7 |
| bcc3459c-9fe4-3836-8e6e-a4f6e3988593 | -12.8552 | -44.3389 | 2026-07-01 07:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 111.4 |
| e600490d-38d5-3e34-a71c-955746c72148 | -12.8359 | -44.3422 | 2026-07-01 07:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 172.5 |
| 3a05d49e-6536-3b6e-aa90-101b3b137223 | -12.7557 | -44.4959 | 2026-07-01 07:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 77.3 |
| 8a2d5581-96bb-3d1e-aae7-a025c1ae6486 | -12.7755 | -44.4693 | 2026-07-01 07:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 85.1 |
| ef7e3d8e-3eaa-3bbe-95de-472e268d35d5 | -12.8354 | -44.3657 | 2026-07-01 07:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 92.3 |
| e597e50c-dc23-3fc5-85ce-6777f83f2ff4 | -12.8552 | -44.3389 | 2026-07-01 07:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 108.8 |
| 5e82c33c-2684-3592-9c11-53542e69159c | -12.8548 | -44.3625 | 2026-07-01 07:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 59.5 |
| 2b55ddc9-f5c0-37b9-901a-4d1e8bbec05b | -12.7562 | -44.4724 | 2026-07-01 07:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 53.6 |
| 36f99364-da15-3b49-a2c3-bd42d9a04bce | -12.7751 | -44.4927 | 2026-07-01 07:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 147.5 |
| f72d3773-2c8e-391b-bc2a-3b0371c1aee8 | -12.8552 | -44.3389 | 2026-07-01 07:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 89.8 |
| 08444626-f24e-3a91-a026-b80e7f47cc5c | -12.7562 | -44.4724 | 2026-07-01 07:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 44.9 |
| ddc5f0c9-2f4f-37b0-9ffb-848f2b06cc29 | -12.8354 | -44.3657 | 2026-07-01 07:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 106.6 |
| eb44164a-5a94-3e0c-9bda-91adb3b266dd | -10.9209 | -43.0384 | 2026-07-01 07:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 55.5 |
| 076ed281-23d9-3814-815f-f0feca488f8c | -10.6784 | -54.5356 | 2026-07-01 07:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 49.7 |
| 1380bd7f-d55e-37f2-bd03-9e4cb5491d40 | -12.8359 | -44.3422 | 2026-07-01 07:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 220.2 |
| 6fc660b7-f21d-38d3-adb3-5ad3028e15f4 | -12.8548 | -44.3625 | 2026-07-01 07:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 44.9 |
| ac53eadd-0922-323a-9929-2fca9dda7bd8 | -12.7557 | -44.4959 | 2026-07-01 07:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 68.8 |
| 04b5b064-000d-3cab-9158-d52e4848b40e | -12.7755 | -44.4693 | 2026-07-01 07:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 85.2 |
| 4f6339d0-9cbd-3531-8082-d2dea002302f | -10.6787 | -54.5153 | 2026-07-01 07:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 44.1 |
| 0130428b-12d2-3d69-a115-37db26bd4c79 | -12.7751 | -44.4927 | 2026-07-01 07:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 130.5 |
| 07bf80fa-1907-364c-84cd-3acee9cd4cf4 | -11.63384 | -59.0132 | 2026-07-01 07:29:00 | AQUA_M-M | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 24.5 |
| efd9949a-2e8e-30f6-b4bb-11ddbcdf1628 | -9.17448 | -58.06401 | 2026-07-01 07:29:00 | AQUA_M-M | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 8f31c15e-269e-3345-9467-f809392f495f | -9.60327 | -56.91873 | 2026-07-01 07:29:00 | AQUA_M-M | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 17.3 |
| 56433aea-499e-3a8d-bb04-727b1bb267cc | -12.4123 | -58.402 | 2026-07-01 07:29:00 | AQUA_M-M | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 7.1 |
| a6a31ae8-b3fd-3c61-9a6e-314c4cb8dce9 | -11.63071 | -59.007 | 2026-07-01 07:29:00 | AQUA_M-M | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 76ce2b5f-1663-3ed7-948a-78d8227ef85f | -9.02507 | -59.53312 | 2026-07-01 07:29:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 1cfe3cbc-73e4-3e2f-ac7f-b2a5cf53bff2 | -10.6686 | -54.53061 | 2026-07-01 07:29:00 | AQUA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 66.6 |
| 105009ff-d034-3a3b-8a80-a462b8b871ea | -10.66094 | -54.52241 | 2026-07-01 07:29:00 | AQUA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 18.2 |
| 527fb59d-acb7-3eea-bc08-2ce2a4d71d8e | -11.42849 | -56.05909 | 2026-07-01 07:29:00 | AQUA_M-M | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 75.5 |
| e00e8c46-0cd2-35ee-abc4-31769ff0f214 | -10.6714 | -54.50791 | 2026-07-01 07:29:00 | AQUA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 46.7 |
| c6c8e1ed-2e12-3ce1-bda4-edda7086f3ae | -11.63235 | -59.02403 | 2026-07-01 07:29:00 | AQUA_M-M | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 72e12706-0b95-3502-aa04-d6f17e790e33 | -11.62914 | -59.01791 | 2026-07-01 07:29:00 | AQUA_M-M | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 25.6 |
| 462c917d-f3b3-3245-89b7-3293205375d2 | -10.6744 | -54.52414 | 2026-07-01 07:29:00 | AQUA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 78.8 |
| 2459fd66-2475-3184-9b4b-0933116af219 | -12.42415 | -58.3913 | 2026-07-01 07:29:00 | AQUA_M-M | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 14.5 |
| aad3384b-412e-3468-9e1a-8acbe4f3fb80 | -12.41398 | -58.38977 | 2026-07-01 07:29:00 | AQUA_M-M | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 0345906c-3531-3c97-b34c-e0ec4f31d0cd | -12.8548 | -44.3625 | 2026-07-01 07:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 64.6 |
| 54780c5d-b549-3caa-889e-053f9201b562 | -12.8354 | -44.3657 | 2026-07-01 07:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 88.0 |
| 3a2ed05d-a9af-3772-9879-95a93653e2c8 | -12.7557 | -44.4959 | 2026-07-01 07:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 79.3 |
| a88ca807-1a7a-3170-88b4-650ca4438ed7 | -12.8552 | -44.3389 | 2026-07-01 07:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 121.1 |
| 95091cdc-2f68-388e-ab93-40b7f39c00a5 | -12.8359 | -44.3422 | 2026-07-01 07:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 175.3 |
| ca0c1e24-13ec-3673-af2c-78446ae45fa0 | -12.7755 | -44.4693 | 2026-07-01 07:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 63.0 |
| acdd1987-6d1d-3330-9a42-de487024ca28 | -12.7751 | -44.4927 | 2026-07-01 07:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 109.1 |
| eda30e11-15ca-3b23-a778-9d2182697be8 | -12.7562 | -44.4724 | 2026-07-01 07:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 51.0 |
| 55cbbdd1-929a-3af2-bd3b-6e3bb29bb04d | -16.3587 | -56.65061 | 2026-07-01 07:31:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 28.3 |
| 3effa002-4023-3642-9463-b4d0856b1059 | -16.36155 | -56.65609 | 2026-07-01 07:31:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 34.0 |
| b1b03a5b-726f-3cc0-a4da-06385d9ecd60 | -12.7557 | -44.4959 | 2026-07-01 07:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 81.5 |
| 283bb009-3d3c-36db-a98b-e70dd224f79c | -12.8359 | -44.3422 | 2026-07-01 07:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 212.3 |
| 0445fda7-ea92-3d0a-93e6-1f14a89e3408 | -12.8552 | -44.3389 | 2026-07-01 07:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 83.8 |
| d002fc1d-0a41-3ae7-844f-c84c7df40003 | -12.7751 | -44.4927 | 2026-07-01 07:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 134.3 |
| 5f4c45a5-2ce4-3b80-b96e-bd93487dce46 | -12.8354 | -44.3657 | 2026-07-01 07:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 94.7 |
| a5674c5e-8430-3391-8757-e3646fecca9f | -12.7755 | -44.4693 | 2026-07-01 07:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 57.1 |
| 00f0eb19-d523-3a84-b9c3-9cb541a6dc0d | -10.6784 | -54.5356 | 2026-07-01 07:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 45.7 |
| 0b76c07a-7466-3cc6-a1b7-c509ae33889a | -12.8552 | -44.3389 | 2026-07-01 07:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 77.8 |
| 4e0152e1-2433-3c29-87af-9b217947ba15 | -12.7751 | -44.4927 | 2026-07-01 07:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 152.5 |
| 863a9c16-a54a-3180-ab22-02727fd23dda | -12.7557 | -44.4959 | 2026-07-01 07:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 54.6 |
| ec015371-8397-36d7-9637-f2245c164f05 | -12.7755 | -44.4693 | 2026-07-01 07:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 66.1 |
| f1acd41e-d7c4-33bf-95db-04a86c18bc02 | -12.8354 | -44.3657 | 2026-07-01 07:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 91.2 |
| e5e4d0f7-df08-3d75-9291-e456ca6532c1 | -12.8359 | -44.3422 | 2026-07-01 07:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 220.0 |
| f94afbdd-6c30-358a-9904-1697253513f0 | -12.7755 | -44.4693 | 2026-07-01 08:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 51.1 |
| e48b709b-6980-3c87-b662-99fb2373163f | -12.8552 | -44.3389 | 2026-07-01 08:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 103.9 |
| 94ef204d-028b-334f-9974-391c0fbdeccb | -12.8359 | -44.3422 | 2026-07-01 08:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 171.8 |
| d5134a26-b0eb-31e9-9007-1d84d914d1e1 | -12.7557 | -44.4959 | 2026-07-01 08:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 60.5 |
| e16fdfb9-961e-37d2-a1bb-01e39a320c0a | -12.8354 | -44.3657 | 2026-07-01 08:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 77.1 |
| ebf64108-36f0-3dc7-b484-27b0b1b51d4b | -12.8548 | -44.3625 | 2026-07-01 08:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 47.7 |
| 43f446f0-2022-3329-be2f-6b693a8d293f | -12.7751 | -44.4927 | 2026-07-01 08:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 128.0 |
| 558d861d-1978-3368-b577-dac60912d004 | -12.7751 | -44.4927 | 2026-07-01 08:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 133.6 |
| d5505d40-2d4a-3726-8c6b-4f361309a09f | -12.8552 | -44.3389 | 2026-07-01 08:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 62.1 |
| c7cf22ba-a0eb-3a93-add6-d83d31f8d349 | -12.8354 | -44.3657 | 2026-07-01 08:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 100.3 |
| c893b6a2-fa52-3dda-84db-921c962fdb22 | -12.7755 | -44.4693 | 2026-07-01 08:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 62.4 |
| 09ec4fb8-c2e1-383d-940f-8c686353fbab | -12.8359 | -44.3422 | 2026-07-01 08:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 176.2 |
| e8a8a0e0-2361-320a-9e6b-12100ecee5af | -12.7557 | -44.4959 | 2026-07-01 08:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 55.4 |
| 78964b69-89b9-3a76-9989-43af9ea08c29 | -12.8359 | -44.3422 | 2026-07-01 08:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 177.3 |
| 3eb17a7e-f5d0-3d74-a8b6-381aa924b640 | -12.7755 | -44.4693 | 2026-07-01 08:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 66.9 |
| 70c26de4-5b31-32e3-b52f-3e4c2f7ed14f | -12.8552 | -44.3389 | 2026-07-01 08:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 61.8 |
| 970ce996-45a2-3b5e-bf81-b77b3a1c3eb0 | -12.8354 | -44.3657 | 2026-07-01 08:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 104.2 |
| 11ff399c-866b-3ce9-8157-7ac252e577b4 | -12.7751 | -44.4927 | 2026-07-01 08:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 122.1 |
| 817a42df-6acc-3098-97b9-9ada06656ae5 | -12.7755 | -44.4693 | 2026-07-01 08:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 53.1 |
| 95a9e42f-817c-30f2-83c5-ff6ecba49bec | -12.7751 | -44.4927 | 2026-07-01 08:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 124.4 |
| 192e1222-b54c-37cd-8a00-3f6216fe5f7e | -12.8359 | -44.3422 | 2026-07-01 08:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 185.6 |
| 785d3c50-6800-3918-ae38-93ad875db50a | -12.8354 | -44.3657 | 2026-07-01 08:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 80.6 |
| 58013498-0287-37ee-b0fb-d939442d3bb7 | -12.8552 | -44.3389 | 2026-07-01 08:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 68.3 |
| 113d153c-dffb-302c-9392-0d7ac6627e3f | -12.7751 | -44.4927 | 2026-07-01 08:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 112.5 |
| 067b6b15-300a-3cdb-a553-50d1f8ea9a52 | -12.8359 | -44.3422 | 2026-07-01 08:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 172.9 |
| 5627ec9b-0e7c-3e53-88f9-1b307de9e3d8 | -12.7557 | -44.4959 | 2026-07-01 08:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 55.9 |
| 1fcd188b-5f79-3741-b332-ba9960ae1f70 | -12.8354 | -44.3657 | 2026-07-01 08:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 72.6 |
| 55cb64f0-df3a-3c69-84c6-b4b9e38178f7 | -12.7755 | -44.4693 | 2026-07-01 08:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 47.2 |
| eddefb89-26d7-3259-9610-ec3088c4d30b | -12.8552 | -44.3389 | 2026-07-01 08:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 57.7 |
| 0369d48d-ff8e-3f9e-bd82-503fdd753a21 | -12.8359 | -44.3422 | 2026-07-01 09:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 128.1 |
| 7df861f2-f8a2-3dff-9a00-f1cac93581e1 | -12.8359 | -44.3422 | 2026-07-01 09:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 138.1 |
| 6653c568-e774-37d5-99ef-005c5e55edeb | -12.8359 | -44.3422 | 2026-07-01 09:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 107.6 |
| 396877ff-de3a-3814-abda-d0b649dedb51 | -12.8359 | -44.3422 | 2026-07-01 10:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 136.6 |
| b132c159-51de-347b-a3bd-ed353554141a | -12.8359 | -44.3422 | 2026-07-01 10:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 125.7 |
| 32520fb7-8dbc-3996-80c9-631aa45aeb0d | -12.8359 | -44.3422 | 2026-07-01 10:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 112.1 |
| 3ac7a736-28d4-3c1c-8ac0-ce6b00f971c3 | -12.8359 | -44.3422 | 2026-07-01 10:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 113.1 |
| 340555f7-e789-3e55-aea0-c30eb8461c00 | -12.8359 | -44.3422 | 2026-07-01 10:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 104.6 |
| 8ef93b16-c399-3315-b9d8-1f8c050cdc97 | -12.8359 | -44.3422 | 2026-07-01 10:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 113.4 |
| a2092f64-1ccd-302a-8612-a5036ba0442f | -12.8359 | -44.3422 | 2026-07-01 11:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 121.4 |
| 825a9a98-a975-3025-ba84-51cf5bc67448 | -9.0175 | -45.7397 | 2026-07-01 11:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 85.8 |


[Clique aqui para ver as próximas entradas](README32.md)
