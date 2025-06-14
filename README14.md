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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| eaa9c09d-ee8d-3788-88e7-efb97643d8e6 | -12.23157 | -44.18074 | 2025-06-14 04:14:00 | NOAA-20 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 6fa2cd25-189c-361b-a8fb-dff2eaa7119a | -14.67325 | -53.38541 | 2025-06-14 04:14:00 | NOAA-20 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8e2ffab0-c1f7-380a-b666-fd2248bf71ea | -13.49423 | -53.48772 | 2025-06-14 04:14:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d264d808-051d-3697-86f2-f42e5f9c20e8 | -9.04393 | -47.02179 | 2025-06-14 04:14:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 319cc385-6661-324b-8a99-c9036d95e1fa | -10.92773 | -56.85129 | 2025-06-14 04:14:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 73725d5d-c02b-34a5-83d8-c0dc88795ab2 | -10.86122 | -54.30339 | 2025-06-14 04:14:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f4fe79c2-db8e-3989-8338-7cfe4093a925 | -15.39068 | -47.88998 | 2025-06-14 04:14:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5c967dd9-c3b0-3947-8f97-2429e2e3e781 | -10.09193 | -52.73943 | 2025-06-14 04:14:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 0e591def-5c30-30f3-85dc-a245ba287cd2 | -9.57272 | -46.74582 | 2025-06-14 04:14:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| eb618e3e-8b76-3662-81dc-c15a90f3a842 | -12.62456 | -57.89356 | 2025-06-14 04:14:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 71d18460-c77a-3860-8b35-b0f7cea5be9c | -12.23212 | -44.17723 | 2025-06-14 04:14:00 | NOAA-20 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| fca1e4e5-eb43-36e7-98ef-25f285b6ff30 | -9.40412 | -48.41349 | 2025-06-14 04:14:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d65c731a-5986-33f1-874a-22af434c34ae | -13.49931 | -53.48881 | 2025-06-14 04:14:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| b3ab6a63-e00a-3d5c-9e92-73003569a96b | -10.92238 | -56.84402 | 2025-06-14 04:14:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 14db84f7-e9b6-3929-9392-5421ab6b201d | -10.65486 | -44.48596 | 2025-06-14 04:14:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3461a265-7ae7-3b98-a513-4e10e54629d1 | -12.26951 | -44.60878 | 2025-06-14 04:14:00 | NOAA-20 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 49e6d206-3b88-3eba-b988-2c535b30e6db | -10.91583 | -56.84263 | 2025-06-14 04:14:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 5ca46922-dce1-33b7-a791-75c87570ecd1 | -11.92854 | -47.84366 | 2025-06-14 04:14:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e4b3904d-85b5-3729-ba16-bfbf36702555 | -10.85049 | -53.78201 | 2025-06-14 04:14:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e751e672-8660-3904-ab63-bd5def149ed1 | -14.21137 | -57.39997 | 2025-06-14 04:14:00 | NOAA-20 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 43ae6ab5-7016-376f-88e5-a0886de48c84 | -10.85104 | -46.70962 | 2025-06-14 04:14:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d378480f-19b4-377b-82d8-64131eb62a28 | -12.60933 | -57.89132 | 2025-06-14 04:14:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5496b642-b3ea-3871-9505-031ba3418646 | -13.49978 | -55.66034 | 2025-06-14 04:14:00 | NOAA-20 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 23214bf7-d241-3343-8105-f9fef58df703 | -11.56836 | -54.57114 | 2025-06-14 04:14:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dd62c175-8f79-3aa5-ad12-18a2df20c074 | -11.49498 | -48.07788 | 2025-06-14 04:14:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 22de13d1-3828-3a52-9c81-38776dbef51b | -11.72535 | -48.87283 | 2025-06-14 04:14:00 | NOAA-20 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5196a46e-b845-3c16-a432-b4c12541f1af | -12.10406 | -48.87121 | 2025-06-14 04:14:00 | NOAA-20 | SUCUPIRA | TOCANTINS | Brasil | 1720853 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cca12590-eb23-316d-924a-5fc7e01a0557 | -11.13288 | -53.9449 | 2025-06-14 04:14:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c5dd8910-6e8e-3fa9-9397-140f69bf803b | -12.68073 | -52.39418 | 2025-06-14 04:14:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 1ef8c349-1994-3627-9759-9f5b6bac844b | -11.00449 | -55.09319 | 2025-06-14 04:14:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 73eba9d4-b968-3fdb-95c8-79625bd64f58 | -8.91739 | -49.84441 | 2025-06-14 04:14:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 97b6ec44-12c9-36cc-8afa-4d94a36b9448 | -9.53352 | -46.29876 | 2025-06-14 04:14:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 13d4cbea-f228-3638-9c2d-531eefe58f9a | -14.21879 | -57.39648 | 2025-06-14 04:14:00 | NOAA-20 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 91a4bc70-602c-30a2-96d4-033a26ab50a7 | -14.20165 | -57.41436 | 2025-06-14 04:14:00 | NOAA-20 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 0314494e-012f-37cd-a25d-d26ec26ddc6f | -13.90189 | -54.61267 | 2025-06-14 04:14:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 5bb718c4-a582-3257-a558-987bf39c8bee | -13.96783 | -54.44807 | 2025-06-14 04:14:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 638f319a-f099-39bc-bdff-19351cb19009 | -10.86483 | -54.29898 | 2025-06-14 04:14:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ad4ba80c-8133-32d1-bdb3-c2464ef31b32 | -11.12694 | -53.94666 | 2025-06-14 04:14:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4e311e19-5aad-33c2-b4c6-63dcba86a32c | -15.39776 | -47.86994 | 2025-06-14 04:14:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 89eb144f-60ab-3dab-8004-f7aacd98678d | -12.61784 | -57.89193 | 2025-06-14 04:14:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 543c8127-3bc2-31f8-b48a-2fd4a408cc16 | -11.89343 | -47.45561 | 2025-06-14 04:14:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c0914170-615e-3c63-bac3-b3039ab0be42 | -11.0029 | -55.08961 | 2025-06-14 04:14:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| bb5e160e-61c7-3bfc-9fd7-2cf1b53415d2 | -13.89627 | -54.64114 | 2025-06-14 04:14:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 829bf34c-4727-3784-b385-5eb9e38b802f | -14.53631 | -46.02667 | 2025-06-14 04:14:00 | NOAA-20 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b3a10a62-0f03-3043-8f83-f27b6a150843 | -14.03733 | -55.13891 | 2025-06-14 04:14:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 40ed9a78-d2cf-3065-ad02-d4c07f3dec29 | -9.40496 | -48.40853 | 2025-06-14 04:14:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6d650d7c-f1a0-3d36-a16f-23d1f5f11db9 | -13.95847 | -54.43877 | 2025-06-14 04:14:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ebd5fb98-0881-371e-9c85-78c3c78a0116 | -13.22763 | -49.83262 | 2025-06-14 04:14:00 | NOAA-20 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 0e566708-26ed-3e37-bf3c-3c2001ba1091 | -14.03402 | -55.12619 | 2025-06-14 04:14:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 149b28d8-15ca-37ae-a299-ebe8acfdecf9 | -10.65044 | -44.49243 | 2025-06-14 04:14:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| efb3ccba-8d18-3b1b-8f16-c74ead513b76 | -12.09391 | -49.83557 | 2025-06-14 04:14:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6461cf9e-1f2b-384e-8f81-2dfa72fba35e | -11.9176 | -57.46656 | 2025-06-14 04:14:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| de29e35e-a683-3866-983e-b6670fa3944a | -10.64824 | -44.48488 | 2025-06-14 04:14:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7c44063a-89c8-39e0-a246-ec1a018d213c | -10.70141 | -46.55968 | 2025-06-14 04:14:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 496f5f10-94af-39a4-9d94-aa22bc4feaa0 | -15.3914 | -47.88584 | 2025-06-14 04:14:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c83c43b5-e7a7-35f3-95d8-6adec69dcd10 | -10.91968 | -54.78633 | 2025-06-14 04:14:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| ebf25cd2-fda3-3c7d-ba12-0f7d214fad4f | -10.65099 | -44.48893 | 2025-06-14 04:14:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6ef7045b-e332-3170-8a0b-27fa4ae1a923 | -14.21337 | -57.39516 | 2025-06-14 04:14:00 | NOAA-20 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 90eb554c-ef91-3eff-a4dc-5682b8524da9 | -12.21165 | -49.63921 | 2025-06-14 04:14:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8ed8f138-2c19-3175-a10d-a7b78cf138a2 | -8.92099 | -49.8494 | 2025-06-14 04:14:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f972a799-220f-350f-a612-24dacbf309f1 | -9.56983 | -46.74111 | 2025-06-14 04:14:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9cc1ff5c-7d28-3844-a030-1759807e2445 | -10.92133 | -54.77783 | 2025-06-14 04:14:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 0968abc1-3b09-3722-abe3-5b9f32c1167b | -10.86194 | -54.29957 | 2025-06-14 04:14:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 08caa0fc-29b1-3854-bd1d-e179811ded3b | -11.12624 | -53.95021 | 2025-06-14 04:14:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f243b0b7-2130-3658-bbdc-2e2d7e308b0c | -10.52447 | -47.58714 | 2025-06-14 04:14:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 506ffef7-83fd-3702-8a0c-bcd79c8cbb6c | -12.56674 | -57.7586 | 2025-06-14 04:14:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4e17976e-05f7-3652-8282-6281a5a2c619 | -12.61743 | -57.88636 | 2025-06-14 04:14:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| dc29ef35-78e9-3879-9c50-4c75ab30ce1b | -15.38042 | -47.86359 | 2025-06-14 04:14:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 601129a2-eed1-3061-94b0-15f4d9b65053 | -13.89037 | -54.61373 | 2025-06-14 04:14:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 8976345a-5f1a-3da2-ab63-8b67a9568b51 | -12.26083 | -46.99664 | 2025-06-14 04:14:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0f3c972d-2773-3bd6-a80f-a6b51dfccd97 | -13.8944 | -54.62193 | 2025-06-14 04:14:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 12c47159-ebee-340b-8297-b2bbb2d3e2dd | -10.85653 | -46.69824 | 2025-06-14 04:14:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e8544298-c952-37e9-9aef-41848cfb647f | -10.84512 | -53.78535 | 2025-06-14 04:14:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a4507a2c-d495-33dd-89fa-bdb680ee18e1 | -12.56547 | -57.76461 | 2025-06-14 04:14:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| acf1459d-1fd2-35fc-84fd-894dc5995d05 | -13.58502 | -54.28835 | 2025-06-14 04:14:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 595cdc71-732e-3550-9a39-8e4cb28b88fe | -10.64493 | -44.48434 | 2025-06-14 04:14:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 56c90912-831f-34ea-8602-37b1d1b433c2 | -9.4055 | -50.42049 | 2025-06-14 04:14:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e3af9502-2eee-3326-b343-045912c5c167 | -15.40048 | -44.25689 | 2025-06-14 04:14:00 | NOAA-20 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Caatinga | 0.7 |
| dc3eee45-038c-3e2c-81e4-36214ca6ac3a | -13.49726 | -53.4851 | 2025-06-14 04:14:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7e5f4d68-c40a-3855-8425-be9ca9c27838 | -14.28038 | -43.77391 | 2025-06-14 04:14:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 848e95f4-7a2b-3153-9c9d-02b4bbc93acb | -13.9012 | -54.61617 | 2025-06-14 04:14:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 946302d1-f687-33ec-ae5d-d3d561b50e16 | -10.36209 | -57.23664 | 2025-06-14 04:14:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f0ea885a-ab1d-329b-b887-42d02415a826 | -16.19562 | -46.46239 | 2025-06-14 04:14:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 19.9 |
| 40cc1b48-adbf-33af-a6de-45fc6a534fa1 | -12.61646 | -57.89839 | 2025-06-14 04:14:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2f482f6b-9ea3-379a-b3a3-a66ce4066ba2 | -14.03167 | -55.12569 | 2025-06-14 04:14:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d73272e3-ddbf-33bb-8146-838fbdb5fde2 | -11.9938 | -51.61351 | 2025-06-14 04:14:00 | NOAA-20 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f872181e-0765-341f-8399-2312a897b157 | -10.9609 | -49.56683 | 2025-06-14 04:14:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f35be220-26a3-302d-a667-af7b9effb875 | -12.61243 | -57.88418 | 2025-06-14 04:14:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 9b744a7c-632f-3ee4-9d82-aed61dde5080 | -11.13837 | -53.91561 | 2025-06-14 04:14:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| be4a88dc-b635-34ef-aee6-940d638b21d3 | -13.8951 | -54.61841 | 2025-06-14 04:14:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| dd01962a-4646-3b29-b205-653be4c0d86a | -14.20359 | -57.40934 | 2025-06-14 04:14:00 | NOAA-20 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 268c452c-cb9b-3c16-9a44-a8b90047eaa6 | -9.64758 | -48.56605 | 2025-06-14 04:14:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ab1787a3-fc2b-3db4-b283-1ee515e89ef4 | -10.85921 | -54.2979 | 2025-06-14 04:14:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c5cc59ab-ac5d-39a0-a1a8-73e70f9abed6 | -11.02107 | -45.23584 | 2025-06-14 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| eb8b07ad-3a9b-3516-91c7-f8cdb678052d | -10.84584 | -53.78165 | 2025-06-14 04:14:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5831e8c4-4f40-3c80-92e0-7f25007f426f | -11.13241 | -53.94777 | 2025-06-14 04:14:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a421123b-7954-3118-bec0-79d2b328f55c | -14.20992 | -57.41102 | 2025-06-14 04:14:00 | NOAA-20 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 7b43287b-318f-3abe-8783-e0ff2c2159cf | -11.01553 | -55.08772 | 2025-06-14 04:14:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| af52f976-019e-3173-97bd-72ba476caa49 | -8.92171 | -49.84524 | 2025-06-14 04:14:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9162af25-99e8-3efc-ae97-aaf90a519c89 | -9.4016 | -48.42852 | 2025-06-14 04:14:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |


[Clique aqui para ver as próximas entradas](README15.md)
