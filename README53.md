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

## Dados Diários - Página 53

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 286804ae-635b-315c-880f-a80dda7aabba | -0.03324 | -49.64477 | 2024-11-23 05:10:00 | NOAA-21 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e1945013-0137-3071-b50f-8b7f22be79a9 | -1.43066 | -53.38419 | 2024-11-23 05:10:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ebdca7fb-97e0-34b0-9da8-514622b2e301 | -1.62301 | -52.43029 | 2024-11-23 05:10:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ab3d2f3c-0a24-39b5-b9f1-beaa499eb820 | -2.14745 | -50.91698 | 2024-11-23 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 54520f3e-e240-3bee-95e6-d29d889118df | -1.63543 | -52.60355 | 2024-11-23 05:10:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 61853ad0-f3d4-3974-9036-3c3bab32f408 | -1.72537 | -52.72602 | 2024-11-23 05:10:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| a1c1fbd7-bfae-3858-8377-e65e4c1ca791 | -1.39221 | -55.20148 | 2024-11-23 05:10:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f0ab54fe-9840-390f-b25f-bc9c1cd5f3d9 | -1.27222 | -52.07141 | 2024-11-23 05:10:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 5ce5469d-ec2f-3f68-a313-6d0cd2d452dd | -2.75408 | -54.10883 | 2024-11-23 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c98572a6-cce5-379a-8fbb-0493ae34b274 | -2.99335 | -52.51506 | 2024-11-23 05:10:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 69d4955a-b36c-32bd-a6df-271eeb3c40b4 | -1.62122 | -53.31671 | 2024-11-23 05:10:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 421a948a-c423-35a3-a7e5-e0e25988a763 | -1.24859 | -51.78595 | 2024-11-23 05:10:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a5da97a4-7fa5-3bfe-aa77-5aca8d7f51dc | -2.15743 | -50.49723 | 2024-11-23 05:10:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 03a25da2-4ebf-3fee-be61-bd668c96cabd | -1.28338 | -54.54638 | 2024-11-23 05:10:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 79239d1d-e0a4-3f04-8540-302d9a621b57 | -1.22788 | -51.73638 | 2024-11-23 05:10:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 306d8bd3-6876-34d3-9b39-35e245cf642f | -1.30526 | -52.2788 | 2024-11-23 05:10:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| c4e59718-1132-39a8-ac7b-7aec7fa65cce | 1.33804 | -56.12982 | 2024-11-23 05:10:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| eff8639c-6263-324e-b6ff-c5990f9d24c9 | -1.51352 | -55.16583 | 2024-11-23 05:10:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b8cb934e-f84c-3337-ab13-e202c6331135 | -2.5992 | -54.05427 | 2024-11-23 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| c4a67752-686a-332a-a820-eb9ef452dece | 1.81583 | -60.69574 | 2024-11-23 05:10:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fb9d311f-d526-376c-be32-74e7ec6f89bd | -1.24221 | -51.61431 | 2024-11-23 05:10:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cd7e72d8-ab31-3f98-a111-fbff09e75d9d | -2.78413 | -52.86945 | 2024-11-23 05:10:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ec71b82b-bf5f-37c5-ade5-b326c0c9d2e3 | -2.89417 | -53.04294 | 2024-11-23 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 30f1e99b-3c91-3751-9f0f-5a590d777fd6 | -0.26432 | -51.55027 | 2024-11-23 05:10:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 760f3e28-bc64-3615-acef-3d7ab3d43b37 | -1.81678 | -55.29253 | 2024-11-23 05:10:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 57cf4960-4008-355c-8ace-241a549b7c56 | -1.44379 | -53.39457 | 2024-11-23 05:10:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0b3c0386-4016-346b-9c03-4bf249eedc3e | -1.64327 | -52.62803 | 2024-11-23 05:10:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 94691dd2-e9c3-3f23-a56a-2bcad980c601 | -2.21989 | -51.84187 | 2024-11-23 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 931ef17d-4d22-3169-af7a-dd65799ad392 | -1.13511 | -53.40158 | 2024-11-23 05:10:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 7ba655fa-a703-3d82-a5b7-203684ed0025 | -2.74624 | -54.01835 | 2024-11-23 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a16fcd46-fd81-303d-98dc-ac2714afda98 | -1.62037 | -52.60122 | 2024-11-23 05:10:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 0d5d59e4-76fb-30a2-9d38-e3c88812f9b3 | 0.85921 | -54.65259 | 2024-11-23 05:10:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c74d2f8a-1e01-3c05-823d-08b14e1323a3 | -1.26425 | -51.76269 | 2024-11-23 05:10:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 14.0 |
| de5d5833-1fb2-39d5-8fa3-d755bee25d82 | -1.62994 | -52.69069 | 2024-11-23 05:10:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9fdf1f6b-6b3b-380a-b3b8-fda37345c908 | -1.6517 | -52.03928 | 2024-11-23 05:10:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3e525f4b-5c7d-3f12-a12e-bdc1036999e8 | -1.0466 | -51.74124 | 2024-11-23 05:10:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 6.4 |
| a2f41e39-e825-3558-a2c1-3fb4868a80e3 | -2.08983 | -50.72645 | 2024-11-23 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c1359f92-e59a-34c0-80ae-e73070117e10 | -1.134 | -54.17628 | 2024-11-23 05:10:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 62ec51ef-27ed-3aff-b9c1-904dad0b0dbe | -2.23486 | -53.66479 | 2024-11-23 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3f09ac22-4f20-3164-bc25-cb2a9680740d | -3.00551 | -51.54858 | 2024-11-23 05:10:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 003519b4-51e9-321f-bf38-a0aa21306b65 | -1.62768 | -53.31509 | 2024-11-23 05:10:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a174acb4-46fd-3050-b246-4fb88054a591 | -1.03913 | -53.17612 | 2024-11-23 05:10:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 3f5c7b6f-b1f8-3ce6-9b4a-448ae805d915 | -1.73796 | -52.71877 | 2024-11-23 05:10:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 15.3 |
| dee406bf-2314-31a9-974f-2670e0eb3516 | -1.73558 | -52.70918 | 2024-11-23 05:10:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 31576ad4-b69b-3ff2-8e2d-cc9dd736d046 | -1.22739 | -51.79293 | 2024-11-23 05:10:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 67e0bce3-ca01-3ae6-b788-d2310e965c30 | -1.21539 | -51.74316 | 2024-11-23 05:10:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| cb384cba-635f-36b4-9c0b-666f615b059a | -1.61921 | -52.60369 | 2024-11-23 05:10:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 248ff076-cdb3-31a9-b00c-64db08aec7e9 | -1.78917 | -53.64265 | 2024-11-23 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 76c285d4-f86e-35b9-91f7-53be8e6ac48e | -1.14345 | -51.68541 | 2024-11-23 05:10:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| bab426f0-9ab0-3003-af06-ab1757ec27cc | -1.31076 | -51.74927 | 2024-11-23 05:10:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f3216e97-8944-3f08-96cd-16013097b93d | -2.56506 | -48.16369 | 2024-11-23 05:10:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1c0c20ca-15de-3221-b9c8-895c4a8a0ff0 | -2.91753 | -53.06496 | 2024-11-23 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 04d74f0e-7cb9-3c78-b810-74a9545efbbf | -1.63405 | -52.61265 | 2024-11-23 05:10:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 13699b43-68ec-3c81-93e1-b412dd478a5f | -1.67903 | -53.20506 | 2024-11-23 05:10:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 69be2f36-e22f-35be-98ae-4895fd505a0b | -1.26108 | -51.75701 | 2024-11-23 05:10:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 70425e17-4417-39a1-bf87-158d114401ee | -1.25791 | -51.75136 | 2024-11-23 05:10:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8351b618-c74c-34e1-8e00-e0ca81042f89 | -2.58566 | -51.92251 | 2024-11-23 05:10:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 38ce34c4-1779-38dd-a4e6-08e973ebd2e0 | -1.54033 | -54.58819 | 2024-11-23 05:10:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d7189943-3a25-34f1-9da6-3f62137cf1c9 | -2.582 | -53.97886 | 2024-11-23 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7c0f8b28-b1a4-369f-8133-342db967e60d | -1.52645 | -51.62698 | 2024-11-23 05:10:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| a0f6a09e-f046-3674-ac8f-577f8a678450 | -1.3476 | -54.63173 | 2024-11-23 05:10:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 056d8cb4-70dd-3c74-9107-fac0cbda553c | -2.30711 | -53.60034 | 2024-11-23 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0b97cd70-4cc8-3385-83bf-eed82129fa94 | -1.0972 | -53.19234 | 2024-11-23 05:10:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 984339fb-5f5f-3868-b25a-af3528b372b5 | -1.27425 | -52.06923 | 2024-11-23 05:10:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9ba59be6-35fb-3bfe-ac95-715c4c9a724a | -1.4235 | -51.61827 | 2024-11-23 05:10:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 09b11c8e-82ab-3963-990a-650deee3bead | -1.19393 | -51.93482 | 2024-11-23 05:10:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d1570e2a-8496-34b4-881f-2c3ade2a44e4 | -2.69874 | -51.86644 | 2024-11-23 05:10:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0be8e21a-5f98-38dd-b8bc-5fcff687e260 | -1.7535 | -52.39018 | 2024-11-23 05:10:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 14fd2ed8-c555-317b-ab0d-41a8079e79ee | -1.78978 | -53.6386 | 2024-11-23 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d05676e2-9130-3aee-9751-a51ff8a65f81 | 0.69483 | -51.99655 | 2024-11-23 05:10:00 | NOAA-21 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4945da48-2ebb-3642-af61-d023142429a3 | -2.55786 | -53.97102 | 2024-11-23 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 941be0dd-8305-316e-8f69-1cffada3f7ce | -1.18183 | -51.95629 | 2024-11-23 05:10:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| fc3eb7ab-a900-3722-a066-d74b72f33d3c | -3.15632 | -45.19831 | 2024-11-23 05:10:00 | NOAA-21 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 865b6a09-6960-3e75-8a37-6f48c5dfec7a | -1.79569 | -53.64779 | 2024-11-23 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 740e1d9f-874e-37ac-ba6c-0d9f402f09b4 | -1.21058 | -51.74401 | 2024-11-23 05:10:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| d8e21141-b83a-3a8d-990c-50ae7d2fd15c | -2.89264 | -51.71917 | 2024-11-23 05:10:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| aa4a5fbc-6741-331d-9ae7-e729f29b5cfd | -0.94224 | -52.41959 | 2024-11-23 05:10:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c9e91616-de5a-3620-91a0-8e67f2aad9f9 | -2.76964 | -54.0546 | 2024-11-23 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 22ca3f23-4872-3819-805b-a203cd2ec617 | -0.76827 | -51.7738 | 2024-11-23 05:10:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 87fb6975-9251-3f9d-a7fb-ecc65742be80 | 1.40172 | -55.90533 | 2024-11-23 05:10:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 088fae73-2bbb-3396-beae-85421aba5124 | -2.80212 | -48.56689 | 2024-11-23 05:10:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6494457a-8f68-3041-a2ee-df3c97732a4f | -1.33574 | -51.40442 | 2024-11-23 05:10:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8266ade0-5ae5-37f6-9e2a-28474c3ea0fc | -2.74542 | -54.07114 | 2024-11-23 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b0e4d11b-7bad-37e4-8be6-3a71555b8fc9 | -1.40305 | -54.4768 | 2024-11-23 05:10:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 690d3166-5e8a-3023-809b-316f5e89d015 | -3.67554 | -47.13684 | 2024-11-23 05:10:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 719c23b0-5afb-3967-808f-2ea8b37c37ac | -2.55045 | -54.04273 | 2024-11-23 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7775c84b-9574-390b-aa14-28d99922a13e | -1.25329 | -51.78155 | 2024-11-23 05:10:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 91bc1988-f475-3f69-a7e7-6eb4785c6fa6 | -1.67681 | -54.99291 | 2024-11-23 05:10:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7cb78e3d-3705-38d8-b301-066ba5c82a0c | -2.70699 | -46.27604 | 2024-11-23 05:10:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 9fe27aa3-5f9c-323e-b140-404d6a5d0d35 | -1.66295 | -52.7004 | 2024-11-23 05:10:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 1d268f30-d807-38a7-8805-ac493073deed | -1.27071 | -52.69952 | 2024-11-23 05:10:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a41b5fef-b6af-31c4-8fec-b0c208eeefc7 | -1.39891 | -54.50351 | 2024-11-23 05:10:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 53d19251-afd0-32ae-8f8a-b0f9abe9bc62 | -1.26347 | -51.76772 | 2024-11-23 05:10:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| fa31f901-e91b-326b-aeaf-7c5fe5763dd8 | -1.551 | -54.33779 | 2024-11-23 05:10:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 90dd398f-9115-3929-a6b0-3ed4a304987e | -2.06778 | -53.23377 | 2024-11-23 05:10:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| bb7fc287-29d6-3774-926b-ebb6d201ce56 | -2.76014 | -54.06937 | 2024-11-23 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 898ef07d-c07a-36d4-8092-cd4d6979c392 | -1.39386 | -55.19085 | 2024-11-23 05:10:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3ca5aa61-b219-388d-a75c-28ce28f091c1 | -1.80232 | -52.29324 | 2024-11-23 05:10:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5bd34205-3e80-3917-8c23-92b3188d0d04 | -1.7827 | -53.64298 | 2024-11-23 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9922aea0-53a6-3147-aeb1-e509844d331e | -0.36256 | -51.41219 | 2024-11-23 05:10:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README54.md)
