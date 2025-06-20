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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0bce8334-f281-319f-8c3f-ce7f30ffe8e9 | -10.494 | -47.0525 | 2025-06-20 03:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 118.9 |
| b8c4f079-445f-31f3-955e-074b314106c5 | -11.9518 | -58.7574 | 2025-06-20 03:10:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 56.8 |
| 98a92a5a-4fe1-38c4-aea3-204ca755f720 | -11.952 | -58.7376 | 2025-06-20 03:10:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 80.5 |
| 0b9c31ce-93ac-370a-97fe-7ce8ed661b8b | -10.4754 | -47.0325 | 2025-06-20 03:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 141.6 |
| 64dde1ac-df4c-3a84-ab15-4b165bea81e4 | -9.4807 | -56.0801 | 2025-06-20 03:10:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 53.6 |
| 29e5e57a-6869-3a6a-80dc-876cbb652699 | -19.63911 | -45.1958 | 2025-06-20 03:15:00 | NOAA-21 | BOM DESPACHO | MINAS GERAIS | Brasil | 3107406 | 31 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 97dd68ed-6de0-3437-8489-919051de8fb0 | -19.63654 | -45.19446 | 2025-06-20 03:15:00 | NOAA-21 | BOM DESPACHO | MINAS GERAIS | Brasil | 3107406 | 31 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 9fa923dd-0208-3663-8150-1ad88dd4fe77 | -22.19806 | -41.64344 | 2025-06-20 03:17:00 | NOAA-21 | CARAPEBUS | RIO DE JANEIRO | Brasil | 3300936 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 536223ef-ed87-3000-9dc8-cf93d5cca2cf | -22.69691 | -43.35005 | 2025-06-20 03:17:00 | NOAA-21 | DUQUE DE CAXIAS | RIO DE JANEIRO | Brasil | 3301702 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 6452764b-9e99-39c5-a236-3a765aea3b65 | -22.19717 | -41.64734 | 2025-06-20 03:17:00 | NOAA-21 | CARAPEBUS | RIO DE JANEIRO | Brasil | 3300936 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| bed7f8f4-2865-3f87-a3c0-edcb550e45d1 | -22.19769 | -41.64615 | 2025-06-20 03:17:00 | NOAA-21 | CARAPEBUS | RIO DE JANEIRO | Brasil | 3300936 | 33 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 399fe0c6-95a7-3351-b1f7-6ef3a8c21763 | -21.23798 | -44.05033 | 2025-06-20 03:17:00 | NOAA-21 | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 63b2710e-d1c8-384e-9232-eed4dad44040 | -22.69901 | -43.34793 | 2025-06-20 03:17:00 | NOAA-21 | BELFORD ROXO | RIO DE JANEIRO | Brasil | 3300456 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| b6d4de81-99bd-3d4c-a6d7-991fc33be884 | -11.9518 | -58.7574 | 2025-06-20 03:20:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 52.8 |
| 0548a53a-58bb-3a36-9b6c-bdb2177368e8 | -10.475 | -47.0548 | 2025-06-20 03:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 213.8 |
| 637f75cf-3549-38ed-aa17-0e45ea194f7b | -10.494 | -47.0525 | 2025-06-20 03:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 70.8 |
| 5435482e-4696-3662-bc48-80c39d29b9e1 | -16.3047 | -58.2676 | 2025-06-20 03:20:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 85.9 |
| 299c889f-45e8-3add-bb8d-4161fda84e3a | -10.4754 | -47.0325 | 2025-06-20 03:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 143.1 |
| ee990561-51f6-30e0-a342-43404483c2b8 | -11.952 | -58.7376 | 2025-06-20 03:20:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 58.4 |
| 20788baf-192a-3c44-b944-c8c400a73b3c | -10.4944 | -47.0302 | 2025-06-20 03:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 90.7 |
| b22cf487-8a25-3c58-8dc1-90d3d0ca9e46 | -9.4807 | -56.0801 | 2025-06-20 03:20:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 56.5 |
| fe6b3649-420e-3bdc-9537-431209a42510 | -10.456 | -47.0571 | 2025-06-20 03:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 61.0 |
| fb80234a-fc36-3958-82e0-d6489af6713b | -7.2219 | -43.0682 | 2025-06-20 03:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 93.8 |
| 8ab67c33-10e2-3663-945b-af4efcacc2ab | -10.4754 | -47.0325 | 2025-06-20 03:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 90.6 |
| d894d7a8-ba5a-31dd-85d5-8a8a8c9f8f62 | -7.2219 | -43.0682 | 2025-06-20 03:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 69.3 |
| 7a432162-e031-30db-94d9-7d22cb5f4467 | -11.952 | -58.7376 | 2025-06-20 03:30:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 69.8 |
| a43d7bd1-8e01-3969-807b-21b0aa4c2911 | -9.4807 | -56.0801 | 2025-06-20 03:30:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 47.0 |
| af424ae0-0d4c-3bbd-8b66-8eb791611197 | -11.1465 | -46.6573 | 2025-06-20 03:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 61.5 |
| 783dfddc-aa79-32ff-b395-352744727192 | -11.9518 | -58.7574 | 2025-06-20 03:30:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 53.1 |
| c8ff73fa-5144-35f0-8a1f-1ac317add29e | -16.3047 | -58.2676 | 2025-06-20 03:30:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 114.9 |
| ad4b6686-b4a8-3329-a6a8-85c015c514a5 | -16.305 | -58.2474 | 2025-06-20 03:30:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 69.3 |
| 4728637b-075f-3b0b-9fb2-911db5a5af07 | -10.475 | -47.0548 | 2025-06-20 03:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 138.3 |
| cb36e7d8-f08e-34a5-8e3c-dac1728c2620 | -10.456 | -47.0571 | 2025-06-20 03:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 59.1 |
| 33106821-0162-375a-ba1a-6bc54cbdb057 | -5.48526 | -42.14176 | 2025-06-20 03:38:00 | NPP-375D | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 02bdeaa1-81f8-3ad5-adbe-692dcf4bedc7 | -9.31579 | -44.83156 | 2025-06-20 03:38:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6a2be283-d597-33e0-9e4c-6cafd4071cd5 | -9.8429 | -44.69074 | 2025-06-20 03:38:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 25ba4352-b285-3a0a-b2db-623972b23163 | -9.33115 | -47.83715 | 2025-06-20 03:38:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| cf531f88-a40e-3d5a-8e0c-704b4897062f | -10.47928 | -47.03604 | 2025-06-20 03:38:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 039f3f83-70f7-3e98-8365-72cb1bf08f80 | -5.12862 | -45.02954 | 2025-06-20 03:38:00 | NPP-375D | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 434c95f5-dbc0-34c3-895e-88fb202e8e96 | -10.4296 | -47.11501 | 2025-06-20 03:38:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0d38f9b2-ed76-3ec1-ab8a-602bafd1e8a5 | -10.48568 | -47.03354 | 2025-06-20 03:38:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 581b12f0-32d9-3d75-84f1-2cc7a132b23a | -6.67017 | -44.24905 | 2025-06-20 03:38:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| cbf27caf-5559-3487-bd8b-2ff12699529f | -9.3042 | -44.82927 | 2025-06-20 03:38:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| dafbadb9-96b1-3766-848e-725359e28980 | -10.46711 | -47.06324 | 2025-06-20 03:38:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 20.5 |
| e1a8b0d3-255c-381c-848f-bdb57b2b6b66 | -7.26636 | -45.35458 | 2025-06-20 03:38:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1fa890c3-d165-34c9-bd7e-11956ec2d086 | -7.38955 | -45.40433 | 2025-06-20 03:38:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| b480d34c-0e6b-3831-bab9-21e2ddca7b60 | -4.81896 | -44.35456 | 2025-06-20 03:38:00 | NPP-375D | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3a1a81b8-b06e-3cc9-ae3b-d98d5be9392b | -10.47816 | -47.04166 | 2025-06-20 03:38:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 37.7 |
| f55bf5f1-8990-3346-9c9c-d381a0c0b491 | -10.47476 | -47.0588 | 2025-06-20 03:38:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 19.6 |
| 8f13c4b3-b3e6-305d-8c95-e998ccd1ddef | -10.48681 | -47.03213 | 2025-06-20 03:38:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4d3336b4-5756-3c0d-bc71-d7a479909fd6 | -9.8471 | -44.69975 | 2025-06-20 03:38:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7b8778fb-672f-3631-8a41-9cba8428788e | -8.37139 | -48.4228 | 2025-06-20 03:38:00 | NPP-375D | BRASILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1703602 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1d263a49-6bad-3382-91b2-3684656a832a | -8.25818 | -44.96213 | 2025-06-20 03:38:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 02d85f63-e3fb-3aad-bb11-90f3d17bc57f | -7.06189 | -43.40211 | 2025-06-20 03:38:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 739b378e-9ea8-3177-bdd9-0fc41048909d | -8.12257 | -43.12792 | 2025-06-20 03:38:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 6f490cf5-7ff4-3af3-ad3c-266173a5e66f | -9.30466 | -47.78962 | 2025-06-20 03:38:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ab2c832b-a61a-30f4-bed0-6d8dc66ced83 | -8.17091 | -43.15055 | 2025-06-20 03:38:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 793f4657-1dfb-3fe7-9c0d-625ab4658cbc | -10.46829 | -47.05731 | 2025-06-20 03:38:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 19.6 |
| 092d2f37-6c67-3cda-8847-7964d7eeea97 | -6.66936 | -44.25352 | 2025-06-20 03:38:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| c3fde689-161a-35e3-9960-62e0784f53e6 | -6.66586 | -44.2506 | 2025-06-20 03:38:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fa3ac3fa-6ee3-343b-a399-40c181b1096f | -5.48006 | -42.1409 | 2025-06-20 03:38:00 | NPP-375D | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| ec1f8532-cdb8-3a8d-8fa2-de0aab2774e5 | -8.72819 | -47.99058 | 2025-06-20 03:38:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 992f659e-fa80-3d4b-8f3a-c6f9a664b9c5 | -6.48941 | -42.84631 | 2025-06-20 03:38:00 | NPP-375D | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| aac9461d-3264-3b5d-9252-f0df716c88f7 | -7.21779 | -43.07204 | 2025-06-20 03:38:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 12.7 |
| 806c7395-d683-3272-84b8-ef3728cadacb | -9.84562 | -44.70758 | 2025-06-20 03:38:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b0ac1b17-b42f-3cc5-ab33-a78359574d72 | -7.01551 | -44.58818 | 2025-06-20 03:38:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 898d85e8-d8fc-38a7-a958-9f9994c5d044 | -5.78061 | -43.46364 | 2025-06-20 03:38:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 2a118dbf-86e2-3ce9-97c4-538f8fc37fc1 | -8.25142 | -44.96526 | 2025-06-20 03:38:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c3cf092d-1254-3b55-a10a-4ee7e99e5ec1 | -9.30438 | -47.7969 | 2025-06-20 03:38:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 3e268252-b882-3453-abe7-34e83a5dceba | -7.38863 | -45.40937 | 2025-06-20 03:38:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 866e6372-6187-3732-b5d6-167ae56ea302 | -8.72299 | -47.9954 | 2025-06-20 03:38:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 1c80dbbc-2a36-305a-ad89-19bc90af7036 | -5.78623 | -43.46477 | 2025-06-20 03:38:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 075acc27-27df-3be3-ae85-b1a1301cbcf1 | -8.26412 | -44.96332 | 2025-06-20 03:38:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 67194f22-0c94-3b7f-b171-37555186a287 | -9.31248 | -47.79228 | 2025-06-20 03:38:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0ca7b034-7b41-3dc9-be14-3ab15893e808 | -7.22378 | -43.06953 | 2025-06-20 03:38:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 12.7 |
| b561adc0-c8a0-37b3-8d18-7d44ce201eaf | -7.27253 | -45.3559 | 2025-06-20 03:38:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 819f2e4c-5f54-3775-9131-30009def380f | -4.77676 | -47.25887 | 2025-06-20 03:38:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| cb8a1d37-cf92-356f-a2ac-e8696ac5b113 | -9.30999 | -44.83042 | 2025-06-20 03:38:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b25d44a0-13b2-3cb4-8f3a-53cf9c398600 | -10.46944 | -47.05148 | 2025-06-20 03:38:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 19.6 |
| 0cd09840-727c-3cd6-b6fd-3851ebed4e85 | -9.95043 | -46.63113 | 2025-06-20 03:38:00 | NPP-375D | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 29810f27-2ff8-39ca-ae79-9600aa6b851b | -5.44552 | -43.57724 | 2025-06-20 03:38:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 369734a4-1adf-316d-81a7-3ba171f3098b | -7.2384 | -44.68651 | 2025-06-20 03:38:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2425ecb0-aa37-3c48-a972-7d326b490df7 | -5.45124 | -43.57824 | 2025-06-20 03:38:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d9a530ce-1789-3fb6-aa8e-7ee6ba541feb | -9.31169 | -44.72536 | 2025-06-20 03:38:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2a37ad8e-aadf-35be-8dce-f196c812f00b | -11.31536 | -45.20479 | 2025-06-20 03:38:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 8acaa303-5eda-3c8e-8332-5b74cd51c835 | -10.49861 | -47.00666 | 2025-06-20 03:38:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bc75df00-165b-34b4-ab72-5e96bee2227e | -9.29888 | -47.78823 | 2025-06-20 03:38:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2c1c984e-902f-3b09-af5c-ad18727b742a | -5.49509 | -42.14684 | 2025-06-20 03:38:00 | NPP-375D | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| b99eb874-5df9-3ca9-807c-28acf5f267bd | -10.48106 | -47.05609 | 2025-06-20 03:38:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b740b3c2-1df3-36b8-977c-6d3cf45034cb | -10.42122 | -47.08913 | 2025-06-20 03:38:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 96ee1459-a5ff-3e80-8667-b76bb28eb0d5 | -10.48221 | -47.05044 | 2025-06-20 03:38:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5a6f4a97-8828-385a-92a0-e1d6e0f223e0 | -6.8432 | -42.79463 | 2025-06-20 03:38:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| b7d524f6-cffe-3ef8-a1cf-b4de1e3a7c4c | -7.38816 | -45.4008 | 2025-06-20 03:38:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| bb22fad1-5e6a-3e42-be56-f642792d826c | -9.31418 | -44.83339 | 2025-06-20 03:38:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 17739adc-2dd6-30ab-8495-7ec450ddd945 | -5.49045 | -42.1427 | 2025-06-20 03:38:00 | NPP-375D | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| aabaa650-0e6d-343d-ac07-38080ccbea52 | -9.95203 | -46.62735 | 2025-06-20 03:38:00 | NPP-375D | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b5b913d6-28b3-3818-9318-4a1a66efb1a1 | -11.88091 | -40.95552 | 2025-06-20 03:38:00 | NPP-375D | TAPIRAMUTÁ | BAHIA | Brasil | 2931301 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| c0a5036d-ae58-31e9-b140-e47b1354e139 | -7.0184 | -44.60638 | 2025-06-20 03:38:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 01c3ed4e-2da6-3f0d-97b1-4a27ed5ce601 | -7.11944 | -43.14402 | 2025-06-20 03:38:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 945d3747-dd3d-3d1a-9cbc-ef31b6dfc44b | -11.31446 | -45.20619 | 2025-06-20 03:38:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |


[Clique aqui para ver as próximas entradas](README7.md)
