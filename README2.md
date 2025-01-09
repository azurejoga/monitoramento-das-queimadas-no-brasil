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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 283e1805-5d74-3918-b1ba-a7ffa51dad45 | -19.3057 | -53.7227 | 2025-01-09 01:20:00 | GOES-16 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 81.3 |
| 59009095-94b5-32b2-b669-240b652a0849 | -9.9279 | -36.422 | 2025-01-09 01:20:00 | GOES-16 | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | 75.5 |
| 6c92f8a3-1146-3721-adfc-456d33b69864 | -9.9081 | -36.4523 | 2025-01-09 01:20:00 | GOES-16 | JUNQUEIRO | ALAGOAS | Brasil | 2704005 | 27 | 33 | nan | nan | nan | Mata Atlântica | 94.0 |
| bbb9e8d8-1651-3ecc-8df3-a6a03364b949 | -19.3052 | -53.7443 | 2025-01-09 01:20:00 | GOES-16 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 97.7 |
| 4fff325f-f9b7-32bf-bcd0-9c3f1a0a8c81 | -19.3052 | -53.7443 | 2025-01-09 01:30:00 | GOES-16 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 162.6 |
| 7a2e0c58-db19-3ff1-a890-32fb1acc7e7e | -19.3057 | -53.7227 | 2025-01-09 01:30:00 | GOES-16 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 127.7 |
| 78f7f29d-d6b1-3b8f-a3a6-e6ca72eda061 | -10.7606 | -37.2057 | 2025-01-09 01:40:00 | GOES-16 | RIACHUELO | SERGIPE | Brasil | 2805901 | 28 | 33 | nan | nan | nan | Mata Atlântica | 81.2 |
| 113e9201-c2cf-3dab-8e49-4f6c36edaefe | -19.3253 | -53.741 | 2025-01-09 01:40:00 | GOES-16 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 76.2 |
| 88f05396-6741-335f-824e-6fb6af039dff | -19.3052 | -53.7443 | 2025-01-09 01:40:00 | GOES-16 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 168.6 |
| 2370b330-695b-35a8-9062-4d262ee88546 | -19.3057 | -53.7227 | 2025-01-09 01:40:00 | GOES-16 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 109.1 |
| e3f24ad4-3d45-33b9-86c9-024136410036 | -19.2851 | -53.7476 | 2025-01-09 01:40:00 | GOES-16 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 69.1 |
| 4a1f72fc-8f09-3705-a47b-ccc5df058e56 | -19.299 | -53.73341 | 2025-01-09 01:49:00 | TERRA_M-M | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 191.0 |
| 8ccd0f9e-4889-3d39-8dac-9dde23cba4f4 | -19.30297 | -53.75529 | 2025-01-09 01:49:00 | TERRA_M-M | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 108.6 |
| 66f51922-f493-3424-8687-8f1d7970f25a | -10.143 | -36.2491 | 2025-01-09 01:50:00 | GOES-16 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 78.7 |
| 8ce88495-0b0a-38ab-b1f2-70c0d7d1a195 | -19.3057 | -53.7227 | 2025-01-09 01:50:00 | GOES-16 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 66.7 |
| 1bbf1f2b-0b5b-302e-b70d-a0600dbd343e | -10.1424 | -36.2761 | 2025-01-09 01:50:00 | GOES-16 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 81.7 |
| 2dbf788b-c5cb-315b-b3e6-d806917c6884 | 4.1887 | -60.5159 | 2025-01-09 01:50:00 | GOES-16 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 61.2 |
| 889d9896-7bc7-3c6e-a86e-c3ce061d55b2 | -19.3052 | -53.7443 | 2025-01-09 01:50:00 | GOES-16 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 94.9 |
| 8697b701-a311-3f37-a14f-30f234da018c | 2.57325 | -60.69164 | 2025-01-09 01:53:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 6e019ec1-a71f-33dc-8442-486279921616 | 2.92729 | -61.11961 | 2025-01-09 01:53:00 | TERRA_M-M | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 7.0 |
| da192da9-d89a-3e44-bf5e-1c37e5bfc1a2 | 4.05683 | -61.16986 | 2025-01-09 01:56:00 | TERRA_M-M | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 12.7 |
| a5940718-658a-33cd-a388-935aa96b5665 | 4.18746 | -60.53436 | 2025-01-09 01:56:00 | TERRA_M-M | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 11.4 |
| a0495a95-770c-38c3-96b6-834ee4c59942 | 4.05595 | -61.17544 | 2025-01-09 01:56:00 | TERRA_M-M | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 14.4 |
| 4410806b-bfe7-36cc-aa85-0d3cef85e667 | 4.18961 | -60.5182 | 2025-01-09 01:56:00 | TERRA_M-M | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 59.2 |
| 346e4b06-faac-33df-8246-26ea49a3ed3e | -5.88183 | -35.38222 | 2025-01-09 02:55:00 | NOAA-20 | MACAÍBA | RIO GRANDE DO NORTE | Brasil | 2407104 | 24 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 708da8c8-c1bb-3b46-8314-25a8838251c6 | -5.87568 | -35.38111 | 2025-01-09 02:55:00 | NOAA-20 | MACAÍBA | RIO GRANDE DO NORTE | Brasil | 2407104 | 24 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 57870543-7faa-3f4b-971d-5a5c675b0929 | -9.39429 | -35.69169 | 2025-01-09 02:55:00 | NOAA-20 | MACEIÓ | ALAGOAS | Brasil | 2704302 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| e42f294c-7df8-30d9-8a71-e8cde49d21bb | -5.87482 | -35.38585 | 2025-01-09 02:55:00 | NOAA-20 | MACAÍBA | RIO GRANDE DO NORTE | Brasil | 2407104 | 24 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 9ee43aed-228d-3359-81e8-949f2f1bf9c3 | -5.881 | -35.38684 | 2025-01-09 02:55:00 | NOAA-20 | MACAÍBA | RIO GRANDE DO NORTE | Brasil | 2407104 | 24 | 33 | nan | nan | nan | Caatinga | 6.8 |
| fd9f329f-0d8e-34b0-a374-4924c7c88fa6 | -10.66463 | -37.01818 | 2025-01-09 02:57:00 | NOAA-20 | ROSÁRIO DO CATETE | SERGIPE | Brasil | 2806107 | 28 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 235bfea7-e2b3-3a32-a0f8-045d3d7803f6 | -10.31052 | -36.7274 | 2025-01-09 02:57:00 | NOAA-20 | NEÓPOLIS | SERGIPE | Brasil | 2804409 | 28 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 091fbf77-3590-380e-849c-33bc51ad9d2f | -10.34794 | -37.0913 | 2025-01-09 02:57:00 | NOAA-20 | AQUIDABÃ | SERGIPE | Brasil | 2800209 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 236062a8-cebd-36ad-820a-de9d7cfce4e1 | -10.66364 | -37.02325 | 2025-01-09 02:57:00 | NOAA-20 | ROSÁRIO DO CATETE | SERGIPE | Brasil | 2806107 | 28 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 3a994d67-30f2-3204-8246-7c73ed68ebfe | -10.30896 | -36.72529 | 2025-01-09 02:57:00 | NOAA-20 | NEÓPOLIS | SERGIPE | Brasil | 2804409 | 28 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 0136cfff-7563-3063-88ba-367ca0cefb10 | -9.87169 | -36.27723 | 2025-01-09 02:57:00 | NOAA-20 | CAMPO ALEGRE | ALAGOAS | Brasil | 2701407 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| bc33e132-a4ee-3bdc-b5f5-5fc65f914f74 | -9.8726 | -36.27259 | 2025-01-09 02:57:00 | NOAA-20 | CAMPO ALEGRE | ALAGOAS | Brasil | 2701407 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 006f4d74-9cf0-3a69-b572-499f57cf6abb | -9.87197 | -36.27549 | 2025-01-09 02:57:00 | NOAA-20 | CAMPO ALEGRE | ALAGOAS | Brasil | 2701407 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| ca437999-d730-3989-b3f0-f2a7f78c0eb4 | -10.35002 | -37.09037 | 2025-01-09 02:57:00 | NOAA-20 | AQUIDABÃ | SERGIPE | Brasil | 2800209 | 28 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 801bb19f-e13a-34a7-8e1c-b6ade609a25d | -10.30999 | -36.72015 | 2025-01-09 02:57:00 | NOAA-20 | NEÓPOLIS | SERGIPE | Brasil | 2804409 | 28 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| ad44e6b4-aaf7-350e-a6c0-b5a73c385702 | -10.3115 | -36.72229 | 2025-01-09 02:57:00 | NOAA-20 | NEÓPOLIS | SERGIPE | Brasil | 2804409 | 28 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 6bfd745d-eaa4-3ec2-af8e-597a4ffd3d7d | -10.35423 | -37.09282 | 2025-01-09 02:57:00 | NOAA-20 | AQUIDABÃ | SERGIPE | Brasil | 2800209 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 1187a5ed-eb6e-3642-92b1-9a77b6116416 | -10.66182 | -37.01553 | 2025-01-09 02:57:00 | NOAA-20 | ROSÁRIO DO CATETE | SERGIPE | Brasil | 2806107 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| b1bfd608-f22e-3872-bf72-e6b0ea6ca781 | -10.66083 | -37.0204 | 2025-01-09 02:57:00 | NOAA-20 | ROSÁRIO DO CATETE | SERGIPE | Brasil | 2806107 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| dd8a92a6-0161-30d8-b39e-bf8edc1a45dc | -6.76468 | -35.22053 | 2025-01-09 03:46:00 | NOAA-21 | MAMANGUAPE | PARAÍBA | Brasil | 2508901 | 25 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| a64e39ce-3fdf-302d-afa5-19f47fbfd2fd | -4.16045 | -42.02022 | 2025-01-09 03:46:00 | NOAA-21 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 63bc40d4-da12-3d35-a4c6-7edef67b28c2 | -3.85195 | -41.11488 | 2025-01-09 03:46:00 | NOAA-21 | UBAJARA | CEARÁ | Brasil | 2313609 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 6d5a91d5-b3e8-34e0-b20b-2013a5b35aed | -4.39721 | -37.84096 | 2025-01-09 03:46:00 | NOAA-21 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 98290b94-2ace-3914-88ea-a6fc04f17d11 | -5.92729 | -35.62487 | 2025-01-09 03:46:00 | NOAA-21 | SÃO PEDRO | RIO GRANDE DO NORTE | Brasil | 2412708 | 24 | 33 | nan | nan | nan | Caatinga | 1.8 |
| c2209adc-214e-322a-a0ed-8bca904161f9 | -4.39777 | -37.83738 | 2025-01-09 03:46:00 | NOAA-21 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 2.9 |
| a7b18a5b-d937-3942-ac6b-57c2c28ed15a | -5.98705 | -35.4817 | 2025-01-09 03:46:00 | NOAA-21 | MACAÍBA | RIO GRANDE DO NORTE | Brasil | 2407104 | 24 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 8d82d9ae-281d-33e8-b862-35b8d2ff1702 | -4.40496 | -42.54432 | 2025-01-09 03:46:00 | NOAA-21 | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 6a9dbffb-25a4-3b5a-8d72-be2d4e36b553 | -6.77142 | -35.19915 | 2025-01-09 03:46:00 | NOAA-21 | MAMANGUAPE | PARAÍBA | Brasil | 2508901 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 609713d7-cfe6-346a-ba78-21f51e66a94b | -5.16986 | -35.61961 | 2025-01-09 03:46:00 | NOAA-21 | TOUROS | RIO GRANDE DO NORTE | Brasil | 2414407 | 24 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 348a15a1-8b03-3d74-a93c-056acc3a0424 | -5.16959 | -37.7758 | 2025-01-09 03:46:00 | NOAA-21 | QUIXERÉ | CEARÁ | Brasil | 2311504 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 9107ee6a-a026-3a45-bd64-cf09ddf9aa69 | -5.97088 | -37.50648 | 2025-01-09 03:46:00 | NOAA-21 | JANDUÍS | RIO GRANDE DO NORTE | Brasil | 2405207 | 24 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 9951a4a1-c0f5-3f7b-8d1f-097bec2d6038 | -4.39665 | -37.84454 | 2025-01-09 03:46:00 | NOAA-21 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 929fe96b-3836-30ec-934b-854de75d6820 | -6.77482 | -35.19964 | 2025-01-09 03:46:00 | NOAA-21 | MAMANGUAPE | PARAÍBA | Brasil | 2508901 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| c5c56711-8164-330e-b1f3-6853376f6465 | -6.77198 | -35.1955 | 2025-01-09 03:46:00 | NOAA-21 | MAMANGUAPE | PARAÍBA | Brasil | 2508901 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 61c51e52-2a09-3c55-8a6d-f5ea57dbb3ce | -4.84619 | -40.04716 | 2025-01-09 03:46:00 | NOAA-21 | MONSENHOR TABOSA | CEARÁ | Brasil | 2308609 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 55a8cfdf-42ef-3786-afa8-231b7b21f412 | -4.40564 | -42.54011 | 2025-01-09 03:46:00 | NOAA-21 | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| fa72817b-4536-32ed-8b52-a68e15bc145b | -5.42586 | -40.6767 | 2025-01-09 03:46:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 2ad031dc-2188-3038-ae99-6483b42cb3fa | -4.7766 | -40.46626 | 2025-01-09 03:46:00 | NOAA-21 | TAMBORIL | CEARÁ | Brasil | 2313203 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 7dd6d4a8-5426-3db3-96f1-95569bbd2d2f | -4.39945 | -37.84865 | 2025-01-09 03:46:00 | NOAA-21 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 3.0 |
| e5b08aaa-7a08-3b03-82d9-a2e5239344a3 | -2.99495 | -40.38817 | 2025-01-09 03:46:00 | NOAA-21 | BELA CRUZ | CEARÁ | Brasil | 2302305 | 23 | 33 | nan | nan | nan | Caatinga | 2.7 |
| a01d8489-3950-3743-bda1-a52bb232a88a | -5.9742 | -37.507 | 2025-01-09 03:46:00 | NOAA-21 | JANDUÍS | RIO GRANDE DO NORTE | Brasil | 2405207 | 24 | 33 | nan | nan | nan | Caatinga | 1.5 |
| be3116c5-d2c3-362a-aea3-4e5092faa7c0 | -5.25262 | -35.58928 | 2025-01-09 03:46:00 | NOAA-21 | TOUROS | RIO GRANDE DO NORTE | Brasil | 2414407 | 24 | 33 | nan | nan | nan | Caatinga | 1.1 |
| c360e0cd-fa23-3a1b-a4ca-f300f61c0279 | -6.74762 | -35.17306 | 2025-01-09 03:46:00 | NOAA-21 | MAMANGUAPE | PARAÍBA | Brasil | 2508901 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 6a843b62-3f90-3f05-9510-36cb3bb92e49 | -4.40633 | -42.53592 | 2025-01-09 03:46:00 | NOAA-21 | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 6c976280-34cf-32a3-8f7f-290fc99319f3 | -3.04737 | -40.08455 | 2025-01-09 03:46:00 | NOAA-21 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 7ffbd28e-3098-36be-92e2-e00907d7104e | -4.33739 | -39.36213 | 2025-01-09 03:46:00 | NOAA-21 | CANINDÉ | CEARÁ | Brasil | 2302800 | 23 | 33 | nan | nan | nan | Caatinga | 6.8 |
| f21d985d-b084-360c-b304-536b39601f54 | -4.79477 | -40.54437 | 2025-01-09 03:46:00 | NOAA-21 | NOVA RUSSAS | CEARÁ | Brasil | 2309300 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| c97e082f-b737-382c-abab-c29ebf5c61d9 | -5.0066 | -37.60156 | 2025-01-09 03:46:00 | NOAA-21 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 8.3 |
| d5451f41-61ad-3fc0-89d5-81297f53c927 | -5.11993 | -37.78624 | 2025-01-09 03:46:00 | NOAA-21 | QUIXERÉ | CEARÁ | Brasil | 2311504 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 414117e9-649f-3a3d-b52e-40e7f241613b | -4.05364 | -38.79591 | 2025-01-09 03:46:00 | NOAA-21 | MARANGUAPE | CEARÁ | Brasil | 2307700 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 5c52b8db-de19-3eac-9d18-ecd9b497d305 | -6.74706 | -35.17675 | 2025-01-09 03:46:00 | NOAA-21 | MAMANGUAPE | PARAÍBA | Brasil | 2508901 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| d1ba3e5c-99cd-3c72-a496-f8ef8ca7c81b | -2.90247 | -40.38591 | 2025-01-09 03:46:00 | NOAA-21 | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 21f55b41-ea5e-3889-9b97-45689fda5563 | -6.77538 | -35.19599 | 2025-01-09 03:46:00 | NOAA-21 | MAMANGUAPE | PARAÍBA | Brasil | 2508901 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 59285ff8-e5c4-3d24-a93c-a3970d3fbd0c | -5.4251 | -40.6813 | 2025-01-09 03:46:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| e2edb831-21e2-386f-aabc-82d3d9ce7b5e | -4.66724 | -37.82848 | 2025-01-09 03:46:00 | NOAA-21 | ITAIÇABA | CEARÁ | Brasil | 2306207 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 648851ef-fecf-31ea-bde3-f84867b5fba1 | -4.16465 | -42.02092 | 2025-01-09 03:46:00 | NOAA-21 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 7bccab6d-d310-3f5c-8d31-b544429d3933 | -8.76168 | -41.0035 | 2025-01-09 03:49:00 | NOAA-21 | AFRÂNIO | PERNAMBUCO | Brasil | 2600203 | 26 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 677b0c81-cef0-3a38-80eb-deb2d9afcce3 | -8.43102 | -35.31051 | 2025-01-09 03:49:00 | NOAA-21 | ESCADA | PERNAMBUCO | Brasil | 2605202 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 75844842-a0d3-3489-ae7e-a20d88d9e91b | -10.66398 | -37.01194 | 2025-01-09 03:49:00 | NOAA-21 | ROSÁRIO DO CATETE | SERGIPE | Brasil | 2806107 | 28 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| a80d3811-e5b5-3d5f-ab73-5a8d6867f158 | -7.31282 | -39.85889 | 2025-01-09 03:49:00 | NOAA-21 | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 462e232c-57ba-334e-b0fa-b0d3642787ac | -10.63441 | -37.05027 | 2025-01-09 03:49:00 | NOAA-21 | ROSÁRIO DO CATETE | SERGIPE | Brasil | 2806107 | 28 | 33 | nan | nan | nan | Mata Atlântica | 12.9 |
| a496a511-38a5-33f9-85c6-4cd3c412b915 | -7.82057 | -35.21999 | 2025-01-09 03:49:00 | NOAA-21 | TRACUNHAÉM | PERNAMBUCO | Brasil | 2615508 | 26 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| c121c003-8b99-3c81-ae34-98dbbccdef4d | -8.5282 | -40.57532 | 2025-01-09 03:49:00 | NOAA-21 | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 1.2 |
| b5777f53-deaf-31ff-89cc-5ec6afe8ae5c | -9.04409 | -35.73236 | 2025-01-09 03:49:00 | NOAA-21 | JOAQUIM GOMES | ALAGOAS | Brasil | 2703809 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 5d494472-9e66-32ae-89d3-884d06a1e1c7 | -7.3964 | -42.78098 | 2025-01-09 03:49:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 9694cada-ec48-3430-8edd-059c9502f038 | -11.96974 | -37.8718 | 2025-01-09 03:49:00 | NOAA-21 | ESPLANADA | BAHIA | Brasil | 2910602 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 0ab33296-c9d7-307c-9c44-a3b4b0698ae0 | -10.66344 | -37.01547 | 2025-01-09 03:49:00 | NOAA-21 | ROSÁRIO DO CATETE | SERGIPE | Brasil | 2806107 | 28 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| b4b9e46a-fac4-3759-a406-647134e61f2b | -10.63789 | -37.11577 | 2025-01-09 03:49:00 | NOAA-21 | SIRIRI | SERGIPE | Brasil | 2807204 | 28 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 14eeba1f-c483-3471-97ea-7c44984d4d26 | -7.39284 | -42.77649 | 2025-01-09 03:49:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 32296c5e-db65-3652-88e5-3efd09a9fa7d | -8.65005 | -36.90973 | 2025-01-09 03:49:00 | NOAA-21 | PEDRA | PERNAMBUCO | Brasil | 2610806 | 26 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 5083b6bf-73d0-31f7-a19c-719be4153ab2 | -11.02617 | -38.13903 | 2025-01-09 03:49:00 | NOAA-21 | ITAPICURU | BAHIA | Brasil | 2916500 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 0a3fcebd-ab1a-3a35-bd00-d0195ee76d03 | -9.39771 | -35.68729 | 2025-01-09 03:49:00 | NOAA-21 | MACEIÓ | ALAGOAS | Brasil | 2704302 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 18c078d2-ed44-3d7b-ad94-cb28b1b83741 | -10.11794 | -38.35418 | 2025-01-09 03:49:00 | NOAA-21 | JEREMOABO | BAHIA | Brasil | 2918100 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 9dd90b4a-181e-3349-ae40-d97f614d7cc7 | -8.15427 | -35.331 | 2025-01-09 03:49:00 | NOAA-21 | POMBOS | PERNAMBUCO | Brasil | 2611309 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| ce89518e-3b29-33e3-ba05-c58155c95423 | -9.36362 | -35.49526 | 2025-01-09 03:49:00 | NOAA-21 | BARRA DE SANTO ANTÔNIO | ALAGOAS | Brasil | 2700508 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| bd4f837e-64b5-3415-8450-f7c78f554bbc | -11.61612 | -37.51955 | 2025-01-09 03:49:00 | NOAA-21 | JANDAÍRA | BAHIA | Brasil | 2917904 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |


[Clique aqui para ver as próximas entradas](README3.md)
