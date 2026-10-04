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

## Dados Diários - Página 41

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0e1f762b-0d49-3153-8832-22e791ef94c4 | -2.97724 | -54.08416 | 2026-10-04 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 39f2d2de-9585-3c17-8c44-82c0db55b66e | -2.91436 | -49.00009 | 2026-10-04 04:55:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bf78622a-cc5d-3926-9617-840df8d08fc4 | -1.61915 | -55.01702 | 2026-10-04 04:55:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b6fc3f95-a9a4-387c-981f-fc20d55dc043 | -2.25591 | -51.93593 | 2026-10-04 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 65891a8a-5e40-3f47-a1f4-1d980d344cbf | -3.46561 | -50.10619 | 2026-10-04 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| edeb82b1-bdf0-38a6-9029-7f76d8a75a1b | -3.09783 | -51.10132 | 2026-10-04 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b042db95-c198-3d98-a556-30a940c10840 | -2.92399 | -54.10604 | 2026-10-04 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d79b18b4-b7b2-3265-973a-8cfd8afd4246 | 2.00843 | -61.09284 | 2026-10-04 04:55:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dcd9458b-0d5d-352e-9f2f-54500b45d0db | -3.12139 | -53.71521 | 2026-10-04 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 27.6 |
| 4af762a2-1243-3139-9491-9dead2592ea4 | -2.8236 | -54.12999 | 2026-10-04 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 779ce54f-4c70-36c7-b5bf-d7023c38105b | -3.13415 | -53.7431 | 2026-10-04 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e3059462-a573-31d4-9f10-cbdca24902b9 | -4.46048 | -50.97638 | 2026-10-04 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4cddd495-e38a-3639-97b2-5dbfc0ca512e | -2.81896 | -54.11035 | 2026-10-04 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 4bec5c08-ebcf-3b12-b4a1-76e30bdf7e2a | -3.51452 | -54.61151 | 2026-10-04 04:55:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 4e162f12-20b6-34ff-b4cd-c40efa823f08 | -3.17278 | -54.09573 | 2026-10-04 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f0336d38-936e-3402-b9d9-c8224170405b | 1.80441 | -55.5609 | 2026-10-04 04:55:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e24a1d20-8247-3acf-a369-50c0f11dbb47 | -3.43806 | -50.66176 | 2026-10-04 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 58569f31-39fd-36c1-b99e-a3b6684ca661 | -2.584 | -51.87333 | 2026-10-04 04:55:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| c5fbdfc4-8bab-3b27-b3c8-07135936860b | -2.90364 | -54.13568 | 2026-10-04 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 3f0656fe-a6c4-3983-b01c-d7d0f9830b5a | -3.13041 | -53.73005 | 2026-10-04 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 279b298b-9e79-3cea-bc6e-ed1edb172cdc | -3.17414 | -50.5352 | 2026-10-04 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cf9cc069-f0e5-3aa6-a9c4-1aa538ab8cfc | -2.80231 | -54.11707 | 2026-10-04 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| cc2544d0-fdd5-3d4e-aaa3-6596bccbeb31 | -2.59038 | -51.85553 | 2026-10-04 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 42a0ad72-e576-3c6b-a4d3-5dcaf37c8cb6 | -3.47757 | -55.4328 | 2026-10-04 04:55:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 09efc2fc-c0e6-3cf4-99cf-e2acd2941a16 | -2.84864 | -51.28612 | 2026-10-04 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2a225143-082e-3d71-ac57-6477c1854e18 | -2.99146 | -51.04824 | 2026-10-04 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 487a6018-68fd-3a98-8a69-b46658de535c | -3.30172 | -53.84412 | 2026-10-04 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f32b4935-0b8f-3e2e-b928-41f70600fb36 | -3.7004 | -54.19789 | 2026-10-04 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 67bd39cc-7343-358a-9e0e-662e9d05bdac | -3.1674 | -54.08097 | 2026-10-04 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 21cc4aef-e61c-3b77-8b95-7e252532cedb | -2.98256 | -54.09904 | 2026-10-04 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4c95e73a-00e7-3d3b-9c21-7a1684bfcc17 | -5.54737 | -44.21258 | 2026-10-04 04:55:00 | NPP-375D | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 76b87bf3-3e95-33cb-a514-53170c1b4237 | -3.2247 | -54.37203 | 2026-10-04 04:55:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ad20af63-01e8-386e-b217-e890ada59f86 | -3.11492 | -53.73201 | 2026-10-04 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 22.8 |
| 2a4e1e16-b200-32be-8447-b75991fda5b4 | -2.81517 | -54.10973 | 2026-10-04 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| ec9e178e-81da-305a-af9f-9ea97ddfa272 | -3.13341 | -53.73501 | 2026-10-04 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| caf515eb-a52b-3aae-a942-9ed8ce4d08cc | -3.11728 | -50.27781 | 2026-10-04 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 44d63204-b1e3-3aa1-88a6-cd7bc200dfab | -3.06503 | -49.5349 | 2026-10-04 04:55:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e5cd9c88-8f3e-3024-8f42-c3a16ee419e7 | -3.00452 | -53.87194 | 2026-10-04 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 36461c3f-b1a2-33e1-a7bc-b9a745131b7e | -2.57998 | -51.87646 | 2026-10-04 04:55:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 53e69f1f-4cb8-31f6-9b62-e5e239218941 | -4.26795 | -50.73992 | 2026-10-04 04:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a3055ccf-6f99-31a6-b286-9dd8f2ad5abf | -3.11261 | -53.72272 | 2026-10-04 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 34.6 |
| 316eb873-4ddb-3782-9ef6-4f4367a2494e | -2.82105 | -50.50073 | 2026-10-04 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 71ced23c-ac0f-3c51-b525-0f4d07962999 | -2.44988 | -57.97302 | 2026-10-04 04:55:00 | NPP-375D | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| fe5d6e88-0bb8-3103-9582-eeeebd759bc2 | -4.46271 | -50.98385 | 2026-10-04 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 21d295f2-ef45-3b3f-80bb-8d98ab96c111 | -2.97424 | -54.10238 | 2026-10-04 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| f5f7bce2-8657-3994-aaff-78656416ca68 | -3.12093 | -53.74191 | 2026-10-04 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| c8bdae7c-0dda-3a8e-810c-de29efde4741 | -2.24679 | -51.92686 | 2026-10-04 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3f932c02-07b1-3d37-a9af-9d05ced8435f | -3.12001 | -53.7239 | 2026-10-04 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 603cd0b6-6e3a-38a1-b001-d7d438c2622a | -3.70628 | -50.65847 | 2026-10-04 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 74960e8e-39ec-3446-9531-5e2f91eac860 | -2.83383 | -54.21268 | 2026-10-04 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d4f0b057-67f6-3cf8-9c49-86561aec7085 | -3.04366 | -54.22678 | 2026-10-04 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 44930791-7b75-317f-876f-2520452f8a2f | 0.70091 | -51.43085 | 2026-10-04 04:55:00 | NPP-375D | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 53b170e8-c96a-304b-9c47-b86e9f4a259b | -1.86436 | -50.62376 | 2026-10-04 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 76ea2042-064d-3a01-a380-d87233805e2e | -1.8677 | -50.62428 | 2026-10-04 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0dcf9c01-1739-3f8c-9fb0-b98e265b9b86 | -2.90059 | -54.13047 | 2026-10-04 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e8565cd6-5838-384e-874e-b297b4bd42dd | -3.10457 | -50.29352 | 2026-10-04 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2b001e59-7503-32c8-aefb-2d466a075e31 | -4.14315 | -46.83075 | 2026-10-04 04:55:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 30317156-7048-33bd-a336-b23c827c7724 | -3.1803 | -48.68882 | 2026-10-04 04:55:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2aeecf16-ed36-391c-b6aa-7492d8c75444 | -3.12602 | -53.7338 | 2026-10-04 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 07acb288-a3b8-31c6-95e4-8384b5919bd6 | -2.99569 | -54.23339 | 2026-10-04 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a07e5b0a-41f7-3a55-8176-2873fb3b5bf6 | -4.28613 | -50.26398 | 2026-10-04 04:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 64.0 |
| a3241fd5-4012-3f79-989e-0922417c4bac | -2.58176 | -51.86544 | 2026-10-04 04:55:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 09404fa5-fa8d-3703-91d0-faae17010c49 | -1.0989 | -54.1093 | 2026-10-04 04:55:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 01a83232-243d-3d0a-b2d1-47ccce6050e8 | -3.52149 | -54.61761 | 2026-10-04 04:55:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7eb5003d-5391-331e-8717-0eb811c12164 | -2.25396 | -51.88241 | 2026-10-04 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 926bfef8-bfc8-3913-87c5-25b97ea98869 | -2.54625 | -57.40095 | 2026-10-04 04:55:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c37490cc-20f5-3c48-b6a8-b53a18831193 | -3.27853 | -53.82262 | 2026-10-04 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a1a82dbd-1f8e-37be-9cf0-c6b3cdd2ca46 | -2.57589 | -49.99783 | 2026-10-04 04:55:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f2f549bb-ca81-3260-a429-dbc2ce6de0a0 | -0.35732 | -51.98391 | 2026-10-04 04:55:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 550ddb43-1dc7-3d15-b4e4-6841247f6332 | -4.2562 | -46.36971 | 2026-10-04 04:55:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 2eafce6b-822b-3348-94d9-9fa04ae10cf1 | -2.58413 | -51.85075 | 2026-10-04 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 52b00a54-c4d2-3867-b135-2cb43cea62e1 | -4.48333 | -45.53898 | 2026-10-04 04:55:00 | NPP-375D | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b36e92ad-99d2-3824-9a4c-d515536d9c33 | -2.97395 | -53.26081 | 2026-10-04 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a28f5b11-2451-3fe5-93a2-08a4d1c29408 | -4.28783 | -48.56296 | 2026-10-04 04:55:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b90c43b2-be57-356d-9988-60bde1375739 | 2.51677 | -60.99957 | 2026-10-04 04:55:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 607e6cbc-f7cd-3897-aad9-9324d69f447d | -3.07061 | -49.54292 | 2026-10-04 04:55:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 43871480-1a39-3e68-8647-805a6f713181 | -4.85646 | -48.77025 | 2026-10-04 04:55:00 | NPP-375D | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5e022d71-5d23-3c3d-b819-ee52ddbde2ba | -2.94756 | -54.12873 | 2026-10-04 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 564ca446-df8d-30ea-aa47-8e3bd50fc21b | -4.28781 | -50.27489 | 2026-10-04 04:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 43.7 |
| 519e30f3-adea-367c-a0c1-579049ff8007 | -3.10844 | -53.74882 | 2026-10-04 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| a6cf6678-7e87-397b-b406-81b3babb59bb | -3.08338 | -49.52705 | 2026-10-04 04:55:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 15a75019-e4d6-31f6-94fa-d5405ab5063a | -3.17493 | -54.08223 | 2026-10-04 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 51fe1f28-2c53-3c20-b5ba-34f0ac43dd6f | -4.28061 | -50.27731 | 2026-10-04 04:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 15.2 |
| 18aa0f71-05c1-3c0b-b4a0-6dcb9925425a | -2.79695 | -54.10209 | 2026-10-04 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f2adb577-d3ce-3a63-b198-cc6617f2e6df | -3.19261 | -57.92115 | 2026-10-04 04:55:00 | NPP-375D | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 283d1cac-7910-32b2-8073-504517104a7c | -3.0573 | -54.16136 | 2026-10-04 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| f9424651-5977-3c78-b6ae-338ab541b41c | -2.81439 | -48.66203 | 2026-10-04 04:55:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 88164c1b-187e-3e48-a5b6-fe6b256c4cc0 | -2.96818 | -54.09203 | 2026-10-04 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7c9afbf2-7110-309c-b151-5146814d950a | -2.94683 | -54.13331 | 2026-10-04 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 659a3513-574c-3a2a-8906-50b7f2856c05 | -4.27671 | -49.97812 | 2026-10-04 04:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e4d5dd2e-5638-3d8d-b77c-2eb4b52600c1 | -2.75407 | -51.55304 | 2026-10-04 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 51b0cbf1-80a3-307d-a959-3903a259ab47 | -3.28473 | -53.8549 | 2026-10-04 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7363cc4b-332c-3dd6-bd35-84f8c433382f | -3.13261 | -53.72946 | 2026-10-04 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| ea5f41f2-065b-3d06-a5b2-8679e8548621 | -2.90289 | -54.14028 | 2026-10-04 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 7bb37c30-480c-38c9-a2f0-bf26eca5cf4c | -4.2619 | -50.73898 | 2026-10-04 04:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 29fad2ee-cf6c-37e3-85d8-4be0e4c31025 | -4.2756 | -50.26588 | 2026-10-04 04:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 80a4e7da-7954-3ac3-8e7e-f7a0b3f13052 | -4.26144 | -46.36113 | 2026-10-04 04:55:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 6.4 |
| b0a6be58-7257-3406-9af7-7156a0a0f03c | 2.34161 | -50.75225 | 2026-10-04 04:55:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| acc83063-1577-36a5-919e-47745c35ed40 | -2.265 | -54.81927 | 2026-10-04 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 847326d9-5663-36e0-8c4b-8b3ee1a9dcf4 | -4.30514 | -50.78484 | 2026-10-04 04:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |


[Clique aqui para ver as próximas entradas](README42.md)
