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

## Dados Diários - Página 39

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e3acb5f8-2bdf-3fe5-a4d7-cedb27f81540 | -4.3581 | -54.7899 | 2026-09-11 13:40:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 72.5 |
| 9c3ef15c-e15e-3d97-8051-738eba3c8fa3 | -13.3243 | -61.6709 | 2026-09-11 13:50:00 | GOES-19 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 73.1 |
| 46ffa9d3-35c7-3ec2-95c4-6811c6516d92 | -9.0431 | -65.3988 | 2026-09-11 13:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 58.7 |
| 0adc33e5-0be1-3b81-926d-04d7db386666 | -11.3513 | -45.7922 | 2026-09-11 13:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 438.6 |
| d4e360a1-ef3e-3642-bdfa-9a21f98a3b0b | -14.5836 | -48.8409 | 2026-09-11 13:50:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 77.9 |
| e34d3b3f-883c-3ee7-a52e-d6b81773e7f7 | -9.043 | -65.4175 | 2026-09-11 13:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 80.8 |
| 1e1e3887-78fc-336e-b5a0-b090902881eb | -10.7674 | -60.7666 | 2026-09-11 13:50:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 62.6 |
| 74ca559b-017c-3db2-8d78-ededdae048e0 | -7.5932 | -45.1361 | 2026-09-11 13:50:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 120.5 |
| f6074ff3-5ca0-3343-9ca8-8cb8f76d6f54 | -10.7359 | -46.1465 | 2026-09-11 13:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 119.8 |
| 4d93a025-8dc6-3a60-aaf5-050152507b04 | -13.3241 | -61.6903 | 2026-09-11 13:50:00 | GOES-19 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 54.9 |
| 2cbf044c-a66e-36c8-99ac-a50029dcd3ea | -14.6026 | -48.8601 | 2026-09-11 13:50:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 117.2 |
| b32bc4bb-7349-3e6f-98af-3954e71d54f0 | -8.9412 | -44.3995 | 2026-09-11 13:50:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 93.7 |
| 0ccdd991-820f-3792-a7f9-14360df94ddc | -10.7963 | -45.9348 | 2026-09-11 13:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 127.3 |
| c0e5b757-5887-31f0-9b10-b209fdbdab30 | -7.6118 | -45.1571 | 2026-09-11 13:50:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 110.2 |
| 82f66047-9c61-3121-aa21-671aa0d3aab3 | -22.2649 | -55.8315 | 2026-09-11 13:50:00 | GOES-19 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 154.5 |
| 413c0c2d-d2e8-34e5-a8c1-9004a68ff26b | -10.5475 | -51.3578 | 2026-09-11 13:50:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 113.5 |
| 72b7a514-c243-39ff-a925-abba0de25120 | -11.3326 | -45.772 | 2026-09-11 13:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 123.1 |
| d7ce580b-e977-3af2-a580-3383854ee24f | -9.0244 | -65.4181 | 2026-09-11 13:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 52.7 |
| 97499ce1-245a-347b-a8fd-d47815e3c222 | -7.9834 | -43.9951 | 2026-09-11 13:50:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 171.5 |
| a93aa769-3b35-3589-811a-69f034095831 | -7.9645 | -43.9971 | 2026-09-11 13:50:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 104.4 |
| 4f85c41f-dc93-37af-bbd4-7d3fc3848640 | -9.8075 | -43.5011 | 2026-09-11 13:50:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 204.5 |
| edd1c62d-ca12-3366-b650-234c1f09e43a | -10.5478 | -51.3367 | 2026-09-11 13:50:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 157.3 |
| a1358e4a-5448-380c-8522-593bb95d708f | -13.268 | -61.597 | 2026-09-11 13:50:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 195.4 |
| 77837a62-11ff-3a93-bb87-e4e2e6a9df23 | -7.9831 | -44.0183 | 2026-09-11 13:50:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 137.3 |
| 9e36cfc7-feda-37b2-a5cb-dc3a0c3690f4 | -14.6031 | -48.8379 | 2026-09-11 13:50:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 115.9 |
| 157d39c9-ab23-3424-82d1-fdbb3a727e5a | -13.2297 | -61.6384 | 2026-09-11 13:50:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 56.4 |
| 58a1ed3a-10e1-384b-ab4f-dcff2a798cf0 | -8.0023 | -43.9931 | 2026-09-11 13:50:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 86.1 |
| ea031e6d-9506-3e0b-8f9e-3f2811bb125a | -10.641 | -46.136 | 2026-09-11 13:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 119.1 |
| fc5f255a-a23f-34f0-8e23-df79645d87c9 | -13.249 | -61.5983 | 2026-09-11 13:50:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 105.0 |
| e1a9de6c-4718-3a4e-8634-6f462138cc85 | -7.5553 | -45.1624 | 2026-09-11 13:50:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 108.5 |
| 9f4da94c-9fa5-3232-bf08-a8fc3b5677bb | -13.3433 | -61.6696 | 2026-09-11 13:50:00 | GOES-19 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 92.1 |
| 4b071a5c-2282-3067-86a0-f90747b006c8 | -22.2856 | -55.828 | 2026-09-11 13:50:00 | GOES-19 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 111.9 |
| 5f1e0f0d-90d6-37a4-be09-a3e6fb3d65b8 | -9.9041 | -45.91 | 2026-09-11 13:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 472.0 |
| 606925ae-376f-3351-8923-ac55802acf4a | -7.593 | -45.1589 | 2026-09-11 13:50:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 106.9 |
| 9f687418-7e55-3841-b81e-7fb379e46653 | -22.2645 | -55.8532 | 2026-09-11 13:50:00 | GOES-19 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 80.3 |
| 808357aa-e786-371e-8a3b-490d54a996c8 | -13.2682 | -61.5775 | 2026-09-11 13:50:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 90.3 |
| 15f8a660-8d9d-3101-88fc-06364b3b95c1 | -4.3582 | -54.77 | 2026-09-11 13:50:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 156.8 |
| 3696dc05-a817-314c-867b-2a099912cb0a | -7.593 | -45.1589 | 2026-09-11 14:00:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 131.9 |
| 175baa71-a8a0-3753-999e-ad01bf83d912 | -2.7331 | -57.6271 | 2026-09-11 14:00:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 66.1 |
| 0f701f8e-1ce0-3ea4-93bb-41aa3a12db00 | -14.5836 | -48.8409 | 2026-09-11 14:00:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 84.7 |
| e3724dca-06e4-3526-be9d-17238ce49f9c | -9.0245 | -65.3994 | 2026-09-11 14:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 56.9 |
| 174be83a-c6d3-3137-90e6-3a0bf74a5b23 | -9.0244 | -65.4181 | 2026-09-11 14:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 62.1 |
| 58af2cf4-960c-33d7-98f8-00724e6446cd | -7.1533 | -45.8766 | 2026-09-11 14:00:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 98.7 |
| 519ab38c-0159-3060-a723-cca23e61541e | -8.0934 | -54.8488 | 2026-09-11 14:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 59.7 |
| 36565fa4-7ac2-3ac5-bcf6-162bc46b138c | -8.0748 | -54.8499 | 2026-09-11 14:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 58.5 |
| 10b6a560-904f-359c-b8e5-45d2dcf397c1 | -14.6026 | -48.8601 | 2026-09-11 14:00:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 184.9 |
| 12bd2508-79af-37a5-8082-e5a5a8686878 | -7.9645 | -43.9971 | 2026-09-11 14:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 116.7 |
| 92347263-f7fa-3e24-a4f7-f5081ca6ac26 | -7.5553 | -45.1624 | 2026-09-11 14:00:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 95.4 |
| 3cfb9937-641c-3535-a1ad-4570ca2dbb8c | -14.8863 | -49.236 | 2026-09-11 14:00:00 | GOES-19 | SÃO LUIZ DO NORTE | GOIÁS | Brasil | 5220157 | 52 | 33 | nan | nan | nan | Cerrado | 108.0 |
| c609798f-1c8b-3fe0-bc66-ff55ee570d54 | -7.5932 | -45.1361 | 2026-09-11 14:00:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 178.1 |
| cf5dde34-bc1d-3583-89a0-c7db5c1be8b2 | -11.3513 | -45.7922 | 2026-09-11 14:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 253.6 |
| dc255148-b10e-31fe-960e-21dd778f2e9d | -8.6496 | -66.5096 | 2026-09-11 14:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 52.1 |
| a9d9e9d0-7ef9-3124-bbe1-0b7b24f3b19a | -13.3241 | -61.6903 | 2026-09-11 14:00:00 | GOES-19 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 67.3 |
| 987a3bda-73d5-3406-aa6f-c9520c56a707 | -10.7359 | -46.1465 | 2026-09-11 14:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 179.9 |
| a31fdbf4-370c-3da7-bd67-47e181350401 | -7.9831 | -44.0183 | 2026-09-11 14:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 89.4 |
| 751bc76d-33a7-3021-ba53-96b4951cc305 | -13.268 | -61.597 | 2026-09-11 14:00:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 144.9 |
| 839ece68-4c2d-363a-af24-71c6f089b69a | -9.043 | -65.4175 | 2026-09-11 14:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 102.6 |
| 88d25bf6-1f52-3028-b2e9-02c37fec5a0a | -7.9833 | -45.5525 | 2026-09-11 14:00:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 94.9 |
| bb854cd1-98b6-32bb-885f-1c508aed236e | -4.3582 | -54.77 | 2026-09-11 14:00:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 221.7 |
| 04cc935b-8e0c-3d14-a405-46339bef7c43 | -13.3243 | -61.6709 | 2026-09-11 14:00:00 | GOES-19 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 90.2 |
| 0184bc31-51dd-3ebd-bdab-cfbb91dc2b87 | -10.5478 | -51.3367 | 2026-09-11 14:00:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 179.5 |
| f532c2ad-381a-32ce-89dc-27e58c3c9d22 | -10.5475 | -51.3578 | 2026-09-11 14:00:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 126.1 |
| e1ba987e-0388-3aa7-bc4c-4c360b7eb261 | -11.417 | -51.416 | 2026-09-11 14:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 84.6 |
| 1ef2c8d1-e4b7-32d5-8232-87f3953b4b4b | -9.1799 | -68.2194 | 2026-09-11 14:00:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 51.6 |
| c7f4516e-fc2a-3690-aec9-1c119903f8fb | -8.0021 | -45.5507 | 2026-09-11 14:00:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 102.8 |
| bee6e6b2-f6e3-3569-b46c-40c4fedc903f | -9.6951 | -43.3981 | 2026-09-11 14:00:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 93.9 |
| 08ff0d86-5b4a-304f-8955-12eccba24619 | -7.9834 | -43.9951 | 2026-09-11 14:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 129.7 |
| b33db06b-a6ba-372e-843e-b34f7f814c0d | -6.2429 | -51.6939 | 2026-09-11 14:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 65.3 |
| 6cdd263f-d8d5-3f6e-9fac-26339840845e | -10.641 | -46.136 | 2026-09-11 14:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 175.7 |
| 27cf0f95-7623-3de6-8607-29cc2f61b6c7 | -9.8075 | -43.5011 | 2026-09-11 14:00:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 152.0 |
| dc50fed1-a316-3ec5-8c88-b2379dd7dec6 | -13.2682 | -61.5775 | 2026-09-11 14:00:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 96.3 |
| 5f534a50-7e90-30d8-9154-88f048f9cac8 | -14.6031 | -48.8379 | 2026-09-11 14:00:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 127.8 |
| 9c5dc7e0-e5bc-3d8c-be63-2166924e60d1 | -22.2649 | -55.8315 | 2026-09-11 14:00:00 | GOES-19 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 126.8 |
| af2ea069-558c-3d06-80c3-c62ff84c6229 | -13.249 | -61.5983 | 2026-09-11 14:00:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 60.4 |
| 6db296cb-074b-315d-b8b7-978f5f3c52e7 | -6.954 | -45.2165 | 2026-09-11 14:00:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 84.2 |
| 92a3a724-aeb3-317b-aa5d-ad25e76d5c37 | -9.0431 | -65.3988 | 2026-09-11 14:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 83.4 |
| 0170f08a-bbb1-37ba-a2eb-654a37004038 | -13.3433 | -61.6696 | 2026-09-11 14:00:00 | GOES-19 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 91.4 |
| 6db1de10-c5a1-32d9-b1b6-6824c13a220c | -13.2088 | -61.8338 | 2026-09-11 14:10:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 51.4 |
| 1b19f600-6481-3ffb-b8e1-e194baee7010 | -13.3435 | -61.6501 | 2026-09-11 14:10:00 | GOES-19 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 61.4 |
| 35cf3999-dc61-333b-8d55-046c8597ba1e | -7.9834 | -43.9951 | 2026-09-11 14:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 207.8 |
| 5f17b50e-8dfa-3ea6-ba5d-8416bbd5659d | -7.5932 | -45.1361 | 2026-09-11 14:10:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 113.9 |
| 73a8fe7c-2d17-383e-9c4c-dfaf9bac3883 | -8.7252 | -62.4367 | 2026-09-11 14:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 53.9 |
| 04b71481-a1dd-3477-ad80-537ad7c83170 | -9.8072 | -43.5246 | 2026-09-11 14:10:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 101.7 |
| cf2954e4-a83b-3f21-beec-7b0da3f46e8d | -14.6031 | -48.8379 | 2026-09-11 14:10:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 107.3 |
| d525c16a-a5c1-339b-8542-598eb53986e4 | -8.0418 | -43.8497 | 2026-09-11 14:10:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Caatinga | 119.7 |
| 9f902078-358c-3b43-9b77-87d4b752015e | -13.3053 | -61.6721 | 2026-09-11 14:10:00 | GOES-19 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 56.3 |
| 3c3efbe8-bac0-30e1-9929-5e329b6b15c4 | -9.9045 | -45.8873 | 2026-09-11 14:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 299.3 |
| f7ecfc01-1a54-38f0-bb99-2fad52c239ac | -11.9547 | -49.7512 | 2026-09-11 14:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 97.8 |
| e3e38d90-4c90-350d-87a1-b0f0942227c6 | -11.417 | -51.416 | 2026-09-11 14:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 84.5 |
| a5015fa7-0a77-3f9e-a4e6-ae9bf91e0840 | -7.9831 | -44.0183 | 2026-09-11 14:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 152.5 |
| 54dd0cd3-3b4b-3af7-8602-c39bbe06f6d8 | -9.8852 | -45.9122 | 2026-09-11 14:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 89.3 |
| 8eca92f4-de26-3d96-97e8-ca98d2924eaf | -10.641 | -46.136 | 2026-09-11 14:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 161.6 |
| eb589c68-6de8-3b0b-b599-42c79d98399b | -7.9645 | -43.9971 | 2026-09-11 14:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 143.6 |
| fa05a325-7937-3595-86c7-67c6ce69dc09 | -9.8855 | -45.8896 | 2026-09-11 14:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 128.1 |
| 15034183-5384-374b-82c2-35949989e3a3 | -13.3245 | -61.6514 | 2026-09-11 14:10:00 | GOES-19 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 57.8 |
| 8498f7a9-3c38-37b8-a298-4e84335f749b | -9.2276 | -65.5797 | 2026-09-11 14:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 53.6 |
| 0eeb1b4f-a347-3d32-ac43-dabe2dc5aa98 | -6.2429 | -51.6939 | 2026-09-11 14:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 74.0 |
| 93be73fd-cfac-3b37-a3f5-1947b6d254a3 | -8.6496 | -66.5096 | 2026-09-11 14:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 57.4 |
| e7fe2dde-dc7f-3c77-a331-730f7ba77722 | -8.0023 | -43.9931 | 2026-09-11 14:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 114.2 |
| 4482e9fe-3a03-3a57-adb3-38f91a231f97 | -9.043 | -65.4175 | 2026-09-11 14:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 101.8 |


[Clique aqui para ver as próximas entradas](README40.md)
