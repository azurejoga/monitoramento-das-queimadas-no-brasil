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

## Dados Diários - Página 38

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| debb7e1b-2c35-33bf-aecc-9cb85e2ef50d | -8.7996 | -48.4814 | 2026-08-30 04:32:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 90a859a5-718b-307e-b5c8-1ac9fd7b8ba4 | -7.94434 | -44.26044 | 2026-08-30 04:32:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 54f77dac-7e08-3328-8534-edd0adb21ce2 | -6.24718 | -55.43605 | 2026-08-30 04:32:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ac5731cf-6cc0-35e6-a4dd-0af717a8ef64 | -6.78729 | -55.67321 | 2026-08-30 04:32:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9959436e-c6a3-3c70-80cf-45b835ee5706 | -5.60616 | -44.12711 | 2026-08-30 04:32:00 | NOAA-20 | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 93ca561a-0f18-3fb6-a3b5-ed628d919994 | -7.00754 | -59.65482 | 2026-08-30 04:32:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 270b80c1-546d-32de-8125-60584423ce9d | -6.24774 | -55.43282 | 2026-08-30 04:32:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0ab85ddb-f98b-33b4-a562-0ee26e39ab2f | -7.12716 | -48.06366 | 2026-08-30 04:32:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a117e794-c1fa-33f7-bf80-71ad865c34cd | -5.88588 | -47.73316 | 2026-08-30 04:32:00 | NOAA-20 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 197fcf2e-c7f4-3c93-be8b-813e7fa95995 | -8.1423 | -45.47526 | 2026-08-30 04:32:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e8007034-8bb7-3a9d-8605-42e18684418b | -5.87371 | -57.77337 | 2026-08-30 04:32:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7a11ed0c-e9d7-335f-82d2-32f91f7406d4 | -7.5 | -55.31622 | 2026-08-30 04:32:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 164cbabb-543d-314c-b463-97e657c523da | -7.29358 | -49.95425 | 2026-08-30 04:32:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0ebdbae7-cc78-342d-8533-3d3fc47da601 | -8.20654 | -44.81373 | 2026-08-30 04:32:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4c45a215-c6c7-3ce9-b534-1d72dab6406a | -3.48636 | -54.65834 | 2026-08-30 04:32:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7f5958d1-301c-3bbf-8e6d-1b60cdb15091 | -7.52498 | -55.59342 | 2026-08-30 04:32:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6c4d3e34-cfbf-3494-b652-04efcaa21ac1 | -7.40707 | -44.25044 | 2026-08-30 04:32:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7d382e96-ceb6-3bd6-a59d-ed66cffc8390 | -2.93654 | -41.73418 | 2026-08-30 04:32:00 | NOAA-20 | PARNAÍBA | PIAUÍ | Brasil | 2207702 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 7a2672bf-48ee-30e8-80bd-8437b9cfb65f | -5.88072 | -57.76973 | 2026-08-30 04:32:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ccae8a07-9556-3553-ad61-1ac5fa5bc1c4 | -4.92581 | -55.768 | 2026-08-30 04:32:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d7691b45-5e9c-3b60-b0b0-f577ba88d520 | -7.18103 | -43.71852 | 2026-08-30 04:32:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d07accf3-e24a-3e0f-a83f-ae64e49a606d | -7.10259 | -42.21783 | 2026-08-30 04:32:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 81075439-c563-3538-9c15-cd9592f76153 | -7.04662 | -42.19442 | 2026-08-30 04:32:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 29aba198-2d8b-31ea-8e9f-041532596994 | -7.61145 | -44.85909 | 2026-08-30 04:32:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 9edd4efe-ee30-38a3-8fc5-36f2d718f7f4 | -5.50443 | -44.62395 | 2026-08-30 04:32:00 | NOAA-20 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0fef6fad-2be7-3eb0-b0fb-367b698ea3f3 | -7.10701 | -42.18857 | 2026-08-30 04:32:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 1702bd6d-7511-38ba-a8c6-a13d27e4775c | -6.77018 | -55.64706 | 2026-08-30 04:32:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b98d08e4-2494-35b6-a98f-d15a3e9f70c5 | -6.31978 | -54.74842 | 2026-08-30 04:32:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 63acd7ea-cf6a-3914-a28c-785367798a1a | -7.3773 | -45.08372 | 2026-08-30 04:32:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 476a125b-2ae3-3ac5-8f54-6ad7e12d2554 | -2.91285 | -54.11954 | 2026-08-30 04:32:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 32f0351e-c303-37de-b38d-6dd1458302ea | -7.12201 | -56.55467 | 2026-08-30 04:32:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 346e5293-d0e7-3eb5-aa37-f47195afbfa4 | -5.85638 | -57.55415 | 2026-08-30 04:32:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| e1e7d9d2-2e6a-344d-a7e2-bd6520db29da | -6.00051 | -45.07993 | 2026-08-30 04:32:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 2ecdfda6-7990-358b-a21e-060554483130 | -2.9361 | -51.48071 | 2026-08-30 04:32:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ee6e7eab-4034-35ef-a9f9-d75edd53bfe4 | -6.43414 | -41.54831 | 2026-08-30 04:32:00 | NOAA-20 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 39109ceb-59c0-3b79-a9d4-9d4ca6051b76 | -7.94315 | -44.26828 | 2026-08-30 04:32:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 93ef447a-6033-3155-a69f-b925930f0249 | -5.87735 | -57.78824 | 2026-08-30 04:32:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 083a2778-e8c1-3e89-90a8-7d526818d132 | -5.48575 | -57.15572 | 2026-08-30 04:32:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 18461ef3-c602-3c5d-8162-72c77bb6fb0c | -6.70821 | -50.94527 | 2026-08-30 04:32:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f1c1d201-841e-3de1-aa47-3791d1aa56ce | -8.15362 | -45.50272 | 2026-08-30 04:32:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 95807abf-4ec0-3b67-b0ed-d4112ef15d66 | -4.9203 | -55.76711 | 2026-08-30 04:32:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 3a061bf4-3150-38d3-8732-eda28fe215ec | -7.48677 | -45.38924 | 2026-08-30 04:32:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 93e3e80f-f9e4-3950-b828-3e2c36c308a8 | -2.95281 | -43.25401 | 2026-08-30 04:32:00 | NOAA-20 | PRIMEIRA CRUZ | MARANHÃO | Brasil | 2109403 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a7e44b55-9885-3063-b6cd-3bd945e0fe52 | -6.78258 | -55.66901 | 2026-08-30 04:32:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e7fefada-9ab2-3c88-8e8e-4536a8734172 | -4.35622 | -55.02467 | 2026-08-30 04:32:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cb6c3fd2-44a5-3d8c-a82e-3abdd3d9039c | -6.77956 | -55.68574 | 2026-08-30 04:32:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2e247bd2-3ee1-3bf2-8774-60e63f5379c9 | -5.87199 | -57.78276 | 2026-08-30 04:32:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 0a14276f-36b1-3e98-b463-45ae5f171ae7 | -8.13893 | -45.47474 | 2026-08-30 04:32:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7983db5d-cbec-31e9-b3cb-0e15b1ed065a | -7.60945 | -45.8409 | 2026-08-30 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f5dc0bf1-63bf-3738-a35a-f1439292c622 | -2.02978 | -48.78115 | 2026-08-30 04:32:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| f1a7f0bd-9c94-3ef2-9f24-3db84fb27465 | -6.63943 | -53.18006 | 2026-08-30 04:32:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 50018134-f3fb-3814-94a4-a51be00e9a93 | -5.86055 | -47.08406 | 2026-08-30 04:32:00 | NOAA-20 | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e59875c3-1279-3afe-94e1-409ef2812a7e | -5.6102 | -44.12391 | 2026-08-30 04:32:00 | NOAA-20 | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 949e5c50-923e-3382-8ab5-579c919454b7 | -6.15517 | -57.78654 | 2026-08-30 04:32:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 3385814b-cff7-3194-a972-20b8c44b15e8 | -6.49381 | -53.26373 | 2026-08-30 04:32:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 812ddd47-5331-333d-8e3c-f56c365be8e2 | -7.31069 | -43.01431 | 2026-08-30 04:32:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 7a621def-7198-3982-b038-ddb2f0ae4927 | -7.60145 | -46.19527 | 2026-08-30 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7f43bde9-00d5-3ece-8e13-12af2b6d7d60 | -5.97112 | -57.6889 | 2026-08-30 04:32:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 2378058b-806e-36f0-bc9a-62fa9bce04e3 | -3.49111 | -54.66283 | 2026-08-30 04:32:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6bf0e5f3-2399-34e8-b8ab-856e3d7cd0a9 | -4.2826 | -48.19374 | 2026-08-30 04:32:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 163b1ab9-e90d-3f2d-99b8-e951949083ee | -7.13038 | -44.31544 | 2026-08-30 04:32:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 93f0c4d9-da3c-3868-a864-df5b5e1bfcc1 | -6.06493 | -44.87606 | 2026-08-30 04:32:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f44370bc-d643-37aa-9e02-a8e09d4b9c4a | -6.18313 | -44.58377 | 2026-08-30 04:32:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b2ab1bb7-d7e5-3982-a389-f659890b16a8 | -6.90794 | -59.49337 | 2026-08-30 04:32:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 78e9f557-7b70-3898-b7a3-e962f60d553e | -4.46823 | -49.70437 | 2026-08-30 04:32:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cee61cb8-9ca2-3366-8e14-8171ca58f795 | -6.86291 | -41.68233 | 2026-08-30 04:32:00 | NOAA-20 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 13.7 |
| 8f885258-c850-30a5-8bf2-94e4be3340c4 | -2.53919 | -48.24397 | 2026-08-30 04:32:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a2587f6f-881b-30d2-9d32-173ff1ad72c5 | -2.93547 | -51.48468 | 2026-08-30 04:32:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e05c933e-beaa-3eb5-a54b-6a4ffd7442df | -4.92586 | -55.76853 | 2026-08-30 04:32:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 109b9875-9bdb-3c33-ad52-a5a3f7c9635a | -6.76781 | -55.66013 | 2026-08-30 04:32:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ee18f123-db1e-3225-a15b-2b969fb933fb | -6.67829 | -58.74689 | 2026-08-30 04:32:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f1cbf890-ea1c-3714-8d95-aa1e01e95e4a | -6.87058 | -42.88353 | 2026-08-30 04:32:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 3308f5e6-4655-3a76-b24a-2f1fb2274e3d | -4.08151 | -45.94362 | 2026-08-30 04:32:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 02ed4eea-723e-3707-b0d5-8f7a3d273ac7 | -7.52147 | -55.31409 | 2026-08-30 04:32:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 707eda86-9140-342b-8515-80b86e6ab089 | -7.94374 | -44.26435 | 2026-08-30 04:32:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 4bec357b-ce90-34c9-a26d-9e19780f0841 | -7.53183 | -44.44659 | 2026-08-30 04:32:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e3c7d3f7-d3ff-3415-adb2-f97a8a020098 | -3.76783 | -59.34008 | 2026-08-30 04:32:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 06220a48-d4d2-333b-9fde-a1e3b54377df | -4.96413 | -55.84161 | 2026-08-30 04:32:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| c4482047-2afd-3299-a9a8-21abde534bbb | -5.04188 | -44.69352 | 2026-08-30 04:32:00 | NOAA-20 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d20ff0d9-a9fc-3d4c-a1cf-b347f3985f89 | -7.23563 | -43.11088 | 2026-08-30 04:32:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 64567db3-4a2b-3449-bf7d-9c42662d498c | -3.49157 | -54.65935 | 2026-08-30 04:32:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c2caae93-3266-32d3-a036-737a119d2b90 | -5.97111 | -57.68933 | 2026-08-30 04:32:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e79ed5e6-1cbe-3ed2-bd4a-058df4fb38f5 | -6.93184 | -55.7134 | 2026-08-30 04:32:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1428d30f-239f-3412-ad8a-ed6290e5e2c3 | -6.76561 | -55.64946 | 2026-08-30 04:32:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e8e9adb7-1716-33d8-ae30-48205b61aa0f | -5.61423 | -44.12069 | 2026-08-30 04:32:00 | NOAA-20 | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2cc0a080-9e97-3c62-83d6-520d6e006dad | -6.86896 | -41.66932 | 2026-08-30 04:32:00 | NOAA-20 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 59b43066-0c99-39e8-82ff-b251c6cd6776 | -6.87404 | -56.57527 | 2026-08-30 04:32:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7012a572-802c-3123-96a2-5283165b7dcc | -6.41991 | -55.5266 | 2026-08-30 04:32:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| caf5f3ae-b239-33a3-b065-2b667feb8684 | -5.63868 | -44.97997 | 2026-08-30 04:32:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bed3cb5c-7feb-33fb-8b8a-02df975f523e | -5.36676 | -50.56803 | 2026-08-30 04:32:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 391412e0-2ad9-3185-b1d6-5bcd2de9bf3c | -7.79657 | -43.90055 | 2026-08-30 04:32:00 | NOAA-20 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 89894202-2234-3c63-825f-578367bac3d1 | -6.85994 | -41.67488 | 2026-08-30 04:32:00 | NOAA-20 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| a127eaca-b511-3f63-801b-84cfcbc1a0d8 | -6.4991 | -53.25995 | 2026-08-30 04:32:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 48acde9e-596e-3d6b-8467-335db8fc3585 | -5.71518 | -52.28626 | 2026-08-30 04:32:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cfd6f82d-c966-3e6e-9b43-babb246adec7 | -5.46005 | -48.91068 | 2026-08-30 04:32:00 | NOAA-20 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| aed14e16-4cfa-35db-9c5c-6290ca21cdd1 | -6.90465 | -43.65348 | 2026-08-30 04:32:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 35086686-9b9a-34c3-82c6-e9e4625667af | -6.40534 | -51.66876 | 2026-08-30 04:32:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ef86c20c-7c45-3258-8735-f6aae9b74c1d | -6.61111 | -55.4521 | 2026-08-30 04:32:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4f0d7d1b-a3c5-3208-aefa-c002377be981 | -7.04977 | -42.19991 | 2026-08-30 04:32:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 31bc8b0d-b880-31f6-95a8-23d7eec39cea | -5.77286 | -44.20176 | 2026-08-30 04:32:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |


[Clique aqui para ver as próximas entradas](README39.md)
