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

## Dados Diários - Página 118

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 086f3c4f-fac7-3ee7-bb17-0bde77b2d69e | -3.5032 | -49.93843 | 2026-10-10 05:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3400ec04-3688-3e3a-99f5-ad10779f5100 | -5.31033 | -60.08582 | 2026-10-10 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cf1a1db2-ab25-3b0d-aaa0-065e2363cb90 | -6.04438 | -59.92389 | 2026-10-10 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9b3716f9-d181-36ab-8c9b-0b2acfa76a46 | -5.96657 | -55.38457 | 2026-10-10 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9b46b829-978a-32e2-b88d-e139eb38a66e | -6.51016 | -55.40631 | 2026-10-10 05:04:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2cce3d60-d6e1-34f9-b6db-3b6a0c51389b | -3.35064 | -50.42147 | 2026-10-10 05:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 01e6efcd-b605-3c06-b974-3338cb1d5982 | -3.33714 | -57.62275 | 2026-10-10 05:04:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| efeac81e-7051-3fec-a6a3-f2543ab454f3 | -4.61146 | -49.21107 | 2026-10-10 05:04:00 | NOAA-20 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| bd597943-9945-344a-98f1-f341cb6a012b | -3.10355 | -53.77514 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0f23fa78-e9fa-31fd-af0e-73939e7cb702 | -6.44296 | -55.03979 | 2026-10-10 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a3636159-521a-3f3b-90f4-e8472159b482 | -4.13901 | -51.14632 | 2026-10-10 05:04:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 646fcf71-e864-345f-9760-cd5441bc279c | -3.09883 | -53.93294 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4b118d78-b582-3fc1-9bc1-ba311bab11c4 | -3.558 | -54.69865 | 2026-10-10 05:04:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 70e8e6d2-9473-30ff-9066-116f4a8cb2fd | -2.89279 | -59.2134 | 2026-10-10 05:04:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cf76c96d-7a4c-3d25-92f7-7aff6462a359 | -3.98788 | -54.45275 | 2026-10-10 05:04:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a9003c42-d4d2-36aa-aa76-0d8c9b28b0f8 | -3.25011 | -54.02737 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8f874cb0-a9ee-39a0-acfc-234c2a8d00ce | -5.71936 | -53.49458 | 2026-10-10 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 77308b9e-7278-3c3c-a97d-db0efdef3e45 | -5.30605 | -60.0851 | 2026-10-10 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ddb77745-1f2f-337a-86ac-d6db2f7b5100 | -5.81208 | -53.42337 | 2026-10-10 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a71bdea2-2f3a-31cb-a045-b25e8ec77039 | -3.12171 | -53.76742 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 962950b0-2121-3fe0-b783-86a6b958b7d9 | -1.61847 | -55.14088 | 2026-10-10 05:04:00 | NOAA-20 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 879c4773-c3f3-34dd-9be7-e6f4d5494b9f | -3.31874 | -54.04562 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 82205365-b0d1-3585-baf6-c8abe366d77f | -6.6414 | -55.33016 | 2026-10-10 05:04:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 936b70b1-0267-3096-a7f5-dff5145ddd22 | -3.27261 | -54.70081 | 2026-10-10 05:04:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e7e2dcc5-c2bc-39a3-bd6e-b35bc410469e | -1.32633 | -56.40343 | 2026-10-10 05:04:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8736dcf1-1607-39f9-9c37-196072e08e38 | 0.2298 | -60.38811 | 2026-10-10 05:04:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cceac35a-00d9-372c-98c9-321a69c0854f | -0.98286 | -52.44647 | 2026-10-10 05:04:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 111d935e-9d97-3bf8-9f9f-dfedc4ac7d7f | -6.04764 | -59.9047 | 2026-10-10 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 76971d13-be64-3b67-b755-688f49d96d09 | -3.57836 | -59.0795 | 2026-10-10 05:04:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| aefbbaa8-2aca-3ca6-b150-fb81ef7bfea7 | -4.59449 | -56.17455 | 2026-10-10 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 651ddff8-40cc-3b68-beb8-fb9865bb8d83 | -3.11568 | -53.78408 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f0acc228-890c-386a-a014-2e9f5754efe3 | -2.49779 | -58.07592 | 2026-10-10 05:04:00 | NOAA-20 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cd552c81-9ac5-3564-b40a-2f4f0315bf5d | -4.3727 | -54.74537 | 2026-10-10 05:04:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| e58ec750-30be-3f45-8845-9b9ecbb1bd10 | -3.01152 | -54.05362 | 2026-10-10 05:04:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1f755e5a-b4a2-3d3c-b8f8-cf8fe9fc2eb9 | -3.0626 | -53.92393 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9cb284b2-9562-3b94-8f4a-5fb197bde4e0 | -3.26505 | -54.06149 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3a6229e0-8212-368f-a452-c07aa6fb8133 | -1.10061 | -54.12521 | 2026-10-10 05:04:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 17dbb76b-3c3b-362b-885e-22dd70fabfb2 | -4.32599 | -55.01512 | 2026-10-10 05:04:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 794ec9a4-0f55-3c2c-873a-9d9618b2c587 | -3.27743 | -53.87644 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 58b7e9db-418f-312c-84bf-bffb6b0e2188 | -1.32536 | -55.35421 | 2026-10-10 05:04:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5735756e-1cf9-3002-a8a3-3a797474c716 | -2.95861 | -54.13023 | 2026-10-10 05:04:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a62afd94-8275-3c57-91e1-0750fac0431d | -2.95552 | -58.42432 | 2026-10-10 05:04:00 | NOAA-20 | SILVES | AMAZONAS | Brasil | 1304005 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3c169ffa-b8af-3972-899e-790256116065 | -3.10139 | -54.2801 | 2026-10-10 05:04:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bdfc4eb5-1221-3774-a5ee-f513173b623c | -2.39408 | -51.30413 | 2026-10-10 05:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8a376126-e7ca-3d66-963d-b50350de631b | -3.58248 | -59.08017 | 2026-10-10 05:04:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 85eb73c4-06f6-371e-9801-c1ffafea05ba | -5.69719 | -53.4624 | 2026-10-10 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| df8a1dad-3662-3757-b890-4b2fcb0b7dab | -6.37302 | -55.15749 | 2026-10-10 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8a01b910-8489-3f31-a28e-eb1a98d08f20 | -2.29701 | -53.80289 | 2026-10-10 05:04:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e4be2bcd-3959-37c5-b75a-808bee4b5ac1 | -3.64038 | -54.52227 | 2026-10-10 05:04:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 205e4c66-aea8-3d85-bdb1-a01d62db5825 | -3.68041 | -55.95179 | 2026-10-10 05:04:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7acfb124-a620-3952-9ea3-01dccbbb4817 | -3.93522 | -55.71883 | 2026-10-10 05:04:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bfe0b930-e625-3fdc-9036-5160ecd6b106 | -3.12063 | -54.18026 | 2026-10-10 05:04:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 64c5f0ed-4e68-30c5-b413-e346ce54cf49 | -4.1083 | -54.01545 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| eefcb9da-82d8-31c7-be47-8190666c28bc | -3.25898 | -54.05702 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ef034242-3591-3daa-8050-22f43110b58a | -2.40179 | -57.89719 | 2026-10-10 05:04:00 | NOAA-20 | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e755dc4c-3f95-3c83-a42a-a72bd26daa8b | -5.88279 | -43.40548 | 2026-10-10 05:04:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5483fe10-f20b-3276-853c-85f82bc65301 | -7.19264 | -52.63435 | 2026-10-10 05:04:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| e92d421b-f014-3406-90d4-dc327c20a997 | -4.40733 | -49.76759 | 2026-10-10 05:04:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 17.2 |
| 80781818-6486-31c5-a3c7-17bd9af6b8a1 | -6.20818 | -45.43107 | 2026-10-10 05:04:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 1e2adb5b-ec13-31a3-9131-6689896e99b8 | -4.11934 | -54.0313 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e97894d3-17ea-3ae2-871c-1204f11b47b7 | -6.49311 | -55.32047 | 2026-10-10 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dce52a61-a402-3087-86a0-d7790f110f37 | -4.55954 | -54.97929 | 2026-10-10 05:04:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ab4bd63f-baef-310f-8d4f-89aa9095c55c | -3.38803 | -44.48793 | 2026-10-10 05:04:00 | NOAA-20 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 083f2d73-d29e-36d8-b62f-3c5f57ff73c2 | -4.17839 | -55.68926 | 2026-10-10 05:04:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 823b3432-0221-324d-bd51-30de494b839a | -3.66356 | -57.00821 | 2026-10-10 05:04:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a9c79004-3759-36af-9b85-57e47abbc189 | -4.10721 | -54.02233 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8da7428c-1d80-318b-a1a0-396b57450a74 | -2.06088 | -61.144 | 2026-10-10 05:04:00 | NOAA-20 | NOVO AIRÃO | AMAZONAS | Brasil | 1303205 | 13 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 725fdef8-cc2a-3631-9395-99ed393e1123 | -3.76157 | -57.16821 | 2026-10-10 05:04:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2a489c2f-6ce1-33ca-a699-4aabc67827f4 | -3.02326 | -54.17226 | 2026-10-10 05:04:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3e743a04-9bdf-314b-a5d2-2eba8c2dbc9e | -6.94618 | -59.11142 | 2026-10-10 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 412fcf37-c7ac-34a6-ad60-78496494e519 | -6.44985 | -55.2919 | 2026-10-10 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 40bef3cf-cbd6-3ef0-95ee-a2d5a7ade50a | -3.19987 | -53.95948 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| de740c48-ffd5-3698-88f6-a0a671c3d9ea | -1.10947 | -54.17685 | 2026-10-10 05:04:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1d95838b-1fa5-3b61-bd90-24fca7d0b7df | -3.32065 | -53.84143 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bfd1b378-d0fc-38f7-8bd5-633d80578789 | -3.18715 | -60.04863 | 2026-10-10 05:04:00 | NOAA-20 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 308e9fee-9688-38c2-b70b-5c0612dad0c1 | -2.99755 | -53.90666 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9198041b-0ec3-3ac3-abf9-af220718a28f | -3.56706 | -59.09665 | 2026-10-10 05:04:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| b4b938fb-236c-3774-adcc-4c599df71519 | -1.87736 | -56.30794 | 2026-10-10 05:04:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9ea662d0-2d59-3f7e-9049-0641d74ecd9c | -3.32575 | -54.70543 | 2026-10-10 05:04:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 443f59a6-7897-3357-bfae-993c989cd0ab | -3.45297 | -59.5504 | 2026-10-10 05:04:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| eb83cd2e-2793-39c2-8185-90f0c48fda27 | -3.2615 | -54.25602 | 2026-10-10 05:04:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e3d9fc8e-fd43-383b-bf10-e745bf30a634 | -3.53051 | -59.34219 | 2026-10-10 05:04:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 71425fa2-a489-3f4e-bd50-993db4fd5ef1 | -3.53794 | -54.73864 | 2026-10-10 05:04:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 7c506ade-8223-3364-b89d-2a722466d7e6 | -3.49895 | -54.19468 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| eefd61cc-c127-3efc-8aae-30acd225f8eb | -3.47378 | -46.06906 | 2026-10-10 05:04:00 | NOAA-20 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0f6f29e8-7f5a-33f5-84cb-5145c4cd4467 | -2.58798 | -56.14431 | 2026-10-10 05:04:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6d181f48-5a2e-3e70-8275-97fd4905954f | -3.22017 | -53.89566 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 873562dc-0554-3a88-ac07-643880b82fa4 | -4.12884 | -50.83541 | 2026-10-10 05:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7d6622df-54ce-3606-a85b-8d9aff04e419 | -4.81869 | -56.08964 | 2026-10-10 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9ac9c9cf-6a1f-3912-9513-20c20d2b39ba | -4.37814 | -55.16122 | 2026-10-10 05:04:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 39194cb7-4b52-37d0-931b-e1d16e6624ac | -3.42417 | -54.06582 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5dc35eb2-3934-31c1-9dbf-a47f516ac91a | -7.52326 | -45.31824 | 2026-10-10 05:04:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| aeb727b7-32e4-351b-9cbb-c98e5b08e653 | -6.46259 | -55.48931 | 2026-10-10 05:04:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 19ad888a-f558-3e3b-9a90-a5e9705c51b7 | -3.57897 | -59.07582 | 2026-10-10 05:04:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6b3dfb85-04af-3051-8d0d-95d09be93d7a | -3.48051 | -50.33207 | 2026-10-10 05:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2e6ac9f3-84cd-3762-9990-f884d1ec6181 | -2.86758 | -54.87256 | 2026-10-10 05:04:00 | NOAA-20 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c4f1aa4f-fbec-3b92-853f-a13718f18203 | -1.47133 | -54.63525 | 2026-10-10 05:04:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 85046834-30d6-3adb-83b5-cce090a356d6 | -4.57627 | -54.96031 | 2026-10-10 05:04:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1d7d517f-6ac1-3dcc-970b-7389882f6f66 | -8.23948 | -46.42565 | 2026-10-10 05:04:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9e109c5b-2b0a-3982-955c-045277ae1998 | -3.12118 | -54.1768 | 2026-10-10 05:04:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |


[Clique aqui para ver as próximas entradas](README119.md)
