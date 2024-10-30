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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7f834181-c392-3a78-a81d-7d6a44cfeaf9 | -2.8197 | -51.942402 | 2024-10-30 00:52:18 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 03261918-b556-36e3-a6fc-3c358b15325a | -2.8214 | -51.9496 | 2024-10-30 00:52:18 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fea778d0-0621-344c-9c9c-75a6bfe88e1f | -2.7572 | -51.712601 | 2024-10-30 00:52:18 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1a706e7a-ff4a-3e3f-85d4-f06305e98fcb | -2.7589 | -51.719898 | 2024-10-30 00:52:18 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9c5aabe2-e29f-316f-a786-e1af3abd0ce5 | -2.14 | -49.057201 | 2024-10-30 00:52:18 | METOP-B | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 09a8795d-761f-33bb-97eb-f60c8c3ee039 | -2.7474 | -51.714802 | 2024-10-30 00:52:18 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8d2c184f-31d0-313a-8b2d-7162150d9b55 | -2.8001 | -51.9468 | 2024-10-30 00:52:18 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 20c14330-02cd-35ef-8b23-1af889cfad00 | -2.9343 | -52.584 | 2024-10-30 00:52:18 | METOP-B | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 57d5f57e-fcb2-36f6-9d71-2a3879d16a9c | -2.923 | -52.5793 | 2024-10-30 00:52:18 | METOP-B | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 46472d67-aacd-34d3-8c8c-8cf733bcc1ec | -2.9245 | -52.586201 | 2024-10-30 00:52:18 | METOP-B | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f9a23c79-7129-368d-98ca-852b28e4f50e | -2.9261 | -52.593201 | 2024-10-30 00:52:18 | METOP-B | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5a94289a-2c85-3f79-8ae1-3651528e6226 | -3.0721 | -53.239101 | 2024-10-30 00:52:18 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 06f387b6-fe71-36a7-bf7b-b40ec92b9784 | -3.0737 | -53.245899 | 2024-10-30 00:52:18 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1e9528fa-1250-394b-afcf-eacb7ae60579 | -2.8 | -52.082199 | 2024-10-30 00:52:18 | METOP-B | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7768537e-3c22-39ca-8b9f-7f36362c1e91 | -2.3743 | -50.3041 | 2024-10-30 00:52:19 | METOP-B | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 08482d58-a2d4-328c-8f6d-7759b80671dc | -2.3762 | -50.312599 | 2024-10-30 00:52:19 | METOP-B | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 07b1733e-f131-3ff7-bcd4-a035272e82ed | -2.3781 | -50.320999 | 2024-10-30 00:52:19 | METOP-B | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e2696baf-e2a5-3c88-9708-f407f3ac29e7 | -3.1147 | -53.7019 | 2024-10-30 00:52:19 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8b889194-08f6-3c3b-96fc-8a569eceba72 | -3.1163 | -53.708698 | 2024-10-30 00:52:19 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fa98ffb2-403e-3254-9766-f23d97eb0081 | -2.6558 | -51.719898 | 2024-10-30 00:52:19 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f3e2ddd9-83aa-3647-96ab-75a25c083408 | -2.6575 | -51.7272 | 2024-10-30 00:52:19 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8bf2a9de-d556-39d9-8c35-e6b15be033a1 | -2.6591 | -51.734501 | 2024-10-30 00:52:19 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2202e09a-d551-3bd4-9310-010eba9a41cf | -2.6608 | -51.741798 | 2024-10-30 00:52:19 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a992988f-9945-3eb6-8040-4c90b846e919 | -2.6624 | -51.7491 | 2024-10-30 00:52:19 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 15e34dd5-32db-30b7-b173-760e4e0f4f27 | -3.1151 | -53.794899 | 2024-10-30 00:52:20 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bd97dc8d-af2b-3133-af92-e70a842d4b8a | -3.1166 | -53.801701 | 2024-10-30 00:52:20 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8536e631-e93f-371d-9002-2ada2c33134f | -3.0192 | -53.415501 | 2024-10-30 00:52:20 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b303d84d-7715-3e47-b68a-70ce1af7a89b | -3.0207 | -53.422298 | 2024-10-30 00:52:20 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2b5731b2-4558-3e99-9416-391360067dfb | -3.0223 | -53.4291 | 2024-10-30 00:52:20 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bcc11b3c-b540-3db9-8c6a-bd6c1663a889 | -3.0094 | -53.417702 | 2024-10-30 00:52:20 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 24259200-a68a-3124-88ab-cd0f0b58bba3 | -3.0109 | -53.4245 | 2024-10-30 00:52:20 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| edce275c-53c7-364a-bc03-286763f50f90 | -3.1352 | -54.250702 | 2024-10-30 00:52:21 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0eebb14d-8854-30a2-ab67-c27e7b0c8318 | -3.1367 | -54.257599 | 2024-10-30 00:52:21 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4b5be689-caf4-3247-83d6-e36f5d785f6f | -3.1383 | -54.2645 | 2024-10-30 00:52:21 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5bc73f70-acbb-3f4d-aad1-7f81ebf590b8 | -3.1269 | -54.2598 | 2024-10-30 00:52:21 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2280d3b1-72e4-37ee-97db-fe803d611d92 | -3.1285 | -54.266701 | 2024-10-30 00:52:21 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b861b00b-e758-3c5f-8f91-3bab2c551040 | -3.13 | -54.273602 | 2024-10-30 00:52:21 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3f43c86a-5caa-3770-a74b-9f85e1ccb926 | -3.0924 | -54.152 | 2024-10-30 00:52:21 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 49979fe8-70b8-325c-a45b-80367252bd57 | -3.0939 | -54.158798 | 2024-10-30 00:52:21 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ec5a0b09-896f-3b22-9d7d-4a62c53eadf8 | -3.1171 | -54.262001 | 2024-10-30 00:52:21 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6aa3ffeb-96a7-3647-8047-1c292d7f84ab | -3.1187 | -54.268902 | 2024-10-30 00:52:21 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e705366d-3af8-37e4-a55c-2db6b8bc8052 | -3.1202 | -54.275799 | 2024-10-30 00:52:21 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e49adedb-5682-3d16-ab53-bb9195dc285b | -3.0826 | -54.154099 | 2024-10-30 00:52:21 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 446c1a87-19c7-3161-b801-807f9970454c | -3.0841 | -54.160999 | 2024-10-30 00:52:21 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 322d1824-e462-3b99-9125-2ad7331eee64 | -3.1089 | -54.271099 | 2024-10-30 00:52:21 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2561d966-ddc1-35d5-8c97-10f113c6d0ee | -3.1104 | -54.278 | 2024-10-30 00:52:21 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8cf8001e-2eee-3e89-bf0e-d63c892e40d8 | -2.8867 | -53.330399 | 2024-10-30 00:52:22 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 64ebb02a-fb30-32f7-97bf-dba3e2f64d1e | -2.8754 | -53.325802 | 2024-10-30 00:52:22 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a7767d87-5482-3d28-ac39-918f7973b030 | -2.8769 | -53.3326 | 2024-10-30 00:52:22 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5aca2bd7-9d19-32cc-ac16-27ee50eb0248 | -2.8784 | -53.3395 | 2024-10-30 00:52:22 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 502a8272-73d2-3572-8f2a-3c2fe699eae9 | -2.8624 | -53.3144 | 2024-10-30 00:52:22 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 69987d30-d856-3c62-9dbd-5c550c994137 | -2.8655 | -53.327999 | 2024-10-30 00:52:22 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3464597a-6910-333f-bac1-faec676812a2 | -2.867 | -53.334801 | 2024-10-30 00:52:22 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2b2d697c-f08b-3d61-9f41-be3d9ab9a2b5 | -2.9838 | -53.852699 | 2024-10-30 00:52:22 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 16c1f929-83b6-3244-a9c5-5345ab98acac | -2.22 | -50.575401 | 2024-10-30 00:52:22 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1f9e436e-8a68-325a-8ec9-7b83a7f46cf6 | -2.2083 | -50.569401 | 2024-10-30 00:52:22 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 13bad364-ee80-3336-91a0-4c8e4cd0d383 | -2.2102 | -50.577599 | 2024-10-30 00:52:22 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b89cbd83-7738-347a-b129-e5f95e99a7ba | -2.212 | -50.5858 | 2024-10-30 00:52:22 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1c588bbe-a2d2-3ec7-89a7-a34921ff70e2 | -2.1785 | -50.619202 | 2024-10-30 00:52:23 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 44d9cec8-dbe7-377b-bfbf-4d259c52d14f | -1.6885 | -48.792599 | 2024-10-30 00:52:24 | METOP-B | ABAETETUBA | PARÁ | Brasil | 1500107 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9ac009f0-eb1b-375f-bf37-c826ae44691a | -2.5974 | -53.9669 | 2024-10-30 00:52:29 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 766109b8-d751-3e4b-adeb-c1f465a7fa85 | -2.5989 | -53.973701 | 2024-10-30 00:52:29 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 176ed5dc-84e8-3ee4-b83b-ea7821a9fad3 | -2.5824 | -53.991699 | 2024-10-30 00:52:29 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f988122f-0d86-3a3a-837c-9d74b6e64127 | -2.5839 | -53.998501 | 2024-10-30 00:52:29 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 660c2741-96af-3c97-9f0f-3611c09cd391 | -2.5855 | -54.005402 | 2024-10-30 00:52:29 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6df1f5ed-0683-31d5-b41f-42a5b4234d65 | -2.5726 | -53.9939 | 2024-10-30 00:52:29 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a1f69542-37f1-36c7-a2f4-f0b09aea5b37 | -2.5741 | -54.000702 | 2024-10-30 00:52:29 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b2f3d574-a7d0-3318-9435-84f7b1668ce0 | -1.0692 | -47.6152 | 2024-10-30 00:52:30 | METOP-B | IGARAPÉ-AÇU | PARÁ | Brasil | 1503200 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d10a072b-b331-325d-b6fe-966e2e4a58eb | -1.0722 | -47.627998 | 2024-10-30 00:52:30 | METOP-B | IGARAPÉ-AÇU | PARÁ | Brasil | 1503200 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4c8e7aa7-f0df-3959-84aa-6d764bb55b43 | -1.0595 | -47.617401 | 2024-10-30 00:52:30 | METOP-B | IGARAPÉ-AÇU | PARÁ | Brasil | 1503200 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e3b2d34a-60df-3df5-a47b-7e20493d2b8c | -1.0624 | -47.630199 | 2024-10-30 00:52:30 | METOP-B | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f77c33ff-d30b-3bcd-8935-b3bb610f0d19 | -2.3035 | -53.760101 | 2024-10-30 00:52:33 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cfdeb18c-2249-3d9d-accf-56fddd290b89 | -2.3051 | -53.766899 | 2024-10-30 00:52:33 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a05980f3-0315-3c71-873b-6f8b29959c4e | -2.2602 | -53.705399 | 2024-10-30 00:52:33 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2d2660f8-2d6e-3199-b24e-82e7969b62f6 | -2.2618 | -53.7122 | 2024-10-30 00:52:33 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c2828031-3753-3725-bab8-54db4bc385a5 | -2.2633 | -53.719002 | 2024-10-30 00:52:33 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7a351d6d-19ca-3054-ab87-f474963752ee | -2.2081 | -53.702702 | 2024-10-30 00:52:34 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| de6e81fa-2a48-3efd-a7f6-22e4cfdf68f4 | -2.186 | -53.650398 | 2024-10-30 00:52:34 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6a9aebae-1717-3477-a44e-96310801d356 | -2.1875 | -53.6572 | 2024-10-30 00:52:34 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 00ba74ce-8324-3bfa-b5d4-cc4cf37a007a | -2.189 | -53.664001 | 2024-10-30 00:52:34 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1e712829-16f4-3f89-9283-96f88b2e2a76 | -2.1762 | -53.652599 | 2024-10-30 00:52:34 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5d8d6552-fae8-3d4d-8b19-c14c613047f4 | -2.1777 | -53.659401 | 2024-10-30 00:52:34 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b917bdbe-d69f-3d4d-9196-98503f75af9c | -2.3605 | -54.836899 | 2024-10-30 00:52:36 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e2138f26-0f9d-3c7d-98d5-2b1ec495d29a | -1.7765 | -52.295601 | 2024-10-30 00:52:36 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7b36eaec-e49a-36e0-affb-183cd9f07101 | -1.7782 | -52.3027 | 2024-10-30 00:52:36 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 21773973-8f90-344a-b18c-5865d02ce1b4 | -1.765 | -52.335602 | 2024-10-30 00:52:36 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 93388d9a-3691-3bad-a53a-bd4f45b845e9 | -1.7536 | -52.3307 | 2024-10-30 00:52:36 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 420a2f19-74e4-362c-88eb-c3f63d133dae | -1.7552 | -52.337799 | 2024-10-30 00:52:36 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 14b50e46-1153-3297-b68c-aba7d1385551 | -2.9207 | -57.6651 | 2024-10-30 00:52:37 | METOP-B | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a6c1f957-9f0a-3123-9187-c060315d497b | -1.7104 | -52.504101 | 2024-10-30 00:52:38 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 50d6dd68-1384-3f84-8e37-e298aba3c53d | -2.8459 | -57.652302 | 2024-10-30 00:52:38 | METOP-B | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| de6c5d8f-e044-3b02-addb-e6d19f816208 | -1.5706 | -52.023701 | 2024-10-30 00:52:38 | METOP-B | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 36e37447-84f2-3caa-9d57-670e858bcff8 | -2.6639 | -56.927101 | 2024-10-30 00:52:38 | METOP-B | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 87d20b72-8f4c-3a1f-9f7a-95adf4997f5a | -1.5561 | -52.095699 | 2024-10-30 00:52:39 | METOP-B | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ea3896a9-98d1-37ce-9426-b09881e8fa6c | -1.5577 | -52.102901 | 2024-10-30 00:52:39 | METOP-B | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 445589ba-64f2-33c1-9fa8-52e53f04d374 | -1.5593 | -52.1101 | 2024-10-30 00:52:39 | METOP-B | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ed841b00-91a4-31e8-8d45-e3c8f96751f1 | -1.561 | -52.117401 | 2024-10-30 00:52:39 | METOP-B | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 23607196-07dd-3888-80f9-ce3e9452b74a | -1.5626 | -52.124599 | 2024-10-30 00:52:39 | METOP-B | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 626a0076-edee-396f-8ef7-738ef31b39b9 | -1.4322 | -51.595001 | 2024-10-30 00:52:39 | METOP-B | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f5edd6c3-835a-3234-b959-170a0e18389b | -1.543 | -52.083302 | 2024-10-30 00:52:39 | METOP-B | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README17.md)
