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

## Dados Diários - Página 25

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9430275e-96a9-3f2a-aff6-0edef78409df | -7.93914 | -44.13947 | 2025-10-15 04:06:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 32d6b48a-eaf5-33c0-871c-5d1534ae8b3e | -5.181 | -43.13481 | 2025-10-15 04:06:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 20a3b74d-3d97-368c-ba43-71c35ad1e858 | -6.45602 | -44.57759 | 2025-10-15 04:06:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 14ad511d-e6ee-3397-a32e-392e360bdba0 | -2.8621 | -49.17146 | 2025-10-15 04:06:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a45f34b9-37ef-3a05-8ee2-e5c5efa95819 | -5.41433 | -44.22646 | 2025-10-15 04:06:00 | NOAA-20 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 37e4b45f-33b1-3600-8122-a30b7c726b46 | -7.64217 | -42.58312 | 2025-10-15 04:06:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| fec2e97c-508d-34e0-bc82-1bb9b39be9a4 | -4.94061 | -45.52974 | 2025-10-15 04:06:00 | NOAA-20 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bb808127-a153-3fbd-967d-a0581a6be02a | -5.27401 | -45.171 | 2025-10-15 04:06:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 0338e91e-811f-3e8d-b1b4-9033cfe3087c | -8.21278 | -44.01585 | 2025-10-15 04:06:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1e3b68b5-ed0d-3ec1-adad-40c31fafb97e | -5.24443 | -44.46879 | 2025-10-15 04:06:00 | NOAA-20 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 96ed2f5c-6d28-3f83-8ec1-286c6f7bd338 | -6.58244 | -42.969 | 2025-10-15 04:06:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e7350f75-7762-3aeb-b69d-aba2ddbc9f0a | -6.45752 | -44.59092 | 2025-10-15 04:06:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| c8decaa1-e8f6-369e-b065-8f19d448533f | -5.39552 | -43.57273 | 2025-10-15 04:06:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f9e3eca7-f44e-3494-a5c0-13706783dbbd | -5.85669 | -43.86042 | 2025-10-15 04:06:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f39f0104-12b8-32d9-919d-9ec8b4bb00c0 | -7.85549 | -43.79981 | 2025-10-15 04:06:00 | NOAA-20 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 6f088434-c7f2-3758-ad5c-2c46ddb4b8a9 | -6.39307 | -41.48636 | 2025-10-15 04:06:00 | NOAA-20 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 19abe34e-24d8-3241-9d36-cd42b39c8f29 | -5.62176 | -42.7276 | 2025-10-15 04:06:00 | NOAA-20 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| fcee707d-3d1a-3464-a421-b57d70d19c76 | -5.99728 | -44.08634 | 2025-10-15 04:06:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 3d02a797-0c40-34f3-bd54-f5ceeb89f23f | -2.86077 | -49.17072 | 2025-10-15 04:06:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 36b54f2e-101f-3dec-be5f-9a85b53f1170 | -7.16277 | -42.50284 | 2025-10-15 04:06:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 41134d17-ec05-3523-b4ab-55454d1f70b2 | -8.22354 | -44.0809 | 2025-10-15 04:06:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 475643be-147b-3be8-9a72-3e25a974d918 | -5.95341 | -42.30598 | 2025-10-15 04:06:00 | NOAA-20 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| e9722a41-0d12-3c68-a8a4-fd3ab89e6a22 | -5.76647 | -47.90857 | 2025-10-15 04:06:00 | NOAA-20 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b5d4b37c-50d6-36a0-b7b2-265d5fcba014 | -5.57029 | -41.32048 | 2025-10-15 04:06:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 0fa3da33-fc2a-3683-833d-0667f9860af8 | -8.12272 | -41.85065 | 2025-10-15 04:06:00 | NOAA-20 | CAMPO ALEGRE DO FIDALGO | PIAUÍ | Brasil | 2202117 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 11f1c0f9-7225-3289-8091-bd065198a6b7 | -6.48476 | -42.06628 | 2025-10-15 04:06:00 | NOAA-20 | BARRA D'ALCÂNTARA | PIAUÍ | Brasil | 2201176 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 51ca6223-0eab-3ec8-9886-6d805bd772a2 | -5.18967 | -46.17279 | 2025-10-15 04:06:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9e3da524-de88-33b4-ade2-4c6286d7421b | -6.14954 | -41.7386 | 2025-10-15 04:06:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 21c0ff98-28f7-3e98-8e42-97954c653f6b | -5.3144 | -42.89655 | 2025-10-15 04:06:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 1.3 |
| d5d33c30-e8d7-30b0-a905-876a2f904ce9 | -4.66042 | -43.12398 | 2025-10-15 04:06:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 35.2 |
| 42c838b5-0a8b-3125-ba9c-768473c20286 | -4.01652 | -48.97141 | 2025-10-15 04:06:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0d5773f8-cdb4-3b5a-befb-3c26126588f4 | -8.18184 | -44.03079 | 2025-10-15 04:06:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 732ab86d-8c4c-30a9-921f-15d607c9f219 | -8.21815 | -44.04832 | 2025-10-15 04:06:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6956b693-9f62-32b9-9d18-27d381e09fbd | -5.96249 | -42.24942 | 2025-10-15 04:06:00 | NOAA-20 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 89f0e540-4313-33e6-8b7e-c353fb7176ec | -5.30248 | -42.5323 | 2025-10-15 04:06:00 | NOAA-20 | PAU D'ARCO DO PIAUÍ | PIAUÍ | Brasil | 2207793 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| dda62973-ceef-3649-a74b-53804823c303 | -7.09012 | -41.95596 | 2025-10-15 04:06:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 3618e741-4934-3cd0-a392-99cd23ba1f1d | -5.93717 | -42.26365 | 2025-10-15 04:06:00 | NOAA-20 | SÃO MIGUEL DA BAIXA GRANDE | PIAUÍ | Brasil | 2210383 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 5e70d411-96aa-370e-8156-0d97b00e4e2a | -6.23159 | -41.56352 | 2025-10-15 04:06:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| d79a0faa-7250-3b9d-906f-7328aaff71ba | -6.05171 | -41.90445 | 2025-10-15 04:06:00 | NOAA-20 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 64a33e6e-f56f-352d-8f83-c908e7842032 | -5.95324 | -38.63187 | 2025-10-15 04:06:00 | NOAA-20 | JAGUARIBE | CEARÁ | Brasil | 2306900 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| fef66db4-b6a4-385c-a212-b2730a46de1a | -6.89395 | -43.96853 | 2025-10-15 04:06:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e639d66d-1538-30e4-907c-1e01ca88d8a4 | -6.33452 | -44.01901 | 2025-10-15 04:06:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| d315b4b6-a1e1-3c97-ae73-f748646d1fbd | -4.73322 | -45.78374 | 2025-10-15 04:06:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e7a31380-f108-3717-ab45-30bc7dd00651 | -5.1856 | -46.17219 | 2025-10-15 04:06:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| aba3048a-2546-3742-a3db-d9489e3411de | -4.94386 | -41.71424 | 2025-10-15 04:06:00 | NOAA-20 | SIGEFREDO PACHECO | PIAUÍ | Brasil | 2210656 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| a111a04c-eb39-3d11-9be4-34c547c9faaf | -4.86794 | -45.67667 | 2025-10-15 04:06:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 95a3d0e9-8546-3ffc-95b3-f9de6925443b | -4.41577 | -40.17299 | 2025-10-15 04:06:00 | NOAA-20 | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 9b8d584d-a951-3542-bdca-9c6ff5e96ff6 | -8.251 | -43.34718 | 2025-10-15 04:06:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 75053c54-ecad-353c-92fc-6ef1db1e9351 | -5.54241 | -41.32276 | 2025-10-15 04:06:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| f72a1354-fc13-3c1b-8308-1842d8cb470f | -5.41886 | -44.22926 | 2025-10-15 04:06:00 | NOAA-20 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 89b64cd4-74e7-3853-991e-47ee33c73fe6 | -5.41594 | -44.22454 | 2025-10-15 04:06:00 | NOAA-20 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d3b5db4e-f553-3db4-98c0-f0b3dcbbd35b | -8.4581 | -46.16637 | 2025-10-15 04:06:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| be3c8abb-de4c-3ee1-b928-23b95c6972e7 | -3.7354 | -44.14124 | 2025-10-15 04:06:00 | NOAA-20 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7ae281e0-2008-3ae2-9422-a13ebf105356 | -3.72512 | -44.13511 | 2025-10-15 04:06:00 | NOAA-20 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bc1c4c88-6d49-3c2e-b630-6cd3b8651ef7 | -6.14457 | -41.74847 | 2025-10-15 04:06:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 3baaecf6-7278-3eac-abed-898285251be5 | -4.81489 | -43.21445 | 2025-10-15 04:06:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a71688d1-ea9f-3af7-a7db-1501cb80de27 | -7.16836 | -42.19031 | 2025-10-15 04:06:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| d851aeff-f070-37ce-8abf-f2ac0d5bf2e1 | -6.22568 | -42.66351 | 2025-10-15 04:06:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 0981dc25-deb2-3b18-b52b-d15fbd3179e0 | -4.91243 | -46.70485 | 2025-10-15 04:06:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f43a98f6-1b0d-3193-829e-b434ce4c47a1 | -5.16844 | -46.27753 | 2025-10-15 04:06:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b18d64cc-8406-31af-afe3-02daaccde0aa | -9.47066 | -46.07128 | 2025-10-15 04:06:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 31cbe49a-376d-33af-ba37-5fdff5376ad1 | -7.89857 | -43.91955 | 2025-10-15 04:06:00 | NOAA-20 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e5040f10-7425-3b30-a166-c69d760938f1 | -4.81771 | -43.21062 | 2025-10-15 04:06:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1013014b-d54c-32ac-ab41-295d474fafef | -4.59357 | -47.03605 | 2025-10-15 04:06:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| aee53e0e-5cef-325f-86b7-79c7bb2e7387 | -7.26864 | -39.27478 | 2025-10-15 04:06:00 | NOAA-20 | BARBALHA | CEARÁ | Brasil | 2301901 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| a8d91ad1-ad90-396d-9932-fa468243bc4d | -5.38271 | -43.23216 | 2025-10-15 04:06:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f79bc444-283d-3249-ba68-1d5ccefa0d18 | -4.948 | -41.7077 | 2025-10-15 04:06:00 | NOAA-20 | SIGEFREDO PACHECO | PIAUÍ | Brasil | 2210656 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 7eb8c348-260d-332f-8b23-8c839499667d | -6.23194 | -44.15956 | 2025-10-15 04:06:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| eef449d6-bca4-315d-83be-e52a010b61b7 | -7.15896 | -42.18523 | 2025-10-15 04:06:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 8fbacc24-a2cb-3446-a2ad-0a7bc3d3a78b | -5.42383 | -44.22157 | 2025-10-15 04:06:00 | NOAA-20 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 19.4 |
| 0cbce194-b985-34c0-8b5d-a07219adba0d | -8.2538 | -43.35138 | 2025-10-15 04:06:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 5446501e-1961-3602-930b-4ee7151317e7 | -6.89045 | -43.96794 | 2025-10-15 04:06:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1afd8caf-014e-3f19-b002-bead00445ffa | -7.07913 | -41.96132 | 2025-10-15 04:06:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| e24e41e6-668c-3e7a-b159-9b8951a2e13c | -4.75909 | -40.86406 | 2025-10-15 04:06:00 | NOAA-20 | ARARENDÁ | CEARÁ | Brasil | 2301257 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| d99767b7-91b9-31d4-b032-c312f2e81087 | -2.94644 | -49.34176 | 2025-10-15 04:06:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ea364ccd-8529-39f6-b147-9695c99cb3df | -3.732 | -48.35989 | 2025-10-15 04:06:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4f4a7d3e-9b05-3558-8d02-7c65e7add61a | -7.48451 | -42.14744 | 2025-10-15 04:06:00 | NOAA-20 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 25289250-01b4-36aa-9698-5e906df5e022 | -7.16616 | -42.18279 | 2025-10-15 04:06:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 15be5148-a72d-367b-a717-4d29f7cac39c | -7.1656 | -42.18629 | 2025-10-15 04:06:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| a81fff29-7ed7-32f4-878e-042065e516e4 | -7.54026 | -42.69028 | 2025-10-15 04:06:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| c526f9ad-391f-3494-a847-9d9d55bec415 | -6.54942 | -43.92553 | 2025-10-15 04:06:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 6db95491-a982-3f29-8744-6d2cb3717bfe | -5.86245 | -43.86952 | 2025-10-15 04:06:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 42922495-536c-39b5-bfd6-e3b2daee9229 | -7.4882 | -42.14445 | 2025-10-15 04:06:00 | NOAA-20 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| c91c5d62-57b9-32f6-a157-c79a3d2bdcac | -5.86852 | -43.85434 | 2025-10-15 04:06:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 3e3bf9d5-2d33-3c2e-9ed8-a8bb7298072d | -5.91881 | -42.8223 | 2025-10-15 04:06:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| c886f1ba-e8f5-3a53-8846-9ab899af7904 | -6.05669 | -41.89453 | 2025-10-15 04:06:00 | NOAA-20 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| c67c1e63-32dc-3cec-8788-86c7a75c2272 | -7.29941 | -41.96473 | 2025-10-15 04:06:00 | NOAA-20 | WALL FERRAZ | PIAUÍ | Brasil | 2211704 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 0167d5d9-8814-3824-a117-4d57591aad63 | -5.03547 | -44.73677 | 2025-10-15 04:06:00 | NOAA-20 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9bd7c152-4b19-37dc-bb60-3ff502d414e3 | -5.43826 | -38.26604 | 2025-10-15 04:06:00 | NOAA-20 | ALTO SANTO | CEARÁ | Brasil | 2300705 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 7baf8bda-bb50-3740-a78b-fcf21fa2da5f | -6.21891 | -41.55796 | 2025-10-15 04:06:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| ba51a4d3-e070-30f5-ae78-78dc88a963da | -5.42744 | -44.22215 | 2025-10-15 04:06:00 | NOAA-20 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 19.4 |
| 447e08ec-03dc-330c-8498-29622605b211 | -8.27311 | -43.41023 | 2025-10-15 04:06:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| ed8feae1-b9a6-337a-9ac2-510a77f170a2 | -4.41632 | -40.16951 | 2025-10-15 04:06:00 | NOAA-20 | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| dc14e663-b6b5-3194-bc13-a16f31b4a212 | -5.03247 | -44.73181 | 2025-10-15 04:06:00 | NOAA-20 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 96453c0a-3537-39b2-81d5-23e4e50c9c81 | -6.16841 | -44.30046 | 2025-10-15 04:06:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6e8b80d3-f041-3a66-8860-6cd9117bf4cd | -5.04412 | -43.26504 | 2025-10-15 04:06:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 86a5553c-ea89-31b2-989f-0a7805bd7025 | -5.39105 | -41.16456 | 2025-10-15 04:06:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 8c16c01d-e15a-34e6-8095-5779865443cb | -4.35732 | -46.78107 | 2025-10-15 04:06:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 159ff31d-f75d-3c30-b3c5-85eb0699899d | -7.74526 | -42.45142 | 2025-10-15 04:06:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 6c411984-95ce-3148-9037-a5dcbfd0c1c0 | -5.23071 | -46.22801 | 2025-10-15 04:06:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README26.md)
