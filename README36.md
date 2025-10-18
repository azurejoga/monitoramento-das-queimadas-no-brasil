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

## Dados Diários - Página 36

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 679478ae-271e-3267-98c0-738a61c6815c | -15.81997 | -42.51738 | 2025-10-18 04:04:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 40582714-b42c-3908-bc42-34098bc00c72 | -15.57952 | -42.38196 | 2025-10-18 04:04:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 097bf2bc-5ea4-3bdc-b4c1-eaccba1d7b90 | -16.13124 | -46.87725 | 2025-10-18 04:04:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 92f3e245-da13-3fed-aa62-37b9cea8ce88 | -17.96439 | -46.7441 | 2025-10-18 04:04:00 | NOAA-21 | LAGAMAR | MINAS GERAIS | Brasil | 3137106 | 31 | 33 | nan | nan | nan | Cerrado | 4.6 |
| f303ede4-aa22-3669-a58c-eedb7d66e82c | -20.03406 | -42.11987 | 2025-10-18 04:04:00 | NOAA-21 | SIMONÉSIA | MINAS GERAIS | Brasil | 3167608 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 5320f87b-d106-3fcf-b768-c59b5e2f0c2f | -18.98649 | -44.16533 | 2025-10-18 04:04:00 | NOAA-21 | CORDISBURGO | MINAS GERAIS | Brasil | 3118908 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| eb68086c-5e51-3239-84d1-3acf92900330 | -15.05191 | -48.73785 | 2025-10-18 04:04:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| eacbc744-4da7-3e9a-a69b-194d1ff410fa | -14.7398 | -47.42381 | 2025-10-18 04:04:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ee3b3d05-8831-3afe-8aa0-733639786308 | -16.20128 | -43.68528 | 2025-10-18 04:04:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c58e700f-b224-320b-a420-34f40a0835c4 | -11.6104 | -44.0913 | 2025-10-18 04:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 105.9 |
| 78bd8291-2b74-3afb-baec-e3541b46cd7d | -11.6109 | -44.0678 | 2025-10-18 04:10:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 80.3 |
| 8c800325-08a6-3b9b-b923-e704cc48c812 | 1.7664 | -55.9805 | 2025-10-18 04:10:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 44.7 |
| 0a6ae9a4-c5b5-3de3-9e0e-ea1edb4f19af | -5.0214 | -46.032 | 2025-10-18 04:10:00 | GOES-19 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 61.9 |
| cd4726ba-f43f-3887-a2bc-0d63f1f8e05b | -10.475 | -43.4342 | 2025-10-18 04:10:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 66.7 |
| 7ab55546-caad-3d06-a72f-6a7756ac22a1 | -10.4941 | -43.4315 | 2025-10-18 04:10:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 144.4 |
| 26a0d443-4f45-3510-929f-334fa11814fb | -3.1431 | -50.2464 | 2025-10-18 04:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 50.0 |
| c3c7362d-cc95-3478-abb8-174b9dcac79d | -4.4632 | -43.2386 | 2025-10-18 04:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 64.4 |
| cd9e16b5-e23f-36bc-bd21-d6b75015c17a | -13.0361 | -46.9549 | 2025-10-18 04:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 44.6 |
| f0b1635e-650f-3a94-8188-69b9f28fa5aa | -11.204 | -47.8318 | 2025-10-18 04:10:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 52.5 |
| 05d9d82e-cd83-3e5a-879c-da17ab830aa2 | -4.4445 | -43.2397 | 2025-10-18 04:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 69.7 |
| 6b498ff9-618b-3827-b23e-c992b0865062 | -5.0215 | -46.0097 | 2025-10-18 04:10:00 | GOES-19 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 65.9 |
| 56668b70-9789-31ce-8284-63ed37394de4 | -10.4937 | -43.4552 | 2025-10-18 04:10:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 99.0 |
| 958aeeb6-2c64-3486-b0e2-2f3798a788ed | -4.4632 | -43.2386 | 2025-10-18 04:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 59.1 |
| 8c951f79-fd74-3752-86ed-9ebd56b6abe6 | -10.4941 | -43.4315 | 2025-10-18 04:20:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 124.3 |
| 6256d403-30d2-37f5-bf67-6e333ff775e2 | -11.6104 | -44.0913 | 2025-10-18 04:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 81.4 |
| 1c93243c-225b-3d1a-b36a-9d1221840e39 | -12.6135 | -52.8202 | 2025-10-18 04:20:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 68.0 |
| a761c638-db88-3b4f-a32d-b1c94ae45235 | -10.4937 | -43.4552 | 2025-10-18 04:20:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 84.3 |
| 3308e4ce-f66c-3395-b526-eeafcb22c363 | -4.4445 | -43.2397 | 2025-10-18 04:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 70.9 |
| cb4b3f25-7c7e-363c-a33c-fa76ede6f916 | -5.0215 | -46.0097 | 2025-10-18 04:20:00 | GOES-19 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 82.5 |
| 94523663-6457-3bfa-b2ec-84161d5b707d | -11.6109 | -44.0678 | 2025-10-18 04:20:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 66.9 |
| 80120858-c06c-3d0b-a1a2-8fa6e41826d6 | -10.475 | -43.4342 | 2025-10-18 04:20:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 59.3 |
| 92f07d31-56f1-3ca3-b95f-711971633674 | -3.1431 | -50.2464 | 2025-10-18 04:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 47.9 |
| 8821a67b-b3f4-3c91-b65e-6aad2f3034fa | -5.0214 | -46.032 | 2025-10-18 04:20:00 | GOES-19 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 54.5 |
| 65fc7150-65cc-3d15-8f3b-e80f92f8b454 | 0.9955 | -51.18803 | 2025-10-18 04:27:00 | NPP-375D | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5507b643-ebb5-3cb1-a1d0-02f2302b477f | 1.76338 | -55.98636 | 2025-10-18 04:27:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 6cfc7315-acf7-3542-a3f7-18e7710236b1 | -3.57562 | -41.61787 | 2025-10-18 04:27:00 | NPP-375D | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 82bdc6f3-98e7-332b-899a-e9d48a7b760e | -2.56746 | -49.116 | 2025-10-18 04:27:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1abf82d2-d8ea-3ae0-8a7b-f6a0af8a2190 | 1.76524 | -55.95579 | 2025-10-18 04:27:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5eddda83-835b-3de8-8f35-287616863ada | 0.99998 | -51.18729 | 2025-10-18 04:27:00 | NPP-375D | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c9e4fcc5-124f-3084-b68e-0290c057e337 | -3.99703 | -45.50653 | 2025-10-18 04:27:00 | NPP-375D | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 4f899f5d-ac64-3bae-89fb-9f164810e904 | -2.92371 | -49.18139 | 2025-10-18 04:27:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 807e1f96-419b-352c-bee2-d3f419749657 | -2.30576 | -48.56827 | 2025-10-18 04:27:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f7aa5afa-b284-3e60-907a-5864d8b3f631 | -4.53727 | -44.79966 | 2025-10-18 04:27:00 | NPP-375D | IGARAPÉ GRANDE | MARANHÃO | Brasil | 2105203 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2db02e58-74f4-3daf-bfff-e1148b0519df | -4.08779 | -38.21334 | 2025-10-18 04:27:00 | NPP-375D | CASCAVEL | CEARÁ | Brasil | 2303501 | 23 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 1f3eaa8a-2c27-34aa-a524-a839065081ba | -4.37615 | -46.53201 | 2025-10-18 04:27:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 332e661b-dc60-31ff-a5cb-c233b03026ca | -3.51549 | -45.98684 | 2025-10-18 04:27:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 77af2e11-2c5b-324c-b17b-1c4eaee6bf1e | -2.87483 | -50.73443 | 2025-10-18 04:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8c9cbbb3-f804-3ce5-9e5e-b3e977aeb5f4 | -2.74671 | -49.39331 | 2025-10-18 04:27:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c2303c1a-4f14-3c29-a8ca-5d4774011ac4 | -3.59193 | -45.97414 | 2025-10-18 04:27:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 22a53adf-c7a4-3cc3-84ae-93d604f56e09 | -2.44567 | -49.37094 | 2025-10-18 04:27:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| bbbe485e-37f7-3783-9182-0af1424f11ed | -4.62128 | -43.58124 | 2025-10-18 04:27:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4369376b-266e-33da-b836-74dcd91289c3 | -3.5732 | -49.44009 | 2025-10-18 04:27:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9e03b1f1-62fb-34b1-886c-30f48ff5745e | -2.86194 | -50.73606 | 2025-10-18 04:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 6b45fe19-6596-38c8-9560-ec94b15017c4 | 1.5026 | -56.06504 | 2025-10-18 04:27:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ac5aef76-4737-358b-a5f7-2411e885350b | -3.99757 | -45.50307 | 2025-10-18 04:27:00 | NPP-375D | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 71921f1e-1254-3c25-b4b2-0f6baebe6c36 | -3.85232 | -41.56663 | 2025-10-18 04:27:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 4f4a3ffa-cd35-387b-987c-e827631e6d82 | -4.74353 | -44.43893 | 2025-10-18 04:27:00 | NPP-375D | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c49127de-c778-3bd1-913b-136e49948e6b | 1.76602 | -55.98178 | 2025-10-18 04:27:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8c66e07d-5c74-36a9-a28f-f9e734da60a7 | -2.41058 | -48.65632 | 2025-10-18 04:27:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4eee4af0-1f44-30ad-98ac-f53c48902c0e | -2.01881 | -47.55344 | 2025-10-18 04:27:00 | NPP-375D | MÃE DO RIO | PARÁ | Brasil | 1504059 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cfc04c21-ae82-361f-8192-281214bbc159 | -3.06665 | -43.21947 | 2025-10-18 04:27:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a1d8399d-e9ab-3be0-a209-9f81ee4a6d0d | -2.36948 | -48.51865 | 2025-10-18 04:27:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 20ecd2d4-4181-3909-8d82-6ea7bbc32aea | -4.93484 | -41.53566 | 2025-10-18 04:27:00 | NPP-375D | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| bb9be967-e161-3b96-81ec-8a6dad1d72ef | -3.99812 | -45.49961 | 2025-10-18 04:27:00 | NPP-375D | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5380566b-f716-3f31-9c91-99107303d84f | -0.90018 | -47.55062 | 2025-10-18 04:27:00 | NPP-375D | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7c6e8c9a-2f9c-38bc-86da-11e0bc386b9d | -3.34874 | -49.25095 | 2025-10-18 04:27:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3af103d5-8ea5-3260-9fd6-4594b078a04e | -3.13973 | -50.25375 | 2025-10-18 04:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 6820c1b4-15f1-385b-b2a1-0eac9ac9aea7 | -2.72467 | -48.83701 | 2025-10-18 04:27:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d2910321-1afd-3f16-b4fc-90db9c88dc63 | -3.49612 | -42.72828 | 2025-10-18 04:27:00 | NPP-375D | MILAGRES DO MARANHÃO | MARANHÃO | Brasil | 2106672 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 4e058f41-f576-3552-860f-f9864fe29c4a | -3.05676 | -43.21399 | 2025-10-18 04:27:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 3ab27daa-6415-33e7-8186-e2fe29b6c35f | -3.59526 | -45.97467 | 2025-10-18 04:27:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1f85c63c-f91f-3c83-aa9b-512e3a969dfa | 1.01107 | -51.19932 | 2025-10-18 04:27:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d957de90-fb26-334f-a5ba-7376d00b1ef5 | -2.7035 | -49.85803 | 2025-10-18 04:27:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f89c20d8-245d-3f9a-83fc-a2c1e9c3b925 | -2.56817 | -49.11158 | 2025-10-18 04:27:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4820fcfa-d5d4-32e8-905b-a77ced5f2a51 | 0.97685 | -51.18637 | 2025-10-18 04:27:00 | NPP-375D | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e4851130-5baa-381d-961a-cd723c54b65a | -2.87015 | -50.73738 | 2025-10-18 04:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6fda79b9-0a3b-36bc-9c1b-e4952b152d9c | 1.76817 | -55.97546 | 2025-10-18 04:27:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 453174d1-6a50-377a-8387-df722a35884a | -3.14106 | -50.44711 | 2025-10-18 04:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7b0d80cf-5cb8-3f66-a694-6a199fef4292 | -3.25147 | -45.96284 | 2025-10-18 04:27:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 55088ec6-a52f-37d5-b64b-7a1cea083d45 | -2.36824 | -48.29594 | 2025-10-18 04:27:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 914646e5-0316-3bb7-9544-026257ba6945 | -3.75861 | -49.03945 | 2025-10-18 04:27:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| abae5103-bd1c-3bf8-bc19-3dc0618b4879 | -2.57118 | -49.11661 | 2025-10-18 04:27:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9ce31443-545d-3154-9650-fd3a66852a9a | -4.40189 | -43.43864 | 2025-10-18 04:27:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9a3a5d9f-0406-3c9d-b2f7-769681220062 | 1.76524 | -55.97681 | 2025-10-18 04:27:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 62970cf2-808b-39f1-8b38-ac1eaed02936 | -3.52721 | -50.30342 | 2025-10-18 04:27:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| baacd2e5-838a-333e-993c-a3ebceae7e88 | 1.75975 | -55.98273 | 2025-10-18 04:27:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 8a530fe2-4f67-3cac-87bf-99a03a72b734 | -3.25504 | -52.9115 | 2025-10-18 04:27:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 16c53d9a-8c11-3b5e-af5f-57681fdf9ab3 | -2.86546 | -50.74035 | 2025-10-18 04:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 5de236bc-0d92-34b6-bbc0-4a1db8867bf9 | -4.21878 | -48.362 | 2025-10-18 04:27:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a038f847-7aab-3116-bb41-b45bc1156db3 | -3.05735 | -43.21014 | 2025-10-18 04:27:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6f877767-ee6f-3308-b851-f10ec60e762c | -3.80866 | -47.45832 | 2025-10-18 04:27:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1ed3349d-ebb4-372f-a37a-bd8d27b24295 | -4.40186 | -43.43547 | 2025-10-18 04:27:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0a9e946c-1399-3167-aa7d-7bbbac5d0a76 | -2.72535 | -48.83278 | 2025-10-18 04:27:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 19d0cabc-11d2-3d5a-8bb4-859b40a89d09 | -3.41225 | -43.01116 | 2025-10-18 04:27:00 | NPP-375D | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 1d72cc07-32bf-3825-86ac-cf20c9688a3b | -2.87425 | -50.73805 | 2025-10-18 04:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 11d04e27-6077-3308-9951-f4862be7d969 | -3.57246 | -49.44454 | 2025-10-18 04:27:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 6451a21c-9dea-3bcb-be5b-59f125ccef81 | -2.37182 | -48.29651 | 2025-10-18 04:27:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ea307f2f-2bcd-3acc-a4b0-97fd2922e4af | -4.71063 | -44.35951 | 2025-10-18 04:27:00 | NPP-375D | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| f8456fd6-b27a-3e70-97cd-cb585cc801f2 | -1.89337 | -51.01261 | 2025-10-18 04:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d028c3a7-dc14-39dd-8d04-0ef13ee8b1a7 | 1.76463 | -55.9318 | 2025-10-18 04:27:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |


[Clique aqui para ver as próximas entradas](README37.md)
