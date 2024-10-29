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

## Dados Diários - Página 69

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8af75cb5-1486-319b-a09a-9a98a356e268 | -29.77722 | -51.17495 | 2024-10-29 04:46:00 | NOAA-21 | SÃO LEOPOLDO | RIO GRANDE DO SUL | Brasil | 4318705 | 43 | 33 | nan | nan | nan | Pampa | 0.4 |
| 95f34971-f065-3eb5-9abe-7b1aa18b9693 | -26.59501 | -51.74994 | 2024-10-29 04:46:00 | NOAA-21 | ÁGUA DOCE | SANTA CATARINA | Brasil | 4200408 | 42 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 5b3ed65a-b0bf-3775-95fb-1936b6e25c3d | -12.3522 | -49.94 | 2024-10-29 04:46:16 | GOES-16 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 76.2 |
| 488f58a8-4d8e-3fc8-aec6-28a73aa509f4 | -12.3526 | -49.9184 | 2024-10-29 04:46:16 | GOES-16 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 89.5 |
| dd53ee4f-8d90-3bc3-9df0-aa8ffc973333 | -13.6891 | -46.1017 | 2024-10-29 04:46:23 | GOES-16 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 75.2 |
| 21061859-ccba-3038-842b-1657e423cc44 | -13.6887 | -46.1247 | 2024-10-29 04:46:23 | GOES-16 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 82.9 |
| 2d876b5e-5fc5-39da-ac6f-6cd733eed9ce | -12.77141 | -39.54162 | 2024-10-29 04:49:00 | AQUA_M-M | SANTA TEREZINHA | BAHIA | Brasil | 2928505 | 29 | 33 | nan | nan | nan | Mata Atlântica | 6.7 |
| 5d16332a-ad71-34ee-9c2a-22f7698971bd | -12.77004 | -39.55067 | 2024-10-29 04:49:00 | AQUA_M-M | SANTA TEREZINHA | BAHIA | Brasil | 2928505 | 29 | 33 | nan | nan | nan | Mata Atlântica | 18.5 |
| ab0eed9d-17b4-3542-9084-544f40af7e7e | -13.33649 | -41.80016 | 2024-10-29 04:49:00 | AQUA_M-M | ABAÍRA | BAHIA | Brasil | 2900108 | 29 | 33 | nan | nan | nan | Caatinga | 8.3 |
| 930f80a4-7c3f-38f6-88fb-58de5cc5cc9a | -15.93103 | -41.97668 | 2024-10-29 04:49:00 | AQUA_M-M | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 356e4049-3617-3331-8d4c-67e47c687bdb | -6.35701 | -41.57211 | 2024-10-29 04:49:00 | AQUA_M-M | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 9.4 |
| 359ad9ca-06de-3014-902d-cbbc89a0eb11 | -6.99972 | -41.32865 | 2024-10-29 04:49:00 | AQUA_M-M | SUSSUAPARA | PIAUÍ | Brasil | 2210938 | 22 | 33 | nan | nan | nan | Caatinga | 8.5 |
| b033a9cc-39c4-3df1-a18a-e00d656c621a | -11.10581 | -43.33909 | 2024-10-29 04:49:00 | AQUA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 19.4 |
| 011f6293-a787-35f6-937c-ed60af968eeb | -12.66768 | -43.80621 | 2024-10-29 04:49:00 | AQUA_M-M | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 8b1a22b5-2221-3ac0-9948-3096fd9b44df | -12.66521 | -43.82068 | 2024-10-29 04:49:00 | AQUA_M-M | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 23.6 |
| ec91289b-5831-3501-a50f-0281afe3566f | -12.66383 | -43.81491 | 2024-10-29 04:49:00 | AQUA_M-M | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 23.0 |
| 42301fdd-d79c-33f6-b942-4b7c83175aa0 | -12.43595 | -43.73338 | 2024-10-29 04:49:00 | AQUA_M-M | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 9025d687-a218-345b-95ff-e3dcbcb5a2a9 | -14.15686 | -44.07809 | 2024-10-29 04:49:00 | AQUA_M-M | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 0365e54a-ce21-3ff9-9ceb-99d677f1a7a3 | -14.14833 | -44.06178 | 2024-10-29 04:49:00 | AQUA_M-M | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 625868ac-1d73-376a-aa93-26162bb73c13 | -14.14591 | -44.07613 | 2024-10-29 04:49:00 | AQUA_M-M | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 90.1 |
| 1a1ef783-8d72-3a26-b7d4-9d1e201ccbaf | -14.13308 | -44.35231 | 2024-10-29 04:49:00 | AQUA_M-M | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 519b86ba-e3df-3afe-b99b-a63898fcfe71 | -14.13238 | -44.36063 | 2024-10-29 04:49:00 | AQUA_M-M | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 9.5 |
| a9e6d59a-8b97-3b3b-b7bd-49fa4b77f2b0 | -5.93787 | -43.68024 | 2024-10-29 04:49:00 | AQUA_M-M | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 28.4 |
| 67eb3284-9f7a-3ac1-b020-e8fab75df86f | -5.93699 | -43.67294 | 2024-10-29 04:49:00 | AQUA_M-M | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 27.5 |
| 69a8fde8-d5a4-338f-a685-d25fef7fba0c | -6.46084 | -44.65981 | 2024-10-29 04:49:00 | AQUA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 25.5 |
| 3f2a0913-96fc-3c58-b147-280342d1b384 | -6.45725 | -44.6815 | 2024-10-29 04:49:00 | AQUA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 39.8 |
| 83755a10-91de-30f0-90fa-0f2bcbbb9f2b | -13.70252 | -46.10223 | 2024-10-29 04:49:00 | AQUA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 46.9 |
| c95b89a3-4a8a-337a-b991-e415a3b421cc | -13.69886 | -46.12288 | 2024-10-29 04:49:00 | AQUA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 86.0 |
| 7ae947c3-8366-358b-b344-c2aec3c7a390 | -13.68591 | -46.1205 | 2024-10-29 04:49:00 | AQUA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 19.1 |
| 0ffc4b6a-ee04-366c-9bb2-4a3ee6b953d5 | -13.60928 | -45.58278 | 2024-10-29 04:49:00 | AQUA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 61.6 |
| beeb65ee-d4ae-3a1b-8085-a05b4d682cb3 | -13.60597 | -45.6017 | 2024-10-29 04:49:00 | AQUA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 16.7 |
| a091301e-0f0d-3d83-8764-c22c1e8d0c68 | -9.7038 | -46.23614 | 2024-10-29 04:49:00 | AQUA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 21.2 |
| 80ef66fd-c91d-3b04-afe2-0e465d52c32d | -12.34027 | -49.91116 | 2024-10-29 04:49:00 | AQUA_M-M | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 55.7 |
| aafc2cf9-15a5-39d1-b82e-f63537d6e083 | -12.35541 | -49.92203 | 2024-10-29 04:49:00 | AQUA_M-M | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 42.7 |
| 4b8b65ba-4264-3a48-ac93-cd212b92d8d9 | -6.60371 | -47.37958 | 2024-10-29 04:49:00 | AQUA_M-M | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 58.0 |
| 6240a798-0987-38de-b0de-1f19463557dc | -6.60823 | -47.38826 | 2024-10-29 04:49:00 | AQUA_M-M | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 58.2 |
| 6e654141-825f-3029-8cee-e46e8e6381f0 | -6.51128 | -47.03493 | 2024-10-29 04:49:00 | AQUA_M-M | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 33.5 |
| 2a6aff1b-e434-3b0e-95f8-65671d6fa731 | -2.6667 | -49.246 | 2024-10-29 04:55:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 74.5 |
| f53bf05b-5fb4-31d1-be72-274c148590a3 | -2.6666 | -49.2673 | 2024-10-29 04:55:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 67.0 |
| d8f80064-546d-3c32-83e3-d13fe7211dfa | -2.8146 | -49.2206 | 2024-10-29 04:55:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 58.2 |
| 29a4265b-b374-390b-a82d-0673bab84c00 | -2.833 | -49.2413 | 2024-10-29 04:55:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 101.0 |
| d693e404-70c3-30c1-824d-3de356cb8dea | -2.8331 | -49.22 | 2024-10-29 04:55:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 56.3 |
| 2abff528-2986-3875-ac8e-6bafb2bd1bc5 | -2.8145 | -49.2418 | 2024-10-29 04:55:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 76.6 |
| f5c6a335-5617-32e2-a44f-a9bf6dfb5100 | -3.1097 | -54.2865 | 2024-10-29 04:55:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 68.4 |
| eb508593-74c1-397c-a467-b20d0181a2ad | -3.1794 | -50.3922 | 2024-10-29 04:55:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 64.5 |
| b4238f72-811d-3576-a899-657634c107c2 | -3.2503 | -46.8709 | 2024-10-29 04:55:24 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 95.9 |
| e5cc2642-1920-38b9-bc03-c57d9727de99 | -12.3522 | -49.94 | 2024-10-29 04:56:16 | GOES-16 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 72.2 |
| a427083a-d4a8-328f-bfa4-3bd18d47b244 | -12.3526 | -49.9184 | 2024-10-29 04:56:16 | GOES-16 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 91.0 |
| 9f8ad64c-09fc-3484-ad3d-c6a3174a459f | 2.36086 | -50.77407 | 2024-10-29 04:59:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8a46c985-86de-3152-b050-85b3900dda0a | 2.35827 | -50.7578 | 2024-10-29 04:59:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ac75517c-963e-3d7b-8bda-463b65d80bd1 | 3.58781 | -51.2682 | 2024-10-29 04:59:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| eeb5b141-6117-3f2f-a41a-ab3ba3a996ef | 3.58048 | -51.28874 | 2024-10-29 04:59:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 87ebf7f6-bf54-3da0-b4b2-9f23dc4b7a5e | 3.57987 | -51.28496 | 2024-10-29 04:59:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 334fb5bb-26f3-316f-a2f9-c456b0e62583 | 3.5787 | -51.28807 | 2024-10-29 04:59:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5b75a778-4304-38f2-a0f2-4d629667830b | 3.57632 | -51.27293 | 2024-10-29 04:59:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ca743b2c-b9b5-3e89-b5ce-a909ec75dfe1 | 3.57458 | -51.27417 | 2024-10-29 04:59:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8ee66c32-bfa3-3854-bab5-bc0714566863 | 3.57345 | -51.27727 | 2024-10-29 04:59:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 07f83bc0-cc1e-34d8-bf38-e4dca5a20679 | 3.57286 | -51.27348 | 2024-10-29 04:59:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 133f2a00-261a-380b-8d6e-325e7b938fee | 3.57118 | -51.28539 | 2024-10-29 04:59:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 92a379b6-d273-3cae-a49d-704d83f92dee | 3.57059 | -51.2816 | 2024-10-29 04:59:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 5d9628de-a323-3e0d-a28e-40430e58d2e5 | 3.56999 | -51.27782 | 2024-10-29 04:59:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 188b3814-47fb-392f-926b-cf9679467f46 | 3.56713 | -51.28215 | 2024-10-29 04:59:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 5.3 |
| a984c0a9-fb53-3e7d-a826-acb2f232c5ff | 3.45286 | -51.24569 | 2024-10-29 04:59:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 413fcbcf-7fe6-3768-aa94-a2e188f7b059 | 3.4518 | -51.26144 | 2024-10-29 04:59:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 3.5 |
| b0cfa73e-bd20-3aa1-a66a-5dfed51fd36a | 3.4506 | -51.25384 | 2024-10-29 04:59:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ab30c82c-a0ac-3f50-8b24-e24e6a89b073 | 3.45 | -51.25004 | 2024-10-29 04:59:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a8e457e2-e1ff-3254-ad91-8056b14105e3 | 3.44833 | -51.26199 | 2024-10-29 04:59:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 6ef38e01-89be-3b1d-8e72-4667fdeabbb3 | 3.19302 | -51.30858 | 2024-10-29 04:59:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2af24e5b-8e5e-394f-ad85-da257396a3a1 | 2.62182 | -50.9164 | 2024-10-29 04:59:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 0.3 |
| ae45e515-1eba-3ce6-8d12-e1adbf3c5bad | 2.61827 | -50.91697 | 2024-10-29 04:59:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 563ce53b-93b8-3c96-9781-18fad6997e6d | 2.51943 | -51.00062 | 2024-10-29 04:59:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b01c85a3-6a69-3a10-b88d-9593a7e71f3f | 4.09761 | -61.13128 | 2024-10-29 04:59:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 8a0d2c08-7aa3-3e42-aef6-470365fe6f4b | 4.06301 | -61.237 | 2024-10-29 04:59:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 96063d02-5cdc-3702-b7b4-8ccc04cc13f4 | 4.06121 | -61.2592 | 2024-10-29 04:59:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 44c8fa6f-5825-3dde-bebb-35eed9cf92ec | 4.06024 | -61.25251 | 2024-10-29 04:59:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 2e3173e9-7026-3bd6-8529-0277c38c96d3 | 4.05947 | -61.24723 | 2024-10-29 04:59:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 77c0e983-39a2-3aaf-bc4e-bb1ea7df2ae1 | 4.05879 | -61.2426 | 2024-10-29 04:59:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e58be1ed-9a6e-3297-90f4-d8614b31fa24 | 4.05642 | -61.26098 | 2024-10-29 04:59:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0b7eab20-2c2b-39d1-aa34-73cf3247e1be | 4.05554 | -61.25495 | 2024-10-29 04:59:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 91b02707-7823-3c25-ab2e-859770467159 | -3.84684 | -50.984 | 2024-10-29 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d6183480-07e9-37e2-a56f-fee1667a9cb7 | -6.35974 | -41.5731 | 2024-10-29 05:01:00 | NPP-375D | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 183bfb8e-6783-306e-b364-a7e4ea8a757b | -6.35156 | -41.5788 | 2024-10-29 05:01:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 82980c0f-5c51-30b1-9d57-158d85b3774c | -5.92261 | -42.85934 | 2024-10-29 05:01:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 10.1 |
| c4930d5f-fde9-3e21-a16f-860ab01d93b0 | -5.91661 | -42.85294 | 2024-10-29 05:01:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 21.4 |
| 7d76f0d4-fba0-32d9-81d5-6505570ecaac | -5.9158 | -42.85886 | 2024-10-29 05:01:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 21.4 |
| 231406b3-6b91-31c0-be8c-a7aa3ee1a33e | -5.94206 | -43.68176 | 2024-10-29 05:01:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| a90fa742-aa2a-3630-995c-8159a2f7a0c2 | -5.94167 | -43.68132 | 2024-10-29 05:01:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 92f2bb90-3397-371e-a89a-71a11c473d12 | -5.93637 | -43.67533 | 2024-10-29 05:01:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 47659c3e-b313-3a5f-8d76-831737b594c3 | -5.93565 | -43.68082 | 2024-10-29 05:01:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 00f7165b-8fe5-3ed5-b866-a05834d888ee | -5.93525 | -43.68039 | 2024-10-29 05:01:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d834d7ce-2a2e-3e6b-8791-75910a45eb15 | -5.93496 | -43.68605 | 2024-10-29 05:01:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 186b3c58-8932-3f3f-89ff-8da4c861a079 | -5.93452 | -43.68562 | 2024-10-29 05:01:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 21067c80-0169-392a-907c-b57eb6d0164b | -5.92925 | -43.67974 | 2024-10-29 05:01:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 3dee9358-2b70-353f-a2c6-c7486e96b138 | -5.92886 | -43.67933 | 2024-10-29 05:01:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ec77bb15-2865-39fb-b461-5b536084817d | -5.28666 | -43.40755 | 2024-10-29 05:01:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f84a2a73-98c6-365b-bb7a-9d6642babe63 | -5.28592 | -43.41291 | 2024-10-29 05:01:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5b9f38af-31c6-3a74-a03b-e32c6411d723 | -5.28022 | -43.40641 | 2024-10-29 05:01:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a30648b8-2fe7-3455-9b61-e2d24b7c6b39 | -5.27949 | -43.41171 | 2024-10-29 05:01:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 73c218e8-6ca1-3693-ac53-9ed7f8c00e34 | -3.07451 | -44.10826 | 2024-10-29 05:01:00 | NPP-375D | PRESIDENTE JUSCELINO | MARANHÃO | Brasil | 2109205 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| edec62d0-783f-3f28-be33-178cf3570fe6 | -3.07383 | -44.11285 | 2024-10-29 05:01:00 | NPP-375D | PRESIDENTE JUSCELINO | MARANHÃO | Brasil | 2109205 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |


[Clique aqui para ver as próximas entradas](README70.md)
