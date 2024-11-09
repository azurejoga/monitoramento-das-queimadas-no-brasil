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

## Dados Diários - Página 40

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b7d6a7c1-d411-36d1-88cd-106647543466 | -2.40081 | -48.49331 | 2024-11-09 04:31:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 18ee6a25-5c45-3f30-8421-d34cb9221b1e | -2.28081 | -50.67522 | 2024-11-09 04:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| c8a051f4-ecf2-3087-9ef1-7b037bb221c2 | -1.52268 | -51.30821 | 2024-11-09 04:31:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 650fc563-e78f-3757-be99-c9b4174a1cc6 | -3.11374 | -45.95754 | 2024-11-09 04:31:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| aaf6e18e-240e-3db5-80e9-acf4b3a0e8bd | -2.65373 | -46.07137 | 2024-11-09 04:31:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 789aa403-daa0-3f40-a91e-7e56c7159359 | -2.65071 | -46.74583 | 2024-11-09 04:31:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5b1a03c9-0f33-3248-99a6-488846070cf6 | -1.923 | -48.93672 | 2024-11-09 04:31:00 | NOAA-21 | ABAETETUBA | PARÁ | Brasil | 1500107 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 171a3dce-b7c9-3031-ba37-553e455036a6 | -2.82683 | -46.64309 | 2024-11-09 04:31:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5c063273-8219-30ef-bc3f-27d04a834b10 | -1.76394 | -52.68803 | 2024-11-09 04:31:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c154c2c0-c60b-320d-92fa-21c7ee89ebe0 | -2.65101 | -46.54823 | 2024-11-09 04:31:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 77448005-545f-3f83-a8b1-70ced00e114b | -2.47745 | -49.80964 | 2024-11-09 04:31:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a3e6b9af-81a3-3886-be8e-c95c1c1412b1 | -2.39754 | -46.75608 | 2024-11-09 04:31:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2495d985-cdff-31a2-8a78-e6afdb99487f | -2.12748 | -48.33041 | 2024-11-09 04:31:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fefee904-bed1-349a-8c7d-3c565065fcb0 | -2.48622 | -47.23703 | 2024-11-09 04:31:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7a140b71-47e1-3b53-8210-f53e50c7e3f3 | -2.3988 | -46.79144 | 2024-11-09 04:31:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 26fa6c26-5235-3029-925c-99959dd417c2 | -2.11006 | -50.57179 | 2024-11-09 04:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3678c7b7-07d0-379d-aec1-241ae4975efc | -1.64403 | -50.43942 | 2024-11-09 04:31:00 | NOAA-21 | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3c039f1d-cc5c-3dfb-985a-c529d1a9cc07 | -2.2376 | -48.36549 | 2024-11-09 04:31:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 02a83cbb-0cc4-3d89-ae84-5507a364371f | -1.99237 | -46.84388 | 2024-11-09 04:31:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b7545138-9ac2-373d-8dd8-7289f5be3aa8 | -2.4116 | -48.84227 | 2024-11-09 04:31:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a7e7a538-ddce-329f-8d97-e1ff595b3346 | -2.57021 | -46.16973 | 2024-11-09 04:31:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c0409d92-7dca-354b-adf1-e782c53f3671 | -2.23481 | -50.5188 | 2024-11-09 04:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 69b6947b-a9e4-3894-926f-957de3bdd0df | -2.18592 | -51.73894 | 2024-11-09 04:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c6be2eff-e476-308f-9860-8d6a8b9479a6 | -2.29627 | -48.55353 | 2024-11-09 04:31:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 1b8e8d03-4e60-3397-bc24-1cd126dd3211 | -2.37773 | -48.58447 | 2024-11-09 04:31:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| c74e6499-8e20-3bfc-9686-4a8a2f7424f6 | -2.81259 | -48.4551 | 2024-11-09 04:31:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 42b30a76-9a21-3a72-9279-e4b70264b937 | -2.20021 | -49.51995 | 2024-11-09 04:31:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ec4eaa0b-6f2a-3900-b746-b7d6c8ad7ab3 | -2.46004 | -49.78268 | 2024-11-09 04:31:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 13.5 |
| f6215be6-bcd5-3d6d-a39b-19af960d3f24 | -2.53269 | -47.30742 | 2024-11-09 04:31:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4948a5e1-1c0e-3f2a-8e15-08ce9908b48f | -2.06997 | -48.62956 | 2024-11-09 04:31:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 633aed60-616a-3a2d-a128-e41383d0ed88 | -2.36445 | -46.85998 | 2024-11-09 04:31:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 2dc2986d-20c5-3178-9850-a0613f802945 | -2.2665 | -48.98484 | 2024-11-09 04:31:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f7f11fcc-2a13-345f-b2e9-cbde1eb95c20 | -1.15655 | -51.9987 | 2024-11-09 04:31:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2be8321c-f51a-3a9c-ad99-05d69f5f3718 | -1.31887 | -55.88226 | 2024-11-09 04:31:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d42dc676-e1d3-368d-91a0-3e0b4f2bcca4 | -3.23798 | -45.3886 | 2024-11-09 04:31:00 | NOAA-21 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d0a3dfc1-c1ec-39c1-8a99-19947da9fbed | -2.15984 | -48.27733 | 2024-11-09 04:31:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b865179d-4fc3-3c90-99f9-82b33212c26a | -2.23447 | -46.55765 | 2024-11-09 04:31:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 72eb08b2-0082-3d47-826f-ba69a95b99fc | 3.3578 | -51.27227 | 2024-11-09 04:31:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 418d7aaa-1aa7-30e9-980c-d3e88d82bda0 | -1.46158 | -53.42012 | 2024-11-09 04:31:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2d9cd14e-125e-39c2-a5a5-3a174e835ba6 | -2.37933 | -46.74273 | 2024-11-09 04:31:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4f270024-a38e-3e70-b8ce-f51bb4726c70 | -2.43271 | -48.59721 | 2024-11-09 04:31:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0ae36046-50d2-3f7d-8cb6-bb350192aa98 | -2.42829 | -48.47197 | 2024-11-09 04:31:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c9528169-fe12-337a-a20c-7d941fdef0bf | -2.61675 | -46.15538 | 2024-11-09 04:31:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1964938c-b581-376c-96ee-5c7f65881206 | -2.60955 | -46.15786 | 2024-11-09 04:31:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ef49c66a-33f3-34d7-ad0d-1557069788db | -2.62861 | -48.4735 | 2024-11-09 04:31:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| a4d1840d-103b-3eb5-94d5-dd0e0a1d1a98 | -2.13064 | -50.82753 | 2024-11-09 04:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2f981b50-e539-33ff-a654-ba2b5baab9b8 | -2.03437 | -50.08556 | 2024-11-09 04:31:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| de7f8081-314e-31d1-a3b8-18e217c6fe45 | -2.65706 | -46.07187 | 2024-11-09 04:31:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 31cc12ea-5a94-3c45-9754-2d610afa33d3 | -2.72394 | -47.99865 | 2024-11-09 04:31:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c674cb18-435b-3884-846a-b4395d314bc6 | -2.15594 | -48.28035 | 2024-11-09 04:31:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2bb274ca-2988-382d-aabf-0c07f06ff327 | -1.40187 | -52.00357 | 2024-11-09 04:31:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 478cccac-a07d-3ab2-a3e3-d7a05492fff7 | -1.4946 | -51.99699 | 2024-11-09 04:31:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 217b2eb2-28b5-3b47-b045-deb7ccbf052b | -3.10368 | -45.95599 | 2024-11-09 04:31:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2cb3f11a-131d-38d7-a7e8-f7d7045ee7f0 | -1.14664 | -53.65948 | 2024-11-09 04:31:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| e71d28df-d97d-3019-a4ec-40ed19e0261f | -2.18781 | -48.31792 | 2024-11-09 04:31:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4add1269-9ab3-3885-a0bf-0f3a651100d6 | -2.03208 | -50.08631 | 2024-11-09 04:31:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2c0cc696-6c8d-3772-a503-8f5560dc03e3 | -2.4105 | -50.3063 | 2024-11-09 04:31:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0cef4c96-b57c-3db1-9281-00ba75c3179b | -2.31291 | -49.0911 | 2024-11-09 04:31:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 49de0629-1e11-3f30-aecd-a30e01852bfa | -2.06673 | -53.27775 | 2024-11-09 04:31:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a89fc586-b351-3be7-8f78-f97263a1145e | -1.68728 | -51.91484 | 2024-11-09 04:31:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 57590705-f933-3e6b-a09d-8f8fd8d74955 | -3.12727 | -45.95264 | 2024-11-09 04:31:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| bbf22c2b-1874-31dd-aaae-ba005ae1101f | -1.19963 | -53.91896 | 2024-11-09 04:31:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0d62b9be-9f94-35ef-a11b-e962193c08b8 | -1.65953 | -55.08714 | 2024-11-09 04:31:00 | NOAA-21 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 01196262-4090-3a73-b091-2672a534b143 | -2.23369 | -48.36853 | 2024-11-09 04:31:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| fb58cea2-53fd-353a-9e55-916d03c16937 | 1.08716 | -51.30338 | 2024-11-09 04:31:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3d16c955-36e6-3c76-a0dc-929b76be664b | -2.65264 | -48.5612 | 2024-11-09 04:31:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 42dd63fa-cf4f-3b27-83df-cf43a83b42b3 | -2.12091 | -46.7655 | 2024-11-09 04:31:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a3fd708d-dfaa-38f7-b67e-c134ac8cee83 | -2.23931 | -48.70738 | 2024-11-09 04:31:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e1a9ebe4-3e3b-3e72-a29b-1dc26a3e9ffe | -2.07717 | -52.0378 | 2024-11-09 04:31:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d223cfa4-eb10-3fb5-b90c-df498a535080 | -0.0842 | -51.4049 | 2024-11-09 04:31:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7a789257-c9ec-32f3-a579-2ba560111274 | -2.92918 | -47.03225 | 2024-11-09 04:31:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8307cf43-d453-3dec-ab51-03f5876ea6e8 | -1.60331 | -53.32391 | 2024-11-09 04:31:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| c49cf2d1-0ba9-341a-821a-8cd599c8dfd4 | -2.31017 | -48.31858 | 2024-11-09 04:31:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a14af8fb-581e-35ee-984f-7e975eb1d2c2 | -2.29233 | -48.5566 | 2024-11-09 04:31:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 88cb68ac-542e-3dee-83ac-592630317b1d | -2.13533 | -48.38987 | 2024-11-09 04:31:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 73d41333-64f6-3be9-89d9-e3adbd8024b6 | -1.50915 | -52.16903 | 2024-11-09 04:31:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0ecaf7a3-6483-32fc-a8ac-b1e08d7edbbf | -2.38005 | -46.78153 | 2024-11-09 04:31:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7c97d5ea-8068-39e2-972e-58ccb1ae47d3 | -2.24798 | -46.49269 | 2024-11-09 04:31:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c8d0cb0c-a23f-3740-acdf-1c416adb7c5f | -2.09557 | -46.53276 | 2024-11-09 04:31:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c2d2b6fb-0640-3ed2-9858-da2ff2a5ef0f | -1.52789 | -52.18314 | 2024-11-09 04:31:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cf365b45-ea7b-3c17-951c-258a037c1e0b | -2.1698 | -48.7301 | 2024-11-09 04:31:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f9feb9b0-3248-3aa7-9b11-363ce18c9fe9 | -2.26023 | -46.82987 | 2024-11-09 04:31:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 994ace66-577b-3558-9e75-d5e31f83745b | -2.54253 | -46.3046 | 2024-11-09 04:31:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9c0eb45f-d26e-3447-8cfe-c29ac968f649 | -2.33434 | -48.86354 | 2024-11-09 04:31:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6a0825de-f710-3337-8b2a-6a7414ea77ab | -2.54706 | -47.32368 | 2024-11-09 04:31:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f9a553d6-27b4-323d-b61d-027c4ca05fce | -1.97482 | -53.14021 | 2024-11-09 04:31:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 589e44e3-a69a-3794-95a0-e89b77036b43 | -2.67601 | -46.78212 | 2024-11-09 04:31:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 140e80cb-8d08-3fff-a2ae-6effcebd8583 | -2.19845 | -48.37402 | 2024-11-09 04:31:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f6b44e93-7a04-3ddb-b6fc-5eb8821a0769 | -2.24442 | -50.41102 | 2024-11-09 04:31:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4e0f4633-bae4-36fd-90fe-795e92489d0e | -1.95097 | -46.41114 | 2024-11-09 04:31:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1c28ad00-3e58-3a39-9069-400d936996d6 | -3.12338 | -45.95567 | 2024-11-09 04:31:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 04c4d5da-5f87-327e-a009-33c95ba9fd0d | -2.30377 | -46.72406 | 2024-11-09 04:31:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 38cb9720-f660-3d61-a6e5-3c3af9f23a68 | 3.37192 | -51.28173 | 2024-11-09 04:31:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 47a91e8a-804a-3903-b39b-ffd1541aa2f7 | -3.31163 | -49.63328 | 2024-11-09 04:33:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4246ee54-6b71-3fce-a1b0-e43e8634f57e | -1.83208 | -55.19784 | 2024-11-09 04:33:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e917709f-0fcd-35f6-84bf-4db887bc263f | -3.97471 | -48.18071 | 2024-11-09 04:33:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 85.0 |
| a11c3787-46da-3a57-9448-7efc0ce018c8 | -11.18503 | -44.6193 | 2024-11-09 04:33:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 32d0ba24-6b37-3759-9257-98241f548295 | -6.17717 | -45.45118 | 2024-11-09 04:33:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| be33f32a-bd0a-3ca2-abbe-3175da70c784 | -3.25128 | -46.4714 | 2024-11-09 04:33:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0de9f3fb-a1ad-3fe3-baf6-ddf1e098c485 | -3.94166 | -48.3469 | 2024-11-09 04:33:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README41.md)
