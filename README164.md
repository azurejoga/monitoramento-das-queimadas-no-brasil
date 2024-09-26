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

## Dados Diários - Página 164

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 19175db3-e83d-3048-881b-ce661ecb7417 | -11.94384 | -65.01947 | 2024-09-26 05:48:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bc873362-15a4-3435-965f-2c2eea1214e0 | -11.94213 | -64.98112 | 2024-09-26 05:48:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 897071a3-15de-395d-80e3-2bff39c8da61 | -11.94026 | -65.01893 | 2024-09-26 05:48:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 30e5c677-c93f-341a-98a8-dc64909e352b | -11.92844 | -64.94942 | 2024-09-26 05:48:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a71bc19c-3831-39e3-8e2d-6c3c07ba4dba | -11.28554 | -64.95322 | 2024-09-26 05:48:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 493e6590-9085-3512-b028-3ae71985811b | -11.28138 | -64.95681 | 2024-09-26 05:48:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5656182e-b873-333f-ae77-2ad76ba51725 | -11.2727 | -65.26019 | 2024-09-26 05:48:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2f7cefc8-2af3-35b8-b6f7-694e91c0fb4d | -11.26917 | -65.28388 | 2024-09-26 05:48:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 14.6 |
| 12c6190d-ec1a-3ad1-b21f-b7697d6397cb | -11.26858 | -65.28785 | 2024-09-26 05:48:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 4.6 |
| c85fd1c7-aa39-39c3-886f-71a1c8a66853 | -11.26799 | -65.29182 | 2024-09-26 05:48:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 4f7f7f4e-4a5c-3445-b721-ab3c437d8ed8 | -11.26566 | -65.28335 | 2024-09-26 05:48:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 14.6 |
| 1d9e80ba-1555-34ce-98c3-12a46157f2ce | -11.26507 | -65.28732 | 2024-09-26 05:48:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 4.6 |
| a2489970-4c40-36ff-9723-573c89260438 | -11.26448 | -65.29128 | 2024-09-26 05:48:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 4.6 |
| b5ce8aa4-440a-3c97-a4c8-717f9a2cd7ca | -11.26389 | -65.29525 | 2024-09-26 05:48:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 329e2874-6147-383a-a722-f44b859c1ff6 | -11.26215 | -65.28283 | 2024-09-26 05:48:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e3fbd0bc-5ec7-344b-909c-580020d5fc3f | -11.26157 | -65.28677 | 2024-09-26 05:48:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 14.6 |
| 544403d3-58aa-34f2-b55d-fdf0fc05a2a4 | -11.26098 | -65.29074 | 2024-09-26 05:48:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 14.6 |
| 95d98ae4-6f44-339a-8e5a-77ed8ceae43a | -11.26038 | -65.29471 | 2024-09-26 05:48:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 0a3129d2-76ca-3406-a2d5-62d15c3db90a | -11.25864 | -65.28232 | 2024-09-26 05:48:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 836fe6ea-fead-32a2-94f2-89e86bcf1dd0 | -11.25806 | -65.28625 | 2024-09-26 05:48:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 14.6 |
| c7f69ea9-b587-37e5-91f0-8924e65cbefc | -11.25747 | -65.29021 | 2024-09-26 05:48:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 14.6 |
| 739cb346-fad0-35cf-83ec-e0e9701f8abb | -11.25688 | -65.29417 | 2024-09-26 05:48:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 632e1bd4-86c2-395e-a4d6-61184c977cd6 | -11.25396 | -65.28969 | 2024-09-26 05:48:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 4f3c0ff1-cac1-3c7e-83ae-ae74c1f886c4 | -11.25338 | -65.29364 | 2024-09-26 05:48:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d8f19314-8949-375f-a355-7c42e7373349 | -11.24987 | -65.29312 | 2024-09-26 05:48:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 74e863f0-ea7d-3294-a05f-ac1f27ad8b37 | -11.20311 | -65.26987 | 2024-09-26 05:48:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d6873cab-4a77-37b0-a1fb-ccc090454cc3 | -11.19902 | -65.2733 | 2024-09-26 05:48:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d74418f1-f5d3-3294-a1c7-1f89d1637b73 | -11.19854 | -65.27046 | 2024-09-26 05:48:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 417ba71e-0e5f-37c6-8ff8-060edd946573 | -11.19437 | -65.28065 | 2024-09-26 05:48:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8a587f6a-9beb-3714-a504-6208a9853114 | -11.1255 | -65.30376 | 2024-09-26 05:48:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3726e6d1-375f-3f3f-8633-c838603e09c9 | -11.08155 | -65.18476 | 2024-09-26 05:48:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3167b64d-0ad0-3d5b-98f2-a0166ed3bbea | -11.07863 | -65.18026 | 2024-09-26 05:48:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c04b9c88-a217-3d3a-a8b5-3f33d8c2d992 | -11.07804 | -65.18423 | 2024-09-26 05:48:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f8de143a-89ac-3b6e-977a-5cc453c6c155 | -11.65257 | -65.18301 | 2024-09-26 05:48:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e043c387-14db-30e9-a44b-f2e3f5af327c | -11.65243 | -65.03848 | 2024-09-26 05:48:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e5656abd-e3f5-3ac6-af8a-83d5cf1c31b9 | -11.64826 | -65.04203 | 2024-09-26 05:48:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1864b512-7a0b-3207-8f06-dfc8fa01c688 | -11.63053 | -65.01431 | 2024-09-26 05:48:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 392b489e-c00e-3d06-8d6a-60b2e2383422 | -11.62696 | -65.01378 | 2024-09-26 05:48:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 46fac0d1-2fc7-31c3-8ee5-bdafd8a2e956 | -11.62636 | -65.01789 | 2024-09-26 05:48:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0f17c349-554c-3788-b1de-7ddecbe72b82 | -11.6234 | -65.01325 | 2024-09-26 05:48:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 447ae050-12b3-3262-92b5-c5033d954625 | -11.62279 | -65.01736 | 2024-09-26 05:48:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2cb5011a-87b1-36c0-bd0b-a2679eb03f44 | -11.62219 | -65.02146 | 2024-09-26 05:48:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3aa36a22-bf3f-3dab-97d2-d199186c4284 | -11.61923 | -65.01684 | 2024-09-26 05:48:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2b14544f-e8fd-3888-9699-5f6c6a9c633b | -11.6171 | -65.17847 | 2024-09-26 05:48:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ea820835-5c3e-3a93-b7d1-cc47350096dd | -11.61566 | -65.0163 | 2024-09-26 05:48:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6af455b7-0f7f-3b41-ae38-f05ac4d1943e | -11.61506 | -65.02043 | 2024-09-26 05:48:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b422916e-2192-3e4e-a035-7bec522db87d | -11.61357 | -65.17793 | 2024-09-26 05:48:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8d8a0f3d-22af-31d8-904c-0da60499687f | -11.6115 | -65.0199 | 2024-09-26 05:48:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9bb66b52-6b97-3b37-a17c-6841ab901455 | -11.60824 | -65.1895 | 2024-09-26 05:48:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3ce4d72b-df96-36ed-8402-df2c5e27a0dd | -11.60764 | -65.19353 | 2024-09-26 05:48:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d35ce03c-7283-36af-aed2-992264f62f38 | -11.6008 | -65.04327 | 2024-09-26 05:48:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d8e30f43-9109-3e6f-8123-0f473aacf0cb | -11.59783 | -65.03868 | 2024-09-26 05:48:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6fd2b9ae-b83e-3df3-ab2d-3df7548f401a | -11.59487 | -65.03407 | 2024-09-26 05:48:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ecb734bb-6d1b-319d-9368-2f17cdce1823 | -11.59132 | -65.03351 | 2024-09-26 05:48:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7190db1f-595e-3725-86f9-eca1009c0cfc | -11.58716 | -65.03704 | 2024-09-26 05:48:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 850a0bf0-f6b7-3dd4-a401-df72a34def93 | -11.57115 | -65.04723 | 2024-09-26 05:48:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e0cec192-55ed-3115-82c7-ad8e146b0aee | -11.57056 | -65.05128 | 2024-09-26 05:48:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 84b72d9d-3ba8-392f-b3d0-735782406727 | -11.56345 | -65.05022 | 2024-09-26 05:48:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 01ed157e-77e8-37c1-88cf-60515451eb77 | -11.5593 | -65.05376 | 2024-09-26 05:48:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6a2a542a-c299-35fc-9bb6-496514221b44 | -11.55213 | -65.05813 | 2024-09-26 05:48:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| acdefee8-bb26-344e-9048-dcaebe7ca544 | -11.54797 | -65.06166 | 2024-09-26 05:48:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| df926922-7595-3ad7-b9da-69ffcbdf0e77 | -11.5432 | -65.06927 | 2024-09-26 05:48:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1e0b57d0-9658-3ce0-af86-d35e7a585a93 | -11.53905 | -65.07278 | 2024-09-26 05:48:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cb279aeb-e259-3577-9077-efdaf0d051fa | -11.53368 | -65.08443 | 2024-09-26 05:48:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 500fa349-c2c7-34d1-8fe9-0acb4f528d34 | -11.53308 | -65.08849 | 2024-09-26 05:48:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 4fe96ea2-b05c-3e3c-8931-835929f78a71 | -11.53187 | -65.0966 | 2024-09-26 05:48:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bf81c338-c15d-364c-93c4-7b825a64fb2f | -11.53014 | -65.08389 | 2024-09-26 05:48:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 77d6c5c5-7dc7-3872-8338-db581c9d3a99 | -11.52953 | -65.08795 | 2024-09-26 05:48:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d7083dce-4ba4-370b-a392-1a12c51971a5 | -11.52893 | -65.09202 | 2024-09-26 05:48:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1f89c616-1172-3f27-86af-00f0ab017727 | -10.51354 | -69.41562 | 2024-09-26 05:48:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 21092852-f63c-3be2-a7c8-6b3446486236 | -9.7433 | -62.34018 | 2024-09-26 05:48:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2f55db13-411d-338d-a65f-5c6d64a716ac | -9.73925 | -62.33953 | 2024-09-26 05:48:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 33b675d3-f950-3669-a6e8-f8d15efbdc45 | -9.51223 | -62.44606 | 2024-09-26 05:48:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 404e15bb-e1cd-3802-900f-7edf33809bfb | -9.37078 | -62.45033 | 2024-09-26 05:48:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 14e0b80e-119b-338a-a715-d08e3122680d | -9.37028 | -62.45384 | 2024-09-26 05:48:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 753427d8-97f4-3877-b6b2-a31503a39388 | -10.7087 | -62.73924 | 2024-09-26 05:48:00 | NOAA-20 | JARU | RONDÔNIA | Brasil | 1100114 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6b8b167c-0208-373d-8707-e1df39882e22 | -10.29269 | -62.88852 | 2024-09-26 05:48:00 | NOAA-20 | CACAULÂNDIA | RONDÔNIA | Brasil | 1100601 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 440fb98f-2128-35db-bd3c-4e8076820a73 | -10.29196 | -62.89365 | 2024-09-26 05:48:00 | NOAA-20 | CACAULÂNDIA | RONDÔNIA | Brasil | 1100601 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ee2ff853-7d9f-312a-b1ef-35e27cf7b3af | -10.28944 | -62.88298 | 2024-09-26 05:48:00 | NOAA-20 | CACAULÂNDIA | RONDÔNIA | Brasil | 1100601 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0ad76a3e-e440-372c-b405-6f6bf302ae89 | -10.28871 | -62.88815 | 2024-09-26 05:48:00 | NOAA-20 | CACAULÂNDIA | RONDÔNIA | Brasil | 1100601 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4828f382-bbfe-3006-ba05-d87328d8c616 | -10.28549 | -62.88242 | 2024-09-26 05:48:00 | NOAA-20 | CACAULÂNDIA | RONDÔNIA | Brasil | 1100601 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 54e90c10-04d1-3edf-85b7-060a11339b85 | -10.28477 | -62.88753 | 2024-09-26 05:48:00 | NOAA-20 | CACAULÂNDIA | RONDÔNIA | Brasil | 1100601 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f85677bb-87e5-308e-8e17-a4f7ff734cf9 | -9.37464 | -62.33553 | 2024-09-26 05:48:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 57bf27d9-4d80-38ac-938b-7a0c8902f77c | -11.04629 | -62.57625 | 2024-09-26 05:48:00 | NOAA-20 | MIRANTE DA SERRA | RONDÔNIA | Brasil | 1101302 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7d5b71a5-0dfa-3b0d-bbde-14c3e20f12f3 | -11.04618 | -62.57578 | 2024-09-26 05:48:00 | NOAA-20 | MIRANTE DA SERRA | RONDÔNIA | Brasil | 1101302 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 11bf3a93-635d-316c-8c9d-f618986004f8 | -11.04579 | -62.57974 | 2024-09-26 05:48:00 | NOAA-20 | MIRANTE DA SERRA | RONDÔNIA | Brasil | 1101302 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 17d83f8a-0602-3d2d-b677-929e775a2e93 | -11.04571 | -62.57925 | 2024-09-26 05:48:00 | NOAA-20 | MIRANTE DA SERRA | RONDÔNIA | Brasil | 1101302 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 43e19bc2-5f66-3a4f-a0e6-5916497617b3 | -8.91877 | -63.29014 | 2024-09-26 05:48:00 | NOAA-20 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f08905dd-efc5-3be8-bfab-cbeac772ed65 | -8.91499 | -63.28958 | 2024-09-26 05:48:00 | NOAA-20 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8d5431ce-6b88-3463-9a61-892f60e98fbc | -8.90437 | -63.67593 | 2024-09-26 05:48:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| beb16a39-102b-33f3-9da4-d6a4dfa03d09 | -8.83882 | -63.71115 | 2024-09-26 05:48:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 50c53cec-be5a-3084-8955-6dc5d4896476 | -8.83577 | -63.70619 | 2024-09-26 05:48:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8bddcbc9-c00f-333d-b74c-1f9d3f9b68b6 | -8.83513 | -63.71058 | 2024-09-26 05:48:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 269d9a0a-2b25-3a90-9a60-d4150b4bd707 | -8.83337 | -63.70358 | 2024-09-26 05:48:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 8ad95e88-f0c9-3c02-a1c1-071d1e60f348 | -8.83271 | -63.70795 | 2024-09-26 05:48:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 4.7 |
| f6f9e0ac-9d8d-358d-b9dc-c9549d848b86 | -8.83271 | -63.70121 | 2024-09-26 05:48:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| dd6355f0-204a-3fe6-bf00-636c19b0700b | -8.83208 | -63.70562 | 2024-09-26 05:48:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d9571b26-d46a-3e15-a709-fcd3024b6b01 | -8.83206 | -63.71233 | 2024-09-26 05:48:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 4.7 |
| bc3c56b8-0fdb-378b-9aa3-6bd4da5b977d | -8.83145 | -63.71 | 2024-09-26 05:48:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ab6d6abf-e656-3b2f-a71e-6889cc6b542d | -8.83035 | -63.6986 | 2024-09-26 05:48:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 5.3 |


[Clique aqui para ver as próximas entradas](README165.md)
