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

## Dados Diários - Página 176

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 47560934-2ec7-332c-9625-02c07cfd488f | -11.66614 | -65.1956 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a3e7eee2-5cce-3691-91f9-19cd24381fcd | -11.6649 | -65.20279 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d4d5b4c6-583a-39ef-af7d-0ae1ff7a71ae | -11.66273 | -65.19128 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 881b789f-80a2-3b1f-ba5d-e7e08f200ed7 | -11.66211 | -65.19487 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 15a7716f-151c-321e-ba6d-6a3e9c9f1829 | -11.66025 | -65.20565 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 949b6424-345f-3e3e-b06a-856922e2de41 | -11.65911 | -64.97468 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f146c64c-9b0b-3d58-ad7d-0444d9b3638e | -11.65899 | -65.02241 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 4.2 |
| d5cd76d0-7b55-3122-a881-e16b1449c83d | -11.65838 | -65.02593 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b613d285-6f1b-3704-a2ef-f6be3d2dc16d | -11.65623 | -65.20491 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c531feee-da3a-34f3-9d47-20c1590a543b | -11.65561 | -65.2085 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3d31955b-0a74-32e6-aa60-17ada59d252f | -11.65441 | -65.02516 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.9 |
| c75a71dd-8db6-3037-8d5c-b3492940297e | -11.65423 | -64.97917 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 372fc343-88cf-365d-81e3-6c33f8ee2237 | -11.65027 | -64.97842 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a6eed449-bd11-3522-bd92-cbd69bef12f5 | -11.64936 | -64.98366 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d84000b7-65db-331c-b8f2-a1802c4371ed | -11.64539 | -64.9829 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 25817564-89b8-3a08-b838-6279da891ab0 | -11.6405 | -64.98742 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 6709296e-62ad-3062-b65a-ab72b081a36d | -8.78727 | -68.7974 | 2024-10-03 05:16:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 37fde173-eb85-3d33-9200-aa31fd58a7f5 | -8.78599 | -68.8043 | 2024-10-03 05:16:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8d5d3c9a-3468-3eb2-873d-7d4947b45f3b | -8.78372 | -68.84673 | 2024-10-03 05:16:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 965a5838-eddf-3bbf-847e-6adf5f86245b | -8.77833 | -68.84575 | 2024-10-03 05:16:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5d74a165-b56e-3d23-8fa7-39f7d9e4a972 | -8.77769 | -68.84922 | 2024-10-03 05:16:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8e776d4e-6803-3788-a3bc-8b5dae2bbe31 | -9.50283 | -68.95727 | 2024-10-03 05:16:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0774bb9f-9511-32f3-9d88-3458ad1bdfd5 | -9.49748 | -68.95625 | 2024-10-03 05:16:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| faa69388-00b8-3068-b0da-00012d605226 | -9.45214 | -68.94753 | 2024-10-03 05:16:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 13071636-983f-308b-9b29-bbdc0b4b0cbf | -9.44741 | -68.94308 | 2024-10-03 05:16:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 103c7746-1471-339c-a758-88085bb0165f | -9.4402 | -68.95213 | 2024-10-03 05:16:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 53453e40-4de7-3e4f-9e75-cb5194e62444 | -9.43548 | -68.94766 | 2024-10-03 05:16:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 313fca24-8922-31f6-a354-4c0461867ac2 | -9.43485 | -68.95107 | 2024-10-03 05:16:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| eb668e26-225d-32a9-a04b-ef36c14d3146 | -9.33279 | -68.91807 | 2024-10-03 05:16:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 732fe5f6-ff4a-3b1c-b07e-7887790758d4 | -9.33217 | -68.92145 | 2024-10-03 05:16:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3fcee1cf-514e-3e05-a591-f83684809c24 | -8.78663 | -68.80085 | 2024-10-03 05:16:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 0caedb6c-dda5-3c92-9739-0183b33925d6 | -8.78308 | -68.8502 | 2024-10-03 05:16:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4120e83c-fad3-3439-9427-a012a5278f9b | -8.78127 | -68.79982 | 2024-10-03 05:16:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 81e745f7-01e8-382a-9392-f858b7f90151 | -8.62556 | -70.02131 | 2024-10-03 05:16:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3f0b0138-1d39-3a22-8f4a-85e2423683cb | -8.6248 | -70.02546 | 2024-10-03 05:16:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ff6430c1-08f0-39e4-abff-cbda6e6c364e | -8.62463 | -70.02142 | 2024-10-03 05:16:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0173a4a1-dfb5-3d0a-98b9-f61cc3602846 | -8.62384 | -70.02557 | 2024-10-03 05:16:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5a860814-e131-3531-8435-c00454b485ad | -8.61316 | -70.02319 | 2024-10-03 05:16:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c84596c3-3155-34c2-a2c3-d5a00e79196b | -8.61239 | -70.02736 | 2024-10-03 05:16:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ea910bd6-d1a2-33f0-9ef2-b8b36f956478 | -8.55275 | -69.95972 | 2024-10-03 05:16:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ec952e30-9467-3618-9f64-9b51f000aa5d | -8.54696 | -69.95856 | 2024-10-03 05:16:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 6f6619ba-5cc7-3e24-9909-93762626a8d5 | -8.18856 | -70.09111 | 2024-10-03 05:16:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4e32b64c-f4b6-3ca7-b226-ff03900fa660 | -8.18596 | -70.09302 | 2024-10-03 05:16:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d1d0f8dd-a334-3e48-8fe7-43a220baca50 | -8.18266 | -70.09003 | 2024-10-03 05:16:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.1 |
| dd678d43-3332-328b-8616-fa3fa632a110 | -8.18087 | -70.08767 | 2024-10-03 05:16:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b6d51c1e-c89a-33cd-8d1c-cda1286e59b1 | -8.18005 | -70.09197 | 2024-10-03 05:16:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1d9d664e-29f2-3e9a-a643-b01c63157248 | -10.72467 | -69.31747 | 2024-10-03 05:16:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 22e44178-7465-351c-bc03-b543e86abfa4 | -10.72224 | -69.3131 | 2024-10-03 05:16:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d30c2b5f-ff4d-3d4a-ba71-d057b9385f3c | -10.72157 | -69.3166 | 2024-10-03 05:16:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5f4e9e56-1220-3e49-9e91-4c28b3d29703 | -10.71994 | -69.31293 | 2024-10-03 05:16:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 44908d01-dd6a-3273-871d-333c93b59bc9 | -10.71504 | -69.43823 | 2024-10-03 05:16:00 | NOAA-20 | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0f840316-a355-308d-8cde-98243205c871 | -10.70893 | -69.44078 | 2024-10-03 05:16:00 | NOAA-20 | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ccf84b83-0c85-314e-823d-819ba1b489e2 | -10.70826 | -69.38591 | 2024-10-03 05:16:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 88711af9-2f73-365b-bf02-038313682521 | -10.70648 | -69.38592 | 2024-10-03 05:16:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e2cb8cc9-c3fd-310c-8a12-70429e4b9f01 | -10.70583 | -69.38941 | 2024-10-03 05:16:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 96d7b074-a423-3426-ac3d-6f9a855a9aa5 | -10.70286 | -69.38489 | 2024-10-03 05:16:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5da665e1-f689-370f-932b-3a72cdf82b09 | -10.7022 | -69.38835 | 2024-10-03 05:16:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 4.2 |
| ee1f825c-b961-312d-aa96-12fb22284563 | -10.70043 | -69.38839 | 2024-10-03 05:16:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b029fc19-04a3-3a2b-942a-86f034e8dd31 | -10.69977 | -69.39196 | 2024-10-03 05:16:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a46708cf-e632-36b3-bc28-287b469c63f2 | -10.69678 | -69.38739 | 2024-10-03 05:16:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7f384b13-4dfd-3b35-bf44-21d097228577 | -10.6961 | -69.39092 | 2024-10-03 05:16:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1cf7f656-5801-3f97-8b6e-9070cbfdaeed | -10.69542 | -69.39447 | 2024-10-03 05:16:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 68a8061c-e2cc-37de-9968-8d1483d35ab0 | -10.69437 | -69.39096 | 2024-10-03 05:16:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 54a06a1d-c18c-3ea4-9a2b-91dfda4bb87e | -10.69371 | -69.39449 | 2024-10-03 05:16:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1b0f001a-4b9c-3341-b804-fcf1c212271e | -10.66635 | -69.30207 | 2024-10-03 05:16:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ae104713-906e-3e52-99ee-e6f580b3234d | -10.66571 | -69.30544 | 2024-10-03 05:16:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bf9ead12-51d1-393f-bb42-cc1a63016e50 | -10.65199 | -69.6497 | 2024-10-03 05:16:00 | NOAA-20 | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b86bacd9-49c3-3130-9730-511624fe601b | -10.6253 | -69.25481 | 2024-10-03 05:16:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| de1152e2-637c-34f7-b8ad-16a5a0958b1e | -10.62465 | -69.25822 | 2024-10-03 05:16:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 348473ff-9451-341d-98ef-f59d36d87299 | -10.57723 | -69.43959 | 2024-10-03 05:16:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 81138663-7bd2-322d-9f19-370be9bfa25a | -10.57298 | -69.43955 | 2024-10-03 05:16:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 3ebedd0b-acba-3def-9e42-2ccb965e6cea | -10.5718 | -69.43861 | 2024-10-03 05:16:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 528129be-8822-33f6-bc4f-f99c2abf7656 | -10.56506 | -69.44457 | 2024-10-03 05:16:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 2.5 |
| de5651eb-ae02-3236-91ba-2018368ac6e9 | -10.56415 | -69.18165 | 2024-10-03 05:16:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ae6ca1ae-022a-3ef1-9b92-3b76c414ddb1 | -10.56351 | -69.18507 | 2024-10-03 05:16:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1815fc7e-2e23-303a-b835-ef3c3b1438ff | -10.55789 | -69.2442 | 2024-10-03 05:16:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1204b690-0728-3b00-bc09-30ca6dc761b4 | -10.55723 | -69.2477 | 2024-10-03 05:16:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e1dd1faf-0597-3054-a783-fb2edb315eed | -10.54916 | -69.23168 | 2024-10-03 05:16:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c5905a48-a087-328d-95c4-145346315fbd | -10.54849 | -69.23518 | 2024-10-03 05:16:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 2.6 |
| de42dcdd-9283-335a-bee9-29d2cc338fd5 | -10.54379 | -69.23071 | 2024-10-03 05:16:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 578a057a-b9a2-34fe-bf83-1f08cebf214c | -10.54313 | -69.23419 | 2024-10-03 05:16:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e15ea138-88f5-38d5-b040-8e10c91a733d | -10.54095 | -69.33397 | 2024-10-03 05:16:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d56af409-3022-3cc6-ab50-61ac1c24ef72 | -10.54029 | -69.33749 | 2024-10-03 05:16:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 920b51f6-3a03-3d11-808c-5507a5ab0056 | -10.53626 | -69.32925 | 2024-10-03 05:16:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0632dc03-783e-3feb-bac5-e0f61849d9d8 | -10.53559 | -69.33278 | 2024-10-03 05:16:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9775eedc-db15-3a2b-a8c0-02b4c5727c8b | -10.52046 | -69.2366 | 2024-10-03 05:16:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 4f02d347-6964-3891-a033-77bfa47399b6 | -10.51801 | -69.23642 | 2024-10-03 05:16:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 618930d1-1fe8-38ca-9d0a-f09a31c7dcca | -10.51737 | -69.2399 | 2024-10-03 05:16:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 83ab0406-e0c9-38bc-86b6-c626d1e0e334 | -10.5151 | -69.23558 | 2024-10-03 05:16:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 3.5 |
| c36d9b49-402f-3c43-ba80-895f4721cbd4 | -10.51443 | -69.23905 | 2024-10-03 05:16:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 117aa50f-e777-309a-a558-7b09985d6f70 | -10.50397 | -69.16242 | 2024-10-03 05:16:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 21847507-e776-3cae-bb01-015c4eeb63aa | -10.50334 | -69.1658 | 2024-10-03 05:16:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a38b02df-a393-35fe-a16e-de7844f4d7bb | -10.50072 | -69.45732 | 2024-10-03 05:16:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3f1db119-848d-31a6-b197-a55256fdbcf0 | -10.4953 | -69.45619 | 2024-10-03 05:16:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9a50db2c-4b78-3977-bab7-9cf5956f4674 | -10.45025 | -69.18337 | 2024-10-03 05:16:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 69a3f79c-63cd-3067-80f8-6dc3fcebfc5e | -10.4496 | -69.18681 | 2024-10-03 05:16:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 678a7dda-9009-3a91-ac98-11e8b9951d1a | -10.42031 | -69.70403 | 2024-10-03 05:16:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e0ef8418-f320-3b23-8cbc-8061c5c32867 | -10.41942 | -69.703 | 2024-10-03 05:16:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a2e9e70a-136b-30eb-a53b-19f08f7270ac | -10.41872 | -69.70663 | 2024-10-03 05:16:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 75877af0-fc36-3fff-9173-9aa1b7896f16 | -10.41482 | -69.70271 | 2024-10-03 05:16:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README177.md)
