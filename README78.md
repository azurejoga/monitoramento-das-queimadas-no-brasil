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

## Dados Diários - Página 78

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e1028d9b-fc5c-397a-88b0-9356402a7135 | -7.75166 | -70.16128 | 2025-08-29 05:29:00 | NOAA-20 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5ee69815-c59f-3657-8db8-87019b118e4c | -10.35084 | -58.04122 | 2025-08-29 05:29:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e24d279a-9542-3589-8d63-eff38bac3078 | -8.17968 | -61.37616 | 2025-08-29 05:29:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| e874155f-3922-3f47-afce-d0f69dfdafde | -14.30638 | -53.29765 | 2025-08-29 05:29:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 23bccbff-71ea-30f6-bb6c-3a32c05cbf7a | -8.25529 | -61.50124 | 2025-08-29 05:29:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f1e52118-9c75-3ad8-9725-1185f53824b9 | -7.57596 | -63.03889 | 2025-08-29 05:29:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e458734d-91f1-3bd2-8f3b-2bed3137aef0 | -13.00301 | -56.90791 | 2025-08-29 05:29:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 657e7e51-3f28-3d56-860f-e93f2021fe03 | -11.70469 | -60.19569 | 2025-08-29 05:29:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a8d4636e-3cd8-31a1-9ff4-80d2ed963b73 | -9.92206 | -59.92553 | 2025-08-29 05:29:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 3c30a015-7892-3f8a-9e0d-7468c1be60ab | -9.41304 | -60.57044 | 2025-08-29 05:29:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 60ca6d48-d2bf-31c7-ba3b-73b6e130901e | -9.00887 | -65.70999 | 2025-08-29 05:29:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c08e8911-cb0b-35dd-b9e8-9e1ef308985c | -9.15208 | -65.78183 | 2025-08-29 05:29:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 79f8230a-a78c-35e9-b1d3-c52ab67bea22 | -8.17297 | -61.3751 | 2025-08-29 05:29:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e9b0253e-9a2e-333f-b86b-4aa5c5450550 | -9.1842 | -67.75552 | 2025-08-29 05:29:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 91e387f3-00a6-37b2-8e08-eee4ff2b76b2 | -10.25521 | -64.50622 | 2025-08-29 05:29:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 918670d2-e5a2-38bc-b9e2-fa79793088d8 | -10.46908 | -57.9347 | 2025-08-29 05:29:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3ea111d8-ee9c-38b7-9335-339ee999c1ae | -8.93015 | -65.93918 | 2025-08-29 05:29:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6758c860-2b24-34b9-b5ef-1623f8a33ea9 | -8.94899 | -65.95962 | 2025-08-29 05:29:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 725cdd78-f56f-3226-a860-48c6c9a29511 | -9.01513 | -65.69424 | 2025-08-29 05:29:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bed06290-c2fc-3a76-9144-40215469d60a | -7.55953 | -63.84164 | 2025-08-29 05:29:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5f2d4ddb-eb6b-3b1b-8525-3c8bb5df80d6 | -11.21945 | -55.05751 | 2025-08-29 05:29:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0905d00c-dc05-3f38-a369-1daa0484f8ae | -9.11061 | -65.79728 | 2025-08-29 05:29:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 51e452e8-2754-3a53-b310-c8b88524758b | -9.16358 | -60.78341 | 2025-08-29 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 00ed85db-060d-31b1-9acb-6217b64797d4 | -9.13697 | -65.79329 | 2025-08-29 05:29:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| edfa8fe4-804b-3b1e-a71b-d69ee30f4d6b | -8.95551 | -65.96503 | 2025-08-29 05:29:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6a3b6163-c9b4-388a-b136-89016935c6c8 | -8.17352 | -61.37153 | 2025-08-29 05:29:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4dc96a16-a53d-388e-9f4f-acda4950e4c1 | -9.21992 | -60.87269 | 2025-08-29 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 4ee676cb-b215-387e-b85d-9beb33b96300 | -7.70232 | -62.32573 | 2025-08-29 05:29:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d561cdf0-88d8-3acf-9544-dc97f3e40f0b | -13.0295 | -56.91611 | 2025-08-29 05:29:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 47fdfe03-648f-3325-9cd6-20e6badb43d3 | -9.31194 | -57.69615 | 2025-08-29 05:29:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 502dfd48-6a5c-3a5f-97f5-993fa7a165d9 | -9.1643 | -65.79652 | 2025-08-29 05:29:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ff8655ab-05c9-32a0-8107-875e02d70221 | -8.12437 | -61.21043 | 2025-08-29 05:29:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 22140688-b198-3880-89ea-ed6a8d1af5c0 | -8.8856 | -60.74546 | 2025-08-29 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4cb8e074-ec2a-383e-9813-1294f9824d54 | -10.50792 | -64.3322 | 2025-08-29 05:29:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dfd1602e-f227-37ae-96a7-1e2ae7f6b61b | -9.21763 | -60.86464 | 2025-08-29 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 8119ee92-eeb5-3ccb-a727-b2814adeafb1 | -8.18248 | -61.38025 | 2025-08-29 05:29:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 15bc17d7-2c91-3aea-99c3-9800023d6072 | -10.3761 | -57.83195 | 2025-08-29 05:29:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| b7815c5a-7a3c-3928-b122-4c8df761dd01 | -12.62963 | -60.25011 | 2025-08-29 05:29:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 99b90155-8369-3b49-addd-e81d21bf613e | -9.31566 | -57.69995 | 2025-08-29 05:29:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b9afa90b-ea49-3feb-8c12-7864830a0852 | -9.1071 | -61.431 | 2025-08-29 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6703262f-0813-31f3-a3d6-b59deb3109dd | -12.44026 | -63.91633 | 2025-08-29 05:29:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d2f0ce2b-dcd8-3d28-b611-e749c7b3ac2f | -10.28573 | -64.48885 | 2025-08-29 05:29:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 005a96c3-c41c-357f-9d4b-667766491405 | -13.00181 | -56.91719 | 2025-08-29 05:29:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3e50fc92-7d6a-38eb-8868-802988cc9434 | -13.23378 | -57.13476 | 2025-08-29 05:29:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f221d242-b474-3271-96f7-67dc9203cc1d | -10.93917 | -68.384 | 2025-08-29 05:29:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2621042e-c8d7-3ac4-86d5-4b13084132da | -9.16638 | -59.56038 | 2025-08-29 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 698e7744-8966-3114-8337-f29a5afe0bdc | -9.48173 | -62.39026 | 2025-08-29 05:29:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 837b4535-4ea6-38df-8747-c6bd62c21b51 | -9.77781 | -64.24678 | 2025-08-29 05:29:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 17d0cc54-b29e-3d8c-8f2c-d190c4b666cf | -10.85031 | -60.79887 | 2025-08-29 05:29:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 781cfce5-2d3f-3215-8dc1-d8b0a9266e2e | -8.94538 | -65.959 | 2025-08-29 05:29:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e3250658-f671-3050-8804-36d1db1cfa7a | -9.12404 | -65.78264 | 2025-08-29 05:29:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 87aac71e-23d9-33d8-af33-43c4ce8c3f98 | -10.38377 | -57.83239 | 2025-08-29 05:29:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 22c31f52-2932-3bf9-8967-b508b9cf4163 | -9.15496 | -65.78653 | 2025-08-29 05:29:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 26c0f058-212a-3d46-80d9-73c42e1b25b6 | -9.15483 | -59.58876 | 2025-08-29 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dae538cf-8c4e-3d76-9bb9-a3bbbeb163c5 | -8.1903 | -61.37414 | 2025-08-29 05:29:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| c39c1387-d8c1-3867-95f2-cc484d7e0167 | -8.89825 | -62.47277 | 2025-08-29 05:29:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dba3a2f0-7495-3639-b761-54837baf3166 | -9.12336 | -65.78671 | 2025-08-29 05:29:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1e64f1ec-ff9a-30ae-9057-94d96dc8952e | -10.37199 | -57.83152 | 2025-08-29 05:29:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 7.4 |
| c2e4d5c6-a6cf-336e-975a-91002e924c3e | -10.85901 | -60.81221 | 2025-08-29 05:29:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 066051c3-d571-3bc9-82b9-c912f86b67f1 | -9.23876 | -59.77961 | 2025-08-29 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f31a2f99-da0d-3cd4-af36-7f8388cba7d2 | -9.46944 | -60.56279 | 2025-08-29 05:29:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fe824e11-8b7a-3b5d-a066-345d1a422d46 | -12.43638 | -63.91932 | 2025-08-29 05:29:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 0b6e1bf8-1ec3-33dd-84a4-09cedb953d66 | -9.10582 | -65.73743 | 2025-08-29 05:29:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6f19b2b1-d4e6-312f-bd6e-6868f2aeb50f | -9.80481 | -67.84287 | 2025-08-29 05:29:00 | NOAA-20 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 8963a8a1-33d4-35f8-8fe4-29a2a8112d7f | -9.45728 | -60.57277 | 2025-08-29 05:29:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 3cd45775-dbd2-301b-a7fd-baab6e0580e2 | -10.10868 | -68.95908 | 2025-08-29 05:29:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2a6fa61f-8378-3773-876b-87cbd98876f6 | -14.46102 | -53.07323 | 2025-08-29 05:29:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 321594a5-a792-3231-9963-885a516447ea | -7.9956 | -70.28574 | 2025-08-29 05:29:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 33a9709f-4068-302a-a2fa-2cf865220cfd | -9.13234 | -65.29408 | 2025-08-29 05:29:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 66e92b15-d287-3546-af8d-85ccb8a016c1 | -9.11197 | -65.78902 | 2025-08-29 05:29:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 76d800e0-a476-3d47-9d46-6119c4977301 | -10.37451 | -59.39547 | 2025-08-29 05:29:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dae0e958-4894-3be9-bee5-67e95a0c1b5c | -9.67159 | -64.98619 | 2025-08-29 05:29:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 01ed50d8-cda7-31c9-bbd4-347c4d47e7d4 | -12.63388 | -60.24638 | 2025-08-29 05:29:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7314fe00-8a0b-357b-9b43-0d7b521ae4c9 | -9.19327 | -61.02504 | 2025-08-29 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 048c50ab-2ef6-3bf5-b850-b0924e35a4ed | -10.32095 | -62.62363 | 2025-08-29 05:29:00 | NOAA-20 | THEOBROMA | RONDÔNIA | Brasil | 1101609 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 851b69c2-837b-34bc-8c7b-867f578295ba | -9.44915 | -60.55584 | 2025-08-29 05:29:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 25.2 |
| 34107fc9-299e-3ea9-ac59-9190bc24b6ed | -9.11535 | -65.76852 | 2025-08-29 05:29:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 28.1 |
| ae3844d3-2d60-3f9c-bfb7-b12956913709 | -12.9961 | -56.92589 | 2025-08-29 05:29:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e7323d03-0794-3d16-9970-df149c06d19e | -8.18414 | -61.36953 | 2025-08-29 05:29:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 8b30e2c7-f099-374f-a0d0-5fba43e0b9e0 | -14.11976 | -53.95837 | 2025-08-29 05:29:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4768bae4-981f-3b87-bf3e-2614f68077b9 | -8.93471 | -64.16615 | 2025-08-29 05:29:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5c5a43f8-fe17-372b-a2c9-8574a847f492 | -7.53932 | -63.83837 | 2025-08-29 05:29:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9c22bc3d-2651-3adf-b055-4c78802ec2e5 | -9.29634 | -56.81687 | 2025-08-29 05:29:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e046d558-fc42-3c2e-8e46-98b91a42c7fa | -9.80773 | -61.19643 | 2025-08-29 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ab6a31ed-44a5-3f17-91ff-17f89b0fbf00 | -9.17486 | -59.44963 | 2025-08-29 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 42b793ae-4199-307a-958a-d9178f3e9d38 | -8.88274 | -60.74115 | 2025-08-29 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1ec78e00-9996-3bcf-88d9-10664eb0454e | -13.35807 | -54.388 | 2025-08-29 05:29:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 35c1c105-5556-3bff-ab07-cdaec9d284b7 | -9.16993 | -65.78485 | 2025-08-29 05:29:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3def6f3a-9db4-3b6c-9580-6ef73a108b07 | -8.95773 | -65.97401 | 2025-08-29 05:29:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8d4beb46-5ce7-3813-8499-f4f381bd928a | -9.77503 | -64.24262 | 2025-08-29 05:29:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 85ca2640-13b8-3a46-b2cb-c6b2636d736d | -10.42615 | -64.48596 | 2025-08-29 05:29:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8957d9f2-dca6-3e97-99a6-d7a1428a8972 | -9.02541 | -65.39062 | 2025-08-29 05:29:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 795754a3-9380-35df-b058-07204bbeb46a | -10.36791 | -57.83092 | 2025-08-29 05:29:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 7.4 |
| b1404157-706a-38fb-9b02-a543d170d0bb | -9.94103 | -60.49999 | 2025-08-29 05:29:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 5374b89e-6463-3d40-92d2-38b95cb17f24 | -9.0289 | -65.72183 | 2025-08-29 05:29:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d57ddbb4-fabb-38a8-87af-59a333aebbf2 | -8.9504 | -65.95119 | 2025-08-29 05:29:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1e5c3807-8a2c-3311-852d-38e8a11f84b2 | -9.54068 | -62.40314 | 2025-08-29 05:29:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 27081a3d-fba1-3f8e-b2a7-d11a22e376d9 | -12.98158 | -54.76281 | 2025-08-29 05:29:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 966a325c-fecd-3798-8f54-618fd7a683c0 | -9.12383 | -65.76157 | 2025-08-29 05:29:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2c890979-2f20-3ec6-8700-8d55ba61d3fc | -9.09088 | -65.73916 | 2025-08-29 05:29:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README79.md)
