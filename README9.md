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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 69b862de-5187-3e85-a3f2-b4da466f3182 | -10.6313 | -52.1891 | 2025-11-01 02:30:00 | GOES-19 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 76.7 |
| 8d2f3ecc-a848-36cf-9ba5-de2123f11bde | -11.3773 | -48.9307 | 2025-11-01 02:30:00 | GOES-19 | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 96.2 |
| fc19d66d-1d13-38d8-98b8-61a7da1c82d5 | -16.9135 | -50.4707 | 2025-11-01 02:40:00 | GOES-19 | PARAÚNA | GOIÁS | Brasil | 5216403 | 52 | 33 | nan | nan | nan | Cerrado | 92.2 |
| e987a237-011f-3cdb-8f25-b3409a350d3f | -16.9328 | -50.4894 | 2025-11-01 02:40:00 | GOES-19 | PARAÚNA | GOIÁS | Brasil | 5216403 | 52 | 33 | nan | nan | nan | Cerrado | 98.4 |
| b740839e-ba7f-335f-8e49-dc829c7b73bb | -3.2156 | -50.5795 | 2025-11-01 02:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 74.1 |
| 06ef1207-d593-31ad-9109-36d3239f5a1b | -3.234 | -50.5999 | 2025-11-01 02:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 72.2 |
| 6ea2be7a-4acd-334f-83f4-b60754e885c6 | -3.234 | -50.5789 | 2025-11-01 02:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 115.4 |
| 70e97f4e-9ed8-36ab-ad8b-1cbc8d615726 | -16.9333 | -50.4673 | 2025-11-01 02:40:00 | GOES-19 | PARAÚNA | GOIÁS | Brasil | 5216403 | 52 | 33 | nan | nan | nan | Cerrado | 97.7 |
| 568dc8ed-a987-3078-aedb-72792ae4bf26 | -16.9131 | -50.4927 | 2025-11-01 02:40:00 | GOES-19 | PARAÚNA | GOIÁS | Brasil | 5216403 | 52 | 33 | nan | nan | nan | Cerrado | 90.7 |
| 85fc3145-9d7f-3fb4-abdf-fd60aabef1df | -16.9135 | -50.4707 | 2025-11-01 02:50:00 | GOES-19 | PARAÚNA | GOIÁS | Brasil | 5216403 | 52 | 33 | nan | nan | nan | Cerrado | 94.7 |
| 9d09a8b7-aa4f-38dd-8587-316f8093ef66 | -16.9333 | -50.4673 | 2025-11-01 02:50:00 | GOES-19 | PARAÚNA | GOIÁS | Brasil | 5216403 | 52 | 33 | nan | nan | nan | Cerrado | 78.4 |
| a8a156b2-adf9-354b-8ddd-6d930a00f342 | -16.9328 | -50.4894 | 2025-11-01 02:50:00 | GOES-19 | PARAÚNA | GOIÁS | Brasil | 5216403 | 52 | 33 | nan | nan | nan | Cerrado | 85.9 |
| 2e00193c-22c0-34f3-9b91-343a5221234b | -16.9131 | -50.4927 | 2025-11-01 02:50:00 | GOES-19 | PARAÚNA | GOIÁS | Brasil | 5216403 | 52 | 33 | nan | nan | nan | Cerrado | 104.4 |
| b65c79d0-470b-3d79-9272-28c3f152f6b1 | -3.2156 | -50.5795 | 2025-11-01 02:50:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 67.9 |
| a24fd948-b16e-34cb-961c-9080964407ea | -3.234 | -50.5789 | 2025-11-01 02:50:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 130.4 |
| 43d2f9df-302b-3af1-9e5e-1cc70a7529f9 | -3.234 | -50.5999 | 2025-11-01 02:50:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 66.8 |
| bdeca319-4832-3206-9028-890e528b1869 | -6.5833 | -48.7356 | 2025-11-01 02:50:00 | GOES-19 | PIÇARRA | PARÁ | Brasil | 1505635 | 15 | 33 | nan | nan | nan | Amazônia | 46.1 |
| 77b59191-b324-324c-85ec-499806ca3f74 | -9.73776 | -36.07951 | 2025-11-01 02:58:00 | NOAA-21 | SÃO MIGUEL DOS CAMPOS | ALAGOAS | Brasil | 2708600 | 27 | 33 | nan | nan | nan | Mata Atlântica | 11.4 |
| 53eab192-8996-3879-abda-04b6b094d5f2 | -9.73921 | -36.07516 | 2025-11-01 02:58:00 | NOAA-21 | SÃO MIGUEL DOS CAMPOS | ALAGOAS | Brasil | 2708600 | 27 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| 275ffe4e-6228-32bd-a87d-440c7723dafc | -9.73082 | -36.08296 | 2025-11-01 02:58:00 | NOAA-21 | SÃO MIGUEL DOS CAMPOS | ALAGOAS | Brasil | 2708600 | 27 | 33 | nan | nan | nan | Mata Atlântica | 23.1 |
| 64512edd-1898-364d-8a51-8fadca00a06c | -9.73132 | -36.08327 | 2025-11-01 02:58:00 | NOAA-21 | SÃO MIGUEL DOS CAMPOS | ALAGOAS | Brasil | 2708600 | 27 | 33 | nan | nan | nan | Mata Atlântica | 18.2 |
| de0a1764-bdf4-366c-9124-2902c397f5cc | -10.10855 | -36.32711 | 2025-11-01 02:58:00 | NOAA-21 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 16.3 |
| f5685852-1e2f-37a1-bf5f-60bbb05582cb | -9.74437 | -36.08099 | 2025-11-01 02:58:00 | NOAA-21 | SÃO MIGUEL DOS CAMPOS | ALAGOAS | Brasil | 2708600 | 27 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| 59d9e54d-9b1a-3f60-a37c-778a94b1ed37 | -9.73224 | -36.07859 | 2025-11-01 02:58:00 | NOAA-21 | SÃO MIGUEL DOS CAMPOS | ALAGOAS | Brasil | 2708600 | 27 | 33 | nan | nan | nan | Mata Atlântica | 15.7 |
| 7da7352a-ecdc-3eda-8c8f-92444e520ecc | -9.74347 | -36.08564 | 2025-11-01 02:58:00 | NOAA-21 | SÃO MIGUEL DOS CAMPOS | ALAGOAS | Brasil | 2708600 | 27 | 33 | nan | nan | nan | Mata Atlântica | 8.8 |
| 68f0a932-8e86-3f06-837e-f988b666f601 | -9.7317 | -36.07827 | 2025-11-01 02:58:00 | NOAA-21 | SÃO MIGUEL DOS CAMPOS | ALAGOAS | Brasil | 2708600 | 27 | 33 | nan | nan | nan | Mata Atlântica | 11.4 |
| 44bc2f5a-df42-3401-b512-4cbfe7c3a6a9 | -7.97236 | -38.27868 | 2025-11-01 02:58:00 | NOAA-21 | SERRA TALHADA | PERNAMBUCO | Brasil | 2613909 | 26 | 33 | nan | nan | nan | Caatinga | 2.4 |
| ca41bf4e-afae-3610-a5b0-842d9a3e2f1e | -7.66965 | -35.02016 | 2025-11-01 02:58:00 | NOAA-21 | ITAQUITINGA | PERNAMBUCO | Brasil | 2607802 | 26 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 139a1bb0-57c5-3e49-9905-88e4270b029d | -7.96812 | -38.28127 | 2025-11-01 02:58:00 | NOAA-21 | SERRA TALHADA | PERNAMBUCO | Brasil | 2613909 | 26 | 33 | nan | nan | nan | Caatinga | 5.6 |
| e328592b-c67d-32be-b51d-6c8df7d16fde | -9.7383 | -36.07981 | 2025-11-01 02:58:00 | NOAA-21 | SÃO MIGUEL DOS CAMPOS | ALAGOAS | Brasil | 2708600 | 27 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| 97f45217-131c-36f9-a09f-80f649460aa4 | -10.10848 | -36.32943 | 2025-11-01 02:58:00 | NOAA-21 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 13.8 |
| 4d0407de-0f53-32fc-a6f4-d48f7bf8c00f | -7.67149 | -35.01962 | 2025-11-01 02:58:00 | NOAA-21 | ITAQUITINGA | PERNAMBUCO | Brasil | 2607802 | 26 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 766f1508-f9af-379b-ba79-5d8cf35a127f | -7.97091 | -38.28596 | 2025-11-01 02:58:00 | NOAA-21 | SERRA TALHADA | PERNAMBUCO | Brasil | 2613909 | 26 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 292d5c49-fcc0-3c17-b199-dc7f73e6be3f | -10.10941 | -36.32458 | 2025-11-01 02:58:00 | NOAA-21 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 8.1 |
| e2d51786-5a0a-350b-815e-8bd639dd6634 | -16.9333 | -50.4673 | 2025-11-01 03:00:00 | GOES-19 | PARAÚNA | GOIÁS | Brasil | 5216403 | 52 | 33 | nan | nan | nan | Cerrado | 98.0 |
| c8d1a436-af1b-3d20-aa10-cf37c865c80c | -6.5833 | -48.7356 | 2025-11-01 03:00:00 | GOES-19 | PIÇARRA | PARÁ | Brasil | 1505635 | 15 | 33 | nan | nan | nan | Amazônia | 58.3 |
| 1ff20d57-42cb-30dc-8c9e-0b38078e00ca | -9.7419 | -36.0772 | 2025-11-01 03:00:00 | GOES-19 | SÃO MIGUEL DOS CAMPOS | ALAGOAS | Brasil | 2708600 | 27 | 33 | nan | nan | nan | Mata Atlântica | 64.6 |
| 63b8179e-6ae3-393b-913f-a96fb2a37ec5 | -3.2156 | -50.5795 | 2025-11-01 03:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 56.2 |
| ad804fb3-45db-34af-87c9-0e2ed57dce33 | -3.234 | -50.5999 | 2025-11-01 03:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 74.6 |
| 503a6af4-ec7c-3d05-8722-1e80d10cfcd8 | -16.9131 | -50.4927 | 2025-11-01 03:00:00 | GOES-19 | PARAÚNA | GOIÁS | Brasil | 5216403 | 52 | 33 | nan | nan | nan | Cerrado | 103.2 |
| b8a4661d-ad63-3b9e-b694-a78c8c29d8c0 | -16.9135 | -50.4707 | 2025-11-01 03:00:00 | GOES-19 | PARAÚNA | GOIÁS | Brasil | 5216403 | 52 | 33 | nan | nan | nan | Cerrado | 105.8 |
| 4dfb794c-59c9-3209-9119-0908a9ed6250 | -3.234 | -50.5789 | 2025-11-01 03:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 111.6 |
| cfd8172f-0e47-3d22-aa5c-02ecf8e34988 | -16.9328 | -50.4894 | 2025-11-01 03:00:00 | GOES-19 | PARAÚNA | GOIÁS | Brasil | 5216403 | 52 | 33 | nan | nan | nan | Cerrado | 93.7 |
| ce3f9b76-f04f-3dda-929f-946502fa4cb2 | -11.3773 | -48.9307 | 2025-11-01 03:10:00 | GOES-19 | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 79.6 |
| d2d205df-87f9-349d-a685-71dbed34bc4b | -16.9131 | -50.4927 | 2025-11-01 03:10:00 | GOES-19 | PARAÚNA | GOIÁS | Brasil | 5216403 | 52 | 33 | nan | nan | nan | Cerrado | 99.7 |
| 2b0a291b-8eea-3c1e-abe1-976d9ce4f20b | -16.9328 | -50.4894 | 2025-11-01 03:10:00 | GOES-19 | PARAÚNA | GOIÁS | Brasil | 5216403 | 52 | 33 | nan | nan | nan | Cerrado | 68.2 |
| 6dc8c346-2df6-313d-9397-739b25f27101 | -9.7226 | -36.0805 | 2025-11-01 03:10:00 | GOES-19 | SÃO MIGUEL DOS CAMPOS | ALAGOAS | Brasil | 2708600 | 27 | 33 | nan | nan | nan | Mata Atlântica | 63.5 |
| 3b9dd4c5-4e08-3c34-a177-239a3bdf7a7e | -16.9135 | -50.4707 | 2025-11-01 03:10:00 | GOES-19 | PARAÚNA | GOIÁS | Brasil | 5216403 | 52 | 33 | nan | nan | nan | Cerrado | 111.5 |
| 765c8ece-8b73-31a9-8ebb-e62fff4d0743 | -11.3963 | -48.9284 | 2025-11-01 03:10:00 | GOES-19 | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 58.9 |
| d5226692-9ae0-3158-8266-82ed788fe46a | -6.5833 | -48.7356 | 2025-11-01 03:10:00 | GOES-19 | PIÇARRA | PARÁ | Brasil | 1505635 | 15 | 33 | nan | nan | nan | Amazônia | 68.2 |
| 0141f652-ae6c-3281-b28a-fb5b6c4623f2 | -3.234 | -50.5999 | 2025-11-01 03:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 72.8 |
| 0d306bce-09b9-3403-9316-0128ee87dece | -11.2607 | -45.5078 | 2025-11-01 03:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 53.6 |
| e1b1b891-fe59-3eac-abee-a8ffa732ed00 | -9.7419 | -36.0772 | 2025-11-01 03:10:00 | GOES-19 | SÃO MIGUEL DOS CAMPOS | ALAGOAS | Brasil | 2708600 | 27 | 33 | nan | nan | nan | Mata Atlântica | 112.2 |
| fa22aa11-df0b-3b5d-bb3e-266ad635cc43 | -16.9333 | -50.4673 | 2025-11-01 03:10:00 | GOES-19 | PARAÚNA | GOIÁS | Brasil | 5216403 | 52 | 33 | nan | nan | nan | Cerrado | 70.7 |
| 43772ada-014b-38db-8d53-72867a21ba7a | -3.234 | -50.5789 | 2025-11-01 03:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 106.5 |
| 2756911f-d9e7-3538-a4c4-ac7d847446bf | -16.9135 | -50.4707 | 2025-11-01 03:20:00 | GOES-19 | PARAÚNA | GOIÁS | Brasil | 5216403 | 52 | 33 | nan | nan | nan | Cerrado | 67.5 |
| 123f2276-b538-3f9b-aee0-57ceacaac924 | -6.5833 | -48.7356 | 2025-11-01 03:20:00 | GOES-19 | PIÇARRA | PARÁ | Brasil | 1505635 | 15 | 33 | nan | nan | nan | Amazônia | 61.8 |
| 5d124535-d963-34f7-9c04-481680ecbd1c | -3.234 | -50.5789 | 2025-11-01 03:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 96.7 |
| 6d3d292f-12e6-3f9e-a0c9-fb0ebf75f79e | -16.9131 | -50.4927 | 2025-11-01 03:20:00 | GOES-19 | PARAÚNA | GOIÁS | Brasil | 5216403 | 52 | 33 | nan | nan | nan | Cerrado | 59.5 |
| 974ed130-e86b-33d6-b34d-98f88b042438 | -3.234 | -50.5999 | 2025-11-01 03:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 66.0 |
| c217a88e-249d-325a-aefa-1bfc2758fa1a | -3.87345 | -38.37865 | 2025-11-01 03:25:00 | NPP-375D | AQUIRAZ | CEARÁ | Brasil | 2301000 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 8721d39d-7862-3d37-8b85-ea9c0117e0f2 | -5.48221 | -43.08738 | 2025-11-01 03:25:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 383f1b17-5c8b-37c8-968f-2ad5881e20f2 | -2.8873 | -40.493 | 2025-11-01 03:25:00 | NPP-375D | JIJOCA DE JERICOACOARA | CEARÁ | Brasil | 2307254 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| b2528e48-c2f2-331d-bdbf-af86a8e844cd | -6.32461 | -43.62361 | 2025-11-01 03:25:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 825c9138-0b87-3713-84d9-aecc752c59d9 | -5.12059 | -43.39473 | 2025-11-01 03:25:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 5afaf160-374f-3af8-a902-5fc28f03a8e3 | -5.48606 | -43.09509 | 2025-11-01 03:25:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a75438e2-48d0-3876-8636-67a7c6b3338b | -5.12147 | -43.38835 | 2025-11-01 03:25:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f2e0e872-6950-3500-a3a7-a6002410c2c6 | -5.12747 | -43.39606 | 2025-11-01 03:25:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 40bf197f-63d6-30cc-9f63-904ac915fb5b | -2.89328 | -40.49408 | 2025-11-01 03:25:00 | NPP-375D | JIJOCA DE JERICOACOARA | CEARÁ | Brasil | 2307254 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 459be62e-27cf-3baa-885a-e918ceeca390 | -3.87554 | -38.37959 | 2025-11-01 03:25:00 | NPP-375D | AQUIRAZ | CEARÁ | Brasil | 2301000 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 4c3b06a6-a7fc-356e-a0fc-de60070046f2 | -2.79924 | -43.35223 | 2025-11-01 03:25:00 | NPP-375D | PRIMEIRA CRUZ | MARANHÃO | Brasil | 2109403 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 982e8547-275c-3e71-8348-9642d9957eb9 | -5.48719 | -43.08881 | 2025-11-01 03:25:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b5cc2d64-8e8d-3265-9163-f2b6a72bf9e2 | -5.12867 | -43.38935 | 2025-11-01 03:25:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| d61d66a8-2a24-3104-bd22-ce82fb349214 | -4.4529 | -44.21521 | 2025-11-01 03:25:00 | NPP-375D | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 70fabcc3-4927-3138-8547-f67c952078c2 | -4.44561 | -44.21391 | 2025-11-01 03:25:00 | NPP-375D | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d3e484f2-de20-3c7c-9bdc-27eb719ddd0b | -2.79544 | -43.35161 | 2025-11-01 03:25:00 | NPP-375D | PRIMEIRA CRUZ | MARANHÃO | Brasil | 2109403 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 496cc27c-5d86-3752-8848-e17a2a6ff3b5 | -5.11376 | -43.39315 | 2025-11-01 03:25:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b02c2818-04c8-3196-9d59-98cb56647252 | -4.66284 | -41.96395 | 2025-11-01 03:25:00 | NPP-375D | COCAL DE TELHA | PIAUÍ | Brasil | 2202711 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 56262a2e-11e8-3104-aeeb-0924758e07d8 | -4.66192 | -41.96912 | 2025-11-01 03:25:00 | NPP-375D | COCAL DE TELHA | PIAUÍ | Brasil | 2202711 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 70b73cc7-94fb-3060-9c1b-01e2994f3dcd | -4.66205 | -41.96311 | 2025-11-01 03:25:00 | NPP-375D | COCAL DE TELHA | PIAUÍ | Brasil | 2202711 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| ff68a5d4-5b5e-3d0a-bf54-911bb771df44 | -5.83293 | -44.0657 | 2025-11-01 03:25:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 18.1 |
| 015aa220-4a53-39bf-a44c-8d47c8d1d955 | -5.16311 | -35.7336 | 2025-11-01 03:25:00 | NPP-375D | SÃO MIGUEL DO GOSTOSO | RIO GRANDE DO NORTE | Brasil | 2412559 | 24 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 57650fff-6071-31b1-8de5-2c5c1ff7ddb8 | -5.88387 | -44.52908 | 2025-11-01 03:25:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| e3b445f9-3f77-34d5-9361-33c3ed690596 | -5.12712 | -43.39629 | 2025-11-01 03:25:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 285e43d3-da48-3140-a537-ce9b2637f8c8 | -5.82956 | -44.06509 | 2025-11-01 03:25:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| d5ec9d3d-af75-3590-8293-94cfc970f823 | -5.12178 | -43.38807 | 2025-11-01 03:25:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 12e0b63c-abfc-3675-903c-5850701b2ee6 | -6.32344 | -43.62991 | 2025-11-01 03:25:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 11660131-f773-3b5c-bfba-2b69493ba3fa | -5.79833 | -40.83556 | 2025-11-01 03:25:00 | NPP-375D | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 6.3 |
| 2ecacdac-8071-334a-8189-ac59a570b93d | -5.11341 | -43.39343 | 2025-11-01 03:25:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| cd387cbc-0cd5-3391-80e7-d9ddd999e96e | -3.87297 | -38.38158 | 2025-11-01 03:25:00 | NPP-375D | AQUIRAZ | CEARÁ | Brasil | 2301000 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 3084fd5b-6b21-3f0a-baaa-df5f411d0214 | -5.12024 | -43.39499 | 2025-11-01 03:25:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9342263e-2a9a-3d13-aa00-d286b3bf4251 | -4.96156 | -40.55371 | 2025-11-01 03:25:00 | NPP-375D | TAMBORIL | CEARÁ | Brasil | 2313203 | 23 | 33 | nan | nan | nan | Caatinga | 7.3 |
| b46cf937-92b8-3b4f-a8b4-4809c72a736f | -5.12836 | -43.38961 | 2025-11-01 03:25:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| a0408cf5-3776-337d-b6c0-b1290d1eeaf6 | -3.87503 | -38.38259 | 2025-11-01 03:25:00 | NPP-375D | AQUIRAZ | CEARÁ | Brasil | 2301000 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 4e62cdb8-0468-3165-ae32-c448927054d2 | -7.02844 | -37.24421 | 2025-11-01 03:25:00 | NPP-375D | PATOS | PARAÍBA | Brasil | 2510808 | 25 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 6b821fe0-747b-3e53-becd-fcbbf1d769d8 | -5.83664 | -44.06643 | 2025-11-01 03:25:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 51295c6c-8230-3e2e-9d1f-4a62a7092c4d | -4.66116 | -41.9683 | 2025-11-01 03:25:00 | NPP-375D | COCAL DE TELHA | PIAUÍ | Brasil | 2202711 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 8a4c1787-a2f1-326d-8df5-92748d2f576a | -2.79666 | -43.34469 | 2025-11-01 03:25:00 | NPP-375D | PRIMEIRA CRUZ | MARANHÃO | Brasil | 2109403 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5dc44e65-d970-3961-9f2e-b2656250b995 | -2.79213 | -43.35096 | 2025-11-01 03:25:00 | NPP-375D | PRIMEIRA CRUZ | MARANHÃO | Brasil | 2109403 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 191e97bc-880b-37d7-8e75-960873336b35 | -5.48891 | -43.08873 | 2025-11-01 03:25:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |


[Clique aqui para ver as próximas entradas](README10.md)
