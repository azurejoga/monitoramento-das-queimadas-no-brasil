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

## Dados Diários - Página 62

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c649b450-a0c8-3a24-947a-9b8f832fcdb8 | -7.10594 | -42.52921 | 2026-10-08 04:02:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 0380188d-2190-3a24-8d46-c67daf3ab736 | -6.60561 | -37.89848 | 2026-10-08 04:02:00 | NOAA-20 | LAGOA | PARAÍBA | Brasil | 2508109 | 25 | 33 | nan | nan | nan | Caatinga | 1.4 |
| abe6ae47-0b2f-3159-aa10-904b8f417a10 | -5.52649 | -44.62788 | 2026-10-08 04:02:00 | NOAA-20 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c6d09854-0c90-309d-9955-94aca86d6507 | -5.47995 | -42.86944 | 2026-10-08 04:02:00 | NOAA-20 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| c53fd3c4-925a-3d82-ae6f-88b6cd0c9bd8 | -6.79155 | -41.25476 | 2026-10-08 04:02:00 | NOAA-20 | SÃO LUIS DO PIAUÍ | PIAUÍ | Brasil | 2210375 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 70175319-4de7-3e16-a347-4b6811f0488a | -3.35578 | -50.48582 | 2026-10-08 04:02:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8fc3e3ed-b3b1-3809-9dd4-a3b7810bbe05 | -11.23721 | -45.24874 | 2026-10-08 04:02:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 285c9827-0848-32c7-a50a-30084fcce93c | -6.59623 | -37.89331 | 2026-10-08 04:02:00 | NOAA-20 | LAGOA | PARAÍBA | Brasil | 2508109 | 25 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 23f4b654-7acf-3bc2-919a-378a44fb797f | -7.37348 | -44.03681 | 2026-10-08 04:02:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 4a892be3-56ef-3952-b38b-ce1a23050595 | -11.86014 | -40.19783 | 2026-10-08 04:02:00 | NOAA-20 | BAIXA GRANDE | BAHIA | Brasil | 2902609 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 176df3cd-049b-3d6a-81ec-1ab823586e4f | -4.26197 | -46.39954 | 2026-10-08 04:02:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3ca52ee8-7088-36b2-9970-1b064b400bd1 | -6.83428 | -39.56165 | 2026-10-08 04:02:00 | NOAA-20 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 75d44444-fd23-3c25-9b06-7226fe78feb0 | -11.61733 | -43.63762 | 2026-10-08 04:02:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 800e2d13-1790-3ede-979f-562e080887f5 | -11.45738 | -43.38937 | 2026-10-08 04:02:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ca8be72b-58e7-395c-a067-cce3fa8552c8 | -6.84651 | -39.54937 | 2026-10-08 04:02:00 | NOAA-20 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| b94e630c-17d0-3988-b735-9a6d10ba3d96 | -11.84509 | -43.53328 | 2026-10-08 04:02:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d2cb5dbb-98c5-322b-b179-c3f2e56478e8 | -6.63475 | -43.74068 | 2026-10-08 04:02:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 22.3 |
| 7da38eac-226d-3d64-8172-d35dae3bd372 | -4.28529 | -49.09159 | 2026-10-08 04:02:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b6e6b71f-6be1-3214-88b4-7ef99239e0b5 | -5.412 | -37.7781 | 2026-10-08 04:02:00 | NOAA-20 | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 1.1 |
| a413a380-894e-3aa5-a69b-522a5c4efeea | -8.7161 | -45.18283 | 2026-10-08 04:02:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 529a6b0b-a785-375a-8b19-2ac1b3a68493 | -6.83073 | -43.64265 | 2026-10-08 04:02:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 186b1e8d-0d09-31d4-b6c3-5bde6f671308 | -5.71723 | -41.63668 | 2026-10-08 04:02:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 6f47a53a-7183-358d-a785-8a476b2276ce | -5.73841 | -41.75803 | 2026-10-08 04:02:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| f68e580c-be06-3cf1-9af3-45683f104bb9 | -8.29095 | -50.26718 | 2026-10-08 04:02:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 10eef47f-9896-303b-ba50-2905f9641aad | -6.94564 | -45.27733 | 2026-10-08 04:02:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e9ec8e27-b54b-3dfa-bc65-c77de6802fff | -5.68692 | -40.89209 | 2026-10-08 04:02:00 | NOAA-20 | NOVO ORIENTE | CEARÁ | Brasil | 2309409 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| c1bcf2d1-a997-39c6-8004-c0cd47f7f5a0 | -6.94785 | -45.29107 | 2026-10-08 04:02:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 6ed91722-de74-3a9a-801f-31a380081dca | -6.61545 | -37.90036 | 2026-10-08 04:02:00 | NOAA-20 | LAGOA | PARAÍBA | Brasil | 2508109 | 25 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 2e7e11b4-471c-3a62-ad42-6e6141b8b6b0 | -3.17652 | -50.44851 | 2026-10-08 04:02:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 70026668-af4c-3b6f-a8bd-98db169e5989 | -6.94339 | -45.29024 | 2026-10-08 04:02:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| bd749b58-6683-36eb-be7c-22aa4f5e4eac | -6.63247 | -43.72924 | 2026-10-08 04:02:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 81c1c38f-4a06-3055-9c47-9bd6b2a9006a | -5.83047 | -47.40069 | 2026-10-08 04:02:00 | NOAA-20 | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f9123e69-54f8-3906-9fea-b7f5d038d6cd | -5.17754 | -45.33907 | 2026-10-08 04:02:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 41357f7e-de7f-30e4-954a-c7c61da146a8 | -8.45012 | -46.41129 | 2026-10-08 04:02:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 50d99812-f9b0-365d-bbcf-d415d7033c1b | -8.73912 | -45.15279 | 2026-10-08 04:02:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 17.9 |
| 87a6448f-2546-3cd0-96fc-10a228e495c1 | -6.61599 | -37.89687 | 2026-10-08 04:02:00 | NOAA-20 | LAGOA | PARAÍBA | Brasil | 2508109 | 25 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 1dddd795-fd46-34b6-a8c5-583aaf4948f3 | -6.14048 | -47.92772 | 2026-10-08 04:02:00 | NOAA-20 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 2dd79c45-1133-39d4-b5cd-1369167bc761 | -9.78962 | -37.32295 | 2026-10-08 04:02:00 | NOAA-20 | PÃO DE AÇÚCAR | ALAGOAS | Brasil | 2706406 | 27 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 796d5340-76f2-380d-989f-9a5558ee3989 | -3.80142 | -47.4906 | 2026-10-08 04:02:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 057c56f1-9e43-3e1c-9469-dbbfe55972ed | -8.59956 | -45.63627 | 2026-10-08 04:02:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| bf887e20-cbc3-3f77-9585-1850893e9a3d | -3.34575 | -50.48344 | 2026-10-08 04:02:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 657d3999-87af-33b3-9943-15ebc28a3408 | -8.72041 | -45.18364 | 2026-10-08 04:02:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 8617d9e6-d670-3574-b918-019fcb698f83 | -11.71414 | -43.66194 | 2026-10-08 04:02:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6372608a-48e7-3ec7-a059-ff732dfc2935 | -3.18157 | -50.55739 | 2026-10-08 04:02:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e8508bab-e07b-3b6c-9352-f890f1e28ab9 | -8.72616 | -45.17616 | 2026-10-08 04:02:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 8f18871f-0475-37e5-8467-badb2dd84e16 | -9.45307 | -44.62259 | 2026-10-08 04:02:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2233574a-b79b-3c32-9ce3-4dbd578b55bf | -9.96882 | -43.55452 | 2026-10-08 04:02:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e8dc1c31-f15e-3443-8334-d1d8f43ecc91 | -3.17457 | -50.45977 | 2026-10-08 04:02:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| feb860ce-a853-354b-9ddd-b74951f56f3b | -7.3115 | -43.98491 | 2026-10-08 04:02:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b51f80e5-94db-3aad-bca1-cd679271e074 | -3.54372 | -50.09866 | 2026-10-08 04:02:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 187d8c7d-eb4e-39e2-9627-75023bd227e8 | -6.94639 | -45.27302 | 2026-10-08 04:02:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| a274890f-15ea-34d6-bd83-8104bd100e06 | -7.59937 | -46.76651 | 2026-10-08 04:02:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5f466f64-9e92-35f9-99b1-96cfa4684fa4 | -5.71581 | -41.75863 | 2026-10-08 04:02:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 5dd9b24c-35a3-3b02-8f36-49ef9ab70ed4 | -3.18262 | -50.55146 | 2026-10-08 04:02:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9cf9481c-0f03-3046-b2be-346cf218283d | -6.84206 | -39.55582 | 2026-10-08 04:02:00 | NOAA-20 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| b92a7fc5-6063-32ec-92bd-42bbf586bc93 | -7.46753 | -42.84951 | 2026-10-08 04:02:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 765b61ec-de25-30cd-b766-5434b72db4b5 | -11.62087 | -43.6846 | 2026-10-08 04:02:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 58d8936b-7700-3e8f-90a7-412fdcab0835 | -11.77957 | -43.53616 | 2026-10-08 04:02:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ee35a859-b231-37dc-8fd8-b4ddd2f4dfca | -9.36937 | -45.94155 | 2026-10-08 04:02:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ddd248c1-ea8c-3305-9b35-a632c9a3b222 | -11.22403 | -45.25054 | 2026-10-08 04:02:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3f74cc64-b854-3ae0-9c7f-751b92846b3b | -5.37822 | -44.17637 | 2026-10-08 04:02:00 | NOAA-20 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 410695cb-0749-3c10-adf0-642924643c21 | -7.48446 | -42.79537 | 2026-10-08 04:02:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 52acbdda-84a5-3c61-b590-528682281e7c | -5.75455 | -42.06805 | 2026-10-08 04:02:00 | NOAA-20 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 20b0e05f-d103-366c-9414-b14bc4e3b52d | -9.45781 | -44.61966 | 2026-10-08 04:02:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 50fad449-6f2b-323d-8ff2-400cd7392cab | -5.87082 | -50.10173 | 2026-10-08 04:02:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 32cc9b81-321d-32f3-a1f4-8ee9c6f4c3da | -9.79854 | -44.77811 | 2026-10-08 04:02:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 57a2a3aa-2afe-3406-be60-32ee09861cdf | -8.97778 | -45.9135 | 2026-10-08 04:02:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8c85b2c6-f43a-3623-a387-12c3461834b1 | -3.18827 | -50.55856 | 2026-10-08 04:02:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 07f2cbff-856e-3f8b-98ed-4fa85fc8a87a | -5.51253 | -42.81889 | 2026-10-08 04:02:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 107c932b-6b81-34db-84b8-44b4a725dce5 | -4.78303 | -45.68298 | 2026-10-08 04:02:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 962384e0-f4d4-3c1b-b837-73d4a65ba925 | -8.217 | -46.33075 | 2026-10-08 04:02:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 12.1 |
| d9c12b84-93fc-324b-9cd1-32c30697aef8 | -6.14652 | -47.92522 | 2026-10-08 04:02:00 | NOAA-20 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 47.5 |
| dcc3f728-d446-3d53-bf1d-b4a69627c9c4 | -3.55019 | -50.09989 | 2026-10-08 04:02:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 17efbaf7-9ca5-3096-8f61-3db08a761331 | -4.55468 | -40.7268 | 2026-10-08 04:02:00 | NOAA-20 | IPUEIRAS | CEARÁ | Brasil | 2305902 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 7e7f3ddf-5759-3a4f-99c7-4973f1e4a2b2 | -3.36346 | -50.48109 | 2026-10-08 04:02:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4b1d0d71-b480-3096-9401-fcc9e735151f | -9.37018 | -45.93699 | 2026-10-08 04:02:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e218a95c-4873-3a44-a29a-17c5d19cb6e6 | -8.99667 | -46.7652 | 2026-10-08 04:02:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| dd7da13a-d24f-3bf7-ae32-5f8fe3ce4bf0 | -11.64415 | -43.68681 | 2026-10-08 04:02:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| feb65a74-1503-37be-a820-854cc692c4f6 | -7.14632 | -46.52221 | 2026-10-08 04:02:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 60c63d56-6e0f-3281-abeb-c4bb1c711588 | -8.71537 | -45.18699 | 2026-10-08 04:02:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 9f608e55-74eb-35e7-8648-8fb7bb03fd11 | -9.02708 | -46.90116 | 2026-10-08 04:02:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 46c323e0-73bd-3743-880e-044c380ded5c | -6.63188 | -43.73281 | 2026-10-08 04:02:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 53.1 |
| 3cb1d328-5209-3674-8cf9-2cf0c8d497e9 | -8.29006 | -50.27184 | 2026-10-08 04:02:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 451fe94c-8e64-3cb5-bf22-7529c03b0954 | -9.91226 | -44.79828 | 2026-10-08 04:02:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 23b2feb9-8744-30d4-b59b-b18b26d5bf5e | -7.07049 | -40.94323 | 2026-10-08 04:02:00 | NOAA-20 | ALAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2200251 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 09da18d0-356e-3c59-b0fd-cd033d038603 | -3.4785 | -50.08978 | 2026-10-08 04:02:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 350903cc-198b-3b17-bd5a-63d340b1fee6 | -7.07458 | -40.93993 | 2026-10-08 04:02:00 | NOAA-20 | ALAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2200251 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| bd547bb3-0aa0-3c53-8387-c7dd24d937d5 | -7.15117 | -46.52309 | 2026-10-08 04:02:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ba513251-5a8f-3958-8894-f7dc3b21e3d9 | -6.98543 | -40.03828 | 2026-10-08 04:02:00 | NOAA-20 | ASSARÉ | CEARÁ | Brasil | 2301604 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 3849d932-71a5-3922-9eb0-1f4596340354 | -8.72405 | -45.16284 | 2026-10-08 04:02:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 9.7 |
| ae3a66e6-c018-31ea-942b-9e3302a59665 | -6.84595 | -39.55287 | 2026-10-08 04:02:00 | NOAA-20 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| dbfa3d74-8cd8-359e-bc86-b00599129da6 | -5.24727 | -50.91963 | 2026-10-08 04:02:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c994b070-223b-317d-8362-010247bccd8f | -8.71391 | -45.19534 | 2026-10-08 04:02:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e6b20a95-91db-34e0-b856-3d3db4e09d5a | -3.19497 | -50.55973 | 2026-10-08 04:02:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 1482568f-0d60-3aef-8d2a-0caa9a3b3802 | -6.94415 | -45.28587 | 2026-10-08 04:02:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 3d30f1a1-4691-3857-9bf5-1b7d75cb8326 | -4.49618 | -42.54437 | 2026-10-08 04:02:00 | NOAA-20 | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| b42c2013-f1cd-331f-bfd6-42c2b9cf0f87 | -5.73091 | -45.15863 | 2026-10-08 04:02:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 547fbc21-222b-33dc-95c8-1e237fd7bfca | -3.35237 | -50.48481 | 2026-10-08 04:02:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 720f3c90-4a84-3cad-9aab-8987209263f6 | -9.47201 | -47.7581 | 2026-10-08 04:02:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 77cd6271-8498-38e1-84cd-3dbf2bb8db46 | -8.37844 | -46.28812 | 2026-10-08 04:02:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |


[Clique aqui para ver as próximas entradas](README63.md)
