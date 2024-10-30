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

## Dados Diários - Página 29

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1edc26b8-901b-3ad0-a13b-16f28582a3e2 | -6.6635 | -44.70024 | 2024-10-30 03:28:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 085a1a29-5fd0-3b72-bc39-1aaaad20a948 | -6.66246 | -44.70583 | 2024-10-30 03:28:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 076faaf5-0095-3a7c-943c-fa8f3f2d64ee | -5.97059 | -45.36845 | 2024-10-30 03:28:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 21.2 |
| 14ea23c6-f1ff-3445-a875-63b38c5200b2 | -5.96962 | -45.36805 | 2024-10-30 03:28:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 21.3 |
| 9dfb8dad-c582-3b8b-966b-bb385f6d99b2 | -5.96941 | -45.37498 | 2024-10-30 03:28:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 19.0 |
| d4c63c45-77fa-3f0a-a5d4-38ec6f3f4ac8 | -5.9684 | -45.37455 | 2024-10-30 03:28:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 21.3 |
| ac40fc3c-192a-38a2-ad53-4b7238cf180e | -5.96824 | -45.38147 | 2024-10-30 03:28:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 19.0 |
| e160b16e-ef87-36c9-a7d1-c6af27bb2eac | -5.96719 | -45.381 | 2024-10-30 03:28:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 7e3accd8-959c-362d-b183-85a4043dc93d | -5.55526 | -44.32918 | 2024-10-30 03:28:00 | NOAA-20 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4aa70209-f17d-341e-b792-e808b9a08ae0 | -5.54972 | -44.32234 | 2024-10-30 03:28:00 | NOAA-20 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| f485158a-179a-3552-9faf-810f3152a149 | -5.5487 | -44.32799 | 2024-10-30 03:28:00 | NOAA-20 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 19.7 |
| c390d248-cb75-3766-a545-2f9522f477f1 | -5.46148 | -45.50885 | 2024-10-30 03:28:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| cced8719-1250-331b-8da7-58bd07293d54 | -5.45446 | -45.50747 | 2024-10-30 03:28:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e5301214-17fb-335c-b6b4-b294b8bbba11 | -5.29556 | -44.93924 | 2024-10-30 03:28:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 5a5ae503-c689-318a-b0b7-76b246320301 | -5.2945 | -44.94016 | 2024-10-30 03:28:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| bfcff3d1-754c-3b57-b956-a00eee65447e | -5.2943 | -44.94608 | 2024-10-30 03:28:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 8856ddb3-11ea-322b-9008-5d1172d22441 | -5.29329 | -44.94699 | 2024-10-30 03:28:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| e42f901f-cf14-3c4e-882b-491d61f5ac9c | -5.22098 | -44.91385 | 2024-10-30 03:28:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 966cde82-bd6a-3c0a-a7be-84dbc83b2a37 | -5.21603 | -44.90588 | 2024-10-30 03:28:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c539cb70-f3c8-3b55-8e71-b529719cde71 | -5.21482 | -44.91249 | 2024-10-30 03:28:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 65fb9bce-8d18-3055-8bd9-29372f47fc05 | -5.21417 | -44.91248 | 2024-10-30 03:28:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0145355b-c19b-38bf-9b4a-aaba51cf1e83 | -5.11483 | -45.15153 | 2024-10-30 03:28:00 | NOAA-20 | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ad8eba10-8cf8-34c4-b08c-33574fdc9baa | -5.09033 | -44.81828 | 2024-10-30 03:28:00 | NOAA-20 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1f785456-3160-3e8c-afc0-6db65fa2b488 | -5.08944 | -44.8157 | 2024-10-30 03:28:00 | NOAA-20 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9c63d800-96ba-3a92-be31-aadc186f520c | -5.08834 | -44.8219 | 2024-10-30 03:28:00 | NOAA-20 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 51e7e91a-ce31-3788-bde3-f34a385ef00e | -5.05983 | -44.22732 | 2024-10-30 03:28:00 | NOAA-20 | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 347538c8-afcb-39e8-b95b-ea817158cc9c | -5.05331 | -44.2258 | 2024-10-30 03:28:00 | NOAA-20 | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c4d26afb-46d2-31f2-8e75-945c0e41f581 | -5.04909 | -45.16372 | 2024-10-30 03:28:00 | NOAA-20 | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 681fff12-8862-35d3-b6dd-6d167c95c1b9 | -5.04791 | -45.1704 | 2024-10-30 03:28:00 | NOAA-20 | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a1e976be-2bd1-3ca6-b46f-f599c5e7c864 | -5.00017 | -44.36997 | 2024-10-30 03:28:00 | NOAA-20 | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| abca3482-addf-3eef-bf6a-64c9f8b257e3 | -4.99915 | -44.37565 | 2024-10-30 03:28:00 | NOAA-20 | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 410c398b-ed5b-337f-a3c2-46d9b6093130 | -4.9966 | -44.36718 | 2024-10-30 03:28:00 | NOAA-20 | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 10456315-a808-3741-90b2-f080b324e148 | -4.99557 | -44.37308 | 2024-10-30 03:28:00 | NOAA-20 | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 0359f6ce-80e4-34cd-99a5-81777d8bd944 | -4.62185 | -45.61141 | 2024-10-30 03:28:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c48180e2-857d-3c9b-8dfc-08981058db2a | -4.61791 | -45.60625 | 2024-10-30 03:28:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| cbe843b1-03f1-33bd-b4b1-abd58e4eb252 | -4.61667 | -45.61296 | 2024-10-30 03:28:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6cae2eda-1531-3e05-b7ab-8b227007004f | -4.61472 | -45.60991 | 2024-10-30 03:28:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a1f09b27-8580-393a-9ef3-711005fa45ac | -4.59945 | -44.29957 | 2024-10-30 03:28:00 | NOAA-20 | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| d9db0a8a-e40e-3e96-9492-8d224e7dc310 | -4.59837 | -44.30563 | 2024-10-30 03:28:00 | NOAA-20 | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 6d89ce51-718d-300d-8d19-bde1e2dd4502 | -4.59735 | -44.31135 | 2024-10-30 03:28:00 | NOAA-20 | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 713231ed-f57d-33d8-b04b-3e4ab8f7c7d9 | -15.651 | -39.18496 | 2024-10-30 03:30:00 | NOAA-20 | CANAVIEIRAS | BAHIA | Brasil | 2906303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 0ca27364-2c4e-3d6a-9fa6-c1f253fd4ed4 | -14.60369 | -42.36175 | 2024-10-30 03:30:00 | NOAA-20 | LICÍNIO DE ALMEIDA | BAHIA | Brasil | 2919405 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 8cb51e36-6f7c-3e5a-af26-44851a1e7f05 | -14.60363 | -42.36368 | 2024-10-30 03:30:00 | NOAA-20 | LICÍNIO DE ALMEIDA | BAHIA | Brasil | 2919405 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| e2c73726-520d-34eb-b853-d3d8acb8d87d | -14.44413 | -42.14056 | 2024-10-30 03:30:00 | NOAA-20 | RIO DO ANTÔNIO | BAHIA | Brasil | 2926806 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 1fe1fc98-eb75-3e97-bf03-2c08e7b10ef4 | -13.91475 | -41.93656 | 2024-10-30 03:30:00 | NOAA-20 | LIVRAMENTO DE NOSSA SENHORA | BAHIA | Brasil | 2919504 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 511238da-675e-3293-b129-8764b43cb920 | -13.86603 | -43.06324 | 2024-10-30 03:30:00 | NOAA-20 | MATINA | BAHIA | Brasil | 2921054 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 151b6108-5953-303f-9a6a-1c0e5119f9e2 | -13.57116 | -43.42747 | 2024-10-30 03:30:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e14c983a-2179-3b19-ad27-c858034dcfec | -13.47701 | -43.26088 | 2024-10-30 03:30:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 6d20e664-fa3b-3b96-a3a8-f5d534a53d92 | -13.47633 | -43.2644 | 2024-10-30 03:30:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| ce439b57-57df-330c-bef3-68b888850cee | -13.47367 | -43.25977 | 2024-10-30 03:30:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 8de9379e-3a26-3606-9c88-8bf44652b148 | -13.47297 | -43.26329 | 2024-10-30 03:30:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 78c64cc5-1719-3e08-96e4-31aea9383042 | -13.47165 | -43.25969 | 2024-10-30 03:30:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 8fd0bcce-2809-3f6f-8364-f834fe3adbe0 | -13.47097 | -43.26324 | 2024-10-30 03:30:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| e0e84794-0995-38dc-bb6d-11abaa162ca4 | -13.25314 | -43.68033 | 2024-10-30 03:30:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c1fd7611-97ff-36fa-8cfc-d10e9be32732 | -12.89538 | -45.06427 | 2024-10-30 03:30:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| fdd99357-f058-3ea4-ac56-25efbd9211d0 | -12.89027 | -45.0582 | 2024-10-30 03:30:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| a7c902d4-33e0-3e37-9277-1cb85c4908b7 | -12.88148 | -44.622 | 2024-10-30 03:30:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f3076f06-f967-3b23-a6ed-b9598983282e | -12.88063 | -44.6263 | 2024-10-30 03:30:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c80e0db5-fb51-32c2-b5bc-a11958c7f25d | -12.87905 | -44.62037 | 2024-10-30 03:30:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 0a907e12-052e-36c0-967b-33e9c785f763 | -12.87816 | -44.62468 | 2024-10-30 03:30:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 808ea82f-163a-32bf-aed5-e3a0bc1870b3 | -12.87645 | -44.61628 | 2024-10-30 03:30:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8a935091-fd70-347a-bad0-8654416dd3df | -12.8756 | -44.62058 | 2024-10-30 03:30:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a9089fd1-3869-3f0a-8c40-d8bcd470268c | -12.87473 | -44.62498 | 2024-10-30 03:30:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0a756090-1d0c-30d2-9422-efecfb422fcb | -12.87405 | -44.61467 | 2024-10-30 03:30:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 49c026f3-3b69-3b2e-9aa5-86bd3ee7cae1 | -12.87317 | -44.61897 | 2024-10-30 03:30:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9bc7b4a0-b6e4-3765-aa19-20787c2b8cd5 | -12.86971 | -44.61921 | 2024-10-30 03:30:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3c28ffc4-d814-39e5-bc00-32c902cc05c3 | -12.86728 | -44.61766 | 2024-10-30 03:30:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1a903a69-2a0a-3dc5-9fa4-a9f9eeeb9e55 | -12.28138 | -44.25651 | 2024-10-30 03:30:00 | NOAA-20 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 5694584f-28d9-3bab-bac4-66aa25847e53 | -12.28055 | -44.26073 | 2024-10-30 03:30:00 | NOAA-20 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 26.0 |
| bbc6b0cb-fd51-381e-9d16-5574e39908c3 | -12.27979 | -44.2578 | 2024-10-30 03:30:00 | NOAA-20 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 28.5 |
| 97233ff6-e37d-3fa0-961c-90140ccd2985 | -12.27974 | -44.26488 | 2024-10-30 03:30:00 | NOAA-20 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 26.0 |
| dc7133ba-f588-3af8-a0b7-00a9903d9ece | -12.27895 | -44.26194 | 2024-10-30 03:30:00 | NOAA-20 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 28.5 |
| 811b1878-b0bc-303f-8f89-10be38184f1e | -12.27811 | -44.26607 | 2024-10-30 03:30:00 | NOAA-20 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 5fc86d74-69eb-375f-a19d-5edc3ee3e445 | -12.27475 | -44.25932 | 2024-10-30 03:30:00 | NOAA-20 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 33566b69-47aa-3167-b42c-10dfeb3be26d | -11.96721 | -43.29309 | 2024-10-30 03:30:00 | NOAA-20 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 32bf0700-2fb2-32cd-befb-91e1131dc01a | -11.87955 | -43.82749 | 2024-10-30 03:30:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d96c03f3-ccd6-36be-b94b-7b858b3b57e7 | -11.87874 | -43.8316 | 2024-10-30 03:30:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| faa01467-631c-33bd-8c38-5e53aa9960f7 | -11.74068 | -44.32616 | 2024-10-30 03:30:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8c702035-19ed-3be3-81cd-53c0b234f87d | -11.67722 | -41.13663 | 2024-10-30 03:30:00 | NOAA-20 | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| f3168db2-624a-3aa8-be94-dfb69dffa568 | -11.61697 | -43.91271 | 2024-10-30 03:30:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 36bd9d8a-7e54-3c2f-82a0-7ca034c1489b | -11.61687 | -43.91095 | 2024-10-30 03:30:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8e61bb8f-59f8-3a5d-ab27-bfbb254c9944 | -11.61118 | -43.91151 | 2024-10-30 03:30:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 404a5bd0-29cf-3d0b-9f01-04019cae7543 | -11.61109 | -43.90975 | 2024-10-30 03:30:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 9b2fc53e-1fe1-3f03-889c-22f55d04dc34 | -11.28967 | -41.86271 | 2024-10-30 03:30:00 | NOAA-20 | IRECÊ | BAHIA | Brasil | 2914604 | 29 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 6f1ae7c2-9f93-3a08-b2a1-7d99f5ed2ddb | -11.28908 | -41.86582 | 2024-10-30 03:30:00 | NOAA-20 | IRECÊ | BAHIA | Brasil | 2914604 | 29 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 48a93d25-44ae-3251-84e1-92e631a2af18 | -11.05898 | -45.37152 | 2024-10-30 03:30:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9008e331-efd3-354d-be9e-ff4fa37f79c6 | -11.05266 | -45.3699 | 2024-10-30 03:30:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d5ec77d7-fbfb-3631-85ab-bdb0989f525f | -10.8752 | -44.54042 | 2024-10-30 03:30:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d8454794-2c30-3399-8eff-04be326f1dd1 | -10.86912 | -44.53913 | 2024-10-30 03:30:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| afe69e78-b12e-36c0-b2f9-75a45604dc3f | -10.86815 | -44.544 | 2024-10-30 03:30:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 41d14750-b02c-3631-b9e1-96652a282ee8 | -10.86778 | -44.41507 | 2024-10-30 03:30:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d73f5292-472f-3943-8574-6ac8e04d81a9 | -10.86357 | -42.93784 | 2024-10-30 03:30:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9c1ed82a-6145-3a38-b465-aa0fb771e786 | -10.86306 | -44.41103 | 2024-10-30 03:30:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1c1313b3-2fbc-31f3-ae8a-463df8c12b18 | -10.86212 | -44.4157 | 2024-10-30 03:30:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d2c846fc-a7ea-3db2-82fe-049f6a145f13 | -10.86177 | -44.41362 | 2024-10-30 03:30:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 43dd8dc3-d201-374a-9190-870cd80f8425 | -10.85806 | -42.93673 | 2024-10-30 03:30:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cbbfb7d4-23ec-30ae-aa8d-1a96a66f40d4 | -10.77715 | -40.94229 | 2024-10-30 03:30:00 | NOAA-20 | OUROLÂNDIA | BAHIA | Brasil | 2923357 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 18b0512a-44e3-3e3f-890d-e3a03985153c | -10.7111 | -44.92365 | 2024-10-30 03:30:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 19.8 |
| 92ebd83f-ff53-353f-a6f7-cdb7eee6743f | -10.7101 | -44.9287 | 2024-10-30 03:30:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 32.6 |
| 3a9f496e-a9f3-3060-ad60-9943011264de | -10.61144 | -44.94883 | 2024-10-30 03:30:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |


[Clique aqui para ver as próximas entradas](README30.md)
