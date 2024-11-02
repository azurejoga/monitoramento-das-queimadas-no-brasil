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

## Dados Diários - Página 88

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 52edc647-8774-3cca-8447-b30a0ac764d3 | -3.11479 | -54.29694 | 2024-11-02 05:27:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| b43b73aa-cce3-3333-b6dd-e3600632ac00 | -3.11236 | -54.29481 | 2024-11-02 05:27:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| e6a4f6a3-6b48-35ea-a80b-ecabe32fde70 | -3.11232 | -53.72257 | 2024-11-02 05:27:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e9a9a4c5-17cc-3156-8af2-f0e5cf5eebc0 | -3.11219 | -54.26537 | 2024-11-02 05:27:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| bcc7985c-a8a4-34a0-b04c-1aa49d95c233 | -3.11086 | -54.29144 | 2024-11-02 05:27:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| cd90810a-a35b-37cd-a7c5-16c94a395db7 | -3.10995 | -54.27977 | 2024-11-02 05:27:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 94b1b7f3-70a0-3f3b-bc89-97bd66c9b503 | -3.10921 | -54.28454 | 2024-11-02 05:27:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0444ad02-d5b7-35af-9682-31c8a6b15427 | -3.10834 | -54.27637 | 2024-11-02 05:27:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 776917d5-5bd0-3bc1-b873-d69076e635f1 | -3.10458 | -54.28384 | 2024-11-02 05:27:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 89eef9c6-3f00-362c-b7d5-f6b49006a48e | -3.10345 | -53.71587 | 2024-11-02 05:27:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 58e8e7bc-7d8d-355c-a081-f949e3311456 | -3.1031 | -54.29339 | 2024-11-02 05:27:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 2bc5ec90-473a-3a4e-b840-14e4b829eaa8 | -3.103 | -54.28044 | 2024-11-02 05:27:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a7d00e4f-89f5-35cc-9d3f-7a7651409dec | -3.10159 | -54.29002 | 2024-11-02 05:27:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| c8d6fe8a-140b-3c59-bf7d-c98ca0713ff5 | -3.09907 | -54.27489 | 2024-11-02 05:27:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e43af311-6505-3d66-844e-662fb7c0ecf0 | -3.07972 | -54.16628 | 2024-11-02 05:27:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 6ed802a0-03b4-3542-8d3c-3c23e9aa7964 | -3.07579 | -54.16068 | 2024-11-02 05:27:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| a69ca0b4-839f-3f52-83e8-9e40bed4b09d | -3.07504 | -54.16561 | 2024-11-02 05:27:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 11f89509-520e-3b51-8fc1-f2e68a288457 | -3.06494 | -54.16923 | 2024-11-02 05:27:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 09122b74-1d7d-3194-b615-e566c75d57a3 | -3.03747 | -53.79864 | 2024-11-02 05:27:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dab82ce0-30e6-3051-b159-576141a25286 | -3.01132 | -53.8745 | 2024-11-02 05:27:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 3a25c1a8-7aea-3742-8ba4-ba2bcc08d277 | -2.98996 | -53.88699 | 2024-11-02 05:27:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7bf91d9f-980f-3f0e-8393-8debc9ab0880 | -2.96655 | -53.91358 | 2024-11-02 05:27:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 7394608a-b298-31ea-b1cd-aa3536c1037f | -2.73975 | -54.12336 | 2024-11-02 05:27:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a9e2d8bb-a52a-394e-8c01-271a0bde665b | -2.63991 | -54.26304 | 2024-11-02 05:27:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6d21e7d3-7d11-3798-8ea1-d325db3f8431 | -2.57738 | -54.78975 | 2024-11-02 05:27:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5b44a411-e3a9-3a0b-9427-95eccbe581a6 | -2.55689 | -54.00754 | 2024-11-02 05:27:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 61589fac-d5c0-3750-9d8d-9b49fb5afbc2 | -2.5522 | -54.00682 | 2024-11-02 05:27:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| fac9fdd6-9e9b-38d6-9712-aa48adae5413 | -2.5 | -54.13177 | 2024-11-02 05:27:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 4e17f684-72e3-34a7-a8ea-26f5d2993cc3 | -2.47033 | -54.06123 | 2024-11-02 05:27:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 9112b791-95d8-3e6b-824c-82bebdd9a99e | -2.46824 | -53.98145 | 2024-11-02 05:27:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 68906a42-f387-3fff-9b18-fbead0d8d4d0 | -2.46013 | -54.15804 | 2024-11-02 05:27:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f9dedb1b-1c1a-32cc-84c5-d07441d2aeee | -2.45626 | -54.15244 | 2024-11-02 05:27:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ba74ab25-668d-3025-9872-72f9cd208007 | -2.45553 | -54.15713 | 2024-11-02 05:27:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 33a59043-6253-38ba-bb43-ca9f6a8421e0 | -2.38643 | -53.8444 | 2024-11-02 05:27:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ef773443-8dc1-39f2-b97a-2e19d6073a10 | -2.36138 | -53.72169 | 2024-11-02 05:27:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 48ccd6ad-5e71-35f5-8605-0d709095f1eb | -2.35982 | -53.73202 | 2024-11-02 05:27:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 9c0ebc16-43ac-3118-87c4-91f56289bf12 | -2.35581 | -53.72628 | 2024-11-02 05:27:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 6867e68c-3b63-3ce1-9740-108c66bc3ec3 | -2.32375 | -53.74613 | 2024-11-02 05:27:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9ad9a997-e5bb-32c7-b66d-3cdd8c56d636 | -2.27467 | -53.74896 | 2024-11-02 05:27:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| b2a2d991-bcad-36c7-ac9a-11732d2ac54a | -2.27069 | -53.74318 | 2024-11-02 05:27:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| dedcc5e3-b9ec-3c93-b887-70ef863f12a6 | -2.2688 | -53.65907 | 2024-11-02 05:27:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8f6cd637-2467-3850-b75d-3778a899155a | -2.26747 | -53.73234 | 2024-11-02 05:27:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 54f64672-6546-384d-b7a7-0c7a705f2028 | -2.26348 | -53.72655 | 2024-11-02 05:27:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1e11d216-aea5-3b80-bdf1-244eacd685c8 | -4.50922 | -55.46216 | 2024-11-02 05:27:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fe69fca4-eda0-3f40-b506-f3f52798ab51 | -4.50485 | -55.46153 | 2024-11-02 05:27:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c4853341-9d1f-3972-beac-1fa5270de080 | -4.42612 | -55.39125 | 2024-11-02 05:27:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ed29b3db-fe5a-374e-ab30-7ec09c02d4a4 | -4.42547 | -55.39559 | 2024-11-02 05:27:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ac7c4ef1-3c85-3b08-a016-bc42fffb59c2 | -4.42173 | -55.39068 | 2024-11-02 05:27:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c750b21f-e2f6-35d4-ae23-8a1b837a38d7 | -4.42106 | -55.39509 | 2024-11-02 05:27:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e767ec61-6961-3bc9-8686-f9798ad228ae | -4.42042 | -55.39934 | 2024-11-02 05:27:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f52e8f06-ff80-35ed-a5cf-e62f2906f479 | -4.41668 | -55.39445 | 2024-11-02 05:27:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 79e289ef-4bf9-38e2-b665-860e97a99484 | -4.41229 | -55.39384 | 2024-11-02 05:27:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6907ed0c-cfe2-3302-9910-f296c6e1a5e1 | -4.41166 | -55.39807 | 2024-11-02 05:27:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 983ad7ce-3129-3b0c-81c3-06603f5dcd5f | -4.37178 | -55.4255 | 2024-11-02 05:27:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7a3a4507-0747-38fd-863f-147475fc95c8 | -4.34227 | -55.35206 | 2024-11-02 05:27:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b953b9ad-07ce-3521-a810-8de00749e5ae | -4.34189 | -55.35387 | 2024-11-02 05:27:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8184d926-0ccf-3404-ace2-3905ebe0ccb4 | -4.34167 | -55.35622 | 2024-11-02 05:27:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9b6986b8-e018-31ac-b318-56e2d8b8c1a3 | -4.29881 | -55.12904 | 2024-11-02 05:27:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6786ea98-4bda-34ea-98e3-859dd4a17fbe | -4.27468 | -55.10717 | 2024-11-02 05:27:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ab9dd21f-53fe-3956-9280-8ef5661beba3 | -4.27339 | -55.14738 | 2024-11-02 05:27:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| a8f94e86-6d73-3f3f-b20c-0a98e828bbf6 | -4.27208 | -55.10928 | 2024-11-02 05:27:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dff07f43-5b28-386e-b712-ce82b0f4e663 | -4.2712 | -55.14479 | 2024-11-02 05:27:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2624e69b-49cd-3f90-893c-aa3a0b9c21f4 | -4.2696 | -55.14216 | 2024-11-02 05:27:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c9f235ac-fc66-36d1-9f9c-add73b72d65c | -4.26587 | -55.17953 | 2024-11-02 05:27:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ae7e9533-4077-3eb4-a303-4a529d5ea66e | -4.26452 | -55.17708 | 2024-11-02 05:27:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9daf32e6-0326-30bd-9929-4b42ab01cd7a | -4.26387 | -55.18158 | 2024-11-02 05:27:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 589a187c-77c7-3688-8c2a-3757b783affa | -4.21343 | -55.40483 | 2024-11-02 05:27:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 28f96e99-89e8-3f90-a478-6f61c62552ec | -4.1662 | -54.79276 | 2024-11-02 05:27:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8887a5df-b28b-3090-908f-4939bdfc1f03 | -4.16549 | -54.7975 | 2024-11-02 05:27:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0b587ce9-64d2-3ab9-b880-f5f59a355eae | -4.16095 | -54.79674 | 2024-11-02 05:27:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9e39e891-d024-3fed-8566-57afd961da79 | -4.15339 | -55.15088 | 2024-11-02 05:27:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2f3f3ba4-8e2f-3ce1-b700-f1a5c67e5e64 | -4.15274 | -55.1551 | 2024-11-02 05:27:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b4238036-9899-3ef0-93c4-975c11058b5e | -4.14246 | -55.43237 | 2024-11-02 05:27:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5e840c23-aaab-3205-8675-bcc2b57d45e8 | -4.0866 | -54.35254 | 2024-11-02 05:27:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bbd5cc45-0f9e-3f2e-95fa-7963a7dba6c6 | -4.08191 | -54.35189 | 2024-11-02 05:27:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b3a2805d-0708-3f41-a45f-80f35ec11585 | -4.07216 | -54.08271 | 2024-11-02 05:27:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0f2ae633-9f0d-3e7d-b1cb-45ea83b88013 | -4.01295 | -54.82269 | 2024-11-02 05:27:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a95c4b29-7ee3-3fb7-b0fd-9ba0e0ae0f82 | -3.88468 | -54.13465 | 2024-11-02 05:27:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5fb7f75e-117b-38aa-9498-4216e8ae0f58 | -3.88396 | -54.13961 | 2024-11-02 05:27:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0d6cde1f-e4db-3947-b740-69aaf913543e | -3.88326 | -54.13799 | 2024-11-02 05:27:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 19d1f284-e4f3-35f0-b5c6-31e27be9db12 | -3.8825 | -54.14297 | 2024-11-02 05:27:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0662a0b2-d2dd-3b87-b333-0f1c1a249de0 | -3.87922 | -54.13889 | 2024-11-02 05:27:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| a366ddaa-9174-38b2-9dd2-97962deda520 | -3.87852 | -54.13729 | 2024-11-02 05:27:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e6338553-eb7b-3fd6-a262-0d981317a6c2 | -3.87777 | -54.14224 | 2024-11-02 05:27:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7b0f972b-c25b-3bb3-b791-90ab54e598e6 | -3.75297 | -54.74521 | 2024-11-02 05:27:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 408b084e-1028-3a56-8987-bb1c7a7bf3b4 | -6.22695 | -55.65792 | 2024-11-02 05:27:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 698681d9-f657-3613-90fd-4c9acfc132b5 | -6.22653 | -55.65585 | 2024-11-02 05:27:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 4cffd047-4cc7-3309-b78c-947a60695968 | -6.22254 | -55.65724 | 2024-11-02 05:27:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c1f65b08-1443-3117-a794-d752a10374f1 | -2.12698 | -55.78696 | 2024-11-02 05:27:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 85ec9829-1e1a-34d3-8a08-c0db1ed1da45 | -2.06674 | -56.02096 | 2024-11-02 05:27:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 662a4211-4c82-3ee3-93a9-d7fb4ab01b79 | -2.06065 | -55.98003 | 2024-11-02 05:27:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b7e59f4e-a5ed-39b9-9067-c36f6f299809 | -2.04093 | -55.69793 | 2024-11-02 05:27:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 42440cbc-b8df-39a1-a840-2709147a9f06 | -1.99187 | -55.99497 | 2024-11-02 05:27:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7049e84f-1fe3-3176-b1d4-6a01668891e8 | -1.87872 | -55.68223 | 2024-11-02 05:27:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0add4a1d-0a0a-3555-b309-7f8a820dfa1e | -1.78208 | -55.41797 | 2024-11-02 05:27:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1e4ea558-e92b-3523-846a-eb8544845584 | -1.56583 | -55.8839 | 2024-11-02 05:27:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 1ecb81cf-4b78-388f-9991-4d3e2145abb7 | -1.56532 | -55.88419 | 2024-11-02 05:27:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 4dc49ab0-6ff3-3f69-8766-b8e923fd29de | -1.56177 | -55.88328 | 2024-11-02 05:27:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0c39a40b-6d89-3845-906e-fe3d1dd6491b | -1.56121 | -55.88683 | 2024-11-02 05:27:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 609c7679-a842-3f2f-a47e-af6eefb1e3cf | -1.56064 | -55.89038 | 2024-11-02 05:27:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README89.md)
