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

## Dados Diários - Página 48

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0c724f34-18e9-39ab-98a1-ec05e72fc3e3 | -6.21193 | -35.26297 | 2024-10-04 03:13:00 | NOAA-20 | ARÊS | RIO GRANDE DO NORTE | Brasil | 2401206 | 24 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| d9a9ab14-3b88-3d22-8a64-a42d1ba6570c | -6.21118 | -35.26736 | 2024-10-04 03:13:00 | NOAA-20 | ARÊS | RIO GRANDE DO NORTE | Brasil | 2401206 | 24 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 095c2f71-ebf5-364f-b257-709659c2e047 | -6.20749 | -35.26213 | 2024-10-04 03:13:00 | NOAA-20 | ARÊS | RIO GRANDE DO NORTE | Brasil | 2401206 | 24 | 33 | nan | nan | nan | Mata Atlântica | 36.6 |
| bdc50ae1-9385-3c16-9913-a37faabf23e7 | -6.20673 | -35.26652 | 2024-10-04 03:13:00 | NOAA-20 | ARÊS | RIO GRANDE DO NORTE | Brasil | 2401206 | 24 | 33 | nan | nan | nan | Mata Atlântica | 36.6 |
| 6d4e7cb1-2b71-3cbe-b348-ccb96639bb4a | -6.20598 | -35.27092 | 2024-10-04 03:13:00 | NOAA-20 | ARÊS | RIO GRANDE DO NORTE | Brasil | 2401206 | 24 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| 6aaf36b4-7bef-35c5-8e58-2d179bd9840e | -6.2038 | -35.2569 | 2024-10-04 03:13:00 | NOAA-20 | ARÊS | RIO GRANDE DO NORTE | Brasil | 2401206 | 24 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 236a32bb-805e-3bd6-aeb0-b6b5293dd480 | -6.20304 | -35.2613 | 2024-10-04 03:13:00 | NOAA-20 | ARÊS | RIO GRANDE DO NORTE | Brasil | 2401206 | 24 | 33 | nan | nan | nan | Mata Atlântica | 36.6 |
| 86b4c6bf-4e2f-3dcf-995b-616cdb534e6d | -6.20229 | -35.2657 | 2024-10-04 03:13:00 | NOAA-20 | ARÊS | RIO GRANDE DO NORTE | Brasil | 2401206 | 24 | 33 | nan | nan | nan | Mata Atlântica | 36.6 |
| 1cff232a-c6b3-3b78-af3e-c571cf8027be | -6.20153 | -35.2701 | 2024-10-04 03:13:00 | NOAA-20 | ARÊS | RIO GRANDE DO NORTE | Brasil | 2401206 | 24 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| 25cb1f9f-91e8-3ece-a451-c3d33958ae71 | -6.19859 | -35.26055 | 2024-10-04 03:13:00 | NOAA-20 | ARÊS | RIO GRANDE DO NORTE | Brasil | 2401206 | 24 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 7951eac1-d49a-3595-aed8-26f1c5f08f05 | -6.19783 | -35.26492 | 2024-10-04 03:13:00 | NOAA-20 | ARÊS | RIO GRANDE DO NORTE | Brasil | 2401206 | 24 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 9c4779e9-0f5f-3e1f-8336-2d1ff9d0475d | -4.72112 | -38.46023 | 2024-10-04 03:13:00 | NOAA-20 | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 49f26cc9-9cb8-3b9a-9707-89ffb3b3d7c5 | -4.72045 | -38.46413 | 2024-10-04 03:13:00 | NOAA-20 | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 075cc582-e8fb-36b6-b2b0-919cfc3205b9 | -5.16635 | -38.14286 | 2024-10-04 03:13:00 | NOAA-20 | LIMOEIRO DO NORTE | CEARÁ | Brasil | 2307601 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 031e5df1-190d-3ebf-9f6b-b88ab7dd2dac | -6.5198 | -41.94493 | 2024-10-04 03:15:00 | NOAA-20 | NOVO ORIENTE DO PIAUÍ | PIAUÍ | Brasil | 2206902 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 417f2a81-b73e-388f-95d4-8dbbacef8b3d | -6.51848 | -41.95196 | 2024-10-04 03:15:00 | NOAA-20 | NOVO ORIENTE DO PIAUÍ | PIAUÍ | Brasil | 2206902 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 531fb250-a34b-32e6-914c-3658413a9ba9 | -6.51795 | -41.94927 | 2024-10-04 03:15:00 | NOAA-20 | NOVO ORIENTE DO PIAUÍ | PIAUÍ | Brasil | 2206902 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 11c6d545-b434-34a1-903b-40280a326dc3 | -6.51109 | -41.94827 | 2024-10-04 03:15:00 | NOAA-20 | NOVO ORIENTE DO PIAUÍ | PIAUÍ | Brasil | 2206902 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| e96a5ed8-9cda-3414-980f-ffb48497db0e | -13.29936 | -42.31539 | 2024-10-04 03:15:00 | NOAA-20 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 12c405ab-aa6d-36eb-9cf6-55be51cbd1c3 | -13.29611 | -42.31145 | 2024-10-04 03:15:00 | NOAA-20 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 2.7 |
| b05b8038-b7b6-37a8-a327-e2ebfbba6289 | -6.83685 | -42.83252 | 2024-10-04 03:15:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 8.9 |
| 145d3875-7551-368b-b1c3-61ee0f1be908 | -6.82968 | -42.83138 | 2024-10-04 03:15:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 7.3 |
| d9133bf2-42a2-3724-9765-dab2feeb7f1b | -9.15534 | -43.16493 | 2024-10-04 03:15:00 | NOAA-20 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 093dd8dd-ecb8-36a3-95af-36818b42f41e | -9.15304 | -43.16384 | 2024-10-04 03:15:00 | NOAA-20 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 8a81f30a-ea5e-3f9e-a83f-b5d6069b3b75 | -9.15176 | -43.1702 | 2024-10-04 03:15:00 | NOAA-20 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 41498fdd-0069-3060-b02c-d64a7227348e | -9.1484 | -43.16314 | 2024-10-04 03:15:00 | NOAA-20 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| f255d8be-91e5-3f2a-93a6-9b11b2d0c5b3 | -9.14711 | -43.16973 | 2024-10-04 03:15:00 | NOAA-20 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| dbb27548-bf7f-3fb3-a7a9-9a416412fa07 | -9.14614 | -43.16193 | 2024-10-04 03:15:00 | NOAA-20 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 49543b88-110f-3ef9-b98a-5ec5e4c21ce5 | -11.10995 | -43.33858 | 2024-10-04 03:15:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 30f983cd-3e34-3e1a-b370-763b573d8792 | -11.10865 | -43.34492 | 2024-10-04 03:15:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| af3ef058-4266-3a3c-bcf5-a2ee1883ea1b | -6.8563 | -39.62215 | 2024-10-04 03:15:00 | NOAA-20 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 21.3 |
| b7eb8b9b-d552-3b3a-97e4-3cb072b94d84 | -7.03847 | -34.99847 | 2024-10-04 03:15:00 | NOAA-20 | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 26.3 |
| 8ed32fb2-184f-3313-9b1c-471ab19f5a41 | -7.03777 | -35.00258 | 2024-10-04 03:15:00 | NOAA-20 | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 26.3 |
| bbbad7f5-087a-3fac-936a-3a7bf2218179 | -7.03346 | -35.00181 | 2024-10-04 03:15:00 | NOAA-20 | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 26.3 |
| e57526bd-c420-3e95-afb7-8e5afe4972e2 | -9.33036 | -35.47194 | 2024-10-04 03:15:00 | NOAA-20 | PASSO DE CAMARAGIBE | ALAGOAS | Brasil | 2706505 | 27 | 33 | nan | nan | nan | Mata Atlântica | 8.2 |
| 6363446a-3095-3e88-b433-865592a1dbe4 | -9.32608 | -35.47112 | 2024-10-04 03:15:00 | NOAA-20 | PASSO DE CAMARAGIBE | ALAGOAS | Brasil | 2706505 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| fac6234e-38c5-3780-9117-a3c9fe4aa3e6 | -10.545 | -36.86954 | 2024-10-04 03:15:00 | NOAA-20 | JAPARATUBA | SERGIPE | Brasil | 2803302 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| f23a84f4-ed16-3655-99e8-e9ac478071fd | -10.54039 | -36.86866 | 2024-10-04 03:15:00 | NOAA-20 | JAPARATUBA | SERGIPE | Brasil | 2803302 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 70f9d597-450e-3caf-9377-524124531d26 | -9.84179 | -38.90802 | 2024-10-04 03:15:00 | NOAA-20 | JEREMOABO | BAHIA | Brasil | 2918100 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| dddc5f28-cf34-3e69-810e-d37a207cb7ad | -6.86299 | -39.61883 | 2024-10-04 03:15:00 | NOAA-20 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 9.7 |
| 33677321-7921-3ab4-9df3-a2ec37c5f394 | -6.8622 | -39.6232 | 2024-10-04 03:15:00 | NOAA-20 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 21.3 |
| 56972fab-e7fc-3218-acd3-14ae6769ad90 | -6.85712 | -39.61766 | 2024-10-04 03:15:00 | NOAA-20 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 9.7 |
| bb3ec3f7-070a-3160-8382-01b5367cd886 | -8.37964 | -40.30905 | 2024-10-04 03:15:00 | NOAA-20 | SANTA CRUZ | PERNAMBUCO | Brasil | 2612455 | 26 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 838f788f-6230-3671-899b-ccb52ed12d9c | -9.63122 | -40.61798 | 2024-10-04 03:15:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| a174afee-9c81-3d2b-adbd-83b18458e651 | -2.9014 | -50.7142 | 2024-10-04 03:15:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 47.8 |
| 42c549c0-a5aa-37d0-8268-c659ec78c68f | -3.2349 | -50.3695 | 2024-10-04 03:15:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 62.3 |
| 7b45ecb0-a65c-314d-bf3c-6de7217af6a2 | -3.2534 | -50.3689 | 2024-10-04 03:15:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 61.9 |
| ee111d86-dbf1-3e1c-ba9a-1576c34415a3 | -3.3084 | -50.451 | 2024-10-04 03:15:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 231.3 |
| 93ba01fe-b9f6-35b5-95ef-1eef42f2123c | -3.3665 | -42.3112 | 2024-10-04 03:15:25 | GOES-16 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Caatinga | 111.0 |
| ca1fff3d-5f0f-3a96-b8a1-08ec456e7982 | -3.3667 | -42.2875 | 2024-10-04 03:15:25 | GOES-16 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Caatinga | 269.8 |
| 83db0862-c8d8-33db-a323-3bb2220d9589 | -3.3854 | -42.2866 | 2024-10-04 03:15:25 | GOES-16 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 122.1 |
| fd93a57c-1025-3150-a99e-fe4bd6951dc8 | -3.2899 | -50.4725 | 2024-10-04 03:15:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 96.1 |
| b5fd5a88-8597-3804-b9cf-7d650aec22f1 | -3.2899 | -50.4516 | 2024-10-04 03:15:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 174.8 |
| 97bad74f-3869-3246-b32b-0fb92102383c | -3.29 | -50.4306 | 2024-10-04 03:15:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 50.2 |
| 74a08aeb-02c4-38d7-8609-28a8ad098fd8 | -3.3083 | -50.4719 | 2024-10-04 03:15:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 111.1 |
| 7efef707-847d-321b-967c-3cb474975367 | -3.3085 | -50.43 | 2024-10-04 03:15:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 50.2 |
| 40d1ade4-5a15-3dd9-a0e0-90e770e5926c | -4.0763 | -48.4902 | 2024-10-04 03:15:29 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 105.9 |
| 105112a3-13cf-3e4c-8e14-3280d391c660 | -4.0949 | -48.4894 | 2024-10-04 03:15:29 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 224.9 |
| 546eef9b-fd77-3ec0-ae9a-824ff3ca3187 | -4.095 | -48.4679 | 2024-10-04 03:15:29 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 104.4 |
| d30aa51d-18f1-3c6d-a7da-8744c5240856 | -4.5375 | -43.304 | 2024-10-04 03:15:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 91.7 |
| 20292cb5-d481-3880-ab0b-51e35c264b7f | -4.6684 | -45.8961 | 2024-10-04 03:15:32 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 97.6 |
| 7552ae00-8b89-3572-bb36-1fbfaf9fd272 | -4.6686 | -45.8738 | 2024-10-04 03:15:32 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 151.5 |
| 75fa4f18-0d47-3f33-af40-dc6530d93d3a | -4.687 | -45.8951 | 2024-10-04 03:15:32 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 157.4 |
| cfefe538-e409-317e-afcc-484b1e020b8a | -4.6872 | -45.8727 | 2024-10-04 03:15:32 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 261.1 |
| 00e5ecb7-66b8-3e7c-8a1a-04fd4b1b8ab1 | -5.8216 | -44.1196 | 2024-10-04 03:15:39 | GOES-16 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 66.0 |
| a2e74e3e-c759-36a1-ab89-7caf4b63034f | -6.1972 | -35.2595 | 2024-10-04 03:15:40 | GOES-16 | ARÊS | RIO GRANDE DO NORTE | Brasil | 2401206 | 24 | 33 | nan | nan | nan | Mata Atlântica | 106.7 |
| 28016fee-bee1-3c7e-b634-f959e67cd330 | -7.0391 | -34.9917 | 2024-10-04 03:15:45 | GOES-16 | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 70.2 |
| 73f17e97-a9d6-3e86-8018-4cb8df25da1a | -7.8539 | -45.3611 | 2024-10-04 03:15:50 | GOES-16 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 73.0 |
| 49c8e0cb-5be2-38ce-9d7d-7575da3b3add | -9.0851 | -50.9247 | 2024-10-04 03:15:57 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 63.9 |
| e45e71d8-d775-37f3-9289-a084825fe50f | -9.0853 | -50.9036 | 2024-10-04 03:15:57 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 167.7 |
| 7f935466-0f10-3f36-9829-9ef5741af77b | -9.0856 | -50.8825 | 2024-10-04 03:15:57 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 71.4 |
| cd8f380a-872a-3398-b110-411768eadbf1 | -9.1039 | -50.9231 | 2024-10-04 03:15:58 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 76.5 |
| fa1b20ce-9b42-3687-8025-0b4c034adc57 | -9.1041 | -50.902 | 2024-10-04 03:15:58 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 152.8 |
| fcb6c99c-77da-3d47-8821-3e0d9845398f | -9.1043 | -50.8808 | 2024-10-04 03:15:58 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 64.3 |
| 6fbddefd-3d5c-34e3-9a79-516f91d59d31 | -9.3115 | -50.8203 | 2024-10-04 03:15:59 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 91.2 |
| fc3fcc95-74e3-3239-935c-668223fc41ea | -9.3118 | -50.7991 | 2024-10-04 03:15:59 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 147.1 |
| 4e6d0867-bc9d-35dd-8531-5e97908d002b | -9.3306 | -50.7974 | 2024-10-04 03:15:59 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 143.5 |
| a6982e8f-5540-306e-b389-aadb3d26d104 | -9.7684 | -51.9139 | 2024-10-04 03:16:01 | GOES-16 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 76.8 |
| 5109c593-403d-3367-a125-bedf60251b3e | -9.7873 | -51.9122 | 2024-10-04 03:16:02 | GOES-16 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 78.9 |
| 04a89639-342f-35aa-b0fb-914c8a45df53 | -11.2566 | -60.5825 | 2024-10-04 03:16:10 | GOES-16 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 57.4 |
| f99aee50-695f-3f7b-9eef-d68b32e37d3f | -11.8242 | -56.6009 | 2024-10-04 03:16:13 | GOES-16 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 48.5 |
| 33e33ba0-c744-3ba7-afcb-a68fcadbe631 | -12.5898 | -53.1359 | 2024-10-04 03:16:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 97.8 |
| f2bb92f5-dd0b-3bfd-a537-3ad50ba0fdcd | -12.5901 | -53.115 | 2024-10-04 03:16:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 155.7 |
| 3cb32094-992a-39fa-aa19-727edd488c26 | -13.1587 | -48.6764 | 2024-10-04 03:16:20 | GOES-16 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 79.1 |
| 2268c995-57e6-335c-bc93-25cd3eab779e | -13.1166 | -51.1551 | 2024-10-04 03:16:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 127.4 |
| 4bf9955f-12e9-3913-a821-d536fbc15aa9 | -13.117 | -51.1337 | 2024-10-04 03:16:20 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 67.1 |
| 8adea6bc-23a5-3583-bd32-07e3c0d9847c | -14.6822 | -48.759 | 2024-10-04 03:16:28 | GOES-16 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 76.5 |
| c68f0024-a00e-349c-ae58-b33f06eaa7db | -16.4151 | -57.3823 | 2024-10-04 03:16:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 61.2 |
| 29597718-8125-36f8-943f-7393909be722 | -16.5935 | -57.1988 | 2024-10-04 03:16:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 98.1 |
| 7b9d5369-c72a-38f4-82ca-f6d8cb0de0ef | -16.5938 | -57.1783 | 2024-10-04 03:16:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 135.5 |
| 099e25ec-8794-34b3-8972-fc1144e11db4 | -16.613 | -57.1965 | 2024-10-04 03:16:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 124.7 |
| 2e9cc6df-8603-33e5-a7c1-8f362e6cffa8 | -16.6133 | -57.176 | 2024-10-04 03:16:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 113.9 |
| d69422b3-985b-36f2-89a6-83de28846adf | -16.6868 | -57.4741 | 2024-10-04 03:16:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 55.3 |
| ef7e49e6-01d9-3a23-bce9-2f1428372884 | -16.6871 | -57.4536 | 2024-10-04 03:16:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 58.9 |
| 971d1d43-7920-35c3-b43b-8574b434c09f | -16.7455 | -57.4674 | 2024-10-04 03:16:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 64.1 |
| d68ba9cd-1dbb-3864-a476-7b0013a03487 | -16.7647 | -57.4856 | 2024-10-04 03:16:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 55.6 |
| 55e68fde-4663-37d7-b3b3-b8bd1703083c | -16.765 | -57.4652 | 2024-10-04 03:16:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 53.9 |
| d7342653-999f-3868-8821-6027af2f6655 | -16.9087 | -55.843 | 2024-10-04 03:16:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 56.3 |
| bdbc1e2a-8b62-3cdf-bc36-e0cd4dc5fcd9 | -16.9283 | -55.8405 | 2024-10-04 03:16:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 73.1 |
| 77ce5278-d644-33bf-8424-5b027e03232c | -16.9287 | -55.8197 | 2024-10-04 03:16:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 59.7 |


[Clique aqui para ver as próximas entradas](README49.md)
