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

## Dados Diários - Página 66

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 813fcaa4-0c61-34b6-bdcf-0421921c88bf | -8.45358 | -64.13855 | 2025-09-15 06:01:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 945bc214-c516-3b59-a695-5cb356b0bb38 | -10.66677 | -68.95009 | 2025-09-15 06:01:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9eb4b0cd-7b8a-3836-beb2-0056e25a1d4c | -10.55193 | -67.74126 | 2025-09-15 06:01:00 | NOAA-21 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a77ef223-94e9-3210-8e0c-ad7419d9dcff | -12.32147 | -64.07738 | 2025-09-15 06:03:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3916a133-d2f1-3885-902a-2dace83e902f | -12.43741 | -63.8941 | 2025-09-15 06:03:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 192c7c34-7043-3368-a9ae-59949fa9602b | -15.86116 | -59.40232 | 2025-09-15 06:03:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0831c307-f119-3ec1-9842-d00177a05797 | -15.85791 | -59.39646 | 2025-09-15 06:03:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 2bbb9151-70b8-3bf6-8034-f2cc7fc93c18 | -12.41348 | -63.8908 | 2025-09-15 06:03:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 580e1600-e9d3-3327-9850-fe7db0573d53 | -12.32082 | -64.08244 | 2025-09-15 06:03:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6444a8e1-221a-3651-990f-ce42e5fe54b8 | -15.85728 | -59.40291 | 2025-09-15 06:03:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 8e201cbe-2e3b-3970-a0ed-a5a6bfbac949 | -15.86179 | -59.3954 | 2025-09-15 06:03:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5ea753fa-5a6c-3486-b48f-e6d9b3a570cb | -12.43329 | -63.88817 | 2025-09-15 06:03:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2e2f85f8-0a20-3453-8ef4-d615d5d1a73c | -12.40891 | -63.88781 | 2025-09-15 06:03:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b65300ad-4588-3d29-9ad8-3c65c77ca2e1 | -15.84347 | -59.4063 | 2025-09-15 06:03:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3eedbd83-d8ec-39de-8693-38c5ca15b866 | -12.40869 | -63.89014 | 2025-09-15 06:03:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c0514324-0472-3f0f-83ca-fca86064ade9 | -12.43395 | -63.88286 | 2025-09-15 06:03:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8e4b355a-f00e-3aa8-8d63-9b2829008e31 | -12.43874 | -63.88351 | 2025-09-15 06:03:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a11bbb7b-1c7b-3fbc-b891-43399c0614d3 | -15.84287 | -59.41254 | 2025-09-15 06:03:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d6c278a2-4b52-3ffd-8d04-1a22df941421 | -12.41369 | -63.88848 | 2025-09-15 06:03:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| da852416-4eea-3b39-882c-1f57795a1954 | -14.8028 | -51.6175 | 2025-09-15 06:20:00 | GOES-19 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 71.6 |
| c0ec99bf-2c61-307d-8a7b-0eb7e25f288e | -6.96742 | -44.5475 | 2025-09-15 06:25:00 | AQUA_M-M | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 51.0 |
| 76de2c3a-404a-3ebf-aa82-14d4a025cea5 | -8.62394 | -46.37461 | 2025-09-15 06:25:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 26.3 |
| 881484ff-58a8-3d5a-8e6a-c8688f1321e5 | -6.97518 | -44.55221 | 2025-09-15 06:25:00 | AQUA_M-M | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 39.6 |
| 5e8c09af-415a-336a-98d7-da906008d7aa | -6.40609 | -46.93164 | 2025-09-15 06:25:00 | AQUA_M-M | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 17.8 |
| d895ff7a-248c-394a-a877-09edf5ebe3ae | -3.65118 | -54.05839 | 2025-09-15 06:25:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 16.7 |
| 7ae9e8b9-4bd9-3ab4-acb6-29127c69da4a | -4.17361 | -48.56667 | 2025-09-15 06:25:00 | AQUA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 22.8 |
| d185a883-d30b-3a16-95f5-500d00697b86 | -9.00576 | -47.04799 | 2025-09-15 06:25:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 18.6 |
| 38e94d2f-975d-37f6-b068-35106aed262b | -3.65252 | -54.04956 | 2025-09-15 06:25:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 8aad55fc-3ad8-37e0-b1de-4bbe84b07a3c | -7.39834 | -49.98892 | 2025-09-15 06:25:00 | AQUA_M-M | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 7b3e1100-1e1e-3f78-a7ae-ef60083b6053 | -5.48622 | -57.09026 | 2025-09-15 06:25:00 | AQUA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 3abb57a3-57cd-3f8b-92fe-9dc98269c761 | -8.92703 | -54.44525 | 2025-09-15 06:25:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| a84840f8-8705-3f0b-885b-ed08a913dc67 | -9.73902 | -55.36559 | 2025-09-15 06:27:00 | AQUA_M-M | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 18.7 |
| 2fbd9287-ff66-39b3-ba3d-de567d6c78d1 | -15.80142 | -53.47059 | 2025-09-15 06:27:00 | AQUA_M-M | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 7f453d37-0dbd-3858-beb3-d4a272841c1a | -16.35319 | -48.96651 | 2025-09-15 06:27:00 | AQUA_M-M | ANÁPOLIS | GOIÁS | Brasil | 5201108 | 52 | 33 | nan | nan | nan | Cerrado | 56.1 |
| dad5b2ee-8a4b-3b28-9f85-97fc6b1c6aa4 | -15.83906 | -59.41288 | 2025-09-15 06:27:00 | AQUA_M-M | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 29edc65b-eb31-3759-970f-67aab863221f | -12.00325 | -46.6567 | 2025-09-15 06:27:00 | AQUA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 40.9 |
| 4a798867-a1d9-36af-967a-44bf31719e48 | -14.79674 | -51.59445 | 2025-09-15 06:27:00 | AQUA_M-M | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 7308e31e-2a80-3ff0-acd8-db6b9b1e7860 | -9.73765 | -55.37456 | 2025-09-15 06:27:00 | AQUA_M-M | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 15.7 |
| c204a441-2370-3e2b-b2ec-3febef692461 | -14.79497 | -51.60788 | 2025-09-15 06:27:00 | AQUA_M-M | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 75.2 |
| 01e33dd9-a5ef-3194-b465-4cca6228c321 | -16.67395 | -49.76586 | 2025-09-15 06:27:00 | AQUA_M-M | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 21.4 |
| d47af3e1-b87a-3d5e-8329-f04151097e4a | -15.8029 | -53.45982 | 2025-09-15 06:27:00 | AQUA_M-M | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 920e7519-f58e-3996-80c6-a87f11eb4b76 | -15.78385 | -53.45732 | 2025-09-15 06:27:00 | AQUA_M-M | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 15.4 |
| bf23b996-e375-3aab-b448-feb6bb8a2cf3 | -11.77247 | -50.429 | 2025-09-15 06:27:00 | AQUA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 6cdba791-2cfe-302b-b3b3-57ef95b0f79f | -13.18799 | -47.28331 | 2025-09-15 06:27:00 | AQUA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 42.8 |
| 62267b7f-7fbf-36bb-b8e8-666095a0a4ce | -15.09792 | -52.47764 | 2025-09-15 06:27:00 | AQUA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 24.9 |
| cacd94ac-0d06-3b99-9c1b-3deedbc32f4b | -14.63738 | -52.02775 | 2025-09-15 06:27:00 | AQUA_M-M | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 8412731a-a58e-3c1c-9a62-fc92191d86a6 | -15.78241 | -53.46793 | 2025-09-15 06:27:00 | AQUA_M-M | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 111686a6-20d2-3a75-80e8-c1389ed7293f | -13.74379 | -48.76078 | 2025-09-15 06:27:00 | AQUA_M-M | CAMPINORTE | GOIÁS | Brasil | 5204706 | 52 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 9b0d4e4f-0226-3d58-8f99-86ee83774899 | -15.85297 | -59.39082 | 2025-09-15 06:27:00 | AQUA_M-M | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 446d331a-0346-3698-aa3d-9df9825fae74 | -14.42659 | -53.36094 | 2025-09-15 06:27:00 | AQUA_M-M | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 76a5175a-aa52-3942-9f3f-172f0114291e | -13.18573 | -47.27859 | 2025-09-15 06:27:00 | AQUA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 50.8 |
| a765ed82-01ed-3c60-b269-977f30919ca1 | -16.35056 | -48.9885 | 2025-09-15 06:27:00 | AQUA_M-M | ANÁPOLIS | GOIÁS | Brasil | 5201108 | 52 | 33 | nan | nan | nan | Cerrado | 18.3 |
| 0a55d589-66b1-31bb-a7d5-30c432210170 | -13.88738 | -48.31182 | 2025-09-15 06:27:00 | AQUA_M-M | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 24.5 |
| fb695cc7-2536-31a7-8c87-8180ba17267c | -15.78663 | -52.20414 | 2025-09-15 06:27:00 | AQUA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 11.2 |
| a44b0a41-08d1-36a9-b754-acf2698c0fb6 | -14.436 | -53.3623 | 2025-09-15 06:27:00 | AQUA_M-M | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 31609859-8b8e-3ad3-90fd-2dd10ea823e7 | -13.75683 | -48.76263 | 2025-09-15 06:27:00 | AQUA_M-M | CAMPINORTE | GOIÁS | Brasil | 5204706 | 52 | 33 | nan | nan | nan | Cerrado | 19.9 |
| 8c3c0d21-5f34-36ec-be43-b8e35a2c8094 | -13.89389 | -48.30625 | 2025-09-15 06:27:00 | AQUA_M-M | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 47.4 |
| b646f4f2-6b2d-3a74-b3be-dfa5d03d4bfa | -12.9681 | -47.96817 | 2025-09-15 06:27:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 23.1 |
| 46bdce5b-9865-3a18-b9c3-e3a9217610a4 | -16.3613 | -48.97491 | 2025-09-15 06:27:00 | AQUA_M-M | ANÁPOLIS | GOIÁS | Brasil | 5201108 | 52 | 33 | nan | nan | nan | Cerrado | 69.1 |
| 9a93de62-9b5d-3799-9ac3-3e8cbf28f7c7 | -15.77913 | -53.46065 | 2025-09-15 06:27:00 | AQUA_M-M | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 69757e4e-8a57-3f27-889f-ea15b5ae9ded | -15.10793 | -52.47908 | 2025-09-15 06:27:00 | AQUA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 20.3 |
| fa24c656-980c-34e2-97f9-4c7608693092 | -12.00381 | -46.65225 | 2025-09-15 06:27:00 | AQUA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 38.8 |
| 0f62823b-476d-3f68-a7b5-d154e0531d26 | -14.51376 | -47.33863 | 2025-09-15 06:27:00 | AQUA_M-M | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 21.0 |
| 7262cddb-295a-31e4-a757-0a9d29b26192 | -20.45476 | -54.57355 | 2025-09-15 06:29:00 | AQUA_M-M | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 04d06294-8bc7-3ab5-b1d3-9085f698b3a9 | -22.50571 | -52.97203 | 2025-09-15 06:29:00 | AQUA_M-M | ROSANA | SÃO PAULO | Brasil | 3544251 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.1 |
| a8146177-2593-3393-948d-5e8499f3ea44 | -22.26884 | -56.03769 | 2025-09-15 06:29:00 | AQUA_M-M | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 4.0 |
| ca6fff80-183e-3905-a6b5-7e8c5d76b2d7 | -22.26744 | -56.0477 | 2025-09-15 06:29:00 | AQUA_M-M | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 856eba82-e47a-30fa-a61a-a10e4544c834 | -20.45621 | -54.56279 | 2025-09-15 06:29:00 | AQUA_M-M | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 00bd3c24-6695-3a20-b949-853b1e8a41c6 | -12.43212 | -63.89063 | 2025-09-15 06:29:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1ba1cbc0-7f13-35a0-96cf-1a79017057f4 | -10.21588 | -69.05116 | 2025-09-15 06:29:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 56bbee2f-7712-3c37-89bb-56a1ba4f26a2 | -10.21086 | -69.05049 | 2025-09-15 06:29:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2e97fa9a-72aa-3a94-a9fe-c61a46ab11d2 | -12.44001 | -63.88436 | 2025-09-15 06:29:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0277d453-847e-3e93-96cd-372e7f0a3b5c | -7.88782 | -63.70674 | 2025-09-15 06:29:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 75f334e5-2d70-367d-a308-458152515e6e | -8.4554 | -64.14711 | 2025-09-15 06:29:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a456deba-70dd-385e-a311-d2573453c522 | -8.45395 | -64.14123 | 2025-09-15 06:29:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e7732cb7-2837-3163-9eca-46a318f98fa7 | -8.73801 | -70.54386 | 2025-09-15 06:29:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.3 |
| ef5ede02-3bb1-3a11-92f3-17337a183332 | -8.60774 | -69.92417 | 2025-09-15 06:29:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6977e473-c109-3d9e-8e97-40b464536d97 | -7.88866 | -63.7008 | 2025-09-15 06:29:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e7c1bd8d-e5ce-3248-b21f-904197ca064b | -7.88862 | -63.70046 | 2025-09-15 06:29:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 652313e4-05d8-3cb0-aa14-7914fe4c473e | -8.45613 | -64.14125 | 2025-09-15 06:29:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| abe3a3aa-3f9f-390d-b2c7-f3ed637a6fe2 | -8.74225 | -70.53879 | 2025-09-15 06:29:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c1faccc9-55af-3dfd-9118-df4b3a15bec7 | -8.45317 | -64.1471 | 2025-09-15 06:29:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7d5a3094-b586-3578-8510-a0361a5bfba3 | -8.74307 | -70.54014 | 2025-09-15 06:29:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1d748abb-75b3-3a22-9beb-1a6b42c63a8a | -7.88783 | -63.70706 | 2025-09-15 06:29:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2d702523-4dd5-3c98-b951-aa82b70b1951 | -8.74166 | -70.5431 | 2025-09-15 06:29:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f2869702-2d4e-3a86-bef4-75fa59e07802 | -8.73863 | -70.53954 | 2025-09-15 06:29:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5538a5cc-7e36-3117-b438-0de2f7663aab | -8.73443 | -67.19419 | 2025-09-15 06:29:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 71545b73-65c2-34a7-b602-44ead25b41f2 | -14.8028 | -51.6175 | 2025-09-15 06:40:00 | GOES-19 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 82.0 |
| f12861ee-86c4-331c-8c9f-6d2dc5857408 | -10.075 | -47.1908 | 2025-09-15 07:20:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 48.2 |
| c611e82a-a213-344e-b79c-0fa81aa55821 | -13.1838 | -47.2929 | 2025-09-15 07:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 83.0 |
| 1f092419-3f36-3508-8e2b-38debf5efc5b | -13.1842 | -47.2704 | 2025-09-15 07:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 86.4 |
| 72c60bb0-af2a-3fab-8773-ca4310de2395 | -17.9864 | -46.9541 | 2025-09-15 07:50:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 65.2 |
| 81d84974-f4b6-3497-b1cc-f8194c165fcd | -13.0177 | -47.9657 | 2025-09-15 08:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 69.0 |
| 6b529e5d-9bcc-399e-b50f-48b5b1a9d2d8 | -12.9599 | -47.974 | 2025-09-15 08:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 62.9 |
| 2b374c25-c8ec-340f-a214-0a7ff5f7dc09 | -16.3758 | -48.9681 | 2025-09-15 08:30:00 | GOES-19 | ANÁPOLIS | GOIÁS | Brasil | 5201108 | 52 | 33 | nan | nan | nan | Cerrado | 88.1 |
| 9f4cbbc2-c68a-3f3c-9874-2f97d72c440d | -12.9791 | -47.9713 | 2025-09-15 08:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 67.7 |
| 2dd105b0-3d2c-3fa6-a83a-9706a6f44db8 | -12.8003 | -47.2375 | 2025-09-15 09:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 118.2 |
| e425f3ab-9b66-3603-9782-6633fde023a6 | -7.8753 | -43.5876 | 2025-09-15 09:30:00 | GOES-19 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 110.0 |
| 0a236d22-2ff8-3877-b370-7ded0535af4a | -7.8942 | -43.5857 | 2025-09-15 09:40:00 | GOES-19 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 112.0 |
| 9af9623a-e2a2-34b4-87f3-15303ce6c9ed | -7.8756 | -43.5643 | 2025-09-15 09:40:00 | GOES-19 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 144.7 |


[Clique aqui para ver as próximas entradas](README67.md)
