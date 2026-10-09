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

## Dados Diários - Página 45

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f7ae91bd-c0b8-3dfd-b26a-31a340b4e1be | -4.6282 | -49.2147 | 2026-10-09 00:50:00 | GOES-19 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 73.4 |
| 05d17a64-1eed-3146-b13b-7946da8e33ec | -5.6932 | -53.487 | 2026-10-09 00:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 74.0 |
| d43ea357-9ef0-3c70-ab59-998bac706a4b | -3.5493 | -54.6752 | 2026-10-09 00:50:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 92.0 |
| 33f73554-ab00-3910-a3fe-fee912abf11a | -3.0002 | -54.0684 | 2026-10-09 00:50:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 72.5 |
| 2c2560b4-e4fc-373d-8275-f79a67ea5596 | -7.2182 | -55.1416 | 2026-10-09 00:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 92.0 |
| 0cfcfc5a-3420-3a0a-87a0-02f8296ad41f | -7.1825 | -52.6283 | 2026-10-09 00:50:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 73.0 |
| 51416e4b-be5b-3dfa-8f61-03c932781123 | -5.7117 | -53.4862 | 2026-10-09 00:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 108.8 |
| f279ff68-9513-3a98-b246-fe3832def96e | -8.8961 | -44.9336 | 2026-10-09 00:50:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 59.0 |
| 2880487f-cbf0-3b6c-93c7-34921516dbae | -3.0924 | -53.9656 | 2026-10-09 00:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 64.8 |
| 4c73f7d7-da14-39f4-94aa-3dfbf5082248 | -8.9107 | -45.2519 | 2026-10-09 00:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 80.8 |
| 12c0d9a5-4869-3679-9ba1-e62f6966d5fe | -5.6934 | -53.4667 | 2026-10-09 00:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 80.2 |
| d19f101e-cf5b-3319-8e3e-449bda98f122 | -12.0058 | -43.464 | 2026-10-09 00:50:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 209.4 |
| 85bb6416-1716-3386-ba71-7eee5e54e9d6 | -3.364 | -50.4072 | 2026-10-09 00:50:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 144.1 |
| 076b8e71-af37-3c6f-9b50-4d576792117b | -7.2187 | -55.0815 | 2026-10-09 00:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 53.7 |
| 90bc3629-aec3-36a8-b03b-4038363ff489 | -5.7679 | -43.8467 | 2026-10-09 00:50:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 53.1 |
| 9dd77f23-436b-3fa8-b99b-a4de46950ebf | -3.3639 | -50.4282 | 2026-10-09 00:50:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 50.9 |
| 2ea12ad5-85f4-3adf-ac20-5dda22be5442 | -3.3454 | -50.4288 | 2026-10-09 00:50:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 76.7 |
| 4ba192a1-4b9f-37e8-a6cb-57db45e01271 | -11.8499 | -43.5835 | 2026-10-09 00:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 76.3 |
| f390495c-1bac-3647-80a7-cec21a284d12 | -3.3456 | -50.3869 | 2026-10-09 00:50:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 36.6 |
| e4483147-3581-3a45-8ef2-ac02f8ebf24b | -11.9865 | -43.4671 | 2026-10-09 00:50:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 81.4 |
| 9257b58b-d952-329e-907b-6d2422a3e010 | -6.0021 | -40.9594 | 2026-10-09 00:50:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 342.3 |
| 3a447754-4bfc-36c6-b750-f162f5069e51 | -13.5117 | -44.368 | 2026-10-09 00:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 77.5 |
| 91842a7e-9cb6-3118-861f-ae80f37dfcf9 | -5.9833 | -40.961 | 2026-10-09 00:50:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 120.5 |
| 4eb408a1-71bd-3d9c-9210-e7b2cd83d481 | -3.1109 | -53.945 | 2026-10-09 00:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 87.0 |
| 5ef6d9c1-ffb8-3270-aad8-7a504ce433db | -3.1285 | -54.1657 | 2026-10-09 00:50:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 126.7 |
| 7f53c6a1-e754-3caf-8242-34028e4265d8 | -8.9113 | -45.2062 | 2026-10-09 00:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 185.4 |
| 203cc29a-d202-3e58-a97a-e13783e5849d | -8.8921 | -45.2311 | 2026-10-09 00:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 177.7 |
| c94d0237-78d4-3f19-9ffd-05fa8aec7963 | -3.1114 | -53.8041 | 2026-10-09 00:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 63.1 |
| 84f3db73-4014-3547-91dd-c90dc6df73a5 | -3.1101 | -54.1661 | 2026-10-09 00:50:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 168.5 |
| 7595cb9d-0447-399d-ac94-ae22a8734c47 | -3.11 | -54.1862 | 2026-10-09 00:50:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 113.3 |
| d6ecd881-a643-336e-bf63-5dd9ec0af693 | -6.4903 | -62.8554 | 2026-10-09 00:50:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 95.7 |
| b9ce1c88-bcfe-33e7-b5b0-613e560900d2 | -8.911 | -45.229 | 2026-10-09 00:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 552.2 |
| d5ba63b6-4d09-3828-b251-d0f339a92b38 | 4.4435 | -60.9657 | 2026-10-09 00:50:00 | GOES-19 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 60.1 |
| 7bfb65a3-ec61-30a4-a789-d5a28bbb8dc5 | -8.7231 | -45.1583 | 2026-10-09 00:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 57.6 |
| a0192abf-d13f-3584-b452-150ea4b6aa7c | -7.2367 | -55.1406 | 2026-10-09 00:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 68.7 |
| ac28084a-ec9f-36e4-a511-1cbb4b2f1bf4 | -7.1995 | -55.1627 | 2026-10-09 00:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 86.0 |
| e8c6a4cb-986f-3791-b73e-d0a65f5aa319 | -3.2759 | -54.0614 | 2026-10-09 00:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 61.4 |
| 0e3d4340-a1bd-3883-8f18-403042945315 | -5.7116 | -53.5065 | 2026-10-09 00:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 45.1 |
| 16f35706-aa91-3aee-9e85-ce38628d61ae | -6.0024 | -40.935 | 2026-10-09 00:50:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 78.6 |
| 3234782e-1c3a-3652-9612-a6a5825772bd | -7.5835 | -61.5326 | 2026-10-09 00:50:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 64.0 |
| 93904b89-a89a-3aa9-ae93-dd830b237cec | -7.218 | -55.1617 | 2026-10-09 00:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 141.8 |
| 6b3da431-171d-316e-af94-2ca20bf2be19 | -3.0925 | -53.9455 | 2026-10-09 00:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 108.5 |
| 6d31c4a2-d3ec-3009-ae62-1519d6b6a197 | -7.4442 | -63.5589 | 2026-10-09 00:50:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 59.3 |
| 65fbe0ae-54e0-3858-8893-56d9d5a6edd0 | -8.7423 | -45.1334 | 2026-10-09 00:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 118.0 |
| 5b2beabe-dc80-3dbb-bba8-f360e3e79daa | -6.7363 | -55.1675 | 2026-10-09 00:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 53.2 |
| e2251ea1-8c9d-3b73-b167-86f2af5584e2 | -11.7601 | -61.0743 | 2026-10-09 00:50:00 | GOES-19 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 45.2 |
| 145f776d-7e18-374a-b7da-d3753083ce12 | -3.7346 | -59.4577 | 2026-10-09 00:50:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 53.6 |
| 05f2cfd9-41de-35e2-8a68-9a912831cfe4 | -6.4948 | -55.3195 | 2026-10-09 00:50:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 37.0 |
| 9c3d3902-89f0-3035-a646-dd3b469a6cc8 | -3.2577 | -54.0217 | 2026-10-09 00:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 75.0 |
| 8e6698d8-1d25-36f4-9f06-fb850ddaf879 | -13.1827 | -54.3571 | 2026-10-09 00:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 91.5 |
| 89d393b9-6488-3c6c-96bb-da0b2a81e8f4 | -13.1639 | -54.3385 | 2026-10-09 00:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 91.0 |
| eb06c37e-3201-3160-a2da-8f746a3b5854 | -3.9912 | -59.356 | 2026-10-09 00:50:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 52.1 |
| 8d846699-4ab0-38da-bfc4-80e19d25ff7e | -8.8924 | -45.2083 | 2026-10-09 00:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 61.8 |
| fa50e65f-05da-3a9c-9ad3-dcc419c10b91 | -3.2576 | -54.0418 | 2026-10-09 00:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 80.9 |
| 1923fdf8-84ee-3443-be6b-3ff8dab81594 | -1.1094 | -54.1601 | 2026-10-09 00:50:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 72.0 |
| 1244e721-ae16-3f83-95be-fc9d0e348f21 | -4.2768 | -49.0816 | 2026-10-09 00:50:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 81.2 |
| a3fc6c5f-ff7c-3445-a62c-88f1265340c0 | -12.0054 | -43.4878 | 2026-10-09 00:50:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 156.4 |
| b28031a6-f565-3909-a18b-f79d2ea8dbf8 | -2.499 | -56.0675 | 2026-10-09 00:50:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 74.7 |
| 04c0e037-75ac-3f2a-a122-1586400aa4e9 | -8.7234 | -45.1355 | 2026-10-09 00:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 95.2 |
| 51461993-258f-35c1-aa65-85cb805d2e3b | -12.2154 | -57.1287 | 2026-10-09 01:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 62.3 |
| 3bdad589-9b79-38fc-a83c-0cda917a2c27 | -3.1109 | -53.945 | 2026-10-09 01:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 94.7 |
| 30546ded-d51b-317f-91cc-b68175e09369 | -18.6464 | -41.3443 | 2026-10-09 01:00:00 | GOES-19 | MENDES PIMENTEL | MINAS GERAIS | Brasil | 3141504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 133.2 |
| f16778e8-c94c-3a36-93d8-c75cebdc5971 | -11.9865 | -43.4671 | 2026-10-09 01:00:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 62.0 |
| 0e28cdd3-594b-3eec-a9c9-0c77280e0e0e | -5.7119 | -53.4658 | 2026-10-09 01:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 76.5 |
| d585311e-90bc-35af-ab62-57e94b347ff2 | -13.2018 | -54.3551 | 2026-10-09 01:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 81.4 |
| a4eabc9d-2b37-3623-a2fc-7600be5b942c | -8.8921 | -45.2311 | 2026-10-09 01:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 196.0 |
| e1483752-917c-397f-aeba-9a876603ec9d | -3.0007 | -53.9075 | 2026-10-09 01:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 109.0 |
| 39373372-1170-34e4-84eb-b28af3ae01bd | -12.2158 | -57.0887 | 2026-10-09 01:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 48.2 |
| 2ce5b041-76fb-3d51-8f87-0a9912671cc7 | -3.1972 | -50.5592 | 2026-10-09 01:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 23.4 |
| f5e95338-aeb6-33e6-8064-54e31a2ab51f | -6.3842 | -55.265 | 2026-10-09 01:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 66.0 |
| 3b8881dd-bb56-34b6-a95a-f59aa3f3221a | -11.7603 | -61.0549 | 2026-10-09 01:00:00 | GOES-19 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 46.7 |
| 27b635c2-4806-3b3c-9987-7d335b003450 | -6.8907 | -45.8988 | 2026-10-09 01:00:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 51.2 |
| 243021bc-6794-3a22-9533-1cf230a99c3a | -4.2768 | -49.0816 | 2026-10-09 01:00:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 64.8 |
| 1d1ff134-3662-3eca-adba-eca7914caa5f | -6.0552 | -47.2935 | 2026-10-09 01:00:00 | GOES-19 | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 90.8 |
| a14cb801-a1ea-349d-bcc2-e342023dbb54 | -3.5493 | -54.6752 | 2026-10-09 01:00:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 87.2 |
| 40f734c8-7549-3c78-be71-8ab1cc55864d | -6.4948 | -55.3195 | 2026-10-09 01:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 61.7 |
| 4ca83564-841c-32e1-889f-3f501149e67f | -7.1995 | -55.1627 | 2026-10-09 01:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 105.9 |
| 4ea5f5e7-fac7-3443-a9ee-a6e0432fd4d1 | -3.2945 | -54.0006 | 2026-10-09 01:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 59.5 |
| 24f106c0-222e-322a-bdf9-9d7ebcfd8373 | -3.1101 | -54.1661 | 2026-10-09 01:00:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 112.8 |
| f26a9352-43fe-3a62-afc2-3ee3f7151774 | -12.2156 | -57.1087 | 2026-10-09 01:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 109.7 |
| e6c600f9-c38c-3bcb-af72-2f76d08bd3a2 | -8.8918 | -45.2539 | 2026-10-09 01:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 68.1 |
| 928bbcb5-b4e8-3ad3-87b1-285fb8c35e62 | -3.1285 | -54.1657 | 2026-10-09 01:00:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 168.8 |
| 4c31253a-d131-39bc-8e8e-95af06e58ac6 | -13.1639 | -54.3385 | 2026-10-09 01:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 93.2 |
| 3c61d300-040f-3735-89ad-41812d35af10 | -12.2346 | -57.1071 | 2026-10-09 01:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 94.0 |
| 47c5f57b-3487-30e6-993b-8382b0232998 | -3.2576 | -54.0418 | 2026-10-09 01:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 67.1 |
| 0d44108d-4b2a-3f62-b716-6cde63641ae3 | -3.3455 | -50.4078 | 2026-10-09 01:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 97.0 |
| de115749-dc8e-36f3-8014-0ec10dce27fe | -8.9113 | -45.2062 | 2026-10-09 01:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 91.5 |
| 27708d6a-2e79-34dc-8bf5-fbef07c65c70 | -7.2367 | -55.1406 | 2026-10-09 01:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 92.1 |
| c969deb2-7303-378c-9f12-dbf6ef21e563 | -7.4442 | -63.5589 | 2026-10-09 01:00:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 56.9 |
| 95c9d858-4035-3734-8d61-dcd36f3ac815 | -13.1827 | -54.3571 | 2026-10-09 01:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 99.9 |
| 42c3dc2b-5e09-37a9-b542-ba952207e76f | -12.0058 | -43.464 | 2026-10-09 01:00:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 121.6 |
| 7e703af3-9fb2-3cef-80a5-b3e41a1b1f41 | -7.2011 | -52.6272 | 2026-10-09 01:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 29.7 |
| dc4faa4b-cee9-37d1-b997-7d7282ea3638 | -5.6934 | -53.4667 | 2026-10-09 01:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 74.2 |
| 4397aff8-8412-3b5a-a109-79c197141aba | -3.9912 | -59.356 | 2026-10-09 01:00:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 65.5 |
| 32f99e91-e692-31eb-ab75-5146aad10fc9 | -6.0021 | -40.9594 | 2026-10-09 01:00:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 255.4 |
| 44f46317-1d01-3db5-80e2-8ab75193e4ea | -9.7054 | -58.0854 | 2026-10-09 01:00:00 | GOES-19 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 59.4 |
| 40e42907-5eae-317b-bdac-d611cc43a8b7 | -3.1114 | -53.8041 | 2026-10-09 01:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 56.7 |
| 80389ec4-3b8a-33a5-9689-a7845ded6bee | -12.0251 | -43.4609 | 2026-10-09 01:00:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 79.5 |
| 9455d282-00ee-3667-a58a-4d542ae9f04c | -8.8961 | -44.9336 | 2026-10-09 01:00:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 64.9 |
| db1de1b6-9ae4-34a8-834c-8a6e344087c1 | -4.6282 | -49.2147 | 2026-10-09 01:00:00 | GOES-19 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 87.5 |


[Clique aqui para ver as próximas entradas](README46.md)
