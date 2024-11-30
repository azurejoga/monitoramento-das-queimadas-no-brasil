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

## Dados Diários - Página 93

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9b262466-85fd-316a-9735-2fbc53f4111b | -3.49593 | -53.84436 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b3fda3d6-17e2-3a87-a1fd-d0de9370612f | -3.05777 | -51.30083 | 2024-11-30 05:01:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 27e89966-a208-3b66-9b80-a73a7930c2e1 | -1.15535 | -51.69466 | 2024-11-30 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2f87611e-0589-3859-af99-32807c8ba348 | -2.52229 | -48.1838 | 2024-11-30 05:01:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c75b177e-9ae7-30c2-abf1-952f944db225 | -3.16344 | -53.24352 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 251e53a8-3e38-39a6-8f8f-7990890ced9a | -1.69581 | -52.43264 | 2024-11-30 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 403bdc09-4a68-3c9c-be38-258aacce1628 | -1.11623 | -53.59361 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5ce92534-f377-3174-831d-5f5d315239c1 | -3.46207 | -48.93103 | 2024-11-30 05:01:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0482a997-8cff-37d5-a22b-a494e8d2ad6f | -1.08047 | -53.63499 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 8b5e7d5d-7484-34e1-bef9-4865471c2c9b | -0.26551 | -51.61865 | 2024-11-30 05:01:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7b6582bc-7cbc-3809-907f-5cda9a81df78 | -2.17488 | -51.42006 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1e41f6c1-66fb-3aa6-9eeb-0bccaab1e239 | -2.43528 | -46.51194 | 2024-11-30 05:01:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 83bbfb3f-5dc9-3730-ba10-8b38d3a23c6f | -1.0896 | -53.35873 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 009a9b7f-3d67-32c0-91f2-b67c48817f48 | -1.69892 | -52.63762 | 2024-11-30 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f233b473-ec06-3836-b170-fec5054b09a2 | -3.06906 | -54.02466 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0718bf6a-833e-3721-9786-7abe5581c123 | -2.98126 | -53.89605 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| b60befad-c6e9-3165-a3a9-dd22ad2a9556 | -2.44511 | -53.62123 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 3d23bdcd-1a7a-3ac0-ae6b-5f5d7075d961 | -1.16409 | -51.9351 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3cc146d1-7965-397c-aea3-0e5e36e7e74a | -1.98903 | -53.29944 | 2024-11-30 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c220c346-eae1-3c00-a270-78c04c4fa786 | -2.97923 | -53.28336 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 517d4b02-f6e3-3993-919b-d1f8bf22cae4 | -3.06709 | -50.56985 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1012ba80-809f-3ba4-ac17-fac2fd31ed16 | -3.74329 | -51.8318 | 2024-11-30 05:01:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 68e7d002-d13e-3345-a8bc-1a0c8f4ddfda | -2.80247 | -53.05363 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 64308e68-1400-3840-a7d5-544d6cfb1922 | -3.40895 | -50.66047 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e008e44f-7023-3ef2-b7dc-ea5d91e64896 | -3.30937 | -51.57513 | 2024-11-30 05:01:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b0355ad0-0c37-3bfc-8a3e-b08c3c6eb8cf | -1.14601 | -53.70937 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 539a6f01-aa3c-3ebd-bf2f-897dac2df78b | -1.70387 | -52.64147 | 2024-11-30 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a961ab3d-91b2-317a-9c16-d4478ecda274 | -1.5372 | -51.61919 | 2024-11-30 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bb8122c2-a674-3929-80b8-8cce36fff026 | -3.04513 | -54.04616 | 2024-11-30 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2f3eee9f-114f-3d38-8bd8-ea32bbc1cd10 | -2.28398 | -53.74148 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5322c4b5-4608-3360-808f-f23684724a23 | -3.03805 | -51.47686 | 2024-11-30 05:01:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 52f72eb6-084b-31d8-b28b-6de19c97427e | -3.22002 | -53.42038 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 325407f3-c0f6-329f-90b7-436e26de5a44 | -2.84044 | -54.0363 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 6ed8ac12-a9ec-33a9-b9ed-4dbcc0bc3724 | -2.80565 | -48.62186 | 2024-11-30 05:01:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4d71bd64-d5bd-3674-aa2c-bb000fa76162 | -1.07005 | -53.16636 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b6bc9095-4391-3d1b-a67f-21060f2510d6 | -1.13273 | -53.39081 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4e030652-aa18-39d7-84f5-8124da05dfe1 | -0.97794 | -53.7268 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 84cbe7b4-be81-36db-9054-769ef995f636 | -3.25395 | -53.29144 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0ccdc5dc-c408-3e5f-8de3-2239733bd57b | -1.23227 | -51.79959 | 2024-11-30 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 4bdb8208-77d9-33d9-8802-2d460fda2761 | -3.28165 | -50.57743 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9877a63e-28e8-3c78-9380-32e2af28e077 | -2.74347 | -54.07518 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c8b91e5a-bbb1-3e06-a7a0-4835336d12d3 | -1.51379 | -52.03009 | 2024-11-30 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 18a53950-5704-3f06-8e04-d4bd9ebd0cc5 | -2.81681 | -53.94638 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c7e96b2f-c9ed-3dde-8b9a-be9bbbe5873f | -2.89001 | -55.22795 | 2024-11-30 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8384d79d-1b55-3d6f-9628-3fa808ab6d06 | -3.31805 | -53.75176 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c4e52233-c6fa-30bb-9b17-6d2491b3a8c5 | -2.59467 | -53.98351 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 8a1c8976-50c6-3bcf-997a-2174d078ab0a | -2.43358 | -54.02309 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7689185a-4cc2-3993-a07c-11b8354fe972 | -2.53507 | -54.0674 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0b922873-ec16-321b-96ab-3dc09cc617f4 | -3.12184 | -50.29415 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8f988762-c7d6-3d7d-89d3-3f7c5c0c2ead | -1.58733 | -53.85277 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 014cb17c-edb6-38c9-ba9e-c8ec576333b3 | -1.32763 | -51.42649 | 2024-11-30 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 00675171-5fcf-3033-a007-9089cd42ebad | -3.35074 | -50.51437 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ce167dbf-1b87-3674-8d82-95de7e8a08c7 | -3.0239 | -54.0285 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9261055a-50f1-39e6-a5ee-e0510563711a | -3.34063 | -53.20707 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cc2b12e3-08df-3363-9bce-201898aa08a7 | -3.98943 | -48.94335 | 2024-11-30 05:01:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 5cff9a2a-f6b0-35a1-8b2f-9257de7e7e41 | -2.8331 | -53.99568 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0e8972b2-6846-3a75-a648-cd1a0200d496 | -3.14596 | -53.831 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d3353142-fcd8-3eb7-a081-40ce7f282bf0 | -1.67789 | -54.99594 | 2024-11-30 05:01:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 56e3ffbc-e3d2-3860-8749-f60e4d3d6c37 | -2.89333 | -55.22846 | 2024-11-30 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a9fb7127-dd2a-3f5d-bf75-d147deb1231f | -3.12802 | -51.12213 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0f0a6345-afdf-3b2d-b6e0-5d15adc5e357 | -3.11397 | -53.26961 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4740b2d1-04a3-3eb0-b412-5d2bdb442f38 | 1.52957 | -55.70691 | 2024-11-30 05:01:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 75c91df9-d41b-31c7-9d4d-2cde6beef48f | -2.8911 | -55.22104 | 2024-11-30 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| fc70971d-499e-393a-a432-85054af664e8 | 1.35816 | -50.72368 | 2024-11-30 05:01:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d1f3df05-fbb9-375f-8a85-2bcdf63887a7 | -1.20568 | -53.86839 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 5746def2-bfad-3dad-8a4f-6901d6a2d27f | -2.82832 | -54.09177 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 36bfc076-1b48-3b9e-b651-edfcdd6b7ecf | -2.1065 | -50.34464 | 2024-11-30 05:01:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| acefa333-9a93-3321-b20c-7819eea7bb70 | -2.9513 | -54.44906 | 2024-11-30 05:01:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 210b474f-c64a-322a-a2c9-1fcfac482fa2 | -2.80231 | -53.12151 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d62c4c21-dccd-3acf-baec-cf3d6c712727 | -0.14952 | -51.42179 | 2024-11-30 05:01:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 10535295-566a-3365-bf52-5986c7fbd01b | -1.18228 | -53.41266 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 81f46f37-a49d-3298-a789-c4a16aa5577f | -3.55694 | -53.54144 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a6703425-ebf0-3f74-a953-d4b4dae6383c | -1.17529 | -53.91005 | 2024-11-30 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 74bc0e2d-420b-3379-9023-685105a00097 | -4.00488 | -50.34881 | 2024-11-30 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d746421e-f1ae-3bd5-bd7d-af3dd3d6a82b | -2.53223 | -54.04195 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 95228133-6487-330c-b15a-8f08c5276b97 | -3.03157 | -53.03924 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 71ef2b42-f8b9-3943-aa3e-6c7ce98fddf3 | -3.65708 | -54.17696 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 62655970-075b-3ce7-80be-9dbb080c7822 | 1.18639 | -55.96648 | 2024-11-30 05:01:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 504f0522-cc75-36d4-946e-022fff07808e | -2.83475 | -49.84293 | 2024-11-30 05:01:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a41afc3a-95d6-3ad7-9872-d88e4620789e | -3.61988 | -51.53754 | 2024-11-30 05:01:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4c5e84f0-297b-3e73-a6f6-1012dd059aa2 | -2.96078 | -53.71883 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3947498b-ec77-325d-9453-bcd57ed86a91 | -3.09749 | -54.0183 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f9c2ffe1-e950-388d-bfd0-d61382f1fe48 | -1.53691 | -55.86472 | 2024-11-30 05:01:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2872ccdc-6e11-32ec-8dc7-04c62651c67a | -2.98516 | -53.89305 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a7418985-e464-3a1b-9faf-350620bebaf3 | -3.28195 | -45.56729 | 2024-11-30 05:01:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f2970624-f402-34b9-bf0a-a5913585a17d | -3.14815 | -53.71834 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 08b5c0fc-6245-3bc2-b16e-2953e697ea7b | -0.79776 | -53.05856 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 24759190-3a81-3822-bb84-dab92172a991 | -2.34743 | -53.92757 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2edccdb5-236c-3486-8766-2939b209e49c | -3.03452 | -50.98105 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e5f5e28e-9351-3409-9ed6-c11cea8025c2 | -2.66839 | -53.04104 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7f2dca91-5768-3aba-8958-b58c992c2850 | -2.81874 | -54.0437 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| c4c8fa48-aa7f-3a35-b3d4-3aaae19867f5 | -3.54298 | -51.28316 | 2024-11-30 05:01:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 32d4d391-5e8b-37d2-b0ef-6260383a962f | 0.98085 | -50.25436 | 2024-11-30 05:01:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 13f0936b-4fb6-33b5-b1be-d72a2e420bbc | -3.05969 | -53.1717 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5ccd0103-3746-3133-865a-46eafc18d189 | -1.58291 | -52.27899 | 2024-11-30 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cd8c930f-5d51-3104-901d-85d8ae3a4bb3 | -1.06275 | -53.37636 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1d06e948-f93c-306c-90c0-96f5b0ef6c28 | -1.07453 | -53.38905 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2ebf395e-71c3-3dac-923d-96031d6438f1 | -1.47867 | -55.38345 | 2024-11-30 05:01:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b466d311-38b9-3fa3-adc8-3ec2cbbdbf00 | -3.74469 | -53.39107 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ee409a13-549c-3124-8533-318fee6bbbbd | -1.68838 | -55.21009 | 2024-11-30 05:01:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README94.md)
