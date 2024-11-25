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

## Dados Diários - Página 45

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7062b96e-160f-3943-95c9-8a8cfbdcf9ac | -1.06323 | -53.19904 | 2024-11-25 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 953ac4f3-4fc1-3586-9bc4-60b56e1bfb14 | -2.69208 | -52.91051 | 2024-11-25 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a8480d18-684f-3276-b7e1-2fb61357de6b | -1.21063 | -51.74052 | 2024-11-25 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 31e93c54-9d11-355b-86f3-3df41cab130a | -3.39814 | -53.79815 | 2024-11-25 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 35d27b35-3ec9-32a9-acb5-2b2cb9405abb | -1.19222 | -51.77029 | 2024-11-25 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ab203d22-2efa-3958-afa9-bf10bae9fc10 | -3.25689 | -53.70897 | 2024-11-25 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8d74b486-8c93-3de0-8f37-3f44f13fd2b8 | -3.29318 | -50.54078 | 2024-11-25 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e7664926-9944-38cd-b087-e5de054cbb18 | -3.88405 | -50.98263 | 2024-11-25 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 72111dc8-ede6-358a-8e57-b78090938c03 | -2.97119 | -53.8879 | 2024-11-25 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 41d46426-a8f0-3940-8b6a-289368be2d23 | -4.16963 | -46.81722 | 2024-11-25 04:55:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f97e0099-5e95-3363-ae4e-d28edfd8a141 | -0.272 | -51.62117 | 2024-11-25 04:55:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3ae09e3c-a125-3156-93aa-19e89025c75a | -3.3219 | -51.63103 | 2024-11-25 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bf5f9b9b-f550-3c34-bf54-b24a87e49f97 | -2.80432 | -53.01638 | 2024-11-25 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7430c5c4-e4c6-3b48-8a74-713afafc0cab | -3.28839 | -53.85205 | 2024-11-25 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 61d95c44-28af-3dbc-a1a4-31c6115fdbd9 | -2.81105 | -54.02279 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d6c9bcca-cb7f-303a-ba3e-afb79b77d65d | -0.94434 | -51.71803 | 2024-11-25 04:55:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e8d957f0-ede1-3100-82ca-f439d72a23d5 | -1.08739 | -53.64588 | 2024-11-25 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 710df0ec-8791-3bae-b84f-6d18cc0b820c | -3.21486 | -51.42164 | 2024-11-25 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a072e739-6b4a-31f8-8fc9-2b8309e4dbbe | -3.75913 | -49.93289 | 2024-11-25 04:55:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5986a649-9308-3e26-b87a-19c6bb5661de | -3.4757 | -51.98866 | 2024-11-25 04:55:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c14f7300-9c1b-31b9-96cd-d764082ec9cd | -0.25392 | -51.517 | 2024-11-25 04:55:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c013c276-1fc4-3a42-95e2-6c987ba95389 | -3.25513 | -54.23549 | 2024-11-25 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| fb326ff3-753c-3c29-a21f-1d17602730d5 | -5.75851 | -45.90477 | 2024-11-25 04:55:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 92a43c16-476b-3c80-a160-942d30508fa5 | -2.68852 | -46.26786 | 2024-11-25 04:55:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 903d6d69-fa9f-3b5b-88a6-e87af3d50764 | -2.58971 | -54.05289 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4779a0f7-c989-3357-9649-498d2dfb8a15 | -3.67922 | -50.21672 | 2024-11-25 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 8881fde6-9404-3c27-94aa-e5b1c178b625 | -3.973 | -47.71887 | 2024-11-25 04:55:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 12624fef-b8d2-39c7-a389-a18f73a19aa3 | -0.66749 | -51.66413 | 2024-11-25 04:55:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5c7021c1-3635-3be5-a887-ec42deae84ea | -2.55284 | -54.03278 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cb241f9c-49b1-3f3b-8430-a85d8e76d73d | -2.84766 | -53.98569 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7367d83b-9eed-3106-aa24-1efe3645a14b | -3.25159 | -53.59149 | 2024-11-25 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 087fcd7e-4453-35e2-9e91-d82185ea1d64 | -4.51699 | -49.05862 | 2024-11-25 04:55:00 | NPP-375D | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 726c300a-28b3-3773-a738-295075cbf994 | -4.10507 | -50.71782 | 2024-11-25 04:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 30377e25-635f-3518-8012-a464e76b1d04 | -3.08834 | -53.98453 | 2024-11-25 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a69c16fe-dbaa-3d28-9a16-818a130b40b8 | -0.21099 | -51.18876 | 2024-11-25 04:55:00 | NPP-375D | AFUÁ | PARÁ | Brasil | 1500305 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| bce93153-7070-3f6f-88fe-0060b649f805 | -4.16204 | -54.57543 | 2024-11-25 04:55:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 528a5893-00fe-3af0-927e-c1420fa7a85c | -2.55618 | -54.03329 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 79be759c-7b31-3b27-b5d1-8b3deebc2ba9 | -2.61666 | -54.25102 | 2024-11-25 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c99106ce-9358-3d74-9b16-6e3907a4a6cc | -3.11211 | -53.7042 | 2024-11-25 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 05924f46-c0ff-31b9-b9ca-ba399dfcaa66 | -1.25604 | -51.78018 | 2024-11-25 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4e0fd6e2-c5b6-3e3a-9cac-656904dd15b1 | -1.5686 | -52.00902 | 2024-11-25 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| a3bfd97b-f4e2-3258-9284-979ac98f234f | -3.37421 | -54.67765 | 2024-11-25 04:55:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ac67bfea-1d18-3195-97b6-4e2b732d960f | -2.66893 | -51.722 | 2024-11-25 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bcc3131a-4ab2-32bc-89ab-769b09784a84 | -3.05909 | -53.22243 | 2024-11-25 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e95d5892-8398-382e-b32a-13ecb08b9d1a | -2.56912 | -54.05324 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 790bf56e-d193-33a4-b518-5cc1b8a5e637 | -0.96915 | -51.76874 | 2024-11-25 04:55:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5741aa88-50f4-3b43-80cf-75fa8b758a8a | -1.11775 | -53.72973 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| aba8f033-83a1-3f60-a46a-f8d171f04cfa | -1.60266 | -52.52439 | 2024-11-25 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 07462c46-a5db-32a8-9761-d786a5cc8412 | -1.7769 | -52.72879 | 2024-11-25 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 3fba4881-0c72-355a-83d1-e893ac58c5af | -1.6142 | -52.57556 | 2024-11-25 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9efbc50d-e6a0-3f34-9386-a07e040a979e | -3.71077 | -51.77888 | 2024-11-25 04:55:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| b019014f-813c-3843-b052-a3bcc1f8274c | -0.98638 | -51.72438 | 2024-11-25 04:55:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 93a6a731-4386-35b0-a180-740cf8486def | -2.59305 | -54.05341 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a9f7040d-76bd-3f42-a48b-8f82417ffbba | -2.24636 | -53.61449 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6718e480-7720-3235-beb4-355554ae9b69 | -0.35235 | -51.97445 | 2024-11-25 04:55:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 76afd168-f670-3613-a55e-d2389d9e0784 | -2.85096 | -53.96482 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 09c16f74-e5a2-33d3-a055-4bb17518d65c | 1.70638 | -55.82195 | 2024-11-25 04:55:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 815dc81b-00f9-3d0b-ae7a-bf70de58cb2d | -2.33631 | -52.17793 | 2024-11-25 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 74650508-2134-399e-b5e5-64821e7b0b11 | -1.77026 | -52.72776 | 2024-11-25 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 237e3cc8-b736-3805-968f-e7b3d6574db1 | -1.23904 | -53.39314 | 2024-11-25 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8fa65417-9c8a-3f1e-9a50-8e5fae6a8635 | -2.6055 | -54.25649 | 2024-11-25 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7994e11a-7706-3b39-a61a-7e976e9df05b | -3.10554 | -53.98365 | 2024-11-25 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f8e2df74-0f16-3c50-b2f8-97413e26c832 | -3.96465 | -49.95089 | 2024-11-25 04:55:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| cf335195-27f8-3b68-8377-bae0e023dda1 | -1.47478 | -51.96235 | 2024-11-25 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6d637216-f96a-37d0-aa27-2423d8b62ac8 | -0.24562 | -53.76668 | 2024-11-25 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a64d76f5-a841-34d4-ae54-9c56c7202330 | -1.61814 | -52.59387 | 2024-11-25 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 552ae936-b010-3e87-949f-3b2ca2bc5980 | -0.91414 | -51.73506 | 2024-11-25 04:55:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 558f9d5d-4192-3a32-87c3-e7510e756eba | -3.50245 | -50.467 | 2024-11-25 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1dadb77d-c5e5-375d-8fb1-ee6f2ca179d1 | -3.06295 | -53.2195 | 2024-11-25 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 7becbd12-81b2-3001-b8c9-1e59e776fade | -4.24656 | -47.99256 | 2024-11-25 04:55:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 35aa8378-06f2-3851-9983-84c7be73f6e3 | -0.90918 | -52.58618 | 2024-11-25 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 932466d0-5bc1-3458-887d-a1c6f09651d1 | -2.87935 | -54.00134 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 98ca915a-e6fb-37b8-a993-aafc6e821f4a | -1.2448 | -51.74219 | 2024-11-25 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| dbebb3a3-5850-30af-ae77-5b0867876588 | -3.63016 | -52.25348 | 2024-11-25 04:55:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1daa58e7-7433-350e-9476-c23ae273b149 | -1.42822 | -51.12699 | 2024-11-25 04:55:00 | NPP-375D | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7befe46a-7338-3a8a-a900-4d20a08daa3a | -3.00218 | -52.51059 | 2024-11-25 04:55:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6ad4e237-ce93-337a-993d-172905e69c6b | -3.55416 | -51.50684 | 2024-11-25 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7d76c458-9cfe-3bab-b14e-3fd8b6a37010 | -3.04122 | -54.02349 | 2024-11-25 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| edfc3105-54e4-31e5-aed9-77d076e9cb6e | -2.87104 | -55.18377 | 2024-11-25 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1a62f033-f5ea-38ef-aa48-da71dd063981 | -3.29836 | -53.85361 | 2024-11-25 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 84e38c86-5da7-308d-b908-56a2e2cc4cd0 | -4.34916 | -45.78897 | 2024-11-25 04:55:00 | NPP-375D | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f151a11f-ad8b-3ca3-9029-f5c26e40a460 | -2.58929 | -54.22868 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7da988b7-667f-3713-84b0-487ff27a6761 | -0.27801 | -51.51712 | 2024-11-25 04:55:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 53f7ef58-f09b-30db-b901-ae212224d69b | -3.64591 | -51.38636 | 2024-11-25 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b1f2a35b-03bc-3094-96b1-dd6aaf61ddc1 | -1.3057 | -51.86713 | 2024-11-25 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 84ed65ec-e727-3af1-8885-7be1a4888832 | -3.8497 | -52.14492 | 2024-11-25 04:55:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 30b95931-0ad4-3896-af49-c306c4b1b9d5 | -3.39073 | -50.32463 | 2024-11-25 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 56600d3a-5ca9-3e36-8919-89fe7d6df291 | -3.10887 | -53.98417 | 2024-11-25 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 59f51a1b-bda4-3d67-a63d-ab9440d69821 | 1.51107 | -55.67461 | 2024-11-25 04:55:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d35ab17f-3707-3d13-bc8d-64ecddea46ab | -2.85876 | -53.98029 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0f8e6c2f-0570-34af-9e6f-b9705b23ae5a | -4.3041 | -49.92461 | 2024-11-25 04:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 90a0ffe7-924c-3f88-bea0-9ef491fdecc7 | -2.9909 | -52.90373 | 2024-11-25 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7d719d1b-991f-3150-9b0a-f94c21909999 | -2.7949 | -53.01139 | 2024-11-25 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5ccdbd8a-f34e-33dc-90aa-b9d720836505 | -1.59702 | -52.25694 | 2024-11-25 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e7122358-c182-3ab5-864b-948c176361e1 | -2.7558 | -54.03207 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 70089e21-7b06-3927-8d42-7be9f2ec451b | -0.57992 | -51.70868 | 2024-11-25 04:55:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| dd0503e5-f8ea-3598-b4b6-e896353e981e | -4.35406 | -45.78979 | 2024-11-25 04:55:00 | NPP-375D | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7e5dabea-b5fa-3de5-b4d7-279e90cf3327 | -3.18993 | -53.25343 | 2024-11-25 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dfd4e73b-c7eb-37e6-a5be-47489c823ffb | -1.93635 | -52.09812 | 2024-11-25 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a9534b6b-f85a-3b9b-8e79-ac6a3ec8fef6 | -3.71398 | -52.41203 | 2024-11-25 04:55:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |


[Clique aqui para ver as próximas entradas](README46.md)
