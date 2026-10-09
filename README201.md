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

## Dados Diários - Página 201

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e42fe101-c572-3416-acfd-e673fa9a01d5 | -2.62141 | -56.48413 | 2026-10-09 05:23:00 | NOAA-20 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 10ed95c5-338b-3deb-8ab1-d63677596b3f | -3.15515 | -57.68303 | 2026-10-09 05:23:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8ca8e5da-734f-3207-9761-b3fcd98ddb58 | -7.22081 | -55.13715 | 2026-10-09 05:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 145a886e-527c-3f9b-bc22-07b17e24f621 | 1.7019 | -55.59843 | 2026-10-09 05:23:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8d28cbb9-d7f2-36f1-81ff-6278927c9f5e | -3.82866 | -59.39293 | 2026-10-09 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 75d126f3-b2f7-38df-8618-42b182e11d2e | -2.51041 | -56.16394 | 2026-10-09 05:23:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cfc8c15d-2326-3079-950b-5400f82bd778 | -2.90578 | -57.21827 | 2026-10-09 05:23:00 | NOAA-20 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 42f72866-bb3e-31d4-947c-a2445ac4f5cf | -3.56538 | -59.4691 | 2026-10-09 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1e267b79-839d-3eb2-8d45-6a03fa02caca | -3.40583 | -59.59546 | 2026-10-09 05:23:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9a69a34a-75ad-3cf9-a578-e3051bac3a18 | -2.89351 | -56.67067 | 2026-10-09 05:23:00 | NOAA-20 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 013f75c4-3d0d-3cf3-a273-3605b550a92c | -2.73516 | -54.11402 | 2026-10-09 05:23:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4cbe744b-bb76-3524-97b8-e909b09bbc6d | -2.86679 | -54.16521 | 2026-10-09 05:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bed28cfd-9827-35ac-aa5f-a8209ce95553 | -9.09722 | -59.40041 | 2026-10-09 05:23:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4eecc3c2-8c9b-331a-a743-e4f2d7947908 | -3.07531 | -54.29302 | 2026-10-09 05:23:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3893b0f2-4792-3a50-b87c-61326ade2936 | -3.71055 | -58.91901 | 2026-10-09 05:23:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 38dbd554-9c53-399d-8e33-b5146809dd69 | -0.24692 | -55.91633 | 2026-10-09 05:23:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2a05dced-d4ec-37eb-a106-4d20a604bfd6 | -3.50264 | -59.26577 | 2026-10-09 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ae9fa7ad-5942-3b71-8bcc-ed131ad596bd | -3.60208 | -61.62337 | 2026-10-09 05:23:00 | NOAA-20 | ANAMÃ | AMAZONAS | Brasil | 1300086 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c0da4adc-9af6-3315-87cc-3a369e133f4c | -1.28756 | -55.69475 | 2026-10-09 05:23:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| aa5ce037-f41b-3da8-920d-a1d22e2ca0aa | 0.78097 | -59.19579 | 2026-10-09 05:23:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 97cc57a3-cb9b-3ee8-92e5-c885151226f9 | -6.69008 | -59.96622 | 2026-10-09 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 27517929-de31-3455-861d-2d54c0c4ce93 | -3.98465 | -59.35266 | 2026-10-09 05:23:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 4d43526b-fc32-3e8d-80ae-6316749ac121 | -4.73742 | -54.60675 | 2026-10-09 05:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7abb0a43-6c86-3c74-a4fc-ffa548d0efbe | -4.57971 | -55.725 | 2026-10-09 05:23:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 273492e8-f624-3bfb-b350-359518fd401c | -3.52438 | -56.89329 | 2026-10-09 05:23:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 02b335a3-a85d-3b12-a56a-204712df7dd2 | -3.2781 | -53.8195 | 2026-10-09 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2b54c9b8-c613-336b-888b-2a52708538bc | -4.15144 | -47.98935 | 2026-10-09 05:23:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 684b9d4d-de24-3ce1-a24c-3bdc56c36a34 | -2.46262 | -56.09166 | 2026-10-09 05:23:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a3bd99f4-0afd-3c29-9627-d51dccb95e61 | -3.12034 | -54.17249 | 2026-10-09 05:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 17.1 |
| 5ed55051-85f4-311d-9e3f-a85679c326bb | -2.81882 | -54.09539 | 2026-10-09 05:23:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e0a78ab2-306b-38c2-b143-769d836f1634 | -3.20662 | -58.00333 | 2026-10-09 05:23:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6bb5ac7a-3819-3adb-83d1-080a9a8fc87a | -2.07233 | -46.57442 | 2026-10-09 05:23:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0a393ab9-388d-3117-870a-36df532ceb78 | -2.84618 | -59.11967 | 2026-10-09 05:23:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4ec4ac14-3813-3a36-911d-3b21988ca841 | -3.43627 | -56.93901 | 2026-10-09 05:23:00 | NOAA-20 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e5f6fac7-eb5c-3871-be56-4810c2b29d12 | -3.28281 | -60.9992 | 2026-10-09 05:23:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8f87a54f-365d-3583-a915-0c8b3c4b7b35 | -1.32675 | -55.44508 | 2026-10-09 05:23:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 20b9103d-d861-3014-8136-48e48529dd3c | -3.11504 | -54.16488 | 2026-10-09 05:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 18af2ada-e537-3520-964e-51b9ebc49d60 | -6.73308 | -63.04713 | 2026-10-09 05:23:00 | NOAA-20 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7080c49b-0263-376d-9e6e-9a934f55391b | -3.08055 | -54.28446 | 2026-10-09 05:23:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a312e0c5-cc62-396a-89bb-81b091af4628 | -3.05899 | -53.9407 | 2026-10-09 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8011a54b-7a35-3cdf-abce-cc51b390a012 | -9.09942 | -59.38645 | 2026-10-09 05:23:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2baa3326-c02f-3d04-be48-26ed2cd86df2 | -3.55522 | -54.69123 | 2026-10-09 05:23:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 6cab2101-aa81-3f17-aa52-2a445d63ffb4 | -6.6099 | -62.97268 | 2026-10-09 05:23:00 | NOAA-20 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4cfaa1f9-8508-3fb4-b50f-8afa1ef74d6d | -2.88546 | -54.1901 | 2026-10-09 05:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| bd5e72a5-f585-3a88-ae73-75bc62ecdc25 | -3.29309 | -51.57116 | 2026-10-09 05:23:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 280ecc58-9b80-34ce-ac20-d6719732ce39 | -2.84056 | -54.13249 | 2026-10-09 05:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3fcda52f-e304-3515-9fe1-15d92c425511 | -9.68947 | -58.09512 | 2026-10-09 05:23:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 07d083c9-9905-3c6d-a669-07361377d246 | -8.70527 | -62.41557 | 2026-10-09 05:23:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 740ae4b1-e0e8-36ad-ad45-abae9e28c457 | -2.58221 | -56.15582 | 2026-10-09 05:23:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e36b5f75-bb5a-3a2b-91a2-b53d1954e921 | -3.52544 | -59.35515 | 2026-10-09 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e77a6e9f-532c-3acf-b166-853bb93f8d1d | -2.51526 | -56.26773 | 2026-10-09 05:23:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d03c90ce-c9df-3bde-b84b-85d9a366276e | -3.34704 | -50.40672 | 2026-10-09 05:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 43c8b733-2cb0-3c47-9bc1-e81ab6c1e129 | -6.94352 | -59.10007 | 2026-10-09 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e445385f-5469-37fa-84c7-335aa80bb69c | -3.48384 | -59.38445 | 2026-10-09 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0fa56ada-b183-31b5-b756-8bde5bd09848 | -3.00982 | -54.0565 | 2026-10-09 05:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8f2fc193-04da-3b65-ada4-b48677131f41 | -3.0113 | -54.12495 | 2026-10-09 05:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9e734031-b25e-31ef-9406-5b1e96672286 | -2.77351 | -56.49921 | 2026-10-09 05:23:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4a41fed2-c34c-3416-8cf2-f9114eff07e2 | -3.35377 | -59.47564 | 2026-10-09 05:23:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b8a184fd-1069-313c-9dbf-931fb4af4cca | -3.57017 | -54.6935 | 2026-10-09 05:23:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 229d37a1-5a30-3695-a856-3f1d3273beae | -2.98 | -54.05949 | 2026-10-09 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c41ff346-7804-365c-8a12-d9bb3da61261 | -3.6551 | -54.52272 | 2026-10-09 05:23:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 548f716a-62d5-3f09-b351-8a7ac70f7e18 | -3.30673 | -53.86686 | 2026-10-09 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 240bb3a9-f335-385e-ad42-8b47199dbb39 | -2.75722 | -54.0981 | 2026-10-09 05:23:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 378bfcfd-c11b-36de-877c-2a187b7adde4 | -3.25878 | -54.02478 | 2026-10-09 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d2d95d93-f2c1-3b90-a4fc-9b8f058e57ca | -3.64808 | -59.56892 | 2026-10-09 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 57640abd-fba3-343b-b001-c80e9669eedb | -2.41009 | -56.53383 | 2026-10-09 05:23:00 | NOAA-20 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d1eb8d05-af70-33ab-9a2e-68f4a54e87ab | -7.23152 | -55.14396 | 2026-10-09 05:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 99ab01ef-d3be-3a9d-9d47-998c0207e200 | -3.08833 | -54.30664 | 2026-10-09 05:23:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a76ff1ef-4825-3f63-9554-bf17495c839e | -3.00855 | -54.07852 | 2026-10-09 05:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 87bc79e2-bdc0-359d-8ccc-32ecf66ffeae | -3.0136 | -51.00945 | 2026-10-09 05:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| ff046fef-0aa4-3e95-9f3b-a7c02ae9f55f | -3.89799 | -59.45045 | 2026-10-09 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d7f83f62-9b6e-3513-b5b3-917c87318958 | -2.40952 | -56.53746 | 2026-10-09 05:23:00 | NOAA-20 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 66203fe0-4204-3fec-9f46-a9b47dd6bacf | -2.52696 | -58.06898 | 2026-10-09 05:23:00 | NOAA-20 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7e55141c-a45b-382a-bb86-060abb419f27 | -6.9992 | -59.11243 | 2026-10-09 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0f840320-3511-342c-9389-1703b2ca7c27 | -3.98188 | -59.34866 | 2026-10-09 05:23:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| e45dfa7b-730c-304a-96e2-ac39c1ad2482 | -3.55219 | -54.68615 | 2026-10-09 05:23:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c7c41cff-5c83-3442-a0fb-e4498d7eaf8f | -2.75959 | -54.10808 | 2026-10-09 05:23:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 7dd0ebd9-5f75-3e4f-856e-e9b3bbfa5494 | -3.30078 | -54.06087 | 2026-10-09 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 214a88e1-ace5-3e72-9014-b4c9ad0da273 | -2.89869 | -54.07631 | 2026-10-09 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 672632ab-22fa-3ed9-bc90-fb2ac598cdda | -3.5957 | -58.9996 | 2026-10-09 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9662f458-dd65-3a3c-b95b-c371748f21d5 | -2.90299 | -57.21422 | 2026-10-09 05:23:00 | NOAA-20 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 676711be-3ccb-37ab-af0c-2bac0ac972aa | -3.74802 | -59.47305 | 2026-10-09 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| d3a88ef7-02f9-3e68-b1d1-94d0bd85b291 | -3.30839 | -54.03729 | 2026-10-09 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c5d60293-866b-3d63-957e-8b451eae7170 | -3.22609 | -53.97265 | 2026-10-09 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 87ce97ce-4a7c-3966-a833-c53271ec3756 | -7.57215 | -61.54052 | 2026-10-09 05:23:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 15fb61f4-10bc-36e3-85c8-1331803be7a4 | -4.10961 | -54.01956 | 2026-10-09 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 23e574e5-ca29-32e5-96f8-922c3a8e10eb | -3.72879 | -53.69797 | 2026-10-09 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| ef316f17-0ec8-36e1-92e2-f504423cc604 | -2.82066 | -58.29512 | 2026-10-09 05:23:00 | NOAA-20 | SILVES | AMAZONAS | Brasil | 1304005 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3053cfcf-0218-36c8-ac51-28537c839687 | -2.85626 | -59.2672 | 2026-10-09 05:23:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 37702d63-f1dd-3098-92d7-7843039dcf07 | -3.52989 | -59.34869 | 2026-10-09 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2897c10c-7a6a-326e-92fb-f16ba0e17616 | -1.30197 | -54.19209 | 2026-10-09 05:23:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 44f286e8-6a10-3d27-841b-de94a7bf9b57 | -3.39825 | -57.99483 | 2026-10-09 05:23:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 951cd5ad-da94-3cc6-97b9-d0bf38182935 | -4.56119 | -54.21293 | 2026-10-09 05:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 328a0391-0e85-3756-931b-742695d9eac1 | -3.0064 | -54.11709 | 2026-10-09 05:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ab7673f0-78f5-387b-b3a9-f95ead07e675 | -3.02576 | -57.64205 | 2026-10-09 05:23:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 89fd3200-8745-3d5f-936e-bc12e59a28ee | -3.25974 | -54.04453 | 2026-10-09 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 9f4295b5-7bd5-3e68-93b0-ec34e1e40b06 | -1.81093 | -57.11644 | 2026-10-09 05:23:00 | NOAA-20 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 84bc3b63-c2ab-30e6-924b-f1e4b213b48f | -3.7531 | -56.84298 | 2026-10-09 05:23:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6d906d6a-b3cd-3d1a-92d7-4ab28cd1e12b | -3.21024 | -54.36982 | 2026-10-09 05:23:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ab9270aa-fd31-3bd4-85c3-69ca8df0f8f0 | 0.61318 | -60.12997 | 2026-10-09 05:23:00 | NOAA-20 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README202.md)
