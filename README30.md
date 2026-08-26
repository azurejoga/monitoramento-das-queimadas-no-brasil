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
| ac9702cc-d42b-3376-a012-e22af47cb409 | -7.33351 | -46.95847 | 2026-08-26 04:51:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| af69ad4d-68e1-3ec5-90aa-bc672f6b8a05 | -4.56282 | -49.51967 | 2026-08-26 04:51:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 6dafd1e9-4dcd-39cb-a0e7-5c155e344975 | -6.70506 | -56.3429 | 2026-08-26 04:51:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ec40a960-1a22-34c6-8cad-3345de88ef2e | -7.75914 | -44.76504 | 2026-08-26 04:51:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 8fe0099f-55f8-3b4c-8011-d567ff49bd5b | -7.27236 | -44.07518 | 2026-08-26 04:51:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c100a9a4-809e-30f3-a24e-8aa49068ad1a | -6.98497 | -59.26331 | 2026-08-26 04:51:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 235e7a0c-f91d-3c1f-8565-d66d9bfdb4ca | -6.10374 | -53.40751 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 031f6890-423b-3767-acbf-6de2c26392c2 | -8.0153 | -51.80769 | 2026-08-26 04:51:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cae6afef-6e91-33e3-b5e8-1ff8c4e0aa25 | -8.29829 | -47.61576 | 2026-08-26 04:51:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3238c830-61b5-3511-b2f7-8c7a2b18141c | -6.14403 | -53.69118 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cd8082ab-62eb-3707-893d-fa52a77f9929 | -5.94112 | -57.73669 | 2026-08-26 04:51:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 235d3ca5-d7e9-3917-b02b-13a88312351a | -8.03354 | -51.81466 | 2026-08-26 04:51:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4cdb7842-1af0-3b98-907d-09ba104f1709 | -6.54219 | -56.26133 | 2026-08-26 04:51:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ca1ef7b2-fd2d-3887-9b51-9ae0606a0997 | -9.52166 | -51.68245 | 2026-08-26 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a52326c7-a72a-3020-b141-43264ce14fb5 | -7.53204 | -61.38654 | 2026-08-26 04:51:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 35460123-5312-3c09-ba7a-32b2893ac541 | -3.2567 | -52.23555 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fe7bd710-180d-35e8-ae21-c03b24c2fd86 | -9.65737 | -48.31299 | 2026-08-26 04:51:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| decc3ac1-b8ed-3e08-adea-75fd2ee2ba05 | -6.12624 | -57.83052 | 2026-08-26 04:51:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| c65ca76c-466c-3794-bae6-ce2e9f6fa180 | -7.11158 | -56.56477 | 2026-08-26 04:51:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 49cee09f-20b6-3841-a1b9-be649c23ddd3 | -6.26345 | -55.4204 | 2026-08-26 04:51:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f84b786f-c049-3413-b8fd-51a04fee4947 | -6.5037 | -53.26479 | 2026-08-26 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7e214800-14b7-3fa8-8cf0-2d7accd465d7 | -8.07008 | -47.52225 | 2026-08-26 04:51:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b7edb6b2-6e39-3019-9a1c-d8671a0a2929 | -7.2789 | -45.35659 | 2026-08-26 04:51:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 158a4e7b-e040-35f5-94e7-5b78ce4f5068 | -8.52774 | -54.84607 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a24f06e2-0477-3ca6-8724-ee5110c0afff | -7.38197 | -55.15734 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 46d77822-380e-37f2-b09b-3ffb81ba481c | -3.53268 | -48.18309 | 2026-08-26 04:51:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 2962e80c-895f-3582-972b-9768bbe656fb | -8.12513 | -47.47391 | 2026-08-26 04:51:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c7da2eb6-809f-3423-ba98-113f2eb359d2 | -8.15013 | -47.50923 | 2026-08-26 04:51:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 29.4 |
| 17371075-e304-3fbb-885d-c972d7a2654b | -6.12683 | -57.82694 | 2026-08-26 04:51:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 9aa7ea66-f5ea-34c2-9ae9-dae839442a90 | -3.13112 | -61.18299 | 2026-08-26 04:51:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b54da9bf-c7e4-3e01-9974-493e479c1afc | -8.02964 | -51.81778 | 2026-08-26 04:51:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d3696e47-8330-31e1-bed1-62d5608f751b | -6.1538 | -57.94246 | 2026-08-26 04:51:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0b954e49-f281-38a5-81ed-5204d13d8f49 | -6.24725 | -55.47514 | 2026-08-26 04:51:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d113b536-909f-3b41-b9b5-2823cbdc9a59 | -6.9184 | -60.06641 | 2026-08-26 04:51:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| bfbefca4-9b81-3808-9c89-1b8086009619 | -6.68575 | -58.71635 | 2026-08-26 04:51:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 13f1971d-b16c-3de1-b941-6eb7b56df3fb | -7.54629 | -61.36497 | 2026-08-26 04:51:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 978bf2f2-1f86-3190-a49f-17c0d3f49bc8 | -5.77459 | -57.55318 | 2026-08-26 04:51:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8f4ad52c-e4ef-329e-9298-5c7972c99011 | -9.90218 | -46.48527 | 2026-08-26 04:51:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1f8caf9c-5329-30eb-9722-ff20256c3eda | -6.50479 | -53.25784 | 2026-08-26 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| cb94f53c-2d06-3514-a298-3fd0280f55fa | -7.28833 | -44.08003 | 2026-08-26 04:51:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 24c78ed6-83a2-3f2a-a6a8-c27814b3b7c7 | -7.39156 | -55.15821 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 167f2840-4c41-362a-aa89-8d46b88022ef | -8.06953 | -47.52609 | 2026-08-26 04:51:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 02964cd9-f011-3ad4-8118-9d7e00b930a3 | -6.27001 | -53.36647 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 3fe7962e-41cc-3285-8bb1-973d509d3bca | -7.56153 | -61.42522 | 2026-08-26 04:51:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d44cc58a-e173-37ec-a831-cbe8776d75d3 | -10.37461 | -45.06536 | 2026-08-26 04:51:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 6b70d020-f9f6-307b-ba57-000a6b3beaee | -6.25015 | -53.36329 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5f610e18-2ea5-33e3-9ed5-6a69b64117f4 | -3.78242 | -59.27959 | 2026-08-26 04:51:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 91ab30cc-0cb1-359f-99b8-0675069d3b8b | -6.28627 | -53.58741 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bebf2ac6-b939-36c5-883b-90e40cad2e0d | -7.483 | -55.2868 | 2026-08-26 04:51:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5fa5c776-7df1-39e6-b081-464a2550a527 | -8.59335 | -54.71842 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 89b17fcb-2ffb-301c-ab37-7132e32659c1 | -6.47406 | -55.86947 | 2026-08-26 04:51:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 150a683a-6058-3609-86da-f2b5b7ee92b7 | -4.59171 | -56.05568 | 2026-08-26 04:51:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4599a114-45ed-390d-adb4-bc5717552042 | -8.59509 | -54.70757 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 344be7a6-6743-336e-94d2-923e3b49f9e8 | -4.80938 | -45.76675 | 2026-08-26 04:51:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| eb083b97-b523-3c7d-9405-2b84b1b3f890 | -6.62596 | -58.50808 | 2026-08-26 04:51:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 437aedb0-93c0-336d-bcfc-a0c59f32b0e3 | -9.02013 | -50.78028 | 2026-08-26 04:51:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9c469058-27cd-3e1f-8b2f-db1a9abf26d0 | -6.15849 | -53.68624 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 83e35cb4-92ee-32ca-99f9-d9af8c034e26 | -7.39849 | -55.15919 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b388908c-bc04-36e3-ab2b-6d65c1dd9d6c | -6.93861 | -62.88177 | 2026-08-26 04:51:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 83c529f4-4c7e-34a3-b5c2-ea6c643f3305 | -9.69552 | -49.14503 | 2026-08-26 04:51:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 23ad7625-9358-3a21-81eb-bf274c656baa | -8.01512 | -51.82287 | 2026-08-26 04:51:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 13e30d91-a0e5-3f36-a08d-c43c75ec5b61 | -7.56228 | -44.47797 | 2026-08-26 04:51:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a69d0657-5161-33c6-9789-f579b5fd0a08 | -6.982 | -59.25414 | 2026-08-26 04:51:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1668b2a7-8807-3cfe-8601-1d89631e9037 | -8.06482 | -47.52924 | 2026-08-26 04:51:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3ac1ca8e-3e66-3ff4-a286-ae770a7fd34c | -7.5122 | -61.38626 | 2026-08-26 04:51:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bb42f822-ccee-3f53-a436-a45d0999e04c | -7.02152 | -59.23409 | 2026-08-26 04:51:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 698d016f-5725-3c0a-bb1f-cbedc61cf16d | -6.14595 | -59.92253 | 2026-08-26 04:51:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 19df6d0b-1f7c-3d51-804c-261846752f1d | -3.42399 | -52.92802 | 2026-08-26 04:51:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8768b376-7bde-3750-89c6-d7b8a4dca7e8 | -7.2919 | -44.08801 | 2026-08-26 04:51:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| d06ffe40-4df9-3f7c-b3d5-252314e5347e | -7.09596 | -56.54417 | 2026-08-26 04:51:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c505a4a9-9482-3124-8b93-c0839929fb47 | -6.61095 | -58.38614 | 2026-08-26 04:51:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f32abd29-f13d-3a66-a949-816b43140346 | -8.62776 | -54.69791 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4531656c-ac62-338c-b224-c67482fa01f7 | -6.90819 | -58.99598 | 2026-08-26 04:51:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 518c0776-3e81-3b74-8f34-a081ded37490 | -6.14281 | -57.70574 | 2026-08-26 04:51:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b9355ace-c57d-3a1a-ae45-74b24855af86 | -8.14595 | -47.50858 | 2026-08-26 04:51:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 29.4 |
| 3aa258fa-dc3d-3919-a095-5bea3a383edd | -7.32182 | -42.97805 | 2026-08-26 04:51:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| ee4b976e-9b53-37cd-bc8f-fbc03cf2ae40 | -8.58998 | -54.71786 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7c07f7d5-dedf-3e34-b43a-435a2ebe64a4 | -9.04058 | -50.78728 | 2026-08-26 04:51:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 92b54a5b-a497-38b4-8887-24f7b0e76229 | -7.38121 | -55.15649 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 74dd774c-7abf-36b1-bcb5-22db297a5b5f | -6.28329 | -53.36855 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 34635f9c-78fe-36c3-9880-89b73a1b3066 | -6.6273 | -58.50022 | 2026-08-26 04:51:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 4c3f3e53-9754-3f36-98be-aefc99ac85ba | -7.45062 | -43.09865 | 2026-08-26 04:51:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 47802202-bacb-329d-b540-90cf4a8df58f | -6.309 | -53.573 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 2621a1ca-5373-3983-8ed6-eb2bd94e99a5 | -7.52784 | -61.38588 | 2026-08-26 04:51:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| b58f9c52-0e8e-3744-928b-9dc0aee60c8e | -6.98645 | -59.28132 | 2026-08-26 04:51:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| f2943bdc-97b6-34f1-bc1d-df0f4c5b4417 | -9.52278 | -51.67506 | 2026-08-26 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d10a121c-0209-3da4-94ab-338a30201a60 | -7.01273 | -59.23264 | 2026-08-26 04:51:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 51250a8f-8c07-3824-80dc-940a3a366c98 | -6.16841 | -53.49354 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1306327b-f67a-3869-9425-d07cc9c09798 | -3.12606 | -61.19231 | 2026-08-26 04:51:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 611d20cd-e9ea-3314-a7e7-d4df7634ccdc | -8.75912 | -44.25051 | 2026-08-26 04:51:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| de0ecd82-e500-3fb6-a5fa-2821e3e0f0b6 | -6.43904 | -54.96634 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0f76a22e-fa59-337f-b263-b3f8794c9aba | -7.31901 | -42.98147 | 2026-08-26 04:51:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 2d8a7f70-c09d-30bc-a392-83cfd81cefb4 | -6.74651 | -59.63813 | 2026-08-26 04:51:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6f9e5b1b-b0e4-362c-a6cc-e58830e99df7 | -6.27777 | -53.38196 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a9a702c9-6513-39ce-aa81-ce9a6def3355 | -8.09249 | -51.67597 | 2026-08-26 04:51:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5f586132-ab3b-3abe-a08b-b0f4f989d6df | -7.47138 | -61.38213 | 2026-08-26 04:51:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 186bdc49-174b-3275-b0a6-917c605d58a3 | -5.9417 | -57.7332 | 2026-08-26 04:51:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 69bb54d3-6522-3b66-af2a-6afb6bd1384d | -10.37796 | -45.06367 | 2026-08-26 04:51:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 10.9 |
| b18464f5-313a-3e49-a2f4-49d71230670e | -6.18614 | -53.48916 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a1769fa2-4f01-3088-b9a0-82a19e2af2ac | -3.10985 | -61.22431 | 2026-08-26 04:51:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |


[Clique aqui para ver as próximas entradas](README31.md)
