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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6c1717e1-09b9-3c49-a830-d87665080169 | -9.80071 | -47.74108 | 2025-05-17 04:17:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| aa4176d3-8246-3fce-a2a9-b211956f19a5 | -19.43967 | -44.34135 | 2025-05-17 04:17:00 | NPP-375D | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 945641a8-0815-3b9f-8773-f495b63681b3 | -10.31309 | -48.64533 | 2025-05-17 04:17:00 | NPP-375D | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3bedaec6-68aa-3bbe-ab5d-54beba98148c | -12.9947 | -46.32346 | 2025-05-17 04:17:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4ef01e90-61d9-3918-b696-312b6c4e39c4 | -11.41913 | -44.71196 | 2025-05-17 04:17:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8211fed5-5dd1-32a1-8587-2a8cb9323088 | -9.31038 | -44.83126 | 2025-05-17 04:17:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 62380bb7-dbb0-3627-a6b1-3da22f96f4e0 | -19.97793 | -47.18984 | 2025-05-17 04:17:00 | NPP-375D | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fae497da-592c-3ed7-8d99-38213af686b1 | -11.36465 | -52.94799 | 2025-05-17 04:17:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f78ba966-83a5-3ab7-b8ac-c03127b72cbc | -12.35419 | -49.96039 | 2025-05-17 04:17:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e1550fe0-4bf1-3943-bd73-a66c69c79544 | -22.7851 | -43.75716 | 2025-05-17 04:19:00 | NPP-375D | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 55fa26ed-d2ad-3337-a7f4-9b2d03e57ada | -21.60431 | -51.59581 | 2025-05-17 04:19:00 | NPP-375D | DRACENA | SÃO PAULO | Brasil | 3514403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 82e5e7ed-6c23-3bcb-ab9f-dbcd8a0b14ac | -20.9507 | -56.60775 | 2025-05-17 04:19:00 | NPP-375D | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 23fa11f2-c9b3-3d30-a282-37b887afd9fc | -14.02391 | -55.144 | 2025-05-17 04:19:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 33700c08-efa7-3dc5-8b13-7e4ec48bba6b | -15.56891 | -47.85531 | 2025-05-17 04:19:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 23444a20-a819-3c68-9546-d01cd0960543 | -16.0316 | -43.68042 | 2025-05-17 04:19:00 | NPP-375D | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 83a14ebd-de2f-38dd-be31-8a25fc6ac80f | -23.73725 | -52.44697 | 2025-05-17 04:19:00 | NPP-375D | TERRA BOA | PARANÁ | Brasil | 4127205 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 58f8d9b3-0f0c-3db2-bd4f-3528877485db | -20.95531 | -56.61251 | 2025-05-17 04:19:00 | NPP-375D | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 6.8 |
| af144eb7-2673-3bb3-8f32-b931ffd506cf | -15.26702 | -51.47817 | 2025-05-17 04:19:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 10321dac-9ca3-3633-b6db-fb8e028f831e | -23.34047 | -46.77219 | 2025-05-17 04:19:00 | NPP-375D | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| e8bdcf28-87c4-3fbf-b306-e6ad7ca98098 | -23.59457 | -49.01813 | 2025-05-17 04:19:00 | NPP-375D | ITAÍ | SÃO PAULO | Brasil | 3521804 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7cb3a60a-cc57-3ce5-ba97-3461a601ca1b | -13.39613 | -56.9161 | 2025-05-17 04:19:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 51ccccd7-4431-321e-9a8d-64e5093d3370 | -15.27214 | -51.47477 | 2025-05-17 04:19:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| ad513fce-6fc5-3cfa-88aa-1fe2fd93d209 | -16.88503 | -45.10693 | 2025-05-17 04:19:00 | NPP-375D | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b33d1744-53b7-3a95-bc26-d1ca6537c872 | -13.14279 | -56.81031 | 2025-05-17 04:19:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 950dcccc-9f8d-30f2-baf4-7dbb30a7990b | -13.66722 | -52.19677 | 2025-05-17 04:19:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 536565ec-c4fb-3df5-b3ab-8fbfed903719 | -12.65313 | -57.19065 | 2025-05-17 04:19:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c21db6d4-22dc-3e2d-9f42-32a7c05268d9 | -23.98572 | -48.91608 | 2025-05-17 04:19:00 | NPP-375D | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 0.4 |
| faea1a28-8282-398e-a852-2458ee5d0990 | -15.26621 | -51.48246 | 2025-05-17 04:19:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| fda9e7f7-15ea-3326-b1af-61c4ac1910d4 | -20.95148 | -56.60423 | 2025-05-17 04:19:00 | NPP-375D | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 9c92556f-fbdc-3908-a923-02afabe7faee | -22.69737 | -47.52754 | 2025-05-17 04:19:00 | NPP-375D | IRACEMÁPOLIS | SÃO PAULO | Brasil | 3521408 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 6fc854d4-6904-39bb-9736-7c78dc6d073c | -13.39722 | -56.911 | 2025-05-17 04:19:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 759e5b0c-5796-3730-842f-07a5691e577e | -13.15012 | -56.80674 | 2025-05-17 04:19:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 397faa38-5d7e-3f35-bce2-38330ed52772 | -23.29619 | -55.30931 | 2025-05-17 04:19:00 | NPP-375D | CORONEL SAPUCAIA | MATO GROSSO DO SUL | Brasil | 5003157 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| baf7050d-aa6d-3938-88db-6394c64874b7 | -13.39498 | -56.91464 | 2025-05-17 04:19:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| e37c41db-88c5-3eb1-af67-be889d59bf3d | -13.38866 | -56.91331 | 2025-05-17 04:19:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 0054c271-a7ae-3a59-b0a8-5fcdbbc7e439 | -14.02468 | -55.14022 | 2025-05-17 04:19:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6fcaa182-e074-330b-beea-74adec1daaa3 | -25.19329 | -49.32751 | 2025-05-17 04:19:00 | NPP-375D | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 490f3f92-2a07-3846-9a1e-629569fd6d75 | -22.70071 | -47.52818 | 2025-05-17 04:19:00 | NPP-375D | IRACEMÁPOLIS | SÃO PAULO | Brasil | 3521408 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 70b81adc-65f8-32ba-bdfd-5459d5d1b01c | -14.02138 | -55.12773 | 2025-05-17 04:19:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 81a41838-a359-3456-a5ef-6979d30bd5f4 | -15.26189 | -51.48161 | 2025-05-17 04:19:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 742c8ac7-6fbd-3fe3-ac60-ae26969db89a | -23.59524 | -49.01414 | 2025-05-17 04:19:00 | NPP-375D | ITAÍ | SÃO PAULO | Brasil | 3521804 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7b0f4ff7-e4f2-318a-afe7-eee099f2dc05 | -21.60333 | -51.60109 | 2025-05-17 04:19:00 | NPP-375D | DRACENA | SÃO PAULO | Brasil | 3514403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| d8cf7e39-bac1-3ca8-99cc-3f609385406a | -13.39091 | -56.90965 | 2025-05-17 04:19:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c28e6921-ba7a-3514-9304-8a57f6607c9e | -13.14906 | -56.81179 | 2025-05-17 04:19:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 6e63c170-1142-3856-8a57-03f2841fa1c0 | -14.02061 | -55.13152 | 2025-05-17 04:19:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3dd8b87d-d536-3313-9476-da29e07d9f7f | -22.78574 | -43.75562 | 2025-05-17 04:19:00 | NPP-375D | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 0bb56d24-236f-393b-b1d5-65c84d68b53a | -13.1449 | -56.80022 | 2025-05-17 04:19:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| c93e43d0-249a-3a06-ba26-430a5b438fec | -12.64667 | -57.18909 | 2025-05-17 04:19:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| ae01c009-e970-34bd-a3d4-beb158ccd841 | -13.38981 | -56.91479 | 2025-05-17 04:19:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 7.3 |
| c1106c1c-4157-3f05-bdab-1719179a6342 | -22.17868 | -49.96898 | 2025-05-17 04:19:00 | NPP-375D | MARÍLIA | SÃO PAULO | Brasil | 3529005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 35aebe0f-0f66-3f51-a2f0-165959a8dc40 | -22.90068 | -43.75311 | 2025-05-17 04:19:00 | NPP-375D | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 9f42de7f-0525-3385-a053-2f1d894207f7 | -14.01984 | -55.1353 | 2025-05-17 04:19:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6a74acdb-35be-32ec-b61f-c3bf75bb3a5e | -16.03501 | -43.68098 | 2025-05-17 04:19:00 | NPP-375D | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 67462e8e-43d4-3ce8-b97b-6fb376f5ea16 | -15.26269 | -51.47733 | 2025-05-17 04:19:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ca0ec5bb-e396-3acf-9233-2da16cf98d51 | -21.60235 | -51.6064 | 2025-05-17 04:19:00 | NPP-375D | DRACENA | SÃO PAULO | Brasil | 3514403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| 90a6b5c0-b7ab-3f3b-a93f-38bf8dea6012 | -22.68443 | -50.47444 | 2025-05-17 04:19:00 | NPP-375D | ASSIS | SÃO PAULO | Brasil | 3504008 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7f48cbeb-7bc9-3882-af24-53430f3198a9 | -21.72629 | -48.43679 | 2025-05-17 04:19:00 | NPP-375D | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 807f2b6a-b461-3f00-bae4-b635ba512b4a | -14.0173 | -55.11908 | 2025-05-17 04:19:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8eacb459-5c05-3963-ad67-f351dfe727f3 | -24.24365 | -50.73976 | 2025-05-17 04:19:00 | NPP-375D | ORTIGUEIRA | PARANÁ | Brasil | 4117305 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 4655c5f4-7515-384d-978a-4834bf8425d8 | -20.94992 | -56.6113 | 2025-05-17 04:19:00 | NPP-375D | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 4a5a2138-7aa5-3e99-aed0-9f2be4492646 | -15.26861 | -51.46968 | 2025-05-17 04:19:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2d6d9f4d-72ee-3d8b-951a-467feeef4b80 | -14.02545 | -55.13643 | 2025-05-17 04:19:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b3174697-e019-353d-917d-46bd806f0ef4 | -13.14384 | -56.80527 | 2025-05-17 04:19:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| c392f482-5082-3e0b-80d8-c248818effa2 | -21.62753 | -43.46789 | 2025-05-17 04:19:00 | NPP-375D | JUIZ DE FORA | MINAS GERAIS | Brasil | 3136702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| e07e8ef9-f8f1-333d-8fd8-d7a5c182ce9b | -15.79674 | -48.13289 | 2025-05-17 04:19:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0f14e939-cfe4-395a-95b6-d8013267c29a | -16.03445 | -43.68476 | 2025-05-17 04:19:00 | NPP-375D | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e8bc7729-0a85-394f-b55b-1f0f36c74f37 | -13.39604 | -56.90949 | 2025-05-17 04:19:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 63c1b7bb-e25f-35df-b1d4-528002459787 | -22.54079 | -48.81489 | 2025-05-17 04:19:00 | NPP-375D | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 76577167-87e0-3138-b015-57e54b11372c | -14.02214 | -55.12397 | 2025-05-17 04:19:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9cd3872a-2bf4-32db-a213-990a96dcae44 | -13.16065 | -56.81939 | 2025-05-17 04:19:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c9238a18-ba7f-3d8d-ba1f-615d9190e45a | -15.26782 | -51.47392 | 2025-05-17 04:19:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 1cb75678-e0ed-3502-8a5c-6fb0570ec3f5 | -25.18988 | -49.32685 | 2025-05-17 04:19:00 | NPP-375D | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| d4c32356-4f91-3a6a-99ee-853c9e278a97 | -13.13759 | -56.80372 | 2025-05-17 04:19:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| dd659110-af74-354a-9f43-2f2f2c3aea9a | -12.64554 | -57.19448 | 2025-05-17 04:19:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 73044b7c-b072-3698-92e3-865e051b539c | -20.99541 | -51.79272 | 2025-05-17 04:19:00 | NPP-375D | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| de0e2f03-d27e-3538-8f6e-cedcc486ad14 | -14.02622 | -55.13264 | 2025-05-17 04:19:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5f632ec7-42a4-3a18-8f2b-50b9dc943185 | -26.41257 | -48.83297 | 2025-05-17 04:19:00 | NPP-375D | JOINVILLE | SANTA CATARINA | Brasil | 4209102 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 208fbbfe-e066-3bc9-b1df-9771b547c363 | -13.16169 | -56.81437 | 2025-05-17 04:19:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1d55c01f-df3a-39ec-8146-73c733070865 | -20.95609 | -56.60899 | 2025-05-17 04:19:00 | NPP-375D | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 5.2 |
| bca7592e-c838-3ea4-be51-041a805a8cc9 | -23.29736 | -55.30382 | 2025-05-17 04:19:00 | NPP-375D | CORONEL SAPUCAIA | MATO GROSSO DO SUL | Brasil | 5003157 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 01969c3c-943e-3f20-8888-9d3c910bdf64 | -13.1498 | -56.8054 | 2025-05-17 04:20:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 45.9 |
| 64d49814-4787-3d61-80c7-e3059b59787a | -4.80839 | -48.49615 | 2025-05-17 04:36:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b310661d-2d3e-3963-acbc-d5327d9a4005 | -5.1034 | -44.79878 | 2025-05-17 04:36:00 | NOAA-20 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 22.6 |
| d29af5ed-ab83-3a73-876b-d59c1f254fa3 | -5.09954 | -44.79819 | 2025-05-17 04:36:00 | NOAA-20 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 22.6 |
| ae6614a0-a90a-32b1-878f-0e79ae60c12e | -5.67193 | -44.80073 | 2025-05-17 04:36:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 273609f8-6527-3ca4-a385-074a638db262 | -11.32134 | -46.48785 | 2025-05-17 04:38:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f081ff6c-91be-3dbc-a0c6-5003b31a68dc | -13.32687 | -45.39731 | 2025-05-17 04:38:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7f5d0395-7cf1-3547-b105-d9f1eced4521 | -6.62694 | -48.01865 | 2025-05-17 04:38:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cb802950-a5d5-376e-8029-7695155ec678 | -11.41785 | -44.7122 | 2025-05-17 04:38:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b3ed24d4-6806-33e7-9fde-a0763f1922f2 | -11.79594 | -47.40881 | 2025-05-17 04:38:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ec144f1a-732a-3af0-bda9-5d8c43e37d38 | -13.3149 | -45.3917 | 2025-05-17 04:38:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e1b201c4-51f8-3fd8-baba-0e7bfe58c0ed | -9.96108 | -49.80682 | 2025-05-17 04:38:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 423b49b5-e6a0-3569-9d78-6683dc346293 | -6.71748 | -42.12732 | 2025-05-17 04:38:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| f4a2f5fd-bad8-33b8-98b4-b9b64fd4a410 | -13.05079 | -47.82042 | 2025-05-17 04:38:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2652cef1-276f-3e40-a944-e59ad46c0518 | -6.70803 | -42.12598 | 2025-05-17 04:38:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 6.5 |
| 1c25e679-0dd2-3e94-a2bd-729f33699fe0 | -7.90654 | -44.48371 | 2025-05-17 04:38:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 938f6d2e-0d30-3a33-941e-d7a3a84ffd34 | -13.31334 | -45.37175 | 2025-05-17 04:38:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 27d5d295-a573-344e-8bc9-f6f08fc96dda | -12.11915 | -54.6675 | 2025-05-17 04:38:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ddcc85ff-7bb1-316b-842d-c5cd4e0cfb2b | -11.79673 | -47.37858 | 2025-05-17 04:38:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bd6a923a-0270-31f4-94d1-2f95a6e05c0e | -11.57985 | -47.61765 | 2025-05-17 04:38:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |


[Clique aqui para ver as próximas entradas](README9.md)
