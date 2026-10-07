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

## Dados Diários - Página 174

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 82a33e80-d9cb-386f-94eb-e12b440bd104 | 3.53485 | -51.28363 | 2026-10-07 16:05:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 24.2 |
| 6908f281-9c12-3b38-89a4-4bbb36fcccde | 1.47918 | -50.76144 | 2026-10-07 16:05:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 248a1f52-9440-3091-b376-ee16117e678c | 2.19442 | -50.97459 | 2026-10-07 16:05:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 11.4 |
| c9e2a014-e3d0-3037-977d-289c3bef960d | -1.10937 | -52.26278 | 2026-10-07 16:05:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 5.9 |
| f793da8c-53df-34ca-bf6c-3cce0cc2efd1 | 3.22624 | -51.31572 | 2026-10-07 16:05:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 019664eb-5ec6-33dc-8a93-806d140bb36f | 3.2232 | -51.2966 | 2026-10-07 16:05:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 7f357bb3-c21f-37bd-ac06-9d6db590b114 | 2.11814 | -50.82698 | 2026-10-07 16:05:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 14.5 |
| 09e9cad9-6474-3107-b590-2ffccab54779 | 2.11457 | -50.83075 | 2026-10-07 16:05:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 52cf8fef-4549-39f2-b8dd-d082e5c14cc4 | 4.01611 | -51.616 | 2026-10-07 16:05:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 15.2 |
| 00a69cf9-4809-395d-a53e-ecbd3f4f7515 | -1.42195 | -52.84933 | 2026-10-07 16:05:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 277dce50-bcff-3b15-bf89-dd8e2191f02b | 3.21639 | -51.30025 | 2026-10-07 16:05:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 12.4 |
| ced63cbf-547f-3b74-bf53-54e8fb2aebbc | 2.55602 | -51.10514 | 2026-10-07 16:05:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 59.7 |
| 849a1398-a786-34ae-8698-e3715e0aa13e | 2.19208 | -50.97409 | 2026-10-07 16:05:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 15.8 |
| 1e2badae-005f-34b3-9650-64a9e0fb1bac | 1.47469 | -50.77421 | 2026-10-07 16:05:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 27.0 |
| fdfe7389-6249-3cd7-a503-0a3c36107392 | 3.99717 | -51.7231 | 2026-10-07 16:05:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 708b1591-1e9c-3e8c-8ba3-2d44090f5c01 | 2.71408 | -51.36645 | 2026-10-07 16:05:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 84bc2798-68b0-3c85-a87f-b168b794a068 | 1.47769 | -50.77034 | 2026-10-07 16:05:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 14.7 |
| 96d67ae7-3c08-3fdb-a739-5a5c1bbb8466 | 3.40544 | -51.30441 | 2026-10-07 16:05:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 14938120-7355-349a-96f1-c2acbc7a0db7 | -0.11122 | -49.69653 | 2026-10-07 16:05:00 | NOAA-21 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| d60339dd-2485-3b7b-8a79-eaa863446679 | 0.8107 | -51.22227 | 2026-10-07 16:05:00 | NOAA-21 | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 17.7 |
| 89c8b48f-cca9-3ab7-b889-a6c1848b57e1 | 2.45554 | -50.82267 | 2026-10-07 16:05:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 988acb2e-67a1-36e8-b353-e3c86bf2a562 | 3.22311 | -51.30845 | 2026-10-07 16:05:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 48.5 |
| e8aca929-74be-3707-9220-ef795edff8b7 | 1.34991 | -50.84502 | 2026-10-07 16:05:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 7.1 |
| ff5b9f2e-dd15-32ac-8ed8-a658bc4c4c39 | 1.47226 | -50.751 | 2026-10-07 16:05:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 12aed203-6030-318d-857b-0645cbee4389 | 2.11068 | -50.83489 | 2026-10-07 16:05:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 88e7a467-2e41-3808-aa74-286ab1901026 | 3.22468 | -51.29935 | 2026-10-07 16:05:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 7.0 |
| ea6ae7f0-80a9-327c-967a-0acef1cd59e1 | 4.02121 | -51.61678 | 2026-10-07 16:05:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 9d215829-4828-32a1-ae20-fbbec94560b1 | 3.21488 | -51.30934 | 2026-10-07 16:05:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 36.8 |
| cddc58ad-cc9b-3fbc-8d75-42803e0d103d | 1.33854 | -50.83866 | 2026-10-07 16:05:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 69c1d35e-c486-3b2d-9a9f-f2d0753da5fe | 1.47683 | -50.76083 | 2026-10-07 16:05:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 13.2 |
| ea8a319c-e664-3043-8371-1d9852e51613 | 2.4496 | -50.82174 | 2026-10-07 16:05:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 02795f30-5b38-30c2-a97b-90838c656ee2 | 3.51307 | -51.26646 | 2026-10-07 16:05:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 61183e54-d9ed-30f5-a779-15f450e7e7a6 | 3.74887 | -51.62428 | 2026-10-07 16:05:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 5.3 |
| b36e4b36-f4a5-308b-8c09-0a7d2d5a2eaf | 3.22093 | -51.31027 | 2026-10-07 16:05:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 36.8 |
| f096ecfc-8ff4-32fb-a46b-a7d0ee93da10 | 2.11385 | -50.83518 | 2026-10-07 16:05:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 0f422b2b-c8ec-3602-86ce-40a22bb09221 | 3.53034 | -51.27375 | 2026-10-07 16:05:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 16.7 |
| bc4b7e1c-8a1f-3854-b03b-3b1aba784d81 | 3.53751 | -51.28158 | 2026-10-07 16:05:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 53.8 |
| c63dc8bc-85a4-367b-b448-ed0b0809a3b4 | 3.51982 | -51.26295 | 2026-10-07 16:05:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 1543ab2c-990b-3973-8f00-ec2d6d823556 | 0.20281 | -50.00941 | 2026-10-07 16:05:00 | NOAA-21 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 64060837-cff2-3a42-802e-e7cccb95e345 | -0.22255 | -48.96597 | 2026-10-07 16:05:00 | NOAA-21 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| d078f0da-32b9-38c6-a0a4-78a9ef871de5 | 3.36758 | -51.34481 | 2026-10-07 16:05:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 5adff23a-6355-3209-8d60-dad45c833ed5 | 3.2126 | -51.32305 | 2026-10-07 16:05:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 82ee01e0-8a0c-3d80-b01a-f9cc5f1c18d6 | 3.22699 | -51.31121 | 2026-10-07 16:05:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 0dab1236-31ef-37d2-bfab-0f4de905bd7c | 3.21256 | -51.2976 | 2026-10-07 16:05:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 16.7 |
| 195eb4e9-5ac9-39a5-896b-14bf2051f163 | 3.22169 | -51.30569 | 2026-10-07 16:05:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 36.8 |
| eb155fa4-bdf2-374d-ac1b-5595fa7789ea | 0.73025 | -51.37919 | 2026-10-07 16:05:00 | NOAA-21 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 8.7 |
| a383e167-b1e3-30c3-a676-f0e5680dbb48 | 0.72556 | -51.36806 | 2026-10-07 16:05:00 | NOAA-21 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 215de711-5247-3df8-bef9-61b4dbac9020 | 3.21184 | -51.32762 | 2026-10-07 16:05:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 9.4 |
| f235f388-cb93-337a-9ef7-5fe9bf6f6261 | 4.0151 | -51.6159 | 2026-10-07 16:05:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 5.8 |
| d7820c55-bee5-3404-b3f8-bc53058e0e20 | 3.9969 | -51.72324 | 2026-10-07 16:05:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 1a78765a-fb06-3863-bdcd-dab4948a9a28 | 0.8099 | -51.22723 | 2026-10-07 16:05:00 | NOAA-21 | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 13.8 |
| cc3e1030-6b63-39fb-97e1-7a2d3739cd66 | 3.74967 | -51.61959 | 2026-10-07 16:05:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 2474252f-62e6-3ed6-afd5-aeceb4a09d4a | 1.47844 | -50.7659 | 2026-10-07 16:05:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 14.7 |
| 79fdeeaf-94c1-3be5-a780-6c2247a3b2bf | 3.52508 | -51.26836 | 2026-10-07 16:05:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 10.9 |
| f9d8de82-4471-319e-ac61-b9492ba9f3e1 | -9.4565 | -64.3344 | 2026-10-07 16:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 62.7 |
| 1aaa5182-fb49-356a-83d5-b48cba9bced6 | -0.4136 | -52.0151 | 2026-10-07 16:10:00 | GOES-19 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 68.6 |
| e76ee025-df6d-30d1-a0cd-3d47aec2e86e | -9.75 | -65.0562 | 2026-10-07 16:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 51.2 |
| 02d1e1c9-37bd-307b-b234-6e54cf0a6681 | -1.1713 | -49.2544 | 2026-10-07 16:10:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 68.6 |
| daa43b64-9f2d-30ab-843b-bf4a9f0a3a14 | -8.1035 | -70.1349 | 2026-10-07 16:10:00 | GOES-19 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 72.7 |
| 807610cd-7f7a-3f1d-8dd1-c0243bc5c2b5 | -8.5911 | -67.3269 | 2026-10-07 16:10:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 52.8 |
| 28f6a9b7-6f6f-305b-bd59-ac1490432df9 | -8.2495 | -70.8289 | 2026-10-07 16:10:00 | GOES-19 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 71.4 |
| 17b098a3-e2be-32fb-8c39-86aa5ebe0bea | 1.8768 | -55.7227 | 2026-10-07 16:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 73.0 |
| f2d795cc-c160-36c4-91aa-7944eb030718 | -9.6419 | -68.6156 | 2026-10-07 16:10:00 | GOES-19 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 60.2 |
| e77e7147-a976-361b-bd4c-9878ffd73a7a | -9.5177 | -67.0987 | 2026-10-07 16:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 55.0 |
| 7281003d-996a-30f2-88e3-a6108a7ae152 | -8.3234 | -70.7364 | 2026-10-07 16:10:00 | GOES-19 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 73.6 |
| f8e9c7ff-8b1b-32ea-9d07-0886b917e611 | -2.8899 | -54.0912 | 2026-10-07 16:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 68.3 |
| 461e68bb-1828-3e89-8384-ea78dd85967b | -0.3768 | -51.9947 | 2026-10-07 16:10:00 | GOES-19 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 81.2 |
| f81b7bbe-360c-3559-9267-229da7be80f6 | -2.998 | -54.7492 | 2026-10-07 16:10:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 79.4 |
| 89bd3367-fd1d-3c91-9799-5ea4e0dec110 | -1.1898 | -49.2542 | 2026-10-07 16:10:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 64.2 |
| c0f3334a-e570-30c7-9d14-4a28faba0c9d | -8.868 | -67.4497 | 2026-10-07 16:10:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 65.8 |
| dfcf7f09-15b0-34d0-9288-c96f3c5f1afb | -9.8059 | -65.0354 | 2026-10-07 16:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 57.6 |
| 7b329ce5-42d9-3ed2-b78a-1d628449e430 | -9.8061 | -64.9979 | 2026-10-07 16:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 109.1 |
| bd0e596d-7393-3aad-b620-fb52d700f142 | -9.6757 | -65.0401 | 2026-10-07 16:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 83.7 |
| c33afe6f-ca27-3c8e-ac1b-dec8fd2355e3 | 3.5263 | -51.2778 | 2026-10-07 16:10:00 | GOES-19 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 121.9 |
| ae8dcd18-9735-3889-81be-76f6149d53f9 | -9.8619 | -64.9958 | 2026-10-07 16:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 62.5 |
| 4f9bb0cc-7caf-3f48-9b9d-fec3d40a6441 | -9.1076 | -67.7215 | 2026-10-07 16:10:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 55.4 |
| e42df033-2b8f-34c1-9db0-98baf29aea89 | -9.5176 | -67.1173 | 2026-10-07 16:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 58.2 |
| 0a417153-ae4c-3105-b07d-d6e05eab00df | -9.432 | -45.8293 | 2026-10-07 16:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 157.6 |
| 4971bbef-79a5-346b-87a1-fbf489d76a20 | -12.2132 | -44.6991 | 2026-10-07 16:10:00 | GOES-19 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 189.0 |
| 0a939ad8-8844-302c-9da5-0a7be166bcc6 | -1.2265 | -49.381 | 2026-10-07 16:10:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 72.0 |
| 687ce473-bcb2-31dd-afa4-f6a90b236d28 | -1.3927 | -49.2727 | 2026-10-07 16:10:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 92.9 |
| 4bb5e74a-65e3-398b-98a8-5f08f0463e12 | -1.4662 | -49.4625 | 2026-10-07 16:10:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 94.1 |
| 9eedd7ba-bc43-37c3-b051-676addfd9a89 | 1.5283 | -56.0227 | 2026-10-07 16:10:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 88.3 |
| 2dd98367-db2c-318f-b350-7a6e3ebb707b | -12.1742 | -44.7284 | 2026-10-07 16:10:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 256.9 |
| d50d1412-d350-3498-bcbc-d67c457683a3 | 1.6385 | -55.8047 | 2026-10-07 16:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 82.0 |
| 910f09f2-784b-32bd-9084-93644e718e78 | -9.8246 | -65.016 | 2026-10-07 16:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 60.8 |
| 47584b95-810c-34bc-beae-b1c0706f1cff | -0.3584 | -51.9948 | 2026-10-07 16:10:00 | GOES-19 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 64.1 |
| fbf7f4c3-beff-315a-8ce2-0596537dd81f | -9.806 | -65.0167 | 2026-10-07 16:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 93.2 |
| cccd6533-6649-3208-8398-a7db3a22a492 | -8.5912 | -67.3084 | 2026-10-07 16:10:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 108.2 |
| 2065afc8-4e5b-33a1-8a82-abda411ec56a | -9.1076 | -67.703 | 2026-10-07 16:10:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 51.7 |
| a6efd953-aa99-3fca-9234-d7532854beb2 | 1.8767 | -55.7424 | 2026-10-07 16:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 73.4 |
| a951f109-051e-383e-a6ef-514d1858dcbf | -9.6572 | -65.022 | 2026-10-07 16:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 55.0 |
| f89b7709-8a49-3a37-964c-e83858b6925d | -10.9949 | -45.4298 | 2026-10-07 16:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 127.9 |
| 2b38968a-30e3-3fc9-85ea-1d89543cfd25 | -9.8245 | -65.0348 | 2026-10-07 16:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 58.4 |
| d202c383-8a6d-33fb-95c0-c3b25f0d04d6 | -12.19 | -44.78 | 2026-10-07 16:15:00 | MSG-03 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e1344fd3-854d-36e0-9270-aa0220e7cdc5 | -6.58 | -41.59 | 2026-10-07 16:15:00 | MSG-03 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| c91ffe36-8d7d-3467-8d38-257de8e93b4f | -12.25 | -44.75 | 2026-10-07 16:15:00 | MSG-03 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 2d362d27-07b5-399a-a923-267514fa0417 | -2.76 | -54.02 | 2026-10-07 16:15:00 | MSG-03 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9d867ac3-c5b4-3645-a476-d061aebaeb9d | -3.87 | -44.12 | 2026-10-07 16:15:00 | MSG-03 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9ce31cae-d12f-3e5b-a5bc-1d8d6e4720e4 | -5.72 | -41.75 | 2026-10-07 16:15:00 | MSG-03 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | nan |


[Clique aqui para ver as próximas entradas](README175.md)
