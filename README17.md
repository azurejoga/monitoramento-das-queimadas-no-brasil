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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 626039a8-8b61-3a29-8016-4ddbacfc3ef3 | -8.57113 | -54.67377 | 2025-08-11 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a62107d0-86fb-3293-8b33-d399246f1e15 | -7.28678 | -44.53093 | 2025-08-11 04:25:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 29d47ddf-501a-3c77-8516-41ba3a2f575d | -8.57016 | -54.67905 | 2025-08-11 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0ea43f06-3dec-34d9-9897-ff23651f0d7b | -7.21904 | -46.23308 | 2025-08-11 04:25:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b6868a2e-9836-3b03-826d-338cb9d2e899 | -7.05166 | -59.17946 | 2025-08-11 04:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c33e9f1c-9c99-3bde-aa31-169d193c829b | -6.28746 | -43.71383 | 2025-08-11 04:25:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a1688eea-d898-3fe3-b890-48becc042267 | -7.08092 | -59.19351 | 2025-08-11 04:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 13324949-cf6d-35c4-b9eb-5a2fa8fceece | -3.76036 | -51.87009 | 2025-08-11 04:25:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 192a709a-f64e-3479-bc8a-50d75b2ef770 | -7.05399 | -59.20359 | 2025-08-11 04:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 103e701b-c796-3cda-897d-49154e667ccb | -6.93041 | -42.96632 | 2025-08-11 04:25:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 3d257a78-ca8c-312f-9ff4-232c448f4fe2 | -6.58257 | -44.55618 | 2025-08-11 04:25:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| d6bb5930-932c-30e0-8300-358658549fcd | -8.56613 | -54.68154 | 2025-08-11 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6d98f8b5-8e3f-37d8-8988-5caa2a0ae96a | -7.33712 | -45.27654 | 2025-08-11 04:25:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 99253530-3b89-34da-9963-15c9b88f4beb | -7.12281 | -44.23163 | 2025-08-11 04:25:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 901c9099-f1c0-3ac7-b847-70c26ef2abb9 | -6.97225 | -43.08741 | 2025-08-11 04:25:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b47f6b4d-6f5a-36b4-a957-2c3501d40fb8 | -4.29979 | -48.07142 | 2025-08-11 04:25:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c88531dc-9b51-3465-b32e-21b6d2e410e2 | -8.56239 | -54.7029 | 2025-08-11 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| c04181af-9002-33ba-b835-c31d508b53f2 | -7.06389 | -59.18722 | 2025-08-11 04:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4d269250-ee40-3faf-acab-b1bd7b9aa88d | -6.29328 | -43.72289 | 2025-08-11 04:25:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c3906bb4-b0b8-3119-9c52-a7919fa59b4a | -8.57189 | -54.67714 | 2025-08-11 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 18839579-637d-3bd4-93d7-3589fe8271e2 | -10.24012 | -48.26097 | 2025-08-11 04:25:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 253f8598-e01e-35d4-bf2e-dac9c2cdcbd5 | -6.97663 | -44.79568 | 2025-08-11 04:25:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| aad9d5ff-41d0-330a-b50e-e6f42cdbd4a6 | -6.28279 | -43.69711 | 2025-08-11 04:25:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 082e6f63-a950-3d1b-b934-3df1af82847b | -7.06802 | -59.16507 | 2025-08-11 04:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9931a368-2172-34cc-85c5-0490ed815495 | -10.36189 | -46.63329 | 2025-08-11 04:25:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 697ce32f-a738-3425-a765-275faeb0530d | -8.56427 | -54.69217 | 2025-08-11 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 61f34a55-7014-3848-a2ea-ff820d8b9c34 | -7.42999 | -43.7616 | 2025-08-11 04:25:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 97c4c527-39d2-3d82-bcbf-32ffd325ddb7 | -9.64345 | -43.83646 | 2025-08-11 04:25:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| ed9d20a2-87ce-3a22-a145-8056ec382bac | -6.58655 | -44.553 | 2025-08-11 04:25:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0aa94f4b-0941-3c7e-91e2-3f12517e4390 | -8.03902 | -44.78443 | 2025-08-11 04:25:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c027c157-9c03-308f-8df9-6773f5de667a | -9.64408 | -43.83216 | 2025-08-11 04:25:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 3.6 |
| c73f1a90-af7a-3103-bad0-49246b939d21 | -9.21477 | -44.53144 | 2025-08-11 04:25:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8de65e31-2826-3a88-80c5-0cfe7b81ccdb | -6.5877 | -44.56826 | 2025-08-11 04:25:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7e17e106-511d-3aa9-836a-b5d04d11a7ac | -7.2816 | -44.5874 | 2025-08-11 04:25:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 391e39b3-2888-3618-86ae-c87a886e412d | -6.97607 | -44.79937 | 2025-08-11 04:25:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2032a3d7-a0f0-3afe-afa5-a448c0367d8f | -9.22826 | -48.52907 | 2025-08-11 04:25:00 | NOAA-20 | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 95978583-2871-3763-bcbe-90ba9c6ed285 | -10.37269 | -50.83565 | 2025-08-11 04:25:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 08ab484e-9a8a-39e3-899b-d9037b1fedaa | -8.03905 | -44.78463 | 2025-08-11 04:25:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7d806c38-cebe-346d-959e-e6accb3ef464 | -6.96344 | -44.21543 | 2025-08-11 04:25:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e8b5c4aa-1277-3cf2-95ba-bd98837a17cd | -8.56706 | -54.67624 | 2025-08-11 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 94b92f50-9ba1-3f2d-8037-3abb58eb811f | -10.36979 | -50.80817 | 2025-08-11 04:25:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| acc28954-7bc8-3759-90e3-a1b1de2885ca | -7.55377 | -49.61214 | 2025-08-11 04:25:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 37529c3f-aef0-3e8b-b8e7-908e1ad5d584 | -7.13093 | -44.22507 | 2025-08-11 04:25:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7e76d3df-2cb8-3615-b8ff-fd961ffa7b2a | -7.0781 | -59.18435 | 2025-08-11 04:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 33dd3f1f-d6b8-32b9-adcc-baade9efe6c3 | -4.11055 | -48.2062 | 2025-08-11 04:25:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 42fc5138-85e9-3077-a61f-9fcbedcc87c6 | -8.5613 | -54.68065 | 2025-08-11 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 15208a06-6a5c-353c-bb42-e821fb05581f | -7.07466 | -59.16608 | 2025-08-11 04:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cd74e467-ce1b-3b8a-b0e2-6c202d6d8c2c | -6.29036 | -43.7184 | 2025-08-11 04:25:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fc66408e-0db6-337b-b643-db471e29e876 | -7.87362 | -44.97239 | 2025-08-11 04:25:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c22c88c3-ef5f-30d0-808f-11435ff4bb69 | -6.57802 | -44.56307 | 2025-08-11 04:25:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 11.3 |
| bb0613d0-6d2c-3e51-ba70-27bfc6d3d80f | -7.07376 | -59.20769 | 2025-08-11 04:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.8 |
| ee029ce3-831b-3e03-9b2b-e6f12f24c8d4 | -4.77708 | -42.72329 | 2025-08-11 04:25:00 | NOAA-20 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8cab3db8-45f4-3a8f-8eb4-90965d015b18 | -10.37271 | -50.81318 | 2025-08-11 04:25:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| b88fc619-5cf8-3983-a242-24d1c544584e | -7.05728 | -59.18598 | 2025-08-11 04:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 39893a01-b30a-3e14-b586-20470226723f | -7.07979 | -59.19936 | 2025-08-11 04:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 362084f0-1e07-31a4-ba08-74f55d82a002 | -8.56046 | -54.70478 | 2025-08-11 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| e1ad0dcd-aef7-3111-8202-36f7ce1f27cf | -4.11464 | -48.20292 | 2025-08-11 04:25:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 21c91c1d-0067-348f-b165-9d0b11b3da7e | -10.35814 | -46.63612 | 2025-08-11 04:25:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 378a6e12-7784-3744-bf10-587368f803ba | -6.28864 | -43.70605 | 2025-08-11 04:25:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2797a074-d7a8-3e3e-8ebd-036f5ee61c06 | -11.04766 | -43.27026 | 2025-08-11 04:25:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 7f640716-e1cc-3a17-aa29-f21332af5731 | -11.94444 | -43.39289 | 2025-08-11 04:25:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| c2b48866-fb97-3268-a854-2386dc855897 | -8.30208 | -44.98748 | 2025-08-11 04:25:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c8b8a1f6-20de-3744-9c3c-f6e46f75cdea | -7.07594 | -59.19596 | 2025-08-11 04:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| adb47cf9-2550-33f1-8c79-58f58fad88a4 | -8.57306 | -54.69054 | 2025-08-11 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0d9b940c-ca64-30d9-b28c-d0d604c549fb | -14.4819 | -47.07124 | 2025-08-11 04:27:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 009b8e9e-ae35-35c8-aac2-0d1aab55f0d7 | -13.64651 | -48.99501 | 2025-08-11 04:27:00 | NOAA-20 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b431d2fa-f542-3a93-b483-8ac1d8c386db | -12.24337 | -45.05815 | 2025-08-11 04:27:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 859a7b3f-47dd-3cca-907b-7a1e1379eb30 | -16.37522 | -42.53169 | 2025-08-11 04:27:00 | NOAA-20 | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 20bc34f5-853c-3f0c-b25c-0ac61461d4a6 | -15.44512 | -53.93704 | 2025-08-11 04:27:00 | NOAA-20 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 6.9 |
| aa46867b-7f7f-3f3b-98e0-0425dfdedd15 | -18.93146 | -45.73017 | 2025-08-11 04:27:00 | NOAA-20 | TIROS | MINAS GERAIS | Brasil | 3168903 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f7972093-6289-39ca-aa48-a3fc787cc497 | -18.17428 | -47.0115 | 2025-08-11 04:27:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 2f7012e0-8246-363f-bd02-afa3fb59ce6a | -12.55252 | -47.06416 | 2025-08-11 04:27:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9b7dfeb6-a363-38ad-b2ea-2289bb9a62c6 | -11.7778 | -49.56863 | 2025-08-11 04:27:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 9f2e19bf-1143-3b27-b7d1-ddd9ded55783 | -15.44853 | -53.94161 | 2025-08-11 04:27:00 | NOAA-20 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 5b41e705-b9bb-3a83-a600-5e8f51a92367 | -19.16734 | -44.53187 | 2025-08-11 04:27:00 | NOAA-20 | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ab9eae86-923a-3623-9274-305c5f4ad69c | -11.4392 | -50.60216 | 2025-08-11 04:27:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 13b456a7-2315-30f6-a526-67913af72492 | -11.78185 | -49.56541 | 2025-08-11 04:27:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d9fe762b-d61b-3130-aaa3-49c34223f270 | -19.41476 | -43.36829 | 2025-08-11 04:27:00 | NOAA-20 | ITAMBÉ DO MATO DENTRO | MINAS GERAIS | Brasil | 3132800 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 66440ef5-0857-37c6-959f-de151c17fa92 | -14.11027 | -45.39997 | 2025-08-11 04:27:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9787f77d-3a6d-34ad-99e8-1bd15afe0199 | -13.345 | -52.25736 | 2025-08-11 04:27:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| dfd29f1e-6ab2-35d1-a422-ab68ef6318e5 | -15.41515 | -53.9157 | 2025-08-11 04:27:00 | NOAA-20 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ddd49473-3a94-38cd-9234-fb611d1d6ea0 | -12.5492 | -47.06362 | 2025-08-11 04:27:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 471dbe9e-36cc-34ef-b99d-4555088c1ff2 | -18.32591 | -43.68007 | 2025-08-11 04:27:00 | NOAA-20 | DATAS | MINAS GERAIS | Brasil | 3121001 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fff3789f-e700-3019-ab8b-527881d8b5a2 | -12.6103 | -47.1278 | 2025-08-11 04:27:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2891cf3d-e121-37b2-a9e8-46f15690865c | -11.77488 | -47.39158 | 2025-08-11 04:27:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 17948302-5883-33f8-858e-d94280b59b65 | -16.40721 | -42.58894 | 2025-08-11 04:27:00 | NOAA-20 | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9779f822-1631-38fb-bce5-56b55e03c9e7 | -11.92706 | -49.55823 | 2025-08-11 04:27:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d3fd7416-fd67-3b10-8aa9-2e257d28e758 | -11.76094 | -49.11493 | 2025-08-11 04:27:00 | NOAA-20 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d3f237ee-ad4b-3b6d-bdff-6346a3116de8 | -15.44827 | -53.93752 | 2025-08-11 04:27:00 | NOAA-20 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 21ad0e7b-361b-3224-a4f9-dcb7c7f94079 | -15.41447 | -53.91946 | 2025-08-11 04:27:00 | NOAA-20 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ee83a204-555a-3f62-a514-fc89dfcb78b6 | -15.42264 | -53.92102 | 2025-08-11 04:27:00 | NOAA-20 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 32.5 |
| 3174964d-9533-347d-a37c-b45ab614d915 | -19.41531 | -43.36388 | 2025-08-11 04:27:00 | NOAA-20 | ITAMBÉ DO MATO DENTRO | MINAS GERAIS | Brasil | 3132800 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cffb0935-a882-3517-ad05-52afe7003f04 | -18.6119 | -46.85996 | 2025-08-11 04:27:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 68b7f4b1-fca4-3468-a1d4-808276ee8c14 | -11.71665 | -50.10999 | 2025-08-11 04:27:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5e07f0ca-c9b6-37c8-9d80-bc1022d632b9 | -16.21219 | -49.98428 | 2025-08-11 04:27:00 | NOAA-20 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cfed695e-35d8-3601-9891-a45fa5c45554 | -11.76034 | -49.11861 | 2025-08-11 04:27:00 | NOAA-20 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7b6d8b8d-75a3-38c9-a7b4-43cb88617d31 | -15.4308 | -53.9226 | 2025-08-11 04:27:00 | NOAA-20 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 69.3 |
| ff9ba76c-1fcd-35ff-b0e3-1a0b459c26a4 | -15.42195 | -53.92479 | 2025-08-11 04:27:00 | NOAA-20 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 40.4 |
| 8e058737-fbf3-39c6-8eeb-ac6c35dbba47 | -15.57398 | -43.4133 | 2025-08-11 04:27:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 89c5c56e-7a27-3060-b3c7-e2ba6c019426 | -11.77764 | -47.39563 | 2025-08-11 04:27:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |


[Clique aqui para ver as próximas entradas](README18.md)
