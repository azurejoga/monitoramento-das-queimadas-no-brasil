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

## Dados Diários - Página 279

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 05c908fb-f17f-3071-acd8-a2fe4ab50604 | -5.87761 | -45.9479 | 2026-10-08 16:20:00 | NPP-375 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 26.0 |
| b3d2506f-2124-323b-9baa-c7e41e342670 | -1.39923 | -48.93782 | 2026-10-08 16:20:00 | NPP-375 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4e7b6c78-76c7-3529-b267-890f655a55a7 | -5.74054 | -42.07182 | 2026-10-08 16:20:00 | NPP-375 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 44.3 |
| 9e477ed8-b2fc-3265-b65c-76532a2fb6b6 | -6.21285 | -43.83411 | 2026-10-08 16:20:00 | NPP-375 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 100904ba-73c2-3876-b707-eee0afc96379 | -5.09496 | -46.22059 | 2026-10-08 16:20:00 | NPP-375 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 20.8 |
| 5aca5031-ad04-3e0e-9b54-cd5caf67230c | -5.09947 | -46.21998 | 2026-10-08 16:20:00 | NPP-375 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 20.8 |
| a3bea6e7-c544-3bae-857c-47252c84818f | -5.7784 | -43.33031 | 2026-10-08 16:20:00 | NPP-375 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 5815bdfa-ec4d-30a4-8da3-0c95d43321bb | -7.31597 | -43.99538 | 2026-10-08 16:20:00 | NPP-375 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 3c73cc1e-4a22-37f3-8d5b-2317cce01d03 | -5.94835 | -45.6916 | 2026-10-08 16:20:00 | NPP-375 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 24.2 |
| 4dc71c6b-609c-33d6-bc9c-7f151d347244 | -6.15352 | -47.92479 | 2026-10-08 16:20:00 | NPP-375 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 00146720-fcf2-3448-b65c-6782ffe445f3 | -5.70731 | -41.72725 | 2026-10-08 16:20:00 | NPP-375 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 13.0 |
| cf47faf5-e932-3ef0-af86-542ad8fb115b | -1.41622 | -51.53611 | 2026-10-08 16:20:00 | NPP-375 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| f3dadd0e-c431-30f1-ad9e-2b1503d4cb2f | -6.12537 | -44.14637 | 2026-10-08 16:20:00 | NPP-375 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| d91339ac-b616-39bc-81d3-e92ce9c2ae6d | -5.7003 | -53.48796 | 2026-10-08 16:20:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 14.2 |
| d07cb51a-a22b-365f-b8ef-8963913da5d7 | -5.89035 | -45.97335 | 2026-10-08 16:20:00 | NPP-375 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 284b9ab9-983c-3e39-ad21-bdcdba5472c2 | -4.09727 | -43.26872 | 2026-10-08 16:20:00 | NPP-375 | AFONSO CUNHA | MARANHÃO | Brasil | 2100105 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 12d37a83-8c90-3f6e-9e0a-35edfa07eafe | -6.0719 | -43.87966 | 2026-10-08 16:20:00 | NPP-375 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 14ca4b66-aa27-324c-9a87-87a77e8db86f | -7.6025 | -42.39228 | 2026-10-08 16:20:00 | NPP-375 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 121.5 |
| c1cfc1e9-cb1c-34a1-a20b-48de76a55e07 | -5.97451 | -41.37102 | 2026-10-08 16:20:00 | NPP-375 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 2f8ce030-a18e-3ccc-84b6-1c9a28cb07bc | -7.19684 | -44.26274 | 2026-10-08 16:20:00 | NPP-375 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 30.1 |
| 0f8adf95-b068-3424-aa22-e8987907bc51 | -7.33918 | -45.27972 | 2026-10-08 16:20:00 | NPP-375 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 7260f34e-d270-38c5-a434-751b4078fb69 | -6.8375 | -39.56327 | 2026-10-08 16:20:00 | NPP-375 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 6.3 |
| 641fcc75-4538-3de7-9be1-84b0a32d3a22 | -5.94952 | -45.69991 | 2026-10-08 16:20:00 | NPP-375 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 16.8 |
| a935a3cd-5fc6-3df1-87c6-f963f8b4c873 | -5.96335 | -43.90322 | 2026-10-08 16:20:00 | NPP-375 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 16.2 |
| 16831e9a-ec4e-3b91-a549-cdf340b12fce | -3.00566 | -54.08776 | 2026-10-08 16:20:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 29.8 |
| 326c236f-2ce1-3d42-b040-69ffa41ce5a2 | -6.17512 | -39.40937 | 2026-10-08 16:20:00 | NPP-375 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 467d41fb-d08e-301c-b619-b75c1029f884 | -5.72252 | -41.63926 | 2026-10-08 16:20:00 | NPP-375 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 32ffae1a-b027-3433-9152-454d54983e19 | -6.53392 | -45.37206 | 2026-10-08 16:20:00 | NPP-375 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 85.8 |
| a8e1d60f-0828-30a1-9e50-9932fc507020 | -5.7084 | -41.75843 | 2026-10-08 16:20:00 | NPP-375 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 10.1 |
| dee19920-bfa2-3570-b05d-69fdf91b7c06 | -5.66715 | -43.62362 | 2026-10-08 16:20:00 | NPP-375 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 763a3708-e0c4-3ee7-922c-4a30df085503 | -3.78405 | -41.66348 | 2026-10-08 16:20:00 | NPP-375 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 9.3 |
| bf428e3d-3b27-36b7-b39b-47371361b2db | -3.27416 | -44.20796 | 2026-10-08 16:20:00 | NPP-375 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 2adaae05-3271-3f13-a641-ec0820357b39 | -7.24401 | -44.52963 | 2026-10-08 16:20:00 | NPP-375 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 61.9 |
| 73eea316-2d1e-369b-a3ee-243d8123d1d5 | -7.10587 | -42.52921 | 2026-10-08 16:20:00 | NPP-375 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 8.3 |
| fa37d7c2-7a7d-37bb-b2f0-0fa251eaf4ee | -5.2775 | -47.91631 | 2026-10-08 16:20:00 | NPP-375 | SAMPAIO | TOCANTINS | Brasil | 1718808 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| a8dca55f-a86a-3fd1-a255-040e76b3731c | -6.24123 | -52.67624 | 2026-10-08 16:20:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 19.5 |
| 19647976-b09f-347a-8ffa-bf9012d3e7ec | -5.30512 | -45.72893 | 2026-10-08 16:20:00 | NPP-375 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 18.7 |
| b765aa34-3ae6-3acb-8673-f61d29c6d436 | -2.43633 | -49.62998 | 2026-10-08 16:20:00 | NPP-375 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 03ebdef6-4ae7-36a5-83bd-ec0523dd21a8 | -6.93678 | -44.56443 | 2026-10-08 16:20:00 | NPP-375 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| f29227a8-1ac5-3196-b951-f6a4c4cb6977 | -5.13423 | -44.74129 | 2026-10-08 16:20:00 | NPP-375 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e23b8e2e-f34b-3c79-add1-ed5a56d9f745 | -6.36861 | -45.596 | 2026-10-08 16:20:00 | NPP-375 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| f9c61bdb-0abd-37d3-b0ea-d080c463a5a7 | -4.1577 | -43.19952 | 2026-10-08 16:20:00 | NPP-375 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| ca3be76c-4527-3999-a302-d66b75e46fa2 | -2.51044 | -47.3793 | 2026-10-08 16:20:00 | NPP-375 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| af79cc6e-e4fd-3e2c-9b85-06cdaaec3c63 | -5.37919 | -44.19422 | 2026-10-08 16:20:00 | NPP-375 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 29.3 |
| 728631eb-d635-3bd9-b69f-70d86743c0cf | -5.22153 | -36.75596 | 2026-10-08 16:20:00 | NPP-375 | CARNAUBAIS | RIO GRANDE DO NORTE | Brasil | 2402501 | 24 | 33 | nan | nan | nan | Caatinga | 8.9 |
| 3520c7c5-bdc0-3682-8c00-be332dbb0cd8 | -1.59386 | -47.35736 | 2026-10-08 16:20:00 | NPP-375 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| abf74125-463f-3cf3-a023-3ec1b262520a | -6.15562 | -47.94002 | 2026-10-08 16:20:00 | NPP-375 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 93.0 |
| 85c4013e-d0e1-3d9e-b43e-75658fb9e3d9 | -5.74818 | -42.07474 | 2026-10-08 16:20:00 | NPP-375 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 11.8 |
| b913db55-c032-3e85-9370-a717ec03764e | -3.73239 | -39.53438 | 2026-10-08 16:20:00 | NPP-375 | ITAPAJÉ | CEARÁ | Brasil | 2306306 | 23 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 0fe8375b-5bed-3fe6-9fe7-d387a40ceafa | -5.78375 | -45.37938 | 2026-10-08 16:20:00 | NPP-375 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 05ab869c-81e1-3f29-b4da-404048f8fb39 | -3.00974 | -54.06474 | 2026-10-08 16:20:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 14.8 |
| 688447c2-f2ef-3dc9-8d8f-ce68f6e1fb95 | -5.58672 | -43.2054 | 2026-10-08 16:20:00 | NPP-375 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| bdc167cc-4e5d-3a73-a74d-f4cea56df466 | -5.74879 | -42.0545 | 2026-10-08 16:20:00 | NPP-375 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 17.6 |
| 471dc3c1-73dd-3dfb-9447-9f966ad7ff0f | -7.11313 | -40.68695 | 2026-10-08 16:20:00 | NPP-375 | FRONTEIRAS | PIAUÍ | Brasil | 2204303 | 22 | 33 | nan | nan | nan | Caatinga | 9.1 |
| b3203afe-e5ed-30c0-a22d-d3141618c6b7 | -7.77784 | -43.81634 | 2026-10-08 16:20:00 | NPP-375 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Caatinga | 14.4 |
| a2a12243-a29f-3580-a884-c1a25f8a2dd2 | -5.70155 | -53.49269 | 2026-10-08 16:20:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 20.3 |
| a8ffb7dd-36d2-3091-8fcc-76fbf8573acf | -1.56581 | -48.22518 | 2026-10-08 16:20:00 | NPP-375 | BUJARU | PARÁ | Brasil | 1501907 | 15 | 33 | nan | nan | nan | Amazônia | 25.6 |
| 88780d80-ad99-39f0-971d-b73a16c98a63 | -5.68243 | -42.5915 | 2026-10-08 16:20:00 | NPP-375 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 7.5 |
| ee04f67b-59ea-3b97-8dc8-f8e8ebd5d6cf | -3.09004 | -53.95796 | 2026-10-08 16:20:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 35.6 |
| 7188286b-1e09-3e7e-8b59-8b900fd60ad5 | -6.96859 | -43.43914 | 2026-10-08 16:20:00 | NPP-375 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 9.0 |
| a3e9f385-e2f3-3f9b-bbb7-231fd31fd630 | -5.75171 | -42.07421 | 2026-10-08 16:20:00 | NPP-375 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 11.8 |
| 2f7d4eca-8346-3fb3-bdec-ca645e46d3b0 | -6.22479 | -44.85766 | 2026-10-08 16:20:00 | NPP-375 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 185.1 |
| f9fa37e1-3de8-3c13-9516-4cc6eba038a3 | -5.49481 | -40.54016 | 2026-10-08 16:20:00 | NPP-375 | INDEPENDÊNCIA | CEARÁ | Brasil | 2305605 | 23 | 33 | nan | nan | nan | Caatinga | 15.3 |
| 957f831e-c5c6-3fa4-bfe8-edfd1b38eb40 | -2.0705 | -46.57001 | 2026-10-08 16:20:00 | NPP-375 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 183b82f5-5d6d-332d-8e34-c382aa1b1a63 | -6.57188 | -41.6111 | 2026-10-08 16:20:00 | NPP-375 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 15.1 |
| 32ea4716-8868-33c4-af51-6f4e3612e4a4 | -7.85469 | -44.96249 | 2026-10-08 16:20:00 | NPP-375 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 48fd2307-f038-3964-92a4-6f3ba8c52599 | -1.19979 | -48.93122 | 2026-10-08 16:20:00 | NPP-375 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 3271bcb0-7d09-3a55-946f-9b943d85fce8 | -6.91605 | -41.23422 | 2026-10-08 16:20:00 | NPP-375 | BOCAINA | PIAUÍ | Brasil | 2201804 | 22 | 33 | nan | nan | nan | Caatinga | 5.7 |
| aa12b71c-4bed-374c-87f3-cb57a8f55be0 | -4.62676 | -42.75304 | 2026-10-08 16:20:00 | NPP-375 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 598b74ca-916d-3510-8c4e-fe559debfdfe | -4.77259 | -42.67778 | 2026-10-08 16:20:00 | NPP-375 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 13.5 |
| a875c506-3b72-30ab-afee-df72a8a76665 | -4.49392 | -38.94714 | 2026-10-08 16:20:00 | NPP-375 | ITAPIÚNA | CEARÁ | Brasil | 2306504 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 3baccf77-c0df-344e-8745-517f3db7c7e6 | -6.19668 | -52.87763 | 2026-10-08 16:20:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 20.7 |
| d1a7930b-ed4c-3913-afca-c94ef3cc23fb | -6.68522 | -41.76919 | 2026-10-08 16:20:00 | NPP-375 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 14.2 |
| 8b50cea2-c73d-33b8-b2db-e9308745202e | -4.37122 | -41.83278 | 2026-10-08 16:20:00 | NPP-375 | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 15.0 |
| 139ab84e-6617-3b96-aea0-2f635c0b8ded | -6.15209 | -43.38558 | 2026-10-08 16:20:00 | NPP-375 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 157fad83-8f05-3ba0-9c7e-2f52f60fe193 | -2.43636 | -49.6288 | 2026-10-08 16:20:00 | NPP-375 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 456f1b52-0c21-3c20-9f46-0c720df47ae9 | -6.9333 | -45.25994 | 2026-10-08 16:20:00 | NPP-375 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 16.5 |
| a0f8a03e-e288-33d8-9d86-b872d2fb2f03 | -3.30257 | -53.71144 | 2026-10-08 16:20:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 14.2 |
| d82b409a-5462-3621-bde0-2bec6ea37c1e | -6.38787 | -52.72333 | 2026-10-08 16:20:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 71b281fd-4e8b-3c71-94f5-5462898e8d1b | -6.23028 | -44.86135 | 2026-10-08 16:20:00 | NPP-375 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 50.4 |
| 6bb9696c-55db-3839-95ce-7cda27dcfbf6 | -3.00175 | -43.11284 | 2026-10-08 16:20:00 | NPP-375 | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 149a3531-1235-3c5e-a50d-d45d08811339 | -6.15844 | -52.64082 | 2026-10-08 16:20:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 30.1 |
| b222dd71-2eab-38bd-b0ac-1f3f4c8cbb8e | -5.26374 | -45.40895 | 2026-10-08 16:20:00 | NPP-375 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| b97a0812-a082-343a-a1a0-b4f442c80044 | -5.30392 | -45.72055 | 2026-10-08 16:20:00 | NPP-375 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 25.9 |
| d66dd5d4-8e6c-3844-af09-3e9c4878c085 | -6.12464 | -44.14124 | 2026-10-08 16:20:00 | NPP-375 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 0d2b74ef-f376-30e6-9075-e4ce192ffb17 | -7.17008 | -47.7995 | 2026-10-08 16:20:00 | NPP-375 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| a8287f8c-8f82-36d7-a8f7-c7f4e7f42219 | -6.84642 | -39.55485 | 2026-10-08 16:20:00 | NPP-375 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 8.3 |
| 42ae58a2-4660-3a74-b185-9dfcc1d78b34 | -4.51972 | -44.01555 | 2026-10-08 16:20:00 | NPP-375 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 4d8e781d-4fb4-3d42-99e0-d6121a7ac62d | -2.8466 | -54.13137 | 2026-10-08 16:20:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| a5a68b6f-8758-3d22-8a66-d907126e0cb9 | -7.23268 | -45.31905 | 2026-10-08 16:20:00 | NPP-375 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 24.1 |
| b1020efe-420a-3601-87b9-9973872f3e61 | -6.92953 | -43.66207 | 2026-10-08 16:20:00 | NPP-375 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 18.7 |
| 4fef3031-e68b-30b8-bc26-80a0441fc33d | -6.31789 | -43.49144 | 2026-10-08 16:20:00 | NPP-375 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 05e34079-844c-3c30-b80e-a5a0a244e0b6 | -5.10147 | -46.20222 | 2026-10-08 16:20:00 | NPP-375 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 79.6 |
| ff8a473d-3357-30f7-88ad-0a5e9efb3967 | -7.11368 | -40.69059 | 2026-10-08 16:20:00 | NPP-375 | FRONTEIRAS | PIAUÍ | Brasil | 2204303 | 22 | 33 | nan | nan | nan | Caatinga | 8.3 |
| 4e7d54bb-2238-3c70-a7d7-f5312a5ae871 | -1.41546 | -51.53256 | 2026-10-08 16:20:00 | NPP-375 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| f02172a0-91c8-3031-9b5b-675a1702f986 | -5.09883 | -46.21564 | 2026-10-08 16:20:00 | NPP-375 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 259.9 |
| aaa86f99-13e0-38bc-9408-c95032fee567 | -6.8883 | -43.70611 | 2026-10-08 16:20:00 | NPP-375 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 30.9 |
| 38dbe7d5-e7a1-394a-8111-eecd4c97eb75 | -3.18137 | -50.59328 | 2026-10-08 16:20:00 | NPP-375 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 44.0 |
| a047313e-6026-3b6d-9912-7e67ccc5fc5a | -5.39759 | -45.6536 | 2026-10-08 16:20:00 | NPP-375 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 2a9ee687-e3a0-3fb7-a532-a7148b1e7810 | -7.26871 | -44.21838 | 2026-10-08 16:20:00 | NPP-375 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 15.6 |


[Clique aqui para ver as próximas entradas](README280.md)
