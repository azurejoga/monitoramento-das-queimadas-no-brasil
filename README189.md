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

## Dados Diários - Página 189

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d61334dd-3d23-3973-80d2-40ced6b78e82 | -9.36162 | -68.19999 | 2024-10-03 06:08:00 | NOAA-21 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 71100d61-3768-3acd-b8c5-d88a0013682c | -9.36095 | -68.20468 | 2024-10-03 06:08:00 | NOAA-21 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c144d240-ce51-30fa-8722-4f24a46fa195 | -9.36028 | -68.20937 | 2024-10-03 06:08:00 | NOAA-21 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2c485de8-50c3-3f42-8375-77b9b039b0ea | -9.35783 | -68.19942 | 2024-10-03 06:08:00 | NOAA-21 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4f25ef5c-5355-38a6-b929-544c79379efc | -9.35716 | -68.2041 | 2024-10-03 06:08:00 | NOAA-21 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 608c01b6-a560-3b41-84bc-7bf7d6dbce05 | -9.35649 | -68.20879 | 2024-10-03 06:08:00 | NOAA-21 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 67788769-f592-3326-bd25-a96f54daeef3 | -9.35337 | -68.20354 | 2024-10-03 06:08:00 | NOAA-21 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9b7ba0c0-7456-3845-a48c-9ce8b79927c7 | -9.34205 | -68.22846 | 2024-10-03 06:08:00 | NOAA-21 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 950d89be-5962-3135-950b-4c2a3626732a | -9.34136 | -68.23311 | 2024-10-03 06:08:00 | NOAA-21 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 39713814-488c-3036-9609-1cc6bddfaafe | -9.32915 | -68.23801 | 2024-10-03 06:08:00 | NOAA-21 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 735bb4e7-8869-318d-bba2-df7f160b3753 | -9.32865 | -68.24066 | 2024-10-03 06:08:00 | NOAA-21 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 6ce220d9-dfb1-3eec-9256-59bb50e1eed2 | -9.3285 | -68.24264 | 2024-10-03 06:08:00 | NOAA-21 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 15bb39b2-018d-3bfd-bf1e-3944b33e89a7 | -9.32589 | -68.20696 | 2024-10-03 06:08:00 | NOAA-21 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5b7e6b65-4568-37f6-9a7c-9ea45ace92ed | -9.32487 | -68.24008 | 2024-10-03 06:08:00 | NOAA-21 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c1a18a39-b3c1-3d73-8a5e-f684d490d276 | -9.11885 | -67.89999 | 2024-10-03 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9238a0f2-e7f0-3a05-845f-f1a1a01cf1b7 | -9.11815 | -67.90482 | 2024-10-03 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 32ecea7b-0d68-330b-99d2-5e817d5b530c | -9.11345 | -67.46606 | 2024-10-03 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 67d1a862-cf95-3506-8a60-284fd2b82891 | -9.11255 | -67.46719 | 2024-10-03 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7b618eb3-9e56-3e9c-8ab7-95b1f7bab6c0 | -9.10544 | -67.54819 | 2024-10-03 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6ef2db57-4c47-36e0-9be7-b13f9ca4c372 | -9.1047 | -67.55324 | 2024-10-03 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 24b838f9-716a-3074-95f0-1b49e3e9acc4 | -9.10277 | -67.5115 | 2024-10-03 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 7d22fa65-7319-313f-9b1f-b52d6b147ad7 | -9.10203 | -67.51659 | 2024-10-03 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1bf047ca-0f46-34c2-a608-96900d9f94d0 | -9.09883 | -67.51093 | 2024-10-03 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 16030388-3312-31ac-bda6-aa4e2938a588 | -9.09809 | -67.51602 | 2024-10-03 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 00cf4def-7662-337b-b346-a865969c2da0 | -9.09758 | -67.54703 | 2024-10-03 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 2c4d2700-966d-3cf5-8d80-2fc9faa23684 | -9.09563 | -67.50526 | 2024-10-03 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 04d9f947-06a8-3574-a4cc-ed24ea027dfd | -9.09489 | -67.51037 | 2024-10-03 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 0512010f-9835-33fa-bfa1-524ce233cef7 | -9.09415 | -67.51545 | 2024-10-03 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| d53eb7d3-c345-3004-87cd-642a31b2ed96 | -9.09341 | -67.52052 | 2024-10-03 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 087d211a-bf2f-35a0-8499-003002266e6a | -9.09046 | -67.54079 | 2024-10-03 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e5dbc8f4-bac7-3978-8631-91ce9ba4e710 | -9.08972 | -67.54585 | 2024-10-03 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 7ecc2210-3bcb-344f-8e68-e5271056070c | -9.08531 | -67.57614 | 2024-10-03 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| c037b883-f5f8-37c1-b749-1be3f028439b | -9.08138 | -67.57556 | 2024-10-03 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 2252195a-e6e0-375b-a070-f6c9ec8f88a2 | -9.07997 | -67.66737 | 2024-10-03 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 4cfabf1c-a926-38bc-8ff8-0ca7f998a3f1 | -9.07924 | -67.67236 | 2024-10-03 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 1fd2e218-c30b-3df5-a615-8d0a938729bb | -9.05822 | -67.85625 | 2024-10-03 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2b2576d6-4e08-3d0b-a246-479120147b77 | -9.05753 | -67.86111 | 2024-10-03 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 35260438-7302-3548-a142-32984fbc1699 | -9.05685 | -67.86595 | 2024-10-03 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 89f7ebcf-fb78-38c2-b0d2-e600b40eab36 | -9.05575 | -67.85922 | 2024-10-03 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| e3ee44b8-3b2d-353c-8b69-50a4a86a2604 | -9.05504 | -67.86405 | 2024-10-03 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| f698b73f-4712-3f69-8271-e43ec19d81e7 | -9.05476 | -67.50959 | 2024-10-03 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2088271e-7df3-32f9-86cc-e251fe750c5f | -9.05119 | -67.86347 | 2024-10-03 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| e9a3dbf9-d169-395f-a307-3e1c13db41dc | -9.05048 | -67.8683 | 2024-10-03 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 93d80793-b1d2-385e-a086-5771282db5a7 | -9.04734 | -67.86289 | 2024-10-03 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 21.6 |
| 9d33752f-be15-3a14-9f7f-934596a43ce6 | -9.04663 | -67.86772 | 2024-10-03 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 21.6 |
| c6a7345a-1392-33cc-9c8a-3abe9c05cb36 | -9.045 | -67.798 | 2024-10-03 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 66b780e9-fefd-3007-831c-9257d96b19dc | -9.04439 | -67.49763 | 2024-10-03 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 05adcc70-39f5-38af-9ad6-ed35aed6bc40 | -9.04367 | -67.50272 | 2024-10-03 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 680eb92b-96dc-3d5f-ae88-319b5aab0a6a | -9.04045 | -67.49704 | 2024-10-03 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c1ad68fa-f378-33c7-bede-8381ccc688a6 | -9.03401 | -67.48569 | 2024-10-03 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 97b0a32d-79ad-3831-af5e-b8155cfd9e5e | -9.02111 | -67.74437 | 2024-10-03 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 71f67833-3a69-309a-b026-f22e6b663356 | -9.01723 | -67.74377 | 2024-10-03 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 0dfe7c94-f233-322d-b7e2-7d1f49859c6e | -9.01686 | -67.3865 | 2024-10-03 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8297e7d7-e9cc-3bb5-94f0-c37ae2803832 | -9.01653 | -67.7487 | 2024-10-03 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 78f87b2b-8132-3b5a-b89d-831a4a28c84b | -9.01603 | -67.38335 | 2024-10-03 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 816a7e69-bf2e-3c3f-82b2-87760df97f24 | -9.01335 | -67.74319 | 2024-10-03 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 37dd6d55-3097-3c66-92dc-9eaca831b9d4 | -9.0129 | -67.38593 | 2024-10-03 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b8cea8d7-eb57-3ad2-98ee-513951475567 | -9.00789 | -67.52841 | 2024-10-03 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 848d3002-1c7a-3ea6-b681-293551649114 | -9.00772 | -67.53118 | 2024-10-03 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 29dba34a-d395-3473-b20c-69f5a7120af3 | -8.99967 | -67.81113 | 2024-10-03 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f21ae6a4-ff05-365b-9e95-e63af2ef860e | -8.99581 | -67.81054 | 2024-10-03 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9b8c4c63-a6b5-3d6b-a102-d58ad8787de5 | -8.99256 | -67.41443 | 2024-10-03 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d4381a63-910a-3a0c-b0de-fb9ada71db1a | -9.4619 | -68.52223 | 2024-10-03 06:08:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ce1f882b-4def-3ca5-a9c1-bc6cbb15b6dd | -8.99008 | -67.40356 | 2024-10-03 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 14.5 |
| 4ff5110d-c0ef-329d-ae94-60454a1fe6f6 | -8.98934 | -67.4087 | 2024-10-03 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 17.9 |
| 5d521d6c-3e97-3642-9889-eb3866d498e3 | -8.9886 | -67.41383 | 2024-10-03 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 17.9 |
| 669f4ca7-4d1f-3d71-8670-d20c972b9e7a | -8.98786 | -67.41894 | 2024-10-03 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e1a7bece-1f64-3115-b4a1-9ddc7aaad215 | -8.98538 | -67.4081 | 2024-10-03 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 17.9 |
| bc651b97-8649-3480-8bb1-8465e859e14a | -8.98464 | -67.41325 | 2024-10-03 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 17.9 |
| 524d4052-d108-328b-9eed-149d0c918886 | -9.74827 | -68.41845 | 2024-10-03 06:08:00 | NOAA-21 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 559c1d33-632e-3912-a6dc-206649805b8e | -9.74761 | -68.42307 | 2024-10-03 06:08:00 | NOAA-21 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e968617d-666c-3a1d-8dc8-989c9c7fc851 | -9.74721 | -68.42091 | 2024-10-03 06:08:00 | NOAA-21 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 3ba31142-ae61-37fd-93df-4d07d1d5f99a | -9.74385 | -68.42252 | 2024-10-03 06:08:00 | NOAA-21 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4d7399cd-bc9b-3d04-907c-270105a42af4 | -9.74345 | -68.42036 | 2024-10-03 06:08:00 | NOAA-21 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8a7cc5ed-eb53-340d-b798-20fff94fd190 | -9.7432 | -68.42714 | 2024-10-03 06:08:00 | NOAA-21 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b506f498-63a4-312c-b414-17f74bf8599b | -9.74009 | -68.42195 | 2024-10-03 06:08:00 | NOAA-21 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8b705a53-bb3d-3460-b88b-da9b8dfa4c6c | -9.73944 | -68.42657 | 2024-10-03 06:08:00 | NOAA-21 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 276c5b00-a5ed-34b0-8d4b-142c72d1bc6b | -9.73833 | -68.42903 | 2024-10-03 06:08:00 | NOAA-21 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 966f4b46-0f2a-3108-9986-756312e0073b | -9.73765 | -68.43362 | 2024-10-03 06:08:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.4 |
| de8430a2-253c-3dde-a791-0edb69bb19e1 | -9.73438 | -68.43522 | 2024-10-03 06:08:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 29d581b0-afab-389c-8091-5a2702fff3c8 | -9.73006 | -68.38072 | 2024-10-03 06:08:00 | NOAA-21 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a1dfe820-0374-36ca-ab25-1a6ee27ad1a9 | -9.72629 | -68.38016 | 2024-10-03 06:08:00 | NOAA-21 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 97c839dc-5698-3c22-8bcb-90df6ba40b7f | -9.68153 | -68.80758 | 2024-10-03 06:08:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 260f86a9-3437-3518-b2ad-266e3825ecf1 | -9.67601 | -68.54072 | 2024-10-03 06:08:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 009b31e6-a763-309d-bb18-aafe175730ff | -9.67447 | -68.80862 | 2024-10-03 06:08:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 7fb56fbd-c8fb-3a47-a4c6-07de0abab759 | -9.63804 | -68.64529 | 2024-10-03 06:08:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 25c5a4a2-97ef-3a91-ad47-9717bb0fd223 | -9.59826 | -68.51318 | 2024-10-03 06:08:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f56d5740-977b-35cf-92fa-4a237fbea53b | -9.58697 | -68.58986 | 2024-10-03 06:08:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 24c8be77-cb52-3a25-8b3e-27bc980a960c | -9.58631 | -68.59436 | 2024-10-03 06:08:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 5dcad981-cb39-337c-a8b4-edbe837c328b | -9.58325 | -68.58929 | 2024-10-03 06:08:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 74abe792-143b-387a-8e31-527b8ec85705 | -9.58259 | -68.59381 | 2024-10-03 06:08:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 5a89d691-332d-3b8d-ad8a-2a3838fbb1ff | -9.57954 | -68.58872 | 2024-10-03 06:08:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 332a3180-47d3-3d08-9af5-2220a2e80871 | -9.55498 | -68.46951 | 2024-10-03 06:08:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5433803b-4992-3b3f-8b14-bc4036b86e96 | -9.55186 | -68.27612 | 2024-10-03 06:08:00 | NOAA-21 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c39f9ff4-fa7d-3a25-9df5-c8ed830ed519 | -9.55109 | -68.57542 | 2024-10-03 06:08:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 94845516-4e07-39b0-be41-1ff58fb92f47 | -9.5494 | -68.26623 | 2024-10-03 06:08:00 | NOAA-21 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 3.9 |
| f6a7974e-4c1f-3e3d-b695-f1fd5361056b | -9.54913 | -68.26812 | 2024-10-03 06:08:00 | NOAA-21 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 657fd256-ea4a-3143-bb7b-3319325e4672 | -9.51174 | -68.5049 | 2024-10-03 06:08:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 92e095c2-b174-37a3-8188-7454ca3b3cea | -9.51123 | -68.4462 | 2024-10-03 06:08:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 07e98a47-8a70-3329-83a6-745a63b9ed59 | -9.51064 | -68.50175 | 2024-10-03 06:08:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |


[Clique aqui para ver as próximas entradas](README190.md)
