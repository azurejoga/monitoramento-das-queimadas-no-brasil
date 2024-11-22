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

## Dados Diários - Página 64

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 999afb36-06d8-3ac6-84d3-fc59c36847d1 | -3.29 | -53.85385 | 2024-11-22 05:52:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| e9808c31-1199-3f69-a14a-7a45e6b2917e | -3.20746 | -54.25706 | 2024-11-22 05:52:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 2edee97b-0132-330e-b44a-a366d4248029 | 1.38303 | -55.94196 | 2024-11-22 05:52:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d49e80c9-e7d3-39db-83c2-6f55faeec6f8 | -3.19892 | -54.24891 | 2024-11-22 05:52:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| df9d9081-a076-31ea-927f-9714780efd2d | -3.57173 | -54.685 | 2024-11-22 05:52:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f785abff-bea3-3f78-832c-ef32b69e9555 | -2.15957 | -53.79074 | 2024-11-22 05:52:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 385cad4e-d58d-3446-908c-c830170f647f | -2.00645 | -54.51646 | 2024-11-22 05:52:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2afdad31-c40e-3c13-b915-e5a0b06f7534 | -3.20839 | -54.2509 | 2024-11-22 05:52:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 2047136f-3e99-3c1b-9d7f-8664f86294c7 | -3.2234 | -54.24636 | 2024-11-22 05:52:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 10f22c95-094b-3fe6-81eb-a2a697838137 | -3.20595 | -54.24979 | 2024-11-22 05:52:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| f821f8d7-6114-3821-a3fe-7c015ebc3e7a | -3.21545 | -54.25158 | 2024-11-22 05:52:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 87b40a4b-965f-39f1-92ca-61acd3e28043 | -3.58141 | -54.51774 | 2024-11-22 05:52:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f12eb672-a5e0-3aa1-ae5d-7301719b529e | -3.20507 | -54.25588 | 2024-11-22 05:52:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 3b5eba5c-406d-3ecb-aeba-178207a9af75 | -3.57952 | -54.67955 | 2024-11-22 05:52:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 97195f4d-683c-3de8-8462-aee4187cafdd | -3.22245 | -54.25265 | 2024-11-22 05:52:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| b4708f80-7c98-3f5b-a6b4-6a8c561a7588 | -3.24981 | -54.2436 | 2024-11-22 05:52:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| b0e189a3-b7a3-339c-b7ba-d5c42d8001ce | -1.20872 | -53.68616 | 2024-11-22 05:52:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| b7184773-da0e-3848-a464-3be6560de55d | -3.24795 | -54.25631 | 2024-11-22 05:52:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 85e4795a-60c5-3895-9a8e-1fdb5509026e | -3.28603 | -53.83158 | 2024-11-22 05:52:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 6af0055d-ee19-3e0a-b6c3-62c266566e43 | 1.37712 | -55.94294 | 2024-11-22 05:52:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7746cfaf-365a-39e4-8475-19518d4dc82d | -2.22248 | -53.72995 | 2024-11-22 05:52:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 22f8db12-3b58-3f31-8edc-3846663eadc8 | -3.27781 | -53.83745 | 2024-11-22 05:52:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 13d7df81-c486-3d09-8a75-58bf5bc3a0f7 | -2.73989 | -54.13426 | 2024-11-22 05:52:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8793bdba-7afd-3c9e-bb0b-2434567d2bfe | -3.22795 | -54.24615 | 2024-11-22 05:52:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 13.7 |
| a34d54b8-169a-3add-baa8-bc2450363dd5 | 1.40136 | -55.91945 | 2024-11-22 05:52:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ac6e8982-b80e-3a3f-aab7-8ae8981e737d | -3.28496 | -53.83868 | 2024-11-22 05:52:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 6d97f58d-bbf1-38ae-b1b0-47434fe7eda0 | -3.51598 | -54.68493 | 2024-11-22 05:52:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6926d7e7-bf30-3940-9518-d9cd03fe0162 | -3.25678 | -54.24495 | 2024-11-22 05:52:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 48d6c974-3940-37c7-a5c8-fc91beb95acc | -1.1233 | -53.39482 | 2024-11-22 05:52:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8bcb9b80-9eab-3a26-9cdb-585264a11885 | -3.29216 | -53.85265 | 2024-11-22 05:52:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 18049e58-151a-3e08-8b60-6575413d97be | -3.17677 | -54.31887 | 2024-11-22 05:52:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d5132356-3514-3fb6-8122-b47de0359110 | -3.5153 | -53.81319 | 2024-11-22 05:52:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 063c36f9-8805-3bfb-b437-550d5b548843 | -1.13315 | -53.40509 | 2024-11-22 05:52:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| c31368e1-f237-3c1d-bc6e-6124eb3c42ed | -3.26666 | -53.82594 | 2024-11-22 05:52:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1e3f07ae-6c15-3f01-ba08-c7c4bef59caa | -1.5965 | -53.81016 | 2024-11-22 05:52:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| aa43bfda-eb2d-3fd1-9a5c-5bf72baaf413 | -1.20503 | -53.688 | 2024-11-22 05:52:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| dcae14c5-26ac-33a2-b06f-f02de1088080 | -3.50779 | -53.80441 | 2024-11-22 05:52:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| e5cac008-0788-3187-a033-96622ad5e6f4 | -3.5797 | -54.68065 | 2024-11-22 05:52:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4886c60e-c36a-3ff9-bd85-18512cdfe3f4 | -1.59423 | -53.80512 | 2024-11-22 05:52:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| e3bd42a3-0b72-3ac2-b9bb-328b0c510419 | -3.28804 | -53.83035 | 2024-11-22 05:52:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6605fafb-df76-334b-bbf2-f883edfed228 | -3.22184 | -54.23888 | 2024-11-22 05:52:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 00ffc91c-1267-3ee6-bf53-2e7916f067c7 | -3.2718 | -53.82858 | 2024-11-22 05:52:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| c5330f72-faf5-32ab-8c4b-28fcd53f18c8 | -3.27293 | -53.82107 | 2024-11-22 05:52:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| a5716696-7964-321b-8c6d-05c2fdb05bbc | -3.32648 | -54.09537 | 2024-11-22 05:52:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 385864fc-5135-368a-9d9c-5bcbabf4b2e8 | 1.37258 | -55.95237 | 2024-11-22 05:52:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 43d0bd2c-c534-3bcb-82a3-af879d0d0a62 | -3.23404 | -54.25355 | 2024-11-22 05:52:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 13.7 |
| b935ec4a-9f89-3025-9957-923fdb19ab31 | -3.32284 | -54.09013 | 2024-11-22 05:52:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| dff2f061-bb55-3f17-a70d-af86831d0232 | -1.11615 | -53.39362 | 2024-11-22 05:52:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7ad0e5b8-c91a-3f9b-908e-df94c01f98d7 | -3.57284 | -54.67966 | 2024-11-22 05:52:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 608095a0-4732-3e9d-86c1-9bd028cd18f7 | -1.21225 | -53.68795 | 2024-11-22 05:52:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 7a1f7372-d944-31af-a1bf-557eb29f5068 | -3.24376 | -54.23597 | 2024-11-22 05:52:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 23d09c24-c689-321c-85c0-dc7ec3793785 | -2.00107 | -54.51899 | 2024-11-22 05:52:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7d5e08d9-c25d-3e83-8a3c-d3dd9ce796c7 | -3.20684 | -54.24355 | 2024-11-22 05:52:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| c83a85ba-648a-399b-9f54-0961ff13f3a9 | -2.20172 | -53.65661 | 2024-11-22 05:52:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3c7fdd17-420d-3b9a-b50a-59f6ec28c68f | -3.22977 | -54.23356 | 2024-11-22 05:52:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 4e4fd654-c160-3ff8-a1c2-ebbff76eaead | -3.57875 | -54.68702 | 2024-11-22 05:52:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a054de23-2668-3f34-8b02-9bcd7ac35370 | -3.23676 | -54.23476 | 2024-11-22 05:52:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 3b10a62b-f628-3bf7-8459-55a836cef1f6 | -1.20149 | -53.6862 | 2024-11-22 05:52:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| b3794d2b-5417-3abf-bbcc-8d04e80494cd | -3.50265 | -53.79869 | 2024-11-22 05:52:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| d31d833c-3d80-3edc-90ba-4c5ea7c09ce9 | -3.11062 | -54.292 | 2024-11-22 05:52:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a8897793-ca92-3fba-86a3-3ab497bb11d9 | -1.07323 | -53.36645 | 2024-11-22 05:52:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 3fdf4056-1b1b-33b1-94a4-7a071cf2ef69 | -3.21392 | -54.24413 | 2024-11-22 05:52:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 83ed78d0-57d3-3f6c-9c7e-8aaa059622be | -1.25538 | -53.35929 | 2024-11-22 05:52:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6213fc0a-7389-327f-bf99-064ffd2c25b4 | -2.5068 | -54.14984 | 2024-11-22 05:52:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 59bdc4cf-94e7-3a1e-8746-a79bb36ac593 | 1.40327 | -55.91661 | 2024-11-22 05:52:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 19a3f0b7-e6cf-35b8-8497-deaf9da66e8f | -3.20932 | -54.24473 | 2024-11-22 05:52:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 87a41bff-1426-31b9-aa96-05ae749afcf5 | -2.50581 | -54.15626 | 2024-11-22 05:52:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4f65acde-91f9-3a9f-8273-f509da20c244 | -3.11046 | -54.28484 | 2024-11-22 05:52:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c3eb3eeb-316c-3b91-84e6-cac3cbb1f158 | -2.51227 | -54.15297 | 2024-11-22 05:52:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 41dbc247-2c88-32bc-9a04-68677739ccc4 | -3.52148 | -54.64725 | 2024-11-22 05:52:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 35c3747a-8232-3bf3-bfb7-c95920428341 | -3.28894 | -53.86092 | 2024-11-22 05:52:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| ccf778f8-fed6-322a-b094-de7562a0d361 | -3.64501 | -54.32135 | 2024-11-22 05:52:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 47048952-083b-3337-ba3b-829f87d0630e | -3.18274 | -54.32668 | 2024-11-22 05:52:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 7df913fd-f393-357d-a80c-b24dfffbc372 | -3.50883 | -53.79746 | 2024-11-22 05:52:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 53dba0ae-8039-3491-9330-5d6211f4616a | -1.12602 | -53.40384 | 2024-11-22 05:52:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 64ee996d-7050-3388-ae9f-a2ad2a43d746 | -1.44615 | -53.39109 | 2024-11-22 05:52:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| d56f417c-9c3c-3091-838e-b7579c8332d8 | -0.14708 | -60.86967 | 2024-11-22 05:52:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7d009871-2279-3201-bd43-2ad94df217a9 | -3.285 | -53.85147 | 2024-11-22 05:52:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 955ea99b-64c0-3520-bd49-637e6c857ccb | -3.19474 | -54.32788 | 2024-11-22 05:52:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 55db8803-85ce-35c2-af3c-2ca6b59bed41 | -1.12937 | -53.40307 | 2024-11-22 05:52:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4f471545-6e20-3e41-9b27-a7c6267988ad | -3.23305 | -54.26036 | 2024-11-22 05:52:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 21.1 |
| eb4adcb4-3b44-37d6-b58c-72875d9b7a8f | -3.21303 | -54.2503 | 2024-11-22 05:52:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 846cc911-137c-35d3-b95a-c0ee3c778abc | -3.18274 | -54.3121 | 2024-11-22 05:52:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| db01a68c-c393-3d0a-be84-d5d4155d7d99 | -11.36931 | -57.57825 | 2024-11-22 05:57:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| e12e8b68-0c2f-39c3-8aa7-5dbc9b2f2ea7 | -11.37093 | -57.57627 | 2024-11-22 05:57:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| cb50055c-1505-30bb-a97d-36ab4ab1f41e | -11.36994 | -57.57302 | 2024-11-22 05:57:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| fd0d2315-415c-315a-a5b6-b2ec5f4323b4 | -3.50354 | -53.79349 | 2024-11-22 05:59:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 18.3 |
| 87b8b572-2113-358b-b41f-34226df206a5 | -3.20569 | -54.24784 | 2024-11-22 05:59:00 | AQUA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 22.8 |
| eff75ccc-b2b4-336d-b5f6-2c226ba4eb53 | -1.60766 | -52.5779 | 2024-11-22 05:59:00 | AQUA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 207ca7e7-f748-310e-92a5-ac94f62b63c3 | -1.62122 | -52.42212 | 2024-11-22 05:59:00 | AQUA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 9468ba66-4a8b-36bd-a323-2539ab89499e | -2.84636 | -53.99894 | 2024-11-22 05:59:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 997793a6-31a1-336f-b83b-aba99e77ba4a | -1.20273 | -53.67949 | 2024-11-22 05:59:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| e464455d-bbe1-336e-8ae2-4b8a9d6d96c6 | -4.14127 | -54.6598 | 2024-11-22 05:59:00 | AQUA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| ce46e0fc-0524-3744-974b-b111d4b88786 | -3.09756 | -54.28954 | 2024-11-22 05:59:00 | AQUA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| afedd6fa-a50b-3994-a720-748a9cafd00c | -2.74409 | -54.12309 | 2024-11-22 05:59:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| ac9ed002-d84c-3273-aba0-f9b23c0249e3 | -1.73581 | -52.39575 | 2024-11-22 05:59:00 | AQUA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| c1cd8aee-37c4-3fc7-b385-6c24bf7eee44 | -1.45769 | -52.66058 | 2024-11-22 05:59:00 | AQUA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 02b2f39a-63bb-3cfa-81b3-f73744c14fba | -1.60604 | -53.26917 | 2024-11-22 05:59:00 | AQUA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| ec7bfeb2-333a-399b-afc0-faa00536bbc4 | -3.51249 | -53.79477 | 2024-11-22 05:59:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 149e993a-7fb3-3e38-8e02-09e38e10dc53 | -2.56781 | -54.06693 | 2024-11-22 05:59:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |


[Clique aqui para ver as próximas entradas](README65.md)
