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

## Dados Diários - Página 57

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9edd5e22-db8b-32da-9b9a-3c9d32724c7e | -2.87419 | -50.73834 | 2025-10-19 05:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5c6da38e-2a60-376e-8582-059a889973ab | -9.71646 | -67.47487 | 2025-10-19 05:23:00 | NOAA-21 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f280d32d-84dc-3968-b5dd-0acb1c9d6067 | -3.89511 | -52.40588 | 2025-10-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 84bcf733-3f39-3db1-b056-d67eb6764afd | -3.64297 | -49.96647 | 2025-10-19 05:23:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 97b7c1ba-9cd5-35c5-a1f5-390bafe9b62e | -2.65493 | -49.52101 | 2025-10-19 05:23:00 | NOAA-21 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 69086769-be90-32b6-8b2a-5d57303edc28 | -9.22472 | -61.82641 | 2025-10-19 05:23:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d46ad66a-f6f5-36eb-ac95-3325879de2da | -3.09842 | -51.29492 | 2025-10-19 05:23:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a559f28f-ae78-3b05-8e6f-8ea77d4ed276 | -3.39684 | -54.06249 | 2025-10-19 05:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b45bd4c3-25fe-30aa-b510-1cb0426b94f0 | -2.6885 | -49.54442 | 2025-10-19 05:23:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 211863ef-49a5-3a7a-a3f2-752e59c229fd | -9.64055 | -65.25792 | 2025-10-19 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 8e2a0da8-32f0-3dac-87c4-33ec61fc7db1 | -4.58578 | -46.30043 | 2025-10-19 05:23:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d4b65b44-d4fb-3011-86cd-d7eac00f671f | -10.17942 | -62.92903 | 2025-10-19 05:23:00 | NOAA-21 | CACAULÂNDIA | RONDÔNIA | Brasil | 1100601 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1127a5dd-eafc-347f-9f2d-6c7c2ba56076 | -9.65157 | -64.10503 | 2025-10-19 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 724edb57-ed28-3957-88be-67bef65f4047 | -1.77521 | -55.44677 | 2025-10-19 05:23:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 66443b5f-b31a-34c5-979a-3dc610822c7f | -4.96607 | -56.26315 | 2025-10-19 05:23:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| da8ebb71-eda9-3ceb-8f57-d3b0ab359d2a | -5.09069 | -60.2188 | 2025-10-19 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b9534f03-09b1-34f6-b2e4-b8063d753ddc | -2.25767 | -51.91312 | 2025-10-19 05:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| c88d6365-0d1c-3ad6-9b55-dee7fb51426e | -8.20858 | -43.94801 | 2025-10-19 05:23:00 | AQUA_M-M | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 18.8 |
| 1107e0b0-ef73-34b5-9ac5-8c5f2bdc2565 | -4.25387 | -48.56766 | 2025-10-19 05:23:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c3416dc8-c3a9-3776-aa11-4d57d5812230 | -6.67639 | -58.74387 | 2025-10-19 05:23:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 43197649-2ddd-3bff-8e64-c3c06e0f50d4 | -2.68737 | -49.55219 | 2025-10-19 05:23:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| bc2c6c31-3511-3ba9-8409-d1767547eca7 | -12.45312 | -45.42517 | 2025-10-19 05:23:00 | AQUA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 26.5 |
| 74119182-9408-34c1-bc23-c19fe0d384cf | -6.93013 | -59.28309 | 2025-10-19 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 741236b8-139b-3ecf-b1fe-66241101daea | -6.63358 | -60.01392 | 2025-10-19 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b43e87e5-d280-3818-9897-f0ad473829be | -3.40107 | -54.06309 | 2025-10-19 05:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| af8f8be0-a7c6-30ff-a5f9-8328a626c36f | -3.64803 | -49.9711 | 2025-10-19 05:23:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 12369f4b-ae60-3cb8-8896-7d348c49b219 | -11.2655 | -60.89504 | 2025-10-19 05:23:00 | NOAA-21 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cd19d5eb-d74f-31eb-a296-b7be2ea2b9af | -9.20333 | -67.89802 | 2025-10-19 05:23:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e6885729-6d0b-3fd4-ad6b-446cb219aaf8 | -2.81683 | -54.38492 | 2025-10-19 05:23:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 36c87ba2-4dac-3c93-9b2b-88e1440be050 | -9.85474 | -68.11217 | 2025-10-19 05:23:00 | NOAA-21 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f55fa49b-8907-3791-a913-667b01309a97 | -6.67978 | -58.7444 | 2025-10-19 05:23:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0260e637-d8ec-34a8-9846-eaa0803629c9 | -4.29347 | -49.66551 | 2025-10-19 05:23:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4553b5c5-38ec-303b-8429-df78edc402fb | -4.40988 | -49.76376 | 2025-10-19 05:23:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c4416f6e-9f87-3a87-bc51-f001526be161 | -9.22693 | -46.07538 | 2025-10-19 05:23:00 | AQUA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 20.3 |
| 069ce68c-a990-3926-bfdc-704547f0777f | -9.22416 | -61.82991 | 2025-10-19 05:23:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 7.9 |
| d10f680d-105e-3bda-8562-55aa375d8fcf | -9.5588 | -66.6466 | 2025-10-19 05:23:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 40c55f89-5aed-339b-aa3d-78bfac05c883 | -6.3703 | -45.748 | 2025-10-19 05:23:00 | AQUA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 26.4 |
| 9f2e6cc2-8a54-39f4-8d58-e04b4ddd305b | -2.52048 | -51.92823 | 2025-10-19 05:23:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d9d01409-a7f9-3d5d-8f2a-b4cb699eff58 | -5.36203 | -47.21451 | 2025-10-19 05:23:00 | NOAA-21 | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Amazônia | 15.6 |
| fb9255b5-dd0e-3b5a-b3a6-7ab0b19935ce | -6.92733 | -59.279 | 2025-10-19 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| eab04a69-6cc4-3382-b902-132d47c1b59e | -2.86795 | -50.74403 | 2025-10-19 05:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 071f4501-6d66-35e3-a5ad-e0440a4bf3d1 | -2.44521 | -49.37354 | 2025-10-19 05:23:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 57067fd3-c506-3c46-adba-83fb859479f0 | -9.90005 | -60.06562 | 2025-10-19 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 71d4cb38-e47f-3e6e-9345-58506b16a01e | -2.25207 | -51.91759 | 2025-10-19 05:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 48910dc4-cf59-3645-adc3-6a1d8d098128 | -3.15094 | -50.24326 | 2025-10-19 05:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f0dafcc2-4128-3e29-9f33-16c91bc82a3c | -2.68281 | -49.54352 | 2025-10-19 05:23:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 8744c27e-ca04-3430-8711-c9bfe0c2ac45 | -9.36006 | -60.85711 | 2025-10-19 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4935458a-ef83-34ce-9535-71bb74ede097 | -2.70359 | -49.87098 | 2025-10-19 05:23:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9f71b4ea-db78-3e6f-8605-92fb7334845d | -3.22476 | -53.14131 | 2025-10-19 05:23:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a1183bf4-82f5-342b-aebf-9a5eda67cf2c | -8.56652 | -48.51118 | 2025-10-19 05:23:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 8f54141c-8c44-383b-993a-4f3298203fc4 | -9.09921 | -65.37845 | 2025-10-19 05:23:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e3ef2f06-5a30-3d60-b8f7-287ab3a08c4f | -4.41564 | -49.76454 | 2025-10-19 05:23:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 482c5c44-5447-34e5-a64a-c648ef215bab | -4.96915 | -56.2682 | 2025-10-19 05:23:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 55f477ec-a2bd-3eff-a2a8-c1b0461259e6 | -9.64182 | -63.98751 | 2025-10-19 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 05b4e72e-819f-3ce5-93e0-fd479d1160fc | -2.87613 | -50.72525 | 2025-10-19 05:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 64c0467c-cba6-33a5-8867-fa3f397288ea | -8.20905 | -43.95514 | 2025-10-19 05:23:00 | AQUA_M-M | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 29.0 |
| 60067d81-7df3-3bb3-a8ee-c87f058dbaaa | -9.89468 | -64.17218 | 2025-10-19 05:23:00 | NOAA-21 | BURITIS | RONDÔNIA | Brasil | 1100452 | 11 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 6cec22cc-b3b2-360a-8241-1cf3ebed56ea | -9.59131 | -63.50129 | 2025-10-19 05:23:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ff8935fb-1b86-33c7-95a0-687d43169424 | -2.79142 | -49.65363 | 2025-10-19 05:23:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e5d3eac4-888a-3603-98b6-dbc96e7d70d8 | -2.74673 | -49.38681 | 2025-10-19 05:23:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b60fd8e7-2862-35c7-95b1-297ba914471f | -12.14945 | -45.05726 | 2025-10-19 05:23:00 | AQUA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 3b6fb25e-1112-32c1-a2a3-8febfa2d0d80 | -9.46885 | -63.23974 | 2025-10-19 05:23:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a8f741d1-0287-3a4b-94b1-294244ee3f12 | -3.63381 | -55.28814 | 2025-10-19 05:23:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 75a702b5-60f2-3a92-91b1-14c63701ea95 | -3.0447 | -51.21412 | 2025-10-19 05:23:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| faa68e64-289e-37d9-82ef-5c5f655155ae | -2.68224 | -49.54742 | 2025-10-19 05:23:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 3fb178f6-d624-3668-a4a9-7e1a44be5f2d | -2.86989 | -50.73094 | 2025-10-19 05:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4a9c4c1c-b06c-3b06-a54c-1450e86efc83 | -3.52102 | -51.66166 | 2025-10-19 05:23:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2d63d8b2-2da8-3847-8da9-0315cd1826d3 | -2.69419 | -49.5453 | 2025-10-19 05:23:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 9d3505b1-c041-3d3d-8584-541b370bd1e4 | -2.81497 | -58.29086 | 2025-10-19 05:23:00 | NOAA-21 | SILVES | AMAZONAS | Brasil | 1304005 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 12a01f77-d091-3b90-8187-c7e49e4640d3 | -3.86087 | -49.82206 | 2025-10-19 05:23:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 273c04c5-0bff-37e3-aa9c-a7e6a9ef1fa6 | -6.93252 | -59.53048 | 2025-10-19 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9bfc6af2-8b01-3435-8546-4a90f872674a | -10.22291 | -44.05867 | 2025-10-19 05:23:00 | AQUA_M-M | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 8cf54369-af83-38a4-a54a-4f731ab0a16a | -3.47416 | -52.40256 | 2025-10-19 05:23:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a710ea40-4aa2-3663-90cf-5d25d4f00a05 | -6.91481 | -55.45827 | 2025-10-19 05:23:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5ecddec2-1e17-3149-8742-43b96a582e2c | -2.70046 | -49.54225 | 2025-10-19 05:23:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 83ad3d09-c094-3edc-a34b-1c16e66a3708 | -2.34634 | -57.00926 | 2025-10-19 05:23:00 | NOAA-21 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2643cd03-9e59-38db-a48d-ee0602df3d41 | -2.70528 | -49.85976 | 2025-10-19 05:23:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 08022038-a725-3118-8344-c53af746eaf2 | -10.03481 | -59.35594 | 2025-10-19 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 64a622bf-8a19-3064-8fea-6946898a41de | -10.88862 | -46.06104 | 2025-10-19 05:23:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 22.9 |
| fa469654-7b81-3f41-a4e1-7ee867ecb4e0 | -2.4464 | -49.36558 | 2025-10-19 05:23:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 995f1643-9fec-3d2b-9acf-6e7cae34bd76 | -8.60538 | -40.1957 | 2025-10-19 05:23:00 | AQUA_M-M | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 43.5 |
| 9764913c-110a-3663-adb7-ffd11d44b95d | -4.1496 | -47.65905 | 2025-10-19 05:23:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| dd11c0b5-aba9-316c-aec8-8354de9aab58 | -3.40052 | -54.06464 | 2025-10-19 05:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ec639d3d-0a70-3720-92ee-db50b58b48bf | -5.36284 | -47.20844 | 2025-10-19 05:23:00 | NOAA-21 | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Amazônia | 14.0 |
| b4ceaffd-fb67-3a36-81ad-83867e925444 | -5.08686 | -60.22172 | 2025-10-19 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e642e0d2-2593-390f-b58f-3a642e8e31a6 | -9.85163 | -68.11426 | 2025-10-19 05:23:00 | NOAA-21 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 38257f5f-ecb1-3eb6-8c8b-d11ddf688f09 | -10.04051 | -59.36453 | 2025-10-19 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 219e40f2-c16a-3254-906a-698eebe31853 | -9.87299 | -64.99117 | 2025-10-19 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 045b0504-613f-373a-833f-caf6ed296c8c | -2.69989 | -49.54615 | 2025-10-19 05:23:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| c859db04-62c8-3a21-b0e9-b3422f29458c | -6.93068 | -59.27951 | 2025-10-19 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1383c30c-28e1-3eb5-a3dc-dfc5343ae1fb | -3.52442 | -58.36252 | 2025-10-19 05:23:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 370722b5-0337-3460-80ce-78987a8cfc89 | -3.80518 | -51.6479 | 2025-10-19 05:23:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 36e19a0a-7983-304b-9f4c-b0d65e1570a0 | -9.66946 | -61.91968 | 2025-10-19 05:23:00 | NOAA-21 | VALE DO ANARI | RONDÔNIA | Brasil | 1101757 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ed8e28b6-7484-3475-ba24-8d0b95866b35 | -9.78316 | -64.99075 | 2025-10-19 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 20188314-f25f-3286-9949-a306b3935059 | -9.33613 | -62.68781 | 2025-10-19 05:23:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dc8396c0-0ea2-3d32-94fb-248a5c465499 | -9.69344 | -63.30723 | 2025-10-19 05:23:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e972ec21-9c9e-3853-8b67-b97f04cc5f41 | -3.4674 | -47.69146 | 2025-10-19 05:23:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 531a9ca0-ebc6-3300-bfac-2d80d4928517 | -6.66619 | -58.7423 | 2025-10-19 05:23:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7df7afd2-b52a-3261-b6de-469e632f83b1 | -3.2473 | -54.51602 | 2025-10-19 05:23:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7a830fa0-5eba-35c4-a579-32851702bf43 | -9.42649 | -63.70972 | 2025-10-19 05:23:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |


[Clique aqui para ver as próximas entradas](README58.md)
