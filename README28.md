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

## Dados Diários - Página 28

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 80264b2d-efb4-38ca-9b4f-ebaa2082b329 | -2.39487 | -46.78684 | 2024-11-11 04:18:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ead6d686-827c-399a-b4d7-35f6de94f6d3 | -1.56693 | -53.42213 | 2024-11-11 04:18:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ba14503f-81c3-3d64-b3cd-57993df392b2 | -3.89814 | -52.20668 | 2024-11-11 04:18:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d02abbc1-74f5-3603-bc44-a0c813186ac1 | -4.73072 | -43.25104 | 2024-11-11 04:18:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d3fac666-9eb5-386d-b89f-79803e2e7b71 | -2.16804 | -46.68967 | 2024-11-11 04:18:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8e2741b8-75ce-3e8a-9ac6-a5efcd389bca | -2.34403 | -46.56157 | 2024-11-11 04:18:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7d26fac8-f036-39c8-8ada-a429467c20d5 | -2.72693 | -54.13971 | 2024-11-11 04:18:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a9676ba7-7862-3e94-9dd1-e147e6bf7c4e | -2.06398 | -46.34178 | 2024-11-11 04:18:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e496170e-dff2-3329-8265-878ef258c04d | -0.28753 | -51.72701 | 2024-11-11 04:18:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2ef54ec2-1379-3ccd-ad6c-eb4f631747b8 | -2.09299 | -46.45714 | 2024-11-11 04:18:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5b5c9d8f-9790-34f9-a150-3a52468f8829 | -3.10427 | -54.29578 | 2024-11-11 04:18:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| d2b6700c-11fa-3859-9d1e-2f8338d308f5 | -3.55975 | -44.95827 | 2024-11-11 04:18:00 | NPP-375D | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 6.6 |
| e826d12b-cc92-36a8-bc81-24807e34e729 | -2.15249 | -48.89998 | 2024-11-11 04:18:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fa5d6089-89c4-34cc-8d99-3bec50a57115 | -2.54503 | -46.31254 | 2024-11-11 04:18:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 559fd7ab-5b0c-310b-98b7-ed64ddd300e8 | -3.12265 | -45.97389 | 2024-11-11 04:18:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7b1bd6c3-ce08-32b7-9b1a-16733eea3f89 | -3.01598 | -53.26453 | 2024-11-11 04:18:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e0199143-a382-3d3d-a2df-7940a95f8c3b | -2.1983 | -48.38077 | 2024-11-11 04:18:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 39281d6f-f12a-3e7e-a4bb-adda5e85dd1f | -2.59698 | -48.1943 | 2024-11-11 04:18:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 51ec77f9-d8ad-30c1-946d-0595281e58c8 | -3.00055 | -46.94281 | 2024-11-11 04:18:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d378101b-3105-3b4c-80cf-12928ebedcf4 | -2.26992 | -53.74633 | 2024-11-11 04:18:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cf8bd828-a3b5-3556-bcbb-2c987c86dd14 | -2.65992 | -49.39639 | 2024-11-11 04:18:00 | NPP-375D | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 6f1d470a-ac60-33d8-8cf2-8e8bf00cea99 | -2.11558 | -47.89727 | 2024-11-11 04:18:00 | NPP-375D | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9b78959b-e531-37be-be28-fa8292697776 | -1.54377 | -52.21412 | 2024-11-11 04:18:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5471a225-a9d7-3928-bc02-1ae89a9110db | -2.24036 | -53.66645 | 2024-11-11 04:18:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4acbd4d0-f4fa-3b8a-b6bf-43c6c08eb929 | -1.60676 | -54.40363 | 2024-11-11 04:18:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b09d6901-0f85-372d-a066-ad54a062b486 | -2.69277 | -46.81331 | 2024-11-11 04:18:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4e908f0d-ffeb-34af-bd8d-042d772c516a | -5.31569 | -43.72893 | 2024-11-11 04:18:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| dae40a76-c70f-3934-a5ac-293414e0574d | -2.69639 | -46.81385 | 2024-11-11 04:18:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 14517bbd-e893-352e-80ed-89daff23d40d | -2.87353 | -45.36761 | 2024-11-11 04:18:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9e70dde1-c442-3be4-a2d5-2c8134a53c58 | -2.2978 | -46.52927 | 2024-11-11 04:18:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1398f53f-c0a6-3666-ab26-fa7f69f5e1bc | -2.59509 | -54.2454 | 2024-11-11 04:18:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7f94c509-d82b-3526-af16-24bc8965cf54 | -4.40888 | -41.90274 | 2024-11-11 04:18:00 | NPP-375D | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 6f177639-7e56-3d5f-9584-0296342c633d | -2.36891 | -46.74033 | 2024-11-11 04:18:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 164f5cd4-f3b6-3135-a8bd-ebc788dc5e34 | -3.12205 | -45.97765 | 2024-11-11 04:18:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 83a2b443-4338-36cc-b177-d36b67d8208a | -0.04008 | -50.77815 | 2024-11-11 04:18:00 | NPP-375D | AFUÁ | PARÁ | Brasil | 1500305 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| cc56d562-d86b-37d4-8937-8210297f6b66 | -2.69214 | -46.81732 | 2024-11-11 04:18:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 972e130b-c52d-39d5-8dd2-2cf2dd1c68c7 | -3.95716 | -46.70955 | 2024-11-11 04:18:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6ddbf4a2-c7b3-3b67-be64-3a22c200ad9f | -1.65832 | -52.63684 | 2024-11-11 04:18:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cb1987f8-e8a1-3924-b1f2-2623bc2bdf08 | -2.59275 | -51.71922 | 2024-11-11 04:18:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 22650232-7ddf-3b18-8b00-37037b04eafc | -2.32419 | -53.88164 | 2024-11-11 04:18:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0e8ff856-e083-3420-b26b-1492970615ec | -2.59326 | -51.72055 | 2024-11-11 04:18:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| cabd4e54-b283-3a2c-8fe2-2497223fa04d | -2.60372 | -46.16964 | 2024-11-11 04:18:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bffbf2a9-a20b-3494-96d7-10ef3e46097e | -2.39518 | -50.32114 | 2024-11-11 04:18:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 258e7c48-3d3f-3275-b444-ac30112cb3ce | -2.65145 | -46.79414 | 2024-11-11 04:18:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 207e137f-ce3c-3275-9101-10e6595bdf94 | -1.31714 | -54.63922 | 2024-11-11 04:18:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 2d6e5e0c-8d13-38e0-b323-ff77dab036c7 | -3.02612 | -50.97621 | 2024-11-11 04:18:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| dd1bb7cb-5fc0-3b0a-a49b-3d81e3a609ba | -3.74668 | -45.91622 | 2024-11-11 04:18:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 635631b3-89ce-3e23-9d38-0fbbb3f3378c | -2.39451 | -46.76561 | 2024-11-11 04:18:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b9952055-7e8f-3edf-9dcd-4ba12ad9e04d | -2.60245 | -48.18513 | 2024-11-11 04:18:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 79fdb2c3-906b-3823-8693-dc5d044cc6aa | -5.2518 | -45.63502 | 2024-11-11 04:18:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5ced422e-64ac-3ca8-902f-f57fc2a0d638 | -4.61597 | -45.9855 | 2024-11-11 04:18:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 3aa3331a-05b9-3a09-9294-fa56096ed19d | 0.45525 | -50.96302 | 2024-11-11 04:18:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b5773505-1fee-3b66-9b09-c97edc0b09b1 | -2.72626 | -54.14381 | 2024-11-11 04:18:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5560495c-d868-3b4e-83e7-5fbe19ad9983 | -2.53573 | -47.31302 | 2024-11-11 04:18:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e4468e5d-875c-37ce-8e71-22a3514308c1 | -3.96552 | -46.70278 | 2024-11-11 04:18:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1a5f7c0b-de74-3283-b886-de4ca8f4a407 | -2.17099 | -46.69436 | 2024-11-11 04:18:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 93ff86f4-2ba6-3029-810e-438565c806ba | -2.31738 | -50.67601 | 2024-11-11 04:18:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| aa01c96c-cf0c-3a7e-a14f-8c5d9821cb91 | -3.53403 | -43.18062 | 2024-11-11 04:18:00 | NPP-375D | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| db53127d-097e-385a-ab1a-8b2e74e61877 | -4.07367 | -43.95001 | 2024-11-11 04:18:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ddde9272-ff6a-320a-9053-834a37943259 | -2.73208 | -54.14478 | 2024-11-11 04:18:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1251312d-aa92-36a5-8950-ea74a12186f0 | -4.84141 | -45.84419 | 2024-11-11 04:18:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dca704d0-5253-323b-9280-f813f766689f | -0.88474 | -52.9356 | 2024-11-11 04:18:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 18511650-0862-3b8a-acec-15a45f175595 | -4.08579 | -43.93775 | 2024-11-11 04:18:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2d62e277-70a7-3a9f-ba0e-00de6506fcf3 | -4.14281 | -48.97324 | 2024-11-11 04:18:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 50890cbf-b5c4-3809-93db-ebd9d11d5d9d | -2.24545 | -53.7432 | 2024-11-11 04:18:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 912915dc-4a17-35a1-a7ca-3763d7fb9799 | -3.38683 | -46.37498 | 2024-11-11 04:18:00 | NPP-375D | SÃO JOÃO DO CARÚ | MARANHÃO | Brasil | 2111029 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b1578f43-3c78-3c4c-a937-7660bb9dec03 | -2.54441 | -46.31649 | 2024-11-11 04:18:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 284ebad9-653a-3a67-be04-e2fae33c6141 | -2.3119 | -49.12006 | 2024-11-11 04:18:00 | NPP-375D | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 635a328c-2e03-3fa2-8a2c-f1b83e4c29de | -3.02456 | -45.8204 | 2024-11-11 04:18:00 | NPP-375D | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2ad4eefc-576e-38ca-b2f1-b55df19db7e4 | -3.01539 | -53.26804 | 2024-11-11 04:18:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f0d2a8f7-9d25-36c5-a506-3505756e3c38 | -1.38335 | -52.41428 | 2024-11-11 04:18:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ea5af70f-c6af-3fc4-9077-a9674bc8321b | -3.57005 | -52.30197 | 2024-11-11 04:18:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| dfe33bec-3b69-3ce3-9da8-8ca6ae24ed09 | -2.48381 | -52.56616 | 2024-11-11 04:18:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bb264e83-df45-3362-b0b5-ab1c76024dcd | -2.9572 | -48.01519 | 2024-11-11 04:18:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9d714cd2-1547-3299-90f4-3c5021f6f176 | -2.40011 | -49.85451 | 2024-11-11 04:18:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1862da33-7ec3-3613-8cb5-6c476e5abfc9 | -2.19215 | -46.58414 | 2024-11-11 04:18:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a879f881-852d-3905-9358-8d0499a21617 | -3.24161 | -46.53816 | 2024-11-11 04:18:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3d1426bc-0e99-3bcc-8630-7648d5de7c07 | -4.61939 | -45.98602 | 2024-11-11 04:18:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.2 |
| f0e22ee0-1434-3fc0-bc7e-25205858063a | -2.40819 | -46.51669 | 2024-11-11 04:18:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 385489b6-05bf-3553-9d7a-5486b8e6d4e3 | -3.26411 | -53.69695 | 2024-11-11 04:18:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1cb50e33-d891-3d4d-9478-fb0e962b96e7 | -2.35967 | -46.79825 | 2024-11-11 04:18:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0346c9c0-09e8-3c8c-a14b-2b58ff40831e | -2.61484 | -46.16745 | 2024-11-11 04:18:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 60f48c7c-d8ae-3fcc-a688-319c925cf39d | -2.6449 | -46.78889 | 2024-11-11 04:18:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d41dafc9-0281-3ccf-b5e1-32483657c859 | -2.19598 | -48.36993 | 2024-11-11 04:18:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 814500c9-9534-3f19-b78d-5ef88103f2b2 | -3.02616 | -47.96627 | 2024-11-11 04:18:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| a4b64f52-5f74-3a21-9434-d5d82055db41 | -2.93817 | -52.77344 | 2024-11-11 04:18:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| af26e83b-b44a-3dea-abaf-b56106fa2600 | -3.08815 | -51.06725 | 2024-11-11 04:18:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 579eba10-8457-34a9-852a-028fa55ef244 | -2.2849 | -48.1935 | 2024-11-11 04:18:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0cffad73-d8f1-36ee-aeb6-14adb80248af | -2.41176 | -46.51723 | 2024-11-11 04:18:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5a975595-1c86-3b45-9bbe-e5c79ae20fab | -1.49601 | -51.73801 | 2024-11-11 04:18:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7d38a8b4-9736-31d3-8429-d4eb551764e9 | -1.63016 | -52.53982 | 2024-11-11 04:18:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6c2c5969-f70c-329d-b81d-36931cbf0297 | -1.38286 | -52.41737 | 2024-11-11 04:18:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| dd3340dc-3f88-3355-b7cd-41f2bee2cb7a | -3.02475 | -50.97447 | 2024-11-11 04:18:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| b28dfaf0-2a44-37d7-bbf1-22a206933a8e | -2.33265 | -46.56394 | 2024-11-11 04:18:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3a4cd721-e37a-3fc3-a89b-73bd5cbd98d6 | -2.68427 | -46.82021 | 2024-11-11 04:18:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6154c7c6-4f41-3aeb-8368-5f3a239451ff | -3.70558 | -53.75366 | 2024-11-11 04:18:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 5fbc68c0-7069-39d2-93ef-27eb36578fb9 | -2.09702 | -46.52421 | 2024-11-11 04:18:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 03894b23-64fb-3cfd-9e7d-ce9074704240 | -0.84052 | -52.53756 | 2024-11-11 04:18:00 | NPP-375D | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| af1585a3-593a-3486-bb0d-5cb1e570b309 | -1.39158 | -52.36248 | 2024-11-11 04:18:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d648e42d-34bb-3ca8-972a-6f405391ea21 | -3.73144 | -44.53348 | 2024-11-11 04:18:00 | NPP-375D | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |


[Clique aqui para ver as próximas entradas](README29.md)
