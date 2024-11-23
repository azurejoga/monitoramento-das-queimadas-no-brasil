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

## Dados Diários - Página 33

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1ab53592-b547-3692-b832-49d9009150b1 | -2.08262 | -46.28264 | 2024-11-23 04:16:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d739c2bd-627e-33d0-9f76-b2536db04794 | -2.43452 | -49.37551 | 2024-11-23 04:16:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8395f582-8e25-351c-9bcc-3fc3736526fa | -1.23364 | -51.74485 | 2024-11-23 04:16:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b10aae7c-492e-3873-821b-504efd08da74 | -0.32283 | -51.54067 | 2024-11-23 04:16:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 959df920-0be7-33df-933f-e3643389c64d | -1.13024 | -53.40373 | 2024-11-23 04:16:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 618479aa-7c66-3d08-abee-35cd9748cb8c | -2.15327 | -50.61928 | 2024-11-23 04:16:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a759b785-524d-326a-8e5b-7f1c858b5040 | -2.73749 | -47.53856 | 2024-11-23 04:16:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6bfc9042-e2b3-3d19-b7b1-abb80d021e95 | -2.20745 | -48.91152 | 2024-11-23 04:16:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9cc46a42-cafc-3939-b550-3a344c1f70a1 | -1.7485 | -52.38551 | 2024-11-23 04:16:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1c772114-e314-3316-b753-d72b07ed99d2 | -1.74314 | -52.38831 | 2024-11-23 04:16:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 58894937-690a-36a2-b8d5-87dd5de4de22 | -3.07881 | -45.97888 | 2024-11-23 04:16:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 400024ec-471e-36d6-b24d-8a6078c77c6d | -1.38878 | -55.19653 | 2024-11-23 04:16:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8e036076-0821-3bbd-b466-4154122125ae | -2.44441 | -46.53549 | 2024-11-23 04:16:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 621cd9f9-b9f4-3dfd-8786-e7e24ec9c122 | -1.79424 | -48.44409 | 2024-11-23 04:16:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b4ef029d-c710-3c2e-b6c5-4b4dba489d0a | -0.36454 | -51.5713 | 2024-11-23 04:16:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d02108f1-2236-384c-8cf2-fb2f1e20d2e8 | -2.6833 | -46.26182 | 2024-11-23 04:16:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c6bc0999-6b22-38d3-949f-ed91ec8ba172 | -0.96696 | -51.71586 | 2024-11-23 04:16:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 596781e9-5b42-35bc-8560-c1cd521c86ff | -2.82681 | -45.15968 | 2024-11-23 04:16:00 | NOAA-20 | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 88b3781d-7b7d-3b11-aefd-982dc3daba61 | -1.63679 | -52.41142 | 2024-11-23 04:16:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b2be7055-a3a7-363f-a679-b960e38e5aea | -2.69727 | -46.26403 | 2024-11-23 04:16:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a3ee89ac-8050-3a18-851c-4e59fe548df7 | -0.26038 | -51.57551 | 2024-11-23 04:16:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b7259636-b420-382f-91c8-4557901103a4 | -2.65677 | -46.61252 | 2024-11-23 04:16:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 576affcd-81f8-3338-83a2-11068c31313a | -2.37747 | -49.10382 | 2024-11-23 04:16:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7060875b-42dd-3d45-8cf3-3e37480b97b9 | -1.72069 | -52.72176 | 2024-11-23 04:16:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ed2ac3f1-bb7f-3654-80a0-d3e12cfd1041 | -2.65724 | -46.24574 | 2024-11-23 04:16:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4a2a50d8-9981-3b59-87c0-341c36edb5eb | -2.70721 | -46.08859 | 2024-11-23 04:16:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b6b36531-aea8-38ab-9233-add4659794ff | -2.64055 | -46.57716 | 2024-11-23 04:16:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 566c237f-a690-3dc4-abb0-5a3ded00f129 | -1.72603 | -52.72265 | 2024-11-23 04:16:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b1e01be9-1514-3f6c-b2c0-c8fe6d6ac13f | -1.79828 | -45.71819 | 2024-11-23 04:16:00 | NOAA-20 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ff56e674-61a9-3918-a2d6-23199be922a6 | -1.72657 | -52.71931 | 2024-11-23 04:16:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bdd7057c-a8c7-39e7-a331-4d276cc3d255 | -1.45842 | -55.45684 | 2024-11-23 04:16:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c39bb9b0-3403-3e5c-a191-f01b8fac5ec8 | -0.05216 | -51.23893 | 2024-11-23 04:16:00 | NOAA-20 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2569fae4-49b6-39ac-a8b4-fcde77395a62 | -2.72213 | -46.10656 | 2024-11-23 04:16:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f3858e24-ba6e-3f58-9f0c-b47cd78c19e1 | -1.22276 | -53.68913 | 2024-11-23 04:16:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 83976583-8ef1-338b-8654-5e5398bf9dc1 | -0.91537 | -51.65068 | 2024-11-23 04:16:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f728aecb-4f52-39b3-a69c-730f86e972b1 | -3.24295 | -46.48114 | 2024-11-23 04:16:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2b811aa5-83d6-345f-a51c-4d8021cf9592 | -2.6004 | -46.25687 | 2024-11-23 04:16:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 29f16a2d-d699-3b65-8648-8536ddfb85a2 | -2.20568 | -48.92237 | 2024-11-23 04:16:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 908d6453-cf7e-352b-a0cd-96e5e8a5cb57 | -2.42341 | -46.50761 | 2024-11-23 04:16:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f1243de1-145a-32e7-a1cd-8e64fc9f3230 | -2.74592 | -45.97825 | 2024-11-23 04:16:00 | NOAA-20 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f93ba4cf-d6ad-3b59-ac27-b5ed9358abbb | -1.19363 | -51.76823 | 2024-11-23 04:16:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6769c543-634f-3f4a-9626-52c949890735 | -1.29722 | -51.73441 | 2024-11-23 04:16:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b04bfb95-1082-3b8d-820f-0d7f11aac56b | -2.6909 | -46.25906 | 2024-11-23 04:16:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 05aa31ab-643b-3bef-8566-e61ea24ba561 | -1.42284 | -52.67114 | 2024-11-23 04:16:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 4fb11044-24fe-32b7-8a3c-118b596ffa7a | -1.66678 | -52.66149 | 2024-11-23 04:16:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 92036485-7e81-37ee-af04-b9a774cf8f6e | -2.61785 | -46.25972 | 2024-11-23 04:16:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d5810313-fa7f-3d69-a200-3b529ff2ee9c | -1.59997 | -52.60293 | 2024-11-23 04:16:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| a924dc8d-a2a4-3e38-806b-1ddc3c540bc4 | -1.19527 | -51.76462 | 2024-11-23 04:16:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1d73b8f1-b622-3ba1-a135-18a42dad46d4 | -2.58981 | -46.18802 | 2024-11-23 04:16:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ecfaa9c4-fcd7-35d9-bf78-1a954fabca3f | -2.69144 | -46.18797 | 2024-11-23 04:16:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6d3c0702-ff16-32af-98d4-42c8c587b7da | -1.23113 | -51.79243 | 2024-11-23 04:16:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| dcdce1b7-df74-3579-8ba7-4db9e0a77fd2 | -1.52485 | -51.62936 | 2024-11-23 04:16:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 14.4 |
| 9303cdbf-1160-3d86-9012-292183e57362 | -1.04415 | -51.74424 | 2024-11-23 04:16:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 2d9e9657-9a5e-3a78-bad5-5711ff63eb95 | -3.1793 | -46.6046 | 2024-11-23 04:16:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 40940fdd-cbf5-3669-bb41-467c75ae725e | -2.53196 | -46.3941 | 2024-11-23 04:16:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 025eddb9-c962-3c68-a476-1533037a4600 | -2.70254 | -46.09562 | 2024-11-23 04:16:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 646b7d13-927a-3466-82bb-dd99a82fe6aa | -1.61058 | -52.60468 | 2024-11-23 04:16:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 90e19411-9990-3d7c-8fe2-5af367971803 | -1.19768 | -51.96719 | 2024-11-23 04:16:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d0eb62bf-6580-34f5-b397-860aed84c9c8 | -1.77699 | -53.652 | 2024-11-23 04:16:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8beaaaf6-945a-3755-b8cd-7a0eb157eebd | -2.64615 | -46.24794 | 2024-11-23 04:16:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6549552e-46dc-3f6c-bd8a-d94a0d42c8dc | -2.67468 | -46.2485 | 2024-11-23 04:16:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| efa1a6ca-96e9-3db6-933f-19e5678b99ea | -3.2318 | -46.43195 | 2024-11-23 04:16:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 35cfaaf3-ad25-3f5a-b0f0-100942d6747d | -1.2201 | -51.79655 | 2024-11-23 04:16:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5c77b616-2e83-3cba-acfa-31db71e5d503 | -2.66218 | -46.14792 | 2024-11-23 04:16:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a201dc75-3613-3606-8f88-a91a028e9414 | -2.38159 | -49.10452 | 2024-11-23 04:16:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 73a0899c-811e-3c01-af32-f8bee6d34c0d | -1.22861 | -51.74402 | 2024-11-23 04:16:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4fefc2a4-9716-372d-917d-250d5948cb77 | -3.32109 | -45.38293 | 2024-11-23 04:16:00 | NOAA-20 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bddeb185-762c-3e73-813a-f9a4d9f2b317 | -1.6201 | -52.61303 | 2024-11-23 04:16:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 97a0bb33-03ff-35c5-8d33-90507116f366 | -2.58645 | -46.55218 | 2024-11-23 04:16:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1eb29e84-2f24-37ff-9bbd-43235c5ddf4b | -2.24652 | -49.22168 | 2024-11-23 04:16:00 | NOAA-20 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e676cb3f-7ca1-3908-8c79-d40144c1f128 | -3.09221 | -45.78284 | 2024-11-23 04:16:00 | NOAA-20 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9bfadbea-d44c-3fe5-84ff-3ef4c0792e2d | -0.7668 | -51.77386 | 2024-11-23 04:16:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fc28a7f9-45f6-3736-8f8b-93a1ae372b44 | -1.83814 | -54.52638 | 2024-11-23 04:16:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 310b4fe8-9868-35e2-8fa9-db5b1f348b07 | -2.69596 | -46.20447 | 2024-11-23 04:16:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4b6a159f-91cf-30d2-93e2-e5868bbffdfb | -2.207 | -46.29766 | 2024-11-23 04:16:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c8da5fc0-ab0c-37e6-89ca-de55a3cee4b2 | -1.62861 | -53.31849 | 2024-11-23 04:16:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 75290ad1-a1d7-33a0-ad0f-7b3548bb13c8 | -1.60135 | -52.60204 | 2024-11-23 04:16:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 1d944d4c-8e13-31e1-a9a5-4cf28bbf6995 | -0.04358 | -50.82092 | 2024-11-23 04:16:00 | NOAA-20 | AFUÁ | PARÁ | Brasil | 1500305 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 852dc075-e2f8-361b-83f8-7c27399ae9d7 | -2.76395 | -45.93108 | 2024-11-23 04:16:00 | NOAA-20 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 4b652184-2042-37fd-9b1e-a1790ec74fb3 | -2.66266 | -46.55201 | 2024-11-23 04:16:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f887d840-f43c-37f9-9167-15cc401393e3 | -2.56108 | -46.55287 | 2024-11-23 04:16:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ac071a73-2eb0-35dc-86c4-b26503c96984 | -1.78266 | -53.65295 | 2024-11-23 04:16:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b3c9ea79-6e45-30cd-b21f-78f73ba342f6 | -2.68058 | -46.16657 | 2024-11-23 04:16:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 94477fdd-1e15-34cf-98cc-7b15d0c95335 | -2.7164 | -46.09784 | 2024-11-23 04:16:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 29b97db8-4a6a-3d4e-a018-ceb036d10f17 | -1.19481 | -51.76752 | 2024-11-23 04:16:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3e581a0a-835d-3f04-b7c5-fc3080dc66cc | -1.28279 | -54.54917 | 2024-11-23 04:16:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 261d9e76-8f03-3bb5-b2ef-8d850953af38 | -3.24762 | -45.37895 | 2024-11-23 04:16:00 | NOAA-20 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 84096e05-79e5-3125-8019-f61f4e53739a | -1.82488 | -46.62506 | 2024-11-23 04:16:00 | NOAA-20 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 072e66ae-c01c-37cf-b941-d01df6d5ce93 | -2.66134 | -46.24244 | 2024-11-23 04:16:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7a768d83-e5ea-3c71-9c35-bbbdede355b2 | -1.73245 | -52.71685 | 2024-11-23 04:16:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 9ebe5baa-9e38-39e0-a8c7-4da6320001d6 | -2.25181 | -49.0008 | 2024-11-23 04:16:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7df761cf-4b14-3568-ace9-5b334e8eb224 | -2.64739 | -46.2402 | 2024-11-23 04:16:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7149ecfa-6e0a-3ed1-98ac-612b8d129597 | -2.53485 | -46.39856 | 2024-11-23 04:16:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f13cb84e-c490-3a26-ae04-f104c29320f3 | -2.44626 | -49.0874 | 2024-11-23 04:16:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 944f5115-725a-3ebd-b509-5323d533c278 | -2.1405 | -46.9215 | 2024-11-23 04:16:00 | NOAA-20 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5d55a9bb-8a9b-315a-bcd7-ced960d9e92b | -1.76712 | -52.70552 | 2024-11-23 04:16:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3cd010be-7a30-36ed-9298-46ce6fa32feb | -2.69535 | -46.20832 | 2024-11-23 04:16:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c2792e1b-6bfa-3a3d-8ff4-a07c682c1d54 | -2.70729 | -46.2458 | 2024-11-23 04:16:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 51fb47df-810f-351a-aad1-b68622960d0a | -1.70318 | -45.83543 | 2024-11-23 04:16:00 | NOAA-20 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 02d2df8b-dd14-3a33-8164-b6437ab35ff8 | -2.76336 | -45.93484 | 2024-11-23 04:16:00 | NOAA-20 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 9.2 |


[Clique aqui para ver as próximas entradas](README34.md)
