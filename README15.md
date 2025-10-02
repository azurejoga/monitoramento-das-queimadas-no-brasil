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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d48502cf-ad9f-34e5-90e5-3d20ad800fe1 | -10.8424 | -46.6289 | 2025-10-02 02:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 86.8 |
| 6bb0befc-72be-3f49-bcf5-ad1b079aaddd | -16.0413 | -50.9177 | 2025-10-02 02:40:00 | GOES-19 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 56.3 |
| ec167a06-f0df-390f-b924-cfdc1ac20819 | -6.6955 | -48.7062 | 2025-10-02 02:40:00 | GOES-19 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 55.6 |
| 6721bbd9-636c-3f4f-8604-92f60f5baa2f | -9.9563 | -43.7162 | 2025-10-02 02:40:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 84.5 |
| c85d9ec2-5cf4-3501-810e-46014620835d | -13.1743 | -47.8093 | 2025-10-02 02:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 72.9 |
| a696e167-ff91-31dd-bdc1-d484a788f8a8 | -14.3119 | -45.9736 | 2025-10-02 02:40:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 86.8 |
| cb9275f8-7af0-3bc1-bcf8-3febbac7c56e | -15.2551 | -49.2661 | 2025-10-02 02:40:00 | GOES-19 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 95.1 |
| 8c3680b9-31ef-3396-b1a5-f43a64b2785e | -14.425 | -46.1381 | 2025-10-02 02:40:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 70.7 |
| 774800ef-4f93-3c68-871a-a568a73a9605 | -7.7941 | -42.5369 | 2025-10-02 02:40:00 | GOES-19 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 72.9 |
| 56e5b065-1f81-37db-bf7d-1bc7f770c150 | -7.7563 | -42.541 | 2025-10-02 02:40:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 87.5 |
| 89878882-d977-3d16-a0f0-8396eeaaac21 | -15.2547 | -49.2883 | 2025-10-02 02:40:00 | GOES-19 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 83.0 |
| 1f7e8186-3a5d-350d-9d24-919bf63ed64a | -14.426 | -46.0919 | 2025-10-02 02:40:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 96.3 |
| 4cfc51fb-9c5d-33d3-a154-8b16e083410a | -14.3114 | -45.9967 | 2025-10-02 02:50:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 90.0 |
| 62e695b2-0fbb-3283-8b26-02636c96da40 | -14.3119 | -45.9736 | 2025-10-02 02:50:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 60.7 |
| 59b71d72-ec10-3c29-9f43-d9c824e3929a | -13.8156 | -47.5332 | 2025-10-02 02:50:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 81.1 |
| 651ac5a3-eb24-35d9-9948-e038c727058b | -7.7563 | -42.541 | 2025-10-02 02:50:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 72.7 |
| 4e198f47-4881-334c-8ba0-6793c5b3dfa0 | -13.1743 | -47.8093 | 2025-10-02 02:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 70.1 |
| 0b92d661-d310-3da3-ad9a-d52dc648d0bf | -9.9361 | -43.7891 | 2025-10-02 02:50:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 85.1 |
| fdcba57d-1e0a-3ae3-903e-b5d5d2a115ba | -12.4737 | -47.2621 | 2025-10-02 02:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 56.5 |
| 4a7316a2-cc27-3969-b721-1a55dd7111dc | -14.4255 | -46.115 | 2025-10-02 02:50:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 81.6 |
| 3239f6ea-a1ad-3c4a-a335-3bb2f1db68a1 | -7.7755 | -42.5152 | 2025-10-02 02:50:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 77.3 |
| 81111e1c-82c3-33fc-bc0b-6f61216a6141 | -15.2551 | -49.2661 | 2025-10-02 02:50:00 | GOES-19 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 88.3 |
| 74c49878-ba03-3282-bc77-b6f648cb4fba | -6.6955 | -48.7062 | 2025-10-02 02:50:00 | GOES-19 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 66.8 |
| f007920e-f36c-3c81-8d3d-dff74892b7ae | -6.6953 | -48.7277 | 2025-10-02 02:50:00 | GOES-19 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 41.5 |
| 452163f3-3f26-3537-a724-5e3aeeee6fb8 | -15.2547 | -49.2883 | 2025-10-02 02:50:00 | GOES-19 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 85.4 |
| 28bdf578-521d-36c3-ab0c-f588415951e8 | -7.7752 | -42.539 | 2025-10-02 02:50:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 187.2 |
| 59289a08-409b-321b-b330-dc1a6dad76ee | -14.3114 | -45.9967 | 2025-10-02 03:00:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 123.9 |
| 78bd66f4-d696-3212-af8d-e1d457b234d6 | -7.7752 | -42.539 | 2025-10-02 03:00:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 135.6 |
| b797f866-4e22-3b95-a440-53b313b1cedc | -14.3119 | -45.9736 | 2025-10-02 03:00:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 76.3 |
| 54fc7f02-977e-3446-8cd5-12c7142887d6 | -6.7213 | -44.1387 | 2025-10-02 03:00:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 67.3 |
| 19ec936f-cfe5-36ed-ae3c-8c55b2032a01 | -15.2738 | -49.3073 | 2025-10-02 03:00:00 | GOES-19 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 49.3 |
| a0fc3018-6fff-319d-a1a3-9fab5ca803f4 | -6.6955 | -48.7062 | 2025-10-02 03:00:00 | GOES-19 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 79.3 |
| a763273c-5aa7-333d-9b4c-ea13cffec3c4 | -14.4255 | -46.115 | 2025-10-02 03:00:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 77.1 |
| b9d6c2d3-b280-3355-803e-0b2e9e427556 | -7.7755 | -42.5152 | 2025-10-02 03:00:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 86.7 |
| 29bf61d1-6cf1-3dc7-a492-355cf4d9970f | -10.2031 | -50.2681 | 2025-10-02 03:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 50.6 |
| 76f895a6-4cc9-3f76-b9e0-cb6a73d7bc1d | -6.7213 | -44.1387 | 2025-10-02 03:10:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 69.2 |
| 0cf50e74-4e34-3e80-9309-2d918503fa37 | -5.3193 | -43.7636 | 2025-10-02 03:10:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 90.8 |
| 01ff2304-fcb5-3c17-975b-e30aa05ceeeb | -14.3114 | -45.9967 | 2025-10-02 03:10:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 81.4 |
| dd2c188d-0560-3496-ab34-31be1f756595 | -7.7752 | -42.539 | 2025-10-02 03:10:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 142.5 |
| 4da0f719-5932-336b-90f9-ab7a90bfb199 | -6.6955 | -48.7062 | 2025-10-02 03:10:00 | GOES-19 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 70.0 |
| 5b033066-1bb3-3e37-bbc0-697b64083853 | -7.7755 | -42.5152 | 2025-10-02 03:10:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 80.8 |
| 777325fa-cebe-3733-aae9-14703b2a535c | -10.8234 | -46.6313 | 2025-10-02 03:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 57.6 |
| 34c30b2a-0dd6-3ff5-ac12-b624575f49b0 | -13.1743 | -47.8093 | 2025-10-02 03:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 82.8 |
| a00b9566-15d2-32e6-8634-25a568896fb1 | -11.175 | -47.2581 | 2025-10-02 03:10:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 61.0 |
| b884f8a7-d119-356a-ab32-cb4c57c72c30 | -5.3382 | -43.7391 | 2025-10-02 03:10:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 53.7 |
| 53d70e51-76fc-345f-8301-d3eb089ddcea | -14.3119 | -45.9736 | 2025-10-02 03:10:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 57.8 |
| 9089bba9-70c0-3632-b573-59bc4868dc02 | -11.1746 | -47.2805 | 2025-10-02 03:10:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 76.6 |
| 3255751e-d3cb-3258-b83f-8c708d59cec8 | -5.3379 | -43.7855 | 2025-10-02 03:10:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 38.0 |
| 79b6d589-0235-3606-88a3-fda53f4ce702 | -9.9361 | -43.7891 | 2025-10-02 03:10:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 116.1 |
| 3041053d-889d-3692-9e2f-4226b54d72ca | -5.338 | -43.7623 | 2025-10-02 03:10:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 177.4 |
| 4a5dae20-a82b-3754-b898-863403f1d614 | -10.2767 | -36.34215 | 2025-10-02 03:10:00 | NOAA-20 | FELIZ DESERTO | ALAGOAS | Brasil | 2702702 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| cff314ab-10f5-3abf-aced-bed83a49f106 | -5.39617 | -37.70422 | 2025-10-02 03:10:00 | NOAA-20 | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 26ce0715-f52e-3567-896d-f52d1a0093be | -5.65466 | -38.31276 | 2025-10-02 03:10:00 | NOAA-20 | IRACEMA | CEARÁ | Brasil | 2306009 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 17a35587-c820-32eb-8aa5-0073f26bb7f7 | -10.28168 | -36.34312 | 2025-10-02 03:10:00 | NOAA-20 | FELIZ DESERTO | ALAGOAS | Brasil | 2702702 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 1787548c-5e88-3219-a1cc-5c48b0ed268b | -10.28247 | -36.3388 | 2025-10-02 03:10:00 | NOAA-20 | FELIZ DESERTO | ALAGOAS | Brasil | 2702702 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| c53d16e0-a672-35c1-a165-667ccd7dc6d4 | -5.3895 | -37.70742 | 2025-10-02 03:10:00 | NOAA-20 | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 46038702-dff0-3045-b42d-46672357c5bc | -15.17089 | -43.6283 | 2025-10-02 03:13:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 17.0 |
| e1d683ec-e063-3d73-9c77-b0a9f0991477 | -15.74434 | -43.6866 | 2025-10-02 03:13:00 | NOAA-20 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 37803866-d1b0-3848-9e8b-8b926e44bbe3 | -15.73729 | -43.68501 | 2025-10-02 03:13:00 | NOAA-20 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8b8e96a6-2e93-35b0-8431-c95ad0abfbec | -15.94519 | -43.33059 | 2025-10-02 03:13:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 028d31b8-2d08-3eb1-bf82-fd7f299d8041 | -15.82048 | -41.89831 | 2025-10-02 03:13:00 | NOAA-20 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3811fb1a-f555-3b23-aa38-03e4b2768b3e | -15.81408 | -41.89698 | 2025-10-02 03:13:00 | NOAA-20 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9ca558a6-8dc0-33ae-b862-5d6f3e835fe0 | -15.78728 | -43.74351 | 2025-10-02 03:13:00 | NOAA-20 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| a02522fb-c6d7-35f2-a38d-ba136b02b45b | -15.93833 | -43.32889 | 2025-10-02 03:13:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| faff818e-a0f2-3e9d-8d69-08118839502f | -15.93691 | -43.33971 | 2025-10-02 03:13:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b7826358-2811-3a33-9048-ab815e6b9235 | -15.9353 | -43.34695 | 2025-10-02 03:13:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1506a1ad-7e4c-359c-93fb-8c7133bcae48 | -15.94311 | -43.31181 | 2025-10-02 03:13:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e7216a97-d3c6-3640-9ce7-1f754258ec10 | -15.79163 | -43.74017 | 2025-10-02 03:13:00 | NOAA-20 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 6.9 |
| dd949012-ad62-3c65-bd1c-43be3da9e3fd | -15.94204 | -43.34435 | 2025-10-02 03:13:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 22645d0c-39c4-35d4-821a-83805bd100e1 | -15.81471 | -41.89843 | 2025-10-02 03:13:00 | NOAA-20 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 42d69391-1d47-3433-9fcf-fcb86a9473d6 | -15.74085 | -43.6871 | 2025-10-02 03:13:00 | NOAA-20 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a8c75bc5-3f5e-3425-82c6-a32600ffb7fd | -15.94363 | -43.33739 | 2025-10-02 03:13:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 53445130-9787-3e64-a356-47e812aa1657 | -15.94152 | -43.31495 | 2025-10-02 03:13:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 75c5b8c3-3cfe-31fb-879c-66a89b664923 | -15.94325 | -43.30739 | 2025-10-02 03:13:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a4d491eb-db8b-30fc-89ec-cfb91a5035c1 | -15.93518 | -43.34262 | 2025-10-02 03:13:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 4.7 |
| e650cfd9-4230-3c87-b451-2d5c67735d76 | -15.92834 | -43.34082 | 2025-10-02 03:13:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d99eb414-c1aa-30b3-b3b2-6e5af2dbe188 | -15.16777 | -43.62852 | 2025-10-02 03:13:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 12.7 |
| 352c8cd9-80c2-31e0-af4f-72c1d17cf39a | -16.86996 | -40.60157 | 2025-10-02 03:13:00 | NOAA-20 | SANTA HELENA DE MINAS | MINAS GERAIS | Brasil | 3157658 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 35b0ae09-ef24-3c6d-ad71-3d851be3c075 | -15.78891 | -43.73639 | 2025-10-02 03:13:00 | NOAA-20 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| ecd45d0e-ad5d-370a-80c6-2659f34bb419 | -15.94149 | -43.31911 | 2025-10-02 03:13:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9c5ba398-dfc0-31fd-886f-35fef7e66beb | -15.74249 | -43.67999 | 2025-10-02 03:13:00 | NOAA-20 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| be23f4a1-4cdd-3aaf-886d-4bd52ed63111 | -21.57635 | -44.96657 | 2025-10-02 03:15:00 | NOAA-20 | LUMINÁRIAS | MINAS GERAIS | Brasil | 3138708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 3a4cbe05-595e-3a93-9168-290d01009dee | -19.67372 | -43.88252 | 2025-10-02 03:15:00 | NOAA-20 | LAGOA SANTA | MINAS GERAIS | Brasil | 3137601 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 948e5c73-354e-379c-8a73-e4a8f217f405 | -18.34127 | -44.51359 | 2025-10-02 03:15:00 | NOAA-20 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 69513253-4a32-3037-aac2-c2766e8ef745 | -21.57785 | -44.96049 | 2025-10-02 03:15:00 | NOAA-20 | LUMINÁRIAS | MINAS GERAIS | Brasil | 3138708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 884d7022-ea67-3283-baa8-ee8e78894059 | -19.57451 | -41.90408 | 2025-10-02 03:15:00 | NOAA-20 | IMBÉ DE MINAS | MINAS GERAIS | Brasil | 3130556 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| 6a44a614-d137-301d-8752-82ef5654bdf1 | -20.23022 | -43.91062 | 2025-10-02 03:15:00 | NOAA-20 | ITABIRITO | MINAS GERAIS | Brasil | 3131901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 60d24246-777a-3617-9368-2c45f00e89ae | -20.21688 | -44.18753 | 2025-10-02 03:15:00 | NOAA-20 | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 43c4a761-edd9-3629-aa00-cd48c605a1fb | -18.58817 | -43.0409 | 2025-10-02 03:15:00 | NOAA-20 | SABINÓPOLIS | MINAS GERAIS | Brasil | 3156809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| ea2682e7-c0f3-3031-8b6e-8e941cab61ee | -19.9563 | -43.66204 | 2025-10-02 03:15:00 | NOAA-20 | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| cff7c99d-4aea-351c-829c-005674f60a0b | -19.28887 | -43.74858 | 2025-10-02 03:15:00 | NOAA-20 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7d2dba70-7304-3f17-925e-6f6a94584a0a | -18.50021 | -44.05284 | 2025-10-02 03:15:00 | NOAA-20 | SANTO HIPÓLITO | MINAS GERAIS | Brasil | 3160603 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 1545bc53-0413-3cd1-a95a-ecb69c9a0720 | -22.52515 | -44.79163 | 2025-10-02 03:15:00 | NOAA-20 | QUELUZ | SÃO PAULO | Brasil | 3541901 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 733da362-c906-3042-8ab4-13e424aa8657 | -18.50414 | -44.03627 | 2025-10-02 03:15:00 | NOAA-20 | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 5.3 |
| dd84529e-0b58-38ad-b221-e3ed417b6e4e | -18.33796 | -44.51416 | 2025-10-02 03:15:00 | NOAA-20 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 968475c0-4b7e-38e2-a034-eb111638d4cc | -18.46491 | -40.57318 | 2025-10-02 03:15:00 | NOAA-20 | ECOPORANGA | ESPÍRITO SANTO | Brasil | 3202108 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| a5d5e166-80eb-363e-889c-483acfb96e53 | -19.95128 | -43.65405 | 2025-10-02 03:15:00 | NOAA-20 | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 1afbff89-1897-3f76-8885-dc19baf07f30 | -18.34665 | -44.50901 | 2025-10-02 03:15:00 | NOAA-20 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6ae2cbd6-580e-30d2-a7af-d1257c36192d | -19.45716 | -44.28061 | 2025-10-02 03:15:00 | NOAA-20 | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| efb79bcc-7bf8-3a3e-83eb-9d2d61a1426d | -22.07979 | -43.0875 | 2025-10-02 03:15:00 | NOAA-20 | CHIADOR | MINAS GERAIS | Brasil | 3116209 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |


[Clique aqui para ver as próximas entradas](README16.md)
