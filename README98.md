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

## Dados Diários - Página 98

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 321c63b9-4563-37a3-9ce1-be809f4955bb | -2.66651 | -53.34797 | 2024-10-12 05:21:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 271a1417-a118-34c9-ac9b-ad7ebdf5caf8 | -2.66642 | -53.34848 | 2024-10-12 05:21:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ab05eff5-f343-3685-916e-851a969e74f8 | -2.66588 | -53.35221 | 2024-10-12 05:21:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1ecb8056-7be2-35ff-80a7-bc2e3490d63b | -2.66576 | -53.3527 | 2024-10-12 05:21:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 668c2582-663c-3741-bf66-ae06c984dd1a | -2.66538 | -52.53366 | 2024-10-12 05:21:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1322d74d-bb6b-3611-9a09-6fe35dda38d7 | -2.66343 | -52.53109 | 2024-10-12 05:21:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2bbe9246-128d-349c-a97b-4afb972a4c1d | -2.66275 | -53.34307 | 2024-10-12 05:21:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 58e3a197-9561-36f7-b3aa-7cee6ed00f95 | -2.6627 | -53.34358 | 2024-10-12 05:21:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5fb727c5-36d5-3590-be82-c8d53b713a87 | -2.66212 | -53.34731 | 2024-10-12 05:21:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0527a385-61b8-313d-9574-fe366c8e2839 | -2.66203 | -53.34781 | 2024-10-12 05:21:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b4342fa9-15d1-3c22-9f1c-742fded67bf4 | -2.66149 | -53.35155 | 2024-10-12 05:21:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 96c7dd68-afb0-3cd7-be40-3c421bce9f7b | -2.66137 | -53.35204 | 2024-10-12 05:21:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c831dcb0-1520-3794-8e5a-1f9853ca0412 | -2.66087 | -53.35577 | 2024-10-12 05:21:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e443dda7-e930-3296-b488-c3426de03ae2 | -2.65878 | -52.53043 | 2024-10-12 05:21:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ef78161b-410e-3915-a675-e761a8ae9ec6 | -2.65773 | -53.34663 | 2024-10-12 05:21:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b7ccc3db-10cc-31fc-93d5-8f6804538443 | -2.65765 | -53.34714 | 2024-10-12 05:21:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e7f811f7-67c7-381f-a580-3461a6dab7fa | -2.65711 | -53.35087 | 2024-10-12 05:21:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| aec346ac-5b45-3590-839a-ef89a174d942 | -2.65699 | -53.35138 | 2024-10-12 05:21:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 505b5960-53e8-3985-ad49-a4723b762723 | -2.65335 | -53.34595 | 2024-10-12 05:21:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 22c815de-782b-3138-861a-f36af41c1212 | -2.65326 | -53.34647 | 2024-10-12 05:21:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7b7f2a6e-779e-3dfe-b9a2-d73c1674b327 | -2.65272 | -53.35019 | 2024-10-12 05:21:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9dc92f57-b5f0-3585-bef8-e1f9f9c00ce7 | -2.6526 | -53.35071 | 2024-10-12 05:21:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 23c835f6-971a-3924-8306-754bd53c5241 | -2.63732 | -52.54651 | 2024-10-12 05:21:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c09903ad-7126-37f9-8279-9cbcf9739c15 | -2.25692 | -53.47759 | 2024-10-12 05:21:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| aa41a934-e96f-377e-a680-62ff811975b3 | -2.25197 | -53.48108 | 2024-10-12 05:21:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9bf9a2c1-7b14-337d-bb2a-9a7b7dd7449c | -2.24765 | -53.4804 | 2024-10-12 05:21:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 206b33af-d867-3dcd-b368-ea5052a7d558 | -1.59589 | -53.3463 | 2024-10-12 05:21:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 1ef6e3e4-5643-3ec6-830f-d262241a7daf | -1.59527 | -53.35036 | 2024-10-12 05:21:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 8707d938-2a32-3f52-9997-5ec7f6302284 | -1.59157 | -53.34567 | 2024-10-12 05:21:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| cf4d24cf-e035-3601-86a4-98550114d0a3 | -1.58946 | -53.34703 | 2024-10-12 05:21:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9a22c971-6b30-359c-a977-0c37cdb3cab1 | -1.17072 | -53.39814 | 2024-10-12 05:21:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 909b353f-e89f-38d9-ac1e-0d2a4023f1ce | -1.16644 | -53.3975 | 2024-10-12 05:21:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 504d1861-c306-3b48-91ce-1b259b8b7e5b | -1.16156 | -53.40082 | 2024-10-12 05:21:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d9993569-fa18-3693-8934-90cb5f7da2a5 | -1.16096 | -53.40477 | 2024-10-12 05:21:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| efb433be-0e21-39ff-af8e-0cd804e02c5d | -1.11598 | -53.61494 | 2024-10-12 05:21:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0b50898c-189e-35fa-a6c3-6ca2f275fd82 | -1.11545 | -53.6159 | 2024-10-12 05:21:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 15023034-ddfa-321f-9701-0d9d2a69de66 | -1.11536 | -53.61902 | 2024-10-12 05:21:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b1d826de-b34b-3f73-8f66-a818c9836df0 | -1.1148 | -53.61997 | 2024-10-12 05:21:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 01e24ffb-9401-358f-8476-5c4dbe241866 | -1.11121 | -53.61543 | 2024-10-12 05:21:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ed20f6e2-1117-3f4e-8544-00ef2e159b15 | -1.11113 | -53.61852 | 2024-10-12 05:21:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3d72a583-50bd-3a8a-93da-310fff7c46c4 | -2.10278 | -54.69646 | 2024-10-12 05:21:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 9708db75-9f24-3287-80c1-e1d149a2b2a6 | -2.10199 | -54.70155 | 2024-10-12 05:21:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 744e490a-803d-370f-82d6-c5d00a04c62d | -1.92063 | -54.58595 | 2024-10-12 05:21:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e85a3ab4-09a1-36cc-9d76-913918b3f1e2 | -1.91663 | -54.58534 | 2024-10-12 05:21:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 95414a82-b27f-301b-ba21-91a2f49aca86 | -1.90009 | -54.42754 | 2024-10-12 05:21:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 42f227c7-e315-31bf-94d2-f7391caa9bb3 | -1.8966 | -54.42339 | 2024-10-12 05:21:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 778852b9-ca43-3ec4-a32e-d876c3fd1cab | -1.89605 | -54.42692 | 2024-10-12 05:21:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a6b65b53-b124-3424-9159-2aad0d3197ac | -1.89551 | -54.43044 | 2024-10-12 05:21:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| a41d6c3f-74b8-39f5-b167-cbafff5149d1 | -1.89348 | -54.62895 | 2024-10-12 05:21:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 5b2e809b-d1eb-32ad-ae3a-6df7a5fd1fc9 | -1.89256 | -54.42278 | 2024-10-12 05:21:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 3766760b-3203-39df-a481-27d55f76a63d | -1.89202 | -54.42629 | 2024-10-12 05:21:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 7402be3a-9c7c-3bb2-938f-8fb08a1558f1 | -1.88907 | -54.41863 | 2024-10-12 05:21:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 40564d71-1712-3253-b64e-a9455ccfd250 | -1.88853 | -54.42215 | 2024-10-12 05:21:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 7b78316f-277f-371d-92b0-37b015e2d3df | -1.88799 | -54.42567 | 2024-10-12 05:21:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| cfa29861-af6e-3853-a3e7-3ea0ae287534 | -1.88745 | -54.42918 | 2024-10-12 05:21:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 469c42d8-fbf9-3e90-b1d4-b94ecaa61813 | -1.88449 | -54.42152 | 2024-10-12 05:21:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e727bbef-23e7-3275-9f0c-5267c3050bc2 | -1.88396 | -54.42503 | 2024-10-12 05:21:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3eee35b7-40e4-347a-9f90-c1620c2462f9 | -1.88342 | -54.42854 | 2024-10-12 05:21:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e323f192-3233-3e96-acd9-58c76a269269 | -1.88288 | -54.43204 | 2024-10-12 05:21:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| aac1f67f-dba5-3f1b-9099-51b869c1f73a | -1.88235 | -54.43555 | 2024-10-12 05:21:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8d2807b7-48fa-360b-8073-916a92b7ff85 | -1.87939 | -54.42789 | 2024-10-12 05:21:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d6bb342d-e95d-3b82-8ef2-8a3b55f39d5a | -1.87885 | -54.43141 | 2024-10-12 05:21:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| cdcbc62e-5f3c-31d2-a21f-6f1a50b3c9b9 | -1.87832 | -54.43492 | 2024-10-12 05:21:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 81282d69-2362-313a-9d02-ef7f293a1f64 | -1.87778 | -54.43843 | 2024-10-12 05:21:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f12c4d22-edc5-39ff-a05c-97e5ecf999fb | -1.87536 | -54.42727 | 2024-10-12 05:21:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 494b5426-cd17-35fa-a2bb-b0ac3cda1597 | -1.87482 | -54.43079 | 2024-10-12 05:21:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4b4b16df-ea52-36b8-baf2-6c2232ce6f20 | -1.2701 | -54.67968 | 2024-10-12 05:21:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 79f54dfb-c657-365e-abed-c4d29ab2e14f | -1.26961 | -54.6762 | 2024-10-12 05:21:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3609aec9-cc41-32a9-8908-c1c6b88384d3 | -1.26885 | -54.68119 | 2024-10-12 05:21:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b946277e-7369-3693-8617-5e3922b5db0c | -1.26616 | -54.67913 | 2024-10-12 05:21:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 5f8abbf5-7ace-3d87-bf6c-1b4e124283b0 | -1.26567 | -54.67564 | 2024-10-12 05:21:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b060f13d-6431-3706-ba02-a2eff6f9f45c | -1.26538 | -54.684 | 2024-10-12 05:21:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 4bbacdae-950a-3591-81b7-73edf1196e52 | -1.26491 | -54.68064 | 2024-10-12 05:21:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 84e42052-92cc-316b-8702-f936d37861e5 | -1.26417 | -54.68549 | 2024-10-12 05:21:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8161d0a4-8d35-336c-8365-96785faf25bf | -1.26222 | -54.67859 | 2024-10-12 05:21:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 20732cba-3f86-3b3a-af34-4e02c19129a2 | -1.15894 | -53.78091 | 2024-10-12 05:21:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1889c47b-d121-3987-9447-5c3b11f607ec | -1.11571 | -54.05679 | 2024-10-12 05:21:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 109ad082-0d6b-3dbc-a8df-e5acab044a51 | -1.02492 | -53.7282 | 2024-10-12 05:21:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6fd27277-5ee7-36a3-a0bb-515178d9042a | -1.0207 | -53.72792 | 2024-10-12 05:21:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ffefe464-545d-3368-899e-5619db1fab9e | -1.02011 | -53.73176 | 2024-10-12 05:21:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c182d783-ddf9-3a01-bf04-d37bee733b49 | -2.22637 | -54.92916 | 2024-10-12 05:21:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a25e248d-ab44-3f89-ab86-05c18f6f4fed | -2.18577 | -54.48526 | 2024-10-12 05:21:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 39a749b2-00c5-39aa-83ca-3d9c5f9f485a | -2.18173 | -54.48465 | 2024-10-12 05:21:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9736c46c-3544-3460-865b-a3522ab64e30 | -2.17769 | -54.48405 | 2024-10-12 05:21:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b3a0fe1c-b26d-34f1-a814-a868902377f8 | -2.10676 | -54.69707 | 2024-10-12 05:21:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 0cdaf1c6-901d-3c1c-813c-fd31a7d1f936 | -2.91431 | -54.0208 | 2024-10-12 05:21:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 96bb9918-c5cb-3f87-812e-d92b7efe66ca | -2.81761 | -54.71445 | 2024-10-12 05:21:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a0e71a22-9ed4-352f-85b5-b5620b5884c1 | -2.80612 | -54.08334 | 2024-10-12 05:21:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1d329c34-6e9a-30c7-ad6b-3d37afd96ea9 | -2.80251 | -54.0789 | 2024-10-12 05:21:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e8ff1d18-0a3f-394b-b641-4cb6a0032e13 | -2.80194 | -54.0827 | 2024-10-12 05:21:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 00f31b43-dc9c-36a2-809c-64a597ed37ab | -2.79833 | -54.07824 | 2024-10-12 05:21:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5e5fc600-1a22-3d0f-b9fa-62bd177897c3 | -2.79718 | -54.08586 | 2024-10-12 05:21:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 262d1528-64f0-3094-80f1-675edb419f9a | -2.7919 | -54.00695 | 2024-10-12 05:21:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| db614d67-c496-3ab9-a5fd-ea4d405111db | -2.79132 | -54.01079 | 2024-10-12 05:21:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| d766ac95-90c7-33ee-a26a-99e4c5d542e9 | -2.79075 | -54.01462 | 2024-10-12 05:21:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 107f6149-6fda-3f2e-a513-839dc44b908d | -2.7877 | -54.00627 | 2024-10-12 05:21:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| dc6e2caf-b05f-3fd4-a4ff-1c1f6521d045 | -2.78425 | -54.02933 | 2024-10-12 05:21:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6e6906f1-3178-3b9d-a5b6-97362aa894b4 | -2.78005 | -54.02869 | 2024-10-12 05:21:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cdad3d73-9947-3c53-8f4c-7ca7dea12ffa | -2.57672 | -54.25967 | 2024-10-12 05:21:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 67982f20-a0dd-3fe6-a57c-24ae68a02d12 | -2.57616 | -54.26332 | 2024-10-12 05:21:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |


[Clique aqui para ver as próximas entradas](README99.md)
