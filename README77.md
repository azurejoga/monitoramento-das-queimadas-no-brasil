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

## Dados Diários - Página 77

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 34788bd9-4f45-3539-a94e-a3d33bef161c | -9.18641 | -44.72196 | 2024-11-20 12:10:00 | TERRA_M-T | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 58.9 |
| 3f76e6ea-00cc-3bf3-b973-56f5e1777779 | -7.69305 | -42.6995 | 2024-11-20 12:10:00 | TERRA_M-T | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 11.5 |
| 498a41d5-fca5-349e-8509-50c3a01da84f | -8.28839 | -37.76717 | 2024-11-20 12:10:00 | TERRA_M-T | CUSTÓDIA | PERNAMBUCO | Brasil | 2605103 | 26 | 33 | nan | nan | nan | Caatinga | 6.7 |
| 609821b2-2166-3dde-924f-cef657cff534 | -8.84792 | -40.42308 | 2024-11-20 12:10:00 | TERRA_M-T | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 89.4 |
| 51535959-ffb5-3fcd-a503-fe83a0c34744 | -9.19534 | -44.73911 | 2024-11-20 12:10:00 | TERRA_M-T | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 80.5 |
| 421b0f6d-e7f0-37a5-a8d8-78cdec94d5f3 | -7.16623 | -41.49554 | 2024-11-20 12:10:00 | TERRA_M-T | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 8.4 |
| b371d751-cbd0-3c37-ab5e-5936e37021c3 | -9.10073 | -40.45394 | 2024-11-20 12:10:00 | TERRA_M-T | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 7.2 |
| 5ac5631a-b26e-3f77-91b7-30061ee56455 | -10.59502 | -38.7261 | 2024-11-20 12:10:00 | TERRA_M-T | BANZAÊ | BAHIA | Brasil | 2902658 | 29 | 33 | nan | nan | nan | Caatinga | 7.4 |
| 86769bca-28cb-33b0-beac-eccbd54e08fe | -7.15404 | -40.3278 | 2024-11-20 12:10:00 | TERRA_M-T | SALITRE | CEARÁ | Brasil | 2311959 | 23 | 33 | nan | nan | nan | Caatinga | 9.2 |
| 8af51de4-f30b-3d91-81c8-805f04bec72b | -9.18629 | -44.73178 | 2024-11-20 12:10:00 | TERRA_M-T | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 204.9 |
| 58e823cd-9aab-34f6-8cc1-d2c75337b342 | -7.93926 | -38.66666 | 2024-11-20 12:10:00 | TERRA_M-T | SÃO JOSÉ DO BELMONTE | PERNAMBUCO | Brasil | 2613503 | 26 | 33 | nan | nan | nan | Caatinga | 10.3 |
| f9ad9fbe-14eb-3266-863a-f261114137e9 | -9.17484 | -44.73014 | 2024-11-20 12:10:00 | TERRA_M-T | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 52.4 |
| f90c3b4a-00ff-3a77-b442-178ba99e4262 | -7.88619 | -39.36409 | 2024-11-20 12:10:00 | TERRA_M-T | SERRITA | PERNAMBUCO | Brasil | 2614006 | 26 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 3c2545c6-cf53-39c9-a190-6b44c548026e | -7.58492 | -37.9159 | 2024-11-20 12:10:00 | TERRA_M-T | TAVARES | PARAÍBA | Brasil | 2516607 | 25 | 33 | nan | nan | nan | Caatinga | 7.4 |
| 9ed15feb-a187-3928-bd72-7b7e159e1c9c | -10.17766 | -41.10331 | 2024-11-20 12:10:00 | TERRA_M-T | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 15.9 |
| 551bc560-526d-31ae-944d-2fa085257613 | -10.53563 | -39.5407 | 2024-11-20 12:10:00 | TERRA_M-T | MONTE SANTO | BAHIA | Brasil | 2921500 | 29 | 33 | nan | nan | nan | Caatinga | 8.5 |
| 761ac42f-3653-354a-87fe-bc7f03b969e2 | -8.50276 | -39.93898 | 2024-11-20 12:10:00 | TERRA_M-T | SANTA MARIA DA BOA VISTA | PERNAMBUCO | Brasil | 2612604 | 26 | 33 | nan | nan | nan | Caatinga | 14.1 |
| 2a2b4494-5966-3f02-88a9-2642249339cf | -8.52491 | -39.72446 | 2024-11-20 12:10:00 | TERRA_M-T | SANTA MARIA DA BOA VISTA | PERNAMBUCO | Brasil | 2612604 | 26 | 33 | nan | nan | nan | Caatinga | 7.9 |
| 88721447-227c-33bf-9f31-e915c9d66899 | -8.06764 | -38.02298 | 2024-11-20 12:10:00 | TERRA_M-T | FLORES | PERNAMBUCO | Brasil | 2605608 | 26 | 33 | nan | nan | nan | Caatinga | 21.0 |
| 2e6f3fad-98e4-30e0-bcc7-27124e2b8a06 | -7.16471 | -41.5058 | 2024-11-20 12:10:00 | TERRA_M-T | AROEIRAS DO ITAIM | PIAUÍ | Brasil | 2200954 | 22 | 33 | nan | nan | nan | Caatinga | 17.1 |
| 4818a291-3173-38a9-9652-7064553d3309 | -9.20011 | -44.71809 | 2024-11-20 12:10:00 | TERRA_M-T | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 43.1 |
| 40a7c142-149e-31f3-b774-1a6f0a6106e1 | -8.2286 | -42.81764 | 2024-11-20 12:10:00 | TERRA_M-T | BREJO DO PIAUÍ | PIAUÍ | Brasil | 2201988 | 22 | 33 | nan | nan | nan | Caatinga | 12.2 |
| 02441b18-f05f-3c56-9ecd-12aa0efcd581 | -9.80608 | -41.97239 | 2024-11-20 12:10:00 | TERRA_M-T | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 36.2 |
| 97484c28-7363-3820-a27e-e052a6519147 | -7.36517 | -38.55835 | 2024-11-20 12:10:00 | TERRA_M-T | CONCEIÇÃO | PARAÍBA | Brasil | 2504405 | 25 | 33 | nan | nan | nan | Caatinga | 9.3 |
| 9d6adbdb-647b-3398-91d1-44520f852078 | -7.98321 | -38.29387 | 2024-11-20 12:10:00 | TERRA_M-T | SERRA TALHADA | PERNAMBUCO | Brasil | 2613909 | 26 | 33 | nan | nan | nan | Caatinga | 11.6 |
| f89cb74c-20fb-3bc3-adcc-0b1a559e2fb6 | -7.96831 | -37.81162 | 2024-11-20 12:10:00 | TERRA_M-T | FLORES | PERNAMBUCO | Brasil | 2605608 | 26 | 33 | nan | nan | nan | Caatinga | 12.3 |
| 916872ed-2b0f-38f7-8a2c-e5261464f190 | -9.19773 | -44.73353 | 2024-11-20 12:10:00 | TERRA_M-T | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 102.0 |
| 8d72fbfe-b85e-3867-aacb-86b3f84389cc | -8.61705 | -40.79715 | 2024-11-20 12:10:00 | TERRA_M-T | AFRÂNIO | PERNAMBUCO | Brasil | 2600203 | 26 | 33 | nan | nan | nan | Caatinga | 10.0 |
| 9c769a3f-bd00-305c-abe4-96dafccb37c4 | -9.81006 | -41.71284 | 2024-11-20 12:10:00 | TERRA_M-T | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 10.7 |
| dca7f2c4-5a9e-3e6d-a56a-56a78228fbca | -7.58521 | -37.78251 | 2024-11-20 12:10:00 | TERRA_M-T | JURU | PARAÍBA | Brasil | 2508000 | 25 | 33 | nan | nan | nan | Caatinga | 11.3 |
| 71b1e719-465b-3a96-8636-c74ea3642eae | -9.41677 | -40.69202 | 2024-11-20 12:10:00 | TERRA_M-T | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 16.9 |
| 688c9e81-a5d1-358e-a458-edbb5bdda715 | -8.04575 | -37.52832 | 2024-11-20 12:10:00 | TERRA_M-T | CUSTÓDIA | PERNAMBUCO | Brasil | 2605103 | 26 | 33 | nan | nan | nan | Caatinga | 11.7 |
| fef4d1e1-f62f-374e-836e-b495ea867e45 | -10.6982 | -40.33069 | 2024-11-20 12:10:00 | TERRA_M-T | PINDOBAÇU | BAHIA | Brasil | 2924603 | 29 | 33 | nan | nan | nan | Caatinga | 12.3 |
| 04f5902e-a8a2-37aa-956c-74e8005d0704 | -10.69577 | -40.97339 | 2024-11-20 12:10:00 | TERRA_M-T | MIRANGABA | BAHIA | Brasil | 2921401 | 29 | 33 | nan | nan | nan | Caatinga | 13.3 |
| bc0e5934-3af3-398a-bbc5-4f0b9782b558 | -7.11984 | -41.67666 | 2024-11-20 12:10:00 | TERRA_M-T | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 20.8 |
| 59cc6ca4-b0df-3935-80c1-525c8293235d | -8.16876 | -39.38661 | 2024-11-20 12:10:00 | TERRA_M-T | TERRA NOVA | PERNAMBUCO | Brasil | 2615201 | 26 | 33 | nan | nan | nan | Caatinga | 14.0 |
| f70d4975-1d63-3ebc-aa06-42d08fc18c29 | -7.86348 | -38.09677 | 2024-11-20 12:10:00 | TERRA_M-T | TRIUNFO | PERNAMBUCO | Brasil | 2615706 | 26 | 33 | nan | nan | nan | Caatinga | 15.9 |
| 2cb65458-4a08-3d31-9d5e-1f950d8c6f00 | -9.79941 | -41.97562 | 2024-11-20 12:10:00 | TERRA_M-T | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 29.9 |
| 3e5d2f50-8ca4-3e93-8957-db12a8bf1f3c | -10.45846 | -40.3865 | 2024-11-20 12:10:00 | TERRA_M-T | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 27.7 |
| d9e5a54a-f4b0-3d3f-b6d5-69364d19df28 | -8.85682 | -40.42439 | 2024-11-20 12:10:00 | TERRA_M-T | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 10.3 |
| 4fb12137-e3b0-356f-976e-16ae5753601b | -8.74249 | -40.51245 | 2024-11-20 12:10:00 | TERRA_M-T | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 14.8 |
| b2fa246b-5b3d-3fd4-ae60-dbfd52296113 | -7.97577 | -37.16887 | 2024-11-20 12:10:00 | TERRA_M-T | MONTEIRO | PARAÍBA | Brasil | 2509701 | 25 | 33 | nan | nan | nan | Caatinga | 10.2 |
| af4a4e76-ac5c-3984-b06b-92dadd27848c | -9.13575 | -43.05378 | 2024-11-20 12:10:00 | TERRA_M-T | ANÍSIO DE ABREU | PIAUÍ | Brasil | 2200707 | 22 | 33 | nan | nan | nan | Caatinga | 8.2 |
| 48489040-24aa-39cf-9ce1-98bff82933c7 | -10.45977 | -40.37756 | 2024-11-20 12:10:00 | TERRA_M-T | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 29.3 |
| 2529ef2d-a402-308a-95cd-60a080bedbb3 | -8.75219 | -37.26854 | 2024-11-20 12:10:00 | TERRA_M-T | TUPANATINGA | PERNAMBUCO | Brasil | 2615805 | 26 | 33 | nan | nan | nan | Caatinga | 33.6 |
| 07aff2ac-5c64-3a4a-a172-fc04f7c20402 | -10.69713 | -40.96423 | 2024-11-20 12:10:00 | TERRA_M-T | MIRANGABA | BAHIA | Brasil | 2921401 | 29 | 33 | nan | nan | nan | Caatinga | 9.5 |
| 067b2980-a722-3208-9567-7678daadece2 | -9.10205 | -40.4449 | 2024-11-20 12:10:00 | TERRA_M-T | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 9.4 |
| 7934f4e3-954a-3916-a1e9-326a208114c4 | -8.83292 | -36.44174 | 2024-11-20 12:10:00 | TERRA_M-T | SÃO JOÃO | PERNAMBUCO | Brasil | 2613206 | 26 | 33 | nan | nan | nan | Mata Atlântica | 13.0 |
| 7e3d4aea-39bd-37b4-a7e7-a029067565b0 | -8.38107 | -41.52062 | 2024-11-20 12:10:00 | TERRA_M-T | LAGOA DO BARRO DO PIAUÍ | PIAUÍ | Brasil | 2205565 | 22 | 33 | nan | nan | nan | Caatinga | 9.8 |
| e66f8b84-e39f-358e-8dc9-3701a9ef6755 | -7.58653 | -37.7731 | 2024-11-20 12:10:00 | TERRA_M-T | JURU | PARAÍBA | Brasil | 2508000 | 25 | 33 | nan | nan | nan | Caatinga | 7.2 |
| 40508db3-d8fd-3ac0-af38-46d8674a15b1 | -8.84658 | -40.43213 | 2024-11-20 12:10:00 | TERRA_M-T | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 14.0 |
| 68011563-abb8-32a8-8ff7-cdfdde81c131 | -10.46184 | -38.42727 | 2024-11-20 12:10:00 | TERRA_M-T | CÍCERO DANTAS | BAHIA | Brasil | 2907806 | 29 | 33 | nan | nan | nan | Caatinga | 11.3 |
| b3910a97-6afc-3ae3-a57d-4a22d24dae93 | -10.67657 | -41.34873 | 2024-11-20 12:10:00 | TERRA_M-T | UMBURANAS | BAHIA | Brasil | 2932457 | 29 | 33 | nan | nan | nan | Caatinga | 8.2 |
| e3c99b0e-1132-3bce-8ce6-1046206dc84d | -7.88491 | -39.37294 | 2024-11-20 12:10:00 | TERRA_M-T | SERRITA | PERNAMBUCO | Brasil | 2614006 | 26 | 33 | nan | nan | nan | Caatinga | 6.7 |
| 9778e827-05b9-3dad-8bb5-65080ddb6c81 | -8.84629 | -37.46254 | 2024-11-20 12:10:00 | TERRA_M-T | MANARI | PERNAMBUCO | Brasil | 2609154 | 26 | 33 | nan | nan | nan | Caatinga | 8.7 |
| 4717caf4-368b-3957-871a-ae486891ddc1 | -7.4597 | -41.19207 | 2024-11-20 12:10:00 | TERRA_M-T | JAICÓS | PIAUÍ | Brasil | 2205201 | 22 | 33 | nan | nan | nan | Caatinga | 12.0 |
| 140a4643-58cc-3285-aa25-24b0aaa60906 | -9.1839 | -44.7374 | 2024-11-20 12:10:00 | TERRA_M-T | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 97.0 |
| 22521aca-ee64-3cd2-8945-40fca445cc51 | -9.58528 | -42.04515 | 2024-11-20 12:10:00 | TERRA_M-T | REMANSO | BAHIA | Brasil | 2926004 | 29 | 33 | nan | nan | nan | Caatinga | 14.8 |
| 50a34c86-d88a-3c46-9f86-ad2c0ba5c696 | -15.88538 | -41.94516 | 2024-11-20 12:12:00 | TERRA_M-T | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 8b4b35ef-ab7e-3962-a692-ae7f1d865e31 | -17.16595 | -40.15495 | 2024-11-20 12:12:00 | TERRA_M-T | ITANHÉM | BAHIA | Brasil | 2916005 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| 5c4fa4f0-5533-397e-a730-e0c557dff1cb | -12.24162 | -38.80919 | 2024-11-20 12:12:00 | TERRA_M-T | CORAÇÃO DE MARIA | BAHIA | Brasil | 2908903 | 29 | 33 | nan | nan | nan | Caatinga | 11.5 |
| 9c3d3a08-c0b4-3651-98df-9c494b92427c | -13.3751 | -43.03669 | 2024-11-20 12:12:00 | TERRA_M-T | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 9.1 |
| 57931d7c-1be8-3348-b769-c92a1717dead | -12.22979 | -38.36464 | 2024-11-20 12:12:00 | TERRA_M-T | ARAÇÁS | BAHIA | Brasil | 2902054 | 29 | 33 | nan | nan | nan | Mata Atlântica | 15.4 |
| 502e9ab7-31de-3178-8f35-854fef94fbf9 | -12.88547 | -42.36945 | 2024-11-20 12:12:00 | TERRA_M-T | IBIPITANGA | BAHIA | Brasil | 2912509 | 29 | 33 | nan | nan | nan | Caatinga | 10.5 |
| 1088c8e4-7239-3606-af31-f1075ba66855 | -12.29354 | -42.51111 | 2024-11-20 12:12:00 | TERRA_M-T | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 7.0 |
| d7732fee-3047-336a-8fd0-c859aa07afac | -14.29416 | -41.72686 | 2024-11-20 12:12:00 | TERRA_M-T | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 6.9 |
| f64d961b-b7a7-35f3-876e-e3a60a99e4b8 | -15.92336 | -42.4348 | 2024-11-20 12:12:00 | TERRA_M-T | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 2f676e38-d1ba-3798-b1fa-c90eed563792 | -13.88282 | -42.86205 | 2024-11-20 12:12:00 | TERRA_M-T | MATINA | BAHIA | Brasil | 2921054 | 29 | 33 | nan | nan | nan | Caatinga | 7.6 |
| f96c7989-84ef-35e6-b02a-0cefb1669205 | -15.39003 | -42.78941 | 2024-11-20 12:12:00 | TERRA_M-T | MATO VERDE | MINAS GERAIS | Brasil | 3141009 | 31 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 8877cd31-dbf6-39ca-8691-7c1885d7248b | -17.84976 | -39.87069 | 2024-11-20 12:12:00 | TERRA_M-T | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| 7ed80e35-1370-31ed-9f59-9f6c6868b587 | -15.9248 | -42.42535 | 2024-11-20 12:12:00 | TERRA_M-T | NOVORIZONTE | MINAS GERAIS | Brasil | 3145372 | 31 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 663baaf2-f907-3fff-a767-1d290acca72d | -12.23253 | -38.80782 | 2024-11-20 12:12:00 | TERRA_M-T | CORAÇÃO DE MARIA | BAHIA | Brasil | 2908903 | 29 | 33 | nan | nan | nan | Caatinga | 12.1 |
| 07a970e8-d6d3-3e21-9891-2c0065701f59 | -13.7753 | -41.55351 | 2024-11-20 12:12:00 | TERRA_M-T | RIO DE CONTAS | BAHIA | Brasil | 2926707 | 29 | 33 | nan | nan | nan | Caatinga | 7.4 |
| 3112752d-dd3b-3687-b96f-d2ce8046b419 | -12.84138 | -42.55084 | 2024-11-20 12:12:00 | TERRA_M-T | BOQUIRA | BAHIA | Brasil | 2904100 | 29 | 33 | nan | nan | nan | Caatinga | 22.1 |
| 55013794-a1d7-3e99-b928-00c08930eed9 | -13.88125 | -42.87232 | 2024-11-20 12:12:00 | TERRA_M-T | MATINA | BAHIA | Brasil | 2921054 | 29 | 33 | nan | nan | nan | Caatinga | 8.9 |
| 3b933ca7-08ab-351a-b1d9-de1cc6d8f97b | -12.83986 | -42.5609 | 2024-11-20 12:12:00 | TERRA_M-T | BOQUIRA | BAHIA | Brasil | 2904100 | 29 | 33 | nan | nan | nan | Caatinga | 12.6 |
| b75b7c87-c81d-39c7-83f2-3b8a4450b995 | -12.29201 | -42.52126 | 2024-11-20 12:12:00 | TERRA_M-T | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 8.8 |
| 670aeebf-1b05-3aef-971f-3999b3a68328 | -11.44024 | -42.28134 | 2024-11-20 12:12:00 | TERRA_M-T | IBIPEBA | BAHIA | Brasil | 2912400 | 29 | 33 | nan | nan | nan | Caatinga | 12.8 |
| 61b7c048-67df-3c71-b9d9-9e4152ce54a9 | -14.2254 | -41.56837 | 2024-11-20 12:12:00 | TERRA_M-T | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 28.3 |
| ca366027-3ad8-3e9a-b6e6-587f84a8e789 | -14.40727 | -40.75813 | 2024-11-20 12:12:00 | TERRA_M-T | CAETANOS | BAHIA | Brasil | 2905156 | 29 | 33 | nan | nan | nan | Caatinga | 7.4 |
| 1d252658-659a-3ce8-a410-f03bc925aef5 | -20.13296 | -41.46737 | 2024-11-20 12:14:00 | TERRA_M-T | LAJINHA | MINAS GERAIS | Brasil | 3137700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 13.5 |
| 663d3da0-0567-3114-9fae-2dd1316267d6 | -20.5804 | -41.62566 | 2024-11-20 12:14:00 | TERRA_M-T | ALEGRE | ESPÍRITO SANTO | Brasil | 3200201 | 32 | 33 | nan | nan | nan | Mata Atlântica | 6.2 |
| d79ec282-9b40-3baa-b5a4-901585567b0c | -20.38637 | -42.52126 | 2024-11-20 12:14:00 | TERRA_M-T | JEQUERI | MINAS GERAIS | Brasil | 3135506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| eecfcb6c-ace1-3f9e-b9b7-6ccf2a7498e7 | -20.8724 | -41.8352 | 2024-11-20 12:14:00 | TERRA_M-T | VARRE-SAI | RIO DE JANEIRO | Brasil | 3306156 | 33 | 33 | nan | nan | nan | Mata Atlântica | 6.4 |
| c01a3351-c4f0-3462-8876-7c9c5c2ddaff | -1.6556 | -47.2661 | 2024-11-20 12:20:00 | GOES-16 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 127.6 |
| 9050ed4e-9525-38b1-a8c2-c0f5957b5be4 | -6.9421 | -41.1859 | 2024-11-20 12:30:00 | GOES-16 | SANTO ANTÔNIO DE LISBOA | PIAUÍ | Brasil | 2209401 | 22 | 33 | nan | nan | nan | Caatinga | 85.8 |
| a4b63f1f-d2b5-3567-ac97-afc797808703 | -3.3739 | -44.4247 | 2024-11-20 12:30:00 | GOES-16 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 120.7 |
| 04784dc1-4f4f-39b8-a726-5401342f933f | -3.3925 | -44.4239 | 2024-11-20 12:30:00 | GOES-16 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 108.8 |
| 47dba46d-2ff6-3403-9809-8156a0fddfc3 | -7.1944 | -39.1048 | 2024-11-20 12:40:00 | GOES-16 | MISSÃO VELHA | CEARÁ | Brasil | 2308401 | 23 | 33 | nan | nan | nan | Caatinga | 100.6 |
| 0fbf0b0b-f720-3dbc-a880-7da41025d184 | -7.1941 | -39.1301 | 2024-11-20 12:40:00 | GOES-16 | MISSÃO VELHA | CEARÁ | Brasil | 2308401 | 23 | 33 | nan | nan | nan | Caatinga | 88.5 |
| 06009f7e-3729-3924-9868-871beb37726c | -3.4802 | -42.045 | 2024-11-20 12:40:00 | GOES-16 | MURICI DOS PORTELAS | PIAUÍ | Brasil | 2206696 | 22 | 33 | nan | nan | nan | Caatinga | 119.7 |
| 38187730-f173-340d-b0c1-83d685b8ff03 | -6.9421 | -41.1859 | 2024-11-20 12:40:00 | GOES-16 | SANTO ANTÔNIO DE LISBOA | PIAUÍ | Brasil | 2209401 | 22 | 33 | nan | nan | nan | Caatinga | 98.1 |
| 4cd81cb7-334d-33db-ab23-84f9792b1490 | -3.3739 | -44.4247 | 2024-11-20 12:40:00 | GOES-16 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 111.0 |
| 96d1da25-99eb-3c68-ab4e-2f2c5c2a207c | -3.5174 | -42.0669 | 2024-11-20 12:40:00 | GOES-16 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 144.8 |
| deb1a10c-352c-3bf5-8df0-0d6f3e2ccba5 | -7.1941 | -39.1301 | 2024-11-20 12:50:00 | GOES-16 | MISSÃO VELHA | CEARÁ | Brasil | 2308401 | 23 | 33 | nan | nan | nan | Caatinga | 91.7 |
| 3ec9f0f3-5078-3120-ae13-df974aa5b8cd | -3.4802 | -42.045 | 2024-11-20 12:50:00 | GOES-16 | MURICI DOS PORTELAS | PIAUÍ | Brasil | 2206696 | 22 | 33 | nan | nan | nan | Caatinga | 95.4 |
| b9327048-09b1-3588-b7b8-ca699dcf22ee | -7.1944 | -39.1048 | 2024-11-20 12:50:00 | GOES-16 | MISSÃO VELHA | CEARÁ | Brasil | 2308401 | 23 | 33 | nan | nan | nan | Caatinga | 108.2 |
| 2fd122d0-5a34-3ae1-93e5-8427cadff77f | -3.5361 | -42.066 | 2024-11-20 13:00:00 | GOES-16 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 135.4 |
| 715da34b-a3ee-3c05-9295-a905ad246f98 | -7.1944 | -39.1048 | 2024-11-20 13:00:00 | GOES-16 | MISSÃO VELHA | CEARÁ | Brasil | 2308401 | 23 | 33 | nan | nan | nan | Caatinga | 139.0 |
| f4f4001d-45e0-37ec-8fc2-b96bebb1f54f | -7.1941 | -39.1301 | 2024-11-20 13:00:00 | GOES-16 | MISSÃO VELHA | CEARÁ | Brasil | 2308401 | 23 | 33 | nan | nan | nan | Caatinga | 110.8 |


[Clique aqui para ver as próximas entradas](README78.md)
