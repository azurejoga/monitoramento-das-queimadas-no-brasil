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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 91215fec-2f16-3d62-ba0d-1b0df93ae3b3 | -3.67332 | -54.58171 | 2024-12-05 05:10:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0d837783-2ca8-39fe-8aac-8542961fa4ab | -3.70444 | -54.19282 | 2024-12-05 05:10:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 374895cf-c21d-38f7-85fa-7177c7deb19f | -3.11655 | -54.0561 | 2024-12-05 05:10:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3576d351-4a83-3a0d-b5ef-cd910c64bcbf | -3.11182 | -54.06336 | 2024-12-05 05:10:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dbec8354-7d01-3863-be65-98a8139c6848 | -6.15337 | -46.67749 | 2024-12-05 05:10:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1bfc22d8-23ec-35a3-ad48-64499461f633 | -3.1089 | -54.05891 | 2024-12-05 05:10:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8537cb5d-5d43-3ad1-bc7a-e29f5b0901d0 | -3.12007 | -54.05664 | 2024-12-05 05:10:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c2566ca1-bcc5-355b-b3dc-aec04c00d2da | -1.84575 | -60.27309 | 2024-12-05 05:10:00 | NPP-375D | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e3c0d496-26bb-3066-8b74-b6f0d0edb3be | -3.11242 | -54.05946 | 2024-12-05 05:10:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| aa6515e9-8263-35ac-a3a7-5cc4aa1f36d9 | -3.10478 | -54.06226 | 2024-12-05 05:10:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| afb5e7cf-93f5-396a-bdba-d6494ee580e3 | -3.70747 | -53.7514 | 2024-12-05 05:10:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 50655e9b-da3d-3bc9-9e13-d7281fe789b2 | -3.57275 | -53.02384 | 2024-12-05 05:10:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b8ca009a-807c-342a-938d-5b48802c181d | -3.71107 | -53.75193 | 2024-12-05 05:10:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 38f53038-ea11-3f8e-99c8-72c387185fd7 | -4.64541 | -46.31863 | 2024-12-05 05:10:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 0023715f-582c-3171-8c68-301620e52f6e | -3.71148 | -54.19395 | 2024-12-05 05:10:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9e1e1ddc-cbaa-3d94-8844-b7194620a54a | -4.64598 | -46.31458 | 2024-12-05 05:10:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| f89dfb17-3390-370b-bc9f-6a19524096b0 | -3.11715 | -54.05218 | 2024-12-05 05:10:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e227afc8-064a-3aa0-9e9d-c8566c501567 | -6.15276 | -46.68188 | 2024-12-05 05:10:00 | NPP-375D | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f79c120a-b4ee-32f6-ba06-2ae6d860494d | -3.12068 | -54.05272 | 2024-12-05 05:10:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8773833f-279d-387b-92e7-c47d69f2cbb9 | -3.63666 | -54.44051 | 2024-12-05 05:10:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dceea9c0-934b-332c-8b87-ac4bf85359ed | -3.10538 | -54.05835 | 2024-12-05 05:10:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3af371a2-1238-3ff5-9d7a-83800d3641ea | -4.64179 | -46.318 | 2024-12-05 05:10:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 86defdff-21f1-3775-a045-69324ef97107 | -15.09007 | -59.64538 | 2024-12-05 05:12:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8545d907-c8fc-3bad-98e4-8cf3bba2f4ce | -15.09178 | -59.63464 | 2024-12-05 05:12:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 32a5b12d-bbff-3cde-9392-19f8a2da9341 | -15.08674 | -59.64482 | 2024-12-05 05:12:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 38825d27-a08a-386c-b788-baef6b0e7d94 | -11.94633 | -55.14505 | 2024-12-05 05:12:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 41da5acf-1628-3dbd-b915-e0001b4512a8 | -15.06897 | -59.64918 | 2024-12-05 05:12:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c28c0eeb-a464-342f-a8a6-575e2ec14f5b | -15.08171 | -59.655 | 2024-12-05 05:12:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 858c0de3-364a-3fd6-aa04-84310a11a07f | -15.09786 | -59.63934 | 2024-12-05 05:12:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5312b027-e344-3208-8d0d-16706afa6edb | -15.08845 | -59.63408 | 2024-12-05 05:12:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c8eec83f-10dc-3fa1-8181-c77eca643d8f | -11.94569 | -55.14943 | 2024-12-05 05:12:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b60b3337-47ef-3a1f-abb1-0c67cfd6263d | -15.09291 | -59.62748 | 2024-12-05 05:12:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6100a046-c11a-3f9d-bc84-93b09f5737ae | -15.07838 | -59.65443 | 2024-12-05 05:12:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f8968f37-8890-3394-a808-106d922a7940 | -15.07847 | -59.6324 | 2024-12-05 05:12:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5e43553b-952a-3461-86b2-68b1f0f66438 | -15.08959 | -59.62692 | 2024-12-05 05:12:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| d1a5f5ea-c48e-3e75-bee0-924671dff50e | -11.95001 | -55.14558 | 2024-12-05 05:12:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 45665668-c136-3e60-b096-ade5a49839a0 | -15.07514 | -59.63185 | 2024-12-05 05:12:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ffda529d-df69-3927-b181-abbfe92d5dad | -15.07952 | -59.64728 | 2024-12-05 05:12:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6d55dffd-e478-3b23-bdb3-6ce9823f8a40 | -11.20422 | -53.82346 | 2024-12-05 05:12:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| da62f725-c32d-3c41-b9d8-d87aa3b1432d | -11.77013 | -54.69167 | 2024-12-05 05:12:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 641a749c-2a84-32cf-875f-d1491c2ca8a9 | -15.0723 | -59.64974 | 2024-12-05 05:12:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9eb00e7f-487a-3a4d-97a6-e420e80245f1 | -15.10062 | -59.64348 | 2024-12-05 05:12:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6cf2253a-c821-383b-90ce-7b597e8b7dff | -15.0895 | -59.64896 | 2024-12-05 05:12:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 13f78570-5b85-33d9-9c7d-0f0985eebde7 | -15.08902 | -59.6305 | 2024-12-05 05:12:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 8f96cbcd-ad3a-3933-a82c-57f5301e7abe | -15.09235 | -59.63106 | 2024-12-05 05:12:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 42536d47-f014-3330-970f-69241663e941 | -15.06783 | -59.65634 | 2024-12-05 05:12:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8ecc7681-e2ce-3487-93f4-298314101d11 | -15.07173 | -59.65332 | 2024-12-05 05:12:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 43ea5593-7641-33fd-a722-fe296597ac94 | -15.08893 | -59.65254 | 2024-12-05 05:12:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c0921b7a-3b6e-3f19-a99c-a34e657283d5 | -11.76636 | -54.69111 | 2024-12-05 05:12:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 14d9bd43-7a23-3f4e-b4b0-ba896ad952b6 | -15.07904 | -59.62882 | 2024-12-05 05:12:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 75f4d599-6706-3520-93e9-e40242ad94b0 | -15.07562 | -59.6503 | 2024-12-05 05:12:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d54b8809-32a9-38d8-bddd-afe65cb420b7 | -15.10005 | -59.64706 | 2024-12-05 05:12:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 05f0070e-f3dd-31b3-bce4-627ad0db0a43 | -11.20816 | -53.82408 | 2024-12-05 05:12:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 66513e1d-3980-3589-9fa0-a2fe085895d3 | -15.07895 | -59.65086 | 2024-12-05 05:12:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f887e4b7-46e4-38ff-9e4d-b46247c2e155 | -12.15361 | -55.17627 | 2024-12-05 05:12:00 | NPP-375D | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2db15b6d-4aa1-366c-91ac-388cc687a118 | -15.90405 | -60.14718 | 2024-12-05 05:14:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e36cc411-8356-3b40-9e67-191d41cbfc09 | -25.19114 | -49.32765 | 2024-12-05 05:16:00 | NPP-375D | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| c2968f99-bbf5-3977-9a31-e0e78dc72794 | -25.19782 | -49.32256 | 2024-12-05 05:16:00 | NPP-375D | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 8d8db6fa-b8d0-30ac-9d6d-835b361a2201 | -2.1725 | -54.6063 | 2024-12-05 05:20:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 43.0 |
| 4f782aab-69d3-3a42-8d89-299691e10fd0 | -2.1724 | -54.6263 | 2024-12-05 05:20:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 60.0 |
| 0c0e4494-4d16-35a4-910c-cbca11c1fdfd | 4.40898 | -60.65379 | 2024-12-05 05:29:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b19bd228-1592-3fe5-8101-7d71eec3d092 | 4.40952 | -60.65726 | 2024-12-05 05:29:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d0aa5e6e-8f17-37d1-8a6c-877a8f67e80a | -2.1725 | -54.6063 | 2024-12-05 05:30:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 43.5 |
| 59ef0413-3697-3a0c-9567-27ffb267db7e | -2.1724 | -54.6263 | 2024-12-05 05:30:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 65.5 |
| 4a584902-156d-3ee8-ae88-6a43f9d02d8a | 0.75316 | -59.655 | 2024-12-05 05:31:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ec09b869-dfde-35fa-8c77-f81f8d4300d2 | 2.43091 | -60.6507 | 2024-12-05 05:31:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 7.9 |
| e576277e-9351-345a-a44e-f7067d86007e | -2.16438 | -54.61696 | 2024-12-05 05:31:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| c1653fb1-c067-388f-a3a5-485d30cfb1fa | -2.16388 | -54.62893 | 2024-12-05 05:31:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5e16e8fe-6121-377a-95a0-b35e48d2b97b | -1.07879 | -62.65802 | 2024-12-05 05:31:00 | NOAA-20 | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7f0f9b94-3ec8-3419-a05a-be44ea6090f2 | 0.16483 | -60.59191 | 2024-12-05 05:31:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7c68eb69-f28a-337e-951b-9898c6faf38e | 1.1315 | -60.51651 | 2024-12-05 05:31:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 4421341e-093d-3b88-8a12-f61578e00529 | -1.8453 | -60.27586 | 2024-12-05 05:31:00 | NOAA-20 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 240e45f8-eb26-3882-a4fb-8151cc5e86ae | 1.08436 | -55.9763 | 2024-12-05 05:31:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| cd081a94-5a36-3c66-952c-704fda015fe6 | -0.14401 | -60.86591 | 2024-12-05 05:31:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d57332dc-3627-337b-adeb-250480eb75c6 | -2.16933 | -54.6177 | 2024-12-05 05:31:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| bb86b94f-c98a-3651-8c04-2759f45f54ed | 1.41269 | -56.07884 | 2024-12-05 05:31:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 63cd8ce3-f3d2-36c4-acb9-32a53444b0d6 | -1.07435 | -62.64326 | 2024-12-05 05:31:00 | NOAA-20 | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e391a73c-fa69-3fc8-b4c1-6a1f4d21c583 | 0.75376 | -59.65881 | 2024-12-05 05:31:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b9d68570-3808-37b1-afa4-63a47b92e26f | 1.11986 | -59.58524 | 2024-12-05 05:31:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 60a62ffc-f186-3201-aa6c-75c4d39fec2c | 0.17158 | -60.59085 | 2024-12-05 05:31:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 30f0e506-b4b1-3613-9d25-22f89ceebaa0 | -1.20222 | -61.33305 | 2024-12-05 05:31:00 | NOAA-20 | NOVO AIRÃO | AMAZONAS | Brasil | 1303205 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a506b66a-d819-3005-9553-290a4454617f | -1.32098 | -54.96894 | 2024-12-05 05:31:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a6699e4b-1a13-325e-b797-3537524e2da8 | -1.07933 | -62.65458 | 2024-12-05 05:31:00 | NOAA-20 | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5c9f7c69-91e4-312d-a87b-bcee54561980 | 2.48212 | -60.69609 | 2024-12-05 05:31:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c8f55e88-9945-38b0-9d44-e18ad57d2c51 | 2.71359 | -61.49483 | 2024-12-05 05:31:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2beb7742-2217-3a67-a679-be4907260c92 | -1.43647 | -53.81087 | 2024-12-05 05:31:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b6fd7149-38e7-3d86-831e-777b37b75165 | -1.07104 | -62.64275 | 2024-12-05 05:31:00 | NOAA-20 | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d14b547c-ce21-3521-8301-b1d8eb25d2ce | 1.1002 | -55.9656 | 2024-12-05 05:31:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2e3a2169-e69c-3234-9690-cd797d8b47d4 | 1.40847 | -56.07953 | 2024-12-05 05:31:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 223e072f-2a78-3375-bb3d-9f5b4dfa3eb8 | 0.59034 | -60.4457 | 2024-12-05 05:31:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.4 |
| c30fc0a7-c4fb-3ba6-87c0-1adc6b77b3e3 | -1.0705 | -62.64618 | 2024-12-05 05:31:00 | NOAA-20 | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 50f80982-4b1e-3057-a6ea-46bed2979794 | 1.11925 | -59.58143 | 2024-12-05 05:31:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| df81a159-346a-350f-93ac-0d1ed291e674 | -1.25883 | -54.54418 | 2024-12-05 05:31:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7bb25f37-dcb0-339b-bf98-7b2eca7f6114 | -1.25391 | -54.54348 | 2024-12-05 05:31:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ba0f0626-606f-3956-8789-0734fcedd1d5 | 2.48157 | -60.6926 | 2024-12-05 05:31:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0eb83cb2-c431-359d-9836-69dc75fca0c7 | 2.42758 | -60.65121 | 2024-12-05 05:31:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 7.9 |
| aa78daf3-1f33-3dc9-9eb7-c3deb5c50363 | -2.16884 | -54.62967 | 2024-12-05 05:31:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 42ba699c-dd29-3e8f-8a7a-047516cb7744 | 2.57717 | -60.69613 | 2024-12-05 05:31:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 3.9 |
| cf92d215-78a2-3215-8dd4-c676bfb11810 | -1.43979 | -53.81318 | 2024-12-05 05:31:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 9ad3aad5-0090-3ec3-af62-476a1b93ee05 | -2.16759 | -54.62888 | 2024-12-05 05:31:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |


[Clique aqui para ver as próximas entradas](README14.md)
