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

## Dados Diários - Página 75

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ef560a7d-c3f9-30fb-8a7a-3aa8dc0709da | -3.39599 | -50.30502 | 2024-11-21 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f73e76e4-5ec5-349a-ab52-2f22e1bc1a97 | -3.35855 | -50.18031 | 2024-11-21 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 2220d2d7-ea07-31c4-8ec8-1c1a6a28b099 | -2.81384 | -54.02456 | 2024-11-21 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3b5e6109-8881-3625-86f5-eae21a18c954 | -2.1371 | -54.50398 | 2024-11-21 04:55:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c8bf33b7-d3a5-3e4e-a772-27ff6a8c6907 | -2.57409 | -54.07925 | 2024-11-21 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| beacebb3-a07d-3b21-9126-976ea5a71b8a | -2.70975 | -53.1761 | 2024-11-21 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a242ffdc-7058-36b1-9783-60ec884c58d8 | -3.3882 | -53.26838 | 2024-11-21 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 454e055a-f18c-3357-a0cb-309e1f59c8fb | -3.48763 | -50.31761 | 2024-11-21 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dc204334-5f7e-3704-a158-903c047a2312 | -3.30071 | -51.29278 | 2024-11-21 04:55:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9f9eef46-7df6-388d-8378-f123640e25aa | -2.76237 | -52.12045 | 2024-11-21 04:55:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 235c43c5-9a5e-3ae2-86b8-d5c9ced38c19 | -4.05334 | -54.22276 | 2024-11-21 04:55:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1b45d8ff-ce76-3f13-855b-0976855e20f6 | -3.18754 | -54.32542 | 2024-11-21 04:55:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b59b0bc1-0a1c-35a2-aa7e-91a8fde59b94 | -2.57732 | -53.97305 | 2024-11-21 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 37350ff7-c6c3-342c-95c0-7fdd916db13d | -3.33649 | -54.07108 | 2024-11-21 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 55eb8562-81fd-3276-9ec2-a47a046dd501 | 1.1598 | -50.69736 | 2024-11-21 04:55:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b5a61699-8a9b-3b08-8c21-38a888be4c97 | -2.63366 | -54.28133 | 2024-11-21 04:55:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f181bdf6-044a-33b1-b59f-da56bb6a447e | -4.10609 | -51.04935 | 2024-11-21 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2f64a3e4-614d-35ba-88db-0dedf440492d | -2.9073 | -53.06258 | 2024-11-21 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2c612811-6e42-350f-b6c2-431c7fcc853b | -3.66337 | -50.44303 | 2024-11-21 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 33b7db57-4b6e-3ae0-b743-f25aae4d6030 | -3.1689 | -49.15636 | 2024-11-21 04:55:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f2b0a195-604b-3913-8fac-986e33bce699 | -4.08848 | -54.08658 | 2024-11-21 04:55:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0c22e7ab-c24b-3e82-8681-9d0247bead26 | -3.04324 | -49.46797 | 2024-11-21 04:55:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b87b1d5a-a584-3d66-b327-1004b5f0f0aa | -3.46519 | -54.56599 | 2024-11-21 04:55:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a9010794-a044-31aa-ac1c-c87fe84a810e | -3.49195 | -50.11714 | 2024-11-21 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7ab8e57a-049e-3a54-850a-51f52cb019ec | -4.38606 | -47.77715 | 2024-11-21 04:55:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 275d06e6-dfb9-3d2a-b69e-323b68db6fc0 | -3.42037 | -49.22512 | 2024-11-21 04:55:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 6d36b5ee-8394-3bb5-8678-3c1bd3118acd | -4.14908 | -49.22528 | 2024-11-21 04:55:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 2c9de5a6-5b3b-3e85-8684-fc7e6e8c9b8a | -4.57558 | -48.01807 | 2024-11-21 04:55:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d8abf907-fcb2-3bc1-beca-fc6f27c2885f | -2.80146 | -51.80104 | 2024-11-21 04:55:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4aa327d5-f406-3dc7-809d-aad8455af49d | -3.81315 | -51.14562 | 2024-11-21 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 03840863-045b-3aea-a2c9-2697f51ad2d8 | -3.39427 | -53.27284 | 2024-11-21 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 675bb3a5-edd9-365d-8971-80805eeb2ee4 | -3.05808 | -54.41232 | 2024-11-21 04:55:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 31582e3b-c974-3728-b591-ff22c07e44ce | -3.07172 | -51.25474 | 2024-11-21 04:55:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b3d0a69a-7ca6-3ee7-8ef1-8b4016470f2a | -3.86835 | -54.36114 | 2024-11-21 04:55:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a96bf9a4-d033-3dd6-81f7-dac6ebaf94bc | -2.75281 | -52.1016 | 2024-11-21 04:55:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f1e3698a-dcc0-3efe-a8d8-9b3861a540c0 | -3.08709 | -53.3022 | 2024-11-21 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cac5a932-bfa9-3a1d-9d00-a28a38dd76d1 | -3.36152 | -50.18514 | 2024-11-21 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1071bfc1-8624-3e43-9029-5c3240517488 | -3.08699 | -54.55375 | 2024-11-21 04:55:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3295aa8f-ac28-3d34-a356-3023b982720b | -5.23574 | -42.64132 | 2024-11-21 04:55:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dc1f35ea-217c-3635-8321-7aa775207aa7 | -3.25914 | -50.63165 | 2024-11-21 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5af19961-9dbd-3840-8778-3f44c75c2e07 | -3.23274 | -54.10458 | 2024-11-21 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 378ef718-5312-3185-8dbb-877dcd7612ff | -2.59505 | -54.01131 | 2024-11-21 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 268c4f84-bc24-364f-8269-89290ff3645e | -3.49395 | -48.22863 | 2024-11-21 04:55:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a3f97e77-cb3b-3d32-9c9e-61183df1f65f | -2.75807 | -54.05457 | 2024-11-21 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c31aeaa1-c7a4-333d-9d6c-45ecb8b60009 | -4.15889 | -42.02427 | 2024-11-21 04:55:00 | NOAA-20 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 7845286c-b4ad-3635-b50e-0e4aab237e23 | -3.42291 | -53.28439 | 2024-11-21 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 11016dc8-9ca6-3dfc-adea-53d942e6c896 | -2.5962 | -54.04707 | 2024-11-21 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 15cee1cd-63f5-3043-b096-25d55737d98b | -3.10265 | -53.7443 | 2024-11-21 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 26d8b014-eff9-3e11-a5ef-51a5a13fa086 | -2.75584 | -54.04711 | 2024-11-21 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a8b45182-0bcf-380b-b4ec-c8345e3fcc34 | -3.3607 | -51.05555 | 2024-11-21 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9da2577c-f694-3a85-b3dc-4da0c0d9da9b | -2.99511 | -52.37307 | 2024-11-21 04:55:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5e49275d-35a4-3b04-a809-e4e7bacb8efb | -3.28912 | -53.85497 | 2024-11-21 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| d5596b12-d61a-3f70-a50e-8a46a7df2026 | -3.04253 | -49.47256 | 2024-11-21 04:55:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f2813e4a-32d8-3305-88bc-0c928c8900f0 | -4.10422 | -50.31823 | 2024-11-21 04:55:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6a381cc9-1481-392e-b5dc-537178692f22 | -6.11656 | -42.52058 | 2024-11-21 04:55:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 6e712427-9628-34b2-99c5-c6a5037000c8 | -2.55902 | -53.95918 | 2024-11-21 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 71107708-d9e0-3044-af18-c2e642c57991 | -3.08549 | -49.47258 | 2024-11-21 04:55:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 61e299be-cd11-3d4b-84b5-323af4377ab7 | -3.77162 | -51.68701 | 2024-11-21 04:55:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 90eb1d1d-3789-39ea-a1ad-6fecfb0f79d3 | -4.09131 | -51.07498 | 2024-11-21 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 09a01be5-2d81-329a-a71c-ac05eb72ca24 | -3.26869 | -53.83416 | 2024-11-21 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 31e772fb-7a04-3671-b20b-c30b82d03c92 | -3.86111 | -52.32906 | 2024-11-21 04:55:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 51fe712c-5233-3298-a1f9-13b6c5fa7327 | -3.29991 | -50.36769 | 2024-11-21 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 449c76c8-4d59-306c-8a5d-1b86a4c838d5 | -4.63404 | -49.54487 | 2024-11-21 04:55:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 09cfe625-b860-3a5e-954a-ac2b6d6b14c2 | -2.61805 | -54.37951 | 2024-11-21 04:55:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| de87e698-a200-37f8-8a97-96658832588e | -2.59291 | -51.71459 | 2024-11-21 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 66e7031c-9c13-3c36-b8bf-4bd7cc25bbf3 | -3.48167 | -50.30818 | 2024-11-21 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 72839912-3ad3-3f22-abbf-ba0a4d5ec141 | -3.25846 | -50.82222 | 2024-11-21 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| bf1493d3-ec3b-3729-968d-382ff66b4166 | -7.98823 | -55.31541 | 2024-11-21 04:55:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e7d20a93-0bd1-3e77-9d17-deeaf57105ef | -2.99746 | -51.46117 | 2024-11-21 04:55:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 723c2596-80d4-3c4e-83fc-504c3c168dae | -2.90454 | -53.05862 | 2024-11-21 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f567b92a-917f-3bc1-8094-9ff407736b86 | -3.18422 | -54.32491 | 2024-11-21 04:55:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 29ecc5f6-0e59-3824-948c-90269e7227e5 | -3.10476 | -49.44749 | 2024-11-21 04:55:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 21f59f82-d4c6-322f-8229-e267152a167f | -5.95127 | -44.46833 | 2024-11-21 04:55:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6f4fcc79-d00e-3077-ad51-35032ee01c1b | -2.75975 | -54.06549 | 2024-11-21 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 235318c6-d953-3e1a-a14b-ebe11f1df894 | -3.70979 | -53.75187 | 2024-11-21 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 99d7cb1c-18f5-3c0d-9916-c074fb138dd5 | -4.10417 | -48.48597 | 2024-11-21 04:55:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 267e22bc-dd02-3d74-9d10-ea09fa6a7974 | -2.72519 | -51.81598 | 2024-11-21 04:55:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8f962aed-635f-3c74-ac2c-d08f4a8fc436 | -3.80019 | -52.22206 | 2024-11-21 04:55:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 16d4073c-1baf-3534-8bbb-9d1f44bbacf5 | -2.92275 | -53.07201 | 2024-11-21 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5c435b8d-84eb-397c-b72b-852685f6b33f | -4.88605 | -45.84011 | 2024-11-21 04:55:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 58091add-3949-30bb-a2c4-f0842c7ae72a | -3.05007 | -52.76003 | 2024-11-21 04:55:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a9a982c5-5e2a-3849-ae57-aa6c0fa72eb4 | -3.30351 | -50.36823 | 2024-11-21 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 21e7cc9e-4001-358a-85a4-ed5bbaebceb2 | -3.23915 | -51.30268 | 2024-11-21 04:55:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| add27bb6-ab2b-3cb7-9742-64b72a5620ed | -3.64558 | -52.36156 | 2024-11-21 04:55:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d3ef2877-1752-39d3-a3a8-e994a19b88ae | -4.7658 | -44.49629 | 2024-11-21 04:55:00 | NOAA-20 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a7bedada-b05c-3748-970f-cf3ff23bf756 | -2.82666 | -54.09407 | 2024-11-21 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7e57fb50-e29a-30e2-b075-2fdb203bf329 | -3.71274 | -51.186 | 2024-11-21 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9cfb477c-38a2-380e-9cd3-6d49cbb38e2b | -2.77025 | -54.06357 | 2024-11-21 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ff344166-72ad-3000-b719-756789d6d8c9 | -3.53641 | -54.59156 | 2024-11-21 04:55:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6754f6bc-a936-327d-b9fe-bdd57eda5ff5 | -3.35724 | -50.18877 | 2024-11-21 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 1a202ab2-15dc-3281-a276-6d63fe13d301 | -3.42897 | -53.28886 | 2024-11-21 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0a6b1aaa-2061-356a-9365-54750fbcc309 | -3.39701 | -50.10264 | 2024-11-21 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 129673de-e62c-3430-bef6-eb33043499f8 | -4.14985 | -43.88066 | 2024-11-21 04:55:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| e9a2c749-a896-39e3-bcec-c517eebb61fa | -3.29189 | -53.85893 | 2024-11-21 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 9e6f1c3a-0a6d-31d3-9dd9-40d78f4b1115 | -3.14863 | -54.48435 | 2024-11-21 04:55:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 39a8bbfc-65ac-3a7f-ae83-dcef19fc54b0 | -2.7268 | -51.73872 | 2024-11-21 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ac8c9b79-0edb-3fe8-a9d7-29628074f800 | -4.14132 | -49.22409 | 2024-11-21 04:55:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f6635b79-431c-3c51-b790-9e975578a450 | -3.05974 | -54.40185 | 2024-11-21 04:55:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3f3b5e4d-899b-30a3-af8c-2f8543d5431f | -3.28577 | -53.83328 | 2024-11-21 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 2923ae8f-baf0-3282-b8b8-c5f714a4a995 | -2.7489 | -52.10463 | 2024-11-21 04:55:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |


[Clique aqui para ver as próximas entradas](README76.md)
