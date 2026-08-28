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

## Dados Diários - Página 49

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 94c20321-f2c8-32fe-bc4b-851db00ea2a8 | -6.76137 | -46.14043 | 2026-08-28 05:10:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 544b2562-2bc7-3eb5-b10c-d5c0d8dd14c8 | -6.13191 | -53.5279 | 2026-08-28 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8a9bfe78-2866-335c-908b-72a3ad961948 | -6.49028 | -53.5007 | 2026-08-28 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8911c059-c02b-3cb6-8c13-5808c1410a91 | -6.11823 | -57.68686 | 2026-08-28 05:10:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d3ed6b6e-5338-318f-a81a-5f0d8a1544aa | -10.55016 | -50.47921 | 2026-08-28 05:10:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ab31780a-e206-3e8a-8f5e-b159d0c65df5 | -8.23796 | -54.97222 | 2026-08-28 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ed235427-1d9f-3ebe-a235-cac403fed724 | -9.0797 | -53.0383 | 2026-08-28 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| da7c399f-f32b-37d5-af50-14de77523104 | -6.55976 | -56.54964 | 2026-08-28 05:10:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4439067a-3518-3d88-aab3-acc5d708908f | -6.37346 | -54.95383 | 2026-08-28 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 129c3751-6a1d-32d3-8a9d-c51682ea3d5d | -9.65786 | -48.30025 | 2026-08-28 05:10:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e460e272-385a-30ac-b18f-4b3ecae531f5 | -8.5986 | -54.79158 | 2026-08-28 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 88f578a6-79d2-3e2c-871f-54986719f161 | -6.24742 | -55.43235 | 2026-08-28 05:10:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5b6e01d2-87c3-389e-a9dd-eaaa95215ea6 | -6.53153 | -55.24507 | 2026-08-28 05:10:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 6b00f3f0-0995-3281-b5dc-e6a89baf2047 | -4.96263 | -56.27383 | 2026-08-28 05:10:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0c957e87-ddfa-374e-a659-fc3aafa6aac8 | -9.22268 | -51.54627 | 2026-08-28 05:10:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 47bb813a-d30f-358f-8f73-81112476fdb8 | -8.59131 | -54.70351 | 2026-08-28 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6ead783b-cd46-3a8f-8da7-33d046b6cbf2 | -8.59183 | -54.7679 | 2026-08-28 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0e3138be-ef29-3274-b6bd-4f22ab395ef1 | -6.22431 | -55.42871 | 2026-08-28 05:10:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5e6ff77b-5d93-33d0-8085-02eec055791a | -6.13074 | -53.53556 | 2026-08-28 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b182862c-d2cc-368a-ae29-b39f96864a43 | -9.43744 | -51.69875 | 2026-08-28 05:10:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 307fd1dd-f6ee-379d-99c4-02ab0cb0104e | -8.59012 | -54.77892 | 2026-08-28 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 799ea1f6-adee-360a-a897-efb861447f54 | -6.2365 | -53.48378 | 2026-08-28 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c5558cd7-bf3d-3e2c-8260-d039cdec5d27 | -8.93393 | -50.71557 | 2026-08-28 05:10:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 16762b44-06fa-374b-a44e-4f63faee1df9 | -5.87303 | -52.18668 | 2026-08-28 05:10:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 213aab84-5970-3632-91e9-7427fc026755 | -6.16752 | -57.79312 | 2026-08-28 05:10:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 31d913e2-253d-3065-aaeb-d23b86241d55 | -6.00075 | -57.82737 | 2026-08-28 05:10:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1e63dd85-d8c8-3e2c-a081-6170d000a5bc | -9.45953 | -51.71609 | 2026-08-28 05:10:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6726092e-5088-3540-91ad-62c4259f40e9 | -6.37291 | -54.95736 | 2026-08-28 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f63a9e68-12dd-3cab-9b14-93851af1ccc4 | -6.15951 | -57.7994 | 2026-08-28 05:10:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ec2b3c70-8c34-3fcf-9976-b8828b344896 | -6.75711 | -55.69064 | 2026-08-28 05:10:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 7736e89c-6389-3d38-ab97-ed43d84013d7 | -5.91869 | -52.1231 | 2026-08-28 05:10:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5bc28d03-b8b4-3804-a2fb-607c80b9ebe4 | -9.23538 | -51.54393 | 2026-08-28 05:10:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 30e17517-7a33-3f71-acb1-c7658708c066 | -6.51768 | -55.24648 | 2026-08-28 05:10:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 86a8b863-e03f-3437-8bae-b19a529d5490 | -8.95088 | -50.18128 | 2026-08-28 05:10:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| da6e6dba-c2df-31c4-a08c-e383b27835b3 | -7.49543 | -55.33474 | 2026-08-28 05:10:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4d38e27a-2e4e-3e08-b53b-d85206b085a2 | -6.5221 | -55.24001 | 2026-08-28 05:10:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5b883c11-26f8-3643-8b70-26802d8738d0 | -6.43052 | -54.93401 | 2026-08-28 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1544f6dc-622d-35ff-8daa-79283c203885 | -6.57932 | -55.43871 | 2026-08-28 05:10:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 26ae786e-f638-3c97-8bb7-9cffb7802f28 | -9.42989 | -51.69418 | 2026-08-28 05:10:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1b07a742-be10-3ca8-9f46-9e037a7a5a6e | -7.44468 | -50.92038 | 2026-08-28 05:10:00 | NOAA-20 | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9e039504-feef-3538-8052-464bd49874a6 | -7.2535 | -45.87006 | 2026-08-28 05:10:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| de866b53-85ce-3f4f-9f06-be9b8fd6a847 | -6.24806 | -55.47157 | 2026-08-28 05:10:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0a3648b3-59d8-38a3-bc42-74e9b254f09c | -8.56015 | -54.90542 | 2026-08-28 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8b64e1a9-4df4-3d25-b275-d573c0a4024b | -7.36914 | -55.51232 | 2026-08-28 05:10:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f4eb2822-e079-334c-99d0-0029a4de1249 | -4.19636 | -56.30588 | 2026-08-28 05:10:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6edef827-8df6-34f6-bd5c-d1ce005a03d7 | -8.59352 | -54.77945 | 2026-08-28 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d039bd0d-ebcb-39c2-b05a-718f1c70df0d | -6.1884 | -55.4195 | 2026-08-28 05:10:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bd5d5929-c475-3a89-8600-4578aeaa7cb1 | -6.521 | -55.24699 | 2026-08-28 05:10:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e2801d2e-ee67-3edd-b173-57ac7fce8ac3 | -5.98791 | -55.72159 | 2026-08-28 05:10:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3c0c187c-7fd5-348e-99ca-35f1ae53d298 | -8.50759 | -55.35455 | 2026-08-28 05:10:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d84563bc-04d1-34f1-8ae0-16100b61da26 | -10.55526 | -50.4152 | 2026-08-28 05:10:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0ab2e25d-b5a4-3f70-ad05-940717ced04d | -9.07906 | -53.04255 | 2026-08-28 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d45d4c7b-7ad1-3b8b-9257-6fe68a4c4864 | -6.63906 | -53.1896 | 2026-08-28 05:10:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 30fff7a2-2c88-35ec-b418-366377443b8e | -8.59238 | -54.78682 | 2026-08-28 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| bce5f594-13fa-3b6a-a44f-b7b74b3986ce | -6.24411 | -55.43182 | 2026-08-28 05:10:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 32e2885d-dcde-30bc-bc26-b5ec8cbdbd29 | -6.25455 | -55.40853 | 2026-08-28 05:10:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8e9f61e4-bd3c-350c-8bb7-33e3b25b69ae | -9.43491 | -51.68775 | 2026-08-28 05:10:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b22cceed-18a5-3888-be0d-73200150cb42 | -8.59071 | -54.75263 | 2026-08-28 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 09e6ff4d-9ba3-363d-b1f4-03328121a92d | -10.0608 | -46.94472 | 2026-08-28 05:10:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ec49d13d-b75a-3e33-ba08-731b401c99b5 | -8.55441 | -54.71679 | 2026-08-28 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 484446fb-20cd-3e69-84f5-a8e45d2eb018 | -6.52766 | -55.24804 | 2026-08-28 05:10:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 449f4c25-47f0-3f71-bcc9-d09119f3ece4 | -6.58209 | -55.4427 | 2026-08-28 05:10:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6d41d079-f1a8-32a8-918c-c2d8a84c8692 | -11.23736 | -45.04966 | 2026-08-28 05:10:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2855edb1-9e66-3a24-a2d9-6f385d06f693 | -7.26806 | -45.35706 | 2026-08-28 05:10:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 9c0f0a8e-d43e-346f-b31a-9f48dae9929a | -6.17412 | -55.46704 | 2026-08-28 05:10:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 8db5fb0c-78dd-362e-98c5-131c5e811f09 | -11.01691 | -45.07443 | 2026-08-28 05:10:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 8842287d-15e1-3020-968e-025dc2465019 | -6.96457 | -55.64541 | 2026-08-28 05:10:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 915f0ce2-7c27-35a7-882b-da36d4f00414 | -7.28339 | -49.94577 | 2026-08-28 05:10:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0c56397c-6f98-37e2-ac6b-0adbf6713965 | -9.22373 | -51.5388 | 2026-08-28 05:10:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b5b4b476-72c5-3f2a-b4f4-41d32a720c44 | -8.9477 | -50.17209 | 2026-08-28 05:10:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 94ef7cd5-cb70-31a6-8435-066f4fa60c2b | -6.16188 | -57.78465 | 2026-08-28 05:10:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3a31f184-5287-3580-bf3c-3a5624424105 | -10.00847 | -46.41991 | 2026-08-28 05:10:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f203fb9d-45f3-381e-a067-04bf6e43afd6 | -7.87333 | -46.10129 | 2026-08-28 05:10:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| ac6138ac-f290-3e08-a31c-44cd7c41483a | -6.13888 | -53.52898 | 2026-08-28 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7aa278ae-208e-311c-838a-e8f7bef3a54e | -6.76265 | -55.69862 | 2026-08-28 05:10:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9601fde9-e4d0-3680-8c0d-93ab8b583f79 | -6.27797 | -53.13853 | 2026-08-28 05:10:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5d57e86a-2fe3-34e2-a1f9-c245279dbcd8 | -6.64973 | -53.19119 | 2026-08-28 05:10:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5f8c3e46-4317-3847-8f41-7409426a2c9d | -6.25842 | -55.40557 | 2026-08-28 05:10:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c75da3b8-3619-353f-bbef-639b1357a663 | -4.19303 | -56.30534 | 2026-08-28 05:10:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 879dff4a-b1cc-37d3-9309-b2e29c1ebafe | -8.77905 | -50.06645 | 2026-08-28 05:10:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ebbb5c44-c98a-3795-a1b6-b7af04239f9d | -4.84422 | -45.39168 | 2026-08-28 05:10:00 | NOAA-20 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 8a6c83d2-a83f-3699-9971-69144104cf9e | -6.47014 | -55.87225 | 2026-08-28 05:10:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6267e433-4917-367e-b322-a991ea051a10 | -9.38791 | -55.97781 | 2026-08-28 05:10:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 454e9fdd-d837-3be5-a79a-1950113ea3d4 | -7.37453 | -55.14932 | 2026-08-28 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| df73a6c5-5762-3e9d-91e3-589db8bc9760 | -8.08374 | -45.80876 | 2026-08-28 05:10:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b6519a51-4071-3d43-b44a-79a46b0b3942 | -9.45198 | -51.71164 | 2026-08-28 05:10:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2d72a078-1f8f-3ca8-99d1-8067f7a5e1f0 | -8.7785 | -49.94455 | 2026-08-28 05:10:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 23aabc95-0395-33f3-b8d6-9fd5fa411c0b | -8.80306 | -50.0815 | 2026-08-28 05:10:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5ac6943b-6294-3b97-8d22-378a7e0b9645 | -6.06287 | -53.77121 | 2026-08-28 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1097c566-a723-38b7-a737-6c4e3dcd2b92 | -8.21601 | -54.95787 | 2026-08-28 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6482009a-6391-3a27-86f4-ac39442928a8 | -9.05612 | -45.78037 | 2026-08-28 05:10:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e4f3e25e-0233-340b-a0a7-8dcc6bcb0efc | -8.17311 | -46.16356 | 2026-08-28 05:10:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e6cf3973-d0af-3610-8087-7e594fe7d203 | -6.27382 | -53.14198 | 2026-08-28 05:10:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 6b117f82-9e3e-3d9e-b7bd-02dab880ce1b | -6.24143 | -55.47052 | 2026-08-28 05:10:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 00174ac0-d06c-3873-bd8c-4fb780ecb179 | -6.22762 | -55.42923 | 2026-08-28 05:10:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fe1dc0e7-2cd2-38d5-8c5d-0a31e78dcbaa | -3.53438 | -59.02495 | 2026-08-28 05:10:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e9d476aa-eaf5-30fb-b51e-44fbfc1cfb05 | -6.27608 | -53.34176 | 2026-08-28 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9642b7f9-f50d-3c38-803d-92df04c2eaae | -9.61227 | -55.12212 | 2026-08-28 05:10:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| da2cf139-5aab-3484-92b8-86f2e8f81284 | -4.61454 | -56.17599 | 2026-08-28 05:10:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1faffedf-cda9-3e53-b11b-1b644ae5ddfc | -9.22329 | -51.57105 | 2026-08-28 05:10:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README50.md)
