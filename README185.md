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

## Dados Diários - Página 185

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fac2d9f2-03cf-37c9-b06f-5d867868ab51 | -3.29578 | -54.67116 | 2026-10-08 05:42:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 816129a2-4bf1-3af9-a3a9-0cde41e5e406 | -2.49859 | -56.13147 | 2026-10-08 05:42:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 20a679ca-2f09-361f-974a-0b6510122713 | -2.76061 | -54.09699 | 2026-10-08 05:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 435d1be4-caa8-369d-b569-5619d3327f28 | -4.44693 | -54.97769 | 2026-10-08 05:42:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2459e985-76e3-3516-9c82-a4397417624e | -3.18232 | -50.55861 | 2026-10-08 05:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7a149b89-2c17-3bbc-a2b7-087f7d651981 | -3.51205 | -54.66236 | 2026-10-08 05:42:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 37069586-ee64-3bf8-b4fd-eb3f149d8265 | -6.16616 | -52.66535 | 2026-10-08 05:42:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b9f8b8c7-513b-3f10-88fe-825672e4ce21 | -6.48363 | -55.29636 | 2026-10-08 05:42:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b6010a22-35fc-378c-a8cd-9383d40385ec | -2.50389 | -56.12746 | 2026-10-08 05:42:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 00ccbca6-9552-3ceb-8bf0-07caa887938b | -2.99148 | -54.05936 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 07df3171-6429-333b-bc50-3e060fd5a1f9 | -3.08338 | -53.9571 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 43.2 |
| 08040e4a-8057-3be7-b286-bd26e616e23e | -5.87169 | -50.09866 | 2026-10-08 05:42:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 151346c2-b712-3ffd-8fc8-bc1d5deff28b | -2.87431 | -54.19744 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| f36c268e-4b49-31fe-be42-1a656e94e11c | -3.66628 | -60.6299 | 2026-10-08 05:42:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ea73fec8-c892-3b88-bc70-b7f70b93055a | -7.21727 | -55.10736 | 2026-10-08 05:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 371533af-42f8-38d2-89d7-894675e4967f | -3.67842 | -55.94716 | 2026-10-08 05:42:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7f0524f2-9dfd-377c-a9df-8948a8faac07 | -3.61743 | -55.28084 | 2026-10-08 05:42:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 50882933-9c77-305c-b867-84293390d4cb | -5.68732 | -53.48698 | 2026-10-08 05:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 96a85163-be47-397f-81ec-53a7d0b1c4b9 | -6.81021 | -55.29642 | 2026-10-08 05:42:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d06fbfa2-8650-3884-9156-12c84ca2e7f3 | -3.54364 | -54.67784 | 2026-10-08 05:42:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 6c8aceb5-cfc7-342c-80bd-a59bc8adbe44 | -2.98731 | -54.77337 | 2026-10-08 05:42:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 539ef5f7-9aa9-311a-be16-ab98fa14bf7f | -3.02275 | -54.10445 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e8fe0a64-b6d8-3e13-9439-24c1276e1802 | -2.75579 | -54.09299 | 2026-10-08 05:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 347552b9-30dc-32a0-853b-345e5fe6b546 | -3.43687 | -56.93578 | 2026-10-08 05:42:00 | NOAA-20 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cdbd947e-6bb8-3c97-90b3-103f774562d8 | -5.22315 | -60.2437 | 2026-10-08 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 19d47e6b-541e-337d-b840-1800ce376eee | -3.3579 | -50.48283 | 2026-10-08 05:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8be0c1f1-5a7f-3104-baf7-16feeadce8ca | -3.1022 | -54.18035 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| bf44cd35-fef5-326e-995a-9f3dc6587b86 | -3.17162 | -50.44855 | 2026-10-08 05:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| dc522e94-bfc4-3bdb-ac52-f20a203d3795 | -3.58482 | -54.68374 | 2026-10-08 05:42:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 16d5c29c-1071-3de7-8c53-8bf5bd88c430 | -3.18988 | -50.55375 | 2026-10-08 05:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 03a92e2a-d7ef-3f13-8de5-be1262237842 | -3.29485 | -54.03322 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 59caf27b-b42a-3de6-9690-cf6715da7a6f | -3.5565 | -59.47823 | 2026-10-08 05:42:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2a4aa491-0b57-3295-8e6d-8b4189277132 | -5.29478 | -60.09011 | 2026-10-08 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fb8beb2c-a3e3-3b1d-abaa-fc4b11f94943 | -4.53989 | -55.61783 | 2026-10-08 05:42:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3f42e24d-8a79-3d54-9c7e-36ddb018f5b1 | -3.01907 | -54.05677 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ca6b47d4-52da-31da-a835-0fa6544a331a | -2.84126 | -54.12958 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 55b886ff-22d7-37eb-bed7-db1c8ccd963d | -3.10294 | -54.28289 | 2026-10-08 05:42:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 74ab2f5f-7acb-3a59-9d7d-2fd9188cab38 | -3.52908 | -54.66959 | 2026-10-08 05:42:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c0871e5f-4a16-357b-b859-6f19822011f4 | -3.00635 | -54.10532 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| a38d18f3-1394-3d2e-a130-b97071013a93 | -2.7364 | -57.6145 | 2026-10-08 05:42:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 08a73e9c-d7c1-3872-a74a-bc949fc4a4c0 | -3.29994 | -54.67817 | 2026-10-08 05:42:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 94e95e22-72cd-32f3-90c0-429c65865e93 | -2.93534 | -54.15041 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9e631aa9-658d-3b52-a8cd-1d880c38351e | -4.21577 | -56.05181 | 2026-10-08 05:42:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3b6496a5-b2a7-3dca-bcac-e893cc4e80f9 | -3.29147 | -54.01891 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 67cb39ce-3d57-36f9-8de9-4809e95f4e3a | -3.49733 | -51.68842 | 2026-10-08 05:42:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| da126a05-35db-3d77-86f2-8982769a81b7 | -3.08389 | -54.26678 | 2026-10-08 05:42:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f5e671a2-7cab-3032-a85b-fa379b6f1614 | -3.09134 | -53.94107 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 9922880a-7111-319c-aecb-36bcf6ccfb86 | -3.56533 | -59.47044 | 2026-10-08 05:42:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 5ee5cf23-28ea-374f-b59a-d9a4f573362d | -3.29996 | -54.05102 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6f98f538-fe65-3895-8676-c1dec96e1bb8 | -4.36915 | -54.75695 | 2026-10-08 05:42:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 22e874d2-7706-3dae-a92f-bc8d52dcbaf8 | -2.93344 | -54.05641 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c3162d59-7b88-36d7-b081-320aeb83e54e | -3.29545 | -54.00915 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cd4fab4f-6df0-3249-8291-509e6479db21 | -3.17744 | -58.64238 | 2026-10-08 05:42:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| bec4c87a-2f81-3394-8888-939a99c1cfb1 | -2.98855 | -54.07913 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| d5cb87f7-162e-3f7d-9823-3c458a066611 | -3.03969 | -53.91951 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5337979d-2980-37cc-98ff-7eb07b3a29c5 | -3.30291 | -54.67702 | 2026-10-08 05:42:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 413196aa-6234-37ab-a06a-3658875c6829 | -2.84218 | -54.12933 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7ba0295b-918a-36dc-b2b4-6b77d3106728 | -2.77987 | -54.07664 | 2026-10-08 05:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 7fb570b1-f62c-35c0-9e4f-7055b241dda1 | -5.85747 | -53.45957 | 2026-10-08 05:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| f4c9e654-db75-3aad-bcf7-b8e9aa6a9d70 | -3.0209 | -54.08075 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| c96d4e55-b62e-3bd9-90bb-e24ab4123858 | -2.51705 | -56.25947 | 2026-10-08 05:42:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 642cc8ad-deb9-3d04-b65d-a7de7671b82d | -3.59677 | -54.56886 | 2026-10-08 05:42:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 81575ed3-c567-3c2d-9035-cc4fff8113e3 | -3.85528 | -55.9785 | 2026-10-08 05:42:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5a0210e3-fcd6-3c6b-9f1d-34ea46e49827 | -2.87967 | -54.12552 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2baa6454-4d3b-3a0c-9d93-9f4ed8b1157b | -3.27975 | -54.06192 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cc268d29-7484-3f46-93ad-81c1d90e3654 | -3.02508 | -53.90694 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4da0acdf-2c83-3f9a-8ccb-3f14725ef11a | -3.29205 | -54.06689 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8b3baf91-bb7d-30fe-a995-1575ad40faca | -3.55412 | -59.4687 | 2026-10-08 05:42:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2cf79fe4-3a47-3e99-bc56-4ceaa0509237 | -5.29543 | -60.09164 | 2026-10-08 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| eb703224-4195-3a43-a9e4-a1da7c1c9c02 | -4.3212 | -50.78679 | 2026-10-08 05:42:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 75d2595a-dec7-328d-8477-d0a74b3500be | -3.01695 | -54.10693 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 0fa6b395-2420-343d-9ce2-9af7e7710480 | -7.21771 | -55.10426 | 2026-10-08 05:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 73ab256a-e4fd-3c6f-9e0b-47552811fb08 | -3.59735 | -61.62885 | 2026-10-08 05:42:00 | NOAA-20 | ANAMÃ | AMAZONAS | Brasil | 1300086 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4a416da1-05fc-381a-9b2f-fa731eb03ea4 | -3.05043 | -53.92118 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c812b25b-1bf0-31cf-9565-459bdf6fb873 | -7.22448 | -55.1675 | 2026-10-08 05:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 186ae89e-edbc-3fc1-a8a7-29a75f0bf286 | -3.7233 | -59.69189 | 2026-10-08 05:42:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1402195d-2932-33fb-aed8-59335c49ba51 | -2.78802 | -54.09449 | 2026-10-08 05:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 53b45a62-abf3-3613-8eaa-d2e4bba6d4de | -3.11607 | -53.79071 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| ee20e994-e0d0-323b-ba8d-799df390d07c | -3.29869 | -54.66999 | 2026-10-08 05:42:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a2655795-4cc6-35a8-bd68-12c718e396ba | -3.00203 | -54.09797 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 8e4e60e4-2f19-310b-bafb-dcccc815b352 | -3.53715 | -59.49553 | 2026-10-08 05:42:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7f9df210-a1e3-3ecc-8f6c-61db9433442f | -3.52702 | -54.66771 | 2026-10-08 05:42:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ddbeaa7c-4209-3cbc-a944-88ac5c057b9e | -2.95051 | -59.16247 | 2026-10-08 05:42:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| de12ece4-0c05-3a9e-ac70-fc991b3869fc | -3.10675 | -53.77855 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e9b8e873-ce3b-3d7f-bc82-d06605ce7cd8 | -3.14806 | -53.72439 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 932349e4-4482-3b53-ba9d-007f8105e92a | -3.53754 | -59.5027 | 2026-10-08 05:42:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5113e13b-83c6-3eef-a711-a4f0f0fc0097 | -3.08717 | -53.95074 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| e2dccc71-a439-37ab-8f0e-0ee31c2cd8a7 | -3.7088 | -60.54331 | 2026-10-08 05:42:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3320e55a-8bed-3070-b8eb-2ae0cb50db00 | -3.53646 | -59.49998 | 2026-10-08 05:42:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| aea059e3-0057-360e-b8e0-50549bae460d | -3.78118 | -59.19825 | 2026-10-08 05:42:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5997124b-f1a2-3199-a916-0be0549da4a2 | -3.57538 | -54.31799 | 2026-10-08 05:42:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2f6587f9-98c5-312d-b65e-d0e63dd5aca5 | -3.67 | -54.51082 | 2026-10-08 05:42:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4b623723-be36-3b9e-8e08-5efae925d634 | -3.74813 | -59.31137 | 2026-10-08 05:42:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 694d16ef-5d44-3db1-88b1-a9af1f99b604 | -3.99839 | -56.25718 | 2026-10-08 05:42:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 464a5d40-8609-3452-8ade-d78792d5a665 | -3.17609 | -54.61477 | 2026-10-08 05:42:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ef0a7b9d-6798-38c9-ad94-cd58cd273e9a | -4.42418 | -59.49625 | 2026-10-08 05:42:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 69722e7f-c035-3058-863f-a57c45935f27 | -2.88928 | -59.20759 | 2026-10-08 05:42:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c2c0d2d1-b478-3edc-8f67-910de625fc58 | -2.99239 | -54.08979 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 7e6179a9-5048-3392-83b2-c33674852664 | -3.58058 | -54.31668 | 2026-10-08 05:42:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4071aa3e-9a72-38c1-83f4-c06798fb265f | -3.11961 | -56.66086 | 2026-10-08 05:42:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README186.md)
