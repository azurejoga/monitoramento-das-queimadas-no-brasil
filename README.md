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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6eda4f5d-6f5b-3921-aad0-67b280b8c2bd | -15.7404 | -59.8284 | 2025-01-28 00:20:00 | GOES-16 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 62.9 |
| 0b6542ca-32b5-32e2-9f1f-7505f31e5b2f | -15.7402 | -59.8484 | 2025-01-28 00:20:00 | GOES-16 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 67.1 |
| 03cf584e-8a89-3f93-b851-88fe966cf5f2 | -10.2193 | -36.2892 | 2025-01-28 00:20:00 | GOES-16 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 188.2 |
| 8b618607-a4a6-3555-be2c-751cd117d6aa | -11.0506 | -45.3731 | 2025-01-28 00:38:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| cd48e6a4-8ce7-3183-8946-cff76dec724d | -10.9419 | -45.171398 | 2025-01-28 00:38:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 1faf5855-f50a-3b88-a2b5-dba7ec71138c | -12.351 | -47.990002 | 2025-01-28 00:38:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5732f0b5-0d25-32ab-b12a-7f5c0fb02728 | -14.2125 | -47.011002 | 2025-01-28 00:38:00 | METOP-C | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 7b9cd4d3-1ee0-31d1-8bb5-172f307d4330 | -5.2722 | -45.771999 | 2025-01-28 00:38:00 | METOP-C | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6abe7896-1c61-3c56-9910-1fd6c7005704 | -2.8201 | -49.006699 | 2025-01-28 00:38:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b2646d37-ee49-3254-8ece-feccc6e48804 | -5.4507 | -44.813 | 2025-01-28 00:38:00 | METOP-C | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e5c9c965-1e52-3e4e-8d6f-55845dc9d2ab | -6.2113 | -46.218399 | 2025-01-28 00:38:00 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 81cf786c-d7e3-3c14-a72f-e5528eb95231 | -12.7726 | -44.831699 | 2025-01-28 00:38:00 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 9e692f1b-9af2-3592-89df-dee34982a95a | -6.2659 | -48.028301 | 2025-01-28 00:38:00 | METOP-C | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f0e0406c-ead3-3c56-aa6c-cf4b4e16a839 | -2.8103 | -49.008801 | 2025-01-28 00:38:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2f7bc70a-85f7-3951-991e-231e8638dec4 | -5.4488 | -44.804798 | 2025-01-28 00:38:00 | METOP-C | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ed58aac2-b494-3748-8ac4-936592ad2f91 | -5.2704 | -45.764599 | 2025-01-28 00:38:00 | METOP-C | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f4e4974b-b87a-3ce7-9668-ac15982bc569 | -12.4887 | -43.7924 | 2025-01-28 00:38:00 | METOP-C | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| b5cf2b6a-2f89-3213-a29a-64365d49ff10 | -11.0295 | -45.0592 | 2025-01-28 00:38:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| d84a9b07-e2ca-3582-9bb1-f41dd0c6c892 | -12.4851 | -43.776798 | 2025-01-28 00:38:00 | METOP-C | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| a6af131a-58b9-3cef-a19c-5342e46f5790 | -5.0175 | -45.9632 | 2025-01-28 00:38:00 | METOP-C | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 2b988f43-bfd1-39de-85a4-0fb360c29afc | -6.2675 | -48.035198 | 2025-01-28 00:38:00 | METOP-C | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b3c23eb8-d5aa-3c8f-b344-f934c5cecdad | -11.0278 | -45.051998 | 2025-01-28 00:38:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 6893dddb-3200-3c95-9bcc-5fa0c2caae6e | -2.8216 | -49.013599 | 2025-01-28 00:38:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 42648ea8-04dc-3f17-958a-ae7c90c4a0ca | -2.8118 | -49.015701 | 2025-01-28 00:38:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c7b5aaa7-7bec-3107-a8b4-95f022786d2e | -11.0522 | -45.380199 | 2025-01-28 00:38:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| d181a89e-a257-3988-aaab-1587405c4bd1 | -6.3411 | -47.095001 | 2025-01-28 00:38:00 | METOP-C | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1a475d91-b5dc-3669-b597-5973647c506f | -12.4869 | -43.784599 | 2025-01-28 00:38:00 | METOP-C | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 5d3f271d-901a-3242-a716-87302dcca8a4 | -29.61699 | -56.46318 | 2025-01-28 01:15:00 | TERRA_M-M | URUGUAIANA | RIO GRANDE DO SUL | Brasil | 4322400 | 43 | 33 | nan | nan | nan | Pampa | 18.8 |
| 3eb8846f-fd48-35c8-bdeb-526aa61219dc | -29.6153 | -56.44664 | 2025-01-28 01:15:00 | TERRA_M-M | URUGUAIANA | RIO GRANDE DO SUL | Brasil | 4322400 | 43 | 33 | nan | nan | nan | Pampa | 31.9 |
| f568ad3d-a1a8-3508-b98a-b6df5384f6fb | -29.60583 | -56.46472 | 2025-01-28 01:15:00 | TERRA_M-M | URUGUAIANA | RIO GRANDE DO SUL | Brasil | 4322400 | 43 | 33 | nan | nan | nan | Pampa | 9.5 |
| f0f48c09-8f4e-3cd0-9209-4c8026b5fbc4 | -29.60415 | -56.44813 | 2025-01-28 01:15:00 | TERRA_M-M | URUGUAIANA | RIO GRANDE DO SUL | Brasil | 4322400 | 43 | 33 | nan | nan | nan | Pampa | 11.2 |
| 36fb0c1f-db04-3978-b8e7-6345c835c930 | -14.55683 | -53.97829 | 2025-01-28 01:19:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| de05d4a3-8500-354e-ac26-cb69eb09995c | -29.607201 | -56.447399 | 2025-01-28 01:20:00 | METOP-B | URUGUAIANA | RIO GRANDE DO SUL | Brasil | 4322400 | 43 | 33 | nan | nan | nan | Pampa | nan |
| 769edf94-1a43-3a25-bf36-6071b8fb20a8 | -29.615101 | -56.436501 | 2025-01-28 01:20:00 | METOP-B | URUGUAIANA | RIO GRANDE DO SUL | Brasil | 4322400 | 43 | 33 | nan | nan | nan | Pampa | nan |
| 0114ff4e-2511-3d92-b5d9-6907f7dedf49 | -29.616899 | -56.444599 | 2025-01-28 01:20:00 | METOP-B | URUGUAIANA | RIO GRANDE DO SUL | Brasil | 4322400 | 43 | 33 | nan | nan | nan | Pampa | nan |
| 0e232fdb-da65-3f47-9534-bd3bfd97c73f | -29.6054 | -56.439301 | 2025-01-28 01:20:00 | METOP-B | URUGUAIANA | RIO GRANDE DO SUL | Brasil | 4322400 | 43 | 33 | nan | nan | nan | Pampa | nan |
| f2f9a9e4-270e-3a87-9807-deeb75ca6d22 | -1.72302 | -54.67577 | 2025-01-28 01:21:00 | TERRA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 8ca72583-b4d7-3135-8619-0bf8aef464a7 | -15.7538 | -59.8228 | 2025-01-28 01:22:00 | METOP-B | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 440dfe92-228e-3358-bb78-40d8dfca8601 | -12.48277 | -43.78705 | 2025-01-28 03:19:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4f74fd11-07c3-3a32-a9e3-d265e68271bd | -15.5911 | -42.40018 | 2025-01-28 03:19:00 | NPP-375D | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a42129fa-26ff-32b0-b2b3-6414b12cb98a | -12.48953 | -43.7887 | 2025-01-28 03:19:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f6222adc-1202-33d5-ace7-a8d2968785a7 | -12.56843 | -38.16951 | 2025-01-28 03:19:00 | NPP-375D | DIAS D'ÁVILA | BAHIA | Brasil | 2910057 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| c36ee904-bc00-35c3-a9f9-c6deabea78c1 | -15.58921 | -42.40064 | 2025-01-28 03:19:00 | NPP-375D | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 60a3e08b-ba62-37bd-8281-cd251fbbb915 | -12.4825 | -43.78773 | 2025-01-28 03:19:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a2a4606c-c798-3da2-8ee0-f072d146993a | -12.3661 | -38.45428 | 2025-01-28 03:19:00 | NPP-375D | CATU | BAHIA | Brasil | 2907509 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 0403f329-ef17-3709-98cb-6c4cfd5318fc | -15.58514 | -42.39897 | 2025-01-28 03:19:00 | NPP-375D | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 536194e9-8cdf-3f68-9f30-51eb63ef60f6 | -12.48143 | -43.7933 | 2025-01-28 03:19:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f35e9b64-6459-3c59-acde-c2ee92400aa1 | -12.48926 | -43.78942 | 2025-01-28 03:19:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a54af85c-ed7a-31b3-a94b-9b02d4f069cf | -6.26207 | -48.03912 | 2025-01-28 03:40:00 | NOAA-20 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8639fb47-744c-3c40-a530-978d1e6c1136 | -5.02372 | -45.97299 | 2025-01-28 03:40:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 39d7c5d9-c8c7-3c94-b1d5-3557759a7078 | -6.3395 | -47.09929 | 2025-01-28 03:40:00 | NOAA-20 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7a30fc07-d39a-3445-ac74-c17f61e979b9 | -5.97046 | -40.38186 | 2025-01-28 03:40:00 | NOAA-20 | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 4f5a3e51-2a8f-37ea-b8de-d07ec162021f | -4.92149 | -38.91825 | 2025-01-28 03:40:00 | NOAA-20 | QUIXADÁ | CEARÁ | Brasil | 2311306 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 571e6f4e-c437-3b0d-baf6-8726970cd04d | -9.64917 | -36.51012 | 2025-01-28 03:40:00 | NOAA-20 | TAQUARANA | ALAGOAS | Brasil | 2709103 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 0b369eb5-02e3-33ed-9400-03ff7f26e0f2 | -6.20943 | -46.22121 | 2025-01-28 03:40:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 29b41e63-420e-3a73-b810-901187694ae1 | -9.74919 | -36.45831 | 2025-01-28 03:40:00 | NOAA-20 | LIMOEIRO DE ANADIA | ALAGOAS | Brasil | 2704203 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 9fe13875-60f2-3380-ad6a-e80dfb1415e3 | -3.13522 | -40.04527 | 2025-01-28 03:40:00 | NOAA-20 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 452841ed-5fa7-3889-8d1a-df8f5fb91517 | -4.92853 | -37.10915 | 2025-01-28 03:40:00 | NOAA-20 | AREIA BRANCA | RIO GRANDE DO NORTE | Brasil | 2401107 | 24 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 81eaf992-1555-3b68-acdb-189e2829418f | -4.92209 | -38.91554 | 2025-01-28 03:40:00 | NOAA-20 | QUIXADÁ | CEARÁ | Brasil | 2311306 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| b62dbfb6-a737-345e-b1c0-0cb6bf773693 | -5.01854 | -45.96721 | 2025-01-28 03:40:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1c00e00b-224e-3f5a-a43c-0d3a4207f574 | -10.46469 | -45.09424 | 2025-01-28 03:42:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b6d8a8c3-c0c9-3b80-82cf-f3c548ebb018 | -10.46424 | -45.09391 | 2025-01-28 03:42:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e5fe4e6b-7200-3fc3-b5f9-6e83af7b03ab | -11.06191 | -38.43677 | 2025-01-28 03:42:00 | NOAA-20 | RIBEIRA DO AMPARO | BAHIA | Brasil | 2926509 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 7d4b9af6-3847-37aa-baa0-ada7a7549961 | -10.45907 | -45.09278 | 2025-01-28 03:42:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d18bdb69-cb18-33a5-ae6e-7d5ee309d7aa | -10.46014 | -45.0899 | 2025-01-28 03:42:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3c54e023-cfc6-3d8d-a290-904dc4424bd1 | -9.89198 | -36.82059 | 2025-01-28 03:42:00 | NOAA-20 | GIRAU DO PONCIANO | ALAGOAS | Brasil | 2702900 | 27 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 10766ed9-06cb-3c9f-9979-bd71b5b7c0e9 | -9.77805 | -42.01331 | 2025-01-28 03:42:00 | NOAA-20 | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 409a530c-acf4-39db-946d-19bd38593d53 | -10.01862 | -37.69317 | 2025-01-28 03:42:00 | NOAA-20 | POÇO REDONDO | SERGIPE | Brasil | 2805406 | 28 | 33 | nan | nan | nan | Caatinga | 0.3 |
| d30dce15-91d4-3f7c-9e0b-cf32adcbe9c7 | -10.11705 | -42.20206 | 2025-01-28 03:42:00 | NOAA-20 | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 0fb4352f-44d9-3056-9ae9-c4fa6bedbde3 | -10.45953 | -45.09312 | 2025-01-28 03:42:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1c490037-5f11-3378-88ee-6306d539d31f | -10.78708 | -37.19183 | 2025-01-28 03:42:00 | NOAA-20 | LARANJEIRAS | SERGIPE | Brasil | 2803609 | 28 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| feda0acc-0a3a-305b-b17c-7fb591a3cb35 | -11.02825 | -45.06362 | 2025-01-28 03:42:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| afae738c-ad43-3203-8abb-b5543486ad69 | -11.04874 | -45.38183 | 2025-01-28 03:42:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7312c127-b23c-361d-8714-dd075f21359a | -15.43922 | -39.79878 | 2025-01-28 03:42:00 | NOAA-20 | PAU BRASIL | BAHIA | Brasil | 2923902 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| c2d89996-37f3-3da1-a2f5-1f705ef25987 | -12.36381 | -38.45615 | 2025-01-28 03:42:00 | NOAA-20 | CATU | BAHIA | Brasil | 2907509 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 6636f05b-4830-3ca9-a647-4e0d4c3daba3 | -12.36723 | -38.45671 | 2025-01-28 03:42:00 | NOAA-20 | CATU | BAHIA | Brasil | 2907509 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 7450b16d-21cf-3bae-82c0-88f3e26cfee2 | -10.94625 | -45.1789 | 2025-01-28 03:42:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b1c0f724-f41d-3e85-baec-2b70f4ef27c4 | -14.13447 | -41.69184 | 2025-01-28 03:42:00 | NOAA-20 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| dbe43034-0ac9-39f1-bb45-00c1a8447e11 | -11.05442 | -45.38288 | 2025-01-28 03:42:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ed83f1ed-7d94-3f93-b992-c2dda3fb3def | -10.94683 | -45.17578 | 2025-01-28 03:42:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4401aef5-f62b-3cca-a567-9b8252909fdb | -13.92217 | -42.49654 | 2025-01-28 03:42:00 | NOAA-20 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 42ec5be4-6b90-3a41-94c5-d927c62286a1 | -11.02768 | -45.06665 | 2025-01-28 03:42:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7a968c28-5af4-393f-b718-4755f97b8443 | -15.64786 | -39.18682 | 2025-01-28 03:42:00 | NOAA-20 | CANAVIEIRAS | BAHIA | Brasil | 2906303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 20f1bede-045a-3b90-b7e5-1a5f5046a6bd | -15.65127 | -39.1874 | 2025-01-28 03:42:00 | NOAA-20 | CANAVIEIRAS | BAHIA | Brasil | 2906303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| f52da6b7-79bc-3a72-abac-e6b15fb95774 | -11.82646 | -41.22646 | 2025-01-28 03:42:00 | NOAA-20 | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 67461d85-5666-3919-b674-85cb9ffe48b1 | -11.04921 | -45.38174 | 2025-01-28 03:42:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 51a1bcd7-8fda-308b-b9b7-15295b08e58d | -12.85119 | -44.87062 | 2025-01-28 03:42:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ef0277f1-6f5e-372a-89ac-f27afe770f51 | -11.05395 | -45.38296 | 2025-01-28 03:42:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| de014071-19e0-3ff6-903d-5e1d7752703d | -12.48602 | -43.78609 | 2025-01-28 03:42:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| be518622-50ff-3d6f-9837-b68ec584e463 | -12.48513 | -43.79092 | 2025-01-28 03:42:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 6fbf923b-f56d-3d33-be40-38000a9663ca | -14.12053 | -41.67969 | 2025-01-28 03:42:00 | NOAA-20 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| fbe29a72-5790-3903-9c25-bf5ccf50ad62 | -11.02883 | -45.06057 | 2025-01-28 03:42:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c1abea08-b372-3939-9582-bd4f2a5a406c | -18.03843 | -39.92608 | 2025-01-28 03:44:00 | NOAA-20 | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 1a4c9284-44ff-333c-a56d-4edf9ad7bd4c | -19.76001 | -40.04981 | 2025-01-28 03:44:00 | NOAA-20 | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 55b13f73-b20f-3b64-a756-82404df305a9 | -15.58867 | -42.40036 | 2025-01-28 03:44:00 | NOAA-20 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a0c0ae3a-d224-37e6-94b9-fbb1f409bb3f | -15.58931 | -42.39682 | 2025-01-28 03:44:00 | NOAA-20 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 63ee0043-8086-3404-a6eb-3511fe2c763d | -15.7317 | -41.14894 | 2025-01-28 03:44:00 | NOAA-20 | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 1232c50b-ab86-3931-be07-5761f3ed6142 | -15.60712 | -42.29757 | 2025-01-28 03:44:00 | NOAA-20 | INDAIABIRA | MINAS GERAIS | Brasil | 3130655 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0be94dc5-e491-3ddd-8198-27dc6914ce23 | -19.83819 | -40.08427 | 2025-01-28 03:44:00 | NOAA-20 | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 424744b9-f2f8-3b34-ab62-497c42075d06 | -29.61065 | -56.45817 | 2025-01-28 03:49:00 | NOAA-20 | URUGUAIANA | RIO GRANDE DO SUL | Brasil | 4322400 | 43 | 33 | nan | nan | nan | Pampa | 3.7 |


[Clique aqui para ver as próximas entradas](README2.md)
