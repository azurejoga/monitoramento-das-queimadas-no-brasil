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

## Dados Diários - Página 83

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ff8a7805-0d51-3b82-8979-709115c26ca9 | -6.33639 | -53.43235 | 2025-09-01 05:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a8805a04-5fff-3d67-b474-757e8c89ef90 | -15.69746 | -48.96524 | 2025-09-01 05:25:00 | NOAA-21 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 8c4f05d4-51c1-382f-b94d-fbea04211d95 | -6.33102 | -53.43658 | 2025-09-01 05:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1a47e9cd-df4d-3073-bdb4-67c20e3cf642 | -11.65198 | -57.35521 | 2025-09-01 05:25:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 42f4558b-8250-365d-9d58-8459c76cadb5 | -15.71104 | -48.89566 | 2025-09-01 05:25:00 | NOAA-21 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| b4683635-dd95-31e4-ae6f-c73ac16fc0e6 | -12.78328 | -48.08942 | 2025-09-01 05:25:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7e7c5c9f-bf37-3023-853f-c25bba3181ca | -6.83728 | -52.82013 | 2025-09-01 05:25:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 918a29ca-6827-3091-94bb-f67db53ef427 | -6.86573 | -52.79634 | 2025-09-01 05:25:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2eb1896a-e516-3f43-8380-7148bfa27a0d | -15.71877 | -48.88928 | 2025-09-01 05:25:00 | NOAA-21 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| c240f771-415a-32e8-b09e-adc59fa2129a | -14.42382 | -51.66718 | 2025-09-01 05:25:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 3b164a3a-0907-3b6d-9302-49fe7a0c7a63 | -6.43414 | -55.62093 | 2025-09-01 05:25:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 442f9de7-d55c-330b-883a-59e288a4f522 | -12.9754 | -48.11632 | 2025-09-01 05:25:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| ba3aab32-b826-3d87-b63d-b2f3a09335ca | -6.3324 | -53.42673 | 2025-09-01 05:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| cd22694a-4012-3613-9bf9-a4193fc94ebf | -6.82077 | -52.81706 | 2025-09-01 05:25:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 512fdd4f-69ec-32e0-910f-82b351332a35 | -14.42334 | -51.67142 | 2025-09-01 05:25:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| f63fc676-898d-3a23-9984-07cc5493b3be | -6.43465 | -55.61737 | 2025-09-01 05:25:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 33c8672c-1500-3ec0-96fd-ecdc69930597 | -14.02162 | -54.03143 | 2025-09-01 05:25:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5bf37364-178e-327a-aed9-780d2633c9cb | -5.8284 | -51.37817 | 2025-09-01 05:25:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6b69721f-d834-373e-be2f-22e369a0d1fa | -8.05958 | -48.41916 | 2025-09-01 05:25:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c7e5929c-4c8d-3bda-af71-907e49764fe9 | -6.8267 | -52.82407 | 2025-09-01 05:25:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 054e74f8-a43a-397b-ad18-56641be0fc22 | -6.85926 | -52.80662 | 2025-09-01 05:25:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 3a8c2c80-1a1c-3ade-b168-2db2daec3355 | -15.69275 | -48.93933 | 2025-09-01 05:25:00 | NOAA-21 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 36e17f20-53b3-3f89-9799-50b61ee7730d | -6.80185 | -52.8088 | 2025-09-01 05:25:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| e5618da4-fa8c-3178-b0ae-6dc2fe6c4731 | -12.60412 | -48.20865 | 2025-09-01 05:25:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 35424ed9-e8b5-3faf-98b8-b9552f929ff3 | -12.59934 | -48.22624 | 2025-09-01 05:25:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 1f6512fe-9627-32fc-a883-4b39cb41b196 | -15.69491 | -48.91582 | 2025-09-01 05:25:00 | NOAA-21 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 8.8 |
| e5eaeb10-6fe7-3272-bc17-61c56e54e3f5 | -6.85203 | -52.82254 | 2025-09-01 05:25:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| bf2a676e-1e16-32bf-aad0-c6ad7d40f374 | -15.69059 | -48.96268 | 2025-09-01 05:25:00 | NOAA-21 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 59e3b68c-a156-313f-9945-7eceac0eb154 | -12.56389 | -48.22126 | 2025-09-01 05:25:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 403d3c56-ce0e-3766-889b-d39c788d2566 | -6.43061 | -55.61679 | 2025-09-01 05:25:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ed562cfc-2183-38f9-9176-943240fdfb71 | -6.22296 | -53.57382 | 2025-09-01 05:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dea14766-a154-3796-8ff8-4785bd28c893 | -6.86419 | -52.80737 | 2025-09-01 05:25:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 8bb3a28e-e29e-30b0-bf27-4db311ca3ad0 | -15.70289 | -48.90666 | 2025-09-01 05:25:00 | NOAA-21 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 11.6 |
| d299fa68-18c8-3f68-9ceb-69db7c45ee4c | -12.96817 | -48.11606 | 2025-09-01 05:25:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f8d27962-54c7-3811-841f-e296435c6348 | -15.72837 | -48.99381 | 2025-09-01 05:25:00 | NOAA-21 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 32.5 |
| c15b88c7-dfe2-38b5-9762-cd878850d697 | -10.08822 | -68.47274 | 2025-09-01 05:25:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b1a60a66-55b0-36ea-9edb-f246a1c79626 | -15.73012 | -48.99556 | 2025-09-01 05:25:00 | NOAA-21 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 22.1 |
| 5cc67e74-6f9a-3f90-96cf-62738a985e76 | -6.8585 | -52.81209 | 2025-09-01 05:25:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| c314e73a-0fd0-3a1a-866c-b43fb56a3125 | -18.66467 | -52.5955 | 2025-09-01 05:25:00 | NOAA-21 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 921abdfb-e07d-3e5f-a5a7-d02cd998c52f | -12.60856 | -48.2065 | 2025-09-01 05:25:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| cf87f9db-6f4b-3354-9336-8d9b9bcf0c5a | -15.72419 | -48.98328 | 2025-09-01 05:25:00 | NOAA-21 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| e50ef07f-ea9b-33e9-93eb-1ad06bcc7979 | -15.69751 | -48.88751 | 2025-09-01 05:25:00 | NOAA-21 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 48906a39-08e9-31f6-9fd7-202da5ebe7cf | -12.43674 | -63.90865 | 2025-09-01 05:25:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 67dc37af-955e-3469-9bda-40d025f731ca | -12.42252 | -63.9101 | 2025-09-01 05:25:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 704eccba-0e4f-34e3-8b82-5d5c784b377c | -15.16186 | -52.34745 | 2025-09-01 05:25:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f1127657-5637-3740-a41e-6f868b7be838 | -12.5664 | -48.22482 | 2025-09-01 05:25:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 29ed7341-cc2b-315c-b76c-01e7f09c1295 | -5.82794 | -51.38158 | 2025-09-01 05:25:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 40c3c936-61b7-30fe-8aec-dd384fce2fbe | -14.45972 | -53.0528 | 2025-09-01 05:25:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 106aefa4-f08c-3fbc-a9f4-7c0035e3f9e9 | -16.20442 | -55.94968 | 2025-09-01 05:25:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 499659ee-0fb1-321d-892c-1c7ac99616dd | -11.52059 | -54.46795 | 2025-09-01 05:25:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| f53b883c-ef8f-343d-a099-9736df9c66be | -6.82251 | -52.81795 | 2025-09-01 05:25:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 2fc1ade7-791c-3dd9-9306-790616143239 | -11.96284 | -51.36104 | 2025-09-01 05:25:00 | NOAA-21 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 97feb35c-73c2-3b23-a9eb-ac64b522f2e6 | -16.15198 | -49.63568 | 2025-09-01 05:25:00 | NOAA-21 | ITAUÇU | GOIÁS | Brasil | 5211404 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| efb4ab5f-b217-3133-a456-353f1b424409 | -15.70508 | -48.88278 | 2025-09-01 05:25:00 | NOAA-21 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| e957f24a-89ef-33a4-9320-26b941a19b19 | -12.85273 | -48.08063 | 2025-09-01 05:25:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| b887ce1d-6dae-3d2c-b047-810135b33689 | -12.83116 | -48.07837 | 2025-09-01 05:25:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f1422d9e-9e49-33c2-a65a-ebb36b1b13fa | -14.317 | -60.34496 | 2025-09-01 05:25:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| a8147702-70a8-32e0-89e2-911b20f0c5d4 | -6.81682 | -52.82286 | 2025-09-01 05:25:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 22da22dd-5884-3793-bd5d-cc9adf5ac2ca | -11.59602 | -55.56017 | 2025-09-01 05:25:00 | NOAA-21 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 10f31e72-b951-30fe-a31e-990f3c964197 | -10.83945 | -61.46498 | 2025-09-01 05:25:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 73675041-784d-39fc-be86-0377a9f50563 | -12.8241 | -48.07632 | 2025-09-01 05:25:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0e32d51d-1104-3620-b623-762e0f9d5119 | -6.35117 | -55.56164 | 2025-09-01 05:25:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4d12848a-2905-35ab-bb5e-bf2b307ad4bb | -6.34108 | -53.43301 | 2025-09-01 05:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 62b847b5-0b7c-3adf-9746-084bc749d9d2 | -14.30956 | -60.34763 | 2025-09-01 05:25:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ddeae681-ed85-3f18-8f83-ef306088dc6e | -12.42181 | -63.9105 | 2025-09-01 05:25:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 14a21344-edc4-3d94-bda9-fcca23349ead | -15.69804 | -48.95901 | 2025-09-01 05:25:00 | NOAA-21 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| a3a636c1-df72-3886-8f0b-48838eda935e | -9.66363 | -68.97786 | 2025-09-01 05:25:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 442150bc-9009-3e8c-b0db-79fac6f40f7f | -6.47863 | -56.00719 | 2025-09-01 05:25:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 04955813-87b0-308c-a466-f0d2e9b39ea7 | -11.51524 | -54.47235 | 2025-09-01 05:25:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 9194da92-5937-3ab4-9b72-97ef723b5cd6 | -12.85369 | -48.07121 | 2025-09-01 05:25:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| a140a4d0-453e-3a2f-a164-d1080d0b88df | -10.09358 | -68.46887 | 2025-09-01 05:25:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 285b54a2-5ac8-3733-b161-0c84e32946eb | -7.38782 | -47.43782 | 2025-09-01 05:25:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 545367a7-b772-3a48-87b1-d51d5e4ec7d8 | -14.61148 | -48.93423 | 2025-09-01 05:25:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| e4de3598-2c5b-37c6-b4f5-82a1fb5d300b | -16.5122 | -55.03355 | 2025-09-01 05:25:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f726b241-4202-341e-8fbb-cd5788491d4d | -12.5724 | -48.20817 | 2025-09-01 05:25:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 1698d68f-836d-3153-9c2e-3b7630b46f81 | -14.58693 | -54.5372 | 2025-09-01 05:25:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| acdb6e71-1f43-3175-a6a5-6acff2752115 | -15.69216 | -48.94569 | 2025-09-01 05:25:00 | NOAA-21 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 68f92443-6fd7-323e-a76e-f7df7d074584 | -18.66426 | -52.59369 | 2025-09-01 05:25:00 | NOAA-21 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 2379da6d-b254-3708-99f5-85152cd41c26 | -11.65128 | -57.36009 | 2025-09-01 05:25:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 77cb1f75-7a87-321a-9f3e-01932b4e337c | -11.65587 | -57.3558 | 2025-09-01 05:25:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 6f60dc02-7db4-31be-b49d-75c8103d4343 | -10.27222 | -64.29679 | 2025-09-01 05:25:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 1ebd8049-987c-3911-8447-7522961be638 | -15.72299 | -48.99591 | 2025-09-01 05:25:00 | NOAA-21 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 7.5 |
| a616e1e8-6749-3ca1-a139-67eec48eaa2b | -11.88596 | -51.69894 | 2025-09-01 05:25:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a8e30e14-f819-34a2-bfb6-7b3eda864040 | -12.84561 | -48.07919 | 2025-09-01 05:25:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 77fa3b7c-b9f4-38ad-9ba7-a2fa977f0118 | -6.83653 | -52.82559 | 2025-09-01 05:25:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 2f2f5cc8-c1e6-37b3-977e-35c812ee0e83 | -12.86872 | -48.16809 | 2025-09-01 05:25:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| da3da998-54f4-3419-9d2d-3fb0412f70b7 | -6.34179 | -53.42804 | 2025-09-01 05:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3882f6b5-a086-34a0-959b-6457920b85f1 | -12.44449 | -63.92534 | 2025-09-01 05:25:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b5814817-25c2-3adb-a405-9b663b8e169b | -7.39479 | -47.43899 | 2025-09-01 05:25:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e630f657-742c-3314-8ef9-eca9a11a6028 | -6.81757 | -52.81733 | 2025-09-01 05:25:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| c71e067c-82d1-3176-bd07-ebfb571b6eaa | -6.81188 | -52.82224 | 2025-09-01 05:25:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a519971d-b5c9-39e9-9e16-a18b6ebf81d3 | -6.82745 | -52.81855 | 2025-09-01 05:25:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 3ac9057d-81f2-37fd-8728-20933e1354f9 | -6.83806 | -52.8145 | 2025-09-01 05:25:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 8b3c7441-4e29-365d-b11b-6e7282779d3a | -15.69344 | -48.9318 | 2025-09-01 05:25:00 | NOAA-21 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 766363e0-393a-353f-a67b-e73329aa48b9 | -9.9604 | -66.87187 | 2025-09-01 05:25:00 | NOAA-21 | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d98c5d9d-c8e8-3949-8dcc-e559f524162b | -6.81999 | -52.82254 | 2025-09-01 05:25:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 69eb9387-9f39-30e4-a758-dd09789ec2db | -11.51995 | -54.47305 | 2025-09-01 05:25:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 6d26aa9a-36e6-3de4-a8ad-64deb84d4505 | -12.60336 | -48.21561 | 2025-09-01 05:25:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| a249243e-649d-3218-964f-baf10ab42965 | -6.84298 | -52.81526 | 2025-09-01 05:25:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 18fd2604-1d79-3508-950f-e2f72d550ec9 | -6.71662 | -59.78685 | 2025-09-01 05:25:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README84.md)
