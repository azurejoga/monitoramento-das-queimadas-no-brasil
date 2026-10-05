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

## Dados Diários - Página 132

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ba12979d-943f-3f77-b254-115bb2ea31bd | -3.69111 | -59.6401 | 2026-10-05 17:34:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| c74047c0-d4ad-3433-9227-b65c640685d4 | -3.44624 | -59.61651 | 2026-10-05 17:34:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| ac79989d-15cb-32ee-a951-4547f8481330 | -6.16441 | -55.37798 | 2026-10-05 17:34:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 525410c4-1362-3b90-8ade-29a35292026f | -6.21449 | -55.66454 | 2026-10-05 17:34:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| f1a1cfe1-6188-3a77-9f60-d353b6a1bc70 | -3.48817 | -59.56253 | 2026-10-05 17:34:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 2a733a06-a746-34a4-ae41-d3a8f3e88def | -8.28909 | -70.37505 | 2026-10-05 17:34:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 81ad0381-e376-340f-ae7b-ee0fd42c374f | -6.91503 | -59.26372 | 2026-10-05 17:34:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 14a99d93-b4b2-305d-841c-0daa94a69cb0 | -3.98112 | -59.33873 | 2026-10-05 17:34:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 26b136ce-c8bd-3620-af2a-3053c1db01b7 | -8.1167 | -70.18394 | 2026-10-05 17:34:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 4dfd87de-581f-3eae-82e5-c82b44f711b7 | -3.36966 | -58.18349 | 2026-10-05 17:34:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ee51a288-ee94-3f81-83b3-256972841b90 | -3.24452 | -57.87181 | 2026-10-05 17:34:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 37c8cee1-d84b-3b56-900e-beb8ac6e7239 | -2.95704 | -54.15555 | 2026-10-05 17:34:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 15.1 |
| 27106831-30b3-32e1-ba5b-8017b70f758d | -3.24812 | -57.87127 | 2026-10-05 17:34:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 65ea6848-89c9-372a-b024-4ef6abecce94 | -10.64656 | -64.78574 | 2026-10-05 17:34:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 26.4 |
| f4d9bb42-ab3d-32da-9fb9-f8cb647dd8ee | -6.17087 | -55.71729 | 2026-10-05 17:34:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 99c308e0-83a2-32b4-84f6-02448ea26e79 | -4.11663 | -55.01114 | 2026-10-05 17:34:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| dc98bdd6-3520-3764-9dd0-8f6a190a2139 | -3.53732 | -59.41227 | 2026-10-05 17:34:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| bdc9e0d1-3707-39a6-8f60-4d6365dd5f9f | -1.85184 | -50.63447 | 2026-10-05 17:34:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 855a20db-9f8f-3e65-a16f-9bfe51f20e32 | -13.50415 | -61.12343 | 2026-10-05 17:34:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 20.8 |
| 74f8810d-7bbd-376a-be5d-a65b0a2187c9 | -3.44748 | -60.28769 | 2026-10-05 17:34:00 | NOAA-20 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 4a01c930-279c-3222-80dc-8000fe4fc4a5 | -3.84019 | -59.55413 | 2026-10-05 17:34:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 2f180c24-9e48-39a2-a75d-8346723d97f4 | -12.8296 | -62.13929 | 2026-10-05 17:34:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b403985c-9282-3960-a0aa-28b46cd09cab | -10.02297 | -47.60591 | 2026-10-05 17:34:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| d654c662-55b9-33d1-9b44-78cc700b3533 | -3.50778 | -59.5559 | 2026-10-05 17:34:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 2c476792-f3c2-350e-b57b-3f11a1e4f16f | -3.73857 | -59.42059 | 2026-10-05 17:34:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 1d27c551-c7d1-39a6-8ba0-1cafddc709e7 | -6.39988 | -67.94986 | 2026-10-05 17:34:00 | NOAA-20 | ITAMARATI | AMAZONAS | Brasil | 1301951 | 13 | 33 | nan | nan | nan | Amazônia | 19.6 |
| 10ec8b2e-dde4-343b-ba76-d03ee525dfd8 | -3.10937 | -57.65697 | 2026-10-05 17:34:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 5.6 |
| c0819795-8541-3af6-ba4b-db5fba98ade8 | -6.19444 | -55.34992 | 2026-10-05 17:34:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 6c245023-37e5-393d-a34a-3bd8e6a1f167 | -7.55984 | -66.18314 | 2026-10-05 17:34:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 16.3 |
| 0574c3e4-40e0-36d1-8b7f-bf0fdb1c6db5 | -9.51798 | -46.81657 | 2026-10-05 17:34:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 0ddc072e-4927-36e8-abb6-5eb2a2e30211 | -3.49371 | -57.77085 | 2026-10-05 17:34:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 200bc0d3-a8b0-3c3d-a319-0901d0d1d314 | -7.45785 | -73.6371 | 2026-10-05 17:34:00 | NOAA-20 | MÂNCIO LIMA | ACRE | Brasil | 1200336 | 12 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 19df722e-d148-3e5c-9671-4347d8a198d6 | -8.20776 | -72.51652 | 2026-10-05 17:34:00 | NOAA-20 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 32614b30-31c5-32bf-b862-563a8563ce10 | -2.95777 | -54.16022 | 2026-10-05 17:34:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 15.1 |
| 5e383a82-da79-3dd1-a048-a99cefab0b76 | -3.66974 | -52.0939 | 2026-10-05 17:34:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| de7429b2-52b8-309c-ad7d-7b17e772e677 | -2.90713 | -54.0773 | 2026-10-05 17:34:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| be83e5ca-23e5-3039-8b24-a759666166bc | -7.37633 | -73.15746 | 2026-10-05 17:34:00 | NOAA-20 | MÂNCIO LIMA | ACRE | Brasil | 1200336 | 12 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 31edfa5c-44f9-3058-9676-b159f04fe8b8 | -5.8149 | -53.8373 | 2026-10-05 17:34:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 44.2 |
| cd9692a0-8acd-3fa4-b224-8f705cd5ab2b | -3.06656 | -54.16063 | 2026-10-05 17:34:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 2aee38c8-d635-3eb3-b0dc-e0001e0b1b02 | -3.24354 | -58.75341 | 2026-10-05 17:34:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| fd24c320-6652-32e7-8e96-81677e9fdbe3 | -3.39667 | -59.51825 | 2026-10-05 17:34:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 7.0 |
| f40e56fb-2f74-38a9-9149-e5233678af60 | -3.71171 | -58.92925 | 2026-10-05 17:34:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 89.1 |
| 66aa8c63-1b46-35b6-a481-5bb5da5b8c66 | -3.97775 | -59.33925 | 2026-10-05 17:34:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 70f7444b-445d-383f-8a82-61518d673fd1 | -3.62031 | -58.60986 | 2026-10-05 17:34:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| c088be62-26d3-3cae-9648-2e71d96c86b2 | -2.95078 | -54.14343 | 2026-10-05 17:34:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 62198580-12d3-3dff-85e3-38490b821217 | -3.92953 | -52.22141 | 2026-10-05 17:34:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| f338b36e-e8e0-391a-8780-13db3e7df421 | -3.72907 | -55.47798 | 2026-10-05 17:34:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 20.4 |
| d3b62bde-7c49-38e0-b99d-57e947812b5d | -4.13095 | -59.8979 | 2026-10-05 17:34:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 36.1 |
| 365bc224-9d77-3498-8e4d-a761e723f89d | -3.07717 | -54.16838 | 2026-10-05 17:34:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 22.5 |
| 1a450672-0eea-3494-9222-6d6f9f552704 | -4.00288 | -55.67516 | 2026-10-05 17:34:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 36.0 |
| fd088c33-7de7-3fb6-987d-ba0926f96f51 | -9.61622 | -47.69304 | 2026-10-05 17:34:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 44f81d2f-24da-3ebb-ba84-88113f1aa221 | -7.27622 | -72.71595 | 2026-10-05 17:34:00 | NOAA-20 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 6.3 |
| bfc134eb-83f7-3cc0-8d76-7e4fe472af93 | -2.8681 | -54.12659 | 2026-10-05 17:34:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 35.8 |
| e5d78a9e-a881-376c-9c78-c18e2c2cd564 | -7.50291 | -70.05502 | 2026-10-05 17:34:00 | NOAA-20 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 6f0e0263-385b-38fb-b382-907cd6d3dc1f | -11.79662 | -64.88779 | 2026-10-05 17:34:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 90c05382-f32c-3053-b74f-f6cf22407da3 | -3.33157 | -57.64187 | 2026-10-05 17:34:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 61797f71-5110-34ee-b524-bf4c061e5d8a | -3.07417 | -54.17847 | 2026-10-05 17:34:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 91.6 |
| 2e2bbf02-650b-3f0c-8f3e-ba73234e9e5a | -6.9189 | -59.26672 | 2026-10-05 17:34:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 954e7684-68cf-31f9-aeec-a33e15f8dad2 | -3.67924 | -60.53764 | 2026-10-05 17:34:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 7.8 |
| c4e19eb2-a6ae-31c2-a8d1-c574efaa4cf3 | -3.07145 | -54.16751 | 2026-10-05 17:34:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 64722353-19e3-3dbe-8a46-c81a1ff38c76 | -3.66993 | -54.53754 | 2026-10-05 17:34:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| dfd9c2c3-290d-3e28-86ad-df18130f49f5 | -3.19793 | -57.08737 | 2026-10-05 17:34:00 | NOAA-20 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 449b2054-8ee4-3c4b-8cea-eb4ae5987aa8 | -9.58633 | -59.26299 | 2026-10-05 17:34:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| bc7e54a3-ef65-3586-a108-edf6da49b918 | -3.73411 | -59.02762 | 2026-10-05 17:34:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 064283f9-f324-38b7-9e32-cf7268591529 | -3.98492 | -63.15852 | 2026-10-05 17:34:00 | NOAA-20 | COARI | AMAZONAS | Brasil | 1301209 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 9acad17f-f89c-3aca-b554-4f0ed58dadbc | -3.64605 | -58.8217 | 2026-10-05 17:34:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 40676b05-1570-3115-988d-d2a0660f2089 | -3.28691 | -53.84014 | 2026-10-05 17:34:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| f721db39-cc16-3d5c-a131-e50e81e87fca | -3.74868 | -56.79924 | 2026-10-05 17:34:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 89592a6e-cb0f-33c0-9d96-6b025b9475cd | -3.63137 | -58.93052 | 2026-10-05 17:34:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 72a5a6da-390e-3731-be6a-1ef9fb5d2e14 | -2.89167 | -54.15628 | 2026-10-05 17:34:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| ae4ffe00-8594-3c7f-add6-d13bc19d3257 | -12.9204 | -62.17615 | 2026-10-05 17:34:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 0910fff8-5268-322b-9ad0-a29880c4a69f | -12.01954 | -62.52835 | 2026-10-05 17:34:00 | NOAA-20 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 1db9f7f4-dd8b-3e8e-9b84-1ffde3c75d6b | -3.01332 | -57.92284 | 2026-10-05 17:34:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 17.9 |
| 95b8b822-3307-3969-bb35-d9ef298fbcb0 | -10.36354 | -64.98907 | 2026-10-05 17:34:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 3.9 |
| dbe27186-382e-3d23-865b-19eb754ebef7 | -3.07186 | -54.16447 | 2026-10-05 17:34:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 17.2 |
| b5eb8d71-3c20-3dc4-a3c9-8f6b82f0d14b | -5.81762 | -53.8338 | 2026-10-05 17:34:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 41.4 |
| 26d032fa-6926-32ce-9acc-b361804a0beb | -3.72625 | -59.4078 | 2026-10-05 17:34:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 040c9d3e-ea46-30eb-883f-72932cb6fdda | -3.5575 | -54.48431 | 2026-10-05 17:34:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| ca3816bc-7166-3fa8-8d55-01517b7765ca | -3.37088 | -58.19146 | 2026-10-05 17:34:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| bdda7ba7-56ac-36cd-882e-b38d9d7382d6 | -3.42186 | -59.72546 | 2026-10-05 17:34:00 | NOAA-20 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 109.3 |
| 54068627-257f-3832-a4c2-15f929bf28c7 | -3.47639 | -55.42731 | 2026-10-05 17:34:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| ccb3154f-c374-3574-bbb6-5cda368185ec | -12.24339 | -51.22853 | 2026-10-05 17:34:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 8.1 |
| f05a8336-c5da-3966-b94c-e3ec37dbf3c8 | -3.70829 | -58.92977 | 2026-10-05 17:34:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 89.1 |
| f52a7c86-32ab-3897-8c74-e5cbce0a842f | -3.40059 | -59.52131 | 2026-10-05 17:34:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 0432d6be-9cd2-37ac-9449-b22ce46dad8a | -3.24862 | -58.49825 | 2026-10-05 17:34:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| b0c8973c-d57c-3fa9-9d9c-7a7fc3c935ee | -3.0734 | -54.17381 | 2026-10-05 17:34:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 22.5 |
| e04d699a-a350-3d02-b454-712e7f4924e8 | -3.08704 | -54.17168 | 2026-10-05 17:34:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 13.9 |
| 8e9cebff-f676-3955-9706-c53c13d9ac48 | -8.03121 | -71.10231 | 2026-10-05 17:34:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 10.1 |
| cadf184e-30b7-3c25-8750-fc232fd9a97f | -3.62895 | -60.20933 | 2026-10-05 17:34:00 | NOAA-20 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 5a32df14-26e9-3289-ba22-3eb51818f70f | -3.30932 | -59.49917 | 2026-10-05 17:34:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 6670f1e3-8569-35d3-9fd6-69dad71c920c | -3.4339 | -59.62567 | 2026-10-05 17:34:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 17.0 |
| 8d8d512b-d930-3364-a197-d411b11dcf3c | -3.44642 | -60.28076 | 2026-10-05 17:34:00 | NOAA-20 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 18.8 |
| 76726022-643a-39c1-b2d9-ae26819387b8 | -3.42317 | -60.54943 | 2026-10-05 17:34:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 10632c82-9ec3-3494-8dcc-56183f9f96eb | -3.28613 | -53.83532 | 2026-10-05 17:34:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 932d1119-e9f7-3e1d-bdc9-2f00d6388a9d | -6.32691 | -55.32055 | 2026-10-05 17:34:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 005c0d61-df1b-395b-a07f-46a2e711ae01 | -5.23941 | -60.19778 | 2026-10-05 17:34:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| fb583c65-d152-33d3-975f-0f666244d1d0 | -3.53456 | -59.39429 | 2026-10-05 17:34:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 83d6d6d9-ded2-3fa5-b224-4c3c00538e7c | -2.97514 | -57.90255 | 2026-10-05 17:34:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 2b2ff131-938c-3cad-aec1-38b7951ea5ea | -11.38241 | -47.72234 | 2026-10-05 17:34:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 67500ba9-153d-32b2-9d4c-4adc4bd3473b | -3.57501 | -55.41951 | 2026-10-05 17:34:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |


[Clique aqui para ver as próximas entradas](README133.md)
