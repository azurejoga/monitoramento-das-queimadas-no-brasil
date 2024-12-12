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

## Dados Diários - Página 30

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e6db900f-7aba-39a0-980e-d6d7ae6b213d | -5.92364 | -48.06363 | 2024-12-12 05:01:00 | NOAA-20 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 6e67583e-d104-3f3d-a3ed-9326689757fe | -10.5411 | -44.68022 | 2024-12-12 05:01:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 7f195fb9-69e0-318c-a535-4140dc82fda2 | -4.01926 | -53.986 | 2024-12-12 05:01:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| aba2dfdb-2328-34fd-94ae-929cf4b70ebe | -10.23728 | -52.84162 | 2024-12-12 05:01:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ce6a283d-4efe-3638-81cd-351cb607a3d3 | -3.60172 | -53.72263 | 2024-12-12 05:01:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c7458c00-e5ab-3de3-b5ec-54c61c65eca9 | -5.92484 | -48.05169 | 2024-12-12 05:01:00 | NOAA-20 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d82d0f68-215d-3e54-b60a-22af90d8e7b8 | -3.53314 | -53.94337 | 2024-12-12 05:01:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0383c064-29af-3b17-aa9e-b3bf0321de4c | -3.73155 | -53.78563 | 2024-12-12 05:01:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 953ff5e6-79ee-3940-86ed-f9ee7b1a03e2 | -10.54051 | -44.68527 | 2024-12-12 05:01:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 218885f9-8ff1-315b-bc47-ee66f6f3024d | -7.47397 | -44.73889 | 2024-12-12 05:01:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 00f8aea7-870d-34d7-bca0-68d81deb1ae3 | -8.31738 | -55.11909 | 2024-12-12 05:01:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 241774ce-7c21-3d26-bd5c-4d85b89c5d85 | -5.93041 | -48.04694 | 2024-12-12 05:01:00 | NOAA-20 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 09159678-7935-3d81-89ac-4696cc4952df | -10.53734 | -44.68757 | 2024-12-12 05:01:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 80346241-ddce-36df-b140-1c3a5e0d6783 | -4.07221 | -54.29934 | 2024-12-12 05:01:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 501fd4eb-001e-3e9c-9ad9-e08d9d209c96 | -5.91888 | -48.06293 | 2024-12-12 05:01:00 | NOAA-20 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 1c0ec940-1cdd-3b91-8bb8-5c601e6e4871 | -9.11243 | -49.46923 | 2024-12-12 05:01:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d46feb4f-2178-3cbd-8e7f-54f07f14799b | -5.3022 | -43.28564 | 2024-12-12 05:01:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| ba44a110-3524-3157-b7ed-a91dbb094b6b | -9.63715 | -56.85694 | 2024-12-12 05:01:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 940fc728-9d03-3550-a8fd-ea1e197a66f8 | -4.03324 | -53.65311 | 2024-12-12 05:01:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 996886ff-6dec-33fc-b4af-09d4f659cf58 | -4.83182 | -44.21446 | 2024-12-12 05:01:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5beefa6f-24a5-3a5f-95ce-4a9016483474 | -9.37595 | -57.55259 | 2024-12-12 05:01:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1b6d80bf-1c81-34f4-9829-b1e0298eca7a | -11.4791 | -48.21383 | 2024-12-12 05:01:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0d714f0a-118d-32f2-986a-09062f09953b | -7.47333 | -44.74355 | 2024-12-12 05:01:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| cb8db6e1-d4dc-33d1-b5d5-2aefd589ef54 | -9.31605 | -58.35135 | 2024-12-12 05:01:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8b3a3056-0c5c-3d6f-b217-633fd8278fd7 | -8.30513 | -55.10994 | 2024-12-12 05:01:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b1698902-b1a7-32d6-be5c-d257c452962b | -4.07113 | -54.30627 | 2024-12-12 05:01:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 152786ab-df1d-360a-be7a-6543534d4a01 | -10.59188 | -44.98399 | 2024-12-12 05:01:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| a0ca06e3-55b4-3a9d-8d40-48102b5797e9 | -5.92028 | -48.05293 | 2024-12-12 05:01:00 | NOAA-20 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 13.3 |
| ffcd5b2f-0dbb-3aa2-8124-41aea1f06acc | -10.34925 | -57.25015 | 2024-12-12 05:01:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e0c74995-6fe7-3b03-9b10-bdb62e6029f8 | -4.30088 | -48.10135 | 2024-12-12 05:01:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 886fb8e3-9f57-383f-bd58-e61a02a9eb40 | -4.8002 | -50.82223 | 2024-12-12 05:01:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 361b06a2-3e83-37f3-8f41-225044ca9108 | -5.30311 | -43.28171 | 2024-12-12 05:01:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 5be894ce-1fa3-36c2-acb3-fc80305f161e | -5.93057 | -48.04877 | 2024-12-12 05:01:00 | NOAA-20 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6d2566fe-c0da-3999-aea2-7eb6f62751ef | -9.19094 | -49.4778 | 2024-12-12 05:01:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 01e508ed-1f12-3fad-abcb-7a81278e604c | -5.09361 | -45.83783 | 2024-12-12 05:01:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 74cac9e7-3806-306f-a74c-8cd079a973dc | -4.80409 | -50.82282 | 2024-12-12 05:01:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e2748d35-52a2-349d-b1af-6a1428330eb2 | -5.92433 | -48.05865 | 2024-12-12 05:01:00 | NOAA-20 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 13.2 |
| d8419978-36e6-371e-8271-217597cccfb2 | -10.53798 | -44.68249 | 2024-12-12 05:01:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e160f7e9-7684-3b75-b397-e41b73e5366a | -7.42978 | -44.74544 | 2024-12-12 05:01:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e569afa3-8074-3cbc-babb-4859fe0acb8a | -4.49814 | -46.10848 | 2024-12-12 05:01:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c59ebb15-8c6d-327f-a60d-16c2634ce7d4 | -5.92505 | -48.05353 | 2024-12-12 05:01:00 | NOAA-20 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 13.2 |
| a0d384c4-1282-331c-b73e-a058f456abed | -4.56977 | -48.47661 | 2024-12-12 05:01:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 9f1aaa01-aab5-314a-aba5-8cacff096c15 | -4.01956 | -54.28749 | 2024-12-12 05:01:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 72e8e254-964c-39ee-9bf3-ea258c95bb8e | -4.11813 | -54.91535 | 2024-12-12 05:01:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bf298789-a425-34a6-bd01-3b4fcbf74e64 | -4.56821 | -48.47871 | 2024-12-12 05:01:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 888103a5-1a32-380a-8ff5-40611e1c8a63 | -3.85989 | -54.39767 | 2024-12-12 05:01:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4dd7ca30-cb8c-3480-8fe6-2848231be663 | -3.67743 | -54.3051 | 2024-12-12 05:01:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d6836ac6-c7a9-3655-9500-33e5caffdb98 | -5.92333 | -48.06191 | 2024-12-12 05:01:00 | NOAA-20 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 4fa084de-3d14-390b-bb1e-f90d3444d4ac | -4.07167 | -54.3028 | 2024-12-12 05:01:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b8aa6c3b-d882-3599-8429-6eac380248dd | -8.6231 | -50.01656 | 2024-12-12 05:01:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c2c9c77d-1c7e-3842-915b-d6a99fd64fe5 | -9.23433 | -46.6726 | 2024-12-12 05:01:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1ef28122-0c79-326f-bfe9-c8813f68ad74 | -5.18753 | -56.08256 | 2024-12-12 05:01:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 6b410714-9428-33b2-91ba-ef95bf4bb63b | -5.14077 | -46.18252 | 2024-12-12 05:01:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2b76bf9e-7408-373d-8696-e6cc5287fd9f | -3.59837 | -53.72211 | 2024-12-12 05:01:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 63a549d8-1d68-3125-ad77-63156e5ec820 | -4.11314 | -54.90399 | 2024-12-12 05:01:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7f48f840-f94c-3e57-9031-174966537236 | -3.60228 | -53.71908 | 2024-12-12 05:01:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d5c45e5a-414f-3898-a106-dd9c6b941760 | -4.075 | -54.30332 | 2024-12-12 05:01:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 137ff03c-adff-3488-a1b0-ff29cbc9e4ce | -10.51262 | -53.58116 | 2024-12-12 05:01:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| cd3db267-6d35-3720-b448-d499a5ca426a | -3.67412 | -54.30458 | 2024-12-12 05:01:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1bb16516-5a8a-3e9d-b6f4-31453a0b07e3 | -6.05506 | -44.04758 | 2024-12-12 05:01:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 916ba67b-11d4-3d75-bf93-16a87e6eac4b | -5.91858 | -48.06122 | 2024-12-12 05:01:00 | NOAA-20 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| b5e62f30-e711-3c00-a916-88b92637b9b5 | -4.13073 | -54.33638 | 2024-12-12 05:01:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 692abd16-185f-3a3d-9920-2ef40830cf3b | -5.14124 | -46.17914 | 2024-12-12 05:01:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1d376522-f0a1-3162-88f4-97da69ca7431 | -9.23544 | -46.66962 | 2024-12-12 05:01:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8e1d3f93-0bed-3ad5-bbc4-62fb9a784f6c | -10.34981 | -57.24662 | 2024-12-12 05:01:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 57be5a27-a4fc-3552-be2a-f6ef7eec0189 | -9.23481 | -46.66909 | 2024-12-12 05:01:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e29c6003-69fb-39f3-bc5a-311921628066 | -9.31666 | -58.34757 | 2024-12-12 05:01:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 95e3789c-e303-322d-a4ff-10de6484ed84 | -4.56892 | -48.47397 | 2024-12-12 05:01:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 68908b89-acbd-3f02-96cf-306d16812418 | -10.29569 | -53.69954 | 2024-12-12 05:01:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e0e48fc9-fad1-3f5c-9407-389d6b3a5d0a | -14.9164 | -52.87696 | 2024-12-12 05:03:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d84bccaa-5b7d-380c-b9db-70bec1ffe0fe | -14.75449 | -52.65057 | 2024-12-12 05:03:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| cb0937dc-10eb-3e5c-a518-4c8dd57c193f | -15.08193 | -59.64657 | 2024-12-12 05:03:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 05021ced-2a73-33cb-8b70-367de9e0d36f | -15.08105 | -59.63056 | 2024-12-12 05:03:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c8bca9bb-9834-32b7-b092-579e599561bf | -15.07889 | -59.62231 | 2024-12-12 05:03:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c932e7e6-3190-3a10-bb08-f7995990bac6 | -14.74838 | -52.64804 | 2024-12-12 05:03:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 4794020a-e5ff-39b2-bdd7-6c66f6449d68 | -11.43179 | -55.91423 | 2024-12-12 05:03:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 358af4b3-54b4-3a4e-bb36-849d97a93206 | -15.08295 | -59.61908 | 2024-12-12 05:03:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bef61f0c-33d9-3b9a-b2fe-c5a48571a104 | -15.96751 | -57.16951 | 2024-12-12 05:03:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 03531a8b-4063-3691-a2fb-ef774ae913df | -13.3738 | -54.24635 | 2024-12-12 05:03:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fa1fb099-2305-3acf-b699-0ba5b1e05831 | -12.5702 | -57.76623 | 2024-12-12 05:03:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d14e0185-3f96-35f0-979a-42617f3fc79c | -15.07036 | -59.65244 | 2024-12-12 05:03:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1ab6ec6e-9e9a-37c8-b6c5-d490a817d76e | -12.57134 | -57.75913 | 2024-12-12 05:03:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cbcbfdcc-cdbb-33e8-a805-dfbfde3e0243 | -14.75558 | -52.65446 | 2024-12-12 05:03:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 71a056fa-b48d-3b22-bb5b-5a592e7d6e81 | -12.91768 | -55.72931 | 2024-12-12 05:03:00 | NOAA-20 | SORRISO | MATO GROSSO | Brasil | 5107925 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1ba6c378-6672-3cdc-ae11-aa15e0b4e92b | -15.08168 | -59.62673 | 2024-12-12 05:03:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c2222ca7-7460-3260-b7bb-014bdbe72bab | -15.96862 | -57.16229 | 2024-12-12 05:03:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 46fcdd3a-ff81-3333-9ba5-bb0d71c6437a | -15.07723 | -59.65364 | 2024-12-12 05:03:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fb8289ec-c894-30ff-8251-995193652b18 | -14.74368 | -52.65269 | 2024-12-12 05:03:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 687eb31e-e1b3-367a-b010-7df588c4b4f6 | -15.08041 | -59.63441 | 2024-12-12 05:03:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 61f20ffc-bdcf-3493-83b2-36bf9d6d230d | -11.19974 | -53.83887 | 2024-12-12 05:03:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 35b4ebb4-e366-3e73-babd-59b0b2d47e86 | -11.20807 | -53.83178 | 2024-12-12 05:03:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e5549f52-5872-3a95-b883-1a2e1a80c15a | -12.11959 | -64.16672 | 2024-12-12 05:03:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c1e7d441-7a7d-30d1-9008-49a7cba8544f | -10.51829 | -58.80664 | 2024-12-12 05:03:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 31c26509-e2b2-35fa-b5c2-fad0e0efdd91 | -12.54092 | -57.73582 | 2024-12-12 05:03:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 87cb1e76-e815-3157-b06d-2f1776295193 | -15.92575 | -59.80694 | 2024-12-12 05:03:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5918df6f-5ac8-378d-bd52-1b4c079dd4de | -15.08384 | -59.63502 | 2024-12-12 05:03:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e8d28b12-05b7-3683-a388-d606b3bb2c30 | -12.54036 | -57.73937 | 2024-12-12 05:03:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8bb29e51-fac9-34e0-9b5a-f6403d6310b0 | -15.09196 | -59.62855 | 2024-12-12 05:03:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8de9c9ef-9e6e-3f2b-88ae-7940de2b1c19 | -13.32247 | -52.41006 | 2024-12-12 05:03:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2eed1b8c-4fc3-35c2-8268-544647ea18b1 | -12.53266 | -57.72351 | 2024-12-12 05:03:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |


[Clique aqui para ver as próximas entradas](README31.md)
