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

## Dados Diários - Página 85

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0bb286ec-c983-3071-8ab3-69ea87de399b | -11.95317 | -58.72897 | 2025-09-04 05:18:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3fb9797c-6a04-38b3-8c8c-faafd700ee3e | -12.18397 | -53.89034 | 2025-09-04 05:18:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3381ed09-4262-30b8-91d1-48bcd7160644 | -15.02633 | -48.11133 | 2025-09-04 05:18:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 1e8739f6-65e3-3190-96e2-ff8b639eff80 | -13.30361 | -46.8467 | 2025-09-04 05:18:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 55932567-6333-30ae-9b1f-9951860dce2b | -11.87579 | -51.53566 | 2025-09-04 05:18:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5b6912ff-f1b9-3d65-aaf4-59ed5ac4d917 | -11.5821 | -52.11626 | 2025-09-04 05:18:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3e1bc3a4-ce60-33c0-b9a5-396032a18a7a | -15.05565 | -50.04345 | 2025-09-04 05:18:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d3585058-5ad8-3386-b295-f358d3861a34 | -11.65107 | -54.52663 | 2025-09-04 05:18:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 32b827fc-9cb5-3155-a36b-3995cd7b14af | -11.63653 | -52.19706 | 2025-09-04 05:18:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3cc5c1d1-9ebf-3d30-aeab-0c559903229e | -11.86189 | -51.43758 | 2025-09-04 05:18:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b41fe0b2-aa7c-357f-83e5-d07e3690c013 | -12.63924 | -57.00516 | 2025-09-04 05:18:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3a1e6aa4-515b-342d-8e89-e3dedf9a0e4f | -14.81983 | -48.33208 | 2025-09-04 05:18:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 731bf4bd-c543-3f1b-97a7-4d4f9f872e87 | -15.02669 | -50.03403 | 2025-09-04 05:18:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| dd6e1cf2-1a3b-3ad3-8f7c-e8ade8f8581c | -14.75375 | -48.09157 | 2025-09-04 05:18:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 82ec5094-75dc-3a9d-a650-3961698e5bfc | -14.81236 | -48.33202 | 2025-09-04 05:18:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4b136cab-3fea-38b4-990e-c4bd1e050c80 | -14.53943 | -48.06643 | 2025-09-04 05:18:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 97c3287d-3cf1-372f-82d9-65debe8c6f90 | -12.49393 | -53.84807 | 2025-09-04 05:18:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 867a031a-5572-3aba-a7db-e099d93f2b22 | -11.8512 | -51.43871 | 2025-09-04 05:18:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c7161602-3c11-3898-922c-70233322a032 | -14.55916 | -48.07051 | 2025-09-04 05:18:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 9ea0104c-6ba3-3c70-8564-10f6d652da08 | -11.67939 | -57.34882 | 2025-09-04 05:18:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 24b8323f-1a86-3ced-9797-9a45a5c888be | -15.98707 | -55.98208 | 2025-09-04 05:18:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 4a62b235-a72c-309e-bbaf-a35d3819edf0 | -15.04978 | -50.04227 | 2025-09-04 05:18:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| dc9a8409-b5c3-3d4c-861e-ab8037fc4833 | -12.49184 | -48.07322 | 2025-09-04 05:18:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f0900961-6803-3925-b3d8-3f54fee2f5aa | -12.63621 | -57.00027 | 2025-09-04 05:18:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8f8c5578-2ff2-3736-a00b-f6becae83680 | -12.64353 | -57.00132 | 2025-09-04 05:18:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5639d3ab-2b23-35df-826a-5baf6ffc23a5 | -12.60333 | -56.99535 | 2025-09-04 05:18:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d76a14f6-c8a6-396f-9167-1ec018be74f6 | -12.52591 | -53.81135 | 2025-09-04 05:18:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 14b52ce7-7395-3a00-8e2b-21d262b5fad2 | -16.5362 | -55.08633 | 2025-09-04 05:18:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| d22cb571-71b9-3923-944b-d37af1d28ba5 | -13.57874 | -48.12931 | 2025-09-04 05:18:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2e3a8b0b-1acc-3ff5-8189-8803fe30f47b | -11.64349 | -52.19984 | 2025-09-04 05:18:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dcc279a8-bdee-3ce2-9185-68cea4130b57 | -11.91416 | -46.65519 | 2025-09-04 05:18:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5c15251f-b67e-300f-a851-fba6488d5696 | -15.01443 | -50.03635 | 2025-09-04 05:18:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 70cd7ab4-b691-3c8e-9b6a-de4a9e762a0c | -12.64113 | -56.99208 | 2025-09-04 05:18:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0298849c-18ef-3586-b04c-9b56448adc0d | -14.81151 | -48.2212 | 2025-09-04 05:18:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| c97136a7-153a-36f5-870b-d3d69a5b05b3 | -13.84986 | -47.98691 | 2025-09-04 05:18:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3146f9ce-5ddc-3e3a-a5d1-3dfe1dc94b6c | -12.87993 | -48.02321 | 2025-09-04 05:18:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5dbed876-8475-374d-88fb-c16fbf2dc8a5 | -12.90976 | -56.93731 | 2025-09-04 05:18:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 700a1ee3-e790-30d9-89b8-6e01e458f0ad | -11.86152 | -51.52423 | 2025-09-04 05:18:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 92a92cb3-d25d-30e3-836a-0aec767cee1d | -11.8754 | -51.53873 | 2025-09-04 05:18:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 88cbb814-e486-31e4-9947-5f3425be4b0e | -11.88454 | -51.5492 | 2025-09-04 05:18:00 | NOAA-20 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ac8db546-b9c8-3568-a3d6-22a7f075e9cb | -14.56887 | -54.55093 | 2025-09-04 05:18:00 | NOAA-20 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 48b80c88-560b-3571-9ccf-8f2347081d23 | -13.81181 | -56.60887 | 2025-09-04 05:18:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3cdaca2c-bd1c-3f43-b597-b8464adc56fc | -14.75437 | -48.08566 | 2025-09-04 05:18:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6843717e-704a-3d6a-abad-e9bacd72cbf2 | -14.20153 | -48.08605 | 2025-09-04 05:18:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a560861e-6e99-32a0-897f-f088cbddcc42 | -12.95345 | -48.06638 | 2025-09-04 05:18:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 453fabc5-51e0-3690-9c15-b10f8f6a1a9b | -11.59208 | -47.76165 | 2025-09-04 05:18:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 053cd805-1c74-38b0-a5e8-b2fa101be090 | -15.30386 | -52.7688 | 2025-09-04 05:18:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| bbdf52b4-17d5-3b79-9fde-b528354f5ff1 | -11.63086 | -52.20205 | 2025-09-04 05:18:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2f343c49-a6ed-3e96-8e12-adac636b23a2 | -14.05755 | -54.0314 | 2025-09-04 05:18:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0d216f87-3e68-3f22-aa1b-3c699bc8c8c6 | -16.55138 | -55.1055 | 2025-09-04 05:18:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 33a1789c-9107-3b8a-b2ed-5fe46f10e8d6 | -12.96575 | -54.76928 | 2025-09-04 05:18:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 326f3589-2958-3775-a458-cac514ecfb50 | -11.64206 | -52.21104 | 2025-09-04 05:18:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| fa9d4d22-f4d3-3fe4-8e30-78eab9531bdd | -14.77459 | -48.1478 | 2025-09-04 05:18:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 85aaac1f-580c-3cac-9426-5ebe63e9f789 | -11.8806 | -50.60593 | 2025-09-04 05:18:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b9081a56-33b9-38bf-ba0f-ae8ad57a6ad2 | -15.78647 | -48.19783 | 2025-09-04 05:18:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 05be5ac5-9269-3068-8cd3-6b8c81d0c2c0 | -15.30099 | -52.75122 | 2025-09-04 05:18:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1e7497aa-5244-3810-aff4-50cc0d012261 | -12.86637 | -48.01855 | 2025-09-04 05:18:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 3c8b4e46-f10d-31d5-89b8-85b683606486 | -11.6032 | -47.78001 | 2025-09-04 05:18:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| afaa077a-6ecf-360e-9bc0-55a6b98c6d4d | -12.86674 | -48.02272 | 2025-09-04 05:18:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 73a83546-8178-357c-b967-061b6e845aa6 | -14.30003 | -53.08736 | 2025-09-04 05:18:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0a8500df-21e9-38ed-bebd-275c0d550af7 | -15.30573 | -52.75859 | 2025-09-04 05:18:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d8addad6-4c1e-3d89-85c9-685f312b0115 | -15.30214 | -52.74612 | 2025-09-04 05:18:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1d1e63db-efaa-3750-ae93-c8e9acf5ccac | -13.81491 | -56.6142 | 2025-09-04 05:18:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a2c3516b-3d7a-3e85-b4d6-21ee8552f767 | -11.58776 | -52.11135 | 2025-09-04 05:18:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| acd6130e-b09e-385c-abc4-ad93bc4e8939 | -12.91021 | -56.9389 | 2025-09-04 05:18:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| d8d0646b-c583-39bf-aa27-0a6ce1aaadf7 | -13.86429 | -47.97736 | 2025-09-04 05:18:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f8476a19-66a9-343a-96f3-69f9ae2fdd24 | -12.91944 | -57.00155 | 2025-09-04 05:18:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b78edd44-9f7e-3a1c-9e80-a8ccceddb9f0 | -11.19401 | -55.01848 | 2025-09-04 05:18:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2f971b30-2ad4-3247-9a7e-d5c08a3660a6 | -12.8673 | -48.01786 | 2025-09-04 05:18:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 1e746bbe-cc79-39b7-94c8-ad4be6353270 | -15.03948 | -50.08091 | 2025-09-04 05:18:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a3ce9a1e-cd75-309a-ae6b-374089785bc6 | -11.16687 | -55.0362 | 2025-09-04 05:18:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 091f63f6-d4ba-37c1-99be-a2d07a9f1057 | -12.17897 | -53.89421 | 2025-09-04 05:18:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 61465bc1-fc7e-3592-834b-95661502a08e | -15.02584 | -50.04171 | 2025-09-04 05:18:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 4613b7f0-af18-3da4-9194-080a11ae1df2 | -11.63161 | -52.19645 | 2025-09-04 05:18:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a45c20c6-8567-3755-8979-fadfb60f236f | -15.15251 | -52.37599 | 2025-09-04 05:18:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 574a2b5f-617c-34c5-9f6c-cfb21da0f9c3 | -11.58282 | -52.11069 | 2025-09-04 05:18:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| bd1fccf5-3208-34e6-8e9c-048a0ab4f224 | -12.88753 | -56.93989 | 2025-09-04 05:18:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| fc47f203-c8b0-3b6a-95ee-8f9f951f60fb | -13.10829 | -57.1158 | 2025-09-04 05:18:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 93f3967e-a286-3dc2-81eb-bb910b32cce9 | -15.9859 | -55.95943 | 2025-09-04 05:18:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 115ddde5-963b-38e4-b8f2-b2bad4b21d12 | -10.88367 | -55.73705 | 2025-09-04 05:18:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fcfb8601-0f42-3158-969b-c1284a5fc0de | -12.90855 | -57.00131 | 2025-09-04 05:18:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 47c3ca9a-06eb-32ae-b658-e2469eec1534 | -11.59178 | -52.15739 | 2025-09-04 05:18:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| abede16f-4b54-3fb9-b931-47f60a3ad053 | -12.88929 | -56.95364 | 2025-09-04 05:18:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 08e6097c-7bd9-32c8-a9f9-21a782339cdd | -16.30785 | -52.96492 | 2025-09-04 05:18:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 95be869c-f597-35af-98a6-0000ba954748 | -14.57174 | -48.05315 | 2025-09-04 05:18:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b404b318-3905-397c-820c-9f5d4c644fc3 | -12.48531 | -48.07281 | 2025-09-04 05:18:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 891f65dd-fada-34f0-91db-f0d097968ba5 | -11.67583 | -57.34828 | 2025-09-04 05:18:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 2a5c0357-0b39-3071-bb4b-b2153cdb152c | -12.6405 | -56.99644 | 2025-09-04 05:18:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 70110e98-a5db-34ad-b169-f982e952c807 | -11.73182 | -47.75066 | 2025-09-04 05:18:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 268d5dfb-fb2f-3107-8d30-57e70f274a40 | -11.59603 | -47.78469 | 2025-09-04 05:18:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| f2dd8834-2e09-35a9-b7be-2aa5c786771e | -12.90915 | -56.94171 | 2025-09-04 05:18:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| b28fac5d-b7f4-3639-9172-399caf7eed9c | -14.55927 | -48.04336 | 2025-09-04 05:18:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| dcef5225-0854-395d-9e33-03efffbff30b | -12.88689 | -56.94429 | 2025-09-04 05:18:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e6f19972-f750-30d7-8c63-784a77b4c921 | -11.63365 | -52.19869 | 2025-09-04 05:18:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 97a06411-6d17-3638-b6c7-6e1923316c75 | -12.97144 | -54.79021 | 2025-09-04 05:18:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 337c0890-2d7c-346d-8d43-5dce416db968 | -15.15361 | -52.36661 | 2025-09-04 05:18:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b778c85f-be38-3c57-a2eb-7d7c6418560b | -15.41324 | -55.93372 | 2025-09-04 05:18:00 | NOAA-20 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 63338b56-8672-3324-b453-0958060cee14 | -12.49831 | -48.07415 | 2025-09-04 05:18:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 10.3 |
| b4a055e0-9542-3930-8e78-cc69c479d8f4 | -15.6161 | -52.88683 | 2025-09-04 05:18:00 | NOAA-20 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| da579682-666e-3ae8-b785-86b852358dfc | -15.54863 | -48.40356 | 2025-09-04 05:18:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |


[Clique aqui para ver as próximas entradas](README86.md)
