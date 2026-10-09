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

## Dados Diários - Página 88

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 54295f19-e745-3477-8be4-ba16a0cbfdd7 | -3.57084 | -54.48307 | 2026-10-09 04:25:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8510a63a-b3b8-3904-b866-fbe0141fdcc9 | -6.04481 | -44.03225 | 2026-10-09 04:25:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d1c5e119-b38d-3c35-82d1-025ecb764059 | -3.90762 | -55.89769 | 2026-10-09 04:25:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| cc616b7b-2970-3cf7-a5c0-dede0ffd9184 | -3.11259 | -53.76644 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| a5cee56c-4809-3e01-97ca-fba55886bb26 | -2.99311 | -54.08786 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e30e04a0-25f0-3141-883e-dccff5ab8209 | -2.34186 | -48.86323 | 2026-10-09 04:25:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0976f9e1-b018-3866-86d5-45a320c27d7f | -2.84888 | -54.11857 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9093a99a-d398-38af-913c-383140678466 | -3.17646 | -54.74953 | 2026-10-09 04:25:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b603243d-1f61-3602-94ef-8cb02cf16664 | -4.73118 | -55.66247 | 2026-10-09 04:25:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 55f3a1a4-52fc-3ab6-b09b-aa78e30eb945 | -3.25982 | -54.02786 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 153ef88e-930c-39be-a3fc-58d8382dd4c9 | -1.10834 | -54.17657 | 2026-10-09 04:25:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 1db32e65-4f30-3571-a972-d3d201f1f3d8 | -3.65597 | -54.52457 | 2026-10-09 04:25:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| eb5bf45a-d355-3304-870a-036c0a64dcdf | -4.74706 | -55.66822 | 2026-10-09 04:25:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| e00e955a-a339-3b4d-85e4-f2ab190e23bf | -6.55546 | -47.40362 | 2026-10-09 04:25:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e1bf5ce5-d94a-364e-95d2-fa213d5dc600 | -3.10925 | -53.942 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| fa33673c-2eca-3e2a-b414-40f52ba9bd9b | -2.84035 | -54.13868 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2655968e-e35e-30ab-9d16-95c3ebfd7f93 | -3.08977 | -53.93566 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f3542c40-3648-378e-8ec0-e00f442c0dc3 | -5.7113 | -53.45863 | 2026-10-09 04:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 68221ca8-0f87-3a56-82b3-75a4b0dda0dd | -3.56477 | -54.68665 | 2026-10-09 04:25:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 0f348bb9-b633-3ab2-bdbe-65b53a48d677 | -3.08175 | -54.27059 | 2026-10-09 04:25:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f29e4ced-a893-3124-a3e2-e6080e6e640e | -2.46857 | -56.06224 | 2026-10-09 04:25:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 51c096a6-7a30-3fe5-b9b4-67c0ddaa2bba | -3.10551 | -54.18821 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f29833b9-92a9-32ed-a408-d6dad622530d | -4.28414 | -49.08503 | 2026-10-09 04:25:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 7eda9954-823e-340e-854a-9589d73ce4b7 | -5.0927 | -56.19815 | 2026-10-09 04:25:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 937a0e98-ea7b-36b7-850e-7264b3b314c4 | -3.12115 | -54.17952 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 86bf3714-8d9b-35e1-a002-539ceddca89e | -2.82315 | -57.62206 | 2026-10-09 04:25:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 318ea6a1-17b2-3237-8ed4-f777b4bddd44 | -6.15434 | -47.91795 | 2026-10-09 04:25:00 | NOAA-21 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4e5cf195-5a09-3571-ac4a-77c91ca975f0 | -3.34615 | -50.41661 | 2026-10-09 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 59bb5947-753e-3cef-bdb1-6c954e80df1b | -6.88442 | -43.69353 | 2026-10-09 04:25:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d7b406ea-f00f-3f42-8080-325d10c330cc | -1.5344 | -54.53587 | 2026-10-09 04:25:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c260075a-bd7c-3b86-8faa-ed8e9303e729 | -3.01321 | -54.05459 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 033dcf2e-07be-3a3a-973d-85441f995bfb | -3.7896 | -59.37831 | 2026-10-09 04:25:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 5f5a945a-65d1-375d-a9fb-9e329c392e16 | -2.41022 | -56.53613 | 2026-10-09 04:25:00 | NOAA-21 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 06f1e5ac-d79c-339e-bb58-19113087186a | -2.9255 | -54.11958 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e8557030-f61a-3e38-8c67-907a2fddaefa | -5.34417 | -45.17921 | 2026-10-09 04:25:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| cd6b667c-4c41-3177-ab3e-9b2b42136781 | -1.60701 | -55.15939 | 2026-10-09 04:25:00 | NOAA-21 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e74476c9-0ff3-32b2-bf9e-c84a6dfd0bd8 | -1.5241 | -54.56492 | 2026-10-09 04:25:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c85f2349-4338-3c2c-9e9f-56025b1455d6 | -1.52962 | -54.53167 | 2026-10-09 04:25:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f7e0c5ab-7498-364b-83ca-fc9e4ff3e009 | -3.00833 | -53.89917 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 1ac74b5d-a5ae-3ace-a8d2-430635887c4c | -6.11875 | -44.81228 | 2026-10-09 04:25:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b60d888d-1721-3a05-83d8-88d21b42cb5b | -3.79727 | -50.04796 | 2026-10-09 04:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 035e31c9-0adf-3e1c-bc2d-234c76b0ada0 | -3.17105 | -50.45285 | 2026-10-09 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| aadd8153-fab1-3786-b104-0410874ddf0b | -3.01588 | -54.04313 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d6e03ed3-361c-3023-8907-7c21df4bd97a | -2.97357 | -54.11217 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7b231a1f-b0fe-31b3-81a6-9fcd1f699040 | -6.9575 | -45.27879 | 2026-10-09 04:25:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| fedbe398-9cec-3f0b-bd8f-ac04b8d09819 | -6.89105 | -45.88871 | 2026-10-09 04:25:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| c54d063b-bcfd-3532-ba48-e22f49722275 | -4.7961 | -56.14581 | 2026-10-09 04:25:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 0b83e083-d41e-3be9-8ab4-d140ef9b6881 | -1.42275 | -54.62563 | 2026-10-09 04:25:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c629db5e-9bc4-31e0-844f-fea40df880bf | -2.5466 | -57.99809 | 2026-10-09 04:25:00 | NOAA-21 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 769c0c0c-494b-31e9-8e54-83c03d53da65 | -3.1671 | -50.45512 | 2026-10-09 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 16b5922a-1ecb-3b19-bb67-a5757bd97312 | -2.08467 | -46.57349 | 2026-10-09 04:25:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c7cfc55b-0015-3b60-8d53-630735f62368 | -3.25314 | -50.39384 | 2026-10-09 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5afb6aa2-9015-3112-bff6-7283b73a1d40 | -3.27507 | -54.05997 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c07c661c-e08f-3bad-8cf6-6c3d06cd9995 | -3.23035 | -54.29726 | 2026-10-09 04:25:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9cb6ce99-727b-3678-9d36-5df1ac7fd9bd | -4.08749 | -44.15148 | 2026-10-09 04:25:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b152ba0f-a06c-3e97-a1ff-bcc807cc4fae | -4.65888 | -55.94842 | 2026-10-09 04:25:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| aa36e028-2b29-3d76-8496-ea0a9d0600ee | -3.17324 | -54.60714 | 2026-10-09 04:25:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bcf19467-3035-3eb6-baa5-ed16416390a0 | -3.16933 | -50.58711 | 2026-10-09 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 94ecad2d-78d7-30ed-8d11-d7812bc8079d | -4.46379 | -55.40018 | 2026-10-09 04:25:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 29d58ee5-7c9c-3a13-bb29-2987b136954d | -3.18633 | -50.58279 | 2026-10-09 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| ba8516a5-ba1b-3880-b0af-d2fd647d50d2 | -6.82328 | -39.55124 | 2026-10-09 04:25:00 | NOAA-21 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| b0c55e3e-f97c-34b7-80c0-7a198d8065b8 | -3.926 | -56.02766 | 2026-10-09 04:25:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| cc41f773-b34f-3320-b2f3-74d5476883fb | -3.08929 | -53.93858 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0cd403c7-b077-3f9b-9d4a-4186f5663e6b | -3.28877 | -49.51195 | 2026-10-09 04:25:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 8b4fb843-b91c-337b-9dd3-277d6c3fd65e | -3.97532 | -56.11674 | 2026-10-09 04:25:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0a411662-72bc-315d-9a7a-19b2c5ddad1c | -2.97987 | -54.07358 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b954ca47-ced6-3a2e-a687-3319a529ed9d | -4.63801 | -50.96169 | 2026-10-09 04:25:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| fe810056-ccbb-30d4-8ca0-a32d5f1fa61d | -4.6604 | -49.23469 | 2026-10-09 04:25:00 | NOAA-21 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7611f32d-3013-3ef4-a042-22f463b5df4e | -2.84085 | -54.13565 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| eab2cb51-2829-34bf-b3b4-2d8de19f4608 | -3.35224 | -50.47918 | 2026-10-09 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 358e7d5a-410c-3127-aa9f-cbb565949739 | -5.09835 | -46.2152 | 2026-10-09 04:25:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6760c3c3-5800-31cc-93d6-ce59b7e106db | -2.74094 | -54.1185 | 2026-10-09 04:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 04140ce7-4bbe-3963-a1b4-11452055f75b | -3.20308 | -53.87357 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0d6da466-88f6-3f45-bd95-999e7ce34e2e | -3.004 | -54.11687 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| f9b344a4-1ed6-3d9d-a97d-7eee64888d14 | -2.41094 | -56.53166 | 2026-10-09 04:25:00 | NOAA-21 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 39805f14-9447-32b6-91d7-d1a74fb6409a | -2.81687 | -58.29463 | 2026-10-09 04:25:00 | NOAA-21 | SILVES | AMAZONAS | Brasil | 1304005 | 13 | 33 | nan | nan | nan | Amazônia | 18.0 |
| 14d8ce8c-9cdf-36e7-90e9-d715884eb1bf | -3.0361 | -54.10362 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b6a65d09-c028-33ba-bb3a-73910cad2a44 | -2.88041 | -47.85266 | 2026-10-09 04:25:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 664d5419-a4b5-39e5-869a-e08e92dd38db | -4.12724 | -55.03291 | 2026-10-09 04:25:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4ddfb7a1-b006-312f-adbe-3ea2030908a0 | -3.91867 | -52.1342 | 2026-10-09 04:25:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 730fb8a9-5a1a-339b-8d06-e3b42c470d81 | -3.00227 | -54.09538 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cc9ee0eb-1789-3c24-b3e2-574d761281b6 | -1.21165 | -55.65012 | 2026-10-09 04:25:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 287e24c8-a494-39e5-8605-6a466ea29408 | -1.2486 | -46.371 | 2026-10-09 04:25:00 | NOAA-21 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c30cbb55-b567-37ba-bb5f-d5d9f0a755c9 | -5.996 | -40.94043 | 2026-10-09 04:25:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 13.3 |
| 41923356-ec8f-3b34-bb66-b36710d984da | -3.56611 | -54.67458 | 2026-10-09 04:25:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 67362d52-6ac9-30e7-ac2b-d9f8742a15d1 | -4.08324 | -48.95835 | 2026-10-09 04:25:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 107ad719-7064-312a-be55-5fbfbaab04d7 | -2.99523 | -53.85424 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9aa686fd-0938-3480-9125-9b249426e3b8 | -3.10239 | -53.95251 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 0fab317a-24be-32e8-8ebc-7905a58f7512 | -2.82436 | -51.28129 | 2026-10-09 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 04cfb741-778a-36b4-a4dc-e774f526dead | -5.34519 | -45.76798 | 2026-10-09 04:25:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9956a45e-8f22-335e-a1b3-b8b244c39274 | -3.89956 | -55.88914 | 2026-10-09 04:25:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 3fc8e96d-a6c2-3762-a906-bba4c85de68c | -3.56713 | -54.66832 | 2026-10-09 04:25:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 3eb0e91f-a1b0-38da-b18b-dc31f48fd624 | -2.22303 | -53.70116 | 2026-10-09 04:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5b792ebe-3b1e-381d-a76b-8321b9162949 | -5.88403 | -43.41324 | 2026-10-09 04:25:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 0257c072-e8de-389e-8a02-3c7797148369 | -7.23877 | -41.90672 | 2026-10-09 04:25:00 | NOAA-21 | WALL FERRAZ | PIAUÍ | Brasil | 2211704 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 89ff8a96-fa9f-3d5c-8a85-f346ee7cc4d7 | -2.88589 | -54.18 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d3fa3ffc-ee88-35dc-87d3-905e23b9163d | -2.5676 | -56.1831 | 2026-10-09 04:25:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bcf3b64e-75ef-3823-afba-20699eaf7c2c | -5.34751 | -45.17973 | 2026-10-09 04:25:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 01abe13c-4c2f-3b16-86d5-b8c681bf9f6c | -3.10335 | -53.94667 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| d1e7e34e-ae5f-37e2-897d-8a63b2e1ce22 | -3.36958 | -50.4716 | 2026-10-09 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |


[Clique aqui para ver as próximas entradas](README89.md)
