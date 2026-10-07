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

## Dados Diários - Página 92

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5c000706-1ffd-3495-ac01-b24650eb6a4c | -3.29114 | -54.03484 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| c9e0967f-21f9-37ef-acf0-a3fbbbe0e339 | -3.99886 | -56.25922 | 2026-10-07 05:04:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4fc9ce72-7de5-33eb-b0e3-1ad74d5031f9 | -2.77516 | -54.11353 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 3f14dac3-e276-37b9-a255-dd6dad5a166c | -2.9952 | -51.0114 | 2026-10-07 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0668bd06-5a27-3e3b-ac38-c1072fdadd61 | -5.67815 | -47.93395 | 2026-10-07 05:04:00 | NOAA-21 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 2.9 |
| fb544d17-c505-3454-89bd-16ea42460d96 | -4.30059 | -50.78745 | 2026-10-07 05:04:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2773d5de-0c37-37c7-ad06-7b39d0ea6f57 | -3.01476 | -57.73604 | 2026-10-07 05:04:00 | NOAA-21 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 821b9c2b-10a1-34b3-a559-96805074053d | -3.48736 | -57.7831 | 2026-10-07 05:04:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| eda4a048-376a-30b5-ad1c-c9886ad3bff0 | -3.04264 | -53.90205 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2e5ac836-00e4-371d-862d-01c165718e6c | -2.75239 | -49.5322 | 2026-10-07 05:04:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| acc59449-7888-3ff5-b305-f3822492564e | -4.84868 | -42.86275 | 2026-10-07 05:04:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a7c00dd9-c97b-3539-82c9-61d674a2eff7 | -3.58722 | -55.56145 | 2026-10-07 05:04:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 915717fa-a08d-3601-b088-f5691e0b6100 | -2.88753 | -54.15642 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4e66c0cc-3427-3a19-b581-76935072a55b | -3.28393 | -54.05909 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 1eae911b-97eb-3b7b-9bb4-a7bc2bacf8db | -2.77228 | -54.08798 | 2026-10-07 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| bb244ddb-0fa7-3b03-8850-90b3395f13f4 | -3.06269 | -54.1473 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 118fa832-19f5-3c4d-9b10-a595b9314f73 | -6.15277 | -51.73429 | 2026-10-07 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 67e6bf31-91e4-3932-95e2-1cd5d7b2a9be | -4.75819 | -55.66886 | 2026-10-07 05:04:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cbd62a52-11f6-34b1-86b9-e2d2ae4edc6f | -3.03484 | -53.90813 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| dfc00962-f2ab-357c-82ad-3a6c1a784d19 | -4.42167 | -55.75301 | 2026-10-07 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d144e584-939f-3e4c-ad41-28e121097d01 | -2.97712 | -54.1269 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 795826bb-2e58-32fc-996f-392b6d00a832 | -3.28783 | -54.05607 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 8662cbe2-5c6e-3993-a471-b8e96774ea8d | -2.78345 | -54.10404 | 2026-10-07 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f45a867f-10ac-3d6b-bf54-8841e28e8ac3 | -1.46859 | -54.5271 | 2026-10-07 05:04:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 28b3a846-01ca-3059-a149-d318e2f71723 | -2.85414 | -51.30128 | 2026-10-07 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b1af2a47-b63c-3ca4-8cb2-541b133f992b | -3.50953 | -59.95317 | 2026-10-07 05:04:00 | NOAA-21 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 20b5921e-6a29-3d74-a2a4-0b91ffa4337a | -2.96883 | -56.62048 | 2026-10-07 05:04:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b88888cf-cf6b-3e48-8b35-92756948d30d | -3.05814 | -54.2184 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 42ccb03d-7c5c-34ce-9e8b-e05564759e6f | -2.03405 | -57.04987 | 2026-10-07 05:04:00 | NOAA-21 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 92739454-ed66-3bbc-be3c-f48eed537a18 | -3.06093 | -54.2224 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f362cd23-6e27-39c9-813f-c3717d5bbaba | -3.0239 | -54.17726 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d68636f4-b543-3d85-b752-b88540fb3882 | -3.00472 | -57.75435 | 2026-10-07 05:04:00 | NOAA-21 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4082ea5a-27cd-3dff-a812-39864eafd805 | -5.67686 | -53.49247 | 2026-10-07 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c76e2e4f-9c90-3ef1-a5c7-17493560253c | -3.52829 | -54.63022 | 2026-10-07 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 2de7240f-8e6e-39e2-824e-44f9a0896371 | -3.52288 | -54.66486 | 2026-10-07 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 55c392a8-a367-35dc-a3ed-603b7c21c438 | -3.59052 | -55.56196 | 2026-10-07 05:04:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3086e423-2ad4-30e9-a98f-f8d4b61327f3 | -3.52813 | -52.74952 | 2026-10-07 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f11396e2-fa2c-3358-bb21-3f468b01a824 | -2.764 | -54.09746 | 2026-10-07 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 05232b01-f26b-3bfb-b22b-26b99011b5ec | -2.95011 | -54.10503 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5053dc2a-7eb8-3876-bb46-e37f288fd32a | -3.27585 | -54.1767 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 624f4758-5e2b-3bf6-8d1c-e17dab03f92a | -3.85691 | -55.99162 | 2026-10-07 05:04:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f021dbd9-27d3-3767-a05f-71d7f762835e | -3.0727 | -54.25644 | 2026-10-07 05:04:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 3bf6ec8b-df0a-309a-89e5-f9d076076745 | -3.73181 | -55.98643 | 2026-10-07 05:04:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3034bb9d-3cdd-335c-9c27-6794e8433a1a | -3.08655 | -54.255 | 2026-10-07 05:04:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 7334a237-1395-3021-b5d6-f359f949ae6f | -3.02903 | -54.51669 | 2026-10-07 05:04:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f414c63c-db22-3f76-8d06-d21069d10bd3 | -1.29045 | -54.55928 | 2026-10-07 05:04:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7a15511e-1175-3eec-8335-f4cca416da4f | -3.66368 | -57.09372 | 2026-10-07 05:04:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 89ed25e0-6b43-3e33-8598-f575c9d2fd99 | -3.29503 | -54.03181 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| ded6091a-ea58-3e38-92d0-b3b0439b020b | -4.16499 | -56.34999 | 2026-10-07 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 61faa3ff-a499-37ef-ba23-86a0f2cbcfed | -8.59784 | -67.05463 | 2026-10-07 05:06:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 78111177-d30d-301f-ab2b-45f685b47d3f | -11.62086 | -48.59745 | 2026-10-07 05:06:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a4df15d1-603e-3319-8258-a319ea551a9b | -9.47187 | -67.07081 | 2026-10-07 05:06:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 03560482-af51-39a7-82a4-a4b859e5645d | -8.23793 | -50.56669 | 2026-10-07 05:06:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 30fa8bb2-54a8-3c06-bf50-e97bad5b2f90 | -9.87229 | -44.80748 | 2026-10-07 05:06:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fe1bf6aa-75be-3c78-ad47-76162ba2536d | -9.33627 | -63.67686 | 2026-10-07 05:06:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| d727e233-6447-3ab6-8dee-e9e48770fc0d | -11.73025 | -43.64874 | 2026-10-07 05:06:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 92e7f0c8-b190-3b4c-91c9-a26c42db6909 | -11.61157 | -44.14882 | 2026-10-07 05:06:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 57f057a4-bdc1-3178-ad0f-e7ecfc974d0c | -9.19242 | -66.01564 | 2026-10-07 05:06:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0bc871bb-d202-3d61-9875-4477e91a77f7 | -11.7365 | -43.65639 | 2026-10-07 05:06:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 7f8b6e34-a97e-3527-a066-e0ca040b763f | -10.58695 | -69.24195 | 2026-10-07 05:06:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 2f0211b6-6cdb-3e19-a69e-e28de590c7a6 | -10.99097 | -45.42078 | 2026-10-07 05:06:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 62eb429d-700a-3fe9-bfe9-ab1f7cae6944 | -8.86077 | -68.77583 | 2026-10-07 05:06:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1b30e552-b385-3a5e-bd9e-f341b29462f5 | -9.60356 | -67.48112 | 2026-10-07 05:06:00 | NOAA-21 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| af14a4ae-7883-3647-a2f3-fa1791caea44 | -8.28527 | -50.26535 | 2026-10-07 05:06:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| cdf407fd-d85b-3125-8e02-a486389e0aa3 | -11.05041 | -49.5722 | 2026-10-07 05:06:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 60487e19-1543-35ed-8313-a7e15c7007c2 | -11.23528 | -45.24966 | 2026-10-07 05:06:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| be401ab4-658a-3778-af4c-094d75ad5b60 | -12.41288 | -54.36124 | 2026-10-07 05:06:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ea4dbdce-6dff-3372-9281-251adb0c026b | -10.32127 | -54.91948 | 2026-10-07 05:06:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f8725b6b-0c35-3d08-9b83-6f0be4446e7d | -9.22465 | -63.61168 | 2026-10-07 05:06:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0f3175ca-8a72-39c7-819b-13b13ddff199 | -12.47215 | -51.29044 | 2026-10-07 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 737f6efe-510e-3cf8-9321-da177000aa02 | -12.17906 | -44.72816 | 2026-10-07 05:06:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5bdb9d12-e197-361d-83c7-9a63985e24f3 | -7.75119 | -54.9436 | 2026-10-07 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 10d995d7-f8b7-3c7a-9497-38fe97347553 | -11.3722 | -46.6999 | 2026-10-07 05:06:00 | NOAA-21 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 58858995-6176-37fa-a60b-803077517682 | -11.23233 | -44.86736 | 2026-10-07 05:06:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 4fcf825e-0716-3566-a8f5-69ade34ffb5b | -8.62843 | -67.05276 | 2026-10-07 05:06:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 5ca7c9c9-1ec4-3164-81fe-48012d4a0c9a | -7.44372 | -55.57494 | 2026-10-07 05:06:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a158e640-9e84-3194-9fea-ba53110544ce | -9.44133 | -46.48317 | 2026-10-07 05:06:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 18144b68-04e3-34cd-bd2f-be552a7cc1cb | -8.5977 | -53.12616 | 2026-10-07 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c3d3005b-d114-3475-8cfd-10c5d501e2b5 | -9.10155 | -65.35715 | 2026-10-07 05:06:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2f3893cd-fd82-362f-b350-39ee4063eccc | -9.19306 | -66.01218 | 2026-10-07 05:06:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 03374ec0-501b-3277-b1bc-416f89cc081c | -9.12031 | -67.85789 | 2026-10-07 05:06:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9824e8eb-cc3e-37e5-8b34-754aa4348d42 | -10.03754 | -67.74969 | 2026-10-07 05:06:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 3f0ba8f8-cb5c-3486-a16a-b28626c3c31a | -12.19486 | -44.70646 | 2026-10-07 05:06:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| c17176f2-0dfb-3e71-8b4f-c19236a790f9 | -11.66946 | -43.62181 | 2026-10-07 05:06:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 983d0858-bcc9-3b13-890a-1bbef358f2b4 | -11.32693 | -46.67746 | 2026-10-07 05:06:00 | NOAA-21 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 8db16a1b-2d95-3311-ba24-5311d28734b1 | -9.51373 | -67.1618 | 2026-10-07 05:06:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 02a337ba-0451-3e7a-9674-b1b94af52568 | -11.72953 | -43.65545 | 2026-10-07 05:06:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 7b494da9-0cba-3839-87e3-4bde931ecb7d | -12.4839 | -51.30054 | 2026-10-07 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 19135a94-f5bc-33aa-b3cc-cd4e5d47f8cb | -10.85532 | -50.66633 | 2026-10-07 05:06:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6f5ced09-ffe8-3b77-91ab-46060264779b | -9.10781 | -65.35188 | 2026-10-07 05:06:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 83e8092e-dee6-31c7-a81d-2772d8d441df | -6.84554 | -58.59299 | 2026-10-07 05:06:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| afc0c37a-d1f6-3695-b4c4-4d1f10c08144 | -13.6364 | -44.42755 | 2026-10-07 05:06:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f8c3ee21-4d61-3033-b8f3-350602d45699 | -9.95166 | -67.19439 | 2026-10-07 05:06:00 | NOAA-21 | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cb1989ff-0b5f-3031-ad74-4e6af51d1da3 | -10.28284 | -60.54518 | 2026-10-07 05:06:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 84644cd1-ddeb-3cb6-b5dc-dad8c0d65eb8 | -13.50248 | -44.3725 | 2026-10-07 05:06:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 8d9ea0c1-aeb7-3b09-95d8-4318b33184bc | -9.14288 | -65.30398 | 2026-10-07 05:06:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e103f204-610b-37ee-ae35-63ca11ead467 | -10.59631 | -50.10886 | 2026-10-07 05:06:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 116d4269-15a3-343b-b7b4-958ff0b0b469 | -11.00211 | -45.43357 | 2026-10-07 05:06:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 50527bfd-a452-3f2e-b770-456b5d23e865 | -9.37212 | -55.97031 | 2026-10-07 05:06:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a41a1e9a-4e44-3aa9-bd1e-0f68933dfb63 | -11.23317 | -44.86731 | 2026-10-07 05:06:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 19.2 |


[Clique aqui para ver as próximas entradas](README93.md)
