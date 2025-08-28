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

## Dados Diários - Página 42

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 019e1c66-479a-38b0-a9e6-c61873cd146b | -13.46002 | -46.98265 | 2025-08-28 04:08:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 3ce60db6-ae06-3e20-9430-3e3cf27cc0c5 | -11.10355 | -44.75034 | 2025-08-28 04:08:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 48534ef6-3401-3073-a354-c368a3b0d289 | -12.79847 | -48.14642 | 2025-08-28 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 7e75d1fc-e1b1-3d05-8055-1e60dfd30144 | -7.6002 | -43.94585 | 2025-08-28 04:08:00 | NOAA-20 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 50806bf8-1e58-3890-aa61-c155154ccd48 | -8.89111 | -44.40112 | 2025-08-28 04:08:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 181d7365-bdda-3589-82d7-49d25661fe47 | -12.71511 | -48.16771 | 2025-08-28 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fbef1bf1-c925-39a0-a173-73b37e4d4f61 | -8.27971 | -45.16494 | 2025-08-28 04:08:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 42.3 |
| 5a950a98-511f-3b4b-94ab-bb0ffb8b5b43 | -11.34554 | -43.54922 | 2025-08-28 04:08:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 0356199e-47a3-3bd6-821b-172210d5d60a | -12.8964 | -44.64172 | 2025-08-28 04:08:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| be805517-5c4b-3b45-9510-dc05eb2d4434 | -13.43497 | -46.9726 | 2025-08-28 04:08:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c3361836-b38b-3a93-bc56-13f8bf8276ed | -13.17688 | -45.28458 | 2025-08-28 04:08:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9d80c6df-ab6f-31e3-a956-1559e4fd3bb8 | -12.80971 | -48.12966 | 2025-08-28 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3f261767-7807-3a0c-bfa0-5578b8c562bf | -8.27334 | -45.1809 | 2025-08-28 04:08:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8b7cdaef-e3d8-31a8-9219-2d8389f2bb8f | -8.27902 | -45.16908 | 2025-08-28 04:08:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 141.5 |
| 5804c039-a797-309f-a62a-dc35dd477097 | -12.44086 | -48.71531 | 2025-08-28 04:08:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0c40c61c-1dff-3387-a6a2-1b0cb745d103 | -13.55246 | -46.90088 | 2025-08-28 04:08:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e4680b14-1fb1-3d38-ad0f-7a50410ae726 | -11.10011 | -44.74975 | 2025-08-28 04:08:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d62b8974-0ed2-32a4-a6fc-c65a957dc5c5 | -13.5451 | -46.89945 | 2025-08-28 04:08:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2a80e2d2-8197-365a-b06c-e414f6d2492e | -8.88392 | -45.72427 | 2025-08-28 04:08:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 03684e74-078a-364c-bc5e-f47126787b6e | -13.66755 | -46.90812 | 2025-08-28 04:08:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7b4bbcc2-97a7-3425-aa6f-2748661ecb02 | -13.62288 | -48.24258 | 2025-08-28 04:08:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c0cd8bd8-4d28-33e2-b43c-e5c0abccbb17 | -13.41808 | -47.0038 | 2025-08-28 04:08:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 0ea06a61-3464-32c9-ba75-4f4a611151d6 | -11.55456 | -46.34007 | 2025-08-28 04:08:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 25c927a5-25f5-3689-a870-2593f345f28b | -8.27195 | -45.18924 | 2025-08-28 04:08:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2b5dc8fb-4491-3893-a89a-63b47b61e9db | -8.30049 | -45.15134 | 2025-08-28 04:08:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4e6855c4-6dad-36a0-a7ef-fbeba821478d | -11.92689 | -46.70513 | 2025-08-28 04:08:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8676d53a-03c6-3675-a88a-90d6b71c1584 | -10.32446 | -46.78558 | 2025-08-28 04:08:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 4bff3276-e30c-37cc-99fd-dd45edc3026b | -8.27265 | -45.18506 | 2025-08-28 04:08:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2592feae-3076-3c77-9e8c-7f1a150b5a4e | -8.30339 | -45.15614 | 2025-08-28 04:08:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 65beee6e-f550-3712-8501-b4b18b2d6df2 | -13.5264 | -46.91944 | 2025-08-28 04:08:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 67565f32-c35a-376d-b471-8961d29a8bd6 | -12.94834 | -46.33398 | 2025-08-28 04:08:00 | NOAA-20 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 141a845d-c4b3-3b94-a08c-7f26516238fb | -14.84701 | -42.79395 | 2025-08-28 04:08:00 | NOAA-20 | ESPINOSA | MINAS GERAIS | Brasil | 3124302 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8713c39d-10ec-35ae-b68b-5bc605c688da | -11.83654 | -46.80008 | 2025-08-28 04:08:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7a29c1f3-c768-3dca-bf5d-55a1d5f086c3 | -11.33014 | -43.54321 | 2025-08-28 04:08:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5970eb5e-eff4-3b87-8e8f-a1a964a7d869 | -11.34164 | -43.55222 | 2025-08-28 04:08:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 14.5 |
| c7d35337-f9e6-3fd4-9139-73c8d968c781 | -11.24867 | -44.97424 | 2025-08-28 04:08:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| acb017a0-fefc-307c-afd6-18671659e7c4 | -13.44473 | -46.84994 | 2025-08-28 04:08:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7817b93f-b6ba-3f91-a4f1-fb4d55f673e6 | -8.28301 | -47.21709 | 2025-08-28 04:08:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| ee821a26-4412-3581-8118-fc2207f22be6 | -13.39006 | -51.75264 | 2025-08-28 04:08:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5c043c9d-65bd-380a-a9e4-359f56bc3719 | -13.37657 | -51.76815 | 2025-08-28 04:08:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a69e679f-c9b2-36e6-a94c-3abd27b6d30e | -8.19494 | -43.59166 | 2025-08-28 04:08:00 | NOAA-20 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 55c37d97-8d15-365c-a8ca-6b341b27aed3 | -12.77798 | -48.16844 | 2025-08-28 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5746ee8d-ef5d-3cd8-a90a-619cb7dffb16 | -12.9512 | -46.33899 | 2025-08-28 04:08:00 | NOAA-20 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bcc2c901-fbd2-397d-be00-ff026d83d6d4 | -7.23802 | -45.42971 | 2025-08-28 04:08:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| f7367581-ef74-3778-aa36-0c5346890736 | -13.37244 | -51.76984 | 2025-08-28 04:08:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 04a9f55a-a464-3b64-b24d-a6fde5c50984 | -12.88756 | -48.11809 | 2025-08-28 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a0969bea-9719-34ea-8f03-818e32a365ba | -11.21845 | -55.05621 | 2025-08-28 04:08:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 316f8f69-3632-3b96-91ac-a9e842f84006 | -13.45929 | -46.98691 | 2025-08-28 04:08:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| f4a37c31-6469-31d7-abf9-cbd42c11593d | -13.49341 | -46.85401 | 2025-08-28 04:08:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7147e2e8-acbf-3834-aef2-909c94b7dddb | -8.46189 | -43.69444 | 2025-08-28 04:08:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d0ee85e5-ab67-377a-832d-6c8898134e9e | -12.25303 | -45.05708 | 2025-08-28 04:08:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9608557b-18ed-3e9e-a665-69e6f93999b2 | -12.79458 | -48.16843 | 2025-08-28 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 094650f7-f448-3763-8181-303abb2633cd | -13.42342 | -46.9951 | 2025-08-28 04:08:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b949280c-81a5-341f-b25f-4a268523b68a | -8.28846 | -45.17919 | 2025-08-28 04:08:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b48fe570-3ac7-3abc-a73d-e5f8ccebd665 | -12.92482 | -46.31295 | 2025-08-28 04:08:00 | NOAA-20 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4ee41312-aaac-3885-acb1-cd77adf0deca | -9.86345 | -44.69064 | 2025-08-28 04:08:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 932328a2-1a04-3789-ab4b-ab1aac693c59 | -8.29689 | -45.15074 | 2025-08-28 04:08:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 27.1 |
| 6270d669-2c8a-389c-9868-bd9478c081af | -11.33907 | -43.5301 | 2025-08-28 04:08:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 39ee9764-5eb5-3c7a-9355-466564e80304 | -13.43666 | -46.9628 | 2025-08-28 04:08:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 9.7 |
| e3784964-16b8-3298-bc47-0ff4f81332f7 | -12.43638 | -45.96148 | 2025-08-28 04:08:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 95b48fc5-713a-3a38-803c-0f54f6e62494 | -13.60536 | -48.22566 | 2025-08-28 04:08:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5296fd89-4275-30fb-8e31-04a5900c9680 | -13.61545 | -48.23813 | 2025-08-28 04:08:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a53de188-a9b9-3391-a291-9ac942f35698 | -13.08312 | -46.33419 | 2025-08-28 04:08:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 29d2ebd4-62ce-3047-b4e6-9c4fa8e45240 | -7.44361 | -46.13174 | 2025-08-28 04:08:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8137199c-8474-3676-b881-eda85514a016 | -11.31796 | -43.5339 | 2025-08-28 04:08:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7829e1ff-fda9-34e7-8d53-3afa82944c21 | -11.3407 | -43.5413 | 2025-08-28 04:08:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 063eb131-1c16-37d9-882b-3bf9238ff11c | -11.34497 | -43.55277 | 2025-08-28 04:08:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 04c1516e-1f49-3511-a98b-1077d9c0defb | -12.79928 | -48.16534 | 2025-08-28 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 33e1a455-e66f-3439-8df9-2ac89f5ac318 | -8.2955 | -45.15909 | 2025-08-28 04:08:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 766b572e-4916-39ca-98f4-19bf0038ebe8 | -10.37132 | -45.16802 | 2025-08-28 04:08:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b95f5ad7-1ffb-35b0-afff-8448ee8b1f66 | -8.08542 | -44.98129 | 2025-08-28 04:08:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9989b298-da18-38ee-aef5-e4b6afdc792c | -13.43245 | -46.9872 | 2025-08-28 04:08:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| b2f02117-44c7-3650-ab48-6adffbedd7b5 | -13.41364 | -46.85386 | 2025-08-28 04:08:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 9.0 |
| b36d593a-4116-35f1-a591-c5d3f6eeb8aa | -11.23638 | -55.0645 | 2025-08-28 04:08:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 33577b28-c87e-331d-87a5-260603b884db | -13.43368 | -46.84795 | 2025-08-28 04:08:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 2f6361a4-133c-3d5e-bd0f-22be87942dd9 | -13.51006 | -46.86052 | 2025-08-28 04:08:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 35615a15-5053-3bfc-b5a8-746610ab6745 | -13.61882 | -48.24224 | 2025-08-28 04:08:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 56632998-3392-3848-9023-8c3e36d50b15 | -8.45822 | -43.65245 | 2025-08-28 04:08:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ffd235e8-a413-39d1-ba8c-b01f65dcca46 | -11.79661 | -46.807 | 2025-08-28 04:08:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 76b0b94b-7c76-37ce-a4e4-7307634d2c25 | -13.61953 | -48.23831 | 2025-08-28 04:08:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 8c978dc8-fc8d-34d9-8629-5ce0a88fadac | -6.48766 | -53.39651 | 2025-08-28 04:08:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1f4d9297-b253-3f0d-b3de-aeaa9f7bef7d | -11.32129 | -43.53445 | 2025-08-28 04:08:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cceee0fe-e969-30d3-88fc-fde61e7b0833 | -13.08253 | -46.31602 | 2025-08-28 04:08:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3fa80d44-b11b-35b0-9bc2-c30882aa447d | -13.18657 | -45.29022 | 2025-08-28 04:08:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3ad4c9ef-3726-3ec1-a5fd-ec8db7043324 | -13.61299 | -48.19489 | 2025-08-28 04:08:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 136e8cac-d337-381f-a7d9-ac5a1afa2cbe | -11.93077 | -47.13611 | 2025-08-28 04:08:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9f5757d4-c441-3183-9e43-32157add0b62 | -11.06616 | -44.59228 | 2025-08-28 04:08:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ca758528-89d2-3972-9542-c627c5d85d2d | -12.67965 | -48.18029 | 2025-08-28 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 8631676c-e9d9-3ea8-9b1b-02e10e077610 | -10.53445 | -46.71407 | 2025-08-28 04:08:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a716d967-f8ee-3626-ab49-910dbd67d6dc | -8.2501 | -45.14274 | 2025-08-28 04:08:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 225ef1f5-012b-3a9d-b739-24523bf5353b | -12.86044 | -48.10807 | 2025-08-28 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c1b9ea6f-a414-373d-8adf-8d71db06d4dc | -9.45661 | -51.95432 | 2025-08-28 04:08:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 035a23b6-020e-36c1-83d4-7abca6e71c39 | -12.78133 | -48.1729 | 2025-08-28 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3eb63d40-77c3-3755-a7c6-7299d705c178 | -12.67493 | -48.18344 | 2025-08-28 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f1cb445f-c76e-317b-bd8a-f9cf500dbca5 | -10.52763 | -46.70809 | 2025-08-28 04:08:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3aff091b-db39-3a73-b601-1a1fb0c36eb4 | -8.09271 | -45.00389 | 2025-08-28 04:08:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 1b4558c2-5066-339c-925b-a8ff4dfe4b8d | -11.83199 | -46.80402 | 2025-08-28 04:08:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bea6a3a3-9ffb-3391-8caa-cdb5bf9dc494 | -12.86703 | -48.11736 | 2025-08-28 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3b8795fc-df53-3107-b100-27bc56e6d428 | -11.31657 | -43.28658 | 2025-08-28 04:08:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 81667c63-511f-363b-9145-60f0b8334e14 | -13.60069 | -48.22868 | 2025-08-28 04:08:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |


[Clique aqui para ver as próximas entradas](README43.md)
