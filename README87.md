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

## Dados Diários - Página 87

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 67447f46-aa2c-32fa-86dc-e14783f111e4 | -6.00407 | -40.97191 | 2026-10-09 04:25:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 5c4c0f7d-1676-34f5-b350-c6fbf069f62d | -3.00428 | -53.89265 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 243bb4f9-93a2-3c7c-9b2f-629ddca837f6 | -3.94666 | -59.80022 | 2026-10-09 04:25:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 38643482-c069-3494-9f19-62b29808f07b | -2.88541 | -54.18299 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 6ca62ece-ab66-3d42-9cbf-213b633416ee | -6.15097 | -47.91742 | 2026-10-09 04:25:00 | NOAA-21 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 23c5c786-1c7e-3145-b4cf-a3092ce95cd3 | -6.16834 | -44.86081 | 2026-10-09 04:25:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ade555a0-aacc-3149-a02b-96bf112833f1 | -3.55378 | -54.68823 | 2026-10-09 04:25:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| a3a26685-6312-3f16-b1ea-c6c1e3c1f20c | -3.10938 | -51.03067 | 2026-10-09 04:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fb5f133a-2a35-3ae9-991a-01e81f07bd25 | -3.11056 | -54.18921 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6305d1fb-1c60-368a-931d-0166b305bc9f | -5.71438 | -53.49765 | 2026-10-09 04:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 0156ed97-ccbe-3cb1-a6e2-27b08f227939 | -3.50218 | -59.27137 | 2026-10-09 04:25:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5500e4a5-0d7c-37d9-a383-558f5e35ee8d | -3.2956 | -53.99825 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 29b2df4b-80af-32c6-ac48-03fc4791c33b | -6.87896 | -45.9011 | 2026-10-09 04:25:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 6ad71211-68a7-303e-84d5-44206b64f069 | -3.72846 | -53.69398 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 7304b846-cd64-37c7-ab9d-6dfe9c583c58 | -5.71033 | -53.48526 | 2026-10-09 04:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| bd9bd54b-fa86-3f16-9d15-4c23985215f0 | -6.15154 | -47.91382 | 2026-10-09 04:25:00 | NOAA-21 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b1ec158b-241a-3d04-91d7-02c8efef9e40 | -3.08331 | -53.94369 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 47eed270-c941-3470-a181-8aa2adf944c4 | -6.45566 | -46.01973 | 2026-10-09 04:25:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4559abf6-33e3-3cd3-aac7-82fd954bd696 | -3.54372 | -54.68048 | 2026-10-09 04:25:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7df5697e-04be-3422-a2d5-ede94f23b9d8 | -1.47569 | -54.63924 | 2026-10-09 04:25:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 63d8e90e-f50a-37cc-a4f2-b7929861bfa6 | -2.98949 | -54.07817 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b35f8b96-1120-3156-8d20-1678a7a08185 | -1.8948 | -54.67696 | 2026-10-09 04:25:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 47392f3f-d4a2-3fa0-8887-f56309135217 | -3.08099 | -54.29334 | 2026-10-09 04:25:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0332534a-0f7c-368e-8d5f-7626325ea737 | -3.89985 | -58.95667 | 2026-10-09 04:25:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 1095bcdf-f165-3d1c-b728-2d6bc506e0b4 | -6.4595 | -46.01679 | 2026-10-09 04:25:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 072cd96e-476d-316a-ac4e-dd504be6cd76 | -3.56531 | -54.68353 | 2026-10-09 04:25:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 3f0e8aec-b24a-38dc-942e-7147cd15450f | -5.51995 | -42.8262 | 2026-10-09 04:25:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 0e2d939f-1a51-3a91-acb4-edcfe41dfe38 | -6.15491 | -47.91435 | 2026-10-09 04:25:00 | NOAA-21 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d044d8f1-05b5-30ce-8667-fdf37ac683f4 | -6.5167 | -47.39042 | 2026-10-09 04:25:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| e9f72625-cb58-329d-abf7-69a216a72c64 | -4.52982 | -48.0603 | 2026-10-09 04:25:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| afbe1605-15a7-3576-914e-edb9975dd2fe | -3.04123 | -54.26161 | 2026-10-09 04:25:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 76d193c1-1b21-3c83-b2a3-d08fba0844df | -6.59017 | -41.54517 | 2026-10-09 04:25:00 | NOAA-21 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| da52f2f0-1575-3e48-b55b-66754a485e45 | -3.56192 | -54.66748 | 2026-10-09 04:25:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 479bd4c6-f54f-30d5-a11c-8f9cbfa5be43 | -3.08458 | -54.30322 | 2026-10-09 04:25:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| c8c762d9-6074-3a01-8cc9-42c137550562 | -0.99876 | -47.65313 | 2026-10-09 04:25:00 | NOAA-21 | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 14012634-1d21-3fa1-8c14-8243b99476b9 | -2.88088 | -54.19867 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a249c1e1-e558-3007-8485-e66e3a450846 | -4.83676 | -45.79748 | 2026-10-09 04:25:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fc9cdc25-f092-35e6-89bf-d7fddc72bcb5 | -3.30161 | -54.05536 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dea02896-e744-3404-83d5-99d345ccfcbe | -3.56382 | -54.66083 | 2026-10-09 04:25:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 935db700-de8d-3cfe-9eea-89ccd7731eb9 | -2.33824 | -48.86267 | 2026-10-09 04:25:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 922cc8ad-9d0e-3abc-a206-2889d654c4ae | -3.77238 | -58.58857 | 2026-10-09 04:25:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 6.8 |
| e7ebb672-042d-3af6-b885-8bc864672c05 | -3.07954 | -53.96655 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b6bdc240-54a0-386d-8066-a3cab2fb13e3 | -4.15675 | -55.14116 | 2026-10-09 04:25:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e601337d-a115-39ad-b68c-71005bb99d57 | -5.41877 | -44.6246 | 2026-10-09 04:25:00 | NOAA-21 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| efbf1def-0ce7-31c6-9605-1c2c93f25ac3 | -3.57264 | -54.67191 | 2026-10-09 04:25:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c05ff19b-b8e6-3df2-a6e6-cacc3c3d6eef | -5.1044 | -46.21966 | 2026-10-09 04:25:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 98620f79-945e-3e43-9f38-3542756ffa3f | -3.9039 | -55.89782 | 2026-10-09 04:25:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| e9e9f6de-3b8f-3e12-8596-98f7d4042723 | -3.2252 | -54.29667 | 2026-10-09 04:25:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| a2afc40c-0112-3f25-885d-6bae3f4cd4af | -3.07881 | -54.28873 | 2026-10-09 04:25:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2082fa35-5ab4-3bbb-a4e3-db6a63e8a8fd | -2.49337 | -56.16408 | 2026-10-09 04:25:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 4f057645-0692-3711-96bd-7e04d995dd29 | -3.94777 | -49.00938 | 2026-10-09 04:25:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c6b580f8-6f68-30e3-a824-f42f9b20ff67 | -3.09749 | -59.19532 | 2026-10-09 04:25:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 60a44a54-46e2-3fa1-98b2-7ef00b842f53 | -5.10824 | -46.21674 | 2026-10-09 04:25:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 181324af-3ef0-330e-b967-b0ab19ecf3e6 | -6.92204 | -44.56391 | 2026-10-09 04:25:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b71f2c4f-dcbb-32d0-b3b2-4e4032d66553 | -5.98445 | -41.35818 | 2026-10-09 04:25:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 012e3585-61cd-3c62-86ad-853fc7b122b2 | -4.74839 | -55.66045 | 2026-10-09 04:25:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 57668d7d-5cb0-376b-9a53-9ebc56cd00ab | -3.25939 | -50.40501 | 2026-10-09 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 64c68a47-aa94-3e83-a7d3-de455dfc605d | -1.54173 | -52.75929 | 2026-10-09 04:25:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 18f6b568-4d43-3d36-8f2c-05a0788a3d82 | -5.70268 | -53.47436 | 2026-10-09 04:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 024e6e4d-138c-3ecc-a555-1c3eeccff0fa | -4.79677 | -56.14189 | 2026-10-09 04:25:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 6e8c6972-0726-3e78-a17f-8f6c394660c3 | -3.00627 | -54.76532 | 2026-10-09 04:25:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 86878001-4615-3ced-8430-4ffeb0829d56 | -3.24876 | -54.03233 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 711c23ea-f66d-3700-a426-946659bd4ca0 | -5.93345 | -49.70143 | 2026-10-09 04:25:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dd032002-887a-3179-b071-b4a4baadcf04 | -3.55901 | -54.689 | 2026-10-09 04:25:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 61f69582-873e-39e5-8731-28c4d2584391 | -3.72223 | -54.21842 | 2026-10-09 04:25:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 321a9197-5b16-3d2a-8395-a435b49f7f93 | -3.27825 | -53.81793 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b81aa222-30b0-342c-89d4-515aab363768 | -2.59418 | -47.35407 | 2026-10-09 04:25:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cfe76d18-3ec3-35f9-9dde-4572dee1c7ef | -2.20192 | -46.43415 | 2026-10-09 04:25:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 471df9a0-4f3d-3635-b07a-6426e7f8de3d | -4.28854 | -48.56149 | 2026-10-09 04:25:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 77ff8d23-085c-35c6-bfa1-f271b883600b | -3.50087 | -49.93544 | 2026-10-09 04:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 649e62be-6510-3cd0-9519-62b615ecd9d8 | -5.70881 | -53.49408 | 2026-10-09 04:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| c52c73bc-4fbe-3369-8b6a-5dac13619789 | -3.74977 | -59.48208 | 2026-10-09 04:25:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 27ed1e64-7352-3aee-be07-1b6793e1eb18 | -5.09727 | -46.22207 | 2026-10-09 04:25:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e8f66a5b-67d8-3494-851a-40f8df842067 | -3.89841 | -58.95534 | 2026-10-09 04:25:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| abfa473b-4657-31f7-bb61-926a242a534d | -3.26466 | -53.99895 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| dd293feb-4a7c-3523-a7b0-f9b4594fc6ee | -3.05035 | -51.22322 | 2026-10-09 04:25:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 01688d92-5f05-381a-a881-732c2c243d46 | -6.00625 | -40.95698 | 2026-10-09 04:25:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 10.2 |
| 76831415-e73a-31c4-af71-505dd73d07fb | -5.36614 | -43.19865 | 2026-10-09 04:25:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5299f165-8830-3b45-a0c2-2753ddc6411e | -4.0803 | -55.38121 | 2026-10-09 04:25:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5bda2a24-9cf7-30bd-9ca8-13a788aec8f5 | -3.49045 | -50.49514 | 2026-10-09 04:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c0b782b3-b67e-3c22-aa0d-f3591740061e | -3.11942 | -45.616 | 2026-10-09 04:25:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cdf422ad-7cd6-3e68-907c-fc267535b434 | -2.82489 | -51.28577 | 2026-10-09 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| cc45fb07-f4c2-3434-a781-33cccb42ec5c | -6.69004 | -41.76144 | 2026-10-09 04:25:00 | NOAA-21 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| f20e6710-9a23-33bc-98a7-052430577cf2 | -3.17845 | -54.60805 | 2026-10-09 04:25:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4e3acfaf-9a6b-3626-b75a-ff4e21ed6fd1 | -3.55847 | -54.69215 | 2026-10-09 04:25:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| b73065b8-6d4f-3e5d-a117-67f201b37ba1 | -3.85186 | -51.93404 | 2026-10-09 04:25:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dd088f92-26c9-39bb-9bf9-71d8ddf0b6a3 | -3.30006 | -53.69746 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b0d4c100-0286-3846-8773-0556928e6a15 | -5.70956 | -53.48971 | 2026-10-09 04:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 48ce459e-f41c-3dea-9c84-ce63ef7b6c80 | -2.33688 | -48.87106 | 2026-10-09 04:25:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e545ec97-eb6a-3a6c-ad51-07862dde8b33 | -5.61393 | -44.83903 | 2026-10-09 04:25:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4ebb6ee9-fa6d-351b-a4b2-c94c0dc67b43 | -2.56439 | -50.67844 | 2026-10-09 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 25837e88-cd67-3acd-b5ed-9e5983014227 | -1.5255 | -54.56831 | 2026-10-09 04:25:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 73166379-25f0-3bac-9af7-d9a7358487e7 | -0.67174 | -50.77063 | 2026-10-09 04:25:00 | NOAA-21 | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 82eb87f1-ef8e-33b2-b54d-a39d3429a86b | -1.77634 | -55.02192 | 2026-10-09 04:25:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 8e3cc3d7-7850-384d-861f-bd12d84e22b4 | -4.28954 | -54.80914 | 2026-10-09 04:25:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d8dee104-3d5a-3e21-9542-d0cf9db1150a | -4.40026 | -49.13165 | 2026-10-09 04:25:00 | NOAA-21 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 03ebe196-de2d-32d9-9016-1fc049274d29 | -6.37582 | -42.52343 | 2026-10-09 04:25:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 507a7e7b-2e22-32b2-ac71-89c04e86b6e9 | -2.75258 | -54.11118 | 2026-10-09 04:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 6b8def54-228e-3c46-a2d2-49b3e3b35bf4 | -2.77318 | -54.08065 | 2026-10-09 04:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 04523669-f4b7-3500-9dbc-809a60aae816 | -3.0233 | -54.05624 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README88.md)
