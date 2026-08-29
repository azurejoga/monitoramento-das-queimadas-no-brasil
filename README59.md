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

## Dados Diários - Página 59

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| afe30d81-5f8b-35b1-ae1c-7c31a149b0ef | -7.48284 | -61.40616 | 2026-08-29 05:36:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 62e2f070-c0e8-36ad-85e8-27c6e5d4db0d | -5.88507 | -57.75833 | 2026-08-29 05:36:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 14.0 |
| a43a12b4-4eb1-3051-beeb-50ef03408bb5 | -5.89486 | -57.7513 | 2026-08-29 05:36:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 975df1dc-20be-3a8d-83d5-9320fa46bf0f | -6.82521 | -59.94879 | 2026-08-29 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 789e3dfb-7f8c-30a4-8cdb-ad7f4ba63b8f | -6.77186 | -55.66266 | 2026-08-29 05:36:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| f94e06b1-2293-3c24-81df-79d41cc2c4f2 | -6.8161 | -59.4552 | 2026-08-29 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 667a13ab-fb71-30db-898f-86e5d57a894d | -6.82891 | -59.42185 | 2026-08-29 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2fb76af7-a6ba-3fbc-990f-0b5caeebdeae | -6.20335 | -55.41268 | 2026-08-29 05:36:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cb9ccab7-8d42-3fba-8b8a-b6da2feab4c7 | -8.24092 | -54.97013 | 2026-08-29 05:36:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f10e9a9f-90dc-302d-a38c-4b5b4275449b | -6.77946 | -59.42707 | 2026-08-29 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0f183beb-5567-30ff-aba9-fee92d12c5c3 | -6.77228 | -55.66252 | 2026-08-29 05:36:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| dee8ef72-1e09-3a91-9d96-e433dfd69ea7 | -6.95528 | -59.48785 | 2026-08-29 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 098f17cd-4a95-3037-8443-b63cece70cb3 | -4.18552 | -54.57396 | 2026-08-29 05:36:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 8203620b-1376-391b-847a-e0256de3c6aa | -6.77876 | -55.68743 | 2026-08-29 05:36:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1b9fa004-b07a-30d0-b24b-1ba28bfb5ada | -6.75523 | -55.67436 | 2026-08-29 05:36:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 35aeaade-aa04-3916-af04-255ca2eb3743 | -3.16098 | -54.62624 | 2026-08-29 05:36:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5426fdbe-5832-3131-a0f1-8ea2d785df32 | -6.89037 | -59.4108 | 2026-08-29 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 56485a04-ff80-3915-a283-23e3c520ceb3 | -3.43331 | -52.77663 | 2026-08-29 05:36:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a58d381b-ea8f-365d-b609-d8b584f11aa3 | -2.75095 | -60.23668 | 2026-08-29 05:36:00 | NOAA-21 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 0f3721af-5553-3ec4-9009-1ee4774b38de | -6.79207 | -59.40104 | 2026-08-29 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0ba958f8-e990-3979-9b6a-9c9bbd986e40 | -8.24177 | -54.96387 | 2026-08-29 05:36:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 01321729-2962-3d9f-9968-885803821b03 | -6.43858 | -55.77607 | 2026-08-29 05:36:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5c7bea8f-8336-3468-a349-5b04b520feff | -6.40741 | -51.68142 | 2026-08-29 05:36:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 6cb37c66-aa9f-34a3-bce2-9d31fe4b3e07 | -6.76765 | -55.6558 | 2026-08-29 05:36:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| af670a85-cc22-3900-a7d5-8aa699173a81 | -6.76106 | -55.66938 | 2026-08-29 05:36:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 95b966c1-68a4-3729-987e-01dd3f3ad125 | -6.16553 | -57.78671 | 2026-08-29 05:36:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0d0f0e36-8f2f-36e7-a763-9ab6703581ee | -5.88877 | -57.76306 | 2026-08-29 05:36:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 14.0 |
| a43d46c6-48a1-3b93-918b-8bf3740deb67 | -3.16142 | -54.62334 | 2026-08-29 05:36:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 270f1664-728e-34f6-a145-beb8a017b82a | -4.33208 | -54.90273 | 2026-08-29 05:36:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7b8a2423-554b-3de5-8ab3-86c051f3f7fd | -5.77015 | -57.56188 | 2026-08-29 05:36:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8f5ecfaa-6b6c-3d84-a71a-798bd617d5ae | -6.1242 | -57.69032 | 2026-08-29 05:36:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2d3f0443-38fd-3516-88dd-9119f5c743df | -6.79987 | -59.40226 | 2026-08-29 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2995896b-12b0-3ab1-8318-a797ce29736b | -6.77725 | -55.66365 | 2026-08-29 05:36:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 116b38f7-0b31-3eab-b399-5510593d1f13 | -6.15635 | -57.78954 | 2026-08-29 05:36:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 06b1d5cd-2f95-30ce-91d3-ecda635de003 | -7.5007 | -55.29634 | 2026-08-29 05:36:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 39ac8a4b-122b-3541-9e64-ce0de0d65148 | -6.81292 | -59.4497 | 2026-08-29 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 31797416-4286-390f-bf23-ff726f8d7f43 | -4.14794 | -60.76351 | 2026-08-29 05:36:00 | NOAA-21 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f235ec8f-c3b1-36cd-a03a-27700bf5d09f | -6.15406 | -57.80587 | 2026-08-29 05:36:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1e9f47bb-99c2-3800-87ad-79102d4bad12 | -6.78147 | -55.66741 | 2026-08-29 05:36:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| ddd78960-0aad-3ec8-9af7-7424210f3062 | -5.89425 | -57.75549 | 2026-08-29 05:36:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| eda87cc4-b578-3a0d-ac93-c34cf85e1d93 | -6.16983 | -57.78738 | 2026-08-29 05:36:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2fdd802f-1259-368b-92c7-541f8a831154 | -6.76024 | -55.67513 | 2026-08-29 05:36:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| a371eb37-fea7-3914-aabb-668b0c4943a9 | -6.17042 | -57.78321 | 2026-08-29 05:36:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 33f20ab5-bec1-3704-b459-16298bb1971d | -5.98638 | -57.68328 | 2026-08-29 05:36:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b3607f1b-fc31-3720-9b9d-ccb0405f6ab7 | -6.77764 | -55.65781 | 2026-08-29 05:36:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 23.4 |
| 64a982c2-f0ee-3aa6-b9e4-9821fe7daa43 | -6.5427 | -55.24881 | 2026-08-29 05:36:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4fe970fe-1632-331d-ae21-3fc534b8b6f1 | -6.91567 | -59.48697 | 2026-08-29 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 9e9ad64f-85f5-300f-8940-0df8a6fc0de8 | -6.94665 | -58.95115 | 2026-08-29 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a61e6ee5-2ff9-3b5a-8213-c44899df9609 | -6.5825 | -55.43735 | 2026-08-29 05:36:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3f96d632-e127-3e60-8ca7-473bd61d8e6d | -7.367 | -55.17353 | 2026-08-29 05:36:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bdabad77-0eed-3e26-a0e8-66a14753c4a2 | -7.50986 | -55.30715 | 2026-08-29 05:36:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 3d76bde9-7e52-35cc-b949-629a7da197b2 | -6.16065 | -57.7902 | 2026-08-29 05:36:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 480cabd9-ae64-3568-bc0f-5032649bdfa5 | -6.60123 | -55.45238 | 2026-08-29 05:36:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ac9645ed-7c00-34af-99b9-c989cb528c25 | -6.78265 | -55.6587 | 2026-08-29 05:36:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 23.4 |
| eff1aa40-aa98-3ae1-8d27-968fc83dc5ef | -6.88518 | -59.44541 | 2026-08-29 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e0c76ccf-a7e5-3826-9ed0-50933e1c6be0 | -5.78019 | -57.58469 | 2026-08-29 05:36:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 14c233b8-7d4a-35f5-8baa-2d727af1fb5b | -6.77767 | -55.66072 | 2026-08-29 05:36:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 14.7 |
| f81979bd-6246-3967-b4a3-04bcac839ba8 | -5.88277 | -57.77425 | 2026-08-29 05:36:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f527b4b8-57b0-3c61-87b4-834e32933480 | -6.263 | -55.42169 | 2026-08-29 05:36:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 97fa9141-6498-34f1-9dbf-2a791032901d | -6.16671 | -57.7784 | 2026-08-29 05:36:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 05ba9a5b-d39e-336b-baa8-d1fbc59114e2 | -4.54402 | -54.92298 | 2026-08-29 05:36:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9d1cd95c-1d59-368f-95ff-3d974073e86f | -7.47696 | -61.39714 | 2026-08-29 05:36:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 802eabb1-ec34-3648-8f9c-17450961f59b | -5.98697 | -57.67913 | 2026-08-29 05:36:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5d859b8e-fa0a-3f2b-b070-ae55cefd0dfe | -6.74318 | -55.46521 | 2026-08-29 05:36:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4c0f8f51-6aed-332e-b69f-95a57a21299f | -6.15891 | -57.80251 | 2026-08-29 05:36:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b7f18d78-4f6f-311a-b2bd-4e50d0327d22 | -4.96111 | -56.27415 | 2026-08-29 05:36:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| aeef2880-c9d4-32fa-ada2-8ffdcd03ad2c | -6.16182 | -57.78189 | 2026-08-29 05:36:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d3e5eb98-6424-3618-b69e-b08d81b94b9e | -6.84476 | -59.94712 | 2026-08-29 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 38746d51-7741-34fd-9709-cbac78550129 | -6.11989 | -57.68963 | 2026-08-29 05:36:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7bf5dd9b-e5b3-30e2-b62f-d0aa856b5cf1 | -7.55554 | -61.30677 | 2026-08-29 05:36:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b958897e-cda7-3258-859e-5d94a93bb0b5 | -3.60985 | -60.54148 | 2026-08-29 05:36:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d13b06c2-3b9a-341c-bad6-803f3ac25ffb | -6.93859 | -58.95002 | 2026-08-29 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d80eef05-12d0-3844-80a0-1f7b85287068 | -5.89915 | -57.75195 | 2026-08-29 05:36:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 65abe688-6048-3ed3-9ab5-9726a3fc93c3 | -7.53115 | -61.37271 | 2026-08-29 05:36:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b671b750-9f84-3fb6-aa82-5f47bd535bbd | -6.78689 | -55.6652 | 2026-08-29 05:36:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 26.0 |
| 1129dd52-226d-3c6d-8f11-d8b396e5c150 | -6.76805 | -55.65286 | 2026-08-29 05:36:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e5814499-5a47-394b-9ca4-2768ffaf2488 | -6.82831 | -59.95404 | 2026-08-29 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| c10d33ad-9d11-39be-a47b-68a1f59cd88f | -6.22595 | -55.6171 | 2026-08-29 05:36:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 848f5c01-1f10-3c17-a44a-b5418b079528 | -3.71129 | -57.22913 | 2026-08-29 05:36:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| aa3d5394-6f24-3f0d-b010-f814f96ab2d3 | -6.78185 | -55.6646 | 2026-08-29 05:36:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 9c9926cb-4b7a-3d4e-a416-0207eca8dd72 | -3.62165 | -59.77057 | 2026-08-29 05:36:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d8e22ecb-01c5-39f1-8329-3390533e3297 | -4.34248 | -55.44193 | 2026-08-29 05:36:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 827cc4a5-73bb-3e2e-9f84-5b1514c13a25 | -6.87232 | -59.39796 | 2026-08-29 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 727d720c-eb9e-3bc3-b175-58d1cc1947d2 | -5.87788 | -57.77777 | 2026-08-29 05:36:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 3a791e46-354d-33df-8c62-b3fce63548c1 | -6.76607 | -55.66762 | 2026-08-29 05:36:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fd69d6a4-2b5c-32fd-8305-0506598e2f69 | -7.36218 | -55.1698 | 2026-08-29 05:36:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 63105967-a387-345e-8f3d-268f9b0ca083 | -6.15949 | -57.79844 | 2026-08-29 05:36:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| dfbaca49-3d51-351f-b7de-12e0d1e7ee71 | -3.37159 | -49.53668 | 2026-08-29 05:36:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 446120f6-5760-36ca-8bd8-a6794fcd14c3 | -5.29064 | -50.93735 | 2026-08-29 05:36:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 040f94dc-dcd7-3634-a009-7d0ae06ef8f6 | -5.85019 | -57.75714 | 2026-08-29 05:36:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e324ed7e-8180-3eb0-ab27-ed4db7420dc1 | -5.99011 | -57.68802 | 2026-08-29 05:36:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| d2121180-3d18-3f02-91fb-d88fc1c8cac5 | -6.76686 | -55.6617 | 2026-08-29 05:36:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| a957966a-69d6-3cc0-b99d-7ebe23bcb49f | -6.15406 | -57.78709 | 2026-08-29 05:36:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| aa7e4815-ae2b-364f-9f88-fc6c5167b7b2 | -3.20589 | -61.14333 | 2026-08-29 05:36:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 899c49ff-fa48-3f65-807e-114ef67c6d6b | -7.5107 | -55.30091 | 2026-08-29 05:36:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 018621c7-ece7-3409-b018-d9c06e97359e | -6.88573 | -59.41513 | 2026-08-29 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0fe66833-14f5-38cc-b753-f57886c304c5 | -6.54871 | -55.24333 | 2026-08-29 05:36:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 76a3cf08-0787-3923-b200-26869c68d175 | -6.8461 | -59.93789 | 2026-08-29 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 86ce8b40-e2f1-3593-82e2-c890be9d1910 | -6.76726 | -55.65875 | 2026-08-29 05:36:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 52bad597-0a5a-37c0-9043-c499b524b00b | -6.76647 | -55.66466 | 2026-08-29 05:36:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |


[Clique aqui para ver as próximas entradas](README60.md)
