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

## Dados Diários - Página 26

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 061a9c8f-4517-3944-93b0-4c634d494a91 | -7.95833 | -43.89214 | 2025-09-22 04:38:00 | NOAA-20 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 38da4bee-dea8-3c07-8555-6c5d0ed2fc6e | -5.11934 | -50.62359 | 2025-09-22 04:38:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3271b494-1541-3580-803e-4bcac98e782e | -6.23044 | -51.71764 | 2025-09-22 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6ff3d6af-4a2b-3581-a661-99bcd6b787c9 | -7.44027 | -40.10812 | 2025-09-22 04:38:00 | NOAA-20 | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 1.6 |
| ce83cd88-ff60-34e3-932b-874b4755f1ad | -10.25444 | -46.0752 | 2025-09-22 04:38:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1931c73c-1e11-30d1-8a6b-9d3448a727bc | -10.38196 | -46.07607 | 2025-09-22 04:38:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 16c227a5-479f-318a-9a4b-7a0750b033c3 | -5.0643 | -40.47169 | 2025-09-22 04:38:00 | NOAA-20 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| fd9c19d6-4b8c-3697-801e-a6de0115c27e | -7.22849 | -43.7473 | 2025-09-22 04:38:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 10dfe18b-76a1-3e47-b821-bbc807d903a1 | -7.60678 | -44.44782 | 2025-09-22 04:38:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3a4efe72-2c5d-380e-84aa-b5b5fab4f284 | -5.6534 | -51.46276 | 2025-09-22 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 45549b48-3a9c-3e98-9b08-50a57d8941c4 | -7.71428 | -55.45215 | 2025-09-22 04:38:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| dc364b1b-3b10-3820-84fc-3b42d843c426 | -10.38578 | -46.07668 | 2025-09-22 04:38:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5718c26c-ea90-316f-90d3-fb336cc9e187 | -7.61019 | -44.48191 | 2025-09-22 04:38:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1eff9847-a253-32eb-b9b1-5201fc026d82 | -7.44096 | -40.10789 | 2025-09-22 04:38:00 | NOAA-20 | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 635bdeb8-f02b-3a98-a11b-bd62361f1004 | -6.58884 | -62.93144 | 2025-09-22 04:38:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8fcadd1e-638d-33cd-a2fe-1ce9c2d87309 | -10.36567 | -46.06207 | 2025-09-22 04:38:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 01591f67-726f-39fb-a791-60fb2dd1cb36 | -5.66755 | -51.66189 | 2025-09-22 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e4640df4-86fd-3420-99f9-f78f5b81a845 | -7.22364 | -43.75073 | 2025-09-22 04:38:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e7959e9b-8312-358c-b8c5-e0cac596b511 | -10.40105 | -47.85318 | 2025-09-22 04:38:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1edc7181-a2cf-36ce-8aa1-026255cf0a28 | -10.65838 | -44.23785 | 2025-09-22 04:38:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a4f7fa89-46f7-37fb-a660-94dffe7028df | -4.315 | -48.08904 | 2025-09-22 04:38:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| dc662ca3-2d74-3a65-87e7-02345ca75b56 | -7.6591 | -61.127 | 2025-09-22 04:38:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| f8934d74-724e-3882-993e-7e838a49dafa | -7.36537 | -43.84298 | 2025-09-22 04:38:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 05306133-fa6d-3ea4-96d5-97b251cdbd69 | -7.93684 | -44.09811 | 2025-09-22 04:38:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 156a5117-0395-3900-b5b3-b6c01b9135d1 | -3.05067 | -46.92962 | 2025-09-22 04:38:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 505f62f6-f8f0-316f-9347-d1eb0a2b6313 | -5.82747 | -49.91606 | 2025-09-22 04:38:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| a26c9f2a-f787-3055-85d4-155d65fd16d8 | -7.79957 | -46.19387 | 2025-09-22 04:38:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 397a35ca-c3e6-311e-be29-72ba1b5ccee8 | -7.81366 | -46.20021 | 2025-09-22 04:38:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3036a51f-9879-3a0e-b9e3-b4f9ece04a7b | -10.40863 | -47.85032 | 2025-09-22 04:38:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c020ef00-9b06-3c7a-be8f-3f8a9a7dcdec | -10.37882 | -46.0707 | 2025-09-22 04:38:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 185c5370-8048-32c2-9877-9d4b4a4792e9 | -7.02783 | -46.30804 | 2025-09-22 04:38:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| db5a605c-d08b-3114-a904-4a03ad28a41a | -7.36237 | -44.55955 | 2025-09-22 04:38:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 75d23a45-e43c-3ac2-b82d-1d499c51ee11 | -7.93627 | -44.102 | 2025-09-22 04:38:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5f230593-a8a3-3f64-a465-a13cfe86df63 | -7.37749 | -44.56898 | 2025-09-22 04:38:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 81bbbb0d-9d4f-33a0-bef3-584a1eb45189 | -6.31366 | -45.91521 | 2025-09-22 04:38:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b9e86509-2e6a-3610-b512-55086cceb74f | -5.80801 | -50.21063 | 2025-09-22 04:38:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c9c2a5c9-6931-350a-becf-1f62687746fa | -6.39525 | -50.9106 | 2025-09-22 04:38:00 | NOAA-20 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cd518197-24e6-32d2-a835-0b86006a2bfd | -7.35884 | -44.55541 | 2025-09-22 04:38:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4012ead3-ec05-30a6-8c4d-c75de174d66f | -6.04222 | -51.63652 | 2025-09-22 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6a893c54-7a5a-3e46-a498-1a552fcbb12f | -5.57302 | -48.98959 | 2025-09-22 04:38:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 99197a64-d3c3-37e1-82e9-3ae411a5e507 | -3.63053 | -52.35983 | 2025-09-22 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 962a837a-63c1-320e-85db-d01d99083ef9 | -7.60559 | -44.48497 | 2025-09-22 04:38:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| d7dcd9b0-3a25-3875-92c0-27ecdae15971 | -5.65217 | -51.47037 | 2025-09-22 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| b51b00d3-d927-3bae-a7cf-e5e8542fb9f8 | -10.28084 | -46.67723 | 2025-09-22 04:38:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7f739824-1e71-34af-8ad6-c686deb3ae3e | -10.25215 | -46.07267 | 2025-09-22 04:38:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 3984cfcd-f74a-3b0a-9f81-2699bbe5c9f5 | -3.62977 | -53.65335 | 2025-09-22 04:38:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5dc54e2a-3d08-30c9-9486-480d8394fb59 | -6.41546 | -43.84665 | 2025-09-22 04:38:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b513bc8f-e68f-3b7c-9ec6-648211236967 | -8.30324 | -43.68292 | 2025-09-22 04:38:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 40f0a751-c6f0-330b-b17d-8c478f97bde7 | -5.68906 | -51.75636 | 2025-09-22 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5cf0d259-e12a-3d36-8df2-a2e7efcb3709 | -5.11253 | -46.16714 | 2025-09-22 04:38:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ad597241-efdf-3ddb-988b-b44fede78549 | -7.23216 | -43.75188 | 2025-09-22 04:38:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 3ad6e8e2-fb6a-39f7-8edc-ea187f08cc85 | -5.56876 | -42.12795 | 2025-09-22 04:38:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| fa04c76d-3f2f-332f-a8f2-209b1a1a3f9b | -3.70121 | -51.41217 | 2025-09-22 04:38:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7b6a8f13-8661-3f47-84c3-e3e1ad235c72 | -6.39466 | -50.91422 | 2025-09-22 04:38:00 | NOAA-20 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5cbb0568-9ac4-3f66-985e-c8513d241251 | -5.58126 | -51.90535 | 2025-09-22 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 55e7c778-1c5c-3925-acfd-5d039ed16e19 | -7.35631 | -44.54429 | 2025-09-22 04:38:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 432c3fb8-fd87-35af-a167-70af8aa1d5e1 | -4.47113 | -55.09776 | 2025-09-22 04:38:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f14d204b-e477-3e4f-989d-90da4c7e003b | -10.32122 | -46.09897 | 2025-09-22 04:38:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0a3c2a61-2123-3872-bfb8-25f988ca1e0e | -7.58881 | -45.50308 | 2025-09-22 04:38:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dbdec2cb-ecf3-37c8-a4e5-d1e2311351ee | -6.71256 | -45.36471 | 2025-09-22 04:38:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3e3ce1e3-f8fe-3428-a414-00621cf34af7 | -7.23582 | -43.75651 | 2025-09-22 04:38:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f65ce623-2401-399d-bd85-942e347d13a3 | -6.0073 | -44.33401 | 2025-09-22 04:38:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9177bc80-c20a-3cb4-b859-2ab4cc57531c | -6.45336 | -45.67903 | 2025-09-22 04:38:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| aadfee11-057a-3cb1-b65c-7f4bc929d852 | -5.58425 | -49.24284 | 2025-09-22 04:38:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 599930f2-b9e9-3ba2-9fad-90abdeaefb45 | -10.3406 | -46.0731 | 2025-09-22 04:38:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 39a19efa-13ed-3394-993e-1d7f0ae379fe | -10.39455 | -46.09735 | 2025-09-22 04:38:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1aa8bbf0-b1ec-3543-8f67-93eb658c323d | -7.65895 | -61.1253 | 2025-09-22 04:38:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 399694b2-601b-3862-81e6-e5ce04ff8e2f | -4.31391 | -48.09602 | 2025-09-22 04:38:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 169327d6-5c4a-36ed-a106-05e155da4e08 | -6.44459 | -45.68684 | 2025-09-22 04:38:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b926ceba-1bdf-373d-919b-6e779ca7f1a5 | -6.9004 | -44.76668 | 2025-09-22 04:38:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 18.1 |
| 8541aa58-5183-3a82-94ee-843c2648e04d | -5.607 | -49.05544 | 2025-09-22 04:38:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4a9bbe41-b3b3-3ddd-943c-ad57825e772e | -7.70585 | -55.45073 | 2025-09-22 04:38:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 71ecf91a-ac98-3733-bc3f-9ba058003f61 | -7.70653 | -55.44682 | 2025-09-22 04:38:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| e9471a18-b489-3274-b70b-9b07bc02438d | -3.371 | -52.79589 | 2025-09-22 04:38:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 65a57e34-eac5-3411-9571-38449ca69312 | -3.9959 | -51.06596 | 2025-09-22 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4dae0786-79ef-37f6-aa6e-b9502a8812d8 | -5.57803 | -42.12939 | 2025-09-22 04:38:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| b9c3ba79-9c3a-3344-8d91-98149fc7214a | -7.36689 | -44.55677 | 2025-09-22 04:38:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 882c9c02-c133-3599-8b11-c2df96b4a06e | -8.02487 | -54.88422 | 2025-09-22 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cdd25a29-f3c9-3022-a1ca-130f434f8876 | -3.55164 | -51.66383 | 2025-09-22 04:38:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 47cc44ae-1005-3e31-b69a-39919c6a0e29 | -3.8947 | -52.18065 | 2025-09-22 04:38:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7ab0f4e6-7156-33e9-a122-cc4b86e94895 | -8.00912 | -45.71837 | 2025-09-22 04:38:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4a575086-bcda-3052-8980-306a0e298ed3 | -10.25196 | -46.06514 | 2025-09-22 04:38:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| c6482f49-9726-3a14-b509-afd94a344df8 | -7.81641 | -46.48355 | 2025-09-22 04:38:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ea58250e-1838-3c68-92dd-51ea93cc0cef | -4.32152 | -55.50756 | 2025-09-22 04:38:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ee88dbd3-e8e7-314d-9e03-fcd524564150 | -5.59031 | -46.25451 | 2025-09-22 04:38:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d62300e6-ecc5-312c-a6fc-250ac3d18ff2 | -7.23156 | -43.75591 | 2025-09-22 04:38:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 912bc669-f877-3bd4-bd84-90d6c917166e | -7.23096 | -43.75997 | 2025-09-22 04:38:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7879f46a-83ff-3e24-9afc-953383a3e48b | -10.40453 | -47.85375 | 2025-09-22 04:38:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7e04e879-4b87-3826-88d4-2dd53061e8a8 | -10.40514 | -47.84975 | 2025-09-22 04:38:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1d646a03-0e5a-34df-8503-00360d8007fd | -5.9153 | -50.00518 | 2025-09-22 04:38:00 | NOAA-20 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b7f2c8e8-df91-3961-88e5-ecabe75f667b | -10.46723 | -48.03802 | 2025-09-22 04:38:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 125bec91-2d4b-3b7a-baee-5a394826dca0 | -5.57774 | -51.90478 | 2025-09-22 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fa00d0c1-e9e5-3622-916e-e0557f142ef7 | -4.42782 | -47.26502 | 2025-09-22 04:38:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b64c7a80-7d00-3187-9ad2-a0c80aed1184 | -5.92009 | -51.33339 | 2025-09-22 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 168a2ddc-cab0-3ecd-b8c6-c064696bfb83 | -5.58673 | -46.25397 | 2025-09-22 04:38:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| aa86c6db-9946-3f8f-a0fa-6e5d2ffae630 | -4.31107 | -48.09565 | 2025-09-22 04:38:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ef9b7122-7da9-3972-b7fd-d18d3411a7b3 | -6.63163 | -62.93314 | 2025-09-22 04:38:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| cce0bacf-0b65-370a-927f-df6467627d9e | -7.80018 | -46.18972 | 2025-09-22 04:38:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| b5ed0f36-f013-3273-b4f5-e386c72b4a23 | -3.5579 | -52.20143 | 2025-09-22 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 42bdc593-0aa2-3f4f-964d-f7af0461f498 | -10.38894 | -46.08196 | 2025-09-22 04:38:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |


[Clique aqui para ver as próximas entradas](README27.md)
